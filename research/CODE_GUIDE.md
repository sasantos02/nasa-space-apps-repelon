# Code Guide — Repelón Risk Lens

*A plain-English walkthrough of the code, its inputs, outputs, assumptions, and limits.*

## Start here: two related analyses, not one prediction

Repelón Risk Lens has **two separate analytical branches**:

```text
BRANCH 1 — TERRITORIAL SCREENING
Cadastral boundaries + CHIRPS rainfall + Sentinel-2 vegetation
  → rainfall hazard (A) + vegetation vulnerability (V)
  → environmental screening score (R)
  → parcel CSV/GeoPackage → data.js + geo.js → interactive map

BRANCH 2 — REGIONAL CROP-CLIMATE EXPLORATION
NASA POWER daily weather + assumed crop calendars and coefficients
  → reference evapotranspiration (ET0)
  → crop water demand (ETc = ET0 × Kc)
  → daily climatic shortfall (max[ETc − rainfall, 0])
  → six-crop comparisons + three sequential rotations
  → simulation CSVs + rotation_results.js → interactive explorer

SEPARATE OBSERVATIONAL CHECK
One IDEAM rain gauge compared with CHIRPS and GPM at its location
  → preliminary data-source comparison; not crop or parcel validation
```

**Do not connect the two branches with an invented formula.** The parcel screening score does not determine the best rotation for that parcel. The website places these complementary views side by side; its rainfall controls do not turn the regional crop calculations into field-specific predictions.

## Where the code lives

| File | What it does | Main result |
|---|---|---|
| [`research/Notebook_1_riesgo_territorial_chirps_v4_2.ipynb`](research/Notebook_1_riesgo_territorial_chirps_v4_2.ipynb) | Builds and checks the parcel-level environmental screening | Corrected territorial CSV and GeoPackage; browser map exports |
| [`research/Notebook_2_Rotaciones_6_Cultivos.ipynb`](research/Notebook_2_Rotaciones_6_Cultivos.ipynb) | Processes historical weather and compares crop water demand and sequential rotations | Six-crop and rotation CSVs; dashboard summaries |
| [`research/Notebook_3_validacion_ideam.ipynb`](research/Notebook_3_validacion_ideam.ipynb) | Audits a single station's observations and compares rainfall products | Preliminary station-level comparison CSV when executed |
| `index.html` | Presents the dashboard and explanations | Browser interface |
| `data.js`, `geo.js` | Provide parcel attributes and geometry | Interactive territorial map |
| `crop_results.js`, `rotation_results.js` | Supply precomputed crop/rotation display data | Interactive comparison panels |

The JavaScript dashboard works **without running Colab**. Notebooks are research code; they require external inputs and permissions to execute from scratch. See [`COLAB_REPRODUCIBILITY.md`](COLAB_REPRODUCIBILITY.md).

## Notebook 1 — From satellite imagery to a parcel screening map

**Question:** What environmental signals are visible across the mapped rural parcels?

1. **Configure the study.** The first code cell sets the Earth Engine project, Drive input paths, dates, cloud threshold, spatial scales, vegetation weights, and risk thresholds. The fixed rainfall study window is **September 16–October 31, 2026**, using **nine complete CHIRPS pentads**; the reference uses matching pentads from **2016–2025**.
2. **Load and clean cadastral geometry.** Reads `repelon_predios_rurales.gpkg`, removes exact duplicates, and, when the same cadastral code has different geometries, retains the largest. The notebook asserts **1,848 unique parcel codes**. This rule is a data-cleaning decision, not proof that other geometries were invalid.
3. **Extract vegetation indicators.** Uses Sentinel-2 surface reflectance, filters scenes by cloud percentage, and masks pixels using the **SCL classification band**. It derives **NDVI** (greenness), **NDMI** (vegetation moisture signal), and **SAVI** (vegetation index adjusted for soil background). It extracts parcel-level values with Earth Engine.
4. **Build vegetation vulnerability (`V_Vulnerability`).** Converts each vegetation index into a relative stress score between 0 and 1 using **assumed critical/healthy thresholds**. Combines them with weights **NDVI 0.4, NDMI 0.4, SAVI 0.2**. Higher vulnerability indicates less favorable vegetation signals under these assumptions, not a confirmed diagnosis of crop damage.
5. **Build rainfall hazard (`Amenaza_Norm`).** Compares CHIRPS rainfall in the study window against the corresponding historical reference period and normalizes the rainfall-based signal. `Precip_pct_normal` expresses observed rainfall relative to that reference; **it is not the final hazard score**. The detailed normalization is implemented in the notebook's section **“5. Amenaza”**.
6. **Combine the two scores.** `Riesgo_Index = 0.5 × Amenaza_Norm + 0.5 × V_Vulnerability`. The code classifies scores **≤0.25 Low**, **>0.25–0.50 Moderate**, **>0.50–0.75 High**, and **>0.75 Critical**. Weights and thresholds are provisional, not calibrated against observed crop losses.
7. **Add geographic context.** The later sections attach irrigation-district context, predominant **ESA WorldCover 2021** land cover, and **SoilGrids** surface clay estimates. These do **not** establish irrigation access or full soil suitability. The notebook flags parcels smaller than **0.1 ha** as lower-confidence cases.
8. **Export and verify.** Writes corrected territorial `CSV` and `GPKG` files and produces compact data for the browser. It asserts uniqueness, complete core scores, and expected parcel counts.

**Published outputs:** `research/outputs/territorial/repel_riesgo_consolidado_chirps_contexto_corregido.csv` and `.gpkg`. The map uses `data.js` and `geo.js` as packaged browser assets. **Published counts:** 858 Low, 579 Moderate, 411 High; 382 parcels flagged agricultural. **Interpretation warning:** 406 of 411 High parcels are below 0.1 ha, 395 are bare or built-up, and only 10 are agricultural. Switching rainfall products changed the High count substantially (CHIRPS 411 vs GPM 38); see [`LIMITATIONS.md`](LIMITATIONS.md).

### Worked example: how a screening score is obtained

Suppose a parcel has **rainfall hazard A = 0.20** and **vegetation vulnerability V = 0.76**. Then `R = 0.5 × 0.20 + 0.5 × 0.76 = 0.48`, which is **Moderate** under the notebook's thresholds. This is an **illustrative calculation, not a specific parcel record**. A displayed rainfall percentage such as “83.8% of normal” must first be converted through the notebook's hazard normalization; do **not** substitute `0.838` directly into the risk formula.

## Notebook 2 — From historical weather to crop and rotation comparisons

**Question:** Under the historical regional climate, how do different crop calendars compare in estimated climatic water shortfall?

This notebook contains **both earlier exploratory work and the final six-crop/three-rotation extension**. Its section numbering reflects its development history (for example, sections 13–14 precede some sections numbered 2–8); read the cells in **notebook order**, not numeric heading order.

1. **Read existing territorial context and configure the environment.** The notebook is designed to run independently of Notebook 1's Python memory, but it still expects specified Drive files and Earth Engine configuration.
2. **Get daily NASA POWER weather for 2018–2025.** Retrieves or reuses daily meteorological data, converts dates and numeric fields, and checks completeness.
3. **Estimate reference evapotranspiration (`ET0`).** Applies **FAO-56 Penman–Monteith** to approximate the atmosphere's daily evaporative demand. ET0 describes a reference surface, **not** the exact water need of a given crop.
4. **Apply crop coefficients (`Kc`).** Each crop has a provisional growing-cycle duration and stage-dependent Kc values. The notebook builds a daily Kc curve and calculates **`ETc = ET0 × Kc`**. ETc is the estimated crop water demand for that stage and climate, not observed field water use.
5. **Compare demand with rain.** For each day, computes **`max(ETc − rainfall, 0)`**; adds or averages daily values over the simulated crop cycle. This is a **climatic shortfall indicator**, not a soil-water balance: rain is not stored for later days, and runoff, drainage, effective irrigation and yields are not modeled.
6. **Retain earlier exploratory analyses.** The notebook also contains a hypothetical cassava water-exposure exercise, CHIRPS/NDVI calendar, GPM/ERA5-Land comparison, and an earlier **three-crop** (cassava/maize/sorghum) parameter sensitivity audit. Its CSVs are in `research/outputs/three_crop_audit/`. **Do not interpret those results as the six-crop comparison.**
7. **Simulate six crop profiles.** The final extension models **Maize (120 days), Sorghum (120), Cassava (210), Dry bean (100), Tomato (130), and Rice (120)**, using assumed stages and coefficients. It explores planting months, historical years and rainfall factors. The published file contains **1,662 complete crop-cycle simulations**.
8. **Simulate three sequential rotations.** A: **Maize → Dry bean → Cassava** (430 cropped days); B: **Sorghum → Tomato → Rice** (370); C: **Rice → Dry bean → Maize → Cassava** (550). Each successive crop begins after a **14-day unmodeled management gap**. A 24-month horizon is enforced. The published outputs include **162 complete rotation scenarios** and **540 crop segments**.
9. **Treat flooded rice separately.** The code adds an **illustrative extra water component** (200 mm saturation + 100 mm water layer + 6 mm/day × 120 days = **1,020 mm**) for rice scenarios. This is **not measured local irrigation** and is **not included in the regular climatic shortfall ranking**.
10. **Export traceable outputs.** The final cells write simulation CSVs, assumptions JSON and a compact `rotation_results.js` file for the dashboard.

**Published outputs:**

- `research/outputs/six_crop_rotations/six_crop_climate_scenarios.csv` — individual six-crop simulated cycles.
- `research/outputs/six_crop_rotations/three_rotations_24_months.csv` — rotation-level simulations.
- `research/outputs/six_crop_rotations/rotation_segments.csv` — each crop segment within a rotation.
- `research/outputs/six_crop_rotations/assumptions.json` — cited sources and model limitations.
- `rotation_results.js` — precomputed display summaries; **not a full simulation log**.

### Worked example: what Kc and ET0 mean

If **ET0 = 5 mm/day** and the crop's **Kc = 0.8**, then **ETc = 4 mm/day**. If that day has **2 mm of rain**, the modeled climatic shortfall is **2 mm**. The calculation does **not** establish that the plant actually lacked 2 mm: stored soil water or irrigation might have supplied it. This example is illustrative, not a recorded model row.

**How to read the rotations:** reported means are **per cropped day**, not per calendar day across two years. Different rotations occupy different numbers of days, so a lower average is **not** proof of a superior whole-farm strategy. Crop prices, disease, planting feasibility, labor, soil response and measured yields are not modeled.

## Notebook 3 — What the IDEAM check can and cannot establish

**Question:** Do two satellite rainfall products agree with one local station over a specified period?

1. **Load the original station file** `Precipitación_20261115.csv` from Drive. The notebook expects the station code, sensor code, timestamp, observation value, coordinates and unit columns.
2. **Audit observations.** Parses dates and decimal-comma values, preserves station identifiers as strings, checks missing or negative readings, and detects conflicting duplicate timestamps before deduplicating.
3. **Check temporal coverage.** Uses a **10-minute** expected observation interval for **September 16–October 31, 2026**, and requires at least **95%** coverage for the main comparison. The station total is meaningful **only if `ValorObservado` is incremental rainfall per interval**; the notebook explicitly flags this assumption for verification.
4. **Compare matching satellite periods at the station point.** Uses **CHIRPS V3 pentadal** rainfall and **NASA GPM IMERG** half-hourly rainfall in Earth Engine, checks coverage and converts GPM rainfall rate to accumulated millimeters for 30-minute steps.
5. **Export a preliminary comparison** to `validacion_ideam_chirps_gpm_punto_2026.csv` in the configured Drive folder, then inspects rainfall events and suspicious repeated values.

**Critical limits:** the committed Notebook 3 has **no saved execution outputs**, and its original IDEAM CSV is **not packaged**. Its comparison is preliminary and **does not validate parcel-level risk, crop suitability or yields**. Do not describe this as a completed, independently reproducible validation.

## How results reach the website

```text
Notebook 1 → corrected parcel data / geometries → data.js + geo.js ─┐
                                                                  ├→ index.html
Notebook 2 → six-crop and rotation CSVs → rotation_results.js ────┘
             earlier three-crop exports → crop_results.js (legacy)
Notebook 3 → station comparison output (research check only)
```

The published JavaScript assets are **already generated**. Opening the dashboard does not fetch NASA POWER, CHIRPS or Sentinel-2 anew, and does not rerun Python. The map's satellite **basemap imagery** requires internet access; the underlying parcel results are precomputed. The rainfall scenario slider is illustrative and should not be confused with a forecast or a rerun of the entire research pipeline.

## Spanish code: a short bilingual glossary

| In notebooks / exports | Meaning in English |
|---|---|
| `predios`, `CODIGO` | Cadastral parcels, parcel identifier |
| `precip_mm`, `precip_normal_mm` | Study-period rainfall, reference rainfall |
| `Precip_pct_normal` | Rainfall as percentage of historical reference |
| `Amenaza_Norm` | Normalized rainfall hazard |
| `V_Vulnerability` | Vegetation vulnerability score |
| `Riesgo_Index`, `Nivel_Riesgo` | Screening index, screening class |
| `cobertura_dominante` | Predominant land-cover category |
| `uso_agropecuario` | Agricultural-use screening flag |
| `ET0`, `Kc`, `ETc` | Reference evaporative demand, crop coefficient, estimated crop demand |
| `shortfall_mm_day` | Mean modeled climatic water shortfall per cropped day |
| `rain_factor` | Hypothetical multiplier applied to rainfall |

**Why Spanish?** The research notebooks were developed in the project's Colombian context. Their variable names and comments remain in Spanish to preserve the audited calculations. This English guide explains their purpose and outputs without renaming code or changing results.

## Reproduction and scientific boundaries

- **Website:** static and reviewable online; no Colab execution required.
- **Published simulation outputs:** supplied for independent CSV inspection, without rerunning Earth Engine.
- **Full notebook reruns:** not guaranteed from a new Google account. They refer to `/content/drive/MyDrive/Agro/`, an Earth Engine Cloud project, and original inputs that are not all included in the package. Read [`COLAB_REPRODUCIBILITY.md`](COLAB_REPRODUCIBILITY.md) before attempting a clean rerun.
- **Evidence:** this is a transparent, **rule-based exploratory prototype**, not a yield forecast, an agronomic recommendation, or a field-validated crop prescription. Read [`LIMITATIONS.md`](LIMITATIONS.md) and [`AUDIT.md`](AUDIT.md).
