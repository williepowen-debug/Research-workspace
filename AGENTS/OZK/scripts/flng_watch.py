#!/usr/bin/env python3
"""OZK FDIC filings watch — prints every cert-110 filing added after a baseline.

OZK files 8-K/10-Q/10-K with the FDIC, not the SEC, so EDGAR-keyed feeds never see them.
This is the instrument for the pre-reprice watch on the $350M sub notes (DOCKET L126 / L463):
any 8-K between now and 10/1 prints here; the filing list is the whole check.

    .venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py            # vs baseline id
    .venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py --since 11981
    .venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py --selftest # fixture tests, no network

rc 0 = no newer filing RETURNED by a response that passed schema + coverage checks
       (a reprice is then SCHEDULED-UNCONTRADICTED, never CONFIRMED)
rc 1 = NEW filing(s) printed
rc 2 = UNKNOWN — fetch failed, or the response was malformed/incomplete. Never read as quiet.
"""
import argparse
import json
import sys
import urllib.request

API = "https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/cert/110"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
# Baseline = newest filing as of the 2026-09-24 sweep: FLNG 11981, the Q2'26 10-Q filed 2026-08-05 (182 filings).
BASELINE_ID = 11981
# Coverage floor: the list held 182 filings on 2026-09-24 and only grows. A response far below it is truncated.
MIN_ROWS = 170


def evaluate(rows, since, baseline=BASELINE_ID, min_rows=MIN_ROWS):
    """Pure verdict on a decoded response -> (rc, message, new_rows). No network, no printing."""
    if not isinstance(rows, list):
        return 2, f"UNKNOWN: response is {type(rows).__name__}, not a list — schema changed or error body", []
    if len(rows) < min_rows:
        return 2, f"UNKNOWN: only {len(rows)} filings returned (floor {min_rows}) — incomplete response", []
    bad = [i for i, r in enumerate(rows)
           if not isinstance(r, dict) or not isinstance(r.get("instFlngId"), int) or isinstance(r.get("instFlngId"), bool)]
    if bad:
        return 2, f"UNKNOWN: {len(bad)} row(s) lack an integer instFlngId (first at index {bad[0]}) — malformed response", []
    ids = {r["instFlngId"] for r in rows}
    if len(ids) < min_rows:
        return 2, f"UNKNOWN: only {len(ids)} unique filing ids among {len(rows)} rows (floor {min_rows}) — duplicated/incomplete response", []
    if baseline not in ids and max(ids) < baseline:
        return 2, f"UNKNOWN: baseline FLNG {baseline} absent and newest id {max(ids)} is older — response does not cover the baseline", []
    new = sorted((r for r in rows if r["instFlngId"] > since), key=lambda r: r["instFlngId"])
    if not new:
        return 0, (f"QUIET: {len(rows)} filings returned (schema + coverage OK), none after id {since} — "
                   f"no newer filing RETURNED at FDIC FLNG cert 110"), []
    return 1, f"NEW: {len(new)} filing(s) after id {since} — read each; a sub-notes redemption/refi is a 🟠 REGINALD signal", new


def selftest():
    def row(i, name="x.pdf"):
        return {"instFlngId": i, "sysAddRecDttm": "2026-09-30T00:00:00",
                "instFlngAtchList": [{"instFlngAtchId": 1, "instFlngAtchOrglNme": name}]}
    base = [row(i) for i in range(11800, 11800 + 181)] + [row(BASELINE_ID)]
    cases = [
        ("normal: baseline present, nothing newer", base, 0),
        ("normal: one new filing", base + [row(12001, "8-K.pdf")], 1),
        ("missing: empty list", [], 2),
        ("missing: empty object", {}, 2),
        ("missing: error body", {"Message": "error"}, 2),
        ("missing: truncated list", base[-20:], 2),
        ("malformed: row without instFlngId", base + [{"sysAddRecDttm": "2026-09-30"}], 2),
        ("malformed: string id", base[:-1] + [dict(row(0), instFlngId="11981")], 2),
        ("malformed: non-dict row", base + ["oops"], 2),
        ("coverage: baseline absent and all ids older", [row(i) for i in range(11000, 11000 + 182)], 2),
        ("coverage: 182 copies of the baseline row (1 unique id)", [row(BASELINE_ID) for _ in range(182)], 2),
    ]
    fails = 0
    for name, data, want in cases:
        got = evaluate(data, BASELINE_ID)[0]
        ok = got == want
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  rc {got} (want {want})  {name}")
    print(f"FLNG-WATCH SELFTEST {'PASS' if not fails else 'FAIL'}: {len(cases) - fails}/{len(cases)}")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, default=BASELINE_ID, help="print filings with instFlngId above this")
    ap.add_argument("--selftest", action="store_true", help="run fixture tests (no network) and exit")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        req = urllib.request.Request(API, headers={"User-Agent": UA})
        rows = json.load(urllib.request.urlopen(req, timeout=30))
    except Exception as e:  # a failed pull is UNKNOWN, never a quiet result
        print(f"FLNG-WATCH 2 UNKNOWN: fetch failed ({e.__class__.__name__}: {e}) — the watch did NOT run")
        return 2
    rc, msg, new = evaluate(rows, a.since)
    print(f"FLNG-WATCH {rc} {msg}")
    for r in new:
        added = str(r.get("sysAddRecDttm") or "")[:10]
        for att in r.get("instFlngAtchList") or [{"instFlngAtchId": "?", "instFlngAtchOrglNme": "(no attachment list)"}]:
            print(f"  {added}  FLNG {r['instFlngId']}/{att.get('instFlngAtchId')}  {att.get('instFlngAtchOrglNme')}")
            print(f"      {API.rsplit('/cert', 1)[0]}/{r['instFlngId']}/attachment/{att.get('instFlngAtchId')}")
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # never let a crash's exit code collide with rc 1 NEW
        print(f"FLNG-WATCH 2 UNKNOWN: internal error ({e.__class__.__name__}: {e}) — the watch did NOT complete")
        sys.exit(2)
