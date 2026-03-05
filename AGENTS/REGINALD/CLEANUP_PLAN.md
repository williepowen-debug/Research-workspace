# REGINALD Cleanup Plan
**Created:** 2026-03-05 | **Template:** HENRY (gold standard)
**Goal:** Bring REGINALD to HENRY-level cleanliness

---

## Current State
- STATUS.md: 216 lines (target ~160)
- CLAUDE.md: 169 lines (check FILES table completeness)
- 130+ files including 4 sub-agents (CORAL, CREED, RENO, TEX)
- 2 unprocessed inbox signals
- Workbook naming inconsistent (ML.tsv vs KB.tsv standard)
- Root-level files of unclear status (BANK_EXPOSURE_MATRIX.md, RESEARCH_STATUS.md, SUB_AGENTS.md)
- OZK subdirectory with its own STATUS.md

## Execution Order

### Step 1: Self-Audit Spawn
Spawn REGINALD to audit his own domain (same task as HENRY). Focus on:
- Stale data, contradictions, missing/orphaned files
- Prediction hygiene
- Sub-agent status (active or dead?)
- Write to `workbook/SELF_AUDIT_REPORT.md`

### Step 2: Sub-Agent Decision (NEEDS WILL INPUT)
CORAL, CREED, RENO, TEX each have full STATUS/workbook/research trees.
- Are they still actively spawned? Or were they one-off research that's done?
- If done: archive to `archive/sub-agents/` and remove from active tree
- If active: standardize their structure (KB.tsv rename, OUTBOX cleanup)
- This decision determines scope of remaining work

### Step 3: Process Inbox
- `inbox/2026-03-04_carl_fl_ui_cliff.md` — FL UI exhaustion cliff Mar 24
- `inbox/2026-03-04_hans_european_bank_stress.md` — European bank stress / iTraxx

### Step 4: Condense STATUS.md (216 → ~160)
Pattern from HENRY:
- Archive session logs to workbook/
- Move static reference tables to domain/
- Condense detailed sections to summaries + pointers
- Identify what's narrative vs live state

### Step 5: Standardize Workbook
- Rename workbook/ML.tsv → workbook/KB.tsv (knowledge base)
- Same for sub-agent workbooks if they survive Step 2
- Check for stale VX.tsv rows (apply HENRY's 50% stale rule)
- Archive slow-movers to VX_HISTORY.tsv

### Step 6: CLAUDE.md FILES Table
- Ensure every active file/directory is indexed
- Add boot vs no-boot guidance
- Clarify root TSV vs workbook TSV purposes
- Add sub-agent reference (if they survive Step 2)

### Step 7: OUTBOX + LESSONS
- Structure OUTBOX with PENDING/DELIVERED sections
- Check LESSONS.md for staleness, add any new lessons from recent sessions

### Step 8: Verify
- Run second self-audit (like HENRY's SELF_AUDIT_MAR5B.md)
- Confirm no duplicate IDs, broken paths, stale references
- Final commit

---

## Key Questions for Will Before Starting
1. Sub-agents (CORAL, CREED, RENO, TEX) — keep active or archive?
2. OZK subdirectory — should this stay under REGINALD or move to FORGE?
3. BANK_EXPOSURE_MATRIX.md — still referenced? Still current?
