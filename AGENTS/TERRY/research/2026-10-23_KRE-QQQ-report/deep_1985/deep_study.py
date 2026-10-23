"""Deep push: the KRE/QQQ episode rule run back to 1985 on stand-in series.

Bank stand-ins: Ken French 49-industry 'Banks' daily (equal- and value-weighted, CRSP 202608, file
raw_french/49_Industry_Portfolios_Daily.csv) and the KBW Bank Index ^BKX (1993+). Tech: ^NDX (QQQ's index).
STEP 1 (validation, 2006-06-22 -> 2026-08-31 overlap): does each stand-in vs ^NDX reproduce KRE vs QQQ?
STEP 2 (deep): episode rule (signal = first close with 20-session corr <= -0.2357, the 10/22 KRE/QQQ reading;
re-arm above 0), outcomes from the signal close, 1985-10 -> 2026-08.
STEP 3 (precursor test): big joint declines (both legs >= 10% below a start close within 40 sessions);
was a see-saw signal in the 60 sessions before? vs the base rate of a signal in any 60-session span.
Run: .venv/bin/python -I deep_study.py  -> RESULTS.md
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
TH = -0.2357

# ---------------- data
def french(section_title):
    path = os.path.join(HERE, "raw_french", "49_Industry_Portfolios_Daily.csv")
    lines = open(path, encoding="latin-1").read().splitlines()
    start = next(i for i, l in enumerate(lines) if section_title in l)
    header = [h.strip() for h in lines[start + 1].split(",")]
    rows = []
    for l in lines[start + 2:]:
        if not l.strip() or not l.strip()[0].isdigit():
            break
        rows.append([c.strip() for c in l.split(",")])
    d = pd.DataFrame(rows, columns=["date"] + header[1:])
    s = pd.to_numeric(d["Banks"]).replace([-99.99, -999], np.nan) / 100
    s.index = pd.to_datetime(d["date"], format="%Y%m%d")
    return s

px = pd.read_csv(os.path.join(HERE, "hist_idx.csv"), index_col=0, parse_dates=True)
R = pd.DataFrame({
    "FF_EW_Banks": french("Average Equal Weighted Returns -- Daily"),
    "FF_VW_Banks": french("Average Value Weighted Returns -- Daily"),
})
for c in ("^NDX", "^BKX", "KRE", "QQQ"):
    R[c] = px[c].pct_change(fill_method=None)
R["TNX"] = px["^TNX"].reindex(R.index).ffill()
R = R[R.index <= "2026-08-31"]  # French file ends 2026-08 (CRSP 202608)

def corr20(a, b):
    x = R[[a, b]].dropna()
    return x[a].rolling(20).corr(x[b])

def signals(c, th=TH):
    out, armed = [], True
    for d, v in c.items():
        if np.isnan(v):
            continue
        if armed and v <= th + 1e-12:
            out.append(d); armed = False
        elif not armed and v > 0:
            armed = True
    return out

L = ["# Deep push — KRE/QQQ see-saw episodes back to 1985 on stand-in series (TERRY, 2026-10-23)\n",
     f"Threshold = the 10/22 KRE/QQQ 20-session correlation ({TH}); re-arm above 0. French file ends 2026-08-31, so the deep study ends there. "
     "Stand-ins: Ken French 'Banks' industry portfolio (equal- and value-weighted; all US banks), KBW Bank Index ^BKX (large banks, 1993+); tech = ^NDX.\n"]

# ---------------- STEP 1 validation
ov = (R.index >= "2006-06-23") & (R.index <= "2026-08-31")
ref_c = corr20("KRE", "QQQ")
ref_sig = signals(ref_c[ref_c.index <= "2026-08-31"])
L.append("## Step 1 — do the stand-ins reproduce KRE vs QQQ? (overlap 2006-06 → 2026-08)\n")
L.append(f"Reference KRE vs QQQ: {len(ref_sig)} signals in the overlap.\n")
L.append("| Stand-in pair | Daily-return corr of bank leg with KRE | Corr of the 20d-corr series with KRE/QQQ's | Signals | Matched to a KRE/QQQ signal (±10 sessions) | KRE/QQQ signals recovered |\n|---|---:|---:|---:|---:|---:|")
cand = {}
for b in ("FF_EW_Banks", "FF_VW_Banks", "^BKX"):
    x = R.loc[ov, [b, "KRE"]].dropna()
    rc = x[b].corr(x["KRE"])
    c = corr20(b, "^NDX")
    cc = pd.concat([c, ref_c], axis=1).loc["2006-06-23":"2026-08-31"].dropna()
    s_ov = [d for d in signals(c) if pd.Timestamp("2006-06-23") <= d <= pd.Timestamp("2026-08-31")]
    pos = {d: i for i, d in enumerate(R.index)}
    match = sum(any(abs(pos[d] - pos[r]) <= 10 for r in ref_sig) for d in s_ov)
    rec = sum(any(abs(pos[d] - pos[r]) <= 10 for d in s_ov) for r in ref_sig)
    cand[b] = (rc, cc.iloc[:, 0].corr(cc.iloc[:, 1]), len(s_ov), match, rec)
    L.append(f"| {b} vs ^NDX | {rc:.2f} | {cc.iloc[:,0].corr(cc.iloc[:,1]):.2f} | {len(s_ov)} | {match} of {len(s_ov)} | {rec} of {len(ref_sig)} |")
best = max(cand, key=lambda b: (cand[b][4] + cand[b][3] - abs(cand[b][2] - len(ref_sig)), cand[b][1]))
L.append(f"\n**Chosen stand-in: {best} vs ^NDX** (best signal agreement with KRE/QQQ over the overlap).\n")

# ---------------- STEP 2 deep episodes
def run_episodes(bank, tech, start, th=TH):
    x = R[[bank, tech, "TNX"]].dropna(subset=[bank, tech])
    x = x[x.index >= start]
    lvl_b = (1 + x[bank]).cumprod(); lvl_t = (1 + x[tech]).cumprod()
    c = x[bank].rolling(20).corr(x[tech])
    idx = list(x.index); pos = {d: i for i, d in enumerate(idx)}
    rows = []
    for d in signals(c, th):
        i = pos[d]
        if i < 20:
            continue
        ratio = lvl_b / lvl_t
        dirn = 1 if ratio.iloc[i] / ratio.iloc[i - 20] > 1 else -1
        row = {"signal": d.date(), "dir": "banks over tech" if dirn > 0 else "tech over banks",
               "tnx20": x["TNX"].iloc[i] - x["TNX"].iloc[i - 20]}
        for h in (20, 40):
            j = i + h
            row[f"B+{h}"] = lvl_b.iloc[j] / lvl_b.iloc[i] - 1 if j < len(idx) else np.nan
            row[f"T+{h}"] = lvl_t.iloc[j] / lvl_t.iloc[i] - 1 if j < len(idx) else np.nan
        j = i + 20
        rd = dirn * (ratio.iloc[j] / ratio.iloc[i] - 1) if j < len(idx) else np.nan
        row["class20"] = np.nan if np.isnan(rd) else ("CONTINUED" if rd >= .03 else "SNAP-BACK" if rd <= -.03 else "FLAT")
        w = slice(i + 1, i + 41)
        bd = lvl_b.iloc[w] / lvl_b.iloc[i] - 1; td = lvl_t.iloc[w] / lvl_t.iloc[i] - 1
        row["complete"] = len(bd) == 40
        row["jf5"] = bool((bd <= -.05).any() and (td <= -.05).any())
        row["jf10"] = bool((bd <= -.10).any() and (td <= -.10).any())
        row["jr5"] = bool((bd >= .05).any() and (td >= .05).any())
        row["worstB"] = bd.min(); row["worstT"] = td.min()
        cc = c.iloc[i + 1:]; up = cc[cc > 0]
        row["runway"] = pos[up.index[0]] - i if len(up) else np.nan
        f5b = (lvl_b.shift(-5) / lvl_b - 1).iloc[i + 1:i + 16]; f5t = (lvl_t.shift(-5) / lvl_t - 1).iloc[i + 1:i + 16]
        row["dropB3"] = bool((f5b <= -.03).any()); row["dropT3"] = bool((f5t <= -.03).any())
        rows.append(row)
    return pd.DataFrame(rows), x, c, lvl_b, lvl_t

ep, X, C, LB, LT = run_episodes(best, "^NDX", "1985-10-01")
ep.to_csv(os.path.join(HERE, "episodes_deep.csv"), index=False)
p = lambda v: "—" if pd.isna(v) else f"{v*100:+.1f}%"
L.append(f"## Step 2 — every episode, {best} vs ^NDX, {X.index[0].date()} → {X.index[-1].date()} ({len(X)} sessions)\n")
L.append("| Signal | Direction | 10y prior 20d | Banks +20 | Tech +20 | Class @20 | Banks +40 | Tech +40 | Worst banks / tech in 40d | Both ≥5% down | Both ≥10% down | Both ≥5% up | Runway |\n|---|---|---:|---:|---:|---|---:|---:|---|---|---|---|---:|")
for _, e in ep.iterrows():
    L.append(f"| {e['signal']} | {e['dir']} | {e['tnx20']:+.2f} | {p(e['B+20'])} | {p(e['T+20'])} | {e['class20'] if isinstance(e['class20'], str) else '—'} | "
             f"{p(e['B+40'])} | {p(e['T+40'])} | {p(e['worstB'])} / {p(e['worstT'])} | {'YES' if e['jf5'] else 'no'} | {'YES' if e['jf10'] else 'no'} | "
             f"{'YES' if e['jr5'] else 'no'} | {'—' if pd.isna(e['runway']) else int(e['runway'])} |")
done = ep[ep["complete"]]
pre = done[pd.to_datetime(done["signal"]) < "2006-06-22"]; post = done[pd.to_datetime(done["signal"]) >= "2006-06-22"]

def summ(d, label):
    cl = d["class20"].value_counts()
    return (f"| {label} | {len(d)} | {int(cl.get('CONTINUED',0))}/{int(cl.get('FLAT',0))}/{int(cl.get('SNAP-BACK',0))} | {int(d['jf5'].sum())} | {int(d['jf10'].sum())} | "
            f"{int(d['jr5'].sum())} | {int(d['dropB3'].sum())} | {int(d['dropT3'].sum())} | {d['runway'].median():.0f} |")
L.append("\n## Summary (complete 40-session windows)\n")
L.append("| Period | Episodes | Class @20 (C/F/S) | Both ≥5% down in 40d | Both ≥10% down | Both ≥5% up | Banks ≥3% 5-day drop | Tech ≥3% 5-day drop | Median runway |\n|---|---:|---|---:|---:|---:|---:|---:|---:|")
L.append(summ(pre, "1985 → mid-2006 (NEW)")); L.append(summ(post, "mid-2006 → 2026-08 (stand-in)")); L.append(summ(done, "All"))
L.append("\n| Threshold sensitivity (all, complete) | Episodes | Both ≥5% down in 40d | Both ≥10% down | Both ≥5% up |\n|---:|---:|---:|---:|---:|")
for th in (-0.15, -0.20, TH, -0.30):
    e2 = run_episodes(best, "^NDX", "1985-10-01", th)[0]; e2 = e2[e2["complete"]]
    L.append(f"| {th:.2f} | {len(e2)} | {int(e2['jf5'].sum())} | {int(e2['jf10'].sum())} | {int(e2['jr5'].sum())} |")

# ---------------- STEP 3 precursor test
idx = list(X.index); pos = {d: i for i, d in enumerate(idx)}
sig_i = [pos[pd.Timestamp(s)] for s in ep["signal"]]
jd, i = [], 20
while i < len(idx) - 40:
    bd = LB.iloc[i + 1:i + 41] / LB.iloc[i] - 1; td = LT.iloc[i + 1:i + 41] / LT.iloc[i] - 1
    if (bd <= -.10).any() and (td <= -.10).any():
        jd.append(i); i += 60
    else:
        i += 1
L.append(f"\n## Step 3 — did a see-saw come BEFORE big joint declines? ({best} vs ^NDX)\n")
L.append("Joint decline = both legs ≥10% below a start close within 40 sessions (first qualifying start; next search 60 sessions later).\n")
L.append("| Joint decline start | Banks worst 40d | Tech worst 40d | 20d corr at start | See-saw signal in prior 60 sessions? |\n|---|---:|---:|---:|---|")
hit = 0
for i in jd:
    bd = (LB.iloc[i + 1:i + 41] / LB.iloc[i] - 1).min(); td = (LT.iloc[i + 1:i + 41] / LT.iloc[i] - 1).min()
    prior = [s for s in sig_i if i - 60 <= s <= i]
    hit += bool(prior)
    L.append(f"| {idx[i].date()} | {p(bd)} | {p(td)} | {C.iloc[i]:+.2f} | {'YES (' + str(idx[prior[-1]].date()) + ')' if prior else 'no'} |")
cov = np.zeros(len(idx), bool)
for s in sig_i:
    cov[s:min(s + 61, len(idx))] = True
L.append(f"\n**{hit} of {len(jd)} joint declines had a see-saw signal in the prior 60 sessions; base rate (any session with a signal in its prior 60): {cov[20:].mean()*100:.0f}%.**")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))

# ---------------- STEP 4 robustness: French equal-weighted Banks vs ^NDX from 1985 (reaches pre-1993)
L.append("\n## Step 4 — robustness: FF_EW_Banks vs ^NDX from 1985 (the only stand-in that reaches 1985–1993)\n")
e4, X4, C4, LB4, LT4 = run_episodes("FF_EW_Banks", "^NDX", "1985-10-01")
e4.to_csv(os.path.join(HERE, "episodes_deep_ffew.csv"), index=False)
L.append("| Signal | Direction | Banks +20 | Tech +20 | Class @20 | Worst banks / tech in 40d | Both ≥5% down | Both ≥10% down | Both ≥5% up | Runway |\n|---|---|---:|---:|---|---|---|---|---|---:|")
for _, e in e4.iterrows():
    L.append(f"| {e['signal']} | {e['dir']} | {p(e['B+20'])} | {p(e['T+20'])} | {e['class20'] if isinstance(e['class20'], str) else '—'} | "
             f"{p(e['worstB'])} / {p(e['worstT'])} | {'YES' if e['jf5'] else 'no'} | {'YES' if e['jf10'] else 'no'} | {'YES' if e['jr5'] else 'no'} | "
             f"{'—' if pd.isna(e['runway']) else int(e['runway'])} |")
d4 = e4[e4["complete"]]
L.append("\n| Period | Episodes | Class @20 (C/F/S) | Both ≥5% down in 40d | Both ≥10% down | Both ≥5% up | Banks ≥3% 5-day drop | Tech ≥3% 5-day drop | Median runway |\n|---|---:|---|---:|---:|---:|---:|---:|---:|")
L.append(summ(d4[pd.to_datetime(d4["signal"]) < "2006-06-22"], "1985 → mid-2006"))
L.append(summ(d4[pd.to_datetime(d4["signal"]) >= "2006-06-22"], "mid-2006 → 2026-08"))
L.append(summ(d4, "All"))
idx4 = list(X4.index); pos4 = {d: i for i, d in enumerate(idx4)}
s4 = [pos4[pd.Timestamp(s)] for s in e4["signal"]]
jd4, i = [], 20
while i < len(idx4) - 40:
    bd = LB4.iloc[i + 1:i + 41] / LB4.iloc[i] - 1; td = LT4.iloc[i + 1:i + 41] / LT4.iloc[i] - 1
    if (bd <= -.10).any() and (td <= -.10).any():
        jd4.append(i); i += 60
    else:
        i += 1
hit4 = sum(any(i - 60 <= s <= i for s in s4) for i in jd4)
cov4 = np.zeros(len(idx4), bool)
for s in s4:
    cov4[s:min(s + 61, len(idx4))] = True
corr_at = [C4.iloc[i] for i in jd4]
L.append(f"\nPrecursor test on this pair: **{hit4} of {len(jd4)} joint declines** (from {idx4[jd4[0]].date()}) had a see-saw signal in the prior 60 sessions; base rate {cov4[20:].mean()*100:.0f}%. "
         f"Median 20d corr at the start of a joint decline: {np.median(corr_at):+.2f}.")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L[L.index('\n## Step 4 — robustness: FF_EW_Banks vs ^NDX from 1985 (the only stand-in that reaches 1985–1993)\n'):]))
