#!/usr/bin/env python3
"""
HENRY Data Update Script
Pulls live market data using FORGE/tools/market-data/fetch.py
Appends new row to workbook/MARKET_DATA.tsv

Usage:
  python3 scripts/update_data.py              # fetch and append
  python3 scripts/update_data.py --print      # show latest row only
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HENRY_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = HENRY_DIR / "workbook"
DATA_TSV = WORKBOOK / "MARKET_DATA.tsv"

# Tickers we track (must match STATUS.md Market Data table)
PRICE_TICKERS = ["^GSPC", "^VIX", "BZ=F", "JPY=X", "KRE", "APO"]
FRED_SERIES = {
    "BAMLH0A0HYM2": ("HY_OAS", 100),  # Multiply by 100 for bps
    "BAMLH0A3HYC": ("CCC_OAS", 100),   # Multiply by 100 for bps
    "DGS10": ("10Y_Yield", 1),
}

TSV_HEADER = "Date\tSPX\tVIX\tBrent\tGas\t10Y_Yield\tUSDJPY\tHY_OAS\tCCC_OAS\tKRE\tAPO\tSource\n"


def run_fetch(command):
    """Run fetch.py and return JSON output."""
    fetch_py = HENRY_DIR.parent.parent / "FORGE" / "tools" / "market-data" / "fetch.py"
    try:
        result = subprocess.run(
            [sys.executable, str(fetch_py)] + command,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print(f"fetch.py error: {result.stderr}", file=sys.stderr)
            return None
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error running fetch.py: {e}", file=sys.stderr)
        return None


def fetch_prices():
    """Fetch price data for tracked tickers."""
    data = run_fetch(["price"] + PRICE_TICKERS + ["--json"])
    if not data:
        return {}
    
    result = {}
    for ticker, info in data.items():
        if "error" in info:
            continue
        # Map ticker names to our column names
        mapping = {
            "^GSPC": "SPX",
            "^VIX": "VIX",
            "BZ=F": "Brent",
            "JPY=X": "USDJPY",
            "KRE": "KRE",
            "APO": "APO",
        }
        col = mapping.get(ticker)
        if col:
            result[col] = info.get("price")
    return result


def fetch_fred():
    """Fetch FRED data for tracked series."""
    result = {}
    for series_id, (col_name, multiplier) in FRED_SERIES.items():
        data = run_fetch(["fred", series_id, "--json"])
        if data and "observations" in data and len(data["observations"]) > 0:
            latest = data["observations"][0]
            try:
                val = float(latest["value"])
                if val is not None and val == val:  # Check for NaN
                    result[col_name] = val * multiplier
            except (ValueError, TypeError):
                pass
    return result


def fetch_gas():
    """Fetch gas price from FRED."""
    data = run_fetch(["fred", "GASREGW", "--json"])
    if data and "observations" in data and len(data["observations"]) > 0:
        latest = data["observations"][0]
        try:
            val = float(latest["value"])
            if val is not None and val == val:
                return val
        except (ValueError, TypeError):
            pass
    return None


def get_latest_row():
    """Read the latest row from MARKET_DATA.tsv."""
    if not DATA_TSV.exists():
        return None
    
    # ⚠️ COMMENT-AWARE 2026-08-28. This used to do `headers = lines[0]`, which broke the
    # moment MARKET_DATA.tsv gained its CAPTURE-BASIS GUARD header (7 leading `#` lines):
    # lines[0] became a comment, so zip() paired a 1-element header against a 12-element
    # row and returned a ONE-KEY dict with NO error and rc=0 — the QUIET failure class
    # (SIG-W-20260828-019). Caught by running the parser rather than assuming the append
    # was additive. -> finding_a_correction_pass_is_unreviewed_work.
    lines = [l for l in DATA_TSV.read_text().strip().split("\n")
             if l.strip() and not l.startswith("#")]
    if len(lines) < 2:  # Header only
        return None

    headers = lines[0].split("\t")
    latest = lines[-1].split("\t")
    if len(headers) != len(latest):
        # FAIL LOUD rather than return a silently-short dict.
        raise ValueError(
            f"MARKET_DATA.tsv schema mismatch: header has {len(headers)} cols, "
            f"latest row has {len(latest)}. Refusing to return a partial row.")
    return dict(zip(headers, latest))


def append_row(data):
    """Append a new row to MARKET_DATA.tsv."""
    WORKBOOK.mkdir(exist_ok=True)
    
    # Create file with header if it doesn't exist
    if not DATA_TSV.exists():
        DATA_TSV.write_text(TSV_HEADER)
    
    # Build row
    today = datetime.now().strftime("%Y-%m-%d")
    row = [
        today,
        str(data.get("SPX", "")),
        str(data.get("VIX", "")),
        str(data.get("Brent", "")),
        str(data.get("Gas", "")),
        str(data.get("10Y_Yield", "")),
        str(data.get("USDJPY", "")),
        str(data.get("HY_OAS", "")),
        str(data.get("CCC_OAS", "")),
        str(data.get("KRE", "")),
        str(data.get("APO", "")),
        "fetch.py",
    ]
    
    with open(DATA_TSV, "a") as f:
        f.write("\t".join(row) + "\n")
    
    return row


def main():
    if "--print" in sys.argv:
        latest = get_latest_row()
        if latest:
            print("Latest data row:")
            for k, v in latest.items():
                print(f"  {k}: {v}")
        else:
            print("No data found.")
        return
    
    print("Fetching price data...")
    prices = fetch_prices()
    
    print("Fetching FRED data...")
    fred = fetch_fred()
    
    print("Fetching gas price...")
    gas = fetch_gas()
    
    # Merge data
    data = {**prices, **fred}
    if gas:
        data["Gas"] = gas
    

    
    if not data:
        print("No data fetched.", file=sys.stderr)
        sys.exit(1)
    
    # Append to TSV
    append_row(data)
    
    print(f"Data appended to {DATA_TSV}")
    print("Values:")
    for k, v in data.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
