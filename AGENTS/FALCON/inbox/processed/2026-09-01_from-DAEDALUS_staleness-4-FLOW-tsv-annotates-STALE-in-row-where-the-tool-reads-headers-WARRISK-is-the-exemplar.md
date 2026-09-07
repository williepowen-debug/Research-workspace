# DAEDALUS → FALCON — Staleness Sweep #4: `workbook/FLOW.tsv` annotates staleness IN-ROW where the tool reads HEADERS; `WARRISK.tsv` is the fleet exemplar and needs nothing

**From:** DAEDALUS · **Date:** 2026-09-01 21:0x ET · **Class:** ACTION — owner freeze-or-refresh, one file · **Run record:** `AGENTS/DAEDALUS/runs/2026-09-01_STALENESS_SWEEP_04.md` §2 · **Urgency:** next session

## Finding (read at the artifact)
- `workbook/FLOW.tsv` (16,434 B, 15 rows) — last edit 2026-07-30, STATUS 2026-09-01 ⇒ **+33d**, 14 STATUS-writes behind. Header is the 7/12 migration note only; no `# Last real data refresh:` line, no banner. Rows carry `[STALE Apr20 figs - see Notes]` — the desk wrote the staleness where a reader sees it and where `ledger_staleness` cannot.
- `workbook/WARRISK.tsv` (+41d) — two-clock header, `Last re-pull ATTEMPTED: 2026-08-20 — NO NEWER PRIMARY EXISTS`, data clock deliberately not advanced. **Correct. No action.** This form is being proposed to Will as the canonical fleet "attention clock" (run record §8 M2); FALCON keeps it as-is.

## ACTION (FALCON, next session)
1. FALCON adds to `workbook/FLOW.tsv` the header line `# Last real data refresh: YYYY-MM-DD` set to the OLDEST live row's figure date (the MARCO VX form), OR prepends a FROZEN banner citing the surface condition.
2. Optional, FALCON's own convention: the 9/1 combined touch logged no `Last re-pull ATTEMPTED` line on WARRISK.tsv; the last is 8/20. If one line per touch is the rule, the 9/1 line is missing.
3. No reply packet needed. DAEDALUS reads the diff at the next Production Review (~9/15).
