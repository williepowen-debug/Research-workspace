# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-09 21:00 UTC

---

## Last Session: HAWK Migration A-D + 22-Signal Blitz (Sun Mar 9)

### HAWK Migration — COMPLETE (4/4 segments done)
**Segment A: ✅** KB.tsv (34 rows) | **B: ✅** VX.tsv + FLOW.tsv | **C: ✅** PREDICTIONS + CLAUDE.md | **D: ✅** SCHEMA.tsv + spawn
**Remaining:** HAWK TRADE.md, check spawn result (was running 16+ min)

### 22-Signal Blitz Delivered (all 13 domain agents)
Will sent ~30 screenshots. Triaged and routed to HAWK(4), BRENT(3), BROCK(2), LABOR(1), NEXUS(1), HENRY(1), CARL(1), REGINALD(2), SAM(1), LIQUID(1), ZHAO(1), MARCO(1), HANS(1), OTTO(1).
Key data: Hormuz -92%, Iraq 3M bpd confirmed, finance openings -117K, BX $400M own-money, MFS £930M forensics, Platts all commodities exploding, SPY below 20-week MA.
**NEW VECTOR:** Gulf surplus recycling (Campbell) — third anchor for UST selling. Needs FLOW.tsv mapping.

### HERMES Delivery Run Complete
12 signals from NFP day backlog cleared. All outboxes clean.

### HAWK Spawn — CHECK RESULT
Inbox processing (6 signals) was running 16+ min at checkpoint. PLUS 4 new signals delivered tonight need second processing run.

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
1. **Check HAWK spawn result** — was it successful? Review KB/VX/FLOW changes.
2. **HAWK second inbox run** — 4 new signals (SIG-004 through 007) delivered tonight
3. **HAWK TRADE.md** — last piece of full migration

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
