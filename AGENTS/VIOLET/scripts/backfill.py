#!/usr/bin/env python3
"""VIOLET Backfill — populate VX_DAILY.tsv with historical data.

Pulls:
  - yfinance daily history for ^VIX, ^VIX3M, ^VIX6M, ^VVIX, ^SKEW (default 90 days)
  - CBOE VX futures settlement CSV for each trading day (default 30 days)

Merges into workbook/VX_DAILY.tsv. Rows keyed by date; existing rows are
updated (not duplicated), preserving columns the backfill doesn't touch.

⚠️  M1:M2 CONVENTION HAZARD — UNRESOLVED (VIOLET 6/13, Orc). The m1m2 path here
    writes SAME-DAY settlement keyed to the row date and does NOT stamp
    m1m2_settle_date. thresholds.py writes m1m2 as T-1 (prior settle) WITH the
    stamp. The two conventions DISAGREE. The ~79 currently-blank m1m2 cells are
    protected only by the skip-if-present guard (backfill_m1m2). DO NOT run the
    m1m2 path (full backfill, or --m1m2-only) until the convention is resolved —
    it would inject same-day/unstamped values into a T-1 series. `--spot-only` is
    always safe (skips m1m2 entirely). See MAINTENANCE.md (#4 convention decision).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py --spot-only   # SAFE
  .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py --spot-days 180   # spot only
  # full / --m1m2-only: BLOCKED on the convention decision — see hazard note above
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VX_DAILY.tsv"

TICKERS = {"vix": "^VIX", "vix3m": "^VIX3M", "vix6m": "^VIX6M", "vvix": "^VVIX", "skew": "^SKEW"}
CBOE_URL = "https://www.cboe.com/us/futures/market_statistics/settlement/csv/"
ROLL_WINDOW = 5


def load_existing() -> tuple[list[str], dict[str, dict]]:
    """Return (header, {date: row_dict})."""
    if not DAILY_LOG.exists():
        raise FileNotFoundError(DAILY_LOG)
    with open(DAILY_LOG) as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = {r["date"]: r for r in reader if r.get("date")}
        header = reader.fieldnames or []
    return header, rows


def write_merged(header: list[str], rows: dict[str, dict]):
    sorted_dates = sorted(rows.keys())
    with open(DAILY_LOG, "w") as f:
        f.write("\t".join(header) + "\n")
        for d in sorted_dates:
            row = rows[d]
            f.write("\t".join(str(row.get(col, "") or "") for col in header) + "\n")


def determine_regime(vix: float | None) -> str:
    if vix is None:
        return "UNKNOWN"
    if vix < 15: return "COMPLACENCY"
    if vix < 20: return "LOW_VOL"
    if vix < 30: return "RISING_VOL"
    if vix < 40: return "HIGH_VOL"
    return "CRASH"


def backfill_spot(days: int, rows: dict[str, dict]) -> int:
    import yfinance as yf
    import pandas as pd

    period = f"{max(days + 10, 30)}d"
    print(f"  Fetching yfinance history ({period}) for {list(TICKERS.values())}")
    hist = {}
    for key, sym in TICKERS.items():
        tk = yf.Ticker(sym)
        df = tk.history(period=period, auto_adjust=False)
        if df.empty:
            print(f"    ⚠ {sym}: empty history")
            continue
        # Normalize each Series's index to plain date BEFORE concat — tz-aware
        # DatetimeIndex types can differ subtly between tickers, which causes
        # pd.concat(axis=1) to emit two rows per date (one per ticker) instead
        # of one merged row. .date() before concat collapses them correctly.
        s = df["Close"]
        s.index = [d.date() if hasattr(d, "date") else d for d in s.index]
        hist[key] = s

    if "vix" not in hist:
        print("  ✗ cannot backfill: no VIX history")
        return 0

    # Combine into aligned date index
    df = pd.concat(hist, axis=1).dropna(how="all")
    # Holiday guard: yfinance ^VIX sometimes carries forward on US market holidays
    # (e.g. Memorial Day) while companion tickers correctly skip. Require ^VIX3M
    # corroboration; an orphan ^VIX row is treated as a phantom and dropped.
    if "vix3m" in df.columns:
        df = df[df["vix3m"].notna()]

    touched = 0
    for d, series in df.iterrows():
        d_str = d.isoformat()
        row = rows.get(d_str, {"date": d_str})
        changed = False
        for key in TICKERS:
            if key in hist and not pd.isna(series.get(key)):
                val = round(float(series[key]), 4)
                if str(row.get(key, "")) != str(val):
                    row[key] = val
                    changed = True
        # Recompute derived columns when we have both
        vix = row.get("vix")
        vix3m = row.get("vix3m")
        if vix and vix3m:
            try:
                row["vix3m_vix_ratio"] = round(float(vix3m) / float(vix), 4)
                changed = True
            except (ValueError, ZeroDivisionError):
                pass
        if vix:
            try:
                row["regime"] = determine_regime(float(vix))
            except ValueError:
                pass
        if changed:
            rows[d_str] = row
            touched += 1
    return touched


def fetch_cboe_settlement(query_date: date) -> list[dict]:
    r = requests.get(
        CBOE_URL, params={"dt": query_date.isoformat()},
        headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.cboe.com/"},
        timeout=15,
    )
    if r.status_code != 200:
        return []
    reader = csv.DictReader(io.StringIO(r.text))
    out = []
    for row in reader:
        if row.get("Product") != "VX":
            continue
        sym = row["Symbol"]
        # Standard monthlies only: VX/XN (no digits between VX and /)
        prefix = sym.split("/")[0] if "/" in sym else sym
        if prefix != "VX":
            continue
        try:
            out.append({
                "symbol": sym,
                "expiration": datetime.strptime(row["Expiration Date"], "%Y-%m-%d").date(),
                "price": float(row["Price"]),
            })
        except (ValueError, KeyError):
            pass
    out.sort(key=lambda r: r["expiration"])
    return out


def compute_m1m2(contracts: list[dict], as_of: date) -> tuple[float | None, float | None, str, str]:
    live = [c for c in contracts if c["expiration"] > as_of]
    if len(live) < 2:
        return None, None, "", ""
    m1, m2 = live[0], live[1]
    strict = (m2["price"] - m1["price"]) / m1["price"] * 100
    dte = (m1["expiration"] - as_of).days
    if dte < ROLL_WINDOW and len(live) >= 3:
        m3 = live[2]
        adj = (m3["price"] - m2["price"]) / m2["price"] * 100
        return round(strict, 4), round(adj, 4), m2["symbol"], m3["symbol"]
    return round(strict, 4), round(strict, 4), m1["symbol"], m2["symbol"]


def backfill_m1m2(days: int, rows: dict[str, dict], pause_s: float = 0.5) -> int:
    # Runtime guardrail — fires at the moment of danger even if the docstring
    # went unread (VIOLET 6/13, Orc). The convention is unresolved; this path
    # writes SAME-DAY/unstamped m1m2, inconsistent with thresholds.py's T-1 series.
    print("  ⚠️  M1:M2 CONVENTION HAZARD: this path writes SAME-DAY/unstamped m1m2,")
    print("      inconsistent with thresholds.py's T-1 series — convention UNRESOLVED")
    print("      (VIOLET 6/13). Prefer --spot-only until decided. See MAINTENANCE.md.")
    today = date.today()
    touched = 0
    requested = 0
    skipped_existing = 0
    for i in range(days + 1):
        d = today - timedelta(days=i)
        # Skip weekends
        if d.weekday() >= 5:
            continue
        d_str = d.isoformat()
        row = rows.get(d_str, {"date": d_str})
        if row.get("m1m2_adj_pct") not in (None, "", 0, "0"):
            skipped_existing += 1
            continue
        requested += 1
        try:
            contracts = fetch_cboe_settlement(d)
        except Exception as e:
            print(f"    ✗ {d_str}: {e}")
            continue
        if not contracts:
            continue
        strict, adj, m1s, m2s = compute_m1m2(contracts, d)
        if adj is None:
            continue
        row["m1m2_strict_pct"] = strict
        row["m1m2_adj_pct"] = adj
        row["m1_symbol"] = m1s
        row["m2_symbol"] = m2s
        rows[d_str] = row
        touched += 1
        time.sleep(pause_s)
    print(f"  CBOE: requested {requested} dates, touched {touched}, skipped {skipped_existing} (already present)")
    return touched


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--spot-days", type=int, default=90)
    p.add_argument("--m1m2-days", type=int, default=30)
    p.add_argument("--spot-only", action="store_true")
    p.add_argument("--m1m2-only", action="store_true")
    args = p.parse_args(argv)

    header, rows = load_existing()
    print(f"Loaded {len(rows)} existing rows from {DAILY_LOG.name}")

    if not args.m1m2_only:
        print(f"\n[1/2] Backfilling spot history ({args.spot_days} days)...")
        touched = backfill_spot(args.spot_days, rows)
        print(f"  touched {touched} rows")

    if not args.spot_only:
        print(f"\n[2/2] Backfilling M1:M2 steepness ({args.m1m2_days} trading days)...")
        touched = backfill_m1m2(args.m1m2_days, rows)
        print(f"  touched {touched} rows")

    write_merged(header, rows)
    print(f"\n✓ wrote {len(rows)} rows to {DAILY_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
