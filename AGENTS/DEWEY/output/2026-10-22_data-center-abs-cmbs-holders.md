# Data-center ABS and CMBS: size, tenants and holders
**Date:** 2026-10-22 | **Mode:** Thesis | **Status:** PARTIAL — web-search budget exhausted mid-run; presales and insurer Schedule D not read | **Confidence:** Size: Medium-High · Issuance 2026 YTD: Medium (mixed perimeters) · Tenant concentration: Low-Medium · Holders: High for Athene only, otherwise Low · Stress record: Medium (bounded absence) | **Request:** REQ-DEWEY-20261022-007 (WALTER) | **Recipients:** SHADE (action); BROCK, VULCAN, CREED, LIQUID, RED, PROME (info)

## Key Finding

US data-center securitized debt outstanding is about **$58–61B** (Barclays "YTD 2026" $61B; Diamond Hill $40.5B ABS + $18.0B CMBS at 2/28/26), roughly 12% of esoteric ABS and 6% of SASB CMBS, and 2026 issuance (~$18–19B combined YTD, DEWEY arithmetic) is running **below** 2025 (~$26B) and far below the $30–40B start-of-year forecasts. Documented large deals rest on unnamed investment-grade hyperscale tenants or diversified colocation pools; **no rated ABS/CMBS with CoreWeave, Crusoe or Nebius as tenant was found**, and the only reported non-IG AI-cloud-tenant securitization is a ~$301M Lambda-leased SASB whose outcome is unknown. On holders, **"small" is documented only for Athene** (~$0.5B data-center ABS; ~$2.4B total data-center assets, ~0.6% of $387B invested, 12/31/25); every other named PE-affiliated insurer's exposure is **UNKNOWN, not small**, and no private-credit fund or BDC was found holding data-center ABS/CMBS.

## Intake check

| Check | Result |
|---|---|
| Kill condition: does SHADE, BROCK, VULCAN or CREED already hold a data-center ABS/CMBS size-and-holder table? | **No.** Read-only grep of the four desks (2026-10-22) found only routed WALTER signals (SIG-W-20260915-003, SIG-W-20261008-006), CREED `KB-CREED-037` (source disposition on the "$17B DC CMBS / 165bp" Bloomberg channel, unresolved perimeter) and `KB-CREED-060`, and one map row (#7) in VULCAN `reports/2026-10-21_L782_ai-infra-financing-weak-links.md`. No sized table, no holder breakdown. Run proceeds. |
| Scope split with REQ-005 | This report covers **securitized** debt (ABS, CMBS) and its holders. Hyperscaler corporate bonds and project financings (Meta's Beignet/Hyperion, Applied Digital's secured notes) belong to REQ-005 and appear here only to mark the boundary (Table 2b). |
| Prior DEWEY work | `output/2026-07-09_coreweave-neocloud-credit.md` (CoreWeave GPU DDTLs) — adjacent; not a size/holder study. |

## Evidence

### (1) Size and issuance

**Table 1a — Outstanding (keep figures separate; perimeters differ)**

| Figure | As-of / basis | Source |
|---|---|---|
| **$61B** ABS + CMBS outstanding (from $4B in 2020) | "YTD 2026" in a 7/23/26 note citing Barclays Credit Research 6/9/26 | [INSTITUTIONAL: SFA Research Corner, 23 Jul 2026](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf) |
| DC ABS ≈ **12% of esoteric ABS** (3% in 2020); DC CMBS ≈ **6% of SASB CMBS** | same | same |
| Barclays projection: $180B by YE2028 (~20% of esoteric ABS, ~15% of SASB) | forecast | same |
| **$40.5B ABS + $18.0B CMBS** (sum ≈ $58.5B, DEWEY arithmetic) | 28 Feb 2026 | [INSTITUTIONAL: Diamond Hill, 19 Mar 2026](https://www.diamond-hill.com/insights/a-899/articles/ais-securitized-footprint-the-rise-of-data-center-financing/) |
| ABS ≈ three-quarters of outstanding securitized balances | Q1 2026 | [PRIMARY: Morningstar DBRS, "U.S. Data Center Q1 2026 Research", 27 Apr 2026](https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research) (summary page only) |
| Cumulative >$50B raised since 2018 (~$36B ABS, ~$17B CMBS); securitization backs "just under 10%" of ~42GW US capacity | 30 Jun 2025 | [INSTITUTIONAL: Morgan Stanley, "Bridging a $1.5tr Data Center Financing Gap", 16 Jul 2025](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf) |

**Table 1b — Issuance by year (US)**

| Year | ABS | CMBS (SASB/large loan) | Total | Source |
|---|---|---|---|---|
| 2021 | $6.2B | $3.2B | $9.4B | [INSTITUTIONAL: CREFC Data Center e-Primer, 25 Feb 2026, citing J.P. Morgan](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf) |
| 2022 | $1.0B | $0.3B | $1.3B | same |
| 2023 | $5.9B | $2.7B | $8.6B | same |
| 2024 | $8.4B | $3.0B | $11.4B | same (Morgan Stanley: $11.7B) |
| 2025 | ~$15B (Barclays **$15.5B**) | ~$11B | **~$26B** (CREFC "preliminary") | CREFC e-Primer; Barclays via [NEWS: The Real Deal/Yahoo, 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html) |
| 2026 Q1 | ABS-led | QTS SASB $2.05B | **$9.51B** | [PRIMARY: Morningstar DBRS Q1 2026](https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research) |
| 2026 YTD ABS | **$11.9B** (Barclays; cut-off unstated, ~late Sep) | — | — | [NEWS citing Barclays: Real Deal/Yahoo, 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html) |
| 2026 YTD CMBS | — | **7.7% of $85.04B SASB ≈ $6.5B** (DEWEY arithmetic) vs 10.6% of $72.92B ≈ $7.7B prior-year YTD | — | [PRIMARY-industry: CREFC CMBS New Issue Snapshot, data to 16 Oct 2026](https://assets.informz.net/cmbs/data/images/CREFC_CMBS_New_Issue_Snapshot_10-16-26.pdf) |
| 2026 to 31 Jul CMBS | — | $5.7B = 9.8% of SASB; **zero in conduit** | — | [NEWS citing Trepp: Scotsman Guide, Aug 2026](https://www.scotsmanguide.com/news/cmbs-issuance-passes-76-billion-in-the-first-seven-months-of-2026/) (summary only) |
| **2026 YTD combined** | — | — | **~$18–19B** — DEWEY arithmetic, Barclays ABS (~late Sep) + CREFC SASB (16 Oct); mismatched dates and perimeters; excludes the October DataBank 2026-2/3/4 deal (size not disclosed) | derived |
| 2026 forecasts (start of year) | — | — | $30–40B gross ("several sell-side desks"); Morgan Stanley ~$33.5B gross | CREFC e-Primer |

Two cautions govern Table 1. First, **do not add the DBRS Q1 total ($9.51B) to Barclays' YTD ABS figure**: Q1 less the QTS CMBS implies ~$7.5B Q1 ABS, which would leave only ~$4.4B for Q2–Q3 under Barclays — implausibly low given named mid-year deals (Aligned $1.1B, Compass $830M, Flexential $1.4B per an [UNVERIFIED blog, Crane Frontier, 28 Jul 2026](https://cranefrontier.substack.com/p/data-center-abs-by-the-numbers)). The trackers' perimeters differ. Second, in July 2026 SEC Division of Structured Finance staff, answering a Latham & Watkins request, said a major subset of data-center securitizations are **"not asset-backed securities"** under the Exchange Act definition, putting them outside Reg AB disclosure and risk-retention rules; SASB CMBS is unaffected ([NEWS: InvestmentNews, 11 Aug 2026](https://www.investmentnews.com/alternatives/sec-exemption-clears-path-for-more-data-center-asset-backed-bonds/267767); the 29 July letter date is UNVERIFIED). After July, some trackers may classify these notes outside "ABS," which further weakens year-on-year comparison.

The **2026 slowdown** is the notable size finding: ~$18–19B YTD against ~$26B for 2025, with the data-center share of SASB falling from 10.6% (prior-year YTD) to 9.8% (31 Jul) to 7.7% (16 Oct). This contradicts the "record year" framing InvestmentNews relayed from Bloomberg data in August. For context, non-securitized data-center debt is much larger per deal (Project Jupiter ~$18B; Meta Louisiana ~$30B), and Morgan Stanley sizes private credit at $800B through 2028 against $150B for ABS/CMBS ([Morgan Stanley, Jul 2025](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf)).

### (2) Tenant concentration in the largest deals

Data-center securitizations usually **do not name tenants**: "tenant identities are typically not disclosed" ([INSTITUTIONAL: Impax AM, 14 Apr 2026](https://impaxam.com/insights-and-news/blog/data-centre-securitisation-navigating-a-fast-growing-asset-class/)). "Investment-grade tenant" is therefore usually the rating agency's or sponsor's characterization, not something an investor can verify from public text.

**Table 2a — Largest documented or reported deals, 2025–2026**

| Deal (type) | Date | Size | Tenant profile | Tenant IG? | Non-IG AI-cloud tenant? | Status / source |
|---|---|---|---|---|---|---|
| BX 2025-VOLT (SASB, floating; Blackstone/QTS) | Nov 2025 | $3.46B | ~10 QTS data centers; tenants not obtained | UNKNOWN | Not documented | Documented deal; tenants unread — [CREFC e-Primer](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf) |
| SWCH 2025-DATA (SASB; Switch) | Feb 2025 | $2.4B | 3 Nevada campuses; tenant mix not obtained | UNKNOWN | Not documented | CREFC e-Primer |
| Centersquare 2025-5/6/7 (ABS master trust) | Dec 2025 | $1.10B | **1,593 customers; largest 5.6%; top 20 = 39.9%**; WA remaining contract term **2.7 yrs** | Not stated (colocation) | No | [PRIMARY: KBRA, 17 Nov 2025](https://www.kbra.com/publications/VnNyrVVh/kbra-assigns-preliminary-ratings-to-centersquare-series-2025-5-6-7); size from Csquare 10-Q Q2 2026 (SEC CIK 2105398) |
| CONE 2026-DFW3 (SASB) | 2026 (date unconfirmed) | $1.05B | Two Allen TX data centers; KBRA LTV 96.1% on KBRA value | UNKNOWN | Not documented | [NEWS: Traders Union](https://tradersunion.com/news/financial-news/show/2092123-kbra-rates-texas-data-center-cmbs/) |
| Stack Infrastructure Issuer 2026-1 (ABS; Blue Owl ODIT) | Mar 2026 | $695M A-2 | Sponsor portfolio: "Hyperscale Tenant 1" **42.1%**, "Tenant 2" **17.9%** of rent; "predominately investment-grade and hyperscale" | Self-described IG | Not disclosed | [PRIMARY: ODIT 10-K FY2025, CIK 2069692](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=2069692) — ⚠️ portfolio-level, not trust-level |
| DataBank COLO 2026-1 (ABS) | Jan 2026 | $665M | ~1,750 colocation tenants | Diversified | No | CREFC e-Primer |
| DataBank 2026-2/3/4 (ABS) | Prelim. 9 Oct 2026 | Not disclosed | 1,851 customers; largest 3.6%; top 20 = 37.0%; **AI = 9.1% of AMRR**; WA remaining term 2.6 yrs | Diversified | No | [PRIMARY: KBRA via BusinessWire, 9 Oct 2026](https://www.financialcontent.com/article/bizwire-2026-10-9-kbra-assigns-preliminary-ratings-to-databank-issuer-llc-and-databank-co-issuer-llc-series-2026-234) |
| QTS Issuer ABS II 2025-1 (Phoenix) | Sep 2025 | ~$600M | **Single hyperscale tenant**, triple-net, ~36MW | Assumed, not stated | No | CREFC e-Primer |
| ODIT data-center CMBS facility | Jun 2026 | $559.1M | One data center; tenant not named | UNKNOWN | Not disclosed | PRIMARY: ODIT 10-Q Q2 2026 |
| Lohrasp Enterprise II 2026-1 (single-asset notes) | Jul 2026 | $520M | **Single hyperscale tenant, AA-** (unnamed), 15-yr NNN lease to Feb 2040 | Yes | No | [NEWS: Asset Securitization Report, 8 Jul 2026](https://asreport.americanbanker.com/news/data-center-refinance-supports-520-million-in-cmbs) |
| Unnamed 7-property CMBS (Fitch presale) | ~Oct 2026 | UNKNOWN | **Four confidential IG tenants**; WALRT 12.9 yrs | Yes | No | [UNVERIFIED: presale text via X post, relayed in WALTER SIG-W-20261008-006] |
| **Pevco/Numerios SASB, Kansas City ~24MW** | Marketed ~22 Sep 2026 | **~$301M** | **Lambda, sole tenant** (AI cloud, unrated) | **No** | **YES** | **REPORTED-not-documented** — [GlobalCapital headline](https://www.globalcapital.com/securitization/article/2gxhge1gwhoncexr3czy8/securitization/cmbs/pevco-markets-301m-data-center-cmbs-at-225bp-for-triple-as) (body unread); reporter LinkedIn posts [UNVERIFIED]; agency, class sizes and outcome UNKNOWN |
| Elk Grove (IL) data-center CMBS | ~Sep 2026 | $356M | UNKNOWN | UNKNOWN | UNKNOWN | [NEWS: CRE Daily relaying Bloomberg, 15 Sep 2026](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/); identity unreconciled with a $375M "DATA 2026-800D" in CREED's relay — UNVERIFIED |

**Table 2b — Boundary marker: AI-tenant project bonds (NOT ABS/CMBS; REQ-005 scope)**

| Instrument | Size | Tenant | Tenant IG? | Source |
|---|---|---|---|---|
| Applied Digital 9.25% Senior Secured Notes due 2030 (Polaris Forge 1, Ellendale ND) | **~$2.5B fair value at 31 Aug 2026** | **CoreWeave** (warrants issued "in connection with certain data center leases with CoreWeave") | **No** | [PRIMARY: APLD 10-Q, period ended 31 Aug 2026, filed 7 Oct 2026, CIK 1144879](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1144879) |
| Beignet Investor LLC 6.581% due 2049 (Meta Hyperion) | $27.3B | Meta, with residual-value guarantee | Yes | CREFC e-Primer; ~91c on 7 Oct 2026 per WALTER SIG-W-20261008-024 relay [UNVERIFIED] |

The tenant picture splits in two. Hyperscale deals are concentrated (one tenant, or a sponsor portfolio where one unnamed hyperscaler pays 42% of rent) but carry long IG leases. Colocation trusts are granular (largest customer 3.6–5.6%) but on short contracts (2.6–2.7 years WA remaining), so their risk is re-leasing, not tenant credit. Lease demand behind both is itself concentrated: in 2025 through October the top five hyperscalers (AWS, Microsoft, Google, Meta, Oracle; rated BBB+ to AAA) took **73%** of MW leased ([CREFC e-Primer](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf), "Source: Various").

**The non-IG AI-cloud share of data-center securitized debt has no published estimate.** As an illustration only — not a measured share — the Lambda deal alone (~$0.3B) would be **under 1%** of a ~$58–61B market. That figure rests on an incomplete deal census with no presales read. The documented non-IG AI-tenant risk sits instead in **project bonds** (Applied Digital's CoreWeave-leased notes, ~$2.5B) and in leveraged and private loans (Volta, below).

### (3) Holders

**Table 3 — Holder evidence**

| Holder (type) | Instrument | Amount | As-of | Source |
|---|---|---|---|---|
| **Athene (Apollo)** — PE-affiliated life insurer | Data-center ABS | **1% of $54.4B ABS ≈ $0.5B** (derived); ABS book 97.6% IG, WA credit enhancement 23% | 31 Dec 2025 | [PRIMARY: Athene Asset Portfolio Compendium, May 2026, pp. 35–36](https://d1io3yog0oux5.cloudfront.net/_d304b27429f14a31800e4e64b4454b8c/athene/db/2271/22536/pdf/Athene+Asset+Compendium+-+May+2026.pdf) |
| Athene | Data-center commercial mortgage whole loans (not CMBS) | **$1.4B** (3% of $42B CMLs) | 31 Dec 2025 | same, p. 48 |
| Athene | ARI CML book bought from Apollo's REIT (closed 24 Apr 2026) | data centers 6% of ~$9B ≈ **$0.5B** (derived) | portfolio at 31 Dec 2025 | same, pp. 51–52 |
| Athene, total | All data-center assets ≈ **$2.4B ≈ 0.6% of $387B** gross invested assets | DEWEY arithmetic | 31 Dec 2025 | derived from same |
| KKR/Global Atlantic; Brookfield/American Equity; Blackstone-affiliated insurer mandates; Blue Owl/Kuvare | Any data-center ABS/CMBS | **UNKNOWN** | — | No disclosure found; investor decks not retrievable |
| US life insurers, industry | Data-center ABS/CMBS (Schedule D) | **UNKNOWN** | — | NAIC index pages refused; NAIC YE2024 CRE report has no data-center breakout ([PRIMARY: NAIC CMB](https://content.naic.org/sites/default/files/capital-markets-special-reports-cml-cre-ye2024.pdf)) |
| Blue Owl ODIT (private REIT) | **Issuer/owner** of Stack ABS + CMBS facility; also holds CMBS (collateral unstated) | Secured ABS+CMBS liabilities **$2,379.1M**; CMBS held **$153.0M** FV | 30 Jun 2026 | [PRIMARY: ODIT 10-Q Q2 2026, CIK 2069692](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=2069692) |
| Blue Owl "Other Accounts" | One account's digital-infrastructure investments "must be leased to non-investment-grade tenants" | UNKNOWN | FY2025 | PRIMARY: ODIT 10-K FY2025 |
| State Street IG Public & Private ABS ETF; Short Duration IG Public & Private Credit ETF | Lohrasp Enterprise II 5.51% 2056 | $220k par (0.88% NAV); $660k (1.08%) | 31 Jul 2026 | [PRIMARY: SSGA Active Trust N-PORT, CIK 1516212](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1516212) |
| Registered funds (DoubleLine, Sterling, American Beacon, Vanguard Wellesley/Wellington, Forum, RiverPark, Fundrise) | Vantage, QTS ABS; SWCH CMBS | Amounts not extracted | 2025–2026 | PRIMARY: EDGAR full-text hits only |
| Carlyle Tactical Private Credit Fund | CoreWeave GPU DDTLs (not DC ABS) | ≥5 rows of $0.6–3.8M FV | 30 Jun 2026 | [PRIMARY: N-CSRS, CIK 1725472](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1725472) |
| BDCs (Great Elm; Trinity, Eagle Point Trinity, LAGO, Monroe Income Plus) | **Loans** to CoreWeave and Crusoe — not ABS/CMBS | Not extracted | 2024–2026 | PRIMARY: EDGAR full-text hits. **No BDC filing found holding a DC ABS/CMBS bond** |
| Investor base by structure | ABS → esoteric-ABS specialists; CMBS → SASB/CRE investors | — | Feb 2026 | CREFC e-Primer |

Boundary entries (REQ-005 scope): Beignet appears in insurer-affiliated variable trusts (Northwestern Mutual Series Fund, $384,598, 0.32% of NAV, 30 Jun 2026; Brighthouse, PIMCO VIT, Columbia VIT and others, amounts not extracted) — these are separate-account funds, not general accounts.

Three readings follow from Table 3. Athene, the one PE-affiliated insurer with a data-center line, shows **small** exposure, and most of it is whole loans rather than securitized paper. Registered funds hold data-center ABS in small positions (0.3–1.1% of NAV in the three measured), consistent with a broad IG investor base, though the sample is tiny. Private-credit firms appear mainly as **owners and sponsors** (Blue Owl/Stack, Blackstone/QTS), whose exposure is equity-like and sits below the notes, not as holders of weak tranches. AM Best warned on 15 Jun 2026 that insurers' asset-side data-center exposure "has not yet fully priced" ([NEWS: Insurance Journal, 16 Jun 2026](https://www.insurancejournal.com/news/national/2026/06/16/873909.htm); report unread), and a Moody's headline dated 21 Oct 2026 reads "US life insurers face rising concentration risk from data center, hyperscaler holdings" ([Moody's data-center hub](https://www.moodys.com/web/en/us/insights/credit-risk/data-centers.html); body unread). Neither quantifies securitized holdings.

### (4) Structure and ratings

**Table 4 — Structure and observed ratings**

| Feature | ABS | SASB CMBS | Source |
|---|---|---|---|
| Sizing | 75–80% advance rate on cash flow | 65–70% LTV | [CREFC e-Primer](https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf) |
| Maturity | Master trust; 5–10-yr ARD, IO before ARD, step-up + hyper-amortization after; 25–30-yr legal final | Often floating, 2-yr initial + extensions, or ~5-yr hard maturity; balloon | [Diamond Hill](https://www.diamond-hill.com/insights/a-899/articles/ais-securitized-footprint-the-rise-of-data-center-financing/); [SFA](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf) |
| Single-tenant hyperscale seniors | **QTS PHX 2025-1: S&P A-(sf)**, LTV 58.6%; **HYPER 2025-1: Moody's (P)A3(sf)**, DSCR 1.32x, LTV 65.8% | — | CREFC e-Primer (citing presales) |
| Diversified/IG-pool seniors | DataBank COLO 2026-1 A-2: (P)A3, LTV ~48–50%; Compass: AAA/AA [UNVERIFIED] | Lohrasp A-2-I: AAA (DBRS, S&P) | CREFC; ASR; Crane Frontier |
| Agency method | Moody's (Feb 2025): land value only at legal final, unrated tenants assumed B1–Caa1, ~75% renewal; KBRA (Jan 2026); Fitch ~12 months liquidity for AAA; S&P; DBRS unified ABS/CMBS | same | CREFC e-Primer |
| Spreads | Hyperscaler DC ABS **150bp over 5-yr UST** early Sep 2026 (+16bp YoY) | AAA DC floating SASB **~165bp** vs office 93, industrial 125 (~14 Sep 2026) | Barclays via [Real Deal/Yahoo](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html); Barclays via Bloomberg relayed by [CRE Daily](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/) |

**Senior ratings are not uniformly AAA**: single-tenant hyperscale ABS seniors cluster at **A-/A3**, while AAA/AA appears on diversified or IG-pool deals and single-asset notes with long IG leases. No source gave a market-wide rating distribution or subordination by class.

### (5) Stress events

**Table 5 — Stress record to 22 Oct 2026**

| Event | Instrument type | Detail | Status / source |
|---|---|---|---|
| Rating downgrade, watch, special servicing, delinquency or loss on any US DC ABS/CMBS | ABS/CMBS | **None found** | Bounded absence — rating-action sweep not done. Trepp Sep 2026 special-servicing report names no data-center loan ([PRIMARY-industry: Trepp](https://www.trepp.com/hubfs/Trepp%20CMBS%20Special%20Servicing%20Report%20September%202026.pdf)); KBRA expects to **affirm** DataBank 2021-1/2023-1/2024-1/2026-1 (9 Oct 2026); CREED relay 26 Sep 2026 found none |
| Lambda-tenant Kansas City SASB | CMBS | ~$301M; AAA guided **SOFR+225** on 22 Sep 2026, ~50–65bp wide of CREFC floating SASB AAA (3-mo avg S+159, latest S+175, 16 Oct); later Bloomberg clip reports **weak demand** | **Outcome UNKNOWN** (priced, resized or pulled) — GlobalCapital headline; [CREFC snapshot](https://assets.informz.net/cmbs/data/images/CREFC_CMBS_New_Issue_Snapshot_10-16-26.pdf) |
| Elk Grove $356M | CMBS | Priced wide of initial guidance, "third such case" | [NEWS: CRE Daily, 15 Sep 2026](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/); identity UNVERIFIED |
| DC ABS spreads flat-to-wider while broad ABS tightened | ABS | Trading closer to hyperscaler corporate debt | [NEWS citing Barclays (Lipchak), 30 Sep 2026](https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html) |
| Volta Infrastructure | **Leveraged loan — not ABS/CMBS** | ~$5B ($1.3B TLC + $3.712B GPU TL), **S+650 / 95 OID**, a day past its 14 Oct deadline | [INSTITUTIONAL: Octus, 16 Oct 2026](https://octus.com/resources/articles/americas-leveraged-finance-weekly-ma-volta-infrastructure/) |
| Project Jupiter (NM; Oracle tenant) | **Bank construction loan — not ABS/CMBS** | ~$18B quoted **89–91c** | [NEWS: FT via Reuters, relayed Yahoo, 23 Sep 2026](https://finance.yahoo.com/markets/stocks/articles/oracle-project-jupiter-loans-trading-145155502.html). The **84c** figure traces only to an X post relayed by [HuggingNews](https://huggingnews.com/ai/update-oracles-18b-project-jupiter-loans-fall-to-84-cents-on-the-dollar-c71b22c4) — **UNVERIFIED** |

Stress so far is in **pricing and market access**, concentrated on non-IG AI tenants and converted collateral, not in credit performance. The deep markdowns (5–11 points) are in non-securitized loans.

## Counter-Evidence

**Against "data-center paper is a material exposure":** the asset class is small — ~$58–61B outstanding, ~12% of esoteric ABS and ~6% of SASB (Barclays via [SFA](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf)), ~4% of 2025 US ABS issuance (DEWEY arithmetic from Barclays $15.5B and a total backed out of [KBRA's 2026 outlook](https://www.kbra.com/publications/FNXsxrbn/kbra-releases-research-2026-u-s-abs-sector-outlook-growing-issuance-amid-diverging-sector-trends?format=web)). Securitization takes out only stabilized, leased assets; construction and power risk stays with project and private lenders ([SFA](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf)). Agency methods are conservative (Moody's land-only terminal value; Fitch 12-month liquidity). Morgan Stanley's Katy Huberty called DC ABS "notably more resilient" than corporate credit in August ([InvestmentNews](https://www.investmentnews.com/alternatives/sec-exemption-clears-path-for-more-data-center-asset-backed-bonds/267767)), though that predates September–October widening. Securitized CRE spreads overall had not followed HY wider through 16 Oct.

**Against "small and safe":** "small" is documented for one insurer only. The clean credit record is **weak evidence** — ABS dates from 2018 and SASB CMBS from 2021, and few deals have faced an ARD or balloon refinancing under stress. Colocation trusts rely on renewal assumptions (2.6–2.7-yr WA remaining terms). Single-tenant hyperscale income is "binary" (CREFC). Collateral quality is drifting: an under-construction asset entered CMBS (GSMS 2025-800D, per [Morgan Stanley](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf)), investors flag "asset-quality creep as master trusts expand" (CREFC), and KBRA put CONE 2026-DFW3's LTV at 96.1% on its own value. Market participants cite obsolescence and "longer-term mark-to-market risk" (Citi, Trepp, Axonic via [CRE Daily](https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/)). The July SEC staff letter takes much DC ABS outside Reg AB disclosure, so transparency may fall as volume grows.

## Unknowns

| Unknown | Why it matters | Follow-up that would close it |
|---|---|---|
| Data-center ABS/CMBS held by KKR/Global Atlantic, Brookfield/American Equity, Blackstone-affiliated mandates, Blue Owl/Kuvare | SHADE's materiality question; "small" cannot be extended from Athene | Statutory Schedule D Part 1 (CUSIP-match to Vantage, Stack, QTS, DataBank, Centersquare, SWCH, BX VOLT, Lohrasp, Switch); investor-day decks |
| Industry-wide insurer holdings | Concentration check | NAIC Capital Markets Bureau special report (if any); Moody's 21 Oct 2026 life-insurer report body |
| Non-IG-tenant share of DC ABS/CMBS | VULCAN's L782 check | Barclays/JPM/BofA/MS DC securitization research; presale tenant sections for top-20 deals |
| Tenant names/ratings for BX VOLT, SWCH, Vantage, QTS, HYPER | Concentration table is mostly descriptive | Read KBRA/S&P/Fitch/DBRS/Moody's presales |
| Lambda SASB outcome, agency, classes | Only reported non-IG AI-tenant securitization | GlobalCapital/Bloomberg/ASR follow-up; KBRA/Fitch new-issue reports |
| Who holds subordinate/BBB/BB classes | BROCK's weak-tranche question | Presale class tables + N-PORT/N-CSR searches by CUSIP; private-credit fund holdings are not public |
| Rating actions 2018–2026 | Bounds the "no stress" claim | Sweep of agency press releases for downgrade/watch on DC ABS/CMBS |
| Current outstanding after July 2026; DataBank Oct 2026 deal size | Size freshness | Finsight/Green Street/KBRA sector tables; closing 8-K or KBRA new-issue report |
| Secondary prices on outstanding DC ABS/CMBS | Pricing stress beyond new issue | TRACE (144A ABS), BWIC data |

## Source Quality Assessment

Size and issuance rest on institutional research read in full (SFA/Barclays, CREFC e-Primer, Morgan Stanley) plus primary industry data (CREFC snapshot, DBRS summary) — good for orders of magnitude, weak for exact perimeter, and 2026 YTD mixes tracker cut-offs. Tenant concentration rests on one primary KBRA release, two SEC filers (Csquare, ODIT) and secondary deal profiles; no presale was read, so most tenant cells are descriptive. Holder evidence is strong for Athene (primary compendium) and N-PORT samples, and absent for every other insurer. The Lambda deal and Elk Grove items are relay-grade. Stress-absence is bounded by an unfinished rating-action sweep.

## References

All accessed 2026-10-22 unless noted.
- SFA Research Corner (citing Barclays), 23 Jul 2026 — https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf
- Diamond Hill, 19 Mar 2026 — https://www.diamond-hill.com/insights/a-899/articles/ais-securitized-footprint-the-rise-of-data-center-financing/
- Morningstar DBRS, U.S. Data Center Q1 2026 Research, 27 Apr 2026 — https://dbrs.morningstar.com/insights/commentary/479757/us-data-center-q1-2026-research
- Morgan Stanley Research, 16 Jul 2025 — https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf
- CREFC Data Center e-Primer, 25 Feb 2026 — https://www.crefc.org/common/Uploaded%20files/Learn/DataCenters-eprimer-2026.02.25.pdf
- CREFC CMBS New Issue Snapshot, data to 16 Oct 2026 — https://assets.informz.net/cmbs/data/images/CREFC_CMBS_New_Issue_Snapshot_10-16-26.pdf
- The Real Deal via Yahoo, 30 Sep 2026 — https://finance.yahoo.com/real-estate/articles/data-center-securities-flash-warning-120000014.html
- InvestmentNews, 11 Aug 2026 — https://www.investmentnews.com/alternatives/sec-exemption-clears-path-for-more-data-center-asset-backed-bonds/267767
- Scotsman Guide (Trepp), Aug 2026 — https://www.scotsmanguide.com/news/cmbs-issuance-passes-76-billion-in-the-first-seven-months-of-2026/
- KBRA 2026 US ABS Sector Outlook, 20 Nov 2025 — https://www.kbra.com/publications/FNXsxrbn/kbra-releases-research-2026-u-s-abs-sector-outlook-growing-issuance-amid-diverging-sector-trends?format=web
- KBRA, Centersquare 2025-5/6/7, 17 Nov 2025 — https://www.kbra.com/publications/VnNyrVVh/kbra-assigns-preliminary-ratings-to-centersquare-series-2025-5-6-7
- KBRA via BusinessWire, DataBank 2026-2/3/4, 9 Oct 2026 — https://www.financialcontent.com/article/bizwire-2026-10-9-kbra-assigns-preliminary-ratings-to-databank-issuer-llc-and-databank-co-issuer-llc-series-2026-234
- Asset Securitization Report, Lohrasp, 8 Jul 2026 — https://asreport.americanbanker.com/news/data-center-refinance-supports-520-million-in-cmbs
- Traders Union, CONE 2026-DFW3 — https://tradersunion.com/news/financial-news/show/2092123-kbra-rates-texas-data-center-cmbs/
- Crane Frontier, 28 Jul 2026 (UNVERIFIED) — https://cranefrontier.substack.com/p/data-center-abs-by-the-numbers
- Impax AM, 14 Apr 2026 — https://impaxam.com/insights-and-news/blog/data-centre-securitisation-navigating-a-fast-growing-asset-class/
- GlobalCapital headline, Pevco, ~22 Sep 2026 — https://www.globalcapital.com/securitization/article/2gxhge1gwhoncexr3czy8/securitization/cmbs/pevco-markets-301m-data-center-cmbs-at-225bp-for-triple-as
- CRE Daily, 15 Sep 2026 — https://www.credaily.com/briefs/data-center-cmbs-boom-rewrites-real-estate-risk/
- Trepp CMBS Special Servicing Report, Sep 2026 — https://www.trepp.com/hubfs/Trepp%20CMBS%20Special%20Servicing%20Report%20September%202026.pdf
- Octus, Volta, 16 Oct 2026 — https://octus.com/resources/articles/americas-leveraged-finance-weekly-ma-volta-infrastructure/
- Yahoo (FT via Reuters), Project Jupiter, 23 Sep 2026 — https://finance.yahoo.com/markets/stocks/articles/oracle-project-jupiter-loans-trading-145155502.html
- HuggingNews (UNVERIFIED), Jupiter 84c — https://huggingnews.com/ai/update-oracles-18b-project-jupiter-loans-fall-to-84-cents-on-the-dollar-c71b22c4
- Athene Asset Portfolio Compendium, May 2026 — https://d1io3yog0oux5.cloudfront.net/_d304b27429f14a31800e4e64b4454b8c/athene/db/2271/22536/pdf/Athene+Asset+Compendium+-+May+2026.pdf
- NAIC CMB special report, CML/CRE YE2024 — https://content.naic.org/sites/default/files/capital-markets-special-reports-cml-cre-ye2024.pdf
- Insurance Journal (AM Best), 16 Jun 2026 — https://www.insurancejournal.com/news/national/2026/06/16/873909.htm
- Moody's data-center hub (headline 21 Oct 2026) — https://www.moodys.com/web/en/us/insights/credit-risk/data-centers.html
- SEC EDGAR filings (reproduce via company search by CIK): Csquare 10-Q Q2 2026 (CIK 2105398, acc. 0002105398-26-000004); ODIT 10-K FY2025 (CIK 2069692, acc. 0002069692-26-000016) and 10-Q Q2 2026 (acc. 0002069692-26-000057); Applied Digital 10-Q period ended 31 Aug 2026 (CIK 1144879, acc. 0001144879-26-000059); SSGA Active Trust N-PORT (CIK 1516212, acc. 0001410368-26-095862/-095864); Northwestern Mutual Series Fund N-PORT (CIK 742212, acc. 0001410368-26-083374); Carlyle Tactical Private Credit N-CSRS (CIK 1725472, acc. 0001725472-26-000005); Vantage ABS-15G (CIK 1727983, acc. 0001140361-25-039876) — https://www.sec.gov/cgi-bin/browse-edgar
- Fleet artifacts (context, not graded): VULCAN `reports/2026-10-21_L782_ai-infra-financing-weak-links.md`; WALTER SIG-W-20261008-006, SIG-W-20261008-024, SIG-W-20261016-017, SIG-W-20261020-011; CREED `workbook/KB.tsv` KB-CREED-037.

## Process Report

- **DEWEY verification and provenance:**
  - DEWEY ran the kill-condition grep itself (SHADE/BROCK/VULCAN/CREED) before launch.
  - Two Opus legs ran in data-return mode; a report-writer sub-agent drafted this report and DEWEY reviewed it before filing.
  - **Follow-up owed in a fresh session (search budget reset):**
    - A rating-action sweep for data-center ABS/CMBS since 2018.
    - Presale reads for BX 2025-VOLT, SWCH 2025-DATA, the Vantage 2025 series and QTS 2025-1/2 (tenant names and shares).
    - The outcome of the Pevco/Numerios (Lambda) SASB.
    - Insurer exposure for KKR/Global Atlantic, Brookfield/American Equity, Blackstone-affiliated insurers and Blue Owl/Kuvare.
- **Searches run:** Two research legs (size/structure/stress; tenants/holders). **The session-wide WebSearch cap (200 calls shared across all agents) ran out mid-run** — the tenants/holders leg got only 8 queries. After that, work used direct fetches of already-found URLs, PDF text extraction, and EDGAR full-text search (10-K/10-Q, N-PORT, N-CSR). Worked well: SFA, CREFC, Morgan Stanley and Athene PDFs; EDGAR full-text for fund holdings.
- **Data gaps:** **No rating-agency presale was read in full**, so most tenant names, class sizes and subordination are missing. **A rating-action sweep was not done**, so "no stress events" is a bounded absence. No insurer Schedule D; no holder data for any insurer except Athene; no published non-IG-tenant share; no post-July outstanding figure; Lambda deal outcome unknown.
- **Source frustrations:** **NAIC Capital Markets Bureau index pages returned 403** to both user agents. **Quartr returned "subscription required"** (insurer decks). GlobalCapital and Bloomberg bodies paywalled. Goldman's 19 Oct 2026 spread note (via ANI) returned 403. Trackers disagree on perimeter, worsened by the SEC staff "not ABS" letter.
- **Confidence in findings:** Size Medium-High (two independent institutional sources within 5%); 2026 YTD issuance Medium (mixed cut-offs, labelled DEWEY arithmetic); tenant concentration Low-Medium; holders High for Athene, Low elsewhere; stress Medium (bounded).
- **If I had more time/tools:** Read presales for the top 20 deals; run the rating-action sweep; pull Schedule D for the PE-affiliated life insurers and CUSIP-match; read the Moody's 21 Oct life-insurer report and the AM Best June report; extract N-PORT amounts for all DC ABS/CMBS CUSIPs.
- **Suggestions:** Add to `scripts/BACKLOG.md`: (1) an N-PORT CUSIP-holder scanner for a named deal list (EDGAR full-text hits found many funds, but amounts were extracted by hand); (2) a NAIC fetch workaround (403 on index pages); (3) a reserved per-agent WebSearch allocation so one leg cannot be starved by a shared cap.
