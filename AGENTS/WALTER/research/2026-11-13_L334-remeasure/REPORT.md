# D:L334, WQ-556 C two-week remeasurement of lever (a)

Owner WALTER (walter-d4, Claude Code, Opus 5.5). Due November 13, delivered November 13. Script `remeasure.py`, output `results.json`; data `routed/delivery_log.tsv` and `routed/route_log.tsv` as of commit 6ea651a830.

**Result: lever (a) did not measurably lower INFO copies to three of the four desks. Copies per signal rose at HENRY, LIQUID and SAM and fell only at REGINALD. No trimmed desk later had to be sent a copy (0 late adds in either window), so there is no sign the trims cost anything, and also little sign they happened at scale.**

Windows: BEFORE October 16 to 29 (14 days, 397 signals), AFTER October 30 to November 12 (14 days, 328 signals; lever in force from the October 30 dispatch).

| Desk | INFO rows before → after | INFO copies per 100 signals | ACTION rows | Late adds | Strict / broad citation, first 7 days of window |
|---|---|---|---|---|---|
| HENRY | 111 → 101 | **28.0 → 30.8** | 28 → 25 | 0 / 0 | 0 of 53, 1 of 53 → 5 of 37, 5 of 37 |
| LIQUID | 108 → 99 | **27.2 → 30.2** | 37 → 20 | 0 / 0 | 0, 7 of 56 → 0, 5 of 57 |
| REGINALD | 96 → 66 | **24.2 → 20.1** | 23 → 12 | 0 / 0 | 1, 5 of 34 → 0, 0 of 43 |
| SAM | 44 → 54 | **11.1 → 16.5** | 8 → 8 | 0 / 0 | 0, 0 of 23 → 0, 0 of 12 |
| All four | 359 → 320 (−11%) | 0.90 → 0.98 per signal | 96 → 65 | 0 | — |

Raw INFO rows fell 11%, but signals fell 17%, so the per-signal rate went up. The raw drop is volume, not the lever.

Why the lever barely moved: it trims only discretionary copies. Most INFO copies to these four desks are default routes in ROUTING_TABLE (HENRY is secondary or INFO on most macro, AI and credit clusters; LIQUID on funding and credit), which WQ-556 C left untouched by design. The dispatch notes record "no optional HENRY/LIQUID/REGINALD/SAM copies added" as a self-attestation. They do not count what was trimmed, so the trimmed volume cannot be read from the record. The flat rate says it was small.

Limits:
- The cluster mix differs between windows (AFTER carries the Nvidia CEO exit, Iran/Houthi claims and the 10-year above 5%), and those clusters route to HENRY and LIQUID by default. A mix shift alone can raise the per-signal rate.
- Citation is a lower bound, and the AFTER cite window has had 7 to 14 days to be cited against 21 to 28 for BEFORE. The counts are too small to compare (largest cell 7).
- Late adds measure only copies WALTER itself added later. A desk that needed a trimmed item and found it on BOARD leaves no trace.
- Self-report: this session sent source-confirmation INFO copies to HENRY (SIG-W-20261113-001) and LIQUID (-002). Both desks were the sources and both copies follow prior practice. They are discretionary under a strict reading of lever (a).

Recommendation: no change WALTER can make. Lever (a) can continue at no measured cost, but it is not reducing the copy count. A real reduction lives in the default routes (a ROUTING_TABLE change, Rule 8, Will proposal) or in levers (b) and (c), which Will did not approve. WALTER does not propose either here; it reports the number. The predictive leg (November 5 REPORT, no bar) and this remeasurement close WALTER's two deliverables on the row.
