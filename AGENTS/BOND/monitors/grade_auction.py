#!/usr/bin/env python3
"""BOND — Treasury coupon auction grader.

WHY THIS EXISTS
---------------
Auction grades are done under time pressure minutes after a 1PM print, and
2026-08-18 demonstrated that this desk makes METHOD errors under exactly
those conditions: mixed counting conventions, per-year truncation, partial
refreshes, and benchmarks ported across tenors. Hand-deriving the same
computation a fifth time is the error surface.

Every rule below is one BOND learned the expensive way:

  * **% of COMPETITIVE ACCEPTED**, never of total accepted. Wire figures
    often use total (which includes noncompetitive + SOMA add-ons) and run
    lower; reconciling across denominators produces spurious divergence.
  * **Benchmarks are PER TENOR.** The 7Y's 56.42% indirect floor applied to
    a 10Y auction (floor 63.95%) is simply the wrong bar. That error was
    live in THESIS, TRADE and PROTOCOL until 2026-08-18.
  * **TIPS are a different instrument** with a different buyer base. A
    "30-Year" nominal and a "29-Year 6-Month" TIPS reopening are not
    comparable and are never pooled.
  * **NO TAILS.** A tail needs the when-issued yield at bid deadline and
    TreasuryDirect does not publish it. Retired 2026-07-28 as unscoreable
    from primaries; no gate may key on one.
  * **State the margin on every leg** (v1.1.4(e)) so a knife-edge leg and a
    13pp leg are never reported as the same verdict.
  * **Carry a RESIDUAL branch** (v1.1.4(d)). BND-13 landed 0.03pp from a
    print that would have fired no branch at all.
  * **Declare the aggregation.** Median and mean can disagree; both are
    printed, because a wire called the 8/13 30Y "below average" while it sat
    above its median.

USAGE
-----
    python3 monitors/grade_auction.py --cusip 912810UW6
    python3 monitors/grade_auction.py --cusip 912810UX4      # pre-print: reports the BARS
    python3 monitors/grade_auction.py --date 2026-08-13
    python3 monitors/grade_auction.py --cusip X --n 12

    rc 0 = graded (or bars reported pre-print)   rc 2 = fetch/lookup failure
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
import urllib.request

UA = {"User-Agent": "BOND-research/1.0 (williepowen@gmail.com)"}
AUCTIONED = ("https://www.treasurydirect.gov/TA_WS/securities/auctioned"
             "?format=json&dateFieldName=auctionDate&startDate={s}&endDate={e}")
UPCOMING = "https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json"
MIN_N_FOR_GATE = 6   # below this, a composition gate is not supportable


def _get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        if r.status != 200:
            raise RuntimeError(f"HTTP {r.status} from {url[:70]}")
        return json.load(r)


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


CORPUS = __import__("pathlib").Path(__file__).resolve().parent.parent / "data" / "auction_history_v2_prome-spawned.csv"
FRN_CACHE = CORPUS.parent / "frn_cusips_ta_ws.json"
FRN_SEARCH = "https://www.treasurydirect.gov/TA_WS/securities/search?type=FRN&format=json"


def frn_cusips():
    """CUSIPs of every 2-Year FLOATING RATE NOTE TreasuryDirect has auctioned.

    ⚠️ 2026-09-02: FRNs carry securityType "Note", originalSecurityTerm "2-Year" and
    securityTerm "2-Year" (new) / "1-Year 11-Month" (reopening) — i.e. they are
    INDISTINGUISHABLE from nominal 2Y notes on every field this tool keyed on, and the
    corpus has no floating flag at all. Every 2Y bar this desk published through
    2026-08-27 (indirect MIN 50.91, dealer MAX 49.09, I' 55.75) was set by FRN prints
    (the 3/25 print is a 2Y FRN reopening: indirect 50.91 / dealer 49.09). FRN buyer
    composition is structurally different (dealer 27-62%, directs ~0), so pooling them
    measures a SUPERSET of the instrument the composition test is about
    ([[finding_instrument_measures_a_superset_of_the_thesis_subject]]).
    Live pull from TA_WS `type=FRN`; local cache is the fallback and is refreshed on
    every successful pull. A failed pull WITH no cache raises — a silent empty set would
    re-admit the contamination and report clean.
    """
    try:
        rows = _get(FRN_SEARCH)
        cus = sorted({r["cusip"] for r in rows if r.get("cusip")})
        if cus:
            FRN_CACHE.write_text(json.dumps(cus))
            return set(cus)
    except Exception as e:  # noqa: BLE001
        print(f"[grade] ⚠️ FRN list pull failed ({e}); using cached {FRN_CACHE.name}", file=sys.stderr)
    if FRN_CACHE.exists():
        return set(json.loads(FRN_CACHE.read_text()))
    raise RuntimeError("no FRN CUSIP list (live pull failed and no cache) — refusing to build 2Y benchmarks over a pool that may contain FRNs")


TERM_MAP = {"2Y": "2-Year", "3Y": "3-Year", "5Y": "5-Year", "7Y": "7-Year",
            "10Y": "10-Year", "20Y": "20-Year", "30Y": "30-Year"}


def _from_ta_ws():
    """TA_WS `auctioned` — used ONLY for recent prints, never for history.

    ⚠️ 2026-08-18: this endpoint's date filter is INOPERATIVE. startDate/endDate
    are ignored; it returns the most recent 250 rows for ANY window (verified:
    requesting 2024 returns 2025-02-24 -> 2026-08-18, identical to requesting
    2022-2030). Building benchmarks off it silently truncates rare instruments
    -- 30Y TIPS showed n=2 here against n=7 in the local corpus -- and the
    cutoff SLIDES as new auctions land, so the same query gives different
    history on different days. Same defect class as the FR2004 stale series
    break: a query artifact read as a property of the data.
    """
    rows, out = _get(AUCTIONED.format(s="2022-06-01", e="2030-01-01")), []
    if len(rows) >= 250:
        print(f"[grade] ⚠️ TA_WS returned {len(rows)} rows = AT CAP. Its date filter is "
              f"inoperative; this feed is used for RECENT PRINTS ONLY, never for benchmarks.",
              file=sys.stderr)
    for r in rows:
        if r.get("securityType") not in ("Note", "Bond"):
            continue
        if r.get("floatingRate") == "Yes":   # 2Y FRN — not a nominal 2Y (2026-09-02)
            continue
        ind, dir_, pd_ = (_f(r.get("indirectBidderAccepted")),
                          _f(r.get("directBidderAccepted")),
                          _f(r.get("primaryDealerAccepted")))
        if None in (ind, dir_, pd_):
            continue
        comp = ind + dir_ + pd_
        if comp <= 0:
            continue
        out.append({"date": r["auctionDate"][:10], "cusip": r.get("cusip", ""),
                    "term": r.get("originalSecurityTerm") or r.get("securityTerm"),
                    "secterm": r.get("securityTerm"), "tips": r.get("tips") == "Yes",
                    "reopening": r.get("reopening") == "Yes",
                    "btc": _f(r.get("bidToCoverRatio")), "hy": r.get("highYield"),
                    "offering": _f(r.get("offeringAmount")) or 0.0, "comp": comp,
                    "ind": 100 * ind / comp, "dir": 100 * dir_ / comp,
                    "dlr": 100 * pd_ / comp, "src": "TA_WS"})
    return out


def _from_corpus():
    """Local corpus = the BENCHMARK source. Real history back to 2023-01."""
    import csv as _csv
    if not CORPUS.exists():
        print(f"[grade] ⚠️ corpus missing at {CORPUS}; benchmarks will be TRUNCATED.", file=sys.stderr)
        return []
    out = []
    frn = frn_cusips()
    dropped = 0
    with open(CORPUS, encoding="utf-8") as fh:
        for r in _csv.DictReader(fh):
            if r.get("cusip", "") in frn:   # 2Y FRN rows filed under tenor 2Y (2026-09-02)
                dropped += 1
                continue
            comp = _f(r.get("total_competitive_accepted"))
            pd_ = _f(r.get("primary_dealer_accepted"))
            dir_ = _f(r.get("direct_bidder_accepted"))
            ind = _f(r.get("indirect_bidder_accepted"))
            btc = _f(r.get("bid_to_cover_ratio"))
            if not comp or comp <= 0 or None in (pd_, dir_, ind) or btc is None:
                continue
            out.append({"date": r["auction_date"][:10], "cusip": r.get("cusip", ""),
                        "term": TERM_MAP.get(r.get("tenor"), r.get("tenor")),
                        "secterm": r.get("tenor"),
                        "tips": str(r.get("is_tips")).strip().lower() == "true",
                        "reopening": str(r.get("is_reopening")).strip().lower() == "true",
                        "btc": btc, "hy": r.get("high_yield"),
                        "offering": _f(r.get("offering_amt")) or 0.0, "comp": comp,
                        "ind": 100 * ind / comp, "dir": 100 * dir_ / comp,
                        "dlr": 100 * pd_ / comp, "src": "corpus"})
    if dropped:
        print(f"[grade] corpus: {dropped} FRN row(s) EXCLUDED from the 2Y pool (floating-rate notes are not nominal 2Y)", file=sys.stderr)
    return out


def load(start=None, end=None):
    """Benchmarks from the LOCAL CORPUS; recent prints overlaid from TA_WS."""
    corpus = _from_corpus()
    seen = {(x["cusip"], x["date"]) for x in corpus}
    recent = [x for x in _from_ta_ws() if (x["cusip"], x["date"]) not in seen]
    if corpus:
        newest = max(x["date"] for x in corpus)
        added = [x for x in recent if x["date"] > newest]
        print(f"[grade] corpus: {len(corpus)} rows through {newest}"
              f" | +{len(added)} newer print(s) overlaid from TA_WS")
    out = corpus + recent
    out.sort(key=lambda x: x["date"])
    return out


def bench(recs, term, tips, before, n):
    """Trailing-n benchmark: SAME tenor, SAME tips flag, STRICTLY prior."""
    h = [x for x in recs if x["term"] == term and x["tips"] == tips
         and x["date"] < before and x["btc"] is not None][-n:]
    if not h:
        return None
    def agg(k):
        v = [x[k] for x in h]
        return {"median": st.median(v), "mean": st.mean(v), "min": min(v), "max": max(v)}
    return {"n": len(h), "from": h[0]["date"], "to": h[-1]["date"],
            "btc": agg("btc"), "ind": agg("ind"), "dlr": agg("dlr")}


def show_bars(b, label):
    print(f"\n  BENCHMARK — {label}")
    print(f"    method : trailing-{b['n']} SAME-TENOR SAME-TIPS auctions, strictly prior,")
    print(f"             % of COMPETITIVE ACCEPTED (PD+direct+indirect)")
    print(f"    window : {b['from']} -> {b['to']}   n={b['n']}")
    for k, nm in (("btc", "BTC"), ("ind", "indirect%"), ("dlr", "dealer%")):
        a = b[k]
        print(f"    {nm:10} median {a['median']:7.2f} | mean {a['mean']:7.2f} "
              f"| min {a['min']:7.2f} | max {a['max']:7.2f}")
    print(f"\n    ⇒ COMPOSITION-FAILURE test : indirect < {b['ind']['min']:.2f}%  AND  dealer > {b['dlr']['max']:.2f}%")
    print(f"    ⇒ COVER-MARKER test        : BTC < {b['btc']['min']:.2f} with composition intact")
    if b["n"] < MIN_N_FOR_GATE:
        print(f"    🔴 n={b['n']} < {MIN_N_FOR_GATE}: THIN BASE — this cannot support a composition gate.")
        print(f"       Report as a LEVEL read against its own thin base rate; do NOT set a gate.")
    if b["ind"]["min"] == b["ind"]["min"] and b["dlr"]["max"] == b["dlr"]["max"]:
        pass
    return


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cusip"); ap.add_argument("--date")
    ap.add_argument("--n", type=int, default=12)
    a = ap.parse_args()
    if not (a.cusip or a.date):
        ap.error("need --cusip or --date")

    try:
        recs = load()
    except Exception as e:
        print(f"[grade] FETCH FAILURE: {e}", file=sys.stderr)
        return 2

    hit = [x for x in recs if (x["cusip"] == a.cusip if a.cusip else x["date"] == a.date)]

    # ⚠️ REOPENING TRAP (found by testing, 2026-08-18): a reopened CUSIP appears in
    # BOTH feeds -- the ORIGINAL issue in `auctioned` and the pending reopening in
    # `upcoming`. Taking the auctioned record would silently grade a MONTHS-OLD
    # auction as if it were the pending one. Tested on 912810US5: without this
    # guard the grader returned the 2026-02-19 original for a 2026-08-20 reopening.
    # If the CUSIP has a PENDING auction, the pre-print path wins.
    if a.cusip and hit:
        try:
            pending = [r for r in _get(UPCOMING) if r.get("cusip") == a.cusip]
        except Exception:
            pending = []
        if pending:
            print(f"[grade] ⚠️ {a.cusip} is a REOPENING with a PENDING auction "
                  f"({pending[0]['auctionDate'][:10]}). The auctioned record dated "
                  f"{hit[-1]['date']} is the ORIGINAL ISSUE, not the pending print — "
                  f"reporting PRE-PRINT bars instead of grading stale results.")
            hit = []

    if not hit:
        # Pre-print: report the bars so the gate is frozen BEFORE the result.
        try:
            up = [r for r in _get(UPCOMING) if r.get("cusip") == a.cusip]
        except Exception as e:
            print(f"[grade] FETCH FAILURE: {e}", file=sys.stderr)
            return 2
        if not up:
            print(f"[grade] no auctioned OR upcoming record for {a.cusip or a.date}", file=sys.stderr)
            return 2
        r = up[0]
        term = r.get("originalSecurityTerm") or r.get("securityTerm")
        tips = r.get("tips") == "Yes"
        amt = _f(r.get("offeringAmount"))
        print("=" * 78)
        print(f"PRE-PRINT — no results published yet. Reporting the BARS.")
        print(f"  {r.get('securityTerm')}  {r.get('cusip')}  "
              f"{'$%.0fB' % (amt/1e9) if amt else 'size TBA'}  "
              f"tips={r.get('tips')}  reopening={r.get('reopening')}  auction {r['auctionDate'][:10]}")
        if tips:
            print("  ⚠️ TIPS — different buyer base. Never benchmarked against nominals.")
        b = bench(recs, term, tips, r["auctionDate"][:10], a.n)
        if not b:
            print("  🔴 NO HISTORY for this tenor/tips combination — no bars derivable.")
            return 0
        show_bars(b, f"{term}{' TIPS' if tips else ''}")
        print("\n  ⇒ Freeze these bars NOW, before the print. That is the whole point.")
        print("=" * 78)
        return 0

    r = hit[-1]
    b = bench(recs, r["term"], r["tips"], r["date"], a.n)
    print("=" * 78)
    print(f"GRADE — {r['date']}  {r['secterm']}  {r['cusip']}  "
          f"${r['offering']/1e9:.0f}B  tips={r['tips']}  reopening={r['reopening']}")
    print(f"  BTC {r['btc']:.2f} | indirect {r['ind']:.2f}% | direct {r['dir']:.2f}% "
          f"| dealer {r['dlr']:.2f}% | high yield {r['hy']}")
    print(f"  (percentages are of COMPETITIVE ACCEPTED = ${r['comp']/1e9:.3f}B)")
    if r["tips"]:
        print("  ⚠️ TIPS — benchmarked only against prior TIPS of the same tenor.")
    if not b:
        print("  🔴 NO BENCHMARK HISTORY — cannot grade.")
        return 0
    show_bars(b, f"{r['term']}{' TIPS' if r['tips'] else ''}")

    print("\n  LEG MARGINS (v1.1.4(e) — every leg, always):")
    legs = {}
    for k, nm in (("btc", "BTC"), ("ind", "indirect%"), ("dlr", "dealer%")):
        v, a_ = r[k], b[k]
        legs[k] = {"v": v, "vs_med": v - a_["median"], "vs_mean": v - a_["mean"]}
        print(f"    {nm:10} {v:7.2f}   vs median {v-a_['median']:+7.2f}   vs mean {v-a_['mean']:+7.2f}"
              f"   {'⚠️ median/mean DISAGREE on sign' if (v>a_['median'])!=(v>a_['mean']) else ''}")

    ind_fail = r["ind"] < b["ind"]["min"]
    dlr_fail = r["dlr"] > b["dlr"]["max"]
    cover = r["btc"] < b["btc"]["min"]
    print("\n  VERDICT")
    print(f"    indirect below trailing-{b['n']} MIN ? {'YES' if ind_fail else 'NO'}  "
          f"({r['ind']:.2f} vs {b['ind']['min']:.2f}, margin {r['ind']-b['ind']['min']:+.2f}pp)")
    print(f"    dealer  above trailing-{b['n']} MAX ? {'YES' if dlr_fail else 'NO'}  "
          f"({r['dlr']:.2f} vs {b['dlr']['max']:.2f}, margin {r['dlr']-b['dlr']['max']:+.2f}pp)")
    print(f"    BTC     below trailing-{b['n']} MIN ? {'YES' if cover else 'NO'}  "
          f"({r['btc']:.2f} vs {b['btc']['min']:.2f}, margin {r['btc']-b['btc']['min']:+.2f})")

    if b["n"] < MIN_N_FOR_GATE:
        print(f"\n  ⚪ NO GATE VERDICT — n={b['n']} is too thin to support one. Level read only.")
    elif ind_fail and dlr_fail:
        print("\n  🔴 COMPOSITION FAILURE — the demand-hole test. Foreign stepping away WHILE dealers warehouse.")
        print("     Signal LIQUID, ZHAO, PROME SAME-DAY. This is the thesis-kill leg.")
    elif cover:
        print("\n  🟠 COVER MARKER — thin cover; composition did NOT fail.")
        print("     ⚠️ SAY EXPLICITLY THAT THE MECHANISM DID NOT FAIL. A thin cover is a PRICE")
        print("     concession; only a composition failure is a mechanism failure.")
        if ind_fail or dlr_fail:
            leg = "indirect" if ind_fail else "dealer"
            m = (r["ind"] - b["ind"]["min"]) if ind_fail else (r["dlr"] - b["dlr"]["max"])
            print(f"     ⚠️ BUT ONE COMPOSITION LEG IS ALSO BREACHED: {leg} by {m:+.2f}pp.")
            print("        Do NOT report this as 'composition held' unqualified — the failure test")
            print("        needs BOTH legs, and it is not met, but one leg IS outside its bar.")
            print("        (Added 2026-08-18: BOND's own 7/27 5Y grade said 'composition HELD' while")
            print("         indirect sat 0.18pp below its trailing-12 min. True on the cross-tenor")
            print("         same-day comparison, overstated on the same-tenor trailing-12 one.)")
    elif ind_fail or dlr_fail:
        print("\n  🟡 ONE COMPOSITION LEG BREACHED, not both — does NOT meet the failure test.")
        print("     RESIDUAL branch (v1.1.4(d)): report the breached leg with its margin; fires no gate.")
    else:
        print("\n  🟢 CLEAN — no cover marker, no composition failure, both legs inside their bars.")
    print("\n  ⛔ NO TAIL IS COMPUTED OR REPORTED. TreasuryDirect publishes no when-issued yield;")
    print("     a tail is unscoreable from primaries and may never fire a gate (retired 2026-07-28).")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
