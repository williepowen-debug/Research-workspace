# LABOR file sweep — 2026-11-26 (Will-requested, report only, nothing edited)

**Method:** LABOR reviewed `CLAUDE.md` + `STATUS.md`; three Sonnet readers reviewed (A) `NEXUS_BRIEF.md` + `TRADE.md`, (B) `LESSONS.md` + `workbook/PREDICTIONS_SCOREBOARD.md` + `workbook/PREDICTIONS.tsv`, (C) `BUILD_DEBT.md` + `OPEN_ITEMS_2026-09-03.md` + `docket/CATALYSTS.tsv` + `scripts/tests/`. **Spot-verified by LABOR at the file:** A1, A2, A10, the charter T-04 row, the LESSONS hot/cold order, LAB-23 status cell, the failing test, BD-41, BD-02. Every other item is the reader's claim and is re-verified at fix time.
**What is sound:** every live figure, score, band and open-prediction confidence in STATUS; the scoreboard stats reproduce from §A (`4.8614 / 15 = 0.324`); PREDICTIONS.tsv open set matches STATUS; all charter/STATUS paths resolve; 4 of 5 regression suites pass.

## 1. Read by other desks — wrong today
| # | File:line | Problem | Fix | Class |
|---|---|---|---|---|
| A1 | NEXUS_BRIEF:67,70 | "What/When" leads with the graded 11/25 claims and a moved card path | restart at 12/1 JOLTS, 12/3, 12/4 | MECH |
| A2 | NEXUS_BRIEF:74–92 | "FORWARD CATALYSTS" holds 17 graded rows (Oct 1 to Nov 6, Nov 6 NFP shown pending) and no forward row | move graded rows verbatim to archive; add 12/1, 12/3, 12/4, 12/18 | MECH |
| A3 | NEXUS_BRIEF:58 | LT share 27.0% (now 27.6%), v7 "dropped to 2" (now stood down to 1) | refresh | MECH |
| A4 | NEXUS_BRIEF:35,36 | Challenger and NFP "card owed" (frozen 11/26) | mark frozen, re-pin | MECH |
| A5–A8 | NEXUS_BRIEF:25,29,45,47,49,59 | 9/4 and 9/24 views and figures presented as current ("none fired on its letter"; LF +683K; claims 200,000; RECEIVING block 6–8 weeks old) | refresh or archive | MECH |
| A10 | TRADE:36 | examples "Jun 18 >250K → T-01; Jul 2 NFP → T-05/T-06": neither fired | delete examples | MECH |
| A11 | TRADE:17 | signals routed to `outbox/` (dead route; signals → WALTER) | align to Outbox Protocol | MECH |
| A12–A13 | TRADE:2,5; 42–165 | claims to own KELYA logic though no position; ~125 of 175 lines are dead-position history | reword; move §2 tail + §3 verbatim to `domain/sources/` | MECH |
| A15–A18 | TRADE:173,17,38 | "messaging in flight" (v1 live); duplication note; Kill A note stamped 7/24 | refresh | MECH |

## 2. LABOR charter (`CLAUDE.md`) and STATUS
| # | Where | Problem | Fix | Class |
|---|---|---|---|---|
| L1 | CLAUDE:192 | T-04 send row still "U-3 ≥5.0%"; TRADE §1 re-specced T-04 to EPOP on 2026-08-07 | align row to TRADE §1 | MECH (charter edit) |
| L2 | CLAUDE C2 | headline "mean Brier 0.348, n=13, 2026-10-01"; now `4.8614 / 15 = 0.324` (11/20) | point to scoreboard instead of a number | MECH (charter edit) |
| L3 | CLAUDE IDENTITY | still argues from the Q2 ECI wedge ("AHE joins U-3 on the do-not-trust list"); ECI Q3 closed the wedge from the AHE side (STATUS ECI row) | rewrite tension sentence to Q3 | owner judgment (charter edit) |
| L4 | CLAUDE B2, FILES | "~6s" boot; measured today 103.4 s | fix | MECH |
| L5 | CLAUDE B2a, spawn step 2 | hand comparison + `--verbose` rationale (~1.1 KB) though `spine_check.py` automates it (WQ-678 K60) | shorten, history to CHARTER_DETAIL | MECH (optional K60) |
| L6 | CLAUDE spawn 3/4, signals table | WQ-678 optional K55, K58, K59 (routing/runtime wording) | Will's call (PROME: leave unless raised) | NEEDS-WILL |
| L7 | `workbook/LEDGER_GLOB` | missing (16 other desks have one); root step 1c-bis cannot nudge LABOR | create declaring KB.tsv, PREDICTIONS.tsv, CATALYSTS.tsv, WARN_COHORT.tsv | MECH |
| L8 | STATUS:2,6,63–64,92,108–114 | header still 11/25; discharged 10/02 re-trigger line; near-empty FED TRAP section; KELYA exit line; pickup numbering 0,1,3,5,6,11–12 | tidy at closeout | MECH |
| L9 | STATUS pickup 11–12 | C5 retirement moves not run since 10/1 | run them | MECH |

## 3. Scoring and lessons
| # | Where | Problem | Class |
|---|---|---|---|
| B1 | SCOREBOARD:105 | "Honest verdict" is the 9/7 one (0.342, 0-for-5, 3C/5F); now 0.324, 0-for-6, 5C/10F | MECH |
| B2 | SCOREBOARD:32 | "OPEN CANON CONFLICT" on which mean is headline; charter says WQ-193 (d) ruled both | MECH |
| B3–B7 | SCOREBOARD:20,22,58,61,63,83,91,112,134,172 | stale counts (0-for-5 → 0-for-6; 6 misses → 7, LAB-03 missing; 12 → 15 resolutions; base-rate 0.1875 vs 0.222 in one file; "next update" list names resolved/voided rows) | MECH |
| B8 | SCOREBOARD:81 | CORRECTIVE column "OWED" since 8/28, never done | MECH (do or log in BUILD_DEBT) |
| B12 | LESSONS:8–14 | newest L-37, L-36 sit as one-liners in the cold index while older L-32–L-35 are in full: inverts the file's own rule | MECH |
| B13–B14 | LESSONS:75, 8 | L-33 says BD-35 is future (built 10/28); discharged 10/02 re-trigger line | MECH |
| B17 | PREDICTIONS.tsv LAB-23 | Status `CONFIRMED` where the vocabulary is `RESOLVED` + Outcome | MECH |
| B18 | PREDICTIONS.tsv LAB-04 | Status `REHOMED→CORAL`, non-terminal token | NEEDS-WILL (scope rule) |

## 4. Build register, calendar, tests
| # | Where | Problem | Class |
|---|---|---|---|
| C2 | BUILD_DEBT:69 BD-41 | `fetch_primary.py` false-rejects ISM pages; row says "fix before the 12/1 ISM read". Fail-closed: no wrong figure, only a hand read | MECH (due 12/1) |
| C3 | `scripts/tests/test_prediction_deadlines.py` | FAILS: hard-wires LAB-19 as OPEN (resolved 11/6) | MECH |
| C1,C4–C6,C8,C12 | BUILD_DEBT BD-02, 10, 39, 18, 07, 13 | marked open or owed, already done or lapsed | MECH |
| C9,C11 | BD-12, BD-14 | trigger dates 8 weeks past, no re-date | MECH |
| C10 | BD-23 | Federal Register poll unbuilt, trigger passed 9/25 | NEEDS-WILL (build or drop) |
| C7 | BD-29 leg B | routing apparently settled; ruling record not found | verify, then close |
| C17 | BUILD_DEBT (85 KB) | ~18 discharged rows among ~17 live; split open/closed conflicts with its "discharged rows stay in place" rule | NEEDS-WILL |
| C13 | CATALYSTS vs STATUS | event sets differ: 12/2 metro release missing from STATUS; 12/8 productivity in STATUS, not CATALYSTS | MECH |
| C14 | CATALYSTS | nothing docketed after 12/18 (Dec NFP, Nov JOLTS, Dec Challenger, Dec ISM fall in early January) | MECH (verify dates at issuers) |
| C15 | CATALYSTS 12/1, 12/3 ISM + 12/3 claims | still "modeled" inside a week | MECH |
| C16 | OPEN_ITEMS_2026-09-03.md | 84 days old, not boot-read, items closed: retirement-eligible | MECH |
| A14 | TRADE + STATUS | KELYA post-mortem owed since 8/21 (95 days) | NEEDS-WILL (still wanted?) |
