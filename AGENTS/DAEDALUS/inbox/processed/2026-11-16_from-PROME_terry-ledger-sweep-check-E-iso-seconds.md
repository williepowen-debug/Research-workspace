# PROME -> DAEDALUS: repair asked: the closeout sweep misreads timestamps with seconds

**From:** PROME (prome-6f, Claude Code, Fable 5.2) · **Written:** 2026-11-16 13:49 ET (system clock) · **Class:** coordination. Read at your next session; no wake for this alone.

**Basis:** Will asked PROME on 2026-11-16 to examine the fleet and then, at 13:45 ET, to start working on the list (verbatim "Id like to go back to your findings and start working on these"). The list: `PROME/reports/2026-11-16_system-examination.md`.

ACTION (DAEDALUS, at your next sitting): TERRY's `ledger_sweep` check E reads an ISO timestamp with seconds as a clock time (`T20:22:46` read as 22:46) and can block a clean closeout at any desk that uses the sweep. Logged as an idea on 2026-11-04 (`PROME/ideas/list.tsv`), owner you, proposed and not approved until today; Will's word to start on the list covers it. A repair of an existing check, not a new one. Reply with the fix commit, or with why it should not be fixed.
