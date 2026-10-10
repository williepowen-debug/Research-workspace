#!/usr/bin/env python3
"""Frozen-baseline price-ladder detector for REGINALD VX rows.

Exists because VX-REG-6.03 (FLG vs FROZEN $14.24) broke band 1 on 2026-09-16
and nobody saw it for 8 days: no script implemented the ladder (PROME census
2026-09-23, FLG packet 2026-09-24). A ladder that lives only in a TSV cell is
a manual check with no owner.

Grades SETTLED daily closes only (yfinance history, auto_adjust=False) against
ABSOLUTE band levels derived from a FROZEN baseline -- never a rolling window.
Settled = settled_bars.settled_closes(): today's (ET) bar and any NaN bar are excluded and
printed as NOT GRADED (fixed 2026-10-09: an intraday run counted FLG's in-progress $11.25
as a third close below RED; an evening run printed 'last close $nan').

Usage (from repo root):
  .venv/bin/python3 AGENTS/REGINALD/scripts/vx_ladder_check.py
Exit: 0 = no band broken · 1 = at least one band broken (read the output) · 2 = data error.
"""
import sys

try:
    import yfinance as yf
except ImportError:  # wrong interpreter must not read as a breach (rc 1)
    print("DATA ERROR: yfinance not importable — run with the repo .venv/bin/python3")
    sys.exit(2)

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from settled_bars import settled_closes  # noqa: E402

# id, ticker, frozen baseline, baseline date, band fractions (Yellow/Orange/Red)
LADDERS = [
    ("VX-REG-6.03", "FLG", 14.24, "2026-08-12", (-0.10, -0.15, -0.20)),
]
NAMES = ("YELLOW", "ORANGE", "RED")


def main():
    worst = 0
    for vid, tkr, base, bdate, fracs in LADDERS:
        levels = [round(base * (1 + f), 2) for f in fracs]
        try:
            raw = yf.Ticker(tkr).history(start=bdate, auto_adjust=False)["Close"]
        except Exception as e:  # noqa: BLE001
            print(f"{vid} {tkr}: DATA ERROR {e}")
            return 2
        closes, excluded = settled_closes(raw)
        if closes.empty:
            print(f"{vid} {tkr}: DATA ERROR no closes since {bdate}")
            return 2
        last_d, last_c = closes.index[-1], float(closes.iloc[-1])
        print(f"{vid} {tkr} frozen ${base} [{bdate}] bands "
              + " / ".join(f"{n} ${lv}" for n, lv in zip(NAMES, levels)))
        print(f"  last SETTLED close ${last_c:.2f} [{last_d:%Y-%m-%d}] = {last_c / base - 1:+.1%} vs baseline")
        for d, why in excluded:
            print(f"  ⏸  {d} NOT GRADED — {why}")
        state = "GREEN"
        for n, lv in zip(NAMES, levels):
            below = closes[closes < lv]
            if below.empty:
                continue
            first = below.index[0]
            state = n
            worst = 1
            print(f"  🔴 {n} ${lv} BROKEN — first close below: {first:%Y-%m-%d} "
                  f"${float(below.iloc[0]):.2f}; closes below since: {len(below)}")
        nxt = [(n, lv) for n, lv in zip(NAMES, levels) if last_c >= lv]
        if nxt:
            n, lv = nxt[0]
            print(f"  next band {n} ${lv} is {lv / last_c - 1:+.1%} from last close")
        print(f"  STATE (worst band ever breached, state machine): {state}")
        print("  ⚠️ yfinance daily bars can be MISSING for single names (FLG + WAL 9/22/2026) — a gap is not a close.")
    return worst


if __name__ == "__main__":
    sys.exit(main())
