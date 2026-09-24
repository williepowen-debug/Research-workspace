#!/usr/bin/env python3
"""OZK FDIC filings watch — prints every cert-110 filing added after a baseline.

OZK files 8-K/10-Q/10-K with the FDIC, not the SEC, so EDGAR-keyed feeds never see them.
This is the instrument for the pre-reprice watch on the $350M sub notes (DOCKET L126):
any 8-K between now and 10/1 prints here; the filing list is the whole check.

    .venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py            # vs baseline id
    .venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py --since 11981

rc 0 = no new filings · rc 1 = NEW filing(s) printed · rc 2 = fetch failed (UNKNOWN — not "quiet")
"""
import argparse
import json
import sys
import urllib.request

API = "https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/cert/110"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
# Baseline = newest filing as of the 2026-09-24 sweep: FLNG 11981, the Q2'26 10-Q filed 2026-08-05 (182 filings).
BASELINE_ID = 11981


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, default=BASELINE_ID, help="print filings with instFlngId above this")
    a = ap.parse_args()
    try:
        req = urllib.request.Request(API, headers={"User-Agent": UA})
        rows = json.load(urllib.request.urlopen(req, timeout=30))
    except Exception as e:  # a failed pull is UNKNOWN, never a quiet result
        print(f"FLNG-WATCH 2 UNKNOWN: fetch failed ({e.__class__.__name__}: {e}) — the watch did NOT run")
        return 2
    new = sorted((r for r in rows if r["instFlngId"] > a.since), key=lambda r: r["instFlngId"])
    if not new:
        print(f"FLNG-WATCH 0 QUIET: {len(rows)} filings on file, none after id {a.since} — swept and empty at FDIC FLNG cert 110")
        return 0
    print(f"FLNG-WATCH 1 NEW: {len(new)} filing(s) after id {a.since} — read each; a sub-notes redemption/refi is a 🟠 REGINALD signal")
    for r in new:
        added = (r.get("sysAddRecDttm") or "")[:10]
        for att in r.get("instFlngAtchList") or []:
            print(f"  {added}  FLNG {r['instFlngId']}/{att['instFlngAtchId']}  {att['instFlngAtchOrglNme']}")
            print(f"      {API.rsplit('/cert', 1)[0]}/{r['instFlngId']}/attachment/{att['instFlngAtchId']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
