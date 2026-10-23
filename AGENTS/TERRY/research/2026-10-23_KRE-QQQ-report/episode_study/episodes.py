"""How do KRE/QQQ negative-correlation episodes end? Mechanical episode rule, no hand-picked windows.

Rule: corr20 = rolling 20-session correlation of daily returns (KRE, QQQ). SIGNAL = first close with
corr20 <= the 10/22 reading (-0.2357, displayed -0.24); RE-ARMS only after corr20 closes back above 0.
Sensitivity: the same counts at thresholds -0.15 / -0.20 / -0.30 are printed at the foot.
Divergence direction = sign of the KRE/QQQ ratio change over the 20 sessions up to the signal.
Outcomes are measured from the SIGNAL close (what is knowable on that day), at +5/+10/+20/+40 sessions.
Classification at +20 sessions (ratio signed in the divergence direction):
  CONTINUED  ratio moved >= +3% further in the divergence direction
  SNAP-BACK  ratio moved >= 3% back against it
  FLAT       otherwise
Joint fall within 40 sessions = BOTH KRE and QQQ closed >= 5% below the signal close at some point.
Joint rally within 40 sessions = BOTH closed >= 5% above it at some point.
Data: hist.csv (yfinance auto-adjusted closes), through 2026-10-22 (10/23 bar intraday, dropped).
Run: .venv/bin/python -I episodes.py   -> RESULTS.md, episodes.csv
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "hist.csv"), index_col=0, parse_dates=True)
df = df[df.index <= "2026-10-22"].dropna(subset=["KRE", "QQQ"])
df["TNX"] = df["^TNX"].ffill(); df["VIX"] = df["^VIX"].ffill()
r = df[["KRE", "QQQ"]].pct_change()
df["corr20"] = r["KRE"].rolling(20).corr(r["QQQ"])
df["ratio"] = df["KRE"] / df["QQQ"]
N_BARS = len(df); START = df.index[0].date(); END = df.index[-1].date()

TH_NOW = float(df["corr20"].iloc[-1]); REARM, H = 0.0, [5, 10, 20, 40]
idx = list(df.index)

def signals(th):
    out, armed = [], True
    for i in range(len(idx)):
        c = df["corr20"].iloc[i]
        if pd.isna(c):
            continue
        if armed and c <= th + 1e-12:
            out.append(i); armed = False
        elif not armed and c > REARM:
            armed = True
    return out

sig = signals(TH_NOW)

rows = []
for i in sig:
    d = idx[i]; row = {"signal": d.date()}
    k0, q0, x0 = df["KRE"].iloc[i], df["QQQ"].iloc[i], df["ratio"].iloc[i]
    pre = df["ratio"].iloc[i] / df["ratio"].iloc[i - 20] - 1
    dirn = 1 if pre > 0 else -1
    row.update(corr=df["corr20"].iloc[i], dir="KRE over QQQ" if dirn > 0 else "QQQ over KRE",
               ratio_prior20=pre, tnx_chg20=df["TNX"].iloc[i] - df["TNX"].iloc[i - 20], vix=df["VIX"].iloc[i])
    for h in H:
        j = i + h
        if j < len(idx):
            row[f"KRE+{h}"] = df["KRE"].iloc[j] / k0 - 1
            row[f"QQQ+{h}"] = df["QQQ"].iloc[j] / q0 - 1
            row[f"ratio_dir+{h}"] = dirn * (df["ratio"].iloc[j] / x0 - 1)
            row[f"corr+{h}"] = df["corr20"].iloc[j]
        else:
            row[f"KRE+{h}"] = row[f"QQQ+{h}"] = row[f"ratio_dir+{h}"] = row[f"corr+{h}"] = None
    w = df.iloc[i + 1:i + 41]
    complete40 = len(w) == 40
    kd, qd = w["KRE"] / k0 - 1, w["QQQ"] / q0 - 1
    row["joint_fall40"] = bool(((kd <= -.05).any() and (qd <= -.05).any())) if len(w) else None
    row["joint_rally40"] = bool(((kd >= .05).any() and (qd >= .05).any())) if len(w) else None
    both_down = w[(r["KRE"].loc[w.index] <= -.01) & (r["QQQ"].loc[w.index] <= -.01)]
    row["first_joint_1pct_day"] = (idx.index(both_down.index[0]) - i) if len(both_down) else None
    row["worst_KRE40"] = kd.min() if len(w) else None; row["worst_QQQ40"] = qd.min() if len(w) else None
    row["complete40"] = complete40
    rd20 = row["ratio_dir+20"]
    row["class20"] = None if rd20 is None else ("CONTINUED" if rd20 >= .03 else "SNAP-BACK" if rd20 <= -.03 else "FLAT")
    # days until corr20 back above 0
    after = df["corr20"].iloc[i + 1:]
    up = after[after > 0]
    row["sessions_to_corr_above0"] = (idx.index(up.index[0]) - i) if len(up) else None
    rows.append(row)

ep = pd.DataFrame(rows)
ep.to_csv(os.path.join(HERE, "episodes.csv"), index=False)

def p(x, nd=1):
    return "—" if x is None or pd.isna(x) else f"{x*100:+.{nd}f}%"

L = [f"# KRE/QQQ negative-correlation episodes — mechanical study (TERRY, data {START} → {END}, {N_BARS} bars)\n",
     "Rule: signal = first close with 20-session correlation of daily returns ≤ −0.24; re-arms only after it closes back above 0. "
     "Outcomes from the signal close. yfinance auto-adjusted closes. Small sample: every row is one episode.\n"]
cur = ep.iloc[-1]
assert str(cur["signal"]) == "2026-10-22", cur["signal"]
L.append(f"**Episodes found: {len(ep)}** — {len(ep)-1} completed plus the current one (signalled {cur['signal']}, threshold {TH_NOW:.4f}).\n")
L.append("## Every episode\n")
L.append("| Signal | Direction | 10y over prior 20d | VIX | KRE +20 | QQQ +20 | Ratio +20 (divergence dir.) | Class @20 | KRE +40 | QQQ +40 | Both fell ≥5% (40d) | Both rose ≥5% (40d) | First day both ≤−1% | Corr > 0 after |\n"
         "|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---:|---:|")
for _, e in ep.iterrows():
    jf = "—" if e["joint_fall40"] is None else ("YES" if e["joint_fall40"] else "no") + ("" if e["complete40"] else " (partial)")
    jr = "—" if e["joint_rally40"] is None else ("YES" if e["joint_rally40"] else "no") + ("" if e["complete40"] else " (partial)")
    fj = "—" if pd.isna(e["first_joint_1pct_day"]) else f"{int(e['first_joint_1pct_day'])} sessions"
    ca = "—" if pd.isna(e["sessions_to_corr_above0"]) else f"{int(e['sessions_to_corr_above0'])} sessions"
    L.append(f"| {e['signal']} | {e['dir']} | {e['tnx_chg20']:+.2f} pts | {e['vix']:.1f} | {p(e['KRE+20'])} | {p(e['QQQ+20'])} | {p(e['ratio_dir+20'])} | "
             f"{e['class20'] or 'pending'} | {p(e['KRE+40'])} | {p(e['QQQ+40'])} | {jf} | {jr} | {fj} | {ca} |")

hist = ep.iloc[:-1]
done = hist[hist["class20"].notna()]
L.append(f"\n## Summary over the {len(done)} completed episodes (current one excluded)\n")
cnt = done["class20"].value_counts()
L.append("| Outcome at +20 sessions | Count |\n|---|---:|")
for k in ("CONTINUED", "FLAT", "SNAP-BACK"):
    L.append(f"| {k} | {int(cnt.get(k, 0))} of {len(done)} |")
d40 = hist[hist["complete40"]]
L.append(f"\n| Within 40 sessions (n = {len(d40)} complete) | Count |\n|---|---:|")
L.append(f"| Both KRE and QQQ fell ≥5% at some point | {int(d40['joint_fall40'].sum())} |")
L.append(f"| Both rose ≥5% at some point | {int(d40['joint_rally40'].sum())} |")
L.append(f"| A day with both ≤ −1% occurred | {int(d40['first_joint_1pct_day'].notna().sum())} (median {d40['first_joint_1pct_day'].median():.0f} sessions in) |")
L.append(f"| Correlation back above 0 within 20 sessions | {int((done['sessions_to_corr_above0'] <= 20).sum())} of {len(done)} |")
L.append("\n| Median from signal | +5 | +10 | +20 | +40 |\n|---|---:|---:|---:|---:|")
for lab, col in (("KRE", "KRE"), ("QQQ", "QQQ"), ("Ratio, divergence direction", "ratio_dir")):
    L.append(f"| {lab} | " + " | ".join(p(ep[f'{col}+{h}'].iloc[:-1].median()) for h in H) + " |")
L.append("\n## Split by rate direction (10y change over the 20 sessions before the signal)\n")
L.append("| 10y | Episodes | Class @20 (C/F/S) | Both fell ≥5% in 40d | Both rose ≥5% in 40d |\n|---|---:|---|---:|---:|")
for lab, m in (("Falling", done["tnx_chg20"] < 0), ("Rising", done["tnx_chg20"] >= 0)):
    s = done[m]; c = s["class20"].value_counts(); s40 = s[s["complete40"]]
    L.append(f"| {lab} | {len(s)} | {int(c.get('CONTINUED',0))}/{int(c.get('FLAT',0))}/{int(c.get('SNAP-BACK',0))} | "
             f"{int(s40['joint_fall40'].sum())} of {len(s40)} | {int(s40['joint_rally40'].sum())} of {len(s40)} |")
L.append(f"\n**Current episode:** signalled {cur['signal']}, corr {cur['corr']:.2f}, direction {cur['dir']}, 10y {cur['tnx_chg20']:+.2f} pts over the prior 20 sessions, VIX {cur['vix']:.1f}. "
         f"Sessions observed since signal: {len(df) - 1 - sig[-1]}.")
L.append("\n## Sensitivity — same rule at other thresholds (completed episodes only)\n")
L.append("| Threshold | Episodes | Class @20 (C/F/S) | Both fell ≥5% in 40d | Both rose ≥5% in 40d |\n|---:|---:|---|---:|---:|")
for th in (-0.15, -0.20, TH_NOW, -0.30):
    ss = [i for i in signals(th) if i + 40 < len(idx)]
    cl = {"C": 0, "F": 0, "S": 0}; jf = jr = 0
    for i in ss:
        k0, q0, x0 = df["KRE"].iloc[i], df["QQQ"].iloc[i], df["ratio"].iloc[i]
        dirn = 1 if df["ratio"].iloc[i] / df["ratio"].iloc[i - 20] > 1 else -1
        rd = dirn * (df["ratio"].iloc[i + 20] / x0 - 1)
        cl["C" if rd >= .03 else "S" if rd <= -.03 else "F"] += 1
        w = df.iloc[i + 1:i + 41]; kd, qd = w["KRE"] / k0 - 1, w["QQQ"] / q0 - 1
        jf += int((kd <= -.05).any() and (qd <= -.05).any()); jr += int((kd >= .05).any() and (qd >= .05).any())
    L.append(f"| {th:.2f} | {len(ss)} | {cl['C']}/{cl['F']}/{cl['S']} | {jf} | {jr} |")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
