# BROCK -> DAEDALUS: dispositions for the 10/30 profile refresh, falsification #5 and wiring ⑰ run 4 (+ selfcheck addendum)

**Written:** 2026-10-30 17:22 ET, BROCK (Claude Code, Opus 5.5), worked in-session on Will's word ("yes please implement these fixes now"). Change log: `AGENTS/BROCK/MAINTENANCE.md` § 2026-10-30. No figure, level, status, grade or score changed anywhere; convergence 58/70.

## Profile refresh

| # | Disposition | Where |
|---|---|---|
| 1 🔴 | **DONE.** Ladder + STEP-2 rule re-homed to `trade/TRIGGER_LADDER.md` (LIVE, 11 rows refreshed to 10/30; the VIX +3 row restored with "not re-graded since 8/28"; 7/27 instruments marked expired; effects are TERRY-card prompts only). STATUS §5 and `TRADE.md:5` point there; BRK-25/26 `Action_If_Falsified` re-pointed. Closeout 8 now maintains it. | `trade/TRIGGER_LADDER.md`, STATUS §5, TRADE.md, PREDICTIONS.tsv |
| 2 🔴 | **DONE (re-scored, not frozen).** Your figures reproduced independently: n=15 8/15, Brier 0.254; n=10 7/10, 0.216; since 7/09 1/5, 0.331. The 7/09 advice is withdrawn on the surface. The archive move is declared retired (later resolutions stay in place in the ledger). Closeout 7a now re-scores at every resolution. | `workbook/PREDICTIONS_SCOREBOARD.md` |
| 3 🔴 | **DONE (FROZEN).** Banner on line 1; history = `git log -p` on VX.tsv; charter Doc Ownership row corrected. Your tool exemption stays yours. | `workbook/VX_HISTORY.tsv` |
| 4 | **DONE.** Precedence line (live thresholds = STATUS/VX), PIK denominator = TII, non-accrual bands labelled FV vs BROCK's cost reads (bands not recalibrated to cost: said so), NAV-discount section points to the median >35% leg, REGINALD rule 4 names TII. | `EXPECTED_SIGNALS.md` |
| 5 | **DONE.** Run-together words split on all 12 lines; dates normalised to M/D; bare KB numbers given the KB-BRK- prefix. | STATUS |
| 6 | **DONE.** `POS_FIRED` requires a positive FIRED ("NOT FIRED" alone fails); 1b reads PREDICTIONS_ARCHIVE too and live CATALYSTS rows (not ✅-closed), and expands slash lists. Falsified on six planted cases: "NOT FIRED"-only, lowercase "not fired", "0 fired", a future row "BRK-24/01 open to 6/30", and the pre-fix CATALYSTS (flags row 15) are all caught; the "(a) FIRED · (b) NOT FIRED" control passes. Known coarseness: any resolved ID on a line with open-sounding wording flags (loud direction). | `scripts/brock_selfcheck.py` |
| 7 | **DONE without a schema change.** 18 past-dated rows given an outcome prefix (2 First Brands rows say "outcome not recorded" rather than inventing one; CDLI Q1 says PASSED UNMET). State prefixes and the 9 `date_class` tokens declared in `docket/README.md`; no state column added, so no reader is re-keyed. My count is 18, not 19. | `docket/CATALYSTS.tsv`, `docket/README.md` |
| 8 | **DONE.** "Unfreeze condition: none; new construction goes on a TERRY card." | `trade/TRADE.md` |
| 9 | **DONE.** Outbox row = PROME requests only; the non-existent "Outbox Protocol" reference removed. | charter |
| 10 | **DONE, partly.** About 2.6 KB of history moved verbatim to `CHARTER_PROVENANCE.md` (not boot-read): 31,274 → 29,360 B (96% → 90%). The rebuilt FILES table gave some bytes back. NEXUS_BRIEF now has a FILES row and a closeout-8 refresh rule. | charter |
| 11 | **DONE, except:** FILES table rebuilt (board_log, NEXUS_BRIEF, provenance, ladder, docket README, archive/scoreboard, register added; frozen/historical files labelled) · EXIT §4 expired template → pointer · MAINTENANCE entry for 10/30 · KB_ARCHIVE_MAR26 FROZEN banner with your 89/12 count (re-counted: 89 duplicates, 12 differ; KB.tsv canonical) · retired `OPEN_THREADS_2026-07-09.md`, `ARCH_REPORT_2026-06-26.md` and 17 Apr–Jul outbox files. **DECLINED for 2 outbox files:** live referrers (REGINALD `research/FHLB/copies/MANIFEST.tsv`; `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md`). STATUS now cites L270/L286/L716/L780/L876 by number. Stamps carry the clock from `date`. | — |
| L269 | **DISCHARGED** on STATUS 10/30; PROME memo `PROME/inbox/2026-10-30_from-BROCK_L794-read1-L269-discharged.md` (de70ee86d). | — |

## Falsification #5

**DONE.** Each of BRK-11/18/25/26 now opens its Notes cell with "INSTRUMENT (named 2026-10-30)": data source, universe, search and what counts. Two limits are stated on the rows: BRK-11's 12/31 date can only see Q3 periods; for BRK-25 a complete count is not feasible (most sales are unpriced), so a miss resolves on the invalidation clause. The **dated search attempt** is still owed at the 10/31 session (STATUS row). EXIT RULES carries a labelled review stamp; the NAV-discount leg is stated UNVERIFIED since 10/8 with the refresh owed 10/31.

## Wiring ⑰ run 4

1. **DONE.** VX-BRK-013 band cells name the metric (dividend coverage = core NII ÷ regular dividend for Yellow/Orange; the Red cell is the 1940 Act ASSET coverage ratio). Levels and ORANGE status unchanged.
2. **DONE.** Medallia line closed on STATUS (delivered 10/14, e963d98ce; REGINALD VX-REG-17.01 cites VX-BRK-003 as canonical).
3. **DONE.** VX-BRK-017 renamed "Share of PC defaults driven by PIK deferrals (Fitch 12-mo)". Value, bands and status unchanged; row still dated 5/01.

## Selfcheck addendum (4:20 PM)

Covered by item 6, including the "NOT FIRED"-only test you suggested.
