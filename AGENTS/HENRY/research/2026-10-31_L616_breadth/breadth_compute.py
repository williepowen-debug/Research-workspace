#!/usr/bin/env python3
"""L616 breadth — ETF proxies + direct constituent breadth, as of Friday 2026-10-30.

Run: .venv/bin/python3 -I <this> <research_dir> <cache_dir>
Inputs : universe.csv (SSGA holdings as of 29-Oct-2026), cache px_const.pkl / px_etf.pkl
         (yfinance daily bars, auto_adjust=False: Close = split-adjusted price,
          Adj Close = split+dividend adjusted = total-return basis), semis.json (optional).
Outputs: breadth_daily.csv, stock_snapshot.csv, results.json, report.txt (all in research_dir)

Definitions (stated once, used everywhere):
  above 50/200-day  : Close > simple moving average of Close over 50 / 200 sessions
                      (name needs a full window; denominator printed)
  advance / decline : Close vs prior Close (price basis, like exchange A/D)
  new 52-wk high/low: intraday basis — High >= max(High of prior 251 sessions) /
                      Low <= min(Low of prior 251 sessions); full prior window required
  horizon return    : Adj Close total return, ref date = last session on/before the anchor
  relative return   : ratio basis, (A/B)_t / (A/B)_ref - 1, in pp (VULCAN mag7.py basis)
  cap-weighted (CW) : SPY fund shares held (29-Oct-2026) x Close at the ref date — an
                      approximation of index weights (constant shares); validated vs SPY
Survivorship: the universe is TODAY's membership applied backwards (names added for
strength are in, names removed for weakness are out) — history reads slightly too strong.
"""
import sys, os, json, pickle
import numpy as np
import pandas as pd

R, C = sys.argv[1], sys.argv[2]
uni = pd.read_csv(os.path.join(R, "universe.csv"))
px = pickle.load(open(os.path.join(C, "px_const.pkl"), "rb"))
pe = pickle.load(open(os.path.join(C, "px_etf.pkl"), "rb"))
D0 = pd.Timestamp("2026-10-30")
px = px.loc[:D0]
pe = pe.loc[:D0]
HZ = {"1d": "2026-10-29", "1w": "2026-10-23", "1m": "2026-09-30", "3m": "2026-07-31",
      "6m": "2026-04-30", "YTD": "2025-12-31", "12m": "2025-10-30"}
MAG7 = ["AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "NVDA", "META", "TSLA"]
OUT = {}
lines = []
def P(*a):
    s = " ".join(str(x) for x in a)
    lines.append(s)
    print(s)

def refdate(idx, d):
    d = pd.Timestamp(d)
    return idx[idx <= d][-1]

# ---------------------------------------------------------------- ETF proxies
ec, ea = pe["Close"], pe["Adj Close"]
assert ec.index.max() == D0, f"etf last bar {ec.index.max()} != {D0}"
def etf_ret(t, d, basis="tr"):
    s = (ea if basis == "tr" else ec)[t].dropna()
    r0 = refdate(s.index, d)
    return (s.loc[D0] / s.loc[r0] - 1) * 100
def rel(a, b, d):
    s = (ea[a] / ea[b]).dropna()
    r0 = refdate(s.index, d)
    return (s.loc[D0] / s.loc[r0] - 1) * 100

ETFS = ["SPY", "RSP", "OEF", "QQQ", "QQEW", "MDY", "IJH", "IJR", "IWM", "SOXX", "SMH"]
SECT = ["XLK", "XLC", "XLY", "XLF", "XLV", "XLI", "XLE", "XLP", "XLU", "XLB", "XLRE"]
IDX = ["^GSPC", "^NDX", "^SP400", "^SP600", "^RUT"]
P("=== A. ETF / INDEX RETURNS to 2026-10-30 close (ETF = total return on Adj Close; ^index = price) ===")
P("ref dates:", {k: str(refdate(ea['SPY'].dropna().index, v).date()) for k, v in HZ.items()})
tab = {}
for t in ETFS + SECT + IDX:
    tab[t] = {h: round(etf_ret(t, d, "tr" if not t.startswith("^") else "px"), 2) for h, d in HZ.items()}
    P(f"{t:7s}", "  ".join(f"{h}:{v:+7.2f}" for h, v in tab[t].items()))
OUT["etf_returns"] = tab
P("\n=== B. RELATIVE RETURNS (ratio basis, pp) ===")
PAIRS = [("RSP", "SPY", "equal- vs cap-weight S&P 500"), ("QQEW", "QQQ", "equal- vs cap-weight Nasdaq-100"),
         ("OEF", "SPY", "S&P 100 mega vs S&P 500"), ("MDY", "SPY", "S&P 400 mid vs S&P 500"),
         ("IJR", "SPY", "S&P 600 small vs S&P 500"), ("IWM", "SPY", "Russell 2000 vs S&P 500"),
         ("SOXX", "SPY", "semis vs S&P 500"), ("XLK", "SPY", "tech sector vs S&P 500")]
relt = {}
for a, b, lab in PAIRS:
    relt[f"{a}/{b}"] = {h: round(rel(a, b, d), 2) for h, d in HZ.items()}
    P(f"{a}/{b:5s}", "  ".join(f"{h}:{v:+6.2f}" for h, v in relt[f'{a}/{b}'].items()), " |", lab)
OUT["relative"] = relt
# sector scoreboard
P("\n=== C. SECTOR SPDRs (11, cap-weighted GICS sectors of the S&P 500) ===")
sec_sb = {}
for h, d in HZ.items():
    spy = tab["SPY"][h]
    pos = sum(1 for s in SECT if tab[s][h] > 0)
    beat = sum(1 for s in SECT if tab[s][h] > spy)
    rk = sorted(SECT, key=lambda s: tab[s][h])
    sec_sb[h] = {"positive": pos, "beat_SPY": beat, "SPY": spy, "best": [rk[-1], tab[rk[-1]][h]], "worst": [rk[0], tab[rk[0]][h]]}
    P(f"{h:4s} positive {pos:2d}/11  beat SPY {beat:2d}/11  SPY {spy:+6.2f}  best {rk[-1]} {tab[rk[-1]][h]:+6.2f}  worst {rk[0]} {tab[rk[0]][h]:+6.2f}")
OUT["sector_scoreboard"] = sec_sb

# VULCAN reconciliation: RSP/SPY 63-session relative return (mag7.py basis)
P("\n=== D. VULCAN S1 breadth leg reproduced (RSP/SPY 63-session, Adj Close, ratio) ===")
rs = (ea["RSP"] / ea["SPY"]).dropna()
s63 = ((rs / rs.shift(63) - 1) * 100).dropna()
s63 = s63.loc["2003-05-01":]
for d in ["2026-08-20", "2026-09-01", "2026-10-01", "2026-10-08", "2026-10-15", "2026-10-22", "2026-10-29", "2026-10-30"]:
    dd = refdate(s63.index, d)
    hist = s63.loc[:dd]
    pct = (hist < s63.loc[dd]).mean() * 100
    P(f"{dd.date()}  63d {s63.loc[dd]:+6.2f}pp  pctile(2003-05..date) {pct:5.1f}")
OUT["vulcan_63d_1030"] = round(float(s63.loc[D0]), 4)
OUT["vulcan_63d_1029"] = round(float(s63.loc[pd.Timestamp('2026-10-29')]), 4)
mn = s63.loc["2026-01-01":].idxmin()
P(f"2026 min of the 63d series: {s63.loc[mn]:+.2f}pp on {mn.date()}")
# RSP/SPY ratio level vs its own history
P(f"RSP/SPY ratio (Adj Close) 10/30 {rs.loc[D0]:.5f}; 52-wk range {rs.loc['2025-10-30':].min():.5f}-{rs.loc['2025-10-30':].max():.5f}; "
  f"min date {rs.loc['2025-10-30':].idxmin().date()} max date {rs.loc['2025-10-30':].idxmax().date()}")

# ---------------------------------------------------------------- constituents
close, adj, high, low = px["Close"], px["Adj Close"], px["High"], px["Low"]
have = [t for t in uni.yf_ticker if t in close.columns and close[t].notna().sum() > 0]
missing = [t for t in uni.yf_ticker if t not in have]
uni = uni[uni.yf_ticker.isin(have)].copy()
P(f"\n=== E. CONSTITUENT UNIVERSE: {len(have)} names with data; missing {len(missing)}: {missing}")
last_bar = close[have].apply(lambda s: s.last_valid_index())
lagging = last_bar[last_bar < D0]
P(f"names whose last bar is before 10/30: {len(lagging)} {list(lagging.index)[:20]}")
G = {"SP500": uni[uni["index"] == "SP500"].yf_ticker.tolist(),
     "SP400": uni[uni["index"] == "SP400"].yf_ticker.tolist(),
     "SP600": uni[uni["index"] == "SP600"].yf_ticker.tolist()}
G["SP1500"] = G["SP500"] + G["SP400"] + G["SP600"]
P({k: len(v) for k, v in G.items()})

sma50 = close.rolling(50, min_periods=50).mean()
sma200 = close.rolling(200, min_periods=200).mean()
a50 = (close > sma50).astype(float).where(sma50.notna() & close.notna())
a200 = (close > sma200).astype(float).where(sma200.notna() & close.notna())
chg = close / close.shift(1) - 1
adv = (chg > 0).astype(float).where(chg.notna())
dec = (chg < 0).astype(float).where(chg.notna())
phh = high.shift(1).rolling(251, min_periods=251).max()
pll = low.shift(1).rolling(251, min_periods=251).min()
nh = ((high >= phh).astype(float)).where(phh.notna() & high.notna())
nl = ((low <= pll).astype(float)).where(pll.notna() & low.notna())

daily = pd.DataFrame(index=close.index)
for g, names in G.items():
    daily[f"{g}_pct50"] = a50[names].mean(axis=1) * 100
    daily[f"{g}_n50"] = a50[names].notna().sum(axis=1)
    daily[f"{g}_pct200"] = a200[names].mean(axis=1) * 100
    daily[f"{g}_n200"] = a200[names].notna().sum(axis=1)
    daily[f"{g}_adv"] = adv[names].sum(axis=1)
    daily[f"{g}_dec"] = dec[names].sum(axis=1)
    daily[f"{g}_nh"] = nh[names].sum(axis=1)
    daily[f"{g}_nl"] = nl[names].sum(axis=1)
    daily[f"{g}_nhnl_n"] = nh[names].notna().sum(axis=1)
    daily[f"{g}_medchg"] = chg[names].median(axis=1) * 100
    daily[f"{g}_ewchg"] = chg[names].mean(axis=1) * 100
daily["SPX"] = pe["Close"]["^GSPC"].reindex(daily.index)
daily["SPY_tr"] = (pe["Adj Close"]["SPY"] / pe["Adj Close"]["SPY"].shift(1) - 1).reindex(daily.index) * 100
daily["RSP_SPY"] = rs.reindex(daily.index)
for g in G:
    daily[f"{g}_cumAD"] = (daily[f"{g}_adv"] - daily[f"{g}_dec"]).loc["2025-01-02":].cumsum()
daily = daily.loc["2025-01-02":]
daily.round(5).to_csv(os.path.join(R, "breadth_daily.csv"))

P("\n=== F. CONSTITUENT BREADTH SNAPSHOTS (share of names, %; NH/NL intraday 52-wk) ===")
KEY = ["2025-12-31", "2026-04-30", "2026-07-31", "2026-08-31", "2026-09-30", "2026-10-06", "2026-10-23", "2026-10-29", "2026-10-30"]
snap = {}
for g in G:
    P(f"-- {g}")
    snap[g] = {}
    for d in KEY:
        dd = refdate(daily.index, d)
        r = daily.loc[dd]
        snap[g][str(dd.date())] = {"pct50": round(r[f"{g}_pct50"], 1), "pct200": round(r[f"{g}_pct200"], 1),
                                   "nh": int(r[f"{g}_nh"]), "nl": int(r[f"{g}_nl"]), "adv": int(r[f"{g}_adv"]),
                                   "dec": int(r[f"{g}_dec"]), "n50": int(r[f"{g}_n50"]), "n200": int(r[f"{g}_n200"])}
        P(f"{dd.date()}  >50d {r[f'{g}_pct50']:5.1f}% (n={int(r[f'{g}_n50'])})  >200d {r[f'{g}_pct200']:5.1f}% (n={int(r[f'{g}_n200'])})  "
          f"NH {int(r[f'{g}_nh']):3d} NL {int(r[f'{g}_nl']):3d}  adv {int(r[f'{g}_adv']):4d} dec {int(r[f'{g}_dec']):4d}  SPX {r['SPX']:.2f}")
OUT["snapshots"] = snap
# weekly new highs/lows: names making >=1 new high / low during the window
P("\n-- names making at least one 52-wk high / low inside the window (intraday basis)")
win = {"wk 10/26-10/30": ("2026-10-26", "2026-10-30"), "wk 10/19-10/23": ("2026-10-19", "2026-10-23"),
       "Oct (10/1-10/30)": ("2026-10-01", "2026-10-30"), "Sep": ("2026-09-01", "2026-09-30"),
       "Aug": ("2026-08-01", "2026-08-31")}
wk = {}
for g in G:
    wk[g] = {}
    for lab, (a, b) in win.items():
        h_ = int((nh[G[g]].loc[a:b].max(axis=0) == 1).sum())
        l_ = int((nl[G[g]].loc[a:b].max(axis=0) == 1).sum())
        wk[g][lab] = [h_, l_]
    P(g, wk[g])
OUT["window_nhnl"] = wk

# ---------------------------------------------------------------- horizon participation (SP500)
P("\n=== G. S&P 500 PARTICIPATION BY HORIZON (constituent total returns) ===")
sp = uni[uni["index"] == "SP500"].set_index("yf_ticker")
shares = sp["shares_held"].astype(float)
try:
    semis = json.load(open(os.path.join(R, "semis.json")))["semis_sp500"]
except Exception:  # noqa: BLE001
    semis = []
semis_x = [t for t in semis if t not in MAG7]
part = {}
for h, d in HZ.items():
    r0 = refdate(adj.index, d)
    r = (adj[sp.index].loc[D0] / adj[sp.index].loc[r0] - 1) * 100
    r = r.dropna()
    w = (shares.reindex(r.index) * close[r.index].loc[r0])
    w = w / w.sum()
    cw = float((w * r).sum())
    spy = tab["SPY"][h]
    top10 = w.sort_values(ascending=False).index[:10].tolist()
    con = w * r
    grp = {"Mag7": float(con.reindex([t for t in MAG7 if t in con.index]).sum()),
           "SemisExMag7": float(con.reindex([t for t in semis_x if t in con.index]).sum()),
           "Top10wt": float(con.reindex(top10).sum())}
    grp["RestExMag7Semis"] = cw - grp["Mag7"] - grp["SemisExMag7"]
    top_pos = con.sort_values(ascending=False).head(10)
    part[h] = {"ref": str(r0.date()), "n": int(r.size), "SPY_tr": spy, "CW_const": round(cw, 2),
               "EW_mean": round(float(r.mean()), 2), "median": round(float(r.median()), 2),
               "pct_positive": round(float((r > 0).mean() * 100), 1),
               "pct_beat_SPY": round(float((r > spy).mean() * 100), 1),
               "xs_std": round(float(r.std()), 2),
               "contrib_pp": {k: round(v, 2) for k, v in grp.items()},
               "top10_contributors": {k: round(float(v), 3) for k, v in top_pos.items()},
               "top10_share_of_CW": round(float(top_pos.sum() / cw * 100), 1) if abs(cw) > 1e-9 else None}
    P(f"{h:4s} ref {r0.date()} n={r.size}  SPY {spy:+6.2f}  CW(const) {cw:+6.2f}  EW {r.mean():+6.2f}  median {r.median():+6.2f}  "
      f"%up {((r>0).mean()*100):5.1f}  %beat SPY {((r>spy).mean()*100):5.1f}  | contrib pp: Mag7 {grp['Mag7']:+.2f} semis(exMag7) {grp['SemisExMag7']:+.2f} "
      f"rest {grp['RestExMag7Semis']:+.2f} (top10-by-weight {grp['Top10wt']:+.2f})")
OUT["participation_sp500"] = part
P("semis set (S&P 500, from yfinance industry):", semis)

# participation for SP400 / SP600 (EW only, no shares basis)
for g in ["SP400", "SP600"]:
    P(f"-- {g} EW participation")
    for h, d in HZ.items():
        r0 = refdate(adj.index, d)
        r = ((adj[G[g]].loc[D0] / adj[G[g]].loc[r0] - 1) * 100).dropna()
        P(f"{h:4s} n={r.size} EW {r.mean():+6.2f} median {r.median():+6.2f} %up {((r>0).mean()*100):5.1f}")

# ---------------------------------------------------------------- Friday 10/30
P("\n=== H. FRIDAY 10/30 DECOMPOSITION ===")
d1 = pd.Timestamp("2026-10-29")
r1 = ((close.loc[D0] / close.loc[d1] - 1) * 100)
fri = {}
for g in G:
    rr = r1[G[g]].dropna()
    fri[g] = {"n": int(rr.size), "down": int((rr < 0).sum()), "up": int((rr > 0).sum()),
              "pct_down": round(float((rr < 0).mean() * 100), 1), "median": round(float(rr.median()), 2),
              "EW": round(float(rr.mean()), 2), "down_gt2pct": int((rr < -2).sum()), "down_gt5pct": int((rr < -5).sum())}
    P(g, fri[g])
w1 = (shares * close[sp.index].loc[d1]).dropna()
w1 = w1 / w1.sum()
c1 = (w1 * r1.reindex(w1.index)).dropna()
cw1 = float(c1.sum())
fri["SP500_CW_const"] = round(cw1, 3)
grp1 = {"Mag7": float(c1.reindex([t for t in MAG7 if t in c1.index]).sum()),
        "SemisExMag7": float(c1.reindex([t for t in semis_x if t in c1.index]).sum())}
grp1["Rest"] = cw1 - grp1["Mag7"] - grp1["SemisExMag7"]
fri["SP500_contrib_pp"] = {k: round(v, 3) for k, v in grp1.items()}
P(f"S&P 500 CW(const) price return {cw1:+.3f}% vs ^GSPC {tab['^GSPC']['1d']:+.2f}% | contributions pp: {fri['SP500_contrib_pp']}")
P("largest negative contributors:", {k: round(float(v), 3) for k, v in c1.sort_values().head(12).items()})
P("largest positive contributors:", {k: round(float(v), 3) for k, v in c1.sort_values().tail(6).items()})
ex = [t for t in sp.index if t not in MAG7 and t not in semis_x]
rr_ex = r1.reindex(ex).dropna()
fri["SP500_exMag7Semis"] = {"n": int(rr_ex.size), "pct_down": round(float((rr_ex < 0).mean() * 100), 1),
                            "median": round(float(rr_ex.median()), 2), "EW": round(float(rr_ex.mean()), 2)}
P("S&P 500 ex Mag7 & semis:", fri["SP500_exMag7Semis"])
P("-- by GICS sector (S&P 500): n, %down, EW, median, CW contribution pp")
secf = {}
for s, sub in sp.groupby("gics_sector"):
    t = [x for x in sub.index if x in r1.index]
    rr = r1.reindex(t).dropna()
    secf[s] = {"n": int(rr.size), "pct_down": round(float((rr < 0).mean() * 100), 1), "EW": round(float(rr.mean()), 2),
               "median": round(float(rr.median()), 2), "contrib_pp": round(float(c1.reindex(t).sum()), 3)}
for s, v in sorted(secf.items(), key=lambda kv: kv[1]["contrib_pp"]):
    P(f"  {s:24s} {v}")
fri["SP500_sectors"] = secf
semr = r1.reindex([t for t in semis if t in r1.index]).dropna()
P("semis 10/30 (S&P 500 members):", {k: round(float(v), 2) for k, v in semr.sort_values().items()})
OUT["friday"] = fri

# ---------------------------------------------------------------- base rates for a day like 10/30
P("\n=== I. BASE RATES: how narrow was 10/30 for a day of its size? ===")
spy_d = (pe["Adj Close"]["SPY"] / pe["Adj Close"]["SPY"].shift(1) - 1) * 100
rsp_d = (pe["Adj Close"]["RSP"] / pe["Adj Close"]["RSP"].shift(1) - 1) * 100
relrs = (((pe["Adj Close"]["RSP"] / pe["Adj Close"]["SPY"]) / (pe["Adj Close"]["RSP"] / pe["Adj Close"]["SPY"]).shift(1)) - 1) * 100
dfb = pd.DataFrame({"spy": spy_d, "rsp": rsp_d, "rel": relrs}).dropna().loc["2003-05-01":]
today = dfb.loc[D0]
hist = dfb.loc[:"2026-10-29"]
for lo_, hi_ in [(-2.3, -1.3), (-99, -1.5)]:
    sub = hist[(hist.spy >= lo_) & (hist.spy <= hi_)]
    pct = (sub.rel < today.rel).mean() * 100
    P(f"SPY day in [{lo_},{hi_}]%: n={len(sub)} days since 2003-05; RSP-vs-SPY rel median {sub.rel.median():+.2f}pp, "
      f"p90 {sub.rel.quantile(.9):+.2f}, max {sub.rel.max():+.2f} on {sub.rel.idxmax().date()} | 10/30 rel {today.rel:+.2f}pp -> pctile {pct:.1f}")
    OUT[f"base_rsp_{lo_}_{hi_}"] = {"n": int(len(sub)), "median": round(float(sub.rel.median()), 2),
                                   "p90": round(float(sub.rel.quantile(.9)), 2), "today": round(float(today.rel), 2),
                                   "pctile": round(float(pct), 1)}
    top = sub.sort_values("rel", ascending=False).head(6)
    P("   most equal-weight-favourable such days:", [(str(i.date()), round(r.spy, 2), round(r.rel, 2)) for i, r in top.iterrows()])
qq = (pe["Adj Close"]["QQQ"] / pe["Adj Close"]["QQQ"].shift(1) - 1) * 100
qrel = (((pe["Adj Close"]["QQEW"] / pe["Adj Close"]["QQQ"]) / (pe["Adj Close"]["QQEW"] / pe["Adj Close"]["QQQ"]).shift(1)) - 1) * 100
dq = pd.DataFrame({"qqq": qq, "rel": qrel}).dropna()
tq = dq.loc[D0]
hq = dq.loc[:"2026-10-29"]
subq = hq[(hq.qqq <= -2.5)]
P(f"QQQ day <= -2.5%: n={len(subq)} since {hq.index.min().date()}; QQEW-vs-QQQ rel median {subq.rel.median():+.2f}pp | 10/30 rel {tq.rel:+.2f}pp -> pctile {(subq.rel < tq.rel).mean()*100:.1f}")
OUT["base_qqew"] = {"n": int(len(subq)), "median": round(float(subq.rel.median()), 2), "today": round(float(tq.rel), 2),
                    "pctile": round(float((subq.rel < tq.rel).mean() * 100), 1)}
# constituent base rate: % of S&P 500 decliners on SPY days of similar size (2025-01..2026-10-29, today's members)
dd_ = daily.loc[:"2026-10-29"]
dd_ = dd_[(dd_.SPY_tr <= -1.3)]
pdn = dd_["SP500_dec"] / (dd_["SP500_adv"] + dd_["SP500_dec"]) * 100
P(f"S&P 500 days with SPY <= -1.3% (2025-01-02..10/29, n={len(dd_)}): % of members down median {pdn.median():.1f}, min {pdn.min():.1f} on {pdn.idxmin().date()}; "
  f"median-stock move median {dd_['SP500_medchg'].median():+.2f}% | 10/30: {fri['SP500']['pct_down']}% down, median {fri['SP500']['median']:+.2f}%")
OUT["base_const"] = {"n": int(len(dd_)), "pct_down_median": round(float(pdn.median()), 1), "pct_down_min": round(float(pdn.min()), 1),
                     "pct_down_min_date": str(pdn.idxmin().date()),
                     "list": [(str(i.date()), round(float(dd_.loc[i, 'SPY_tr']), 2), round(float(pdn.loc[i]), 1), round(float(dd_.loc[i, 'SP500_medchg']), 2)) for i in dd_.index]}
P("   days:", OUT["base_const"]["list"])

# ---------------------------------------------------------------- divergence at index highs
P("\n=== J. DID BREADTH CONFIRM THE INDEX HIGHS? (S&P 500 record closes, 2026) ===")
spx = pe["Close"]["^GSPC"].dropna()
rec = spx[spx >= spx.cummax()]
rec26 = rec.loc["2026-01-01":]
P(f"record closes in 2026: {len(rec26)}; last record {rec26.index[-1].date()} {rec26.iloc[-1]:.2f}; all-time closing high in data {spx.max():.2f} on {spx.idxmax().date()}")
last_by_month = rec26.groupby(rec26.index.to_period("M")).tail(1)
div = []
for d, v in last_by_month.items():
    r_ = daily.loc[d]
    div.append({"date": str(d.date()), "SPX": round(float(v), 2), "pct50": round(r_["SP500_pct50"], 1),
                "pct200": round(r_["SP500_pct200"], 1), "nh": int(r_["SP500_nh"]), "nl": int(r_["SP500_nl"]),
                "cumAD": int(r_["SP500_cumAD"]), "RSP_SPY": round(float(r_["RSP_SPY"]), 5),
                "SP1500_pct200": round(r_["SP1500_pct200"], 1)})
    P(div[-1])
OUT["record_highs"] = div
# A/D line vs SPX: highs since 2026-07-31
ad = daily["SP500_cumAD"]
P(f"S&P 500 cum A/D (base 2025-01-02): max {ad.max():.0f} on {ad.idxmax().date()}; at 10/06 {ad.loc['2026-10-06']:.0f}; at 10/30 {ad.loc[D0]:.0f}")
ad15 = daily["SP1500_cumAD"]
P(f"S&P 1500 cum A/D (base 2025-01-02): max {ad15.max():.0f} on {ad15.idxmax().date()}; at 10/06 {ad15.loc['2026-10-06']:.0f}; at 10/30 {ad15.loc[D0]:.0f}")
OUT["cumAD"] = {"sp500_max": [str(ad.idxmax().date()), int(ad.max())], "sp500_1006": int(ad.loc["2026-10-06"]), "sp500_1030": int(ad.loc[D0]),
                "sp1500_max": [str(ad15.idxmax().date()), int(ad15.max())], "sp1500_1006": int(ad15.loc["2026-10-06"]), "sp1500_1030": int(ad15.loc[D0])}
# peaks of pct50 / pct200 in 2026
for c in ["SP500_pct50", "SP500_pct200", "SP1500_pct50", "SP1500_pct200"]:
    s = daily[c].loc["2026-01-01":]
    P(f"{c}: 2026 max {s.max():.1f} on {s.idxmax().date()}, min {s.min():.1f} on {s.idxmin().date()}, 10/30 {s.loc[D0]:.1f}")

# ---------------------------------------------------------------- per-stock snapshot
snapdf = pd.DataFrame({
    "index": uni.set_index("yf_ticker")["index"], "sector": uni.set_index("yf_ticker")["gics_sector"],
    "fund_weight_pct": uni.set_index("yf_ticker")["fund_weight_pct"],
    "close_1030": close.loc[D0], "sma50": sma50.loc[D0], "sma200": sma200.loc[D0],
    "above50": a50.loc[D0], "above200": a200.loc[D0], "nh_1030": nh.loc[D0], "nl_1030": nl.loc[D0],
    "r1d_px": r1})
for h in ["1w", "1m", "3m", "YTD"]:
    r0 = refdate(adj.index, HZ[h])
    snapdf[f"r{h}_tr"] = (adj.loc[D0] / adj.loc[r0] - 1) * 100
snapdf = snapdf.loc[[t for t in uni.yf_ticker]]
snapdf.round(4).to_csv(os.path.join(R, "stock_snapshot.csv"))
json.dump(OUT, open(os.path.join(R, "results.json"), "w"), indent=1, default=str)
open(os.path.join(R, "report.txt"), "w").write("\n".join(lines) + "\n")
P("\nwritten: breadth_daily.csv stock_snapshot.csv results.json report.txt")
