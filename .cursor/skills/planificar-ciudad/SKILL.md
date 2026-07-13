---
name: planificar-ciudad
description: Planifica o refina el itinerario día a día de una ciudad en cualquier viaje Viaxes (2026-china, 2027-japon, etc.). Usar al crear o editar actividades/[ciudad].md, horarios, cierres o restricciones — en cualquier carpeta YYYY-destino/.
---

# Planificar ciudad

Skill **universal** del harness Viaxes: misma estructura y normas para **todos los viajes** (`2026-china/`, `2027-japon/`, etc.).

No asumir reglas de un destino concreto (China, Japón…) salvo que estén en el fichero de **ese** viaje (p. ej. `2026-china/consejos-locales.md`).

Complementa `viajes-harness` (estructura general del repo).

**Plantilla:** [plantilla.md](plantilla.md) — copiar al crear un fichero nuevo en `YYYY-destino/actividades/[ciudad].md`.

## Antes de escribir

1. Leer `SESSION-LOG.md`, **`intereses.md`** (raíz), `reservas.md` y `ciudades.md` **del viaje activo**.
2. Leer **`YYYY-destino/consejos-locales.md`** si existe (horarios, trucos del destino).
3. Leer **`YYYY-destino/conversion.md`** si existe (tabla moneda → €; **obligatorio** cuando el destino no usa euro).
4. Leer el fichero existente `actividades/[ciudad].md` si existe.
5. Si es fichero nuevo, copiar [plantilla.md](plantilla.md).
6. Cruzar el itinerario con las **fechas reales** del viaje (día de la semana importa para cierres).

## Normas obligatorias

### Restricciones por actividad (importantísimo)

La columna **Restricciones** recoge horarios, cierres y requisitos operativos que **afectan a la planificación**.

**Solo rellenar cuando haya una restricción real**, por ejemplo:

- Horario de apertura/cierre (`08:30–17:00`)
- Días de cierre (`cierra lun`)
- Reserva o cupo obligatorio
- Última entrada relevante
- Estacionalidad que cambie el horario

**No rellenar** si no hay restricción útil:

- Dejar la celda **vacía**
- No poner «abierto 24h», «exterior 24h» ni equivalentes
- No inventar horarios
- No poner `—` como relleno

Si se conoce que hay horario pero no el detalle exacto: `⚠️ verificar horario` (solo entonces).

### Precio de entrada

Columna **Entrada** en **Programa**, **Plan B** (si aplica) y **Deck** (sitios de pago).

| Caso | Qué escribir |
|------|----------------|
| Gratis | `Gratis` |
| Precio conocido | `[moneda local] (≈€)` — ej. `180 CNY (≈25 €)`, `¥1.500 (≈10 €)`, `12 €` |
| Precio desactualizado | Igual + año `(2022)` — **solo** cuando la fuente no es reciente |
| Desconocido | Celda vacía |

- **Siempre** moneda local + equivalente en **euros** entre paréntesis cuando haya moneda distinta del €.
- Usar **≈** para aproximaciones, no `~` (el tilde puede renderizarse como tachado en Markdown).
- Tipo de cambio → usar **`YYYY-destino/conversion.md`** (tabla ancla fácil de recordar). Crear desde [conversion.plantilla.md](../viajes-harness/conversion.plantilla.md) si no existe.
- Extras en la misma celda: `40 CNY (≈6 €) + ≈100 teleférico (≈14 €)`.
- Los totales del viaje van también en `presupuesto.md` cuando se confirme.

Al proponer un día concreto, comprobar que **ese día de la semana** el sitio está abierto.

**Formato compacto** (cuando aplique):

```
L–D 08:30–17:00 · última entrada 16:00
cierra lun · reserva obligatoria
abr–oct 06:30–20:00 / nov–mar 07:00–18:00
```

### Horarios del programa

- Horas **realistas** dentro de apertura + tiempo de visita + traslados del día.
- Patrones locales (picos turísticos, siesta, último tren…) → investigar o leer `consejos-locales.md` del viaje; **no** copiar reglas de otro país.
- Si el destino tiene consejos de franja horaria documentados, aplicarlos en ese viaje únicamente.

### Estructura por día

Ver [plantilla.md](plantilla.md). Resumen:

- **Programa** — horario principal
- **Plan B (misma zona)** — lista de actividades extra en la zona del día, por si queréis cambiar de plan o no completar el programa (no es contingencia por cierres)
- **Deck** — fuera del itinerario; no cabe en los días previstos. **Sin** columna «sustituiría a». Incluir **Por qué** el esfuerzo (bajo / medio / alto)
- **Compras y curiosidades** — menú opcional. Consultar `intereses.md`; **máx. 1–2 toques** por interés y ciudad, sin saturar
- **Gastronomía** — apartado sin horario: platos típicos (nombre + descripción corta), **imprescindible** si solo allí, restaurantes muy emblemáticos
- **Experiencias** — espectáculos y actividades (la comida va en **Gastronomía**)

Si el día tiene **varias zonas** (mañana/tarde), agrupar Plan B por subzona.

Cada día: **Zona** y **Base noche**.

### Otras normas

- No escribir en `reservas.md` salvo confirmación explícita del usuario.
- Ritmo incremental: un día o un bloque por iteración salvo petición contraria.
- Actualizar `ciudades.md` (estado, días) y `SESSION-LOG.md` al terminar.

## Flujo de trabajo

1. Confirmar cuántos días y qué quiere ver el usuario.
2. Agrupar por zona geográfica para minimizar traslados.
3. Leer `consejos-locales.md` del viaje si existe.
4. Investigar restricciones donde existan (web, fuentes oficiales).
5. Redactar Programa con horas realistas respetando aperturas.
6. Añadir Plan B: actividades extra en la misma zona (lista, no formato «si falla X → Y»).
7. Añadir Deck para lo que no cabe (con motivo del esfuerzo).

### Deck — esfuerzo

| Nivel | Cuándo usarlo | Ejemplo de «Por qué» |
|-------|---------------|----------------------|
| **bajo** | Hueco de 1–2 h, poco traslado, encaja sin replanificar mucho | «Noche, cerca del hotel, reserva online» |
| **medio** | Medio día o cruce moderado de ciudad | «≈3 h visita + metro 30 min desde centro» |
| **alto** | Día entero o traslado largo | «2 h ida desde la ciudad, día completo» |

La columna **Por qué** explica en una frase: traslado, duración, replanificación necesaria.

8. Añadir **Gastronomía** (platos + restaurantes emblemáticos, sin días).
9. Añadir **Compras y curiosidades** (menú local / curiosidades del destino).
10. Sección **Pendiente** con lo por verificar o decidir.

## Validación antes de dar por bueno

- [ ] Restricciones solo donde aportan (celdas vacías si no hay)
- [ ] Los días propuestos no caen en cierre semanal de sitios clave
- [ ] Horas del programa encajan dentro de apertura + tiempo de visita
- [ ] Estructura coincide con [plantilla.md](plantilla.md)
- [ ] Apartado **Gastronomía** con platos y restaurantes (sin horario)
- [ ] Consejos específicos del destino aplicados **solo** si están en `consejos-locales.md` de ese viaje
- [ ] Euros en tablas cuadran con `conversion.md` del viaje (si moneda ≠ €)
