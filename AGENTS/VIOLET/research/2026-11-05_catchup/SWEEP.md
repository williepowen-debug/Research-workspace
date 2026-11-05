# VIOLET file sweep: stale, incomplete and owed items

**Run:** 2026-11-05 10:03 ET, on Will's request. Scope: every top-level desk file, thesis, workbook ledgers, outbox, inbox lifecycle, research retirement and open DOCKET rows.

## Fixed in this sweep

| Item | Fix |
|---|---|
| HY basis error, written by this session at 09:5x ET | STATUS, NEXUS_BRIEF, GRADE and both pages said +24bp from 10/13. Correct: +72bp from 268bp [9/22], peak +76bp. Conclusion unchanged, still under 100bp. KB-VIO-371. |
| NVIDIA results 11/17 missing from the calendar | Added HIGH. Evening before the 11/18 VIX AM SOQ. Same class as KB-VIO-324. |
| Credit-vol endpoint 11/17 had no calendar row | Added MEDIUM. |
| VX_TERM_HISTORY three months stale, needed by L441 on 12/16 | Rebuilt through 11/04: 536 rows added, 0 existing rows changed. |
| TRADE.md header named the October 14 mirror | Now the October 30 capture. Review stamp scoped to the header. |
| 7 outbox packets sat in the not-delivered lane | Moved to delivered/, recipient copy found for each. |
| 7 ACTIVE KB rows overtaken by later rows | Closed STALE with disposition. KB-VIO-328 Stale_By moved to the endpoint. |
| Path A F2 audit missing from the STATUS queue | Added. Not run. |
| Month-number glue | Fixed in CALENDAR, MEMORY, CANARY_MAP, thesis, CHANGELOG. |

## Open: needs Will

1. **Path A F2 audit, owed since 8/27.** The pre/post-2018 test of Path A's ~70% hit rate. Not commissioned. If the sample is too thin, the result is no gate, never waived (KB-VIO-217).
2. **MOVE pause/resume line.** Its parent is the rising-vol registration design and GATE-VIO-RV1 is retired, yet the line still reads ARMED. It looks orphaned. Not verified that the commission is dead. Retiring a registered line is a gate change.
3. **Desk CLAUDE.md conflicts (edit needs Will's word).** The MAIL paragraph forbids inbox work on normal spawns while step 5a and practice drain it, and it cites HERMES; steps 5b and 5a are out of order; "Position sizing → FORGE" conflicts with root TERRY ownership.

## Open: lower priority, no decision needed yet

- **PREDICTIONS.tsv:** all 6 rows terminal, so VIOLET has no open registered prediction and the staleness alert cannot clear. A banner waits on DOCKET TSV stamp row (DAEDALUS/PROME).
- **VX_M1_HISTORY.tsv:** ended 7/29, no script reads it. Candidate to freeze.
- **Research retirement:** 14 entries past 60 days, unreferenced by live desk docs, DOCKET or GATES. Not moved: KB rows may cite these paths, and the 8/27 F2 split is evidence for the Path A question.
- **1 outbox packet with no delivery proof:** 2026-08-27 GATE-VIO-RV1 transcription verified clean. RV1 is retired, so low value.
- **29 ACTIVE KB rows past Stale_By:** mostly durable method rows with short dates. The validator treats this as ageing, not review owed.
- **board_log history gaps:** 3 WALTER and 5 root packets since 9/20 have no row. Not reconstructed.
- **FLOW.tsv:** last row 10/19. The file is scoped to formal sends, so this may be correct.
- **Other glued text:** word-number gluing beyond month names remains in older KB and FLOW rows.
- **Review stamps:** README 10/19; CANARY_MAP 10/14, monthly sweep due about 11/14.
- **implied_corr.py:** stamps SETTLE by clock. Rows repaired, tool fix not commissioned.
