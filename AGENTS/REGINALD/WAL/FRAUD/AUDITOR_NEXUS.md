# WAL Auditor & Gatekeeper Nexus — Complete Findings
**Created:** 2026-03-27
**Sources:** PCAOB inspection reports, SEC enforcement actions, EDGAR filings, Gotham City Research (Jan 28 2026)

---

## Summary

WAL's three fraud vectors all failed at the gatekeeper level. This doc maps the audit firms across the fraud cluster and finds WAL's own auditor (RSM) has documented deficiencies in exactly the areas that matter.

---

## The Auditor Map

| Entity | Auditor | Fraud Status | WAL Connection |
|--------|---------|-------------|----------------|
| **Western Alliance (WAL)** | **RSM US LLP** | 3 active fraud vectors | Direct — RSM signs off on WAL's reserves + collateral |
| **Tricolor** | **Grant Thornton** | DOJ indicted, $800M fraud | WAL exposure via NDFI/warehouse/BDC |
| **Carvana/DriveTime/GoFi** | **Grant Thornton** | SEC subpoena; Gotham alleges fraud | WAL auto/NDFI exposure |
| **First Brands Group** | **BDO USA** | DOJ indicted, $9.3B+ | WAL exposure via Jefferies/Point Bonita |
| **Zions (ZION)** | Ernst & Young | Stupin victim — charged off 83% | Same fraud ring as WAL Vector 3 |

Three different audit firms (RSM, GT, BDO) all failed to catch collateral fraud across this cluster. Not a single-firm problem — a systemic gatekeeper failure.

---

## RSM US LLP — WAL's Auditor

### PCAOB Deficiency History

| Year | Audits Reviewed | Deficiencies | Rate |
|------|----------------|-------------|------|
| 2024 | 17 | 7 | **41%** |
| 2023 | 17 | 8 | **47%** |
| 2022 | 17 | 4 | 24% |
| 2021 | 17 | 4 | 24% |
| 2020 | 15 | 7 | **47%** |
| 2017 | 15 | 11 | **73%** |

### 🔴 Critical Finding: "Issuer B – Financials" (2024 PCAOB Report)

RSM audited a financial institution that purchased collateralized loans at a discount. PCAOB found:

1. **Collateral verification failure** — RSM failed to evaluate reasonableness of significant assumptions used by company specialists to develop collateral fair values. They only inquired of management and read specialist-prepared information WITHOUT independent testing. (AS 1105.A1-.A10; AS 2501.16)
2. **Fair value measurement failure** — Failed to evaluate reasonableness of adjustment factors used as inputs for significant estimates. Failed to evaluate relevance of certain data used.
3. **Controls testing failure** — Didn't evaluate the specific procedures the control owner performed.

**Direct relevance to WAL:** This is exactly how collateral fraud goes undetected — the auditor accepts management's representations about collateral values without independent verification. WAL's Stupin fraud involved forged title policies. WAL's internal review found "no additional irregularities" — but if RSM's verification method is "ask management and read what they give us," that review is circular.

### Allowance for Credit Losses (ACL)

PCAOB reviewed ACL in **2 RSM audits** in 2024. **Both had deficiencies.** 100% fail rate on the specific procedure that determines whether WAL's 30% reserve on Stupin (vs ZION's 83% charge-off) is adequate.

### SEC Enforcement History

| Year | Action | Detail |
|------|--------|--------|
| 2022 | SEC charges + **$3.75M fine** | Improper professional conduct — 2 partners + 1 senior manager |
| 2019 | SEC censure + **$950K fine** | Auditor independence violations across **100+ audit reports, 15+ clients** |
| 2020 | **$17M settlement** | Professional negligence (Physicians United Plan) |
| 2006 | **$41.5M settlement** | Business fraud class action |

### WAL Is RSM's Outlier Client

RSM's confirmed bank clients are almost exclusively community banks under $20B in assets:
- International Bancshares (IBOC) — ~$15B (their largest)
- Bridgewater Bancshares — ~$8B
- Bar Harbor Bankshares — ~$4B
- Community banks in the $3-5B range

**WAL at $80B+ is 5x larger than RSM's next-biggest bank client.** WAL's complexity (NDFI, SSFA structures, warehouse lending, specialty finance, three active fraud vectors) far exceeds anything else in RSM's bank audit practice. This raises the question: does RSM have the institutional capability to audit a bank this complex?

---

## Grant Thornton — Counterparty Auditor

### GT Client Map
- **Tricolor** — auditor 2023-2024. Hired after Crowe raised concerns. Gave clean opinions during $800M fraud.
- **Carvana** — current auditor. 10-K filed on time (Feb 18 2026). No resignation as of Mar 27.
- **DriveTime** — current auditor. Common control with CVNA (Garcia family).
- **GoFi LLC** — current auditor. Garcia family entity.

### Gotham Predictions vs Reality (as of Mar 27 2026)
| Prediction | Status |
|-----------|--------|
| GT will resign from Garcia entities | ❌ Not yet |
| CVNA 10-K delayed | ❌ Filed on time Feb 18 |
| Financials require restatement | ⏳ Pending |
| SEC enforcement action | ⏳ Pending (subpoena confirmed Jun 2025) |

### No Direct GT→WAL Link in Public Filings
EDGAR full-text search found zero SEC filings containing both "Grant Thornton" and "Western Alliance." The connection runs through private companies (Tricolor SPVs, warehouse borrowers) that don't file with the SEC. **The opacity is itself the risk factor.**

---

## BDO USA — First Brands Auditor

BDO USA audited First Brands Group before Chapter 11 (Sept 28 2025). BDO faces scrutiny for failing to detect ~$12B in undisclosed off-balance-sheet debt. A second firm (BMF, Ohio-based) also had an audit/accounting role.

No direct BDO→WAL link found in public filings. First Brands is private (KPS Capital portfolio company).

---

## The Gatekeeper Failure Thesis

| Fraud Vector | Gatekeeper | Failure Mode |
|-------------|-----------|-------------|
| Stupin/Cantor | Title insurance + RSM (WAL's auditor) | Forged titles accepted; RSM signed off on 30% reserve |
| First Brands | BDO USA + servicer/SPV | BDO missed $12B off-balance-sheet; perfection lapsed |
| Tricolor | Grant Thornton | Clean opinions during $800M double-pledging |
| W&D "systemic" | CRE originators/appraisals | Inflated NOI industry-wide |

**Thesis:** Late-cycle fraud epidemics overwhelm gatekeepers simultaneously. WAL's underwriting model outsources verification to these gatekeepers. When they all fail at once — which is what's happening — WAL's portfolio quality is unverifiable. The market hasn't connected that WAL's own auditor (RSM) has the worst PCAOB track record of any firm in this cluster, with specific deficiencies in collateral verification at financial institutions.

---

## Apr 21 Earnings — Key Questions

1. Has RSM issued any Critical Audit Matters (CAMs) related to collateral verification or fraud exposure?
2. Did RSM perform independent collateral verification on the Stupin portfolio, or rely on WAL's internal review?
3. Will RSM's opinion on WAL's ACL methodology address the 30% vs 83% reserve gap with ZION?
4. Has WAL's audit committee discussed auditor adequacy given the bank's growth and complexity?
5. Is WAL considering a Big 4 auditor transition? (This would itself be a signal.)

---

## Canonical References
- `GRANT_THORNTON_NEXUS.md` — original GT analysis (superseded by this doc)
- `STUPIN_CRE.md` — auditor liability section
- `TRICOLOR.md` — GT thread
- `RQ-REG-A02B` — forensic insurance/auditor analysis
- OTTO: `Gotham_CVNA_Main_Report_2026-01-28.txt` — GT section
