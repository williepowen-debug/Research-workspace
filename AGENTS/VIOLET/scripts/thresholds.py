#!/usr/bin/env python3
"""VIOLET Thresholds — live vol dashboard + daily log append.

Fetches spot VIX / VIX3M / VIX6M / VVIX / SKEW via yfinance, pulls M1/M2 futures
steepness from the shared vix_futures CLI, classifies against VIOLET thresholds,
and appends one row to AGENTS/VIOLET/workbook/VX_DAILY.tsv.

Classifications come from VIOLET/STATUS.md Signal Dashboard and KB-VIO-025
(M1:M2 contango bands).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/thresholds.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/thresholds.py --json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VX_DAILY.tsv"
VIX_FUTURES_CLI = WORKSPACE / "FORGE" / "tools" / "market-data" / "vix_futures.py"
VENV_PY = WORKSPACE / ".venv" / "bin" / "python3"

TICKERS = {
    "vix": "^VIX",
    "vix3m": "^VIX3M",
    "vix6m": "^VIX6M",
    "vvix": "^VVIX",
    "skew": "^SKEW",
}

# (label, getter, bands) — bands are (green_upper, yellow_upper, orange_upper); >orange = red
# Direction: higher = worse for most vol metrics, except VIX3M/VIX (lower = worse).
BANDS = {
    "vix":            {"green": 15,  "yellow": 20,  "orange": 30,  "red_above": True,  "fmt": "{:.2f}"},
    "vvix":           {"green": 80,  "yellow": 120, "orange": 150, "red_above": True,  "fmt": "{:.2f}"},
    "skew":           {"green": 120, "yellow": 140, "orange": 150, "red_above": True,  "fmt": "{:.2f}"},
    "vix3m_vix_ratio": {"green": 1.15, "yellow": 1.0, "orange": 0.9, "red_above": False, "fmt": "{:.3f}"},
    "m1m2_adj_pct":   {"green": 5.6, "yellow": 8.99, "orange": 12.0, "red_above": True,  "fmt": "{:+.2f}%"},
}


def classify(key: str, value: float) -> str:
    if value is None:
        return "⚪"
    b = BANDS.get(key)
    if not b:
        return "⚪"
    if b["red_above"]:
        if value < b["green"]: return "🟢"
        if value < b["yellow"]: return "🟡"
        if value < b["orange"]: return "🟠"
        return "🔴"
    else:
        if value > b["green"]: return "🟢"
        if value > b["yellow"]: return "🟡"
        if value > b["orange"]: return "🟠"
        return "🔴"


def fetch_spot() -> dict:
    import yfinance as yf
    out = {}
    for key, sym in TICKERS.items():
        try:
            tk = yf.Ticker(sym)
            out[key] = round(float(tk.fast_info["lastPrice"]), 4)
        except Exception as e:
            out[key] = None
            out[f"{key}_error"] = str(e)
    return out


def fetch_m1m2() -> dict:
    """Invoke vix_futures.py --json, return its dict (or {} on failure)."""
    try:
        result = subprocess.run(
            [str(VENV_PY), str(VIX_FUTURES_CLI), "--json"],
            capture_output=True, text=True, timeout=30, cwd=str(WORKSPACE),
        )
        if result.returncode != 0:
            return {"_error": result.stderr[:200]}
        return json.loads(result.stdout)
    except Exception as e:
        return {"_error": str(e)}


def determine_regime(vix: float | None) -> str:
    if vix is None: return "UNKNOWN"
    if vix < 15: return "COMPLACENCY"
    if vix < 20: return "LOW_VOL"
    if vix < 30: return "RISING_VOL"
    if vix < 40: return "HIGH_VOL"
    return "CRASH"


def append_daily_log(row: dict) -> bool:
    """Append one row keyed by date. Skip if date already present."""
    if not DAILY_LOG.exists():
        return False
    existing_dates = set()
    with open(DAILY_LOG) as f:
        header = f.readline().strip().split("\t")
        for line in f:
            parts = line.strip().split("\t")
            if parts and parts[0]:
                existing_dates.add(parts[0])
    if row["date"] in existing_dates:
        return False  # already logged today
    with open(DAILY_LOG, "a") as f:
        f.write("\t".join(str(row.get(col, "")) for col in header) + "\n")
    return True


def build_report() -> dict:
    now = datetime.now(timezone.utc)
    spot = fetch_spot()
    m1m2 = fetch_m1m2()

    ratio = None
    if spot.get("vix") and spot.get("vix3m"):
        ratio = round(spot["vix3m"] / spot["vix"], 4)

    m1m2_strict = None
    m1m2_adj = None
    m1_sym = ""
    m2_sym = ""
    if "_error" not in m1m2 and m1m2:
        m1m2_strict = m1m2["strict"]["steepness_pct"]
        m1m2_adj = m1m2["adjusted"]["steepness_pct"]
        m1_sym = m1m2["adjusted"]["front"]["symbol"]
        m2_sym = m1m2["adjusted"]["back"]["symbol"]

    row = {
        "date": now.strftime("%Y-%m-%d"),
        "vix": spot.get("vix") or "",
        "vix3m": spot.get("vix3m") or "",
        "vix6m": spot.get("vix6m") or "",
        "vvix": spot.get("vvix") or "",
        "skew": spot.get("skew") or "",
        "vix3m_vix_ratio": ratio if ratio is not None else "",
        "m1m2_strict_pct": m1m2_strict if m1m2_strict is not None else "",
        "m1m2_adj_pct": m1m2_adj if m1m2_adj is not None else "",
        "m1_symbol": m1_sym,
        "m2_symbol": m2_sym,
        "regime": determine_regime(spot.get("vix")),
        "source_ts": now.isoformat(timespec="seconds"),
    }

    classifications = {
        "vix": classify("vix", spot.get("vix")),
        "vvix": classify("vvix", spot.get("vvix")),
        "skew": classify("skew", spot.get("skew")),
        "vix3m_vix_ratio": classify("vix3m_vix_ratio", ratio),
        "m1m2_adj": classify("m1m2_adj_pct", m1m2_adj),
    }

    appended = append_daily_log(row)

    return {
        "row": row,
        "classifications": classifications,
        "appended_to_daily_log": appended,
        "m1m2_raw": m1m2,
    }


def print_report(rep: dict):
    row = rep["row"]
    cls = rep["classifications"]
    print(f"VIOLET THRESHOLDS  {row['date']}  UTC {row['source_ts'][-8:]}")
    print(f"  Regime: {row['regime']}")
    print(f"")
    print(f"  {cls['vix']} VIX        {row['vix']:>7}")
    print(f"     VIX3M      {row['vix3m']:>7}")
    print(f"     VIX6M      {row['vix6m']:>7}")
    print(f"  {cls['vvix']} VVIX       {row['vvix']:>7}")
    print(f"  {cls['skew']} SKEW       {row['skew']:>7}")
    print(f"  {cls['vix3m_vix_ratio']} VIX3M/VIX  {row['vix3m_vix_ratio']:>7}")
    if row['m1m2_adj_pct'] != "":
        adj = rep['m1m2_raw']['adjusted']
        strict = rep['m1m2_raw']['strict']
        print(f"  {cls['m1m2_adj']} M1:M2 adj  {row['m1m2_adj_pct']:>+7.2f}%  ({row['m1_symbol']}/{row['m2_symbol']})  [{adj['classification']}]")
        if strict['steepness_pct'] != adj['steepness_pct']:
            print(f"     M1:M2 strict {strict['steepness_pct']:+.2f}%  ({strict['m1_days_to_expiry']}d to M1 expiry, roll-contaminated)")
    else:
        err = rep['m1m2_raw'].get('_error', 'unknown')
        print(f"  ⚪ M1:M2 adj  UNAVAILABLE  ({err[:60]})")
    print()
    if rep['appended_to_daily_log']:
        print(f"  ✓ appended to VX_DAILY.tsv")
    else:
        print(f"  · VX_DAILY.tsv already has a row for {row['date']} (skip)")

    # Emit KEY_MARKERS lines for boot.py collapse mode
    hottest = [f"{k}={cls[k]}" for k in cls if cls[k] in ("🟠", "🔴")]
    if hottest:
        print(f"  ⚠️  ALERT  {' '.join(hottest)}")
    else:
        print(f"  ✓ no threshold breaches")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args(argv)

    rep = build_report()

    if args.json:
        print(json.dumps(rep, indent=2, default=str))
    else:
        print_report(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
