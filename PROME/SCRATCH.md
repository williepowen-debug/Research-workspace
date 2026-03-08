# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-09 00:15 UTC

---

## Last Session: BRENT KB Migration Complete (Sun Mar 8 evening)

Migrated BRENT's KB.tsv from 6-column to 13-column schema. 102 rows, 4 chunks, each audited for signal preservation. Zero data loss.

### 13-Column KB Schema (FINALIZED & CODIFIED)
```
ID | Date | Group | Entity | Fact | Source | Conf | Epistemic | Status | Stale_By | DerivedFrom | Vectors | Notes
```
- Schema codified in `AGENTS/CLAUDE_TEMPLATE.md` with full Admiralty Code tables, field specs, and 3-pass cold-boot protocol
- BRENT is the first agent fully migrated — serves as reference implementation

### BRENT Migration Stats
- 102 rows: 75 EMPIRICAL, 25 ESTIMATE, 2 ASSUMPTION
- 56 A-tier, 34 B-tier, 4 C-tier, 6 D-tier (unverified X posts), 2 F-tier
- 17 DerivedFrom chains, 57 Stale_By dates, 95/102 have Vectors
- Old file backed up as `KB_old_6col.tsv`

### Next KB Migrations (Sprint 3 remainder):
- **📋 READ `AGENTS/KB_MIGRATION_PLAYBOOK.md` BEFORE STARTING ANY MIGRATION.** Column mappings, audit steps, pitfalls, chunk plans — all there.
- **Sprint 3c:** LABOR KB.tsv (11→13 columns, 81 rows, 4 chunks). Chunk plan in playbook.
- **Sprint 3d:** HENRY KB.tsv (15→13 columns, 89 rows — merging needed)
- **Sprint 3e:** REGINALD KB.tsv (15→13 columns, 116 rows — hardest)
- **Sprint 3f:** Update all agent CLAUDE.md files with new schema definition
- **Also created:** `AGENTS/VOCABULARIES.tsv` (controlled vocabulary for Group/Entity/Source). NOT enforced yet — let groupings emerge through migrations before consolidating.

### NEXUS synthesis completed (check output — not yet reviewed)

---

## Queued for Monday:
1. **SSB trim 50%** — first trading day
2. **HERMES delivery run** — critically backlogged
3. **Monday live data pulls** — see BRIEFING.md
4. **WAL position confirm** — $85P Jun open or closed?
5. **Prompts C & D** — fertilizer chain + SPR/transformers not yet run
6. **TRADE.md rollout** — BROCK, CARL, HAWK
7. **HERMES cron automation**
8. **LABOR:** LESSONS.md + domain/ folder migration
9. **Sprint 4:** REGINALD sub-agent audit
10. **Sprint 5:** Cross-agent verification pass
