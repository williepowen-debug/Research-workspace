# G:GATE-BRENT-COT-35B (REGISTRY COT-FUEL-35B), vintage #14 as-of 2026-11-10: NOT GRADEABLE on 2026-11-13

Written 2026-11-13 ~16:25 EST (from `date`).

## Result

| Check | Read |
|---|---|
| `cot_grade.py --expect 2026-11-10` | rc 3, NOT FRESH: newest report date in the row is 2026-11-03, DO NOT GRADE. Retried every 2 minutes from 15:31 EST; last run 16:22:28 EST (`grade_run.txt`). Re-issue watch: the live 11/3 row matches the ledger (shorts 125,654, open interest 1,908,732). |
| Second, independent raw pull | `curl` of cftc.gov/dea/newcot/f_disagg.txt 16:22 EST, http 200, 455,984 bytes: WTI-PHYSICAL row report date 2026-11-03. Agrees. |
| Why | CFTC 2026 release schedule (cftc.gov ReleaseSchedule, read 16:23 EST, saved `cftc_release_schedule_2026-11-13.html`): November **06, 16\*, 20, 30\***, \* = delayed release because of a federal holiday. Veterans Day (Wed 11/11) moves the as-of 11/10 report to **Monday 11/16, 15:30 ET**. |

**Leg A and Leg B, by the row's own letter:** neither leg can be graded. The resolving vintage is "the first print carrying the as-of report_date" and no print carrying 2026-11-10 exists. The REVERT rule ("re-read every print, never a latch") has nothing new to re-read. **The row's standing state stays vintage #13 (as-of 11/3), JOINT NOT-SPENT, seventh consecutive:** Leg A 125,654 shorts ≥ 118,326 NOT-SPENT; Leg B 6.5831% > 4.909% NOT-SPENT. No level, band or threshold set or changed.

**Recommended review_by: 2026-11-16** (Monday release, ~15:30 ET; grade with `--expect 2026-11-10`). Then #15 as-of 11/17 on Fri 11/20, and #16 as-of 11/24 on **Mon 11/30** (Thanksgiving delay, same schedule).

## The miss, classified

My own forward calendar (`docket/CATALYSTS.tsv`), SCRATCH and NEXUS_BRIEF all dated #14 to Friday 11/13, and so did the GATES row's review_by. The CFTC publishes the delay in advance; nobody read the schedule. Consequence: none (the grader refused on its letter; no grade was fabricated). Fixed in the CATALYSTS row (re-dated 11/16, with the 11/30 delay noted). No new check added.

## Earlier Friday grade under another name

Yes. The last grade is **#13, as-of 11/3, graded live 2026-11-06 15:34 EST**, commit `b5fdbb37e3` "BRENT: COT #13 NOT-SPENT, BRT-33 first session no observation, closeout". The subject named the vintage, not the row key. PROME consumed it 2026-11-07 (the row's consumed_by cell). There has been no CFTC release from 11/7 to now, so no grade was owed in that span; none is missing.
