# Architecture Comparison: HENRY vs REGINALD

**Date:** 2026-03-05
**Purpose:** Deep structural comparison to create a standardized agent architecture template
**Baseline:** HENRY = "gold standard" (two audit passes); REGINALD = ~90% cleaned

---

## 1. Structural Differences

### Directory Layout

| Component | HENRY | REGINALD |
|-----------|-------|----------|
| **Total files** | ~52 | ~85+ |
| `domain/` | 3 files + `sources/` + `session_archive/` | 1 file + `sources/` |
| `workbook/` | 8 files (KB/VX/FLOW/VX_HISTORY.tsv + 5 .md) | 9 files + `archive/` subdir |
| `research/` | 3 subdirs (prompts/, outputs/, standalone) | 3 subdirs (prompts/, outputs/, FL_CONVERGENCE.md) |
| `sources/` (root) | 3 Burry files | 4 external source files |
| `archive/` | 6 files (clean) | 6 files |
| `inbox/processed/` | 3 files | 8 files |
| `sub-agents/` | ❌ None | ✅ 4 sub-agents (CREED, CORAL, TEX, RENO) + BROCK ref |
| `OZK/` | ❌ None | ✅ Deep-dive subdirectory (2 files) |
| `earnings_briefs/` | ❌ None | ✅ 1 file |
| `session_archive/` | In `domain/` (odd) | Root-level (1 file) |
| `ML.tsv` | ✅ Root-level | ❌ Archived to `workbook/archive/` |
| `TRADE.md` | ✅ (deprecated stub) | ❌ None |
| `SUB_AGENTS.md` | ❌ None | ✅ 155 lines |
| `BANK_EXPOSURE_MATRIX.md` | ❌ None | ✅ 614 lines |
| `CLEANUP_PLAN.md` | ❌ None | ✅ Residual from cleanup |

### Unique to HENRY
- `ML.tsv` at root (data release accuracy log) — clean separation from KB.tsv
- `domain/ECON_CALENDAR.md` — release schedule with thresholds
- `domain/REFERENCE_TABLES.md` — static reference (cascade order, transmission paths)
- `domain/BEIGE_BOOK_MAR4_2026.md` — template for future releases
- `TRADE.md` (deprecated pointer — clean deprecation pattern)

### Unique to REGINALD
- `SUB_AGENTS.md` — coordination protocol (155 lines)
- `BANK_EXPOSURE_MATRIX.md` — 614-line scoring matrix
- `OZK/` — entity-specific deep dive subdirectory
- `sub-agents/` — 4 sub-agent directories with their own workbooks
- `workbook/THESIS_VALIDATION.md` — explicit validation criteria
- `workbook/OTTO_INTEL.md` — cross-agent intel (307 lines)
- `research/FL_CONVERGENCE.md` — synthesis doc
- `CLEANUP_PLAN.md` — should be removed (residual)

---

## 2. What HENRY Does Better

### 2a. VX_HISTORY.tsv — Actually Populated
HENRY: **43 rows** of archived vector snapshots with dates, values, percentiles.
REGINALD: **Header only** (1 line, empty). This is a critical gap — REGINALD has no historical vector tracking despite having 61 active vectors.

**Recommendation:** REGINALD must populate VX_HISTORY.tsv. Without it, there's no way to see trend direction on slow-moving vectors.

### 2b. ML.tsv as Distinct Root File
HENRY keeps `ML.tsv` (data release accuracy — Date/Event/Actual/Consensus/Error) separate from `workbook/KB.tsv` (knowledge base). Clear purpose distinction. REGINALD archived ML.tsv into `workbook/archive/` — meaning data release tracking is effectively dead.

**Recommendation:** REGINALD should revive ML.tsv if it tracks any data releases (bank earnings, CMBS DQ prints, FHLB data).

### 2c. domain/ as Reference Library
HENRY's `domain/` has 3 clean reference files:
- `ECON_CALENDAR.md` — future release schedule with thresholds
- `REFERENCE_TABLES.md` — static frameworks (cascade order, leading indicators)
- `BEIGE_BOOK_MAR4_2026.md` — template for release synthesis

REGINALD's `domain/` has only 1 file (`FL_MIGRATION_REFERENCE.md`) plus `sources/`. The static reference material (convergence channel definitions, threshold tables) is embedded in STATUS.md and CLAUDE.md instead of being in dedicated domain files.

**Recommendation:** REGINALD should extract static reference tables from STATUS.md into `domain/REFERENCE_TABLES.md`.

### 2d. FLOW.tsv Consistency
HENRY: 19 rows, consistent columns: `ID | From_State | Trigger | To_State | Historical_Precedent | Confidence` — though some rows bleed extra columns.
REGINALD: 22 rows, better column set: `ID | Name | Speed | Layer | Status | Trigger | Current_Position | Pathway | Key_Insight | Cross_Links | Last_Updated`.

Actually — REGINALD's FLOW.tsv format is **superior** (see §3).

### 2e. Clean Deprecation Pattern
HENRY's `TRADE.md` is a 7-line pointer: "Positions → STATUS.md. Deprecated Mar 4." No ambiguity. REGINALD still has `CLEANUP_PLAN.md` that should have been removed.

### 2f. STATUS.md — Tighter Signal Dashboard
HENRY's Signal Dashboard (167 lines total) is pure data: indicator, value, source, status. No narrative. Every entry has `[CONF]` or `[EST]` tags. REGINALD's is similar but less consistently tagged.

---

## 3. What REGINALD Does Better

### 3a. research/README.md — Key Findings + Data Gaps + Exhausted Topics
*(Already back-ported to HENRY.)* REGINALD's research README has: Key Findings Summary, Data Gaps table, Exhausted Topics (do-not-re-research), Next Research Priorities, Sub-Agent Research Status. HENRY adopted this pattern.

### 3b. FLOW.tsv Schema
REGINALD's FLOW.tsv has **10 columns** including Speed, Layer, Status, Current_Position, Pathway, Key_Insight, Cross_Links, Last_Updated. HENRY's has 6 columns but some rows have extra unstructured content bleeding into wrong columns.

**Recommendation:** Standardize on REGINALD's FLOW.tsv schema. HENRY should adopt the Speed/Layer/Status/Current_Position columns.

### 3c. Predictions.tsv — Invalidation Criteria Column
REGINALD: Has explicit `Invalidation` column (e.g., "Phoenix office sales <40% discounts", "Advances stay <$550B through Q3"). Clear falsification.
HENRY: No invalidation column. Invalidation is sometimes in Notes but not structured.

**Recommendation:** HENRY must add an `Invalidation` column to PREDICTIONS.tsv.

### 3d. VX.tsv — Threshold Columns
REGINALD: `Yellow | Orange | Red` threshold columns per vector. Enables mechanical status assessment.
HENRY: No threshold columns — status is manually assigned with notes explaining why.

**Recommendation:** HENRY should add Yellow/Orange/Red threshold columns.

### 3e. KB.tsv — Richer Schema
REGINALD (116 rows, 15 columns): `ID | Date | Session | Entity | Category | Description | Analysis | Data_Quote | Source | Status | Confidence | Thesis_Impact | Vector_Links | Cross_Links | Notes`
HENRY (89 rows, 7 columns): `ID | Date | Domain | Title | Content | Confidence | Links`

REGINALD's schema enables filtering by entity, category, and thesis impact. HENRY's is more compact but less queryable.

**Recommendation:** Add at minimum `Entity`, `Source`, and `Thesis_Impact` columns to HENRY's KB.tsv.

### 3f. BANK_EXPOSURE_MATRIX.md — Deep Reference Doc
614 lines of multi-channel bank scoring. This is the kind of reference doc that should exist in every agent's `domain/` for their core analytical framework. HENRY has nothing equivalent for cascade scoring.

### 3g. Entity Sub-Directories (OZK/)
Dedicated subdirectory for deep-dive targets with their own STATUS.md. Clean pattern for entities that need sustained tracking beyond a KB.tsv entry.

### 3h. workbook/THESIS_VALIDATION.md
Explicit validation/invalidation criteria for the core thesis. HENRY embeds thesis validation in STATUS.md but doesn't have a dedicated file.

---

## 4. CLAUDE.md Comparison

| Aspect | HENRY (178 lines) | REGINALD (152 lines) |
|--------|-------------------|---------------------|
| **Identity block** | ✅ Clear role, network position | ✅ Clear role, "convergence point" framing |
| **Spawn protocol** | ✅ 6 steps, INBOX caveat | ✅ 7 steps (includes sub-agent check), INBOX caveat |
| **INBOX processing** | ✅ 6-step protocol, identical | ✅ 6-step protocol, identical |
| **Stale data rules** | ✅ VX.tsv, STATUS.md, VOL REGIME block | ✅ VX.tsv, STATUS.md, Call Report dating |
| **Output rules** | ✅ Tables > prose, 250-line cap | ✅ Tables > prose, 250-line cap |
| **Domain scope** | ✅ "You own / You do NOT own" | ✅ "You own / Sub-agents own / You do NOT own" |
| **Cross-agent signals** | ✅ Send/receive tables | ✅ Send/receive tables |
| **Key thresholds** | ✅ Table with current values + implications | ✅ Table with current values + implications |
| **FILES table** | ✅ **Comprehensive** — 16 entries, explains every file | ✅ **Comprehensive** — 18 entries + sub-agent file table |
| **Data release protocol** | ✅ Explicit template for macro drops | ❌ None (bank earnings template missing) |
| **War context** | ✅ Dedicated section | ❌ None (handled in STATUS.md) |
| **Hidden CRE methodology** | N/A | ✅ Embedded in CLAUDE.md — original discovery |
| **Bank watchlist** | N/A | ✅ Quick tier summary |

**Both are strong.** Key differences:
- HENRY has a **Data Release Protocol** section — REGINALD should add an equivalent for bank earnings drops
- REGINALD has the **Hidden CRE methodology** in CLAUDE.md — this is domain reference that should arguably be in `domain/` not CLAUDE.md, but it's useful at boot
- Both have complete FILES tables — gold standard pattern

---

## 5. STATUS.md Comparison

| Metric | HENRY (167 lines) | REGINALD (191 lines) |
|--------|-------------------|---------------------|
| **Under 250-line cap?** | ✅ Yes | ✅ Yes |
| **First line format** | Timestamped + one-sentence state | Date + one-sentence state |
| **Known Data Issues** | ❌ None | ✅ Explicit block |
| **Positions section** | ✅ 2 positions, clean table | ✅ 10 positions, table |
| **Thesis section** | ✅ "The Loaded Machine" — 3 fractures | ✅ "The Convergence" — 9-channel table |
| **Signal Dashboard** | ✅ 14 indicators, [CONF]/[EST] tags | ✅ 14 indicators, less consistently tagged |
| **Key Levels** | ✅ SPX technical levels table | ✅ Bank price levels table |
| **Cascade Status** | ✅ Step-by-step cascade state | ❌ Implicit in FLOW references |
| **Predictions inline** | ✅ Summary table (10 predictions) | ✅ Summary table (5 predictions) |
| **Cross-agent triggers** | ❌ Not in STATUS | ✅ Explicit table (6 conditions) |
| **Key Catalysts calendar** | ❌ Not in STATUS (→ ECON_CALENDAR.md) | ✅ Inline table with dates |
| **Bottom line** | ✅ Clean summary | ✅ Clean summary |
| **Duplicate content** | ⚠️ Some — Quality Rotation also in KB | ⚠️ Some — FL Migration appears twice |
| **Archival pointers** | ✅ Clean ("archived → file") | ✅ Clean |

**HENRY's STATUS.md** has better signal-to-noise: each section has a clear purpose, [CONF]/[EST] tagging is consistent, and the Cascade Status section is a unique high-value addition.

**REGINALD's STATUS.md** has better cross-agent awareness: the Cross-Agent Triggers table and Key Catalysts calendar are useful operational additions. The "Known Data Issues" block at the top is excellent — prevents stale data propagation.

**Recommendations:**
- HENRY should add a "Known Data Issues" block
- HENRY should add "Cross-Agent Triggers" table to STATUS.md
- REGINALD should add [CONF]/[EST] source tags to Signal Dashboard
- REGINALD should remove duplicate FL Migration section (appears both standalone and in FLORIDA MIGRATION section)
- Both should add a "Cascade Status" section (HENRY has one; REGINALD doesn't)

---

## 6. Workbook Comparison

### TSV Formats

| File | HENRY | REGINALD | Winner |
|------|-------|----------|--------|
| **KB.tsv** | 89 rows, 7 cols (compact) | 116 rows, 15 cols (rich) | **REGINALD** — more queryable |
| **VX.tsv** | 44 rows, 7 cols (no thresholds) | 61 rows, 12 cols (Y/O/R thresholds) | **REGINALD** — mechanical thresholds |
| **FLOW.tsv** | 19 rows, 6 cols (some bleed) | 22 rows, 10 cols (clean schema) | **REGINALD** — better schema |
| **VX_HISTORY.tsv** | 43 rows (populated) | 1 row (empty!) | **HENRY** — REGINALD broken |

### Naming Conventions
- HENRY: `ML-HEN-xxx`, `VX-HEN-x.xx`, `FLOW-HEN-xxx`
- REGINALD: `ML-REG-xxx`, `VX-REG-x.xx`, `FLOW-REG-x.xx`
- Both consistent within their domains. Good.

### Staleness Management
Both CLAUDE.md files have identical stale data rules for VX.tsv (skip [STALE], 5-day window, >50% stale = note and move on). Good standardization.

### VX_HISTORY Usage
HENRY: Active — 43 snapshots from Jan 26 baseline readings. Used for tracking vector drift over time.
REGINALD: **Dead** — header only. Despite having more vectors (61 vs 44), none have been archived. This means REGINALD cannot track trend direction on slow-moving indicators.

### Additional Workbook Files
REGINALD has `THESIS_VALIDATION.md` (explicit invalidation criteria) and `OTTO_INTEL.md` (cross-agent intel dump, 307 lines). HENRY has session logs and audit reports. Neither is better — just different operational needs.

---

## 7. Prediction Systems

| Aspect | HENRY | REGINALD |
|--------|-------|----------|
| **Format** | 7 cols: ID, Prediction, Confidence, Made_Date, Resolve_Date, Status, Result, Notes | 10 cols: Pred_ID, Date_Made, Prediction, Confidence, Timeframe, Status, Date_Resolved, Outcome, Invalidation, Notes |
| **Count** | 10 predictions (1 retired/invalid, 9 active) | 20 predictions (1 failed, 1 confirmed, 18 open) |
| **Invalidation** | ❌ Not structured — sometimes in Notes | ✅ Dedicated column |
| **Resolution tracking** | Resolve_Date + Status + Result | Date_Resolved + Outcome |
| **Confidence updates** | In Notes (e.g., "upgraded 60→70%") | In Notes (e.g., "UPGRADED 55→68%") |
| **ID format** | Mixed (H1-H7 legacy + HEN-01–05 new) | Clean (REG-01 through REG-20) |
| **Dependencies noted** | ❌ No | ✅ "CREED dependency", "LIQUID dependency" |

**REGINALD's format is superior.** Key advantages:
1. Explicit `Invalidation` column — every prediction has a kill switch
2. Dependency tracking — which sub-agent/peer feeds the prediction
3. Clean sequential ID format (REG-01, not mixed H1/HEN-01)
4. `Date_Resolved` + `Outcome` separate from `Status`

**HENRY's one advantage:** `Resolve_Date` is a future date (when we'll know), while REGINALD uses `Timeframe` (vaguer, e.g., "H1 2026"). HENRY's is more operationally useful for monitoring.

**Recommended standard:** REGINALD's schema + HENRY's `Resolve_Date` specificity + add `Dependency` column.

---

## 8. LESSONS.md

| Aspect | HENRY (34 lines, 8 lessons) | REGINALD (42 lines, 8 lessons) |
|--------|----------------------------|-------------------------------|
| **Format** | `### [Category] — Title` + Pattern/Rule | `### [Category] — Title` + Mistake/Rule |
| **Categories** | Data (2), Analysis (3), Process (1), Verification (2) | Data (3), Analysis (2), Process (2) |
| **Specificity** | ✅ High — cites specific events (Aug 2024 VIX, ADP revision, Iran leak) | ✅ High — cites specific errors (PSEC 35% PIK, Brent $118, MFS £500M→£600M) |
| **Actionable?** | ✅ Every lesson has a concrete Rule | ✅ Every lesson has a concrete Rule |
| **Cross-agent** | ✅ "LIQUID's HY OAS model overestimated by ~30bps" | ✅ "Cross-Agent Signal Values May Conflict" |

**Both are excellent.** Same format, same specificity, same usefulness. This is already a standardized pattern.

**One gap in both:** Neither has a lesson about STATUS.md size management or context budget. Given both agents had audit/cleanup cycles, a process lesson about pruning would be valuable.

---

## 9. Sub-Agent Architecture

### Current State
- **REGINALD:** 4 sub-agents (CREED, CORAL, TEX, RENO) + coordinates with BROCK (top-level)
  - SUB_AGENTS.md: 155 lines — directory, data ownership, sync protocol, escalation rules, spawning examples
  - Sub-agents have their own `workbook/`, `sources/`, `STATUS.md`
  - Last sync tracker shows all synced Feb 11-14 (3+ weeks stale)
  - TEX and RENO are "dormant" — carrying weight without producing
- **HENRY:** No sub-agents

### Should HENRY Have Sub-Agents?
**No.** HENRY's domain (market structure, macro data, vol) is inherently centralized — one agent tracking correlated indicators. Sub-agents make sense when domain decomposes into **independent geographic or entity-specific** tracks (which is REGINALD's pattern: FL vs TX vs NV vs CRE market-level).

### Should the Pattern Be Standardized?
**Yes, but lightweight.** Recommended standard for agents with sub-agents:

1. `SUB_AGENTS.md` at agent root — directory + data ownership + sync protocol
2. Sub-agent directories: `sub-agents/{NAME}/` with `STATUS.md`, `workbook/`, `sources/`
3. Last Sync Tracker in SUB_AGENTS.md — prevents staleness
4. Dormant sub-agents should be archived or explicitly flagged (TEX/RENO are dead weight)

### Specific Issues
- RENO's `sources/` has 7 files from Feb 11 — all stale, no updates since creation
- TEX has a full workbook (ML.tsv, VX.tsv, FLOW.tsv, PREDICTIONS.tsv) but no STATUS updates
- SUB_AGENTS.md describes CORAL as "CLO Expert" but CORAL is actually Florida-specific (per CLAUDE.md). Likely stale description.

---

## 10. Gaps in Both

### Neither Agent Has:

| Gap | Impact | Priority |
|-----|--------|----------|
| **SIGNALS.md** | Both CLAUDE.md files reference `AGENTS/SIGNALS.md` for cross-agent threshold breaches, but neither maintains their own signal log | 🔴 High |
| **Audit trail for confidence changes** | Predictions get upgraded (55→68%) but the reasoning is buried in Notes. No structured changelog. | 🟠 Medium |
| **Data freshness metadata** | No automated way to flag when STATUS.md values go stale. Relies on human/spawn discipline. | 🟠 Medium |
| **Workbook pruning rules** | No documented policy for when KB.tsv entries should be archived or VX.tsv rows marked stale. | 🟠 Medium |
| **Error log / failed predictions analysis** | REGINALD has 1 failed prediction (REG-10). Neither has a section analyzing WHY predictions failed. | 🟡 Low |
| **Position P&L tracking** | Both list positions but neither tracks entry price, current P&L, or Greeks. | 🟡 Low (FORGE's job) |
| **Template for new agents** | The patterns are good but undocumented. No AGENT_TEMPLATE/ exists. | 🔴 High (this report's purpose) |

---

## 11. Recommendations — Prioritized

### P0 — Critical (do now)

1. **Populate REGINALD VX_HISTORY.tsv** — Snapshot all 61 current VX values. Without history, trend detection is impossible.
2. **Add Invalidation column to HENRY PREDICTIONS.tsv** — Adopt REGINALD's schema (keep HENRY's Resolve_Date specificity).
3. **Remove REGINALD CLEANUP_PLAN.md** — Residual from cleanup, not part of architecture.
4. **Fix SUB_AGENTS.md CORAL description** — Currently says "CLO Expert", should say "Florida CRE/Condo Crisis".

### P1 — Important (this week)

5. **Standardize FLOW.tsv schema** — Adopt REGINALD's 10-column format for all agents. HENRY's FLOWs are richer in content but worse in structure.
6. **Add Yellow/Orange/Red threshold columns to HENRY VX.tsv** — Mechanical status assessment beats manual.
7. **Add Known Data Issues block to HENRY STATUS.md** — Prevents stale data propagation.
8. **Add Cross-Agent Triggers table to HENRY STATUS.md** — REGINALD's pattern is operationally useful.
9. **Add [CONF]/[EST] source tags to REGINALD Signal Dashboard** — HENRY's pattern prevents citing estimates as facts.
10. **Extract REGINALD static references from STATUS.md** — Hidden CRE methodology + convergence channel definitions → `domain/REFERENCE_TABLES.md`.
11. **Archive or flag dormant sub-agents** — TEX/RENO haven't been updated since Feb 11-12. Either archive or add `⏸️ DORMANT` status.

### P2 — Nice to Have (next audit cycle)

12. **Enrich HENRY KB.tsv** — Add Entity, Source, Thesis_Impact columns (REGINALD's schema).
13. **Add Data Release Protocol to REGINALD CLAUDE.md** — Template for bank earnings drops (like HENRY's macro data template).
14. **Add Cascade Status section to REGINALD STATUS.md** — HENRY's step-by-step cascade tracking is high-value.
15. **Clean HENRY prediction IDs** — Migrate H1-H7 → HEN-06–HEN-12 for consistent sequential format.
16. **Revive REGINALD ML.tsv** — If REGINALD tracks bank earnings data releases, this should be active.
17. **Create AGENT_TEMPLATE/** — Document the standard architecture based on this comparison.

### P3 — Future Consideration

18. **Standardize PREDICTIONS.tsv across all agents** — REGINALD's schema + HENRY's Resolve_Date + Dependency column.
19. **Add prediction failure analysis** — When predictions resolve wrong, log the WHY.
20. **Consider entity sub-directories for HENRY** — If HENRY ever needs sustained tracking of a specific instrument (e.g., PLTR for H5), the OZK/ pattern works.

---

## Summary

**HENRY excels at:** Tight STATUS.md, VX_HISTORY tracking, clean deprecation, domain reference files, [CONF]/[EST] tagging, cascade status tracking.

**REGINALD excels at:** TSV schemas (KB, VX, FLOW, PREDICTIONS), invalidation criteria, cross-agent trigger tables, sub-agent coordination, entity deep-dives, Known Data Issues block.

**The ideal agent template combines both:** HENRY's operational discipline with REGINALD's structural richness. The 17 recommendations above would bring both agents to parity with the best patterns from each.

---

*Generated by PROME architecture comparison subagent, 2026-03-05*
