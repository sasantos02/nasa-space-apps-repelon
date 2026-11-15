# Notebook guide (English)
The notebook `riesgo_agroclimatico_repelon_v2_2.ipynb` is written in Spanish (comments, labels and column names) because it was built and checked with local collaborators. This page is the English map. We did not translate the code, to avoid introducing errors after the results were verified.

## How to run
1. Open it in Google Colab. You need a Google Earth Engine project (set `PROJECT_ID`) and a Drive folder (`RUTA_BASE`) with two inputs: `repelon_predios_rurales.gpkg` (parcels) and `predios_en_distrito_nuevo.csv` (QGIS district cross-check). Both are in `01_entradas/`.
2. Run the sections in order. Section 0 holds all parameters (analysis end date, window length, cloud limit, thresholds, weights).
3. Section 11 writes `03_salidas_finales/predios_para_demo_<date>.csv` and `parametros_modelo_<date>.json`. After that, run `python complementary_analysis.py` from the repository root.

## Section map
| Section | What it does |
|---|---|
| 0 | Configuration: dates, 60-day window, cloud limit, index thresholds, weights (all uncalibrated assumptions) |
| 1 | Libraries, Earth Engine authentication, Drive |
| 2 | Loads and cleans parcels (adaptive buffer; 9 repeated parcel codes) |
| 3 | Dates and the helper that extracts raster values per parcel in batches |
| 4 | **Vulnerability** from Sentinel-2 (ESA): NDVI, NDMI, SAVI stress, weights 0.4 / 0.4 / 0.2 |
| 5 | **Hazard** from NASA GPM IMERG V07: 60-day rain against the same window of the previous 10 years |
| 6 | **Risk** = 0.5·Hazard + 0.5·Vulnerability and risk classes |
| 7 | Visual review of sample parcels (not a validation) |
| 8 | Monthly calendar of the zone (GPM rain and Sentinel-2 NDVI, 2021–2025) |
| 9 | Inside/outside the irrigation district (from the QGIS cross-check) and example-parcel candidates |
| 9b | ESA WorldCover 2021 land cover per parcel (`uso_agropecuario` = cropland + grassland ≥ 50 %) |
| 9c | ISRIC SoilGrids clay 0–5 cm, **context only**, not in the risk score (g/kg ÷ 10 = %; saved outputs predate this fix) |
| 10 | Monthly NDVI curve of the example parcel |
| 11 | Exports the final CSV and the parameters JSON |
| 12 | Rainfall check: GPM IMERG (NASA) against ERA5-Land (ECMWF) |

## Column glossary (final CSV)
`CODIGO` parcel code (30 digits; open as text) · `area_ha` area · `en_distrito` inside irrigation district · `dist_distrito_km` distance to the ADR reference point · `NDVI`, `NDMI`, `SAVI` indices · `V_Vulnerability` vulnerability (0–1) · `precip_mm`, `Precip_pct_normal` window rainfall and % of normal · `Amenaza_Norm` hazard (0–1) · `Riesgo_Index` risk (0–1) · `Nivel_Riesgo` Bajo / Moderado / Alto / Crítico = Low / Moderate / High / Critical · `cobertura_dominante` dominant WorldCover class (Arboles = trees, Pastizal = grassland, Cultivo = cropland, Construido = built-up, Suelo_desnudo = bare soil) · `pct_agropecuario` % cropland + grassland · `uso_agropecuario` agricultural flag · `soil_clay_pct` clay % (context) · `baja_confianza` parcel < 0.1 ha · `lat`, `lon` centroid.
