> **ACTUALIZACIÓN 15-nov-2026 (tarde) — LEER PRIMERO.** Este paquete reemplaza al anterior.
> - Usar siempre **1.848 predios únicos: Bajo 1.074 · Moderado 736 · Alto 38** (las cifras 1.857 / 1.083 de abajo cuentan 9 filas repetidas).
> - Nuevo: `README.md` (inglés), `figures/`, `tables/`, `complementary_analysis.py`, `01_entradas/EVA_2019_2025_Base_Agricola.csv`, `06_documentos/ROTATION_SCENARIOS_EN.md`, sección E de `LIMITACIONES.md`.
> - Los 38 Alto: 36 de suelo desnudo y 36 de <0,1 ha. No interpretarlos como cultivos en estrés.
> - Suelo (ISRIC SoilGrids, arcilla) = capa de contexto, no entra al riesgo; el cuaderno ya divide g/kg entre 10.
> - NO implementado: prioridades del agricultor, simulación de rotaciones, MODIS/SMAP. Dato NASA usado: solo GPM IMERG V07.
> - CSV con `soil_clay_pct` (en %) y JSON de parámetros ya incluidos en 03_salidas_finales/. FALTA solo copiar a 01_entradas/ el .gpkg y los PNG del cuaderno (de Drive).

# CHECKPOINT v2 — NASA Space Apps 2026 · Crop-rotation decision support (Repelón)
Estado a: sábado 14-nov-2026, 23:30 (hora Colombia). Reemplaza al checkpoint anterior.
Para retomar en otra cuenta/IA: adjunta esta carpeta (ZIP) y di "Lee 00_LEEME_CHECKPOINT.md y 06_documentos/LIMITACIONES.md; continúa en la sección 8".

## 1. Resumen en 6 líneas
- Qué es: una herramienta de apoyo a decisiones que ordena 1.857 predios rurales de Repelón (Atlántico, Colombia) por riesgo agroclimático, combinando verdor/humedad de la vegetación (Sentinel-2) con la lluvia reciente frente a la normal (NASA GPM IMERG).
- Cómo: reglas simples y transparentes (sin machine learning). Riesgo = 0,5·Amenaza (lluvia) + 0,5·Vulnerabilidad (estado de la vegetación).
- Qué NO es: no predice, no reemplaza al agricultor ni al técnico, y no sabe qué cultivo hay en cada predio.
- Estado: el modelo está terminado y revisado. Falta empaquetar y contar (deck, formulario, GitHub).
- DEADLINE: domingo 15-nov-2026, 11:59 p. m. (hora local). Se puede reenviar; cuenta la última versión.
- Quién: Samuel, solo, primer hackathon, no programador (la IA escribió el código).

## 2. Requisitos de entrega (del reto)
- Demo: deck de máx. 7 slides (con título e intro) O video de máx. 30 s. Todo en inglés (el video puede ir en español con subtítulos en inglés). Hospedado fuera (GitHub/Drive/YouTube), enlace público sin login. Si se pasa del límite, queda fuera del juicio global.
- Formulario en inglés, todos los campos obligatorios: Project Name · High-Level Summary · Link to Demo · Link to Final Project · Detailed Description · Use of Super Intelligence (uso de IA) · NASA Data · Space Agency Partner Data and Other References.
- Imágenes en el formulario: JPG/PNG/GIF hasta 10 MB. Videos/documentos: solo por enlace.
- Nada de imágenes/voz de menores de 18 años.
- Criterios de evaluación: Impact, Creativity, Validity, Relevance, Presentation.
- Reto: comparar ≥3 estrategias de rotación (incluida la actual) con por qué / evidencia / beneficios / vacíos de información / riesgos que requieren revisión local; la herramienta apoya, no reemplaza, el juicio experto; explicar la incertidumbre.

## 3. Método (todo es transparente y reproducible)
- Zona: 1.857 predios (clave CODIGO de 30 dígitos; 9 CODIGO repetidos → se conserva uno).
- Sentinel-2 SR Harmonized (ESA; COPERNICUS/S2_SR_HARMONIZED): mediana de escenas sin nubes (SCL 4 y 5), 10 m. NDVI=(B8−B4)/(B8+B4); NDMI=(B8−B11)/(B8+B11); SAVI=1,5·(B8−B4)/(B8+B4+0,5) con bandas ÷10000.
- Estrés por índice = clip((sano−x)/(sano−crítico), 0, 1). Umbrales (crítico, sano): NDVI (0,2; 0,7) · NDMI (−0,1; 0,3) · SAVI (0,05; 0,5).
- Vulnerabilidad V = 0,4·E_NDVI + 0,4·E_NDMI + 0,2·E_SAVI.
- NASA GPM IMERG V07 (mm/h, imágenes de 30 min → ×0,5): lluvia de la ventana en el píxel (~11 km) del centroide del predio. Lluvia "normal" = misma ventana de los 10 años anteriores, promedio de la zona.
- Amenaza A = clip(1 − lluvia/normal, 0, 1). Riesgo R = 0,5·A + 0,5·V. Niveles: Crítico >0,75 · Alto >0,5 · Moderado >0,25 · Bajo el resto.
- Distrito de riego: registro ADR (Repelón: ASUREP, área bruta 6.825 ha, neta 3.613 ha, 416 familias, Embalse del Guájaro) + polígono UPRA/ANT cruzado en QGIS con la regla "centroide dentro".
- GOES: solo observación/contexto (imágenes descargadas, NO integradas al modelo). No hay pronóstico.
- Ejemplo resuelto (predio 086060003000000010286000000000, corrida final): NDVI 0,399 · NDMI −0,137 · SAVI 0,225 → V 0,763; lluvia 304,7 mm → A 0,215; R = 0,5·0,215 + 0,5·0,763 = 0,489 → Moderado (a solo 0,011 del corte de Alto).

## 4. Resultados (corrida FINAL, FIN = 2026-11-15, ventana 60 días)
| | Dentro del distrito (472) | Fuera (1.385) | Total |
|---|---|---|---|
| NDVI medio | 0,63 | 0,51 | 0,54 |
| NDMI medio | 0,13 | 0,08 | 0,09 |
| Vulnerabilidad media | 0,29 | 0,47 | 0,43 |
| Bajo / Moderado / Alto | 81 % / 19 % / 0 % | 51 % / 46 % / 3 % | 1.083 / 736 / 38 |
- Lluvia media 374 mm (304–383) ≈ 96 % de la normal (≈388 mm). A medio 0,036.
- Los predios dentro del distrito están más verdes y menos vulnerables. Es una asociación coherente, no una prueba de causa.
- Corrida de contraste (marzo 2025, 90 d, época seca): Bajo 973 · Moderado 884 · Alto 0; V dentro/fuera 0,43/0,52. Amenaza = 0 en todos por un evento de lluvia en dic-2024 (112,6 mm en un mes; otros años 12–27 mm); coherente con prensa (El Heraldo y El Universal, 27-dic-2024), sin cifra oficial de IDEAM verificada.
- La vulnerabilidad de marzo y la de noviembre se parecen mucho entre predios (correlación 0,91): el ordenamiento es estable.
- Calendario mensual 2021–2025: época seca dic–mar, mínimo de NDVI mar–abr, lluvias abr–nov con una baja en julio.
- Hipótesis descartada: el contraste dentro/fuera del distrito NO se ensancha en época seca (V: 0,19 en nov → 0,09 en marzo). No usar esa frase.

## 5. Qué está comprobado y qué no (lo importante para ser honesto)
| Afirmación | Estado | Cómo se comprobó |
|---|---|---|
| El cuaderno calcula lo que dice (V y R) | ✅ Verificado | Recálculo independiente de los 1.857 predios: diferencia máx. 0,0001 |
| Dentro del distrito = 472 predios, ~5.600 ha | ✅ Verificado | Cruce QGIS, regla centroide; cabe en el área bruta del distrito (6.825 ha) |
| Los predios más "secos" se ven secos/desnudos | ✅ Verificado (muestra pequeña) | 5 predios mirados en Google Maps satélite; incluye uno urbano y un campo deportivo |
| Los más "verdes" son monte, no cultivo | ✅ Verificado (muestra pequeña) | Mismos 5 predios; revela que el modelo no distingue cultivo de bosque |
| La anomalía de lluvia de marzo 2025 | ✅ Explicada | Desglose mensual; un solo mes aportó ~70 % |
| La lluvia de noviembre es coherente | ✅ Verificado | 96 % de la normal |
| El riesgo "Alto" corresponde a estrés real del cultivo | ⬜ No comprobable aún | No hay datos de campo ni de cultivo por predio |
| Los umbrales y pesos son correctos | ⬜ No calibrados | Son supuestos iniciales; no hay calibración local |
| El resultado resiste cambios de umbral (±20 %) | ✅ El ORDEN sí (Spearman ≥0,996); la etiqueta Alto NO (0–441) | complementary_analysis.py, 1.000 combinaciones aleatorias |
| La lluvia GPM coincide con estaciones (IDEAM) | ⬜ No evaluado | Pendiente; se espera una cifra anual ~1.400 mm |
Regla práctica: lo comprobado es que el sistema es **coherente y reproducible**; lo no comprobado es que sea **exacto frente al campo**. Así se presenta.

## 6. Archivos (carpeta única Agro_FINAL; subirla entera a Drive y a GitHub)
- 01_entradas/: predios_en_distrito_nuevo.csv (QGIS, 1.187 filas; SOLO cuentan las de `asoc` llena = 472) · Distritos_de_Riego_activos_20261114.csv (registro ADR). FALTA copiar aquí: repelon_predios_rurales.gpkg (está en Drive/Agro).
- 02_cuaderno/: riesgo_agroclimatico_repelon_v2_2.ipynb (cuaderno vigente: sección 9 usa el CSV nuevo y filtra `asoc`; sección 11 guarda con fecha).
- 03_salidas_finales/: predios_para_demo_2026-11-15.csv (resultado FINAL, 1.857 filas; 1.848 predios únicos por los 9 CODIGO repetidos) · calendario_mensual.csv · ndvi_predio_ejemplo.csv. FALTA copiar aquí: parametros_modelo_2026-11-15.json (de Drive/Agro) y los PNG de gráficas (calendario_mensual.png, ndvi_predio_ejemplo.png, revision_visual.png).
- 04_historico/: corridas anteriores (no usar para la entrega; sirven como contraste y bitácora).
- 05_evidencia/: capturas de Google Maps de la comparación. Añadir aquí el Google Doc "Análisis visual de los 5 predios" exportado a PDF.
- 06_documentos/: GUIA_Y_BITACORA.md · LIMITACIONES.md (texto honesto, en español e inglés).
Excel corrompe los CODIGO de 30 dígitos: abrir los CSV solo como texto o con Python.

## 7. Datos usados (para el formulario)
- NASA: GPM IMERG V07 (lluvia). GOES (descargado, solo contexto visual).
- Socio espacial / otros: Sentinel-2 (ESA/Copernicus); registro de distritos de riego de la ADR; polígono de distritos de adecuación de tierras (UPRA y ANT); catastro de predios de Repelón; Google Maps (solo inspección visual).
- Listado de datos NASA del reto no usados por no cubrir Colombia: SSURGO, WSS, CDL, PRISM, NAIP, NLCD, NWIS, NASS, AMS, OpenET, LANDFIRE, CoCoRaHS. Aplicables pero no usados: SMAP, MODIS/VIIRS/Landsat, POWER, SRTM, ECOSTRESS, GLDAS, ERA5, FAO GAEZ (trabajo futuro).

## 8. Pendientes y orden (hasta el domingo 15, 11:59 p. m.)
1. [Esta noche] Mover todos los archivos a la carpeta Agro_FINAL (ver sección 6) y subirla a GitHub (repositorio PÚBLICO) con un README corto.
2. [Domingo mañana] Deck de 7 slides (la IA lo redacta; Samuel revisa): problema y reto · datos · método · mapa de riesgo · calendario y predio de ejemplo · 3 rotaciones · limitaciones y siguientes pasos.
3. [Domingo mediodía] Textos del formulario en inglés (resumen, descripción, uso de IA, datos).
4. [Domingo tarde] Las 3 rotaciones como ESCENARIOS con supuestos declarados (sin datos de cultivo por predio): actual + 2 alternativas, cada una con por qué / evidencia / beneficios / vacíos / riesgos que requieren revisión local. Cultivos y ciclos solo con cita (FAO GAEZ, AGROSAVIA, EVA/Agronet) o marcados "supuesto".
5. Revisar enlaces en ventana privada. Enviar antes de las 8 p. m. y reenviar si hace falta.
6. Opcional si sobra tiempo: página web de mapa; GIF de GOES; sensibilidad ±20 %; comparación con IDEAM/ERA5; máscara de cobertura (ESA WorldCover).

## 9. Reglas para la IA que continúe
- Samuel no programa: instrucciones de una en una, explicadas en sencillo; celdas completas para pegar.
- No inventar datos (cultivos, ciclos, cifras). Todo con cita o marcado "supuesto".
- No cambiar el método; sin ML. Decir siempre que umbrales y pesos son supuestos sin calibrar.
- No sobre-afirmar: "fuera del distrito" ≠ secano; el cruce con el distrito es asociación; GOES no predice; NDVI alto ≠ cultivo sano.
- Español con Samuel; inglés para todo lo que vean los jueces.
- La honestidad sobre la incertidumbre es un punto a favor, no una debilidad: presentar limitaciones como "lo que sabemos / lo que aún no podemos afirmar".
- Datos: ni Sentinel-2 ni los registros ADR/UPRA son de NASA; no atribuirlos a NASA.

---
## ACTUALIZACIÓN 15-nov-2026, 00:35 (reemplaza lo contrario en secciones 5 y 8)
Cuaderno vigente: riesgo_agroclimatico_repelon_v2_2.ipynb (añade sección 9b cobertura del suelo, sección 12 comparación de lluvia y columnas cobertura_dominante / pct_agropecuario / uso_agropecuario / baja_confianza en el CSV final). El CSV final ya las incluye.

### Los 4 puntos de robustez
1. ✅ Cobertura del suelo (ESA WorldCover 2021, 10 m). De 1.857 predios solo 386–387 son agropecuarios (cultivo+pastizal ≥50 %). Dominante: árboles 743 · pastizal 359 · construido 339 · suelo desnudo 307 · cultivo 42 · matorral 38 · humedal 25 · agua 4. V media por clase: árboles 0,17 · cultivo 0,29 · pastizal 0,33 · construido 0,65 · suelo desnudo 0,95. De los 38 predios Alto, 37 no son agropecuarios.
2. ✅ Lluvia GPM vs ERA5-Land (ECMWF), mensual 2021–2025: correlación 0,88; GPM promedia 115 mm/mes y ERA5-Land 134 mm/mes (GPM ≈14 % menor). Anual (GPM / ERA5): 2021 1.092/1.505 · 2022 1.695/2.000 · 2023 1.286/1.311 · 2024 1.553/1.679 · 2025 1.248/1.545. Ambas ven el evento de dic-2024 (GPM 82 mm, ERA5 65 mm en dic; 53 y 35 mm en ene), así que NO es un artefacto de GPM. No se sabe cuál fuente está más cerca de la lluvia real: faltan estaciones IDEAM.
3. ⬜ Dato NASA extra como contexto (SMAP humedad del suelo, o SRTM relieve): opcional, solo si sobra tiempo. No entra al puntaje.
4. ✅ Predios pequeños: columna baja_confianza (área < 0,1 ha) en el CSV; 849 predios la tienen.

### Hallazgo clave: el contraste del distrito sobrevive al control por cobertura
- Solo predios agropecuarios (386): V media 0,265 dentro del distrito (232 predios) frente a 0,429 fuera (154).
- Solo pastizal (mismo tipo de cobertura): V 0,261 dentro (202) frente a 0,427 fuera (157). Con ≥1 ha y agropecuarios: 0,253 (214) frente a 0,332 (89).
- Matiz: el contraste TOTAL (0,29 vs 0,47) mezcla tipos de cobertura distintos: de 307 predios de suelo desnudo, 304 están fuera del distrito (V≈0,95). Por eso el control es necesario. La diferencia entre predios del mismo tipo (pastizal) es menor que la total pero se mantiene.
- Sigue siendo una asociación, no una prueba de que el riego sea la causa.
- Candidatos para ejemplo (agropecuarios ≥1 ha de mayor V, todos pastizal ≥87 %): …230 (53 ha, Alto), …286 (53 ha, ejemplo actual), …004 (80 ha), …003 (65 ha). En distrito y vulnerable: …274 (4,9 ha, V 0,80).
- Cautelas WorldCover: es un mapa modelado de 2021; "construido" (339) y "suelo desnudo" (307) pueden incluir confusión en zona seca; "árboles" puede incluir potreros arbolados. Se usa como etiqueta de apoyo, no como verdad de campo; revisar 3–4 predios en Google Maps.

### Sección 8 (plan) actualizada
Modelo y robustez: CERRADOS. Lo que queda, en orden: (a) mover archivos a Agro_FINAL y subir a GitHub público + README; (b) deck de 7 slides en inglés; (c) textos del formulario en inglés; (d) 3 rotaciones como escenarios con supuestos declarados; (e) revisar enlaces y enviar antes de las 8 p. m. del domingo 15.
