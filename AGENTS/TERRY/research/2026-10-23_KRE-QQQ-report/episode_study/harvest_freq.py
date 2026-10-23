"""Step (b): during past KRE/QQQ negative-correlation episodes, how often did each side give a
sellable drop? Drop = close-to-close decline of >= X% over 5 sessions (any start day inside the window).
Window = the 20 sessions after each signal (episodes.csv rule). Baseline = every 20-session window
since 2006 (non-overlapping, stepped by 20). Also: episode runway (sessions until corr20 back above 0).
yfinance auto-adjusted closes, hist.csv, through 2026-10-22. Run: .venv/bin/python -I harvest_freq.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "hist.csv"), index_col=0, parse_dates=True)
df = df[df.index <= "2026-10-22"].dropna(subset=["KRE", "QQQ"])
ep = pd.read_csv(os.path.join(HERE, "episodes.csv"), parse_dates=["signal"])
ep = ep[ep["signal"] < "2026-10-22"]  # completed only
idx = list(df.index)
fwd5 = {t: df[t].shift(-5) / df[t] - 1 for t in ("KRE", "QQQ")}
TH = [0.02, 0.025, 0.03, 0.05]

def window_stats(i0):
    """drops inside sessions i0+1 .. i0+20 (5-session moves must also END inside the window)"""
    out = {}
    for t in ("KRE", "QQQ"):
        s = fwd5[t].iloc[i0 + 1:i0 + 16]  # start days whose 5-session move ends by i0+20
        for th in TH:
            out[(t, th)] = bool((s <= -th).any())
            out[(t, th, "up")] = bool((s >= th).any())
    return out

ev = [window_stats(idx.index(d)) for d in ep["signal"]]
base_starts = list(range(20, len(idx) - 21, 20))
bs = [window_stats(i) for i in base_starts]

def share(rows, key):
    return sum(r[key] for r in rows) / len(rows)

L = [f"# Step (b) — sellable drops during past episodes (TERRY; {len(ev)} completed episodes; baseline {len(bs)} non-overlapping 20-session windows since 2006)\n",
     "A 'drop' = a 5-session close-to-close fall of at least the threshold, starting and ending inside the 20 sessions after the signal. yfinance auto-adjusted closes. MODEL-free (prices only).\n",
     "| Threshold (5-session move) | KRE drop: episodes | baseline | QQQ drop: episodes | baseline | BOTH sides dropped at some point: episodes | baseline |",
     "|---:|---:|---:|---:|---:|---:|---:|"]
for th in TH:
    both_e = sum(r[("KRE", th)] and r[("QQQ", th)] for r in ev) / len(ev)
    both_b = sum(r[("KRE", th)] and r[("QQQ", th)] for r in bs) / len(bs)
    L.append(f"| ≥{th*100:.1f}% | {share(ev,('KRE',th))*100:.0f}% ({sum(r[('KRE',th)] for r in ev)}/{len(ev)}) | {share(bs,('KRE',th))*100:.0f}% | "
             f"{share(ev,('QQQ',th))*100:.0f}% ({sum(r[('QQQ',th)] for r in ev)}/{len(ev)}) | {share(bs,('QQQ',th))*100:.0f}% | "
             f"{both_e*100:.0f}% | {both_b*100:.0f}% |")
L.append("\n## Per episode (≥3% drops over 5 sessions, within 20 sessions of the signal)\n")
L.append("| Signal | Direction | KRE ≥3% drop | QQQ ≥3% drop | Sessions until corr > 0 |\n|---|---|---|---|---:|")
for (_, e), r in zip(ep.iterrows(), ev):
    L.append(f"| {e['signal'].date()} | {e['dir']} | {'yes' if r[('KRE',0.03)] else 'no'} | {'yes' if r[('QQQ',0.03)] else 'no'} | {int(e['sessions_to_corr_above0'])} |")
run = ep["sessions_to_corr_above0"]
L.append(f"\n**Runway:** sessions from signal until the 20-day correlation closed back above 0 — median {run.median():.0f}, range {run.min():.0f}–{run.max():.0f}; within 20 sessions in {(run <= 20).sum()} of {len(run)}.")
open(os.path.join(HERE, "HARVEST_FREQ.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
