## COMPLETION — REGINALD — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/scripts/{8k_monitor,insider,earnings_countdown,vx_ladder_check,boot}.py, AGENTS/REGINALD/scripts/settled_bars.py (new), AGENTS/REGINALD/reports/2026-10-09_Q3_earnings_read_plan.md (new), AGENTS/REGINALD/reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md (Amendment A3), CALENDAR.md, STATUS.md, MEMORY.md, ROADMAP.md, SCRATCH.md, POSITIONS.md, NEXUS_BRIEF.md, board/BOARD_LOG.tsv, archive/{STATUS,MEMORY}_rotation_2026-10-09.md
RESULT:
- **Monitor repair (Will-directed, bounded):**
  - OZK's filing checks moved from the SEC (no filings since 2017) to the FDIC, reusing the OZK desk's `flng_watch`.
  - VLY was keyed to OLD REPUBLIC's SEC CIK (74260 → 714310).
  - FLG / AMTB / CFG / CUBI added.
  - Failed, unparseable or uncovered banks now return no verdict, never an all-clear (tested with the network blocked).
  - The countdown reads a CALENDAR table, and unsettled or NaN daily bars are excluded from settled grades.
- **Q3 read plan written on the existing frozen frames:**
  - Provisional cross-bank judgment: CONCENTRATED on 6/30 evidence.
  - Total-CRE bad-loan rate 2.23%. The multifamily sub-read rose 3.23 → 3.58% in Q2, all at FLG / EGBN / CFG, which is individual-bank, not spread.
- **Will's clarifications (21:33 ET):**
  - Individual-bank deterioration ≠ cross-bank spread.
  - L180 is graded on the ORIGINAL total-CRE basis, with multifamily as a separate sub-read.
  - Missing banks → UNKNOWN wherever they could flip a breadth verdict.
  - 11/07 is the planned Call Report retrieval, with completeness checked then.
GAPS: CUBI and FLG Q3 dates NOT ANNOUNCED (searched 10/9 21:2x ET; estimates in the CALENDAR table). The WAL 10/9 exit row is not graded, because the settled bars were not posted at 20:3x ET; it is owed next session. The FRED cache-busted CSV route failed tonight; the API route was used.
WILL_NEEDS: FFIEC CDR JWT regeneration before **11/05** (WILL_QUEUE row 31). The L180 breadth verdict needs the 11/07 Call Report retrieval. Optional: "new foreclosure build" in L180 is unquantified, and the literal reading (any QoQ rise) already counts WAL at Q2 (+2.3%). A materiality floor would be his rule.
FOLLOW-UP:
- **(1) PROME, please annotate DOCKET L180** with Will's 10/9 restatement. Its "IF INSUFFICIENT: record which banks… and grade the rest" is superseded wherever the missing banks could change the ≥3-of-5 verdict:
  - *c* ≥ 3 → BROADER · *c* + *m* < 3 → NOT BROADER · else UNKNOWN.
  - Basis: total-CRE bad-loan RATE (nonaccrual + 90+ over construction + MF + NOO, Call Report) + `oreo_total_k`. Multifamily is a separate sub-read, not counted.
  - 11/07 = planned retrieval with completeness checked then.
  - Plan of record: `AGENTS/REGINALD/reports/2026-10-09_Q3_earnings_read_plan.md` §2.0.
- **(2) The earnings reads proceed on the existing schedule:** CFG Fri 10/16 first.

**WQ-249 closeout receipt:** REGINALD session 2026-10-09 evening (Will-launched, Opus 5.5) CLOSED OUT. Commits are path-scoped and pushed via `safe-push.sh`; the receipt line is in the closeout message.
