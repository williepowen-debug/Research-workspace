# OFR Brief 26-02: Measuring Counterparty Exposures to Private Credit — Comprehensive Analysis

## Executive Summary

The Office of Financial Research published Brief 26-02, "Measuring Counterparty Exposures to Private Credit," on March 12, 2026, authored by Ted Berg and Jung Hoon Lee. The brief provides the most authoritative available estimate of the counterparty exposure network between the U.S. private credit ecosystem and traditional financial institutions. Using two confidential regulatory datasets — SEC Form PF and Federal Reserve Y-14 — that no prior study had integrated simultaneously, OFR estimates **$410–$540 billion** in total bank and nonbank lending to private credit entities and **~$300 billion** in uncalled LP capital commitments, all as of year-end 2024. The OFR's headline conclusion is measured: current vulnerabilities "appear contained," but the counterparty channel between banks and private credit funds is "the main channel for risk transmission" and warrants close monitoring given rapid growth.[^1][^2][^3]

This analysis is important not because the OFR is sounding systemic alarms — it is not — but because it provides a first rigorous, dual-dataset estimate of a system that policymakers previously could see only partially.

***

## 1. Methodology and Data Sources

### 1.1 Primary Datasets

OFR Brief 26-02 is distinguished by its simultaneous use of two confidential regulatory datasets that previous researchers had only employed separately:[^1]

**SEC Form PF**: Captures borrowings by private credit *funds* from both banks and nonbanks, including foreign lenders. Covers approximately 2,000+ identified private credit fund filers. Does **not** cover BDCs, which are separately registered. Reports three metrics per fund: gross assets, net assets, and borrowings.[^1]

**Federal Reserve Y-14 (CCAR submissions)**: Captures loan-level data submitted by the largest U.S. bank holding companies subject to stress testing. Covers lending to both private funds and BDCs. Provides individual loan characteristics — risk ratings, default probabilities, collateral type, maturity — not available in Form PF. As of year-end 2024, 551 private credit funds and 147 BDC borrowers were identified in Y-14.[^1]

**Supplementary sources**: Public pension fund annual comprehensive financial reports (for fund identification), insurer statutory Schedule B/A filings (insurers classify private credit under "private equity-mezzanine financing"), and SEC 10-Q/10-K filings for BDC borrowing totals.[^1]

### 1.2 Fund Identification Methodology

Identifying private credit funds in regulatory data is a central methodological challenge because "private credit" is **not** a designated category in Form PF as currently implemented. OFR staff used keyword searches (terms including "alternative credit," "asset-based," "direct lend," "illiquid credit," "middle-market," "mezzanine," "senior debt," "venture debt") and cross-referenced results against pension filings, insurer filings, and commercial databases (Preqin, Pitchbook). A key finding from this exercise: pension and insurer filings capture some large private credit funds that are **notably absent from commercial databases** — prominent established funds that don't need to market themselves via fund discovery platforms.[^1]

### 1.3 Geographic Scope and Time Period

The analysis is **predominantly U.S.-focused**. Form PF covers U.S.-registered funds (though it captures foreign lender borrowings to those funds). Y-14 covers the largest U.S. bank holding companies under CCAR, with foreign banks less represented. All data is as of **year-end 2024**. Foreign-domiciled private credit funds (Cayman, Luxembourg) are largely outside the analytical perimeter.[^1]

***

## 2. The $410–$540 Billion Exposure Range

### 2.1 Construction of the Estimate

The range is constructed from two additive components, because BDCs are excluded from Form PF and must be sourced separately:[^1]

| Component | Low Estimate | High Estimate | Source |
|-----------|-------------|--------------|--------|
| Private credit fund borrowings (Form PF, excl. BDCs) | $215B (reported) | $345B (adjusted) | SEC Form PF |
| BDC borrowings (bank + nonbank) | $195B | $195B | SEC 10-Q/10-K |
| **Total** | **~$410B** | **~$540B** | Combined |

The $215B figure is the directly reported Form PF total. The $345B upper bound accounts for a systematic discrepancy: for many funds, the difference between gross and net assets substantially exceeds reported borrowings, suggesting underreporting. OFR cautions that this gap may also include non-interest-bearing liabilities (accounts payable, accrued expenses), so the upper bound should be "interpreted with caution."[^1]

The $195B BDC figure comes from aggregating all BDC 10-Q and 10-K filings, capturing both bank and nonbank sources (BDCs issue bonds and notes to nonbank institutional investors in addition to drawing on bank credit facilities).[^1]

### 2.2 What Is and Is Not Included

**Included:**
- Subscription credit lines (drawn and undrawn, captured in committed Y-14 data)
- NAV loans (to the extent they appear in Form PF borrowings or Y-14 as loans to funds)
- Working capital borrowings by private credit funds
- Term loans and revolving credit facilities to BDCs
- Bonds and institutional notes issued by BDCs

**Structural limitations (not fully captured):**
- BDC SPV borrowings: many BDCs use special purpose vehicles with unique names. Y-14 likely undercounts BDC bank exposure because SPV-level borrowings are difficult to identify by counterparty name.[^1]
- Off-balance-sheet leverage (derivatives) is excluded from the gross/net ratio used for Form PF funds.[^1]
- Form PF reports do not include full balance sheets, so there is no internal reconciliation mechanism.[^1]

### 2.3 Y-14 Committed vs. Utilized Exposure

Y-14 data provides an important sub-view: the largest U.S. banks had **$123 billion committed** to private credit obligors (incl. $30B to BDCs) as of year-end 2024, of which **$74 billion was utilized** (incl. $16B to BDCs). The historical utilization ratio has fluctuated between 50% and 65%. These committed exposures represent less than 5% of total C&I loans outstanding across the Y-14 bank sample, which collectively holds aggregate Tier 1 capital of over $1.6 trillion.[^1]

***

## 3. Lender Breakdown: Who Is Lending

### 3.1 Domestic vs. Foreign

Using Form PF data across approximately 850 private funds (excluding middle-market CLOs), **U.S. financial institutions provide approximately 80% of all lending** to private credit funds, with foreign institutions providing the remaining ~20%. This concentration "highlights the interconnectedness between traditional domestic financial institutions and the private credit ecosystem."[^1]

### 3.2 Bank vs. Nonbank, and the G-SIB Concentration

For the subset of funds classified as Qualifying Hedge Funds (QHFs) under Form PF — 109 funds that are required to submit detailed counterparty information including specific creditor identities and amounts — OFR finds that **G-SIBs and other banking institutions constitute the predominant funding sources**. The Form PF Figure 4b (referenced in the brief) breaks lenders into G-SIBs and other banking institutions, but specific bank-by-bank names and amounts are not disclosed in the public brief, as this information derives from confidential regulatory submissions.[^1]

The brief does not publish a top-5 bank concentration ratio. What can be inferred: because G-SIBs are the dominant lenders and there are only eight U.S. G-SIBs (JPMorgan, BofA, Citigroup, Goldman Sachs, Morgan Stanley, Wells Fargo, BNY Mellon, State Street), exposure is almost certainly highly concentrated among a small number of institutions, though the relative shares are not published.[^1]

### 3.3 Secured vs. Unsecured

The brief addresses this using Y-14 data on bank loans to private credit funds and BDCs:[^1]

- **86% secured** (first or second liens)
- **14% unsecured or other**

The collateral backing secured loans is the **portfolio of individual corporate loans** held by the private credit fund or BDC — diversified pools of middle-market company debt. OFR notes it "cannot directly observe loan-to-value ratios in confidential regulatory data," but understands that loans are "often significantly overcollateralized to account for the riskiness of the underlying portfolio loans which serve as collateral."[^1]

Other structural characteristics of the Y-14 bank loan universe:[^1]
- **41% are five-year term loans**, remainder primarily revolving credit
- **52% are syndicated** — risk distributed across multiple institutions
- **Only 21% classified as "leveraged loans"** under regulatory criteria
- All are **floating-rate** — banks bear minimal interest rate risk

***

## 4. Leverage Analysis

### 4.1 Distribution Across Private Funds (Form PF, excl. BDCs)

OFR's leverage analysis uses gross assets ÷ net assets as its metric (a ratio of 1.0 = no leverage). Key findings:[^1]

- **Median leverage ratio: ~1.0** (no leverage)
- Leverage is low across all size cohorts, though larger funds employ somewhat more leverage
- **95th percentile: leverage ratio exceeds 3.5**
- The 95th percentile and above cohort: **$81 billion in borrowing**, representing approximately **23% of total Form PF private credit borrowing**
- Within this high-leverage tail, **three funds rank among the largest by gross assets**

OFR's assessment: leverage risk "overall appears limited," driven by the fact that the median fund uses no leverage. The tail risk is concentrated in a smaller number of funds.

**Important caveat**: BDCs are statutorily limited to a maximum debt-to-equity ratio of 2:1, but private funds have **no statutory leverage limits**. Off-balance-sheet leverage via derivatives is also not captured by the gross/net ratio.[^1]

***

## 5. The $300 Billion in Uncalled Capital Commitments

### 5.1 Structure of LP Commitments

Under standard private fund mechanics, LPs commit capital at fund inception but that capital is drawn down incrementally by the general partner over the fund's life. The "uncalled" portion represents legal obligations to fund future capital calls. OFR estimates these at **~$300 billion** as of year-end 2024.[^1]

### 5.2 LP Breakdown

| LP Type | Estimated Uncalled Commitment | Notes |
|---------|------------------------------|-------|
| Pension funds | **~$100 billion** | Explicitly stated in brief |
| Insurance companies | **~$90 billion** | Per OFR data cited by ThinkAdvisor[^4][^5] |
| Other investment funds | Remainder | Includes fund-of-funds, family offices, endowments |
| "Other" (corps, advisers, GPs, employees) | Included in total | |

Primary LP investors in private credit funds by net assets: pension funds, other investment funds, and insurance companies (Figure 5a in OFR brief). Insurers held approximately $110 billion in U.S. private credit assets as of 2024, with $90 billion in additional committed (but uncalled) capital.[^4][^1]

### 5.3 Risk Pathways Through LP Relationships

OFR identifies two distinct risk amplification channels through LP relationships, even when funds carry no leverage:[^1]

**Channel 1 — Investment Loss Transmission**: Losses in private credit portfolios flow directly to LPs. Some LPs (e.g., leveraged investment funds) may be forced to liquidate unrelated assets to meet their own obligations, potentially triggering broader contagion. The OFR acknowledges a secondary LP interest market exists but transactions "would likely occur at substantial discounts to fund net asset values during periods of market stress."[^1]

**Channel 2 — Capital Call Liquidity Stress**: Capital calls during protracted market downturns could force LPs to sell liquid assets (publicly traded stocks and bonds) to fulfill contractual obligations. OFR explicitly references the 2007–08 crisis, during which "capital calls created severe liquidity strains for some very large private university endowments." Harvard's 2009 endowment crisis is a direct historical analog.[^1]

### 5.4 LP Default Provisions and Stress Dynamics

LP defaults on capital calls are governed by limited partnership agreements. Penalties "can be extremely punitive, potentially including forfeiture of the defaulting LP's entire prior capital contributions." This bilateral stress dynamic is important: an LP facing its own liquidity crisis must weigh the penalty of defaulting on calls against the cost of forced asset sales.[^1]

**Mitigant**: Private credit funds (unlike private equity) pay regular periodic cash distributions. To the extent LPs receive sufficient distributions to cover calls, the calls are "self-funding." However, in a sustained downturn, distributions decline due to portfolio company defaults and increased payment-in-kind (PIK) substitution, eroding this mitigant precisely when it is needed most.[^1]

**Concentration risk**: The OFR does not explicitly identify whether a small number of LPs account for a disproportionate share of the $300B. With pension funds accounting for ~$100B and pension allocations increasingly concentrated among the largest plans (CalPERS, CalSTRS, CDPQ, etc.), concentration is structurally plausible but not quantified in the brief.[^6]

**Stress scenario funding rate**: OFR does not model what fraction of the $300B would actually be called and funded in a stress scenario. The brief characterizes the risk as "significant liquidity stressors during protracted market downturns" without providing a specific haircut estimate.[^1]

***

## 6. Counterparty Network Structure

### 6.1 Bank Concentration

OFR does not publish individual bank names or exposure amounts — the Y-14 and Form PF data underlying the analysis are confidential. What the brief establishes:[^1]

- G-SIBs and other banking institutions are the **predominant creditors** at the fund level
- U.S. financial institutions account for ~80% of all lending
- The Y-14 universe (largest CCAR-subject banks) accounts for $123B committed/$74B utilized, a fraction of the total $410–$540B (suggesting substantial nonbank and foreign-bank lending outside the Y-14 perimeter)

The gap between Y-14 committed ($123B) and the Form PF + BDC total ($410–$540B) is explained by: (a) nonbank lenders (insurance companies, pension funds, other institutional investors) lending directly to private credit funds; (b) foreign banks captured in Form PF but not Y-14; (c) BDC bond issuance to nonbanks; and (d) SPV borrowings not captured in Y-14.

### 6.2 Hidden Interconnections

OFR does not explicitly map circular exposure structures (Bank A → Fund B → Company C → Bank A), though the brief acknowledges the interconnection concern implicitly. The brief notes that bank loans to private credit funds use underlying portfolio loans as collateral — creating a link between bank lending conditions, private credit fund health, and the credit quality of middle-market borrowers who may themselves have bank relationships.[^1]

The broader "hidden interconnection" risk documented in adjacent research includes:
- Banks providing subscription lines → funds originate loans → loans bundled into CLOs → CLO tranches held by same banks or their insurance affiliates[^7]
- PE-owned insurers using FHLB advances (at subsidized GSE-backed rates) to invest in funds managed by affiliated PE managers — over 35% of some insurer assets in related-party funds[^8]

OFR Brief 26-02 does **not** map the PE-insurer-FHLB channel. Treasury has explicitly flagged it as a concern in subsequent meetings with insurance regulators.[^9]

### 6.3 The Form PF QHF Counterparty Data

A methodological point worth emphasizing: the detailed bank-level counterparty data (Figure 4b in the brief) derives from only 109 Qualifying Hedge Funds that are required to file granular counterparty disclosures. The vast majority of private credit funds are **not** QHFs and therefore do **not** submit creditor identity information. This means OFR's counterparty-level analysis is based on a subset of the market, and the 80% U.S. / 20% foreign split relies on the broader Form PF aggregate data, not individual fund disclosures.[^1]

***

## 7. Risk Assessment

### 7.1 OFR's Own Assessment

OFR's official characterization is measured and deliberately not alarmist:[^2][^1]

> "While vulnerabilities within this sector appear contained, counterparty exposures between banks and private credit funds are the main channel for risk transmission. This channel merits close monitoring given the industry's rapid growth."

The brief highlights mitigating factors:[^1]
- Bank loans exhibit "favorable risk characteristics" vs. other commercial lending (low default probability, high collateral coverage)
- Most private credit funds employ conservative leverage
- Bank loans are predominantly senior secured with diversified collateral
- Bank exposures are small relative to Tier 1 capital

The brief highlights vulnerabilities:[^1]
- Sector's rapid growth (14% CAGR over a decade)
- Evolving interconnections with broader financial system
- Data opacity: policymakers have "less transparency" into private credit than public markets
- High-leverage tail: $81B in borrowing from funds with >3.5x leverage

OFR does **not** make specific regulatory recommendations in Brief 26-02. The brief is methodological in character — establishing measurement frameworks — rather than a policy prescription document.

### 7.2 Risk Channels

| Risk Channel | OFR Assessment | Supporting Evidence |
|-------------|---------------|---------------------|
| **Credit risk** (direct losses) | Limited; loans well-collateralized, low DPs | 1.3% avg 12-month DP; 86% secured; LGD 32%[^1] |
| **Liquidity risk** (fund/LP fire-sale) | Real but not imminent; mitigated by closed-end structures | Capital call stress plausible in "protracted downturn"[^1] |
| **Counterparty / cascade risk** | Primary identified channel | G-SIBs are largest lenders; 80% US concentration[^1] |
| **Operational / valuation risk** | Acknowledged; OFR lacks visibility | "Policymakers have less transparency" into PC portfolios[^1] |

***

## 8. Comparison With Other Estimates

### 8.1 Lending Exposure Estimates

OFR provides a table of prior studies (Figure 1) showing wide dispersion:[^1]

| Study | Committed ($B) | Period | Methodology |
|-------|---------------|--------|-------------|
| Moody's (2024) | 525 | 2023 | Global survey, 32 banks |
| Call reports | 400 (committed), 264 (drawn) | 2024 | Business credit intermediaries |
| Temple/Penn State | 372 | 2023 | Includes BDCs |
| Federal Reserve FSR (2023) | 200 | 2021 | Excludes BDCs |
| Fed FEDS Notes (Berrospide 2025) | 95 (committed), 56 (drawn) | 2024 | Includes BDCs |
| **OFR 26-02** | **410–540** | **2024** | Form PF + Y-14 + 10-Q/10-K |

The wide range across studies is explained by: definitional inconsistencies for "private credit"; treatment of foreign bank and nonbank lending; committed vs. utilized distinctions; inclusion/exclusion of BDCs; and the coverage limitations of individual datasets. OFR's analysis represents the most comprehensive estimate by virtue of combining Form PF and Y-14 while adding 10-Q/10-K BDC data.[^1]

### 8.2 Market Size Context

| Source | Estimate | Definition |
|--------|----------|-----------|
| OFR 26-02 (U.S.) | **>$1.6 trillion** | U.S. private funds + BDCs, year-end 2024[^1] |
| BIS (March 2026) | **>$2 trillion** | Global[^10] |
| Goldman Sachs GSAM | **~$1.5–2.0 trillion** | U.S. direct lending market[^11] |
| AIMA/ACC (Dec 2025) | **$3.5 trillion** | Global; broad definition incl. originated loans[^12] |
| Moody's outlook 2026 | **>$2T in 2026, ~$4T by 2030** | Global AUM trajectory[^13] |

The OFR's $1.6T U.S. figure (Preqin private debt $1.217T + Pitchbook BDCs $420B) and the user's $3–4T ecosystem estimate are not contradictory. The broader figures include PE-insurer-held assets, CLOs backed by private credit loans, global non-U.S. funds, and infrastructure/real estate private debt strategies that OFR's scope partially excludes.

### 8.3 Default Rate Projections

OFR Brief 26-02 does not project default rates. External estimates as of Q1 2026:[^14][^15][^16][^17]

- **Morgan Stanley / Joyce Jiang (March 16, 2026)**: Direct lending defaults projected to reach **8%**, driven by AI disruption of software sector. Software is ~26% of BDC portfolios and ~19% of private credit CLOs. Maturity wall front-loaded: 11% of software loans due in 2027, 20% in 2028. Characterized as "significant but not systemic."[^18][^19]
- Current observed direct lending default rate: approximately **5.6%**.[^17]
- Historical baseline: ~2–2.5% average default rate for private credit.[^16]

### 8.4 Goldman Sachs / Blostein on Outflows

Goldman Sachs' Alex Blostein projects that **evergreen retail private credit funds will remain in net outflows throughout 2026 and likely 2027**. Goldman's macro team estimates that private credit stress would impose a **0.2–0.5% GDP drag** in an adverse scenario (10% default rate), characterizing the macro risk as "manageable" and "limited." As of Q1 2026, affluent investors have attempted to withdraw over $10 billion from the largest private credit funds, with managers fulfilling approximately 70% of $10.1 billion in redemption requests.[^20][^21][^22][^23]

Bloomberg Intelligence estimates private credit firms have **$543 billion in dry powder** (unused funds raised but not deployed), a figure broader than OFR's $300B uncalled commitment estimate, as it includes non-committed AUM held by managers awaiting deployment.[^24]

***

## 9. Data Gaps and Blind Spots

OFR is candid about several limitations, and additional gaps are evident from the brief's methodology:

### 9.1 Gaps Explicitly Acknowledged by OFR

1. **BDC SPV borrowing undercount**: Many BDCs use SPVs (dedicated entities for each bank lender), and Y-14 identification methodology misses SPV-level borrowings. Y-14's $74B utilized BDC figure likely understates actual bank exposure.[^1]

2. **Form PF gross-net discrepancy**: No full balance sheets in Form PF; cannot reconcile the $130B gap between reported borrowings ($215B) and gross-minus-net difference ($345B).[^1]

3. **Off-balance-sheet leverage**: Derivatives-based leverage entirely excluded from gross/net ratio. SPV borrowings may also be off-balance sheet depending on structure.[^1]

4. **No observable LTV ratios**: Cannot directly observe loan-to-value on overcollateralized loans from Y-14 or Form PF.[^1]

5. **No strategy-level leverage breakdown**: Cannot classify leverage by direct lending vs. mezzanine vs. distressed strategies due to fund classification imprecision.[^1]

6. **"Private credit" not a Form PF category**: Forces keyword/cross-reference identification, which produces conflicting results. Form PF amendments adding private credit as a distinct category have had their compliance date delayed to October 2026.[^25][^1]

### 9.2 Structural Gaps Not Addressed (Outside Scope or Methodology)

7. **Offshore vehicles**: Cayman Islands and Luxembourg-domiciled private credit funds and feeder vehicles are largely invisible in Form PF (which captures U.S.-registered investment advisers) and Y-14 (which captures U.S. banks). Cayman reinsurance assets have quadrupled since 2020.[^26]

8. **Insurer-to-reinsurer capital transfers**: PE-owned insurers ceding risk to affiliated Cayman or Bermuda reinsurers — a channel Treasury explicitly flagged as a concern in April 2026 insurance regulator meetings. NAIC adopted new reporting requirements in March 2026 to address this, but data gaps remain.[^27][^9]

9. **PE-insurer-FHLB capital recycling**: The circular flow where PE-owned insurers (Athene/Apollo, Global Atlantic/KKR) obtain FHLB advances using mortgage-backed securities as collateral, then reinvest into affiliated PE-managed private credit funds, is not mapped. Over 35% of some insurer assets are invested back in related-party funds.[^8]

10. **Inter-fund lending within the same platform**: Internal capital recycling within large platforms (Ares, Apollo, Blackstone) — where credit facilities, NAV loans, and continuation vehicles interact — is not visible in either Form PF or Y-14 at the consolidated platform level.

11. **Middle-market CLO channel**: Form PF analysis explicitly excludes middle-market CLOs from the 850-fund leverage sample. CLOs securitizing private credit loans represent an additional conduit for bank exposure not fully captured.

12. **Foreign private credit funds**: Non-U.S. funds (European direct lenders, Asian private credit) lending to U.S. borrowers or holding U.S. assets are largely outside scope.

***

## 10. Regulatory Response and Policy Context

### 10.1 What OFR Recommends

Brief 26-02 contains **no explicit regulatory recommendations**. It is a measurement and methodology paper. The policy implications are implicit: better data infrastructure is needed, and the Form PF classification problem (not having "private credit" as a distinct category) must be resolved. The SEC's February 2024 Form PF amendments adding private credit as a category have been delayed until October 1, 2026 under the current administration's regulatory review process.[^25]

### 10.2 Regulatory Actions Post-Publication

Within weeks of OFR Brief 26-02's release, a sequence of regulatory responses unfolded:[^28][^29][^30][^9]

- **March 18, 2026**: Senator Jack Reed wrote Treasury Secretary Bessent requesting that OFR "immediately map all market participants and their financial obligations to each other" and that FSOC conduct "a forward-looking analysis based on this information."[^28]
- **March 25, 2026**: FSOC quarterly meeting received a briefing on private credit sector developments. Council members "noted the resilience of the financial system" and discussed agency monitoring efforts.[^30]
- **April 1, 2026**: U.S. Treasury announced meetings with domestic and international insurance regulators to evaluate private credit market trends, explicitly targeting: fund-level leverage, rating consistency, offshore reinsurance, and liquidity challenges in private credit.[^9]
- **NAIC (March 5, 2026)**: Adopted new reporting requirements providing more specific classification of private credit investments in insurer portfolios.[^27]

The Trump administration's posture toward private credit regulation is characterized by Moody's as likely to emphasize "capital formation" over "enhanced disclosure requirements" — a shift from prior SEC positions. Senator Reed explicitly criticized the OFR and FSOC for having "neglected their core responsibility to conduct forward-looking assessments of systemic risk."[^31][^28]

***

## 11. Reconciling OFR With Broader Estimates

The following framework reconciles OFR's scope with broader ecosystem estimates:

| Layer | OFR Coverage | Approximate Size |
|-------|-------------|-----------------|
| U.S. private credit funds (Form PF borrowings) | ✅ Partial ($215–$345B in borrowing) | $1.2T in fund AUM |
| BDCs (10-Q/10-K) | ✅ Full ($195B borrowing) | $420B in BDC assets |
| U.S. direct bank exposures (Y-14) | ✅ Committed ($123B) | |
| Nonbank lender exposures | ✅ Partially (via Form PF) | Included in $410–$540B |
| Foreign bank/nonbank lending | ⚠️ Partial | Included via Form PF; excluded from Y-14 |
| PE-owned insurer private credit holdings | ❌ Not mapped | ~$482B (Barclays, broad definition)[^32] |
| Middle-market CLOs backed by PC loans | ❌ Excluded | Part of $3.5T global[^12] |
| Offshore (Cayman/Luxembourg) funds | ❌ Excluded | Portion of $3.5T global AIMA[^12] |
| Infrastructure / real estate private debt | ⚠️ Partial | Included in global $3.5T |

The user's $3–4T total ecosystem estimate, which includes PE-insurer assets, CLOs, and bank commitments globally, is consistent with AIMA/ACC's $3.5T global figure. OFR's $1.6T U.S.-focused market figure and its $410–$540B lending exposure estimate are not contradictions of this larger number — they measure different things (U.S. fund AUM vs. global AUM; lending exposures vs. total market size).[^12][^33]

***

## 12. Critical Assessment

**What OFR Brief 26-02 achieves**: For the first time, a U.S. regulator combined two confidential datasets to quantify the private credit counterparty network with a specific, data-grounded number range. The $410–$540B lending exposure figure will likely become the policy anchor for regulatory debate through 2026–2027. The fund identification methodology — cross-referencing pension and insurer filings to capture large funds absent from commercial databases — is a genuine methodological contribution.

**What it does not achieve**: The brief is deliberately conservative in scope and conclusion. It does not: map individual bank exposures; analyze the PE-insurer-FHLB circuit; model stress scenarios with specific funding haircuts; make regulatory recommendations; or address the Cayman/offshore blind spot. It is a first measurement, not a full systemic risk assessment.

**The gap between OFR's assessment and market stress**: By the time the brief was published (March 12, 2026), affluent investors had already attempted to withdraw $10+ billion from the largest private credit funds, Morgan Stanley had issued an 8% default rate warning, and comparisons to 2008 were circulating in major financial press. OFR's "vulnerabilities appear contained" conclusion, based on year-end 2024 data, may be somewhat stale relative to Q1 2026 developments — a structural lag inherent in confidential regulatory data.[^22][^14][^16]

**The regulatory blind spots are material**: The combination of: (a) Form PF's failure to include "private credit" as a category until October 2026 at the earliest; (b) the offshore reinsurance channel being unmapped; and (c) PE-insurer-FHLB circular flows being invisible to current data infrastructure, suggests that even the $410–$540B figure represents a lower bound of total exposures, not a ceiling.

---

## References

1. [[PDF] OFR Brief: Measuring Counterparty Exposures to Private Credit](https://www.financialresearch.gov/briefs/files/OFRBrief-26-02-measuring-counterparty-exposures-private-credit.pdf) - This brief outlines methodologies for identifying private credit funds and offers estimates of the m...

2. [OFR Brief: Private Credit Exposures to Banks - Changeflow](https://changeflow.com/govping/banking-finance/us-fed-2026-03-13-113) - The document analyzes the growing private credit sector and its linkages with traditional financial ...

3. [Briefs | Office of Financial Research](https://www.financialresearch.gov/briefs/) - Briefs · Measuring Counterparty Exposures to Private Credit · Hedge Fund Participation in Cleared Re...

4. [Insurers Have Promised Private Credit Funds $90B - ThinkAdvisor](https://www.thinkadvisor.com/2026/03/18/insurers-have-promised-private-credit-funds-90b/) - Insurers held about $110 billion of the U.S. private credit assets in 2024, and they had legal commi...

5. [Insurers Have Promised Private Credit Funds $90B - Wink, Inc.](https://www.winkintel.com/2026/03/insurers-have-promised-private-credit-funds-90b/) - Insurers held about $110 billion of the U.S. private credit assets in 2024, and they had legal commi...

6. [Private Credit Outlook 2025 - With Intelligence](https://www.withintelligence.com/insights/private-credit-outlook-2025/) - In 2025, investor appetite for direct lending shows no signs of slowing down and we expect another s...

7. [Q2 2026 Credit Research Outlook - State Street Global Advisors](https://www.ssga.com/se/en_gb/intermediary/insights/q2-2026-credit-research-outlook) - Geopolitical and energy shocks raise late cycle risks, but strong banks and senior exposure suggest ...

8. [FHLB System Evolves into Private Equity Engine - LinkedIn](https://www.linkedin.com/posts/toddhbakerprofile_fhlbs-privateequity-insurance-activity-7431021895979925504-RjS7) - The current environment is more systemic: geopolitical shock, oil price spike, slowing growth, and i...

9. [US Treasury to meet with insurance regulators to discuss private ...](https://www.reuters.com/world/us-treasury-meet-with-insurance-regulators-discuss-private-credit-markets-2026-04-01/) - Treasury officials are keen to ​hear regulators' feedback on the rising use of fund-level leverage, ...

10. [Markets recalibrate amid shifting currents](https://www.bis.org/publ/qtrpdf/r_qt2603a.htm) - Globally, private credit stands at over $2 trillion; see F Avalos, S Doerr and G Pinter, "The global...

11. [The Outlook for Private Credit amid Rising Market Stress](https://www.goldmansachs.com/insights/articles/the-outlook-for-private-credit-amid-rising-market-stress) - Retail investors who embraced private credit funds more recently may be pulling some money out, crea...

12. [Strong growth sees private credit market reach US$3.5 trillion](https://www.aima.org/article/press-release-strong-growth-sees-private-credit-market-reach-us-3-5-trillion.html)

13. [Private credit outlook 2026 executive summary - Moody's](https://www.moodys.com/web/en/us/insights/credit-risk/outlooks/private-credit-2026.html) - Private credit's momentum will continue as global capital demand rises and asset-backed finance (ABF...

14. [Private Credit Default Rates to Reach 8%, Morgan Stanley Says](https://www.bloomberg.com/news/articles/2026-03-16/private-credit-default-rates-to-reach-8-morgan-stanley-says) - Default rates in direct lending will climb to 8% as advances in artificial intelligence disrupt the ...

15. [Morgan Stanley Sees Private Credit Default Rates Reaching 8% (2)](https://news.bloomberglaw.com/banking-law/morgan-stanley-sees-private-credit-default-rates-reaching-8-2) - Default rates in direct lending will climb to 8% as advances in artificial intelligence continually ...

16. [Private credit's ‘zero-loss fantasy' is coming to an end as defaults and fund exits rise](https://www.cnbc.com/2026/03/25/private-credit-defaults-loan-quality-debt-risk-systemic-ai-disruption.html) - Private credit is expected to see a surge in defaults as investors continue to pull money from the s...

17. [Private credit investments: 'Some caution is reasonable,' advisor says](https://www.cnbc.com/2026/03/22/private-credit.html) - Among deals involving direct lending, defaults are expected to rise to 8%, up from the current 5.6%,...

18. [Private credit default rates to reach 8%, says Morgan Stanley](https://www.cnbctv18.com/market/private-credit-default-rates-to-reach-8-says-morgan-stanley-ws-l-19869769.htm) - Morgan Stanley predicts default rates in direct lending will rise to 8% due to AI disruption in soft...

19. ["AI Disruption Across the Board" and the Private Credit Storm Hit Hard](https://news.futunn.com/en/post/70368484/ai-disruption-across-the-board-and-the-private-credit-storm) - Overall, we expect direct loan default rates to reach 8%, close to the peak levels seen during the C...

20. [Goldman sees limited macro risk from private credit stress](https://www.investing.com/news/analyst-ratings/goldman-sees-limited-macro-risk-from-private-credit-stress-93CH-4575648) - Goldman sees limited macro risk from private credit stress

21. [Private Credit Concerns in Context](https://www.youtube.com/watch?v=pU3jPw2CyWo&list=PLIyiGQywEp66lKvfhiDbiuZnCboYneuX2) - Goldman Sachs’ Alex Blostein and Vivek Bantwal discuss the market sentiment, fundamentals, and the o...

22. [Retail investors pull billions from private capital's credit gold mine](https://www.ft.com/content/3103e960-5e54-4cff-a439-b61a77ab21bd?syn-25a6b1a6=1) - Flood of redemptions threatens to stall one of Wall Street's most important sources of growth

23. [Retail Outflows in Private Credit Funds to Continue - Markets Media](https://www.marketsmedia.com/retail-outflows-in-private-credit-funds-to-last-until-2027/) - Goldman Sachs expects funds in to see net outflows through 2026 and likely 2027.

24. [Surge of Insurance Capital Into Private Markets Boosts Hiring, Pay ...](https://www.insurancejournal.com/news/international/2026/02/25/859540.htm) - Bloomberg Intelligence estimates that private credit firms are currently sitting on some $543 billio...

25. [SEC and CFTC Extend Form PF Compliance Date to Oct. 1, 2026](https://www.sec.gov/newsroom/press-releases/2025-119-sec-cftc-extend-form-pf-compliance-date-oct-1-2026) - The Commissions extended the compliance date to Oct. 1, 2026. The Form PF amendments were adopted in...

26. [Cayman reinsurance assets quadrupled since 2020](https://caymanfinance.ky/2026/02/23/cayman-reinsurance-assets-quadrupled-since-2020/) - Cayman Finance reports rapid growth in the jurisdiction's reinsurance sector, following the publicat...

27. [US insurance regulators pulling back the curtain on private credit](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/3/us-insurance-regulators-pulling-back-the-curtain-on-private-credit-100049804) - US insurance regulators are taking steps to better understand the industry's exposure to private cre...

28. [Ahead of FSOC Meeting, Reed Presses Bessent to Review ...](https://www.reed.senate.gov/news/releases/ahead-of-fsoc-meeting-reed-presses-bessent-to-review-emerging-cracks-in-the-credit-markets) - Senator Reed's letter outlines concerns that U.S. regulators and investors may be blind to pockets o...

29. [[PDF] Letter to Bessent re Credit Conditions 3-24-2026 - Senator Jack Reed](https://www.reed.senate.gov/imo/media/doc/letter_to_bessent_re_credit_conditions_3-24-2026.pdf) - March 24, 2026. The Honorable Scott Bessent, Secretary. U.S. Department of the Treasury. 1500 Pennsy...

30. [READOUT: Financial Stability Oversight Council Meeting on March ...](https://home.treasury.gov/news/press-releases/sb0423) - The update described key developments during the recent quarter in the banking sector, financial mar...

31. [Private Credit 2025 Outlook and Risk Analysis - Moody's](https://www.moodys.com/web/en/us/insights/credit-risk/outlooks/private-credit-2025.html)

32. [Insurer Private-Credit Exposure Jumped 21% Last Year - WSJ](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-03-16-2026/card/insurer-private-credit-exposure-jumped-21-last-year-HA70PEp6FKHP4PI6NYhP) - Private-credit investments held by U.S. life insurance companies jumped 21% –or $83 billion– in 2025...

33. [Private Credit 2026 Dashboard - Is This 2008 All Over Again?](https://www.dds.finance/p/private-credit-2026-dashboard-market) - Defaults climbing. Redemption gates slamming shut. Fund managers scrambling. The private credit mark...

