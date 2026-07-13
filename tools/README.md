# Herramientas Viaxes

## Generar guía PDF

Convierte los markdown de un viaje en un PDF listo para imprimir (A4).

### Requisitos (una vez)

```bash
pip install -r tools/requirements.txt
python -m playwright install chromium
```

### Uso

```bash
# Guía completa del viaje China 2026
python tools/generar-guia.py 2026-china

# Solo ciudades confirmadas (ahora solo Pekín)
python tools/generar-guia.py 2026-china --solo-confirmado

# Versión compacta: solo Programa de cada día
python tools/generar-guia.py 2026-china --compacto

# Ruta de salida personalizada (relativa a la raíz del repo)
python tools/generar-guia.py 2026-china -o mi-guia.pdf
```

### Contenido incluido (orden del harness)

1. Portada (título del viaje + fechas de `ciudades.md`)
2. **Índice** con números de página
3. `reservas.md`
4. `ciudades.md`
5. Cada ciudad de `actividades/` — **subapartado de Ciudades** (indentada en el índice)
6. `consejos-locales.md` (si existe)
7. `conversion.md` (si existe)
8. `transportes.md`
9. `alojamiento.md`
10. `presupuesto.md` (salvo `--sin-presupuesto`)
11. `documentacion.md`

Todos los ficheros se incluyen aunque estén vacíos o en borrador.

### Opciones

| Opción | Descripción |
|--------|-------------|
| `--solo-confirmado` | Solo ciudades con estado `confirmado` en la tabla de `ciudades.md` |
| `--compacto` | Omite Plan B, Deck, Compras, Gastronomía y Experiencias |
| `--sin-presupuesto` | No incluye presupuesto |
| `-o`, `--output` | Ruta del PDF de salida |

El PDF por defecto se guarda en la **raíz del repo**: `guia-YYYY-destino.pdf` (p. ej. `guia-2026-china.pdf`).

### Índice

El PDF incluye un **índice con números de página** (secciones del viaje + cada día del itinerario). Se genera en dos pasadas para que las páginas sean exactas.

Para comprobar el índice de un PDF ya generado:

```bash
python tools/verificar-indice.py guia-2026-china.pdf
```
