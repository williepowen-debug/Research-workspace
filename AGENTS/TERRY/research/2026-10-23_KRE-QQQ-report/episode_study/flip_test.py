"""When a see-saw episode ends (20d corr closes back above 0), does the direction at the flip
(both legs down vs up over the 5 sessions into it) tell a joint fall from a benign end?
Pairs: KRE/QQQ (2006+, episode_study/hist.csv) and ^BKX/^NDX (1993+, deep_1985/hist_idx.csv).
Outcome: both legs >= 5% below the FLIP close within the next 40 sessions (joint fall) / >= 5% above (joint rally).
Run: .venv/bin/python -I episode_study/flip_test.py
"""
import os
import pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.dirname(HERE)
TH = -0.2357
def run(b, t, path, start):
    px = pd.read_csv(path, index_col=0, parse_dates=True)[[b, t]].dropna()
    px = px[(px.index >= start) & (px.index <= "2026-10-22")]
    r = px.pct_change(); c = r[b].rolling(20).corr(r[t]); idx = list(px.index)
    out, armed, i = [], True, 0
    while i < len(idx):
        v = c.iloc[i]
        if pd.notna(v) and armed and v <= TH:
            armed = False; s = i
            j = next((k for k in range(i + 1, len(idx)) if c.iloc[k] > 0), None)
            if j is None or j + 40 >= len(idx) or j < 5:
                break
            b5 = px[b].iloc[j] / px[b].iloc[j - 5] - 1; t5 = px[t].iloc[j] / px[t].iloc[j - 5] - 1
            w = px.iloc[j + 1:j + 41]; bd = w[b] / px[b].iloc[j] - 1; td = w[t] / px[t].iloc[j] - 1
            out.append({"signal": idx[s].date(), "flip": idx[j].date(), "banks5": b5, "tech5": t5,
                        "into_flip": "both down" if b5 < 0 and t5 < 0 else "both up" if b5 > 0 and t5 > 0 else "mixed",
                        "joint_fall40": bool((bd <= -.05).any() and (td <= -.05).any()),
                        "joint_rally40": bool((bd >= .05).any() and (td >= .05).any())})
            armed = True; i = j
        i += 1
    return pd.DataFrame(out)
for lab, b, t, path, st in (("KRE/QQQ", "KRE", "QQQ", os.path.join(HERE, "hist.csv"), "2006-06-01"),
                            ("BKX/NDX", "^BKX", "^NDX", os.path.join(UP, "deep_1985", "hist_idx.csv"), "1993-01-01")):
    d = run(b, t, path, st)
    print(f"\n## {lab}: {len(d)} completed flips")
    print("| Signal | Flip back above 0 | Banks 5d into flip | Tech 5d into flip | Into flip | Both fell >=5% next 40d | Both rose >=5% next 40d |\n|---|---|---:|---:|---|---|---|")
    for _, x in d.iterrows():
        print(f"| {x['signal']} | {x['flip']} | {x['banks5']*100:+.1f}% | {x['tech5']*100:+.1f}% | {x['into_flip']} | {'YES' if x['joint_fall40'] else 'no'} | {'YES' if x['joint_rally40'] else 'no'} |")
    print("\n| Into the flip | n | Both fell >=5% after | Both rose >=5% after |\n|---|---:|---:|---:|")
    for k in ("both down", "mixed", "both up"):
        s = d[d["into_flip"] == k]
        print(f"| {k} | {len(s)} | {int(s['joint_fall40'].sum())} | {int(s['joint_rally40'].sum())} |")
