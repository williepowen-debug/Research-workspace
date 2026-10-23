# A. Oracle credit stack and the "SoftBank investing in Oracle" claim
Reader A (read-only). Compiled 2026-10-22 ~20:45 ET (`date` run 20:41 EDT). WebSearch calls used: 14 of 25. No trade recommendation.
Tokens: VERIFIED = read at the primary (SEC filing/IR release, fetched this session) · INFERRED = derived or supported but not read at the primary · SEARCH-NOT-FOUND · UNKNOWN. "Press" = reported, not filed.
Fiscal-year note: Oracle FY ends May 31. FY2027 = Jun 2026 to May 2027. Q1 FY27 = quarter ended 2026-08-31.

## 0. Answer in brief
- The SoftBank claim: **SEARCH-NOT-FOUND** as stated. No 2026 SoftBank equity stake in Oracle, bond purchase, convertible, or SoftBank financing of Oracle data centers found in press or SEC filings. The only SoftBank-to-Oracle money flow in the primary record is the opposite direction from "investing in Oracle": SoftBank Group bought Ampere and paid Oracle $4.3B cash (closed 2025-11-25; 10-K FY26). See section 5.
- Oracle total debt $125.3B at 2026-08-31 (10-Q, sum of two balance-sheet lines), cash plus securities $37.1B, net debt about $88.3B (derived). Off-balance-sheet: $288B of data-center lease commitments not yet commenced plus $34.2B unconditional purchase obligations. These two dwarf the funded debt.
- Ratings: S&P BBB- stable since 2026-07-09 (press; S&P release not read). Moody's Baa2 negative (affirmed 2026-02-02, press). Fitch BBB (February 2026 press; outlook not found).
- 5Y CDS: fleet DTCC anchor 315-320bp (10/21). Press: 144bp start of year, 198bp 7/17, 215bp early Aug, 261bp 10/8, 288bp 10/15, about 295bp / 300 touch by 10/19.

## 1. Debt stack (latest 10-Q, period ended 2026-08-31, filed 2026-09-11)
Source: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm (accession 0001193125-26-389274). All VERIFIED unless marked.

| Item | 2026-08-31 | 2026-05-31 |
|---|---|---|
| Cash and cash equivalents | $36,369M | $31,289M |
| Marketable securities | $708M | $605M |
| Notes payable and other borrowings, current | $7,625M | $7,199M |
| Notes payable and other borrowings, non-current | $117,712M | $122,342M |
| Total borrowings (sum of two lines; not a reported total) | $125,337M | $129,541M |
| Net debt (derived: borrowings less cash less securities) | about $88,260M | about $97,647M |
| Senior notes and other LT borrowings, face | $125.0B | $128.1B |
| Same, estimated fair value (Level 2) | $105.7B (84.6% of face) | $114.4B (89.3%) |
| Operating lease liabilities / finance lease liabilities | $34,621M / $9,185M (lease maturities table, 10-Q Note 6) | not read |
| Mandatory convertible preferred (6.50% Series D) | $5.0B liquidation preference (100M depositary shares at $50) | issued 2026-02-05 |

- Q1 FY27 debt movement (10-Q MD&A): $3.1B cash scheduled repayments, $1.1B commercial paper repaid, $4.6B long-term borrowings reclassified to current. The interest-expense paragraph says "scheduled repayments of $8.1 billion" in Q1; that does not match the $3.1B cash line. UNKNOWN which is right; not resolved.
- No new senior notes issued in Q1 FY27 (10-Q financing section lists only the $20B ATM). No 2026 bond issue after Feb 2026 found in 8-K list (EDGAR 8-K index through 2026-09-14). VERIFIED against the 8-K list; SEARCH-NOT-FOUND for anything after 9/14.

### Scheduled principal maturities (10-K FY26, as of 2026-05-31; fiscal years)
Source: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm (10-K filed 2026-06-22). VERIFIED.

| Fiscal year (ends May 31) | Principal due | Approx calendar span |
|---|---|---|
| FY2027 | $7,210M | Jun 2026 to May 2027 |
| FY2028 | $10,145M | Jun 2027 to May 2028 |
| FY2029 | $5,500M | Jun 2028 to May 2029 |
| FY2030 | $7,250M | Jun 2029 to May 2030 |
| FY2031 | $9,750M | Jun 2030 to May 2031 |
| Thereafter | $90,250M | |
| Total | $130,105M | |

Specific instruments in that stack (10-K): term loan credit agreement 2, $5.63B original, SOFR plus 112.5-162.5bp by rating, balance $5.137B at 5/31/26, final due 2027-08-16 (extendable); $10.0B 5-year revolver signed 2026-03-06 (undrawn at 5/31/26; due 2031-03-06; SOFR plus 87.5-150bp by rating; covenant EBITDA / net interest not below 3.0x); commercial paper program raised to $10.0B on 2026-03-06 ($1.468B outstanding 5/31/26). Pricing on the revolver and term loan steps with the credit rating, so the BBB- cut raises those margins (INFERRED direction; grid read, step not computed).

### 2026 issuance (all in FY26 or later; Q1 FY27 had none)
| Date | Instrument | Size | Terms | Order book / spread | Source |
|---|---|---|---|---|---|
| 2026-02-02 priced, 2026-02-04 closed | Senior notes, 8 tranches | $25.0B | $0.5B FRN 2029 (SOFR+111bp); $3.0B 4.550% 2029; $3.5B 4.950% 2031; $3.0B 5.350% 2033; $5.0B 5.700% 2036; $2.25B 6.550% 2046; $5.0B 6.700% 2056; $2.75B 6.850% 2066 | Press: orders over $129B (one source $155B); longest tranche about +195bp over Treasuries after initial talk about +225. Spreads at issue for other tranches not found. | Terms VERIFIED: https://www.sec.gov/Archives/edgar/data/1341439/000119312526037840/d23732d8k.htm and ex 4.1. Order book/spread INFERRED (Bloomberg via https://news.bgov.com/capital-markets/oracle-is-selling-25-billion-of-high-grade-bonds-for-ai-4 and itiger summary) |
| 2026-02-02 to 2026-02-05 | 6.50% Series D mandatory convertible preferred (converts Jan 2029) | $5.0B | 100M depositary shares; dividends may be paid in cash or stock; blocks common dividends if arrears | | VERIFIED: https://www.sec.gov/Archives/edgar/data/1341439/000119312526039344/d63638d8k.htm |
| 2026-02-02 program, fully used in Q1 FY27 | Common stock ATM | $20.0B gross; 141M shares, $19.9B net | | | VERIFIED 10-Q Note 7 |
| FY26 total senior notes | $43.0B (so about $18B was Sept 2025) | | | Sept 2025 deal: press says $18B, peak demand near $88B (treasuryandrisk, secondary) | 10-K VERIFIED for $43.0B |

Package: $25B notes + $5B convertible preferred + $20B ATM = $50B plan announced 2026-02-01/02 (press: "$45-50B"). Management said on the June Q4 call it plans to raise about $40B more in debt and equity in FY27 including the $20B ATM (Reuters-based press; call transcript not read). 10-Q release of 2026-09-10: "no incremental impact on its plans to raise capital" from the $30B of new contracts (VERIFIED, https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm).

### Bank facilities and project/structured financing
| Item | Detail | Status |
|---|---|---|
| Oracle revolver / CP / term loan | above | VERIFIED |
| Lease with Oracle guarantee | 10-K: Oracle "guaranteed up to $3.3 billion of the lessor's borrowing, which matures in September 2026" (part of the $260B lease commitments) | VERIFIED (10-K note); outcome at maturity not found, UNKNOWN |
| Project Jupiter, Dona Ana County NM (Oracle tenant, OpenAI end user) | About $18B bank loans, syndicate incl. Santander and Jefferies, raised late 2025; quoted 89-91 cents (FT/Reuters 2026-09-18); sell-down to investors stalled; Oracle sent a force-majeure notice to the Blue Owl unit developing it (Bloomberg, 2026-09-24) citing power delay, reportedly to be protected from payment obligations if the planned 2028 start slips | Press only. https://financefeeds.com/oracle-debt-project-jupiter-loans-90-cents-bonds-85/ ; https://www.investing.com/news/stock-market-news/softbank-shares-fall-as-oracle-datacenter-warning-fuels-ai-funding-fears-4916560 |
| Saline Township, Michigan (Related Digital; Oracle/OpenAI) | Press: about $14B of bonds sold via Bank of America, PIMCO anchored (about $10B); total $16.3B; ceremonial groundbreaking 2026-06-01. Reuters-based Aug piece links the $14B to the rating ("RD Michigan Property Owner") | Press only (Bloomberg 2026-04-25 headline; thenextweb). Amounts differ by source. |
| Port Washington WI (Vantage) | Oracle >$7B letter-of-credit demanded by We Energies after the 7/9 S&P cut | Fleet record SIG-W-20260723-009; not independently re-read |
| Abilene TX | Flagship Stargate site, Crusoe-built, Oracle-leased. 2026 financing details not found | SEARCH-NOT-FOUND for 2026 specifics |
| Vantage (Ares) | $2.4B Ares loan to Vantage, 2026-02-10, part may fund Oracle/OpenAI sites | Press headline only |

### Off-balance-sheet commitments (10-Q Note 6, VERIFIED)
| Item | Amount | Detail |
|---|---|---|
| Additional lease commitments not on balance sheet | **$288B** at 2026-08-31 (was $260B at 2026-05-31; CNBC cited $248B at 2025-11-30, secondary) | "substantially all related to data center arrangements", commence Q2 FY27 to FY2029, terms 15-19 years |
| Unconditional purchase obligations (terms of 1 year or more) | **$34,150M**: FY27 remainder $5,449M; FY28 $6,176M; FY29 $3,863M; FY30 $4,318M; FY31 $6,768M; FY32 $954M; thereafter $6,622M | Now "primarily long-term supply arrangements for purchasing components for cloud infrastructure assets and power supply arrangements for data centers". The 10-K showed a smaller power-focused table (FY27 $1,841M etc.; S&P cites $13B) plus a note of an additional $19B of 5-year purchase commitments entered after 5/31/26. |
| Signed leases by maturity | Operating $48,050M payments / finance $15,195M payments (before imputed interest of $13,429M / $6,010M) | |

## 2. Capex, free cash flow, RPO, customers
| Metric | Figure | Source/token |
|---|---|---|
| FY26 capex / operating cash flow / FCF | $55,663M / $31,977M / -$23,686M | 10-K VERIFIED |
| Q1 FY27 capex / OCF / FCF | $28,499M / $23,103M / -$5,396M (Q1 FY26: -$362M) | 10-Q VERIFIED |
| Last four quarters FCF (FY26 less Q1 FY26 plus Q1 FY27) | **-$28.7B** (derived: -23,686 + 362 - 5,396) | INFERRED arithmetic from VERIFIED inputs |
| Q1 FY27 OCF includes | $11.4B customer prepayments with significant financing component (none in Q1 FY26) | 10-Q VERIFIED. OCF quality: without prepayments Q1 OCF is about $11.7B (derived) |
| FY27 capex guidance | 10-Q says only "higher than fiscal 2026". Press: up to $90-95B gross; Oracle says net own cash outlay about $70B after $20-25B customer repayments (CFO Hilary Maxson, June call) | INFERRED: S&P cites $90-95B and about $70B net (https://ppc.land/s-p-cuts-oracle-to-bbb-as-ai-buildout-widens-cash-deficit-to-42bn/); Reuters-based https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity. Not read at call transcript. The two numbers are gross vs net framings, not a conflict. |
| S&P FY27 free operating cash flow forecast | about -$42B (prior -$24B) | S&P via ppc.land, INFERRED |
| RPO | $664B at 2026-08-31 (was $638B at 5/31/26; $455B at 8/31/25; $138B at 5/31/25). More than $30B of AI contracts booked in Q1. About 13% recognized in next 12 months, 37% months 13-36, 34% months 37-60, remainder after | 10-Q VERIFIED |
| FY27 revenue guide | at least $90B; non-GAAP EPS $8.10 (2026-09-10 release) | VERIFIED |
| Q1 FY27 | revenue $19.3B (+30%), cloud infrastructure $7.4B (+121%), 850MW capacity delivered | VERIFIED |
| OpenAI contract | $300B, five years (WSJ-reported, 2025). S&P (7/9/26): OpenAI "roughly half" of the $638B RPO; Yonhap preview "nearly half". Oracle's 10-K/10-Q do not name OpenAI or disclose a customer split (grep of 10-K and 10-Q: no "OpenAI" hit). | Share INFERRED; non-disclosure VERIFIED |
| Customer concentration | None disclosed by name. S&P's stated key risk: 15-19 year data center leases vs customer contracts of up to five years | Press (Reuters Aug 5 analysis, https://www.thestar.com.my/tech/tech-news/2026/08/05/analysis-oracle-corp-goes-for-high-stakes-ratings-gamble-in-ai-strategy) |

Observation: the RPO delivery profile (13% within 12 months, 71% within 5 years) against funded debt, $288B of lease commitments starting by FY2029 and $34B purchase obligations is the maturity mismatch S&P flags.

## 3. Rating actions 2026
| Agency | Rating / outlook | Date | Detail | Token |
|---|---|---|---|---|
| S&P | BBB- (from BBB), stable; short-term A-3 (from A-2) | 2026-07-09 | Downgrade triggers: leverage sustained above 4.5x; not on path to positive FOCF by FY2029; negative view of AI strategy/industry. Forecasts adjusted leverage "mid-4x" FY27. Adds the $260B leases to debt. OpenAI named as key credit risk. Upgrade unlikely for 2 years. S&P says "firmly committed" to investment grade. | INFERRED (ppc.land and Reuters summaries; S&P release itself not read). Date also in fleet record SIG-W-20260717-010 |
| Moody's | Baa2, negative outlook | affirmed 2026-02-02 (Newsquawk headline); Feb note: leverage "could approach 5x temporarily" | No 2026 downgrade found. Whether Moody's acted after 7/9: SEARCH-NOT-FOUND | INFERRED |
| Fitch | BBB | February 2026 note: sustained EBITDA leverage above 3.5x (4.0x incl. rents) triggers negative action | Outlook and any later action: SEARCH-NOT-FOUND | INFERRED |

Fallen-angel language (press): Morgan Stanley's Lindsay Tyler, "two low BBB ratings for Oracle, maybe even by calendar year-end"; she called junk a medium-term risk (Reuters via thestar.com.my 2026-08-05). No agency "watch negative" or "review for downgrade" statement found. A split would be: S&P BBB- (lowest IG rung), Moody's Baa2 and Fitch BBB two notches above junk. Index treatment needs two of three agencies below IG, so a single further S&P cut would not itself make Oracle high yield (INFERRED from standard index rules, not checked against ICE/Bloomberg rulebooks).

## 4. ORCL 5-year CDS
| Date | Level (bp) | Source | Token |
|---|---|---|---|
| start of 2026 | 144 | Bloomberg per press (BigGo, others) | INFERRED |
| 2026-07-17 | 198.23 (record close then, above 2008 peak) | startupfortune / seekingalpha headline | INFERRED |
| 2026-07-24 | 203 | press | INFERRED |
| about early Aug (Reuters 8/5) | 215, "18-year high"; peers about 80 | https://www.thestar.com.my/... | INFERRED |
| 2026-09-24 | about 221.78 (single source, in fleet SIG-W-20260925-007) | fleet | INFERRED |
| 2026-10-08 | 261 (Bloomberg per Gate) | press | INFERRED |
| 2026-10-15 | 288 close, record, up from 260 a week earlier (S&P Global MI / LSEG) | https://www.securitasglobal.com/risk-perspectives/oracle-cds-record-288-basis-points-ai-debt/ | INFERRED |
| about 2026-10-16 to 10-19 | 295, touched 300 (CNBC 10/19; page returned 403, read via search summary only) | | INFERRED |
| 2026-10-21 | **315-320 disseminated on DTCC public tape** (fleet LIQUID packet L782, `dtcc_cds_probe.py`) | AGENTS/LIQUID/MEMORY.md line 11 | fleet record, not re-run by me |
| (a Monday, probably 10/19) | 322 (BigGo, unverified) | | UNKNOWN |

Cohort comparison (FRED, ICE BofA indices, option-adjusted spread, different instrument from CDS, read via fred.stlouisfed.org/graph/fredgraph.csv 2026-10-22):
| Date | BBB OAS | Broad IG OAS | HY OAS |
|---|---|---|---|
| 2025-12-31 | 101bp | 79bp | 281bp |
| 2026-07-09 | 94bp | 76bp | 270bp |
| 2026-10-15 | 105bp | 84bp | 323bp |
| 2026-10-21 | 109bp | 88bp | 327bp |
At roughly 315-320bp, Oracle CDS is about 3x the BBB index OAS and in HY-OAS territory (327bp), VERIFIED arithmetic on a mixed-instrument comparison. No BBB- cohort CDS series found (SEARCH-NOT-FOUND). Peer hyperscaler CDS: Meta 105-111bp (DTCC 10/19-10/21, fleet); Nvidia record about 82bp 7/27 (fleet). Oracle bond price: senior notes at 84.6 cents on the dollar at 8/31 (10-Q); press says yields about 7-8% (Reuters 8/5).

## 5. The SoftBank claim
**Finding: SEARCH-NOT-FOUND for any 2026 transaction in which SoftBank invests in Oracle (equity, bonds, convertible, or data-center financing).**

What was searched:
- WebSearch (5 queries, 4 of them extended mode): "SoftBank Oracle investment October 2026"; "SoftBank Oracle stake OR financing OR invest in Oracle Son Ellison data center 2026"; SoftBank + Oracle + invests billion bond/shares/convertible/equity; "SoftBank to invest in Oracle data centers / Oracle stake / rescue / backstop / lifeline October 2026"; plus Michigan/Stargate financing. Nothing reported a SoftBank purchase of Oracle securities or lending to Oracle.
- SEC EDGAR full-text search, Oracle filings Jan to Oct 2026 for "SoftBank": 2 hits (10-Q filed 2026-03-11, 10-K filed 2026-06-22); the 10-K hit is the Ampere sale; the 10-Q (Mar) hit not read, likely same (INFERRED). Zero hits in the 10-Q filed 2026-09-11 and the 2026-09-25 proxy statement (VERIFIED by grep of the downloaded text). EDGAR full-text search for "SoftBank" in 8-K/13D/13G filings 2026-10-01 to 10-22 returned 3 unrelated filers (Ethos, Churchill Capital XI, Hawkeye); the form filter may not have applied, so treat as weak negative.
- Oracle 8-Ks 2026 (index through 2026-09-14): no SoftBank item. Ellison's 8-K of 2026-09-12 is about cancelling a stock-sale plan.

What does exist, separately (do not merge):
| # | Item | Date | Direction of money | Source | Token |
|---|---|---|---|---|---|
| 1 | Stargate JV announced: OpenAI, SoftBank, Oracle, MGX as initial equity funders; $100B immediately, up to $500B over four years; SoftBank financial responsibility, OpenAI operational. Oracle is a technology partner and equity investor in the JV. | 2025-01-21 | SoftBank and Oracle both fund the JV; nothing flows into Oracle Corp as such | https://techcrunch.com/2025/01/21/openai-teams-up-with-softbank-and-oracle-on-50b-data-center-project/ (secondary) | INFERRED. Not re-read at a primary. |
| 2 | Five new Stargate sites with Oracle and SoftBank | 2025-09 | site announcement | https://openai.com/index/five-new-stargate-sites/ | search listing only, not read |
| 3 | SoftBank Group acquires Ampere; Oracle receives $4.3B cash for its equity, debt and call option interests, books $2.7B realized gain | closed 2025-11-25 (10-K FY26) | SoftBank pays Oracle | 10-K FY26 Note (Ampere) | **VERIFIED** |
| 4 | SoftBank Corp and Oracle Japan sovereign cloud (Tokyo, east site April 2026, west site October 2026) | announced 2025-10 | commercial partnership | https://www.sdxcentral.com/news/softbank-and-oracle-team-up-on-sovereign-cloud-in-japan/ | INFERRED |
| 5 | SoftBank funds OpenAI ($41B completed December 2025, about 11% stake; further $30B March 2026 per one source); SoftBank sold $11.1B high-yield bonds in Sept 2026 to fund OpenAI stake | 2025-12 to 2026-09 | into OpenAI, which is Oracle's largest customer | CNBC via itiger; Investing.com 2026-09-24 | INFERRED. This is the closest economic link: SoftBank money reaches Oracle only as OpenAI's cash to pay Oracle. |
| 6 | Oracle force-majeure notice on Project Jupiter (a Stargate site); SoftBank shares fell 3.1% | 2026-09-24/25 | | Bloomberg via Investing.com | INFERRED |
| 7 | SoftBank shares down about 26% 10/08 to 10/22 (fleet SIG-W-20261021-018); SoftBank 5Y CDS 424bp (undated Securitas piece); Invezz 10/22: SoftBank lowest since April | Oct 2026 | | fleet; https://invezz.com/news/2026/10/22/softbank-stock-is-in-a-deep-sell-off-as-ai-bubble-index-jumps-to-74/ | INFERRED |

Reading: the phrase most likely compresses (1) Stargate (SoftBank money into the JV that Oracle builds for), (5) SoftBank's OpenAI funding that underwrites Oracle's largest contract, and/or (3) a SoftBank-to-Oracle cash payment for Ampere. Whichever Will saw, UNKNOWN which; the original post/screenshot was not available to me. If the item was a post dated after 10/21 it may postdate everything I could search. Direction of dependency in the data is the reverse of "SoftBank props up Oracle": SoftBank is itself a stressed, levered node (shares down about half from June peak, 424bp CDS per one press piece) whose funding of OpenAI is what Oracle's RPO depends on.

## 6. Oracle equity (for reader D)
Price from fetch.py (FORGE/tools/market-data, Yahoo feed) 2026-10-22: **$125.54, -2.78% on the day**, volume 36.6M (as-of 2026-10-22; session close vs intraday not distinguished by the tool, ran 20:38 ET).

| Reference | Level | Date | Move to $125.54 |
|---|---|---|---|
| All-time high (intraday) | $345.72 | 2025-09-10 | -63.7% |
| 52-week high (intraday) | $287.19 | 2025-10-24 | -56.3% |
| 52-week low (intraday) | $114.50 | 2026-07-28 | +9.6% above |
| 2025-12-31 close | $194.91 | | **YTD -35.6%** |
| Close on S&P cut day | $144.22 | 2026-07-09 | |
| Close day after Q1 release | $150.28 | 2026-09-11 | |
| Prior close | $129.13 | 2026-10-21 | |
Price series: Yahoo chart API (secondary). Ratios derived.

Ellison (2026 proxy DEF 14A filed 2026-09-25, record date 2026-09-21; https://www.sec.gov/Archives/edgar/data/1341439/000119312526402816/orcl-20260925.htm; VERIFIED):
| Item | Figure |
|---|---|
| Beneficial ownership | 1,158,375,174 shares = **38.2%** of class (includes 142,821 exercisable options and the pledged shares) |
| Pledged as collateral for personal indebtedness (incl. various lines of credit) | **413,000,000 shares** as of 2026-09-21 = about 35.7% of his holdings, about 13.6% of all shares (derived; implied shares outstanding about 3.03B) |
| Value of pledged block at $125.54 | about $51.8B (derived) |
| Pledging terms | Board Governance Committee: no margin accounts, Ellison "has the financial capacity to repay the related personal term loans without resorting to the sale or transfer of pledged shares" (company assertion, not an independent test) |
| Pledge trend | Press: 346M a year earlier (Yahoo/proxy summary); not re-verified against the 2025 proxy |
| Stock-sale plan | 10-Q (filed 2026-09-11) disclosed a 10b5-1 plan adopted 2026-06-22 to sell up to 50M shares, ending 2026-10-24. **Oracle 8-K of 2026-09-12 (ex 99.1): Ellison cancelled the plan, no shares were sold under it, and he "has no other plans to sell any of his Oracle stock."** VERIFIED: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389753/d20034dex991.htm |
| Press link of the pledges to son David's Warner Bros bid; also pledged Tesla/SpaceX stock | 2026-10-21 press (Yahoo, 24/7 Wall St); Oracle's filing does not name Warner Bros | secondary, not read |

## 7. Load-bearing uncertainties and gaps
1. SoftBank claim source unidentified (no screenshot). Negative finding is broad but not exhaustive; a post-10/21 item or a non-English item could have been missed.
2. S&P, Moody's and Fitch press releases not read; ratings are from Reuters/Bloomberg-derived summaries. Moody's and Fitch actions after 7/9 and Fitch outlook are SEARCH-NOT-FOUND.
3. CDS levels above 300bp rest on fleet DTCC (315-320, 10/21) and one unverified press figure (322); CNBC and Bloomberg pages were paywalled or returned 403. Press CDS (LSEG/S&P MI) and DTCC tape are different series and not reconciled.
4. FY27 capex: 10-Q gives no number; $90-95B gross and about $70B net rest on press accounts of the June call. Call transcript not read (Quartr tool not used).
5. Project-level financing (Jupiter, Michigan, Abilene, Port Washington) is press-only; Oracle's exposure is through lease commitments (VERIFIED $288B) and any guarantees (one $3.3B guarantee noted in 10-K, outcome at its September 2026 maturity not found).
6. Unreconciled: 10-Q "$8.1B scheduled repayments" vs $3.1B cash repayment line.
