# BOND receipt — 2026-10-29 catch-up and owed work

Task: Will, 10/29: "boot up … get caught up on all new, relevant data to BOND files … work on any owed tasks for BOND." Runtime Claude Code, model `claude-opus-5-5`. Heavy closeout (tool built, charter row added). One read-only general-purpose helper (Opus) summarized the 25 inbox/correction files; every decision packet was then re-read at source by BOND.

| Item | Result | Evidence |
|---|---|---|
| TA_WS schema rename | REPAIRED: `monitors/ta_ws_schema.py`; grader and docket_check import it; docket_check rc 2 on dateless rows | KB-BND-501; selftests 6/6, grader PASS, docket 17/17, regression 18/18 |
| Auction grades | 20Y-R + 5Y TIPS REGISTERED CLEAN; 2Y + 5Y AUDIT ONLY (2Y I′ fire); 7Y pre-print not registrable | KB-BND-502/504/505/506; `analysis/2026-10-29_catchup/grade_*.txt` |
| BND-32 | RESOLVED FALSE (+10.00bp) | KB-BND-507; thesis/PREDICTIONS.tsv |
| Data refresh | Treasury 10/28, ICE 10/27, repo 10/27, FR2004 10/14, ACM 10/27, Bund 10/28, PMMS 10/22 | `analysis/2026-10-29_catchup/raw/manifest.json`, `derived.json`; KB-BND-508–513 |
| F2 carrier | 10/27 op OFF-THE-RUN, routed to RED; ledger row | KB-BND-503; registry/f2_reads.tsv |
| Vectors | VX-04 2→3, VX-07 1→2, VX-17 1→2; 15 states refreshed; composite 17→19 | workbook/VX.tsv; STATUS |
| KB hygiene | 17 rows added (501–517); 29 overdue ACTIVE rows dispositioned (14 SUPERSEDED, 4 CONFIRMED, 11 STALE) | kb_lint conformant |
| Corrections | COR-20261021-02 APPLIED (KB-514), COR-20261022-14 NO-OP | registry/corrections_receipts.tsv; check rc 0 |
| Inbox | 14 WALTER (14 board_log rows) + 9 peer packets → processed | board_log.tsv; KB-BND-515 |
| Owed answers | RED FT-11 precedence ruled; CYPHER boundary confirmed + amendment | RED/CYPHER inbox packets |
| Docket | 7Y by CUSIP; 20Y 11/18 + 10Y TIPS 11/19 added; refunding freeze row 11/5; 4 completed rotated | docket/CATALYSTS.tsv; domain/sources/2026-10-29_completed-catalysts.tsv |
| Packets out | RED ×2, CYPHER, LIQUID, HENRY, PROME | carve-out ① commits |

Not done: VX-BND-20 review (rescheduled 11/11), CDX proxy run, new prediction. Clock: stamps before 06:04 EDT UNVERIFIED (KB-BND-517).
