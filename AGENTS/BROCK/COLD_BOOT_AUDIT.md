# COLD_BOOT_AUDIT.md — BROCK UX Audit
**Auditor:** Fresh BROCK subagent (cold-boot simulation)
**Date:** 2026-03-13
**Method:** Followed boot sequence as documented in CLAUDE.md, read all referenced files, took notes throughout.

---

## Overall Assessment

BROCK's file system is one of the better-designed agent setups in this network. CLAUDE.md is clear, LESSONS.md is genuinely useful, and the workbook split (KB/VX/FLOW/PREDICTIONS) is smart. The STATUS.md is dense but navigable.

But there are real problems. Some are silent landmines for a cold-boot agent. Spend tokens on those below.

---

## 1. CONTRADICTIONS

### 1A. Convergence Score: 47/55 vs 51/55 (CRITICAL)
- **STATUS.md** (primary memory): `Convergence: 47/55 🔴🔴`
- **TRADE.md** (generated same day, Mar 12): `Convergence: 51/55 🔴🔴`

Same date, same session, different scores. A fresh BROCK opening both files sees conflicting authority. Which is ground truth? If TRADE.md was written first and STATUS.md was subsequently updated (or vice versa), one is stale. There's no version note, no explanation.

**Impact:** A BROCK spawn checking trade conviction against STATUS.md will get inconsistent reads. The 4-point difference represents meaningful divergence in urgency framing.

**Fix:** Single line at top of TRADE.md: `[Convergence score as of generation — verify against STATUS.md before trading]`. Or ensure both files are updated atomically.

---

### 1B. BROCK's Place in the Hierarchy: Sub-Agent vs Peer
- **AGENTS_DIRECTORY.md**: `Subs: CREED (CRE), BROCK (BDC) 🟠, CORAL (FL condos) 🟠` — lists BROCK as a REGINALD sub-agent
- **BROCK CLAUDE.md**: BROCK signals REGINALD (`Signals REGINALD...`), receives signals from REGINALD as peer (`You receive from: REGINALD: Bank-level exposure data`)
- **EXPECTED_SIGNALS.md.bak** (old file, still readable): `Parent: REGINALD`

BROCK's own CLAUDE.md treats the relationship as a lateral peer-signal setup (BROCK→REGINALD and REGINALD→BROCK). AGENTS_DIRECTORY.md says BROCK is a REGINALD subordinate. These are operationally different: a sub-agent has different protocol expectations than a peer lateral.

**Impact:** If Prome or another agent routes something to "REGINALD and subs," BROCK should receive it. But BROCK may not know to watch REGINALD's STATUS.md as a parent. Ambiguous authority relationship.

**Fix:** AGENTS_DIRECTORY.md needs to be updated to reflect actual current topology. If BROCK is now a peer, remove from REGINALD's sub list. If BROCK is still a sub, add a section to CLAUDE.md explaining what that means operationally.

---

### 1C. OTTO in Role Header vs Absent from Outbound Signal Table
- **CLAUDE.md role line**: "Signals REGINALD (bank warehouse lines), LIQUID (fund finance/credit), OTTO (BDC-specific)"
- **CROSS-AGENT SIGNALS outbound table**: REGINALD, LIQUID, LABOR, HAWK, ALL — OTTO is absent

The role description says BROCK signals OTTO. The operations table that a spawn would actually use to decide when to file outbox mail has no OTTO entry. No conditions, no priority, no trigger.

**Impact:** BROCK might never file a signal to OTTO because there's no row telling it when to.

**Fix:** Either add OTTO row to the outbound signals table (with specific trigger conditions), or remove "OTTO" from the role description header.

---

## 2. DEAD REFERENCES

### 2A. ML.tsv Listed in FILES Table as workbook/ML.tsv — Doesn't Exist There
- **CLAUDE.md FILES table**: `workbook/ML.tsv | DEPRECATED. Historical event log (ML001-ML011). KB.tsv now serves this purpose.`
- **Actual location**: `archive/ML_DEPRECATED.tsv`
- `workbook/ML.tsv` → does not exist

A fresh spawn following the FILES table to understand the workbook schema will find the path broken. The "DEPRECATED" label helps, but the path is still wrong.

**Fix:** Update FILES table path to `archive/ML_DEPRECATED.tsv` or just delete the row since it's deprecated.

---

### 2B. Missing BRK-15 in PREDICTIONS.tsv
PREDICTIONS.tsv sequences: BRK-14 → BRK-16 (no BRK-15). No comment, no explanation.

**Impact:** If cross-agent signals or PROME reference BRK-15, nothing will resolve. If it was intentionally deleted, the gap creates confusion.

**Fix:** Add a tombstone row: `BRK-15 | [DELETED] | N/A | ... | SUPERSEDED | Replaced by BRK-XX` or renumber.

---

### 2C. SHADE Agent Invisible to BROCK
- **AGENTS_DIRECTORY.md**: `SHADE = insurance plumbing under BROCK/REGINALD | feeds LIQUID on systemic`
- **BROCK CLAUDE.md**: Zero mentions of SHADE

BROCK owns the Athene/insurance/ILS domain. SHADE is described as "insurance plumbing under BROCK/REGINALD." But BROCK has no awareness of SHADE in its spawn protocol, signal table, or domain scope. BROCK doesn't know to receive from SHADE or route insurance findings to it.

**Fix:** Add SHADE to BROCK's "You receive from" section with a description of what SHADE provides, or clarify that SHADE is a Prome-level tool BROCK doesn't interact with directly.

---

## 3. CONFUSION POINTS

### 3A. Two Inbox Directories (CONFUSING)
- `AGENTS/BROCK/inbox/` — exists, has `processed/` subdirectory, appears to be legacy
- `AGENTS/BROCK/mail/inbox/` — current system per CLAUDE.md ("All mail lives in `mail/`")

Both directories are empty currently, but both have `processed/` subdirs. A cold-boot BROCK doing inbox processing might look in the wrong place. CLAUDE.md says "All mail lives in `mail/`" which is clear — but the presence of a top-level `inbox/` is a trap.

**Fix:** Either delete `AGENTS/BROCK/inbox/` (legacy) or add a README.md in it: `DEPRECATED. Mail moved to mail/inbox/. Do not use.`

---

### 3B. Hamilton Framework Referenced in TRADE.md — Not Defined in Any BROCK File
TRADE.md references "Hamilton" 8+ times: "Hamilton lag structure," "Hamilton: Lag 4," "Hamilton lag framework." This framework drives major trade duration decisions (Jun vs Dec expiry). But BROCK's CLAUDE.md, STATUS.md, LESSONS.md, and EXPECTED_SIGNALS.md all have zero definition or reference to Hamilton.

The framework lives in: HENRY's processed inbox, FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md (not verified to exist), and PROME's BOOT_AUDIT_4.md.

A cold-boot BROCK reading TRADE.md needs to know: Hamilton = James Hamilton oil-GDP model, peak damage at lag 4 (Q1 2027 from Q1 2026 shock). Without this, the entire expiry rationale in TRADE.md is opaque.

**Fix:** Add 3-4 line Hamilton summary to LESSONS.md or a `## FRAMEWORKS` section in CLAUDE.md. Don't require BROCK to read HENRY's inbox to understand its own trades.

---

### 3C. Sources Directory Duplication
- `AGENTS/BROCK/sources/` — exists, has content (5+ research files including auto delinquency data, bankruptcy CSVs)
- `AGENTS/BROCK/domain/sources/` — exists, has content (Eisman transcript analysis, FDIC chart, STATUS archive)

CLAUDE.md says `domain/sources/` is for "Research archives, STATUS backups, deep analysis." Top-level `sources/` isn't mentioned anywhere in CLAUDE.md.

A spawn asked to save research doesn't know which to use. Some files ended up in the wrong place.

**Fix:** Migrate top-level `sources/` content to `domain/sources/` and delete the empty directory. Add a note in FILES table clarifying `domain/sources/` is the only research archive.

---

### 3D. STATUS.md Convergence Vector Names Don't Match VX.tsv Names
- STATUS.md convergence matrix uses names like "Fund Gate Cascade," "Blue Owl Liquidity," "Mainstream Narrative"
- VX.tsv uses names like "Fund Gates Count (confirmed)," "Blue Owl (OWL) Fund Liquidity," "Mainstream Narrative Convergence"

Near-matches, not exact. A spawn running a workbook update would have to fuzzy-match across the two systems. No explicit cross-reference (e.g., "BCRED Redemptions → VX-BRK-001").

**Fix:** Add VX IDs to STATUS.md convergence table as a column: `| BCRED Redemptions | 🔴 (4) | ... | VX-BRK-001 |`. Makes the connection explicit.

---

## 4. MISSING CONTEXT

### 4A. BROCK's Relationship to OTTO is Ambiguous
CLAUDE.md role section says BROCK signals OTTO. The "You receive from" section says BROCK receives from OTTO ("BDC earnings data, regulatory signals"). Both can be true — lateral peer with bidirectional flow. But there's no explanation of OTTO's domain or how the two agents coordinate. A fresh BROCK doesn't know: does OTTO own BDC earnings and hand to BROCK, or does BROCK own them and OTTO reports upstream?

**Fix:** One sentence in CLAUDE.md: "OTTO is an event-driven agent that monitors BDC earnings filings; BROCK consumes OTTO's earnings data and provides macro context in return."

---

### 4B. `ARCHITECTURE_AUDIT.md`, `SELF_AUDIT.md`, `MIGRATION_PLAN.md`, `UPGRADE_PLAN.md` Are Invisible
These four files live in BROCK's root directory. None appear in the FILES table. A cold-boot spawn following CLAUDE.md boot sequence will never read them.

SELF_AUDIT.md in particular is valuable — it's a prior BROCK's self-assessment of the instruction set quality. It would help cold-boot agents rapidly calibrate to what's working.

**Fix:** Either add entries to the FILES table for each file, or (better) archive MIGRATION_PLAN and UPGRADE_PLAN to `archive/` (they're point-in-time plans, likely stale), and add a line to CLAUDE.md: "See `SELF_AUDIT.md` for prior spawn quality notes."

---

### 4C. LABOR as a Recipient but Not a Sender
CROSS-AGENT SIGNALS outbound table includes LABOR as a target. But LABOR is absent from the "You receive from" list. If BROCK monitors "portfolio company layoff spike" (which is a LABOR-domain signal), shouldn't BROCK receive from LABOR when layoffs actually happen?

**Fix:** Either add LABOR to "You receive from" with a brief description ("LABOR: employment stress signals, NFP data, layoff spikes relevant to sponsor portfolio companies"), or explain why BROCK doesn't need LABOR's output directly.

---

## 5. REDUNDANCY

### 5A. Exit Rules in Both CLAUDE.md and STATUS.md
Exit rules (Thesis Kill, Position-Specific, Convergence Downgrade, Time-Based) appear in CLAUDE.md as the definitive framework AND are copy-pasted into STATUS.md. They already differ slightly (CLAUDE.md has more detailed phrasing in places).

**Risk:** Next spawn updates STATUS.md exit rules without touching CLAUDE.md. Now they diverge permanently. One becomes stale.

**Fix:** STATUS.md should say `## EXIT RULES — See CLAUDE.md for definitions. Live status: [any recent changes noted here]` and not duplicate the full text. Or pick one canonical location and reference the other.

---

### 5B. Cross-Agent Signal Conditions in Three Places
1. CLAUDE.md CROSS-AGENT SIGNALS table
2. EXPECTED_SIGNALS.md "Cross-Agent Signal Rules" section
3. FLOW.tsv (transmission pathways that imply signals)

The conditions aren't identical across all three. EXPECTED_SIGNALS.md is described as "thresholds only — no live data" but it repeats the signal conditions from CLAUDE.md.

**Fix:** EXPECTED_SIGNALS.md's "Cross-Agent Signal Rules" section can be replaced with: "See CLAUDE.md → CROSS-AGENT SIGNALS for routing conditions." Keeps EXPECTED_SIGNALS focused on threshold interpretation (its stated purpose).

---

### 5C. Old Schema Files in workbook/
`VX_old_11col.tsv`, `KB_old_7col.tsv`, `FLOW_old_6col.tsv`, `PREDICTIONS_old_9col.tsv` are schema migration artifacts. No cleanup timeline, no note on why they're kept (reference? rollback safety?).

**Fix:** Add `## MIGRATION ARTIFACTS` note to workbook README (or SCHEMA.tsv header): "Old-col files retained for reference during Mar 2026 schema migration. Delete after Q1 2026 earnings cycle confirms schema stability."

---

## 6. SUGGESTED IMPROVEMENTS

### Priority 1: Fix the Convergence Score (CLAUDE.md or TRADE.md)
Add one line to TRADE.md header: "Convergence at time of writing: 51/55. Always verify against STATUS.md before executing." Prevents a spawn from acting on a stale score.

### Priority 2: Add Hamilton Framework to LESSONS.md
Three lines. Something like:
> **Hamilton Oil-GDP Lag Framework (from HENRY):** James Hamilton NOPI model. Sustained oil shock → GDP drag -3.0 to -4.9pp at lag 4 (4 quarters from shock initiation). Q1 2026 shock → peak Q1 2027. Credit spreads peak 3-14mo post shock, BEFORE equity trough. Implication: Jun put expiries capture <1/3 of damage — Dec minimum. Full detail: HENRY/STATUS.md or FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md.

This alone would make TRADE.md navigable for a cold-boot BROCK.

### Priority 3: Add VX IDs to STATUS.md Convergence Table
One column. Immediate cross-reference between STATUS.md and VX.tsv. No more fuzzy-matching.

### Priority 4: Resolve the Inbox Directory Confusion
Delete or tombstone top-level `AGENTS/BROCK/inbox/`. Takes 30 seconds.

### Priority 5: Update AGENTS_DIRECTORY.md Hierarchy
Either remove BROCK from REGINALD's sub list or formally acknowledge the hierarchical vs peer ambiguity. One sentence of clarification prevents routing errors.

### Priority 6: Tombstone BRK-15
One row in PREDICTIONS.tsv explaining the gap. Prevents "did I miss something?" confusion.

---

## What's Well-Designed (Brief)

- **CLAUDE.md spawn protocol** — numbered steps, explicit task boundaries, clear file table. Excellent.
- **Source tagging (`[CONF]`/`[EST]`)** — enforced consistently in STATUS.md. Best practice.
- **Convergence matrix** — single-line summary with score makes triage fast.
- **LESSONS.md** — real lessons, not platitudes. PSEC PIK correction is exactly the kind of thing that prevents hallucination repeat.
- **Exit rules structure** — four categories with specific conditions and cross-references. Actually falsifiable.
- **Workbook file split** — each file has a distinct purpose. Good architecture.
- **FLOW.tsv** — transmission pathways with timing, status (FIRED/BUILDING), and vector links. Underrated file.

---

*End of audit. Files read: CLAUDE.md, STATUS.md, LESSONS.md, EXPECTED_SIGNALS.md, TRADE.md, workbook/VX.tsv, workbook/KB.tsv (header), workbook/PREDICTIONS.tsv, workbook/SCHEMA.tsv, workbook/FLOW.tsv (partial), AGENTS_DIRECTORY.md, AGENTS.md, mail/PROTOCOL.md. Cross-checked: SELF_AUDIT.md, ARCHITECTURE_AUDIT.md, AGENTS/VOCABULARIES.tsv (headers).*
