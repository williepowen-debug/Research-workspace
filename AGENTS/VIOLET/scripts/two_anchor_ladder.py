#!/usr/bin/env python3
"""Two-anchor level ladder for the live (May 2026) DIET episode.

CHG-RED-034 derivation (2026-06-10 evening): the KB-VIO-087 ladder quotes
P(touch 23/24/25/26) from the lowest-base anchor (5/29 @ 15.32) using the 6
early40 episodes. This script produces the FIRST-FIRE-anchor column (5/20 @
first-fire close): under that accounting the live episode has NOT printed an
early >=+40%, so the applicable population is the no-early-print episodes
(expected 19 of 25; reconciliation anchor: P(>=+50% | no early) = 42% = 8/19
per research/2026-06-10_diet_path_conditioned_cut.md).

For each ladder level X, required move = X / first_fire_base - 1; the column
reports the fraction of the no-early population whose fwd-60td peak (from
first-fire day) met it. A small-n path-conditioned subset (early peak in
[+20%, +40%) by td-12 — episodes that looked like ours) is reported honestly
as shape-precedent, not statistics.

Methodology: closes only, DIET-class-only clustering (canonical, KB-VIO-088
reconciliation), gap<=21td.

Window/calendar conventions, stated inline (KB-VIO-084/085 construction-note
rule, applied prospectively):
  - ALL counts are TRADING days on the yfinance ^VIX calendar, never calendar
    days.
  - fwd window = first-fire day (td0) + 60 td INCLUSIVE -> 61 closes
    (iloc[i0 : i0+61]).
  - early window = td0..td12 inclusive -> 13 closes (the cut's "by td-12").
  - episode = consecutive DIET-class fire days with gap <= 21 td.
  - peaks measured on CLOSES only; intraday touches are understated by
    construction.
"""
import sys
from pathlib import Path

import pandas as pd

WB = Path(__file__).resolve().parent.parent / "workbook"
EARLY40_TD = 12
FWD_TD = 60
LEVELS = [23.0, 24.0, 25.0, 26.0]
LIVE_FIRST_FIRE = pd.Timestamp("2026-05-20")


def cluster(dates, gap_td, td_index):
    pos = {d: i for i, d in enumerate(td_index)}
    eps, cur = [], [dates[0]]
    for d in dates[1:]:
        if pos[d] - pos[cur[-1]] <= gap_td:
            cur.append(d)
        else:
            eps.append(cur)
            cur = [d]
    eps.append(cur)
    return eps


def main():
    fires = pd.read_csv(WB / "DIET_COILED_SPRING.csv", parse_dates=["date"])
    fires = fires[fires["class"] == "DIET"].sort_values("date")

    import yfinance as yf
    vix = yf.download("^VIX", start="2012-01-01", auto_adjust=False,
                      progress=False)["Close"]
    if isinstance(vix, pd.DataFrame):
        vix = vix.iloc[:, 0]
    vix = vix.dropna()
    td = vix.index

    eps = cluster(list(fires["date"]), 21, td)
    rows = []
    for ep in eps:
        ff_day = ep[0]
        base = float(vix.loc[ff_day])
        i0 = td.get_loc(ff_day)
        win = vix.iloc[i0: i0 + FWD_TD + 1]
        early_pct = (win.iloc[: EARLY40_TD + 1].max() / base - 1) * 100
        peak_pct = (win.max() / base - 1) * 100
        rows.append({"episode": f"{ff_day:%Y-%m}", "ff_day": ff_day,
                     "base": base, "early_peak%": early_pct,
                     "fwd60_peak%": peak_pct, "live": ff_day == LIVE_FIRST_FIRE})
    df = pd.DataFrame(rows)
    hist = df[~df["live"]]
    live = df[df["live"]]

    print(f"historical episodes: {len(hist)}  |  live row found: {len(live)}")
    if len(live):
        lb = float(live["base"].iloc[0])
        print(f"live first-fire base: {lb:.2f}  early_peak {float(live['early_peak%'].iloc[0]):.1f}%")
    else:
        lb = 17.44
        print(f"live episode not in CSV window — using cut's base {lb}")

    early = hist[hist["early_peak%"] >= 40.0]
    noearly = hist[hist["early_peak%"] < 40.0]
    n50 = (noearly["fwd60_peak%"] >= 50.0).sum()
    print(f"\nearly40 group (first-fire): {len(early)} -> {sorted(early['episode'])}")
    print(f"no-early population: {len(noearly)};  P(>=+50% | no early) = {n50}/{len(noearly)}"
          f" = {n50/len(noearly)*100:.0f}%   [reconcile vs cut: 8/19 = 42%]")

    print(f"\nFIRST-FIRE LADDER (base {lb:.2f}, population = {len(noearly)} no-early episodes):")
    print(f"{'level':>6} {'req%':>7} {'count':>7} {'raw P':>7}")
    for x in LEVELS:
        req = (x / lb - 1) * 100
        cnt = (noearly["fwd60_peak%"] >= req).sum()
        print(f"{x:>6.1f} {req:>6.1f}% {cnt:>4}/{len(noearly)} {cnt/len(noearly)*100:>6.0f}%")

    sub = noearly[(noearly["early_peak%"] >= 20.0) & (noearly["early_peak%"] < 40.0)]
    print(f"\npath-conditioned subset (early peak in [+20%,+40%) by td-12, like ours): n={len(sub)}")
    print(sorted(sub["episode"]))
    for x in LEVELS:
        req = (x / lb - 1) * 100
        cnt = (sub["fwd60_peak%"] >= req).sum()
        print(f"{x:>6.1f} {req:>6.1f}% {cnt:>4}/{len(sub)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
