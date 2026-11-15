# Limitations and observations (as of 15 Nov 2026)

Each item says what we know, what we cannot claim, and what would be needed. We present this as transparency about uncertainty, which is what the challenge asks for.

## What we can claim with confidence
- The calculation is reproducible and matches an independent recalculation of all parcels (max difference 0.0001).
- Irrigation-district parcels are systematically greener and less vulnerable (mean vulnerability 0.29 inside vs 0.47 outside; 0.26 vs 0.43 within grassland only). This is an association, not causation.
- The **ranking** of parcels is robust to ±20 % changes in thresholds and weights (Spearman ≥ 0.98; ≥ 0.996 for vulnerability in 1,000 random trials).
- The tool shows where local expertise is needed first; it does not replace it.

## Model and thresholds
1. **Thresholds and weights are uncalibrated assumptions.** Ranking is stable across two very different seasons (correlation 0.91); the Low/Moderate/High cut-offs are not validated. Needed: calibration with field data or local technicians.
2. **The "High" class is unstable.** A one-day shift in the 60-day window moved parcels across a cut-off (259 → 38 High). Under random ±20 % changes, High ranges from 0 to 441 parcels. We treat the ranking as the main output and the classes as indicative.
3. **The 38 High parcels are not an agronomic signal.** 36 are bare-soil-dominated lots under 0.1 ha (median 0.01 ha, flagged `baja_confianza`); 37 of 38 are non-agricultural and none is in the district. We do not read them as crops under stress.

## Data
4. **Indices measure greenness and moisture, not land use.** Visual checks showed the "greenest" parcels are mostly woodland and one "driest" is built-up land beside a sports field. ESA WorldCover 2021 (modelled, 10 m) is used as a supporting label: only about 21 % of parcels (386 of 1,848) are agricultural (cropland + grassland ≥ 50 % of area); 343 of them are grassland and 39 cropland. This is a label, not field truth.
5. **WorldCover vs EVA.** WorldCover marks 359 ha of cropland; UPRA EVA reports 7,967 ha planted in 2024 and 6,146 ha in 2025 (preliminary). The cover map probably underestimates cropland, or our parcels cover only part of the municipality (24,108 of 35,172 ha). EVA shows abrupt 2022→2023 jumps (oil palm 255 → 1,300 ha; lemon 71 → 831 ha) that we cannot explain.
6. **Clouds and haze.** Sentinel-2 scenes are filtered by cloud percentage and pixels are masked with the SCL band (only vegetation and bare-soil classes are used; clouds, shadows and water are excluded). We did not measure how many pixels each parcel lost, so residual haze or shadow may bias individual parcels. The satellite image in the web map (Esri) is only a visual base layer: it is from a different date than the calculation and does not enter the model.
7. **Small parcels are low-confidence.** About a quarter measure 0.01 ha or less; the 10 m pixel is large relative to them (849 parcels under 0.1 ha are flagged). 961 parcels measure 1 ha or more. In the web map, tiny lots are drawn as a minimum-size square only so they can be clicked.
8. **Rainfall resolution is coarse.** GPM IMERG pixels are about 11 km, so hazard varies little between parcels (305–383 mm in the window); vulnerability carries most of the spatial contrast.
9. **Dry-season "normal" rainfall is highly variable** (9.6–72 mm for Dec–Mar over ten years). One December 2024 event (112.6 mm in a month) explains why a March run showed "551 % of normal" and zero hazard. Explained and kept as a dry-season contrast.
10. **GPM vs ERA5-Land.** Monthly rainfall correlates at 0.88 (2021–2025); GPM is about 14 % lower on average (115 vs 134 mm/month); both capture December 2024. We do not know which is closer to ground truth: no IDEAM station comparison yet.
11. **Soil is context only.** ISRIC SoilGrids clay 0–5 cm (global, 250 m, one variable; not NASA data) is shown but is not part of the risk score. Values 29–43 % (mean about 35 %); 1,180 of 1,848 unique parcels have a value (tiny polygons return none). Soil health (organic carbon, erosion, nutrients) is not assessed. No temperature layer.
12. **Irrigation district = association.** Membership uses the parcel centroid against a negative-buffer layer; edge parcels may differ slightly. "Outside the district" does not mean rainfed.
13. **Data quality.** 9 duplicate parcel codes (one kept). Excel corrupts 30-digit codes: open the CSVs as text.

## Rotation scenarios and the web tool
14. **No parcel-level crop or rotation data are public.** The three rotation scenarios (A current grazing, B pasture + forage reserve, C short-cycle crop + cover) are cited evidence crossed with the monthly rainfall calendar, with assumed crop windows. There is no yield, income or crop-growth simulation.
15. **Farmer priorities are partially implemented.** The page has four adjustable priority sliders (low dry-season water exposure, dry-season feed, soil cover, sowing with the rains) that re-rank the three scenarios, plus a 300-random-weights test. Scores are simple shares computed from the editable calendars, and "dry month" (< 50 mm) is an assumption. Which scenario leads depends largely on how the calendars are defined, so the result reflects our assumptions, not field evidence. Priorities themselves are hypotheses to validate with technicians and farmers.
16. **Dry-season exposure index.** A separate analysis (`07_indice_exposicion`) compares when planting falls relative to dry months. It is built on assumed crop cycles and is not a forecast.
17. **Rainfall what-if scenarios are not forecasts.** The page scales the observed rainfall (100 / 80 / 60 % of normal) and recomputes risk; vulnerability stays fixed.

## Validation
18. **Limited validation.** Independent recalculation of all parcels, a sensitivity analysis, a GPM–ERA5 cross-check, and a visual check of 10 parcels by one person using Google imagery that may be from another date. This shows coherence, not statistical accuracy. No field data and no IDEAM comparison.

## Sensitivity summary (one-at-a-time changes, 1,848 unique parcels)
| Change | Spearman rank correlation | Parcels changing class | Overlap in riskiest 10 % | Resulting High |
|---|---|---|---|---|
| Stricter thresholds (+20 % of range) | 0.994 | 34 % | 65 % | 373 |
| Looser thresholds (−20 %) | 0.987 | 16 % | 87 % | 0 |
| NDVI/NDMI/SAVI weights 0.5/0.3/0.2 | 0.999 | 3 % | 97 % | 45 |
| Weights 0.3/0.5/0.2 | 0.999 | 3 % | 94 % | 36 |
| Equal weights | 1.000 | 2 % | 93 % | 26 |
| Hazard weight 0.3 (instead of 0.5) | 0.995 | 34 % | 98 % | 488 |
| Hazard weight 0.7 | 0.981 | 19 % | 89 % | 0 |

Reading: the ordering is very stable; the levels depend heavily on where the cut-offs are placed.

## Data sources and AI use
NASA: GPM IMERG V07 (rainfall). Not NASA: Sentinel-2 and WorldCover (ESA/Copernicus), ERA5-Land (ECMWF), SoilGrids (ISRIC), EVA (UPRA/Agronet), district registry (ADR), UPRA and ANT polygons, Esri imagery (map base layer only). SMAP, MODIS evapotranspiration, NASA POWER and IDEAM stations are future work and were not used. GOES was downloaded but not integrated. AI tools helped draft code and text; the author defined the method and reviewed the results.
