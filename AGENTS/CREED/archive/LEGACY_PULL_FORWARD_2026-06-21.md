# CREED Legacy Pull-Forward — 2026-06-21

**Purpose:** preserve high-value legacy CREED mechanisms from the old REGINALD sub-agent tree without moving/deleting that tree or treating stale Jan/Feb 2026 values as current.

**Legacy source archive:** `AGENTS/REGINALD/sub-agents/CREED/`  
**Current CREED source pack:** `AGENTS/CREED/research/REFRESH_2026-06-21.md`  
**Current thesis rails:** `AGENTS/CREED/thesis/THESIS.md`

---

## Bottom Line

Do **not** wholesale copy the old CREED tree into current CREED. The useful material is not the stale dashboards; it is the **mechanism library**:

- maturity-default / refinancing-gap logic
- special-servicing recognition mechanics
- bank-vs-CMBS delinquency reconciliation
- modification / re-default / extend-and-pretend exhaustion
- forced-sale / private-NAV cascade
- sponsor capitulation framework
- insurance-cost DSCR amplifier
- lease-expiration vacancy ratchet

All legacy levels and dates are stale unless refreshed against current sources.

---

## Pull-Forward Inventory

### 1. Mechanism maps — preserve

Legacy files:
- `AGENTS/REGINALD/sub-agents/CREED/workbook/FLOW.tsv`
- `AGENTS/REGINALD/sub-agents/CREED/workbook/KB.tsv`

High-value mechanisms:

| Legacy flow | Pull-forward use | Current owner / route |
|---|---|---|
| CRE Doom Loop | Vacancy → value decline → LTV breach → modification → re-default → recognition → provisions | CREED → REGINALD |
| Maturity Wall Cascade | Maturities force refinance at lower values; failed refi forces appraisals/NAV marks | CREED → REGINALD + LIQUID |
| Open-End Fund NAV Cascade | Redemptions/gates/forced sales reveal market-clearing values and pressure peer marks | CREED → LIQUID / REITS |
| HOA Super-Lien Cascade | Condo/special-assessment stress can impair bank collateral recovery | CORAL primary; CREED only national/credit context |
| Extend-and-Pretend Collapse | Mods expire/exhaust; re-defaults force charge-offs/provisions | CREED → REGINALD |
| Lease Expiration Vacancy Ratchet | Tenant downsizing at rollover creates vacancy/NOI/DSCR ratchet | CREED → REGINALD / CARL |

Action:
- Preserve as conceptual mechanism library.
- Do not import stale status labels directly.
- Convert into current tracker only after refreshing metrics.

---

### 2. Vector framework — preserve schema, refresh values

Legacy file:
- `AGENTS/REGINALD/sub-agents/CREED/workbook/VX.tsv`

Useful vector categories:

| Category | Legacy vectors worth retaining | Current treatment |
|---|---|---|
| Delinquency | Office CMBS DQ, Bank CRE DQ, Multifamily CMBS DQ, Office vacancy | Refresh monthly/quarterly before use |
| Modifications | CRE mod volume, re-default rate, modification backlog | High priority for bank-recognition timing |
| Valuation | Office price index, cap-rate bid/ask, transaction volume, Chicago price discovery | Use as forced-sale / price-discovery tracker |
| Maturity | CRE maturity wall, CMBS maturity default rate, office lease expiration, 2028 extension concentration | Core CREED timing rails |
| Funds | Open-end fund hidden losses, redemption queues, CRE CLO issuance | Route funding/NAV cascade to LIQUID |
| Regional | HOA/condo assessments, office-to-resi conversion, DC/DOGE, local bank canaries | Route Florida to CORAL; bank canaries to REGINALD |

Action:
- If CREED builds a workbook, use `VX.tsv` as a schema seed only.
- Label any imported legacy vector values as `[STALE: Jan/Feb 2026]`.

---

### 3. Expected signals — partially absorbed, keep as archive

Legacy file:
- `AGENTS/REGINALD/sub-agents/CREED/EXPECTED_SIGNALS.md`

Already absorbed into current rails:
- office CMBS stress re-acceleration
- maturity-default wave confirmation
- bank CRE convergence
- modification exhaustion / re-default
- multifamily term-default broadening
- forced-sale / private-NAV recognition
- AI office-demand risk as secondary accelerator

Current file:
- `AGENTS/CREED/thesis/THESIS.md`

Action:
- Keep legacy expected-signals file as source archive.
- Do not copy it verbatim; current signals supersede it.

---

## Research Files Worth Reusing

### Highest-value durable frameworks

| Legacy file | Why it matters | Pull-forward disposition |
|---|---|---|
| `research/RQ-CREED-001_BANK_DQ_RECONCILIATION.md` | Clarifies bank CRE DQ series vs CMBS comparability | Use for REGINALD handoff / bank-convergence tracker |
| `research/RQ-CREED-003_REFINANCING_GAP.md` | Frames the capacity gap behind maturity-default pressure | Use for maturity/refi framework; refresh numbers |
| `research/RQ-CREED-007_SPECIAL_SERVICING.md` | Explains special-servicing rates, timelines, loss severities, outcomes | Use for recognition mechanics; refresh rates/loss data |
| `research/RQ-CREED-008_BANK_MOD_DISCLOSURES.md` | Modification disclosures and re-default mechanics | Use for extend-and-pretend exhaustion tracker |
| `research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md` | Strategic default / price-discovery pattern | Use for forced-sale recognition framework |
| `research/RQ-CREED-012_INSURANCE_CRE_AMPLIFIER.md` | Insurance as NOI/DSCR amplifier | Keep as CREED↔CORAL bridge; refresh sources |
| `research/RP-CREED-8_Sponsor_Capitulation_Framework_2026-02-11.md` | Sponsor negative-carry / liquidity exhaustion framework | Use as multifamily/sponsor capitulation framework |
| `sources/RP-CREED-9_Office_Lease_Wall_Analysis.md` | Lease-wall / vacancy ratchet mechanics | Use for office demand/lease rollover tracker |

### Useful but route carefully

| Legacy file | Route |
|---|---|
| `research/RQ-CREED-004_SUNBELT_MF_DEEP_DIVE.md` | CREED + CARL; CORAL only if Florida-specific |
| `research/RQ-CREED-005_FL_CONDO_CRISIS.md` | CORAL primary; CREED only for national/credit context |
| `sources/RP-CREED-10_DC-DOGE-Federal-Employment-CRE-Impact.md` | CREED regional case study + REGINALD bank canaries |
| `sources/RP-CREED-10_DC_OFFICE_FEDERAL_WORKFORCE.md` | CREED regional case study + REGINALD bank canaries |
| `sources/RP-CREED-11_MF_DEMAND_STRESS.md` | CREED + CARL multifamily bridge |

### Do not pull forward as current

| Legacy file/type | Reason |
|---|---|
| `AGENTS/REGINALD/sub-agents/CREED/STATUS.md` | Stale Jan/Feb 2026 dashboard; useful only as history |
| `sources/CMBS_DELINQUENCY.md` | Old tracking workbook; current Trepp data lives in Phase 3 refresh |
| `sources/CRE_MATURITY.md` | Old maturity tracker; useful framework but stale values |
| PDFs such as `VLY_Q4_2025_*.pdf` | Keep in legacy archive unless REGINALD needs bank-specific filing evidence |

---

## Candidate Current CREED Tracker Design

If CREED later builds a live workbook, seed it from legacy categories but do not import stale levels:

| Tracker | Cadence | Primary source | Route |
|---|---|---|---|
| CMBS delinquency by property type | Monthly | Trepp | REGINALD/NEXUS |
| Special servicing by property type | Monthly | Trepp | REGINALD/LIQUID |
| Maturity-default share / hard maturities | Monthly/quarterly | Trepp/Morningstar DBRS | REGINALD/LIQUID |
| Bank non-owner CRE PDNA by size | Quarterly | FDIC QBP | REGINALD |
| Bank reserve coverage vs noncurrent CRE | Quarterly | FDIC / filings | REGINALD |
| Modifications / re-defaults | Quarterly | bank filings / servicer data | REGINALD |
| Forced sales / appraisal cuts | Event-driven | CRED iQ / Trepp / filings / news | LIQUID/REGINALD |
| Open-end fund queues/gates | Quarterly/event | ODCE/fund reports | LIQUID |
| Multifamily term defaults | Monthly/quarterly | Trepp / apartment data | CARL |
| Insurance DSCR amplifier | Quarterly/event | insurance/NOI sources | CORAL/REGINALD |

---

## Current Pull-Forward Decisions

- **Do not move or delete** `AGENTS/REGINALD/sub-agents/CREED/`.
- **Do not copy full legacy tree** into top-level CREED.
- **Do preserve** this pull-forward map so current CREED can discover the useful legacy frameworks.
- **Do refresh** all trade-relevant numbers before use.
- **Do route** domain overlap:
  - bank provisions/loss recognition → REGINALD
  - Florida condo/insurance/geography → CORAL
  - maturity/refi/funding/NAV cascades → LIQUID
  - multifamily/household spillovers → CARL

---

## Next Optional Work

1. Create a live CREED tracker template from legacy vector categories.
2. Build a monthly CMBS/special-servicing update process.
3. Create REGINALD handoff note for bank-convergence watch.
4. Create CORAL handoff note for Florida-only legacy findings.
5. Leave Phase 6 migration dormant unless old path confusion becomes a real problem.
