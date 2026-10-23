# D — The Ellison family balance sheet as a transmission node

Reader D (read-only). Compiled 2026-10-22 20:45 ET (`date` run in-session). WebSearch calls used: 21 of 25. Not committed.
Confidence tokens: VERIFIED (checked at primary artifact) / INFERRED / SEARCH-NOT-FOUND / UNKNOWN. "Filed" = on EDGAR; "reported" = press (secondary), always labelled.
Price basis: ORCL close **$125.54 on 2026-10-22** (`FORGE/tools/market-data/fetch.py`, -2.78% on day, vol 36.6M). 2026 high = **$248.15 close / $250.25 intraday on 2026-06-01** (Yahoo daily chart, single vendor; VERIFIED vs. vendor only, not cross-checked at a second source). ORCL all-time close high in window: $328.33 on 2025-09-10.

## 0. Hypothesis scorecard (Will's hypothesis, tested not confirmed)

| Link | Verdict | Basis |
|---|---|---|
| A. ORCL drawdown shrinks collateral behind Larry's personal borrowing | **SUPPORTED on collateral value, UNKNOWN on stress** | Pledged value fell by roughly half while pledged shares rose (sec. 2). Loan sizes, LTV, triggers are not public. No margin call / forced sale found. Oracle says none of the shares sit in margin accounts. |
| B. That borrowing funds David's media roll-up | **PARTLY. Direction plausible, link is press-inferred** | Proxy says pledged shares secure "personal term loans only used to fund outside personal business ventures"; it does not name Paramount/WBD. WSJ (secondary) ties 2026 borrowing to the WBD deal. The filed equity obligor is the Larry Ellison Revocable Trust (sec. 3). |
| C. The family's cash need is large | **WEAKER THAN FRAMED** | Trust commitment was up to $46.72B and personally guaranteed ($45.72B equity piece), but it was syndicated before closing; Ellison-family actual cheque reported ~ $17B (Bloomberg est., secondary). |
| D. Outside money stepped in where capacity was stretched | **Outside money: VERIFIED. "Because stretched": INFERRED only** | Gulf funds + LionTree took the syndicated shares (filed). Company's stated rationale is shareholder-base diversification and warrants. Musk ~$1B (Semafor 10/22, single source, structure unknown). |

Timing fact that cuts both ways: the syndication was announced 2026-04-07, when ORCL was $143.17 (collateral value of his stake ~ $166B, already -34% from the $217.58 close of 2025-12-05 when the "$252B" resources claim was made). It preceded the 6/1 high ($248). So the syndication was NOT a reaction to the June-October slide; it followed the Dec-Feb slide. Whether capacity worries drove it is not documented.

## 1. Larry Ellison's Oracle stake

| Item | Figure | Date / source | Token |
|---|---|---|---|
| Beneficial shares | 1,158,375,174 (38.2% of class) | Record date 2026-09-21; DEF 14A filed 2026-09-25, https://www.sec.gov/Archives/edgar/data/1341439/000119312626402816/orcl-20260925.htm | VERIFIED |
| Of which options exercisable <=60d | 142,821 | same | VERIFIED |
| Shares outstanding | 3,031,501,149 | same | VERIFIED |
| Prior-year beneficial | 1,158,232,353 (40.6%) | DEF 14A filed 2025-09-26, https://www.sec.gov/Archives/edgar/data/1341439/000119312525220801/d72066ddef14a.htm | VERIFIED |
| Value @ today $125.54 | **$145.4B** | 1,158,375,174 x 125.54 | computed |
| Value @ 2026 high close $248.15 | **$287.5B** | same x 248.15 | computed |
| Value @ 9/25/26 close $137.10 | $158.8B | | computed |
| Annual dividend (not net of tax) | ~ $579M per quarter, ~ $2.32B/yr at $0.50/qtr | Oracle 10-Q (Aug-31 qtr, filed 2026-09-11) declared $0.50 payable 2026-10-23 | VERIFIED (rate); count x rate computed |
| Net worth aggregators (Oct 2026) | Bloomberg $178B, #8 as of 10/16 (Nairametrics); Dave Manuel tracker $165.7B | https://nairametrics.com/2026/10/19/billionaire-larry-ellison-loses-194-billion-in-one-year-as-oracle-stocks-fall/ | secondary; the two disagree by $12B and Nairametrics' own Oracle component ($122B) does not match 1.158B x $128.23 = $148.5B. Do not cite either as reconciled. |

Open-market selling: EDGAR submissions for Ellison (CIK 901999) list only 5 Form 4s since 2025-06-01: option exercises 2025-06/07 (5M, 2.5M, 2.5M, 1M, 1.5M, 5M at $51.13, all code M, no sales), a 571,286-option grant 2025-10-23 at $280.07 strike, and a 223,099-RSU grant 2026-10-15. No Form 4 sale, no Form 144 under his CIK. Beneficial count rose only by 142,821 options year over year. VERIFIED (https://data.sec.gov/submissions/CIK0000901999.json, pulled 2026-10-22). Pledge changes are not Form 4 reportable; they surface only in the proxy.

Planned sale: Oracle 10-Q (filed 2026-09-11) Item 5: Ellison adopted a Rule 10b5-1 plan on **2026-06-22** to sell up to **50,000,000** shares, scheduled to end 2026-10-24. Oracle 8-K filed 2026-09-14 (Ex. 99.1 dated 2026-09-12): plan cancelled, "No Oracle stock was sold under that plan, and he has no other plans to sell any of his Oracle stock." 50M shares ~ $7.5B at the 9/11 close $150.28; ~ $8.75B at the 6/22 close $175.07. Sources: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm ; https://www.sec.gov/Archives/edgar/data/1341439/000119312526389753/d20034d8k.htm . VERIFIED. Reason for the cancellation: UNKNOWN (Oracle gave none; "to fund the WBD bid" is press inference, NLPC/WSJ).

## 2. Pledged shares

Exact proxy language (2026): "Includes 142,821 shares subject to stock options exercisable within 60 days of the record date and **413,000,000 shares pledged as collateral to secure certain personal indebtedness, including various lines of credit**." Governance section: "As of September 21, 2026, Mr. Ellison ... had pledged 413 million shares ... The pledged shares secure personal term loans only used to fund outside personal business ventures. None of Mr. Ellison's shares are pledged as collateral for margin accounts. The pledged shares are not used to shift or hedge any economic risk ... The Board believes that Mr. Ellison has the financial capacity to repay his personal term loans without resorting to the pledged shares." No other officer/director pledges. Governance Committee reviews every fiscal quarter. VERIFIED.

### 2a. Proxy time series (all VERIFIED from each DEF 14A, EDGAR accession folders under /Archives/edgar/data/1341439/)

| Proxy filed | As-of date | Pledged shares | Beneficial shares (% class) |
|---|---|---|---|
| 2016-09-23 | 2016-09-19 | 315,000,000 | n/p |
| 2017-09-28 | 2017-09-18 | 260,000,000 | n/p |
| 2018-09-26 | 2018-09-17 | 305,000,000 | n/p |
| 2019-09-27 | 2019-09-20 | 305,000,000 | n/p |
| 2020-09-18 | 2020-09-08 | 317,000,000 | n/p |
| 2021-09-24 | 2021-09-13 | 317,000,000 | n/p |
| 2022-09-23 | 2022-09-19 | 307,000,000 | 1,157,482,353 (42.9%) |
| 2023-09-22 | 2023-09-18 | 307,000,000 | 1,152,982,353 (42.1%) |
| 2024-09-25 | 2024-09-16 | 277,000,000 | 1,153,232,353 (41.6%) |
| **2025-09-26** | **2025-09-19** | **346,000,000** | 1,158,232,353 (40.6%) |
| **2026-09-25** | **2026-09-21** | **413,000,000** | 1,158,375,174 (38.2%) |

(n/p = not extracted.) Year-over-year: +67M shares (+19.4%) 2025 to 2026; +69M (+24.9%) 2024 to 2025; 2024 was the series low since 2017. Pledged = 35.7% of his holdings and 13.6% of shares outstanding (2026).

### 2b. Pledged value (computed; shares x price)

| Basis | ORCL px | 413M pledged | 346M pledged |
|---|---|---|---|
| 2026 high close (2026-06-01) | $248.15 | **$102.5B** (intraday high $250.25: $103.4B) | |
| 2026-09-21 record date | $148.56 | $61.4B | |
| 2026-09-25 (press date) | $137.10 | $56.6B | |
| 2026-10-16 | $128.23 | $53.0B | |
| **Today 2026-10-22** | **$125.54** | **$51.9B** | $43.4B |
| 2025-09-19 (prior record date) | $308.66 | | **$106.8B** |
| Series peak close 2025-09-10 | $328.33 | $135.6B | |

Read: pledged share count rose 19% (346M to 413M) while ORCL fell; the pledged package was worth $106.8B on 2025-09-19 and is worth $51.9B today (-51%, different share counts), and the same 346M shares would be $43.4B (-59%). Price is -49.4% vs the 2026 high close. Price now is also -61.8% vs the 2025 peak close and -8.4% vs the 9/25 price. INFERRED: the +67M increase while price fell is consistent with topping up collateral or adding new loans; the filings do not say which.

Loan size / LTV / maintenance triggers / lenders' margin terms: **UNKNOWN**. Oracle states it does not disclose; the 2026 proxy gives no dollar debt. Illustration only (not data): a loan sized at 25% of pledged value at the 6/1 high would be ~ 49% of pledged value now; to keep a 50% LTV ceiling the price floor scales with loan size, which no document gives.

### 2c. Lender liens (reported, secondary; originating outlet WSJ 2026-10-20, paywalled, not read by me)

Press (Billionaires.Africa 10/21, NLPC, 24/7 Wall St 10/21, Quartz) attribute to WSJ, citing California lender filings (UCC): Citigroup, HSBC, JPMorgan, UBS, BNP Paribas hold security interests in **87M Oracle shares, up from ~30M a year earlier**; on or about 2026-09-25 / 2026-10-01 JPMorgan and Citigroup added SpaceX and Paramount Skydance stock (first-time pledges, days before the 10/6 close); Citigroup Tesla collateral reportedly cut to 1.5M shares from 3M (unit pre/post split unknown); "the filings do not show how much he borrowed." The 87M is a subset measure (lien filings) and must not be added to 413M. Token: INFERRED/reported, not verified at the lien filings. URLs: https://www.billionaires.africa/2026/10/21/american-billionaire-larry-ellison-pledges-tesla-spacex-stock-for-sons-110bn-warner-deal/ ; https://nlpc.org/corporate-integrity-project/ellisons-borrowing-spree-shows-why-oracle-shareholders-need-nlpcs-proposal/ ; https://247wallst.com/investing/2026/10/21/larry-ellison-borrowed-against-his-tesla-and-spacex-stock-to-fund-his-sons-warner-bros-deal/ . I could not retrieve the California filings or the WSJ text.

### 2d. Pledging policy and board exceptions

- Policy on Pledging Oracle Securities (in the 2024, 2025, 2026 proxies, identical text): bars directors, executive officers and immediate family from margin accounts and from pledging Oracle securities to secure indebtedness, with two exceptions: (i) target-company pledges in place when Oracle acquires the target; (ii) "Mr. Ellison may continue to pledge Oracle securities as collateral to secure or guarantee indebtedness, but he may not hold Oracle securities in a margin account." Pledges must be pre-cleared under the Insider Trading Policy. VERIFIED (2026 proxy pp. 28-29).
- The 2016 proxy already describes "Regular Board and committee oversight of share pledging by Mr. Ellison" and quarterly Governance + Compensation Committee review with factors including loan terms, pledged share count vs. outstanding and vs. his holdings, market value, and "independent ability to repay ... without recourse to the already-pledged shares." VERIFIED (2016 DEF 14A). The date the Ellison exception was first adopted: SEARCH-NOT-FOUND (earliest proxy I pulled is 2016). Forbes (secondary, 2025-07-30) says pledging for lines of credit reportedly began around 2008: https://www.forbes.com.au/news/billionaires/how-larry-ellison-and-his-son-pulled-off-8-billion-paramount-deal/ .
- Wording drift: "including various lines of credit" appears in the beneficial-ownership footnote every year; the governance bullets ("term loans only used to fund outside personal business ventures") are unchanged 2024-2026. The multiple of required ownership rose from 4,500x (2024) / 4,600x (2025) to 15,000x (2026), reflecting the stock-ownership requirement being re-set, not a holdings change.

## 3. How the family funded Skydance, then Paramount, then WBD

### 3a. Skydance-Paramount (closed 2025-08-07)

| Item | Fact | Source | Token |
|---|---|---|---|
| Who bought NAI (Redstone's controlling vehicle) | "entities controlled by the Ellison Family, and affiliates of RedBird Capital Partners" (the NAI Equity Investors) | Skydance Corp 10-K FY2025 filed 2026-02-25, https://www.sec.gov/Archives/edgar/data/2041610/000204161026000011/psky-20251231.htm | VERIFIED |
| Control after | Harbor Lights (ex-NAI) holds 100% of Class A; Ellison Family entities indirectly ~ 77.5% of Class A | same | VERIFIED |
| Dollar split of the ~$8B | Ellison family ~ $6B, RedBird ~ $2B; $2.4B NAI purchase, $4.5B to public holders, $1.5B balance sheet | TheWrap via ottverse, https://ottverse.com/oracle-founder-larry-ellison-invests-in-sons-paramount-buyout-with-6-billion/ ; announcement-level sources give no split | secondary, UNVERIFIED at a filing |
| Signatory/obligor for Larry's money | Not given in the 10-K; pre-merger FCC filings (Forbes AU) say Larry held all voting and equity in the Pinnacle Media Ventures entities that bought the stake; Oct 2024 amendment moved 100% of Pinnacle voting to David, Larry kept the equity | Forbes AU 2025-07-30 | secondary |

### 3b. WBD (merger agreement 2026-02-27; closed 2026-10-06)

Filed facts (Skydance Corp 8-Ks; URLs under https://www.sec.gov/Archives/edgar/data/2041610/):
- **Guarantee.** 8-K 2026-03-02 (0001104659-26-021911): The Lawrence J. Ellison Revocable Trust u/a/d 1/22/88 and Mr. Lawrence J. Ellison ("Ellison Parties") gave WBD a joint and several Guarantee covering the Netflix termination fee, the "Amended Notes Payment Amount", **$45,720,000,000 of the Merger Consideration (equity funding) plus any Contingent Equity Amount**, damages for breach/fraud, the Regulatory Termination Fee and other costs. Carve-out: Oracle Corporation, Ellison Institute of Technology and their controlled affiliates are excluded from what Ellison must cause. VERIFIED. (Earlier December 2025 version: $40.4B personal guarantee, widely reported; tender-offer papers 2025-12-22 stated the Trust "has financial resources well in excess of ... its commitments ... including ... approximately 1.16 billion shares of Oracle stock with a market value of approximately $252 billion" and cited Form 144 filings and the Twitter take-private as track record. VERIFIED, SC TO-T/A 0001104659-25-123493. That $252B equals the 2025-12-05 close $217.58 x 1.16B; at $125.54 the same stake is $145B.)
- **Subscription agreements.** 8-K 2026-04-07 (0001104659-26-040178): concurrently with the merger agreement the Trust and RedBird Capital Partners Fund IV (Master) signed subscription agreements for Class B at $16.02: up to **$46,720,000,000 from the Trust** (the "Ellison Commitment", plus ticking fee/contingent amounts) and **$250,000,000 from RedBird**. VERIFIED. Negotiated for PSKY by a special committee.
- **Syndication.** Same 8-K: the Equity Investors assigned their subscription rights to "affiliates of the Ellison Parties and RedBird as well as ... The Public Investment Fund, L'Imad 1st SPV 2 Exempt RSC LTD (Abu Dhabi), QIA TMT Holding LLC (Qatar Investment Authority), and LionTree Investment Fund, L.P."; "aggregate allocations ... total to the full amount of the Commitments"; syndicate shares are non-voting; Ellison family + RedBird remain sole owners of Class A (100% of votes). Price = 20-day VWAP floored at $12.00 / capped at $16.02; every public Class B holder gets one 10-year warrant per share (exercise = syndication price). Crucially: "The Ellison Guarantee and the Subscription Agreements remain in full force ... The Syndication Assignments do not relieve the Equity Investors of their obligations ... To the extent that any Equity Syndication Party does not perform ..., the obligation of the Equity Investors to fund ... would continue." VERIFIED. So a bank/WBD could always look through to the Trust until funding; after funding the contingent exposure falls away (INFERRED: funding completed 10/6, see next).
- **Close.** 8-K 2026-10-06 (0001104659-26-113913): merger closed 2026-10-06 at $31.00 + ticking fee per WBD share; PIPE investors subscribed 10/6 for **3,917,657,246 Class B shares at $12.00 = $47.01B**; ticker changed PSKY to SKYD, company renamed Skydance Corp. The 8-K does not split the $47.01B by investor. VERIFIED.
- **Debt.** Same 8-K: $30.0B first-lien and $11.4B + EUR 885M second-lien senior secured notes issued 2026-10-05 (coupons 6.30% to 8.90% first lien, 8.25% to 9.125% second lien; 8.750%/8.900% 2056/2066 tranches); plus credit facilities. 8-K 2026-04-09: commitment letter 2025-12-08 of $54.0B bridge + $3.5B revolver (BofA, Citi, Apollo) reduced to $49.0B bridge; pro-rata facilities $2.5B + $2.5B Term A and $5.0B revolver (Citi agent; BofA, Apollo, Deutsche, Wells). TheWrap (secondary, 2026-10-02): ~ $52B debt sold in a week ($30B IG, $12.4B HY, $9.46B loans), pro forma ~ $80B net debt. Debt is at the Skydance/PSKY level, secured on the company; the filings I read do not show lender reliance on Larry's personal balance sheet beyond the equity guarantee. SEARCH-NOT-FOUND for any bank guarantee by Larry of the company debt.
- **Who supplied the $47.01B (reported, not filed):** Bloomberg estimate (via 24/7 Wall St and Billionaires.Africa 10/21): Ellison family ~ **$17B for ~ 1.4B shares** (1.4B x $12 = $16.8B), RedBird ~ $4B, three Gulf sovereign funds ~ $24B (PIF ~ $10B, QIA ~ $7B, L'imad ~ $7B per WSJ April and Bloomberg Gov); FCC-filing post-close shares: PIF 15.1%, L'imad 12.8%, QIA 10.6% = 38.5% (Variety/AGBI, read only via search summary; page fetch blocked). Remainder implied ~ $2B (LionTree / others) INFERRED. Token for the $17B: secondary, single origin, UNVERIFIED at a filing.
- Mark-to-market: SKYD ~ $7.79 today (fetch.py, 2026-10-22; prior close $7.87 on 10/21; low $6.80 on 10/19) vs $12.00 PIPE price. If the family holds 1.4B shares the stake is ~ $10.9B vs ~ $16.8B cost (-$5.9B), INFERRED from the reported count. Yahoo daily chart shows SKYD falling from $9.27 (10/13) to $7.06 (10/14), -23.8% in one day; cause not established by me.

### 3c. Net reading of the funding path

| Layer | Documented | Inferred |
|---|---|---|
| Legal obligor for equity | Trust + Larry personally (guarantee), RedBird $250M | |
| Cash actually from the family | no filed number | ~ $17B (Bloomberg est.) |
| Source of that cash | proxy: pledged-share loans "for outside personal business ventures"; WSJ: borrowing from Citi, HSBC, JPM, UBS, BNP, new pledges of SpaceX and SKYD stock | Loans on ORCL (and Tesla/SpaceX) collateral are the likely source. Not stated in any filing I read. |
| Outside equity | Gulf SWFs + LionTree via filed assignment; Musk ~ $1B (Semafor, single source) | |
| Debt | Company-level secured notes/loans | |

## 4. Other Ellison commitments

| Item | Facts | Source | Token |
|---|---|---|---|
| Ellison Institute of Technology (Oxford) | Original plan GBP 10B/decade; Cherwell (Nov 2025) says scaled back, ~ GBP 2B committed, projects narrowed; Times Higher Ed (Oct 2025): additional GBP 890M on top of the initial GBP 1B; EIT continued activity in 2026 (April 2026 scholar cohort; May 2026 construction milestone). EIT is carved out of the WBD guarantee covenants. No 2026 funding-total announcement found. | https://cherwell.org/2025/11/29/larry-ellison-scales-back-10-billion-oxford-science-initiative/ ; https://www.timeshighereducation.com/node/739477 ; https://eit.org/news | secondary; 2026 revision SEARCH-NOT-FOUND |
| Philanthropy | Giving Pledge 2010: at least 95% of wealth; ~ $1B total to Ellison Medical Foundation (closed); $200M USC cancer center (Fortune 2025-09-23). Annual charitable cash flows 2026: UNKNOWN. | https://fortune.com/2025/09/23/oracle-founder-larry-ellison-has-pledged-to-give-away-95-of-his-393b-fortune-but-sudden-leadership-changes-fuel-a-mystery | secondary |
| Lanai | Owns ~ 98% since 2012 (~ $300M reported). April 2026 land-use petition (Pulama Lanai) to reclassify ~ 170 acres for villas/spa; earlier $340M, 30-year industrial-park plan. No 2026 sale, loan or refinancing found. | https://hoodline.com/2026/04/ellison-eyes-170-lanai-acres-for-plush-new-villas-push/ | secondary; financing SEARCH-NOT-FOUND |
| Tesla | Director 2018-2022 (per brief; not re-checked). Disclosed ~ 3,000,000 shares ($1B) Jan 2019 (Fox Business, Fortune); x15 for the 5:1 (2020) and 3:1 (2022) splits = ~ 45M shares ~ $16.9B at TSLA $374.58 (2026-10-22 fetch.py). Current holding UNKNOWN (no longer a Section 16 filer). WSJ-reported Citigroup collateral "1.5M from 3M" does not reconcile to 45M unless the unit is pre-split or he sold: UNKNOWN. | https://foxbusiness.com/business-leaders/larry-ellison-discloses-1b-stake-in-tesla | 2019 count VERIFIED-secondary; present stake UNKNOWN |
| Twitter 2022 | $1B equity commitment in Musk's take-private, the largest among the >$7B of backers (Fox Business, 2022-05); 2024 unsealed filing: Musk ~ 75% of X Holdings, no other backer >10%. X merged into xAI (2025); SpaceX acquired xAI Feb 2026 (undisclosed amount per press); SpaceX listed 2026-06-12 at $135. Ellison ~ 0.15% of SpaceX at the IPO, ~ $2.7B at a $1.8T valuation (Forbes via secondary). SPCX trades $144.75 today, -9.14% on the day (fetch.py; ticker identity INFERRED from price continuity with the $147.79 reported for SpaceX on 10/20). At that price the 0.15% stake is roughly $2.9B (scaling the $135 IPO price), INFERRED. Terms of his X-to-xAI-to-SpaceX exchange: SEARCH-NOT-FOUND. | https://foxbusiness.com/markets/elon-musk-funding-twitter-acquisition ; https://www.billionaires.africa/2026/10/21/american-billionaire-larry-ellison-pledges-tesla-spacex-stock-for-sons-110bn-warner-deal/ | secondary |
| Related-party tie to Oracle | Oracle proxy: Skydance Animation (Paramount subsidiary) bought ~ $6.51M of Oracle cloud; Safra Catz sits on the Skydance (Paramount) board. | 2026 DEF 14A | VERIFIED |

## 5. 2026 press on Ellison liquidity (all secondary unless stated)

| Date | Event | Source |
|---|---|---|
| 2026-06-22 / 09-11 / 09-12 | 10b5-1 plan to sell up to 50M ORCL adopted, disclosed, cancelled; no sales | Oracle 10-Q, 8-K (VERIFIED, sec. 1) |
| 2026-09-25 | Proxy: 413M pledged, +67M y/y | VERIFIED |
| 2026-10-06 | WBD closes; family cheque ~ $17B est. | 8-K + Bloomberg est. |
| 2026-10-14 to 10-16 | ORCL -8.8% on 10/14 to $130.55, $128.23 on 10/16; stake down ~ $15.3B in five sessions; drivers cited: AI-debt fears, CoreWeave bond yields ~ 15%, Oracle LT debt > $160B, S&P cut to BBB- in July, ~ $40B planned raise, FY capex guide $90-95B, negative FCF $5.4B last quarter, $664B RPO | https://www.billionaires.africa/2026/10/18/american-billionaire-larry-ellison-loses-15-billion-as-ai-debt-fears-hit-oracle/ (single secondary; Oracle financials not re-verified by me) |
| 2026-10-19 | Bloomberg: net worth $178B, #8, down $194B (-52.1%) from ~ $372B a year earlier (as of 10/16) | Nairametrics |
| 2026-10-20 | WSJ: "borrowing spree"; new Tesla/SpaceX/SKYD pledges; 5 banks, 87M ORCL shares | via NLPC, Quartz, 24/7 |
| 2026-10-21/22 | Semafor (10/22 12:26 EDT): Musk invested ~ $1B in Skydance "according to people familiar"; arrived with other equity (incl. board member Laurene Powell Jobs) at about the same time; described as "a much needed financial injection"; structure, price, vote rights not stated. Malone quote ("a deal coming there"; Larry helped finance Skydance partly with Tesla stock) is his claim, unverified. | https://www.semafor.com/article/10/22/2026/elon-musk-makes-1-billion-investment-in-ellisons-skydance |
| 2026-10-22 | ORCL $125.54 (-2.78%), SKYD ~ $7.79, SPCX $144.75 (-9.1%), TSLA $374.58 (-3.1%): every named collateral asset fell today | fetch.py |

No report found of a margin call, forced sale, lender notice, covenant waiver or default (SEARCH-NOT-FOUND across 4 targeted queries).

## 6. Where the hypothesis is exposed, and what would falsify it

1. Collateral is multi-asset now: ORCL 413M (~ $51.9B), plus SKYD (cost ~ $17B, ~ $11B now if 1.4B shares), Tesla (UNKNOWN count), SpaceX (~ $2.9B), all down on 10/22. Correlated risk-off hits every leg together.
2. Oracle stock IS the main loop: Oracle capex/debt (S&P BBB-, ~ $160B LT debt per one secondary) drives ORCL; ORCL drives Larry's borrowing capacity; Larry's capacity backstops Skydance equity and (to the extent a lender relies on him) $80B of Skydance debt. That is a hypothesis-level chain; only the first and third links are documented.
3. Mitigants documented: Oracle says no margin accounts and capacity to repay without the shares; the equity cheque was syndicated down from $46.7B to ~ $17B (reported); no ORCL sale occurred; ~ $2.3B/yr dividends.
4. Falsifiers to watch: a Form 4/144 showing an ORCL sale; a new 8-K/proxy supplement raising the pledged count; Oracle disclosure of a pledge release; Skydance filings of a Trust sale of SKYD or lender pledge disclosure (Skydance 13D/A filed 2026-10-08, accession 0001193125-26-418066, not retrieved; likely holds Trust share counts); a Musk filing (13D/13G) if >5% (not obviously triggered by $1B; Class B market cap not checked).

## 7. Could not reach / not done

- WSJ original (2026-10-20), Bloomberg ($17B / 1.4B shares), Variety FCC piece (redirected host not followed), AGBI (403), E&P (403), Quartz (403).
- California UCC lien filings; any loan agreement, LTV, maintenance-margin terms.
- Skydance Schedule 13D/A (2026-10-08) and Form 3/4 for the Trust / David Ellison (would give the family's actual share count and pledges of SKYD); FCC ownership petition tables.
- Per-investor split of the 3,917,657,246 PIPE shares; Musk transaction documents.
- Tesla current holding; SpaceX share count; terms of X to xAI to SpaceX exchange.
- Oracle FY26 10-K risk-factor language on Ellison pledging and Oracle's own debt metrics (secondary figures only).
- Earliest adoption date of the Ellison pledging exception (proxies before 2016 not pulled).

## SUMMARY FOR PROME

1. **Pledged ORCL shares (VERIFIED, DEF 14A):** 413,000,000 as of 2026-09-21 (proxy filed 2026-09-25) vs 346,000,000 as of 2025-09-19 (filed 2025-09-26); 277M in 2024, 307M in 2022-23, 315M in 2016. Total holding 1,158,375,174 (38.2%); no Form 4 sales since mid-2025; 50M-share 10b5-1 sale plan (adopted 6/22/26) cancelled 9/12/26 with zero sold.
2. **Pledged value (computed):** $102.5B at the 2026 high close ($248.15, 2026-06-01); $51.9B at today's $125.54 (-49%); 346M was worth $106.8B on 9/19/25. Loan size, LTV, margin triggers: UNKNOWN; Oracle says no margin accounts, no hedging, capacity to repay without the shares.
3. **Banks (reported, WSJ via secondary):** Citi, HSBC, JPM, UBS, BNP hold liens on 87M ORCL (30M a year ago); JPM and Citi added SpaceX and SKYD stock around 9/25-10/1; Tesla collateral reportedly cut. Not verified at the lien filings.
4. **Funding path, documented:** Trust + Larry personally guaranteed the WBD equity ($45.72B) and signed a $46.72B subscription (8-Ks 3/2 and 4/7/26); rights were syndicated to affiliates, RedBird, PIF, L'imad, QIA, LionTree; closing 10/6/26 saw 3,917,657,246 Class B shares sold at $12 ($47.01B). **Inferred/reported:** family cheque ~ $17B (Bloomberg), Gulf ~ $24B, RedBird ~ $4B; family cash came from ORCL/Tesla/SpaceX-backed loans (proxy only says "outside personal business ventures"; WSJ links it to WBD). Debt ($41B+ secured notes, ~ $80B net) sits at Skydance; no Larry guarantee of it found.
5. **Hypothesis verdict:** collateral shrinkage VERIFIED on value; "ORCL fall forced outside money in" NOT shown: the syndication (4/7/26, ORCL $143) pre-dated the June high and the filing's stated reason is shareholder-base diversification. Musk ~ $1B is one Semafor report (10/22, anonymous sources, terms unknown).
6. **Load-bearing uncertainties:** (a) loan sizes/LTV/lender triggers are not public, so "stretched" cannot be measured; (b) the family's actual SKYD share count and any SKYD pledge (Skydance 13D/A 10/8/26 and Trust Form 3/4 not retrieved).
7. **Not reached:** WSJ/Bloomberg originals, California UCC filings, FCC ownership tables, Tesla/SpaceX counts, pre-2016 pledging-exception history. Net-worth aggregators disagree ($165.7B vs $178B); neither reconciles to shares x price.
