#!/usr/bin/env python3
"""L616 breadth — verify memo claims before they ship (record-close ranking; character of the
comparable equal-weight-favourable down days; 8/13 tier readings).
Run: .venv/bin/python3 -I <this> <research_dir> <cache_dir>  -> verify_claims.txt
"""
import sys, os, pickle
import pandas as pd
R, C = sys.argv[1], sys.argv[2]
daily = pd.read_csv(os.path.join(R, "breadth_daily.csv"), index_col=0, parse_dates=True)
pe = pickle.load(open(os.path.join(C, "px_etf.pkl"), "rb"))
L = []
def P(*a):
    s = " ".join(str(x) for x in a); L.append(s); print(s)
spx = pe["Close"]["^GSPC"].dropna()
rec = spx[spx >= spx.cummax()].loc["2026-01-01":"2026-10-30"]
t = daily.loc[rec.index, ["SPX", "SP500_pct50", "SP500_pct200", "SP500_nh", "SP500_nl", "SP1500_pct50", "SP1500_pct200", "RSP_SPY"]].copy()
t["SP500_nhnl"] = t.SP500_nh - t.SP500_nl
P(f"2026 record closes: {len(t)}; October records: {[str(d.date()) for d in t.loc['2026-10-01':].index]}")
for c in ["SP500_pct50", "SP500_pct200", "SP1500_pct50", "SP1500_pct200", "RSP_SPY", "SP500_nhnl"]:
    s = t[c]
    P(f"{c:14s} lowest at a record close: {s.min():.4f} on {s.idxmin().date()} | 10/06: {s.loc['2026-10-06']:.4f} | rank of 10/06 from lowest: {int((s < s.loc['2026-10-06']).sum())+1} of {len(s)}")
P(t.loc["2026-08-01":].round(4).to_string())
P("\n8/13 tier readings:", daily.loc["2026-08-13", ["SP400_pct50", "SP400_pct200", "SP600_pct50", "SP600_pct200", "SP1500_pct50", "SP1500_pct200"]].round(1).to_dict())
ea = pe["Adj Close"]
r = (ea / ea.shift(1) - 1) * 100
P("\nCharacter of the most equal-weight-favourable SPY -1.3..-2.3% days (total return %):")
for d in ["2025-01-27", "2026-06-23", "2024-07-24", "2024-07-17", "2026-10-30"]:
    x = r.loc[d, ["SPY", "RSP", "QQQ", "SOXX", "XLK", "XLC", "XLY", "XLE", "XLP", "XLU", "XLV"]].round(2)
    P(d, x.to_dict())
open(os.path.join(R, "verify_claims.txt"), "w").write("\n".join(L) + "\n")
