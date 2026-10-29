#!/usr/bin/env python3
"""TA_WS field-name compatibility — one home for the TreasuryDirect schema rename.

⚠️ BUILT 2026-10-29. Between the 10/20 and 10/29 sessions TreasuryDirect's
`TA_WS/securities/{auctioned,upcoming}` dropped `auctionDate`, `tips` and the four
competitive-award fields every BOND auction tool keys on. Nothing errored at the
HTTP layer: the grader died on a KeyError, and `docket_check` read a 6-row feed
with no parsable date as "feed sees through NOTHING" and returned rc=0 over an
EMPTY coupon set while the 10/29 7Y sat in the feed — the v1 degenerate pass
(KB-BND-198/203) back through a different door.

The new names were validated against the local corpus before adoption: every
mapping below reproduced `data/auction_history_v2_prome-spawned.csv` on all 153
overlapping (cusip, issue_date) rows, zero mismatches (KB-BND row of 2026-10-29).
`subtotalCompetitiveParAwardedOutsideOfOfferingAmount` was 0 on all 161 coupon
rows in the feed; it is added to the inside amount so a nonzero value can never
silently drop out of the competitive total.

Rule: an OLD key the feed still sends always wins (never overwritten). A row with
neither name stays without the key, so callers fail loud exactly as before.

    python3 monitors/ta_ws_schema.py --selftest
"""
from __future__ import annotations

import sys

# old key -> new key (single-field renames)
RENAMES = {
    "auctionDate": "competitiveAuctionCloseDate",
    "tips": "inflationProtected",
    "primaryDealerAccepted": "primaryDealersCompetitiveParAwarded",
    "indirectBidderAccepted": "indirectBiddersCompetitiveParAwarded",
    "directBidderAccepted": "directBiddersCompetitiveParAwarded",
}
COMP_IN = "subtotalCompetitiveParAwardedInsideOfOfferingAmount"
COMP_OUT = "subtotalCompetitiveParAwardedOutsideOfOfferingAmount"


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def normalize(rows):
    """Fill legacy keys in place from their 2026-10 names; returns the same list."""
    if not isinstance(rows, list):
        return rows
    for r in rows:
        if not isinstance(r, dict):
            continue
        for old, new in RENAMES.items():
            if old not in r and r.get(new) not in (None, ""):
                r[old] = r[new]
        if "competitiveAccepted" not in r:
            a, b = _num(r.get(COMP_IN)), _num(r.get(COMP_OUT))
            if a is not None:
                r["competitiveAccepted"] = str(int(a + (b or 0.0)))
    return rows


def selftest() -> int:
    fails = []
    new = {"cusip": "912810UX4", "competitiveAuctionCloseDate": "2026-10-21T00:00:00",
           "inflationProtected": "No", "primaryDealersCompetitiveParAwarded": "1323150000",
           "indirectBiddersCompetitiveParAwarded": "7502510000",
           "directBiddersCompetitiveParAwarded": "4075000000",
           COMP_IN: "12900660000", COMP_OUT: "0"}
    r = normalize([dict(new)])[0]
    if r.get("auctionDate", "")[:10] != "2026-10-21": fails.append("auctionDate not mapped")
    if r.get("tips") != "No": fails.append("tips not mapped")
    if r.get("competitiveAccepted") != "12900660000": fails.append("competitive total wrong")
    if r.get("indirectBidderAccepted") != "7502510000": fails.append("indirect not mapped")
    old = dict(new, auctionDate="2026-01-01T00:00:00", tips="Yes")
    r = normalize([old])[0]
    if r["auctionDate"] != "2026-01-01T00:00:00" or r["tips"] != "Yes":
        fails.append("legacy key overwritten")
    r = normalize([dict(new, **{COMP_OUT: "5"})])[0]
    if r["competitiveAccepted"] != "12900660005": fails.append("outside amount dropped")
    r = normalize([{"cusip": "X"}])[0]
    if "auctionDate" in r or "competitiveAccepted" in r: fails.append("key invented from nothing")
    if normalize({"a": 1}) != {"a": 1}: fails.append("non-list mutated")
    for f in fails:
        print(f"  ❌ {f}")
    print(f"[ta_ws_schema --selftest] {'🔴 FAILED' if fails else '✅ 6 checks passed'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else 0)
