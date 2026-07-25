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

## PCAOB "Issuer B" — High Confidence = WAL

**Source:** PCAOB Release No. 104-2025-100 (May 22, 2025)
**PDF:** https://assets.pcaobus.org/pcaob-dev/docs/default-source/inspections/reports/documents/104-2025-100-rsm.pdf

Issuer B is described as a financial institution that "purchased certain collateralized loans at a discount" and "engaged specialists to estimate fair value of these loans' underlying collateral" to determine whether discounts were "accretable." This is a textbook description of WAL's ~$2B Note Finance division. No other RSM bank client (all <$16B) operates at this scale in purchased distressed loans.

**What PCAOB found RSM failed to do:**
1. Did NOT evaluate reasonableness of significant assumptions used by company specialists for collateral fair values — only inquired of management and read specialist-prepared info
2. Did NOT evaluate relevance of certain data used to develop adjustment factors for impairment
3. Did NOT evaluate the specific review procedures the control owner performed
4. Did NOT perform adequate procedures regarding the work of company's specialists as audit evidence

**Confidence that Issuer B = WAL: HIGH**

---

## WAL FY2025 10-K — RSM Audit Opinion (Filed Feb 23, 2026)

### Opinion: Clean / Unqualified
RSM issued unqualified opinion on both financial statements AND ICFR. **No going concern. No emphasis-of-matter. No qualified language.** Dated Feb 20, 2026. RSM has been WAL's auditor since 1994 (32 years).

### Critical Audit Matters: Weak
- **CAM 1 (ACL):** Generic — about qualitative overlays to quantitative models. Does NOT mention Cantor, Stupin, or fraud specifically. Does NOT address collateral valuation.
- **CAM 2 (MSRs):** Mortgage servicing rights valuation. Unrelated to fraud.
- **No CAM on collateral verification or fraud exposure** — despite PCAOB flagging exactly this deficiency in 2024 inspection.

### Cantor/Fraud Disclosures in 10-K
- **$98.5M facility** to Cantor Group V, nonaccrual
- **$29.6M specific reserve** — established Q3 2025, **UNCHANGED through Q4 2025** (6 months, zero adjustment)
- WAL claims "as-is" appraisals support recoverability; **updated appraisals due March 2026**
- Two "ultra-high net worth" guarantors (Stupin/Marcil, unnamed in filing)
- Risk factor admits NDFI lending "may be less likely to detect fraud"
- **"Stupin" — zero mentions** in entire 10-K
- Audit fees: not in 10-K, will be in DEF 14A proxy (~April)

### The Reserve Gap
| | WAL | ZION |
|---|---|---|
| Exposure | $98.5M | ~$60M |
| Reserved | $29.6M (30%) | $50M (83%) |
| Implied recovery | ~70% | ~17% |
| Auditor | RSM (mid-tier) | EY (Big 4) |
| Reserve change since Q3 | None | Immediate charge-off |

Same fraud ring. Same collateral subordination scheme. WAL reserves 30%, ZION charged off 83%. RSM signed off on the 30% reserve after the PCAOB caught them failing to verify collateral values at what appears to be this exact client.

---

## Cantor Collateral & Appraisal Status (Mar 27 2026)

### What We Know
- WAL's Cantor facility is a **warehouse line secured by CRE loans** (not direct property). Collateral = the loans themselves.
- Cantor pledged loans claiming first-lien position; many were actually junior liens with forged title policies.
- Some underlying properties were **already in foreclosure or transferred** to other entities before the fraud was discovered.
- Portfolio concentrated in **SoCal CRE** — storefronts and office buildings near LA, SF, Orange County.
- Cantor Group LLC: incorporated 2015, based Newport Beach, CA.
- WAL sought receiver appointment (Aug 2025). **No public confirmation receiver was appointed.** Case at Stanley Mosk Courthouse, LA County Superior Court.

### The March 2026 Appraisals
- WAL 10-K (Feb 23): "Updated collateral appraisals are expected in March 2026"
- As of Mar 27, those appraisals should be complete or nearly complete.
- Results will not be public until Q1 earnings (Apr 21) unless WAL files an 8-K.
- **If appraisals confirm junior-lien status on distressed SoCal CRE, recovery assumptions collapse.**

### ZION Recovery Signal
- ZION charged off $50M on $60M (83%) in Q3 2025 and has gone silent.
- No updated "Cantor" or "Stupin" language in recent ZION filings.
- Silence = they're not recovering anything material. This is the best available proxy for what WAL's appraisals will show.

### What We Can't Get
- Specific property addresses (not in public filings — may be in court exhibits)
- Receiver reports (if receiver was appointed)
- The actual appraisal numbers before Apr 21
- **Next step:** Check LA County Superior Court docket for receiver status, exhibits with property lists

---

## Apr 21 Earnings — Key Questions

1. ✅ **ANSWERED:** RSM's CAMs are generic — no fraud/collateral-specific CAM despite PCAOB findings
2. **March 2026 updated appraisals** — will they support the 70% recovery assumption or force a reserve increase?
3. Will WAL's audit committee discuss RSM adequacy given PCAOB deficiency findings?
4. Has WAL considered Big 4 auditor transition? (This would itself be a signal)
5. **DEF 14A proxy** (~April) — audit fees will reveal if RSM is under-resourced for WAL's complexity
6. **All three fraud vectors** — WAL must address First Brands, Tricolor, AND Stupin. What's total reserve?

---

## Canonical References
- `GRANT_THORNTON_NEXUS.md` — original GT analysis (superseded by this doc)
- `STUPIN_CRE.md` — auditor liability section
- `TRICOLOR.md` — GT thread
- `RQ-REG-A02B` — forensic insurance/auditor analysis
- OTTO: `Gotham_CVNA_Main_Report_2026-01-28.txt` — GT section
