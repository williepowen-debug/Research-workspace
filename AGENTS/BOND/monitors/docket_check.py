#!/usr/bin/env python3
"""BOND — docket coverage check.

WHY THIS EXISTS
---------------
On 2026-08-18 BOND discovered that the **August quarterly refunding**
($125B, 8/11-8/13, the largest supply event of the quarter) had run
**ungraded** -- because it was never on `docket/CATALYSTS.tsv` at all.

That failure mode is invisible to every other guard this desk has:
  * a STALE value eventually looks wrong and gets caught on review;
  * a MISSING event looks like nothing, and no boot step, monitor or
    staleness alarm can surface a row that does not exist.

The docket was hand-maintained against BOND's own memory. This check
derives it from the ISSUER instead: it asks TreasuryDirect what is
actually scheduled and diffs that against what BOND has docketed.

USAGE
-----
    python3 monitors/docket_check.py [--days 21]

    rc 0 = every upcoming auction inside the window is docketed
    rc 1 = UNDOCKETED auction(s) found -- add them before closeout
    rc 2 = fetch failure (fail LOUD; a silent pass here would recreate
           exactly the blindness this script was written to remove)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

TD_UPCOMING = "https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json"
UA = {"User-Agent": "BOND-research/1.0 (williepowen@gmail.com)"}
HERE = Path(__file__).resolve().parent
CATALYSTS = HERE.parent / "docket" / "CATALYSTS.tsv"

# Bills are not BOND's instrument class; coupons are.
COUPON_TYPES = {"Note", "Bond"}


def fetch_upcoming() -> list[dict]:
    req = urllib.request.Request(TD_UPCOMING, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 200:
            raise RuntimeError(f"TreasuryDirect returned HTTP {r.status}")
        data = json.load(r)
    if not isinstance(data, list) or not data:
        # A 200 with an empty body is a FAILURE, not "no auctions scheduled".
        raise RuntimeError(
            "TreasuryDirect returned 200 with an empty/!list payload. "
            "Treating as a fetch failure -- an empty result here would read as "
            "'nothing scheduled' and silently reproduce the 8/18 blind spot."
        )
    return data


def load_docket_text() -> str:
    if not CATALYSTS.exists():
        raise RuntimeError(f"docket not found: {CATALYSTS}")
    return CATALYSTS.read_text(encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=21,
                    help="look-ahead window in calendar days (default 21)")
    args = ap.parse_args()

    today = dt.date.today()
    horizon = today + dt.timedelta(days=args.days)

    try:
        rows = fetch_upcoming()
        docket = load_docket_text()
    except Exception as e:  # fail loud, never silently pass
        print(f"[docket_check] FETCH/READ FAILURE: {e}", file=sys.stderr)
        print("[docket_check] rc=2 -- this is NOT a pass. Re-run before closeout.",
              file=sys.stderr)
        return 2

    upcoming = []
    for r in rows:
        if r.get("securityType") not in COUPON_TYPES:
            continue
        try:
            ad = dt.date.fromisoformat(r["auctionDate"][:10])
        except Exception:
            continue
        if today <= ad <= horizon:
            upcoming.append(r)
    upcoming.sort(key=lambda x: x["auctionDate"])

    missing, present = [], []
    for r in upcoming:
        cusip = (r.get("cusip") or "").strip()
        ad = r["auctionDate"][:10]
        # A row counts as docketed only if the CUSIP appears -- a bare date is
        # not enough, because a date can be docketed for the WRONG instrument
        # (the 8/18 JGB-vs-UST 20Y fusion is the worked example).
        (present if cusip and cusip in docket else missing).append(r)

    print(f"[docket_check] window {today} -> {horizon} ({args.days}d)")
    print(f"[docket_check] upcoming coupon auctions: {len(upcoming)} "
          f"| docketed: {len(present)} | MISSING: {len(missing)}")

    for r in present:
        print(f"   ok   {r['auctionDate'][:10]}  {r.get('securityTerm',''):16} "
              f"{r.get('cusip','')}  tips={r.get('tips','')}")

    if not missing:
        print("[docket_check] rc=0 -- docket covers every scheduled coupon auction in the window.")
        return 0

    print("\n[docket_check] 🔴 UNDOCKETED — add these to docket/CATALYSTS.tsv before closeout:",
          file=sys.stderr)
    for r in missing:
        amt = r.get("offeringAmount")
        amt_s = f"${float(amt)/1e9:.0f}B" if amt else "size TBA"
        print(f"   MISSING  {r['auctionDate'][:10]}  {r.get('securityTerm',''):16} "
              f"{r.get('cusip','')}  {amt_s}  tips={r.get('tips','')}  "
              f"reopening={r.get('reopening','')}", file=sys.stderr)
    print("\n[docket_check] ⚠️ Record the INSTRUMENT, not just the date: a TIPS reopening and a "
          "nominal of the same tenor have different buyer bases and different benchmarks.",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
