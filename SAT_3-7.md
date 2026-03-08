# SAT 3/7 — Active Working Session Tracker
**Purpose:** Temporary file tracking everything in-flight from Saturday March 7, 2026. Delete when fully resolved.

---

## 🔧 INFRASTRUCTURE SPRINTS (Agent Standardization)

### Completed ✅
- Sprint 1: Mail system migration (REGINALD + HENRY → mail/inbox/ folders)
- Sprint 2: TSV location standardization (PREDICTIONS.tsv + ML.tsv → workbook/)
- Sprint 3a: LABOR ML.tsv renamed to KB.tsv

### In Progress
- **Sprint 3b: BRENT KB migration** — 103 rows, 6→9 columns (easiest). START HERE next session.
- Sprint 3c: LABOR KB migration — 82 rows, 11→9 columns
- Sprint 3d: HENRY KB migration — 89 rows, 15→9 columns
- Sprint 3e: REGINALD KB migration — 116 rows, 15→9 columns (hardest)
- Sprint 3f: Update all 4 CLAUDE.md with new schema definition

### New 13-Column KB Schema (AGREED, supersedes 9-col):
```
ID	Date	Group	Entity	Fact	Source	Conf	Epistemic	Status	Stale_By	DerivedFrom	Vectors	Notes
```
*(REGINALD's richer schema adopted network-wide. Admiralty Conf codes, Epistemic type, Stale_By, DerivedFrom added.)*

### Still Queued (after KB migration)
- Sprint 3 remainder: LABOR needs LESSONS.md + domain/ folder migration
- Sprint 4: REGINALD sub-agent audit (BELT/CORAL/CREED/RENO/TEX — active?)
- Sprint 5: Cross-agent verification pass

---

## 📊 RESEARCH PROMPTS (Will running in parallel)

### Returned (ingested)
- ✅ Prompt A: Sulphur → Sulphuric Acid → Base Metals (51K chars, ingested by BRENT)
- ✅ Prompt B: Taiwan Energy Security → Semiconductor Output (37K chars, ingested by BRENT)

### Not Yet Run
- ⬜ Prompt C: Fertilizer → Food Security → Sovereign Stress
- ⬜ Prompt D: SPR Mechanics + Grid Hardware Bottleneck

### New Prompts (from NEXUS findings, crafted today)
- ⬜ Prompt 1: Bank Earnings Pre-Announcement History (for C-11)
- ⬜ Prompt 2: DHS Claims Suppression Mechanics (for C-12) — TIME SENSITIVE (Mar 12)
- ⬜ Prompt 3: Tech Goods Deflation — Fed's Last Relief Valve (for C-13)
- ⬜ Prompt 4: Hormuz Resolution Analogs — Speed of Oil Price Reversal (for X-12)
- ⬜ Prompt 5: Stagflation Episodes — What Broke First? (for C-14 + TLT)

---

## 📋 TRADE.md STATUS

### Created ✅
- BRENT TRADE.md (24KB) — LNG spread #1, Phase 2 protocols, correlation risk
- REGINALD TRADE.md (34KB) — Earnings battle plan, SSB trim, EGBN 5/5
- HENRY TRADE.md (27KB) — Threshold matrix, VIX coiled spring, TLT puts
- LABOR TRADE.md (24KB) — Transmission map, claims playbook, FL UI cliff

### Not Yet Created
- ⬜ BROCK TRADE.md
- ⬜ CARL TRADE.md
- ⬜ HAWK TRADE.md

---

## 🔴 MONDAY ACTIONS (Mar 10)

1. **SSB trim 50%** — FIRST action at open
2. **WAL position confirm** — is $85P Jun still open?
3. **12 live data pulls** — see BRIEFING.md for full list
4. **HERMES delivery run** — critically backlogged (HAWK 3 outbox + BRENT→SAM v2 + BRENT→HAWK sulphur)

---

## 🧠 NEXUS FINDINGS (from today's synthesis)

| ID | Finding | Status |
|----|---------|--------|
| C-11 | Q2 Forced Disclosure Cluster (Apr 16-29) | 78% — research Prompt 1 to deepen |
| C-12 | Claims 300K Tripwire | 72% — research Prompt 2 to interpret Mar 12 |
| C-13 | Semiconductor/Stagflation Amplifier | 65% — research Prompt 3 to quantify |
| C-14 | LNG-Credit Shared Root | 80% — correlation ceiling reached (6-9%) |
| X-12 | Path A vs Earnings contradiction | REAL — research Prompt 4 for exit speed |

---

## 🔍 PROME ASSESSMENTS (from today, not yet actioned)

- BRENT TRADE.md: Prome disagrees with EOG at conviction 3/5 — should be 2/5 or conditional. Just directional oil beta with decay.
- BRENT TRADE.md: Missing gas pump peak stress window (Mar 14-21) from CARL's domain as secondary catalyst.
- BRENT predictions BRT-25 (TSMC guidance warning): needs tighter definition — what counts as confirmation?
- NEXUS C-14: HYG $75P should be counted in Hormuz-correlated book. Total exposure 6-9% = at ceiling.
- X post fertilizer data: India 64% urea from GCC, ₹2.5T subsidy at crisis levels, China 10M tpa sulphur (56% ME) — log to BRENT KB when migrated.

## 📝 MISC OPEN ITEMS

- HERMES cron automation — identified as top infra priority, not built yet
- HENRY CLAUDE.md had "TRADE.md is deprecated" — FIXED
- BRENT has MEMORY.md, no other agent does — decide: adopt or remove?
- NEXUS system messages getting swallowed (REGINALD too) — possible OpenClaw issue?
- File structure audit only covered BRENT/REGINALD/LABOR/HENRY — other agents (BROCK, CARL, HAWK, SAM, ZHAO, MARCO, HANS, LIQUID, RED) not yet audited
- BRENT TRADE.md referenced STNG 2 shares — verify current position status
- Overnight BRENT session produced research prompts doc (research/RESEARCH_PROMPTS.md) — some may overlap with new NEXUS prompts

---

*Delete this file when all items resolved or rolled into permanent files.*
