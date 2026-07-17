#!/usr/bin/env python3
"""
cot_grade.py — mechanical grader for the CFTC COT spring-fuel test.

Grades ONLY against the frozen pre-registration:
  setups/2026-07-17_COT-grade-and-FAL02-prereg.md

Primary venue: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (CFTC disaggregated,
futures-only, dataset 72hh-3qpy). Contract name verified against the primary
2026-07-17: the 7/7 row returns MM short 129,072 / MM long 193,113, which
matches the pre-reg baseline exactly.

Primary metric: WoW change in MM GROSS SHORTS off the 129,072 base (as-of 7/7).
  COILED       dShorts >= -7,000   (level >= ~122,000)
  IGNITING     -25,000 < dShorts < -7,000  (level ~104,000-122,000)
  FUEL SPENT   dShorts <= -25,000  (level <= ~104,000)

REPORT-DATE GATE: refuses to grade unless the freshest row is the expected
report date (default 2026-07-14). A stale row exits 3 — never grade last
week's data as this week's print.

Exit codes:
  0 = graded OK
  2 = fetch/parse failure (fail LOUD, never fabricate)
  3 = release not fresh yet (expected report date absent) — wait, do not grade

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/cot_grade.py
  .venv/bin/python3 AGENTS/BRENT/scripts/cot_grade.py --expect 2026-07-14

Built by BRENT 2026-07-17 (pre-print, before the data — the grade is frozen).
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

BASE = "https://publicreporting.cftc.gov/resource/72hh-3qpy.json"
MARKET = "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE"
CORROB = "CRUDE OIL, LIGHT SWEET-WTI - ICE FUTURES EUROPE"  # ICE WTI look-alike

# --- FROZEN PRE-REG CONSTANTS (do not edit post-print) ---
BASE_SHORTS = 129072      # as-of 2026-07-07 [CONF CFTC]
BASE_LONGS = 193113
COILED_BAR = -7000
SPENT_BAR = -25000
EXPECT_DEFAULT = "2026-07-14"


def fetch(market, limit=6):
    url = BASE + "?" + urllib.parse.urlencode({
        "$where": f"market_and_exchange_names = '{market}'",
        "$order": "report_date_as_yyyy_mm_dd DESC",
        "$limit": str(limit),
    })
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        rows = json.loads(r.read())
    out = []
    for x in rows:
        out.append({
            "date": str(x["report_date_as_yyyy_mm_dd"])[:10],
            "short": int(x["m_money_positions_short_all"]),
            "long": int(x["m_money_positions_long_all"]),
        })
    return out


def verdict(d):
    if d >= COILED_BAR:
        return "COILED", "fuel INTACT — the violent unwind is still AHEAD; re-entry conviction HIGHEST"
    if d > SPENT_BAR:
        return "SQUEEZE IGNITING", "fuel BURNING NOW — accelerant live; re-entry MODERATE, dip may not come"
    return "FUEL SPENT", "accelerant largely CONSUMED; re-entry DOWNGRADED absent a fresh kinetic leg"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expect", default=EXPECT_DEFAULT,
                    help="required report date (YYYY-MM-DD); refuses to grade otherwise")
    a = ap.parse_args()

    try:
        rows = fetch(MARKET)
    except Exception as e:
        print(f"FETCH FAILED ({type(e).__name__}: {e}) — fail loud, do not grade", file=sys.stderr)
        return 2
    if not rows:
        print("no rows returned — fail loud", file=sys.stderr)
        return 2

    newest = rows[0]
    print(f"  primary : {MARKET}")
    print(f"  freshest report date: {newest['date']}  (expecting {a.expect})")

    # --- baseline integrity check: the 7/7 anchor must still read 129,072 ---
    anchor = next((r for r in rows if r["date"] == "2026-07-07"), None)
    if anchor:
        ok = anchor["short"] == BASE_SHORTS and anchor["long"] == BASE_LONGS
        flag = "OK" if ok else "!! REVISED — pre-reg base no longer matches primary"
        print(f"  base 7/7 anchor: short {anchor['short']:,} / long {anchor['long']:,}  [{flag}]")
        if not ok:
            print("  ^ CFTC revised the anchor. Grade against the FROZEN base, note the revision.")

    if newest["date"] != a.expect:
        print(f"\n  ⏳ NOT FRESH — newest is {newest['date']}, not {a.expect}. "
              f"Release not out (or delayed). DO NOT GRADE.")
        return 3

    d_short = newest["short"] - BASE_SHORTS
    d_long = newest["long"] - BASE_LONGS
    net_new, net_old = newest["long"] - newest["short"], BASE_LONGS - BASE_SHORTS
    v, read = verdict(d_short)

    print(f"\n  MM gross SHORTS : {BASE_SHORTS:,} -> {newest['short']:,}   ({d_short:+,})")
    print(f"  MM gross longs  : {BASE_LONGS:,} -> {newest['long']:,}   ({d_long:+,})")
    print(f"  MM NET          : {net_old:,} -> {net_new:,}   ({net_new-net_old:+,})")
    print(f"\n  === VERDICT: {v} ===")
    print(f"  {read}")
    print(f"  (bars: COILED >= {COILED_BAR:+,} | IGNITING {SPENT_BAR:+,}..{COILED_BAR:+,} | SPENT <= {SPENT_BAR:+,})")

    # mechanism check — net rise via covering vs fresh longs (pre-reg corroborator)
    if net_new > net_old:
        driver = "SHORT-COVERING" if d_short < 0 and abs(d_short) > abs(d_long) else "FRESH LONGS"
        print(f"  net ROSE, driver = {driver}"
              + ("  <- tag 'fresh longs', NOT squeeze (different mechanism)"
                 if driver == "FRESH LONGS" else ""))

    try:
        c = fetch(CORROB, limit=3)
        if c and c[0]["date"] == a.expect:
            prev = c[1] if len(c) > 1 else None
            ds = f"{c[0]['short']-prev['short']:+,}" if prev else "n/a"
            print(f"\n  corroborating (ICE WTI look-alike): short {c[0]['short']:,} ({ds} WoW)")
        elif c:
            print(f"\n  corroborating (ICE WTI look-alike): newest {c[0]['date']} — not yet fresh")
    except Exception:
        print("\n  corroborating venue: fetch failed (non-fatal)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
