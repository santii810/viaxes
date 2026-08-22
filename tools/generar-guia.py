#!/usr/bin/env python3
"""
Genera un PDF imprimible a partir de los ficheros markdown de un viaje Viaxes.

Uso:
    python tools/generar-guia.py 2026-china
    python tools/generar-guia.py 2026-china -o guia-china.pdf --solo-confirmado
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

# La portada se renderiza como PDF independiente de 1 página y se fusiona al final.
PAGINAS_PORTADA = 1

# Raíz del repo (tools/ → Viaxes/)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Orden de ficheros según el harness (AGENTS.md / viajes-harness)
FICHEROS_ANTES_ACTIVIDADES = [
    ("reservas-summary.md", "Reservas (resumen)"),
    ("reservas-detail.md", "Reservas (detalle)"),
    ("ciudades.md", "Ciudades"),
]
FICHEROS_DESPUES_ACTIVIDADES = [
    ("consejos-locales.md", "Consejos locales"),
    ("conversion.md", "Conversión"),
    ("transportes.md", "Transportes"),
    ("alojamiento.md", "Alojamiento"),
    ("presupuesto.md", "Presupuesto"),
    ("documentacion.md", "Documentación"),
]

def extraer_titulo_viaje(carpeta: Path) -> str:
    """Título del viaje a partir de la carpeta YYYY-destino (p. ej. China 2026)."""
    m = re.match(r"(\d{4})-(.+)", carpeta.name)
    if m:
        destino = m.group(2).replace("-", " ").title()
        return f"{destino} {m.group(1)}"
    return carpeta.name.replace("-", " ").title()


def extraer_ventana_fechas(ciudades_md: str) -> str | None:
    desde = re.search(r"\*\*Desde:\*\*\s*(.+)", ciudades_md)
    hasta = re.search(r"\*\*Hasta:\*\*\s*(.+)", ciudades_md)
    if desde and hasta:
        return f"{desde.group(1).strip()} — {hasta.group(1).strip()}"
    return None


SLUG_ALIASES: dict[str, str] = {
    "pekin": "pekin",
    "pekín": "pekin",
    "beijing": "pekin",
    "xian": "xian",
    "xi'an": "xian",
    "chengdu": "chengdu",
    "chongqing": "chongqing",
    "zhangjiajie": "zhangjiajie",
    "furong": "furong",
    "fenghuang": "fenghuang",
    "guilin": "guilin",
    "yangshuo": "guilin",
    "shanghai": "shanghai",
    "shanghái": "shanghai",
    "shangai": "shanghai",
}


def _normalizar_slug(nombre: str) -> str | None:
    clave = nombre.strip().lower()
    clave = re.sub(r"\s*[/+]\s*.*", "", clave)  # "Guilin/Yangshuo" o "Guilin + Yangshuo"
    clave = clave.replace("'", "")
    return SLUG_ALIASES.get(clave)


ESTADOS_VALIDOS = frozenset({"confirmado", "opción", "opcion", "borrador", "descartado"})


def _estado_desde_tabla(ciudades_md: str) -> dict[str, str | None]:
    """Lee estados solo de la tabla 'Lista en baraja'."""
    estados: dict[str, str | None] = {}
    bloque = re.search(
        r"## Lista en baraja.*?\n(.*?)(?=\n## |\Z)",
        ciudades_md,
        re.S,
    )
    if not bloque:
        return estados

    for m in re.finditer(
        r"^\|\s*([^|]+?)\s*\|\s*`?([^`|]+?)`?\s*\|",
        bloque.group(1),
        re.M,
    ):
        nombre = m.group(1).strip()
        if nombre.lower() in ("ciudad", "---"):
            continue
        estado_raw = m.group(2).strip().lower()
        if estado_raw not in ESTADOS_VALIDOS:
            continue
        slug = _normalizar_slug(nombre)
        if slug:
            estados[slug] = estado_raw
    return estados


def extraer_ciudades_orden(ciudades_md: str, actividades_dir: Path) -> list[tuple[str, Path, str | None]]:
    """
    Devuelve [(nombre, path, estado)] en orden del itinerario.
    estado: 'confirmado', 'opción', etc. o None.
    """
    if not actividades_dir.exists():
        return []

    estados = _estado_desde_tabla(ciudades_md)
    disponibles = {p.stem: p for p in actividades_dir.glob("*.md")}
    ciudades: list[tuple[str, Path, str | None]] = []
    vistos: set[str] = set()

    # Orden explícito: "Pekín → Xi'an → ..."
    orden_bloque = re.search(
        r"## Orden propuesto.*?\n```\n(.+?)\n```",
        ciudades_md,
        re.S,
    )
    if orden_bloque:
        nombres = re.split(r"\s*→\s*", orden_bloque.group(1).strip())
        for nombre in nombres:
            slug = _normalizar_slug(nombre)
            if not slug or slug in vistos:
                continue
            path = disponibles.get(slug)
            if path:
                ciudades.append((nombre.strip(), path, estados.get(slug)))
                vistos.add(slug)

    # Enlaces directos en la tabla (por si el orden propuesto no lista todas)
    for m in re.finditer(
        r"\[`actividades/([^`]+)`\]",
        ciudades_md,
    ):
        slug = m.group(1).strip().removesuffix(".md")
        if slug in vistos:
            continue
        path = disponibles.get(slug)
        if path:
            nombre = slug.replace("-", " ").title()
            ciudades.append((nombre, path, estados.get(slug)))
            vistos.add(slug)

    # Resto de ficheros en actividades/ (alfabético)
    for slug, path in sorted(disponibles.items()):
        if slug not in vistos:
            ciudades.append((slug.replace("-", " ").title(), path, estados.get(slug)))
            vistos.add(slug)

    return ciudades


def leer_fichero(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def md_a_html(fragmento_md: str) -> str:
    return markdown.markdown(
        fragmento_md,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
        output_format="html5",
    )


def _slug_id(texto: str, prefijo: str = "") -> str:
    slug = texto.lower()
    slug = re.sub(r"[^a-z0-9áéíóúñü]+", "-", slug, flags=re.I)
    slug = slug.strip("-")
    base = f"{prefijo}-{slug}" if prefijo else slug
    return base[:80]


def _sec_id(texto: str) -> str:
    return _slug_id(texto, "sec")


def _day_id(seccion: str, dia: str) -> str:
    return _slug_id(f"{seccion}-{dia}", "day")


@dataclass
class ParteGuia:
    titulo: str
    html: str
    categoria: str = "raiz"  # "raiz" | "actividad"


@dataclass
class EntradaIndice:
    id: str
    titulo: str
    nivel: int  # 1 = fichero raíz, 2 = ciudad, 3 = día
    marcador: str


def _marcador_pdf(entrada_id: str) -> str:
    return f"§{entrada_id}§"


def _act_id(texto: str) -> str:
    return _slug_id(texto, "act")


def extraer_entradas_indice(partes: list[ParteGuia]) -> list[EntradaIndice]:
    """Índice: ficheros raíz (nivel 1), ciudades (nivel 2), días (nivel 3)."""
    entradas: list[EntradaIndice] = []
    dias_vistos: set[str] = set()

    for parte in partes:
        if parte.categoria != "actividad":
            sec_id = _sec_id(parte.titulo)
            entradas.append(EntradaIndice(sec_id, parte.titulo, 1, _marcador_pdf(sec_id)))
            continue

        act_id = _act_id(parte.titulo)
        entradas.append(EntradaIndice(act_id, parte.titulo, 2, _marcador_pdf(act_id)))

        for m in re.finditer(
            r'<h2 class="dia" id="([^"]+)">(?:<span[^>]*>[^<]*</span>)?([^<]*)</h2>',
            parte.html,
        ):
            dia_id = m.group(1)
            dia_titulo = m.group(2).strip()
            if dia_id in dias_vistos:
                dia_id = f"{dia_id}-{len(entradas)}"
            dias_vistos.add(dia_id)
            entradas.append(EntradaIndice(dia_id, dia_titulo, 3, _marcador_pdf(dia_id)))

    return entradas


def medir_paginas_pdf(pdf_path: Path, entradas: list[EntradaIndice]) -> dict[str, int]:
    """Localiza en qué página aparece cada entrada (búsqueda secuencial en el PDF)."""
    reader = PdfReader(str(pdf_path))
    paginas: dict[str, int] = {}
    pagina_min = 0

    for idx, entrada in enumerate(entradas):
        encontrada = False
        for i in range(pagina_min, len(reader.pages)):
            texto = reader.pages[i].extract_text() or ""
            texto_norm = re.sub(r"\s+", " ", texto)
            # Los marcadores §…§ pueden degradarse en la extracción de texto del PDF;
            # el id (p. ej. toc-ciudades) se conserva de forma fiable.
            if entrada.id in texto_norm:
                paginas[entrada.id] = i + 1
                pagina_min = i
                encontrada = True
                break
        if not encontrada:
            paginas[entrada.id] = paginas.get(entradas[idx - 1].id, 1) if idx > 0 else 1

    return paginas


def paginas_del_indice(paginas: dict[str, int], entradas: list[EntradaIndice]) -> int:
    """Páginas que ocupa el índice (antes de la primera sección de contenido)."""
    if not entradas:
        return 0
    primera = paginas.get(entradas[0].id, 2)
    return max(1, primera - 2)


def construir_indice_html(
    entradas: list[EntradaIndice],
    paginas: dict[str, int],
) -> str:
    """Genera el HTML del índice con números de página absolutos."""
    filas: list[str] = []
    for entrada in entradas:
        pag = paginas.get(entrada.id, 0)
        nivel = f"indice-nivel-{entrada.nivel}"
        filas.append(
            f'<div class="indice-item {nivel}">'
            f'<span class="indice-texto">{entrada.titulo}</span>'
            f'<span class="indice-puntos" aria-hidden="true"></span>'
            f'<span class="indice-pagina">{pag}</span>'
            f"</div>"
        )

    return (
        '<div class="indice">'
        '<h1 class="indice-titulo">Índice</h1>'
        '<nav class="indice-lista">'
        + "".join(filas)
        + "</nav></div>"
    )


def postprocesar_html(html: str, titulo_seccion: str = "") -> str:
    """Añade clases e ids para saltos de página, estilos e índice."""
    # Días del itinerario
    contador_dia = 0

    def _reemplazar_dia(m: re.Match[str]) -> str:
        nonlocal contador_dia
        contador_dia += 1
        titulo = m.group(1).strip()
        dia_id = _day_id(titulo_seccion, titulo)
        marcador = _marcador_pdf(dia_id)
        return (
            f'<h2 class="dia" id="{dia_id}">'
            f'<span class="pdf-marcador">{marcador}</span>{titulo}</h2>'
        )

    html = re.sub(
        r"<h2>(Día\s+\d+[^<]*)</h2>",
        _reemplazar_dia,
        html,
        flags=re.I,
    )
    # Secciones estándar del harness
    for seccion in ("Programa", "Plan B", "Deck", "Gastronomía", "Compras y curiosidades", "Experiencias"):
        html = re.sub(
            rf"<h3>({re.escape(seccion)}[^<]*)</h3>",
            rf'<h3 class="seccion">\1</h3>',
            html,
            flags=re.I,
        )
    return html


def _html_bloque_raiz(parte: ParteGuia) -> str:
    sec_id = _sec_id(parte.titulo)
    marcador = _marcador_pdf(sec_id)
    return (
        f'<section class="bloque" id="{sec_id}">'
        f'<h1 class="bloque-titulo">'
        f'<span class="pdf-marcador">{marcador}</span>{parte.titulo}</h1>'
        f"{parte.html}</section>"
    )


def _html_actividad(parte: ParteGuia) -> str:
    act_id = _act_id(parte.titulo)
    marcador = _marcador_pdf(act_id)
    return (
        f'<section class="subbloque actividad" id="{act_id}">'
        f'<h2 class="actividad-titulo">'
        f'<span class="pdf-marcador">{marcador}</span>{parte.titulo}</h2>'
        f"{parte.html}</section>"
    )


def _construir_cuerpo(partes: list[ParteGuia]) -> str:
    cuerpo: list[str] = []
    i = 0
    while i < len(partes):
        parte = partes[i]
        if parte.categoria == "actividad":
            i += 1
            continue
        if parte.titulo == "Ciudades":
            actividades = []
            j = i + 1
            while j < len(partes) and partes[j].categoria == "actividad":
                actividades.append(partes[j])
                j += 1
            sec_id = _sec_id(parte.titulo)
            marcador = _marcador_pdf(sec_id)
            subs = "".join(_html_actividad(a) for a in actividades)
            cuerpo.append(
                f'<section class="bloque bloque-ciudades" id="{sec_id}">'
                f'<h1 class="bloque-titulo">'
                f'<span class="pdf-marcador">{marcador}</span>{parte.titulo}</h1>'
                f"{parte.html}"
                f'<div class="actividades">{subs}</div>'
                f"</section>"
            )
            i = j
        else:
            cuerpo.append(_html_bloque_raiz(parte))
            i += 1
    return "".join(cuerpo)


def _estilos_documento(compacto: bool) -> str:
    """CSS compartido del documento (sin portada)."""
    return f"""
    @page {{
      size: A4;
      margin: 18mm 16mm 22mm 16mm;
      @bottom-center {{
        content: counter(page);
        font-size: 9pt;
        color: #666;
      }}
    }}

    * {{ box-sizing: border-box; }}

    body {{
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.45;
      color: #1a1a1a;
      margin: 0;
      padding: 0;
    }}

    /* Índice */
    .indice {{
      page-break-after: always;
      break-after: page;
      padding-top: 4mm;
    }}
    .indice-titulo {{
      font-size: 20pt;
      color: #1a3a5c;
      border-bottom: 2px solid #1a3a5c;
      padding-bottom: 6pt;
      margin: 0 0 14pt;
    }}
    .indice-lista {{
      display: flex;
      flex-direction: column;
      gap: 3pt;
    }}
    .indice-item {{
      display: flex;
      align-items: baseline;
      gap: 4pt;
      line-height: 1.35;
    }}
    .indice-nivel-1 {{
      font-size: 11pt;
      font-weight: 600;
      margin-top: 5pt;
    }}
    .indice-nivel-1:first-child {{
      margin-top: 0;
    }}
    .indice-nivel-2 {{
      font-size: 9.5pt;
      font-weight: 400;
      color: #444;
      padding-left: 14pt;
    }}
    .indice-nivel-3 {{
      font-size: 9pt;
      font-weight: 400;
      color: #555;
      padding-left: 28pt;
    }}
    .indice-texto {{
      flex-shrink: 0;
      max-width: 78%;
    }}
    .indice-puntos {{
      flex: 1;
      border-bottom: 1px dotted #aaa;
      min-width: 12pt;
      margin-bottom: 3pt;
    }}
    .indice-pagina {{
      flex-shrink: 0;
      font-variant-numeric: tabular-nums;
      min-width: 2em;
      text-align: right;
    }}

    h1.bloque-titulo {{
      font-size: 18pt;
      color: #1a3a5c;
      border-bottom: 2px solid #1a3a5c;
      padding-bottom: 4pt;
      margin: 0 0 10pt;
      page-break-after: avoid;
    }}

    section.bloque {{
      page-break-before: always;
    }}
    section.bloque:first-of-type {{
      page-break-before: auto;
    }}

    .bloque-ciudades .actividades {{
      margin-top: 10pt;
    }}
    .subbloque.actividad {{
      page-break-before: always;
      margin-top: 8pt;
    }}
    h2.actividad-titulo {{
      font-size: 15pt;
      color: #1a3a5c;
      border-bottom: 1px solid #1a3a5c;
      padding-bottom: 4pt;
      margin: 0 0 10pt;
      page-break-after: avoid;
    }}

    h2 {{
      font-size: 13pt;
      color: #2c5282;
      margin: 14pt 0 8pt;
      page-break-after: avoid;
    }}
    h2.dia {{
      page-break-before: always;
      border-left: 4px solid #2c5282;
      padding-left: 8pt;
    }}
    section.bloque h2.dia:first-of-type,
    .subbloque.actividad h2.dia:first-of-type {{
      page-break-before: auto;
    }}

    h3 {{
      font-size: 11pt;
      color: #333;
      margin: 10pt 0 6pt;
      page-break-after: avoid;
    }}
    h3.seccion {{
      text-transform: uppercase;
      font-size: 9pt;
      letter-spacing: 0.06em;
      color: #666;
      border-bottom: 1px solid #ddd;
      padding-bottom: 2pt;
    }}

    p {{ margin: 0 0 8pt; }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 9pt;
      margin: 6pt 0 12pt;
      page-break-inside: auto;
    }}
    thead {{ display: table-header-group; }}
    tr {{ page-break-inside: avoid; page-break-after: auto; }}
    th, td {{
      border: 1px solid #ccc;
      padding: 4pt 6pt;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background: #eef2f7;
      font-weight: 600;
    }}
    tr:nth-child(even) td {{
      background: #fafafa;
    }}

    blockquote {{
      margin: 8pt 0;
      padding: 6pt 10pt;
      border-left: 3px solid #ccc;
      color: #555;
      font-size: 9.5pt;
    }}

    code, pre {{
      font-family: Consolas, "Courier New", monospace;
      font-size: 8.5pt;
    }}
    pre {{
      background: #f4f4f4;
      padding: 8pt;
      overflow-x: auto;
      white-space: pre-wrap;
    }}

    ul, ol {{
      margin: 4pt 0 10pt;
      padding-left: 18pt;
    }}
    li {{ margin-bottom: 3pt; }}

    hr {{
      border: none;
      border-top: 1px solid #ddd;
      margin: 12pt 0;
    }}

    strong {{ font-weight: 600; }}

    .pdf-marcador {{
      font-size: 1pt;
      color: transparent;
      letter-spacing: 0;
    }}

    {"section.deck, section.compras, section.gastronomia-extra { display: none; }" if compacto else ""}
    """


def construir_html_portada(titulo: str, fechas: str | None) -> str:
    """HTML mínimo para la portada — se renderiza como PDF de 1 página aislado."""
    fecha_gen = datetime.now().strftime("%d/%m/%Y")
    subtitulo = fechas or "Guía de viaje"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>{titulo}</title>
  <style>
    @page {{
      size: A4;
      margin: 0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html, body {{
      width: 210mm;
      height: 297mm;
      overflow: hidden;
      background: #fff;
    }}
    body {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      color: #1a1a1a;
      padding: 24mm 20mm;
    }}
    h1 {{
      font-size: 28pt;
      font-weight: 700;
      margin-bottom: 12mm;
      letter-spacing: -0.02em;
    }}
    .fechas {{
      font-size: 14pt;
      color: #444;
      margin-bottom: 8mm;
    }}
    .meta {{
      font-size: 9pt;
      color: #888;
      margin-top: 20mm;
    }}
  </style>
</head>
<body>
  <h1>{titulo}</h1>
  <div class="fechas">{subtitulo}</div>
  <div class="meta">Generado {fecha_gen} · Viaxes</div>
</body>
</html>"""


def construir_html_documento(
    titulo: str,
    partes: list[ParteGuia],
    compacto: bool,
    indice_html: str | None = None,
) -> str:
    """HTML del documento (índice + contenido), sin portada."""
    cuerpo = _construir_cuerpo(partes)
    bloque_indice = indice_html or ""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>{titulo}</title>
  <style>{_estilos_documento(compacto)}</style>
</head>
<body>
  {bloque_indice}
  {cuerpo}
</body>
</html>"""


def construir_html(
    titulo: str,
    fechas: str | None,
    partes: list[ParteGuia],
    compacto: bool,
    indice_html: str | None = None,
) -> str:
    """Compatibilidad: documento completo (portada embebida — evitar en producción)."""
    portada = construir_html_portada(titulo, fechas)
    # Extraer solo el body de la portada para embeber (uso legacy)
    m = re.search(r"<body>(.*)</body>", portada, re.S)
    portada_body = m.group(1).strip() if m else ""
    doc = construir_html_documento(titulo, partes, compacto, indice_html)
    return doc.replace("<body>", f"<body>\n  <div class=\"portada\">{portada_body}</div>\n  ", 1)


def filtrar_md_compacto(texto: str) -> str:
    """Mantiene Programa y cabeceras de día; omite Deck, Compras, Gastronomía completa."""
    lineas = texto.splitlines()
    resultado: list[str] = []
    omitir = False
    secciones_omitir = (
        "## Deck",
        "## Compras y curiosidades",
        "## Gastronomía",
        "## Experiencias",
        "### Plan B",
    )

    for ln in lineas:
        if any(ln.startswith(s) for s in secciones_omitir):
            omitir = True
            continue
        if ln.startswith("## Día") or ln.startswith("## Pendiente"):
            omitir = False
        if ln.startswith("## ") and not omitir:
            omitir = False
        if not omitir:
            resultado.append(ln)

    return "\n".join(resultado)


def _añadir_fichero(
    partes: list[ParteGuia],
    path: Path,
    titulo_seccion: str,
    compacto: bool,
    categoria: str = "raiz",
) -> None:
    contenido = leer_fichero(path)
    if compacto:
        contenido = filtrar_md_compacto(contenido)
    html = postprocesar_html(md_a_html(contenido), titulo_seccion)
    if categoria == "actividad":
        # El título va en h2.actividad-titulo; quitar el h1 duplicado del .md
        html = re.sub(r"<h1>[^<]+</h1>\s*", "", html, count=1)
    partes.append(ParteGuia(titulo_seccion, html, categoria))


def recopilar_contenido(
    viaje_dir: Path,
    solo_confirmado: bool,
    sin_presupuesto: bool,
    compacto: bool,
) -> tuple[str, str | None, list[ParteGuia]]:
    ciudades_path = viaje_dir / "ciudades.md"
    if not ciudades_path.exists():
        raise FileNotFoundError(f"No se encuentra {ciudades_path}")

    ciudades_md = leer_fichero(ciudades_path)
    titulo = extraer_titulo_viaje(viaje_dir)
    fechas = extraer_ventana_fechas(ciudades_md)

    partes: list[ParteGuia] = []

    # 1. reservas-summary/detail, ciudades.md
    for nombre_fichero, titulo_seccion in FICHEROS_ANTES_ACTIVIDADES:
        path = viaje_dir / nombre_fichero
        if path.exists():
            _añadir_fichero(partes, path, titulo_seccion, compacto, "raiz")

    # 2. actividades/*.md — subapartado de Ciudades
    actividades_dir = viaje_dir / "actividades"
    for nombre_ciudad, path, estado in extraer_ciudades_orden(ciudades_md, actividades_dir):
        if solo_confirmado and estado != "confirmado":
            continue
        _añadir_fichero(partes, path, nombre_ciudad, compacto, "actividad")

    # 3. transportes, alojamiento, presupuesto, documentacion
    for nombre_fichero, titulo_seccion in FICHEROS_DESPUES_ACTIVIDADES:
        if sin_presupuesto and nombre_fichero == "presupuesto.md":
            continue
        path = viaje_dir / nombre_fichero
        if path.exists():
            _añadir_fichero(partes, path, titulo_seccion, compacto, "raiz")

    if not partes:
        raise ValueError("No hay contenido para generar la guía.")

    return titulo, fechas, partes


def _renderizar_pdf(html: str, salida: Path, page: object) -> None:
    salida.parent.mkdir(parents=True, exist_ok=True)
    page.set_content(html, wait_until="networkidle")
    page.emulate_media(media="print")
    page.pdf(
        path=str(salida),
        format="A4",
        print_background=True,
        prefer_css_page_size=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
    )


def _desplazar_paginas(paginas: dict[str, int], offset: int) -> dict[str, int]:
    return {k: v + offset for k, v in paginas.items()}


def _fusionar_pdfs(fuentes: list[Path], destino: Path) -> None:
    writer = PdfWriter()
    for fuente in fuentes:
        reader = PdfReader(str(fuente))
        for pagina in reader.pages:
            writer.add_page(pagina)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "wb") as f:
        writer.write(f)


def generar_pdf_con_indice(
    titulo: str,
    fechas: str | None,
    partes: list[ParteGuia],
    compacto: bool,
    salida: Path,
) -> int:
    """
    Genera el PDF: portada aislada (1 pág.) + cuerpo con índice en dos pasadas.
    """
    entradas = extraer_entradas_indice(partes)
    paginas_cero = {e.id: 0 for e in entradas}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        html_portada = construir_html_portada(titulo, fechas)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_cover:
            cover_path = Path(tmp_cover.name)
        _renderizar_pdf(html_portada, cover_path, page)

        # Pasada 1: cuerpo con índice provisional → medir marcadores
        indice_prov = construir_indice_html(entradas, paginas_cero)
        html_prov = construir_html_documento(titulo, partes, compacto, indice_html=indice_prov)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            body_path = Path(tmp.name)
        try:
            _renderizar_pdf(html_prov, body_path, page)
            paginas_cuerpo = medir_paginas_pdf(body_path, entradas)
            paginas_finales = _desplazar_paginas(paginas_cuerpo, PAGINAS_PORTADA)
            paginas_indice = paginas_del_indice(paginas_finales, entradas)
        finally:
            body_path.unlink(missing_ok=True)

        # Pasada 2: cuerpo definitivo + fusionar con portada
        indice_final = construir_indice_html(entradas, paginas_finales)
        html_final = construir_html_documento(titulo, partes, compacto, indice_html=indice_final)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp2:
            body_final_path = Path(tmp2.name)
        try:
            _renderizar_pdf(html_final, body_final_path, page)
            _fusionar_pdfs([cover_path, body_final_path], salida)
        finally:
            body_final_path.unlink(missing_ok=True)
            cover_path.unlink(missing_ok=True)

        browser.close()

    return paginas_indice


def generar_pdf(html: str, salida: Path) -> None:
    """Renderizado simple sin índice (uso interno / compatibilidad)."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        _renderizar_pdf(html, salida, page)
        browser.close()


def resolver_viaje(arg: str) -> Path:
    candidato = Path(arg)
    if candidato.is_absolute():
        viaje = candidato
    else:
        viaje = REPO_ROOT / candidato
    if not viaje.is_dir():
        raise FileNotFoundError(f"Carpeta de viaje no encontrada: {viaje}")
    return viaje.resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Genera un PDF imprimible de un viaje Viaxes.",
    )
    parser.add_argument(
        "viaje",
        help="Carpeta del viaje (p. ej. 2026-china)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Ruta del PDF de salida (por defecto: guia-[nombre].pdf en la raíz del repo)",
    )
    parser.add_argument(
        "--solo-confirmado",
        action="store_true",
        help="Solo incluir ciudades con estado confirmado en ciudades.md",
    )
    parser.add_argument(
        "--compacto",
        action="store_true",
        help="Solo Programa por día (sin Plan B, Deck, Compras, Gastronomía)",
    )
    parser.add_argument(
        "--sin-presupuesto",
        action="store_true",
        help="No incluir presupuesto.md",
    )
    args = parser.parse_args(argv)

    try:
        viaje_dir = resolver_viaje(args.viaje)
        titulo, fechas, partes = recopilar_contenido(
            viaje_dir,
            solo_confirmado=args.solo_confirmado,
            sin_presupuesto=args.sin_presupuesto,
            compacto=args.compacto,
        )

        if args.output:
            salida = Path(args.output)
            if not salida.is_absolute():
                salida = REPO_ROOT / salida
        else:
            salida = REPO_ROOT / f"guia-{viaje_dir.name}.pdf"

        paginas_indice = generar_pdf_con_indice(
            titulo, fechas, partes, compacto=args.compacto, salida=salida,
        )

        print(f"PDF generado: {salida}")
        print(f"  Secciones: {len(partes)}")
        print(f"  Índice: {paginas_indice} página(s)")
        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error al generar PDF: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
