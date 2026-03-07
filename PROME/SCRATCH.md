# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-08 22:30 UTC

---

## Last Session: KB Schema Redesign (Sun Mar 8)

Researched KB schema best practices across intelligence analysis (ICD 203/206, Admiralty Code), scientific evidence synthesis (GRADE, Cochrane/PRISMA), investigative journalism (ICIJ), and quant finance (QuantMind, bi-temporal). Will ran prompt on 3 LLMs, cross-analyzed all outputs.

### Result: 13-Column KB Schema (FINALIZED)
```
ID | Date | Group | Entity | Fact | Source | Conf | Epistemic | Status | Stale_By | DerivedFrom | Vectors | Notes
```
- **Conf** = Admiralty digraph A1–F6 (source reliability × info credibility). Default F6.
- **Epistemic** = EMPIRICAL / ESTIMATE / ASSUMPTION
- **Stale_By** = expiration date, null if static
- **DerivedFrom** = parent KB IDs for provenance chains
- Schema codified in `AGENTS/CLAUDE_TEMPLATE.md` with full Admiralty Code tables and 3-pass cold-boot protocol

### Completed Infrastructure Sprints (prior sessions):
- Sprint 1 ✅: Mail system migration
- Sprint 2 ✅: TSV location standardization
- Sprint 3a ✅: LABOR ML.tsv → KB.tsv rename

### BRENT KB Migration — IN PROGRESS
- 102 rows, chunked into 4 pieces
- **Chunk 1 ✅ (KB-BRT-001–018)** — 18 rows. Audited clean.
- **Chunk 2 ✅ (KB-BRT-019–043)** — 25 rows. Audited clean.
- **Chunk 3 ✅ (KB-BRT-044–073)** — 30 rows. Audited clean. Good DerivedFrom chains (bypass total ← 4 routes, STNG EPS ← rates, pump price ← transmission + crack).
- **Next: Chunk 4 (KB-BRT-074–102)** — 29 rows. Macro Transmission, Sulphur Chain, Taiwan. FINAL CHUNK.
- Chunk 2: KB-BRT-019–043 — Demand Destruction, OPEC+ Unwind, LNG
- Chunk 3: KB-BRT-044–073 — Energy Credit, OPEC Spare, Bypass, STNG
- Chunk 4: KB-BRT-074–102 — Macro Transmission, Sulphur, Taiwan
- Old 9-col KB_new.tsv exists but will be replaced with 13-col version

### NEXUS synthesis completed (check output)

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
