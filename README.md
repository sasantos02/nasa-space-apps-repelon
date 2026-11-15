# Repelón Risk Lens

**Explore environmental vulnerability and crop-rotation scenarios in Repelón, Atlántico, Colombia.**  
NASA Space Apps Challenge 2026 — *Field Shift: Adapting Farms with NASA Data*

**Live demo (after publishing this package):** https://sasantos02.github.io/nasa-space-apps-repelon/

> **Research prototype, not a crop prescription.** Parcel-level environmental screening and regional crop-climate scenarios are two complementary analyses at **different spatial scales**. The tool does not predict yields, diagnose crop damage, or confirm that a proposed rotation is suitable for a specific field.

<img width="2800" height="1257" alt="Diagram" src="https://github.com/user-attachments/assets/8e3d383e-6a5c-4b0f-8390-2b57bd520a6a" />

## Try the interactive explorer

Open **`index.html`** in a browser, keeping `data.js`, `geo.js`, `crop_results.js`, and `rotation_results.js` in the **same directory**. The parcel data and boundaries load locally; the satellite basemap needs internet access. For publication, upload these five files to the **root of the existing GitHub Pages repository**. Do not upload the ZIP itself as the website. No build step, backend, API key or machine-learning model is needed.

The interface lets visitors select a parcel, filter to flagged agricultural parcels, inspect a transparent environmental screening score, vary an **illustrative** rainfall setting, compare **six** crop-climate profiles by planting month, and examine **three hypothetical two-year rotations**. Rainfall controls for the map and the crop comparison represent **separate** calculations; moving one does not recalibrate the other.

## What the project actually analyzes

### 1. Territory: environmental screening

- **1,848 unique cadastral parcels**; the latest data export flags **382** as agricultural using the project's screening flag. This is **not** a census of active farms. All 1,848 geometries are present in the interactive map.
- **CHIRPS v3** pentadal rainfall provides the rainfall component of the latest territorial model. **Sentinel-2** NDVI, NDMI and SAVI provide vegetation signals; **ESA WorldCover 2021** describes predominant land cover; **SoilGrids** clay percentage is context, not a complete soil suitability test.
- The prototype computes a rule-based index, **R = 0.5 × A + 0.5 × V**, where **A** is normalized relative rainfall hazard and **V** is vegetation vulnerability. Both the weights and class thresholds are **uncalibrated assumptions**, not validated crop-loss probabilities.
- Latest export: **858 Low, 579 Moderate, 411 High**. High screening scores do not automatically imply agricultural damage: small parcels, bare ground, and nonagricultural land can also receive high scores.
- Irrigation-district intersection is contextual only: being inside a mapped district **does not prove that irrigation is available**. Any distance-to-district-reference figure is a distance to an **ADR reference point**, not the district boundary.

### 2. Regional climate: six crop profiles

**NASA POWER** daily meteorology is used to estimate reference evapotranspiration (**ET0**). Provisional crop coefficients (**Kc**) define crop evapotranspiration (**ETc = Kc × ET0**). The exploratory daily climatic shortfall is **max(ETc − daily rainfall, 0)**, averaged across each modeled crop cycle.

| Crop | Assumed cycle | Botanical family |
|---|---:|---|
| Maize | 120 days | Poaceae |
| Sorghum | 120 days | Poaceae |
| Cassava | 210 days | Euphorbiaceae |
| Dry bean (generic, not confirmed local cowpea) | 100 days | Fabaceae |
| Tomato | 130 days | Solanaceae |
| Flooded rice (illustrative) | 120 days | Poaceae |

The displayed six-crop baseline covers **12 planting months**. It is not a parcel-specific water balance: the model does not carry soil-water storage between days, nor model runoff, effective rainfall, irrigation delivery, drainage or yield.

**Example: April planting, historical baseline (mean modeled shortfall in mm/day):** Cassava **1.109**, Sorghum **1.593**, Dry bean **1.714**, Maize **1.922**, Tomato **1.957**, Rice **2.930**. Lower modeled shortfall does **not** establish higher yields or suitability. The earlier **three-crop sensitivity experiment** is retained separately and its percentages must not be interpreted as six-crop probabilities.

### 3. Three candidate 24-month crop sequences

The rotations below are **proposed scenarios**, not documented farm practices or validated local rotation calendars. Each crop follows the previous crop on one hypothetical field, with an assumed **14-day unmodeled management interval**. A crop sequence alone does not establish pest control, soil improvement or economic feasibility.

| Scenario | Sequence | Modeled crop days | Botanical families | Mean modeled shortfall per cropped day | Additional flooded-rice water assumption |
|---|---|---:|---:|---:|---:|
| A | Maize → Dry bean → Cassava | 430 | 3 | 1.941 mm/day | None |
| B | Sorghum → Tomato → Rice | 370 | 2 | 2.746 mm/day | 1,020 mm per rice cycle |
| C | Rice → Dry bean → Maize → Cassava | 550 | 3 | 2.123 mm/day | 1,020 mm per rice cycle |

The summary uses **18 complete historical baseline simulations per sequence**. The notebook reports **162 rotation simulations** across baseline and rainfall perturbations (54 per sequence), and **1,662 complete six-crop simulations** across crops, years, months and rainfall factors. The `rotation_results.js` shipped here contains **aggregated display results**. The corresponding **full per-simulation CSVs** are now included under `research/outputs/six_crop_rotations/`.

**Crucial comparison caveat:** A/B/C have different numbers of cropped days; a lower **per-cropped-day** shortfall does not mean a better whole-farm rotation. The flooded-rice scenarios include a separate **illustrative 1,020 mm** water component (200 mm saturation + 100 mm water layer + 6 mm/day × 120 days), **excluded from the shortfall score**. Water delivery, local rice system, crop feasibility and actual irrigation are unknown. No definitive winner is claimed.

## Evidence and validation status

- **IDEAM station vs CHIRPS/GPM:** Notebook 3 conducts a preliminary comparison of rainfall estimates, **not** a calibration of parcel risk or crop yields. Rain-gauge accumulation semantics, pixel-versus-point representativeness and gaps require caution.
- **EVA municipal agricultural records (2006–2025):** provide local crop-production context, not proof that the modeled crop sequences are practiced on any particular farm. The audited dataset retains source-data quality flags.
- **Agronomic parameters:** FAO reference materials motivate the exploratory Kc and rice assumptions, but crop stage lengths and Kc have **not been locally calibrated**. Generic dry bean must not be presented as verified local cowpea.
- **Robustness:** the earlier three-crop analysis varied Kc, crop duration and rainfall; its findings **do not establish robustness of the six-crop rotations**.
- **Field validation:** no producer interviews, verified crop calendars, irrigation records, soil-moisture observations or measured yields have been used to validate the proposed sequences.

See [AUDIT.md](AUDIT.md) for package checks and unresolved verification, and [LIMITATIONS.md](LIMITATIONS.md) for a concise scientific disclosure.

## Reproducibility and files

```text
index.html                Interactive dashboard (GitHub Pages entry point)
data.js                   1,848 parcel screening records
geo.js                    Parcel geometries
crop_results.js           Legacy three-crop sensitivity display
rotation_results.js       Six-crop and three-rotation display summaries
research/                 Three current notebooks (Colab)
data/                     Audited small CSVs for traceability
README.md                 This guide
LIMITATIONS.md            Scientific boundaries
AUDIT.md                  Data/UI consistency checks and open items
```

Notebook 1 reconstructs the territorial screening; Notebook 2 models NASA POWER crop scenarios and sequential rotations; Notebook 3 compares IDEAM station rainfall with satellite products. The notebooks reference data stored in the original Colab/Drive workspace; **this GitHub package is a runnable website and research record, not a fully self-contained rerun of the raw data pipeline**. The original raw IDEAM (~41 MB) and original cadastral GeoPackage were not bundled; the corrected territorial GeoPackage and full six-crop/rotation outputs **are included** under `research/outputs/`. Re-running Notebook 2 with its original Drive inputs exports `six_crop_climate_scenarios.csv`, `three_rotations_24_months.csv`, `rotation_segments.csv`, `assumptions.json` and `rotation_results.js`.

## Primary reference materials

- NASA POWER: https://power.larc.nasa.gov/
- CHIRPS: https://www.chc.ucsb.edu/data/chirps
- Copernicus Sentinel-2: https://dataspace.copernicus.eu/
- ESA WorldCover: https://esa-worldcover.org/
- ISRIC SoilGrids: https://soilgrids.org/
- FAO crop water requirements and Kc reference: https://www.fao.org/4/s2022e/s2022e07.htm
- FAO rice irrigation reference: https://www.fao.org/4/s2022e/s2022e08.htm
- IDEAM (Colombia): https://www.ideam.gov.co/
- UPRA EVA: https://upra.gov.co/

**Responsible use:** This is an explainable educational decision-support prototype. Local agronomic expertise and farmer input are required before adopting any rotation.

## Supplementary research exports (November 15, 2026)

The `research/outputs/territorial/` folder contains the **full corrected territorial CSV and GeoPackage** (1,848 records each). The CSV is a tabular export; the GeoPackage preserves parcel geometries. These files are provided for traceability and are not required for the browser demo, which reads `data.js` and `geo.js`.

The `research/outputs/three_crop_audit/` folder contains five original CSV exports from the **earlier maize/sorghum/cassava investigation**: exploratory scenarios, summary, robustness sweep, coverage audit and paired sensitivity audit (45,927 rows). They are **not six-crop or rotation simulation records** and must not be used as such. The original user-provided data are copied without altering their values; `(1)` duplicate download suffixes were removed from packaged filenames.

**Now included:** the six-crop and A/B/C per-simulation CSV exports from Google Drive under `research/outputs/six_crop_rotations/`, together with `assumptions.json`. These allow independent aggregate checks, although a complete rerun from original raw climate inputs still requires the original Drive workspace.

## Complete six-crop and rotation exports

The following files are provided under `research/outputs/six_crop_rotations/`:

- `six_crop_climate_scenarios.csv`: 1,662 completed crop-cycle scenarios across six crops.
- `three_rotations_24_months.csv`: 162 complete 24-month rotation scenarios (54 each for A, B, C).
- `rotation_segments.csv`: 540 individual crop segments forming those rotations.
- `assumptions.json`: source URLs and explicit modeling limitations.

The accompanying `rotation_results.js` at repository root is byte-for-byte identical to the file exported alongside these CSVs. Independent checks confirm that each rotation total equals the sum of its segments, its reported shortfall/day equals shortfall divided by cropped days, and successive crop segments have 14-day gaps without overlaps. Baseline means round to A **1.94**, B **2.75**, C **2.12** mm/day. These checks establish computational consistency, **not agronomic field validation**.
