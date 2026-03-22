# ARCHIVE — Memory Entries (Relocated)

**Purpose:** Entries removed from MEMORY.md that are fully captured in agent STATUS files or dedicated research docs. Not loaded at boot. Reference on-demand only.

---

## Archived 2026-03-22

### Hidden CRE (Memo Item 3) — Feb 22-23
Banks hide CRE in C&I via FFIEC Schedule RC-C Memo Item 3 (RCON2746). Three masking levels: extend-and-pretend, mark-to-model, **classification** (our discovery). Screen: RC-C Part I → Item 4 (C&I) → Memo Item 3 → ratio >20% = flag.
Results: OZK 37.6% (worst), WAL 24.2% (growing), EGBN 23.7%. Clean: ZION 1.8%, SSB 0.9%.
**Now in:** REGINALD STATUS (per-bank data + H.8 systemic confirmation), FORGE/WAL/STATUS.md

### WAL Thesis (A+)
$2.73B hidden CRE, ratio GROWING (15.5%→24.2%), mgmt confirmed relabeling. 474% CRE/Tier1. Three vectors: hidden CRE, Jefferies double-pledging, SSFA arbitrage ($17.2B). Detail → `FORGE/WAL/STATUS.md`
**Now in:** FORGE/WAL/STATUS.md

### OZK 10-K — Feb 25
Reserves CUT 41% while losses accelerated. IL=67% NPLs. $19B unfunded > $14B liquidity. All C-suite selling. SI 14-15% (crowded vs WAL 4.4%). Detail → `AGENTS/REGINALD/OZK/`
**Now in:** AGENTS/REGINALD/OZK/STATUS.md, AGENTS/REGINALD/OZK/10K_ANALYSIS_2024.md

### Eisman/Gober on APO — Mar 2
Athene $37.9B deposit-type contracts (duration mismatch = run risk). Affiliated paper $10B→$40B. Captive financials: $7B liabilities vs $200M real assets. Sellside covering APO are NOT insurance analysts — nobody reads statutory filings. We see structure AND trigger. Detail → `BROCK/domain/sources/EISMAN_GOBER_TRANSCRIPT_ANALYSIS_MAR2.md`
**Now in:** AGENTS/BROCK/domain/sources/EISMAN_GOBER_TRANSCRIPT_ANALYSIS_MAR2.md, FORGE/research/iran-war/reference/

### Consumer K-Shape (Feb 16)
Housing → banks directly, bypasses consumer credit. Consumer credit only cracks if employment cracks (>250K claims).
**Now in:** AGENTS/CARL/STATUS.md (K-shape framework, convergence scoring, transmission logic)

### Convergence Day — Feb 27
Private credit → bank equity transmission confirmed LIVE. MFS fraud (£2B) → Jefferies/Barclays → sector derisking → WAL -10.64% on NO specific catalyst (pure vulnerability premium). H.8 confirmed industry-level Memo Item 3 reclassification: C&I +14.4% while CRE +1.1% (from +5.9%) — the masking is systemic, not bank-specific. HY OAS 320bps = credit transmission threshold.
**Now in:** AGENTS/REGINALD/STATUS.md (Cross-Domain section, written Mar 22)

### NFP -92K — Mar 6
First negative NFP this cycle. Dec revised to -17K. Stagflation locked: earnings +3.8% YoY, Fed can't cut. Harvested 5 short-dated for $3,056 (+183% to +340%). **Rule: harvest short-dated on red days, re-enter on green days.**
**Now in:** AGENTS/LABOR/STATUS.md (extensive NFP -92K refs, stagflation, shadow gap confirmed). Harvest rule in LESSONS.md.

### Chart Analysis (Feb 24)
6-bank watchlist topped Feb 2026 and reversed. GFC 2007 template (slow grind), not SVB. KRE P/C 2.27. 75-80% this is THE TOP. Detail → `FORGE/STATUS.md`
**Now in:** FORGE/STATUS.md (Thesis section, written Mar 22)

### Energy Dominance — Mar 2 (WILL'S INSIGHT)
US running integrated supply consolidation across Venezuela/Iran/Russia + ghost fleet crackdown. Saudi last man standing BY DESIGN. Structural repricing, not war premium. 16M+ bpd at risk. Detail → `HAWK/domain/sources/ENERGY_DOMINANCE_STRATEGY.md`
**Now in:** HAWK sources, FORGE/research/iran-war/reference/ENERGY_DOMINANCE_STRATEGY.md

### Agent Check-in Proposals — Mar 19 (PROCESS FIX)
Was sitting on agent proposals instead of routing to Will. Fixed: AGENTS.md updated. Standard practice now: agent proposes → route to Will → execute on approval.
**Now in:** AGENTS.md (agent trade proposals rule)

### Context Optimization — Mar 12
Injection per message: ~31KB → ~13KB (-58%). Boot reads: ~27KB → ~10KB (-63%). Key insight: injected files = instinct (every message), boot files = lookup (once per session). Safety/signal processing/file editing = instinct. Spawn syntax/handoff/references = lookup. OpenClaw forces IDENTITY.md + TOOLS.md injection from workspace root — can't remove, only minimize. Subagents get fewer injections than main session (no HEARTBEAT.md or MEMORY.md).
**Now in:** Historical process note. No longer needed in active memory.
