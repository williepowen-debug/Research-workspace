# United Fidelity Bank, fsb: public-source check on brokered-deposit waivers, the 2023 OCC order, newer actions, parent filings

Read-only helper for REGINALD. All reads on **2026-11-16, 11:10 to 11:20 EST** (`date` on this box). No paid sources, no logins, no PACER.
Bank: United Fidelity Bank, fsb (UFB), Evansville IN. OCC charter 703676, FDIC cert 29566, RSSD 391575.
Labels: **VERIFIED** = read at the primary source today · **INFERRED** = my reasoning from verified text · **UNKNOWN** · **COULD NOT REACH** = the site blocked or failed. A blocked site is not evidence that something is absent.
Raw downloads are in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-REGINALD/e512674e-ad5f-4334-979b-7119563f295e/scratchpad/dl/`.

## Short answer

1. **The FDIC does not publish brokered-deposit waiver decisions, for any bank (VERIFIED as to each page and rule below).** The FDIC's application-actions database has no waiver application type. Its "Decisions on Bank Applications" page covers only deposit insurance, mutual-to-stock conversions and merger reports. The waiver rule (12 CFR 303.243(a)) provides no public notice, and the FDIC's public-file rule (303.8) applies only to filings that carry a public-notice requirement. So neither a waiver nor the absence of one can be found in public records. The waiver question is also now **moot going forward**. Once UFB is undercapitalized (deemed notice Oct 30, 2026), the rule says it "may not accept, renew, or roll over any brokered deposits under any circumstances". No waiver is available below adequately capitalized.
2. **The 2023 OCC order (#2023-031, docket AA-CE-2023-40, Oct 31, 2023) mentions brokered deposits in one footnote only (VERIFIED).** Footnote 2 says the bank may take brokered deposits only in compliance with 12 USC 1831f and 12 CFR 337.6. It sets **no deposit-rate cap, no brokered-deposit limit and no waiver**. It does set **higher capital minimums**: CET1 8%, leverage 9%, Tier 1 10%, total capital 12%.
3. **No OCC action dated after Oct 30, 2026 is published (VERIFIED as a search result, not proof of absence).** No PCA directive or capital directive has ever been published for UFB. The OCC enforcement database still ends at **Oct 13, 2026**. The November monthly enforcement release is **not yet out**. The latest OCC release is NR 2026-99 (Nov 12, 2026, not an enforcement release). I INFER the enforcement release will come on **Thu Nov 19, 2026**, the third Thursday.
4. **Neither the holding companies nor the bank file anything public that mentions brokered deposits, a waiver, the consent order or capital plans.**
   - EDGAR full-text search (2023-01-01 to 2026-11-16) returns 0 hits for each pair: "United Fidelity" + "brokered deposit", + "consent order", + "capital restoration"; "Fidelity Federal Bancorp" + "consent order"; "Pedcor" + "consent order".
   - Fidelity Federal Bancorp (FFED) last filed on EDGAR on 2023-04-11 (a Form D/A).
   - **New, not in file D:** UFB itself (CIK 1932454) filed a Form D on 2023-01-12 for a **$6.0M equity** sale (3 investors, Piper Sandler).
   - **New, not in file D:** NexPoint Capital (CIK 1588272) holds **1,000 shares of "United Fidelity Bank FSB 7.00%" preferred, cost $1.0M, marked at $500,000 (50%)** at 12/31/2025 and 6/30/2026. A NexPoint 10-K comparative column shows the same holding at $725,000.
   - FFIEC NIC (the FR Y-9 source): COULD NOT REACH (HTTP 403 CAPTCHA).
5. **Federal Register:** 0 documents mention "United Fidelity", "Fidelity Federal Bancorp" or "Pedcor" since 2023-01-01 (VERIFIED, API). **FDIC press:** the only UFB items are its 2014 to 2020 failed-bank deposit assumptions; nothing from 2023 to 2026 (search result). **Fed:** written agreement 24-014 is still unterminated in a feed that now runs to Nov 9, 2026 (VERIFIED).

**One public test on brokered deposits (VERIFIED figures, INFERRED meaning).** In FDIC BankFind, UFB's brokered deposits fell from **$2.526B (12/31/2023, 45.9% of deposits)** to **$1.154B (6/30/2026, 20.5%)**, down 54% over ten quarters. That is consistent with brokered money running off under the not-well-capitalized restriction. It does not tell us whether a waiver existed. The 9/30/2026 figure is not yet in BankFind. It is in the Q3 Call Report (Schedule RC-E memoranda), and **from Oct 30 every maturing brokered deposit must leave the bank**.

---

## Q1. Does the FDIC publish brokered-deposit waivers under 12 CFR 337.6(c)?

**Answer: No. No per-bank waiver list or decision is published, and no entry exists for UFB, 2023 to 2026. VERIFIED from the FDIC pages and rule text below; the "not published" conclusion is INFERRED from all of them together.**

| Source (read 2026-11-16) | What it shows | Status |
|---|---|---|
| FDIC Bank Application Actions, https://www.fdic.gov/regulations/applications/actions.html, and its CSV https://www.fdic.gov/bank-examinations/bank-application-actions.csv | Page text: "Search on actions taken on selected applications received over a rolling 10 year period between October 1, 2016, through September 30, 2026". The type drop-down has 28 types, including Change of Control, Merger, Retire Capital, Retire Subordinated Debt and **"Request for Determination Institution is Operating in a High-Rate Area"**. It has **no brokered-deposit waiver type**. The CSV has 10,045 rows and no type containing "broker". UFB's only row is application 20190449, "Merger - Regular", APPROVE, 7/24/2019. | VERIFIED |
| FDIC Decisions on Bank Applications, https://www.fdic.gov/bank-examinations/decisions-bank-applications | Covers only: "Decisions issued by the FDIC's Board of Directors (or under delegated authority) on applications submitted by an existing or proposed depository institution for federal deposit insurance; and applications filed by an insured state-chartered mutually owned savings bank that proposes to convert from mutual to stock form", plus the Merger Decisions annual report to Congress. No waiver category. | VERIFIED |
| FDIC Brokered Deposit Waiver page, https://www.fdic.gov/bank-examinations/brokered-deposit-waiver (last updated Jan 19, 2024) | "An institution with a capital category of "adequately capitalized" may accept deposits from a deposit broker only if it has received a waiver from the FDIC. An institution that has a capital category of "undercapitalized" or worse is prohibited from accepting deposits from a deposit broker." The page lists procedures, laws and FAQs only, with **no list of waivers granted**. | VERIFIED |
| FDIC Brokered Deposits banker page, https://www.fdic.gov/resources/bankers/brokered-deposits (last updated Oct 26, 2026) | The only list it publishes is the "List of companies that have submitted notices for a Primary Purpose Exception (PPE) … (As of October 15, 2026)". That list covers deposit-placing **companies**, not bank waivers. Waivers are described only as a procedure: "Section 303.243(a) — Brokered Deposits Waivers sets forth the procedures for institutions that are adequately capitalized to file a brokered deposits waiver application with the FDIC." | VERIFIED |
| 12 CFR 303.243(a) (eCFR point-in-time 2026-11-06) | (1) "an undercapitalized insured depository institution may not accept, renew, or roll over any brokered deposits under any circumstances." The FDIC notifies only the bank's primary regulator: it "will provide notice to the depository institution's appropriate Federal banking agency and any state regulatory agency … and will consult with such agency". (2) "Applicants shall submit a letter application to the appropriate FDIC office." (6) "the FDIC will provide the applicant with written notification of the final action". (7) A waiver is "for a fixed period, generally no longer than two years" and "May be revoked by the FDIC at any time by written notice to the institution." **There is no public-notice or publication provision.** | VERIFIED |
| 12 CFR 303.7(a) and 303.8(a), (b) (eCFR 2026-11-06) | 303.7(a): public notice is required only for "a merger transaction, … a change of control transaction, or request deposit insurance". 303.8(a): "For filings subject to a public notice requirement, any person may inspect or request a copy of the non-confidential portions of a filing (the public file)". 303.8(b)(1)(iii) treats as generally confidential "Information, the disclosure of which could seriously affect the financial condition of any depository institution." | VERIFIED |
| 12 CFR 309.5 (FOIA exemptions) and 309.6(a) | 309.5 exempts "(8) Records that are contained in or related to examination, operating, or condition reports prepared by, on behalf of, or for the use of the FDIC or any agency responsible for the regulation or supervision of financial institutions". 309.6(a): "no person shall disclose or permit the disclosure of any exempt records … without written authorization from the Director of the Corporation's Division". | VERIFIED (rule text). Applying it to waiver files is INFERRED |
| 12 CFR 337.6(b)(3) and (c) (Cornell LII) | (b)(3): an undercapitalized institution "may not accept, renew, or roll over any brokered deposit." (c): "Any waiver granted may be revoked at any time by written notice to the institution." Nothing on publication. | VERIFIED |
| OCC Comptroller's Handbook, *Problem Bank Supervision* (v1.0, Sep 2021), p. ~56, liquidity regulations | "Banks that are not well-capitalized may not accept, renew, or roll over any brokered deposit. A bank that is adequately capitalized as defined in PCA may, however, apply for and must receive an FDIC waiver to accept, renew, or roll over any brokered deposit." | VERIFIED |
| FDIC orders site, https://orders.fdic.gov/s/searchresults?searchTerm=United%20Fidelity | curl exit 60 (TLS certificate verification failure), the same failure researcher B hit on 11-11. | **COULD NOT REACH** |
| Web search, site:fdic.gov "United Fidelity" | Only the 2014 to 2020 failed-bank assumptions (Columbia Savings 2014, Highland Community 2015, Premier Bank Denver 2015, Fayette County 2017, First City Bank of Florida 2020). Nothing 2023 to 2026. | Search result, not proof of absence |

**Why a waiver, or its absence, cannot be found (INFERRED from the VERIFIED texts above):**
- The waiver is a letter application that goes only to the FDIC regional office. The decision goes only to the bank, with notice to the OCC.
- No rule requires public notice or a public file.
- The FDIC's two public application surfaces exclude this application type.
- The file content is condition information that the FDIC treats as confidential. A FOIA request would meet Exemption 8 (309.5).

**Only indirect evidence is public.** The Call Report Schedule RC-E memoranda report total brokered deposits each quarter. Between Oct 31, 2023 and Oct 30, 2026 the order made UFB at best "adequately capitalized". Without a waiver, every brokered deposit had to run off at maturity. Sustained new or rolled-over brokered balances would therefore imply a waiver. A steady decline is consistent with either case.

FDIC BankFind API (`api.fdic.gov/banks/financials`, CERT 29566, field BRO = brokered deposits, $000), read 2026-11-16:

| Quarter end | Brokered deposits | Total deposits | Brokered share | Total risk-based capital ratio (RBCRWAJ) |
|---|---|---|---|---|
| 2023-09-30 | $2,481.6M | $5,474.4M | 45.3% | 12.14% |
| 2023-12-31 (order dated Oct 31, 2023) | $2,525.9M | $5,499.9M | 45.9% | 12.68% |
| 2024-06-30 | $2,309.8M | $5,475.0M | 42.2% | 13.61% |
| 2024-12-31 | $2,162.6M | $5,523.2M | 39.2% | 14.20% |
| 2025-06-30 | $1,934.1M | $5,537.0M | 34.9% | 14.54% |
| 2025-12-31 | $1,581.1M | $5,419.6M | 29.2% | 15.02% |
| 2026-03-31 | $1,225.7M | $5,474.6M | 22.4% | 14.97% |
| 2026-06-30 | $1,153.5M | $5,622.4M | 20.5% | 15.09% |
| 2026-09-30 | not yet in BankFind (the API returned 14 quarters, ending 6/30/2026) | | | brief: 7.26% |

- The brokered balance rose by $44.3M in Q4 2023, the quarter the order was signed. INFERRED: this could be accrued interest, sweep or reciprocal mechanics, or deposits taken before the capital category legally changed. It is **not** evidence of a waiver.
- The fall from 12/31/2023 to 6/30/2026 is $1.37B (−54%), while core deposits rose. That is consistent with brokered money running off.
- **So what:** about $1.15B of brokered money (6/30/2026) must now leave the bank as it matures, with no waiver possible. The bank has to replace it with non-brokered deposits, and the rate cap in 12 CFR 337.7 limits what it can pay for them. The Q3 RC-E maturity figures are the next public read.

## Q2. The 2023 OCC consent order's own text

**Order #2023-031, docket AA-CE-2023-40, dated Oct 31, 2023. Consent Order under 12 USC 1818(b), no money penalty.** PDF: https://www.occ.gov/static/enforcement-actions/ea2023-031.pdf, downloaded and text-extracted 2026-11-16. **VERIFIED.**

| Topic | In the order? | Exact text |
|---|---|---|
| **Capital minimums** | YES, Art. IV(1) | "ARTICLE IV CAPITAL PLAN AND HIGHER MINIMUMS (1) Within sixty (60) days of the date of this Order, the Bank shall achieve and thereafter maintain the following capital ratios as defined in and as calculated in accordance with 12 C.F.R. Part 3: (a) a common equity tier 1 capital ratio at least equal to eight percent (8%); (b) a leverage ratio at least equal to nine percent (9%); (c) a tier 1 capital ratio at least equal to ten percent (10%); and (d) a total capital ratio at least equal to twelve percent (12%)." (The PDF prints the (a) to (d) labels in a separate column; I re-paired them with their ratios.) |
| CBLR election override | YES, Art. IV(2) | "Notwithstanding any election to use the community bank leverage ratio ("CBLR") framework under 12 C.F.R. § 3.12, the Bank is subject to the minimum capital levels prescribed in paragraph (1) of this Article pursuant to the OCC's authority to impose affirmative corrective actions pursuant to 12 U.S.C. § 1818(b)(6)" |
| Not "well capitalized" | YES, Art. IV(3) | "The requirement in this Order to meet and maintain a specific capital level for any capital measure means that the Bank may not be deemed to be "well capitalized" for purposes of 12 U.S.C. § 1831o and 12 C.F.R. Part 6, pursuant to 12 C.F.R. § 6.4." |
| **Brokered deposits** | Footnote 2 only (attached to Art. IV(3)) | "The Bank may not solicit, accept, renew, or roll over any brokered deposit (as defined in 12 C.F.R. § 337.6(a)(2)) except in compliance with the applicable restrictions of 12 U.S.C. § 1831f and 12 C.F.R. § 337.6." |
| FDIC waiver | **NO.** The order does not mention a brokered-deposit waiver. Every match on "waiver" is either a covenant waiver on loans (Art. X(2)(h), (i)) or the bank's waiver of procedural rights (Art. XVI). | VERIFIED by full-text search of the extracted PDF |
| **Deposit pricing or rate caps** | **NO** deposit-rate article and no cite to 12 CFR 337.7. The only "pricing" wording is in the list of strategic deviations below. | VERIFIED (search on "pricing", "337.7", "rate") |
| Funding-mix freeze | YES, Art. VI(4) | Until the Strategic Plan receives non-objection, "the Bank shall not significantly deviate from the products, services, asset composition and size, funding sources, structure, operations, policies, procedures, and markets of the Bank that existed immediately before the effective date of this Order without first obtaining the ADC's prior written determination of no supervisory objection". Listed significant changes include "fee structure or pricing, … asset composition and size, or funding strategy". |
| Liquidity | YES, Art. VIII(1) | A 5-year Liquidity Program within 30 days that "shall emphasize the importance of a cushion of highly liquid assets; diversified funding sources; and a formal, well-developed, written contingency funding plan, with robust stress testing". (1)(c): "develop a plan to improve the Bank's primary liquidity position (liquid assets) and contingent sources, including secured funding availability". (1)(d) requires a contingency funding plan with "(i) an identification of early warning liquidity triggers; (ii) a quantitative projection of expected funding capacity under appropriate short- and intermediate-term stress events, based on realistic assessments of the behaviors of funding providers during stress events". |
| Disposition trigger | YES, Art. IV(8) | "If the Bank … fails to achieve and maintain the minimum capital ratios as required by paragraph (1) of this Article, then in the sole discretion of the ADC, the Bank shall, upon written direction of the ADC, within sixty (60) days develop and submit … a Disposition Plan that shall detail the board's proposal to sell or merge the Bank, or implement a voluntary liquidation plan in accordance with 12 C.F.R. § 5.48." |
| Reserved growth and capital remedies | YES, Art. XVIII | Possible further actions include "(a) requirements that the Bank make or increase investments, acquire or hold additional capital or liquidity, or simplify or reduce its operations; or (b) restrictions on the Bank's growth, business activities, or payment of dividends." |

**So what (INFERRED):** a total capital ratio of 7.26% at 9/30/2026 is 4.74 points below the order's 12% minimum. It is also below the 8% PCA line. Art. IV(8) has therefore been available to the ADC. Any written direction to file a disposition plan would not be public until or unless the OCC amends the order.

## Q3. OCC actions after 2026-10-30; any PCA or capital directive ever

**Answer: none published. VERIFIED as search results; this does not prove no action exists.**

| Check (2026-11-16) | Result | Status |
|---|---|---|
| EASearch JSON `https://apps.occ.gov/EASearch/api/WebSearch/Actions?q=United%20Fidelity&srt=1&pg=0&pgsz=100`, and `q=703676` | Exactly 2 records: **2023-031** (C&D, 2023-10-31, TerminationDocumentNumber blank, TerminationDate null, i.e. still active); and the OTS Supervisory Agreement of 2010-08-13 (type FA), terminated 2013-08-05 by document 2013-152. | VERIFIED |
| EASearch vintage: `startDteMin=10/01/2026` | 3 actions, the newest dated **2026-10-13** (Bank of America CMP; American Express C&D and CMP on 2026-10-08). So the database holds nothing dated after Oct 13, 2026. | VERIFIED |
| PCA directive (PCAD) or capital directive (CD) for UFB, any year | None. The only UFB records are the two above. The OCC's enforcement-types page lists both PCADs and CDs as published action types. On PCA it says: "Mandatory restrictions and actions are effective when the bank is notified or is deemed to have notice of its PCA capital category. The OCC imposes discretionary restrictions and actions on the bank through the issuance of a PCA directive." (https://www.occ.gov/topics/laws-and-regulations/enforcement-actions/enforcement-action-types/index-enforcement-action-types.html) | VERIFIED |
| OCC November 2026 monthly enforcement release | **Not yet released.** I probed news releases by number: NR 2026-94 (Oct 27), -95 (Oct 29), -96, -97 (Nov 4), and **-99 (Nov 12, "OCC's Semiannual Risk Perspective Highlights Key Risks…")** exist; -98 and -100 to -103 return 404. None is an enforcement release. Per file B, the last enforcement release was NR 2026-93 (Oct 22). The release is expected on the third Thursday, **Thu Nov 19, 2026** (INFERRED from the usual schedule). | VERIFIED (pages); date INFERRED |
| The OCC news-release index page | 404 at `/news-issuances/news-releases/index-news-releases.html`, so I used the per-number probe instead. | COULD NOT REACH (that page) |

**Note (INFERRED):** a 12 CFR 6.3 capital-category notice, an Art. IV(8) written direction, and the capital restoration plan itself are not published by rule or practice. The mandatory PCA restrictions apply automatically from deemed notice (Oct 30, 2026), with no published action. Under 12 CFR 6.1(e), the bank may not state its PCA category "in any advertisement or promotional material" unless the OCC permits it or law requires it.

## Q4. Holding-company filings

Holding companies (from file D and the Fed agreement): **Fidelity Federal Bancorp** (FFED, Nevada, CIK 910492), **Pedcor Financial Bancorp** (no EDGAR record of its own), and **Pedcor Financial, LLC** (CIK 1185822; only Form 4s, last in 2005).

| Check (2026-11-16) | Result | Status |
|---|---|---|
| EDGAR full-text search, 2023-01-01 to 2026-11-16 (`efts.sec.gov/LATEST/search-index`) | "United Fidelity" + "brokered deposit": **0**. "United Fidelity" + "consent order": **0**. "Fidelity Federal Bancorp" + "consent order": **0**. "Pedcor" + "consent order": **0**. "United Fidelity Bank" + "capital restoration": **0**. | VERIFIED |
| "Fidelity Federal Bancorp" (100 hits) | Only FFED's own Form D and two D/As (Jan to Apr 2023, the $25.25M debt sale) plus fund holders: ArrowMark/BANX N-PORT and N-CSR filings, Angel Oak FINS, Thompson. These match file D. Two bank S-1 exhibits (NB Bancorp 2023, Security Midwest 2024) mention the name, most likely in a peer list (not opened). | VERIFIED |
| FFED filing index, `data.sec.gov/submissions/CIK0000910492.json` | Last filing **2023-04-11 D/A**. Nothing since: no 8-K, no offering circular, no 1-A, nothing on the consent order. | VERIFIED |
| **UFB's own CIK 1932454** ("United Fidelity Bank, F.S.B.") | One filing: **Form D, 2023-01-12**. Equity; $6,000,000 offered and $6,000,000 sold; 3 investors; first sale 2022-12-29; Rule 506(b); Piper Sandler & Co. (CRD 665); signed by Donald R. Neel, President & CEO. Directors listed include Bruce A. Cordingley and Gerald K. Pedigo. https://www.sec.gov/Archives/edgar/data/1932454/000110465923003463/primary_doc.xml | VERIFIED. **New to the desk (not in file D)** |
| **NexPoint Capital, Inc.** (CIK 1588272), 10-Q for 6/30/2026 (filed 2026-08-14), https://www.sec.gov/Archives/edgar/data/1588272/000119312526351830/d174913d10q.htm | Schedule of investments: "United Fidelity Bank FSB (6) (7) 7.00 % 1,000 [shares] 1,000,000 [cost] 500,000 [fair value]" at both 6/30/2026 and 12/31/2025, classed as Level 3. A NexPoint 10-K comparative column shows the holding at **$725,000**; the exact period was not pinned down. INFERRED: this is one of the bank-level non-cumulative perpetual preferreds (the 7% Sep 2021 series per file D). | VERIFIED holding and marks; series identity INFERRED. **New to the desk** |
| Fed FR Y-9 reports via FFIEC NIC, https://www.ffiec.gov/npw/Institution/Profile/391575 | HTTP 403, CAPTCHA page. | **COULD NOT REACH** |
| Bond or preferred offering documents after 2021 | None on EDGAR. Private 506(b) deals file only a Form D, which carries no narrative. | VERIFIED (the absence on EDGAR) |

**So what:** no public parent filing discusses brokered deposits, a waiver, the order or capital plans. The only market-visible signals are the fund marks. File D covers the FFED notes at 95 to 99.5 and the FFED preferred at 60. The new item here is **the bank-level 7% preferred, which NexPoint marks at 50**. All marks are dated before the Q3 2026 loss.

## Q5. Federal Register, FDIC press and Fed, 2023 to 2026

| Check (2026-11-16) | Result | Status |
|---|---|---|
| Federal Register API, `conditions[term]="United Fidelity"`, published on or after 2023-01-01 | count **0** | VERIFIED |
| Same search for "Fidelity Federal Bancorp" and for Pedcor | count **0** each | VERIFIED |
| FDIC press (web search, site:fdic.gov) | Only the 2014 to 2020 failed-bank assumptions; none from 2023 to 2026 | Search result |
| Fed enforcement feed, https://www.federalreserve.gov/supervisionreg/files/ea-cms-recent.json | 386 items, newest dated **2026-11-09** (press release 2026-11-12). The only Pedcor item is still: "Written Agreement", edt 2024-06-18, tdt 1950-01-01 (the feed's code for "not terminated"), covering Pedcor Financial, LLC; Pedcor Financial Bancorp; Fidelity Federal Bancorp. No new Fed action. | VERIFIED |

## Binding restrictions on an undercapitalized bank (OCC public sources)

**OCC Comptroller's Handbook, *Problem Bank Supervision*, Version 1.0, Sep 2021.** URL: https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/problem-bank-supervision/pub-ch-problem-bank-supervision.pdf (read 2026-11-16). The PCA chapter (pp. 59 to 73) has these headings:
- PCA Capital Categories
- Notification of Capital Category
- Reclassification Based on Unsafe or Unsound Condition or Practice
- Prohibition on Disclosure of Capital Category
- PCA Restrictions: All Banks
- **PCA Requirements for Undercapitalized Banks**
  - Restrictions on Asset Growth and Expansion of Activities
  - Monitoring Undercapitalized Banks
- Restrictions for Significantly Undercapitalized Banks and Certain Undercapitalized Banks
  - Restrictions on Senior Executive Officer Compensation
  - Discretionary Actions
- PCA Restrictions for Critically Undercapitalized Banks
- Capital Restoration Plans
  - Guarantee of Capital Restoration Plan by Controlling Company

(The OCC has no standalone "Prompt Corrective Action" handbook booklet; the guessed URL returned 404.)

Undercapitalized row of Table 3 ("Summary of Applicable PCA Provisions"), VERIFIED:
- "Same as adequately capitalized banks". That base rule is: "The bank must not make a capital distribution or pay management fees if the bank would be undercapitalized after making such distributions or paying such fees."
- Plus "restrictions on asset growth, acquisitions, new branches, and new lines of business."
- Plus "the bank must submit an acceptable CRP to the OCC within 45 days of the date the bank was notified of its undercapitalized status, unless the OCC specifies a different time frame."
- Plus "discretionary application of certain restrictions otherwise applicable only to significantly undercapitalized banks." These include restricting affiliate transactions, **restricting interest rates on deposits**, further restricting or reducing assets, management changes and divestitures.

Other restrictions in the same booklet, VERIFIED:
- Asset growth: average total assets in a quarter may not exceed the prior quarter's unless three things hold: "the OCC has approved its CRP", the increase is consistent with it, and tangible equity to assets is rising at a sufficient rate.
- Brokered deposits: "not well-capitalized may not accept, renew, or roll over any brokered deposit". The waiver exists only for adequately capitalized banks.
- Deposit rates: "banks that are not well-capitalized may not solicit deposits that exceed the higher of the national rate plus 75 basis points or 120 percent of the current yield on similar U.S. Treasury obligations or federal funds rate plus 75 basis points".
- Discount window: "Undercapitalized banks may not have discount window advances outstanding for more than 60 days in any 120-day period."

## Fetch failures and limits

- orders.fdic.gov: TLS certificate failure (curl exit 60). COULD NOT REACH.
- FFIEC NIC: HTTP 403 CAPTCHA. COULD NOT REACH.
- OCC news-release index page: 404, worked around by probing release numbers.
- eCFR versioner API: intermittent 406 and timeouts. I retried with compression; 303.243, 303.7, 303.8, 309.5, 309.6, 337.6 and 6.1 were read that way. The 337.6 quotes come from Cornell LII.
- Not done in the time box:
  - the Q3 2026 Call Report RC-E brokered-deposit and maturity figures (the next public read on the runoff);
  - the two bank S-1 exhibits that mention FFED;
  - the exact period of NexPoint's $725,000 mark.
