#!/usr/bin/env python3
"""
CARL ABS Trust Filing Monitor
Checks EDGAR for new 10-D filings from tracked ABS trusts.
Lists recent filings with links. Flags new filings since last check.

== SCOPE (Phase 1) ==
This script DETECTS new 10-D filings. It does NOT parse them.

  Detection (works now):
    - Queries EDGAR submissions API for each tracked trust CIK
    - Identifies 10-D filings newer than last run (via accession dedup)
    - Records filing date, accession number, URL to ABS_FILINGS.tsv
    - Outputs actionable URL list for manual review

  Parsing (future work — likely OTTO's domain):
    A proper parser would need to:
    1. Fetch the 10-D index page (HTML)
    2. Locate the EX-99.1 servicer certificate (exhibit filename varies)
    3. Parse the monthly report tables to extract:
         - 30+/60+/90+ delinquency rates
         - Net loss rate (monthly and cumulative CNL)
         - Payment rate (CC) or prepayment rate (auto)
         - Pool factor / principal balance
         - Charge-off rate
    4. Compare extracted values against ABS_BASELINE.tsv thresholds
    5. Flag CNL trigger breaches, DQ escalations, payment rate drops

    Challenges: Each issuer uses different EX-99.1 templates (SDART vs HAROT vs COMET
    vs DCENT vs Exeter all differ). Parser needs per-issuer handlers. This is the
    real value-add but requires dedicated buildout.

== SCOPE LIMITATIONS ==
  - SoFi consumer loan ABS is PRIVATE (144A) and has NO public 10-D filings.
    VX-CARL-ABS-16 (SoFi 2025-1 CNL 2.6% TRIGGERED) cannot be refreshed via
    this script. See KB-CARL-078 for details.

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

# ABS trusts to monitor
# Two registration patterns exist on EDGAR:
#   - "depositor": single CIK files 10-Ds for ALL trust vintages (SDART, COMET, DCENT)
#   - "per_vintage": each trust vintage is its own registrant (HAROT)
# CIKs verified Apr 14 2026 via EDGAR submissions API.
# SoFi skipped: consumer loan ABS uses private/144A structure, no public 10-D filings.
# CNL trigger data (SoFi 2025-1 at 2.6%) comes from trustee reports to investors, not SEC.
TRUSTS = [
    # Subprime auto canary — Santander depositor files for all SDART trusts
    {"label": "SDART (Santander subprime auto)", "category": "subprime_auto",
     "pattern": "depositor", "ciks": ["0001383094"]},

    # Prime auto control — each HAROT vintage files separately
    # Tracking 4 most recent vintages (drops older as new ones issued)
    {"label": "HAROT (Honda prime auto)", "category": "prime_auto",
     "pattern": "per_vintage", "ciks": [
         "0002077602",  # HAROT 2025-3
         "0002089171",  # HAROT 2025-4
         "0002100818",  # HAROT 2026-1
         "0002062789",  # HAROT 2025-2
     ]},

    # Credit card master trusts — single CIK each, monthly 10-Ds
    {"label": "COMET (Capital One CC)", "category": "cc",
     "pattern": "depositor", "ciks": ["0001163321"]},

    # DCENT/DCMT removed Apr 14 2026 — Discover trusts entered defeasance post-CapOne merger.
    # DCMT filed Form 15-12G (deregistration) Dec 19 2025. DCENT reports are post-defeasance
    # only (investor payment tracking, no DQ/loss data). See KB-CARL-208. Discover CC
    # performance data now rolls into COMET.
    # {"label": "DCENT (Discover CC)", "category": "cc",
    #  "pattern": "depositor", "ciks": ["0001407200"]},

    # Deep subprime auto — Exeter (S&P flagged elevated losses, fills VX-CARL-ABS-11)
    # ⛔ SPLIT INTO TWO ENTRIES 2026-09-11. DO NOT RE-MERGE, AND DO NOT LET THE
    # REGISTERED PANEL "ROLL FORWARD" WITH NEW VINTAGES.
    #
    # THE DEFECT THIS FIXES (4 sessions owed, KB-CARL-398/399/400): this monitor
    # tracked only the four NEWEST Exeter vintages (7-15mo seasoning) while V2's
    # REGISTERED grading panel is EART 2022-2 / 2022-3 / 2023-1 / 2024-1 (31-52mo).
    # The two sets are DISJOINT. So the monitor reported clean against deals the
    # thesis does not grade, and CARL twice graded the wrong deal set off it
    # (8/27 and again on the first pass 9/1). Both pulls were clean at the primary
    # and collection-month matched, so nothing looked wrong — which is why a
    # monitor that cannot see its own panel is worse than no monitor.
    # [[finding_instrument_reports_clean_against_the_wrong_reference]]
    #
    # The newest-vintage set is kept: it is the NEW-ISSUE pipeline and answers a
    # different question (origination quality). It is simply not V2's panel.
    {"label": "Exeter — V2 REGISTERED PANEL (deep subprime, 31-52mo seasoning)",
     "category": "subprime_auto", "registered_panel": True,
     "pattern": "per_vintage", "ciks": [
         "0001920761",  # EART 2022-2 — CIK verified at data.sec.gov 2026-09-11, 52 10-Ds, latest 2026-08-31
         "0001931330",  # EART 2022-3 — verified, 50 10-Ds, latest 2026-08-31
         "0001964225",  # EART 2023-1 — verified, 43 10-Ds, latest 2026-08-31
         "0002005087",  # EART 2024-1 — verified, 31 10-Ds, latest 2026-08-31
     ]},

    # New-issue pipeline — NOT the V2 grading panel. Origination-quality question only.
    {"label": "Exeter — new-issue pipeline (NOT V2's panel)", "category": "subprime_auto",
     "pattern": "per_vintage", "ciks": [
         "0002101848",  # Exeter 2026-1
         "0002092528",  # Exeter 2025-5
         "0002078220",  # Exeter 2025-4
         "0002067124",  # Exeter 2025-3
     ]},

    # Prime/near-prime auto — Ally (comparison vs SDART subprime, fills VX-CARL-ABS-12)
    {"label": "Ally (prime/near-prime auto)", "category": "prime_auto",
     "pattern": "per_vintage", "ciks": [
         "0002087070",  # Ally 2025-1
         "0002035124",  # Ally 2024-2
         "0002010413",  # Ally 2024-1
         "0001980826",  # Ally 2023-1
     ]},

    # Subprime auto — GM Financial (AmeriCredit successor + legacy AmeriCredit trusts)
    {"label": "GM Financial / AmeriCredit (subprime auto)", "category": "subprime_auto",
     "pattern": "per_vintage", "ciks": [
         "0002099048",  # GMF Consumer 2025-4
         "0002047316",  # GMF Consumer 2024-4
         "0002020251",  # AmeriCredit 2024-1
         "0001987878",  # AmeriCredit 2023-2
     ]},
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

    for issuer in TRUSTS:
        label = issuer["label"]
        category = issuer["category"]
        pattern = issuer["pattern"]
        ciks = issuer["ciks"]

        print(f"\n  Checking {label}...", flush=True)

        # Aggregate filings across all CIKs for this issuer
        issuer_filings = []
        errors = []
        for cik in ciks:
            filings, error = fetch_edgar_filings(cik)
            time.sleep(SEC_DELAY)
            if error:
                errors.append((cik, error))
                continue
            for f in filings:
                f["cik"] = cik
                issuer_filings.append(f)

        if not issuer_filings:
            if errors:
                print(f"    ERROR(s): {errors[0][1][:60]}")
            else:
                print(f"    No 10-D filings found")
            continue

        # Sort by date (most recent first)
        issuer_filings.sort(key=lambda f: f["date"], reverse=True)
        latest = issuer_filings[0]
        trust_new = [f for f in issuer_filings if f["accession"] not in known_accessions]

        # Display
        pattern_tag = "[depositor]" if pattern == "depositor" else f"[{len(ciks)} trusts]"
        status = f"\U0001f534 {len(trust_new)} NEW" if trust_new else "\u2705 up to date"
        print(f"    {pattern_tag}  Latest: {latest['date']}  |  Total 10-Ds: {len(issuer_filings)}  |  {status}")

        if trust_new or full_mode:
            show = trust_new if not full_mode else issuer_filings[:5]
            for f in show:
                is_new = f["accession"] not in known_accessions
                marker = "\U0001f195" if is_new else "  "
                print(f"    {marker} {f['date']}  {f['accession']}  (CIK {f['cik']})")

        if errors:
            for cik, err in errors:
                print(f"    \u26a0\ufe0f  CIK {cik} failed: {err[:40]}")

        for f in trust_new:
            new_filings.append((label, category, f))
        for f in issuer_filings:
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
