#!/usr/bin/env python3
"""Realised crack seasonality from EIA daily SPOT prices (no contract rolls).

Series (EIA v2, petroleum/pri/spt, daily): RBRTE (Brent spot), RWTC (WTI spot),
EER_EPMRU_PF4_Y35NY_DPG (NY Harbor conventional gasoline), EER_EPD2DXL0_PF4_Y35NY_DPG
(NY Harbor ULSD). EIA's front-month FUTURES series (petroleum/pri/fut) end 2024-04-05,
so they cannot cover 2024-26; spot is used for all years for one consistent basis.

Run from the repo root: .venv/bin/python3 AGENTS/BRENT/research/2026-09-25_crack-seasonality/crack_seasonality.py
Writes monthly.csv next to this file and prints the seasonal-change tables.
"""
import json, os, sys, urllib.parse, urllib.request
import numpy as np, pandas as pd

ROOT = os.popen("git rev-parse --show-toplevel").read().strip()
sys.path.insert(0, os.path.join(ROOT, "FORGE/tools/market-data"))
import fetch  # key from the gitignored FORGE .env

SERIES = {"BRENT": "RBRTE", "WTI": "RWTC",
          "GAS": "EER_EPMRU_PF4_Y35NY_DPG", "ULSD": "EER_EPD2DXL0_PF4_Y35NY_DPG"}


def pull(sid, start="2010-01-01"):
    out, off = [], 0
    while True:
        p = {"api_key": fetch.EIA_API_KEY, "frequency": "daily", "data[0]": "value",
             "facets[series][]": sid, "start": start, "sort[0][column]": "period",
             "sort[0][direction]": "asc", "offset": off, "length": 5000}
        u = f"{fetch.EIA_BASE}/petroleum/pri/spt/data/?{urllib.parse.urlencode(p)}"
        rows = json.load(urllib.request.urlopen(u, timeout=60))["response"]["data"]
        out += rows
        if len(rows) < 5000:
            return out
        off += 5000


df = pd.DataFrame({k: pd.Series({pd.Timestamp(r["period"]): float(r["value"])
                                 for r in pull(s) if r.get("value") is not None})
                   for k, s in SERIES.items()}).dropna()
df["c321_B"] = (2 * df.GAS * 42 + df.ULSD * 42) / 3 - df.BRENT
df["gas_B"] = df.GAS * 42 - df.BRENT
df["ulsd_B"] = df.ULSD * 42 - df.BRENT
print(f"daily rows {len(df)}  {df.index.min().date()} .. {df.index.max().date()}")

m = df.resample("ME").mean()
m["y"], m["mo"] = m.index.year, m.index.month
m.round(3).to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "monthly.csv"))


def g(col, y, mo):
    s = m.loc[(m.y == y) & (m.mo == mo), col]
    return s.iloc[0] if len(s) else np.nan


for col in ["c321_B", "gas_B", "ulsd_B"]:
    rows = []
    for y in range(2010, 2026):
        s, n = g(col, y, 9), g(col, y, 11)
        rows.append({"y": y, "Sep": s, "Sep->Oct": g(col, y, 10) - s, "Sep->Nov": n - s,
                     "Sep->Dec": g(col, y, 12) - s, "Nov->Dec": g(col, y, 12) - n,
                     "Nov->Jan": g(col, y + 1, 1) - n,
                     "Nov->Dec%": (g(col, y, 12) - n) / abs(n) * 100,
                     "Nov->Jan%": (g(col, y + 1, 1) - n) / abs(n) * 100})
    t = pd.DataFrame(rows).set_index("y")
    print(f"\n=== {col} ($/bbl; % columns relative to the November average)")
    print(t.round(1).to_string())
    for c in t.columns[1:]:
        v = t[c].dropna()
        print(f"  {c:10s} n={len(v)} median {v.median():+.1f} IQR [{v.quantile(.25):+.1f},"
              f"{v.quantile(.75):+.1f}] negative {int((v < 0).sum())}/{len(v)}")
    hi = t[t.Sep > 20]
    print(f"  high-level years (Sep avg > $20, n={len(hi)}): Nov->Dec% median "
          f"{hi['Nov->Dec%'].median():+.1f}  Nov->Jan% median {hi['Nov->Jan%'].median():+.1f}")
