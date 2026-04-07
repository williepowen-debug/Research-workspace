# OFR Brief 26-02: Measuring Counterparty Exposures to Private Credit — Comprehensive Analysis

**Source:** Office of Financial Research (OFR), March 12, 2026  
**Authors:** Ted Berg and Jung Hoon Lee  
**Classification:** Regulatory research — private credit counterparty network  
**Coverage:** Year-end 2024 data, U.S. market focus  
**Related Agents:** BROCK (PC/BDCs), SHADE (PE-insurer), REGINALD (bank exposure), NEXUS (systemic)

---

## Executive Summary

OFR Brief 26-02 provides the most authoritative available estimate of counterparty exposure between U.S. private credit ecosystem and traditional financial institutions. By combining **SEC Form PF** and **Federal Reserve Y-14** data for the first time, OFR estimates:

| Metric | Estimate | Notes |
|--------|----------|:------|
| **Total lending to PC entities** | **$410–540 billion** | Bank + nonbank, lower/upper bounds |
| **Uncalled LP capital commitments** | **~$300 billion** | Legal obligations to fund future calls |
| **Y-14 bank committed exposure** | **$123 billion** | Largest U.S. banks (CCAR) |
| **Y-14 bank utilized exposure** | **$74 billion** | 50-65% historical utilization |
| **U.S. private credit market (incl. BDCs)** | **>$1.6 trillion** | Year-end 2024 |

**Headline conclusion:** Vulnerabilities "appear contained," but counterparty channel between banks and PC funds is "the main channel for risk transmission" and warrants close monitoring given rapid growth.

**Critical context:** Brief published March 12, 2026 — just days before redemption restrictions cascaded across major funds (Blackstone, BlackRock/HPS, Apollo, Ares, Morgan Stanley, Cliffwater). The "contained" conclusion may be stale relative to Q1 2026 developments.

---

## Methodology: Two Confidential Datasets Combined

### SEC Form PF
- Captures borrowings by private credit **funds** from banks and nonbanks (including foreign lenders)
- Covers **2,000+ identified private credit fund filers**
- **Does NOT cover BDCs** (separately registered)
- Reports: gross assets, net assets, borrowings
- Challenge: "private credit" is **not a designated category** — requires keyword searches and cross-referencing

### Federal Reserve Y-14 (CCAR Submissions)
- Loan-level data from largest U.S. bank holding companies subject to stress testing
- Covers lending to **551 private credit funds + 147 BDC borrowers**
- Provides individual loan characteristics: risk ratings, default probabilities, collateral type, maturity
- Underrepresents foreign banks

### Supplementary Sources
- Public pension fund annual comprehensive financial reports
- Insurer statutory Schedule B/A filings
- SEC 10-Q/10-K for BDC borrowing totals

---

## The $410–540 Billion Exposure Range

### Construction

| Component | Low | High | Source |
|-----------|:---:|:----:|:-------|
| Private credit fund borrowings (excl. BDCs) | $215B | $345B | Form PF |
| BDC borrowings (bank + nonbank) | $195B | $195B | SEC 10-Q/10-K |
| **TOTAL** | **$410B** | **$540B** | Combined |

**$215B** = directly reported Form PF total  
**$345B** = adjusted for gross/net asset discrepancies suggesting underreporting (interpret with caution — may include non-interest-bearing liabilities)

### Y-14 Committed vs. Utilized
- **$123 billion committed** ($30B to BDCs)
- **$74 billion utilized** ($16B to BDCs)
- Historical utilization: 50-65%
- Represents **<5% of total C&I loans** across Y-14 banks
- Y-14 banks hold **>$1.6 trillion aggregate Tier 1 capital**

---

## Lender Breakdown

### Domestic vs. Foreign
- **~80% U.S. financial institutions** (Form PF data, ~850 funds)
- **~20% foreign institutions**
- "Highlights interconnectedness between traditional domestic financial institutions and private credit ecosystem"

### Bank vs. Nonbank
- **G-SIBs and other banking institutions** are predominant funding sources
- Only **8 U.S. G-SIBs**: JPMorgan, BofA, Citigroup, Goldman Sachs, Morgan Stanley, Wells Fargo, BNY Mellon, State Street
- Exposure "almost certainly highly concentrated" among small number of institutions

### Secured vs. Unsecured (Y-14 Data)
- **86% secured** (first or second liens)
- **14% unsecured or other**
- Collateral: diversified pools of individual corporate loans
- "Often significantly overcollateralized"

**Other characteristics:**
- 41% five-year term loans
- 52% syndicated
- Only 21% classified as "leveraged loans" under regulatory criteria
- All floating-rate

---

## Leverage Analysis

| Metric | Value | Notes |
|--------|-------|:------|
| **Median leverage** | ~1.0 | No leverage |
| **95th percentile** | >3.5x | High-leverage tail |
| **95th percentile borrowing** | **$81 billion** | ~23% of total Form PF borrowing |

**Assessment:** "Leverage risk overall appears limited" — median fund uses no leverage. Tail risk concentrated in smaller number of funds.

**Caveat:** BDCs statutorily limited to 2:1 debt-to-equity, but private funds have **no statutory leverage limits**. Off-balance-sheet leverage via derivatives not captured.

---

## The $300 Billion Uncalled Capital Commitments

### LP Breakdown

| LP Type | Estimated Uncalled |
|---------|:------------------:|
| Pension funds | ~$100 billion |
| Insurance companies | ~$90 billion |
| Other investment funds | Remainder |
| "Other" (corps, advisers, GPs, employees) | Included in total |

**Note:** Insurers held ~$110B in U.S. private credit assets (2024), with $90B additional committed.

### Risk Pathways

**1. Investment Loss Transmission**
- Losses flow directly to LPs
- Leveraged LPs may be forced to liquidate unrelated assets to meet obligations
- Secondary LP interest market exists but "would likely occur at substantial discounts to fund NAVs during periods of market stress"

**2. Capital Call Liquidity Stress**
- LPs may be forced to sell liquid assets (public stocks/bonds) to fulfill obligations during downturns
- **Historical parallel:** 2007-08 crisis — "capital calls created severe liquidity strains for some very large private university endowments" (Harvard 2009 analog)

**LP Default Provisions:**
- "Extremely punitive, potentially including forfeiture of the defaulting LP's entire prior capital contributions"
- Bilateral stress dynamic: LP must weigh penalty of default vs. cost of forced asset sales

**Mitigant:** Private credit funds pay regular periodic cash distributions (unlike private equity) — calls may be "self-funding" to extent distributions cover them. But in sustained downturn, distributions decline due to defaults and higher PIK substitution.

---

## Data Gaps and Blind Spots

### Explicitly Acknowledged by OFR
1. **BDC SPV borrowing undercount** — Y-14 likely understates BDC bank exposure
2. **Form PF gross-net discrepancy** — $130B gap between reported borrowings and gross-minus-net difference
3. **Off-balance-sheet leverage** — Derivatives excluded from gross/net ratio
4. **No observable LTV ratios** — Cannot directly observe loan-to-value
5. **No strategy-level leverage breakdown** — Cannot classify by direct lending vs. mezzanine vs. distressed
6. **"Private credit" not a Form PF category** — Forced keyword/cross-reference identification; SEC amendments delayed to October 2026

### Structural Gaps (Outside Scope)
7. **Offshore vehicles** — Cayman/Luxembourg funds largely invisible
8. **Insurer-to-reinsurer capital transfers** — PE-owned insurers ceding risk to affiliated Cayman/Bermuda reinsurers
9. **PE-insurer-FHLB capital recycling** — Circular flow: FHLB advances → affiliated PE-managed PC funds
10. **Inter-fund lending within same platform** — Internal capital recycling not visible at consolidated level
11. **Middle-market CLO channel** — Explicitly excluded from leverage sample
12. **Foreign private credit funds** — Non-U.S. funds lending to U.S. borrowers

**Assessment:** Even the $410–540B figure represents a **lower bound**, not a ceiling.

---

## Regulatory Response Timeline

| Date | Event | Significance |
|------|-------|--------------|
| **Mar 12, 2026** | OFR Brief 26-02 published | Baseline measurement established |
| **Mar 16, 2026** | Morgan Stanley projects 8% default rate | Contrasts with OFR's 1.3% bank DP figure |
| **Mar 18, 2026** | Senator Reed letter to Treasury | Requested OFR "immediately map all market participants and their financial obligations to each other" |
| **Mar 25, 2026** | FSOC quarterly meeting | Briefed on PC sector developments; noted "resilience of financial system" |
| **Mar 27, 2026** | CRS Insight IN12674 published | Cited OFR brief directly; Warren statement on PC turmoil |
| **Apr 1, 2026** | Treasury meetings with insurance regulators | Targeting: fund-level leverage, rating consistency, offshore reinsurance, liquidity challenges |

**Posture:** Trump administration emphasizes "capital formation" over "enhanced disclosure requirements" — shift from prior SEC positions. Senator Reed criticized OFR/FSOC for having "neglected their core responsibility to conduct forward-looking assessments of systemic risk."

---

## Comparison With Other Estimates

### Lending Exposure Estimates

| Study | Committed ($B) | Period | Methodology |
|-------|:--------------:|:------:|:------------|
| Moody's (2024) | 525 | 2023 | Global survey, 32 banks |
| Call reports | 400 (264 drawn) | 2024 | Business credit intermediaries |
| Temple/Penn State | 372 | 2023 | Includes BDCs |
| Fed FSR (2023) | 200 | 2021 | Excludes BDCs |
| Fed FEDS Notes (2025) | 95 (56 drawn) | 2024 | Includes BDCs |
| **OFR 26-02** | **410–540** | **2024** | **Form PF + Y-14 + 10-Q/10-K** |

### Market Size Context

| Source | Estimate | Definition |
|--------|----------|:-----------|
| OFR 26-02 (U.S.) | >$1.6 trillion | U.S. private funds + BDCs, year-end 2024 |
| BIS (March 2026) | >$2 trillion | Global |
| Goldman Sachs GSAM | ~$1.5–2.0 trillion | U.S. direct lending market |
| AIMA/ACC (Dec 2025) | $3.5 trillion | Global; broad definition incl. originated loans |
| Moody's outlook 2026 | >$2T in 2026, ~$4T by 2030 | Global AUM trajectory |

**Bloomberg Intelligence:** Private credit firms have **$543 billion in dry powder** (unused funds raised but not deployed).

---

## Default Rate Projections

| Source | Projection | Notes |
|--------|------------|:------|
| **Morgan Stanley / Joyce Jiang (Mar 16, 2026)** | **8%** | Direct lending defaults; AI disruption of software (~26% of BDC portfolios, ~19% of PC CLOs) |
| Current observed direct lending | ~5.6% | — |
| Moody's | 3.0% by Oct 2026 | — |
| BofA | 3.7% for 2026 | — |
| Historical baseline | ~2–2.5% | Average for private credit |

**Goldman Sachs / Alex Blostein:** Projects evergreen retail PC funds will remain in **net outflows throughout 2026 and likely 2027**; macro risk "manageable" and "limited" (0.2–0.5% GDP drag in adverse 10% default scenario).

**Current outflows:** Affluent investors attempted to withdraw **>$10 billion** from largest PC funds (Q1 2026); managers fulfilled ~70% of $10.1B in redemption requests.

---

## Risk Assessment Matrix

| Risk Channel | OFR Assessment | Evidence |
|-------------|----------------|----------|
| **Credit risk** (direct losses) | Limited | 1.3% avg 12-month DP; 86% secured; LGD 32% |
| **Liquidity risk** (fund/LP fire-sale) | Real but not imminent | Capital call stress in "protracted downturn" |
| **Counterparty/cascade risk** | **Primary identified channel** | G-SIBs largest lenders; 80% U.S. concentration |
| **Operational/valuation risk** | Acknowledged; less transparency | "Policymakers have less transparency into PC portfolios" |

---

## Significance for Thesis

### Validates
- PC scale ($1.6T U.S., $3.5T global) is systemically relevant
- Bank exposure ($123B committed) manageable relative to $1.6T Tier 1 capital
- **But** tail risk (95th percentile leverage, $81B) is concentrated
- LP capital call channel ($300B) creates procyclical liquidity risk
- Data gaps mean true exposure > measured exposure

### Contradicts/Complicates
- OFR says "contained" — but published days before crisis accelerated
- Banks report 1.3% default probability vs. Fitch 5.8% actual / Morgan Stanley 8% projected
- "Flying blind" admission (Reed letter) despite OFR report
- Regulatory blind spots (offshore, PE-insurer-FHLB) materially significant

### Implication
The brief establishes empirical baseline but was immediately tested by events. The "contained" conclusion was overtaken by redemption waves within weeks. Supports **Stage 3→Stage 4 transition** thesis (gates → financing tighten → honest marks → spillover).

---

## Files / Cross-References

- Related: `AGENTS/BROCK/inbox/processed/SIG-BROCK-20260331-treasury-fsoc-pc-investigation.md` (Senator Reed OFR letter)
- Related: `AGENTS/BROCK/STATUS.md` (Stage 3 gating, redemption restrictions)
- Related: `AGENTS/SHADE/` (PE-insurer-FHLB channel — OFR data gap)
- Related: `AGENTS/REGINALD/` (bank exposure, Y-14 data)
- Related: `MEMORY.md` (PC Contagion Mechanics)

---

*Comprehensive version captured: April 5, 2026*  
*Source: User research document — detailed OFR Brief 26-02 analysis with regulatory timeline*
