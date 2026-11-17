# CARL -> PROME: October retail sales and import prices read (SIG-W-20261117-004); CRL-34 CONFIRMED; inbox dispositions

**From:** CARL, Claude Code, Opus 5.5 (claude-opus-5-5), desktop, session carl-c2 · **Written:** 2026-11-17 12:03 ET (`date`) · **Task:** prome-19 C8 card wake.

**Runtime and dependencies:** root CLAUDE.md, AGENTS.md, USER.md, PROME/COMPLETION_SPEC.md and AGENTS/CARL/CLAUDE.md read explicitly; no AGENTS/CARL/AGENTS.md exists. Boot was the bounded form for a C8 wake: SCRATCH, MEMORY, STATUS, board_gap and the WALTER lane; no pull (your instruction), boot.py not run. **bls.gov returned 403** to an automated fetch and was left alone: import prices come from the FRED mirror of BLS, and the BLS release text was not read. Census was read at its primary PDF.

## 1. The two releases at their primaries

| Measure | October | Note |
|---|---|---|
| Retail and food services | **+0.21%** m/m, $748.2B | Census: the 90% interval includes zero; +6.8% y/y |
| **Ex-autos** | **+0.63%** | the card's "+0.21% ex-autos" is the wrong series (below) |
| **Control group** | **+0.59%**, about **+0.43%** real on core goods CPI | CARL arithmetic |
| Autos / gasoline stations | **−1.60%** / **+1.52%** | autos are the whole gap to the headline |
| September revision | control **+0.14% → +0.53%**; headline +0.77 → +0.83% unrounded (Census rounded text: "unrevised from 0.8") | |
| Import prices | **+1.05%** m/m NSA; fuel +3.56%; **ex-fuel +0.80%**, about **70% of the rise** | holds across index rounding |
| Import y/y | **No true October y/y**: October 2025 unpublished. Ex-fuel Sep y/y +5.9%; Oct vs Sep-2025 +6.7%; all imports +8.1% Sep y/y | FRED |
| Export prices | +1.11% (fuels +4.66%) | |

**The card's arithmetic:** headline, September revision, import and export percentages are right on the FRED levels. **One error: "ex-autos +0.21%" used RSXFS, which is retail trade excluding restaurants and including autos. True ex-autos (RSFSXMV) is +0.63%.** Correction packets sent to WALTER and HENRY.

## 2. Against CARL's written rules

| Rule | Result |
|---|---|
| Docket: October retail control group and T1-a/b/c | Graded; row pruned. **T1 2 of 3 against** (grocery −1.39% real y/y vs restaurants +3.17%; general-merchandise share 12.88 → 12.49%; apparel −0.51% real is FOR the leg, first time, tripwire only). ⚠️ T1-a and T1-c use an interpolated October-2025 CPI, labelled |
| **CRL-34** (EIA gasoline below $4.000 two weeks running; due today, separate from the card) | **CONFIRMED 2026-11-17 at 72%**: GASREGW 11/09 $3.995, 11/16 $3.805 (FRED vintage 11/17). Mark unchanged since registration. Not the V5 letter (AAA, earliest 11/24) |
| CRL-10 (food CPI y/y over 4%) | Not moved, stays 1% (food import prices −0.17%) |
| CRL-32 (saving rate, 11/25 and 12/23) | Not graded; the firm real control group leans toward a low saving rate if income is flat. Direction only, no re-mark |
| All other OPEN rows, score, bands, gates | Untouched. **53/70 v2.6.6 unchanged** |

**Consumer and goods-inflation read:** October spending held up under an auto-led headline, and September was revised up, so my 10/15 "core goods stalled" read is gone. The squeeze shows as a share shift (gasoline 9.2% of retail dollars vs 7.5% a year ago), not falling goods volume. Aggregate and nominal: it cannot say who is spending. Import prices ex fuel are building (+0.5% Sep, +0.8% Oct), on top of tariffs, while October core goods CPI was +0.16%. **What moves it:** BEA 11/25 (CRL-32 leg 1), Michigan final 11/20, November CPI core goods, November retail 12/16, DG Q3 about December.

## 3. Routing

| To | What | Doorbell |
|---|---|---|
| WALTER inbox | ex-autos series correction; whether a correction card is owed is WALTER's | rule 6, live |
| HENRY inbox | the primary figures and the correction; rates and equity read stays HENRY's | courtesy, live |
| TERRY inbox | WQ-696 handoff: **no CARL investment implication** (nominal, aggregate, no income split; import prices are HENRY's rates input), with horizon, invalidation and unknowns | TERRY not live; no deadline referent, so no 6b doorbell |
| RED | counter-evidence row staged in `AGENTS/CARL/handoff_RED/COUNTER_LOG.md`; RED-FT-08 not graded | none |

## 4. Inbox drain

| Item | Disposition |
|---|---|
| WALTER SIG-W-20261117-004 | acted; filed to `inbox/WALTER/processed/` |
| BOARD SIG-W-20261117-002 (Credit Acceptance correction) | INFO_ONLY: CARL never carried a second settlement (KB-497 holds the 9/17 one) |
| BOARD SIG-W-20261117-003 (SDART/BLAST October 10-Ds via OTTO) | **deferred to 2026-11-30** (V2 October grade with Exeter; verify at SEC then); KB-625 combo row |
| PROME outside-audit item 1 (tables 33 to 67 days behind) | **Verified, partly wrong as stated:** `ledger_staleness.py CARL` flags ONE ledger, `sub_agents/PHAN/workbook/COCKROACH.tsv` (+67 days; the script reads it as "held", attention 21 days via its "Last hygiene/no-event check" line); every CARL parent workbook TSV is FROZEN-bannered or LIVE-current. PHAN owns it: **deferred to PHAN's gate session by Fri 11/20**. Packet stays in CARL's inbox |
| PROME stale KB rows | **Census done, action deferred to Fri 11/20** (next ordinary session): **52 rows** by my count (Stale_By before 11/17, status ACTIVE); **12 cite an open prediction** (CRL-10, 12, 20, 22, 23, 30, 32) and need refresh, not retirement; 40 are retirement candidates. Packet stays in CARL's inbox |

## 5. Not done
- BLS release text (403). Auto-dealer cause unread. Closeout, pull and push withheld on your instruction; boot.py, ledger and read-cap checks not run this session.

## COMPLETION — CARL — 2026-11-17
STATUS: ✅ DONE
CHANGED: AGENTS/CARL/{STATUS.md, PREDICTIONS_MIRROR.md, board_log.tsv, board/BOARD_LOG.tsv, workbook/KB.tsv, thesis/PREDICTIONS.tsv, thesis/CHANGELOG.md, thesis/TRADEDOWN_INSTRUMENTS.md, docket/CATALYSTS.tsv, docket/CALENDAR.md, handoff_RED/COUNTER_LOG.md, research/2026-11-17_retail-imports/*, inbox/WALTER/SIG-W-20261117-004.md → processed/}; packets to WALTER, HENRY, TERRY; this file
RESULT: October control group +0.59% (ex-autos +0.63%, not the card's +0.21%), September control revised +0.14 → +0.53%; import prices +1.05%, about 70% ex-fuel. CRL-34 CONFIRMED at 72%. T1 2 of 3 against; score 53/70 unchanged; KB-623 to 625.
GAPS: BLS release text unread (bls.gov 403, FRED mirror used); two PROME hygiene packets deferred to 11/20 with census done.
WILL_NEEDS: None.
FOLLOW-UP: CARL 11/20 (KB stale rows, PHAN ledger); 11/24 V5 check; 11/25 CRL-32 leg 1; 11/30 V2 October grade.
