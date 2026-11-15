# Running the research notebooks in Google Colab

The published **website** runs without Colab. The notebooks document the research pipeline; they are **not yet one-click reproducible from a different Google account**.

## Clean-account smoke test

1. Open the GitHub notebooks from a second Google account (a separate browser profile or private window).
2. Inspect all input paths before running. The notebooks expect `/content/drive/MyDrive/Agro/`, which points to the **current account's own Drive**. Public sharing of the author’s folder does not automatically mount it there. Copy the necessary input files into the test account's `MyDrive/Agro/`, or update the notebook path variables to point to explicitly accessible copies. Do not grant broad edit access to the original Drive.
3. Earth Engine calls use the project ID `agro-513620`. Each tester must authenticate and use an Earth Engine-enabled Cloud project for which they have the necessary access; if that project is not authorized for the tester, configure their own project ID. A project ID is not a secret and does not confer permissions.
4. Notebook 1 also expects the original cadastral GeoPackage `repelon_predios_rurales.gpkg` and other referenced inputs. The corrected output GeoPackage bundled here is **not necessarily an equivalent substitute for the original input**.
5. Notebook 2 may rely on cached NASA POWER data and other Drive files; inspect `RUTA_*` variables before execution. Notebook 3 requires the original IDEAM input `Precipitación_20261115.csv`, which is not included.
6. Run cells from top to bottom in a fresh runtime and record missing files, permissions and execution errors. Do not claim full independent reproducibility unless this succeeds.

## What a judge can verify immediately

- Open the live GitHub Pages dashboard and inspect the 1,848 parcels, the 382 flagged agricultural parcels, six crop profiles and A/B/C rotations.
- Review the formulas and methods in the three notebooks without executing them.
- Download `research/outputs/six_crop_rotations/` and audit the **1,662 crop-cycle scenarios**, **162 rotation scenarios** and **540 segments**.
- Read `AUDIT.md` and `LIMITATIONS.md` for the rainfall-source sensitivity and absence of field validation.

**Notebook 3 has no saved cell outputs in the committed version.** This package does not present its station-comparison numbers as independently reproduced results.
