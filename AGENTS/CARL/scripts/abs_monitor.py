#!/usr/bin/env python3
"""
CARL ABS Trust Filing Monitor
Checks EDGAR for new 10-D filings from tracked ABS trusts.
Lists recent filings with links. Flags new filings since last check.

Phase 1: Filing detection + metadata (no PDF parsing)
Phase 2 (future): Extract EX-99.1 servicer certificate metrics

Writes to: AGENTS/CARL/scripts/data/ABS_FILINGS.tsv

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/abs_monitor.py
  .venv/bin/python3 AGENTS/CARL/scripts/abs_monitor.py --full   # show all recent, not just new
"""

import json
import sys
import time
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPTS_DIR / "data"
FILINGS_TSV = DATA_DIR / "ABS_FILINGS.tsv"

# Required EDGAR User-Agent header (SEC policy)
EDGAR_UA = "CARL Research carl@research.local"

# ABS trusts to monitor: (label, CIK, trust_filter_prefix, category)
# CIK found via SEC EDGAR company search
TRUSTS = [
    ("Santander Drive (SDART)",   "0001383094", "SDART", "subprime_auto"),
    ("Honda Auto (HAROT)",        "0001437491", "HAROT", "prime_auto"),
    ("Discover Card (DCMT/DCENT)","0001304280", "DC",    "cc"),
    ("Capital One CC",            "0001101215", "COMET", "cc"),
    ("SoFi Consumer Loan",       "0001684706", "SOFI",  "personal"),
]

TSV_HEADER = "Check_Date\tIssuer\tCategory\tFiling_Date\tAccession\tDoc\tURL"

# Rate limiting for SEC
SEC_DELAY = 0.15  # 150ms between requests (SEC allows 10/sec)


def fetch_edgar_filings(cik, form_type="10-D", count=20):
    """Fetch recent filings from EDGAR submissions API."""
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    req = urllib.request.Request(url, headers={"User-Agent": EDGAR_UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        return [], str(e)

    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accns = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])

    filings = []
    for i in range(len(forms)):
        if forms[i] == form_type:
            accn_clean = accns[i].replace("-", "")
            filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{accn_clean}/{docs[i]}"
            filings.append({
                "date": dates[i],
                "accession": accns[i],
                "doc": docs[i],
                "url": filing_url,
            })
            if len(filings) >= count:
                break

    return filings, None


def get_known_filings():
    """Load previously seen filing accession numbers from TSV."""
    known = set()
    if FILINGS_TSV.exists():
        with open(FILINGS_TSV) as f:
            next(f, None)  # skip header
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 5:
                    known.add(parts[4])  # accession number
    return known


def main():
    full_mode = "--full" in sys.argv
    now = datetime.now()
    check_date = now.strftime("%Y-%m-%d")
    run_time = now.strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  CARL ABS Trust Filing Monitor \u2014 {run_time}")
    print(f"{'='*72}")

    known_accessions = get_known_filings()
    new_filings = []
    all_filings = []

    for label, cik, prefix, category in TRUSTS:
        print(f"\n  Checking {label}...", flush=True)
        filings, error = fetch_edgar_filings(cik)
        time.sleep(SEC_DELAY)

        if error:
            print(f"    ERROR: {error[:60]}")
            continue

        if not filings:
            print(f"    No 10-D filings found")
            continue

        latest = filings[0]
        trust_new = [f for f in filings if f["accession"] not in known_accessions]

        # Display
        status = f"\U0001f534 {len(trust_new)} NEW" if trust_new else "\u2705 up to date"
        print(f"    Latest: {latest['date']}  |  Total 10-Ds: {len(filings)}  |  {status}")

        if trust_new or full_mode:
            show = trust_new if not full_mode else filings[:5]
            for f in show:
                is_new = f["accession"] not in known_accessions
                marker = "\U0001f195" if is_new else "  "
                print(f"    {marker} {f['date']}  {f['accession']}")

        for f in trust_new:
            new_filings.append((label, category, f))
        for f in filings:
            all_filings.append((label, category, f))

    # Summary
    print(f"\n  {'='*72}")
    print(f"  SUMMARY")
    print(f"  {'-'*72}")
    print(f"  Trusts checked: {len(TRUSTS)}")
    print(f"  New filings: {len(new_filings)}")
    if new_filings:
        print(f"\n  NEW FILINGS TO REVIEW:")
        for label, cat, f in new_filings:
            print(f"    \U0001f534 {label} ({cat}) \u2014 {f['date']}")
            print(f"       {f['url']}")

    # CARL-specific context
    print(f"\n  ABS THESIS CONTEXT")
    print(f"  {'-'*72}")
    print(f"  SDART: 30+ DQ 22.07%, 60+ DQ 9.31%, CNL 8.48% (Jan 2026)")
    print(f"  HAROT: 30+ DQ 1.21% (prime control, 18x gap)")
    print(f"  SoFi 2025-1: CNL 2.6% TRIGGERED (first ever)")
    print(f"  (Values from ABS_BASELINE.tsv \u2014 update with new filings)")

    # Write new filings to TSV
    if new_filings:
        DATA_DIR.mkdir(exist_ok=True)
        write_header = not FILINGS_TSV.exists()
        with open(FILINGS_TSV, "a") as f:
            if write_header:
                f.write(TSV_HEADER + "\n")
            for label, cat, filing in new_filings:
                row = "\t".join([
                    check_date, label, cat,
                    filing["date"], filing["accession"],
                    filing["doc"], filing["url"],
                ])
                f.write(row + "\n")
        print(f"\n  Wrote {len(new_filings)} new filings to {FILINGS_TSV.relative_to(SCRIPTS_DIR.parent)}")
    else:
        print(f"\n  No new filings to record")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
