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

---

## 2026-08-18 — Reserva tren España confirmada

**Viaje:** 2026-china

**Resumen:** Usuario confirma billete Renfe AVE Santiago → Madrid Chamartín (10/10/2026, localizador FUFRG9). PDF guardado en `2026-china/docs/FUFRG9.pdf`. Escrito en `reservas.md`. No modificar salvo nueva confirmación explícita.

**Confirmado en reservas:** tren AVE 04254, 10/10/2026, FUFRG9 (2 pax).

---

## 2026-08-18 — Reserva tren 2NXU56 confirmada

**Viaje:** 2026-china

**Resumen:** Usuario confirma localizador 2NXU56: AVLO Santiago→Chamartín 10/10/2026 16:26 + AVE Chamartín→Santiago 01/11/2026 14:40. PDF en `2026-china/docs/2NXU56.pdf`. Añadido a `reservas.md`.

**Confirmado en reservas:** tren 2NXU56 (ida AVLO + vuelta AVE, 2 pax).

---

## 2026-08-18 — Vuelos Qatar confirmados

**Viaje:** 2026-china

**Resumen:** Usuario confirma billetes Qatar/Iberia PNR 9O7N2T (Sandra + Santiago). Ida MAD→DOH→HKG (10–11 oct) y vuelta PVG→DOH→MAD (31 oct–1 nov). PDF en `docs/QR-9O7N2T-*.pdf`. Añadido a `reservas.md`.

**Confirmado en reservas:** vuelos 9O7N2T (2 pax, 1.805,60 €).

---

## 2026-08-18 — Reservas partidas en summary + detail

**Viaje:** 2026-china (harness)

**Resumen:** `reservas.md` sustituido por `reservas-summary.md` (histórico cronológico fecha/inicio/qué/fin) y `reservas-detail.md` (detalle). Actualizados AGENTS, skills, rule y `generar-guia.py`.

---

## 2026-08-18 — Replan tras vuelos HKG→PVG

**Viaje:** 2026-china

**Resumen:** Vuelos confirmados cambian la geografía: entrada **HKG 11/10 21:55**, salida **PVG 31/10 18:10**. Usuario quiere mantener las mismas ciudades de primeras. Reescrito `ciudades.md` (escenarios A/B/C) y `transportes.md`. Borrador activo propuesto: Escenario A (norte primero, sin Chongqing/Furong).

**Pendiente:** elegir escenario A vs B/B2; noche HKG; vuelo HKG→PEK; Chongqing drones sí/no; Furong sí/no.

**Confirmado en reservas:** (sin cambios — vuelos ya estaban).

---

## 2026-08-18 — Plan A fichero aparte (HK + Shenzhen)

**Viaje:** 2026-china

**Resumen:** Creado `2026-china/plan-A.md`. Fijado: hotel HK noche 11, día 12 en HK, noche 12 → Shenzhen. Comparativa de saltos desde Shenzhen (óptimo tiempo+€: Guilin en tren AV). Enlace desde `ciudades.md`.

**Pendiente:** destino post-Shenzhen; hotel HK; cruce frontera HK→SZ.

---

## 2026-08-18 — Web MkDocs del viaje

**Viaje:** 2026-china (harness)

**Resumen:** Añadida capa web interactiva con MkDocs Material en `web/`. Sync desde `2026-china/` (`scripts/sync-from-viaje.py`); builds `online` → `web/site/` y `offline` → `web/site-offline/`. Integrado en AGENTS §6, skill `viajes-harness`, rule y `tools/README.md`. Diseño en `docs/superpowers/specs/2026-08-18-mkdocs-web-viaje-design.md`. Privacidad: repo privado + URL no anunciada + noindex; PDFs incluidos.

**Pendiente:** publicar `web/site/` en host (Cloudflare Pages / Pages) cuando se quiera el enlace online.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Horarios Hong Kong → Shenzhen completados

**Viaje:** 2026-china

**Resumen:** Completados en `plan-A.md` los horarios provisionales del cruce: salida de Hong Kong el 12/10 a las 21:00 y llegada a Shenzhen a las 22:00. Duraciones de tabla: Hong Kong 23 h y Shenzhen 21 h hasta el D864 del 13/10.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Tren Shenzhen → Guilin fijado provisionalmente

**Viaje:** 2026-china

**Resumen:** Guardada `docs/plan-A/shenzhen-guilin-d864.png`. Fijado provisionalmente el D864 para el **13/10**: Shenzhenbei 18:32 → Guilinxi 21:18, 2 h 46 min, 31,41 € por persona. Guilin queda con la noche del 13 antes del D3968 a Fenghuang el 14.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Fecha Guilin → Fenghuang fijada

**Viaje:** 2026-china

**Resumen:** Guardada `docs/plan-A/guilin-fenghuang-d3968.png`. Fijado provisionalmente el D3968 para el **14/10**: Guilinbei 14:55 → Fenghuang Gucheng 21:02, 6 h 07 min, 39,07 € por persona. Fenghuang queda con las noches del 14 y 15.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Fechas Hunan fijadas provisionalmente

**Viaje:** 2026-china

**Resumen:** Guardadas las capturas `docs/plan-A/fenghuang-furong-g6422.png` y `furong-zjj-g6422.png`. Fijado provisionalmente: Fenghuang → Furong el 16/10 (09:03→09:37, G6422) y Furong → Zhangjiajie el 17/10 (09:39→10:02, G6422). Furong queda con una noche, la del 16.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Tren Zhangjiajie → Chongqing elegido provisionalmente

**Viaje:** 2026-china

**Resumen:** Guardada `docs/plan-A/zhangjiajie-chongqing-g3870.png`. Fijado provisionalmente para el 19/10 el G3870: Zhangjiajiexi 19:24 → Chongqing Este 22:10, 2 h 46 min, 30,51 € por persona. Chongqing queda con dos noches (19 y 20) antes del G2164 a Chengdu el 21.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Tren Chongqing → Chengdu elegido provisionalmente

**Viaje:** 2026-china

**Resumen:** Guardada `docs/plan-A/chongqing-chengdu-g2164.png`. Fijado provisionalmente para el 21/10 el G2164: Chongqingxi 14:05 → Chengdudong 15:40, 1 h 35 min, 25,01 € por persona. Chengdu queda con dos noches (21 y 22) antes del K998 a Xi'an el 23.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Resumen de ciudades y cronología del Plan A

**Viaje:** 2026-china

**Resumen:** En `plan-A.md`, renombrado “Fijado hasta ahora” a **“Cronología”**. Añadida antes una tabla de ciudades apuntadas con columnas de entrada, salida, duración y estado; las duraciones solo se calculan cuando hay horas disponibles.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Hoteles y noches en el resumen del Plan A

**Viaje:** 2026-china

**Resumen:** Añadida una columna **Noches** en “Fijado hasta ahora” de `plan-A.md` y filas de hotel para Hong Kong, Shenzhen, Xi'an, Pekín y Shanghái. Noches actualmente fijadas: HKG 1, Shenzhen 1, Xi'an 1, Pekín 2 y Shanghái 2. Alojamientos aún pendientes de buscar.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Hipótesis Chengdu → Xi'an con una noche

**Viaje:** 2026-china

**Resumen:** Guardada `docs/plan-A/chengdu-xian-k998.png`. Hipótesis registrada: salir de Chengdu el 23/10 a las 19:27 con K998, llegar a Xi'an el 24/10 a las 07:08, pasar una noche allí y continuar el 25/10 a las 20:35 con D44 hacia Pekín.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Salida de Pekín fijada en Plan A

**Viaje:** 2026-china

**Resumen:** Añadida a “Fijado hasta ahora” la salida de Pekín con el T109 el **28/10 a las 20:05**, con llegada prevista a Shanghái el 29/10 a las 11:00.

**Confirmado en reservas:** (sin cambios; tren todavía no reservado).

---

## 2026-08-18 — Hipótesis D44 Xi'an → Pekín

**Viaje:** 2026-china

**Resumen:** Registrada la captura del D44: Xi'an 20:35 → Beijingxi 08:23 (+1), 11 h 48 min, 28,59 €. Corrección del usuario: salir de Xi'an el 25/10, llegar a Pekín el 26/10 a las 08:23, dormir las noches del 26 y 27, y salir de Pekín el 28. No confirmado ni reservado.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Plan A fija Shanghái en dos días

**Viaje:** 2026-china

**Resumen:** El usuario vuelve al Plan A y fija provisionalmente **2 días en Shanghái**. Si se usa el tren nocturno T109 Pekín→Shanghái (20:05→11:00), la llegada prevista es el **29/10 a las 11:00**; el 29 y 30 quedan para Shanghái, con la mañana del 31 antes del vuelo PVG 18:10. Podría reducirse a 1,5 días más adelante.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Opciones Pekín → Shanghái registradas

**Viaje:** 2026-china

**Resumen:** Guardadas las capturas `docs/plan-A/pekin-shanghai-vuelo.png` y `pekin-shanghai-tren.png`. Comparadas opciones: avión directo 66–79 €; tren nocturno D9 19:35→08:00, 12 h 24 min, 45,59 €; tren rápido G35 4 h 25 min, 87,15 €. Añadido al Plan A.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Opciones Xi'an → Pekín registradas

**Viaje:** 2026-china

**Resumen:** Guardadas las capturas `docs/plan-A/xian-pekin-tren.png` y `xian-pekin-vuelo.png`. Comparadas opciones: tren nocturno D44 20:35→08:23, 11 h 48 min, 28,58 €; vuelos directos 1 h 55–2 h, 79–85 €. Añadido al Plan A.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Precio Guilin → Fenghuang registrado

**Viaje:** 2026-china

**Resumen:** Guardada la captura `docs/plan-A/guilin-fenghuang.png`. D3968 Guilinbei → Fenghuang Gucheng: 14:55→21:02, 6 h 07 min, 39,06 € por persona; billete en prereserva. Actualizada la suma del Plan A con Guilin (~159–190 € por persona en la cadena comparada).

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-18 — Plan B (copia del A, sin Guilin)

**Viaje:** 2026-china

**Resumen:** Creado `2026-china/plan-B.md` copiando el Plan A. Se sacan Guilin/Yangshuo. Shanghái, Pekín, Xi'an, Chengdu, Chongqing y Zhangjiajie quedan iguales. Fijado provisionalmente el G6080 el **15/10**: Shenzhenbei 08:33 → Fenghuang Gucheng 13:54, 5 h 21 min, 70,74 € por persona. Captura en `docs/plan-B/shenzhen-fenghuang-g6080.png` (no se duplicó el resto). Fenghuang queda en 1 noche; los días 13 y 14 quedan libres.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C de cero (solo reservado)

**Viaje:** 2026-china

**Resumen:** Creado `2026-china/plan-C.md` de cero. Cronología y ciudades apuntadas solo con lo confirmado en reservas (trenes España + vuelos HKG/PVG). Enlace añadido en `ciudades.md`. No se tocaron reservas.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: día de la semana

**Viaje:** 2026-china

**Resumen:** Añadida columna **Día** (lun–dom) en la cronología del Plan C, y el día junto a las fechas de HK/Shanghái. Oct 2026: 10 y 31 = sáb; 11 y 1 nov = dom.

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: tren G23 Pekín → Shanghái

**Viaje:** 2026-china

**Resumen:** Usuario fija **jue 29/10** el G23 Beijingnan 11:00 → Shanghai Hongqiao 15:35 (4 h 37 min, 91,17 €/pax). Actualizado `plan-C.md` (ciudades, cronología, captura en `docs/plan-C/pekin-shanghai-g23.png`). Shanghái: tarde 29 + 30 + mañana 31 antes de PVG.

**Confirmado en reservas:** (sin cambios — tren interno aún no reservado).

---

## 2026-08-22 — Plan C: vuelo Chengdu → Pekín (lun 26)

**Viaje:** 2026-china

**Resumen:** Usuario fija vuelo **lun 26/10** Chengdu TFU 11:15 → Pekín PKX 13:55 (China United, directo, equipaje incluido, 99 €/pax). Encaja antes del G23 del jue 29. Captura en `docs/plan-C/chengdu-pekin-vuelo.png`. Pekín: ~2 d 21 h (26 tarde → 29 mañana).

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: tren G2426 Zhangjiajie → Chongqing (jue 23)

**Viaje:** 2026-china

**Resumen:** Usuario fija **jue 23/10** el G2426 Zhangjiajiexi 08:52 → Chongqing Este 10:54 (2 h 02 min, 33,29 €/pax). Encaja antes del G8626 del sáb 25 (drones CQ). Captura en `docs/plan-C/zhangjiajie-chongqing-g2426.png`. Chongqing: ~2 d 4 h (23 tarde → 25 tarde).

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: tren G5646 Hong Kong → Shenzhen (mar 13)

**Viaje:** 2026-china

**Resumen:** Usuario fija **mar 13/10** el G5646 West Kowloon 14:04 → Shenzhenbei 14:28 (24 min, 11,55 €/pax). HK: noche 11 + día 12 + tarde 13. Captura en `docs/plan-C/hongkong-shenzhen-g5646.png`. Falta enlazar Shenzhen → Zhangjiajie (13–22 oct).

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: tren G908 Shenzhen → Guilin (jue 15)

**Viaje:** 2026-china

**Resumen:** Usuario fija **jue 15/10** el G908 Shenzhenbei 11:37 → Guilinxi 14:16 (2 h 39 min, 44,41 €/pax). Shenzhen: ~1 d 21 h (13 tarde → 15 mañana). Falta enlazar Guilin → Zhangjiajie (15–22 oct).

**Confirmado en reservas:** (sin cambios).

---

## 2026-08-22 — Plan C: tren G8626 Chongqing → Chengdu (sáb 25)

**Viaje:** 2026-china

**Resumen:** Usuario fija **sáb 25/10** el G8626 Shapingba 14:35 → Chengdudong 15:50 (1 h 15 min, 21,85 €/pax). Encaja antes del vuelo a Pekín del lun 26. Captura en `docs/plan-C/chongqing-chengdu-g8626.png`. Sáb 25 = posible drones en Chongqing.

**Confirmado en reservas:** (sin cambios).
