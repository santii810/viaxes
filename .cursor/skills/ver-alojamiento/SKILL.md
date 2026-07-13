---
name: ver-alojamiento
description: Recomienda zonas para dormir por ciudad y completa `YYYY-destino/alojamiento.md` con barrios, por qué (logística/ambiente) y precio estimado (moneda local + €).
---

# Ver alojamiento

Skill universal del harness Viaxes para **recomendar barrios** y completar `YYYY-destino/alojamiento.md` en cualquier viaje (`2026-china/`, `2027-japon/`, etc.).

No escribe en `reservas.md` (verdad absoluta) salvo confirmación explícita del usuario.

**Plantilla:** [plantilla.md](plantilla.md) — usar como estructura base de `YYYY-destino/alojamiento.md` si el fichero está vacío o desordenado.

## Antes de escribir (obligatorio)

1. Leer `SESSION-LOG.md`, **`intereses.md`** y `AGENTS.md` (raíz).
2. Identificar el viaje activo (`YYYY-destino/`).
3. Leer `YYYY-destino/reservas.md` antes de sugerir nada que dependa de fechas confirmadas (vuelos, estaciones, etc.).
4. Leer `YYYY-destino/ciudades.md` (orden, días, estado confirmado/opción).
5. Leer los ficheros `YYYY-destino/actividades/[ciudad].md` de las ciudades implicadas para capturar:
   - **Zona** y **Base noche** recomendada en cada día
   - Dónde terminan las noches (cenas/paseos)
   - Si hay días “de salida” (aeropuerto/estación)
6. Leer `YYYY-destino/conversion.md` si existe (obligatorio si moneda ≠ €).
7. Leer `YYYY-destino/consejos-locales.md` si existe (reglas locales útiles: transporte, apps, zonas seguras, etc.).
8. Leer el `YYYY-destino/alojamiento.md` actual.

## Qué producir en `alojamiento.md`

Para **cada ciudad** (o parada) de `ciudades.md`:

- 2–3 **barrios recomendados** (máximo), con el porqué en clave:
  - **Logística**: metro, caminabilidad, traslados a estaciones/aeropuertos, cercanía a “día 1 / día 2…”
  - **Ambiente nocturno**: cenar/pasear sin taxi
  - **Tranquilidad**: si hay zonas ruidosas, decirlo
- **Precio estimado** por noche para **habitación doble (2 pax)**:
  - Si moneda ≠ €: `XXX–YYY [moneda]/noche (≈AA–BB €)`
  - Si moneda = €: `AA–BB €/noche`
- Si hay una recomendación “clara” (por el itinerario), marcarla como **recomendado** y el resto como alternativas.
- Evitar listas de hoteles concretos salvo que el usuario lo pida (este fichero va de **zonas**).

## Normas de formato

- Evitar tablas grandes: priorizar bloques por ciudad con bullets claros.
- No inventar restricciones de check-in/transportes: si es una suposición útil, decirlo como “preferible” (p. ej. “recepción 24h”).
- Precios: indicar que son **estimaciones** y mencionar si es temporada alta (p. ej. octubre en China, sakura en Japón).
- Mantener ritmo incremental: un fichero por iteración salvo petición contraria.

## Validación antes de dar por bueno

- [ ] Cada ciudad tiene **barrios + porqué + precio**.
- [ ] Moneda local + euros cuando aplica (según `conversion.md`).
- [ ] Las zonas recomendadas encajan con “Zona/Base noche” de `actividades/[ciudad].md`.
- [ ] No se ha escrito nada en `reservas.md` sin confirmación explícita.
