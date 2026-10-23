"""KRE vs the rest of financials, now and historically. Input fin_px.csv (pull_fin.py; yfinance auto-adjusted closes,
10/23 bar pulled 16:05 ET). Group rows = equal-weight average of member returns over the window.
Run: .venv/bin/python -I fin_compare.py -> RESULTS.md
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
px = pd.read_csv(os.path.join(HERE, "fin_px.csv"), index_col=0, parse_dates=True)
END = px.index[-1]
GROUPS = {"Money-center banks (JPM, BAC, C, WFC)": ["JPM", "BAC", "C", "WFC"],
          "Alt managers / private credit (APO, BX, KKR, ARES, OWL)": ["APO", "BX", "KKR", "ARES", "OWL"],
          "Software-heavy BDCs (ARCC, BXSL, FSK, GBDC, HTGC)": ["ARCC", "BXSL", "FSK", "GBDC", "HTGC"],
          "Book's regionals (WAL, ZION, OZK, FLG)": ["WAL", "ZION", "OZK", "FLG"]}
ROWS = [("KRE — regional banks", "KRE"), ("KBE — all banks, equal-weight", "KBE"), ("KBWB — large banks", "KBWB"),
        ("XLF — broad financials", "XLF"), ("IAI — brokers / exchanges", "IAI"), ("KIE — insurers", "KIE"),
        ("BIZD — BDC ETF", "BIZD"), ("IWM — small caps (control)", "IWM"), ("SPY", "SPY"), ("QQQ", "QQQ")]
def at(d):
    return px.index[px.index.get_indexer([pd.Timestamp(d)], method="pad")[0]]
W = [("5 days", px.index[-6]), ("Since QQQ peak 10/6", at("2026-10-06")), ("1 month", px.index[-22]),
     ("3 months", px.index[-64]), ("YTD", at("2025-12-31")), ("1 year", px.index[-253])]
def ret(cols, d0):
    r = [px[c].loc[END] / px[c].loc[d0] - 1 for c in cols if pd.notna(px[c].loc[d0])]
    return np.mean(r) if r else np.nan
p = lambda v: "—" if pd.isna(v) else f"{v*100:+.1f}%"
L = [f"# KRE vs the rest of financials (TERRY, closes through {END.date()}, 10/23 bar pulled 16:05 ET)\n",
     "yfinance auto-adjusted closes (dividends included). Group rows = equal-weight average of member returns.\n",
     "## 1. Performance by window\n", "| | " + " | ".join(w for w, _ in W) + " |", "|---|" + "---:|" * len(W)]
for lab, c in ROWS:
    L.append(f"| {lab} | " + " | ".join(p(ret([c], d)) for _, d in W) + " |")
for lab, cols in GROUPS.items():
    L.append(f"| {lab} | " + " | ".join(p(ret(cols, d)) for _, d in W) + " |")

# 2. relative strength vs history: 20d / 60d relative return, percentile over the pair's full history
PAIRS = [("KRE vs large banks (^BKX)", "KRE", "^BKX"), ("KRE vs broad financials (XLF)", "KRE", "XLF"),
         ("KRE vs small caps (IWM)", "KRE", "IWM"), ("KRE vs BDCs (BIZD)", "KRE", "BIZD"), ("KRE vs QQQ", "KRE", "QQQ"),
         ("Large banks (^BKX) vs QQQ", "^BKX", "QQQ"), ("BDCs (BIZD) vs XLF", "BIZD", "XLF")]
L += ["\n## 2. Relative strength now vs each pair's own history (log relative return; percentile = share of past readings below today)\n",
      "| Pair | Since | 20-day relative | percentile | 60-day relative | percentile | Ratio vs its 5-year range (0% = 5y low, 100% = 5y high) |",
      "|---|---|---:|---:|---:|---:|---:|"]
for lab, a, b in PAIRS:
    x = px[[a, b]].dropna(); lr = np.log(x[a] / x[b])
    r20, r60 = lr.diff(20).dropna(), lr.diff(60).dropna()
    five = lr[lr.index >= END - pd.DateOffset(years=5)]
    pos = (lr.iloc[-1] - five.min()) / (five.max() - five.min())
    L.append(f"| {lab} | {x.index[0].year} | {r20.iloc[-1]*100:+.1f}% | {(r20 < r20.iloc[-1]).mean()*100:.0f}% | "
             f"{r60.iloc[-1]*100:+.1f}% | {(r60 < r60.iloc[-1]).mean()*100:.0f}% | {pos*100:.0f}% |")

# 3. year-by-year: KRE minus large banks, KRE minus XLF
L += ["\n## 3. Year by year — KRE's return minus large banks (^BKX) and minus XLF\n", "| Year | KRE | ^BKX | KRE − BKX | XLF | KRE − XLF |", "|---|---:|---:|---:|---:|---:|"]
for y in range(2007, END.year + 1):
    s, e = at(f"{y-1}-12-31"), (at(f"{y}-12-31") if y < END.year else END)
    k, b, f = (px[c].loc[e] / px[c].loc[s] - 1 for c in ("KRE", "^BKX", "XLF"))
    L.append(f"| {y}{' YTD' if y == END.year else ''} | {p(k)} | {p(b)} | {p(k-b)} | {p(f)} | {p(k-f)} |")

# 4. past see-saw episodes: was the bank leg's move regional-specific? 20 sessions INTO each signal
ep = pd.read_csv(os.path.join(os.path.dirname(HERE), "episode_study", "episodes.csv"), parse_dates=["signal"])
L += ["\n## 4. Inside past KRE/QQQ see-saw episodes — 20 sessions into each signal (and NOW)\n",
      "| Signal | Leader | KRE | ^BKX | XLF | IWM | BIZD | KRE − BKX | Regional-specific? |", "|---|---|---:|---:|---:|---:|---:|---:|---|"]
for _, e in ep.iterrows():
    d1 = at(e["signal"]); i1 = px.index.get_loc(d1); d0 = px.index[i1 - 20]
    v = {c: px[c].loc[d1] / px[c].loc[d0] - 1 if pd.notna(px[c].loc[d0]) else np.nan for c in ("KRE", "^BKX", "XLF", "IWM", "BIZD")}
    gap = v["KRE"] - v["^BKX"]
    L.append(f"| {d1.date()} | {e['dir'].split(' over')[0].replace('KRE','banks').replace('QQQ','tech')} | {p(v['KRE'])} | {p(v['^BKX'])} | {p(v['XLF'])} | {p(v['IWM'])} | {p(v['BIZD'])} | {p(gap)} | "
             f"{'yes (KRE ≥2 pts ahead of big banks)' if gap >= .02 else 'no — bank-wide' if abs(gap) < .02 else 'no — big banks led'} |")
d1 = END; d0 = px.index[-21]
v = {c: px[c].loc[d1] / px[c].loc[d0] - 1 for c in ("KRE", "^BKX", "XLF", "IWM", "BIZD")}
gap = v["KRE"] - v["^BKX"]
L.append(f"| **NOW ({d1.date()}, 20 sessions)** | banks | {p(v['KRE'])} | {p(v['^BKX'])} | {p(v['XLF'])} | {p(v['IWM'])} | {p(v['BIZD'])} | {p(gap)} | "
         f"{'yes' if gap >= .02 else 'no — bank-wide' if abs(gap) < .02 else 'no — big banks led'} |")

# 5. regionals up while BDCs down: how unusual is today's 20-day split?
x = px[["KRE", "BIZD"]].dropna(); k20 = x["KRE"].pct_change(20); b20 = x["BIZD"].pct_change(20)
spread = (k20 - b20).dropna(); now = spread.iloc[-1]
L += ["\n## 5. Regionals vs BDCs (private credit) — 20-day return gap, since 2013\n",
      f"KRE 20-day {p(k20.iloc[-1])} vs BIZD {p(b20.iloc[-1])} ⇒ gap {p(now)}; higher than {(spread < now).mean()*100:.0f}% of {len(spread)} daily readings since {x.index[20].date()}. "
      f"Days with KRE up AND BIZD down ≥3% over 20 sessions: {((k20 > 0) & (b20 <= -.03)).mean()*100:.1f}% of days."]
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
