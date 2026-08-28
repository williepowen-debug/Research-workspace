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

import json, sys, urllib.request, urllib.error


class EdgarError(Exception):
    """A reportable EDGAR failure (bad CIK, 403, transport) — not a crash."""

BASE = "https://efts.sec.gov/LATEST/search-index"
SUBMISSIONS = "https://data.sec.gov/submissions/CIK{}.json"

# SEC requires a DECLARED-CONTACT UA and throttles/403s generic ones. Kept
# identical in shape to edgar_doc.py's, which is the verified-working form —
# this file previously declared a placeholder (research@example.com).
HEADERS = {"User-Agent": "Research DEWEY williepowen@gmail.com", "Accept": "application/json"}

def fetch_filings(cik, filing_type=None, limit=10):
    """Returns (name, filings). Raises EdgarError with a READABLE message.

    ⚠️ Never let urllib traceback out of here. A transport error is a REPORTABLE
    RESULT (a bad CIK is a 404, SEC throttling is a 403), and a traceback reads
    to the caller as "the tool is broken" rather than "that CIK does not exist".
    Same defect class fixed in fetch_url.py on 2026-08-02; logged for this file
    2026-08-12 and re-hit 2026-08-27 (the build gate's own 2-hit rule).
    """
    if not cik or cik.startswith("-"):
        raise EdgarError(f"{cik!r} is not a CIK. Usage: edgar_fetch.py CIK "
                         "[--type FORM] [--limit N]  (CIK lookup: "
                         "https://www.sec.gov/files/company_tickers.json)")
    cik_padded = cik.lstrip("0").zfill(10)
    url = SUBMISSIONS.format(cik_padded)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        hint = (f"  no such CIK on EDGAR — verify at "
                f"https://www.sec.gov/files/company_tickers.json"
                if e.code == 404 else
                "  SEC wants a DECLARED-CONTACT User-Agent ('Research NAME email'); "
                "a browser UA gets 403 here" if e.code == 403 else "")
        raise EdgarError(f"HTTP {e.code} for CIK {cik} ({url})\n{hint}".rstrip()) from e
    except urllib.error.URLError as e:
        raise EdgarError(f"transport error for CIK {cik}: "
                         f"{type(e.reason).__name__}: {e.reason}") from e
    except json.JSONDecodeError as e:
        raise EdgarError(f"EDGAR returned non-JSON for CIK {cik}: {e}") from e
    
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
    if not args or args[0] in ("-h", "--help"):
        print("Usage: python3 edgar_fetch.py CIK [--type FORM] [--limit N]")
        print("  CIK lookup: https://www.sec.gov/files/company_tickers.json")
        print("  e.g. python3 edgar_fetch.py 0000799850 --type 8-K --limit 5")
        return 0 if args else 2
    
    cik = args[0]
    filing_type = None
    limit = 10
    
    for i, a in enumerate(args[1:], 1):
        if a == "--type" and i + 1 < len(args):
            filing_type = args[i + 1]
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
    
    try:
        name, filings = fetch_filings(cik, filing_type, limit)
    except EdgarError as e:
        sys.stderr.write(f"{e}\n")
        return 1
    
    print(f"\n=== {name} (CIK: {cik}) ===\n")
    for f in filings:
        acc_clean = f['accession'].replace("-", "")
        url = f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{acc_clean}/"
        print(f"  {f['date']}  {f['form']:<10}  {f['description']}")
        print(f"           {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
