#!/usr/bin/env python3
"""L616 breadth — second-pass tests (run after breadth_compute.py).
Run: .venv/bin/python3 -I <this> <research_dir> <cache_dir>   -> appends to report_extra.txt
"""
import sys, os, json, pickle
import pandas as pd
import yfinance as yf
R, C = sys.argv[1], sys.argv[2]
D0 = pd.Timestamp("2026-10-30")
daily = pd.read_csv(os.path.join(R, "breadth_daily.csv"), index_col=0, parse_dates=True)
pe = pickle.load(open(os.path.join(C, "px_etf.pkl"), "rb")).loc[:D0]
snap = pd.read_csv(os.path.join(R, "stock_snapshot.csv"), index_col=0)
semis = json.load(open(os.path.join(R, "semis.json")))["semis_sp500"]
MAG7 = ["AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA"]
L = []
def P(*a):
    s = " ".join(str(x) for x in a); L.append(s); print(s)

P("=== X1. decline breadth by tier on SPY <= -1.3% days (2025-01-02..10/29, today's members) vs 10/30 ===")
h = daily.loc[:"2026-10-29"]
h = h[h.SPY_tr <= -1.3]
for g in ["SP500", "SP400", "SP600", "SP1500"]:
    pdn = h[f"{g}_dec"] / (h[f"{g}_adv"] + h[f"{g}_dec"]) * 100
    t = daily.loc[D0]
    td = t[f"{g}_dec"] / (t[f"{g}_adv"] + t[f"{g}_dec"]) * 100
    rank = int((pdn < td).sum()) + 1
    P(f"{g}: n={len(pdn)} median %down {pdn.median():.1f} (p10 {pdn.quantile(.1):.1f}) | 10/30 {td:.1f}% -> rank {rank} of {len(pdn)+1} from the narrowest | median-stock move median {h[f'{g}_medchg'].median():+.2f}% vs 10/30 {t[f'{g}_medchg']:+.2f}%")

P("\n=== X2. October's RSP/SPY relative return vs history (22 sessions, Adj Close, ratio, 2003-05..) ===")
ea = pe["Adj Close"]
rs = (ea["RSP"] / ea["SPY"]).dropna()
s22 = ((rs / rs.shift(22) - 1) * 100).dropna().loc["2003-05-01":]
cur = s22.loc[D0]
P(f"10/30 22-session value {cur:+.2f}pp; pctile {(s22 < cur).mean()*100:.1f} of {len(s22)} sessions; max {s22.max():+.2f} on {s22.idxmax().date()}")
ex = s22[s22 >= cur]
ep, last = [], None
for d, v in ex.items():
    if last is None or (d - last).days > 90:
        ep.append([d, v])
    elif v > ep[-1][1]:
        ep[-1] = [d, v]
    last = d
P("distinct episodes (>90 calendar-day gap) with 22-session value >= 10/30's:", [(str(d.date()), round(v, 2)) for d, v in ep])
s22q = ((ea["QQEW"] / ea["QQQ"]).dropna())
P(f"QQEW/QQQ 22-session 10/30: {((s22q.loc[D0] / s22q.shift(22).loc[D0]) - 1) * 100:+.2f}pp")

P("\n=== X3. trajectory (S&P 500 | S&P 1500): % > 50-day, % > 200-day, NH/NL that day, cum A/D (base 2025-01-02) ===")
for d in ["2026-07-31", "2026-08-13", "2026-08-28", "2026-09-11", "2026-09-25", "2026-09-30", "2026-10-06", "2026-10-09", "2026-10-16", "2026-10-23", "2026-10-29", "2026-10-30"]:
    r = daily.loc[daily.index[daily.index <= pd.Timestamp(d)][-1]]
    P(f"{d}  SPX {r.SPX:8.2f} | 500: >50 {r.SP500_pct50:5.1f} >200 {r.SP500_pct200:5.1f} NH {int(r.SP500_nh):3d} NL {int(r.SP500_nl):3d} AD {int(r.SP500_cumAD):5d} "
      f"| 1500: >50 {r.SP1500_pct50:5.1f} >200 {r.SP1500_pct200:5.1f} NH {int(r.SP1500_nh):3d} NL {int(r.SP1500_nl):3d} AD {int(r.SP1500_cumAD):6d} | RSP/SPY {r.RSP_SPY:.5f}")

P("\n=== X4. S&P 1500 daily new highs / new lows, summed by week, Sep 28 - Oct 30 (name-days, intraday basis) ===")
oc = daily.loc["2026-09-28":"2026-10-30", ["SP1500_nh", "SP1500_nl", "SP500_nh", "SP500_nl", "SP600_nh", "SP600_nl"]]
wk = oc.groupby(oc.index.to_period("W-FRI")).sum()
for i, r in wk.iterrows():
    P(f"week ending {i.end_time.date()}: SP1500 NH {int(r.SP1500_nh):4d} NL {int(r.SP1500_nl):4d} | SP500 NH {int(r.SP500_nh):3d} NL {int(r.SP500_nl):3d} | SP600 NH {int(r.SP600_nh):3d} NL {int(r.SP600_nl):3d}")

P("\n=== X5. Friday 10/30: largest S&P 500 decliners OUTSIDE Mag-7 and the semis set (price return %) ===")
s5 = snap[snap["index"] == "SP500"]
rest = s5.drop(index=[t for t in MAG7 + semis if t in s5.index])
P(rest.sort_values("r1d_px").head(15)[["sector", "r1d_px"]].round(2).to_string())
P(f"rest names down > 5%: {(rest.r1d_px < -5).sum()} of {rest.r1d_px.notna().sum()}; by sector: {rest[rest.r1d_px < -5].sector.value_counts().to_dict()}")
P("S&P 500 new 52-wk highs on 10/30 by sector:", s5[s5.nh_1030 == 1].sector.value_counts().to_dict())
P("S&P 500 new 52-wk lows on 10/30:", s5[s5.nl_1030 == 1][["sector", "r1d_px"]].round(2).to_dict("index"))

P("\n=== X6. KRE (regional banks, held-put underlying) horizons, Adj Close total return ===")
k = yf.download(["KRE", "SPY"], start="2025-10-01", end="2026-10-31", auto_adjust=False, progress=False)["Adj Close"].dropna()
for lab, d in {"1d": "2026-10-29", "1w": "2026-10-23", "1m": "2026-09-30", "3m": "2026-07-31", "YTD": "2025-12-31"}.items():
    r0 = k.index[k.index <= pd.Timestamp(d)][-1]
    P(f"KRE {lab}: {(k.KRE.loc[D0]/k.KRE.loc[r0]-1)*100:+.2f}%  (SPY {(k.SPY.loc[D0]/k.SPY.loc[r0]-1)*100:+.2f}%)")
open(os.path.join(R, "report_extra.txt"), "w").write("\n".join(L) + "\n")
