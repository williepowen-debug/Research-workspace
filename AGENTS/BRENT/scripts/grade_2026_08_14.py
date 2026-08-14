#!/usr/bin/env python3
"""ONE-SHOT grader for the 2026-08-14 COT window.

Frozen letter = setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md
Nothing in here is a free parameter. Every constant below is copied from the card.
Run: .venv/bin/python3 AGENTS/BRENT/scripts/grade_2026_08_14.py [path-to-f_disagg.txt]
"""
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/f_disagg.txt"
EXPECT = "2026-08-11"
CODE = "067651"

# ---- INCUMBENT (35a REVERT semantics, non-latching) ----
BASE_ANCHOR = 129072          # 2026-07-07 frozen base
SPENT_CUM_BAR = -25000        # SPENT iff cumulative <= this
INCUMBENT_BOUNDARY = 104072   # <=104,072 HOLDS ; >=104,073 UN-FIRES
PRIOR_PRINT = 102560          # 2026-08-04

# ---- 35b SUCCESSOR (all FROZEN at the approved basis) ----
SUCC_BASE = 122904            # trailing-8wk median, 2026-06-16..2026-08-04
MEDIAN_UNIT = 9160            # FROZEN, basis n=235, 2022-02-08..2026-08-04
LEG_A_BAR = 113745            # base - 1.0 median unit
DEADBAND_LO = 109165          # bar - 0.5 unit
DEADBAND_HI = 118325          # bar + 0.5 unit
LEG_B_BAR = 4.909             # OI-share %, trailing-104wk median

row = None
for line in open(SRC, encoding="utf-8", errors="replace"):
    if CODE in line:
        f = [x.strip().strip('"') for x in line.split(",")]
        if f[0].startswith("WTI-PHYSICAL"):
            row = f
            break
if row is None:
    sys.exit("FATAL: no WTI-PHYSICAL row for code %s in %s" % (CODE, SRC))

name, report_date = row[0], row[2]
oi = int(row[7].replace(",", ""))
short = int(row[14].replace(",", ""))

print("=" * 72)
print("  market       :", name)
print("  report_date  :", report_date, "(verified IN-ROW -- Trap 1)")
print("  OI (field 8) : %s" % format(oi, ","))
print("  MM gross SHORT (field 15): %s" % format(short, ","))
if report_date != EXPECT:
    print("\n  STOP -- vintage is %s, expected %s. DO NOT GRADE." % (report_date, EXPECT))
    sys.exit(3)

wow = short - PRIOR_PRINT
cum = short - BASE_ANCHOR
print("  WoW vs 8/04  : %+d" % wow)
print("  cum vs base  : %+d   (base %s, bar %s)" % (cum, format(BASE_ANCHOR, ","), format(SPENT_CUM_BAR, ",")))

print("\n" + "=" * 72)
print("  STEP 1 -- INCUMBENT FINAL GRADE (35a REVERT, non-latching)")
print("=" * 72)
holds = short <= INCUMBENT_BOUNDARY
print("  boundary     : <=%s HOLDS  |  >=%s UN-FIRES" % (
    format(INCUMBENT_BOUNDARY, ","), format(INCUMBENT_BOUNDARY + 1, ",")))
print("  cum <= -25,000 ? %s" % (cum <= SPENT_CUM_BAR))
print("\n  >>> VERDICT: SPENT %s" % ("HOLDS" if holds else "UN-FIRES"))
print("      margin to boundary: %+d contracts" % (INCUMBENT_BOUNDARY - short))
print("      => fuller-size branch %s" % (
    "STAYS LIVE" if holds else "REVERTS TO BASE CASE (modifier OFF)"))

print("\n" + "=" * 72)
print("  STEP 2 -- 35b SUCCESSOR (register only after Step 1 is written)")
print("=" * 72)
oi_share = short / oi * 100
print("  Leg A: shorts %s vs bar %s" % (format(short, ","), format(LEG_A_BAR, ",")))
if short < DEADBAND_LO:
    leg_a = "SPENT"
elif short > DEADBAND_HI:
    leg_a = "NOT-SPENT"
else:
    leg_a = "NO-VERDICT (inside deadband %s-%s)" % (
        format(DEADBAND_LO, ","), format(DEADBAND_HI, ","))
print("         -> Leg A = %s" % leg_a)
print("  Leg B: OI-share %.4f%% vs bar <=%.3f%%" % (oi_share, LEG_B_BAR))
leg_b = "SPENT" if oi_share <= LEG_B_BAR else "NOT-SPENT"
print("         -> Leg B = %s  (GATING)" % leg_b)

a = leg_a.split()[0]
if a == "NO-VERDICT":
    joint = "NO-VERDICT (Leg A inside deadband)"
elif a == leg_b:
    joint = a
else:
    joint = "NO-VERDICT (legs DISAGREE)"
print("\n  >>> SUCCESSOR JOINT VERDICT: %s" % joint)
if joint.startswith("NO-VERDICT"):
    print("      NO-VERDICT is a REAL ANSWER -> sizing defaults to the BASE CASE (conservative).")
print("\n  median_unit = %s  FROZEN  [basis n=235, 2022-02-08..2026-08-04]" % format(MEDIAN_UNIT, ","))
print("  Re-basing the median unit is a NEW N1 BUILD + a fresh Will ruling, never maintenance.")
print("=" * 72)
