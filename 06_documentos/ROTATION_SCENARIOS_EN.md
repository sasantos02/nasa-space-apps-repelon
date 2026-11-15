# Rotation scenarios for the example parcel (screening, not a recommendation)
Parcel 086060003000000010286000000000. Tags: **[OWN DATA]** computed in this project · **[CITED]** from a source listed at the end · **[ASSUMPTION]** declared, requires local review. No yields, varieties or sowing dates are given because there is no source. We do not name a winner.

**Parcel facts [OWN DATA]:** 53 ha; 88.8 % pasture (ESA WorldCover 2021); outside the irrigation district (9.6 km from the ADR reference point); NDVI 0.399, NDMI −0.137, SAVI 0.225; vulnerability 0.763; risk 0.489 (Moderate, 0.011 below the High cut-off).
**Calendar [OWN DATA, GPM IMERG and Sentinel-2, 2021–2025]:** dry season Dec–Mar (13–34 mm/month); April 106 mm; May–Nov 119–208 mm with a dip in July. Parcel NDVI is lowest in March–April (0.34 and 0.32) and recovers to 0.74 in June. Zone-mean NDVI minimum is 0.47 (March–April).
**Rainfall what-if [OWN DATA, not a forecast, vulnerability fixed]:** at 100 / 80 / 60 % of normal rain, this parcel's risk is 0.382 / 0.482 / 0.582 (Moderate / Moderate / High). Across the 1,848 parcels, High goes 0 → 420 → 597.
**Context [CITED, own calculation on UPRA EVA]:** about 70 % of the transitory-crop sown area in Repelón falls in the first semester (2021–2025). EVA reports maize, cassava, oil palm, lemon, plantain and yam as the main crops in 2024.
**Soil [OWN DATA, context only]:** the global SoilGrids layer gives clay ≈ 35 % (range 29–43 %) across the zone and 35.8 % at this parcel; it is too uniform and too coarse (250 m) to separate parcels, and it is not in the risk score.

## A. Current practice: extensive grazing
- **Why:** land cover suggests pasture [OWN DATA]; that it is grazed is [ASSUMPTION] (no per-parcel land-use data).
- **Evidence:** NDVI drops in March–April [OWN DATA]; dry-season forage shortages are a known issue for livestock producers in Atlántico [CITED: AGROSAVIA / Contexto Ganadero].
- **Benefits:** no investment or change in labour [ASSUMPTION].
- **Information gaps:** stocking rate, water access, soil, actual use.
- **Risks needing local review:** feed shortage and exposed soil in Dec–Apr [OWN DATA: dry season]. Months of the year below 50 mm: 4 of 12 (33 %) [OWN DATA].

## B. Pasture plus dry-season forage reserve (silage)
- **Why:** keeps the current land use and targets the dry months [ASSUMPTION].
- **Evidence:** AGROSAVIA delivered forage sorghum JJT-18 and maize Corpoica V114 silage to Atlántico producers for the dry season [CITED: Contexto Ganadero].
- **Benefits:** dry-season feed security [CITED]; lower exposure of bare ground [ASSUMPTION]. It does not change the pasture's own water exposure [OWN DATA reasoning].
- **Information gaps:** area needed, water for the forage crop, costs, yields on this parcel.
- **Risks needing local review:** establishment depends on rain: at 60 % of normal rain the parcel reaches High (0.582) [OWN DATA what-if].

## C. Short-cycle crop in the rainy season, cover in the dry season
- **Why:** uses the calendar (rain Apr–Nov, dry Dec–Mar) [OWN DATA]. Maize, cassava, yam and beans are traditionally sown at the start of the rains, late April to May [CITED: Contexto Ganadero]. The crop window May–August is an [ASSUMPTION]; sown at that window, 0 of its months are below 50 mm [OWN DATA], which is largely a consequence of the window we chose.
- **Evidence:** EVA reports maize and cassava among the largest crops [CITED]; about 70 % of transitory sowing is in the first semester [CITED, own calculation]. A legume rotation with cereals is recommended by UPRA as reported by Agronegocios [CITED, to verify].
- **Benefits:** possible diversification [ASSUMPTION]; soil cover in the dry season is an [ASSUMPTION].
- **Information gaps:** soil, irrigation (the parcel is outside the district), seed, market, costs, yields.
- **Risks needing local review:** short-cycle crops are the most exposed to a shifting rain calendar [CITED: Contexto Ganadero]; water access is unknown.

## Not covered (declared)
Farmer priorities are not implemented in this version (planned as adjustable weights). Typical priorities (dry-season water risk, dry-season feed, soil cover, sowing timing) are hypotheses to validate with local technicians and farmers, not findings. Soil health (organic carbon, erosion, nutrients) is not assessed.

## Sources (open each link and confirm the wording before submitting)
- UPRA, Evaluaciones Agropecuarias Municipales (EVA) 2019–2025, file in `01_entradas/`.
- Contexto Ganadero, silage of sorghum and maize for Atlántico livestock producers (AGROSAVIA): https://www.contextoganadero.com/ganaderia-sostenible/ganaderos-del-atlantico-reciben-silo-de-sorgo-y-maiz-para-sus-animales
- Contexto Ganadero, agricultural cycles and the changing calendar: https://www.contextoganadero.com/agricultura/ciclos-agropecuarios-ya-no-obedecen-al-calendario-cambio-climatico-altera-siembras-y-aumenta-incertidumbre-en-el-campo
- Agronegocios, transitory-crop sown area, first semester 2023: https://www.agronegocios.co/agricultura/hectareas-sembradas-de-cultivos-transitorios-primer-semestre-de-2023-3742827
- UPRA, Microanálisis de evaluaciones agropecuarias 2023, Atlántico.
