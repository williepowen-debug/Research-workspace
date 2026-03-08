# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-09 18:00 UTC

---

## Last Session: LABOR KB Staleness Updates — Indeed + Cass Complete (Sun Mar 9)

### Completed This Session
- **Indeed (KB-LAB-018):** Refreshed with 4-LLM cross-verification. FRED-confirmed index 104.7. Upgraded B1→A1. VX-LAB-1.04 updated -5.2%→-5.9%.
- **Cass Freight (KB-LAB-043):** Enriched with inferred rates +8.4%, 36-month decline streak, Jan 2020 baseline. Also updated KB-LAB-038, VX-LAB-11.01, FLOW-LAB-6.01.

### Remaining (1 manual + 1 verification)
- **Google Trends** — Will does manually at trends.google.com (LLMs can't pull this)
- **DHS shutdown status** — verification prompt in WILL/PROMPTS.md (HIGH PRIORITY — determines if claims data is clean)
- JOLTS Jan 2026 releases Mar 13 — no action until then
- **PSEC PIK: ✅ DONE.** 35% confirmed poisoned → actual 8.6%. All files corrected.

### Continuing Claims Alert
- 1,868K — **32K from YELLOW threshold (1.9M)**
- Duration proxy 8.0→8.8 weeks
- Hotel California intensifying
- Next print Mar 12 could trigger status change

### Model Rankings (4 prompts, Mar 9)
ChatGPT (1.5 avg) > Perplexity (2.0) > Kimi 2.5 (1.0 but 1 sample) > Gemini (3.3) > DeepSeek (4.0)
Kimi 2.5 worth adding to rotation. DeepSeek droppable.

### Model Rankings (2 prompts complete)
1. Perplexity + ChatGPT tied (1.5 avg) — Perplexity = best sourcing, ChatGPT = most analytical value-add
2. Gemini (3.0) — good narrative, makes errors (inferred rate wrong, consecutive months off by 1)
3. DeepSeek (4.0) — consistently weakest, fabricates specifics

---

## Previous Session: LABOR KB Migration + BLS Data Integration (Sun Mar 9)

LABOR KB fully migrated (81 rows, 4 chunks) then expanded to 90 rows with Mar 6 BLS data. Freshness pass completed. Cross-verification protocol established (2-3 LLMs minimum).

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
- **Sprint 3c: ✅ LABOR KB.tsv COMPLETE.** 90 rows (81 migrated + 9 new BLS entries). Freshness pass done: 7 SUPERSEDED, 7 STALE remaining (need Prompts 2-4: NFIB, Indeed, Cass Freight, Google Trends, continuing claims). PSEC PIK verification still needed (LAB-060/071 may contain poisoned data — MEMORY.md says 8.6% not 35%). Two reusable prompt templates created: `AGENTS/LABOR/research/PROMPT_BLS_EMPLOYMENT.md`, `PROMPT_PRODUCTIVITY.md`.
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
