# Viaxes — harness de planificación de viajes

Este repo planifica viajes. Reglas completas en `AGENTS.md` (raíz) — **léelo al empezar cualquier tarea aquí**, junto con `SESSION-LOG.md` e `intereses.md`.

## Arranque de sesión (obligatorio)

1. Leer `AGENTS.md`, `SESSION-LOG.md` (últimas entradas) e `intereses.md`.
2. Viaje activo: `2026-china/`. Plan vigente: `2026-china/plan-D.md` (ver `ciudades.md` para el estado y "Pendiente de decidir").
3. No asumir nada de reservas que no esté en `2026-china/reservas-summary.md` / `reservas-detail.md`.

## Reglas clave (resumen — detalle en AGENTS.md y skill `viajes-harness`)

- **Reservas = verdad absoluta.** Solo se escriben en `reservas-summary.md` + `reservas-detail.md` (ambos) con **confirmación explícita** del usuario. Inmutables, sin opiniones.
- **Itinerario por ciudad:** `2026-china/actividades/[ciudad].md`, vía skill `planificar-ciudad`. Formato: 30s + mapa + dónde dormir arriba; luego por cada día Programa → Plan B → fotos/descripción de los sitios de ese día. Modelo: `actividades/hong-kong.md`.
- **Ritmo incremental:** un fichero o sección por iteración, sin reescribir todo el viaje.
- **Web:** `python iniciar_china.py` levanta MkDocs Material sirviendo `2026-china/` en `http://localhost:8000`.
- **PDF imprimible:** `python tools/generar-guia.py 2026-china`.
- **Cierre de sesión:** añadir entrada en `SESSION-LOG.md` (fecha, viaje, resumen, pendientes, confirmado en reservas).

## Skills disponibles (`.cursor/skills/`, mismo contenido reutilizable aquí)

- `viajes-harness` — workflow de lectura/escritura del harness.
- `planificar-ciudad` — itinerario día a día (universal).
- `ver-alojamiento` — leer itinerarios → proponer barrios → estimar precio.
