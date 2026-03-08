# KB Migration Playbook

**Purpose:** Step-by-step instructions for migrating any agent's KB from its legacy schema to the standardized 13-column schema. Written so any session of PROME can pick this up cold.

**Reference:** `AGENTS/CLAUDE_TEMPLATE.md` (canonical schema spec), `AGENTS/VOCABULARIES.tsv` (controlled vocabulary)

---

## Pre-Flight (Once Per Agent)

1. **Back up the original:** `cp KB.tsv KB_old_[N]col.tsv` (where N = current column count)
2. **Count rows:** `wc -l KB.tsv` — confirm expected row count
3. **Check for non-uniform column counts:** `awk -F'\t' '{print NF}' KB_old_[N]col.tsv | sort -u` — if multiple values appear, the file has variant schemas (rows written in different sessions with different formats). Document each variant's column mapping separately before migrating. LABOR had 11-col rows (001-050) and 9-col rows (051-060) with shifted field positions.
4. **Map the old schema to new schema.** Every legacy column must have a destination:

### LABOR (11→13 column mapping)
| Old Column | New Column | Transformation |
|---|---|---|
| ID (`ML-LAB-NNN`) | ID (`KB-LAB-NNN`) | Rename prefix |
| Date | Date | Keep as-is |
| Domain | Group | Keep UPPER_SNAKE. Don't force into VOCABULARIES.tsv yet — preserve original terms, note mapping candidates in Notes |
| Title | Entity | Extract the most specific noun from Title. Title was often a label ("Federal Employment Cuts Untracked") — Entity should be the subject noun ("DOGE" or "Federal_Employment") |
| Description | Fact | Keep verbatim. This is the core claim — do NOT summarize or compress. |
| Vectors | Vectors | Keep as-is |
| Status | Status | Map to allowed enum: ACTIVE/CONFIRMED/STALE/SUPERSEDED/CORRECTED. Legacy values like NEW, CRITICAL GAP, FRAMEWORK, DOCUMENTED → see mapping table below |
| Confidence | → absorbed into Conf | Map HIGH→B2, MEDIUM→C3, LOW→D4, VERY HIGH→A2. These are rough — refine if source is known |
| Source | Source | Keep as-is. Use SOURCE_TAGS from VOCABULARIES.tsv where obvious (e.g., "BLS data" → "BLS") but don't force it |
| Cross-Links | → split into DerivedFrom + Vectors | Agent cross-refs (REGINALD, CARL) → append to Vectors as `→REGINALD`. KB-ID refs → DerivedFrom |
| Notes | Notes | Keep as-is, append any overflow from other field mappings |

### New columns to populate
| New Column | How to fill |
|---|---|
| Conf | Derive from old Confidence + Source quality. See Admiralty mapping above. Default F6 if unclear. |
| Epistemic | Classify each row per the sharpened definitions below. Most BLS/JOLTS rows = EMPIRICAL. Framework/thesis rows = ASSUMPTION. Derived numbers/pattern observations = ESTIMATE. |

**Epistemic classification guide (sharpened after chunk 2):**
- **EMPIRICAL** — directly observed or measured. Data releases, confirmed events, verified company announcements, prices.
- **ESTIMATE** — derived numbers or pattern observations from empirical data. "~580K total layoffs" (aggregation), "surface green / hidden orange-red" (pattern from data points). The claim is built from data but adds a quantitative or observational layer.
- **ASSUMPTION** — interpretive frameworks, thesis claims, analytical models that could be wrong. "Barbell labor market", "bifurcation hypothesis", transmission chain logic. These are *conclusions about how the world works*, not observations of what it's doing. If the framework is wrong, downstream analysis breaks.
- **Test:** Ask "could this be directly falsified by a single data point?" EMPIRICAL = yes. ESTIMATE = partially (the components are empirical but the aggregation adds judgment). ASSUMPTION = no (it's a framing that would require multiple contrary data points to overturn).
- **If HENRY/REGINALD migrations surface cases that don't fit these three, consider adding SYNTHESIS as a fourth type in a single pass across all agents.**
| Stale_By | Set for time-sensitive data ONLY if you know the exact next release/review date. If unsure, leave null — guessed dates are worse than no dates. Stale_By can be backfilled in a dedicated freshness pass. Frameworks/static facts → always null. |
| DerivedFrom | Only if this row was explicitly built from other KB rows. Most will be null. **Direction: child points to parent.** "This fact was built from those facts." Never the reverse. |

### Status mapping (legacy → new)
| Legacy Value | New Value | Rationale |
|---|---|---|
| NEW | ACTIVE | Default active state |
| CONFIRMED | CONFIRMED | Direct match |
| CRITICAL GAP | ACTIVE | It's active intelligence with a gap — note the gap in Notes |
| FRAMEWORK | ACTIVE | Analytical frameworks are active reference material |
| DOCUMENTED | ACTIVE | Documented = recorded = active |
| UPDATED | ACTIVE | Was updated, now current |
| SUPERSEDED | SUPERSEDED | Direct match |
| STALE | STALE | Direct match |
| Any other | ACTIVE | Default, note original status in Notes |

---

## Per-Chunk Execution

### Step 1: Read the chunk
Read the specific rows for this chunk from the OLD file. Do NOT read from a partially-migrated file — always work from `KB_old_[N]col.tsv` as source of truth.

### Step 2: Migrate row by row
For each row, apply the column mapping above. Rules:
- **Fact field is sacred.** Never summarize, compress, or editorialize. Copy verbatim from Description. **Exception:** If the old Title contains quantitative data that would be lost during Entity extraction (e.g., "Ed & Health +12.41% vs Total +4.77%"), prepend that data to the Fact field. Entity should be the short noun; the numbers belong in Fact.
- **Entity extraction requires judgment.** Pull the most specific noun. For position agents (BRENT, REGINALD), Entity is typically a company, country, or instrument. For input/velocity agents (LABOR, HENRY), Entity can be a metric or data series name (NFP, Quits_Rate, U6). Use underscore-joined short names. Lean toward the data subject, not the editorial framing.
- **One atomic claim per row.** If a Description contains multiple distinct claims, flag it but do NOT split it during migration. Splitting is a separate pass.
- **Preserve all cross-references.** VX-LAB links, agent names, KB-ID references — nothing gets dropped.
- **When in doubt, preserve.** Put overflow in Notes rather than dropping content.

### Step 3: Write the chunk
Append the migrated rows to the new KB.tsv. First chunk also writes the header row.

**Header:**
```
ID	Date	Group	Entity	Fact	Source	Conf	Epistemic	Status	Stale_By	DerivedFrom	Vectors	Notes
```

### Step 4: Audit the chunk
After writing, re-read the chunk from the NEW file and verify:
- [ ] Row count matches expected
- [ ] **Final chunk only:** Verify last new ID maps to last old ID (accounting for skips/renumbers). Don't trust row counts alone — confirm the actual last entry wasn't dropped.
- [ ] No data from Fact field was lost or truncated
- [ ] All IDs sequential and renamed (KB-LAB-NNN)
- [ ] All Status values are valid enum
- [ ] All Conf values are valid Admiralty digraph
- [ ] All Epistemic values are EMPIRICAL/ESTIMATE/ASSUMPTION
- [ ] Vectors preserved (count VX refs before/after)
- [ ] No tab characters inside field values (breaks TSV parsing)

### Step 5: Checkpoint
After each chunk, write a checkpoint to `memory/YYYY-MM-DD.md`:
```
## KB Migration: [AGENT] Chunk [N] [HH:MM UTC]
- Rows migrated: [range]
- Issues found: [any problems]
- Cumulative: [X/total] rows complete
```

---

## Post-Migration (Once Per Agent, After All Chunks)

1. **Full audit:** Read entire new KB.tsv. Verify total row count matches original.
2. **Fix ID collisions:** Check for duplicate IDs (LABOR has a known ML-LAB-067 duplicate at rows 30 and 68).
3. **Update SCHEMA.tsv:** Copy from BRENT's workbook/SCHEMA.tsv and adjust agent-specific notes if needed.
4. **Update agent CLAUDE.md:** Ensure KB.tsv references point to 13-column schema, remove any old schema references.
5. **Delete GROUP_MAP.tsv** if one was created (temporary migration artifact).
6. **Conf consistency pass:** Scan for rows with identical claim types but different Conf ratings (e.g., two DHS suppression analyses rated B2 and C3). Harmonize.
7. **Freshness pass (separate session):** Scan for rows that should be STALE or SUPERSEDED based on newer data. Migration preserves original Status — staleness assessment is a post-migration task, not a migration task. But schedule it soon after completing each agent.
8. **Git commit:** `git add -A && git commit -m "KB migration: [AGENT] 13-column complete"`

---

## Known Pitfalls (from BRENT migration)

1. **sed/Edit strips newlines at boundaries.** After any programmatic edit, verify no row concatenation occurred.
2. **Tab-in-field corruption.** If a Fact or Notes field contains a literal tab, it shifts all subsequent columns. Scan with `awk -F'\t' '{print NF}' KB.tsv | sort -u` — all rows should have 13 fields.
3. **Don't read partially-migrated files as source.** Always migrate FROM the backup, write TO the new file.
4. **Chunk 4 of BRENT had 5 minor Fact trims** — 3 were restored. Always compare Fact length old vs new when auditing.
5. **Cross-session continuity.** Each session starts by reading this playbook + the latest checkpoint in daily notes. Don't rely on memory from a previous session.

---

## Chunk Plan: LABOR (81 data rows)

| Chunk | Rows | IDs | Theme |
|---|---|---|---|
| 1 | 1-20 | LAB-001→020 | Foundation + BLS/JOLTS core |
| 2 | 21-41 | LAB-021→041 | Synthesis + secondary indicators |
| 3 | 42-61 | LAB-042→060 | Beige Book + analysts + staffing |
| 4 | 62-81 | LAB-061→081 | Staffing firms + late additions |

**Known issues to fix:**
- ML-LAB-067 appears at row 30 (Domain=CONSUMER) AND row 68 (Domain=CLAIMS). Renumber the row-30 entry during Chunk 2.

---

## Future Migrations

| Agent | Current Schema | Rows | Difficulty | Notes |
|---|---|---|---|---|
| HENRY | 15→13 cols | 89 | Medium | 3-letter category codes need expansion. Session column dropped. Analysis/Data_Quote merge into Fact. |
| REGINALD | 15→13 cols | 116 | Hard | Data corruption in Category field (full sentences). Largest KB. Most cross-refs. |

Each agent will need its own column mapping table added to this playbook before starting.
