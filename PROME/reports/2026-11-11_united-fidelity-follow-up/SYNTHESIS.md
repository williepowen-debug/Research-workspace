# United Fidelity Bank follow-up: capital since 9/30, supervisory status, properties and borrowers

**Date:** 2026-11-11 (evening, laptop session 99ea8d53). **Row:** DOCKET L1126 (Will, 2026-11-11 18:51 ET). **Author:** PROME synthesis over three read-only Opus researcher reports in this folder (A, B, C). **Entity:** United Fidelity Bank, fsb, Evansville IN, RSSD 391575, FDIC cert 29566; bank-level figures.
**Starting point, not repeated here:** `AGENTS/DEWEY/output/2026-11-11_united-fidelity-losses-and-capital.md` (losses and capital, 9/30 filing) and `AGENTS/CATO/runs/2026-11-11_1821_dewey-bank-population-review.md`.
**Review state:** IMPLEMENTED, author-checked only. PROME recomputed two things at the artifact (marked ✔ below); everything else is a researcher's reading relayed with its tag. No independent read of this synthesis.

## Answer

| Question | Answer | Confidence |
|---|---|---|
| 1. Capital raised or corrective action since 9/30 | None found in public records. Two registers not checked (parent filings on FFIEC NIC, behind a CAPTCHA; the Evansville paper) | SEARCH-NOT-FOUND, not absence |
| 2. Supervisory status | OCC order 2023-031 ACTIVE, no amendment, termination or newer action published; Fed written agreement 24-014 with the three parents ACTIVE. Latest OCC public record is dated 2026-10-13, before any response to the 9/30 quarter could publish | VERIFIED as published; post-quarter action UNKNOWN |
| 3. Properties, borrowers, other lenders | No public document names a loan, borrower or property behind the $2.14B nonaccrual. The bank is developer, owner, lender and fee-earner on affordable-housing projects sold to related-party partnerships. No outside lender is documented on any impaired loan | Borrower identity UNKNOWN; "isolated, in-house" INFERRED |

**Isolated versus shared:** the evidence leans to an isolated concentration inside one group (bank, its service subsidiaries, a sister insurer, related-party partnerships), not an exposure demonstrably shared with other lenders. That is an inference from who holds the loans, not a loan-level finding. Transmission to other banks is NOT shown. The channels that could carry it outward are funding (brokered deposits), collateral sales, and the Ginnie Mae and tax-credit counterparties at sponsor level; none is evidenced as stressed.

## 1. Capital and funding (report A)

| Item | 6/30/2026 | 9/30/2026 | Note |
|---|---:|---:|---|
| Bank equity, $M | 652.5 | 389.7 | ✔ |
| Capital stock sold, YTD | — | 0 | researcher's read |
| Other transactions with stockholders, YTD $M | — | 10.6 (1.5 in Q3) | researcher's read |
| Domestic deposits, $M | 5,297.4 | 5,046.0 | ✔ −251.4 (−4.7%) |
| Brokered deposits, $M | 1,153.5 | 1,006.5 | ✔ −147.0; $510.5M matures within a year (researcher's read) |
| Cash and balances due, $M | 391.0 | 109.2 | ✔ −281.8 (−72%); the researcher's −$283M to $106M is a slightly different cell basis |
| Pledged securities, $M | 935.7 | 1,229.4 | ✔ +293.7 |

- Rule comparison only: total capital 7.26% is under the 8.0% line of 12 CFR 6.4(b)(3); 12 CFR 337.6(b)(3) says an undercapitalized bank may not accept, renew or roll over brokered deposits. The category the OCC assigned and any FDIC waiver are UNKNOWN.
- The bank advertises CDs at 4.20% to 4.45% APY [its site, 11/6] against an FDIC national 12-month average of 1.76% and a national rate cap of 6.20% [10/19].
- No press, no bank or Pedcor statement, no management change found. A depositor-forum thread titled "UFB Ceases Online Sale Of CDs" returned 403; title only, content unread, and "UFB" may mean a different bank.
- Empty searches: Fed H.2 (Chicago and Board, weeks ending 10/3 to 10/31), Federal Register since 6/1, FDIC structure history, OCC October enforcement release, OCC corporate applications since 7/1 (report B, control query passed).

## 2. Supervisory status (report B)

| Agency | Record | Date | Status |
|---|---|---|---|
| OCC | Consent order 2023-031 (AA-CE-2023-40) | 2023-10-31 | Active; not in any of 36 monthly releases as terminated or amended |
| Federal Reserve | Written agreement 24-014 with Pedcor Financial LLC, Pedcor Financial Bancorp, Fidelity Federal Bancorp | executed 2024-06-18 | Active; no distributions (sub-debt interest included) and no new or guaranteed debt without approval |
| OTS (historical) | Supervisory agreement, lead article affiliate transactions and Regulation W | 2010-08-13 | Terminated 2013-08-05 |
| FDIC | Bank active in BankFind [11/6]; not on the failed-bank list | — | FDIC orders site failed (certificate error): search incomplete |

- The 2023 order targets the multifamily book: concentration limits that name "commercial real estate, including multifamily affordable housing" with stress tests (Art. VII), allowance segmentation of the multifamily portfolio (Art. XII), and loans over the legal lending limit "inappropriately supported by the diminished credit derivatives' structure" (Art. X(g), XIII). It has no affiliate-transaction article. Art. XVII: "troubled condition".
- Art. IV(8): the trigger for a sale, merger or liquidation plan appears met on the 9/30 ratios; it needs the OCC's written direction, at its discretion. No public record of one.
- ⚠️ INFERRED from rule text, not a notice: a capital restoration plan would be due about 2026-12-14 (45 days from the filing date) if the ordinary rule applies. Such a plan needs a parent guarantee; whether the Fed agreement's debt-guarantee bar reaches it is unsettled in public text.
- Next public source: the OCC's November enforcement release (about the third week of November).

## 3. Loans, borrowers, properties (report C)

- **Model (VERIFIED, OCC CRA evaluation 2024-01-08, rating Outstanding):** the bank "on its own and through its wholly owned service corporation subsidiaries develops, owns, finances, and invests in affordable housing projects throughout the country"; 87.8% of loans multifamily at end-2022; loans converted to Ginnie Mae securities. Pedcor is not named.
- **Loan data (HMDA, ✔ recomputed by PROME from the CSVs in `hmda/`):** multifamily originations 2021: 69 loans, $873.2M · 2022: 161, $2,807.1M · 2023: 24, $442.8M · 2024: none · 2025: 2, $52.7M. Total 256 loans, $4.176B, every one retained (no purchaser). 117 first liens, 139 second liens. By state, $M: IN 1,257 · FL 598 · NC 560 · OH 531 · GA 510 · CO 447 · TN 139 · SC 70. (The researcher's "256 loans, $4.18B in 2021 to 2023" is the five-year total; 2021 to 2023 is 254 loans, $4.123B.) Researcher's read, not recomputed: all balloon, 250 interest-only, median loan-to-value 85%, median rates 2.78% to 3.35%. Linking these loans to the nonaccrual set is INFERRED.
- **Credit protection (secondary, AM Best 2026-03-25):** sister company Pedcor Assurance wrote credit derivatives supporting the bank and stopped in Q3 2024.
- **Beyond the loans:** $1.032B of real-estate venture investments and a $146.7M development-fee receivable payable from project cash flows (9/30 filing, researcher's read; parent's 2021 SEC offering filing describes the fees as related-party and contingent).
- **Why now:** the only explanation on record is the bank's note that the loans were current before nonaccrual. The impaired loans sat in the 1 to 3 year maturity or repricing bucket at 6/30 (INFERRED from the bucket falling $3.09B to $0.64B). Balloon and refinance risk, appraisals and examiner pressure are hypotheses; no document says any of them caused the move.
- **Recovery:** no appraisal, occupancy figure, sale, foreclosure, receivership or lawsuit found.
- **Florida:** $598M of originations (Escambia $147M, Leon $94M, Lee $86M per the researcher). Whether any Florida loan is impaired is UNKNOWN.

## Limits and what would change the read

- No finding here forecasts failure, sizes further loss or supports a sector conclusion. The $2.14B nonaccrual balance is not a loss estimate.
- Blocked and not evaded: Pedcor's site (403), HUD tax-credit database, FFIEC NIC parent pages (CAPTCHA), EMMA not attempted, FFIEC amended-filing check not attempted.
- Would change it: an OCC action in the November release · a recapitalization, sale or change-in-control filing · recorded mortgages naming borrowers or senior lenders (match HMDA tracts to county records) · the parents' filings on NIC.
- Not done: TERRY's tradeability read (requested by DEWEY, packet in TERRY's inbox, and again by PROME tonight).

## Addendum, 2026-11-11 20:22 ET: Phase 1 legs B and C of the research plan (reports D and E)

Relayed from the two researcher reports with their tags; PROME has not rechecked these at the sources. Plan: `PROME/plans/2026-11-11_united-fidelity-research-plan.md`.

**Parent paper (report D).** Fidelity Federal Bancorp sold $113.75M of subordinated notes since 2018: $30M 6.785% due 10/2028 · $23.5M 6.00% due 11/2029 (CUSIP 315921AJ5, now 3-month SOFR + 4.65%, 8.40% at 8/31) · $35M 4.50% due 3/2031 · $25.25M sold 12/2022, terms unfound. Holders found, each under 1% of its fund: ArrowMark Financial (BANX) former TARP preferred at 60% of liquidation value, 0.88% of net assets · Angel Oak Financial Strategies Income Term Trust (FINS) $3.0M of notes, 0.66% · Thompson Bond Fund (unlisted) $13.5M, 0.69%. Marks 95 to 99.5% of par through 8/31, all before the Q3 loss was reported; first marks after it: BANX about late November, FINS about late December, Thompson about January. No rating, no recorded missed payment. Fed agreement paragraph 5(a) requires prior approval for interest on subordinated debentures; "no deferral right" is from the offering summary, indenture unread (INFERRED consequence: an unapproved coupon is a missed payment). **Read: no listed holder is materially exposed; the bond trail closes as a trade expression and stays as a dated tell.**

**Borrowers (report E).** No recorded mortgage could be read (every county site blocked automation); evidence is Florida UCC-1 filings naming the bank as secured party, state parcel data and Pedcor's documented purchases. In a sample of 14 matched properties: 9 owners at Pedcor's Carmel headquarters address, 1 co-owned with a Pedcor partnership, 3 "New ___ LLC" entities at 8902 N Meridian St, Indianapolis (a second sponsor group; Pedcor staff still prepared the bank's lien filing on the one checked), 1 unknown. The Florida properties are existing complexes built 1974 to 2005, bought 2020 to 2022, each carrying a first and one or two junior liens to the same bank (for example The Westcott, Tallahassee: $77.9M plus $16.3M). No assignment to another lender, Federal Home Loan Bank or trustee in the seven UCC histories read. Maturities, modifications and foreclosure filings UNKNOWN; property distress not searched. Sample only, not the population; related-party status rests on addresses, not registry records.

**Decision under the plan's gate:** leg C points to (a), a group financing its own and a co-sponsor's apartment purchases at 2021 to 2022 prices with stacked liens from its own bank. Phase 2 (the cross-lender vintage screen) is NOT run. Remaining: TERRY's screen and HOMER's read Thursday 11/12; the dated tells (OCC November release, the three fund marks, the Q4 Call Report).
