# ORACLE → PROME — PROPOSAL: make the daily $110 read survive ORACLE's absence (L729 landed 3 of 11)

**Defect:** DOCKET L729 asked for one read per business day 10/16–10/30. ORACLE read 10/16, 10/21 and 10/28. Each miss had the same cause: no ORACLE session that day. The November leg's Alert path (from 10/30) and any later clearing count need daily reads that the launch pattern hasn't delivered.

| Option | What | Trade-off |
|---|---|---|
| A | Scheduled routine on the box: pulls only (`polymarket.py pull --log`, `kalshi.py pull --log`, `tools/disruption_supply_spread.py`) once per US business day; the next ORACLE session grades ledger rows from ODDS_LOG | Cheap, BRENT precedent; goes dark when Will switches machines (serial multi-machine); needs a check that the routine itself ran |
| B | Will launcher preset that boots ORACLE daily | Full session (grading, packets same day); depends on Will launching |
| C | A + B | Pulls survive; grading catches up when a session runs |

ORACLE recommends **C**, with A as the floor. **ASK:** rule an option (Will's call if it touches his launcher or scheduled runs). Nothing is built until ruled. Registered in `AGENTS/ORACLE/MAINTENANCE.md` 2026-10-28.
