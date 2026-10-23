"""Backdrop at the start of every bank/tech see-saw episode vs today (10/22 close).

Episodes: KRE/QQQ signals 2006+ (../episode_study/episodes.csv) plus pre-2006 signals from the validated stand-ins
(../deep_1985: ^BKX/^NDX and French EW Banks/^NDX; merged when within 20 sessions, earliest kept).
Data: FRED (BAA10Y Baa-10y credit spread, T10Y3M curve, DFF fed funds, DCOILWTICO WTI) pulled to fred_*.csv;
yfinance ^GSPC and DX-Y.NYB (dollar) -> mkt.csv; VIX ../deep_1985/vix_1990.csv; 10y ../deep_1985/hist_idx.csv.
'Story' labels are TERRY's recollection of the period, NOT sourced — context only.
Run: .venv/bin/python -I context.py -> RESULTS.md
"""
import io, os, time, urllib.request
import numpy as np
import pandas as pd
import yfinance as yf

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.dirname(HERE)

def fred(sid):
    path = os.path.join(HERE, f"fred_{sid}.csv")
    if not os.path.exists(path):
        raw = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", timeout=60).read()
        open(path, "wb").write(raw)
    s = pd.read_csv(path, index_col=0, parse_dates=True).iloc[:, 0]
    return pd.to_numeric(s, errors="coerce").dropna()

mp = os.path.join(HERE, "mkt.csv")
if not os.path.exists(mp):
    for i in range(3):
        try:
            m = yf.download(["^GSPC", "DX-Y.NYB"], start="1985-01-01", progress=False, auto_adjust=True)["Close"]; break
        except Exception:
            time.sleep(5)
    m.to_csv(mp)
m = pd.read_csv(mp, index_col=0, parse_dates=True)
vix = pd.read_csv(os.path.join(UP, "deep_1985", "vix_1990.csv"), index_col=0, parse_dates=True).iloc[:, 0]
tnx = pd.read_csv(os.path.join(UP, "deep_1985", "hist_idx.csv"), index_col=0, parse_dates=True)["^TNX"].dropna()
baa, curve, ff, oil = fred("BAA10Y"), fred("T10Y3M"), fred("DFF"), fred("DCOILWTICO")
spx, dxy = m["^GSPC"].dropna(), m["DX-Y.NYB"].dropna()

# ---- episode list
k = pd.read_csv(os.path.join(UP, "episode_study", "episodes.csv"), parse_dates=["signal"])
k = k[k["signal"] < "2026-10-22"]
ev = [(d, "KRE/QQQ", r["dir"].replace("KRE", "banks").replace("QQQ", "tech"), r["class20"], bool(r["joint_fall40"]), bool(r["joint_rally40"]))
      for d, (_, r) in zip(k["signal"], k.iterrows())]
pre = []
for f, lab in (("episodes_deep.csv", "BKX/NDX"), ("episodes_deep_ffew.csv", "FF/NDX")):
    e = pd.read_csv(os.path.join(UP, "deep_1985", f), parse_dates=["signal"])
    for _, r in e[e["signal"] < "2006-06-22"].iterrows():
        pre.append((r["signal"], lab, r["dir"], r["class20"], bool(r["jf5"]), bool(r["jr5"])))
pre.sort(key=lambda x: x[0]); merged = []
for p_ in pre:
    if merged and (p_[0] - merged[-1][0]).days <= 28:
        merged[-1] = (merged[-1][0], merged[-1][1] + "+" + p_[1].split("/")[0], *merged[-1][2:]); continue
    merged.append(p_)
# post-2006 BKX/NDX signals with no KRE/QQQ signal within 28 days (incl. the 2021-11-23 joint-fall counterexample)
bk = pd.read_csv(os.path.join(UP, "deep_1985", "episodes_deep.csv"), parse_dates=["signal"])
kd = [x[0] for x in ev]
extra = [(r["signal"], "BKX/NDX only", r["dir"], r["class20"], bool(r["jf5"]), bool(r["jr5"]))
         for _, r in bk[bk["signal"] >= "2006-06-22"].iterrows() if all(abs((r["signal"] - d).days) > 28 for d in kd)]
ev = sorted(merged + ev + extra, key=lambda x: x[0]) + [(pd.Timestamp("2026-10-22"), "KRE/QQQ", "banks over tech", "NOW", None, None)]

STORY = {  # TERRY recollection, unsourced
    "1995-08": "Bank merger wave (Chase–Chemical announced late Aug 1995); Fed easing after the 1994 hikes",
    "1995-04": "Soft landing after the 1994 Fed hikes",
    "1997-06": "Bank M&A boom; weeks before the Asian crisis",
    "2013-07": "Taper-tantrum aftermath: rising yields lift banks",
    "2016-12": "Post-election reflation trade",
    "2017-06": "Fed hike + stress-test / deregulation hopes",
    "2017-11": "Tax-cut bill advancing",
    "2019-02": "Fed's January 2019 pause",
    "2020-07": "COVID-era megacap tech rally",
    "2020-08": "COVID-era megacap tech rally",
    "2020-11": "Vaccine news; reopening rotation",
    "2021-01": "Georgia runoffs; reflation trade",
    "2021-03": "Bond sell-off; reflation peak",
    "2021-06": "Fed's hawkish June dot plot",
    "2021-11": "Omicron + Powell retires 'transitory' (Fed turns hawkish)",
    "2017-07": "Summer 2017 (no clear driver recalled)",
    "2017-08": "North Korea tensions (Aug 2017)",
    "2024-03": "NYCB aftermath; regional-bank stress",
    "2024-07": "Cool CPI; small-cap rotation",
    "2024-12": "Post-election bank rally fades",
    "2026-10": "NOW: AI/chip sell-off; credit widening; falling 10y",
}

def asof(s, d):
    s = s[s.index <= d]
    return s.iloc[-1] if len(s) else np.nan

def chg(s, d, n, pct=False):
    s = s[s.index <= d]
    if len(s) <= n:
        return np.nan
    return (s.iloc[-1] / s.iloc[-1 - n] - 1) * 100 if pct else s.iloc[-1] - s.iloc[-1 - n]

rows = []
for d, src, dirn, cls, jf, jr in ev:
    sp = spx[spx.index <= d]
    rows.append({
        "signal": d.date(), "src": src, "dir": dirn, "story": STORY.get(d.strftime("%Y-%m"), "—"),
        "VIX": asof(vix, d), "VIX_chg20": chg(vix, d, 20),
        "10y": asof(tnx, d), "10y_chg20": chg(tnx, d, 20),
        "curve": asof(curve, d), "fed": asof(ff, d), "fed_chg6m": chg(ff, d, 126),
        "baa": asof(baa, d), "baa_chg60bp": chg(baa, d, 60) * 100,
        "oil60": chg(oil, d, 60, True), "dxy60": chg(dxy, d, 60, True),
        "spx_vs200": (sp.iloc[-1] / sp.iloc[-200:].mean() - 1) * 100, "spx_dd": (sp.iloc[-1] / sp.iloc[-252:].max() - 1) * 100,
        "class20": cls, "both_fell": jf, "both_rose": jr,
    })
df = pd.DataFrame(rows)
df.to_csv(os.path.join(HERE, "context.csv"), index=False)

# ---- closest analogs to NOW (z-scored over all episodes incl. now)
feat = ["VIX", "10y_chg20", "curve", "fed_chg6m", "baa_chg60bp", "oil60", "spx_vs200", "spx_dd"]
z = (df[feat] - df[feat].mean()) / df[feat].std()
now = z.iloc[-1]
df["distance"] = np.sqrt(((z - now) ** 2).sum(axis=1))

f1 = lambda v, nd=1: "—" if pd.isna(v) else f"{v:.{nd}f}"
s1 = lambda v, nd=1: "—" if pd.isna(v) else f"{v:+.{nd}f}"
def fed_word(c):
    return "—" if pd.isna(c) else ("cutting" if c <= -0.2 else "hiking" if c >= 0.2 else "on hold")
L = ["# Backdrop at each bank/tech see-saw episode vs today (TERRY, 2026-10-23)\n",
     "Values at the signal close. Credit = Moody's Baa minus 10y (FRED BAA10Y; the ICE high-yield series on FRED only reaches back to 2023). "
     "Fed direction = fed funds change over ~6 months (±0.2 pts). 'Story' = TERRY recollection, unsourced. Outcome columns from the earlier studies (40 sessions).\n",
     "| Signal | Leader | Story | VIX (20d chg) | 10y (20d chg) | Curve 10y−3m | Fed | Baa spread (60d chg) | Oil 60d | Dollar 60d | S&P vs 200d / off high | After: @20 · both fell · both rose |",
     "|---|---|---|---|---|---:|---|---|---:|---:|---|---|"]
for _, r in df.iterrows():
    out = "NOW" if r["class20"] == "NOW" else f"{r['class20']} · {'YES' if r['both_fell'] else 'no'} · {'YES' if r['both_rose'] else 'no'}"
    L.append(f"| {'**' if out=='NOW' else ''}{r['signal']}{'**' if out=='NOW' else ''}{' (BKX only)' if r['src']=='BKX/NDX only' else ''} | {r['dir'].split(' over')[0]} | {r['story']} | {f1(r['VIX'])} ({s1(r['VIX_chg20'])}) | "
             f"{f1(r['10y'],2)} ({s1(r['10y_chg20'],2)}) | {s1(r['curve'],2)} | {fed_word(r['fed_chg6m'])} ({f1(r['fed'],2)}) | {f1(r['baa'],2)} ({s1(r['baa_chg60bp'],0)}bp) | "
             f"{s1(r['oil60'],0)}% | {s1(r['dxy60'],1)}% | {s1(r['spx_vs200'],1)}% / {s1(r['spx_dd'],1)}% | {out} |")
past = df.iloc[:-1]
L.append("\n## What the past episodes had in common (medians, " + str(len(past)) + " episodes) vs NOW\n")
L.append("| Measure | Past median | Past range | NOW |\n|---|---:|---|---:|")
for c, lab, nd in (("VIX", "VIX", 1), ("10y_chg20", "10y change, 20d (pts)", 2), ("curve", "Curve 10y−3m (pts)", 2), ("fed_chg6m", "Fed funds change, 6m (pts)", 2),
                   ("baa_chg60bp", "Baa spread change, 60d (bp)", 0), ("oil60", "Oil, 60d %", 0), ("dxy60", "Dollar, 60d %", 1),
                   ("spx_vs200", "S&P vs 200-day avg %", 1), ("spx_dd", "S&P off 52-week high %", 1)):
    L.append(f"| {lab} | {s1(past[c].median(), nd)} | {s1(past[c].min(), nd)} to {s1(past[c].max(), nd)} | **{s1(df[c].iloc[-1], nd)}** |")
L.append("\n## Closest past backdrops to NOW (distance across VIX, 10y move, curve, Fed direction, credit move, oil, S&P trend)\n")
L.append("| Rank | Signal | Story | Distance | What followed (@20 · both fell · both rose) |\n|---:|---|---|---:|---|")
for n, (_, r) in enumerate(past.sort_values("distance").head(5).iterrows(), 1):
    L.append(f"| {n} | {r['signal']} | {r['story']} | {r['distance']:.2f} | {r['class20']} · {'YES' if r['both_fell'] else 'no'} · {'YES' if r['both_rose'] else 'no'} |")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
