# October20 EGBN cash-outcome source audit

Raw request receipts: retrieval.json and extra-retrieval.json (UTC retrieval/status/bytes/SHA256/resolved URL). A200 HTML player/login is not usable audio/records. Source dates remain Q1/Q2/July/August as stated; fresh download does not advance the observation date. Browser-derived access below was checked October20; no failed local response is relabeled as successful raw-source retrieval.

## Primary evidence and locators

- Q1-deck.html and Q1-slide027/028.jpg: SEC0001050441-26-000062. Slide27 Prince George's special-mention row2:56.000; maturityApr21; appraisal62.2/Mar9; LTV90%; DSCR0.62. Slide28 row14:56.000; same maturity/date, appraisal63.7/LTV88%. Original images inspected.
- Q2-deck.html and Q2-slide025/026.jpg: SEC0001050441-26-000088. Slide25 Prince George's substandard row1:56.000/Aug21,63.7/Mar9,88%,0.63 atApr30, accruing. Montgomery storage SM1; Fairfax office SS5; Anne Arundel storage SS10. Slide26 rows14/15 repeat storage/apartment top-loan values and list apartment as Construction CRE. No unique property/borrower identifier supplied. Slide24 has the nonaccrual bridge128.761+36.038−14.658−24.982−14.035=111.124; source HTML text read, prior full source work reused.
- Q2-10Q.html, SEC0001050441-26-000096: selected Note1 modification/collectibility policy and Note4 modification/collateral tables rechecked. Tables78/82 are aggregate hardship modifications, not identified same-loan outcomes. Do not infer that every extension must appear in the hardship-modification table or that a generic reserve is allocated to the56M loan.
- SEC-submissions.json: entity EAGLE BANCORP INC/CIK1050441; filing dates throughOct19Form4. Latest8-K/A Sep14. Latest-8KA.html is solely CEO committee-assignment update, not credit information. Latest10-Q in recent snapshot isAug6 Q2. Search scope = returned submissions snapshot, not an exhaustive review of every historical exhibit.
- Official-Q2-release.html identifies July23 call and replay window throughAug6. Official-Q2-webcast.html is only the accessible JavaScript player shell. No original audio or verbatim primary transcript was obtained; secondary transcript attribution remains explicit.
- Q3 date: https://ir.eaglebankcorp.com/news/news-details/2026/Eagle-Bancorp-Announces-Earnings-Call-on-October-22-2026/default.aspx — browser primary text confirms Oct21 after-close results/Oct22 10ET call. LocalQ3-date.html is403 and retained as failure. Browser IR overview still listsQ2 as latest quarter; directIR-overview.html403.

## Secondary statement evidence, not independent loan evidence

Q2-transcript-secondary.html (StockAnalysis; source creditQuartr, July23): analystSteve Moss asks about56M PG apartment and Montgomery storage; Ryan Riel reportedly expects longer-term restructure of PG and full payoff of storage by year-end. An expectation is not a completed restructuring, cash payoff or a loss estimate. Secondary summaries and duplicate transcript hosts do not add independent corroboration. KBRA-Aug7.html is the agency's own Negative-outlook opinion; it uses bank disclosures and does not independently verify this property's cash.

## Public-record access

- MD-land-records.html redirects to official login https://landrec.msa.maryland.gov/Pages/Login.aspx. MD-account-help.html and MD-search-guide.html confirm remote account/contact information and email authentication. Official guides describe free access. No credentials/session available; no account created or authenticated index search completed.
- MD-case-search.html is403; browser portal had no usable text. No actual docket search was run. The application form's generic status/error text is not an account-status finding.
- Fairfax-land-records.html is404 on an older guessed route. Fairfax-current-CPAN.html200 at https://www.fairfaxcounty.gov/circuit/online-services/court-public-access-network confirms subscriber service. No current subscription fee is asserted from old notes; no account created/purchase made.
- A matched land-record release could verify release of a lien, not necessarily par recovery or who funded repayment. Absence of a recorded amendment does not prove no amendment; recording can lag. No court/land-record result exists here for these four loans.

## Identification searches and nonmatches

Indexed query families: EagleBank + Prince George/apartment/56million/56/Hyattsville/Greenbelt/April/construction/refinance/September/October2026; EagleBank + Montgomery/storage/56/payoff; EagleBank + Anne Arundel/storage/foreclosure; EagleBank + Fairfax/office/22million/foreclosure. No attributable current outcome found. This is bounded SEARCH-NOT-FOUND, never proof of absence or a substitute for an authenticated title/docket search.

Two lender-originated announcements were read as possible identification channels only:
- The-Six-origination.pdf, July18,2022: Residences at The Six,6400 America Boulevard,316units, sponsorPerseusTDC/Transwestern/Griffin; Eagle loan amount not stated. No56M/maturity/criticized-loan link established.
- Margaux-origination.pdf, April27,2022: Urban Atlantic's The Margaux,291units in NewCarrollton; original financing54.25M, separate Amazon low-rate loans25.4M. Original financing differs from56M; subsequent amendments unknown. No link to the criticized loan established.

These properties and sponsors are NOT identified distressed borrowers in this research. County, lender and property type alone do not make a match. No extra property-level distress search or allegations made against them.

Search results also included an old Tysons land foreclosure and a newspaper's mixed-column foreclosure notices. Neither can be matched to the four loans; no balance, loss or court-case identifier attributed from those snippets. Broad search false positives include EagleBank Arena, PrinceGeorgeVirginia, other Eagle institutions and the2011 small-business capital raise; excluded.

## Verification

calculate.py uses manually transcribed, visually checked original slide inputs. It verifies all successful raw request hashes and reproduces the gross-outflow decomposition and hypothetical net-sale arithmetic. It does not certify bank-reported inputs, primary audio, independent recoveries or actual loss reserves. No later economic outcome date is substituted for the June baseline. Current unknowns and next disclosure tests live in the main report and existing workbook rows008/009/013/014.
