#!/usr/bin/env python3
"""
FRED Data Pull — Reusable script for Federal Reserve Economic Data
Usage:
  python3 fred_pull.py SERIES_ID                    # Latest 10 observations
  python3 fred_pull.py SERIES_ID --limit 50         # Latest 50
  python3 fred_pull.py SERIES_ID --start 2024-01-01 # From date
  python3 fred_pull.py SERIES_ID --all              # Full history
  python3 fred_pull.py SERIES_ID --csv              # Output as CSV

Common series:
  BAMLH0A0HYM2  — HY OAS (ICE BofA)
  BAMLC0A0CM    — IG OAS
  SOFR          — Secured Overnight Financing Rate
  RRPONTSYD     — Reverse Repo
  U6RATE        — U-6 Unemployment
  UNRATE        — Unemployment Rate
  ICSA          — Initial Jobless Claims
  CCSA          — Continuing Claims
"""

import json, os, sys, urllib.request, urllib.parse

def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib
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

API_KEY = _fred_key()
BASE = "https://api.stlouisfed.org/fred/series/observations"

def fetch(series_id, limit=None, start=None, all_data=False):
    """limit=None means unbounded. A `start` with no explicit `limit` returns the
    WHOLE range: capping an ascending-sorted range would silently return only the
    oldest N rows of it (the caller asks for 11 years, gets 10 days of 2015)."""
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json",
        "sort_order": "desc",
    }
    if start:
        params["observation_start"] = start
        params["sort_order"] = "asc"
    if not all_data and limit is not None:
        params["limit"] = limit

    url = f"{BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("observations", [])

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 fred_pull.py SERIES_ID [--limit N] [--start YYYY-MM-DD] [--all] [--csv]")
        return
    
    series_id = args[0]
    limit = None
    start = None
    all_data = False
    csv_mode = False

    for i, a in enumerate(args[1:], 1):
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
        if a == "--start" and i + 1 < len(args):
            start = args[i + 1]
        if a == "--all":
            all_data = True
        if a == "--csv":
            csv_mode = True
    
    # Default to the latest 10 ONLY for a bare call. With --start, an unset --limit
    # means "the whole range" (see fetch()); capping it would silently drop the range.
    if limit is None and start is None:
        limit = 10

    obs = fetch(series_id, limit, start, all_data)

    if csv_mode:
        print("date,value")
        for o in obs:
            print(f"{o['date']},{o['value']}")
    else:
        print(f"\n=== {series_id} (Latest {len(obs)} observations) ===\n")
        for o in obs:
            print(f"  {o['date']}  {o['value']}")

if __name__ == "__main__":
    main()
