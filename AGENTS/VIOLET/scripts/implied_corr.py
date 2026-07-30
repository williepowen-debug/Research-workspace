#!/usr/bin/env python3
"""VIOLET implied-correlation instrument — the quantity KB-VIO-126 registers a test on
and that VIOLET was not measuring.

WHY THIS EXISTS (KB-VIO-156, 2026-07-30). KB-VIO-126 registered a dated falsification
hook: *"if correlations RISE and single-stock vol FALLS through the 7/29-8/1 earnings
cluster, the benign typical-earnings pattern wins and the coiled read loses this leg."*
For a week VIOLET graded that hook by eyeballing single-name moves and keeping an
informal "2-for-2 dispersion" tally — **a paraphrase, not the registered test**, and
it drifted toward the answer VIOLET already liked. When the registered version was
finally measured, **both conditions were met and it graded AGAINST that read.**

A registered test whose quantity nobody measures is unsatisfiable by construction
(thesis v3.8). This closes that: the quantity is pullable, so pull it every boot.

WHAT IT MEASURES
  ^COR1M / ^COR3M / ^COR30D — CBOE implied-correlation indices (SPX vs its largest
  components). Low = dispersed market, which MECHANICALLY depresses index vol even
  when constituents are wild (the KB-VIO-126 mechanism, and a sibling of KB-VIO-108's
  hedge-composition suppression).

⚠️ THE DERIVED CONSTITUENT-VOL COLUMN IS [EST] AND DIRECTION-ONLY.
  From the first-order index-variance identity, for a large, roughly equal-weighted
  index:  sigma_index^2 ~= rho * sigma_avg^2   =>   sigma_avg ~= VIX / sqrt(rho).
  This is NOT a measured constituent-vol series. 3Fourteen's measured series read
  ~50.2 where this proxy reads ~70 for the same week — **the LEVELS DO NOT AGREE.**
  Use it for the SIGN of the change and never quote it as a constituent-vol level.

⚠️ FEED LIMIT, verified 2026-07-30: yfinance carries **no daily history** for these
  tickers (period=1mo returns n=1) — only ~5 days of hourly bars. CBOE's delayed-quote
  API supplies today's print plus `prev_day_close`. So this builds its own history
  going forward; there is no deep backfill available, which is exactly why it must run
  every day rather than be reconstructed on demand.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/implied_corr.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/implied_corr.py --boot   # terse, appends
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

VIOLET_DIR = Path(__file__).resolve().parents[1]
LEDGER = VIOLET_DIR / "workbook" / "IMPLIED_CORR.tsv"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _daily_log import upsert_row, describe  # noqa: E402
ET = ZoneInfo("America/New_York")
COLS = ["date", "cor1m", "cor3m", "cor30d", "vix", "constituent_vol_est",
        "cor1m_prev_close", "basis", "source_ts", "note"]


def cboe_quote(sym: str) -> dict | None:
    url = f"https://cdn.cboe.com/api/global/delayed_quotes/quotes/{sym}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=25)).get("data")
    except Exception:
        return None


def yf_last(ticker: str) -> float | None:
    try:
        import yfinance as yf
        return round(float(yf.Ticker(ticker).fast_info["lastPrice"]), 4)
    except Exception:
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--boot", action="store_true", help="terse output, append a row")
    a = ap.parse_args(argv)

    now = datetime.now(timezone.utc)
    et = now.astimezone(ET)
    basis = "SETTLE" if (et.hour, et.minute) >= (16, 15) else "TICK"

    c1 = cboe_quote("_COR1M") or {}
    c30 = cboe_quote("_COR30D") or {}
    cor1m = c1.get("current_price") or yf_last("^COR1M")
    cor30d = c30.get("current_price") or yf_last("^COR30D")
    cor3m = yf_last("^COR3M")
    prev1m = c1.get("prev_day_close")
    vix = yf_last("^VIX")

    sig = None
    if cor1m and vix and cor1m > 0:
        sig = round(vix / math.sqrt(cor1m / 100.0), 1)

    row = {
        "date": et.strftime("%Y-%m-%d"),
        "cor1m": cor1m if cor1m is not None else "",
        "cor3m": cor3m if cor3m is not None else "",
        "cor30d": cor30d if cor30d is not None else "",
        "vix": vix if vix is not None else "",
        "constituent_vol_est": sig if sig is not None else "",
        "cor1m_prev_close": prev1m if prev1m is not None else "",
        "basis": basis,
        "source_ts": now.isoformat(timespec="seconds"),
        "note": "constituent_vol_est is DERIVED VIX/sqrt(rho), first-order, DIRECTION-ONLY",
    }

    # UPSERT, not append-once (KB-VIO-160/163) — see scripts/_daily_log.py.
    # The old guard was `if row["date"] not in existing: append`, which had TWO
    # consequences here, and the second was invisible:
    #   1. an intraday move could never reach the ledger (the shared defect); and
    #   2. the TICK->SETTLE basis upgrade above was UNREACHABLE DEAD CODE — a row
    #      first written before 16:15 ET stayed `TICK` forever, so this ledger
    #      had never once recorded a SETTLE despite computing the flag every run.
    # That matters more here than anywhere else: `^COR*` has no daily history via
    # yfinance, so this series CANNOT be backfilled — a value lost is lost.
    log_msg = "· skipped (no COR1M this run)"
    if cor1m is not None:
        status, changes = upsert_row(LEDGER, COLS, [row[c] for c in COLS],
                                     state_col="basis")
        log_msg = describe(status, row["date"], changes, LEDGER.name,
                           state_col="basis")

    d = None
    if cor1m and prev1m:
        d = 100 * (cor1m / prev1m - 1)
    arrow = "" if d is None else (f"  ({d:+.1f}% d/d)")
    state = "DISPERSED (index vol suppressed)" if (cor1m or 99) < 15 else "correlating"
    print(f"IMPLIED CORR [{row['date']} {basis}]: COR1M {cor1m}{arrow} · COR3M {cor3m} · "
          f"COR30D {cor30d} · VIX {vix} · constituent-vol[EST] {sig} · {state}")
    if not a.boot:
        print(f"  prev COR1M close {prev1m}")
        print(f"  ⚠️  constituent_vol_est is DERIVED (VIX/sqrt(rho)) — DIRECTION ONLY, never a level.")
        print(f"  ⚠️  KB-VIO-126 hook: correlations RISE + constituent vol FALLS => benign pattern wins.")
    print(f"  {log_msg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
