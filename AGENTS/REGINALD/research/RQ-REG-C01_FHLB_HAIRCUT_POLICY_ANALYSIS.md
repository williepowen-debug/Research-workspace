# **FHLB Haircut Policy Research: Collateral Valuation Schedules, Tightening Triggers, and the Zions Bancorporation Fraud Pressure**

## **Executive Summary**

The stability of the United States regional banking sector relies heavily on the symbiotic relationship between depository institutions and the Federal Home Loan Bank (FHLB) system. As the "lender of next-to-last resort," the FHLB provides essential liquidity through secured advances. However, the integrity of this liquidity pipeline is predicated on the valuation and enforceability of the pledged collateral. In late 2025 and early 2026, this system faced a convergence of structural policy tightening and idiosyncratic credit shocks.

This research report provides an exhaustive analysis of the FHLB collateral "haircut" policies—the discounts applied to pledged assets to determine borrowing capacity—specifically focusing on the schedule updates implemented by FHLB Des Moines and FHLB San Francisco throughout 2025\. These systemic changes are analyzed in the context of a significant fraud event involving the "Cantor Group" (unaffiliated with Cantor Fitzgerald), which inflicted material losses on Zions Bancorporation (ZION), Western Alliance Bancorporation (WAL), and a cluster of other regional lenders including Banc of California (BANC) and Enterprise Financial Services Corp (EFSC).

Our analysis reveals that the FHLB system has moved decisively toward a risk-sensitive valuation framework. The 2025 updates to Loan-to-Value (LTV) schedules demonstrate a bifurcated strategy: preserving liquidity for standard, performing housing assets while aggressively penalizing "opaque" risks such as purchased participations and subordinate lien positions. The fraud at Zions Bancorporation, characterized by a failure of collateral perfection on distressed commercial loans, serves as a real-time validation of these tightening measures. The report concludes that while the systemic liquidity backstop remains intact, the cost of access—measured in both collateral over-collateralization and operational scrutiny—has risen sharply for banks with concentrated exposures to specialty finance.

## **Section 1: The Federal Home Loan Bank System in 2025: Structural Context**

To understand the specific pressures facing Zions Bancorporation and its peers, one must first deconstruct the operational architecture of the FHLB system as it stands in 2025\. The FHLBs are not monoliths; they are cooperatives that must balance the liquidity needs of their members with the preservation of their own triple-A credit ratings. This dual mandate drives the complex machinery of collateral valuation.

### **1.1 The Role of the "Implied Guarantee" and Joint Liability**

The FHLB system consists of 11 regionally chartered banks that function as Government-Sponsored Enterprises (GSEs). Although their debt is not explicitly backed by the "full faith and credit" of the U.S. government, the market operates under an assumption of an "implied guarantee".1 This perception allows the FHLB Office of Finance to issue Consolidated Obligations (COs) at rates only slightly above U.S. Treasury yields, passing this low-cost funding to members in the form of advances.1

However, the "Joint and Several" liability structure means that each regional FHLB is ultimately responsible for the debts of the entire system.1 If FHLB San Francisco were to suffer catastrophic collateral losses due to a member failure, FHLB Des Moines and others would be liable. This interdependence creates a powerful systemic incentive for rigorous collateral management. In 2025, this internal discipline manifested as a harmonized tightening of standards across the districts, particularly regarding "niche" collateral types that regional banks have increasingly relied upon for yield.

### **1.2 The Hierarchy of Collateral Pledging Status**

The FHLB system manages member risk through a tiered pledging status, which determines the administrative burden and the "effective" haircut applied to assets. Understanding this hierarchy is crucial for interpreting the pressure on Zions Bancorporation.

1. **Blanket Lien Status:** The most favorable status. The FHLB holds a general security interest in all qualifying assets of the member without requiring a specific list or physical delivery of files. The member reports aggregate collateral data periodically (e.g., quarterly via a Qualifying Collateral Report or QCR). Zions Bancorporation, as a large and generally well-capitalized institution, historically operated under this status for much of its portfolio.4  
2. **Specific Listing (Listing) Status:** The member must provide a detailed loan-by-loan file (often via the "eAdvantage" system for FHLB Des Moines).5 The FHLB assigns value only to the specific loans listed. This status allows for more granular application of haircuts based on individual loan characteristics (e.g., FICO, LTV, DSCR).  
3. **Delivery Status:** The most restrictive status. The member must physically (or electronically) deliver the promissory notes and mortgages to the FHLB or a designated third-party custodian. This creates significant operational friction and cost.  
   * *Insight:* The fraud event at Zions, involving "lien stripping" and "missing deeds," pushes a bank toward **Delivery Status** for the affected asset classes. If the FHLB cannot trust the member's internal records (Blanket) or digital listings (Listing), it must physically possess the collateral to ensure perfection.6

### **1.3 The Move to Dynamic Valuation**

Historically, FHLB haircuts were static percentages based on asset codes (e.g., "Code 1101: Single Family Mortgage \= 75% LTV"). By 2025, the system had evolved toward dynamic valuation.

* **Market Value of Capital Sensitivity:** FHLB San Francisco utilizes this metric to adjust the lending value of equity and assets based on interest rate shocks.7  
* **Effective Lending Value (ELV):** This is the operative metric. It is calculated as:  
  ![][image1]  
  The ELV is not fixed; it fluctuates based on the member's financial condition and the specific attributes of the collateral pool.8

## **Section 2: Comprehensive Analysis of 2025 Collateral Schedule Updates**

The year 2025 saw a concerted effort by FHLB Des Moines and FHLB San Francisco to recalibrate their collateral schedules. These updates were not uniform "tightening" events but rather strategic realignments that punished opacity and rewarded transparency.

### **2.1 FHLB Des Moines: The March and October Recalibrations**

FHLB Des Moines serves Zions Bancorporation following the consolidation of the system (Zions' subsidiary banks, previously members of different FHLBs, consolidated membership into Des Moines).4 Therefore, the Des Moines policies are the primary regulatory constraint on Zions' liquidity.

#### **2.1.1 The March 10, 2025 Update: Multi-Family nuances**

Effective March 10, 2025, FHLB Des Moines revised Loan-to-Value (LTV) discounts for five Multi-Family (MF) collateral types.11

| Type Code | Collateral Description | New LTV Discount | Previous Trend / Insight |
| :---- | :---- | :---- | :---- |
| **1109** | Multi-Family First Mortgage Loan | **64%** | **Stabilization.** The 64% LTV (36% haircut) for standard multi-family loans represents a robust lending value, indicating the FHLB's comfort with the credit performance of housing assets despite broader CRE concerns. |
| **1110** | MF First Mortgage \- Interest Only | **64%** | **Surprising Parity.** Interest-Only (IO) loans are typically viewed as higher risk. Granting them parity with amortizing loans (64%) suggests the FHLB is prioritizing the *cash flow* coverage of the property over the amortization structure of the loan. |
| **1441** | MF First Mortgage Lines of Credit | **64%** | **Liquidity Support.** High LTVs for lines of credit support the operational flexibility of housing developers. |
| **1470** | MF First Mortgage \- Retained Participation | **64%** | **Control Premium.** Loans where the member retains the lead servicing role maintain high borrowing power. |
| **1570** | MF First Mortgage \- Purchased Participation | **58%** | **The Penalty Box.** This is the critical signal. The LTV for *purchased* participations is 600 basis points lower than retained participations. |

* *Strategic Insight:* The 6% differential between Type 1470 (Retained) and Type 1570 (Purchased) is a direct quantification of "Agency Risk." When a bank buys a participation, it relies on the lead lender's underwriting and servicing. The "Cantor Group" fraud exploited exactly this type of distance between the capital provider and the underlying asset. By slashing the LTV on purchased participations, FHLB Des Moines was pre-emptively tightening the screws on the exact asset class where Zions eventually realized losses.

#### **2.1.2 The October 6, 2025 Update: Commercial Real Estate (CRE) Tightening**

Following the March update, FHLB Des Moines implemented a broader set of changes effective October 6, 2025\.5 This update targeted the broader Commercial Real Estate sector, reflecting growing macro-prudential concerns about office and retail valuations.

**Key Commercial LTV Adjustments:**

* **Type 1443 (CRE First Mortgage Line of Credit):** Set at **70%** for monthly listing.13  
* **Type 1444 (CRE Second Mortgage Line of Credit):** Set at **49%**.13  
  * *Analysis:* The sub-50% LTV for second liens effectively demonetizes them for liquidity purposes. A 51% haircut implies that the FHLB views the recovery value of a second lien in a liquidation scenario as negligible. For banks like Zions, which may have extended mezzanine or second-lien financing to distressed borrowers (like the Cantor funds), this change rendered those assets extremely capital-inefficient long before the fraud was discovered.  
* **Type 1571 (CRE Purchased Participation):** Set at **63%**.13 Again, significantly lower than the standard 70% for retained loans, reinforcing the penalty on syndicated risk.

### **2.2 FHLB San Francisco: Securities Margins and Capital Sensitivity**

Western Alliance Bancorporation (WAL) is a member of FHLB San Francisco.15 While Des Moines focused on whole loan LTVs, San Francisco updated its securities margins effective July 1, 2025\.16

**Securities Margin Schedule (Effective July 1, 2025):**

* **U.S. Treasuries (0-1 Year):** 99% Margin (1% Haircut).  
* **U.S. Treasuries (\>10 Years):** 95% Margin (5% Haircut).  
* **Pass-Throughs (Agency MBS):** 98% Margin.  
* **CMBS (Private Label):** 94% Margin (6% Haircut).  
* *Analysis:* The tight margins on government securities (1-2% haircuts) contrast sharply with the 30-50% haircuts on whole loans. This encourages members to hold High-Quality Liquid Assets (HQLA) on their balance sheets. However, for regional banks seeking yield, the spread between a Treasury yielding 4% and a CRE loan yielding 7-8% is vital. The FHLB haircut policy widens the *effective* cost of funding CRE by requiring more capital to support the same liquidity draw.

### **2.3 FHLB New York: The Data Transparency "Iron Curtain"**

Although not the primary regulator for Zions or WAL, FHLB New York introduced a policy in 2025 that serves as a bellwether for the system: the **DSCR Data Requirement**.17

* **The Rule:** Effective for loans originated after Jan 1, 2025, members *must* report the Debt Service Coverage Ratio (DSCR) for pledged income-producing loans.  
* **The Consequence:** Loans missing this data field are assigned **0% Borrowing Capacity**.  
* *Relevance to Zions:* The Zions/Cantor fraud involved "contractual defaults" and "misrepresentations".18 In many fraud cases, the first sign of trouble is the borrower's refusal to provide updated financials. If Zions had been subject to a strict "no data, no liquidity" rule like FHLB NY's, the inability to upload current DSCRs for the Cantor loans might have forced a "collateral exception" earlier, triggering an audit before the exposure grew to $60 million.

## **Section 3: Systemic Tightening Triggers**

Beyond the static schedules, the FHLB system employs dynamic "triggers" that allow for rapid adjustment of haircuts based on borrower behavior or market conditions.

### **3.1 The "Financial Condition" Trigger**

The Member Products Policy (MPP) grants FHLBs the right to alter LTVs based on the member's financial health.6

* **Tangible Common Equity (TCE):** A decline in TCE (often caused by unrealized bond losses or large credit charge-offs) can trigger a migration from "Blanket" to "Listing" status.  
* **Impact on Zions:** Zions' $50 million charge-off in Q3 2025 directly impacts its capital retention. While Zions remains well-capitalized (CET1 \~11.3% 21), the *velocity* of the loss (a sudden $50M hit) alerts the FHLB credit officers. If Zions' profitability were to erode further due to contagion from similar loans, FHLB Des Moines could invoke the "Financial Condition" clause to impose a system-wide haircut increase (e.g., an extra 5% "prudential haircut") on Zions' entire portfolio.

### **3.2 The "Collateral Quality" Trigger**

This is the most relevant trigger for the fraud discussion.

* **Delinquency Thresholds:** If the delinquency rate of the pledged portfolio rises (typically \>2-5%), the FHLB can de-rate the whole pool.  
* **The "Fraud Taint":** The discovery of fraud in a specific asset class creates a "taint" on all similar assets. FHLB collateral audits are not designed to catch sophisticated fraud; they rely on sampling. When fraud is confirmed in one loan, the statistical assumption of the sample fails.  
  * *Result:* The FHLB may require a **100% verification** (forensic scrub) of all loans in that class (e.g., all C\&I loans to investment funds) before they can be pledged again. This effectively freezes liquidity for that segment until the scrub is complete.

### **3.3 The "Concentration" Trigger**

In the wake of the 2023 bank failures (SVB, First Republic), concentration limits became strict.22

* **CRE Concentration:** Banks with CRE exposure \>300% of capital face enhanced scrutiny.  
* **Specialty Finance Concentration:** The "Cantor Group" loans fall into the bucket of "Specialty Finance" or "Lending to Non-Bank Financial Institutions." FHLBs view this as high-correlation risk. If Zions' concentration in this niche exceeds internal FHLB limits, the LTVs on these assets are reduced to discourage further accumulation.23

## **Section 4: Anatomy of the Pressure: The Cantor Group Fraud**

The systemic tightening of FHLB policies provided the backdrop for a severe idiosyncratic shock: the "Cantor Group" fraud. This event was not merely a credit loss; it was a structural failure of collateral perfection that directly impacted the borrowing base of Zions Bancorporation and its peers.

### **4.1 The Architects and the Scheme**

The fraud was orchestrated by **Andrew Stupin** and **Gerald Marcil**, managing entities under the name **"Cantor Group"** (specifically Cantor Group II, IV, and V).24

* **Crucial Distinction:** The "Cantor Group" has **no affiliation** with the global financial firm Cantor Fitzgerald.26 The similarity in naming was likely a deliberate tactic to engender trust among lenders—a common feature of affinity fraud.  
* **The Business Model:** The funds purported to buy distressed residential and commercial mortgage loans, rehabilitating them for profit. Banks lent against these portfolios of distressed assets.25

### **4.2 The Mechanics of "Lien Stripping"**

The core of the fraud was a breakdown in the legal mechanism of "perfection."

1. **The Collateral:** Zions (via subsidiary California Bank & Trust) extended \~$60 million in revolving credit, secured by the deeds of trust on the properties the funds purchased.25  
2. **The Breach:** The borrowers allegedly transferred the deeds to other entities or foreclosed on the properties without notifying the bank. In some cases, they "falsified title documents" (according to Western Alliance's lawsuit) to make it appear the bank still held a first lien.27  
3. **The Result:** The bank held a loan on its books and a security interest on paper, but the actual underlying real estate was legally detached from the debt. When the bank attempted to foreclose, they found the "collateral protections were systematically eliminated".25

### **4.3 Quantifying the Loss: Zions Bancorporation**

Zions Bancorporation bore the brunt of the immediate financial impact in Q3 2025\.

* **Direct Financial Loss:**  
  * **Charge-Off:** **$50 million** recorded in Q3 2025\.18  
  * **Specific Reserve:** **$10 million** set aside for the remaining balance.28  
  * **Total Provision:** The bank recorded a $49 million provision for credit losses, almost entirely driven by this single event.29  
* **Earnings Impact:** Net earnings were **$221 million** ($1.48/share) in Q3 2025, down from expectations due to the charge-off.28 The loss accounted for approximately **22%** of the quarter's net income, a material hit.  
* **Market Reaction:** ZION stock fell **13%** in a single day.25 This sharp decline ($1B+ in market cap) reflects investor fear that the $60 million is just the "tip of the iceberg" regarding control failures.

### **4.4 The Syndicated Contagion: Western Alliance and Others**

The fraud was not isolated to Zions; it was a syndicated or parallel exposure across the regional banking sector.

* **Western Alliance (WAL):** Exposed to **\~$100 million** via Cantor Group V.31 WAL sued in August 2025, alleging the borrower "failed to provide collateral loans in the first position." Crucially, WAL *did not* take a massive charge-off in Q3, asserting that "existing collateral sufficiently covers the debt" based on "as-is" appraisals.31 This divergence in accounting treatment (Zions writing down to zero vs. WAL holding at value) creates significant regulatory tension.  
* **Banc of California (BANC):** Sued Stupin/Marcil to collect on loans. The total "troubled debt" tied to Stupin across lenders is estimated at **$270 million**.32  
* **Enterprise Bank & Trust (EFSC):** Also identified as a plaintiff in lawsuits against Stupin.33  
* **Nano Banc:** Identified in snippets as being "Liable in Massive O.C. Fraud Case," suggesting the exposure might be existential for smaller institutions.34

## **Section 5: The Intersection of Fraud and FHLB Policy**

The Zions fraud event interacts directly with the FHLB policy tightening described in Section 2, creating a compounding pressure on liquidity.

### **5.1 Collateral Ineligibility and the "Borrowing Base"**

The most immediate pressure on Zions is the reduction of its FHLB borrowing base.

* **Rule:** To be eligible for FHLB advances, collateral must be "free and clear of all other liens" (first priority).  
* **Reality:** The $60 million in fraudulent loans lost their lien priority.  
* **Action:** Zions must immediately remove these assets from its FHLB pledge pool. While $60 million is small relative to Zions' total capacity ($18.3B), the *implication* is larger.  
  * *The "Taint" Effect:* FHLB Des Moines likely flagged *all* "distressed mortgage warehouse lines" or "loans to investment funds" in Zions' portfolio as high-risk. Under the "Collateral Quality" trigger, the FHLB may demand that Zions remove *similar* loans until their lien status is verified. If Zions has $500 million of such loans, the liquidity hit is substantial.

### **5.2 The "Forensic Audit" Requirement**

Snippets reference the distinction between standard audits and forensic audits.35

* **Standard Audit:** Checks if the paperwork exists.  
* **Forensic Audit:** Checks if the underlying asset is real and if the lien is legally enforceable (tracing the deed history).  
* **The Pressure:** Following a fraud of this magnitude, FHLB Des Moines typically requires a **Forensic Scrub** of the relevant collateral class. This involves hiring third-party investigators 35 to physically verify title at the county recorder level for every loan in the pool.  
* **Cost of Carry:** During this scrub, the assets are illiquid. Zions cannot pledge them. This forces the bank to hold more expensive HQLA (Treasuries) to meet its internal Liquidity Coverage Ratio (LCR), compressing Net Interest Margin (NIM) in future quarters.

### **5.3 The Strategic Dilemma: Participation vs. Origination**

The fraud highlights the risks of "Purchased Participations" (Type 1570/1571), which FHLB Des Moines aggressively penalized in the March 2025 update (lowering LTV to 58%).

* Zions was essentially "participating" in the risk of the Cantor funds. They relied on the funds to manage the underlying distressed assets.  
* The FHLB's new 58% LTV signals that the system effectively *knew* this risk was underpriced.  
* **Zions' Pressure:** To restore its borrowing power, Zions must pivot away from these "capital-light" participation structures and return to direct origination where they control the collateral. This is operationally intensive and slower, constraining growth.

## **Section 6: Future Outlook and Strategic Implications**

### **6.1 The "Cockroach Theory" and Market Discipline**

JPMorgan CEO Jamie Dimon's comment, "When you see one cockroach, there are probably more," suggests the market expects further disclosures.25 The pressure is now on Zions and its peers to prove this was a contained event.

* **Prediction:** Expect a wave of "voluntary" collateral write-downs across the regional banking sector in Q4 2025 as banks scrub their portfolios to avoid being the next headline. This will temporarily reduce systemic FHLB borrowing capacity.

### **6.2 The Shift to "Conditional Liquidity"**

The era of the FHLB as a passive "check-book" is ending. The 2025 updates move the system toward "Conditional Liquidity."

* **Condition:** Access to advances is now conditional on data granularity (DSCR reporting), forensic confidence (post-fraud scrubs), and structural safety (penalties on participations).  
* **Impact on Treasurers:** Bank treasurers can no longer assume their entire loan book is pledgeable. They must apply severe internal haircuts (potentially 50%+) to any "specialty" assets when calculating their survival horizon.

### **6.3 Zions' Path Forward**

For Zions Bancorporation, the path forward involves:

1. **Litigation:** Aggressively pursuing Stupin and Marcil to recover assets, though the "virtually unrecoverable" disclosure suggests low expectations.  
2. **Collateral Rotation:** Rotating the FHLB pledge pool away from C\&I/Specialty loans and toward standard Multi-Family or 1-4 Family mortgages (where LTVs remain favorable at \~64-74%) to stabilize liquidity access.  
3. **Capital rebuilding:** Using retained earnings to replenish the $50 million hole in capital, ensuring TCE remains above triggers that would worsen their FHLB status.

## **Conclusion**

The convergence of FHLB policy tightening and the Zions/Cantor fraud creates a perfect storm for regional bank liquidity management in 2026\. The FHLB Des Moines and San Francisco schedule updates of 2025 were prescient: they de-rated the exact types of opaque, syndicated risks that the fraud exploited. For Zions Bancorporation, the pressure is not existential—the bank remains capitalized—but it is operational and reputational. The bank must now operate under a regime of heightened verification, where the "haircut" is not just a number on a spreadsheet, but a dynamic reflection of trust. As the system digests the $270 million Cantor Group shock, the definition of "eligible collateral" has fundamentally shifted from "what is on the books" to "what can be forensically proven."

#### **Works cited**

1. Federal Home Loan Banks \- FHLBank Topeka, accessed February 1, 2026, [https://www.fhlbtopeka.com/doccenter/37654e3edd0c4780a10cb4bd9d3ae934](https://www.fhlbtopeka.com/doccenter/37654e3edd0c4780a10cb4bd9d3ae934)  
2. The Role of Federal Home Loan Banks in the Financial System | Congressional Budget Office, accessed February 1, 2026, [https://www.cbo.gov/publication/60064](https://www.cbo.gov/publication/60064)  
3. FHLBs: Meeting liquidity needs in all market conditions \- ABA Banking Journal, accessed February 1, 2026, [https://bankingjournal.aba.com/2023/04/fhlbs-meeting-liquidity-needs-in-all-market-conditions/](https://bankingjournal.aba.com/2023/04/fhlbs-meeting-liquidity-needs-in-all-market-conditions/)  
4. FORM 10-K ZIONS BANCORPORATION, NATIONAL ASSOCIATION, accessed February 1, 2026, [https://s203.q4cdn.com/215756951/files/doc\_financials/2021/ar/ZION-2021-12-31-10-K-2021-12-31-NG-FINAL-FILED-2-24-2022.pdf](https://s203.q4cdn.com/215756951/files/doc_financials/2021/ar/ZION-2021-12-31-10-K-2021-12-31-NG-FINAL-FILED-2-24-2022.pdf)  
5. Collateral \- The Federal Home Loan Bank | Des Moines, accessed February 1, 2026, [https://www.fhlbdm.com/member-support/collateral/](https://www.fhlbdm.com/member-support/collateral/)  
6. 2024 Q4 Lending and Collateral Q\&A \- FHLBanks Office of Finance, accessed February 1, 2026, [https://www.fhlb-of.com/ofweb\_userWeb/resources/lendingqanda.pdf](https://www.fhlb-of.com/ofweb_userWeb/resources/lendingqanda.pdf)  
7. FEDERAL HOME LOAN BANKS \- Combined Financial Report for the Quarterly Period Ended March 31, 2025 \- FHLBanks Office of Finance, accessed February 1, 2026, [https://www.fhlb-of.com/ofweb\_userWeb/resources/2025Q1CFR.pdf](https://www.fhlb-of.com/ofweb_userWeb/resources/2025Q1CFR.pdf)  
8. FEDERAL HOME LOAN BANKS, accessed February 1, 2026, [https://www.fhlb-of.com/ofweb\_userWeb/resources/11Q1end.pdf](https://www.fhlb-of.com/ofweb_userWeb/resources/11Q1end.pdf)  
9. FEDERAL HOME LOAN BANKS, accessed February 1, 2026, [https://www.fhlb-of.com/ofweb\_userWeb/resources/11Q2end.pdf](https://www.fhlb-of.com/ofweb_userWeb/resources/11Q2end.pdf)  
10. ZIONS BANCORPORATION, accessed February 1, 2026, [https://s203.q4cdn.com/215756951/files/doc\_financials/2016/q3/2016-Third-Quarter-10-Q.pdf](https://s203.q4cdn.com/215756951/files/doc_financials/2016/q3/2016-Third-Quarter-10-Q.pdf)  
11. New Collateral LTVs Effective March 10, 2025 \- Federal Home Loan Bank | Des Moines, accessed February 1, 2026, [https://www.fhlbdm.com/news/business-news/updated-collateral-loantovalues-effective-march-10-2025/](https://www.fhlbdm.com/news/business-news/updated-collateral-loantovalues-effective-march-10-2025/)  
12. accessed February 1, 2026, [https://www.fhlbdm.com/news/business-news/updated-collateral-loantovalues-effective-march-10-2025/\#:\~:text=On%20Monday%2C%20March%2010%2C%202025,who%20pledge%20these%20collateral%20types.](https://www.fhlbdm.com/news/business-news/updated-collateral-loantovalues-effective-march-10-2025/#:~:text=On%20Monday%2C%20March%2010%2C%202025,who%20pledge%20these%20collateral%20types.)  
13. FHLB Des Moines LTV Discounts Chart \- Loan Collateral, accessed February 1, 2026, [https://www.fhlbdm.com/webres/File/member-support/collateral/loan-collateral-for-depository-members.pdf](https://www.fhlbdm.com/webres/File/member-support/collateral/loan-collateral-for-depository-members.pdf)  
14. Updated Collateral LTVs take effect October 6, 2025 \- FHLB Des Moines, accessed February 1, 2026, [https://www.fhlbdm.com/news/business-news/updated-collateral-ltvs-take-effect-october-6-2025/](https://www.fhlbdm.com/news/business-news/updated-collateral-ltvs-take-effect-october-6-2025/)  
15. Basel III Regulatory Capital Disclosures, accessed February 1, 2026, [https://s21.q4cdn.com/920996046/files/doc\_downloads/regulatory-disclosures/Q1-2024-Pillar-3-Regulatory-Disclosure.pdf](https://s21.q4cdn.com/920996046/files/doc_downloads/regulatory-disclosures/Q1-2024-Pillar-3-Regulatory-Disclosure.pdf)  
16. Collateral Valuation \- Discount Window, accessed February 1, 2026, [https://www.frbdiscountwindow.org/pages/collateral/collateral\_valuation](https://www.frbdiscountwindow.org/pages/collateral/collateral_valuation)  
17. Changes to Pledging Income Producing Commercial Loan as Collateral \- Federal Home Loan Bank of New York, accessed February 1, 2026, [https://www.fhlbny.com/w/news/bulletins/2025/250319](https://www.fhlbny.com/w/news/bulletins/2025/250319)  
18. What did Zions Bancorp & Western Alliance do, and why is Wall Street so volatile?, accessed February 1, 2026, [https://www.tradingview.com/news/invezz:2d097598a094b:0-what-did-zions-bancorp-western-alliance-do-and-why-is-wall-street-so-volatile/](https://www.tradingview.com/news/invezz:2d097598a094b:0-what-did-zions-bancorp-western-alliance-do-and-why-is-wall-street-so-volatile/)  
19. Securities Fraud Investigation Into Zions Bancorporation, National Association (ZION) Announced – Investors Who Lost Money Urged To Contact Glancy Prongay & Murray LLP, a Leading Securities Fraud Law Firm \- Business Wire, accessed February 1, 2026, [https://www.businesswire.com/news/home/20251017165695/en/Securities-Fraud-Investigation-Into-Zions-Bancorporation-National-Association-ZION-Announced-Investors-Who-Lost-Money-Urged-To-Contact-Glancy-Prongay-Murray-LLP-a-Leading-Securities-Fraud-Law-Firm](https://www.businesswire.com/news/home/20251017165695/en/Securities-Fraud-Investigation-Into-Zions-Bancorporation-National-Association-ZION-Announced-Investors-Who-Lost-Money-Urged-To-Contact-Glancy-Prongay-Murray-LLP-a-Leading-Securities-Fraud-Law-Firm)  
20. Member Products Policy \- Federal Home Loan Bank | Des Moines, accessed February 1, 2026, [https://www.fhlbdm.com/webres/File/member-support/collateral/member-products-policy.pdf](https://www.fhlbdm.com/webres/File/member-support/collateral/member-products-policy.pdf)  
21. Third Quarter Earnings 2025 \- Zions Bank, accessed February 1, 2026, [https://www.zionsbank.com/personal/community/business/third-quarter-earnings-2025/](https://www.zionsbank.com/personal/community/business/third-quarter-earnings-2025/)  
22. Bank Funding during the Current Monetary Policy Tightening Cycle, accessed February 1, 2026, [https://libertystreeteconomics.newyorkfed.org/2023/05/bank-funding-during-the-current-monetary-policy-tightening-cycle/](https://libertystreeteconomics.newyorkfed.org/2023/05/bank-funding-during-the-current-monetary-policy-tightening-cycle/)  
23. Investor behind Zions, Western Alliance bad loans is tied to $270 million in troubled debt, accessed February 1, 2026, [https://www.fidelity.com/news/article/company-news/202510201213RTRSNEWSCOMBINED\_L3N3VY1AB\_1](https://www.fidelity.com/news/article/company-news/202510201213RTRSNEWSCOMBINED_L3N3VY1AB_1)  
24. California Landlord Fraud Fuels Regional Bank Losses \- CRE Daily, accessed February 1, 2026, [https://www.credaily.com/briefs/california-landlord-fraud-fuels-regional-bank-losses/](https://www.credaily.com/briefs/california-landlord-fraud-fuels-regional-bank-losses/)  
25. Trust In Regional Banks Takes A Hit As Two Lenders Lose Millions To Alleged Loan Fraud, accessed February 1, 2026, [https://www.themortgagenote.org/trust-in-regional-banks-take-a-hit-as-two-lenders-lose-millions-to-alleged-loan-fraud/](https://www.themortgagenote.org/trust-in-regional-banks-take-a-hit-as-two-lenders-lose-millions-to-alleged-loan-fraud/)  
26. Official Statement by Cantor Fitzgerald, L.P. Regarding A Lawsuit Between Western Alliance Bank and Cantor Group V, LLC., accessed February 1, 2026, [https://www.cantor.com/official-statement-by-cantor-fitzgerald-l-p-regarding-a-lawsuit-between-western-alliance-bank-and-cantor-group-v-llc/](https://www.cantor.com/official-statement-by-cantor-fitzgerald-l-p-regarding-a-lawsuit-between-western-alliance-bank-and-cantor-group-v-llc/)  
27. Regional bank shares tank after distressed mortgage loans fraud claims \- InvestmentNews, accessed February 1, 2026, [https://www.investmentnews.com/equities/regional-bank-shares-tank-after-distressed-mortgage-loans-fraud-claims/262604](https://www.investmentnews.com/equities/regional-bank-shares-tank-after-distressed-mortgage-loans-fraud-claims/262604)  
28. Zions Bancorporation, National Association Reports Third Quarter Financial Results, accessed February 1, 2026, [https://www.prnewswire.com/news-releases/zions-bancorporation-national-association-reports-third-quarter-financial-results-302589238.html](https://www.prnewswire.com/news-releases/zions-bancorporation-national-association-reports-third-quarter-financial-results-302589238.html)  
29. Zions Bancorp (ZION) Q3 2025 Earnings Call Transcript | The Motley Fool, accessed February 1, 2026, [https://www.fool.com/earnings/call-transcripts/2025/10/21/zions-bancorp-zion-q3-2025-earnings-call-transcript/](https://www.fool.com/earnings/call-transcripts/2025/10/21/zions-bancorp-zion-q3-2025-earnings-call-transcript/)  
30. Zions Bancorp: Loan Write-Off Raises Questions About Underwriting and Risk Management Practices. | Morningstar, accessed February 1, 2026, [https://www.morningstar.com/stocks/zions-bancorp-loan-write-off-raises-questions-about-underwriting-risk-management-practices](https://www.morningstar.com/stocks/zions-bancorp-loan-write-off-raises-questions-about-underwriting-risk-management-practices)  
31. wal-20251016 \- SEC.gov, accessed February 1, 2026, [https://www.sec.gov/Archives/edgar/data/1212545/000162828025045169/wal-20251016.htm](https://www.sec.gov/Archives/edgar/data/1212545/000162828025045169/wal-20251016.htm)  
32. Investor behind Zions, Western Alliance bad loans is tied to $270 million in troubled debt, accessed February 1, 2026, [https://www.investing.com/news/stock-market-news/investor-behind-zions-western-alliance-bad-loans-is-tied-to-270-million-in-troubled-debt-4308575](https://www.investing.com/news/stock-market-news/investor-behind-zions-western-alliance-bad-loans-is-tied-to-270-million-in-troubled-debt-4308575)  
33. From First Brands to Ambipar: latest flashpoints in credit markets By Reuters \- Investing.com, accessed February 1, 2026, [https://www.investing.com/news/stock-market-news/factboxfrom-first-brands-to-ambipar-latest-flashpoints-in-credit-markets-4303919](https://www.investing.com/news/stock-market-news/factboxfrom-first-brands-to-ambipar-latest-flashpoints-in-credit-markets-4303919)  
34. $400M HEIST EXPOSED- FBI-Targeted Continuum Syndicate and Nano Banc Liable in Massive O.C. Fraud Cas by Save Laguna \- Issuu, accessed February 1, 2026, [https://issuu.com/savelaguna/docs/\_400m\_heist\_exposed-\_fbi-targeted\_continuum\_syndic](https://issuu.com/savelaguna/docs/_400m_heist_exposed-_fbi-targeted_continuum_syndic)  
35. Executive Summary, accessed February 1, 2026, [https://le.utah.gov/interim/2024/pdf/00003296.pdf](https://le.utah.gov/interim/2024/pdf/00003296.pdf)  
36. Justice or Injustice in Salt Lake County \- Utah Legislature, accessed February 1, 2026, [https://le.utah.gov/interim/2024/pdf/00003295.pdf](https://le.utah.gov/interim/2024/pdf/00003295.pdf)

[image1]: <data:image/png;base64,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>