# J. Every SoftBank-Oracle investment, 1981-2026

Reader J, read-only. Written 2026-10-22 22:08 ET (`date` run in the same command block). 22 of 25 WebSearch calls used. Primary sources were pulled by `curl` from SEC EDGAR (data.sec.gov, efts full-text search), group.softbank, and oracle.com. Tags: **VERIFIED** = read at the primary document. **INFERRED** = supported, not directly established. **SEARCH-NOT-FOUND** = query returned nothing (scope stated). No trade recommendation.

## Headline

SoftBank has never put money into Oracle Corporation's own treasury (its stock, bonds, or a subsidiary). Searched 1994-2026. Four SoftBank-Oracle money events exist:
1. A small open-market purchase of Oracle common stock (1,220,000 shares, Q1 2025, sold in Q3 2025).
2. SoftBank paying Oracle $4.3B cash for Oracle's stake in Ampere (closed 2025-11-25). Oracle was the seller, so this is a purchase from Oracle, not an investment in it.
3. The Stargate equity-funder framework (2025-01-21). It is money into Stargate LLC, not into Oracle.
4. An Oracle Alloy cloud contract with SoftBank Corp., the SoftBank-controlled telecom (2025-10-08), with no figure disclosed.

For 2026 I found no SoftBank purchase of Oracle stock, bonds, convertibles or preferred, and no SoftBank financing of an Oracle-leased data-center project (negative scope in section 3).

## 1. Master table

| # | Date | SoftBank entity | Oracle-side counterparty | Instrument | Amount | Direction | Status | Source class / tag |
|---|---|---|---|---|---|---|---|---|
| 1 | 1981-1999 | SoftBank Corp (then software distributor / holding co.) | Oracle Corp | any equity / JV | none found | n/a | n/a | Oracle's 227 SEC filings dated 1994-2003 (10-K, 10-Q, proxies, 13D/13G, S-8, tender-offer forms) contain zero "SoftBank". EDGAR full-text search on Oracle's current CIK for 2001-2026 returns 9 filings (listed in section 5), none a SoftBank-Oracle investment. **SEARCH-NOT-FOUND** (Oracle-side). SoftBank annual reports FY1997-FY2005 mention Oracle only in rows 2 and 3 below. |
| 2 | 1985-10-15 to ~2000 | none | Oracle Corporation Japan (TSE 4716) | founding / IPO | Oracle Corp 100% at founding (capital JPY 1,000K); OTC listing 1999-02, TSE-1 2000-04; US parent ~74% today | n/a | n/a | JP secondary (the-shashi.com, Oracle Japan IR PDFs). Oracle's FY26 10-K confirms Oracle is the majority holder. A SoftBank stake in Oracle Japan is **SEARCH-NOT-FOUND**. The Oracle Japan major-shareholder table (yuho / EDINET) was not reachable. |
| 3 | 2003-10 and 2003-11 | SOFTBANK BB Corp. | Oracle Corporation Japan | alliance / contract | no figure | co-operation | historical | **VERIFIED** SoftBank Fact Book 2004 chronology (utility-computing alliance, Oct 2003; remote medical imaging diagnosis system with Doctor Net, Nov 2003). https://group.softbank/system/files/pdf/ir/financials/annual_reports/annual-report_fy2004_02_en.pdf |
| 4 | 2014-12-31 | none (Oracle side) | Oracle 401(k) Plan | SoftBank Corp. shares inside plan holdings | 58,503 sh, $3.5M | Oracle plan to SoftBank | passive | Oracle 11-K filed 2015-05-14, acc. 0001193125-15-187963. Employee plan, not corporate. Trivia, **VERIFIED**. |
| 5 | 2017 (SVF1 first close 2017-05-22) | SoftBank Vision Fund 1 | Ellison family office (not Oracle Corp) | LP interest | undisclosed | Ellison to SVF1 (reverse) | unknown | **Not verified.** DealStreetAsia and Mobile World Live (secondary) report an Ellison family-office commitment. SoftBank's own release (https://group.softbank/en/news/press/20170522) names PIF, Mubadala, Apple, Foxconn, Qualcomm and Sharp, not Ellison or Oracle. Oracle as a corporate LP: **SEARCH-NOT-FOUND**. |
| 6 | 2020-03 to 2021-12 (SB Northstar era) | SB Northstar LP / SBG | Oracle common or options | listed equity / OTC calls | none | n/a | n/a | SBG 13F-HR 2020-Q1 to 2021-Q4: 2 to 15 positions each (Lemonade, Line, Nvidia, T-Mobile, DoorDash...), no Oracle. SoftBank FY2020-21 earnings decks: Oracle appears only once, in a buyback-ranking table (Q1 FY2020 investor deck). SB Northstar's OTC call options were not itemised by issuer; no source names Oracle. **SEARCH-NOT-FOUND**. |
| 7 | 2025-01-21 | SBG (financial responsibility) | Stargate LLC; Oracle listed as co-equity funder and technology partner | JV equity | SoftBank press release gives only "$500B over four years, $100B immediately". Reported by The Information (secondary): SBG $19B, OpenAI $19B, Oracle $7B, MGX $7B. | SBG and Oracle both fund Stargate; no flow from SoftBank to Oracle | open | **VERIFIED** wording: https://group.softbank/en/news/press/20250122 ("initial equity funders in Stargate are SoftBank, OpenAI, Oracle, and MGX"). Dollar split **INFERRED / secondary**. |
| 8 | 2025-Q1 (new vs 2024-12-31) | SBG via included manager #5, Silver Brick Management Pte. Ltd. (investment discretion "defined") | Oracle Corp (CUSIP 68389X105) | common stock, open-market | 1,220,000 sh; $170,568,200 at 2025-03-31 ($139.81/sh implied) | SoftBank buys from the market; no cash to Oracle Corp | **sold** | **VERIFIED** 13F-HR acc. 0001062993-25-009520, filed 2025-05-15 (period 2025-03-31). Absent from 13F-HR acc. 0001062993-25-002489 (period 2024-12-31). Cost and trade dates are not in a 13F: **UNKNOWN**. |
| 9 | 2025-Q2 | same | same | common stock | 1,220,000 sh unchanged; $266,728,600 at 2025-06-30 ($218.63/sh) | same | open at 6/30 | **VERIFIED** 13F-HR acc. 0001062993-25-014418, filed 2025-08-14. |
| 10 | 2025-Q3 | same | same | sale | position gone | n/a | **sold** between 2025-07-01 and 2025-09-30 | **VERIFIED** absence in 13F-HR acc. 0001062993-25-016862 (period 2025-09-30, filed 2025-11-14; 33 rows, Nvidia, TSMC and Symbotic remain in the Silver Brick book). Sale date and price: **UNKNOWN**. Position size is about 0.04% of Oracle's shares outstanding (**INFERRED**, 38.2% = 1,158,375,174 sh per proxy snippet). |
| 11 | 2025-03-20 (JST) announce; 2025-11-25 close | SBG via Silver Bands 6 (US) Corp. (SB6) | Oracle Project Denver Holdings LLC (seller, about 29% holder) | purchase of Oracle's equity, convertible debt and call-option interests in Ampere | **$4.3B cash to Oracle** (Oracle 10-Q FQ2 FY26, 10-Q FQ3, 10-K FY26); $2.7B realized gain. Headline price $6.5B, all-cash, for 100% (SoftBank press release). SoftBank cash paid JPY 964,832M. Sellers: Carlyle, Oracle, Arm. | **SoftBank to Oracle cash** | **closed**; Oracle has no remaining Ampere investment | **VERIFIED** at both ends. Oracle: https://www.sec.gov/Archives/edgar/data/1341439/000119312525315925/orcl-20251130.htm and 10-K FY26 acc. 0001193125-26-277521. SoftBank: https://group.softbank/en/news/press/20250320, /20251126, and the Q3 FY2025 financial report (seller names). |
| 12 | FY2023 to FY2025 | Ampere (SoftBank subsidiary from 2025-11-25) | Oracle | processor purchases / cloud sales | Oracle $104.1M prepay order (FY2023); bought about $3.7M in FY2025; about $97.4M prepay remaining at 2025-05-31. Ampere bought about $2.5M of Oracle cloud in FY2025. | Oracle to Ampere (now SoftBank) and small reverse | open | **VERIFIED** Oracle DEF 14A filed 2025-09-26 (acc. 0001193125-25-220801), related-party section. The 2026 DEF 14A (acc. 0001193125-26-402816) has zero mentions of Ampere or SoftBank, so FY26 purchases are not disclosed (**SEARCH-NOT-FOUND**). |
| 13 | Ampere investor history, 2017-2025 | none | Oracle into Ampere | equity and convertibles | Oracle invested $341M in convertibles in FY25 and $90M in Q1 FY26; carrying value $1.6B (2025-05-31) | Oracle to Ampere, before SoftBank | closed 2025-11-25 | **VERIFIED** Oracle 10-K FY25 and 10-Q FQ1 FY26. |
| 14 | 2025-09-23 and later | SBG | Oracle | Stargate sites; "jointly announced with OpenAI and Oracle" | no SoftBank-to-Oracle money | co-sponsor | open | **VERIFIED** SBG Q2 FY2025 investor deck. CFO Goto on 2025-11-11: on the Oracle 5.5 GW project, "we are not currently considering participation". On 2026-02-12: some projects led by OpenAI, others by Oracle "on a standalone basis"; SBG and OpenAI fund 50/50, roughly 20% equity and 80% debt on average. On 2026-08-06: Stargate is "defined quite broadly and may encompass various data center projects undertaken by SBG, Oracle, and OpenAI". Transcripts: group.softbank, earnings-conference-call PDFs. |
| 15 | 2025-10-08 | SoftBank Corp. (telecom, consolidated by SBG as SBKK) | Oracle Corp / Oracle Japan | Oracle Alloy licence (Cloud PF Type A, sovereign cloud) | no figure | SoftBank Corp. buys platform from Oracle (**INFERRED**) | open; East Japan launch planned 2026-04, West 2026-10 | **VERIFIED** announcement: https://www.oracle.com/news/announcement/softbank-corp-accelerates-japans-ai-and-sovereign-cloud-future-with-oracle-alloy-2025-10-07/. Launch status not verified. |
| 16 | 2025-Q4 to 2026-Q2 | SBG (Silver Brick) and SB Investment Advisers (UK) | Oracle common | 13F | none | n/a | n/a | **VERIFIED** SBG 13F-HR acc. 0001062993-26-000965, -002663, -004387 (periods 2025-12-31, 2026-03-31, 2026-06-30): no Oracle. SB Investment Advisers (UK) 13F-HR, 40 filings 2018-2026: no Oracle. |
| 17 | 2026-02-02 | none found | Oracle | $25B notes; $5.0B 6.50% Series D mandatory convertible preferred; $20B ATM program | buyers undisclosed | n/a | n/a | Oracle 8-Ks 2026-02-04 and 2026-02-05: no SoftBank mention. Order book over $129B (Bloomberg via search, secondary). Bond and preferred holders are not public: **SEARCH-NOT-FOUND**, not proof of absence. |
| 18 | 2026-01-09 | SBG with OpenAI | SB Energy (SoftBank sub), not Oracle | $1B equity ($500M each); Milam County lease to an OpenAI affiliate; warrants granted to OpenAI | $1B | SoftBank/OpenAI into SB Energy | open | Adjacent, not an Oracle flow. SBG Q1 FY2026 report: ¥453.4B derivative loss on Energy Global warrants. The tenant is OpenAI per a secondary source; no Oracle link. |

## 2. Detail on the three contested items

**A. The "$170M of Oracle bought in H1 2025" claim.** The number is real but misread. $170.57M is the quarter-end market value of 1,220,000 shares at 2025-03-31, not a purchase price. The position went from 0 to 1,220,000 shares in Q1 2025 and stayed flat in Q2 (value rose to $266.7M with the stock price). It was gone by 2025-09-30. It sat in the Silver Brick Management book, which is "other included manager 5" in SBG's 13F. That manager's book holds Nvidia, TSMC, Symbotic and PacBio. Silver Brick as the successor to SB Northstar's listed-equity book is **INFERRED**: SBG decks define SB Northstar LP but never mention Silver Brick. SBG's 13F does not show the purchase price or dates. None of this money reached Oracle Corp.

**B. Ampere.** Oracle's own filings say it received $4.3B cash for its equity, debt and call-option interests (closing 2025-11-25) and booked a $2.7B gain. SoftBank's financial report names the seller entity as "Oracle Project Denver Holdings LLC". The $4.3B is about 66% of the $6.5B headline, but the headline includes Ampere's debt repayment and the other sellers, so the share is **INFERRED** and not a clean split. Oracle's pre-sale position was about 29% of Ampere (Oracle DEF 14A, 2025-09-26).

**C. Stargate.** Per SoftBank's own release, Oracle is an equity funder in Stargate and a technology partner. SoftBank is the financial lead and OpenAI the operational lead. No document I read has SoftBank wiring money to Oracle for Stargate. Oracle's reported $7B is a contribution to Stargate (Oracle to JV), reported by The Information and unconfirmed. Oracle's 10-K FY26 and its last 10-Q (period 2026-08-31, filed 2026-09-11) contain zero occurrences of "Stargate", "OpenAI", "SoftBank" or "MGX". The 10-Q says the substantial majority of Oracle's non-marketable investments are in TikTok USDS Joint Venture LLC (15%). So **INFERRED**: Oracle has not booked a material Stargate LLC equity investment. Later Stargate capital calls: **SEARCH-NOT-FOUND** (Stargate LLC is private; no filing exists).

## 3. 2026 negative, stated precisely

No SoftBank purchase of Oracle equity, bonds, convertibles or project debt in 2026 was found. What was searched, where, and when (all 2026-10-22):

| Source | Scope | Result |
|---|---|---|
| SBG 13F-HR (CIK 1065521) | all 13F-HR and 13F-HR/A filings on the EDGAR list (periods 2013-12 to 2026-06; 32 with periods from 2020-03) | Oracle only in 2025-Q1 and 2025-Q2 |
| SB Investment Advisers (UK) 13F-HR (CIK 1731509) | 40 filings; the (US) and (Japan) entities file 13F-NT only | no Oracle |
| SB Northstar GP (CIK 1972882), Silver Brick (CIK 1991269) | own filing lists | no filings |
| Oracle 8-Ks | all 21 filed 2025-01-01 to 2026-10-22, main documents plus exhibits | "SoftBank" appears in none; Ampere in 3 earnings exhibits and the 2025-01-13 8-K |
| Oracle 10-K FY25, FY26; 10-Q Q1 FY26 to Q1 FY27; DEF 14A 2025 and 2026; 424B2 2025-09 | keyword | SoftBank appears only as Ampere buyer |
| EDGAR full-text search for "SoftBank" in Oracle filings, 2001-2026 | all forms | 9 hits: the five 10-K/10-Q Ampere passages, the two 424B2s, the 2025 proxy, and the 2015 11-K |
| SBG Q1 FY2026 deck, financial report and call (2026-08-06), plus FY2024-FY2025 calls, decks and reports | keyword Oracle | Oracle appears in the Stargate and Ampere passages above, nothing on equity or bonds |
| Web | 22 searches, English and Japanese, incl. "SoftBank Oracle investment October 2026" and a "this week" search | no SoftBank investment in Oracle. Related news only: SoftBank's $11.1B bonds for OpenAI (CNBC, 2026-09-23/24); Oracle's force-majeure notice on Project Jupiter (Blue Owl/Stack); Ellison share pledges (Oracle proxy: 413M of 1,158M shares pledged) |

Project financing for Oracle-leased sites, per press (secondary): Abilene by Crusoe, Blue Owl and Primary Digital with JPMorgan debt; Project Jupiter (New Mexico) by Blue Owl equity of about $3B with a bank group of roughly $18B; the $38B JPMorgan/MUFG package for Vantage sites (Wisconsin and Texas); Michigan with Related Digital. None names SoftBank. The likeliest source of the "SoftBank investing in Oracle" headline is Stargate framing or SoftBank's OpenAI funding. That is an INFERENCE about a news item I did not see; no source I found asserts such an investment.

## 4. Reverse flows (Oracle to SoftBank)

| Flow | Detail | Tag |
|---|---|---|
| Oracle LP in Vision Fund | not found in SoftBank's SVF1 release (2017-05-22) or any VF2 coverage | SEARCH-NOT-FOUND |
| Ellison family office in SVF1 | secondary reports, amount undisclosed | unverified |
| Oracle buys Ampere chips | $104.1M prepay (FY2023), $3.7M drawn in FY25, $97.4M left at 2025-05-31; Ampere now SoftBank-owned | VERIFIED, FY26 usage not disclosed |
| Oracle deploys Ampere chips | confirmed by Arm CEO on SoftBank call 2024-08-07 ("Oracle is the customer of Ampere") | VERIFIED |
| Oracle owns SoftBank shares | no | SEARCH-NOT-FOUND |

## 5. What I could not reach

- Q3 2026 13F (period 2026-09-30) is not yet due. Deadline is Mon 2026-11-16 (11-14 is a Saturday). A purchase after 2026-06-30 would not show until then.
- 13F cannot show non-US shares, bonds, convertibles, OTC derivatives or private project debt.
- SBG's Q2 FY2026 results (early November 2026) are not out.
- TDnet, EDINET (needs a key; Oracle Japan major-shareholder table), Nikkei, Bloomberg and Reuters full text are paywalled or blocked. OpenAI's Stargate page and DCD returned 403 or a block page; the SoftBank press release carried the same wording.
- Stargate LLC's actual cap table and any capital calls are private.
- Silver Brick's exact trade dates and cost, and the Alloy go-live status, are not in any source I reached.
