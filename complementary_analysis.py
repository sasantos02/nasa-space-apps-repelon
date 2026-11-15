"""Complementary analysis for the Repelon risk tool (does NOT change the model).
Run from the repository root. Inputs:
  03_salidas_finales/predios_para_demo_2026-11-15.csv
  01_entradas/EVA_2019_2025_Base_Agricola.csv  (UPRA/MinAgricultura, filtered to Repelon)
Outputs: tables/*.csv
"""
import glob, numpy as np, pandas as pd
from scipy.stats import spearmanr

d = pd.read_csv("03_salidas_finales/predios_para_demo_2026-11-15.csv", dtype={"CODIGO": str})
d = d.drop_duplicates("CODIGO").reset_index(drop=True)          # 1,848 unique parcels

BASE_TH = {"NDVI": (0.2, 0.7), "NDMI": (-0.1, 0.3), "SAVI": (0.05, 0.5)}  # (critical, healthy) - assumptions
BASE_W = np.array([0.4, 0.4, 0.2])                                          # assumptions
def stress(x, c, s): return np.clip((s - x) / (s - c), 0, 1)
def vuln(df, th, w):
    return sum(wi * stress(df[k], *th[k]) for wi, k in zip(w, ["NDVI", "NDMI", "SAVI"]))

A = np.clip(1 - d.Precip_pct_normal / 100, 0, 1)
v0 = vuln(d, BASE_TH, BASE_W); R0 = 0.5 * A + 0.5 * v0
print("max |V - V_file| =", float((v0 - d.V_Vulnerability).abs().max()))

# 1) Sensitivity: thresholds and weights +/-20 % (1,000 random draws), A/V weight 0.4-0.6
rng = np.random.default_rng(1); rows = []
top0 = set(v0.nlargest(100).index)
for _ in range(1000):
    th = {k: tuple(x * rng.uniform(0.8, 1.2) for x in v) for k, v in BASE_TH.items()}
    w = BASE_W * rng.uniform(0.8, 1.2, 3); w = w / w.sum()
    wa = rng.uniform(0.4, 0.6)
    v = vuln(d, th, w); R = wa * A + (1 - wa) * v
    rows.append((spearmanr(v0, v)[0], spearmanr(R0, R)[0], len(top0 & set(v.nlargest(100).index)), int((R > 0.5).sum())))
s = pd.DataFrame(rows, columns=["spearman_V", "spearman_R", "top100_overlap", "n_High"])
s.describe().round(3).to_csv("tables/sensitivity_summary.csv"); print(s.describe().round(3))

# 2) What-if rainfall scenarios (NOT a forecast): vulnerability fixed, rain = p % of normal
out = []
for p in (100, 80, 60):
    R = 0.5 * max(0, 1 - p / 100) + 0.5 * v0
    out.append((p, int((R <= .25).sum()), int(((R > .25) & (R <= .5)).sum()), int((R > .5).sum())))
pd.DataFrame(out, columns=["rain_pct_of_normal", "Low", "Moderate", "High"]).to_csv("tables/rain_scenarios.csv", index=False)

# 3) Land cover area vs EVA (municipal) - order-of-magnitude comparison only
print(d.groupby("cobertura_dominante").area_ha.agg(["count", "sum"]).round(1))
f = glob.glob("01_entradas/*EVA*.csv")[0]; e = pd.read_csv(f)
num = lambda x: pd.to_numeric(x.astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")
e["sown_ha"] = num(e["Área sembrada"])
e[e["Municipio"] == "Repelón"].groupby(["Año", "Cultivo"]).sown_ha.sum().reset_index().to_csv("tables/eva_repelon_by_crop.csv", index=False)
print(e[e["Municipio"] == "Repelón"].groupby("Año").sown_ha.sum())
