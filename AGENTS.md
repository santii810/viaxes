# Harness de viajes

Este repositorio planifica viajes. El **harness vive en la raíz** y se reutiliza en todos los viajes. Cada viaje tiene su carpeta `YYYY-destino/`.

## Estructura

```
Viaxes/                          # Raíz — harness reutilizable
├── AGENTS.md                    # Normas del harness (este fichero)
├── SESSION-LOG.md               # Log de conversaciones (todos los viajes)
├── intereses.md                 # Preferencias del viajero (contexto, no prioridad)
├── 2026-china/                  # Un viaje = carpeta YYYY-destino
│   ├── reservas-summary.md      # Histórico cronológico (sin detalle)
│   ├── reservas-detail.md       # Verdad absoluta con detalle / PDFs
│   ├── ciudades.md              # Lista, orden, días totales
│   ├── actividades/             # Un fichero por ciudad/destino
│   │   ├── pekin.md
│   │   ├── xian.md
│   │   └── ...
│   ├── transportes.md
│   ├── alojamiento.md
│   ├── presupuesto.md
│   ├── documentacion.md
│   ├── consejos-locales.md      # (opcional) trucos del destino
│   ├── conversion.md            # obligatorio si moneda ≠ € — tabla ancla CNY→€ etc.
│   └── index.md                 # portada MkDocs (web)
├── 2027-japon/                  # (futuro — misma estructura)
├── web/                         # Sitio MkDocs del viaje activo (ver §6)
│   ├── mkdocs.yml               # docs_dir → ../YYYY-destino
│   └── scripts/
├── tools/                       # Guía PDF, etc.
└── .cursor/
    ├── rules/
    └── skills/
        ├── viajes-harness/
        └── planificar-ciudad/   # plantilla.md + normas itinerario
```

Plantilla de ciudad: `.cursor/skills/planificar-ciudad/plantilla.md`

## Reglas fundamentales

### 1. SESSION-LOG.md — contexto entre sesiones

- Al **iniciar** una sesión: leer `SESSION-LOG.md` e **`intereses.md`** para recuperar contexto.
- Al **cerrar** o tras hitos importantes: añadir una entrada con fecha, viaje afectado y resumen breve.
- No duplicar el contenido de los ficheros del viaje; solo decisiones, pendientes y contexto conversacional.

### 2. Reservas — verdad absoluta (por viaje)

- Rutas: `YYYY-destino/reservas-summary.md` + `reservas-detail.md`.
- **summary** = histórico cronológico (tipo · fecha · hora inicio · qué · hora fin), sin detalle.
- **detail** = localizadores, plazas, PDFs, precios.
- Solo escribir cuando el usuario **confirme explícitamente** (p. ej. "confirma esto en reservas").
- Contenido inmutable una vez confirmado. Nunca opiniones, alternativas ni "quizá". Si hay duda, no va en reservas.
- Al confirmar: actualizar **ambos** ficheros.

### 3. Ficheros por tipo (dentro de cada viaje)

- Investigación, opciones, borradores y notas van aquí, **no** en reservas.
- Se pueden actualizar con libertad; marcar estado cuando aplique: `borrador`, `opción`, `descartado`.

### 4. Itinerario por ciudad — carpeta `actividades/`

- Ruta: `YYYY-destino/actividades/[ciudad].md`.
- **Un fichero por ciudad/destino.** No hay `actividades.md` índice.
- El listado y enlaces viven en `ciudades.md`.
- **Planificar una ciudad** → skill **`planificar-ciudad`** (universal, todos los viajes; plantilla incluida en la skill).
- Restricciones **solo si existen** (celda vacía si no hay). Ver skill.
- Consejos de un destino concreto → `YYYY-destino/consejos-locales.md` si existe.
- Destino sin euro → `YYYY-destino/conversion.md` (tabla ancla; plantilla en skill `viajes-harness`).
- Cada ciudad: **30 segundos + mapa + dónde dormir**. Luego, **por cada día:** Programa → Plan B → fotos/descripción de los sitios de *ese* día. Modelo: `actividades/hong-kong.md`. Luego Deck, Gastronomía, Compras, Experiencias.
- Cada día: **Programa** (horario + restricciones + **entrada** moneda local + €) y **Plan B (misma zona)**. **Zona** y **base noche** coherentes con `alojamiento.md`.

### 5. Ritmo incremental

- Cambios pequeños y revisables. No reescribir todo el viaje en cada iteración.
- Una categoría o un bloque de reservas por paso, salvo que el usuario pida lo contrario.

### 6. Web del viaje (`web/`)

- Sitio **MkDocs Material** del viaje activo (ahora `2026-china`): navegable online y exportable offline.
- MkDocs lee **directamente** `YYYY-destino/` (`docs_dir: ../2026-china` en `web/mkdocs.yml`). Editar ahí; `serve` recarga en caliente.
- Antes de servir o publicar: `python web/scripts/build.py serve|online|offline`.
- Detalle de uso: `web/README.md`. Diseño: `docs/superpowers/specs/2026-08-18-mkdocs-web-viaje-design.md`.
- El PDF (`tools/generar-guia.py`) sigue siendo la versión imprimible; la web es la capa interactiva.
- Privacidad: repo privado + URL no anunciada (sin login). Incluye reservas/PDFs.

## Flujo del agente

1. Leer `SESSION-LOG.md`, **`intereses.md`** y `AGENTS.md` (raíz).
2. Identificar el viaje (carpeta `YYYY-destino/`) en curso.
3. Leer `reservas-summary.md` (y `reservas-detail.md` si hace falta) antes de proponer cambios que lo afecten.
4. Trabajar en el fichero correspondiente — si es una ciudad, invocar skill `planificar-ciudad`.
5. Actualizar `SESSION-LOG.md` al terminar.

## Agentes / Skills

| Rol | Skill | Cuándo |
|-----|-------|--------|
| Harness general | `viajes-harness` | Estructura del repo, reservas, log, ficheros por tipo |
| Planificar ciudad | `planificar-ciudad` | Crear o editar `actividades/[ciudad].md` en **cualquier** viaje |

## Skills (referencia)

- `viajes-harness` — workflow completo de lectura/escritura del harness.
- `planificar-ciudad` — itinerario día a día (universal; ver `consejos-locales.md` del viaje para reglas del destino).
