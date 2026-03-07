# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-07 22:30 UTC

---

## Last Session: Agent Infrastructure Standardization (Sat Mar 7 evening)

Compared file structures across BRENT, REGINALD, LABOR, HENRY. Found inconsistencies and started fixing them sprint-by-sprint.

### Completed Sprints:
- **Sprint 1 ✅:** Mail system — REGINALD + HENRY migrated from INBOX.md → mail/inbox/ folders
- **Sprint 2 ✅:** TSV locations — REGINALD PREDICTIONS.tsv + HENRY PREDICTIONS.tsv/ML.tsv moved to workbook/
- **Sprint 3a ✅:** LABOR ML.tsv renamed to KB.tsv (was already functioning as knowledge base)
- **HENRY CLAUDE.md:** Fixed stale "TRADE.md is deprecated" note

### Next Sprint (start fresh session):
- **Sprint 3b:** BRENT KB.tsv migration to new 9-column schema (easiest — 6→9, 103 rows)
- **Sprint 3c:** LABOR KB.tsv migration (11→9, 82 rows)
- **Sprint 3d:** HENRY KB.tsv migration (15→9, 89 rows)
- **Sprint 3e:** REGINALD KB.tsv migration (15→9, 116 rows — hardest)
- **Sprint 3f:** Update all 4 CLAUDE.md with new schema definition

### New 9-Column KB Schema (AGREED):
```
ID | Date | Group | Entity | Fact | Source | Status | Vectors | Notes
```
- Group = topic/thread tag (SULPHUR, TAIWAN, HIDDEN_CRE, HORMUZ, etc.) — add blank, backfill later
- Fact = merge of old Description+Analysis+Data_Quote into one good sentence
- Vectors = old Vector_Links renamed
- Notes = catch-all absorbing old Confidence, Thesis_Impact, Cross_Links
- Session column dropped (useless to LLMs)
- Category absorbed into Group

### Migration approach per agent:
1. Read current KB.tsv fully
2. Python script maps old columns → new columns
3. Run, output to new file
4. Spot-check (first 5, last 5, random middle)
5. Replace old file, commit

### NEXUS spawned (may have completed):
Spawned NEXUS for full synthesis across BRENT/REGINALD/HENRY/LABOR TRADE.md files. Check for completed output.

---

## Still Queued (from earlier today):
1. **SSB trim 50%** — first trading day (Monday)
2. **HERMES delivery run** — critically backlogged
3. **Monday live data pulls** — see BRIEFING.md for full list (12 items)
4. **WAL position confirm** — $85P Jun open or closed?
5. **Prompts C & D** — fertilizer chain + SPR/transformers not yet run
6. **TRADE.md rollout** — BROCK, CARL, HAWK
7. **HERMES cron automation**
8. **LABOR still needs:** LESSONS.md + domain/ folder migration (Sprint 3 remainder)
9. **Sprint 4:** REGINALD sub-agent audit (BELT/CORAL/CREED/RENO/TEX — still active?)
10. **Sprint 5:** Cross-agent verification pass
