# Repelón Risk Lens
**Parcel-level agroclimatic risk and rotation scenarios for Repelón (Atlántico, Colombia)**
NASA Space Apps Challenge 2026 · *Field Shift: Adapting Farms with NASA Data*

**Live demo:** https://sasantos02.github.io/nasa-space-apps-repelon/  
**Start here:** [How it works](#how-it-works) · [Results](#results) · [Limitations](main/LIMITATIONS.md) · [Rotation scenarios](06_documentos/ROTATION_SCENARIOS_EN.md) · [Notebook guide](02_cuaderno/NOTEBOOK_GUIDE_EN.md)

## What it is
Repelón Risk Lens is a transparent, rule-based (no machine learning) prototype for **screening environmental vulnerability across 1,848 unique rural parcels** and exploring crop-rotation alternatives in Repelón, Atlántico. It combines rainfall from NASA GPM IMERG with vegetation indicators from Sentinel-2, cadastral parcel boundaries, land-cover context and municipal agricultural statistics.

The tool connects two tasks: **(1) observe and screen environmental conditions at parcel level; (2) explore three illustrative management scenarios**—the current-practice baseline and two alternatives—using editable calendars and adjustable priority weights. Each scenario states its evidence, assumptions, information gaps and risks requiring local review.

**What it is not:** it does not identify the actual crop or rotation on each parcel, simulate yields or income, measure complete soil health, forecast weather, or identify a universally best rotation. Its scenario scores are calendar-based exploratory indicators, not agronomic predictions or farmer-survey results. It supports, but does not replace, farmers and local technicians.

## How it works
1. **Observe:** use cadastral boundaries to organize parcel-level outputs; use Sentinel-2 indices to describe vegetation greenness/moisture and NASA GPM IMERG to compare recent rainfall with a historical reference.
2. **Screen:** combine vegetation vulnerability and rainfall deficit in a transparent rule-based index. Land-cover labels and SoilGrids clay are supporting context, not proof of crop identity or a complete soil diagnosis.
3. **Explore:** compare three illustrative management calendars. Users can change rainfall assumptions, edit calendar months and adjust four priority weights to see how the scenario ordering changes.
4. **Interpret carefully:** consult the limitations and scenario notes before treating any result as a basis for field decisions.

**Important reading:** [Limitations and uncertainty](06_documentos/LIMITATIONS.md) · [Rotation scenarios and their assumptions](06_documentos/ROTATION_SCENARIOS_EN.md).

## Method (all thresholds and weights are uncalibrated assumptions)
- **Vulnerability** V = 0.4·stress(NDVI) + 0.4·stress(NDMI) + 0.2·stress(SAVI), from Sentinel-2 (ESA), stress = clip((healthy − x)/(healthy − critical), 0, 1).
- **Hazard** A = clip(1 − rain / normal, 0, 1): 60-day rainfall (NASA GPM IMERG V07) against the same window in the previous 10 years.
- **Risk** R = 0.5·A + 0.5·V. Classes: Moderate > 0.25, High > 0.50, Critical > 0.75, otherwise Low.

## Results (run of 2026-11-15, 1,848 unique parcels)
| | Result |
|---|---|
| Low / Moderate / High | 1,074 / 736 / 38 |
| Mean vulnerability inside / outside the irrigation district | 0.29 / 0.47 (pasture-only parcels: 0.26 / 0.43) |
| Rainfall in the window | 96 % of the 10-year normal |
| Ranking robustness (1,000 random ±20 % changes of thresholds and weights) | Spearman ≥ 0.996 for vulnerability; **High class count ranges 0–441** |
| Independent recalculation of all parcels | max difference 0.0001 |
| GPM IMERG vs ERA5-Land monthly rainfall (2021–2025) | correlation 0.88; GPM ≈ 14 % lower |

**Read this first (what we can and cannot claim)**
- The **ranking** is stable; the **High label is not**, and it is mostly an artifact: 36 of the 38 High parcels are dominated by bare-soil cover (ESA WorldCover 2021) and 36 are tiny lots (< 0.1 ha, flagged `baja_confianza`); 37 of 38 are non-agricultural. We do **not** interpret them as crops under stress.
- The irrigation-district contrast is an **association, not causation**; "outside the district" does not mean rainfed.
- The model cannot distinguish crops from woodland, pasture or bare soil; high NDVI does not mean a healthy crop.
- ESA WorldCover marks only 359 ha as cropland, versus 6,146–7,967 ha planted according to UPRA EVA (2025–2024): the cover map likely underestimates cropland, or our parcels cover only part of the municipality (24,108 ha of 35,172 ha).
- No field validation. No parcel-level crop data.

## Rotation scenarios
See [`06_documentos/ROTATION_SCENARIOS_EN.md`](06_documentos/ROTATION_SCENARIOS_EN.md). Every statement is tagged **[OWN DATA]**, **[CITED]** or **[ASSUMPTION]**. Includes a what-if rainfall table (100 / 80 / 60 % of normal): High parcels go 0 → 420 → 597. This is *not* a forecast.

## Alignment with the challenge brief
| Brief element | Status |
|---|---|
| NASA Earth observations | **Covered, thin:** GPM IMERG V07 only (~11 km, so hazard varies little between parcels; Sentinel-2 drives the ranking) |
| Local soil information | **Partial:** ISRIC SoilGrids clay 0–5 cm, global 250 m (not local), context only, not in the risk score; 1,180 of 1,848 unique parcels have a value (tiny parcels return none) |
| Crop characteristics | **Partial:** qualitative, from cited sources (UPRA EVA, AGROSAVIA); no crop parameters |
| Farmer priorities | **Partial:** four adjustable illustrative weights re-rank three scenarios using calendar-derived indicators; they are not farmer-survey data and have no field validation |
| Explore rotation strategies | **Partial:** 3 scenarios with assumptions; a calendar-overlap reading; no simulation |
| Adapt to changing conditions | **Covered at screening level:** rainfall what-if scenarios |
| Make uncertainty visible | **Covered:** sensitivity test, limitations, labelled assumptions |

## Data sources
- **NASA:** GPM IMERG V07 (rainfall).
- **Other agencies/providers (not NASA):** Sentinel-2 and ESA WorldCover 2021 (ESA/Copernicus); ERA5-Land (ECMWF), rainfall cross-check only; ISRIC SoilGrids (soil clay, context only); GOES-19 imagery (NOAA), visual context only, not in the model; UPRA EVA 2019–2025 (planted area); irrigation district registry (ADR) and polygon (UPRA, ANT); Repelón cadastre.

## Repository map
- `02_cuaderno/` Colab notebook (Earth Engine) that produces the results.
- `03_salidas_finales/` final parcel table (`predios_para_demo_2026-11-15.csv`), monthly calendar, example-parcel NDVI curve.
- `index.html`, `data.js`, `geo.js` interactive map (parcel polygons from the cadastral layer, Esri imagery base map, rainfall what-if, editable rotation calendars and four illustrative priority sliders).
- `complementary_analysis.py` → `tables/` (sensitivity, rain what-if, EVA by crop); `figures/` (risk map, district contrast, monthly calendar, rainfall scenarios).
- `01_entradas/` inputs (district tables, EVA); `04_historico/` archived comparison runs; `05_evidencia/` visual checks; `06_documentos/` public methodology, limitations and scenario documentation.
- Parcel codes have 30 digits: open the CSVs as text or with Python (Excel corrupts them).

## Reproduce
Run the notebook in Google Colab with an Earth Engine project, then run `python complementary_analysis.py` from the repository root.

## Use of AI
Code and documentation were drafted with AI assistants. The author defined the question and method and verified the results (independent recalculation, visual checks, ERA5-Land cross-check, sensitivity test).
## Next steps
1. Validate the illustrative calendars and priority weights with farmers and local technicians (UMATA), and develop a defensible link between parcel conditions and scenario suitability.
2. Improve local soil and crop information (e.g., IGAC records and parcel-level field data); compare rainfall with IDEAM stations.
3. Evaluate additional Earth-observation layers (e.g., SMAP, MODIS or NASA POWER). They are not used in this version.
