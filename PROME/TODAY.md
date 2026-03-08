# TODAY.md — Disposable Daily Working Doc
**Date:** Sunday March 9, 2026 (will rename/delete at end of day)

---

## ACTIVE WORK: LABOR KB Refresh

### ✅ Completed
- [x] Migration: 81 rows, 4 chunks, 11→13 col
- [x] Freshness pass: 7 SUPERSEDED, 12 STALE identified
- [x] BLS Employment Situation (Prompt 1): 5 STALE refreshed + LAB-082→087 added
- [x] Denominator analysis: LAB-083 (U-6/PTER mirage confirmed)
- [x] Productivity & Costs: LAB-088→089 (productivity barbell, mfg -1.9%/ULC +8.3%)
- [x] Prompt 2 (NFIB/Indeed/Cass): LAB-031, LAB-018, LAB-043 refreshed
- [x] Cross-verification: Feb 2025 NFP (+151K not +42K), NFIB YoY baselines, mfg productivity
- [x] Prompt templates: PROMPT_BLS_EMPLOYMENT.md, PROMPT_PRODUCTIVITY.md
- [x] Playbook updated 8x

### 🔲 In Progress
- [ ] **Prompt 3: Google Trends** → updates LAB-040, LAB-041
  - "severance package", "layoffs", "job search"
  - Compare to Jan 2026 benchmarks (100, 92, 88)
  - State-level breakdown
- [ ] **Prompt 4: Claims + JOLTS** → updates LAB-007, LAB-050
  - Latest initial + continuing claims
  - DHS distortion status (clean or still suppressed?)
  - Has Jan 2026 JOLTS been released? (was delayed per LAB-078)

### 🔲 Not Started Today
- [ ] **PSEC PIK verification** — LAB-060 says 35%, MEMORY.md says 8.6%. One is poisoned.
- [ ] **Prompt template for NFIB/Indeed/Cass** — should save like we did for BLS/Productivity
- [ ] **Save Prompts 3 & 4 as templates** — Google Trends + Claims/JOLTS

---

## PARKING LOT (do later, not today)

### LABOR KB Housekeeping
- Hybrid row splitting (LAB-073 PCE, LAB-050, LAB-051)
- DerivedFrom backfill for synthesis rows
- Group consolidation (37 groups → fewer, after all agents migrated)

### KB Migrations
- HENRY: 89 rows, 15→13 col. Column mapping table needed in playbook first.
- REGINALD: 116 rows, 15→13 col. Data corruption in Category field. Hardest.
- All agent CLAUDE.md updates with 13-col schema

### Monday Trading Queue
- SSB trim 50%
- HERMES delivery run (critically backlogged)
- WAL position confirm ($85P Jun — open or closed?)
- Monday live data pulls
- Prompts C & D (fertilizer chain + SPR/transformers)

### Infrastructure
- TRADE.md rollout (BROCK, CARL, HAWK)
- HERMES cron automation
- NEXUS synthesis output — unreviewed
- Sprint 4: REGINALD sub-agent audit
- Sprint 5: Cross-agent verification pass

### Process Improvements
- Codify cross-verification protocol (2-3 LLMs) in LESSONS.md
- Extend prompt template pattern to other agents' key data sources

---

## NOTES / SCRATCH
- NFIB Plans to Hire collapsed 17%→12% — counter-narrative weakening
- Cass Freight new cycle low 0.886 — getting worse
- Productivity barbell: AI sectors surging, durables mfg -3.0%
- LABOR KB at 90 rows, 4 STALE remaining
