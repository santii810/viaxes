# Harness de viajes

Este repositorio planifica viajes. El **harness vive en la raíz** y se reutiliza en todos los viajes. Cada viaje tiene su carpeta `YYYY-destino/`.

## Estructura

```
Viaxes/                          # Raíz — harness reutilizable
├── AGENTS.md                    # Normas del harness (este fichero)
├── SESSION-LOG.md               # Log de conversaciones (todos los viajes)
├── intereses.md                 # Preferencias del viajero (contexto, no prioridad)
├── 2026-china/                  # Un viaje = carpeta YYYY-destino
│   ├── reservas.md              # Verdad absoluta de este viaje
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
│   └── conversion.md            # obligatorio si moneda ≠ € — tabla ancla CNY→€ etc.
├── 2027-japon/                  # (futuro — misma estructura)
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

### 2. reservas.md — verdad absoluta (por viaje)

- Ruta: `YYYY-destino/reservas.md` (p. ej. `2026-china/reservas.md`).
- Solo escribir cuando el usuario **confirme explícitamente** (p. ej. "confirma esto en reservas").
- Contenido inmutable una vez confirmado: reservas hechas, fechas fijadas, vuelos comprados, etc.
- Nunca opiniones, alternativas ni "quizá". Si hay duda, no va en reservas.

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
- Cada ciudad sigue esta estructura por día:
  1. **Programa** — horario principal + restricciones + **entrada** (moneda local + € cuando aplique)
  2. **Plan B (misma zona)** — actividades extra en la zona del día (cambiar de plan, aburrimiento, acortar)
  3. **Deck** — fuera del itinerario; esfuerzo + por qué (sin «sustituiría a»)
  4. **Compras y curiosidades** — menú tiendas locales, productos del destino, curiosidades
  5. **Gastronomía** — platos típicos + restaurantes emblemáticos (sin horario)
  6. **Experiencias** — espectáculos (comida → Gastronomía)
- Cada día indica **zona/barrio** y **base noche** recomendada (coherente con `alojamiento.md`).

### 5. Ritmo incremental

- Cambios pequeños y revisables. No reescribir todo el viaje en cada iteración.
- Una categoría o un bloque de reservas por paso, salvo que el usuario pida lo contrario.

## Flujo del agente

1. Leer `SESSION-LOG.md`, **`intereses.md`** y `AGENTS.md` (raíz).
2. Identificar el viaje (carpeta `YYYY-destino/`) en curso.
3. Leer `reservas.md` del viaje antes de proponer cambios que lo afecten.
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
