# What is inside the stress? CCC bonds and below-80 loans, split three ways, and who holds the software bucket
**Date:** 2026-10-23 (research 15:00–15:33 ET) | **Mode:** Thesis | **Request:** REQ-DEWEY-20261023-003 (WALTER; Will-approved 13:37 ET). It also covers Will's thread 2 ("What is inside CCC?") | **Confidence:** Medium on the bond-tier split (fund holdings and a strategist's sector table; not ICE tier data). Medium on the loan split (JPM figure via news reprints; only the technology share is public). High on the BDC table (each BDC's own 10-Q/10-K, read by DEWEY).

**Kill check at intake (15:00 ET), none fired:** (a) LIQUID, BROCK and VULCAN have published no October CCC or below-80 split (grep since 10/20). (c) FRED HY OAS was 3.40% on 10/22, at or above 3.20%. (b) The deliver-by date (10/26) has not passed.

## Key Finding
**The two distressed pools have different contents.**
- **CCC bonds:** about three-quarters of the October damage is *everything else*: cable/telecom (Altice, Virgin Media, Liberty Puerto Rico, Optimum/CSC), JetBlue and FMC. Software is about **5–8%**. AI builders are about **17%**, almost all CoreWeave.
- **Below-80 leveraged loans:** **technology is 39% ($54.4B)** (JPM, 10/6). The names given are PE-owned software (CDK, Qlik, Quest). Software is only about 10–13% of the loan index, so it is roughly 3× over-represented in distress.
- **Overall:** REQ-002's "mostly broad" verdict **stands for HY bonds**. **"AI broadly defined" is a large share of stress only in loans and private credit**, which is where the software bucket sits. Of listed BDCs, ARCC, BXSL, FSK and GBDC carry the most software dollars; HTGC and GBDC carry the highest software shares.

## (1) Three-way split: CCC bonds

**(a) Price damage in HYG's CCC-proxy sleeve, 10/13 → 10/22.** HYG and JNK publish no ratings. The proxy is bonds with yield-to-worst ≥12% in the 10/13 file: 103 lines, 5.18% of the fund. This is LIQUID's 10/15 method.

| Bucket | Lines | Weight in sleeve | Share of sleeve price loss (weight × Δprice) | Share of yield change | Avg Δprice |
|---|---|---|---|---|---|
| (i) AI builders: CoreWeave ×4, Edged Compute | 5 | 12.7% | **16.6%** | 15.0% | −4.35% |
| (ii) software / AI-disruption, core list | 7 | 7.6% | **5.5%** | 5.2% | −2.41% |
| (ii) broad list (adds IT services, Getty, Xerox and similar) | 11 | 9.5% | 8.0% | 7.0% | −2.78% |
| (iii) everything else | 89 | 79.7% | **77.9%** | 79.8% | −3.26% |

Cross-checks:
- Ending at the 10/21 file instead gives AI 21.4%, software 10.0% and other 68.6%.
- A wider ≥10% sleeve (164 lines) gives AI 18.3%, software 6.1% and other 75.7%.
- **The largest single contributors:** JetBlue (−36.9% price, 23% of the loss), FMC (−62.7%, 16%), Connect Holding II/Brightspeed (−19.4%, 13%), CoreWeave (−4.1%, 13%), Liberty Puerto Rico (LCPR) (−23.4%, 11%), Altice Financing (−16.4%, 11%), and Virgin Media Finance (−37.9%, 7%).

[PRIMARY-derived: iShares HYG holdings, 10/13 file (LIQUID's committed `research/2026-10-14_credit-funding-refresh/hyg-download.xls.gz`) and the 10/22 `latest-holdings.csv` pulled by DEWEY 15:01 ET; 1,328 of 1,332 bonds matched on (name, maturity, coupon).]

**(b) Composition of the CCC index (weights, not moves).** Bloomberg US HY index, Caa weights as of 10/9/2026: CCC = **8.58%** of HY. Its top 10 sectors are Pharma 0.64, Media Entertainment 0.57, Wirelines 0.52, Cable Satellite 0.51, Healthcare Services 0.50, P&C insurance 0.50, Wireless 0.45, Packaging 0.43, Consumer Cyclical Services 0.42, **Software 0.40**, and the rest 3.64. Software is therefore **about 4.7% of the CCC tier**. Janus: "Cable Satellite CCC sector and the Wirelines CCC sector … are responsible for much of the spread widening within CCC". [INSTITUTIONAL: Janus Henderson, Bradford Smith, 2026-10-15, https://www.janushenderson.com/en-lu/investor/article/looking-under-the-hood-differentiating-between-ccc-high-yield-bonds/ ; quotes and table text-checked by DEWEY.] This is the Bloomberg index, not the ICE index behind FRED BAMLH0A3HYC.

**Caveats that matter:**
- **The window covers less than half of October.** The holdings files start 10/13, when CCC OAS was 12.67%. They capture 73bp of October's 161bp CCC widening (11.79% → 13.40%). The 9/30 → 10/13 leg (+88bp) is decomposed only by Janus's sector read: cable and wirelines led.
- **Yield ≥12% is not a rating.** CoreWeave sits in the sleeve on yield. Its agency rating was not checked in this run, and if it is rated above CCC, the AI share of the true CCC tier is lower.
- The software list is a DEWEY name classification of HYG "Other" sector names, with the regex in References. ICE/iBoxx "Technology" does not equal AI.

## (2) Three-way split: leveraged loans below 80

| Bucket | Share of loans ≤80c | $ | Source |
|---|---|---|---|
| (i) AI builders | **not identified** in any distressed-loan list found | — | absence of evidence only |
| (ii) "technology" (JPM label; named contributors CDK Global, Qlik, Quest Software, all PE-owned software) | **39%** | **$54.4B** | [NEWS: JPM strategists incl. Nelson Jantzen, note of 2026-10-06, via Bloomberg; reprinted by The Edge Malaysia 10/7, https://theedgemalaysia.com/node/820835, text-checked by DEWEY; Bloomberg teaser https://news.bgov.com/bankruptcy-law/deeply-distressed-us-loans-rise-to-highest-level-since-pandemic] |
| (iii) everything else | ~61% | ~$85.4B (derived) | other JPM sector shares are not public |
| **Total ≤80c** | 100% | **$139.8B** (+~90% y/y, $4B below the May 2020 high); 141 issuers (+35 y/y); ≤60c: $65B | same |

**Size vs over-representation.**
- Software is ">10%" of the Morningstar LSTA loan index [INSTITUTIONAL: PIMCO, Karoui, 2026-10-19, https://www.pimco.com/us/en/insights/the-credit-market-lens-improved-optics-but-unchanged-economics-in-software-loans], or 13% in a February secondary [UNVERIFIED: SaaStr ~2/19/2026].
- 39% against about 10–13% is about **3× over-representation**. JPM's "technology" bucket is wider than software, so the multiple is approximate.
- The Deep News reprint describes the 39% as a share of the ≤60 bucket. That is arithmetically impossible ($54.4B would be 84% of $65B), so it is treated as a translation error.

**Not a fresh October software leg:** PIMCO shows the average software loan price at about 88, against about 96 for non-software, on 10/14. The gap was about 10 points in June.

## (3) Who holds bucket (ii): listed BDCs (each BDC's own industry labels, at fair value)
All figures are from the **6/30/2026** filings (Q2 10-Qs; PSEC's FY 10-K). **No Q3 (9/30) reports are filed yet.** ARCC and peers report late October to early November, so this table goes stale within about two weeks.

| BDC | Filing (filed) | Total portfolio fair value | Software label(s): % of portfolio fair value | Software $ | Prior period | Adjacent labels, not summed |
|---|---|---|---|---|---|---|
| **ARCC** | 10-Q (7/29) | $29.35B | "Software and Services" **22.0%** | ≈$6.46B (derived) | 23.8% (12/25) | — ; non-accrual 2.4% cost / 1.4% FV |
| **BXSL** | 10-Q (8/6) | $13.36B | "Software" **18.9%** | ≈$2.53B (derived) | 20.5% | Professional Services 10.3% |
| **FSK** | 10-Q (8/6) | $11.42B | "Software & Services" **17.7%** | $2.02B | 16.4% | COPJV joint venture 14.4% (not looked through) |
| **GBDC** | 10-Q (8/3; FY Sep) | ~$8.2B | "Software" **26.0%** | $2.14B | 27.2% (9/25) | IT Services 3.5% |
| **OBDC** | 10-Q (8/5) | $14.96B | "Internet software and services" **11.6%** | ≈$1.73B (derived) | 11.1% | Healthcare technology 5.8% |
| **HTGC** | 10-Q (7/30) | $4.58B | "Application Software" 24.6% + "System Software" 8.2% = **32.8%** (two labels summed) | $1.50B | 34.9% | Venture lender; different risk profile |
| **GSBD** | 10-Q (8/6) | $3.20B | "Software" **19.6%** (46.0% of NAV) | ≈$0.63B (derived) | 17.6% | Health Care Technology 8.6% |
| **OCSL** | 10-Q (8/5; FY Sep) | $2.75B | "Application Software" **17.38%** (34.5% of NAV) | $0.48B | 18.34% (9/25) | — |
| **NMFC** | 10-Q (8/3) | $2.29B | "Software" **16.52%** | ≈$0.38B (derived) | 19.22% | Business Services 20.69% |
| **MAIN** | 10-Q (8/7) | $5.75B | "Internet Software & Services" 3.0% + "Software" 2.1% = **5.1%** (LMM/Private Loan/MM table; excludes Other Portfolio) | ≈$0.29B (derived) | 5.6% | IT Services 2.4% |
| **PSEC** | 10-K FY6/26 (8/20) | ~$6.4B | "Software" **2.3%** | $0.15B | 2.6% | IT Services 0.9% |
| **TSLX** | 10-Q (8/4) | — | **no software line**: TSLX classifies "by end-market … and not by the products or services (such as software)" | — | — | the filing's own disclosure |
| **BBDC** | 10-Q (8/5) | — | **UNKNOWN**: no software row found in the parse | — | — | — |

[PRIMARY: SEC EDGAR filings, accession numbers in References; tables read by DEWEY from the filing text. "Derived" means the percentage times the total fair value stated in the same filing.] Labels differ across BDCs, so **the percentages are not like-for-like**: ARCC and FSK use broad GICS "Software & Services", while BXSL, GBDC and others use narrower "Software". BIZD constituent weights were not pulled (gap).

## (4) HYG and JNK: software and CCC weights
| Fund (as of) | Software / AI-disruption, core list: fund weight | In CCC-proxy / ≤80 subset | AI builders: fund weight |
|---|---|---|---|
| HYG (10/13 file) | **4.1%** (46 lines) | 0.39% of a 5.18% sleeve (YTW ≥12%) = 7.6% of the sleeve | 4.5% (22 lines, wider list) / 3.05% (REQ-002's 17-bond list, 10/22) |
| JNK (10/22) | **3.6%** | **0.02%** of a 3.38% bucket priced <80 (market value / par) = 0.6% | 3.95% (REQ-002's list); 0.15% of the <80 bucket |

[PRIMARY-derived: iShares HYG holdings; SSGA JNK daily holdings XLSX `holdings-daily-us-en-jnk.xlsx`, pulled 15:01 ET.] **Read: the HY ETFs carry little of the software bucket, and almost none of its distressed part.** That exposure sits in loans, CLOs and BDCs.

## (5) Default and distress context
| Measure | Value | Source |
|---|---|---|
| Moody's US spec-grade default rate, Aug 2026 | 5.3%; baseline 4.3% by Dec 2026 | [INSTITUTIONAL: First Trust relaying Moody's, 2026-09-17, https://www.ftportfolios.com/Blogs/InvestBlog/2026/9/17/factoid---thursday,-september-17,-2026] |
| Fitch US leveraged loan / HY default rate, Aug 2026 | 3.9% / 2.8%; loan YE forecast 4.5–5.0%; August loan defaults ~$3B, all distressed exchanges | [NEWS: Foreks wire, 2026-09-18] |
| Fitch "Market Concern Loans" | record $296.2B = 18.3% of the market; "technology led the increase" | same |
| JPM | HY bond default volume YTD exceeds loans, the first time since 2020; bond / loan default rates seen at 2.75% / 4.50% "next year" (year label conflicts between reprints) | The Edge 10/7 |
| Sector default split, Sept prints | **UNKNOWN** | — |

## (6) Counter-evidence
1. **For a software-dominated CCC tier: none found.** Janus attributes the CCC widening mainly to cable/satellite and wirelines, and the overall widening "principally" to rates/hawkish central banks. The HYG sleeve agrees.
2. **The JPM 39% is "technology", not software or AI.** About 61% (~$85B) of the below-80 pool is outside it and unattributed.
3. **Private-credit stress is broad.** MSCI: health care 7.0% of private-credit loans marked below 80 at end-2025; IT 6.1% in Q3 2025, then eased; "stress has not been limited to that sector" [INSTITUTIONAL: MSCI, Warren, 2026-07-15, https://www.msci.com/research-and-insights/quick-take/stress-in-private-credit-is-broader-than-tech].
4. **Software loan prices partly recovered** into mid-October (PIMCO). The loan-side software stress is a 2026 story, not an October shock.
5. **BDC software shares mostly fell** from December 2025 to June 2026: ARCC, BXSL, NMFC, OCSL, GBDC and MAIN were down; FSK, OBDC and GSBD were up. Part of this may be markdowns, not sales.

## (7) UNKNOWNs
1. ICE CCC & lower tier sector composition. ICE/Fidelity publish sector OAS for the whole index, not by tier.
2. Name-level drivers of CCC for 10/1 → 10/13 (+88bp).
3. JPM's non-technology sector shares of the ≤80 pool.
4. CoreWeave's agency rating, which decides whether it sits inside true CCC.
5. Q3 BDC industry tables, due late October to early November.
6. BBDC's software share; BIZD weights; BDC non-accruals by sector.
7. October HY issuance split by sector (see the companion report `output/2026-10-23_hy-issuance-window-october.md`).

## Source Quality Assessment
- BDC table: primary filings.
- HYG/JNK: primary fund files. The sleeve is a yield proxy over 45% of October.
- Janus: institutional, text-checked, Bloomberg index.
- JPM: relayed through a wire reprint, text-checked, primary note unavailable.
- No paid data. Public evidence only, per the REQ guardrail.

## References
(accessed 2026-10-23)
- **HYG:** https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf/latest-holdings.csv (10/22). 10/13, 10/14, 10/16 and 10/21 files are LIQUID's committed downloads under `AGENTS/LIQUID/research/2026-10-1{4,5,9}*` and `2026-10-22_after-close/`.
- **JNK:** https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-jnk.xlsx (10/22).
- **SEC accessions (6/30/2026 filings):** ARCC 0001628280-26-050307; BXSL 0001736035-26-000016; OBDC 0001655888-26-000056; FSK 0001628280-26-053783; MAIN 0001396440-26-000094; GBDC 0001476765-26-000048; HTGC 0001280784-26-000042; TSLX 0001193125-26-332725; OCSL 0001414932-26-000017; GSBD 0001193125-26-338331; PSEC 0001287032-26-000269; BBDC 0001379785-26-000030; NMFC 0001496099-26-000029. URLs follow `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<ticker>-20260630.htm`.
- **FRED:** BAMLH0A3HYC, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A0HYM2.
- Janus, The Edge, PIMCO, MSCI, First Trust: URLs inline.
- **Reproduce:**
  1. Parse the HYG XLS (XML spreadsheet; unescape entities) and the CSV. Match on (name with " Prvt"→" 144A", maturity, float(coupon)). Sleeve = YTW ≥ 12 in the base file. Contribution = weight × (price_end / price_base − 1).
  2. AI regex: `^(COREWEAVE|SOFTBANK|WULF COMPUTE|GALAXY HELIOS|FLASH COMPUTE|EDGED COMPUTE|CORE SCIENTIFIC|CIPHER COMPUTE|BLACK PEARL COMPUTE|APLD COMPUTECO|CSDC FINANCE|MERIDIAN ARC|ZENITH ARC|PR RNO|SV RNO)`. The ≥12% sleeve contains only CoreWeave and Edged, both in REQ-002's verified basket.
  3. Core software regex: `CLOUD SOFTWARE|NEPTUNE BIDCO|ION PLATFORM|ATHENAHEALTH|SS&C|^UKG |CORELOGIC|GEN DIGITAL|CLARIVATE|ROCKET SOFTWARE|MCAFEE|OPEN TEXT|^SABRE|GO DADDY|NCR VOYIX|TWILIO|FAIR ISAAC|CDK STEERCO` (plus absent names).
  4. BDC tables: `AGENTS/DEWEY/scripts/edgar_fetch.py` for the filing, then search the text for the industry-composition note.

## Process Report
**Searches run:** three Opus legs. Loans/CCC: 38 tool calls. Issuance (companion report): 57. BDC: died on an API error after downloading all 13 filings; DEWEY salvaged the downloads and read the tables itself. DEWEY ran the HYG/JNK decomposition directly and text-checked Janus and The Edge.
**Data gaps:** listed in (7).
**Source frustrations:**
- HYG/JNK holdings carry no rating column.
- Saved HYG history starts 10/13.
- Bloomberg and PitchBook are paywalled or return 403.
- The BDC leg's API timeout cost its extraction work.
- My first HYG key match failed on coupon formatting ("10" vs "10.00"): 66 of 103 lines matched, until fixed.

**Confidence in findings:** Medium overall. The bond-vs-loan divergence is consistent across four independent reads (HYG sleeve, JNK <80 bucket, Janus sector table, JPM loan figure).
**If I had more time/tools:** a 9/30 HYG file (it does not exist; nobody saved one); the ICE tier sector table; Q3 BDC filings; a CoreWeave rating check.
**Suggestions:**
- The `etf_holdings.py` build candidate (BACKLOG, past gate) would have produced the 9/30 baseline. This run is a 3rd hit.
- Re-run table (3) when Q3 10-Qs land, around 11/10.
