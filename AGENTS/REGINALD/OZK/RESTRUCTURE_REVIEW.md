# OZK KB Restructure Plan
**Date:** 2026-03-25 | **Status:** IN PROGRESS

---

## Decision: Use Standard 13-Column TSV

The original review proposed a custom schema (Supersedes, Data_As_Of, Verified tier, markdown pipe-tables). **Overruled** — OZK will use the same 13-column TSV format as all other agents for consistency. The standard schema already handles the review's concerns:

| Review Suggestion | How Standard Schema Handles It |
|---|---|
| Supersedes column | `DerivedFrom` + `Status: SUPERSEDED` + Notes |
| Data_As_Of vs Added_Date | `Date` (when logged) + `Stale_By` (when it expires) |
| Verified tier (PRIMARY/SECONDARY/INFERRED) | `Epistemic` (EMPIRICAL/ESTIMATE/ASSUMPTION) + `Conf` (Admiralty scale) |
| Markdown pipe-table format | TSV — consistent with all agents, playbook exists |

## Schema (Standard 13-Column TSV)

```
ID	Date	Group	Entity	Fact	Source	Conf	Epistemic	Status	Stale_By	DerivedFrom	Vectors	Notes
```

**Reference:** `AGENTS/templates/KB_MIGRATION_PLAYBOOK.md`

### Column Definitions
| Column | Description |
|---|---|
| **ID** | `KB-OZK-NNN` (sequential) |
| **Date** | When the claim was logged (YYYY-MM-DD) |
| **Group** | Vector category (see below) |
| **Entity** | Most specific noun — OZK, IQHQ, Bioterra, FDIC, etc. |
| **Fact** | One atomic citable claim. Sacred — never summarize. |
| **Source** | Primary source citation (filing, API, news) |
| **Conf** | Admiralty scale: A2=primary verified, B2=reputable secondary, C3=derived, D4=unverified, F6=unknown |
| **Epistemic** | EMPIRICAL (direct data), ESTIMATE (derived), ASSUMPTION (framework/thesis) |
| **Status** | ACTIVE, CONFIRMED, SUPERSEDED, STALE, CORRECTED |
| **Stale_By** | Date when data expires (next earnings, next release). Null for static facts. |
| **DerivedFrom** | KB-OZK ID this row was built from. Also used for supersession chains. |
| **Vectors** | VX links + cross-agent refs (→REGINALD, →BROCK) |
| **Notes** | Overflow, context, correction history |

### Group Categories (OZK-specific)
| Group | What Goes Here |
|---|---|
| ACL_THINNING | Reserve adequacy, provision vs charge-offs, coverage ratios |
| CRE_CONCENTRATION | CRE ratios, life sciences, office exposure, concentration risk |
| MATURITY_WALL | 2022 vintage, construction maturities, interest reserves |
| MEMO_ITEM_3 | Hidden CRE in C&I, reclassification evidence, RCON2746 |
| SHADOW_CRE | NDFI exposure ($2.74B), debt-on-debt, counterparty risk |
| MGMT_CREDIBILITY | Insider activity, disclosure patterns, management claims |
| DISTRESSED_LOANS | Specific problem loans — IQHQ, Bioterra, Pacific Center, etc. |
| CAPITAL_LIQUIDITY | Capital ratios, deposits, FHLB, funding, uninsured exposure |
| BULL_COUNTER | Rebuttals, green flags, things that could break the thesis |
| GAP | Known unknowns, unresolved audit items. Conf=F6, Epistemic=ASSUMPTION. |

## What We Kept From the Original Review

These suggestions were good and are incorporated:

1. **GAP as a row type** — gaps live alongside the claims they'd strengthen, not in a separate file
2. **MGMT_CREDIBILITY as a group** — insider signals, disclosure gaps, management language now have a home
3. **LIFE_SCI merged into CRE_CONCENTRATION** — it's a sector within CRE, not a separate vector
4. **NDFI renamed SHADOW_CRE** — more descriptive, matches research files
5. **BULL_COUNTER in same DB** — rebuttals alongside claims, not separated
6. **Quarterly snapshot discipline** — after each earnings, snapshot to `archive/KB_Q1_2026.tsv`
7. **Cross-reference format** — narrative files use `[KB-OZK-NNN]` inline anchors

## What We Changed

1. **TSV not markdown** — consistency with all other agent KBs
2. **Standard 13-column schema** — not custom columns (Supersedes, Data_As_Of, Verified)
3. **Admiralty confidence scale** — not 3-tier Verified (PRIMARY/SECONDARY/INFERRED)
4. **Target 55-60 rows** (up from review's 40) — audit alone has 16 items

## Migration Source

- **Primary:** `EVIDENCE.md` (~40 strongest claims)
- **Secondary:** `AUDIT_REPORT_MAR23.md` (~10-15 gaps + corrections)
- **Backfill (post-earnings):** `research/` files, `sources/` documents

## Files — Do NOT Archive

- `AUDIT_REPORT.md` + `AUDIT_REPORT_MAR23.md` — institutional memory
- `10K_ANALYSIS_2024.md` — primary source extraction
- `TEMPLE8_SHORT_THESIS_MAR2026.md` — external source document
- `EVIDENCE.md` — proto-KB, reference until KB.tsv is fully populated

**Safe to archive after KB populated:** `GAP_CLOSURE_PLAN.md`, `GAP_ANALYSIS_REPORT.md` (findings become KB rows)

## Data Fixes Completed (Mar 25)

| Fix | Status |
|---|---|
| NCO rate mislabeled as "Q4" (was FY2025 annual) | ✅ THESIS.md + SCENARIOS.md corrected |
| YoY multiplier "~8x" (was 3.0x) | ✅ THESIS.md corrected |
| Q4 NCO trajectory "accelerating" (was flat Q3→Q4) | ✅ SCENARIOS.md corrected |
| EARNINGS_PREP.md Temple 8 contamination | ✅ Already clean (verified) |
| EVIDENCE.md stale RCON2746 note | ✅ Already removed |
| EVIDENCE.md 1.06% vs 1.07% noncurrent | ✅ Already fixed |
| Life sciences $3.2B vs $3.1B | ✅ THESIS.md uses $3.1B (confirmed) |

## Still Open (Lower Priority)

| Issue | Status | Notes |
|---|---|---|
| Charge-off $160M vs $172.5M gap | OPEN | Mgmt vs FDIC basis — needs reconciliation note |
| KBRA construction 197% vs FDIC 142% | OPEN | 55pt gap, likely definition difference |
| STATUS.md price ~$49 vs SCENARIOS ~$42-44 | OPEN | Check which is current |
| Dallas PDNA gap methodological circularity | OPEN | Audit E6 — rewrite or remove |
| State-level RC-C noncurrent (B1) | OPEN | Not available in standard call report |
| FHLB borrowing capacity (B4) | OPEN | $23.9B pledged, capacity unknown |

## Execution

**Subagent spawned Mar 25** to build initial KB.tsv from EVIDENCE.md + audit.
- Output: `AGENTS/REGINALD/OZK/workbook/KB.tsv`
- Log: `AGENTS/REGINALD/OZK/workbook/KB_MIGRATION_LOG.md`
- Target: 55-60 rows, 10 groups
- Timeout: 300s

**Post-migration:**
1. Audit row count + column integrity
2. Backfill from research/ files (post-earnings)
3. Quarterly snapshot after Apr 16 earnings → `archive/KB_Q1_2026.tsv`

---

*Schema reference: `AGENTS/templates/KB_MIGRATION_PLAYBOOK.md` | Prior review preserved in git history*
