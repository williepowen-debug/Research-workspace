# Data-center ABS and CMBS: size, tenants and holders
**Date:** 2026-10-22 (v2 COMPLETE, ~14:30 ET; supersedes the v1 PARTIAL filed ~13:00 ET, which is in git history) | **Mode:** Thesis | **Confidence:** Size: Medium-High · Issuance 2026 YTD: Medium (mixed perimeters) · Tenant concentration: Medium (agency characterizations; no tenant named) · Holders: High for Athene and registered funds, UNKNOWN for every other insurer · Stress record: High for KBRA/DBRS-rated deals, bounded for S&P/Moody's-only deals | **Request:** REQ-DEWEY-20261022-007 (WALTER) | **Recipients:** SHADE (action); BROCK, VULCAN, CREED, LIQUID, RED, PROME (info)

## Key Finding

US data-center securitized debt outstanding is about **$58–61B** (Barclays, Jul 2026; Diamond Hill, Feb 2026). 2026 issuance is running **below** 2025. In the KBRA- and Morningstar DBRS-rated perimeter, the credit record is clean: **no downgrade, Watch Downgrade, special servicing or delinquency from 2024 to Oct 2026, and three upgrades.** One deal (Vault DI) sat on a Negative trend for two years (Jul 2022 to Jul 2024) after a tenant's insolvency and was never downgraded. The stress that exists is **market access**. The only identified AI-cloud-tenant deal, a **$301M Lambda-leased CMBS**, was still struggling to find buyers as of 21 Oct (Bloomberg). On holders:
- **Private-credit vehicles do hold weak tranches, but in small amounts.** These are subordinate classes at 0.1–2% of NAV in interval funds. One BDC family held a BB- class and has since exited.
- **The largest junior holders are ordinary bond mutual funds.**
- **Insurers are still unknown except Athene.** Athene's data-center ABS is ~$0.5B; Moody's industry estimate is $15–20B, with the perimeter unstated.

## What changed from v1 (PARTIAL)

| Section | v1 said | v2 says | Why |
|---|---|---|---|
| Stress | "None found", a bounded absence | No downgrade or special servicing across about 25 KBRA/DBRS-rated deals; **one documented Negative-trend episode (Vault DI)**; S&P/Moody's-only deals still bounded | Rating-action sweep done (Table 5a) |
| Lambda deal | Outcome unknown | **Not priced as of 21 Oct**; Morgan Stanley "struggled to attract demand"; DBRS calls Lambda "non-investment-grade" | Bloomberg via ASR, 21 Oct; DBRS, 2 Oct |
| Weak-tranche holders | "No private-credit fund or BDC found" | **Documented, small**: Barings BDCs (BB- class, exited); interval funds hold C/D/E/F classes | N-PORT sweep across 664 fund series (Table 3b) |
| Senior ratings | "Single-tenant hyperscale seniors cluster at A-/A3" | **Wrong as a general claim.** Single-tenant SASB seniors are AAA (VLT10, Lohrasp, DATA 800D, BODI); A-/A3 applies to some ABS master trusts | Presale ladders (Table 4b) |
| Elk Grove $356M | Identity unreconciled | Most likely DATA 2026-800D, **$375M** (Fitch/DBRS); the $356M figure is unreconciled | ASR 28 Aug; DBRS 24 Sep 2026 |
| Non-IG share | "No published estimate" | Still no AI-cloud share; S&P-presaled ABS average **73–85% IG tenants** (CRA, Apr 2026) | Table 2c |

## Intake check

| Check | Result |
|---|---|
| Kill condition: does SHADE, BROCK, VULCAN or CREED already hold a data-center ABS/CMBS size-and-holder table? | **No.** A read-only grep of the four desks (2026-10-22) found only routed WALTER signals (SIG-W-20260915-003, SIG-W-20261008-006), CREED `KB-CREED-037` and `KB-CREED-060`, and one map row (#7) in VULCAN `reports/2026-10-21_L782_ai-infra-financing-weak-links.md`. No sized table, no holder breakdown. Run proceeds. |
| Scope split with REQ-005 | This report covers **securitized** debt (ABS, CMBS) and its holders. Hyperscaler corporate bonds and project financings belong to REQ-005 and appear here only to mark the boundary (Table 2b). |
| Prior DEWEY work | `output/2026-07-09_coreweave-neocloud-credit.md` (CoreWeave GPU loans): adjacent, not a size/holder study. |

## Evidence

### (1) Size and issuance

**Table 1a. Outstanding (figures kept separate because their perimeters differ)**

| Figure | As-of / basis | Source |
|---|---|---|
| **$61B** ABS + CMBS outstanding (from $4B in 2020) | "YTD 2026" in a 23 Jul 2026 note citing Barclays Credit Research of 9 Jun 2026; still the latest outstanding figure found | [INSTITUTIONAL: SFA Research Corner, 23 Jul 2026](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf) |
| DC ABS ≈ **12% of esoteric ABS** (3% in 2020); DC CMBS ≈ **6% of SASB CMBS** | same | same |
| Barclays projection: $180B by YE2028 | forecast | same |
| **$40.5B ABS + $18.0B CMBS** (≈ $58.5B, DEWEY arithmetic) | 28 Feb 2026 | [INSTITUTIONAL: Diamond Hill, 19 Mar 2026](https://www.diamond-hill.com/insights/a-899/articles/ais-securitized-footprint-the-rise-of-data-center-financing/) |
| ABS ≈ three-quarters of outstanding securitized balances | Q1 2026 | [PRIMARY: Morningstar DBRS, U.S. Data Center Q1 2026 Research, 27 Apr 2026](https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research) (summary page) |
| Cumulative >$50B raised since 2018; securitization backs "just under 10%" of ~42GW US capacity | 30 Jun 2025 | [INSTITUTIONAL: Morgan Stanley, 16 Jul 2025](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf) |

**Table 1b. Issuance by year (US)**

| Year | ABS | CMBS (SASB/large loan) | Total | Source |
|---|---|---|---|---|
| 2021 | $6.2B | $3.2B | $9.4B | [INSTITUTIONAL: CREFC Data Center e-Primer, 25 Feb 2026, citing J.P. Morgan](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf) |
| 2022 | $1.0B | $0.3B | $1.3B | same |
| 2023 | $5.9B | $2.7B | $8.6B | same |
| 2024 | $8.4B | $3.0B | $11.4B | same (Morgan Stanley: $11.7B) |
| 2025 | ~$15B (Barclays **$15.5B**) | ~$11B | **~$26B** (CREFC "preliminary") | CREFC e-Primer; Barclays via [NEWS: The Real Deal/Yahoo, 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html) |
| 2026 Q1 | ABS-led | QTS SASB $2.05B | **$9.51B** | [PRIMARY: Morningstar DBRS Q1 2026](https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research) |
| 2026 H1 SASB | — | **$4.9B, 9% of SASB** | — | [INSTITUTIONAL: CBRE North America Data Center Trends H1 2026, 27 Aug 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026) |
| 2026 YTD ABS | **$11.9B** (Barclays; cut-off unstated, ~late Sep) | — | — | [NEWS citing Barclays: Real Deal/Yahoo, 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html) |
| 2026 YTD CMBS | — | **7.7% of $85.04B SASB ≈ $6.5B** (DEWEY arithmetic) vs 10.6% of $72.92B ≈ $7.7B a year earlier | — | [PRIMARY-industry: CREFC CMBS New Issue Snapshot, data to 16 Oct 2026](https://assets.informz.net/cmbs/data/images/CREFC_CMBS_New_Issue_Snapshot_10-16-26.pdf) |
| **2026 YTD combined** | — | — | **~$18–19B**. DEWEY arithmetic: Barclays ABS (~late Sep) + CREFC SASB (16 Oct), with mismatched dates and perimeters. Excludes the October DataBank 2026-2/3/4 and Switch 2026-2/3 deals (sizes not disclosed) | derived |
| 2026 forecasts (start of year) | — | — | $30–40B gross; Morgan Stanley ~$33.5B | CREFC e-Primer |

Two cautions govern Table 1:
- **Do not add the DBRS Q1 total ($9.51B) to Barclays' YTD ABS figure.** The trackers' perimeters differ. An unsourced "$38.4B YTD through Aug 2026" figure (US + Europe) circulates. It conflicts with Barclays and is excluded ([UNVERIFIED: datacentres.com, 1 Sep 2026](https://www.datacentres.com/news/data-centre-abs-issuance-hits-38b-as-wall-street-securitizes-the-ai-lease-boom-slot1-2026-09-01)).
- **In July 2026 SEC Division of Structured Finance staff said a major subset of data-center securitizations are "not asset-backed securities."** That puts them outside Reg AB disclosure and risk retention ([NEWS: InvestmentNews, 11 Aug 2026](https://www.investmentnews.com/alternatives/sec-exemption-clears-path-for-more-data-center-asset-backed-bonds/267767)). The 29 July letter date is echoed in press but still not primary. Some trackers may now classify these notes outside "ABS".

The **2026 slowdown** is the notable size finding: ~$18–19B YTD against ~$26B for 2025. The data-center share of SASB fell from 10.6% a year earlier to 7.7% at 16 Oct. Bloomberg's narrower count is ~$17B of data-center CMBS since the start of 2025, ~8% of new CRE bond deals ([NEWS: National Mortgage News, 14 Sep 2026](https://www.nationalmortgagenews.com/articles/wall-streets-data-center-boom-is-reshaping-the-real-estate-bond-market)). Non-securitized data-center debt is much larger per deal (Project Jupiter ~$18B; Meta Louisiana ~$30B).

### (2) Tenant concentration in the largest deals

Data-center securitizations **usually do not name tenants** ([INSTITUTIONAL: Impax AM, 14 Apr 2026](https://impaxam.com/insights-and-news/blog/data-centre-securitisation-navigating-a-fast-growing-asset-class/)). No agency release read for this report names a tenant; "investment grade" is the agency's or sponsor's characterization. DEWEY infers no tenant names. A GlobalCapital subtitle mentioning "Microsoft and Meta leases" on a QTS ABS is headline-only ([UNVERIFIED](https://www.globalcapital.com/article/2g4fq8uz3bri4znvrb75s/securitization/qts-drops-10-year-bonds-from-144a-data-center-abs)).

**Table 2a. Largest deals, 2025–2026: tenant profile**

| Deal (type) | Date | Size | Tenant profile | Top tenant | IG? | WA lease term | Source |
|---|---|---|---|---|---|---|---|
| BX 2025-VOLT (SASB, floating; Blackstone/QTS) | Nov 2025 | $3.46B | 9 multi-tenant data centers + 1 hyperscale; QTS platform >1,200 customers | UNKNOWN | UNKNOWN | UNKNOWN | [PRIMARY: DBRS, 15 Dec 2025](https://dbrs.morningstar.com/research/469566); [NEWS: Commercial Observer, 10 Dec 2025](https://commercialobserver.com/2025/12/biggest-cmbs-loans-of-2025/) |
| SWCH 2025-DATA (SASB, 2-yr floating; Switch) | Feb 2025 | $2.4B | 3 Nevada campuses, "solely collateralized by co-location centers" | UNKNOWN | UNKNOWN | UNKNOWN | [PRIMARY: DBRS, 9 Feb 2026](https://dbrs.morningstar.com/research/473762) |
| BX 2026-VLT9 (SASB; QTS) | Feb 2026 | ~$2.05–2.1B | 3 QTS data centers | UNKNOWN | UNKNOWN | UNKNOWN | [PRIMARY: DBRS, 12 Feb 2026](https://dbrs.morningstar.com/research/473992) |
| BX 2025-VLT7 (SASB; QTS) | Jul 2025 | $1.5B | 2 single-tenant data centers | 100% per building | UNKNOWN | UNKNOWN | Commercial Observer |
| BX 2026-VLT10 (SASB, fixed; QTS) | Jun 2026 | $1.26B | "single hyperscale tenant", "high quality credit worthy" | 100% | Yes (KBRA view) | 20-yr lease to Jul 2045 | [PRIMARY: KBRA, 23 Jun 2026](https://www.kbra.com/publications/DFFykcyz) |
| Centersquare 2025-5/6/7 (ABS master trust) | Dec 2025 | $1.10B | 1,593 customers | 5.6%; top 20 = 39.9% | Not stated | 2.7 yrs remaining | [PRIMARY: KBRA, 17 Nov 2025](https://www.kbra.com/publications/VnNyrVVh/kbra-assigns-preliminary-ratings-to-centersquare-series-2025-5-6-7) |
| Aligned 2026 (ABS; S&P) | Jul 2026 | $1.1B | 4 data centers | UNKNOWN | **90.7% IG** | — | [NEWS relaying presale: ASR, 25 Jun 2026](https://asreport.americanbanker.com/news/aligned-data-centers-raises-1-1-billion) |
| CONE 2026-DFW3 (SASB) | May 2026 | $1.05B | 2 Allen TX data centers; 35 tenants, 99.8% leased | UNKNOWN | UNKNOWN | — | [PRIMARY: KBRA, 20 May 2026](https://www.kbra.com/publications/vmkJFPKV) |
| Flexential 2026-1/2 (ABS) | Mar 2026 | $1.4B | 2,152 customers | 8.8% | — | 2.4 yrs remaining | [PRIMARY: KBRA, 12 Mar 2026](https://www.kbra.com/publications/WDpQNshZ) |
| HYPER 2025-1 (ABS; DataBank; Moody's) | Sep 2025 | >$1B | "primarily … investment grade hyperscale tenants", ~100MW | UNKNOWN | Mostly | "long-term" | [NEWS: ASR, 11 Sep 2025](https://asreport.americanbanker.com/news/dataholdings-ready-to-sell-1-billion-in-data-center-related-abs) |
| QTS 2026 ABS (Fitch presale) | ~Jul 2026 | ~$870M | 3 IG tenants + 3 smaller carriers | **57% of critical IT load** | Mostly | ~14 yrs | [NEWS: CRE Daily, 20 Jun 2026](https://www.credaily.com/?p=219222) |
| Compass (ABS; Moody's) | Feb 2026 | $830M | "unnamed hyperscaler companies"; Phoenix + Toronto | UNKNOWN | IG | — | [NEWS (Bloomberg): ASR, 12 Feb 2026](https://asreport.americanbanker.com/articles/ai-race-mints-top-rated-hyperscaler-backed-data-center-debt) |
| Stack Infrastructure 2026-1 (ABS; Blue Owl ODIT) | Mar 2026 | $695M A-2 | Sponsor portfolio: "Hyperscale Tenant 1" **42.1%**, "Tenant 2" **17.9%** of rent | 42.1% (portfolio, not trust) | Self-described IG | — | [PRIMARY: ODIT 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/2069692/000206969226000057/osnl-20260630.htm); ODIT 10-K FY2025 |
| DataBank COLO 2026-1 (ABS) | Jan 2026 | $665M | 1,757 customers | 3.9% | Diversified | 2.0 yrs remaining | [PRIMARY: KBRA, 12 Jan 2026](https://www.kbra.com/publications/tGrWrdbr) |
| QTS ABS Phoenix 2025 (ABS; S&P) | Sep 2025 | ~$600M | single hyperscale tenant, triple-net, 4 phases | 100% | Not stated | — | [NEWS: ConnectCRE, 8 Sep 2025](https://www.connectcre.com/stories/qts-nears-closing-on-600-refi-for-phoenix-data-center/) |
| CyrusOne 2025-1 (ABS; S&P) | Feb 2025 | $575M | 98 tenants | UNKNOWN | **83.5% IG** | WA original 8.6 yrs | [NEWS: ASR, 10 Feb 2025](https://asreport.americanbanker.com/news/cyrusone-offers-575-million-in-abs-on-virginia-and-texas-data-centers) |
| ODIT CMBS facility | Jun 2026 | $559.1M | one data center; probably BODI 2026-DC1 (single hyperscale tenant), **not confirmed** | 100% | Platform "~99%" IG | — | ODIT 10-Q Q2 2026; [PRIMARY: DBRS, 30 Jun 2026](https://dbrs.morningstar.com/research/484349) |
| Lohrasp Enterprise II 2026-1 (single-asset) | Jul 2026 | $520M | single hyperscale tenant, **AA-** | 100% | Yes | 15-yr NNN to Feb 2040 | [PRIMARY: DBRS, 29 Jul 2026](https://dbrs.morningstar.com/research/486217); [NEWS: ASR, 8 Jul 2026](https://asreport.americanbanker.com/news/data-center-refinance-supports-520-million-in-cmbs) |
| DATA 2026-800D (SASB; Elk Grove IL) | Sep 2026 | **$375M** | "leading global hyperscale tenant with an investment-grade credit profile" | 100% | Yes | "lengthy" | [NEWS: ASR, 28 Aug 2026](https://asreport.americanbanker.com/news/newly-redeveloped-elk-grove-data-center-anchors-375-million-cmbs-deal); [PRIMARY: DBRS, 24 Sep 2026](https://dbrs.morningstar.com/research/489611) |
| Vantage 2025-1 (ABS; S&P) | Sep 2025 | $337M | 13 data centers (10 US, 3 Canada) | **56.4% of AABR**; top 5 = 84.8% | Top tenant **AAA** | — | [NEWS: ASR, 15 Aug 2025](https://asreport.americanbanker.com/news/vantage-data-centers-prepares-to-sell-337-million-from-data-center-leases) |
| Compass II 2025-2 (ABS) | Nov 2025 | $326M | 5 Red Oak TX buildings, "a AAA-rated tenant" | 100% | Yes (AAA) | 15-yr leases to 2040 | [PRIMARY: DBRS, 6 Nov 2025](https://dbrs.morningstar.com/research/466648) |
| **Pevco SASB, Kansas City 24MW (Primary Digital Infrastructure)** | Marketed from ~22 Sep 2026 | **$301M** | **Lambda, sole tenant** of a 2009-built facility; "multi-year agreement" | 100% | **No** (DBRS: Lambda has a "non-investment-grade credit profile") | UNKNOWN | See Table 2d |

**Table 2b. Boundary marker: AI-tenant project bonds (NOT ABS/CMBS; REQ-005 scope)**

| Instrument | Size | Tenant | Tenant IG? | Source |
|---|---|---|---|---|
| Applied Digital 9.25% Senior Secured Notes due 2030 | **~$2.5B fair value at 31 Aug 2026** | **CoreWeave** | No | [PRIMARY: APLD 10-Q, filed 7 Oct 2026, CIK 1144879](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1144879) |
| Beignet Investor LLC 6.581% due 2049 (Meta Hyperion) | $27.3B | Meta, with residual-value guarantee | Yes | CREFC e-Primer |
| High-yield data-center bonds, H1 2026 | ~$27.8B across 12 issues | Used for "projects leased to non-investment-grade tenants" | No | [INSTITUTIONAL: CBRE, 27 Aug 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026) |

**Table 2c. Investment-grade tenant share: what exists**

| Measure | Figure | Perimeter / caveat | Source |
|---|---|---|---|
| Mean "percent of investment grade tenants" in S&P presales | **84.6%** for most of the sample vs **73.4%** for one operator's deals | 54 data-center ABS issuances (S&P presales, incl. 12 peer deals from 2019). ABS only; no CMBS; basis (count or rent) not stated. Non-IG is not the same as AI-cloud | [ACADEMIC/INSTITUTIONAL: CRA Insights, Apr 2026](https://media.crai.com/wp-content/uploads/2026/04/08152509/Insights-Data-center-valuations-and-potential-disputes-April2026.pdf) (DEWEY read the PDF text) |
| Per-deal IG share | CyrusOne 2025-1 83.5%; Aligned 2026 90.7%; Blue Owl platform ~99% | presale relays | Table 2a |
| AI share of DataBank 2026-2/3/4 revenue | 9.1% of monthly recurring revenue | industry tag, not a credit grade | [PRIMARY: KBRA via BusinessWire, 9 Oct 2026](https://www.financialcontent.com/article/bizwire-2026-10-9-kbra-assigns-preliminary-ratings-to-databank-issuer-llc-and-databank-co-issuer-llc-series-2026-234) |
| Non-IG AI-cloud share of DC ABS/CMBS | **No published estimate** | Barclays/JPM/BofA/MS/Goldman research not reachable | — |

On a 9 Feb 2026 review of 13 data-center CMBS deals, DBRS said only "a handful" of the hyperscale buildings are fully let to IG tenants on long leases, and that most tenants have termination options, none exercised ([PRIMARY: DBRS, 9 Feb 2026](https://dbrs.morningstar.com/research/473762)).

**Table 2d. The Lambda deal (the only identified AI-cloud-tenant securitization)**

| Field | Finding | Source |
|---|---|---|
| Deal | "Pevco markets $301m data center CMBS at 225bp for triple-As", ~22 Sep 2026 | [NEWS, headline only: GlobalCapital](https://www.globalcapital.com/securitization/article/2gxhge1gwhoncexr3czy8/securitization/cmbs/pevco-markets-301m-data-center-cmbs-at-225bp-for-triple-as) |
| Underwriter, status | Morgan Stanley "this month has struggled to attract demand for a $301 million commercial real estate bond … tied to a data center in Kansas City." The story covers >$5B of October debt-sale postponements but does not say this deal was pulled | [NEWS (Bloomberg): ASR, 21 Oct 2026](https://asreport.americanbanker.com/articles/surging-yields-bring-biggest-spate-of-debt-sale-delays-this-year) (DEWEY read the article; it does not name Lambda) |
| Link to Lambda | Lambda release: 24MW Kansas City facility, sole tenant, "multi-year agreement", scalable past 100MW. The tie to the Pevco CMBS rests on a reporter's LinkedIn post | [PRIMARY: Lambda, 28 Oct 2025](https://lambda.ai/blog/lambda-to-build-a-100mw-ai-factory-in-kansas-city-mo); LinkedIn [UNVERIFIED] |
| Tenant credit | DBRS refers to Lambda AI's "non-investment-grade credit profile" in rating Lambda Compute I, a $1.008B GPU delayed-draw loan rated A(low). That loan's GPUs sit in Seattle, Kansas City and Dallas under take-or-pay contracts with "two highly rated contract counterparties" | [PRIMARY: DBRS, 2 Oct 2026](https://dbrs.morningstar.com/research/490455) |
| Rating agency, classes, lease term | **UNKNOWN.** Not found on KBRA or DBRS; Fitch, S&P or Moody's unconfirmed | site searches, 22 Oct 2026 |
| Spread context | AAA guidance S+225 vs CREFC floating-SASB AAA 3-month average S+159 (latest S+175, 16 Oct). A sponsor executive says "neocloud spreads reach 275–325 basis points above investment-grade benchmarks" | CREFC snapshot; [NEWS: CRE Daily via Yahoo, 29 Jul 2026](https://finance.yahoo.com/real-estate/articles/neocloud-tenants-spark-data-center-055013734.html) |

Non-IG AI-tenant exposure in securitized form is **one ~$0.3B deal that has not sold**, under 1% of a ~$58–61B market. This is illustration, not a measured share. The documented non-IG AI-tenant debt sits in project bonds (Applied Digital/CoreWeave), high-yield bonds and leveraged loans (Volta).

### (3) Holders

**Table 3a. Insurers**

| Holder | Data-center ABS/CMBS | % of invested assets | As-of | Source |
|---|---|---|---|---|
| **Athene (Apollo)** | ABS **≈ $0.5B** (1% of $54.4B ABS, derived); plus $1.4B DC commercial mortgage whole loans and ≈$0.5B via the ARI loan book. All DC assets **≈ $2.4B** | **≈ 0.6%** of $387B (DEWEY arithmetic) | 31 Dec 2025. The Q2 2026 10-Q has no "data center" text, so there is no newer figure | [PRIMARY: Athene Asset Compendium, May 2026, pp. 35–36, 48, 51–52](https://d1io3yog0oux5.cloudfront.net/_d304b27429f14a31800e4e64b4454b8c/athene/db/2271/22536/pdf/Athene+Asset+Compendium+-+May+2026.pdf); [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm) |
| Corebridge (part Blackstone-managed) | **UNKNOWN.** Private ABS $7,671M (statutory basis) lists "data center leases" as one example collateral; "substantial majority … in the most senior tranches and investment-grade" | UNKNOWN | 30 Jun 2026 | [PRIMARY: 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/1889539/000188953926000141/crbg-20260630.htm) |
| KKR / Global Atlantic | **UNKNOWN**: no data-center breakout | — | 30 Jun 2026 | [PRIMARY: KKR 10-Q](https://www.sec.gov/Archives/edgar/data/1404912/000140491226000027/kkr-20260630.htm) |
| Brookfield / American National (American Equity merged in) | **UNKNOWN** | — | FY2025; Q2 2026 | [PRIMARY: 10-Q](https://www.sec.gov/Archives/edgar/data/1039828/000103982826000016/angpd-20260630.htm) |
| F&G (Blackstone sub-advised) | **UNKNOWN** | — | FY2025 | [PRIMARY: 10-K](https://www.sec.gov/Archives/edgar/data/1934850/000193485026000026/fg-20251231.htm) |
| Blue Owl / Kuvare; Resolution Life; Everlake | **UNKNOWN**: no disclosure / no SEC filings | — | — | [PRIMARY: OWL 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1823945/000182394526000009/owl-20251231.htm) |
| US insurance industry | **~$15–20B** data-center exposure (Moody's estimate). Instrument mix (ABS, CMBS, loans, bonds, equity) **not stated**. A second-hand relay of the same work gives "about $8 billion in data center assets"; the conflict is unresolved | — | 18 Sep 2026 | [NEWS: Alternative Credit Investor, 18 Sep 2026](https://alternativecreditinvestor.com/2026/09/18/moodys-insurers-set-to-boost-private-credit-allocations/); $8B [UNVERIFIED relay of WSJ](https://throughlinesynthesis.substack.com/p/wake-up-wall-street-is-cashing-in) |
| Moody's, 21 Oct 2026 | "US life insurers face rising concentration risk from data center, hyperscaler holdings": **body unread (paywall)** | — | 21 Oct 2026 | [INSTITUTIONAL, headline: Moody's](https://www.moodys.com/research/Private-Credit-US-US-life-insurers-reported-AI-investments-are-Sector-In-Depth--PBC_1485758) |
| Denominators (no DC line) | All US insurers: ABS/other structured **$699.3B**, CMBS **$206.0B**. The 137 PE-owned insurers: ABS **$133.0B**, CMBS **$28.5B**, total invested **$704.3B** | — | YE2024 | [PRIMARY: NAIC CMB, PE-owned insurers YE2024](https://content.naic.org/sites/default/files/capital-markets-pe-owned-ye2024.pdf) |
| Regulatory | NAIC Securities Valuation Office reviewing insurers' data-center investments (tenant credit, lease exits, ratings) | — | 12 Jun 2026 | [NEWS (FT relay): Insurance Business](https://www.insurancebusinessmag.com/us/news/technology/insurers-are-funding-ai-infrastructure--naic-wants-to-know-if-the-ratings-hold-up-578762.aspx) |

Scale check (DEWEY arithmetic, illustration only): even the top of Moody's $15–20B range, if it were all securitized, would be ~2% of insurers' ABS + CMBS ($905B at YE2024). It is not known to be all securitized, and concentration in particular insurers is unknown.

**Table 3b. Registered funds and BDCs: who holds the subordinate tranches** (SEC N-PORT/N-CSR/10-Q; "*" = class inferred by CUSIP match, spot-verified)

| Holder (vehicle type) | Deal / class | Fair value | % of NAV | As-of | Source |
|---|---|---|---|---|---|
| Barings Capital Investment Corp (BDC) | Flexential 2021-1 **Class C** (KBRA BB-, per a secondary table [UNVERIFIED]) | $9.9M | 1.4% | 31 Dec 2025 | [PRIMARY: 10-K](https://www.sec.gov/Archives/edgar/data/1811972/000181197226000004/bdc-20251231.htm) |
| Barings Private Credit Corp (BDC) | same | $9.9M | 0.3% | 31 Dec 2025 | [PRIMARY: 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/1859919/000185991926000068/bdc-20260630.htm) |
| Barings BDC | same | $10.8M (was $15.3M at 31 Dec 2024) | 0.9% | 30 Jun 2025 | [PRIMARY: 10-Q Q2 2025](https://www.sec.gov/Archives/edgar/data/1379785/000137978525000035/bbdc-20250630.htm) |
| → all three Barings positions | **Exited** (absent from current schedules; consistent with the 2021 series being refinanced) | — | — | 2025–26 | same; [KBRA, 31 Mar 2026](https://www.kbra.com/publications/HxrLsNRT) |
| Fundrise Innovation Fund (listed closed-end) | SWCH 2025-DATA **E**; BX 2025-VOLT **C**; VDCM 2025-AZ **D** | $12.4M; $10.0M; $8.9M | 1.6%; 1.3%; 1.2% | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/1867090/000186709026000109/primary_doc.xml) (DEWEY re-pulled) |
| Forum Real Estate Income Fund (interval) | SWCH 2025-DATA **E*** | $10.4M | 2.1% | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/1857314/000119312526364299/primary_doc.xml) |
| AB CarVal Credit Opportunities (interval) | BX VOLT **D***; SWCH **F***, **E*** | $3.0M; $2.0M; $1.0M | 0.5%; 0.4%; 0.2% | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/2012326/000141036826085828/primary_doc.xml) |
| Capital Group KKR Multi-Sector+ / Core Plus+ (interval) | BX VOLT **C**, **D**; SWCH **E** | $1.0M; $0.5M; $0.3M | ≤0.3% | 30 Jun 2026 | [PRIMARY: N-CSRS](https://www.sec.gov/Archives/edgar/data/2040318/000119312526383142/d156081dncsrs.htm); [N-CSRS](https://www.sec.gov/Archives/edgar/data/2040315/000119312526383133/d134188dncsrs.htm) |
| Sardis Credit Opportunities (interval) | QTS Issuer ABS II 2026 **B*** | $1.0M | 4.4% (of a ~$23M fund) | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/2021225/000091047226012775/primary_doc.xml) |
| Lord Abbett Bond Debenture (open-end) | SWCH **D***; BX VOLT **D*** | $38.1M; $32.1M | 0.16%; 0.14% | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/60365/000141036826088195/primary_doc.xml) |
| Janus Henderson Multi-Sector Income (open-end) | SWCH **F**, **E**; Switch 2024-2 **C** | $24.7M; $21.6M; $10.2M | 0.3% each | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/277751/000207169126020326/primary_doc.xml) |
| DoubleLine Total Return (open-end) | QTS II 2026 **B** | $31.8M | — | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/1480207/000094040026032827/primary_doc.xml) |

**Table 3c. Private-credit loans to data-center issuers (loans, NOT tranches)**

| Holder | Borrower | Instrument | Amount | As-of | Source |
|---|---|---|---|---|---|
| Ares Capital (BDC) | Retained Vantage Data Centers Intermediate Holdco / Assets LP | "Senior subordinated loan" 9.50%, 12/2031 | $195.9M (was $40.8M at 31 Dec 2025) | 30 Jun 2026 | [PRIMARY: ARCC 10-Q](https://www.sec.gov/Archives/edgar/data/1287750/000162828026050307/arcc-20260630.htm) (DEWEY re-pulled) |
| Ares Capital | EdgeConneX MCN US Finance Co 1 | Senior subordinated loan, S+600 | $85.4M par / $83.7M FV | 30 Jun 2026 | same (DEWEY re-pulled) |
| Ares Strategic Income Fund | Retained Vantage; EdgeConneX | Senior subordinated loans | $203.5M; $94.7M FV | 30 Jun 2026 | [PRIMARY: 10-Q](https://www.sec.gov/Archives/edgar/data/1918712/000162828026054923/asif-20260630.htm) |
| CION Ares Diversified Credit (interval) | Retained Vantage | Term loans | $78.1M (1.65% NAV) | 30 Jun 2026 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/1678124/000104916926002064/primary_doc.xml) |
| Cliffwater Enhanced Lending (interval) | Retained Vantage | Labelled **"First Lien"** (Ares labels it senior subordinated; conflict unresolved) | $31.3M drawn + $118.8M undrawn | 31 Dec 2025 | [PRIMARY: N-PORT](https://www.sec.gov/Archives/edgar/data/1842754/000119312526080327/ea0276943-01_nportex.htm) |
| Blue Owl ODIT (private REIT) | Issuer/owner of Stack ABS + CMBS facility | Secured ABS+CMBS liabilities | $2,379.1M | 30 Jun 2026 | ODIT 10-Q Q2 2026 |

**N-PORT aggregate (DEWEY arithmetic).**
- Scope: 19 deal-name full-text searches of N-PORT filings dated 15 Jul–22 Oct 2026; 664 fund series; latest position per fund and CUSIP, mostly 30 Jun 2026.
- **About $8.6B** of class-identified data-center ABS/CMBS. **84% ($7.22B) is senior Class A.**
- ABS B/C/D: $570M. CMBS B/C: $400M. CMBS D/E/F: **$403M**.
- Class letter is not a rating; most class ratings were not obtained.
- Not covered: private funds, separate accounts and insurer general accounts, which do not file N-PORT. Searches were capped at 1,000 hits per term.

What Table 3 settles:
- **Private-credit vehicles hold weak tranches in documented but small positions.** The B through F classes sit at 0.1–2% of NAV (one 4.4% outlier on a $23M fund). One BDC family's BB- position has been exited, and no BDC was found holding a current subordinate DC class.
- **The larger private-credit exposure is loans to the platforms** (**~$0.69B** to Vantage- and EdgeConneX-linked borrowers. DEWEY arithmetic on fair value / drawn amounts: ARCC $279.6M + ASIF $298.2M + CION $78.1M + Cliffwater $31.3M; leg C's "about $0.6B" was low) and **sponsor equity** (Blue Owl/Stack, Blackstone/QTS). Both sit below the notes.
- **The largest identified junior holders are ordinary open-end bond funds** (Lord Abbett, Janus, DoubleLine).

### (4) Structure and ratings

**Table 4a. Structure**

| Feature | ABS | SASB CMBS | Source |
|---|---|---|---|
| Sizing | 75–80% advance rate on cash flow | 65–70% LTV; KBRA's own-value LTVs run higher (CONE DFW3 **96.1%**, VLT10 **108.4%**) | [CREFC e-Primer](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf); [KBRA, 20 May 2026](https://www.kbra.com/publications/kpctrMNd); [KBRA, 23 Jun 2026](https://www.kbra.com/publications/wpYjTCDb) |
| Maturity | Master trust; 5–10-yr ARD (anticipated repayment date), interest-only, then step-up and cash sweep; 25–30-yr legal final. A missed ARD triggers a cash sweep, not a default (DBRS on Vault DI) | Floating 2-yr + extensions (SWCH, VOLT, VLT7), or 5–10-yr fixed ARD (VLT10, CONE DFW3, DATA 800D) | Diamond Hill; [DBRS, 21 Jul 2022](https://dbrs.morningstar.com/research/400225) |
| Agency method | Moody's land value only at legal final, unrated tenants assumed B1–Caa1, ~75% renewal; Fitch ~12 months liquidity for AAA | same | CREFC e-Primer |
| Spreads | Hyperscaler DC ABS **150bp over 5-yr UST**, early Sep 2026 (+16bp YoY) | AAA DC floating SASB **~165bp** vs office 93, industrial 125 (~14 Sep 2026) | Barclays via [Real Deal/Yahoo](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html); Barclays via Bloomberg in [CRE Daily](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/) |

**Table 4b. Observed rating ladders**

| Deal | Ladder | Credit metric | Source |
|---|---|---|---|
| SWCH 2025-DATA | AAA / AA / AA(low) / A / BBB(low) / BB(low) / HRR B(high); AAA tranche $1,160M at S+150 | ~60% implied LTV (IFR arithmetic) | [PRIMARY: DBRS, 18 Feb 2025](https://dbrs.morningstar.com/research/448133) |
| BX 2025-VLT6 / VLT7 / 2026-VLT9 | AAA down to BB(low)–B(high) HRR | — | [DBRS, 6 Mar 2025](https://dbrs.morningstar.com/research/449423); [15 Jul 2025](https://dbrs.morningstar.com/research/458747); [25 Feb 2026](https://dbrs.morningstar.com/research/475086) |
| BX 2026-VLT10 (single IG tenant) | AAA / AA+ / AA- / A- / BBB- / HRR B- | KBRA LTV 108.4% | [PRIMARY: KBRA, 23 Jun 2026](https://www.kbra.com/publications/wpYjTCDb) |
| CONE 2026-DFW3 | AAA / AAA / AA- / A- / BBB- / BB / HRR BB- | KBRA LTV 96.1% | [PRIMARY: KBRA, 20 May 2026](https://www.kbra.com/publications/kpctrMNd) |
| Lohrasp II 2026-1 (single AA- tenant) | A-2-I $520M AAA | Fitch LTV 72.7%, DSCR 1.22x | ASR, 8 Jul 2026 |
| Switch ABS 2025-2 | AAA / AA(low) / A(low) / BBB(low) | LTV 51.9 / 63.2 / 73.4 / 83.7% | DBRS; ASR |
| QTS PHX 2025 (single tenant) | S&P A-(sf) | LTV 58.6% | CREFC e-Primer |
| HYPER 2025-1 | Moody's A3 | LTV 65.8% | ASR, 11 Sep 2025 |
| Vantage 2025-1; Aligned 2026; Flexential 2026; DataBank 2026-2/3/4 | Seniors A- (S&P / KBRA); Aligned B at BBB | Flexential LTV A 58.2%; DataBank A2 48.4% | ASR; [KBRA, 9 Oct 2026](https://www.kbra.com/publications/ncrLdQVH) |
| Compass $830M (Feb 2026) | ~$500M Moody's Aaa at +120; Aa3; A2 | senior LTV ~31.5% | ASR (Bloomberg) |

**v1 correction:** single-tenant hyperscale **SASB** seniors are AAA (VLT10, Lohrasp, DATA 800D, BODI). The A-/A3 senior ratings are on **ABS master trusts** (Vantage, QTS PHX, HYPER, Aligned, Flexential, DataBank), which rate the whole senior note at a single A-category level. Subordinate classes reach **BB/B** in the CMBS ladders, and that is where the interval-fund positions in Table 3b sit.

### (5) Stress events

**Table 5a. Rating actions and surveillance, KBRA and DBRS (2022 to Oct 2026)**

| Deal | Agency | Action | Date | Source |
|---|---|---|---|---|
| **Vault DI Issuer 2021** (7 colocation/enterprise DCs) | DBRS | BBB affirmed; **trend Stable → Negative**. Reasons: "the insolvency filing of an unrated, private tenant in April 2022", and "a significant portion of credit risk is deferred to the refinance period in 2026". DBRS said it was likely to downgrade if rates stayed elevated | 21 Jul 2022 | [PRIMARY: DBRS](https://dbrs.morningstar.com/research/400225) (DEWEY read) |
| Vault DI 2021 | DBRS | BBB, Negative kept; DSCR 3.22x | 21 Jul 2023 | [PRIMARY](https://dbrs.morningstar.com/research/417503) |
| Vault DI 2021 | DBRS | BBB; **Negative → Stable** | 19 Jul 2024 | [PRIMARY](https://dbrs.morningstar.com/research/436539) |
| JPMCC 2022-DATA | DBRS | **Classes E, HRR upgraded**; 30 of 32 classes across 5 deals affirmed | 20 Mar 2024 | [PRIMARY](https://dbrs.morningstar.com/research/429922) |
| 8 DC CMBS (Compass II, CONE DFW1, DATA CTR2, DC 2023-DC, BX VOLT/VLT3, JPMCC DATA) | DBRS | All 39 classes affirmed; "no loans on the servicer's watchlist or in special servicing" | 12 Mar 2025 | [PRIMARY](https://dbrs.morningstar.com/research/449784) |
| **13 DC CMBS** | DBRS | **All 74 classes confirmed**; all loans current; none in special servicing; one SWCH loan on the watchlist "for an informational reason" | 9 Feb 2026 | [PRIMARY](https://dbrs.morningstar.com/research/473762) (DEWEY read) |
| **BX 2024-VLT4** | KBRA | **Classes C, D, E, F upgraded**; LTV 104.0% → 90.0%. Initial maturity 9 Jun 2026; "the extension request was in process" | 12 Jun 2026 | [PRIMARY](https://www.kbra.com/publications/LfGpRbtt) (DEWEY read) |
| **DATA 2023-CNTR** | KBRA | **Classes B, C, D, HRR upgraded**; LTV 81.7% → 65.5% | 17 Jul 2026 | [PRIMARY](https://www.kbra.com/publications/xMgkyWKv) |
| BX 2024-VLT5; DataBank 2021–24; TierPoint; Flexential | KBRA | Affirmed (timely interest) | 2024 – Sep 2026 | [VLT5](https://www.kbra.com/publications/tRLdQDbt); [DataBank](https://www.kbra.com/publications/HnWrTWRV); [TierPoint](https://www.kbra.com/publications/VFcjrRFV); [Flexential](https://www.kbra.com/publications/HxrLsNRT) |
| Cologix 2021-1 | KBRA | Withdrawn: **repaid in full** 25 Feb 2026 | 27 Feb 2026 | [PRIMARY](https://www.kbra.com/publications/jrSbKjMy) |

**Table 5b. Other stress and market-access events**

| Event | Type | Detail | Source |
|---|---|---|---|
| Lambda-tenant Kansas City CMBS ($301M) | New-issue access | Not sold as of 21 Oct; see Table 2d | ASR/Bloomberg, 21 Oct 2026 |
| Elk Grove data-center CMBS | New-issue pricing | Priced "significantly wider than initial guidance; third such case". Most likely DATA 2026-800D ($375M); the "$356M" in press is unreconciled | [NEWS: CRE Daily, 15 Sep 2026](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/) |
| DC ABS spreads flat-to-wider while broad ABS tightened | Secondary/primary spread | "Wider spreads for certain data center-backed securities" | [NEWS citing Barclays, 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html); [INSTITUTIONAL: Bracewell, 31 Aug 2026](https://www.bracewell.com/news-events/investors-turn-selective-as-ai-debt-boom-widens-data-center-cmbs-spreads/) |
| Cyxtera rejects a Stack-owned Elk Grove lease (3.5MW) in Chapter 11 | Tenant departure | Whether this building is ABS collateral is **not established** | [NEWS: Baxtel, 2023](https://baxtel.com/news/cyxtera-decids-not-to-lease-data-center-owned-by-stack-in-elk-grove-illinois) |
| Vault DI portfolio sold to Igneo | ARD event | Sale announced 5 Feb 2026, ahead of the 2026 ARD. Treatment of the notes **not found** | [PRIMARY (sale only): CVC, 5 Feb 2026](https://www.cvc.com/media/news/2026/cvc-dif-and-northleaf-divest-us-data-center-portfolio-vault-digital-infrastructure-to-igneo-infrastructure-partners/) |
| Adjacent, **not data center:** ExteNet Issuer 2024-1/2025-1 (communications infrastructure ABS) | Default | Watch Downgrade 19 Jun 2026; missed 27 Jul interest; **D, then withdrawn**; liens "ceased to be perfected" | [PRIMARY: KBRA, 3 Aug 2026](https://www.kbra.com/publications/JDtRxScV) (DEWEY read) |
| Volta Infrastructure (~$5B) | **Unrated syndicated loan, not securitized** | S+625–650 at 95–98 OID | [INSTITUTIONAL: Octus, 16 Oct 2026](https://octus.com/resources/articles/americas-leveraged-finance-weekly-ma-volta-infrastructure/) |
| Project Jupiter (~$18B; Oracle tenant) | **Bank construction loan, not securitized** | Quoted 89–91c; the 84c figure is UNVERIFIED | [NEWS: FT via Reuters/Yahoo, 23 Sep 2026](https://finance.yahoo.com/markets/stocks/articles/oracle-project-jupiter-loans-trading-145155502.html) |

Stress verdict:
- **Documented for KBRA- and DBRS-rated data-center ABS/CMBS** (about 25 deals named above): no downgrade, Watch Downgrade, special servicing or delinquency from Mar 2024 to Oct 2026. Ratings moved only upward. One earlier Negative-trend episode (Vault DI, 2022–24) resolved without a downgrade.
- **Still a bounded absence for S&P-rated master trusts** (Vantage, Stack, Sabey, CyrusOne, Aligned, QTS PHX; S&P reportedly rates 17 DC ABS trusts) and Moody's-rated deals (HYPER, Compass): their surveillance releases were not reachable.
- **The stress is in market access and spreads, concentrated on non-IG tenants.** The deep markdowns (2–11 points) are in non-securitized loans.
- **Trepp's Aug and Sep 2026 delinquency and special-servicing reports name no data-center loan** ([Trepp, Sep 2026](https://www.trepp.com/hubfs/Trepp%20CMBS%20Special%20Servicing%20Report%20September%202026.pdf)). That is weak evidence: Trepp has no data-center property type.

## Counter-Evidence

**Against "data-center paper is a material exposure":**
- **The asset class is small:** ~$58–61B, ~12% of esoteric ABS and ~6% of SASB.
- **Holdings in the observable perimeter are 84% senior Class A.**
- **Junior positions are small** (0.1–2% of NAV), and the one BDC BB- position was exited.
- **Athene's total data-center exposure is ~0.6%** of invested assets.
- **Securitization takes out only stabilized, leased assets.** Construction and power risk stays with project and private lenders (SFA).
- **The rated record is upgrades, not downgrades**, and a missed ARD triggers a cash sweep, not a default.
- **Agency methods are conservative** (Moody's land-only terminal value; Fitch 12-month liquidity).

**Against "small and safe":**
- **"Small" is documented for one insurer only.** Moody's now flags "rising concentration risk" for life insurers (body unread), and NAIC's valuation office is reviewing data-center ratings.
- **The clean record is short.** ABS dates from 2018 and SASB from 2021, and few deals have faced an ARD or balloon refinancing under stress. Vault DI, the one deal that met a tenant insolvency plus a rate shock, went Negative, and its 2026 ARD outcome is unknown.
- **Colocation trusts carry 2.0–2.7-year remaining terms**, so they rely on renewals.
- **Most hyperscale tenants hold termination options** (DBRS, Feb 2026).
- **KBRA's own-value LTVs on recent SASB run 96–108%**, so the senior AAA rests on the lease, not on the building.
- **S&P presales average 15–27% non-IG/unrated tenants.**
- **Transparency is falling.** The SEC staff "not ABS" letter takes much DC ABS outside Reg AB disclosure.
- **The first AI-cloud-tenant deal could not find buyers**, which is evidence the market prices non-IG tenant risk. Read the other way, the market is not absorbing that risk at all yet.

## Unknowns

| Unknown | Why it matters | Follow-up that would close it |
|---|---|---|
| Data-center ABS/CMBS held by Global Atlantic, American National, Corebridge, F&G, Kuvare, Resolution, Everlake | SHADE's materiality question; Athene's "small" cannot be extended to them | Statutory Schedule D Part 1 CUSIP-match (NAIC/S&P data DEWEY lacks); the Moody's 21 Oct report body |
| What Moody's $15–20B (vs "$8B") measures | Industry denominator | Moody's report body; WSJ article |
| Lambda CMBS: agency, classes, lease term, final outcome | Only AI-cloud-tenant securitization | GlobalCapital/ASR follow-up after October |
| S&P and Moody's surveillance on master trusts | Converts the remaining bounded absence to a documented one | S&P/Moody's rating-action pages (403 to DEWEY) |
| Vault DI notes at the Igneo sale; BX 2024-VLT4 and BX 2021-VOLT extension outcomes | First ARD/maturity tests | Servicer reports; DBRS/KBRA 2026 surveillance |
| Class ratings for the subordinate classes held by funds (SWCH D/E/F, VOLT C/D, QTS B, VDCM D) | BROCK's "weak tranche" grading | Presale ladders (partly in Table 4b) mapped by CUSIP |
| Class sizes and credit enhancement for the QTS/BX SASBs and SWCH | Subordination depth | KBRA/DBRS presales (paywalled) |
| Retained Vantage loan seniority (Ares "senior subordinated" vs Cliffwater "first lien") | Where private credit sits | Credit agreement |
| Outstanding after July 2026; DataBank and Switch Oct 2026 sizes | Size freshness | Barclays/Finsight next print; KBRA new-issue reports |
| Secondary prices on outstanding DC ABS/CMBS | Pricing stress beyond new issue | TRACE (144A), BWIC data |

## Source Quality Assessment

**Strong (primary documents, read directly):**
- Stress: KBRA and DBRS releases. DEWEY read the five that carry the verdict itself.
- Holders: Athene's compendium, and N-PORT/10-Q schedules (two re-pulled by DEWEY).
- Insurer filings: these establish UNKNOWN, not small.

**Medium:**
- Size: institutional research read in full, but perimeters differ, and the 2026 YTD figure mixes tracker cut-offs.
- Tenants: agency releases plus ASR relays of presales. No tenant is named anywhere, and no presale was read in full (paywalled).

**Weak:**
- The Lambda deal: one Bloomberg-sourced article (read) plus a headline and a LinkedIn link.
- Industry insurer exposure: one press figure and a conflicting relay.

## References

All accessed 2026-10-22. Primary agency and SEC links are inline in the tables. Key sources:
- SFA Research Corner (citing Barclays), 23 Jul 2026: https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf
- Diamond Hill, 19 Mar 2026: https://www.diamond-hill.com/insights/a-899/articles/ais-securitized-footprint-the-rise-of-data-center-financing/
- Morningstar DBRS U.S. Data Center Q1 2026 Research: https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research
- Morningstar DBRS releases: 400225, 417503, 436539, 429922, 449784, 449802, 473762, 448133, 449423, 458747, 469566, 473992, 475086, 466648, 484349, 486217, 489611, 490455, 491285 at https://dbrs.morningstar.com/research/<id>
- KBRA publications: LfGpRbtt, RrWxJPRh, xMgkyWKv, tRLdQDbt, HnWrTWRV, VFcjrRFV, HxrLsNRT, jrSbKjMy, JDtRxScV, DFFykcyz, wpYjTCDb, vmkJFPKV, kpctrMNd, WDpQNshZ, tGrWrdbr, ncrLdQVH, VnNyrVVh at https://www.kbra.com/publications/<id>
- Morgan Stanley, 16 Jul 2025: https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf
- CREFC Data Center e-Primer, 25 Feb 2026: https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf
- CREFC CMBS New Issue Snapshot, 16 Oct 2026: https://assets.informz.net/cmbs/data/images/CREFC_CMBS_New_Issue_Snapshot_10-16-26.pdf
- CBRE North America Data Center Trends H1 2026: https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026
- CRA Insights, Apr 2026: https://media.crai.com/wp-content/uploads/2026/04/08152509/Insights-Data-center-valuations-and-potential-disputes-April2026.pdf
- ASR (Bloomberg), 21 Oct 2026: https://asreport.americanbanker.com/articles/surging-yields-bring-biggest-spate-of-debt-sale-delays-this-year
- Athene Asset Compendium, May 2026: https://d1io3yog0oux5.cloudfront.net/_d304b27429f14a31800e4e64b4454b8c/athene/db/2271/22536/pdf/Athene+Asset+Compendium+-+May+2026.pdf
- NAIC CMB, PE-owned insurers YE2024: https://content.naic.org/sites/default/files/capital-markets-pe-owned-ye2024.pdf
- Trepp CMBS Special Servicing Report, Sep 2026: https://www.trepp.com/hubfs/Trepp%20CMBS%20Special%20Servicing%20Report%20September%202026.pdf
- Moody's (headline, 21 Oct 2026): https://www.moodys.com/research/Private-Credit-US-US-life-insurers-reported-AI-investments-are-Sector-In-Depth--PBC_1485758
- v1 references not repeated here (InvestmentNews, Scotsman Guide, KBRA 2026 outlook, Impax, Crane Frontier, Octus, HuggingNews, Insurance Journal) are in git history of this file.
- Fleet artifacts (context, not graded): VULCAN `reports/2026-10-21_L782_ai-infra-financing-weak-links.md`; WALTER SIG-W-20261008-006, SIG-W-20261016-017, SIG-W-20261020-011; CREED `workbook/KB.tsv` KB-CREED-037.

**Reproduction recipe, N-PORT aggregate:**
1. Search EDGAR full-text (`efts.sec.gov/LATEST/search-index?q="<deal name>"&forms=NPORT-P`) for 19 deal names: Vantage Data Centers Issuer, Stack Infrastructure Issuer, DataBank Issuer, SWCH, BX 2025-VOLT, QTS 2025/2026, Compass Datacenters, Sabey, CyrusOne, Aligned, Switch ABS, Flexential, CONE, VDCM and others. Use the window 15 Jul–22 Oct 2026.
2. Parse each filing's `primary_doc.xml` `<invstOrSec>` blocks.
3. Keep the latest position per fund series and CUSIP.
4. Classify by the class letter in the title, or by CUSIP match to a labelled filing.

## Process Report

- **DEWEY verification and provenance:**
  - **v1:** two Opus legs plus a report-writer, partial because the session's shared 200-search cap ran out.
  - **v2:** three Opus legs in data-return mode, each with its own search budget (A ≤45, B ≤55, C ≤50). A used 42 searches, B used 29 and C used 15.
  - **DEWEY re-verified the load-bearing items against the primary documents:** DBRS Vault DI 2022, DBRS 9 Feb 2026, DBRS Lambda Compute I, KBRA BX 2024-VLT4, KBRA ExteNet, the ASR/Bloomberg Lambda article, the ARCC 10-Q, the Fundrise N-PORT and the CRA PDF text. All matched.
  - DEWEY wrote v2 directly.
- **Searches run:** 86 WebSearch calls across the legs, plus about 40 agency-page fetches (leg A), the DBRS search API and KBRA site search (leg B), and 1,293 EDGAR N-PORT filings parsed (leg C).
- **Data gaps:**
  - S&P, Moody's and Fitch surveillance (spglobal.com 403; Fitch blocked).
  - Every insurer except Athene.
  - The Moody's 21 Oct report body.
  - Lambda deal terms.
  - Presale class sizes and credit enhancement.
  - Tenant names: none is ever disclosed.
- **Source frustrations:** S&P 403; fitchratings.com blocked; GlobalCapital, Bloomberg and Moody's paywalled; several KBRA pages return 410; DCD 403; the CRA PDF returned an HTML bot page to curl but downloaded through WebFetch; NAIC PDFs refuse curl but work via WebFetch.
- **Confidence in findings:** stress High in the KBRA/DBRS perimeter, bounded elsewhere; weak-tranche holders Medium-High in registered funds and invisible in private funds; insurers UNKNOWN except Athene; size Medium-High.
- **If I had more time/tools:** NAIC Schedule D data (S&P Capital IQ Pro / SNL) for the CUSIP match; S&P RatingsDirect for master-trust surveillance; Bloomberg for the Lambda outcome and secondary prices.
- **Suggestions (to `scripts/BACKLOG.md`):**
  - Promote the N-PORT holder scanner (built this run; needs Will's OK).
  - Record the access routes found: DBRS research-search API, KBRA site search, ASR site search, and WebFetch for NAIC/CRA PDFs that refuse curl.
  - Make per-leg WebSearch budgets standing practice. They worked: 86 of 150 used, and no leg was starved.
