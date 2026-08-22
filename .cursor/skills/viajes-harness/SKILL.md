---
name: viajes-harness
description: Gestiona el harness de planificación de viajes en este repositorio. Usar al planificar viajes, editar ficheros de viaje, itinerarios por ciudad, actualizar reservas o SESSION-LOG, generar la web MkDocs (`web/`), o cuando el usuario mencione Viaxes, viajes u organización de itinerarios.
---

# Viajes Harness

Harness en **raíz del repo** (`AGENTS.md`, `SESSION-LOG.md`). Cada viaje en `YYYY-destino/`.

## Inicio de sesión

1. Leer `SESSION-LOG.md`, **`intereses.md`** y `AGENTS.md` (raíz).
2. Leer `reservas-summary.md` del viaje activo (y `reservas-detail.md` si hace falta detalle).
3. Carpetas de viaje: formato `YYYY-destino`.
4. No asumir nada de reservas que no esté escrito ahí.

## Escribir en reservas

**Solo si el usuario confirma explícitamente.** Actualizar **ambos**:
- `reservas-summary.md` — fila cronológica (tipo · fecha · inicio · qué · fin)
- `reservas-detail.md` — localizador, plazas, PDF, precios

## Ficheros por viaje (`YYYY-destino/`)

| Ruta | Contenido |
|------|-----------|
| `ciudades.md` | Lista, orden, días; enlaces a `actividades/` |
| `actividades/[ciudad].md` | Itinerario día a día |
| `transportes.md` | Vuelos, trenes, transfers |
| `alojamiento.md` | Hoteles, apartamentos |
| `presupuesto.md` | Estimaciones y gastos |
| `documentacion.md` | Visados, seguros, documentos |
| `consejos-locales.md` | *(opcional)* Horarios, trucos **solo de ese destino** |
| `conversion.md` | **Obligatorio si moneda ≠ €** — regla de cabeza + tabla ancla → euros |
| `reservas-summary.md` | Histórico cronológico confirmado (sin detalle) |
| `reservas-detail.md` | Verdad absoluta con detalle / PDFs |

Plantilla de ciudad: `.cursor/skills/planificar-ciudad/plantilla.md`  
Plantilla conversión: `.cursor/skills/viajes-harness/conversion.plantilla.md`

**Planificar ciudad:** skill `planificar-ciudad` (universal). Consejos del destino: `YYYY-destino/consejos-locales.md` si existe.

## Web del viaje (`web/`)

- MkDocs Material del viaje activo (`2026-china` por ahora).
- Editar solo en `YYYY-destino/`; sincronizar con `python web/scripts/sync-from-viaje.py` o `python web/scripts/build.py serve|online|offline`.
- No editar copias en `web/docs/` (excepto `index.md`).
- Ver `web/README.md`.

## Ritmo

- Un fichero o sección por iteración.
- No rellenar con suposiciones.
