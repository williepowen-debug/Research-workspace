#!/usr/bin/env python3
"""
Texas WARN Act Data Puller

PRIMARY SOURCE: TWC Excel listing (freshest — ~4-day publication lag)
  https://www.twc.texas.gov/sites/default/files/oei/docs/warn-act-listings-2026-twc.xlsx
FALLBACK SOURCE: Texas Open Data Portal (Socrata API) — full history but lags ~2-3 WEEKS.

WHY THE REPOINT (2026-07-10): The Socrata feed runs a structural ~2-3 week publication
lag behind TWC's own Excel. On 2026-07-06 the ZeniMax/Bethesda (MSFT/Xbox studio-closure
cohort, 158 wkrs) + Baker Hughes WARNs were in the Excel but INVISIBLE in Socrata — so the
Wed cron read "falsely quiet" and missed a live LAB-17-relevant filing. Excel is now primary;
Socrata is the automatic fallback if the Excel URL rots or openpyxl is unavailable. Either way
the output carries a DATA-CURRENT-THROUGH recency banner so a publication lag can never again
be silently mistaken for "no layoffs." (Owed since Jul 2 sweep; auto-memory L-04 / staleness-loud.)

NOTE: the Excel is CURRENT-YEAR only (2026). For windows reaching back into 2025
(--days >~190) it undercounts the pre-2026 tail — use --source socrata for deep history.

Usage (invoke via the venv — the Excel path needs openpyxl, which is in .venv, not system py):
  .venv/bin/python3 AGENTS/LABOR/scripts/warn_texas.py            # Last 90 days (Excel primary)
  .venv/bin/python3 AGENTS/LABOR/scripts/warn_texas.py --days 30  # Last 30 days
  .venv/bin/python3 AGENTS/LABOR/scripts/warn_texas.py --raw      # Dump windowed records as JSON
  .venv/bin/python3 AGENTS/LABOR/scripts/warn_texas.py --weekly   # Weekly aggregation (breadth)
  .venv/bin/python3 AGENTS/LABOR/scripts/warn_texas.py --source socrata  # deep-history path
(If run via bare `python3` without openpyxl, the Excel path fails safe -> Socrata fallback + loud lag banner.)
"""

import json, sys, urllib.request, urllib.parse
from datetime import datetime, timedelta, date, timezone
from collections import defaultdict

EXCEL_URL = "https://www.twc.texas.gov/sites/default/files/oei/docs/warn-act-listings-2026-twc.xlsx"
SOCRATA_BASE = "https://data.texas.gov/resource/8w53-c4f6.json"
UA = "Mozilla/5.0 (LABOR research agent; Texas WARN monitor)"  # gov sites 403 w/o a UA


def _to_iso(v):
    """Normalize an Excel cell (datetime or str) to 'YYYY-MM-DD', or None."""
    if isinstance(v, datetime):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, date):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, str) and len(v) >= 10:
        try:
            return datetime.strptime(v[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return None
    return None


def fetch_excel(days=90):
    """Primary path: TWC 2026 Excel. Returns records with Socrata-compatible keys.
    Raises on any failure so the caller can fall back to Socrata."""
    import openpyxl  # optional dep; ImportError -> caller falls back
    import io

    req = urllib.request.Request(EXCEL_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        blob = resp.read()

    wb = openpyxl.load_workbook(io.BytesIO(blob), read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        raise ValueError("empty Excel sheet")
    header = [str(h).strip().upper() if h else "" for h in rows[0]]
    idx = {name: header.index(name) for name in
           ("NOTICE_DATE", "JOB_SITE_NAME", "COUNTY_NAME", "TOTAL_LAYOFF_NUMBER", "CITY_NAME")
           if name in header}

    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).date()
    out = []
    for r in rows[1:]:
        if not r or idx.get("NOTICE_DATE") is None:
            continue
        nd = _to_iso(r[idx["NOTICE_DATE"]])
        if nd is None or datetime.strptime(nd, "%Y-%m-%d").date() < cutoff:
            continue
        n_raw = r[idx["TOTAL_LAYOFF_NUMBER"]] if idx.get("TOTAL_LAYOFF_NUMBER") is not None else 0
        try:
            n = int(n_raw) if n_raw not in (None, "") else 0
        except (ValueError, TypeError):
            n = 0
        out.append({
            "notice_date": nd + "T00:00:00.000",
            "job_site_name": str(r[idx["JOB_SITE_NAME"]]) if idx.get("JOB_SITE_NAME") is not None and r[idx["JOB_SITE_NAME"]] else "Unknown",
            "county_name": str(r[idx["COUNTY_NAME"]]) if idx.get("COUNTY_NAME") is not None and r[idx["COUNTY_NAME"]] else "Unknown",
            "total_layoff_number": n,
            "city_name": str(r[idx["CITY_NAME"]]) if idx.get("CITY_NAME") is not None and r[idx["CITY_NAME"]] else "",
        })
    out.sort(key=lambda x: x["notice_date"], reverse=True)
    return out


def fetch_socrata(days=90):
    """Fallback path: Socrata API (full history, ~2-3wk lag)."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00")
    params = urllib.parse.urlencode({
        "$where": f"notice_date >= '{cutoff}'",
        "$order": "notice_date DESC",
        "$limit": 5000,
    })
    req = urllib.request.Request(f"{SOCRATA_BASE}?{params}",
                                headers={"Accept": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch(days=90, force_source=None):
    """Excel-primary with automatic Socrata fallback. Returns (records, source_label)."""
    if force_source == "socrata":
        return fetch_socrata(days), "Socrata API (forced; ~2-3wk lag)"
    try:
        recs = fetch_excel(days)
        return recs, "TWC Excel 2026 (primary)"
    except Exception as e:  # ImportError, URL rot, parse error, network
        sys.stderr.write(f"⚠️  Excel primary failed ({type(e).__name__}: {e}) — falling back to Socrata (~2-3wk lag).\n")
        return fetch_socrata(days), "Socrata API (FALLBACK — Excel unavailable; ~2-3wk lag)"


def recency(records):
    """Newest notice_date + lag vs today. Returns (newest_iso, lag_days) or (None, None)."""
    dates = [r["notice_date"][:10] for r in records if r.get("notice_date")]
    if not dates:
        return None, None
    newest = max(dates)
    lag = (date.today() - date.fromisoformat(newest)).days
    return newest, lag


def print_banner(records, source):
    newest, lag = recency(records)
    print(f"\n{'='*60}")
    print(f"  SOURCE: {source}")
    if newest is None:
        print("  DATA CURRENT THROUGH: (no records in window)")
    else:
        flag = "⚠️ " if (lag is not None and lag > 10) else ""
        print(f"  {flag}DATA CURRENT THROUGH: {newest}  ({lag}d ago)")
        if lag is not None and lag > 10:
            print(f"  {flag}Publication lag > 10d — filings in the last ~{lag}d may not yet")
            print(f"     appear. Absence of recent notices ≠ no layoffs (falsely-quiet trap).")
    print(f"{'='*60}")


def summarize(records):
    total_workers = sum(int(r.get("total_layoff_number", 0) or 0) for r in records)
    companies = set(r.get("job_site_name", "Unknown") for r in records)
    counties = defaultdict(int)
    for r in records:
        counties[r.get("county_name", "Unknown")] += int(r.get("total_layoff_number", 0) or 0)
    top_counties = sorted(counties.items(), key=lambda x: -x[1])[:10]
    by_size = sorted(records, key=lambda r: -int(r.get("total_layoff_number", 0) or 0))[:10]
    return total_workers, len(records), len(companies), top_counties, by_size


def weekly_agg(records):
    weeks = defaultdict(lambda: {"filings": 0, "workers": 0, "companies": set()})
    for r in records:
        dt = datetime.strptime(r["notice_date"][:10], "%Y-%m-%d")
        wk = dt.strftime("%Y-W%W")
        weeks[wk]["filings"] += 1
        weeks[wk]["workers"] += int(r.get("total_layoff_number", 0) or 0)
        weeks[wk]["companies"].add(r.get("job_site_name", ""))
    return {k: {"filings": v["filings"], "workers": v["workers"], "unique_companies": len(v["companies"])}
            for k, v in sorted(weeks.items())}


def main():
    days, raw, weekly, force_source = 90, False, False, None
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--days" and i + 1 < len(args):
            days = int(args[i + 1])
        if a == "--raw":
            raw = True
        if a == "--weekly":
            weekly = True
        if a == "--source" and i + 1 < len(args):
            force_source = args[i + 1].lower()

    records, source = fetch(days, force_source)

    if raw:
        print(json.dumps(records, indent=2))
        return

    print_banner(records, source)

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
        print(f"  {dt}  {r.get('job_site_name',''):<45} {int(r.get('total_layoff_number',0) or 0):>6,}  ({r.get('city_name','')})")


if __name__ == "__main__":
    main()
