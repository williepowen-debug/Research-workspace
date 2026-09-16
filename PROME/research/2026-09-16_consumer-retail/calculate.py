"""Derived measures from Census CB26-153 Table 1, adjusted $millions.
Input transcription checked against the downloaded September 16 PDF.
Control = total minus auto, gasoline, building materials, food services.
"""
import json
from pathlib import Path
rows = {
    "total": [773947,764462,768587],
    "auto": [142379,141565,144140],
    "gas": [62303,60455,60586],
    "building": [42227,42318,42380],
    "foodservice": [105070,103824,103340],
    "nonstore": [141339,137772,140207],
}
rows["control"] = [rows["total"][i]-sum(rows[k][i] for k in ("auto","gas","building","foodservice")) for i in range(3)]
rows["control_ex_nonstore"] = [rows["control"][i]-rows["nonstore"][i] for i in range(3)]
rows["ex_gas_nonstore"] = [rows["total"][i]-rows["gas"][i]-rows["nonstore"][i] for i in range(3)]
results = {}
for name,(aug,jul,jun) in rows.items():
    results[name] = {"aug_million":aug,"jul_million":jul,"jun_million":jun,
      "aug_mom_pct":100*(aug/jul-1),"jul_mom_pct":100*(jul/jun-1),
      "aug_vs_june_pct":100*(aug/jun-1),
      "headline_contribution_pp":100*(aug-jul)/rows["total"][1],
      "share_headline_increase_pct":100*(aug-jul)/(rows["total"][0]-rows["total"][1])}
Path(__file__).with_name("calculations.json").write_text(json.dumps(results,indent=2)+"\n")
print(json.dumps(results,indent=2))
