<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Bank OZK: TDR/Loan Modification Deep Dive — ASC 326 \& FFIEC Call Report Analysis

## Executive Summary

Bank OZK's regulatory and GAAP disclosures reveal a bank running an unusually high volume of loan extensions and modifications against a backdrop of rapidly deteriorating credit quality — the hallmarks of a CRE extend-and-pretend cycle. The specific ASC 326 "financial difficulty modification" table from the 2024 10-K (filed February 2025) is embedded deep in the financial notes and was not directly extractable from available sources, but substantial operational data was sourced across the earnings call transcript, annual report excerpts, and call report aggregators. Here is everything that could be confirmed:

***

## Section I: ASC 326 — Modifications to Borrowers Experiencing Financial Difficulty

### What the 2024 10-K Does and Does Not Disclose

OZK's management has been emphatic in earnings calls that their loan modifications are **not concessions** in the traditional TDR sense — no rate reductions, no spread reductions, no floor reductions, no expanded commitments. This framing is deliberate and legally material: under ASU 2022-02 (which eliminated TDR accounting effective 2023), "financial difficulty" modifications under ASC 326-20-50 are defined by borrower distress, not by the nature of the concession. The bank's insistence that modifications involve fee collection, reserve replenishment, and paydown requirements does **not** by itself disqualify those modifications from the ASC 326-20-50 disclosure regime if the borrower meets the "experiencing financial difficulty" test.[^1][^2]

### Modification Volume — What Is Publicly Confirmed

**Q4 2024 (fiscal year-end quarter):**

- **58 RESG loans** received term extensions or modifications in Q4 2024[^2]
- Associated with those 58 modifications: \$52 million in unscheduled paydowns, \$41.8 million in reduced unfunded commitments, \$8.4 million in modification fees collected (some deferred over loan life for 1-year+ mods, some straight to income for short-term mods), and \$38.8 million in additional reserves/reserve deposits posted[^2]

**Q3 2025 (most recent reported):**

- **41 loans** reaching maturity were extended or modified in Q3 2025, with ~\$70 million in reserve deposits posted, \$13.5 million in fees, over \$80 million in unscheduled paydowns, and \$14 million in unfunded balances curtailed — described as "among the highest over the 13 quarters" being tracked[^3]

**Cumulative 14-Quarter Tracker (through Q4 2025):**

- Over the 14-quarter tracking period, OZK collected: \$1.3 billion in additional equity contributions, \$866 million in reserve deposits, and \$429 million in unscheduled principal paydowns alongside tens of millions in modification fees[^4]


### The Definitional Problem: "Modifications" vs. "Financial Difficulty Modifications"

This is the crux of the analytical issue. OZK discloses **operational modification counts and cash flows** but has structured its disclosures to argue these are routine commercial negotiations rather than ASC 326-20-50 "financial difficulty" modifications. The 2024 10-K's Note 3 (Loans) does contain an ASC 326-20-50 disclosure table — standard for all banks — but the publicly accessible excerpts of that note show the loan portfolio composition table (total loans \$29.97 billion as of December 31, 2024) rather than the financial difficulty modification detail table.[^5]

**What OZK almost certainly discloses in that note (based on structure of peers and regulatory requirements):**
The table would break out modification amounts by type (term extension, rate reduction, payment deferral, principal forgiveness, combination) by loan category, expressed as amortized cost and as a percentage of the loan class. Given the nature of RESG modifications — term extensions with fee and reserve requirements but **no rate reductions** — the vast majority would appear in the **"Term Extension"** column, with minimal or zero in Rate Reduction or Payment Deferral buckets.

***

## Section II: FFIEC Call Report Data (RSSD 107244, FDIC Cert 110)

### RC-C Memoranda Item 1 — Performing Modified Loans

Under the ASU 2022-02 transition, Call Report Schedule RC-C Memoranda items 1.a–1.g replaced the old TDR reporting. Banks report loans modified for borrowers experiencing financial difficulty that are **currently performing** (in compliance with modified terms). If not performing, they migrate to RC-N Memoranda.

**Confirmed Call Report Data (Q3 2024, most recent available from BankRegData):**[^6]


| Metric | Amount |
| :-- | :-- |
| Performing Restructured Loans (RC-C Memo, HK25) | **\$1,764,000** |
| Nonaccrual loans | \$175,665,000 |
| OREO | \$77,198,000 |
| Total adjusted NPAs | \$253,156,000 |
| Texas Ratio (OZK, Q3 2024) | **4.73%** |

The \$1.764 million figure for "performing restructured loans" in the traditional RC-C Memorandum sense is **strikingly low** relative to the 58+ modifications per quarter that management is describing operationally. This divergence is precisely the extend-and-pretend signal you're hunting: the bank is processing hundreds of loan extensions while reporting a de minimis balance of formally restructured/modified loans in the regulatory schedule.

**Note on the Q4 2024 call report:** The December 31, 2024 10-K discloses nonaccrual loans of \$131.5 million and foreclosed assets of \$69.4 million, totaling \$200.9 million in NPAs — slightly down from the Q3 2024 NPA level of \$253.2 million shown in the BankRegData Texas Ratio table, reflecting the Pacific Center loan sale at par in early January 2025.[^7][^6]

### RC-N Memoranda — Past Due Modified Loans

No direct RC-N Memoranda item-level data for OZK was extractable from public sources. However, the annual report discloses: nonaccrual loans of \$131.5 million at 12/31/2024 vs. \$66.7 million at 12/31/2023 — a **97% year-over-year increase** in nonaccruals, while the bank simultaneously processed 58+ modifications per quarter.[^7]

***

## Section III: The Extend-and-Pretend Scorecard

| Signal | Data | Interpretation |
| :-- | :-- | :-- |
| Nonaccrual loans YoY change | \$66.7M → \$131.5M (+97%)[^7] | NPLs doubling while loan book grew ~13% |
| Formal RC-C restructured loans | ~\$1.76M[^6] | Near-zero vs. 58+ mods/quarter operationally |
| RESG modifications Q4 2024 | 58 loans, \$38.8M new reserves, \$8.4M fees[^2] | High-volume, rolling extension activity |
| Term extension characterization | Management: "not concessions"[^2] | No rate relief, but sponsors can't exit — functional forbearance |
| Modification fees Q3 2025 | \$13.5M per quarter; "among highest in 13 quarters"[^3] | Acceleration, not normalization |
| Net charge-off escalation | \$12.4M Q4 2024 → \$98.3M Q4 2025 (8x in one year)[^1] | Extensions delayed but didn't prevent losses |
| ACL/NCO coverage ratio | Fell below 1.0x for first time since 2010[^1] | Reserve inversion — the buffer is consumed |
| 2022 vintage maturity wall | \$13.8B originated; maturing Q1–Q3 2026[^1] | Hard deadlines arriving; extend options narrowing |


***

## Section IV: Interest Reserve Mechanics — The Hidden TDR

One critical disclosure from the 10-K deserves special attention. OZK states explicitly:

> *"During the years ended December 31, 2024, 2023 and 2022, there were no situations where interest reserves were advanced outside of the terms of the contractual loan agreement to avoid such loan from becoming nonperforming."*[^7]

This is a regulatory bright-line statement. However, the scale is staggering:


| Year | Interest Income Recognized from Reserve Advances | Interest Actually Advanced |
| :-- | :-- | :-- |
| 2024 | **\$504 million**[^7] | \$524 million |
| 2023 | \$411 million | \$391 million |
| 2022 | \$340 million | \$332 million |

The maximum committed balance on loans with interest reserves at 12/31/2024 was **\$19.8 billion**, of which **\$8.6 billion was outstanding** and **\$11.2 billion remained to be advanced**. This is the structural mechanism by which construction loans can remain technically "performing" — the bank funds interest payments from its own loan advances, which are contractually permitted. When the reserve is exhausted without stabilization, the loan either extends (new reserves posted) or goes nonperforming. The 58 Q4 2024 modifications represent the subset where reserves ran low and sponsors posted new capital to buy more time.[^7]

***

## Section V: Key Gaps and What to Pull Next

1. **Note 3 full table from the 2024 10-K** — The specific ASC 326-20-50 table breaking out modification amounts by type (term extension, rate reduction, combination) and by loan class. This requires direct access to the full 10-K PDF (FDIC iDocs or SEC EDGAR filing for OZK, accession number for 2024 annual report filed ~February 2025). The eproxymaterials hosted version cut off before this note was accessible.
2. **Re-default rate disclosure** — Under ASC 326-20-50-4, banks must disclose the extent to which previously modified loans subsequently defaulted during the reporting period. This table (typically a few lines showing amortized cost of loans that defaulted within 12 months of modification) is almost certainly present in OZK's 10-K Note 3 but was not reachable in this session.
3. **RC-C Memoranda 1.a–1.g line items (Q4 2024)** — The FFIEC CDR (CDR.ffiec.gov) or iBanknet's RC-C schedule for CERT 110, period 20241231, would show each loan category's modified-performing balance. The Q3 2024 data shows \$1.76M total performing restructured — pulling Q4 2024 would confirm whether this ticked up as modifications accelerated.
4. **RC-N Memoranda 1.a–1.g (Q4 2024)** — Modified loans that failed post-modification. This is the re-default rate at the regulatory level, and given the jump in nonaccruals from \$66.7M to \$131.5M YoY, some portion of that increase likely came from modified loans re-defaulting.

***

## Bottom Line

The extend-and-pretend hypothesis has structural support at Bank OZK. Management is running 41–58+ RESG loan modifications per quarter, collecting fees and characterizing them as commercially positive, while formal regulatory restructured-loan balances sit at ~\$1.76 million — a figure that defies credibility given the operational disclosures. Nonaccruals doubled YoY through 2024, charge-offs grew 8x from Q4 2024 to Q4 2025, and the 2022 vintage maturity wall is arriving in 2026 with fewer extension options remaining. The formal ASC 326-20-50 disclosure table in the 10-K Note 3 — specifically the re-default row — is the single most important number to extract from the filing to confirm whether previously extended loans are now failing at an accelerating rate.[^4][^1][^3][^6][^2][^7]
<span style="display:none">[^10][^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^11][^110][^111][^112][^113][^114][^115][^116][^117][^118][^119][^12][^120][^121][^122][^123][^124][^125][^126][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^8][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^9][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://temple8capital.substack.com/p/bank-ozk-the-next-svb

[^2]: https://earningscall.biz/e/nasdaq/s/ozk/y/2024/q/q4

[^3]: https://www.fool.com/earnings/call-transcripts/2026/01/22/bank-ozk-ozk-q3-2025-earnings-call-transcript/

[^4]: https://finance.yahoo.com/news/bank-ozk-q4-earnings-call-162725227.html

[^5]: https://eproxymaterials.com/interactive/ozk2024/pf/page_107.pdf

[^6]: https://bankregdata.com/bkAQmet.asp?met=TXR\&inst=C110

[^7]: https://eproxymaterials.com/interactive/ozk2024/pf/page_068.pdf

[^8]: https://www.peoplesbancorp.com/wp-content/uploads/2024/05/PEBO-Annual-Report_vF_Revised_WEB-2.pdf

[^9]: https://business.cch.com/BFLD/Supplemental-Instructions-December-2024-Call-Report-Materials-12232024.pdf

[^10]: https://www.fdic.gov/system/files/2024-07/sisummer12-article4.pdf

[^11]: http://gtw3.grantthornton.in/assets/P/Proposed-ASU-Financial-Instruments-Credit-losses-Topic-326-Troubled-debt-restructuring-and-vintage-disclosures.pdf

[^12]: https://www.aes.com/sites/vault/files/2026-03/AES-Corp-2025-Annual-Report-03-20-2026.pdf

[^13]: https://www.fdic.gov/system/files/2024-08/2022-06-rc-c1.pdf

[^14]: https://www.fdic.gov/system/files/2024-06/2012-accounting.pdf

[^15]: https://ww3.fca.gov/readingrm/infomemo/Lists/InformationMemorandums/Attachments/291/ASUonTDRInfoMemo.pdf

[^16]: https://www.agloan.com/wp-content/uploads/2025/03/2024-American-AgCredit-Annual-Report.pdf

[^17]: https://www.fdic.gov/sites/default/files/2024-03/fil08026a.pdf

[^18]: https://www.sahmcapital.com/news/content/rising-non-performing-loans-at-bank-ozk-ozk-challenge-bullish-credit-quality-narratives-2026-01-22

[^19]: https://www.fdic.gov/regulations/examinations/supervisory/insights/sisum12/sisummer12-article4.pdf

[^20]: https://www.sec.gov/Archives/edgar/data/0001331520/000133152026000065/a2025arsfiling.pdf

[^21]: https://www.fdic.gov/supplemental-instructions-december-2024-call-report-materials

[^22]: https://dart.deloitte.com/USDART/home/publications/archive/deloitte-publications/heads-up/2020/faq-tdr-cares-act-interagency-statement

[^23]: https://www.sec.gov/Archives/edgar/data/764038/000155837025002235/ssb-20250102xex99d2.htm

[^24]: https://www.sec.gov/edgar/browse/?CIK=0002034313

[^25]: https://www.sec.gov/Archives/edgar/data/1331520/000133152026000074/a2025annualreport.htm

[^26]: https://www.mainstcapital.com/investors/sec-filings/all-sec-filings/content/0001396440-25-000144/0001396440-25-000144.pdf

[^27]: https://www.sec.gov/Archives/edgar/data/875357/000087535725000020/bokf-20250320.htm

[^28]: https://www.sec.gov/Archives/edgar/data/1169770/000116977025000015/banc-20250327.htm

[^29]: https://www.sec.gov/Archives/edgar/data/1810546/000119312525064760/d914340ddef14a.htm

[^30]: https://www.sec.gov/Archives/edgar/data/729986/000119312524084103/d33137ddef14a.htm

[^31]: https://www.sec.gov/Archives/edgar/data/1331520/000133152024000099/a2023annualreportarsfiling.pdf

[^32]: https://www.sec.gov/Archives/edgar/data/1767042/000119312523088292/d371435dex101.htm

[^33]: https://www.sec.gov/Archives/edgar/data/1649739/000164973924000140/0001649739-24-000140.txt

[^34]: https://www.sec.gov/Archives/edgar/data/102909/000110465924020402/tv0405-bankozk.htm

[^35]: https://www.sec.gov/Archives/edgar/data/764038/000110465924080148/tm2417792-6_424b3.htm

[^36]: https://moneysense.ai/sec-filings/company/ozkap

[^37]: https://ca.marketscreener.com/quote/stock/BANK-OZK-44965059/news/Bank-OZK-Form-10-K-Annual-Report-49218756/

[^38]: https://www.sec.gov/edgar/browse/?CIK=CIK0000807707

[^39]: https://www.stocktitan.net/sec-filings/OZK/

[^40]: https://www.sec.gov/edgar/browse/?CIK=1991261

[^41]: https://in.marketscreener.com/quote/stock/BANK-OZK-44965059/news/Bank-OZK-Form-10-K-A-Amendment-to-Annual-Report-46111785/

[^42]: https://www.sec.gov/edgar/browse/?CIK=2030476

[^43]: https://eproxymaterials.com/interactive/ozk2024/pf/page_141.pdf

[^44]: https://www.nasdaq.com/market-activity/stocks/ozk/sec-filings

[^45]: https://www.marketbeat.com/stocks/NASDAQ/OZK/sec-filings/

[^46]: https://seekingalpha.com/symbol/OZK/sec-filings

[^47]: https://www.sec.gov/Archives/edgar/data/1145722/000119312526085674/0001193125-26-085674-index.htm

[^48]: https://www.sec.gov/edgar/browse/?CIK=1569650

[^49]: https://www.tradingview.com/symbols/NASDAQ-OZK/documents/

[^50]: https://www.marketbeat.com/stocks/NASDAQ/OZKAP/sec-filings/

[^51]: https://www.criadv.com/wp-content/uploads/2023/12/Loan-Modifications-Quick-Reference-Guide.pdf

[^52]: https://www.kbra.com/publications/VBTpyGKR/kbra-affirms-ratings-for-bank-ozk

[^53]: https://eproxymaterials.com/interactive/ozk2024/pf/page_034.pdf

[^54]: https://simplywall.st/stocks/us/banks/nasdaq-ozk/bank-ozk/news/rising-non-performing-loans-at-bank-ozk-ozk-challenge-bullis

[^55]: https://blogs.claconnect.com/financialinstitutions/reporting-loan-modifications-with-the-implementation-of-cecl/

[^56]: https://www.facebook.com/3fm927/posts/banks-non-performing-loans-increase-to-257-in-april-2024/861568226003779/

[^57]: https://www.claconnect.com/en/resources/blogs/reporting-loan-modifications-with-the-implementation-of-cecl

[^58]: https://www.sec.gov/Archives/edgar/data/1746129/000114036125008438/R73.htm

[^59]: https://bankersonline.org/download/17/telebriefing-materials/1964/ficc-april-2025-telebriefing-materials-documenting-and-recording-loan-modifications

[^60]: https://www.federalreserve.gov/apps/reportingforms/Download/DownloadAttachment?guid=e84c65ce-db25-4951-8ab6-23a8f5021a74

[^61]: https://www.sec.gov/Archives/edgar/data/799850/000117184325004811/exh_991.htm

[^62]: https://eproxymaterials.com/interactive/ozk2024/template/toc.php?nn=1\&zz=252\&up=1

[^63]: https://cdn.hl.com/pdf/2024/cre-debt-market-update-oct-2024.pdf

[^64]: https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/allowances-for-credit-losses/pub-ch-allowances-credit-losses.pdf

[^65]: https://www.occ.treas.gov/topics/supervision-and-examination/bank-operations/accounting/allowance-for-credit-losses/index-allowances-for-credit-losses.html

[^66]: https://www.fhfa.gov/advisory-bulletin/ab-2021-03

[^67]: https://www.federalregister.gov/documents/2025/12/05/2025-22015/loan-performance-categories-and-financial-reporting

[^68]: https://eproxymaterials.com/interactive/rbcaa2011/pf/page_148.pdf

[^69]: https://www.fasb.org/news-and-meetings/in-the-news/fasb-improves-guidance-on-purchased-loans-423314

[^70]: https://eproxymaterials.com/interactive/tbsk2016/pf/page_064.pdf

[^71]: https://www.firstresourcebank.com/wp-content/uploads/2024-Final-Annual-Report.pdf

[^72]: https://www.eurobank.gr/-/media/eurobank/omilos/enimerosi-ependuton/oikonomikes-katastaseis-thigatrikon-etairion/oikonomikes-katastaseis-thigatrikon-etairion-2024/eurobank-bulgaria-ad.pdf

[^73]: https://www.fdic.gov/resources/bankers/call-reports/crinst-031-041/2023/2023-09-rc-c1.pdf

[^74]: https://www.farmcreditofvirginias.com/sites/default/files/Financial Reports/15815-FCV-2024AnnualReport-WEB.pdf

[^75]: https://assets.revolut.com/pdf/annualreport2025.pdf

[^76]: https://www.fdic.gov/resources/bankers/call-reports/crinst-031-041/2024/031-041-324-rc-n.pdf

[^77]: https://content.edgar-online.com/ExternalLink/EDGAR/0001228454-24-000003.html?hash=0199b2160c1744d2d33ade3a981c124833e8fdd8d48bb32bee291b2caf8678d4\&dest=bcbp-20231231x10k_htm

[^78]: https://www.eurobank.gr/-/media/eurobank/omilos/enimerosi-ependuton/oikonomikes-katastaseis-thigatrikon-etairion/oikonomikes-katastaseis-thigatrikon-etairion-2023/ifrs-eurobank-fs-2023-eng-29-03-2024.pdf

[^79]: https://www.fdic.gov/system/files/2024-08/2016-03-rc-c1.pdf

[^80]: https://www.sec.gov/Archives/edgar/data/0000885275/000119312526117752/ars_2025.pdf

[^81]: https://www.postbank.bg/-/media/Files_2023/IFRSEurobankFS-2022ENG30032023-for-GRP.pdf?la=en\&hash=57FD7F08A81BA97CFAB28D7744B7CA22

[^82]: https://louisianalandbank.com/wp-content/uploads/2026/03/2025-Annual-Report-with-Cover.pdf

[^83]: http://bankrupt.com/TCR_Public/240825.mbx

[^84]: https://cdr.ffiec.gov

[^85]: https://www.investing.com/news/transcripts/earnings-call-transcript-bank-ozk-beats-q4-2024-earnings-expectations-93CH-3819323

[^86]: https://wifpr.wharton.upenn.edu/wp-content/uploads/2025/10/HSV-Regional-Banks-and-CRE-Risks.pdf

[^87]: https://www.globenewswire.com/news-release/2025/01/16/3011145/0/en/Bank-OZK-Announces-Record-Fourth-Quarter-and-Full-Year-2024-Earnings.html

[^88]: https://ir.oldnational.com/files/doc_financials/2021/q1/3c348ba4-9bad-49db-93f9-163c278a50de.pdf

[^89]: https://jhfinance.web.unc.edu/wp-content/uploads/sites/12369/2025/11/HSSvN_RegionalCRE_082025.pdf

[^90]: https://mandmbank.com/wp-content/uploads/2022/02/2020-Annual-Report-FINAL.pdf

[^91]: https://www.linkedin.com/posts/rebel-c-b253391_extend-and-pretend-in-bank-cre-lending-activity-7297078455039348736-UqWe

[^92]: https://www.sec.gov/Archives/edgar/data/1331520/000119312521305508/d231020ds4.htm

[^93]: https://www.investing.com/news/transcripts/earnings-call-transcript-bank-ozk-q2-2025-shows-strong-loan-growth-93CH-4286819

[^94]: https://www.timelessinvestor.com/2024/06/11/study-of-dpst-kre-and-fas-part-ii/

[^95]: https://www.youtube.com/watch?v=etpmCyLYxjg

[^96]: https://columbusfinance.org/wp-content/uploads/2024/01/2023-Minutes.pdf

[^97]: https://www.theglobeandmail.com/investing/markets/stocks/OZK/pressreleases/37206953/bank-ozk-earnings-call-balances-cre-risk-and-strength/

[^98]: https://www.sec.gov/Archives/edgar/data/720005/000072000519000019/0000720005-19-000019.txt

[^99]: https://www.hawaii.edu/offices/bor/institutional-success/materials/202505010830/Cmte_on_Institutional_Success_Materials.pdf

[^100]: https://www.aol.com/finance/bank-ozk-ozk-q2-2025-192436267.html

[^101]: https://www.sec.gov/Archives/edgar/data/38074/0001193125-12-311349.txt

[^102]: https://www.sec.gov/Archives/edgar/data/1331520/000133152026000065/a2025arsfiling.pdf

[^103]: http://bankrupt.com/TCR_Public/211019.mbx

[^104]: https://www.fdic.gov/bank-financial-reports/031-041-rc-c1-loans-and-leases-december-2024

[^105]: https://finance.yahoo.com/news/bank-ozk-rides-high-rates-140100865.html

[^106]: https://eproxymaterials.com/interactive/ozk2024/pf/page_069.pdf

[^107]: https://www.reginfo.gov/public/do/DownloadDocument?objectID=120800101

[^108]: https://s203.q4cdn.com/718923485/files/doc_financials/2023/q1/10q123.pdf

[^109]: https://www.fdic.gov/resources/bankers/call-reports/crinst-051/2024/2024-03-051-callinst.html

[^110]: https://www.federalreserve.gov/apps/fof/SeriesAnalyzer.aspx?s=FS764035123\&t=S.9.A\&bc=S.9.A%3AFU764035123\&suf=A

[^111]: https://www.ibanknet.com/scripts/callreports/reportlist.aspx?ibnid=usa_107244\&per=20251231

[^112]: https://www.fdic.gov/news/financial-institution-letters/2024/fil24001a.pdf

[^113]: https://www.imf.org/-/media/Files/Publications/covid19-special-notes/en-special-series-on-covid-19-treatment-of-restructured-loans-for-fsi-compilation.ashx

[^114]: https://www.gurufocus.com/stock/OZKAP.PFD/transcripts/2476839

[^115]: https://www.fdic.gov/news/financial-institution-letters/2025/revisions-consolidated-reports-condition-income-call

[^116]: https://www.ibanknet.com/scripts/callreports/getbank.aspx?ibnid=usa_107244

[^117]: https://goghieas.substack.com/p/when-troubled-loans-disappear-inside

[^118]: https://www.ibanknet.com/scripts/callreports/reportlist.aspx?ibnid=usa_107244\&per=20250930

[^119]: https://ng.investing.com/news/stock-market-news/earnings-call-bank-ozk-optimistic-despite-varied-q2-paydowns-93CH-1448105

[^120]: https://www.fdic.gov/news/financial-institution-letters/2024/consolidated-reports-condition-and-income-fourth-quarter

[^121]: https://www.ibanknet.com/scripts/callreports/viewreport.aspx?ibnid=usa_107244\&per=20251231\&rpt=RCM\&typ=html

[^122]: https://www.globenewswire.com/fr/news-release/2025/01/16/3011145/0/en/Bank-OZK-Announces-Record-Fourth-Quarter-and-Full-Year-2024-Earnings.html

[^123]: https://www.fdic.gov/bank-financial-reports/031-041-rc-k-quarterly-averages-december-2024

[^124]: https://eproxymaterials.com/interactive/ozk2024/pf/page_033.pdf

[^125]: https://www.sec.gov/Archives/edgar/data/1027552/000121390023079404/0001213900-23-079404.txt

[^126]: https://www.carnivalcorp.com/wp-content/uploads/2024/08/Carnival-Corporation-plc-2023-Notice-of-Annual-Meetings-and-Proxy-Statement-1.pdf

