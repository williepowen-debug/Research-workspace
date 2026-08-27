#!/usr/bin/env python3
"""ORACLE — TRADE.md mark tracker: the trajectory behind every routed figure.

WHY THIS EXISTS
  TRADE.md is a ROUTING surface -- other desks read its numbers and key positions
  off them -- and it has now rotted twice in the same way. DAEDALUS caught it at
  21 days (7/22 figures live on 8/11); the Will-directed sweep on 2026-08-27
  caught it again at 15 days, with Hormuz-normal off by 14.0pp and best-asset-S&P
  off by 14.5pp. A refresh alone does not fix that -- it just resets the clock on
  the next rot.

  Will's instruction (2026-08-27): refresh it, but "not simply delete" the old
  numbers -- "track how the numbers have changed over time."

  So the fix is structural: every routed figure carries its own history. A row
  that shows 7/22 -> 8/12 -> 8/27 makes its own staleness legible -- a reader
  seeing a trailing date knows the row is old WITHOUT having to check a header.
  Rot that announces itself is a different failure mode from rot that hides.

  Source of truth is ORACLE's OWN append-only logs (workbook/ODDS_LOG.tsv and
  workbook/KALSHI_ODDS_LOG.tsv), so no vintage is ever hand-typed. Every figure
  in TRADE.md is reproducible from a log row by date + slug.

⚠️ THE THING THIS TOOL EXISTS TO GET RIGHT: CONTRACT IDENTITY
  A "trajectory" across two different contracts is not a trajectory, it is a
  category error -- and this desk's own board is full of the trap:
    - bank-failure-by-Dec-31 has had THREE slugs (...0629191920016 / ...0720194747677
      / ...20260824). The 73.0% -> 55.5% "fade" spans a delist+relist and is NOT a move.
    - WTI-$100 is MONTH-STAMPED: Jun / Jul / Aug / Sep are four separate contracts.
      A fresh month has more days-to-touch and is structurally higher.
    - Hormuz-normal ran by-Jun30 / by-Jul15 / by-Dec31 -- different horizons.
  So marks are declared as a FAMILY of slugs, the series is SEGMENTED whenever the
  slug changes, and deltas are computed ONLY inside a segment. A break prints as a
  visible bar (|) and the tool refuses to difference across it.

Usage:  python3 tools/trade_marks.py [--write] [--since YYYY-MM-DD]
"""
import os, csv, argparse, datetime
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
PM_LOG = os.path.join(ORACLE, "workbook", "ODDS_LOG.tsv")
KAL_LOG = os.path.join(ORACLE, "workbook", "KALSHI_ODDS_LOG.tsv")
OUT = os.path.join(ORACLE, "workbook", "TRADE_MARKS.tsv")

# mark_id -> (platform, [slug/ticker patterns, newest last], routes, rolls?)
#   rolls=True  => slug changes are EXPECTED (month/period contracts)
#   rolls=False => a slug change is a DELIST/RELIST identity break
MARKS = [
    ("fed_nocuts",     "PM",     ["will-no-fed-rate-cuts-happen-in-2026"],                 "KRE/OZK/WAL shorts", False),
    ("fed_hike_2026",  "PM",     ["fed-rate-hike-in-2026"],                                "KRE/OZK/WAL shorts", False),
    ("fed_hike_sept",  "PM",     ["will-the-fed-increase-interest-rates-by-25-bps-after-the-september-2026-meeting"], "KRE/OZK/WAL shorts", False),
    ("fed_hike_sept_k","KALSHI", ["KXFED-26SEP-T3.75"],                                    "T6 canonical",       False),
    ("hormuz_normal",  "PM",     ["strait-of-hormuz-traffic-returns-to-normal-by-december"],"BRENT/HAWK/FALCON", False),
    ("wti_100",        "PM",     ["will-wti-reach-100-in-"],                               "BRENT/HAWK/FALCON",  True),
    ("us_invade_iran", "PM",     ["will-the-us-invade-iran-before-2027"],                  "BRENT/HAWK/FALCON",  False),
    ("recession",      "PM",     ["us-recession-by-end-of-2026"],                          "whole bear book",    False),
    ("recession_k",    "KALSHI", ["KXRECSSNBER-26"],                                       "whole bear book",    False),
    ("bank_fail_any",  "PM",     ["us-bank-failure-by-december-31-2026"],                  "REGINALD/WAL/OZK",   False),
    ("bank_fail_named","PM",     ["which-banks-will-fail-by-end-of-2026"],                 "REGINALD/WAL/OZK",   False),
    ("neh",            "PM",     ["nothing-ever-happens-2026"],                            "VIOLET vol/tails",   False),
    ("best_asset_sp",  "PM",     ["bitcoin-vs-gold-vs-sp-500-in-2026"],                    "VIOLET vol/tails",   False),
    ("credit_dngrade", "KALSHI", ["KXCREDITRATING-26DEC31"],                               "BOND (blind-spot)",  False),
]


def load(path, slug_col, prob_col, vol_col, liq_col):
    rows = defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            slug = (r.get(slug_col) or "").strip()
            if not slug:
                continue
            try:
                p = float(r[prob_col])
            except (TypeError, ValueError, KeyError):
                continue
            rows[slug].append({
                "date": r["ts"][:10], "ts": r["ts"], "slug": slug,
                "label": (r.get("label") or "").strip(), "prob": p,
                "vol": r.get(vol_col, ""), "liq": r.get(liq_col, ""),
            })
    return rows


def series_for(store, patterns):
    """All observations whose slug/ticker starts with any declared pattern, by date."""
    out = []
    for slug, obs in store.items():
        if any(slug.startswith(p) for p in patterns):
            out.extend(obs)
    # one obs per date (last pull of that day wins), chronological
    by_date = {}
    for o in sorted(out, key=lambda x: x["ts"]):
        by_date[o["date"]] = o
    return [by_date[d] for d in sorted(by_date)]


def segment(series):
    """Split into runs of identical slug. A slug change = an identity break."""
    segs, cur = [], []
    for o in series:
        if cur and o["slug"] != cur[-1]["slug"]:
            segs.append(cur); cur = []
        cur.append(o)
    if cur:
        segs.append(cur)
    return segs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--since", default="2026-07-22", help="first vintage to display (default: the 7/22 TRADE.md vintage)")
    a = ap.parse_args()

    pm = load(PM_LOG, "slug", "yes_prob", "volume", "liquidity")
    kal = load(KAL_LOG, "ticker", "yes_prob", "volume", "liquidity")

    out_rows, unresolved = [], []
    print(f"ORACLE TRADE.md MARK TRAJECTORIES  (from own logs; vintages >= {a.since})")
    print("=" * 118)
    for mark_id, plat, pats, routes, rolls in MARKS:
        store = pm if plat == "PM" else kal
        ser = series_for(store, pats)
        if not ser:
            unresolved.append(mark_id)          # fail loud, never silently blank
            continue
        segs = segment(ser)
        shown = [o for o in ser if o["date"] >= a.since]
        if not shown:
            unresolved.append(mark_id + " (no obs in window)")
            continue

        print(f"\n{mark_id:<16} [{plat}]  → {routes}")
        parts, prev = [], None
        for o in shown:
            brk = prev is not None and o["slug"] != prev["slug"]
            if brk:
                parts.append("‖BREAK‖" if not rolls else "‖ROLL‖")
            d = ""
            if prev is not None and not brk:
                d = f"({(o['prob']-prev['prob'])*100:+.1f})"
            parts.append(f"{o['date'][5:]} {o['prob']*100:.1f}%{d}")
            prev = o
        print("   " + "  ".join(parts))
        if len(segs) > 1:
            kind = "expected period ROLLS" if rolls else "⚠️ DELIST/RELIST identity breaks"
            print(f"   ⚠️ {len(segs)} contract segments ({kind}) — deltas are computed INSIDE segments only, never across:")
            for s in segs:
                print(f"      · {s[0]['date']}..{s[-1]['date']}  {s[0]['prob']*100:.1f}%→{s[-1]['prob']*100:.1f}%  {s[0]['slug'][:62]}")

        for o in ser:
            seg_i = next(i for i, s in enumerate(segs) if o in s)
            out_rows.append([o["date"], o["ts"], mark_id, plat, o["slug"], o["label"],
                             f"{o['prob']*100:.1f}", o["vol"], o["liq"], f"seg{seg_i+1}",
                             "ROLL" if rolls else "FIXED", routes])

    print("\n" + "=" * 118)
    if unresolved:
        print(f"🔴 {len(unresolved)} mark(s) UNRESOLVED — declared but not found in the logs: {', '.join(unresolved)}")
        print("   A blank row on a routing surface is the failure this tool exists to prevent. Fix the pattern or retire the mark.")
    else:
        print(f"✓ all {len(MARKS)} declared marks resolved against the logs")

    if a.write:
        with open(OUT, "w", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["date","ts","mark_id","platform","slug","label","yes_pct",
                        "volume","liquidity","segment","identity","routes"])
            for r in sorted(out_rows, key=lambda x: (x[2], x[0])):
                w.writerow(r)
        print(f"\nwrote {len(out_rows)} rows → {OUT}")


if __name__ == "__main__":
    main()
