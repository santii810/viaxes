# Diseño — Web MkDocs del viaje (2026-china)

Fecha: 2026-08-18  
Estado: aprobado e implementado

## Objetivo

Sitio estático navegable del viaje **2026-china**, usable:

1. **Online** — host estático, repo privado, URL no anunciada (sin login).
2. **Offline** — ZIP/`site-offline/` con plugin Material `offline` (móvil en destino).

El PDF (`tools/generar-guia.py`) sigue siendo la versión imprimible.

## Decisiones

| Tema | Decisión |
|------|----------|
| Stack | MkDocs + Material for MkDocs |
| Alcance | Solo `2026-china/` |
| Fuente de verdad | Markdown en `2026-china/` |
| `docs_dir` | `../2026-china` en `web/mkdocs.yml` (live reload en `serve`) |
| Privacidad | Repo privado + enlace oscuro; `noindex`; PDFs incluidos online y offline |
| Instant loading | Desactivado (compatibilidad offline) |

## Estructura

- `web/mkdocs.yml` — config
- `web/requirements.txt` — deps
- `web/scripts/build.py` — serve / build online / offline
- `2026-china/index.md` — portada web (MkDocs)
- `web/overrides/` — meta robots

## Fuera de alcance

Harness (`AGENTS`, skills, `SESSION-LOG`, `intereses`), otros viajes, autenticación real.
