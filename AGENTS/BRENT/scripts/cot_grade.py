#!/usr/bin/env python3
"""cot_grade.py — grade the REGISTERED COT test against a CFTC disaggregated print.

⛔⛔ REBUILT 2026-08-21. THE PREVIOUS VERSION GRADED A RETIRED TEST AND SAID SO CONFIDENTLY.

WHAT WAS WRONG, found by auditing the tool ~90 minutes BEFORE the print rather than
running it at the print:
  * It implemented the INCUMBENT `COT-FUEL` band only — BASE_SHORTS=129,072 (the 7/7
    anchor), COILED_BAR=-7,000, SPENT_BAR=-25,000, verdicts COILED / IGNITING / FUEL SPENT.
  * `COT-FUEL` was RETIRED in REGISTRY.tsv on 2026-08-14 and its successor `COT-FUEL-35B`
    registered the same day. The successor's legs were NOWHERE in this file: no Leg-A bar
    (113,745), no NO-VERDICT deadband (109,165-118,325), no Leg-B OI-share bar (4.909%) —
    and it never fetched OPEN INTEREST at all, so Leg B was not computable.
  * It read SOCRATA, which the registered spec explicitly forbids for this grade
    ("Grade off the RAW file, never Socrata — Socrata lagged all 40 polls on 7/17").
  ⇒ Run at the print, it would have printed `=== VERDICT: ... ===` for a RETIRED test,
    from a FORBIDDEN source, and my own SCRATCH handoff instructed me to run exactly this
    command to grade the successor.

★ AND THE PRE-FLIGHT CHECK THAT "PASSED" IS THE POINT: at 13:18 this script returned rc=3
  and printed `base 7/7 anchor: short 129,072 / long 193,113 [OK]`. I read that as "tool
  healthy." It WAS healthy — against the wrong test.
  [[finding_instrument_reports_clean_against_the_wrong_reference]] — wrong by SPEC.
  Third instance on this desk on 2026-08-21 alone (TRADE.md vs LEDGER_GLOB 09:41; the
  Baker Hughes ARCHIVE-vs-current workbook ~13:20; this).

SPEC IMPLEMENTED HERE IS THE FROZEN, WILL-RULED ONE, COPIED FROM `workbook/REGISTRY.tsv`
(row COT-FUEL-35B; build: setups/2026-08-12_35b-COT-successor-band-N1-build.md):
    base 122,904 = trailing-8wk median (2026-06-16..2026-08-04)   [context, not graded]
    median_unit  = 9,160  FROZEN  (basis n=235, 2022-02-08..2026-08-04)
    Leg A  : MM gross shorts <= 113,745                       => SPENT
             NO-VERDICT deadband 109,165 .. 118,325           (bar +/- 0.5 median unit)
             shorts > 118,325                                 => NOT-SPENT
    Leg B  : OI-share = MM gross shorts / Open Interest * 100
             <= 4.909% => SPENT, else NOT-SPENT.  LEG B IS GATING.
    VERDICT: both legs must AGREE; disagreement => NO-VERDICT.
             NO-VERDICT IS A REAL ANSWER — it defaults sizing to the BASE CASE.
             Accepted NO-VERDICT rate 33.6%, on the record.
⛔ DO NOT RE-MEASURE OR RE-BASE ANY OF THESE PER PRINT. Re-basing is a NEW N1 build and a
   fresh Will ruling, never maintenance: the trailing window is a FREE PARAMETER
   (9,160 / 8,586 / 7,652 across three defensible windows moves the bar 1,508 contracts,
   about the incumbent's entire margin).

SOURCING RULES, ALSO FROM THE REGISTERED SPEC:
  * RAW file only: https://www.cftc.gov/dea/newcot/f_disagg.txt   [[finding_cftc_cot_raw_file_beats_socrata_lag]]
  * Match by MARKET NAME, not by contract code — code 067651 spans a 2022 rename.
  * Verify `report_date` IN-ROW against --expect. exit 3 = NOT FRESH, DO NOT GRADE.
  * Browser User-Agent is load-bearing, see LESSONS L25 (a tarpitted UA reads as an outage).

EXIT CODES:  0 graded  |  2 could not grade (fetch/parse/spec problem)  |  3 not fresh, WAIT
"""
import argparse
import csv
import io
import sys
import urllib.request

RAW_URL = "https://www.cftc.gov/dea/newcot/f_disagg.txt"
MARKET = "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE"
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# --- FROZEN SPEC (REGISTRY.tsv :: COT-FUEL-35B). Do not edit without a fresh Will ruling. ---
LEG_A_BAR = 113745
DEADBAND_LO = 109165
DEADBAND_HI = 118325
LEG_B_BAR_PCT = 4.909
MEDIAN_UNIT = 9160
# DISPLAY-ONLY (never compared against anything below). CORRECTED 2026-09-06: the base is
# NOT an integer. The trailing-8wk window 2026-06-16..2026-08-04 is EIGHT observations, so its
# median is the mean of the 4th and 5th sorted values: (122,319 + 123,490) / 2 = 122,904.5.
# Displaying it truncated as 122,904 is what made the frozen letter fail its own arithmetic
# check for three independent blind readers (PROME packet 2026-09-03). THE LEVELS WERE ALWAYS
# RIGHT AND NONE MOVED — carry the .5 and they all reproduce to the contract:
#   Leg-A bar = base - 1.0*median_unit = 122,904.5 - 9,160 = 113,744.5 -> 113,745 (half up)
#   deadband  = bar  +/- 0.5*median_unit = 113,744.5 +/- 4,580 -> 109,165 .. 118,325
BASE_8WK = 122904.5

# disaggregated futures-only column layout (verified 2026-08-21 against the 8/11 print:
# it reproduced the registry's recorded first grade — shorts 110,638 / OI 1,892,429 /
# share 5.8463% — to the digit, which is what validates these indices).
I_REPORT_DATE = 2
I_CODE = 3
I_OI = 7
I_MM_LONG = 13
I_MM_SHORT = 14


def fetch_raw():
    req = urllib.request.Request(RAW_URL, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8", errors="replace")


def find_row(text, market=MARKET):
    hits = []
    for rec in csv.reader(io.StringIO(text)):
        if rec and rec[0].strip().strip('"') == market:
            hits.append([c.strip() for c in rec])
    return hits


def leg_a(shorts):
    if shorts <= LEG_A_BAR and shorts < DEADBAND_LO:
        return "SPENT"
    if DEADBAND_LO <= shorts <= DEADBAND_HI:
        return "NO-VERDICT"
    return "NOT-SPENT"


def leg_b(share_pct):
    return "SPENT" if share_pct <= LEG_B_BAR_PCT else "NOT-SPENT"


def joint(a, b):
    """Both legs must AGREE. Leg B is GATING. Disagreement => NO-VERDICT."""
    if a == "NO-VERDICT":
        return "NO-VERDICT"
    if a == b:
        return a
    return "NO-VERDICT"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expect", required=True,
                    help="expected report_date (as-of Tuesday), YYYY-MM-DD")
    a = ap.parse_args()

    print("  COT-FUEL-35B — registered successor band (COT-FUEL incumbent is RETIRED)")
    print(f"  source  : RAW {RAW_URL}")
    print(f"  market  : {MARKET}  (matched by NAME; code spans a 2022 rename)")
    try:
        text = fetch_raw()
    except Exception as e:
        print(f"  🔴 FETCH FAILED: {type(e).__name__}: {e}")
        print("     ⚠️  If this is a hang/timeout rather than an HTTP error, check the "
              "User-Agent before concluding the host is down (LESSONS L25).")
        return 2

    hits = find_row(text)
    if len(hits) != 1:
        print(f"  🔴 expected exactly 1 row for the market name, got {len(hits)} — NOT GRADING")
        return 2
    r = hits[0]
    rd = r[I_REPORT_DATE]
    print(f"  freshest report date IN-ROW: {rd}  (expecting {a.expect})  code={r[I_CODE]}")
    if rd != a.expect:
        print(f"\n  ⏳ NOT FRESH — newest is {rd}, not {a.expect}. Release not out (or delayed). "
              f"DO NOT GRADE.")
        return 3

    shorts = int(r[I_MM_SHORT]); longs = int(r[I_MM_LONG]); oi = int(r[I_OI])
    share = shorts / oi * 100.0
    va, vb = leg_a(shorts), leg_b(share)
    v = joint(va, vb)

    print(f"\n  MM gross shorts : {shorts:>10,}")
    print(f"  MM gross longs  : {longs:>10,}")
    print(f"  Open interest   : {oi:>10,}")
    print(f"  OI-share        : {share:>10.4f}%")
    print(f"\n  Leg A  shorts {shorts:,} vs bar {LEG_A_BAR:,} "
          f"(deadband {DEADBAND_LO:,}-{DEADBAND_HI:,})  => {va}")
    print(f"  Leg B  OI-share {share:.4f}% vs bar {LEG_B_BAR_PCT}%  [GATING]        => {vb}")
    print("  Leg-A precedence (stated 2026-09-06, changes no grade ever taken): the DEADBAND is")
    print("  decisive inside its range and 113,745 is its CENTRE, never a decision boundary —")
    print(f"  <= {DEADBAND_LO-1:,} SPENT | {DEADBAND_LO:,}..{DEADBAND_HI:,} NO-VERDICT | >= {DEADBAND_HI+1:,} NOT-SPENT")
    print(f"\n  === JOINT VERDICT: {v} ===")
    if v == "NO-VERDICT":
        print("  NO-VERDICT IS A REAL ANSWER — sizing DEFAULTS TO THE BASE CASE (conservative).")
        print("  Accepted NO-VERDICT rate for this band is 33.6%, on the record.")
    print(f"\n  context (NOT graded): base_8wk {BASE_8WK:,} · median_unit {MEDIAN_UNIT:,} FROZEN"
          f" · distance to Leg-A bar {shorts - LEG_A_BAR:+,} "
          f"({(shorts - LEG_A_BAR)/MEDIAN_UNIT:+.2f} median units)")
    print("  ⚠️  SIZING MODIFIER ONLY — never reuse as an ENTRY trigger without a fresh build.")
    print("  ⚠️  NON-CLAIMS TRAVEL WITH THIS ROW: no out-of-sample test; n=0 genuine physical")
    print("      reopenings; no price validation (a positioning DESCRIPTOR, never shown to predict).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
