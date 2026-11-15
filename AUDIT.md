# Final consistency audit — 15 November 2026

## Verified against available files

- **Territorial CSV:** 1,848 rows and 1,848 distinct parcel IDs. Risk classes: Low 858; Moderate 579; High 411.
- **`data.js` + `geo.js`:** 1,848 distinct parcel records and 1,848 geometries; no missing geometry for displayed parcel IDs.
- **Agricultural filter:** 382 `uso_agropecuario=True` in corrected CSV and 382 flagged records in the UI data. Earlier project descriptions mentioned **386**; that count is outdated for this export and must not be reused.
- **Territorial numeric consistency:** `data.js` agrees with the corrected territorial CSV to display rounding precision (risk and vegetation vulnerability within 0.0005; rainfall percent and soil clay within 0.05 percentage points).
- **Six-crop display:** 72 monthly baseline entries (six crops × 12 months); the displayed April results match `rotation_results.js`.
- **Three rotation summaries:** A 1.941 mm/day, 430 crop days, 3 families; B 2.746 mm/day, 370 crop days, 2 families; C 2.123 mm/day, 550 crop days, 3 families. Each has 18 complete baseline historical simulations in `rotation_results.js`.
- **Notebook 2 implementation:** stages sum to 210/120/120/100/130/120 days for cassava/maize/sorghum/dry bean/tomato/rice; 14-day gaps inserted between sequential crops, and no overlapping dates are permitted by its checks. It distinguishes flooded-rice additional water from climatic shortfall.
- **Legacy data:** `crop_results.js` intentionally holds the earlier three-crop, April–June sensitivity display. It is **not** the six-crop dataset.
- **Package wiring:** The website loads the six-crop summaries from the external `rotation_results.js` (single source of truth), plus `data.js`, `geo.js`, `crop_results.js`.

## Important unresolved checks

1. **Full six-crop/rotation CSVs have now been included and checked.** They contain 1,662 crop-cycle rows, 162 rotation scenarios and 540 segments. Totals, cropped days, mean deficit arithmetic, and 14-day crop gaps match. This is an export-level consistency check, not a rerun of the source climate pipeline.
2. **No live browser visual regression was performed.** The existing layout was preserved; JavaScript syntax and file references were checked. Verify map loading, filters, rainfall controls, month selection and A/B/C on the published Pages URL.
3. **FAO and local agronomic documentary verification is incomplete.** Source URLs are included, but stage lengths and Kc were not field-calibrated, and no local source confirms the three exact rotations.
4. **Data pipeline rerun requires the original Drive inputs**, including the cadastral GeoPackage and NASA POWER/IDEAM source datasets. Those large originals are not included in this GitHub-ready ZIP.
5. **Do not imply causality or crop suitability** from territorial screening, or rank the flooded-rice options solely by climatic shortfall.

## Publication checklist

- [ ] Upload `index.html`, `data.js`, `geo.js`, `crop_results.js`, `rotation_results.js` and the documentation to the existing repository root.
- [ ] Open the live GitHub Pages URL in an incognito tab and hard-refresh.
- [ ] Confirm all 1,848 parcels render and the agricultural filter shows 382.
- [ ] Select a parcel; test rainfall presets and map recoloring.
- [ ] Change planting month; confirm six crop cards update.
- [ ] Confirm A/B/C rotation values and the rice-water caveat.
- [ ] Ensure no browser console errors and check the page at normal browser zoom.


## Supplementary uploaded data check (2026-11-15)

- Corrected territorial CSV: **1,848** records.
- Corrected territorial GeoPackage: **1,848** features, in one spatial layer.
- Earlier three-crop scenarios: **72** records.
- Earlier paired sensitivity audit: **45,927** records.
- Five three-crop CSVs are preserved as research artifacts; they do not independently verify six-crop rotation aggregates.
- Browser data were not regenerated from these supplemental uploads; the website files are unchanged from the previous package.

## Final verification of uploaded rotation exports

- Six-crop complete cycles: **1,662**.
- Complete 24-month rotations: **162** (54 per strategy).
- Rotation crop segments: **540**.
- Every rotation scenario matched exactly one group of crop segments; summed cropped days and summed modeled shortfall agree.
- Every sequence has **14-day unmodeled intervals** between successive crops; no overlapping dates were found.
- All per-cropped-day shortfall values agree with total shortfall divided by cropped days (floating-point precision).
- Historical baseline: **18 scenarios per strategy**; means A **1.941**, B **2.746**, C **2.123** mm/day.
- Exported `rotation_results.js` is byte-for-byte identical to the website copy.
- The original raw NASA POWER input and local agronomic calibration are still outside this package; these are **not** field-validated rotations.
