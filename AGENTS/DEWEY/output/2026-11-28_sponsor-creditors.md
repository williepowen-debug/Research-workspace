# Do the Pedcor and Birge & Held groups, and United Fidelity's three parents, owe anyone besides the failed bank?
**Date:** 2026-11-28 (00:27 ET onward, from `date`) | **Mode:** Thesis | **Confidence:** High for what was found (fund filings, Call Report, OCC, IHCDA); Low for completeness (EMMA, county records, Ginnie Mae and FDIC sites refused automation)
**Commission:** PROME prome-80, plan leg 2 (WQ-759 RULED A, Will 23:40 ET 11/27; `PROME/plans/2026-11-27_bank-failure-investigation-PLAN.md`). Session dewey-2026-11-27-8654c74a. Interpretation belongs to REGINALD.

## Key finding
Outside creditors exist. They sit almost entirely in the **parents' capital structure**, not beside the bank on the properties.
- **Already on the record:** Fidelity Federal Bancorp's $113.75M of subordinated notes and the former TARP preferred (report D).
- **New tonight:** a separate issue, the **Pedcor Bancorp 144A subordinated notes due 2/15/2029** (CUSIP 705307AA4, 8.60% floating at 8/31/2026). Pedcor Bancorp was merged into Pedcor Financial Bancorp in 2021. Thompson Bond Fund has held $3.0M of it since at least 2019. The issue's total size is not public.
- **Funds' last marks:** no registered fund that holds the parents' paper had marked it as distressed at its last date (Thompson at 8/31/2026: 95% to 99%, not in default or arrears). Every one of those marks predates the Q3 loss disclosure.

**Sponsor-level bonds:** the Pedcor housing bonds found in money funds carry letters of credit from **other** institutions. These are Citizens Bank and then the Federal Home Loan Bank of Boston on Forest Ridge, an unnamed Federal Home Loan Bank on Elkhart, and U.S. Bank on Nashville. None is shown to be United Fidelity's own letter of credit.
- The Forest Ridge bonds (FHLB Boston) were put up for refunding by the Indiana housing agency in September 2025. They have not appeared in any money-fund filing since 10/31/2025.

**Not seen:**
- No missed payment, default notice or rating action was found anywhere. **EMMA refused automated access (HTTP 403)**, so bond notices could not be read.
- On its own Call Report, United Fidelity had issued **$166.7M of standby letters of credit**, of which **$166.4M was "conveyed to others"**, to parties not named on the form. It also had **$228.6M of letters of credit issued by another party, such as an FHLB, on its behalf**. Those are the bank's own outside counterparties. Who they are cannot be seen in public data.

## Creditors and counterparties found outside the failed bank

| # | Who | Instrument | Amount | Date | Source | Stressed? | State |
|---|---|---|---|---|---|---|---|
| 1 | Holders of Fidelity Federal Bancorp subordinated notes: Thompson Bond Fund ($6.5M 2028 at 95.2%; $7.0M 2029 at 99.3%), Angel Oak FINS ($3.0M), others unknown | FFED subordinated notes (315921AG1, AJ5, AL0, plus a 12/2022 issue) | $113.75M face sold since 2018 | Thompson 8/31/2026 | Thompson N-PORT acc 0000894189-26-029528 (read tonight); report D | Marks near par; `isDefault` N, arrears N, all before the Q3 loss. Holding company sits outside the receivership: impairment INFERRED (REGINALD 11/27) | VERIFIED holdings; impairment INFERRED |
| 2 | **Holders of Pedcor Bancorp 144A subordinated notes:** Thompson Bond Fund $3.0M (97.9% at 8/31/2026); Schwab Prime Advantage MMF held $2.0M as repo collateral from J.P. Morgan Securities, 4/30 to 8/31/2026 (GIBBS) | Subordinated notes due 2/15/2029, CUSIP 705307AA4, coupon 8.60% at 8/31/2026 | Issue size NOT FOUND; Thompson held since ≥ Q1 2019 | 8/31/2026 | Thompson N-PORT (same acc); EDGAR full text 2017–2026 (32 filings, Thompson and Schwab only) | Not in default or arrears at 8/31 | VERIFIED |
| 2a | Obligor today | Pedcor Bancorp merged into **Pedcor Financial Bancorp** (survivor) in 2021, so the notes are PFB's debt. PFB owns about 97.7% of FFED, so these notes sit **one level above** the FFED notes and behind them in reaching bank value | — | 2021 | FFED Form 1-A, acc 0001104659-21-092171 ("Tier 2 Merger", "Pedcor Financial Bancorp as the surviving corporation") | — | Merger VERIFIED; succession to the notes INFERRED (indenture not read) |
| 2b | Is this in addition to the $113.75M? | **Yes.** Different issuer (Pedcor Bancorp, not FFED) and a different CUSIP family (705307 vs 315921). Report D's $113.75M is FFED only | — | — | report D table; this filing set | — | VERIFIED |
| 3 | Other FFED debt at 12/31/2020: promissory note due 1/2027 ($5.0M); note due 7/2026 ($1.739M); secured note to the Gerald K. Pedigo Trust due 6/2029 ($0.71M, an insider); participation notes; $8.0M 8.25% debentures to a StoneCastle CLO (report D) | Holding-company notes | about $15.5M | 12/31/2020 | FFED 1-A (2021) notes to financials | Current balances UNKNOWN | VERIFIED as of 2020 only |
| 4 | **Federal Home Loan Bank of Boston**, preceded by **Citizens Bank, N.A. (Providence)** | Demand feature (letter of credit) on City of Indianapolis variable-rate demand MFH revenue bonds, Series 2007A, Forest Ridge Apartments (Pedcor Investments-2006-LXXXVIII LP), CUSIP 45528TAD6 | $12.595M | in money funds 9/2017 to 10/31/2025; absent after | Federated N-MFP3 (82 filings parsed); IHCDA notice PN-25-36 (9/12/2025): refunding notes up to $12.595M "for the purpose of refunding ... the Series 2007A Bonds" | None seen; yield 3.32% at 10/31/2025 | VERIFIED; refunding completed INFERRED |
| 4a | On whose behalf the FHLB Boston letter of credit was issued | United Fidelity was a member of **FHLB Indianapolis** (FFED 1-A, 2021: "UFB also is a member of and owns stock in the Federal Home Loan Bank of Indianapolis"). An FHLB issues letters of credit only for its own members. The letter of credit passed from Citizens Bank to FHLB Boston, and Citizens is in the Boston district. So this was **not United Fidelity's letter of credit**; a Citizens confirming structure is the likely form | — | — | same | — | INFERRED (bond documents on EMMA not readable) |
| 5 | An FHLB, unnamed ("FEDERAL HOME LOAN BANKS") | Demand feature on County of Elkhart VRDN (Pedcor Investments-2007-CIII LP), CUSIP 287477AG8 | $1.035M at American Century Tax-Free MMF | 10/31/2026 | American Century N-MFP3 acc 0001410368-26-110931; N-CSR 5/31/2026 ($1.06M) | Yield 3.29%, held at par | VERIFIED; which FHLB and which member NOT FOUND |
| 6 | **U.S. Bank NA** | LOC on Nashville and Davidson County H&EFB MFH revenue bonds, Pedcor Investments Series 2006A, VRDO | $10.0M | last seen 2/28/2023 (JPMorgan muni money funds) | JPMorgan Trust N-CSR acc 0001193125-23-135692 | Still outstanding? NOT FOUND (no fund filing after 5/2023 names it; EMMA blocked) | VERIFIED to 2/2023 |
| 7 | FHLB Indianapolis (historical) | LOC on Ohio HFA MFH (Pedcor Willow Lake, Series B) and Hamilton OH MFH (Pedcor Knollwood Crossing II, 2003B) | $0.165M; $0.355M in funds | 2016–2017 | Fidelity Municipal Trust II and Federated N-MFP filings | Old; current status UNKNOWN | VERIFIED (historical). United Fidelity, an FHLB Indianapolis member, is a possible account party, INFERRED only |
| 8 | United Fidelity's own letter-of-credit counterparties | Financial standby LOCs **issued** $166.7M, of which $166.4M **conveyed to others** (RC-L 2, 2.a); standby LOCs **issued by another party (e.g., an FHLB) on the bank's behalf** $228.6M (RC-L 9.c); pledged loans $479.9M; pledged securities $1,229.4M | as stated | 9/30/2026 (6/30: 166.8 / 166.4 / 229.1) | UFB SDF Call Report | Counterparties not named. The FHLB-on-behalf amount was **flat in Q3 (−$0.6M)** while pledged securities rose $293.7M, so **the form does not tie the Q3 pledge rise to letters of credit** | VERIFIED cells; who holds them NOT FOUND |
| 9 | Tax-credit investors in Pedcor projects | U.S. Bank: syndicator and investor, Willow Lake II, Lima OH (2024, OHFA; report C) · U.S. Bancorp: Rosewood Terrace, OR, withdrawing (2017–18) · MutualBank (MutualFirst, since acquired): 8 Pedcor partnerships (10-K 2015) · Fifth Third: subsidiary "Pedcor Investments 1994 XX LP" (10-K 2010) | not stated | 2010–2024 | EDGAR full text; OHFA proposal; web search | None tied to a United Fidelity-financed property; nothing found for 2021–23 Florida or Indiana deals | VERIFIED as listed; coverage thin |
| 10 | Birge & Held | Property manager (not borrower, sponsor or guarantor) of Alpine Studios, loan 20 in D2-Natixis Multifamily Mortgage Trust 2026-M1, $10.55M; sponsor Aminim Properties | — | 8/17/2026 | 424B2 acc 0001539497-26-002280 (FLG); EDGAR full text "Birge & Held" 7 hits, no borrower role | — | VERIFIED |
| 10a | Pedcor or Birge & Held as borrower, sponsor or guarantor in CMBS, CRE CLO or other EDGAR deal documents | none | — | 2010–2026 | EDGAR full text across 424B2/424B5/424H/FWP/ABS-EE/10-D: "Pedcor" 0 deal hits; "Birge & Held" Natixis only | — | SEARCH-NOT-FOUND (Freddie K and Fannie DUS are not on EDGAR and were not searched) |
| 11 | Ginnie Mae | United Fidelity held **$642.9M HTM (amortized cost) and $625.5M AFS (fair value)** of agency commercial MBS (RC-B 4.c.1.a, "FNMA, FHLMC or GNMA"), consistent with its own converted loans. **It reported no servicing for others** | as stated | 9/30/2026 | UFB SDF | Securities guaranteed; they passed to the buyer with "substantially all assets" (INFERRED). Ginnie's issuer list is a JavaScript app with reCAPTCHA and was not read | VERIFIED cells; issuer and servicer NOT FOUND |
| 12 | First Citizens and the FDIC Deposit Insurance Fund | Whole-bank purchase; DIF cost estimate $1.83B | — | 11/27/2026 | REGINALD 11/27 (FDIC, First Citizens releases) | the realized outside loss | VERIFIED (relayed) |
| 13 | Holders of FFED preferred (BANX) | Former TARP cumulative perpetual preferred, Series A and B | marked $1.64M (55%) | 9/30/2026 | REGINALD 11/27 (BANX N-PORT) | yes: 60% to 55% | VERIFIED (relayed) |

**No Florida property is named in any of the above.** The bonds are in Indiana, Ohio, Tennessee and Michigan. No CORAL packet was sent.

## OCC directive: when it became public (lead 8)
- The October release (NR 2026-93, 10/22/2026) published dockets AA-ENF-2026-41, -43, -46 and -47; **-42 is absent**.
- The November release (NR 2026-104, 11/24/2026) published -45; **-42 is absent**.
- So the directive (AA-ENF-2026-42, 9/17/2026, amended 9/29) **was not in either monthly release**. PROME's 11/25 read was correct: the directive was not public through the releases.
- The Wayback Machine has no capture of the OCC enforcement search or of an AA-ENF-2026-42 document. The date the listing first appeared is UNKNOWN. It is visible now with a termination date of 11/27, which suggests it was posted at or after the closing (INFERRED).
- **New primary:** OCC NR 2026-106 (11/27/2026) gives the closing grounds as "unsafe or unsound condition to transact business and was likely to be unable to pay its obligations or meet its depositors' demands in the normal course of business". Those are liquidity grounds as well as condition grounds.

## Read on the plan's branch (c): does the loss reach outside parties?
- **Yes, but through the holding companies, and small next to the fund's loss.** Identified outside holders of parent paper:
  - Thompson: $16.5M face ($13.5M FFED plus $3.0M Pedcor Bancorp).
  - FINS: $3.0M face.
  - BANX: preferred marked at $1.64M.
  - Schwab: $2.0M, but as repo collateral, so its claim is on J.P. Morgan Securities.
- **Total outside paper:** at least $113.75M FFED notes, plus the Pedcor Bancorp notes (size unknown), plus about $15.5M of 2020-dated FFED notes, plus the preferred. That is on the order of **$130M to $150M face known**, against a DIF cost of **$1.83B**. Recovery depends on assets the holding companies hold outside the bank (REGINALD's lane).
- **Not shown:** any loss to another lender on the properties. The sponsor bonds in money funds are backed by other banks' or FHLBs' letters of credit, and those stand in front of the bondholders. A letter-of-credit bank takes a loss only if a Pedcor partnership fails to reimburse a draw, and no draw or default was found.
- **Open channel that public data cannot close:** the $166.4M of United Fidelity standby letters of credit "conveyed to others", and the $228.6M of letters of credit that another party (most likely FHLB Indianapolis) issued on the bank's behalf. With a whole-bank purchase these most likely moved to First Citizens (INFERRED; the purchase agreement is not posted).

## Forward view (unscored, no row; interpretation REGINALD's)
- **Next readable tells:**
  - Thompson's N-PORT for 11/30/2026 (filed about late January). Expect the FFED and Pedcor Bancorp notes to carry default or arrears flags and much lower marks if the holding companies stop paying.
  - FINS 10/31 holdings (about late December).
  - BANX 12/31 (about late February).
  - Coupon dates: FFED 2029 notes pay quarterly (next about 2/1/2027, from report D). The Pedcor Bancorp note coupon dates are not known; the maturity is 2/15.
- **What would change the read:**
  - an EMMA failure-to-pay or letter-of-credit substitution notice on a Pedcor bond;
  - a purchase agreement showing the receiver kept the letters of credit or the participations;
  - a bankruptcy filing by FFED or Pedcor Financial Bancorp naming other creditors.

## What could not be seen
- **EMMA** (403 to automated access; bond notices, trustees, letter-of-credit providers and continuing disclosure).
- **County recorders** (blocked 11/11; not retried).
- **Ginnie Mae issuer pages** (JavaScript and reCAPTCHA).
- **FDIC orders.**
- **PACER** (out of scope).
- The **indentures** of both note programs.
- Who holds United Fidelity's **conveyed letter-of-credit participations**.
- **Tax-credit investors** on the 2021–23 properties United Fidelity financed.
- **Freddie K and Fannie DUS** deal documents (not on EDGAR).

## Counter-evidence
- Fund marks near par and "not in default" are all dated before the Q3 loss and closing. They say nothing about value now.
- A letter-of-credit structure means outside banks do carry Pedcor project credit, even with no default seen. Absence on EMMA is absence of a read, not of notices.

## Source quality
Primary: EDGAR fund filings (492 money-fund filings parsed, 117 Pedcor holding rows), N-PORT, Form 1-A, the United Fidelity Call Report, OCC releases, IHCDA. Relayed: REGINALD and GIBBS 11/27 rows, tagged. Secondary: web search for tax-credit syndicators.

## References (accessed 2026-11-28, 00:00 to 00:27 ET)
- EDGAR full-text search (efts.sec.gov), queries as named.
- Thompson N-PORT acc 0000894189-26-029528.
- Federated N-MFP3 acc 0001193125-25-271499.
- American Century N-MFP3 acc 0001410368-26-110931 and N-CSR acc 0000746458-26-000004.
- JPMorgan Trust N-CSR acc 0001193125-23-135692.
- FFED Form 1-A acc 0001104659-21-092171.
- FHLB Indianapolis 10-K acc 0001331754-21-000050.
- MutualFirst 10-K acc 0001144204-15-015950.
- Fifth Third 10-K acc 0001193125-10-042347.
- IHCDA PN-25-36: https://secure.in.gov/ihcda/files/PN-25-36-Notice-of-Public-MF-Refunding-Notes-Forest-Ridge.pdf (copy in research folder).
- OCC NR 2026-93, 2026-104, 2026-106 (text in research folder).
- Ginnie Mae multifamily issuer page (not readable).
- OHFA Willow Lake II proposal (report C).
- Research folder: `AGENTS/DEWEY/research/2026-11-28_sponsor-creditors/`. The helper `nmfp_pedcor.py` reproduces the money-fund table.

## Process report
**Searches:** about 20 EDGAR full-text queries; 492 N-MFP filings parsed; 9 OCC pages; 3 web searches.
**Blocked and not evaded:** EMMA 403; Ginnie Mae reCAPTCHA; FDIC orders (TLS).
**Not done:** the Washington Prime Group 8-K mention of "Birge & Held" (unread); the Schwab N-MFP3 for September and October (EDGAR full text shows none naming Pedcor after the 9/8 filing).
**If I had more time/tools:** a person's browser read of EMMA for CUSIPs 45528TAD6, 287477AG8 and the Nashville 2006A bonds; the FDIC purchase agreement when posted.
