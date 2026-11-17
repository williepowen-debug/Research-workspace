# Outside read-only audit of 2026-11-16: PROME's items and what was done with each

**Written:** 2026-11-16 23:0x ET by PROME (session prome-d2, laptop).
**Source:** an outside read-only audit Will pasted into PROME's chat at 22:18 ET ("Okay lets look at this next"), and the auditor's reply to PROME's sorting, which Will pasted at 22:54 ET under his one word "response:". The audit's opening instruction: each desk verifies the item against its own files first, fixes it, and reports what it changed or why it disagrees; items marked ASK ME go to Will as queue rows.
**Status of authority:** the auditor's reply recommends "go on its steps 1 to 3". That is the auditor's recommendation, relayed by Will; it is not Will's own word. PROME acted only on what is already inside its authority (its own tools, packets to owners). Anything that needs Will's own word is marked NEEDS WILL below.

## PROME's sixteen items, verbatim, with disposition

| # | The audit's words | Disposition 2026-11-16 |
|---|---|---|
| 1 | Rulings follow-through: William's 10/14 SELL rulings on the OZK and WAL puts were never executed (OZK expires Fri 11/20). The approved HYG hedge has no order. Re-raise both now. Then add a check that every ruling ends in an executed order or a logged reason. | First half NOT DONE by rule: `USER.md` § No expiry nagging (no sell-or-roll prompts; the HYG order is Will's hand). PROME cannot confirm "never executed": the mirror is his 11/10 captures. The auditor withdrew the ask to PROME and put it to Will directly in its reply. Second half: APPROVED tonight as WQ-701 B, not built (DOCKET row dated 2026-11-24). |
| 2 | The broker mirror lists 14 bank and credit put lines with no owner, card or approval. Assign an owner to each or flag it. ASK ME where unclear. | NEEDS WILL (a queue row). Not registered tonight: see § Open with Will. The lines are not yet identified one by one at `FORGE/STATUS.md`; its D-77 row already records "no contract-specific card" for several. |
| 3 | Scoring script: the timing check discards dates earlier than the call date, so it cannot catch calls logged after the outcome. Fix it. | PROME's tool (`PROME/tools/forecast_report.py`). NOT DONE tonight; NOT VERIFIED at the code. Repair row below. |
| 4 | Scoring script: it does not read BOND's archive files, so 23 scorable calls are missing from every report. Make it read them. | PLAUSIBLE: BOND keeps four `thesis/archive/PREDICTIONS_resolved_*.tsv` files; the scorer's file list does not name them. NOT DONE tonight. Repair row below; BOND told by packet. |
| 5 | Report the fleet score at first-logged probability next to the current score. First-logged shows about +0.004, no edge. Most of the reported gain comes from revisions within 30 days of the outcome. | Forward form only, per the auditor's reply: forecast report 2 carries the first-logged score beside the current score. Goes in the repair row. Report 1 is NOT reopened (Will's 11/5 stop). The +0.004 figure is the auditor's, not checked. |
| 6 | 11 scored calls have no record from before their outcome. List them and exclude or re-rule each. | HELD. Historical reconstruction of report 1 is stopped by Will (11/5). The auditor's reply does not ask to reopen it. |
| 7 | Commit the samples behind the two blind-read tables in forecast report 1, or mark those tables unverifiable. | HELD, same stop. |
| 8 | spawn_slate.py line 12 still says "cost against the cap". Update it. | DONE: the docstring now says slate order, no count cap since WQ-667 B. No behaviour change. |
| 9 | Define "blanket launch word" in PROME/CLAUDE.md, Ask First. ASK ME whether "start working on these" counts, and whether a blanket word may pull rows forward (WQ-661 says due rows only, 11/8 did otherwise). | NEEDS WILL (a queue row, and an edit to PROME's charter). Not registered tonight: see § Open with Will. The 11/8 claim is not checked. |
| 10 | Record the pre-launch desk listing in a file so it can be audited. | PROME's own practice. NOT DONE tonight; in the repair row (the listing goes into the ORCH_LOG trigger cell or a dated file, no new tool). |
| 11 | 6,064 inbox packets are past the repo's own 60-day archive rule. Archive them. | DROPPED, the auditor agrees. The 60-day rule covers research and source files. Of about 3,516 tracked packets dated before 2026-09-17, 3,510 are already under `processed/`, and open rows cite those paths. |
| 12 | 2,379 knowledge-base entries are past their stale-by date and still marked active. Retire or refresh them. | HELD for Will's word. The entries are the desks' own files. Count not checked. |
| 13 | The weekly consistency check found 28 rule contradictions on 11/7, up from 4 on 8/29. Resolve them, and propose a rule for which instruction wins in a conflict. ASK ME to approve it. | Contradictions: spine audit 19's 28 blocking items were fixed in that audit (`PROME/STATUS.md` stamp); audit 20 found 9, fixed. Precedence rule: Will left it out of WQ-701 tonight (item F, not approved). HELD. |
| 14 | 167 scripts across 28 desks present themselves as a web browser and no fleet rule covers it. ASK ME for one rule. | DONE as a rule: root `CLAUDE.md` § Data Hygiene, Blocked sites (WQ-701 G, Will 22:07 ET). No sweep of the scripts. |
| 15 | Add a list of the packages the tests need. 78 test files fail on a fresh install because one package is missing. | CONSISTENT with what PROME saw tonight: `pytest` is not installed in `.venv` or system Python on the laptop. NOT DONE; in the repair row. |
| 16 | Postmortems never grade the thesis and two of eight lack a close price. Assign who grades the thesis and fill the missing prices. | HELD for Will's word. The auditor's reply ranks it first among the held items. TERRY owns postmortems (`AGENTS.md`); who grades the THESIS is a seat question, Will's. |

## Desk items

Twenty desks each got one packet, `AGENTS/<DESK>/inbox/2026-11-16_from-PROME_outside-audit-items-verify-first.md`, with the audit's words verbatim, verify first, at the next ordinary session, no wake for it alone: LIQUID, TERRY, HAWK, BRENT, OTTO, YURI (as the likely owner of YUR-005), MARCO, BOND, HENRY, RED, REGINALD, FLG, WATT, CORAL, GIBBS, HOMER, CARL, SAM, HANS, VIOLET. DAEDALUS's item was settled by WQ-701 A2 the same evening (its own packet).

**LIQUID, the most pressing (the auditor's reply):** PROME ran `AGENTS/LIQUID/scripts/test_alert_srf_repair.py` read-only at 22:55 ET: 20 tests, 8 failures and 2 errors, all in `WatcherConsumerTests`, all on the re-kill side (the sub-260 count for `GATE-HY-REKILL`); `hy_oas_watch.py --selftest` passes. Whether the watcher or the tests are wrong is LIQUID's to say. PROME's unverified inference: readings since 11/10 were 320 to 330, far from 260, so a missed or false signal is unlikely. The audit says 10 of 25; PROME's run shows 10 of 20.

**TERRY, must-fix (the auditor's reply):** `AGENTS/TERRY/research/2026-11-06_coupling-test/gas_test.py` line 4 writes `data/gas_closes.csv` at import (verified). The file was intact at 22:20 ET (6,343 lines, unmodified in git).

**Not assigned, held for Will's word:** the research-balance items (CORAL's second item; AEOLUS, WATT and ORACLE's shared item). AEOLUS and ORACLE therefore got no packet.

## Open with Will

1. His own word on whether the 17:51 ET limit on new decision rows covers this audit. If it does not, PROME registers two rows: owners for the unowned put lines (item 2) and the meaning of a blanket launch word (item 9).
2. Whether to take up postmortem thesis grading (item 16), the stale knowledge-base entries (item 12) or the research-balance items.

## Update 2026-11-16 23:2x ET — Will took up the held items

- **23:04 ET**, verbatim "I will okay it. we can do new/more": his 17:51 ET limit does not cover this audit. Items 2 and 9 became WQ-702 and WQ-703, both RULED A at 23:09 ET (`PROME/proposals/2026-11-16_wq702-703-RULED.md`; WQ-703's charter text was WITHHELD after three reads and the charter is unchanged).
- **23:16 ET**, verbatim "yes lets do this", quoting PROME's line naming postmortem thesis grading, the stale knowledge-base entries and the research-balance items.
  - Item 16: packet to TERRY, `AGENTS/TERRY/inbox/2026-11-16_from-PROME_postmortems-thesis-grades-and-missing-close-prices.md`.
  - Item 12: packets to 22 desks, `AGENTS/<DESK>/inbox/2026-11-16_from-PROME_stale-KB-rows-retire-or-refresh.md`, with PROME's per-desk counts (1,673 rows in total on PROME's definition).
  - Research balance: a list of proposed commissions was shown to Will; nothing is commissioned until he says yes to it.
- Follow-through: the DOCKET row dated 2026-11-24 that names these three.
