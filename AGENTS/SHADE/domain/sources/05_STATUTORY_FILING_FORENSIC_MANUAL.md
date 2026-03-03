Advanced Forensic Analysis of Life Insurance Statutory Filings: Navigating Schedule S, D, and BA to Uncover Institutional Risk
The forensic evaluation of life insurance solvency requires a departure from standard corporate financial analysis. While Generally Accepted Accounting Principles (GAAP) provide insights into the earnings potential and shareholder equity of a firm, the National Association of Insurance Commissioners (NAIC) Statutory Accounting Principles (SAP) are engineered specifically for the protection of policyholders.1 For institutional analysts and regulators, the "Blue Blank"—the annual statutory statement—serves as the primary vehicle for identifying "hidden" risks that may not be apparent in consolidated GAAP reports. These risks typically cluster around four critical vectors: affiliated reinsurance arbitrage, the concentration of illiquid alternative assets, duration mismatches between long-dated liabilities and structured assets, and the masking of capital inadequacy through offshore captive arrangements.3
As the life insurance industry, led by asset-intensive firms like Athene Annuity and Life Company (AAIA), increasingly adopts private-equity-influenced investment strategies, the traditional reliance on high-level solvency ratios has become insufficient.6 A granular, schedule-by-schedule interrogation is required to understand how capital is optimized, how assets are classified, and how risk is transferred across complex corporate structures.7
The Statutory Architecture: Understanding the General Account and Surplus
Before diving into specific schedules, the analyst must establish the baseline of the insurer's financial position. Page 2 (Assets) and Page 3 (Liabilities, Surplus and Other Funds) of the statutory filing provide the high-level summary of the "admitted" balance sheet.10 Unlike GAAP, statutory accounting only "admits" assets that are deemed liquid and available to pay claims; "non-admitted" assets, such as certain software, furniture, or past-due premiums, are charged directly against surplus.10
For AAIA, as of late 2025, total admitted assets reached approximately $331.52 billion.13 To assess hidden risk, the analyst must compare this figure to the Total Capital and Surplus (Page 3, Line 38), which for AAIA stands as a relatively small fraction of its total asset base, emphasizing the importance of asset quality and reinsurance recoverables in maintaining solvency.7
The Role of the Asset Valuation Reserve (AVR) and Interest Maintenance Reserve (IMR)
A unique feature of the statutory balance sheet is the bifurcated reserve system for asset fluctuations. The Asset Valuation Reserve (AVR) is a liability that acts as a buffer against credit-related losses (defaults and equity price drops), while the Interest Maintenance Reserve (IMR) captures realized gains and losses resulting from changes in interest rates.14
In a rising interest rate environment, many insurers have faced "net negative IMR" positions as they sell older, lower-yielding bonds to reinvest in higher-yielding assets. Under traditional SAP, net negative IMR was a non-admitted asset (disallowed). However, recent regulatory shifts, such as INT 23-01, allow insurers to admit a portion of negative IMR up to 10% of surplus, provided they meet certain capital requirements.14 When analyzing a firm like Athene, the analyst must check Note 21J to determine if the reported surplus is being "propped up" by the admission of these negative IMR balances.14
Schedule S Part 3 Section 1: The Forensic View of Reinsurance
Schedule S is the most critical tool for identifying capital-relief strategies. Part 3 Section 1 specifically details "Reinsurance Ceded," where the insurer transfers its risk to another entity (the assuming company) and takes a "reserve credit".10
Columnar Interrogation and Red Flags
An analyst should focus on several specific columns in Schedule S Part 3 Section 1 to identify excessive reliance on affiliated reinsurance:

For AAIA, the "Reserve Credit Taken" is a staggering figure—$70.79 billion as of September 2025.13 This represents more than 40% of the company's total direct and assumed reserves.13 When this credit is predominantly taken from an affiliate like Athene Life Re Ltd. (Bermuda), it creates a "captive" risk profile where the insurer's solvency is inextricably linked to a subsidiary operating under a different, often less stringent, regulatory regime.7
The Affiliated Reinsurance Ratio
To quantify the risk of "shadow insurance," analysts calculate the Affiliated Reinsurance Ratio. This ratio measures the extent to which a company's surplus is supported by credits from its own corporate family:

A ratio exceeding 100% indicates that if the affiliate were to fail or face a regulatory intervention, the parent company's entire surplus could be wiped out.23 In the case of Athene, the use of Bermuda-based affiliates is a core part of its "capital-efficient" model, but it requires the analyst to look through the primary filing and examine the statutory financial statements of the Bermuda entities, such as Athene Life Re (ALRe), which reported its own complex web of funds-withheld arrangements.25
Flagging Capital Adequacy Concerns Masked by Captives
Captive arrangements often involve "non-traditional" assets used to support reserves. While a U.S. domestic insurer must hold highly liquid, admitted assets, its offshore captive might support those same reserves with "Soft Assets" such as:
Surplus Notes: Debt instruments that count as equity for the issuer but are senior to policyholder claims at the parent level.4
Letters of Credit (LOCs): Conditional guarantees from banks that may not be fully funded.4
Parental Guarantees: Unsecured promises from the holding company.2
The analyst can identify these "synthetic" capital elements by reviewing Note 23 (Reinsurance) and the "Funds Held" line on Page 3 (Line 24.03/24.07).27 If the reserve credit is high but the "Funds Held" (assets retained by the cedent) is low, it suggests the reinsurer is holding the assets offshore, potentially in higher-risk categories like those found on Schedule BA.16
Schedule D: Interrogating the Invested Asset Portfolio
Schedule D is the heart of the life insurer's investment portfolio, traditionally representing 70-80% of total assets.6 However, the definition of what constitutes a "bond" for statutory reporting underwent a revolutionary change on January 1, 2025.8
The Principles-Based Bond Definition (PBBD)
The implementation of the Principles-Based Bond Definition (PBBD) split Schedule D Part 1 into two sections, fundamentally altering how analysts must search for hidden risk 9:
Schedule D Part 1 Section 1: Issuer Credit Obligations (ICO). These are traditional bonds where repayment depends on the general creditworthiness of an operating entity (e.g., U.S. Treasuries, corporate debentures).29
Schedule D Part 1 Section 2: Asset-Backed Securities (ABS). This category now captures any security where repayment is tied to a specific pool of financial assets (e.g., CLOs, RMBS, CMBS).9
The forensic risk in Schedule D is the "reclassification threat." If a security previously reported as a bond fails to meet the PBBD criteria—specifically the requirement for "meaningful, recurring cash flows" and a "creditor relationship"—it must be moved to Schedule BA.9 This move typically increases the Risk-Based Capital (RBC) charge from a low bond factor (0.5% - 2%) to a punitive equity-like factor (30%).1
Athene’s Structured Credit Concentration
Athene’s portfolio is a prime example of the shift toward Schedule D Section 2 (ABS). As of its 2025 update, Athene reported a significant tilt toward:
Collateralized Loan Obligations (CLOs): 9% of net invested assets.6
Residential Mortgage Loans and RMBS: 17% combined.6
Commercial Mortgage Loans and CMBS: 14% combined.6
The risk in this concentration is not necessarily immediate default, but "rating migration." Because Athene relies on high NAIC designations (97% are NAIC 1 or 2) to keep its capital charges low, any broad downgrade of the structured credit market would force a massive "capital call" on the company's surplus.1 Analysts should monitor the "Actual Cost" vs. "Book/Adjusted Carrying Value" (BACV) in Schedule D. A widening gap suggests the company is holding securities at amortized cost that have significantly depreciated in market value—a "hidden" solvency threat.9
Schedule BA: The Hiding Place for Private Credit and Residuals
Schedule BA ("Other Long-Term Invested Assets") is where the most significant hidden risks in a modern life insurer reside. It is the repository for anything that does not fit into traditional bond, stock, or mortgage categories.34
Identifying Private Credit and Alternative Risk
In the context of PE-backed insurers, Schedule BA is used to house "Private Credit" and "Differentiated Alternatives".5 The analyst must look for specific reporting lines added in recent years to distinguish between different types of alternative risk 36:

For Athene, Schedule BA assets reached over $10 billion in the AAIA entity alone.11 The "hidden" risk here is twofold: illiquidity and valuation opacity. Unlike Schedule D bonds, which have daily pricing, BA assets are often valued using "Level 3" inputs—assumptions made by the management team or the affiliated asset manager (Apollo).1
The "Rated Note" Strategy
A specific technique used by asset-intensive insurers is the "Rated Note" structure. An insurer invests in a private equity fund (Schedule BA), but instead of holding an equity interest, it holds a debt instrument ("Note") issued by a special purpose vehicle (SPV) that owns the fund's assets.8 If the insurer can get a credit rating for this note, it may attempt to report it on Schedule D Section 2 as a bond. The NAIC's 2025 revisions to the "Bond Definition" and the new "Risk-Based Capital Model Governance Task Force" are specifically designed to curb this practice.8 The analyst should cross-reference Schedule BA with Note 10 to see if these "notes" are issued by Apollo-managed affiliates.8
Identifying Illiquid Asset Concentration
Illiquidity risk is the danger that an insurer cannot sell its assets quickly enough to meet a sudden spike in policyholder surrenders.41 While Athene emphasizes its "Available Liquidity" of $75 billion, a forensic examination reveals that much of this is structural (e.g., FHLB borrowing capacity) rather than pure cash.6
The Illiquidity Ratio:
To flag excessive concentration, analysts calculate the Illiquidity Ratio using admitted assets from the most restrictive schedules:

A ratio above 30% for a life insurer focused on retail annuities is a significant red flag.23 For AAIA, the combination of $50B in mortgage loans and $10B in alternatives against $331B in assets puts the ratio near 20%—manageable, but significantly higher than traditional peers.11 The "hidden" kicker is the portion of Schedule D Section 2 (ABS) that is privately placed and may not be tradable in a stressed market.9
The Notes to Financial Statements: The Qualitative Smoking Gun
The Schedules provide the "what," but the Notes provide the "how" and "why." For Athene and its peers, Note 10 and Note 23 are the most important narrative sections.
Note 10: Information Concerning Parent, Subsidiaries, and Affiliates
Note 10 details the relationships that can lead to conflicts of interest or "capital leakage".25 The analyst must search for:
Management Fees: Look for fees paid to the parent (Apollo) that exceed industry norms. High fees act as an unofficial dividend, draining surplus.13
Asset Transfers: Disclosure of "non-economic" transfers where assets were moved between affiliates to "reset" book values or hide impairments.45
Intercompany Notes: AAIA’s balance sheet shows $4.78 billion in "Intercompany notes receivable".25 These are effectively loans from the insurance company back to the holding company. If the holding company faces a liquidity crunch, these "assets" may prove worthless.2
Note 5L: Restricted Assets
Note 5L is a critical, often-overlooked disclosure that lists assets "pledged as collateral" or otherwise restricted.16 For Athene, a large portion of its "high quality" bond portfolio is pledged to the Federal Home Loan Bank (FHLB) to support its $7.4 billion in borrowing capacity.6 If a significant percentage (e.g., >20%) of the insurer's bonds are restricted, it cannot sell them to pay policyholder claims without first repaying the FHLB or other secured lenders.30
Duration Mismatch: The "Silent Killer" of Life Insurers
Duration mismatch occurs when the sensitive of assets to interest rate changes does not equal the sensitivity of liabilities.6 In a falling rate environment, insurers suffer as their assets are called and they must reinvest at lower rates. In a rising rate environment, the risk is "disintermediation"—policyholders surrender their policies to seek higher yields elsewhere, forcing the insurer to sell depreciated bonds at a loss.5
Finding Duration in the Filing
Duration is rarely reported as a single number on the face of the statutory statement. Instead, the analyst must piece it together from:
Schedule D Part 1B: This table provides a "Maturity Distribution" of the bond portfolio.21
The MD&A (Management Discussion and Analysis): Most insurers disclose their "Duration Gap" here. Athene typically targets a gap of less than 0.5 years.33
Note 8 (Derivatives): Large positions in interest rate swaps or floors indicate the company is using "synthetic" duration to fix an underlying mismatch.11
The Forensic Duration Ratio: If the MD&A is vague, the analyst can estimate the mismatch by comparing the "Weighted Average Maturity" of the assets (Schedule D) to the "Aggregate Reserve for Life Contracts" (Page 3, Line 1).10 A high concentration of "Callable" bonds in Schedule D (identified by the "Call Date" column) is a hidden risk, as these assets will disappear exactly when the insurer needs their yield the most.9
Athene AAIA: A Forensic Profile of Hidden Risk
By applying these tools to Athene’s late-2025 data, a nuanced picture of the firm's risk appetite emerges.
The Capital Structure and ACRA Sidecars
Athene utilizes a unique capital structure involving "sidecars" known as ACRA 1 and ACRA 2 (Athene Co-Invest Reinsurance Affiliate).7 These entities are funded roughly 63% by third-party investors but are controlled by Athene.7 Athene retrocedes (re-reinsures) massive blocks of business to these sidecars ($142.1 billion of reserve liabilities).53
The "hidden risk" here is that while AAIA reports a strong Risk-Based Capital (RBC) ratio of 430%, this ratio is calculated on its "Net" business.7 If the ACRA sidecars—which are offshore and less transparent—were to face a capital shortfall, Athene (as the primary writer) would be legally responsible for the policyholder claims.7
Summary of Risk Flags for Athene (AAIA)

Conclusion: The Analyst’s Checklist for Forensic Solvency
To find the risk that is hidden in plain sight, the analyst must look past the "Jurat" page and the high-level ratings (A+ from S&P/AM Best).6 The true health of a life insurer is found in the interplay between its cessions and its alternative assets.
Final Forensic Checklist:
Schedule S: Calculate the Affiliated Reinsurance Ratio. If it's >100%, move to the Bermuda filings.23
Schedule D Section 2: Check for "Non-Designated" ABS. These are the assets most likely to be reclassified to Schedule BA in the next audit.9
Schedule BA: Focus on "Residuals" and "Affiliated Joint Ventures." These represent the highest-risk, lowest-liquidity tranches of the portfolio.36
Note 10: Quantify the "Capital Leakage" from management fees and intercompany notes.25
Note 21J: Determine if the company would still meet its RBC triggers if "Net Negative IMR" were not admitted.14
In the case of Athene, the model is built on the belief that "complexity" and "illiquidity" are not synonymous with "credit risk".5 While this has driven industry-leading returns, it has also created a balance sheet that is uniquely sensitive to the regulatory environment of Bermuda and the valuation methodologies of private credit.7 For the professional peer, the filing is not just a report; it is a map of the trade-offs between capital efficiency and terminal solvency.
Works cited
US NAIC Fall 2025 National Meeting Highlights: Investment-Related Highlights | Insights, accessed March 2, 2026, https://www.mayerbrown.com/en/insights/publications/2026/01/us-naic-fall-2025-national-meeting-highlights-investment-related-highlights
July 1, 2025 - 8-K: Current report - Athene Holding Ltd., accessed March 2, 2026, https://ir.athene.com/sec-filings/all-sec-filings/content/0001193125-25-154072/d948326d8k.htm
reinsurance counterparty analysis in life insurance industry: the impact on firm performance/mergers - Temple University, accessed March 2, 2026, https://scholarshare.temple.edu/bitstreams/6682f80d-d9e8-4302-b708-1f20c3044480/download
1 UNITED STATES DISTRICT COURT SOUTHERN DISTRICT OF NEW YORK Maureen Dempsey, Heinz E. Schlenkermann, and Chris Shelton, individ - Amazon AWS, accessed March 2, 2026, https://si-interactive.s3.amazonaws.com/prod/planadviser-com/wp-content/uploads/2025/01/02145045/Verizon.PRT_.Suit_.pdf
2024 Asset Risk Stress Considerations Presentation - Cloudfront.net, accessed March 2, 2026, https://d1io3yog0oux5.cloudfront.net/_2ba45cb8867cbd1e3b4f9469bb54580e/athene/db/2271/21954/pdf/2024+Asset+Risk+Stress+Considerations+Presentation.pdf
Athene Holding Ltd., accessed March 2, 2026, https://ir.athene.com/
Overview of Athene's Corporate Structure, accessed March 2, 2026, https://docs.publicnow.com/6D7FF01C4039802A93F9D5F031DF79CBA359E9CD
Private Credit Rated Investments – NAIC Proposes that Insurers Document “Process” and “Analysis” as Part of Compliance - Willkie Farr & Gallagher LLP, accessed March 2, 2026, https://www.willkie.com/publications/2025/10/private-credit-rated-investments-naic-proposes-that-insurers-document
Q&A: What to Expect from the NAIC's Principles-Based Bond Updates - CWAN, accessed March 2, 2026, https://cwan.com/resources/blog/what-to-expect-from-the-naics-principles-based-bond-updates/
How to Read a Statutory Filing - The Life Product Review, accessed March 2, 2026, https://lifeproductreview.com/2012/06/25/how-to-read-a-statutory-filing/
Third Quarter 2024 Statutory Financial Statement for Athene Annuity and Life Company, accessed March 2, 2026, https://insurancenewsnet.com/oarticle/third-quarter-2024-statutory-financial-statement-for-athene-annuity-and-life-company
Statutory Issue Paper No. 74 Life, Deposit-Type and Accident and Health Reinsurance - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/074_p.pdf
Company Story & History - Athene, accessed March 2, 2026, https://www.athene.com/about-athene/our-business
REVISIONS TO 2024 NAIC ANNUAL STATEMENT INSTRUCTIONS – LIFE/FRATERNAL NOV 2024, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/2024_11_06_Life_Annual_Revisions.pdf
Meeting Materials - Statutory Accounting Principles (E) Working Group - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/national_meeting/12-9-25%20Meeting%20SAPWG%20Combined.pdf
NAIC Bulletin: September 2025 - EY, accessed March 2, 2026, https://www.ey.com/content/dam/ey-unified-site/ey-com/en-us/technical/accountinglink/documents/ey-naic28378-251us_09-25-2025.pdf
Unaffiliated Credit Life and Disability Reinsurer 1999 Annual Statement Filing Instructions - Arizona Department of Insurance, accessed March 2, 2026, https://difi.az.gov/sites/default/files/Unaffiliated%20L%20and%20D%20Rein%20Annual%20Instructions%20E-UCLDR.I%2020210316.pdf
ANNUAL STATEMENT - The Standard, accessed March 2, 2026, https://www.standard.com/sites/default/files/migrated/2021_statutory_statement_sny.pdf
Case 8:24-cv-00750-PJM Document 35-3 Filed 05/28/24 Page 1 of 19 - Retirement Income Journal, accessed March 2, 2026, https://retirementincomejournal.com/wp-content/uploads/2024/06/035-3-Declaration-of-Thomas-D.-Gober-1.pdf
Statutory Accounting Principles Working Group - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/Att%20One-P_24-06%20-%20RT%20YRT-Combo%20contracts%208-12-25.pdf
Insurance Spotlight — NAIC Accounting Update: 2025 Fall National Meeting (February 5, 2026) | DART, accessed March 2, 2026, https://dart.deloitte.com/USDART/home/publications/deloitte/industry/insurance/naic-accounting-update-2025-fall-national-meeting
naic - joint meeting: life risk-based capital (e) working group and the variable an, accessed March 2, 2026, https://content.naic.org/sites/default/files/call_materials/Joint-LifeRBC-VACRSG-2-11_Materials.pdf
Draft date: 10/31/24 Virtual Meeting FINANCIAL ANALYSIS SOLVENCY TOOLS (E) WORKING GROUP Thursday, November 7, 2024 11:00 a.m. - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/call_materials/Agenda%20and%20Materials%20%281%29.pdf
NTU Management Review - 臺大管理論叢- 台大, accessed March 2, 2026, https://review.management.ntu.edu.tw/ebook/27.2s/HTML/assets/common/downloads/publication.pdf
GAAP Financial Statements - Year-end 2024 - Athene, accessed March 2, 2026, https://www.athene.com/binaries/content/assets/bermuda/about/financials/2025/athene-life-re-audited-gaap-financial-statements-year-ended-2023-and-2024.pdf
Statutory Financial Statements (Unaudited) September 30, 2025 - Athene, accessed March 2, 2026, https://www.athene.com/binaries/content/assets/bermuda/about/financials/2025/alre---stat-fs--q325.pdf
Statutory Accounting Principles (E) Working Group - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/24-07%20-%20Modco%20Reporting.pdf
ANNUAL STATEMENT - Cloudfront.net, accessed March 2, 2026, https://d1io3yog0oux5.cloudfront.net/_ffc623f4a57a9f3ee96edf244de0256f/athene/db/2370/21957/pdf/2018-03-01-Fourth-Quarter-2017-Statutory-Financial-Statement-for-Athene-Annuity-Life-Assurance-Company-%28Unaudited%29.pdf
2025 Quarterly Reporting Item - Principles-Based Bond Project - Gain Compliance, accessed March 2, 2026, https://gaincompliance.com/2025-quarterly-reporting-item-principles-based-bond-project/
Adopted 08/06/2025 - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/Blanks%20Editorial%20Changes%20as%20of%20August%206%202025.pdf
NAIC 2025 Principles-based Bond Project Guidance - Cherry Bekaert, accessed March 2, 2026, https://www.cbh.com/insights/articles/naic-guidance-2025-bond-compliance-for-insurers/
Don't Let the Tail Wag the Dog: For Insurers, It's Investment Discipline First, Capital Efficiency Second - NEPC, accessed March 2, 2026, https://www.nepc.com/dont-let-the-tail-wag-the-dog-for-insurers-its-investment-discipline-first-capital-efficiency-second/
10-K - SEC.gov, accessed March 2, 2026, https://www.sec.gov/Archives/edgar/data/355429/000104746914001556/a2218382z10-k.htm
Comments Secretary Federal Deposit In - SEC.gov, accessed March 2, 2026, https://www.sec.gov/comments/s7-41-11/s74111-190.pdf
NAIC BLANKS (E) WORKING GROUP, accessed March 2, 2026, https://content.naic.org/sites/default/files/committee_related_documents/2023-12BWG_Modified_1.pdf
SCHEDULE BA – PARTS 1 AND 2 - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/19-21e%20-%20Schedule%20BA%20-%20Reporting%20Lines%2002-16.23.doc
Statutory Accounting Principles (E) Working Group - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/23-16%20-%20Schedule%20BA%20Categories_1.pdf
NAIC List of Schedule BA Non-Registered Private Funds - With Underlying Assets Having Characteristics of Bonds or Preferred Stock, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/NAIC%20List%20of%20Schedule%20BA%20Non-Registered%20Private%20Funds%20With%20Underlying%20Assets%20Having%20Characteristics%20of%20Bonds%20or%20Preferred%20Stock.pdf
Insurance: Statutory Reporting – January 2026 - KPMG International, accessed March 2, 2026, https://kpmg.com/us/en/frv/reference-library/2026/insurance-statutory-reporting-january-2026.html
Agenda - Valuation of Securities (E) Task Force - - NCOIL, accessed March 2, 2026, https://ncoil.org/wp-content/uploads/2023/11/VOSTF-Materials-2023-Fall-National-Meeting-v5.pdf
Calculating Liquidity Premiums for Insurance Contracts - SOA.org, accessed March 2, 2026, https://www.soa.org/globalassets/assets/library/newsletters/financial-reporter/2010/september/frn-2010-iss82-reback.pdf
Reinsurance Demand and Liquidity Creation: A Search for Bicausality* - SCOR Foundation, accessed March 2, 2026, https://foundation.scor.com/sites/default/files/2022-01/Reinsurance%20demand%20and%20liquidity%20creation%20-%20A%20search%20for%20bi-causality_0.pdf
9/11/24 Virtual Meeting FINANCIAL ANALYSIS SOLVENCY TOOLS (E) WORKING GROUP Thursday, September 26, 2024 11:30 a.m. - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/call_materials/Agenda%20and%20Materials_10.pdf
Quarterly Financial Supplement for Athene Holding Ltd. for the fourth quarter 2025 (furnished and not filed). - SEC.gov, accessed March 2, 2026, https://www.sec.gov/Archives/edgar/data/1527469/000152746926000010/athq42025financialsuppleme.htm
AARe - GAAP Financial Statements - Year End 2024 - BMA, accessed March 2, 2026, https://cdn.bma.bm/documents/2025-07-02-12-07-10-Athene-Bermuda---2024-Financial-Statement.pdf
65935202020100100 - 65935 Massachusetts Mutual Life Insurance Company PrintBooks Statement, accessed March 2, 2026, https://www.massmutual.com/global/media/shared/doc/financial-documents/statutory-quarterly-and-annual-statements/massachusetts-mutual-life-insurance-company/2020q4_mm_quarterly.pdf
2025-24 - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/25-24%20-%20Commitments%20and%20Contingencies%20Disclosures.docx
May 16, 2025 - 424B2: Prospectus [Rule 424(b)(2)] - Athene Holding Ltd., accessed March 2, 2026, https://ir.athene.com/sec-filings/all-sec-filings/content/0001193125-25-121684/d41474d424b2.htm
24-20 - Restricted Asset Clarification.docx - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/inline-files/24-20%20-%20Restricted%20Asset%20Clarification.docx
PDF Data Detail – Annual Statements - NAIC, accessed March 2, 2026, https://content.naic.org/sites/default/files/insdata-home-pdf-detail.pdf
61492 Athene Annuity & Life Assurance Company PrintBooks Naic Statement - Cloudfront.net, accessed March 2, 2026, https://d1io3yog0oux5.cloudfront.net/_6cd749f4f8506b03fa874cca0fe2b710/athene/db/2370/22464/pdf/3Q+2024+AADE+Statement+-+FINAL.pdf
ANNUAL STATEMENT FOR THE YEAR 2021 OF THE TLIC Oakbrook Reinsurance, Inc. - Iowa Insurance Division, accessed March 2, 2026, https://iid.iowa.gov/sites/default/files/2022-06/2022-03-01_transamerica_oakbrook_annual_statement.pdf
Athene (ATH) expands annuities, funding deals and ACRA-backed capital - Stock Titan, accessed March 2, 2026, https://www.stocktitan.net/sec-filings/ATH/10-k-athene-holding-ltd-files-annual-report-39d0e9b2a8a4.html