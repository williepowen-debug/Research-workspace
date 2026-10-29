# Post-mortems: resolved predictions MIDAS-01 to MIDAS-08

**Written 2026-10-29 00:05 EDT** (desk audit #7 follow-up, Will-directed owed-work session). MIDAS `CLAUDE.md` § PREDICTIONS asks for post-mortems on resolved rows and a failure-pattern synthesis that feeds THESIS as rules gating future calls. **The rows stay in `workbook/PREDICTIONS.tsv`** because `grade_midas07.py` and `scripts/asmade_audit.py` read them verbatim; this file cites them by ID and copies none of their text. Grades are as recorded in each row's `resolution` cell; nothing is re-graded here.

## Record

| ID | Made | Channel | Question (short) | Outcome | What it taught |
|---|---|---|---|---|---|
| MIDAS-01 | 7/11 | M1 | Gold does not fall >10% from 7/10 while real 10Y stays >2% through Q3 | **HIT** 10/1 on the frozen letter | Low information: the window low was still 7.83% above the kill line and no probability was stated. The anchor had to be added after registration (L-10) |
| MIDAS-02 | 7/11 | I1 | Copper does not roll >20% with LME inventory >+100% through Q3 | **HIT** 10/1 | Same shape: neither leg came near firing, so the conjunction was close to certain. The LME median was hardcoded (frozen-denominator risk) and was reported beside an as-of median |
| MIDAS-03 | 7/12 | M1 | CPI-day gold reaction vs real-yield direction (M1 v2 frame) | **HIT** 7/17 | Good design: a dated event, both reaction directions pre-assigned, graded in three sessions |
| MIDAS-04 | 7/12 | I1 | China Q2 GDP miss plus copper −5% within two sessions → I1 yellow | **NO-FIRE**, correct null | Antecedent fired and the consequent did not, which is real discrimination. The registered "~7/16" release was actually 7/15, so anchor to the event, not a calendar guess (L-10) |
| MIDAS-05 | 7/17 | I1 | PBoC LPR cut plus copper +3% → stimulus read | **NO-FIRE**, correct null | LPR held as 23/23 polled expected. A test whose antecedent is ~65% unlikely mostly grades the null; cheap but weak |
| MIDAS-06 | 8/7 | M1 | Does the fired kill-cond #3 divergence persist to 8/28? | Terminal per Will's 8/21 ruling on the frozen letter (row status HIT) | Single-print fragility: branch (a) had no duration clause. Will ruled it a successor-design issue, not a mid-flight edit (L-12) |
| MIDAS-07 | 8/7 | M1 | Gold COT: specs chasing or move absorbed after the 8/5–8/7 melt-up | **INDETERMINATE** 8/14 | The pre-registered modal outcome was (d) INDETERMINATE at about 92%. Honoured correctly, but a test that expects to say nothing tells little |
| MIDAS-08 | 9/2 | M1 | Did the crowded spec long unwind into a −6.35% week? | **INDETERMINATE** 9/5 | Ratio vs absolute: net long fell 6.25% but net/OI moved only −1.92 pp because open interest fell too (L-49) |

**Count:** 3 HIT, 2 correct NO-FIRE nulls, 1 terminal ruling (row status HIT), 2 INDETERMINATE. **There are no MISS or FALSIFIED rows**, so there is no calibration signal yet. No probability was stated on any of the eight rows, so no Brier-type score is possible.

## Failure patterns

1. **Hold-calls with distant kill lines (01, 02) were near-certain and unpriced.** A HIT that was never in doubt does not test the thesis.
2. **Modal-indeterminate designs (07, 08) used the registration slot to learn little.** Both were frozen and graded honestly; the weakness was in the design.
3. **Clock and denominator defects (01 anchor, 04 date, 08 ratio, 02 hardcoded median)** were each caught, but at grading rather than at registration.
4. **Event-reaction tests (03, 04, 05) were the most efficient:** dated antecedent, short window, both directions pre-assigned.

## Rules gating future MIDAS calls

These restate rules already in canon or in later rows, joined in one place. They add no new gate on frozen rows.

| Rule | Status |
|---|---|
| **R1. State a probability and the margin to the kill line at registration.** Prefer lines with a meaningful chance of firing over safe holds | Already practised: MIDAS-13..17 (10/23) each carry P and a base rate |
| **R2. If the modal pre-registered branch is INDETERMINATE, redesign before registering** (or register knowingly as a null-heavy instrument) | New explicit rule from 07/08; applies to successors only |
| **R3. Anchor dates to the event type, not a calendar guess; name the anchor type** | L-10; fleet `finding_resolver_anchored_to_expected_event_inherits_slip_risk` |
| **R4. Register ratio AND absolute quantities; state which binds** | L-49 |
| **R5. Use a stated as-of denominator, not a hardcoded norm** | Practised since the 10/12 maintenance (rolling 730-day LME median) |
| **R6. Duration thresholds carry a continuity rule** | L-12 |

THESIS carries a one-line pointer to this file under its prediction section. No frozen prediction, probability, threshold or score changed.
