#!/usr/bin/env python3
"""
fr2004_join.py — WQ-157 leg ② / DOCKET L271: the PAIRING INSTRUMENT for the I' kill leg.

WHAT THIS ANSWERS
-----------------
The 2026-09-04 Will ruling made the composition kill PAIRED from 2026-09-11 forward:
an I' fire alone no longer kills the thesis; it must be paired with a dealer /
funding confirmation. Nobody had ever measured what pairing DOES. This builds the
join and base-rates the conjunction.

THE QUESTION THAT MATTERS, stated before the numbers so it cannot be reverse-fitted:
    Does pairing actually FILTER anything?
    If P(dealer leg | I' fired) == P(dealer leg | I' did not fire), then the pairing
    adds ceremony and no information, and the "paired" kill is the standalone kill
    wearing a second condition. That is a REPORTABLE finding, not a bug.

JOIN CONVENTION — the load-bearing design choice, declared
----------------------------------------------------------
Dealer warehousing from an auction is a POST-auction effect, measured as a DELTA
ACROSS the auction, not a level beside it. FR 2004A is TRADE-DATE: an allotment is
in the dealer's position FROM THE AWARD DATE (FR 2004 Instructions eff. Jan 2022,
GEN-6 §II.C "Include allotments that are awarded on a report date in that day's
positions"; A-1 trade-date accounting). So the one-week window that CONTAINS the
award is:

    PRE  = the last FR2004 as-of STRICTLY BEFORE the auction date
    POST = the first FR2004 as-of ON OR AFTER the auction date
    delta = POST - PRE      (in $B, per bucket and for the long-end TOTAL)

⚠️ CHANGED 2026-09-25 (WQ-290, Will "Approve WQ-290 with your rec", 02:16 ET).
Until then PRE was ON-OR-BEFORE and POST STRICTLY AFTER, which put a WEDNESDAY
auction's award inside PRE (75 of 228 joined rows) and measured a delta that
excluded it. The as-shipped figures stay in the KB as history (KB-BND-306 /
KB-BND-332); analysis/2026-09-25_fr2004_join_window_sensitivity.py reproduces them.
⚠️ SCOPE (not changed here): LONG_END = 7Y+ buckets; a 2Y/3Y/5Y/7Y award books in a
shorter bucket (A-5) and is NOT in this total — which bucket counts is WQ-157 leg ②.

A level-beside-it join would measure the stock the dealer held BEFORE the auction
it is supposed to be grading, which is the wrong quantity. Both are computed; the
DELTA is the instrument and the level is reported as context.

CEILING
-------
FR2004's long-end buckets (11-21Y, >21Y) exist only from the 2022-01-05 series
break. Pooled SBN2022 (130) + SBN2024 (114) = n=244 weekly prints, VERIFIED by
direct count at the primary 2026-09-14. NOT a decade of dealer data.

COMPARABILITY (WQ-157's open premise)
-------------------------------------
Pooling across the SBN2022/SBN2024 boundary is DEFENSIBLE but INFERRED, never
VERIFIED: there are ZERO overlapping as-of dates, so no direct identity test is
possible from the API. The boundary w/w moves for the two buckets WQ-157 depends
on rank at the 0.4th and 0.8th percentile of their own |w/w| distributions —
quieter than 99%+ of weeks, i.e. no level break. ⚠️ Level continuity is NECESSARY,
NOT SUFFICIENT: a redefinition preserving levels (same maturity bounds, changed
panel or instrument coverage) passes this test unseen. NAMED UNCHECKED PRIMARY:
the NY Fed's own FR2004 form-revision documentation, not consulted.
  → analysis/2026-09-14_FR2004_SBN2022-SBN2024_comparability-probe.md

USAGE
    ../../.venv/bin/python3 monitors/fr2004_join.py            # full join + base rates
    ../../.venv/bin/python3 monitors/fr2004_join.py --selftest
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import csv
import json
import statistics as st
import sys
import time
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])

import fr2004_fetch as FR  # noqa: E402
import grade_auction as GA  # noqa: E402

API = FR.API
UA = FR.UA
BREAK_START = dt.date(2022, 1, 5)   # long-end buckets do not exist before this
TRAIL_N = 12                        # same trailing-12 the live bars use


# ---------------------------------------------------------------- FR2004 side
def all_breaks():
    """Every series break, oldest first. Never hardcoded (KB-BND-234's lesson)."""
    bs = FR._get(f"{API}/list/seriesbreaks.json")["pd"]["seriesbreaks"]
    out = [(b["seriesbreak"], dt.date.fromisoformat(b["startdate"]),
            dt.date.fromisoformat(b["enddate"])) for b in bs]
    out.sort(key=lambda x: x[1])
    return out


def fr2004_pooled():
    """Pool every break that overlaps the long-end-bucket era. Returns
    {asof_date: {bucket: $B, ..., 'LONG_END': $B}} plus a per-break row count."""
    series = {}
    counts = {}
    for sb, s, e in all_breaks():
        if e < BREAK_START:
            continue
        per = {}
        for keyid, label in FR.BUCKETS:
            try:
                per[label] = FR.fetch(keyid, sb)
            except SystemExit:
                per[label] = {}
        dates = set()
        for d in per.values():
            dates |= set(d)
        n = 0
        for ds in sorted(dates):
            d = dt.date.fromisoformat(ds)
            if d < BREAK_START:
                continue
            row = {lab: per[lab].get(ds) for _, lab in FR.BUCKETS}
            if any(v is None for v in row.values()):
                continue
            row["LONG_END"] = row["11-21Y"] + row[">21Y"] + row["7-11Y"]
            row["_break"] = sb
            series[d] = row
            n += 1
        counts[sb] = n
    return series, counts


# ---------------------------------------------------------------- auction side
def auctions_with_iprime():
    """Every NOMINAL coupon auction from BREAK_START, with its own trailing-12 I'
    bar computed by grade_auction.bench — the SAME code that grades live prints,
    so the base rate and the live gate can never drift apart."""
    recs = GA.load()
    out = []
    for r in recs:
        d = dt.date.fromisoformat(r["date"])
        if d < BREAK_START or r["tips"] or r["ind"] is None:
            continue
        b = GA.bench(recs, r["term"], r["tips"], r["date"], TRAIL_N)
        if not b or b["n"] < TRAIL_N or b.get("ind_p15") is None:
            continue
        out.append({
            "date": d, "cusip": r["cusip"], "term": r["term"],
            "ind": r["ind"], "dlr": r["dlr"], "btc": r["btc"],
            "bar": b["ind_p15"], "dlr_max": b["dlr"]["max"], "ind_min": b["ind"]["min"],
            "fired": r["ind"] < b["ind_p15"],                      # I' STRICT
            "old_fired": (r["ind"] < b["ind"]["min"] and r["dlr"] > b["dlr"]["max"]),
        })
    out.sort(key=lambda x: x["date"])
    return out


# ---------------------------------------------------------------- the join
def join(aucs, fr):
    asofs = sorted(fr)
    for a in aucs:
        pre = [d for d in asofs if d < a["date"]]     # trade-date window (WQ-290)
        post = [d for d in asofs if d >= a["date"]]
        a["pre"] = pre[-1] if pre else None
        a["post"] = post[0] if post else None
        if a["pre"] is None or a["post"] is None:
            a["d_long"] = a["d_1121"] = a["d_21"] = None
            continue
        p, q = fr[a["pre"]], fr[a["post"]]
        a["d_long"] = q["LONG_END"] - p["LONG_END"]
        a["d_1121"] = q["11-21Y"] - p["11-21Y"]
        a["d_21"] = q[">21Y"] - p["21Y"] if "21Y" in q else q[">21Y"] - p[">21Y"]
        a["lvl_long_pre"] = p["LONG_END"]
    return [a for a in aucs if a.get("d_long") is not None]


def rate(num, den):
    return float("nan") if den == 0 else 100.0 * num / den


def base_rates(j, label, leg):
    """leg(a) -> bool. Prints the 2x2 and the separation that decides whether
    pairing filters anything."""
    fired = [a for a in j if a["fired"]]
    notf = [a for a in j if not a["fired"]]
    bf = sum(1 for a in fired if leg(a))
    bn = sum(1 for a in notf if leg(a))
    p_f = rate(bf, len(fired))
    p_n = rate(bn, len(notf))
    print(f"\n  ── PAIRING LEG: {label}")
    print(f"     P(leg | I' FIRED)     = {bf}/{len(fired)} = {p_f:.1f}%")
    print(f"     P(leg | I' did NOT)   = {bn}/{len(notf)} = {p_n:.1f}%")
    sep = p_f - p_n
    print(f"     SEPARATION            = {sep:+.1f}pp", end="  ")
    if abs(sep) < 5:
        print("⚠️ NO MEANINGFUL SEPARATION — this leg adds ceremony, not information")
    elif sep > 0:
        print("→ leg is MORE likely after an I' fire")
    else:
        print("🔴 leg is LESS likely after an I' fire — pairing INVERTS")
    paired = sum(1 for a in j if a["fired"] and leg(a))
    print(f"     PAIRED KILL would have fired {paired}/{len(j)} auctions"
          f" = {rate(paired, len(j)):.1f}%   (I' standalone: {len(fired)}/{len(j)}"
          f" = {rate(len(fired), len(j)):.1f}%)")
    return {"sep": sep, "paired": paired, "fired": len(fired), "n": len(j)}



# ------------------------------------------------- significance + does it PREDICT
def two_prop_z(k1, n1, k2, n2):
    """Two-proportion z. Returns (z, approx two-sided p). No scipy dependency."""
    import math
    if min(n1, n2) == 0:
        return float("nan"), float("nan")
    p1, p2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return float("nan"), float("nan")
    z = (p1 - p2) / se
    pv = math.erfc(abs(z) / math.sqrt(2))
    return z, pv


def dgs30_series():
    u = ("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30"
         f"&cosd=2021-12-01&_cb={int(time.time())}")
    rows = list(csv.reader(io.StringIO(
        urllib.request.urlopen(u, timeout=90).read().decode())))[1:]
    return [(r[0], float(r[1])) for r in rows if r[1] not in (".", "")]


def forward_test(j, leg, leg_label):
    """THE question a kill criterion must answer: does firing PRECEDE anything?

    A composition test that fires and is followed by yields FALLING is not
    detecting a demand hole -- it is detecting a cheap print that got bought.
    This desk has carried that warning since 2026-09-02 (MEMORY: 'every
    indirect-keyed composition failure is followed by TLT UP at the median').
    """
    s = dgs30_series()
    idx = {d: i for i, (d, _) in enumerate(s)}
    def fwd(datestr, k):
        i = idx.get(datestr)
        if i is None or i + k >= len(s):
            return None
        return 100.0 * (s[i + k][1] - s[i][1])   # bp
    groups = {"I' FIRED, leg TRUE (PAIRED)": [], "I' FIRED, leg FALSE": [],
              "no I' fire": []}
    for a in j:
        ds = a["date"].isoformat()
        d5, d20 = fwd(ds, 5), fwd(ds, 20)
        if d5 is None or d20 is None:
            continue
        key = ("I' FIRED, leg TRUE (PAIRED)" if (a["fired"] and leg(a))
               else "I' FIRED, leg FALSE" if a["fired"] else "no I' fire")
        groups[key].append((d5, d20))
    print(f"\n  ── FORWARD 30Y YIELD CHANGE AFTER THE AUCTION  (leg = {leg_label})")
    print("     A demand-hole signal should be followed by yields RISING (+bp).")
    print(f"     {'group':<30} {'n':>4} {'median +5d':>12} {'median +20d':>13}")
    for k, v in groups.items():
        if not v:
            continue
        print(f"     {k:<30} {len(v):>4} {st.median(x[0] for x in v):>+11.1f}bp"
              f" {st.median(x[1] for x in v):>+12.1f}bp")
    return groups


def selftest():
    ok = 0; bad = []
    def chk(name, cond):
        nonlocal ok
        if cond: ok += 1
        else: bad.append(name)
    # rate()
    chk("rate zero-den is nan", rate(1, 0) != rate(1, 0))
    chk("rate basic", abs(rate(1, 4) - 25.0) < 1e-9)
    # join convention (WQ-290, trade-date): PRE strictly before, POST on-or-after
    fr = {dt.date(2025, 12, 31): {"7-11Y": 1.0, "11-21Y": 1.0, ">21Y": 3.0, "LONG_END": 5.0},
          dt.date(2026, 1, 7): {"7-11Y": 1.0, "11-21Y": 2.0, ">21Y": 3.0, "LONG_END": 6.0},
          dt.date(2026, 1, 14): {"7-11Y": 1.0, "11-21Y": 4.0, ">21Y": 3.0, "LONG_END": 8.0}}
    def auc(d, c):
        return {"date": d, "fired": True, "ind": 1, "dlr": 1, "btc": 1, "bar": 1,
                "dlr_max": 1, "ind_min": 1, "cusip": c, "term": "10-Year",
                "old_fired": False}
    # WEDNESDAY auction (1/7 = an as-of date): the award is IN the 1/7 print, so the
    # window is 12/31 -> 1/7. The pre-WQ-290 join returned 1/7 -> 1/14 here.
    out = join([auc(dt.date(2026, 1, 7), "W")], fr)
    chk("join produced a row", len(out) == 1)
    chk("WED: PRE is strictly before", out[0]["pre"] == dt.date(2025, 12, 31))
    chk("WED: POST is the award-day as-of", out[0]["post"] == dt.date(2026, 1, 7))
    chk("delta is POST-PRE", abs(out[0]["d_long"] - 1.0) < 1e-9)
    chk("bucket delta", abs(out[0]["d_1121"] - 1.0) < 1e-9)
    # TUESDAY auction (1/13): unchanged by WQ-290 — window 1/7 -> 1/14
    out_t = join([auc(dt.date(2026, 1, 13), "T")], fr)
    chk("TUE: PRE", out_t and out_t[0]["pre"] == dt.date(2026, 1, 7))
    chk("TUE: POST", out_t and out_t[0]["post"] == dt.date(2026, 1, 14))
    # an auction with no POST print must DROP, never impute
    out2 = join([{"date": dt.date(2026, 1, 20), "fired": True, "ind": 1, "dlr": 1,
                  "btc": 1, "bar": 1, "dlr_max": 1, "ind_min": 1, "cusip": "Y",
                  "term": "10-Year", "old_fired": False}], fr)
    chk("no POST print ⇒ row DROPPED not imputed", out2 == [])
    # separation maths
    j = [{"fired": True, "d_long": 1.0}, {"fired": True, "d_long": -1.0},
         {"fired": False, "d_long": 1.0}, {"fired": False, "d_long": -1.0}]
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        r = base_rates(j, "t", lambda a: a["d_long"] > 0)
    chk("zero separation detected", abs(r["sep"]) < 1e-9)
    chk("paired count", r["paired"] == 1)
    chk("BREAK_START is the bucket epoch", BREAK_START == dt.date(2022, 1, 5))
    chk("trailing n matches the live bars", TRAIL_N == 12)
    print(f"[selftest] {ok} passed, {len(bad)} failed")
    for b in bad:
        print("   FAIL:", b)
    return 0 if not bad else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    print("=" * 78)
    print("  FR2004 × AUCTION JOIN — WQ-157 leg ② / DOCKET L271")
    print("  the PAIRING INSTRUMENT for the I' kill leg")
    print("=" * 78)

    fr, counts = fr2004_pooled()
    tot = sum(counts.values())
    print(f"\n  FR2004 weekly prints, pooled across breaks: n={tot}")
    for sb, n in counts.items():
        print(f"     {sb}: {n}")
    print(f"     span {min(fr)} → {max(fr)}")
    print(f"     CEILING CHECK: WQ-157 stated 243; direct count gives {tot}.")

    aucs = auctions_with_iprime()
    print(f"\n  Nominal coupon auctions from {BREAK_START} with a full trailing-{TRAIL_N}"
          f" bar: n={len(aucs)}")
    j = join(aucs, fr)
    dropped = len(aucs) - len(j)
    print(f"  Joined (both a PRE and a POST FR2004 print exist): n={len(j)}"
          f"   [{dropped} dropped — no POST print yet, NEVER imputed]")

    fired = [a for a in j if a["fired"]]
    print(f"\n  I' STANDALONE base rate: {len(fired)}/{len(j)} = "
          f"{rate(len(fired), len(j)):.1f}% of auctions")
    oldf = [a for a in j if a["old_fired"]]
    print(f"  OLD conjunctive base rate: {len(oldf)}/{len(j)} = "
          f"{rate(len(oldf), len(j)):.1f}%")

    print("\n" + "-" * 78)
    print("  DOES PAIRING FILTER ANYTHING?  (the question, asked of each candidate leg)")
    print("-" * 78)
    res = {}
    res["long_build"] = base_rates(
        j, "long-end TOTAL BUILT across the auction (Δ > 0)", lambda a: a["d_long"] > 0)
    res["long_build_1b"] = base_rates(
        j, "long-end TOTAL built > $1B", lambda a: a["d_long"] > 1.0)
    res["b1121"] = base_rates(
        j, "11-21Y bucket BUILT across the auction", lambda a: a["d_1121"] > 0)
    res["b21"] = base_rates(
        j, ">21Y bucket BUILT across the auction", lambda a: a["d_21"] > 0)

    # significance of the best leg's separation
    print("\n" + "-" * 78)
    print("  IS THE SEPARATION REAL?  (two-proportion z, no scipy)")
    print("-" * 78)
    for name, leg, lab in [("long_build_1b", lambda a: a["d_long"] > 1.0,
                            "long-end TOTAL built > $1B")]:
        f = [a for a in j if a["fired"]]; nf = [a for a in j if not a["fired"]]
        k1 = sum(1 for a in f if leg(a)); k2 = sum(1 for a in nf if leg(a))
        z, pv = two_prop_z(k1, len(f), k2, len(nf))
        print(f"  {lab}: z={z:+.2f}  two-sided p={pv:.3f}"
              f"   {'NOT significant at 0.05' if pv > 0.05 else 'significant at 0.05'}")
        forward_test(j, leg, lab)

    print("\n" + "=" * 78)
    print("  READ THIS BEFORE QUOTING ANY NUMBER ABOVE")
    print("=" * 78)
    print("""  · n is CAPPED by FR2004's long-end buckets (2022-01-05 forward), not by
    auction history. This is ~4 years of dealer data, not a decade.
  · Pooling SBN2022+SBN2024 is DEFENSIBLE but INFERRED — zero overlapping as-of
    dates means no direct identity test exists at the API. Level continuity is
    NECESSARY, NOT SUFFICIENT. Unchecked primary: the NY Fed FR2004 form-revision
    documentation.
  · The join is a DELTA ACROSS the auction (POST minus PRE), because warehousing
    is a post-auction effect. A level-beside-it join grades the wrong quantity.
  · An auction with no POST print is DROPPED, never imputed. A publication gap
    must not be allowed to decide a market question.
  · SEPARATION, not the paired rate, is the number that answers WQ-157. A paired
    test whose leg is independent of the fire is the standalone test with extra
    steps.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
