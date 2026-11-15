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
- **Evidence:** EVA reports maize and cassava among the largest crops [CITED]; about 70 % of transitory sowing is in the first semester [CITED, own calculation]. UPRA's director recommends sowing soybean in rotation with rice or maize for soil reasons, as reported by Agronegocios (3 Nov 2023) [CITED, verified 15 Nov 2026]. This is a national statement tied to the soybean expansion in the Llanos Orientales: it is **not** evidence that soybean suits Repelón.
- **Benefits:** possible diversification [ASSUMPTION]; soil cover in the dry season is an [ASSUMPTION].
- **Information gaps:** soil, irrigation (the parcel is outside the district), seed, market, costs, yields.
- **Risks needing local review:** short-cycle crops are the most exposed to a shifting rain calendar [CITED: Contexto Ganadero]; water access is unknown.

## Parcel counts used in the explorer
"Agricultural" = ESA WorldCover cropland + grassland ≥ 50 % of the parcel: **386 unique parcels** (343 grassland-dominated, 39 cropland-dominated, 3 tree-dominated and 1 shrub-dominated). The other 1,462 parcels are non-agricultural or of uncertain use: their score is shown as an environmental reading, not as crop stress.

## The four priority controls (all assumptions)
Each editable calendar gets four scores from 0 to 1; the sliders weight them. They are simple shares, not yield or income models.
1. **Low dry-season water exposure** = 1 − (water-needing months that are dry ÷ water-needing months). Water-needing = pasture, pasture + reserve or crop; a month is dry if the scaled monthly rain is below 50 mm.
2. **Dry-season feed (reserve)** = dry months with reserve feed ÷ dry months.
3. **Soil covered** = 1 − fallow months ÷ 12 (the only proxy for soil health here).
4. **Sowing with the rains** = crop months that are not dry ÷ crop months (0 if the plan has no crop).
The page repeats the ranking under 300 random slider settings. If one scenario leads, that comes from how the calendars are defined (B combines reserve feed and a crop window), not from field evidence.

## Not covered and important limitations
Farmer priorities are partially implemented through four adjustable weights that re-rank the three scenarios. These weights are illustrative assumptions, not preferences collected through farmer surveys, and have not been validated with local producers or technicians.

The tool does not simulate crop growth, yields, income, nutrient cycling or long-term soil-health changes. Soil organic carbon, erosion and nutrient availability are not assessed. Actual crops and rotations at parcel level are unknown. The scenarios are exploratory comparisons to support discussion and local assessment, not agronomic recommendations.

## Sources (the Agronegocios link was opened and checked; confirm the wording of the two Contexto Ganadero links before submitting)
- UPRA, Evaluaciones Agropecuarias Municipales (EVA) 2019–2025, file in `01_entradas/`.
- Contexto Ganadero, silage of sorghum and maize for Atlántico livestock producers (AGROSAVIA): https://www.contextoganadero.com/ganaderia-sostenible/ganaderos-del-atlantico-reciben-silo-de-sorgo-y-maiz-para-sus-animales
- Contexto Ganadero, agricultural cycles and the changing calendar: https://www.contextoganadero.com/agricultura/ciclos-agropecuarios-ya-no-obedecen-al-calendario-cambio-climatico-altera-siembras-y-aumenta-incertidumbre-en-el-campo
- Agronegocios (3 Nov 2023), transitory-crop sown area, first semester 2023, with UPRA's soybean-with-rice-or-maize recommendation: https://www.agronegocios.co/agricultura/hectareas-sembradas-de-cultivos-transitorios-primer-semestre-de-2023-3742827
- UPRA, Microanálisis de evaluaciones agropecuarias 2023, Atlántico.
