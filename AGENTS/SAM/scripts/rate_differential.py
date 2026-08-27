#!/usr/bin/env python3
"""US-Japan rate differential — the SAM-41 bar, mechanized.

WHY THIS EXISTS: SAM-41 (5Y gap <2.25% OR 10Y gap <1.80%, 5 CONSECUTIVE business-day
closes, by 2026-10-31) was carried "still un-run, next session" for EIGHT consecutive
sessions. A check that is deferred eight times is not a check. Mechanizing it is the fix
([[finding_mechanize_the_cap_not_the_ritual]]) -- a boot check, not a remembered ritual.

SOURCES (both PRIMARY, per SAM's standing note "US leg at Treasury/FRED primary, not Yahoo"):
  US : Treasury daily par yield curve CSV (home.treasury.gov)
  JP : own workbook/JGB_YIELDS.tsv, written from the MOF primary by jgb_yields.py

⚠️ SYNCHRONICITY CAVEAT, LOAD-BEARING AND PRINTED EVERY RUN: the two legs share a DATE
LABEL but not a MOMENT -- US is a ~15:00 ET close, JGB a Tokyo close ~14h earlier. At a
gap sitting within a few bp of its bar, that gap is smaller than the asynchrony. Sub-5bp
distances to the bar are NOT resolvable by this instrument and are reported as such.
"""
import sys, csv, urllib.request
from pathlib import Path
from datetime import datetime

SAM = Path(__file__).resolve().parent.parent
JGB_TSV = SAM / "workbook" / "JGB_YIELDS.tsv"
OUT_TSV = SAM / "workbook" / "RATE_DIFFERENTIAL.tsv"
UST_URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
           "daily-treasury-rates.csv/{yr}/all?type=daily_treasury_yield_curve"
           "&field_tdr_date_value={yr}&page&_format=csv")
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

BAR_5Y, BAR_10Y, RUN_REQUIRED = 2.25, 1.80, 5
RESOLUTION_FLOOR_BP = 5.0   # below this, asynchrony dominates; do not call it

def fetch_ust(years):
    rows = {}
    for yr in years:
        req = urllib.request.Request(UST_URL.format(yr=yr), headers=HEADERS)
        txt = urllib.request.urlopen(req, timeout=45).read().decode("utf-8-sig", errors="replace")
        rd = csv.DictReader(txt.splitlines())
        for r in rd:
            try:
                d = datetime.strptime(r["Date"].strip(), "%m/%d/%Y").strftime("%Y-%m-%d")
                rows[d] = (float(r["5 Yr"]), float(r["10 Yr"]))
            except (ValueError, KeyError, TypeError):
                continue
    return rows

def load_jgb():
    out = {}
    with open(JGB_TSV) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            try:
                out[r["Date"]] = (float(r["5Y"]), float(r["10Y"]))
            except (ValueError, KeyError, TypeError):
                continue
    return out

def main():
    jgb = load_jgb()
    years = sorted({d[:4] for d in jgb})
    try:
        ust = fetch_ust(years)
    except Exception as e:
        print(f"  🔴 US leg FETCH FAILED ({type(e).__name__}) — NO VERDICT. "
              f"Never fall back to a non-primary source for this bar.")
        return 1

    dates = sorted(set(jgb) & set(ust))
    if not dates:
        print("  🔴 no overlapping dates — NO VERDICT"); return 1
    rows = [(d, ust[d][0]-jgb[d][0], ust[d][1]-jgb[d][1], ust[d], jgb[d]) for d in dates]

    print(f"\n{'='*70}\n  SAM-41 — US-JAPAN RATE DIFFERENTIAL  ({datetime.now():%Y-%m-%d %H:%M})\n{'='*70}")
    print(f"  Bar: 5Y gap < {BAR_5Y}%  OR  10Y gap < {BAR_10Y}%  on {RUN_REQUIRED} CONSECUTIVE closes, by 2026-10-31")
    print(f"  Overlapping observations: {len(rows)}  ({rows[0][0]} → {rows[-1][0]})")
    print(f"\n  {'Date':<12}{'US5Y':>7}{'JP5Y':>7}{'gap5':>8}{'':>3}{'US10Y':>7}{'JP10Y':>7}{'gap10':>8}")
    for d, g5, g10, u, j in rows[-8:]:
        f5 = "◀" if g5 < BAR_5Y else " "
        f10 = "◀" if g10 < BAR_10Y else " "
        print(f"  {d:<12}{u[0]:>7.3f}{j[0]:>7.3f}{g5:>8.3f}{f5:>3}{u[1]:>7.3f}{j[1]:>7.3f}{g10:>8.3f}{f10}")

    def run_len(vals, bar):
        n = 0
        for v in reversed(vals):
            if v < bar: n += 1
            else: break
        return n

    g5s = [r[1] for r in rows]; g10s = [r[2] for r in rows]
    r5, r10 = run_len(g5s, BAR_5Y), run_len(g10s, BAR_10Y)
    cur5, cur10 = g5s[-1], g10s[-1]

    print(f"\n  CURRENT: 5Y gap {cur5:.3f}% ({100*(cur5-BAR_5Y):+.1f}bp vs bar) · "
          f"10Y gap {cur10:.3f}% ({100*(cur10-BAR_10Y):+.1f}bp vs bar)")
    print(f"  CONSECUTIVE CLOSES THROUGH BAR: 5Y {r5}/{RUN_REQUIRED} · 10Y {r10}/{RUN_REQUIRED}")

    if max(r5, r10) >= RUN_REQUIRED:
        print(f"\n  🔴 SAM-41 CONDITION MET — {RUN_REQUIRED} consecutive closes achieved.")
        print(f"     ⛔ TRUE is NECESSARY BUT NOT SUFFICIENT for v1.8 (CH-017 relabel): a gap")
        print(f"        closes from EITHER side, and a pure US-side move routes USD-haven with")
        print(f"        the yen NOT bidding. Promotion needs a separately-registered FX")
        print(f"        co-condition + RED pass + Will sign-off. DO NOT promote on this alone.")
    elif max(r5, r10) > 0:
        print(f"\n  🟠 RUN IN PROGRESS — not yet {RUN_REQUIRED}. Not resolved. Do not pre-announce.")
    else:
        print(f"\n  🟢 no active run.")

    # the caveat that decides whether the above is even readable
    near = [(lab, abs(100*(g-b))) for lab, g, b in (("5Y", cur5, BAR_5Y), ("10Y", cur10, BAR_10Y))]
    tight = [f"{lab} ({d:.1f}bp)" for lab, d in near if d < RESOLUTION_FLOOR_BP]
    if tight:
        print(f"\n  ⚠️  BELOW RESOLUTION FLOOR: {', '.join(tight)} sits within {RESOLUTION_FLOOR_BP:.0f}bp of its bar.")
        print(f"     The legs share a DATE but not a MOMENT (US ~15:00 ET vs Tokyo close, ~14h).")
        print(f"     A distance this small is smaller than the asynchrony — the instrument CANNOT")
        print(f"     resolve it. Report as UNRESOLVED-AT-THIS-PRECISION, never as a crossing.")

    # base rate: 40% was judgment, not calibration (SAM's own standing note)
    below5 = sum(1 for v in g5s if v < BAR_5Y); below10 = sum(1 for v in g10s if v < BAR_10Y)
    either = sum(1 for a, b in zip(g5s, g10s) if a < BAR_5Y or b < BAR_10Y)
    print(f"\n  BASE RATE over the {len(rows)} observations held: 5Y below bar {below5} ({100*below5/len(rows):.0f}%) · "
          f"10Y below {below10} ({100*below10/len(rows):.0f}%) · either {either} ({100*either/len(rows):.0f}%)")
    print(f"  ⚠️  Short window ({len(rows)} obs, one regime) — a base rate here does NOT calibrate")
    print(f"     the 40%. SAM's own note stands: 40% is judgment, not calibration.")

    with open(OUT_TSV, "w") as f:
        f.write("Date\tUS_5Y\tJP_5Y\tGap_5Y\tUS_10Y\tJP_10Y\tGap_10Y\n")
        for d, g5, g10, u, j in rows:
            f.write(f"{d}\t{u[0]}\t{j[0]}\t{g5:.3f}\t{u[1]}\t{j[1]}\t{g10:.3f}\n")
    print(f"\n  → {OUT_TSV.name} ({len(rows)} rows)\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
