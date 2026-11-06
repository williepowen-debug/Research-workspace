# CREED -> PROME: T-08b graded NOT FIRED for Q3; PRED-012 FALSE; PRED-011 NO-VERDICT

**Date:** 2026-11-06 (Fri) | **From:** CREED, session `7410b7c9-f5c8-465f-bad3-3eec55272e03` (Claude Code, Opus 5.5) | **Under:** WQ-626 A, DOCKET L964 | **Class:** ROUTINE, no fire

**In plain words.** The lender test did not fire. The rule needs five of the ten lenders to have actually written off at least 5% of their book in the quarter, and only two did: KKR Real Estate Finance (KREF) and Granite Point (GPMT). Ready Capital (RC) came closest at 4.8%. The caveat Will should hear with it: half the group lost more than 3% of book value anyway, mostly through reserves and markdowns rather than realized losses. Reserves can turn into write-offs later, so "not fired" means Q3 did not meet the ruled test, not that lenders are fine.

| Item | Result | Source |
|---|---|---|
| Census | Complete, 10 of 10 reporting names; ARI never reports | `research/2026-10-28_MREIT_Q3_CENSUS_PARTIAL.md` addendum 11/06 |
| Leg 1 | Met, 5 of 11; no new cut | RC $0.01, STWD $0.48, ACRE $0.15 flat |
| Leg 2, WQ-620 term | **Not met, 2 of 10, needs 5:** KREF 26.4, GPMT 9.2; RC 4.8 ($53.87M of $1,127.8M) | RC 8-K acc 0001628280-26-071156; PRIMARY-READ 11/06 |
| `CREED-T-08b` | **NOT FIRED for Q3.** Counting RC and NREF anyway gives 4 | `registry/THRESHOLDS.tsv`, `KB-CREED-109` |
| Starwood (STWD) | Realized $38.4M, 0.6%; $336.6M provision, unrealized; book −8.6% DERIVED | 8-K + 10-Q acc 0001465128-26-000030/-31 |
| Ares Commercial (ACRE) | No realized loan loss; book $8.86 | 8-K acc 0001628280-26-071276 |
| `PRED-CREED-012` | RESOLVED-FALSE, 55%, wrong side, Brier 0.3025 | EX-99.2 |
| `PRED-CREED-011` | NO-VERDICT, $6.44 inside $6.43 to $6.55, not scored | EX-99.1 |
| Calibration | n=8, mean Brier 0.292, 4/8 | `workbook/PREDICTIONS_SCOREBOARD.md` |

**Ungraded beside it, as Will ruled:** book erosion over 3% **5 of 10** (GPMT −21.8, BXMT −11.7, STWD −8.6, RC −5.7, NREF −5.2); four-quarter write-offs over 5% **5 of 10** at 9/30, mixed basis, named in the addendum.

**Caveats that travel:**
- ⚠️ The term was written after seeing 7 of the 10 names.
- ⚠️ The erosion figures sit at the one-half line the leg uses; they are not fires and no term moved. STWD's 10-Q attributes its provision to higher projected rates.
- ⚠️ NREF, RC and ACRE 10-Qs were not on EDGAR at the grade; NREF is "none disclosed", not a clean zero. STWD's book is derived, its website supplement unread. All earnings calls unheard.
- ⚠️ `VX-CREED-10.04` is held ORANGE on the realized measure. Its red word "cohort-wide" has no number and erosion reads 5 of 10. No level proposed; a band number would be Will's.

**Unchanged:** S8b 3, convergence 28/45, every band, op and route. Broad CRE-to-bank transmission is not confirmed. No route sent: no fire. No new forecast registered. Pinned rows 001, 004, 007 hash-verified unchanged.

ACTION:
1. PROME closes DOCKET row L964.
2. PROME closes DOCKET row 950 as NO-VERDICT (`PRED-CREED-011`).
3. PROME closes DOCKET row 951 as MISS (`PRED-CREED-012`).
4. PROME tells Will the `T-08b` result with the erosion caveat in the plain-words paragraph above.

## COMPLETION — CREED — 2026-11-06
STATUS: ✅ DONE
CHANGED: AGENTS/CREED/ STATUS, SCRATCH, COVERAGE, CALENDAR, README, board_log, thesis/THESIS + CHANGELOG, research census addendum, workbook KB + VX + VX_HISTORY + FLOW + PREDICTIONS + SCOREBOARD, notes, registry/THRESHOLDS + corrections_receipts, cases/CASES + CASE_EVENTS, catchups/2026-11-06 + INDEX, inbox filed
RESULT: T-08b graded NOT FIRED for Q3, leg 2 at 2 of 10 against 5, leg 1 at 5 of 11. PRED-012 FALSE (Brier 0.3025), PRED-011 NO-VERDICT. KB-109..112 added, 6 mail items filed.
GAPS: NREF, RC and ACRE 10-Qs not filed at the grade, check after filing; the count needs 3 more names to change. STWD website supplement unread.
WILL_NEEDS: None.
FOLLOW-UP: PROME closes L964, 950, 951. CREED holds open for PROME's closeout ask.
