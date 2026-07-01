#!/usr/bin/env python3
"""
CARL Gas Price Tracker
Fetches current gas prices from AAA and tracks them against CARL thesis thresholds.
Also pulls FRED GASREGW (weekly EIA average) for comparison.

Tracks:
  - National average (regular, premium, diesel)
  - State-level (FL, TX, CA — CARL priority states)
  - Days above $4.00 behavioral breakpoint
  - Days above $4.50 next breakpoint

Writes to: AGENTS/CARL/scripts/data/GAS_TRACKER.tsv (append daily row)

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/gas_tracker.py
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPTS_DIR / "data"
GAS_TSV = DATA_DIR / "GAS_TRACKER.tsv"

# FRED config
def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib, sys
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    print("WARN: FRED_API_KEY not found (env or FORGE/tools/market-data/.env) — FRED pulls will fail", file=sys.stderr)
    return ""

FRED_API_KEY = _fred_key()
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

from bs4 import BeautifulSoup

AAA_NATIONAL_URL = "https://gasprices.aaa.com/"
AAA_STATE_URL = "https://gasprices.aaa.com/state-gas-price-averages/"

# Thresholds
BREAKPOINT_1 = 4.00  # behavioral breakpoint (FIRED per STATUS.md)
BREAKPOINT_2 = 4.50  # next breakpoint (CRL-08)
RED_LEVEL = 5.00     # severe stress

TSV_HEADER = "Date\tNational_Reg\tNational_Mid\tNational_Prem\tNational_Diesel\tFL\tTX\tCA\tFRED_GASREGW\tWeek_Chg\tAbove_4\tAbove_4_50\tStatus"


def fred_fetch(series_id, limit=2):
    """Fetch latest FRED observation."""
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CARL-Monitor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        obs = data.get("observations", [])
        return [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
    except Exception as e:
        return [{"error": str(e)}]


def _scrape_page(url):
    """Fetch a page and return BeautifulSoup."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    })
    with urllib.request.urlopen(req, timeout=15) as resp:
        return BeautifulSoup(resp.read().decode(), "html.parser")


def fetch_aaa_national():
    """Scrape AAA national gas prices. Returns dict or None."""
    try:
        soup = _scrape_page(AAA_NATIONAL_URL)
        tables = soup.find_all("table")
        if not tables:
            return None
        # First table: Current Avg row has Regular/Mid/Premium/Diesel/E85
        rows = tables[0].find_all("tr")
        for row in rows:
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            if cells and "Current" in cells[0]:
                return {
                    "regular": cells[1] if len(cells) > 1 else None,
                    "midgrade": cells[2] if len(cells) > 2 else None,
                    "premium": cells[3] if len(cells) > 3 else None,
                    "diesel": cells[4] if len(cells) > 4 else None,
                }
        return None
    except Exception as e:
        print(f"  WARNING: AAA national scrape failed: {e}")
        return None


def fetch_aaa_states():
    """Scrape AAA state-level gas prices. Returns dict {state: regular_price}."""
    result = {}
    try:
        soup = _scrape_page(AAA_STATE_URL)
        tables = soup.find_all("table")
        if not tables:
            return result
        for row in tables[0].find_all("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            if len(cells) >= 2:
                state_name = cells[0]
                # Map full name -> abbreviation
                name_map = {"Florida": "FL", "Texas": "TX", "California": "CA"}
                abbr = name_map.get(state_name)
                if abbr:
                    result[abbr] = cells[1]  # Regular price
        return result
    except Exception as e:
        print(f"  WARNING: AAA state scrape failed: {e}")
        return result


def safe_float(val):
    """Convert to float, stripping $ if present."""
    if val is None:
        return None
    try:
        return float(str(val).replace("$", "").replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def status_for(price):
    """Return status string for a gas price."""
    if price is None:
        return "NO_DATA"
    if price >= RED_LEVEL:
        return "RED"
    if price >= BREAKPOINT_2:
        return "ORANGE"
    if price >= BREAKPOINT_1:
        return "YELLOW"
    if price >= 3.50:
        return "GREEN_ELEVATED"
    return "GREEN"


def has_today_row(tsv_path):
    """Check if TSV already has today's date."""
    if not tsv_path.exists():
        return False
    today = datetime.now().strftime("%Y-%m-%d")
    with open(tsv_path) as f:
        next(f, None)  # skip header
        for line in f:
            if line.startswith(today):
                return True
    return False


def count_days_above(tsv_path, threshold):
    """Count consecutive days above threshold from latest row backward."""
    if not tsv_path.exists():
        return 0
    rows = []
    with open(tsv_path) as f:
        next(f, None)
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                try:
                    rows.append(float(parts[1]))
                except ValueError:
                    pass
    count = 0
    for price in reversed(rows):
        if price >= threshold:
            count += 1
        else:
            break
    return count


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  CARL Gas Price Tracker \u2014 {now}")
    print(f"{'='*72}")

    # --- FRED weekly average ---
    print(f"\n  Fetching FRED GASREGW...", flush=True)
    fred_obs = fred_fetch("GASREGW", limit=4)
    fred_price = None
    fred_prior = None
    if fred_obs and "error" not in fred_obs[0]:
        try:
            fred_price = float(fred_obs[0]["value"])
            if len(fred_obs) > 1:
                fred_prior = float(fred_obs[1]["value"])
        except (ValueError, KeyError):
            pass

    # --- AAA prices ---
    print(f"  Fetching AAA national prices...", flush=True)
    national = fetch_aaa_national()
    print(f"  Fetching AAA state prices...", flush=True)
    states = fetch_aaa_states()

    nat_reg = safe_float(national.get("regular")) if national else None
    nat_mid = safe_float(national.get("midgrade")) if national else None
    nat_prem = safe_float(national.get("premium")) if national else None
    nat_diesel = safe_float(national.get("diesel")) if national else None
    fl_price = safe_float(states.get("FL"))
    tx_price = safe_float(states.get("TX"))
    ca_price = safe_float(states.get("CA"))

    # Use best available national price (AAA > FRED)
    best_national = nat_reg or fred_price

    # --- Compute week change ---
    week_chg = None
    if fred_price and fred_prior:
        week_chg = fred_price - fred_prior

    # --- Display ---
    print(f"\n  NATIONAL GAS PRICES")
    print(f"  {'-'*64}")

    if nat_reg:
        print(f"  Regular:    ${nat_reg:.3f}   {status_for(nat_reg)}")
    if nat_mid:
        print(f"  Midgrade:   ${nat_mid:.3f}")
    if nat_prem:
        print(f"  Premium:    ${nat_prem:.3f}")
    if nat_diesel:
        print(f"  Diesel:     ${nat_diesel:.3f}   {status_for(nat_diesel)}")

    if fred_price:
        chg_str = f"  ({week_chg:+.3f} WoW)" if week_chg else ""
        print(f"  FRED wkly:  ${fred_price:.3f}   (as of {fred_obs[0]['date']}){chg_str}")

    if not nat_reg and fred_price:
        print(f"  (AAA unavailable \u2014 using FRED GASREGW as fallback)")
        nat_reg = fred_price  # fallback for status/threshold

    print(f"\n  STATE-LEVEL (Regular)")
    print(f"  {'-'*64}")
    for label, price in [("FL", fl_price), ("TX", tx_price), ("CA", ca_price)]:
        if price:
            print(f"  {label}:  ${price:.3f}   {status_for(price)}")
        else:
            print(f"  {label}:  no data")

    # --- Threshold check ---
    print(f"\n  THRESHOLD STATUS")
    print(f"  {'-'*64}")
    if best_national:
        if best_national >= BREAKPOINT_2:
            print(f"  \U0001f534 ABOVE $4.50 \u2014 next behavioral breakpoint BREACHED")
        elif best_national >= BREAKPOINT_1:
            gap = BREAKPOINT_2 - best_national
            print(f"  \U0001f7e0 ABOVE $4.00 \u2014 behavioral breakpoint ACTIVE (${gap:.2f} to $4.50)")
        else:
            print(f"  \U0001f7e2 Below $4.00 \u2014 behavioral breakpoint not yet active")
    else:
        print(f"  \u26a0\ufe0f  No price data available")

    # --- Append to TSV ---
    DATA_DIR.mkdir(exist_ok=True)
    if not has_today_row(GAS_TSV):
        days_above_4 = count_days_above(GAS_TSV, BREAKPOINT_1)
        days_above_450 = count_days_above(GAS_TSV, BREAKPOINT_2)
        if best_national and best_national >= BREAKPOINT_1:
            days_above_4 += 1
        if best_national and best_national >= BREAKPOINT_2:
            days_above_450 += 1

        status = status_for(best_national)
        wc = f"{week_chg:+.3f}" if week_chg else ""
        row = "\t".join([
            today,
            f"{nat_reg:.3f}" if nat_reg else "",
            f"{nat_mid:.3f}" if nat_mid else "",
            f"{nat_prem:.3f}" if nat_prem else "",
            f"{nat_diesel:.3f}" if nat_diesel else "",
            f"{fl_price:.3f}" if fl_price else "",
            f"{tx_price:.3f}" if tx_price else "",
            f"{ca_price:.3f}" if ca_price else "",
            f"{fred_price:.3f}" if fred_price else "",
            wc,
            str(days_above_4),
            str(days_above_450),
            status,
        ])

        write_header = not GAS_TSV.exists()
        with open(GAS_TSV, "a") as f:
            if write_header:
                f.write(TSV_HEADER + "\n")
            f.write(row + "\n")
        print(f"\n  \u2705 Appended to {GAS_TSV.relative_to(SCRIPTS_DIR.parent)}")
        print(f"     Days above $4.00: {days_above_4}")
        print(f"     Days above $4.50: {days_above_450}")
    else:
        print(f"\n  \u23e9 TSV already has today's row \u2014 skipping append")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
