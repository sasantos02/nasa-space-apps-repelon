# Scientific limitations and interpretation

1. **Different spatial scales.** Parcel screening (CHIRPS + Sentinel-2) and crop comparisons (NASA POWER regional daily weather) are shown together but **not fused into parcel-specific crop suitability**.
2. **Uncalibrated index.** Environmental risk categories are exploratory. The 0.5/0.5 weighting and classification thresholds are model assumptions. Land-cover misclassification and very small parcels can produce misleading labels.
3. **Rainfall uncertainty.** IDEAM/CHIRPS/GPM comparison is preliminary. IDEAM sensor interpretation and satellite pixel-to-station differences are unresolved; the comparison does not validate crop outcomes.
4. **Shortfall is not a soil-water balance.** `max(ETc - P, 0)` uses gross daily rainfall and does not model water storage, irrigation, runoff, infiltration, percolation outside the rice proxy, or effective rainfall.
5. **Crop parameters are provisional.** Kc curves, stage durations and planting windows need local cultivar and management validation. Generic dry bean is not confirmed local cowpea.
6. **Rice is not directly comparable by shortfall alone.** Flooded rice includes a separate 1,020 mm illustrative extra water assumption, not in the climate shortfall ranking; local irrigation and rice production practices are unknown.
7. **Rotations are hypothetical.** The three crop sequences, 14-day intervals and 24-month timelines are designed for exploration; they are not verified crop rotations in Repelón. Fallow/cover benefits, disease/pest effects, nitrogen cycling and soil improvement are not quantified.
8. **Different cropping intensity.** A=430, B=370, C=550 cropped days. Per-cropped-day shortfall alone cannot rank total farm performance or water consumption.
9. **No field validation.** No yields, actual planted crops per parcel, operational irrigation turns, financial viability or farmer priorities have been measured. Do not prescribe changes for a particular parcel.
10. **Summary data only in this package.** The six-crop/rotation JS includes aggregates; full per-simulation CSV outputs must be retrieved from the original Drive workspace or regenerated in Colab to reproduce every statistic.
