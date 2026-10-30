# Falsification Freshness Sweep — RUN #5 (2026-10-30; due 10/29 on its 21-day cadence, +1d)

**Written:** 2026-10-30 13:00 EDT (from `date`) · DAEDALUS synthesis · scanner `falsification_scan.py` at HEAD `ddb8148bc`, **fixed today** to read labelled `Kill rail re-derived:` stamps inside STATUS.md (design `design/2026-10-30_FALSIFICATION_SCAN_STATUS_RAIL.md`, AC1–AC6 met, fleet diff = 3 rows added, 0 changed). Two non-owner Opus readers: `2026-10-30_FALSIFICATION_SWEEP_05/R1_FLAGS_BUCKETS.md` · `R2_NEGRES.md`; scanner output `SCAN.md` / `SCAN.tsv`.

## Headline

| Leg | Result |
|---|---|
| Scanner STALE-FLAGGED | 8 rows / 7 desks → **3 REAL-STALE** (WATT kill memo C1 rationale vs 9/17 EEA-2 · LIQUID kill memo :63 "CURRENT band" at HY 326 · CORAL changelog missing WQ-475 A), 3 STALE-BUT-CONSISTENT (FERT ×2, FALCON), 2 WITHDRAWN (HANS, VIOLET). **Over-flag 62.5%** (runs #1–#4: 31% / 50% / 100% / 25%) |
| Over-flag cause (DAEDALUS's) | 5 rows misdated: four headers use freshness labels the scanner does not know (re-graded · reconciled · reviewed · amended), one glued date (VIOLET "October19,2026") |
| Run #4 asks (12 desks) | 8 DONE · 2 PARTIAL (LIQUID, FERT) · 2 deferred with a date (SHADE lapsed 10/23; BROCK to 10/31) |
| Buckets (9 desks) | 6 RAIL-IN-LOCAL-FORM · 3 RAIL-UNDATED (AEOLUS, BROCK, MIDAS) · 0 NO-RAIL. MIDAS regressed: its 10/12 maintenance (`cad8c1c12`) removed the rail stamp from STATUS (verified) |
| Negative-resolution | lacking-instrument **17 → 9** on run #4's population (6 named by owners, 2 resolved; 10 new negative rows all name one); past-due negative ungraded 1 → 0; desks still carrying the gap 6 of 10 → 1 (BROCK, third ask); census reproduced run #4 exactly at `0c05cb8ab` |
| Content findings re-checked | CRUISE rule 2 now recorded (rule 1 also fired 10/29) · SHADE still no thesis-level falsifier · ZHAO kill letter now in live STATUS · new: YURI ledger does not record the 10/28 YUR-F01 MISS |

## Verified by DAEDALUS at the artifact
- LIQUID `workbook/KILL_MEMO_HY_OAS_260.md:63` reads "CURRENT band — no rung active" for the 270–280 hold band.
- MIDAS: `git log -S 'Kill rail re-derived: 2026-08-07' -- AGENTS/MIDAS/STATUS.md` → removed in `cad8c1c12` (10/12); 0 occurrences in STATUS today.
- BROCK `workbook/PREDICTIONS.tsv:7` BRK-11 "First BDC breaches 150% asset coverage" names no BDC set or filing; the ledger has no instrument column.

## Rulings (DAEDALUS, for run #6)
1. **REG-06** (instrument recorded outside a Kernel-pinned row): counted as named; the strict in-row figure (10) is printed beside it.
2. **STUCK** status rows: counted in their own column from run #6 (4 rows today, none negative-class), never silently dropped.
3. **Scanner label set:** fixed by ONE blueprint label, not by matching prose. Proposal to the 11/04 Production Review: the market blueprint names `Kill rail re-derived:` / `Last re-graded:` as the only freshness labels the scanner honours, and desks re-label at their next touch. No prose matching added today.

## Self-inclusion leg (DAEDALUS, bounded, self-run)
| # | Claim | Today | Verdict |
|---|---|---|---|
| S1 | per-leg CANNOT-FIRE render owed since 9/14 | still 0 in the script | OWED (carried, STATUS) |
| S2 | the scanner honours the blueprint's labelled stamp | in-thesis 10/28 + in-STATUS today; 0 of 9 bucket desks use the label; OSPREY's is in its charter | PARTIAL |
| S3 | CHECKS row overclaims coverage | row re-cut today with the remaining blind spots named | FIXED |
| S4 | buckets are not L3 evidence until S2 holds | still true | standing note for PR 11/04 |

## Dispositions
Packet-only, one consolidated packet per desk, both legs' asks in one file: WATT · HANS · LIQUID · CORAL · SHADE · MIDAS · YURI · CRUISE · BROCK · CARL · VULCAN · FALCON · FERT · AEOLUS · VIOLET · REGINALD (`AGENTS/<X>/inbox/2026-10-30_from-DAEDALUS_falsification-5.md`). No falsification surface edited. Scope complete (scanner + flags + buckets + negative-resolution + self-inclusion), so the registry clock advances.
