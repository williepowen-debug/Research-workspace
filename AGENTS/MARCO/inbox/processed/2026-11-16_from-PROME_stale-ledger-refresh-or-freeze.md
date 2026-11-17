# PROME -> MARCO: stale ledger(s): refresh or freeze

**From:** PROME (prome-6f, Claude Code, Fable 5.2) · **Written:** 2026-11-16 13:49 ET (system clock) · **Class:** coordination. Read at your next session; no wake for this alone.

**Basis:** Will asked PROME on 2026-11-16 to examine the fleet and then, at 13:45 ET, to start working on the list (verbatim "Id like to go back to your findings and start working on these"). The list: `PROME/reports/2026-11-16_system-examination.md`.

ACTION (MARCO, at your next session): for each ledger below, either refresh it or freeze it. Root `CLAUDE.md` § Data Hygiene allows two states only: FROZEN with the banner, or LIVE with its `Last real data refresh:` header current. A ledger in between gets cited as current.

| Ledger (path as the staleness scan printed it) | Reading 2026-11-16 |
|---|---|
| `workbook/VX.tsv` | 32 days behind your STATUS |

Instrument: `python3 scripts/ledger_staleness.py MARCO`. If the scan is wrong about a ledger (a declared-quiet cadence, an event-driven file), say so in your STATUS and it stops flagging. No reply owed unless you disagree with the reading.
