# BROCK MIGRATION PLAN

**Created:** 2026-03-12
**Goal:** Bring BROCK to gold-standard architecture matching HENRY/REGINALD/LABOR
**Prior audit:** `UPGRADE_PLAN.md` (Mar 6 self-audit — detailed gap analysis, still valid)
**Supersedes:** UPGRADE_PLAN.md for execution purposes (that file remains as reference)

---

## Task Sequence

Tasks are ordered by dependency. Each is designed to fit in a single session segment (between `/clear` or `/new`). **Prome executes all tasks directly** — these are structural/architectural changes, not domain research. BROCK gets spawned AFTER migration is complete to process inbox and populate the new structures with content.

| Task | Name | Depends On | Executor | Est. Size |
|------|------|------------|----------|-----------|
| 1 | TSV Schema Migration | None | Prome | Medium |
| 2 | STATUS.md Prune + Archive | None | Prome | Medium |
| 3 | CLAUDE.md Overhaul | None | Prome | Medium |
| 4 | TRADE.md + EXPECTED_SIGNALS cleanup | Task 3 (CLAUDE.md references TRADE.md) | Prome | Light |
| 5 | Spawn BROCK — inbox processing | Tasks 1-4 complete | BROCK subagent | Medium |

---

## TASK 1: TSV Schema Migration

**What:** Migrate all 4 core TSVs from old schemas to HENRY/REGINALD standard. Preserve all existing data — just restructure columns.

### VX.tsv — Current (11 cols) → Target (12 cols)

**Current:**
```
Vector_ID	Name	Category	Current_Value	Yellow	Orange	Red	Status	Confidence	Last_Updated	Source	Notes
```

**Target (HENRY standard):**
```
ID	Name	Category	Current_Value	Yellow	Orange	Red	Status	Confidence	Last_Updated	Source	Cross_Links	Notes
```

**Migration steps:**
1. Read current VX.tsv fully
2. Rename `Vector_ID` → `ID`
3. Add `Cross_Links` column (empty initially — BROCK populates on next spawn)
4. Verify all rows have Y/O/R threshold values (BROCK already has these ✅)
5. Write back

### KB.tsv — Current (6 cols) → Target (14 cols)

**Current:**
```
ID	Date_Added	Category	Fact	Source	Confidence	Notes
```

**Target (HENRY standard):**
```
ID	Date	Session	Entity	Category	Description	Analysis	Data_Quote	Source	Status	Confidence	Thesis_Impact	Vector_Links	Cross_Links	Notes
```

**Migration steps:**
1. Read current KB.tsv fully
2. Map columns:
   - `Date_Added` → `Date`
   - `Fact` → `Description`
   - `Notes` → `Notes`
   - `Source` → `Source`
   - `Confidence` → `Confidence`
   - `Category` → `Category`
3. Add new columns with sensible defaults:
   - `Session` → blank (historical, no session tracking)
   - `Entity` → derive from Category or ID (e.g., KB-BRK-001 about Athene → `Athene`)
   - `Analysis` → blank (BROCK fills on next pass)
   - `Data_Quote` → extract key numbers from Description if obvious, else blank
   - `Status` → `CONFIRMED` (all existing KB entries are confirmed facts)
   - `Thesis_Impact` → `CONSISTENT` default (all existing KB supports thesis)
   - `Vector_Links` → blank (BROCK cross-references on next spawn)
   - `Cross_Links` → blank
4. Write back

### FLOW.tsv — Current (6 cols) → Target (10 cols)

**Current:**
```
CHANNEL	FROM	TO	MECHANISM	MAGNITUDE	NOTES
```

**Target (HENRY standard):**
```
ID	Name	Speed	Layer	Status	Trigger	Current_Position	Pathway	Key_Insight	Cross_Links	Last_Updated
```

**Migration steps:**
1. Read current FLOW.tsv fully
2. This is a FULL RESTRUCTURE, not a column add. Current format tracks transmission channels (warehouse lines, revolvers, etc.). Target format tracks transmission pathways with status/trigger mechanics.
3. Map:
   - `CHANNEL` → `ID` (e.g., `1_Warehouse_Lines` → `FLOW-BRK-001`)
   - `FROM → TO` → `Pathway` (combine into transmission description)
   - `MECHANISM` → `Name` (short label)
   - `MAGNITUDE` → `Current_Position`
   - `NOTES` → `Key_Insight`
4. Add new columns:
   - `Speed` → classify each channel (DAYS/WEEKS/MONTHS)
   - `Layer` → classify (1-MTM / 2-Credit / 3-Liquidity / 4-Solvency)
   - `Status` → ARMED/BUILDING/ACTIVE/FIRED based on current state
   - `Trigger` → what event activates this channel
   - `Cross_Links` → blank
   - `Last_Updated` → 2026-03-12
5. Write back

### PREDICTIONS.tsv — Current (9 cols) → Target (9 cols) — MINOR

**Current:**
```
Pred_ID	Date_Made	Prediction	Confidence	Timeframe	Status	Date_Resolved	Outcome	Notes
```

**Target (HENRY standard):**
```
ID	Prediction	Confidence	Made_Date	Resolve_Date	Status	Result	Invalidation	Notes
```

**Migration steps:**
1. Read current PREDICTIONS.tsv fully
2. Rename columns:
   - `Pred_ID` → `ID`
   - `Date_Made` → `Made_Date`
   - `Timeframe` → `Resolve_Date` (convert "Q2 2026" → "2026-06-30" etc.)
   - `Date_Resolved` → stays (merge with Result)
   - `Outcome` → `Result`
3. Add `Invalidation` column — what would prove each prediction wrong. **Critical column.** BROCK fills on next spawn.
4. Write back

### Also create:
- `workbook/SCHEMA.tsv` — document all column definitions for BROCK's TSVs (reference file)
- `workbook/VX_HISTORY.tsv` — empty with headers, for archiving slow-moving vectors

---

## TASK 2: STATUS.md Prune + Archive

**What:** Get STATUS.md under 250 lines post-inbox-processing. Archive resolved/historical material. Create archive/ folder.

**Steps:**
1. `mkdir -p AGENTS/BROCK/archive/`
2. Read STATUS.md fully
3. Identify sections to archive:
   - **IRAN FINANCIAL TARGETS section** (~50 lines) → move to `domain/sources/IRAN_FINANCIAL_TARGETS_MAR11.md`
   - **PE DRAWDOWNS table** (~10 lines) → move to `workbook/` or archive
   - **Fertilizer/Taiwan sections** → these are HAWK's domain, not BROCK's. If present, remove (they're in HAWK/STATUS)
   - **Any resolved ACTIVE CATALYSTS** → archive to `archive/CATALYSTS_RESOLVED.md`
4. Add `**Last context:**` line at very top (one sentence orientation)
5. Verify `## BOTTOM LINE` section exists at end
6. Target: ≤200 lines (leave room for inbox integration)

**⚠️ Do NOT process inbox signals.** That's Task 5 (BROCK spawn). Just prune structure.

---

## TASK 3: CLAUDE.md Overhaul

**What:** Add all missing behavioral guardrails from HENRY/REGINALD standard.

**Template:** Read `AGENTS/HENRY/CLAUDE.md` as the reference. BROCK's existing CLAUDE.md is already good on domain scope, cross-agent signals, and exit rules. The gaps are in spawn protocol details and operational rules.

**Add/fix (from UPGRADE_PLAN.md checklist):**

1. ✅ Already has `⚠️ #1 RULE: Always WRITE to STATUS.md` — verify
2. ✅ Already has `⚠️ File > verbal` — verify  
3. **ADD: Stale Data Rules section** (after Outbox Protocol):
   ```
   ### Stale Data Rules
   - **VX.tsv:** Skip rows >5 trading days old without fresh data. If >50% stale, note and move on.
   - **STATUS.md values >24h old:** Pull live data via web_search before citing.
   - **REGIME BLOCK:** Maintain a 5-line block in STATUS.md: current default rate trend, gate cascade status, PIK trend, BDC NAV median, narrative phase. Update every session.
   ```
4. **ADD: Output Rules section** (after Stale Data Rules):
   ```
   ## OUTPUT RULES
   - Tables > prose. "APO $100.30 (-5.47%), BDC avg 78¢" — not paragraphs.
   - Update stale rows in STATUS.md rather than appending new sections.
   - STATUS.md stays under 250 lines. Archive to domain/sources/ if growing.
   - Separate SIGNAL (what happened) from INTERPRETATION (what it means).
   - **Source tags on all data points:** [CONF] for confirmed + source + date. [EST] for estimates. No naked numbers.
   - **Prediction ID format:** BRK-xx (e.g., BRK-01, BRK-05). Prevents cross-agent collisions.
   - **Don't maintain stale copies.** If another agent owns a metric (HENRY→VIX, LIQUID→HY OAS, REGINALD→bank CRE), reference their value with [CONF HENRY Mar 6] rather than your own drifting copy.
   ```
5. **ADD: TRADE.md to FILES table:**
   ```
   | `TRADE.md` | Trade targets derived from BROCK analysis — tickers, instruments, catalysts, conviction |
   ```
6. **ADD: BOTTOM LINE requirement** — already in CLAUDE.md, verify it says "every STATUS.md update must end with ## BOTTOM LINE"
7. **FIX: EXPECTED_SIGNALS.md reference** — update FILES table to say `EXPECTED_SIGNALS.md | Signal interpretation guide — methodology and thresholds ONLY, no live data`
8. **VERIFY:** Sub-agent reference removed (grep showed it's already gone ✅)

---

## TASK 4: TRADE.md + EXPECTED_SIGNALS Cleanup

**What:** Create TRADE.md. Clean up EXPECTED_SIGNALS.md.

### TRADE.md

**Template:** Read `AGENTS/HENRY/TRADE.md` for structure (Sections 1-4, vector links, conviction scoring).

**Content source:** Derive from BROCK's STATUS.md positions + convergence matrix:
- APO puts (Apr + Jun) — roll Jun→Dec decision
- OWL $9.5P Apr — cut decision
- BDC sector shorts (via existing positions)
- DB as new liquid proxy (from today's signals)
- Bank CDS / warehouse line plays (conceptual, for BROCK to flesh out)

**Structure:**
```
# BROCK — TRADE.md
**Generated:** [date]
**Convergence:** [score from STATUS.md]
**Status:** [one-line regime]

## SECTION 1: HIGHEST CONVICTION
## SECTION 2: CONDITIONAL / CATALYST-DEPENDENT  
## SECTION 3: WATCHLIST (Not Yet Positioned)
## SECTION 4: EXISTING POSITION ASSESSMENT
```

Each trade needs: Instrument, Direction, Thesis, Catalyst, Entry Zone, Target Exit, Stop/Invalidation, Conviction (1-5), Sizing, Vector Links.

**⚠️ Prome drafts the structure + populates from STATUS.md. BROCK refines on next spawn.**

### EXPECTED_SIGNALS.md Cleanup

1. Read current file fully
2. Verify header says "methodology and thresholds ONLY, no live data"
3. Check for any stale live data that crept back in (the poisoned file problem from MEMORY.md)
4. If clean → leave as-is, it's already been fixed
5. If stale data found → strip it, keep methodology tables only

---

## TASK 5: Spawn BROCK — Inbox Processing + Population

**What:** After Tasks 1-4, spawn BROCK to:
1. Process 4 inbox signals (today's dump)
2. Populate new columns in migrated TSVs (Cross_Links, Analysis, Invalidation, etc.)
3. Update STATUS.md with new data from signals
4. Review TRADE.md draft, add domain expertise
5. Write LESSONS.md if it doesn't exist (it does exist ✅ — review + update)

**Spawn command:**
```
sessions_spawn(agentId="brock", task="...", cleanup="keep")
```

**Task prompt should include:**
- "Your TSVs have been migrated to new schemas — review column headers, populate blank columns"
- "4 signals in inbox — process per protocol"
- "TRADE.md has been drafted — review and refine with your domain expertise"
- "STATUS.md has been pruned — verify nothing critical was archived incorrectly"

---

## Verification Checklist (Post-Migration)

After all 5 tasks, BROCK should have:

| Item | File | Standard |
|------|------|----------|
| ✅ CLAUDE.md with all guardrails | CLAUDE.md | Stale data rules, output rules, source tags, TRADE.md ref |
| ✅ STATUS.md ≤250 lines | STATUS.md | Last context line, BOTTOM LINE, [CONF] tags |
| ✅ VX.tsv 12-col | workbook/VX.tsv | ID, Name, Category, Current_Value, Y, O, R, Status, Confidence, Last_Updated, Source, Cross_Links, Notes |
| ✅ KB.tsv 14-col | workbook/KB.tsv | Full HENRY schema |
| ✅ FLOW.tsv 10-col | workbook/FLOW.tsv | Full HENRY schema |
| ✅ PREDICTIONS.tsv 9-col | workbook/PREDICTIONS.tsv | With Invalidation column |
| ✅ SCHEMA.tsv | workbook/SCHEMA.tsv | Column definitions reference |
| ✅ VX_HISTORY.tsv | workbook/VX_HISTORY.tsv | Archive for slow vectors |
| ✅ TRADE.md | TRADE.md | Sections 1-4, vector links, conviction |
| ✅ EXPECTED_SIGNALS.md clean | EXPECTED_SIGNALS.md | Methodology only, no live data |
| ✅ archive/ folder | archive/ | For resolved material |
| ✅ LESSONS.md current | LESSONS.md | Reviewed post-migration |
| ✅ Inbox clear | mail/inbox/ | All 4 signals processed |

---

## Notes for Future Prome

- **Read this file first** when resuming BROCK migration work.
- **Each task is one session chunk.** Don't try to do multiple in one segment — context gets heavy.
- **Tasks 1-3 are independent** — can be done in any order. Task 4 depends on Task 3 (CLAUDE.md references). Task 5 depends on all others.
- **Don't spawn BROCK during Tasks 1-4.** You're restructuring his files — a concurrent spawn would create conflicts.
- **After Task 5, delete this file and UPGRADE_PLAN.md** — they'll be obsolete.
