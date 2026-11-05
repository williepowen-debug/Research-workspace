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
`subtotalCompetitiveParAwardedOutsideOfOfferingAmount` is empty or 0 on every coupon
row in the feed; it is added to the inside amount so a nonzero value can never
silently drop out of the competitive total.

Rules (2026-11-05, after the independent read returned HOLD, DOCKET L859):
- An old key that is absent or empty is filled from its new name.
- Both names present and agreeing: the row proceeds.
- Both names present and DIFFERENT: neither is trusted; the row is marked and the
  callers refuse it. A row with neither name stays without the key.
- A missing key does NOT fail loud by itself: `r.get("tips") == "Yes"` reads False.
  Callers must ask `coupon_row_defect()`, which is what makes an unknown value a
  refusal instead of a nominal row.

    python3 monitors/ta_ws_schema.py --selftest
"""
from __future__ import annotations

import datetime as dt
import re
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
CONFLICT = "_schema_conflict"          # set by normalize(); list of disagreeing old keys
KNOWN_TYPES = ("Bill", "Note", "Bond")
COUPON_TYPES = ("Note", "Bond")
YES_NO_FIELDS = ("tips", "floatingRate", "reopening")


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _same(key, a, b):
    """Do two spellings of one field say the same thing?"""
    if key == "auctionDate":
        return str(a)[:10] == str(b)[:10]
    x, y = _num(a), _num(b)
    if x is not None and y is not None:
        return x == y
    return str(a).strip() == str(b).strip()


def iso_date(value):
    """The date in a feed timestamp, or None. Never guesses a format."""
    m = re.match(r"^\d{4}-\d{2}-\d{2}(?:T|$)", str(value or ""))
    if not m:
        return None
    try:
        return dt.date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def type_defect(rows):
    """A row whose securityType is missing or unknown: reason, or None."""
    for r in rows:
        if not isinstance(r, dict) or r.get("securityType") not in KNOWN_TYPES:
            got = r.get("securityType", "<absent>") if isinstance(r, dict) else type(r).__name__
            return f"securityType {got!r} is outside {KNOWN_TYPES}"
    return None


def coupon_row_defect(r, fields=YES_NO_FIELDS):
    """Why this coupon row cannot be trusted, or None. `fields` must read exactly Yes or No."""
    who = r.get("cusip", "?")
    if r.get(CONFLICT):
        return f"{who}: old and new field names disagree on {', '.join(r[CONFLICT])}"
    if iso_date(r.get("auctionDate")) is None:
        return f"{who}: auction date {r.get('auctionDate')!r} is absent or not ISO"
    for k in fields:
        if r.get(k) not in ("Yes", "No"):
            return f"{who}: {k} = {r.get(k, '<absent>')!r}, expected Yes or No"
    return None


def normalize(rows):
    """Fill legacy keys in place from their 2026-10 names; mark disagreements; returns the same list."""
    if not isinstance(rows, list):
        return rows
    for r in rows:
        if not isinstance(r, dict):
            continue
        conflicts = []
        for old, new in RENAMES.items():
            have_old, have_new = r.get(old) not in (None, ""), r.get(new) not in (None, "")
            if have_new and not have_old:
                r[old] = r[new]
            elif have_new and have_old and not _same(old, r[old], r[new]):
                conflicts.append(old)
        a, b = _num(r.get(COMP_IN)), _num(r.get(COMP_OUT))
        if a is not None:
            total = str(int(a + (b or 0.0)))
            if r.get("competitiveAccepted") in (None, ""):
                r["competitiveAccepted"] = total
            elif not _same("competitiveAccepted", r["competitiveAccepted"], total):
                conflicts.append("competitiveAccepted")
        if conflicts:
            r[CONFLICT] = conflicts
    return rows


def selftest() -> int:
    fails, ran = [], []

    def check(name, ok):
        ran.append(name)
        if not ok:
            fails.append(name)

    new = {"cusip": "912810UX4", "competitiveAuctionCloseDate": "2026-10-21T00:00:00",
           "inflationProtected": "No", "primaryDealersCompetitiveParAwarded": "1323150000",
           "indirectBiddersCompetitiveParAwarded": "7502510000",
           "directBiddersCompetitiveParAwarded": "4075000000",
           COMP_IN: "12900660000", COMP_OUT: "0"}
    r = normalize([dict(new)])[0]
    expected = {"auctionDate": "competitiveAuctionCloseDate", "tips": "inflationProtected",
                "primaryDealerAccepted": "primaryDealersCompetitiveParAwarded",
                "indirectBidderAccepted": "indirectBiddersCompetitiveParAwarded",
                "directBidderAccepted": "directBiddersCompetitiveParAwarded"}
    for o, n in expected.items():           # a list of its own, so deleting a rename fails here
        check(f"rename {o} mapped", r.get(o) == new[n])
        e = normalize([dict(new, **{o: ""})])[0]
        check(f"empty old {o} filled from new", e.get(o) == new[n] and CONFLICT not in e)
        c = normalize([dict(new, **{o: "2020-01-01T00:00:00" if o == "auctionDate" else "Maybe" if o == "tips" else "1"})])[0]
        check(f"disagreeing {o} marked", o in c.get(CONFLICT, []))
    check("competitive total summed", r.get("competitiveAccepted") == "12900660000")
    check("no conflict on a new-only row", CONFLICT not in r)
    a = normalize([dict(new, auctionDate="2026-10-21T13:00:00", tips="No", primaryDealerAccepted="1323150000.00")])[0]
    check("agreeing old and new proceed", CONFLICT not in a)
    t = normalize([dict(new, competitiveAccepted="1")])[0]
    check("disagreeing competitive total marked", "competitiveAccepted" in t.get(CONFLICT, []))
    r = normalize([dict(new, **{COMP_OUT: "5"})])[0]
    check("outside amount kept", r["competitiveAccepted"] == "12900660005")
    r = normalize([{"cusip": "X"}])[0]
    check("no key invented from nothing", "auctionDate" not in r and "competitiveAccepted" not in r)
    check("non-list untouched", normalize({"a": 1}) == {"a": 1})
    good = dict(new, auctionDate="2026-10-21T00:00:00", tips="No", floatingRate="No", reopening="Yes")
    check("good row has no defect", coupon_row_defect(good) is None)
    for k in YES_NO_FIELDS:
        check(f"{k} true refused", coupon_row_defect(dict(good, **{k: "true"})) is not None)
        check(f"{k} absent refused", coupon_row_defect({a: b for a, b in good.items() if a != k}) is not None)
    for bad in ("", None, "11/09/2026", "TBA", "2026-13-45", "20261109"):
        check(f"date {bad!r} refused", coupon_row_defect(dict(good, auctionDate=bad)) is not None)
    check("marked row refused", coupon_row_defect(dict(good, **{CONFLICT: ["tips"]})) is not None)
    check("type vocabulary passes", type_defect([{"securityType": t} for t in KNOWN_TYPES]) is None)
    check("unknown type refused", type_defect([{"securityType": "Treasury Note"}]) is not None)
    check("absent type refused", type_defect([{"cusip": "X"}]) is not None)
    for f in fails:
        print(f"  ❌ {f}")
    print(f"[ta_ws_schema --selftest] {'🔴 ' + str(len(fails)) + ' FAILED of ' + str(len(ran)) if fails else '✅ ' + str(len(ran)) + ' checks passed'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else 0)
