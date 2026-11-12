# United Fidelity Bank, fsb: supervisory and enforcement status (public records)

Researcher B (supervisory), read-only. All reads 2026-11-11 between 19:30 and 19:41 EST unless noted. Bank: United Fidelity Bank, fsb, Evansville IN. OCC charter 703676, FDIC cert 29566, RSSD 391575.

## 5-line answer

1. **The OCC consent order 2023-031 (docket AA-CE-2023-40, Oct 31, 2023) is still listed as ACTIVE.** The OCC's own enforcement database shows it with no termination document or date. None of the 36 monthly OCC enforcement releases from Nov 2023 to Oct 2026 names the bank in a termination or amendment. (VERIFIED)
2. **No newer OCC action of any kind is published:** no PCA directive, capital directive, new consent order, civil money penalty or action against an individual. The database runs only to actions dated **Oct 13, 2026**, and the next monthly release is due around the third week of November. A Q3 action, or a 12 CFR 6 capital-category notice (these are not published), could exist and not yet be public. (SEARCH-NOT-FOUND)
3. **The Federal Reserve written agreement 24-014 with Pedcor Financial LLC, Pedcor Financial Bancorp and Fidelity Federal Bancorp (executed June 18, 2024; announced June 25, 2024) is still listed with no termination date.** The Fed's data feed includes terminations through Oct 21, 2026. No newer Fed action names these companies. (VERIFIED)
4. **FDIC:** the bank is ACTIVE in BankFind (index of Nov 6, 2026) and is not on the failed-bank list (latest closing listed Sep 25, 2026). No FDIC order names the bank or Pedcor. The FDIC orders site failed with a TLS error. (VERIFIED / SEARCH-NOT-FOUND)
5. **Rule text only, not evidence that any notice was issued:** a total capital ratio of 7.26% is below the 8.0% line in 12 CFR 6.4(b)(3)(i), which defines "undercapitalized". The other three ratios are at or above their "adequately capitalized" lines. The consent order already bars the bank from being "well capitalized" (6.4(b)(1)(i)(E); Order Art. IV(3)). The order's Art. IV(8) disposition-plan trigger, failure to keep the 8/9/10/12% minimums, appears met on the stated ratios. Any disposition plan, however, needs the ADC's written direction "in the sole discretion of the ADC", and no public record shows one.

## Enforcement records found

| Agency | Number / docket | Date | Type | Status (as published) | URL |
|---|---|---|---|---|---|
| OCC | #2023-031 / AA-CE-2023-40 | 2023-10-31 | Consent Order (C&D, 12 USC 1818(b)), $0 | **Active.** No termination doc/date in EASearch (read 2026-11-11). Not named in any release, Nov 2023 to Oct 2026 | https://www.occ.gov/static/enforcement-actions/ea2023-031.pdf ; announced in NR 2023-126 (Nov 16, 2023) https://www.occ.gov/news-issuances/news-releases/2023/nr-occ-2023-126.html |
| OTS (now OCC record) | Supervisory Agreement (EASearch doc "SA"), OTS Docket 03676 | 2010-08-13 | Supervisory Agreement (listed as FA type) | **Terminated** 2013-08-05, termination doc 2013-152 | https://occ.gov/static/ots/enforcement/97445.pdf |
| FRB Chicago / Board | 24-014-WA/RB-HC | Executed 2024-06-18; announced 2024-06-25 | Written Agreement with Pedcor Financial LLC, Pedcor Financial Bancorp, Fidelity Federal Bancorp | **Active.** Fed feed `tdt` = 1950-01-01, the site's "no termination" sentinel. Feed runs to edt 2026-10-08 / tdt 2026-10-21 | https://www.federalreserve.gov/newsevents/pressreleases/files/enf20240625a1.pdf ; https://www.federalreserve.gov/newsevents/pressreleases/enforcement20240625a.htm |
| FDIC | not identified | listed in PR-128-2020 (2020-11-27) | October 2020 enforcement decisions list "First City Bank of Florida, nka United Fidelity Bank" | UNKNOWN: order type and docket not visible. INFERRED to concern the failed predecessor bank (closed 2020-10-16, deposits assumed by UFB), not UFB's own conduct | https://archive.fdic.gov/view/fdic/15275 |

Method for the OCC row (VERIFIED): EASearch JSON endpoints that the public UI itself calls:
- `https://apps.occ.gov/EASearch/api/WebSearch/Categories?q=United%20Fidelity&cat=`
- `https://apps.occ.gov/EASearch/api/WebSearch/Actions?q=United%20Fidelity&srt=1&pg=0&pgsz=100`
- searches on charter "703676" and city "Evansville"

Every query returned exactly the two OCC records above. The Evansville search returned no individual (IAP) actions tied to UFB; the individual actions it returned concern other Evansville banks (Integra, Old National). A search for "Pedcor" returned nothing.

Database vintage: the latest action start date anywhere in EASearch is 2026-10-13 (query `startDteMin=07/01/2026`).

EASearch subject-matter tags on 2023-031: ALLL/ACL; Asset Quality; Audit; Board/Management Oversight; Capital; Concentration Risk Management; Credit/Collateral Exceptions; Enterprise Governance; Internal Audit; Lending Issues; Liquidity; Loan Review; Other Lending Deficiencies; Problem Loan Identification; Sensitivity to Market Risk; Strategic Planning; Trading & Securities.

## Order 2023-031: article by article (PRIMARY, VERIFIED from the PDF)

Signed by the OCC Assistant Deputy Comptroller (Louisville Office), digitally dated 2023.10.31. Nine bank directors consented, signing between Oct 20 and Oct 31, 2023.

- **Preamble / Art. II, Comptroller's Findings** (neither admitted nor denied), verbatim: "The Bank has engaged in unsafe or unsound practices, including those related to its board and management oversight; strategic planning; capital planning; stress testing; policy development and approval; management and board reporting; contingency funding planning; model risk management; concentration risk management; credit review; credit analysis; risk assessment; allowance for credit losses methodology; data management; internal audit; and internal controls." The preamble places these in "corporate governance and enterprise risk management, credit underwriting and administration, liquidity risk management, and interest rate risk management."
- **Art. I, Jurisdiction:** the bank is a federal savings association, and the OCC acts under 12 USC 1818(b).
- **Art. III, Compliance:** the board meets at least monthly. A progress report is due within 45 days, then within 30 days after each quarter end.
- **Art. IV, Capital Plan and Higher Minimums:**
  - (1) Within 60 days, achieve and maintain CET1 ≥ 8%, leverage ≥ 9%, Tier 1 ≥ 10% and total capital ≥ 12%.
  - (2) These apply notwithstanding any CBLR election, and the bank must file the full RC-R.
  - (3) Verbatim: "the Bank may not be deemed to be 'well capitalized' for purposes of 12 U.S.C. § 1831o and 12 C.F.R. Part 6, pursuant to 12 C.F.R. § 6.4". Footnote 2: "The Bank may not solicit, accept, renew, or roll over any brokered deposit … except in compliance with the applicable restrictions of 12 U.S.C. § 1831f and 12 C.F.R. § 337.6."
  - (4) Internal capital planning process within 30 days.
  - (5) A 5-year Capital Plan within 60 days, which must "(e) include appropriate capital stress testing, including for commercial real estate concentrations."
  - (6) Dividends only if 1831o(d)(1), §3.11(a)(4) and §5.55 are met, plus the ADC's prior written non-objection.
  - (7) Annual review of the plan by Jan 31.
  - (8) Verbatim: "If the Bank fails to submit an acceptable Capital Plan … fails to implement or adhere to a Capital Plan … or fails to achieve and maintain the minimum capital ratios as required by paragraph (1) of this Article, then in the sole discretion of the ADC, the Bank shall, upon written direction of the ADC, within sixty (60) days develop and submit to the ADC … a Disposition Plan that shall detail the board's proposal to sell or merge the Bank, or implement a voluntary liquidation plan in accordance with 12 C.F.R. § 5.48."
  - (9) For a sale or merger, a definitive agreement no later than 120 days after the ADC's non-objection to the Disposition Plan.
  - (10) For a liquidation, a shareholder vote and the start of liquidation within 120 days.
- **Art. V, Board Oversight:** qualified management within 120 days. An independent third-party review of board and management within 30 days. Within 90 days: an action plan, a policy inventory, model inventory and validation, and board reporting.
- **Art. VI, Strategic Plan:** a 5-year plan within 90 days, which must include "(d) concentration limits commensurate with the Bank's risk profile and capital base". Until non-objection, there must be no significant deviation from the pre-order products, asset composition and size, funding and markets. Any deviation needs 60 days' advance written request.
- **Art. VII, Concentrations of Credit:** a Concentration Program within 60 days. Verbatim, (2)(a): "proper identification of the Bank's concentrations of credit including, but not limited to, the Bank's concentration in commercial real estate, including multifamily affordable housing". (2)(d): limits and sub-limits "based on a percentage of tier 1 capital plus the allowance for credit losses, appropriately stratified by, but not limited to, property type, industry, geographic market, tenant concentrations, occupancy, risk rating, loan structure, loan-to-values, debt service coverage, and loans with policy exceptions". (2)(g): "portfolio-level stress tests … consistent with the size, characteristics, and risk profile of the multifamily affordable housing portfolio". The program also requires: market analysis of primary geographic markets, monthly board reporting, action plans to reduce concentrations, and a contingency plan.
- **Art. VIII, Liquidity:** a 5-year Liquidity Program within 30 days, covering a liquid-asset cushion, diversified funding, a contingency funding plan with early-warning triggers, and stress projections of funding capacity.
- **Art. IX, Interest Rate Risk:** an IRR Program within 90 days, covering limits including net income at risk, assumption support, deposit beta and decay backtesting, and independent annual review.
- **Art. X, Credit Underwriting and Administration:** program within 90 days. Covers loan-level stress testing; borrower and guarantor financial information; global cash flow and DSCR consistency; exception and covenant-waiver tracking with quarterly board reporting; and "(g) a plan to address the Bank's current exposure to loans exceeding the Bank's legal lending limit and supervisory LTV limits". Also "(j) an independent loan review process … reporting directly to the board".
- **Art. XI, Annual Reviews:** an annual review program for commercial loans within 30 days. Reviews must include DSCR, stress testing, performance against projections, collateral valuation, "tie geographic market analysis data to the specific loan or project assumptions", and "address refinance risk".
- **Art. XII, Allowance for Credit Losses:** ACL Program within 30 days. It must segment financial assets "including the multi-family housing portfolio" by risk characteristics "including risk layering" under ASC 326-20, with annual independent validation and quarterly board adequacy findings. (3) Any shortfall is remedied by provision before the call report is filed. Verbatim: "If previously filed call reports are determined to be inaccurate due to a miscalculated ACL, the Bank must refile such call reports within sixty (60) days of this order."
- **Art. XIII, Credit Derivatives:** program within 30 days. Verbatim, (2)(a): "a plan to address the Bank's current exposure to loans exceeding its legal lending limit inappropriately supported by the diminished credit derivatives' structure". (2)(b): use gross loan balances (before credit protection) for concentrations, ACL and stress tests. It also requires single-name derivative limits and counterparty credit risk analysis.
- **Art. XIV, Internal Audit:** a revised program within 60 days, under the 12 CFR 30 App. A standards.
- **Art. XV, General Board Responsibilities:** standard board duties.
- **Art. XVI, Waivers:** standard waivers.
- **Art. XVII, Other Provisions:** verbatim: "As a result of this Order, pursuant to 12 C.F.R. § 5.51(c)(7)(ii), the Bank is in 'troubled condition,' and is not an 'eligible savings association' for purposes of 12 C.F.R. § 5.3".
- **Art. XVIII, Closing:** the OCC reserves the right to add civil money penalties or other actions, including "requirements that the Bank … acquire or hold additional capital or liquidity, or simplify or reduce its operations" and "restrictions on the Bank's growth". The order applies to all subsidiaries. It stays effective until amended or terminated in writing by the OCC.

**What the order does NOT contain (VERIFIED by reading the full text):**
- No article on affiliate transactions, Regulation W, insiders, or Pedcor. Affiliates are not mentioned at all.
- No BSA/AML article.
- No appraisal article.
- No problem-asset or criticized-asset reduction article.

The multifamily language is in Art. VII and Art. XII, plus "commercial real estate concentrations" in Art. IV(5)(e).

**Prior action (PRIMARY, VERIFIED):** OTS Supervisory Agreement, Aug 13, 2010, based on the Oct 19, 2009 exam. Its first article is "Transactions with Affiliates": every new or amended affiliate transaction needs notice under 12 CFR 563.41 and compliance with Regulation W, and the bank must "resolve the affiliate transaction violations identified in the 2009 ROE". It also covered:
- a quarterly asset report;
- a bar on new credit to classified or charged-off borrowers without the Regional Director's non-objection;
- an Asset Concentration Policy with limits as a percentage of Tier 1 plus ALLL;
- interest rate risk, measured as NPV.

It was terminated Aug 5, 2013 (OCC doc 2013-152).

## Rule text: what the rules say, NOT evidence that any notice was issued

Sources:
- eCFR 12 CFR Part 6, point-in-time 2026-11-06: https://www.ecfr.gov/api/versioner/v1/full/2026-11-06/title-12.xml?part=6
- 12 USC 1831o (Cornell LII): https://www.law.cornell.edu/uscode/text/12/1831o
- 12 CFR 337.6 (eCFR 2026-11-06)

All read 2026-11-11.

- **Categories, 12 CFR 6.4(b).**
  - **Well capitalized:** total ≥10.0%, Tier 1 ≥8.0%, CET1 ≥6.5%, leverage ≥5.0%, **and** (E) "not subject to any written agreement, order or capital directive, or prompt corrective action directive issued by the OCC pursuant to section 8 of the FDI Act … to meet and maintain a specific capital level for any capital measure."
  - **Adequately capitalized:** total ≥8.0, T1 ≥6.0, CET1 ≥4.5, leverage ≥4.0.
  - **Undercapitalized:** total <8.0 **or** T1 <6.0 **or** CET1 <4.5 **or** leverage <4.0.
  - **Significantly undercapitalized:** total <6.0 / T1 <4.0 / CET1 <3.0 / leverage <3.0.
  - **Critically undercapitalized:** tangible equity to total assets ≤2.0%.
  - Applying the Sep 30, 2026 ratios given in the brief (not re-checked by me): total 7.26 <8.0 meets the "undercapitalized" definition on the total-capital measure alone. T1 6.64, CET1 4.74 and leverage 5.82 clear the adequately-capitalized lines. (INFERRED application of rule to figures)
  - Because the order sets capital levels, the bank cannot hold "well capitalized" even with good ratios. The most it can hold is "adequately capitalized" (6.4(b)(1)(i)(E); Order IV(3)). (VERIFIED rule + order text)
- **When the category applies, 12 CFR 6.3.** A bank is "deemed to have been notified" of its category as of the most recent of: the date a Call Report "is required to be filed", delivery of a final exam report, or written OCC notice. 6.3(c)(1): the bank must notify the OCC within 15 days of a material event that would lower its category. INFERRED: the Q3 2026 Call Report was due 30 days after quarter end, which is Friday Oct 30, 2026. That would be the deemed-notice date if the filed ratios stand.
- **Capital restoration plan, 6.5 and 1831o(e)(2).** The plan is due "within 45 days" of deemed notice unless the OCC sets a different period. INFERRED: Oct 30 + 45 days = Mon Dec 14, 2026. The OCC acts within 60 days. The plan must cover the steps to reach adequately capitalized, capital levels for each year, and activities. The OCC may not accept it unless it is realistic and "each company having control" guarantees compliance until the bank is adequately capitalized on average for 4 consecutive quarters, with liability capped at the lesser of 5% of total assets or the shortfall. Failing to submit or implement a plan means the bank is treated as significantly undercapitalized (6.5(e), (f)).
- **Mandatory restrictions on an undercapitalized bank (6.6(a)(2); 1831o(d), (e)):**
  - no capital distributions or management fees;
  - close monitoring by the OCC;
  - the capital restoration plan;
  - asset growth: average total assets in a quarter may not exceed the prior quarter's, unless the plan is accepted, the growth is consistent with it, and the tangible equity ratio is rising (1831o(e)(3));
  - prior approval for acquisitions, new branches or new lines of business (1831o(e)(4)).
  - Discretionary safeguards under 1831o(e)(5) and (f)(2) are imposed through PCA directive procedures (6.6(b); Subpart B, §§6.20 to 6.25).
- **Brokered deposits, 12 CFR 337.6:** "undercapitalized insured depository institution may not accept, renew, or roll over any brokered deposit". An adequately capitalized bank needs an FDIC waiver. (The order's footnote 2 already ties the bank to 1831f and 337.6.)
- **Reclassification, 6.4(e):** after notice and a hearing, the OCC may treat a bank as one category lower for unsafe or unsound condition or uncorrected less-than-satisfactory component ratings.
- **"Troubled condition" (Order Art. XVII):** under 12 CFR 5.51(c)(7)(ii) this brings director and senior-officer change notice requirements (rule mechanics per 5.51; not read today, so INFERRED from the order's cite).

## Fed written agreement 24-014: content (PRIMARY, VERIFIED)

Source: https://www.federalreserve.gov/newsevents/pressreleases/files/enf20240625a1.pdf, read 2026-11-11. It records that the OCC order addressed "capital planning, risk management, contingency funding planning, and oversight". Its terms:

- **Para 1:** the holding companies must act as a source of strength (1831o-1; 12 CFR 238.8), including to ensure the bank complies with the Consent Order.
- **Para 2:** a board Oversight Plan within 60 days.
- **Para 3:** a strategic plan and 2024 budget, then a plan each year at least 30 days before the year begins.
- **Para 4:** annual cash flow projections.
- **Para 5(a):** no dividends, buybacks, other distributions "including … interest payments due on subordinated debentures" without prior Reserve Bank and Board approval.
- **Para 5(b):** no "incur, increase, prepay, or guarantee any debt" without prior Reserve Bank approval.
- **Para 6:** section 32 notices for directors and officers, and Part 359 limits on indemnification and severance.
- **Para 7:** quarterly progress reports.
- **Para 12:** the agreement stays effective until modified or terminated in writing.

**Open interaction (INFERRED, not resolved):** a PCA capital restoration plan requires a parent performance guarantee. Whether such a guarantee counts as "guarantee any debt" under WA para 5(b), and so needs Reserve Bank approval, is not settled by any public text I read.

## CRA performance evaluation (PRIMARY, VERIFIED)

Source: https://www.occ.gov/static/cra/craeval/May24/703676.pdf, read 2026-11-11.

- **Evaluation and rating:** PE dated January 8, 2024 (published in the OCC's May 2024 batch). **Overall CRA rating: Outstanding**; Lending Test Outstanding; Community Development Test Outstanding. Intermediate Small Bank procedures; evaluation period Jan 1, 2020 to Dec 31, 2022. The prior PE (Nov 13, 2020) was Satisfactory.
- **Business model, verbatim:** "UFB employs a niche business strategy that heavily focuses on multi-family affordable housing. UFB, on its own and through its wholly owned service corporation subsidiaries develops, owns, finances, and invests in affordable housing projects throughout the country. UFB focuses on affordable housing where at least 51 percent of the units in the complex are leased to LMI tenants."
- **GNMA conversion, verbatim:** "supporting the development and financing of multifamily affordable housing projects through loans, which are then converted to mortgage-backed securities through Government National Mortgage Association (GNMA) … The housing projects are generally occupied by low-and moderate- income (LMI) families and are constructed primarily in suburban areas across the United States." The investment balance for these projects was a $258.7M book value at Dec 31, 2022.
- **Loan mix and size at Dec 31, 2022:**
  - $5.7B total assets, $3.5B loans, $4.7B deposits, $424.5M Tier 1.
  - Multifamily (5+) was 87.8% of loans, 1-4 family 5.3%, CRE 4.6%.
  - 23 branches in IN, IL, FL, CO, CA and the USVI (10 assessment areas).
  - Seven acquisitions since 2014, five of them FDIC-assisted.
  - It merged sister bank International City Bank (Los Angeles area) in November 2021.
- **Loans to subsidiary and affiliate deposits:** the loan-to-deposit discussion notes loans to wholly owned subsidiary Village Capital Corporation averaging $185.7M, VCC unused lines averaging $293.2M, and "affiliate funds on deposit" averaging $129.2M per quarter.
- **Not in the PE:** it does not name Pedcor.
- **Newer PE:** none found. Only a web search was run, not the OCC CRA search tool. (SEARCH-NOT-FOUND)

## OCC corporate applications since July 2026 (PRIMARY, VERIFIED)

The OCC Weekly Bulletin has been replaced by the Corporate Applications Search (CAS). Secondary search results give the change date as Dec 19, 2025 or Mar 3, 2026; I did not read the OCC page that states it.

I queried the endpoint the CAS UI calls: `https://apps.occ.gov/CAS/api/search?fromDte=07/01/2026&toDte=11/11/2026&bankName=United%20Fidelity` and also `charter=703676`.
- **Result: 0 filings.**
- Control checks: the same window with no filter returned 1,536 filings (the latest action dated 2026-11-10), and the bankName filter returned 99 for "Bank of America", so the filter works.
- Last 5 years for United Fidelity (Nov 12, 2021 to Nov 11, 2026), 9 rows:
  - 2021 business combination consummated Nov 30, 2021;
  - 2022 combination 326850, consummated Sep 23, 2022;
  - 2022 combination 328230, withdrawn Jun 14, 2023;
  - 2025 Subsidiaries & Equities filing 339854, consummated May 1, 2025.
- So: no charter conversion, change in control, branch closing or business combination is listed for this bank since July 2026.

## Searched and found nothing (statements about my searches, not proof of absence)

- **OCC EASearch** (q = "United Fidelity", "United Fidelity Bank", "703676", "Evansville", "Pedcor"): no action other than the two above, and no IAP action tied to UFB. The database's latest action is dated 2026-10-13.
- **OCC monthly enforcement releases**: all 36 from NR 2023-126 (Nov 2023) to NR 2026-93 (Oct 22, 2026), fetched and grepped for "United Fidelity|Pedcor". Only NR 2023-126 matched (the original order). Releases list terminations by name, and UFB was never named. The November 2026 release is not yet out.
- **Fed enforcement feeds** (`/supervisionreg/files/ea-cms-recent.json`, 385 items, and `ea-old.json`, 2,513 items), grepped for "Pedcor|United Fidelity|Fidelity Federal": only 24-014.
- **FDIC:**
  - BankFind API (FED_RSSD 391575): ACTIVE=1, REGAGNT=OCC, last reported Jun 30, 2026 (assets $6.493B).
  - failed-bank list CSV (https://www.fdic.gov/bank-failures/download-data.csv): no Fidelity or Evansville match. The latest closing listed is Nano Banc, Sep 25, 2026.
  - FDIC failures API: its index is stale (Aug 25, 2026).
  - Web search on fdic.gov for "United Fidelity" OR "Pedcor" enforcement order: only the 2020 listing above.
- **PCA directive, capital directive, CMP, or a 12 CFR 6 notice:** none in any published source. 12 CFR 6.3 capital-category notices and supervisory letters are confidential and would not normally be published.
- **OCC CAS** since Jul 1, 2026: 0 filings.

## Fetch failures

- `https://orders.fdic.gov/s/searchresults?searchTerm=United%20Fidelity`: "unable to verify the first certificate" (TLS). Not retried by other means.
- `https://apps.occ.gov/CAS/api/Search/Applications` and `/api/applications`: HTTP 403 on guessed paths. I stopped and used the endpoint the UI actually calls.
- The first WebFetch of the order PDF returned binary. The text was extracted locally with pdfminer instead.

## Secondary (found, not relied on)

- Current Publishing (youarecurrent.com), 2024-02-06, "Pedcor-owned United Fidelity Bank taking steps to address unsafe or unsound practices": https://www.youarecurrent.com/2024/02/06/pedcor-owned-united-fidelity-bank-taking-steps-to-address-unsafe-or-unsound-practices/. The search snippet says the bank attributed the concerns to rapid growth. Not read in full.
- Morgan Lewis, Oct 2026, OCC/FDIC policy changes on MRAs and "unsafe or unsound practices", plus an Aug 2026 OCC enforcement manual revision (search snippet only). These may affect how or when the OCC escalates. Not read.

## Open unknowns

- Whether the OCC has issued a written direction under Art. IV(8) (disposition plan), a capital-category notice, a PCA directive, or a new or amended order after Sep 30, 2026. None of these would necessarily be public yet, and some never are.
- Whether the bank already fell below the order's 8/9/10/12% minimums in earlier quarters. That would make Art. IV(8) available to the ADC earlier. Researcher A and the call-report series cover this.
- Whether the Sep 30 call report ratios will be amended. Under Art. XII(3), an ACL miscalculation forces refiling.
- Whether a parent guarantee of a capital restoration plan needs Fed approval under WA 24-014 para 5(b).
- The terms of the 2020 FDIC listing for First City Bank of Florida.

**Single most useful next source:** the OCC's November 2026 monthly enforcement release (expected around the third week of November 2026) together with a re-query of the EASearch JSON (`https://apps.occ.gov/EASearch/api/WebSearch/Actions?q=United%20Fidelity&srt=1&pg=0&pgsz=100`). This is the first public place a PCA directive, an amended order or a termination would appear. Second: the parent companies' own disclosures, if any are public.
