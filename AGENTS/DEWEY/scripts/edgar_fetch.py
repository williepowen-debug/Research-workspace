#!/usr/bin/env python3
"""
SEC EDGAR Fetch — Pull recent filings for a company
Usage:
  python3 edgar_fetch.py CIK                    # Latest 10 filings
  python3 edgar_fetch.py CIK --type 10-K        # Filter by filing type
  python3 edgar_fetch.py CIK --type 8-K --limit 5

Known CIKs (verified vs SEC company_tickers.json, 2026-06-20):
  WAL:  0001212545  Western Alliance Bancorporation
  OZK:  0001569650  Bank OZK
  ZION: 0000109380  Zions Bancorporation
  EGBN: 0001050441  Eagle Bancorp
  APO:  0001858681  Apollo Global Management
  MFIC: 0001278752  MidCap Financial Investment Corp
  BXSL: 0001736035  Blackstone Secured Lending Fund
  KRE:  (ETF — no filings)

  Always verify a CIK before citing — map ticker->CIK via
  https://www.sec.gov/files/company_tickers.json (authoritative).
  (Prior version of this cheatsheet had 4 of 5 CIKs wrong — WAL pointed at Old Republic.)
"""

import json, sys, urllib.request

BASE = "https://efts.sec.gov/LATEST/search-index"
SUBMISSIONS = "https://data.sec.gov/submissions/CIK{}.json"

HEADERS = {"User-Agent": "Research Agent research@example.com", "Accept": "application/json"}

def fetch_filings(cik, filing_type=None, limit=10):
    cik_padded = cik.lstrip("0").zfill(10)
    url = SUBMISSIONS.format(cik_padded)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    descriptions = recent.get("primaryDocDescription", [])
    
    results = []
    for i in range(len(forms)):
        if filing_type and forms[i] != filing_type:
            continue
        results.append({
            "form": forms[i],
            "date": dates[i] if i < len(dates) else "",
            "accession": accessions[i] if i < len(accessions) else "",
            "description": descriptions[i] if i < len(descriptions) else "",
        })
        if len(results) >= limit:
            break
    
    company_name = data.get("name", "Unknown")
    return company_name, results

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 edgar_fetch.py CIK [--type FORM] [--limit N]")
        return
    
    cik = args[0]
    filing_type = None
    limit = 10
    
    for i, a in enumerate(args[1:], 1):
        if a == "--type" and i + 1 < len(args):
            filing_type = args[i + 1]
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
    
    name, filings = fetch_filings(cik, filing_type, limit)
    
    print(f"\n=== {name} (CIK: {cik}) ===\n")
    for f in filings:
        acc_clean = f['accession'].replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{acc_clean}/"
        print(f"  {f['date']}  {f['form']:<10}  {f['description']}")
        print(f"           {url}")

if __name__ == "__main__":
    main()
