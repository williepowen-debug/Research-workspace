#!/usr/bin/env python3
"""
Texas WARN Act Data Puller
Pulls from Texas Open Data Portal (Socrata API) — no API key needed.

Usage:
  python3 warn_texas.py              # Last 90 days summary
  python3 warn_texas.py --days 30    # Last 30 days
  python3 warn_texas.py --raw        # Dump all records as JSON
  python3 warn_texas.py --weekly     # Weekly aggregation (breadth signal)
"""

import json, sys, urllib.request, urllib.parse
from datetime import datetime, timedelta
from collections import defaultdict

BASE = "https://data.texas.gov/resource/8w53-c4f6.json"

def fetch(days=90):
    cutoff = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00")
    params = urllib.parse.urlencode({
        "$where": f"notice_date >= '{cutoff}'",
        "$order": "notice_date DESC",
        "$limit": 5000
    })
    url = f"{BASE}?{params}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def summarize(records):
    total_workers = sum(int(r.get("total_layoff_number", 0)) for r in records)
    companies = set(r.get("job_site_name", "Unknown") for r in records)
    counties = defaultdict(int)
    for r in records:
        counties[r.get("county_name", "Unknown")] += int(r.get("total_layoff_number", 0))

    top_counties = sorted(counties.items(), key=lambda x: -x[1])[:10]

    # Largest single layoffs
    by_size = sorted(records, key=lambda r: -int(r.get("total_layoff_number", 0)))[:10]

    return total_workers, len(records), len(companies), top_counties, by_size

def weekly_agg(records):
    weeks = defaultdict(lambda: {"filings": 0, "workers": 0, "companies": set()})
    for r in records:
        dt = datetime.strptime(r["notice_date"][:10], "%Y-%m-%d")
        # ISO week
        wk = dt.strftime("%Y-W%W")
        weeks[wk]["filings"] += 1
        weeks[wk]["workers"] += int(r.get("total_layoff_number", 0))
        weeks[wk]["companies"].add(r.get("job_site_name", ""))
    return {k: {"filings": v["filings"], "workers": v["workers"], "unique_companies": len(v["companies"])} 
            for k, v in sorted(weeks.items())}

def main():
    days = 90
    raw = False
    weekly = False
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--days" and i + 1 < len(args):
            days = int(args[i + 1])
        if a == "--raw":
            raw = True
        if a == "--weekly":
            weekly = True

    records = fetch(days)

    if raw:
        print(json.dumps(records, indent=2))
        return

    if weekly:
        wk = weekly_agg(records)
        print(f"\n{'Week':<12} {'Filings':>8} {'Workers':>10} {'Companies':>10}")
        print("-" * 44)
        for k, v in wk.items():
            print(f"{k:<12} {v['filings']:>8} {v['workers']:>10,} {v['unique_companies']:>10}")
        return

    total_workers, num_filings, num_companies, top_counties, top_layoffs = summarize(records)

    print(f"\n=== TEXAS WARN DATA — Last {days} Days ===")
    print(f"Total filings:  {num_filings}")
    print(f"Total workers:  {total_workers:,}")
    print(f"Unique firms:   {num_companies}")
    print(f"\n--- Top Counties by Affected Workers ---")
    for county, count in top_counties:
        print(f"  {county:<25} {count:>8,}")
    print(f"\n--- Largest Layoffs ---")
    for r in top_layoffs:
        dt = r.get("notice_date", "")[:10]
        print(f"  {dt}  {r.get('job_site_name',''):<45} {int(r.get('total_layoff_number',0)):>6,}  ({r.get('city_name','')})")

if __name__ == "__main__":
    main()
