# Repelón Risk Lens

**Environmental vulnerability screening and agricultural rotation exploration for Repelón, Atlántico, Colombia**

NASA Space Apps Challenge 2026 · *Field Shift: Adapting Farms with NASA Data*

**Live demo:** https://sasantos02.github.io/nasa-space-apps-repelon/

**Project guide:** [Methodology](#how-it-works) · [Results](#what-we-found) · [Rotation scenarios](#exploring-agricultural-alternatives) · [Limitations](LIMITATIONS.md) · [Data sources](#data-sources)

## 1. Project overview

Repelón Risk Lens is a transparent, rule-based prototype (no machine learning) designed to screen environmental vulnerability across **1,848 cadastral parcels** in Repelón, Atlántico, and explore alternative agricultural management scenarios.

The project combines rainfall observations from NASA GPM IMERG with vegetation indicators from Sentinel-2, cadastral boundaries, land-cover information and municipal agricultural statistics.

Within the 1,848-parcel dataset, approximately 386 parcels are classified as predominantly agricultural or grassland according to ESA WorldCover 2021. This distinction matters: environmental screening covers the full cadastral dataset, but agricultural interpretation requires additional caution and local validation.

The project addresses two connected questions:

1. **Where do satellite-derived indicators suggest environmental vulnerability?**
2. **How could alternative agricultural management strategies be explored under different rainfall conditions and priorities?**

Repelón Risk Lens does not automatically prescribe a crop or rotation for any parcel. Instead, it provides an initial screening tool and an exploratory environment for comparing alternatives.

## 2. How it works

The project follows four stages:

### 1. Observe — Understand environmental conditions

Cadastral boundaries provide the spatial framework for organizing parcel-level results.

Sentinel-2 vegetation indices describe vegetation greenness and moisture conditions, while NASA GPM IMERG provides rainfall estimates for examining recent precipitation against a historical reference.

Additional datasets, including ESA WorldCover, SoilGrids and municipal agricultural statistics, provide territorial and agricultural context.

### 2. Screen — Identify environmental vulnerability

The observed indicators are combined into a transparent rule-based index.

Vegetation indicators represent environmental vulnerability, while rainfall deficit represents climatic hazard. Their combination produces a screening score that helps identify parcels requiring closer examination.

Land-cover classifications and soil clay information provide supporting context. They do not establish actual crop identity or constitute a complete soil diagnosis.

### 3. Explore — Compare agricultural alternatives

The project includes three illustrative management scenarios:

- Current practice: extensive grazing.
- Alternative B: pasture combined with a dry-season forage reserve.
- Alternative C: short-cycle crops during the rainy season with soil cover during the dry season.

Each scenario includes its rationale, supporting evidence, assumptions, potential benefits and information gaps.

Users can modify rainfall assumptions, edit calendar months and adjust four illustrative priority weights. These controls change the relative ordering of scenarios using simple calendar-derived indicators.

They do not simulate crop growth, yields or farm profitability.

### 4. Interpret — Support informed local assessment

The results are intended to help identify conditions that deserve attention and questions that require further investigation.

The environmental screening and rotation scenarios are complementary components, not a fully integrated agronomic recommendation system.

Local producers, agricultural technicians and field information are necessary to evaluate whether a particular alternative is suitable for an individual parcel.

## 3. Methodology

All thresholds and weights are **uncalibrated assumptions** used to construct an exploratory screening index.

**Vegetation vulnerability (V)**

V = 0.4 × stress(NDVI) + 0.4 × stress(NDMI) + 0.2 × stress(SAVI)

The three indices are derived from Sentinel-2 imagery (ESA). The stress function compares observed values against predefined healthy and critical reference thresholds.

**Rainfall hazard (A)**

A = clip(1 − rainfall / normal rainfall, 0, 1)

The calculation uses a 60-day rainfall window from NASA GPM IMERG V07, compared with the same period in the previous ten years.

**Combined screening score (R)**

R = 0.5 × A + 0.5 × V

The score combines the rainfall hazard and vegetation vulnerability components.

The resulting classes are indicative, not validated agricultural risk categories. Their interpretation depends on the selected thresholds and weights.

## 4. What we found

**Results from the 15 November 2026 analysis — 1,848 unique parcels.**

| Indicator | Result |
|---|---:|
| Low / Moderate / High | 1,074 / 736 / 38 |
| Mean vulnerability inside the irrigation district | 0.29 |
| Mean vulnerability outside the irrigation district | 0.47 |
| Pasture-only vulnerability, inside / outside | 0.26 / 0.43 |
| Rainfall during the analyzed window | 96% of the 10-year normal |
| Vulnerability ranking robustness | Spearman ≥ 0.996 |
| Independent recalculation maximum difference | 0.0001 |
| GPM vs ERA5-Land monthly rainfall correlation (2021–2025) | 0.88 |

### How should these results be interpreted?

The sensitivity analysis indicates that the relative vulnerability ranking is robust to tested changes in thresholds and weights. However, the number of parcels classified as High varies substantially, from 0 to 441 under random ±20% changes.

Therefore, the ranking is more informative than treating the risk classes as definitive labels.

The 38 parcels classified as High require particular caution:

- 36 are dominated by bare-soil cover.
- 36 are smaller than 0.1 hectares and flagged as low confidence.
- 37 are classified as non-agricultural.

They should not be interpreted as 38 agricultural parcels experiencing crop stress.

The lower mean vulnerability observed inside the irrigation district is an association, not evidence that irrigation alone caused the difference. Being outside the district does not necessarily mean a parcel is rainfed.

Another important limitation is the difference between ESA WorldCover and UPRA agricultural statistics. WorldCover identifies substantially less cropland than the municipal planted-area figures reported by UPRA EVA. This indicates that land-cover classification and cadastral coverage require additional verification before drawing conclusions about agricultural land use.

## 5. Exploring agricultural alternatives

The project compares three illustrative scenarios to examine how different management calendars relate to the local rainfall pattern.

| Scenario | Main idea |
|---|---|
| A. Current practice | Extensive grazing |
| B. Forage reserve | Pasture combined with dry-season forage conservation |
| C. Seasonal cropping | Short-cycle crops during the rainy season and soil cover during the dry season |

The scenarios use local rainfall patterns, municipal agricultural statistics and supporting references to establish their context.

Their calendars and priority weights can be adjusted in the interactive application. The resulting scores are exploratory comparisons based on assumed calendar conditions.

**Important:** the project does not know the actual crop or rotation of each cadastral parcel. The scenarios are not parcel-specific agronomic recommendations and have not been validated with local farmers.

For the detailed assumptions, evidence and information gaps, see [Rotation scenarios](06_documentos/ROTATION_SCENARIOS_EN.md).

## 6. Exploring rainfall changes

The application includes rainfall what-if scenarios at:

- 100% of normal rainfall.
- 80% of normal rainfall.
- 60% of normal rainfall.

These scenarios scale the observed rainfall and recalculate the screening score while keeping vegetation vulnerability fixed.

They allow users to examine how lower rainfall could affect the screening results.

They are **not weather forecasts or climate projections**.

## 7. Alignment with the challenge

| Challenge element | Project contribution |
|---|---|
| NASA Earth observations | GPM IMERG V07 rainfall estimates |
| Local soil information | SoilGrids clay content as contextual information |
| Crop characteristics | Qualitative information from UPRA EVA and AGROSAVIA |
| Farmer priorities | Four adjustable illustrative weights, not survey-derived preferences |
| Rotation strategies | Three exploratory scenarios with editable calendars |
| Changing environmental conditions | Rainfall what-if analysis |
| Uncertainty and transparency | Sensitivity analysis, assumptions and documented limitations |

The project addresses these elements at prototype level. It does not claim to provide a complete agricultural decision-support system.

## 8. Data sources

**NASA**
- GPM IMERG V07 — precipitation estimates.

**Other Earth observation and environmental sources**
- Sentinel-2 — vegetation indices (ESA/Copernicus).
- ESA WorldCover 2021 — land-cover classification.
- ERA5-Land — rainfall cross-check (ECMWF).
- ISRIC SoilGrids — clay content, contextual information only.
- GOES-19 — visual context only; not integrated into the model.

**Agricultural and territorial information**
- UPRA EVA 2019–2025 — municipal planted-area statistics.
- Agricultural irrigation district registry (ADR).
- UPRA and ANT spatial information.
- Repelón cadastral parcel boundaries.

NASA GPM IMERG is the principal NASA dataset used in the current screening model. The other datasets provide complementary environmental, agricultural or territorial context.

## 9. Repository structure

- `02_cuaderno/` — Google Colab notebook and methodology guide.
- `03_salidas_finales/` — final parcel table, monthly calendar and example-parcel NDVI curve.
- `index.html`, `data.js`, `geo.js` — interactive web application.
- `complementary_analysis.py` — sensitivity analysis, rainfall scenarios and agricultural statistics.
- `tables/` and `figures/` — supporting analysis outputs.
- `01_entradas/` — input datasets.
- `04_historico/` — archived analysis runs.
- `05_evidencia/` — visual checks.
- `06_documentos/` — scenario documentation and supporting materials.
- `LIMITATIONS.md` — limitations, uncertainty and validation status.

**Note:** cadastral parcel codes contain 30 digits. Open CSV files as text or use Python; Excel may alter these identifiers.

## 10. Reproducing the analysis

1. Open the Google Colab notebook in `02_cuaderno/`.
2. Configure a Google Earth Engine project.
3. Run the notebook to produce the parcel-level outputs.
4. Run `python complementary_analysis.py` from the repository root to reproduce the complementary analyses.

## 11. Limitations and future work

The current prototype has not been validated with field measurements or parcel-level crop records.

Its principal limitations include uncalibrated thresholds, coarse rainfall resolution, incomplete land-cover representation, limited soil information and the absence of crop-growth or yield simulations.

Future development should prioritize:

1. Validation of scenario calendars and priority weights with local producers and agricultural technicians (UMATA).
2. Better parcel-level soil and crop information.
3. Comparison of rainfall estimates with IDEAM station observations.
4. A more defensible connection between parcel conditions and agricultural scenario suitability.

For a detailed account of uncertainty, sensitivity and validation, see [Limitations and observations](LIMITATIONS.md).

## 12. Use of AI

AI assistants supported the drafting of code and documentation. The project author defined the research question and methodology and reviewed the outputs through independent recalculation, visual checks, rainfall cross-comparison and sensitivity analysis.
