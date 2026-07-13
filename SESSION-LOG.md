# Log de sesiones

Resumen de conversaciones para continuidad entre sesiones. Los agentes añaden entradas al final.

---

## 2026-07-13 — Inicio del harness

**Viaje:** (general / china)

**Resumen:**
- Se define el harness de planificación de viajes.
- Estructura: log de sesiones, carpeta por viaje (`2026-china/`), `reservas.md` como verdad absoluta (solo con confirmación explícita), ficheros por tipo.
- Ritmo incremental: pocos cambios por iteración.

**Decisiones tomadas:**
- Carpetas de viaje: `YYYY-destino` (p. ej. `2026-china`).
- Ficheros por tipo: transportes, alojamiento, actividades, ciudades, presupuesto, documentacion.
- Agentes especializados: pendiente.

**Pendiente de decidir:**
- Formato exacto de entradas en reservas.
- Frase o ritual de confirmación para escribir en reservas.

**Confirmado en reservas:** (nada aún)

---

## 2026-07-13 — Renombre FACTS → reservas

**Viaje:** general

**Resumen:** `FACTS.md` renombrado a `reservas.md`. Referencias actualizadas en AGENTS.md, skill, rule y ficheros del viaje.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Borrador de ciudades China

**Viaje:** 2026-china

**Resumen:** Usuario baraja 9 destinos (Pekín, Xi'an, Chongqing, Chengdu, Furong, Guilin, Fenghuang, Zhangjiajie, Shanghái). Análisis de orden, redundancias y días en `ciudades.md`. Nada confirmado en reservas.

**Pendiente:** duración del viaje, recortar o mantener Furong/Fenghuang/Chongqing.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Ventana de vacaciones

**Viaje:** 2026-china

**Resumen:** Vacaciones pedidas del 10 oct al 1 nov 2026 (23 días calendario, ~19–21 en China). Con 9 ciudades en baraja, el itinerario va justo; recorte sugerido: Chongqing y/o Furong. Actualizado `ciudades.md`.

**Pendiente:** confirmar fechas en reservas, decidir recortes.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Itinerario borrador Pekín (3 días)

**Viaje:** 2026-china

**Resumen:** Pekín confirmado como destino. Usuario propone 3 días (Ciudad Prohibida+Jingshan+Templo del Cielo / Mutianyu+hutongs / Palacio de Verano). Análisis y refinamiento en `actividades.md`. Olímpico (Nido+Cubo) encaja día 3 tarde.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Fichero por ciudad + plantilla

**Viaje:** 2026-china

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Harness raíz + carpeta actividades/

**Viaje:** general (harness)

**Resumen:** Harness reutilizable en raíz (`AGENTS.md`, `SESSION-LOG.md`, `plantilla-ciudad.md`). Itinerarios movidos a `2026-china/actividades/`. Eliminado `actividades.md`. Enlaces en `ciudades.md`.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Skill planificar-ciudad + restricciones

**Viaje:** general (harness)

**Resumen:** Nueva skill `planificar-ciudad` para itinerarios por ciudad. Columna Restricciones obligatoria (horarios, cierres, reservas). Plantilla y `pekin.md` actualizados. Agente documentado en `AGENTS.md`.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Intereses compras Pekín

**Viaje:** 2026-china

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Herramienta PDF guía imprimible

**Viaje:** general (harness)

**Resumen:** Creada `tools/generar-guia.py` para exportar un viaje a PDF A4 (portada, secciones del viaje, ciudades en orden del itinerario). Dependencias en `tools/requirements.txt`. Uso documentado en `tools/README.md`. PDF por defecto en raíz del repo. Índice con números de página (dos pasadas + marcadores `sec-`/`day-`).

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — intereses.md y equilibrio

**Viaje:** general (harness)

**Resumen:** Creado `intereses.md` en raíz. Farmacias = detalle Sandra, 1–2 por ciudad max. Pekín simplificado. Intereses no son prioridad sobre Programa.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Itinerario borrador Xi'an (2 días)

**Viaje:** 2026-china

**Resumen:** Usuario lista: terracota, torres, centro histórico, barrio musulmán, Gran Pagoda. Repartido en 2 días en `actividades/xian.md` + gastronomía shaanxi.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Xi'an + Shanghái confirmados

**Viaje:** 2026-china

**Resumen:** Xi'an y Shanghái marcados confirmados. Shanghái: 2 días Bund/Pudong + Yu/Concesión Francesa. Cierre del viaje.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Zhangjiajie confirmado (2 días)

**Viaje:** 2026-china

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Chengdu y Chongqing (opción)

**Viaje:** 2026-china

**Resumen:** Itinerarios borrador 2 días cada uno, estado `opción`. Chengdu: pandas (reserva usuario) + Kuanzhai/Jinli/Wenshu/People's Park. Chongqing: Luohan, Shibati, Datang/Kuixing, Liziba, Hongyadong; día 2 sábado drones 魅力重庆. Actualizado `ciudades.md`.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Consejos locales: apartado Apps

**Viaje:** 2026-china

**Resumen:** Añadido apartado **Apps** en `2026-china/consejos-locales.md` con pagos (Alipay/WeChat), mapas (AMap), transporte (DiDi), reservas (Trip.com), traductor (Baidu/Papago) y extras recomendables (VPN con estrategia de respaldo, Pleco, Dianping, Baidu Maps).

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Fenghuang, Furong y Guilin/Yangshuo (opción)

**Viaje:** 2026-china

**Resumen:** Itinerarios creados bajo los mismos criterios y en estado `opción`: `actividades/fenghuang.md` (1 día, noche Tuojiang), `actividades/furong.md` (0.5–1 día, cascada nocturna ≈19:30), `actividades/guilin.md` (2 días, crucero Li River + base Yangshuo + Yulong rafting). `ciudades.md` actualizado con enlaces y días.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Alojamiento por barrios + skill nueva

**Viaje:** 2026-china

**Resumen:**
- Rellenado `2026-china/alojamiento.md` con **barrios recomendados** por ciudad/parada (Pekín, Xi’an, Shanghái, Zhangjiajie/Wulingyuan y opciones) y **precio estimado** en CNY y € usando `conversion.md`.
- Creada la skill **`ver-alojamiento`** para estandarizar el flujo de “leer itinerarios → proponer barrios → estimar precio” y reutilizarlo en futuros viajes.

**Confirmado en reservas:** (nada)

---

## 2026-07-13 — Títulos imprimibles en ciudades

**Viaje:** 2026-china (harness)

**Resumen:** Normalizado el encabezado de cada fichero de `2026-china/actividades/*.md` para que al imprimir se vea claramente el **título (ciudad)**: H1 con el nombre de la ciudad + línea `**Duración:** …`. Plantilla de ciudad actualizada para mantener el mismo formato.

**Confirmado en reservas:** (nada)
