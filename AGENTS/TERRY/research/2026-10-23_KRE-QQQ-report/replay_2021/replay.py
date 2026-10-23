"""Replay the divergence-map watch as it would have read each day around the Nov 23, 2021 counterexample,
using only data up to that day. Pairs: KRE/QQQ (the map's own) and ^BKX/^NDX (where the -0.25 signal occurred).
Signals as on the map, generalised for a tech-led episode where noted:
  corr_on   20-session corr > 0
  ratio_on  bank/tech ratio >= 3% off its extreme over the prior 20 sessions, AGAINST the leader
            (bank-led: below its 20-session high; tech-led: above its 20-session low) [map: peak since Oct 6]
  joint_on  any session since the signal with both <= -1% (cumulative from signal day)
  ten_on    10y up >= 15 bp over 5 sessions
  alarm_on  last session with 10y <= -5 bp had the bank leg DOWN
Joint decline = both legs >= 5% (and >= 10%) below the Nov 23, 2021 close.
Run: .venv/bin/python -I replay.py -> RESULTS.md
"""
import os
import pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.dirname(HERE)
a = pd.read_csv(os.path.join(UP, "episode_study", "hist.csv"), index_col=0, parse_dates=True)
b = pd.read_csv(os.path.join(UP, "deep_1985", "hist_idx.csv"), index_col=0, parse_dates=True)
SIG = pd.Timestamp("2021-11-23")
L = ["# Watch replay around the Nov 23, 2021 counterexample (TERRY, 2026-10-23)\n",
     "Each row = what the map's five signs would have shown at that close, from data up to that day only. 10-year = ^TNX (Cboe, via Yahoo). yfinance closes.\n"]
for lab, bank, tech, px in (("^BKX vs ^NDX (large banks; the pair that signalled -0.25)", "^BKX", "^NDX", b),
                            ("KRE vs QQQ (the map's own pair)", "KRE", "QQQ", a)):
    x = px[[bank, tech]].dropna().copy()
    x["ten"] = px["^TNX"].reindex(x.index).ffill()
    x = x[(x.index >= "2021-06-01") & (x.index <= "2022-03-31")]
    br, tr = x[bank].pct_change() * 100, x[tech].pct_change() * 100
    x["corr"] = br.rolling(20).corr(tr); x["ratio"] = x[bank] / x[tech]; x["tb"] = x["ten"].diff() * 100
    i0 = x.index.get_loc(SIG)
    lead_bank = x["ratio"].iloc[i0] > x["ratio"].iloc[i0 - 20]
    b0, t0 = x[bank].iloc[i0], x[tech].iloc[i0]
    rows, first = [], {}
    for i in range(i0 - 5, i0 + 41):
        d = x.index[i]; w = x["ratio"].iloc[max(0, i - 20):i + 1]
        off = (x["ratio"].iloc[i] / w.max() - 1) * 100 if lead_bank else (x["ratio"].iloc[i] / w.min() - 1) * 100
        ratio_on = off <= -3 if lead_bank else off >= 3
        js = ((br.iloc[i0:i + 1] <= -1) & (tr.iloc[i0:i + 1] <= -1)) if i >= i0 else pd.Series(dtype=bool)
        joint_on = bool(js.any()) if i >= i0 else False
        ten5 = (x["ten"].iloc[i] - x["ten"].iloc[i - 5]) * 100
        dn = x["tb"].iloc[:i + 1]; dn = dn[dn <= -5]
        alarm_on = bool(br.loc[dn.index[-1]] < 0) if len(dn) else False
        on = {"corr": x["corr"].iloc[i] > 0, "ratio": ratio_on, "joint": joint_on, "ten": ten5 >= 15, "alarm": alarm_on}
        for k, v in on.items():
            if v and k not in first and i >= i0: first[k] = d.date()
        bd, td = x[bank].iloc[i] / b0 - 1, x[tech].iloc[i] / t0 - 1
        rows.append((d.date(), x["corr"].iloc[i], off, ten5, on, bd, td))
    after = x.iloc[i0 + 1:i0 + 41]
    bdd, tdd = after[bank] / b0 - 1, after[tech] / t0 - 1
    def first_joint(th):
        m = (bdd.cummin() <= -th) & (tdd.cummin() <= -th)
        return m[m].index[0].date() if m.any() else None
    j5, j10 = first_joint(.05), first_joint(.10)
    L.append(f"\n## {lab}\n")
    L.append(f"Leader into Nov 23, 2021: {'banks' if lead_bank else 'tech'}. Joint decline from the Nov 23 close: both ≥5% below first on **{j5}**; both ≥10% below first on **{j10}**.\n")
    L.append("| Close | 20d corr | Ratio off extreme | 10y 5-session | Signs on | Which | Banks vs Nov 23 | Tech vs Nov 23 |\n|---|---:|---:|---:|---:|---|---:|---:|")
    for d, c, off, t5, on, bd, td in rows:
        names = ", ".join(k for k, v in on.items() if v) or "—"
        mark = " **← signal**" if pd.Timestamp(d) == SIG else (" **← both ≥5% down**" if d == j5 else (" **← both ≥10% down**" if d == j10 else ""))
        L.append(f"| {d}{mark} | {c:+.2f} | {off:+.1f}% | {t5:+.0f} bp | {sum(on.values())} | {names} | {bd*100:+.1f}% | {td*100:+.1f}% |")
    L.append("\nFirst date each sign turned on, from the signal day: " + (", ".join(f"{k} {v}" for k, v in first.items()) or "none") +
             f". Joint ≥5% decline: {j5}.")
open(os.path.join(HERE, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
