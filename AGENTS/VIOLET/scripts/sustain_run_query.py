#!/usr/bin/env python3
"""Max consecutive-close runs above the +50% line for early40 DIET episodes.

CHG-RED-033 derivation (2026-06-10 evening): for each DIET episode that printed
>=+40% by td-12 (lowest-base anchor, per the 2026-06-10 path-conditioned cut),
compute the max run of consecutive daily closes ABOVE the episode's +50% line
(1.5 x lowest-base fire-day close) inside the fwd-60td window from the
lowest-base fire day. Purpose: derive the sustain count n for the VIX 23
close-and-hold invalidation register, and test whether run-length discriminates
destination-right retests from destination-wrong re-arms.

Methodology matches research/2026-06-10_diet_path_conditioned_cut.md:
closes only, gap<=21td clustering, lowest-base (max-over-fire-days-consistent)
anchor. Reconciliation key: Orch pre-computed table 2026-06-10 evening.

Window/calendar conventions, stated inline (KB-VIO-084/085 rule): all counts
in TRADING days on the yfinance ^VIX calendar; fwd window = lowest-base fire
day (td0) + 60 td inclusive -> 61 closes; early window = td0..td12 (13
closes); runs counted on consecutive CLOSES strictly above the line.
"""
import sys
from pathlib import Path

import pandas as pd

WB = Path(__file__).resolve().parent.parent / "workbook"
EARLY40_TD = 12
EARLY40_PCT = 40.0
FWD_TD = 60


def cluster(dates, gap_td, td_index):
    """Group fire dates into episodes: gap <= gap_td trading days."""
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
    # DIET-class rows ONLY: the canonical 25-episode set clusters each tier
    # separately (diet_coiled_spring.py line ~212), and class=DIET already
    # excludes STRICT days. Including STRICT rows shifts the 2024-12 anchor
    # to 12/3 (13.30) and admits the all-STRICT 2015-10 cluster — both
    # off-canonical (reconciliation vs Orch answer key, 2026-06-10 evening).
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
        closes = vix.loc[ep]
        base_day = closes.idxmin()
        base = float(closes.min())
        line = 1.5 * base
        i0 = td.get_loc(base_day)
        win = vix.iloc[i0: i0 + FWD_TD + 1]
        early = win.iloc[: EARLY40_TD + 1]
        early_peak_pct = (early.max() / base - 1) * 100
        if early_peak_pct < EARLY40_PCT:
            continue
        # max consecutive closes strictly above the +50% line, full window
        run = best = 0
        for c in win:
            run = run + 1 if c > line else 0
            best = max(best, run)
        end_pct = (win.iloc[-1] / base - 1) * 100
        peak_pct = (win.max() / base - 1) * 100
        rows.append({
            "episode": f"{ep[0]:%Y-%m}", "base_day": f"{base_day:%Y-%m-%d}",
            "base": round(base, 2), "line_+50%": round(line, 2),
            "early_peak%": round(early_peak_pct, 1),
            "max_run>line": best, "peak%": round(peak_pct, 1),
            "end%": round(end_pct, 1),
        })

    out = pd.DataFrame(rows)
    print(out.to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
