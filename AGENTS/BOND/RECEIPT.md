# BOND receipt — 2026-11-12 PROME prome-e8 wake (30Y grade, 11/10 and 11/12 closes, VX-BND-17, FR2004, inbox drain)

Task: PROME prome-e8 due-row wake (WQ-184 C6). Runtime Claude Code, model `claude-opus-5-5`, Linux/WSL desktop. Tools: bash, repo-root `.venv` python, background polls, SendMessage. Failed to connect: mtnewswire, Definite. Not called: Quartr.

| Item | Result | Evidence |
|---|---|---|
| Boot | explicit reads done; docket_check rc=0 after one timeout; boot_recompute rc=1 (T5YIFR distance fixed; VX-17 watcher GAP) | boot outputs |
| 30Y `912810UY2` | REGISTERED CLEAN: indirect 68.11 vs I′ 63.89; dealer 11.39; BTC 2.36; counter 0 → 1 | KB-BND-569; `analysis/2026-11-12_30y/grade_912810UY2.txt` |
| BND-33 | 30Y leg recorded, not regraded; TRUE stands | `thesis/PREDICTIONS.tsv` |
| Yen context | attribution limits stated; no Japan inference | KB-BND-571 |
| Treasury closes | 11/10 (KB-BND-570, curve cells superseded) and 11/12 (KB-BND-573): 10Y 5.10, 30Y 5.43 | Treasury par/real CSVs |
| VX-BND-17 | 2 → 1, 201bp same-date, PROME class C10 | VX.tsv; KB-BND-573 |
| FR2004 as-of 11/4 | long end $150.760B (+3.814); VX-BND-04 held 2 | KB-BND-574 |
| Inbox | 4 packets processed; WQ-671 applied (KB-BND-572); WQ-678 A14 applied, M52–M65 deferred | `inbox/processed/` |
| WALTER lane | 11/11-011, -015; 11/12-005, -007, -008 | board_log; `inbox/WALTER/processed/` |
| Packets | two to PROME (753a23b0dd, 9bdd57186c), both consumed | `PROME/inbox/processed/` |

Pending: 20Y and 10Y TIPS bars by 11/17; VX-BND-20 11/11 review. Details → SCRATCH NEXT.
