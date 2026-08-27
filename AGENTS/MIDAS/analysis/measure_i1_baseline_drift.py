#!/usr/bin/env python3
"""measure_i1_baseline_drift.py — quantify the I1 TRACKED-baseline defect.

Recomputes the I1 band's own denominator (trailing-2yr rolling median of daily
LME copper stock) AS OF a set of past dates, then shows how much a FIXED tonnage's
grade moves purely because the denominator moved. Companion to
analysis/2026-08-23_i1-tracked-baseline-measured-effect.md.

Reuses metals_watch.py's scraper by import — does NOT fork it (the band and this
measurement must share one data path, or the measurement proves nothing about the
band). Run from anywhere; needs the repo .venv for metals_watch's deps.

  .venv/bin/python AGENTS/MIDAS/analysis/measure_i1_baseline_drift.py
"""
import datetime as dt
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import metals_watch as mw  # noqa: E402

WINDOW_DAYS = 730          # the band's own 2yr window
OFFSETS = (0, 2, 7, 14, 30, 60, 90, 180)
# Historical anchors carry the DATE their tonnage is from, never a relative word
# ("latest" frozen to a value goes stale silently the next business day -- L-29).
# The current mark is DERIVED from the series at run time, so it cannot lie.
FIXED_HIST = [("2026-08-14 trough", 204_975), ("2026-08-20 mark", 239_925)]


def series():
    # Year pages are chosen by the CLOCK while every other leg is data-anchored.
    # Harmless today (the scrape self-reports its own span, printed above), but it
    # is the one clock-dependent leg in the file -- do not add more.
    out, yr = [], dt.date.today().year
    for url in [mw.WESTMETALL_CU_URL] + [f"{mw.WESTMETALL_CU_URL}&year={y}" for y in (yr - 1, yr - 2)]:
        try:
            out += mw._parse_westmetall_table(mw._fetch_westmetall(url))
        except Exception as e:  # noqa: BLE001
            print(f"  fetch note: {e}", file=sys.stderr)
    return sorted({(d.date(), t) for d, _label, t in out})


def median_asof(rows, asof):
    lo = asof - dt.timedelta(days=WINDOW_DAYS)
    w = [t for d, t in rows if lo <= d <= asof]
    return (statistics.median(w), len(w)) if w else (None, 0)


def main():
    rows = series()
    if len(rows) < 100:
        print("  INSUFFICIENT SERIES — refusing to report (fail loud, never a partial verdict)", file=sys.stderr)
        return 2
    latest, latest_t = rows[-1]
    print(f"series n={len(rows)}  {rows[0][0]} -> {latest}")
    print(f"\n  \u26a0\ufe0f  AS-OF DEPENDENT BY CONSTRUCTION -- quote every figure below with"
          f"\n      'as-of {latest}'. This script measures the drift of a TRACKED denominator,"
          f"\n      so its OWN headline numbers move between runs. A re-run that disagrees with"
          f"\n      a dated write-up is the defect reproducing, NOT a contradiction of it."
          f"\n      Compare VERDICTS across vintages; never compare bare magnitudes.")

    marks = []
    print("\n-- denominator by as-of date (trailing-2yr rolling median) --")
    for off in OFFSETS:
        med, n = median_asof(rows, latest - dt.timedelta(days=off))
        if med:
            marks.append(med)
            print(f"  as-of {latest - dt.timedelta(days=off)}  median {med:>10,.0f} t  (n={n})")
    drift = 100 * (max(marks) - min(marks)) / min(marks)
    print(f"\n  DENOMINATOR DRIFT [as-of {latest}]: {min(marks):,.0f} -> {max(marks):,.0f} t = {drift:.2f}%")

    print("\n-- same tonnage, grade varies by grading date alone --")
    worst = 0.0
    for label, t in FIXED_HIST + [(f"{latest} current", latest_t)]:
        g = [100 * (t - m) / m for m in marks]
        worst = max(worst, max(g) - min(g))
        print(f"  {label:12s} {t:>8,} t -> {min(g):+.2f}% .. {max(g):+.2f}%   SPREAD {max(g) - min(g):.2f}pp")

    print(f"\n-- vs registered bands: Y+{mw.LME_YELLOW} / O+{mw.LME_ORANGE} / R+{mw.LME_RED} pp --")
    print(f"  worst baseline-only swing [as-of {latest}]: {worst:.2f}pp = {100 * worst / mw.LME_YELLOW:.0f}% of the smallest band")
    crosses = worst >= mw.LME_YELLOW
    print(f"  baseline drift alone {'CAN' if crosses else 'CANNOT'} cross the nearest band unaided.")
    return 1 if crosses else 0


if __name__ == "__main__":
    sys.exit(main())
