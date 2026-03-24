# OZK — Workbook

The canonical knowledge base. KB.tsv is the single source of truth for all verified facts in the OZK thesis.

---

## File Instructions

### KB.tsv
**This is the most important file in the OZK tree.** Every factual claim in THESIS.md, WEAKNESSES.md, or research files should trace back to a KB row.

**Schema:**
`ID | Date | Group | Entity | Fact | Source | Conf | Epistemic | Status | Stale_By | DerivedFrom | Vectors | Notes`

**Rules:**
- **IDs are permanent.** `KB-OZK-001` always means the same thing. Never reuse or renumber.
- **Sequential numbering.** New entries get the next available number.
- **Confidence grades:** A1 (verified primary), A2 (primary with minor uncertainty), B1 (strong secondary), B2 (estimate/derived), C (unverified/single-source)
- **Stale_By dates matter.** Quarterly data goes stale when next quarter drops. Check before citing anything past its stale date.
- **Status:** ACTIVE (current), SUPERSEDED (replaced by newer entry), CORRECTED (was wrong — see Notes)
- **Never delete rows.** Mark as SUPERSEDED or CORRECTED instead. The history matters.

**Groups:** ACL_THINNING, CRE_CONCENTRATION, LIFE_SCI, MATURITY_WALL, MGMT_CREDIBILITY, BULL_COUNTER, MEMO_ITEM_3, IQHQ, REGULATORY

### KB_MIGRATION_LOG.md
Historical record of structural changes to KB.tsv (schema changes, bulk corrections, renumbering). Don't delete.

---

*Thesis → `../THESIS.md` | Sources → `../sources/` | Research → `../research/`*
