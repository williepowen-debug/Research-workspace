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

WHY IT WAS REBUILT (2026-08-27, KB-BND-198)
-------------------------------------------
The v1 check reported a **claim stronger than what it measured**, and it
did so on the exact event class it was written to protect.

Measured at the primary 2026-08-27: `TA_WS/securities/upcoming` returned
**4 rows, ALL BILLS, max auctionDate 2026-09-01** -- a ~5-day forward
horizon against a claimed 21-day window. v1's empty-payload guard checked
the RAW payload (4 rows, non-empty, so it did not fire), THEN filtered to
`{Note, Bond}` (leaving zero), found nothing missing from an empty set,
and printed:

    rc=0 -- docket covers every scheduled coupon auction in the window.

That sentence is a claim about the WORLD. What was actually proved is
"no undocketed coupon auction exists IN MY REFERENCE SET" -- and the
reference set was empty. **A check run over an empty or truncated
reference set returns the same rc=0 as a real pass.**

The guard was at the wrong layer: it protected the FETCH and not the
REFERENCE SET the verdict is computed over.

Underneath is a structural limit, not a coding bug: `upcoming` lists only
formally ANNOUNCED auctions (~1 week ahead for coupons). The forward
schedule lives in the quarterly refunding statement -- a PDF outside
TA_WS -- so **no API path closes it.** And the gap is WIDEST for the
LARGEST events, because refundings announce ~1 week out: on 2026-08-27
the September refunding (~9/8-9/10) sat ~12 days out, inside the claimed
window and invisible to the guard. This tool's own founding failure, set
up to recur.

WHAT v2 DOES INSTEAD
--------------------
1. **Never reports a degenerate pass.** The headline states what was
   actually verified -- "VERIFIED THROUGH <date>" -- never "covers the
   window" when the window was not observable.
2. **Measures the feed's own horizon** (max auctionDate across ALL rows,
   bills included -- bills bound how far the feed can SEE) and names the
   BLIND SPAN it cannot cover.
3. **Declares the blind span UNVERIFIED and does not adjudicate it.**
   TWO drafts of v2 tried to auto-clear the span by text-matching the
   docket, so the tool could stay quiet when the span looked covered.
   Both were wrong in the SAME direction (silencing), and the second was
   caught only by RUNNING it: among the rows it counted as September
   coverage was **this desk's own warning row reading "SEPTEMBER COUPON
   CALENDAR IS NOT DOCKETED"**. The guard read the alarm as proof the
   alarm had been handled.

   A commentary row and a real auction row are not reliably separable by
   vocabulary. So any auto-clear is v1's disease wearing a new costume:
   a verdict stronger than the measurement. **The tool now reports the
   span as unverified every run and lists docket contents as INFORMATION,
   never as a verdict.**

   That is not alarm fatigue, because it is not an alarm -- it is a
   permanent, accurate scope statement, which is exactly what v1 lacked.
   The owed action lives where it belongs: as a dated row on the DOCKET,
   not in this tool's exit code.

USAGE
-----
    python3 monitors/docket_check.py [--days 21]
    python3 monitors/docket_check.py --selftest

    rc 0 = nothing ACTIONABLE found. ⚠️ NOT a statement that the window is
           covered -- read the VERIFIED THROUGH line for what was actually
           established. This tool proves coverage only as far as the feed
           can see.
    rc 1 = an undocketed coupon auction the feed CAN see -- add it to
           docket/CATALYSTS.tsv before closeout
    rc 2 = fetch/read failure (fail LOUD; a silent pass here would
           recreate exactly the blindness this script was written to
           remove)
"""
from __future__ import annotations

import argparse
import datetime as dt
import inspect
import json
import re
import sys
import urllib.request
from pathlib import Path

TD_UPCOMING = "https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json"
UA = {"User-Agent": "BOND-research/1.0 (williepowen@gmail.com)"}
HERE = Path(__file__).resolve().parent
CATALYSTS = HERE.parent / "docket" / "CATALYSTS.tsv"

# Bills are not BOND's instrument class; coupons are.
COUPON_TYPES = {"Note", "Bond"}

# Does a docket EVENT row identify a scheduled coupon auction?
#
# ⚠️ THIS PREDICATE IS ADVISORY ONLY AND MUST STAY THAT WAY. It was twice used
# to auto-clear the blind span, and both times it silenced the tool wrongly:
#   1st (caught by --selftest on its first run): the bare word AUCTION matched
#       "non-auction", because `-` is a word boundary.
#   2nd (caught only by RUNNING it live): scanning the WHOLE LINE, it counted
#       four non-auction rows as September coverage -- a buyback op, the FOMC,
#       the Canadian tariff row, and this desk's OWN warning row reading
#       "SEPTEMBER COUPON CALENDAR IS NOT DOCKETED". Tightened to the EVENT
#       column, the warning row STILL matched, on its own "3Y/10Y/30Y
#       refunding" text.
# Three strikes on the same self-referential row is the tell: a commentary row
# and a real auction row are not separable by vocabulary. So this now feeds an
# "ℹ️ FYI, not a verdict" listing and NOTHING gated on it.
_CUSIP = re.compile(r"\b9128[0-9A-Z]{5,6}\b")
_TENOR = re.compile(r"\b(?:2|3|5|7|10|20|30|40)\s*[-]?\s*Y(?:R|EAR)?\b", re.IGNORECASE)
_AUCTION_WORD = re.compile(r"(?:AUCTION|NEW ISSUE|REOPEN|TIPS|CLUSTER|BILL|NOTE|BOND)", re.IGNORECASE)
_REFUNDING = re.compile(r"REFUNDING", re.IGNORECASE)


def _is_coupon_auction_row(event: str) -> bool:
    """Does this docket EVENT identify a scheduled coupon auction?"""
    if _CUSIP.search(event):
        return True
    if _REFUNDING.search(event):
        return True
    return bool(_TENOR.search(event) and _AUCTION_WORD.search(event))
_ISO = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:\.\.(\d{4}-\d{2}-\d{2}))?$")


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


# ---------------------------------------------------------------- pure helpers
# Extracted as pure functions so --selftest can exercise the PREDICATE, not
# just the plumbing. The v1 defect lived in the predicate and was untestable
# where it sat: `boot_recompute.gate_row_drift` was extracted for the same
# reason on 2026-08-21.

def feed_horizon(rows: list[dict]) -> dt.date | None:
    """Latest auctionDate the feed can see, across ALL security types.

    Bills are included DELIBERATELY: this measures how far the feed SEES,
    which is a property of the feed, not of BOND's instrument class. Using
    coupons only would report a horizon of `None` on exactly the days the
    coupon set is empty -- i.e. it would go blind precisely when it matters.
    """
    seen = []
    for r in rows:
        try:
            seen.append(dt.date.fromisoformat(str(r.get("auctionDate", ""))[:10]))
        except ValueError:
            continue
    return max(seen) if seen else None


def blind_span(today: dt.date, horizon: dt.date,
               fh: dt.date | None) -> tuple[dt.date, dt.date] | None:
    """The part of the requested window the feed cannot speak to."""
    if fh is None:
        return (today, horizon)
    if fh >= horizon:
        return None
    start = max(today, fh + dt.timedelta(days=1))
    return (start, horizon) if start <= horizon else None


def docketed_coupon_rows(docket_text: str, lo: dt.date, hi: dt.date) -> list[str]:
    """Docket rows dated inside [lo, hi] that look like coupon auctions.

    Handles the docket's own date vocabulary: bare ISO, `A..B` ranges, and
    non-dated tokens (`recurring-Wed`, `watch`) which are skipped -- a
    standing watch row is not evidence that a specific auction is docketed.
    """
    hits = []
    for line in docket_text.splitlines()[1:]:
        if not line.strip():
            continue
        cells = line.split("\t")
        m = _ISO.match(cells[0].strip())
        if not m:
            continue
        d0 = dt.date.fromisoformat(m.group(1))
        d1 = dt.date.fromisoformat(m.group(2)) if m.group(2) else d0
        if d1 < lo or d0 > hi:          # no overlap with the span
            continue
        # EVENT column only -- never the notes. A row that merely MENTIONS a
        # tenor in its commentary is not a scheduled auction, and scanning the
        # whole line let this desk's own "September is NOT docketed" warning
        # row count as coverage for September.
        event = cells[1] if len(cells) > 1 else ""
        if _is_coupon_auction_row(event):
            hits.append(f"{cells[0].strip()}  {event[:70]}")
    return hits


# ---------------------------------------------------------------------- report

def evaluate(rows: list[dict], docket: str, today: dt.date, days: int) -> tuple[int, list[str]]:
    """Returns (rc, lines). Pure: no I/O, so --selftest can drive it."""
    out: list[str] = []
    horizon = today + dt.timedelta(days=days)
    fh = feed_horizon(rows)
    span = blind_span(today, horizon, fh)

    upcoming = []
    for r in rows:
        if r.get("securityType") not in COUPON_TYPES:
            continue
        try:
            ad = dt.date.fromisoformat(str(r["auctionDate"])[:10])
        except (ValueError, KeyError):
            continue
        if today <= ad <= horizon:
            upcoming.append(r)
    upcoming.sort(key=lambda x: str(x["auctionDate"]))

    missing, present = [], []
    for r in upcoming:
        cusip = (r.get("cusip") or "").strip()
        # A row counts as docketed only if the CUSIP appears -- a bare date is
        # not enough, because a date can be docketed for the WRONG instrument
        # (the 8/18 JGB-vs-UST 20Y fusion is the worked example).
        (present if cusip and cusip in docket else missing).append(r)

    out.append(f"[docket_check] requested window {today} -> {horizon} ({days}d)")
    out.append(f"[docket_check] feed sees through {fh if fh else 'NOTHING'}"
               f"  |  coupon auctions in reference set: {len(upcoming)}"
               f"  |  docketed: {len(present)}  |  MISSING: {len(missing)}")

    for r in present:
        out.append(f"   ok   {str(r['auctionDate'])[:10]}  {r.get('securityTerm',''):16} "
                   f"{r.get('cusip','')}  tips={r.get('tips','')}")

    rc = 0

    if missing:
        rc = 1
        out.append("")
        out.append("[docket_check] 🔴 UNDOCKETED — add these to docket/CATALYSTS.tsv before closeout:")
        for r in missing:
            amt = r.get("offeringAmount")
            try:
                amt_s = f"${float(amt)/1e9:.0f}B" if amt else "size TBA"
            except (TypeError, ValueError):
                amt_s = "size TBA"
            out.append(f"   MISSING  {str(r['auctionDate'])[:10]}  {r.get('securityTerm',''):16} "
                       f"{r.get('cusip','')}  {amt_s}  tips={r.get('tips','')}  "
                       f"reopening={r.get('reopening','')}")
        out.append("")
        out.append("[docket_check] ⚠️ Record the INSTRUMENT, not just the date: a TIPS reopening and a "
                   "nominal of the same tenor have different buyer bases and different benchmarks.")

    # ---- the v2 leg: never certify a window the feed could not observe ----
    if span is None:
        out.append(f"[docket_check] ✅ coverage VERIFIED across the full requested window "
                   f"(feed reaches {fh} >= horizon {horizon}).")
    else:
        lo, hi = span
        blind_days = (hi - lo).days + 1
        docketed = docketed_coupon_rows(docket, lo, hi)
        out.append("")
        out.append(f"[docket_check] ⚠️ COVERAGE IS PARTIAL — VERIFIED ONLY THROUGH "
                   f"{fh if fh else '(nothing)'}.")
        out.append(f"   BLIND SPAN: {lo} -> {hi} ({blind_days}d of the {days}d window).")
        out.append("   Cause is STRUCTURAL, not a fetch problem: TA_WS/upcoming lists only ANNOUNCED")
        out.append("   auctions (~1wk ahead for coupons); the forward schedule is a QRA PDF outside")
        out.append("   TA_WS. No API path closes it. The gap is WIDEST for the LARGEST events.")
        out.append("   🔴 THIS TOOL CANNOT ADJUDICATE THAT SPAN — IT CAN ONLY DECLARE IT.")
        out.append("      Two drafts of this check tried to auto-clear the span by text-matching the")
        out.append("      docket. Both were wrong in the SAME direction, and the second was caught only")
        out.append("      by running it: the row it counted as September coverage was this desk's OWN")
        out.append("      warning row reading 'SEPTEMBER COUPON CALENDAR IS NOT DOCKETED'. A commentary")
        out.append("      row and a real auction row are not reliably distinguishable by vocabulary, so")
        out.append("      ANY auto-clear here is v1's disease again: a claim stronger than the measurement.")
        out.append("   ⇒ The span is reported UNVERIFIED, always. Verify it against the Treasury QRA /")
        out.append("      tentative auction schedule by hand; the owed action lives on the DOCKET as a")
        out.append("      dated row, not in this tool's exit code.")
        if docketed:
            out.append(f"   ℹ️ FYI — {len(docketed)} docket row(s) fall in the span and mention auction")
            out.append("      language. LISTED AS INFORMATION, EXPLICITLY NOT AS A VERDICT:")
            for h in docketed[:8]:
                out.append(f"        · {h}")
        else:
            out.append("   ℹ️ FYI — no docket row in the span mentions auction language.")

    if rc == 0:
        if span is None:
            out.append("[docket_check] rc=0 — every coupon auction the feed can see is docketed, "
                       "and the feed reached the full window.")
        else:
            out.append(f"[docket_check] rc=0 — NOTHING ACTIONABLE, which is NOT 'the window is covered'. "
                       f"Coverage is PROVEN only through {fh}; "
                       f"{(span[1]-span[0]).days + 1}d of the window remain UNVERIFIED by this tool.")
        out.append("[docket_check] ⚠️ Scope: this tool covers TreasuryDirect COUPON AUCTIONS only. "
                   "FOMC/ECB/CPI/MTS and every other non-auction catalyst are OUTSIDE its guarantee — "
                   "a clean auction check is NOT a clean calendar.")
    return rc, out


# ---------------------------------------------------------------------- selftest

def selftest() -> int:
    """Fixtures are REAL states this tool has been in, not invented ones."""
    # Both numbers in the success line are COMPUTED. This tool shipped
    # "18 assertions" while running 17 -- a self-reported count it never
    # computed, which is the exact defect class it exists to catch.
    _FIXTURES = len(set(re.findall(r"^    # (\d+)\.", inspect.getsource(selftest), re.M)))
    T = dt.date(2026, 8, 27)
    BILLS = [  # the exact 2026-08-27 payload that produced the degenerate pass
        {"auctionDate": "2026-08-31", "securityType": "Bill", "securityTerm": "13-Week", "cusip": "912797VA2"},
        {"auctionDate": "2026-08-31", "securityType": "Bill", "securityTerm": "26-Week", "cusip": "912797WD5"},
        {"auctionDate": "2026-09-01", "securityType": "Bill", "securityTerm": "52-Week", "cusip": "912797WA1"},
        {"auctionDate": "2026-09-01", "securityType": "Bill", "securityTerm": "6-Week",  "cusip": "912797UK1"},
    ]
    EMPTY_DOCKET = "date\tevent\n2026-09-05\tSome non-auction thing\tx\n"
    COVERED_DOCKET = ("date\tevent\n"
                      "2026-09-08\t**3Y/10Y/30Y SEPTEMBER REFUNDING**\tcheck\n")
    fails = []
    ran = []          # COUNTED, never carried -- this tool shipped "18 assertions"
                      # while running 17, which is the same uncomputed-count defect
                      # it exists to catch. A self-reported count must be computed.

    def check(name, got, want):
        ran.append(name)
        if got != want:
            fails.append(f"  ✗ {name}: got {got}, want {want}")

    # 1. THE REGRESSION THAT MATTERS: bills-only feed + nothing docketed in the
    #    blind span must NOT be rc=0. v1 returned 0 here.
    rc, lines = evaluate(BILLS, EMPTY_DOCKET, T, 21)
    check("bills-only feed must NEVER claim window coverage",
          any("covers every scheduled coupon auction in the window" in l for l in lines), False)
    check("must name the blind span", any("BLIND SPAN" in l for l in lines), True)
    check("must say what it actually verified",
          any("VERIFIED ONLY THROUGH" in l for l in lines), True)
    check("rc=0 must be qualified, not read as coverage",
          any("NOT 'the window is covered'" in l for l in lines), True)

    # 2. Same blind feed, but the desk HAS docketed the refunding -> quiet.
    #    This is the anti-alarm-fatigue leg: the tool must go silent once the
    #    operator has done the thing it asked for.
    rc, lines = evaluate(BILLS, COVERED_DOCKET, T, 21)
    check("bills-only + docketed span -> rc=0", rc, 0)
    check("a docketed span is still declared UNVERIFIED, not cleared",
          any("CANNOT ADJUDICATE" in l for l in lines), True)

    # 3. Undocketed coupon the feed CAN see -> rc=1 (v1 behaviour preserved).
    coupon = dict(auctionDate="2026-08-28", securityType="Note",
                  securityTerm="7-Year", cusip="91282CRJ2", offeringAmount="44000000000")
    rc, _ = evaluate(BILLS + [coupon], COVERED_DOCKET, T, 21)
    check("undocketed coupon -> rc=1", rc, 1)

    # 4. Same coupon, docketed by CUSIP -> not flagged by the diff leg.
    rc, _ = evaluate(BILLS + [coupon], COVERED_DOCKET + "2026-08-28\t7Y 91282CRJ2\tx\n", T, 21)
    check("docketed coupon -> rc=0", rc, 0)

    # 5. Feed reaching past the horizon -> no blind span at all.
    far = dict(auctionDate="2026-09-30", securityType="Bill", securityTerm="4-Week", cusip="912797ZZ9")
    check("no blind span when feed reaches past horizon",
          blind_span(T, T + dt.timedelta(days=21), feed_horizon(BILLS + [far])), None)

    # 6. Horizon measured across ALL types, not coupons only (else it goes
    #    blind on exactly the days the coupon set is empty).
    check("feed_horizon spans bills", feed_horizon(BILLS), dt.date(2026, 9, 1))

    # 7. Non-dated docket tokens must not count as coverage.
    check("watch/recurring rows are not coverage",
          docketed_coupon_rows("date\tevent\nwatch\t30Y auction watch\nrecurring-Wed\tFR2004\n",
                               dt.date(2026, 9, 1), dt.date(2026, 9, 30)), [])

    # 8. `A..B` range rows overlapping the span DO count.
    check("range rows count",
          len(docketed_coupon_rows("date\tevent\n2026-09-22..2026-09-24\t2Y/5Y/7Y month-end cluster\n",
                                   dt.date(2026, 9, 1), dt.date(2026, 9, 30))), 1)

    # 9. REGRESSION LOCK, found by this selftest on its own first run:
    #    a row carrying the bare word "auction" but NO tenor/CUSIP must NOT
    #    count as coverage. The first draft matched "non-auction" and silenced
    #    the alarm -- a false positive here is the 8/18 failure, because inside
    #    the blind span this predicate is the only thing standing.
    check("bare 'auction' with no tenor is NOT coverage",
          docketed_coupon_rows("date\tevent\n2026-09-05\tSome non-auction thing\n",
                               dt.date(2026, 9, 1), dt.date(2026, 9, 30)), [])

    # 10. REGRESSION LOCK #2, found by RUNNING v2 live rather than reading it.
    #     These four are the ACTUAL rows v2 counted as September coverage.
    #     None is a coupon auction; each merely mentions a tenor in its notes.
    #     The fourth is the sharpest: it is this desk's OWN warning row saying
    #     September is not docketed, read by the guard as proof that it was.
    NOT_AUCTIONS = (
        "date\tevent\tnotes\n"
        "2026-09-09\t**First stepped-up buyback op (sb0607)**\tF2 test; 10-20y and 20-30y buckets\n"
        "2026-09-16\t**SEPTEMBER FOMC — decision + SEP**\tresolver for the Fed-path arm; 30Y reaction\n"
        "2026-09-08\t**CANADIAN RETALIATORY TARIFFS TAKE EFFECT**\tT10YIE/T5YIFR vs the 10Y real\n"
        "2026-09-03\t**SEPTEMBER COUPON CALENDAR IS NOT DOCKETED**\towed: 3Y/10Y/30Y refunding, 20Y, TIPS\n"
    )
    check("non-auction rows mentioning a tenor are NOT counted",
          docketed_coupon_rows(NOT_AUCTIONS, dt.date(2026, 9, 2), dt.date(2026, 9, 17)), [])
    # ...and the load-bearing one: whatever that listing says, it is FYI and
    # gates nothing. The tool's verdict must be identical either way.
    check("the FYI listing gates NOTHING — verdict identical with and without it",
          evaluate(BILLS, NOT_AUCTIONS, T, 21)[0], evaluate(BILLS, EMPTY_DOCKET, T, 21)[0])

    # 11. And a REAL docketed refunding still counts, so this is not just strict.
    check("a genuine refunding row IS coverage",
          len(docketed_coupon_rows("date\tevent\n2026-09-08\t**3Y/10Y/30Y SEPTEMBER REFUNDING $125B**\n",
                                   dt.date(2026, 9, 2), dt.date(2026, 9, 17))), 1)
    check("a genuine CUSIP row IS coverage",
          len(docketed_coupon_rows("date\tevent\n2026-09-16\t**US 20Y NEW ISSUE 912810UX4**\n",
                                   dt.date(2026, 9, 2), dt.date(2026, 9, 17))), 1)

    if fails:
        print("[docket_check --selftest] 🔴 FAILED")
        print("\n".join(fails))
        return 1
    print(f"[docket_check --selftest] ✅ {len(ran)} assertions across {_FIXTURES} fixtures passed "
          f"(fixture 1 is the exact 2026-08-27 payload that produced the degenerate rc=0; "
          f"fixtures 9-10 lock two regressions found in v2 itself — one by the selftest, "
          f"one only by RUNNING it live).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=21,
                    help="look-ahead window in calendar days (default 21)")
    ap.add_argument("--selftest", action="store_true",
                    help="verify the checker itself against real prior states")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    try:
        rows = fetch_upcoming()
        docket = load_docket_text()
    except Exception as e:  # fail loud, never silently pass
        print(f"[docket_check] FETCH/READ FAILURE: {e}", file=sys.stderr)
        print("[docket_check] rc=2 -- this is NOT a pass. Re-run before closeout.",
              file=sys.stderr)
        return 2

    rc, lines = evaluate(rows, docket, dt.date.today(), args.days)
    stream = sys.stderr if rc else sys.stdout
    for l in lines:
        print(l, file=stream)
    return rc


if __name__ == "__main__":
    sys.exit(main())
