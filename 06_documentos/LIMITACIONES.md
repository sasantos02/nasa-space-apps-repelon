# Limitaciones y observaciones — escritas con honestidad
Idea guía: cada limitación dice (1) qué sabemos, (2) qué todavía no podemos afirmar y (3) qué haría falta. Así se presenta ante los jueces: como transparencia sobre la incertidumbre, que es lo que pide el reto.

## A. Español (para Samuel)

1. **Umbrales y pesos son supuestos iniciales.** Sabemos que el ordenamiento de predios es estable (correlación 0,91 entre dos épocas distintas). No podemos afirmar que los cortes de Bajo/Moderado/Alto sean correctos. Haría falta calibrarlos con datos de campo o con un técnico local.
2. **La categoría "Alto" es sensible a la fecha.** Con un día más de ventana (lluvia de 363 a 374 mm), los predios en riesgo Alto pasaron de 259 a 38, porque muchos estaban justo en el borde del corte. Lo robusto es el orden por vulnerabilidad, no el número exacto de predios en cada nivel.
3. **Los índices miden verdor y humedad, no el tipo de cobertura.** En la revisión visual, los predios "más verdes" eran monte, y uno de los "más secos" era zona urbana junto a un campo deportivo. El modelo no distingue cultivo de bosque, pasto, suelo desnudo o construcciones. Haría falta una capa de cobertura del suelo (por ejemplo ESA WorldCover) para quedarse solo con cultivos y pastizales.
4. **No hay datos de cultivo ni de rotación por predio.** Esa información no es pública. Las tres rotaciones se presentan como escenarios con supuestos declarados y citas, y los riesgos que requieren revisión local se marcan como tales. Haría falta el registro de la UMATA o de los agricultores (EVA, Agronet).
5. **La lluvia tiene baja resolución espacial.** GPM IMERG tiene píxeles de unos 11 km, así que la amenaza casi no distingue un predio de otro (rango 305–383 mm). Por eso el contraste entre predios lo aporta sobre todo la vulnerabilidad.
6. **La "lluvia normal" de la época seca es poco estable.** Entre 2014 y 2024, la lluvia de dic–mar en la zona varió de 9,6 a 72 mm. Un solo evento (112,6 mm en un mes, dic-2024) hizo que la corrida de marzo diera "551 % de lo normal" y amenaza cero. Fue explicado, y la corrida se conserva como contraste de época seca.
7. **El distrito de riego es una asociación, no una prueba.** Los 472 predios "dentro" son más verdes y menos vulnerables, pero no demostramos que el riego sea la causa. "Fuera del distrito" no significa secano. El cruce usa el centroide sobre una capa con búfer negativo, que puede diferir ligeramente de la capa del cuaderno (efecto esperado: pocos predios de borde).
8. **Predios muy pequeños tienen baja confianza.** Cerca de una cuarta parte mide 0,01 ha o menos, y el píxel de 10 m es grande frente a ellos. 961 predios miden 1 ha o más.
9. **La validación visual es una muestra pequeña.** Se revisaron 10 predios, por una persona, con imágenes de Google que pueden ser de otra fecha. Muestra coherencia, no precisión estadística.
10. **Falta contraste con otras fuentes.** No se comparó la lluvia GPM con estaciones IDEAM ni con ERA5. No se probó la sensibilidad de los resultados a cambios de ±20 % en los umbrales.
11. **No hay suelo ni temperatura.** El reto los menciona; no entraron en esta versión (capas posibles: SoilGrids/OpenLandMap, NASA POWER, SMAP).
12. **No es un pronóstico.** GOES se descargó pero no se integró al modelo. Los escenarios de lluvia son "qué pasaría si", no predicciones.
13. **Origen de los datos.** Sentinel-2 es de ESA; el registro del distrito es de la ADR y el polígono de UPRA y ANT. De NASA se usó GPM IMERG.
14. **Calidad de datos.** Hay 9 CODIGO repetidos (se conserva uno); Excel corrompe los códigos de 30 dígitos.

**Lo que sí podemos afirmar con confianza:** el cálculo es reproducible y coincide con un recálculo independiente (diferencia máxima 0,0001); la zona de riego aparece sistemáticamente más verde y menos vulnerable; el ordenamiento de predios es estable entre épocas; la herramienta deja claro dónde hace falta criterio local.

## B. English (paste-ready for the submission form)

**Limitations and how we handle them**

- **Thresholds and weights are initial assumptions, not calibrated.** The ranking of parcels is stable across two very different seasons (correlation 0.91), but the Low/Moderate/High cut-offs are not validated. We recommend calibration with local field data.
- **The "High" class is sensitive to the analysis date.** A one-day shift in the window moved parcels across a cut-off (259 → 38 High). We therefore treat the ordering by vulnerability as the robust output and the class counts as indicative.
- **Spectral indices measure greenness and moisture, not land use.** Visual checks showed that the greenest parcels are mostly woodland and that one of the driest is built-up land. A land-cover mask (e.g., ESA WorldCover) is a planned improvement.
- **No parcel-level crop or rotation data are public.** Rotation strategies are presented as scenarios with explicit assumptions and cited references, and items needing local review are flagged. The tool supports, and does not replace, farmer and expert judgment.
- **Rainfall resolution is coarse (~11 km).** Hazard varies little between parcels; vulnerability carries most of the spatial contrast.
- **Dry-season "normal" rainfall is highly variable** (9.6–72 mm over ten years). A single December 2024 event (112.6 mm in one month) explains why one run showed zero hazard. We report this openly.
- **Irrigation-district membership is an association, not proof of causation.** Parcels outside the district are not necessarily rainfed.
- **Small parcels are low-confidence** at 10 m resolution.
- **Validation is limited:** independent recalculation of the model (max difference 0.0001) and a visual check of 10 parcels; no field data, no comparison yet with IDEAM or ERA5 stations, no sensitivity test.
- **Not a forecast.** The tool describes current conditions and "what-if" rainfall scenarios.

**What the tool already does well:** transparent rule-based logic that anyone can audit, reproducible results from open Earth observation data, a clear separation between what is measured and what is assumed, and explicit pointers to where local expertise is needed.

## C. Prueba de sensibilidad (hecha el 14-nov-2026, sobre predios_para_demo_2026-11-15.csv, sin Earth Engine)
Se movieron umbrales y pesos ±20 % y se comparó con el resultado base (1.848 predios únicos).
| Cambio | Correlación de orden (Spearman) | Predios que cambian de nivel | Coinciden en el 10 % más riesgoso | Alto resultante |
|---|---|---|---|---|
| Umbrales más estrictos (+20 % del rango) | 0,994 | 34 % | 65 % | 373 |
| Umbrales más laxos (−20 %) | 0,987 | 16 % | 87 % | 0 |
| Pesos NDVI/NDMI/SAVI 0,5/0,3/0,2 | 0,999 | 3 % | 97 % | 45 |
| Pesos 0,3/0,5/0,2 | 0,999 | 3 % | 94 % | 36 |
| Pesos iguales | 1,000 | 2 % | 93 % | 26 |
| Peso de la amenaza 0,3 (en vez de 0,5) | 0,995 | 34 % | 98 % | 488 |
| Peso de la amenaza 0,7 | 0,981 | 19 % | 89 % | 0 |
Lectura honesta: el ORDEN de los predios es muy estable (correlación ≥ 0,98); los NIVELES dependen mucho de dónde se pongan los cortes (Alto va de 0 a 488 predios según el supuesto). Por eso se presenta el orden como resultado principal y los niveles como indicativos.
English: "Parcel ranking is robust to ±20 % changes in thresholds and weights (Spearman ≥ 0.98), while class counts are not (High ranges from 0 to 488 parcels). We therefore treat the ranking as the main output and the classes as indicative."

## D. Actualización 15-nov-2026 (cobertura del suelo y lluvia contrastada)
Actualiza los puntos 3 y 10 de la sección A.
- **Punto 3 (cobertura):** ahora medido. Solo ~21 % de los predios (386 de 1.848 únicos) son agropecuarios según ESA WorldCover 2021; 743 tienen árboles dominantes, 339 construido y 307 suelo desnudo. Los predios más "sanos" (V=0) son casi todos de árboles; los más vulnerables en uso agropecuario son pastizales grandes. El mapa de cobertura es un producto modelado de 2021: se usa como etiqueta de apoyo, con revisión visual de una muestra. Ya existe la columna `uso_agropecuario` para filtrar.
- **El contraste del distrito se mantiene con control por cobertura:** V 0,265 dentro frente a 0,429 fuera en predios agropecuarios; 0,261 frente a 0,427 solo en pastizal. Antes del control, la diferencia estaba inflada porque casi todo el suelo desnudo (304 de 307) cae fuera del distrito. Sigue siendo asociación.
- **Punto 10 (lluvia):** GPM y ERA5-Land correlacionan 0,88 mes a mes (2021 a 2025). GPM da en promedio ~14 % menos lluvia que ERA5-Land (115 frente a 134 mm/mes). Ambas muestran el evento de diciembre de 2024. No sabemos cuál se acerca más a la lluvia real: falta contrastar con estaciones IDEAM.
- **Predios pequeños:** columna `baja_confianza` (área < 0,1 ha; 849 predios).
English: "Only ~21 % of parcels are agricultural (cropland + grassland) according to ESA WorldCover 2021, so we flag them and report results both overall and for agricultural parcels. The difference between parcels inside and outside the irrigation district persists within grassland (mean vulnerability 0.26 vs 0.43), but remains an association. Monthly rainfall from GPM IMERG and ERA5-Land correlates at 0.88 (2021–2025); GPM is ~14 % lower on average, and both detect the December 2024 event. Station data (IDEAM) would be needed to tell which is closer to ground truth."

## E. Actualización 15-nov-2026 (tarde): prueba de sensibilidad aleatoria, suelo, EVA y qué NO está hecho
Actualiza los puntos 10 y 11 de la sección A.
- **Sensibilidad aleatoria (script `complementary_analysis.py`, tabla `tables/sensitivity_summary.csv`):** 1.000 combinaciones aleatorias de umbrales y pesos ±20 % (y peso de amenaza 0,4–0,6). La correlación de orden (Spearman) de la vulnerabilidad es ≥0,996 y la del riesgo ≥0,987; de los 100 predios más vulnerables se repiten entre 77 y 100. La etiqueta Alto va de 0 a 441 predios. Es una prueba distinta de la de la sección C (cambios de a uno); ambas dicen lo mismo: el orden es robusto, la etiqueta no.
- **Los 38 predios Alto no son una señal agronómica:** 36 tienen suelo desnudo como cobertura dominante (WorldCover 2021) y 36 miden menos de 0,1 ha (mediana 0,01 ha, marcados `baja_confianza`); 37 de 38 no son agropecuarios y ninguno está en el distrito. NO se interpretan como cultivos en estrés ni se explican como barbecho o erosión: no hay datos que lo respalden.
- **WorldCover frente a EVA:** WorldCover marca 359 ha de cultivo; EVA (UPRA) reporta 7.967 ha sembradas en 2024 y 6.146 ha en 2025 (preliminar). El mapa probablemente subestima el cultivo, o nuestros predios cubren solo parte del municipio (24.108 ha de 35.172 ha). EVA casi no cuenta pastos. EVA muestra saltos bruscos entre 2022 y 2023 (palma de aceite 255 → 1.300 ha; limón 71 → 831 ha); no sabemos la causa.
- **Suelo (punto 11):** se añadió arcilla superficial 0–5 cm de ISRIC SoilGrids (no es dato NASA) como capa de CONTEXTO: es global, de 250 m, una sola variable, y NO entra al riesgo. SoilGrids entrega g/kg; se divide entre 10 para obtener %. Valores 29–43 % (media ≈35 %): casi uniforme en la zona. Solo 1.180 de 1.848 predios únicos tienen valor (65 de los 386 agropecuarios no lo tienen); los sin valor son predios diminutos (mediana 0,01 ha), probablemente porque un polígono menor que un píxel de 250 m no devuelve dato. No se evalúa la salud del suelo (carbono orgánico, erosión, nutrientes).
- **Prioridades del agricultor: NO implementadas.** Los escenarios no se reordenan según prioridades. Cualquier lista de prioridades es una hipótesis por validar con técnicos y agricultores.
- **La herramienta no compara rotaciones por sí misma:** los 3 escenarios (`ROTATION_SCENARIOS_EN.md`) son evidencia citada cruzada con el calendario, con ventanas de cultivo supuestas. No hay simulación.
- **Dato NASA:** solo GPM IMERG V07. SMAP, MODIS (evapotranspiración), POWER e IDEAM quedan como trabajo futuro y no se usaron.
English: "The ranking is robust to 1,000 random ±20 % changes (Spearman ≥ 0.996 for vulnerability), but the High class is not (0–441 parcels). Thirty-six of the 38 High parcels are bare-soil-dominated lots under 0.1 ha, so we do not read them as crops under stress. A global 250 m soil-clay layer (ISRIC SoilGrids) is included as context only and is not part of the risk score. Farmer-priority weights and a parcel-level rotation simulation are not implemented in this version."
