# REGINALD retirement moves — 2026-11-06 18:36 ET

**Authority:** root Data Hygiene retirement rule, run at closeout. No new ruling. PROME relaying Will 18:33 ET asked for the desk's closeout.

**Test:** dated report before 2026-09-07, last commit over 60 days old, not boot-read, no reference from a live analytical or protocol doc. References checked fleet-wide by filename with `git grep`, 11/06 evening.

| Moved to `archive/reports_retired_2026-11-06/` | Last commit | References found | Note |
|---|---|---|---|
| 2026-07-18_ZION_monday_crossread_scaffold.md | 2026-07-18 | the two ZION files below, archives | print graded 7/20 |
| 2026-07-20_ZION_Q2_grade_STAGING.md | 2026-07-20 | ZION grade below, archived outbox | |
| 2026-07-20_ZION_Q2_grade.md | 2026-07-21 | processed inboxes, archives, BOND KB row | evidence kept; REG-29 uses Q3 and Q4, not this file |
| 2026-08-28_OBK_related-party_sizing_governance.md | 2026-08-28 | BOARD_LOG row, processed PROME packet | |
| 2026-08-28_SIG-W-005_five-failures-discriminator.md | 2026-08-28 | BOARD_LOG row, processed packets | |

**Not moved, 16 other reports dated before 2026-09-07:** each has a reference in my tree or a live vector. `2026-08-13_ccc-hy-escalation-standdown.md` had no filename reference but stays: its vector `VX-REG-18.04` is live in STATUS. The other 15 were not judged reference by reference, so this is a partial sweep.

**Known effect:** the BOARD_LOG rows, processed packets and archives that cite these paths now point at a moved file. Those are historical citations, which the root rule does not protect. Find the new home here.
