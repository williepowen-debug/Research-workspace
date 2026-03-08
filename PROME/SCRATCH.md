# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-09 21:00 UTC

---

## Last Session: LABOR KB Sprint Complete + Signal Protocol + HAWK Migration Plan (Sun Mar 9)

### HAWK Migration — QUEUED (4 segments)
**Segment A:** Create KB.tsv from ML.tsv (27 rows) + STATUS.md facts → 13-column schema
**Segment B:** Migrate VX.tsv (9 rows, 8→12 col) + FLOW.tsv (8 rows, 8→10 col)
**Segment C:** Align PREDICTIONS.tsv + update CLAUDE.md with KB schema/cold-boot protocol
**Segment D:** Create SCHEMA.tsv + spawn HAWK to process 3 inbox signals (SIG-001/002/003)

### 3 Signals Waiting in HAWK Inbox
- SIG-2026-03-09-001: Iraq 3M bpd shut-in (🔴 URGENT)
- SIG-2026-03-09-002: Infrastructure escalation — water/oil strikes both sides (🔴 URGENT)
- SIG-2026-03-09-003: Gulf fertilizer supply chain vulnerability — Coface data (🟡 STANDARD)
DO NOT spawn HAWK until migration complete (Segment D).

### Signal Protocol Codified
`PROME/SIGNAL_PROTOCOL.md` — full template with KB staging, source types, Admiralty scale. Referenced from AGENTS.md.

---

## Previous: LABOR KB Staleness Sprint COMPLETE (Sun Mar 9)

### Completed Today (5 prompts + 1 verification)
- **Indeed (KB-LAB-018):** FRED-confirmed index 104.7, -5.9% YoY. Upgraded B1→A1.
- **Cass Freight (KB-LAB-043):** Inferred rates +8.4%, 36-month decline streak, Jan 2020 baseline.
- **Claims (KB-LAB-050):** 1,868K continuing (+46K WoW), 32K from YELLOW. Duration proxy 8.8 weeks.
- **PSEC PIK (KB-LAB-060/071):** 35% POISONED → actual 8.6%. All files corrected. NAV $6.21 (-20.8% YoY).
- **DHS Shutdown (KB-LAB-065):** CONFIRMED ongoing Day 23+. Senate blocked 51-45. All claims suppressed.
- **5 new rows:** VX-LAB-1.04B, VX-LAB-8.05, VX-LAB-1.06, FLOW-LAB-14.01, KB-LAB-091.

### Remaining (1 manual only)
- **Google Trends** — Will does manually at trends.google.com (LLMs can't pull this)
- JOLTS Jan 2026 releases Mar 13 — no action until then
- ✅ DHS shutdown: CONFIRMED ongoing Day 23+ (4 LLMs verified)
- ✅ PSEC PIK: 8.6% confirmed, all poisoned data cleaned

### Continuing Claims Alert
- 1,868K — **32K from YELLOW threshold (1.9M)**
- Duration proxy 8.0→8.8 weeks
- Hotel California intensifying
- Next print Mar 12 could trigger status change

### Model Rankings (4 prompts, Mar 9)
ChatGPT (1.5 avg) > Perplexity (2.0) > Kimi 2.5 (1.0 but 1 sample) > Gemini (3.3) > DeepSeek (4.0)
Kimi 2.5 worth adding to rotation. DeepSeek droppable.

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
- **Sprint 3c: ✅ LABOR KB.tsv COMPLETE.** 91 rows. Staleness sprint done: Indeed, Cass, Claims, PSEC PIK all refreshed via 4-LLM cross-verification. DHS shutdown confirmed. 5 new rows created. Only Google Trends remains (Will manual).
- **Sprint 3d:** HENRY KB.tsv (15→13 columns, 89 rows — merging needed)
- **Sprint 3e:** REGINALD KB.tsv (15→13 columns, 116 rows — hardest)
- **Sprint 3f:** Update all agent CLAUDE.md files with new schema definition
- **Also created:** `AGENTS/VOCABULARIES.tsv` (controlled vocabulary for Group/Entity/Source). NOT enforced yet — let groupings emerge through migrations before consolidating.

### NEXUS synthesis completed (check output — not yet reviewed)

---

## Queued for Next Session:
1. **🔴 HAWK Migration Segment A** — Create KB.tsv from ML.tsv + STATUS.md (see plan above)
2. Then Segments B/C/D across subsequent clears
3. After HAWK migration: spawn HAWK to process 3 urgent signals

## Queued for Monday (Market):
1. **SSB trim 50%** — first trading day
2. **HERMES delivery run** — critically backlogged
3. **Monday live data pulls** — see BRIEFING.md
4. **WAL position confirm** — $85P Jun open or closed?
5. **TRADE.md rollout** — BROCK, CARL, HAWK
6. **HERMES cron automation**
7. **Sprint 3d:** HENRY KB.tsv migration
8. **Sprint 3e:** REGINALD KB.tsv migration
9. **Google Trends** — Will does manually
