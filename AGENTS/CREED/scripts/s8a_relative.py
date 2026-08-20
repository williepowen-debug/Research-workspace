#!/usr/bin/env python3
"""
S8a — CRE equity tape: VNQ vs SPY trailing relative performance.
Feeds `VX-CREED-7.01`, `CREED-T-08a` (< -10pp, Will-frozen 2026-07-21) and `PRED-CREED-007`.

WHY THIS FILE EXISTS
--------------------
COVERAGE lane 9's refresh trigger says "recompute per session that cites S8a," and
until 2026-08-20 it pointed at a yfinance "recipe in this row's source note" that
DID NOT EXIST. The 2026-08-20 reading (-0.34pp / -0.98pp) named its window and its
bases but not its computation, so it could not be re-derived or checked. Dead
pointer found by PROME in an oversight pass; verified and closed by CREED same day.

`FORGE/tools/market-data/fetch.py` cannot produce this figure (price/fred only, no
history), which is why this lives in CREED and not in FORGE.

WHAT BUILDING IT REVEALED — READ THIS BEFORE QUOTING A LEVEL
------------------------------------------------------------
Reproducing the committed figure surfaced an instrument problem larger than the
dead pointer. **A single trailing-3mo point is not a usable read of this vector.**

1. WINDOW-START SENSITIVITY. Holding the end date fixed at 2026-08-20 and moving
   the start across +/-9 sessions swings the total-return relative from -0.78pp to
   +2.80pp -- a 3.58pp spread that CROSSES ZERO SIX TIMES. The sign of the level is
   an artifact of which session you call "three months ago."

2. THE SERIES IS NOISY. Trailing-63-session relative, computed every session over
   244 sessions (2025-09 -> 2026-08): mean -2.14pp, **stdev 4.73pp**, range -11.84
   to +7.69. A 10-session stdev of ~2.0pp means any two-point delta under ~4pp is
   inside the instrument's own noise.

3. SO TWO-POINT DELTAS ON THIS VECTOR ARE NOT TREND CLAIMS. Both readings on
   record are two-point reads: 7/27 "+2.04pp, 12pp away AND RECEDING" and 8/20
   "-0.34pp, DECAYING, direction reversed." Like-for-like on a 63-session basis the
   move is 7/27 +1.62 -> 8/20 +0.12 = **-1.50pp, inside one 10-session stdev** --
   and it conceals a full round trip (8/10 low of -4.30pp, then eight consecutive
   sessions BACK UP). Endpoint comparison across this series manufactures shapes.
   CREED standing trap #6 generalised: it is not only ratios that hide shape.

4. "COMFORTABLY FAR FROM THE BAND" IS ALSO WRONG. The band was **breached 78 days
   ago** -- 2026-06-01/02/03 at -11.68 / -11.84 / -10.51pp -- seven weeks BEFORE it
   was written, so no fire was missed. But base rates on this series are: below
   -5pp 35.2% of sessions, below -8pp 5.7%, below -10pp 1.2%. At stdev 4.73pp, a
   ~0pp reading is ~2.1 sigma from the band, not a safe distance.

Hence this script reports a SERIES, a NOISE BAND and a BASE RATE alongside the
point, and prints the point last. Quote the distribution, not the dot.

THE TWO BASES
-------------
VNQ yields materially more than SPY, so the bases differ by roughly the yield gap
(~0.65pp over 3 months). That is large next to the moves being discussed, so an
unlabelled figure is close to unusable.

    total-return : yfinance auto_adjust=True  -> Close  (splits AND dividends)
    price-only   : yfinance auto_adjust=False -> Close  (splits only, raw close)

`VX-CREED-7.01` stores the TOTAL-RETURN figure. The frozen band states no basis;
this script does not resolve that -- it prints both so a grader says which they graded.

USAGE
-----
    .venv/bin/python AGENTS/CREED/scripts/s8a_relative.py
    .venv/bin/python AGENTS/CREED/scripts/s8a_relative.py --end 2026-07-27   # re-derive a past reading
    .venv/bin/python AGENTS/CREED/scripts/s8a_relative.py --lookback 126     # 6mo

Exit 0 always. Measurement tool, not a gate -- adjudication is a CREED act.
"""

import argparse
import statistics as st
import sys
from datetime import date, timedelta

BAND_YELLOW, BAND_ORANGE, BAND_RED = -5.0, -8.0, -10.0   # Will-frozen 2026-07-21 — propose, don't edit
LOOKBACK = 63            # sessions ~ 3 months; the S8a / PRED-CREED-007 spec
BASE_RATE_SESSIONS = 244 # ~14 months of history for the distribution


def _closes(tickers, start, end, adjusted):
    import yfinance as yf
    df = yf.download(tickers, start=start, end=end, auto_adjust=adjusted,
                     progress=False, group_by="column")
    if df is None or df.empty:
        raise SystemExit("FETCH FAILED — empty frame. Do NOT fall back to a stale figure.")
    return df["Close"].dropna()


def _rel_series(c, tgt, base, lb):
    out = []
    for i in range(lb, len(c)):
        t = (float(c[tgt].iloc[i]) / float(c[tgt].iloc[i - lb]) - 1) * 100
        b = (float(c[base].iloc[i]) / float(c[base].iloc[i - lb]) - 1) * 100
        out.append((c.index[i].date(), t - b))
    return out


def _state(r):
    return ("RED/FIRED" if r < BAND_RED else "ORANGE" if r < BAND_ORANGE
            else "YELLOW" if r < BAND_YELLOW else "GREEN")


def main():
    ap = argparse.ArgumentParser(description="S8a: VNQ vs SPY trailing relative — series, noise, base rate, point.")
    ap.add_argument("--end", help="as-of date YYYY-MM-DD (default: latest close). Use to re-derive a past reading.")
    ap.add_argument("--lookback", type=int, default=LOOKBACK, help=f"sessions in the window (default {LOOKBACK} ~ 3mo)")
    ap.add_argument("--target", default="VNQ")
    ap.add_argument("--base", default="SPY")
    args = ap.parse_args()

    end = date.fromisoformat(args.end) if args.end else date.today()
    hist_start = end - timedelta(days=int((args.lookback + BASE_RATE_SESSIONS) * 1.5))
    fetch_end = end + timedelta(days=1)          # yfinance end is EXCLUSIVE
    tk = [args.target, args.base]

    ser, pt = {}, {}
    for label, adj in (("total-return", True), ("price-only", False)):
        c = _closes(tk, hist_start.isoformat(), fetch_end.isoformat(), adj)
        s = _rel_series(c, args.target, args.base, args.lookback)
        if not s:
            raise SystemExit("Not enough history for the requested lookback.")
        ser[label] = s
        pt[label] = s[-1]

    tr = ser["total-return"]
    vals = [r for _, r in tr]
    recent = [r for _, r in tr[-10:]]
    asof, cur = tr[-1]

    print(f"S8a — {args.target} vs {args.base}, trailing {args.lookback}-session relative")
    print(f"  as of {asof}   (band CREED-T-08a < {BAND_RED:.0f}pp, Will-frozen 2026-07-21)")
    print()

    print("  ── THE SERIES (total-return, last 15 sessions) ──")
    for d, r in tr[-15:]:
        print(f"    {d}  {r:+6.2f}pp  {_state(r):<9} {'#' * int(abs(r) * 3)}")
    print()

    print("  ── NOISE (this is why a single point is not a read) ──")
    print(f"    last 10 sessions : mean {st.mean(recent):+.2f}pp   stdev {st.stdev(recent):.2f}pp")
    print(f"    full sample n={len(vals)} : mean {st.mean(vals):+.2f}pp   stdev {st.stdev(vals):.2f}pp"
          f"   range {min(vals):+.2f} to {max(vals):+.2f}")
    print(f"    ⚠ any two-point delta smaller than ~{2*st.stdev(recent):.1f}pp is inside this instrument's noise.")
    print()

    print("  ── BASE RATE (how far is 'far'?) ──")
    for band in (BAND_YELLOW, BAND_ORANGE, BAND_RED):
        hit = [d for d, r in tr if r < band]
        line = f"    below {band:>5.0f}pp : {len(hit):>3}/{len(vals)} sessions ({100*len(hit)/len(vals):>4.1f}%)"
        if hit:
            line += f"   most recent {hit[-1]} ({(asof-hit[-1]).days}d ago)"
        print(line)
    sd = st.stdev(vals)
    print(f"    current reading is {abs(cur - BAND_RED)/sd:.1f} sigma from the band (sigma = {sd:.2f}pp).")
    print()

    print("  ── THE POINT (quote this LAST, and never alone) ──")
    for label in ("total-return", "price-only"):
        d, r = pt[label]
        print(f"    {label:<13} {r:+.2f}pp   {_state(r)}   ({abs(r - BAND_RED):.2f}pp from the band)")
    agree = (pt["total-return"][1] < 0) == (pt["price-only"][1] < 0)
    print(f"    basis spread {abs(pt['total-return'][1]-pt['price-only'][1]):.2f}pp"
          f"   |   sign robust to basis: {'YES' if agree else '*** NO — report no unqualified sign ***'}")
    print()
    print("  VX-CREED-7.01 stores the TOTAL-RETURN figure. Report the level WITH the")
    print("  10-session stdev; do not characterise a move under ~2 sigma as a trend.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
