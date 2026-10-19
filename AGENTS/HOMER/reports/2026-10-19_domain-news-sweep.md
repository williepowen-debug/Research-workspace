# HOMER — Will-requested domain sweep, October 19, 2026

**Scope:** identify relevant evidence missing from HOMER's captured record after the morning L725 delivery. Source search began after 12:23 ET on 2026-10-19; source retrieval timestamps are saved in the manifest. Independent Will-launched Codex/OpenAI owner session, launch-selected gpt-6.1-sol; same repository/session as the morning delivery. No additional agents, trades, spending or threshold changes.

## What changes the read

**The strongest addition is pressure among loans that are still paying.** Trepp's October 16 study isolates 2021–22-securitized multifamily CRE CLO loans: a small share of the five-state book holds most delinquency, and the reporting subset of performing loans has weak cash-flow coverage. This strengthens the financing-pressure mechanism, but does not prove imminent defaults or bank losses. **The counterweight is stronger rental demand and positive rent growth.** Expensive mortgages can divert households into rentals, supporting landlords even while their floating debt remains difficult to service.

**Nine observations/document reads were missing from the owner record:** two Trepp analyses, Redfin's weekly update, Zillow's September report, Miami-Dade's September release, two HUD letters, the newer MND rate path, and loanDepot's Nomura facility. Most were published October 7–16, rather than breaking today; HUD's build-to-rent letter has no visible issuance date. UWM's capital rescue and October HMI were already captured and are excluded from the novelty count.

## New evidence, ranked by decision relevance

### 1. Performing multifamily loans can be undercovered before delinquency appears

[Trepp, October 16](https://www.trepp.com/trepptalk/cre-clo-multifamily-delinquency-2021-2022), **PRIMARY**, directly fetched and saved.

| Object | Finding |
|---|---|
| Population | **93 floating-rate loans / $3.95B**, securitized in **2021–22**, in CA/TX/NY/FL/GA, the five states with most securitized MF debt |
| Concentration | **12.2%** of those states' CRE CLO MF balance, **80.2%** of delinquent balance |
| Delinquency | Cohort **20.21%**, other securitization years **0.69%** |
| Cash-flow coverage | Median NCF DSCR **1.60x →0.64x**, among **48 loans reporting both measures** |
| Still-paying subset | **93.8%** of performing balance **with reported latest NCF DSCR** below **1.0x**; paired-data performing-loan median **1.57x →0.65x** |

**Meaning:** property cash flow below debt payments can precede payment default; reserves, rate caps or sponsor support may bridge the gap. **Limits:** five-state, securitization-vintage cohort, not all apartments or all CRE CLOs. The 93.8% denominator excludes missing reporters and is not 93.8% of all performing apartment debt. The paired-change count and latest-coverage-share denominator are distinct. Underlying cash-flow reporting dates are not harmonized in the public article. Trepp cannot separate higher debt service from changed cash flow. This is additional C2 evidence, not an independent new root or a C2 threshold input. Texas cohort DQ **30.53%** vs other vintages 1.41% is a within-book observation; statewide Florida interpretation remains CORAL's, with no FL figure republished here.

### 2. The reported multifamily default mix depends on which loans remain in the pool

[Trepp, October 15](https://www.trepp.com/trepptalk/securitized-multifamily-delinquency-cmbs-cre-clo), **PRIMARY**, August 2026 snapshot.

Private-label CMBS has **$75.48B** outstanding and **$5.80B** delinquent, **50.2%** of the study's delinquent balance on roughly **12%** of its outstanding balance. CRE CLO delinquent balance fell to **$1.60B**, versus $2.83B in August 2024. Trepp explains that managers can remove impaired loans; falling reported delinquency need not mean those loans recovered.

**Critical mismatch:** Trepp labels its Freddie securitized cut **0.80%**, while Freddie's own August monthly-volume summary says **0.64%**. Perimeter/definition is unresolved. **Do not overwrite the issuer number or splice this cross-book snapshot into HOMER's headline series.** This study covers specified securitized books, not the entire MF lending market. It uses August **7.69%** CMBS, not the September **8.04%** already captured. Both Trepp articles are related vendor evidence, not two independent confirmations.

### 3. Weekly home demand is weaker than the monthly price headline suggests

[Redfin, October 15](https://www.redfin.com/news/housing-market-update-asking-prices-decline-october/), **PRIMARY via web**, four weeks ending **October 11**, 900+ metros, subject to revision.

| Metric | First observed October 19 vintage |
|---|---|
| Median sale price | **$391,116; +0.5% YoY** |
| Seasonally adjusted asking price | **$396,881; −0.3% YoY** |
| Seasonally adjusted pending sales | **286,531; −12.7% YoY; +1.5% versus preceding four-week observation** |
| Active-listing price-cut share | **22.0%**, versus **20.9%** a year ago |
| Geographic demand | Pending sales down YoY in all **50** populous metros analyzed |

**Meaning:** discounting and contract weakness broaden, while the latest overlapping window improved slightly. **Limits:** this is an overlapping four-week series, not a new calendar-month print or a one-week transactions count. Redfin's history starts in 2021; the price-cut superlative is bounded to that sample. This does not reopen HOM-01 or establish list prices as a validated lead for HPI. Price-cut share is a listing statistic, distinct from NAHB's share of builders cutting prices.

### 4. Rental demand is strengthening — a real counterweight to landlord distress

[Zillow, published October 15](https://www.zillow.com/research/september-2026-rent-report/), **PRIMARY via web**, September 2026.

ZORDI rental-demand index **+19.2% YoY**; single-family +21.6%, multifamily +10.1%. Typical rent **$1,932**, **+2.7% YoY**; MF rent **$1,762**, **+2.2% YoY**, flat MoM. Concessions appear on **39.6%** of rental listings. National ZORI rents are positive YoY in **49/50** major metros; San Antonio is −0.7%, Houston +0.1%, Austin +0.7%.

**Meaning:** rental demand has support while homebuying is expensive; this cuts against a blanket claim that tenant demand is collapsing. **Limits:** ZORDI is a platform demand index, not signed leases or cash collected. ZORI asking-rent growth is not effective rent after concessions, NOI or debt-service coverage. Do not join the new $1,932 level to HOMER's old July $1,962 to claim a seasonal or revision-adjusted decline. **Zillow's 49/50 metro result does not grade the Apartment List frozen 100-city rent-breadth band.** Different geography, sample and method can coexist.

### 5. Miami-Dade condos remain oversupplied relative to sales, but inventory is lower YoY

[MIAMI REALTORS + RWorld, October 16](https://www.miamirealtors.com/2026/10/16/miami-dade-breaks-annual-record-for-30-million-plus-home-sales-in-just-nine-months/), **PRIMARY via web**, September 2026. HOMER-owned county condo cut only.

Condo supply **12.3 months**, median **$417,090 (−0.69% YoY)**, sales **909 versus 904 (+about 0.6%, issuer rounds to 1%)**, active inventory **11,706 (−7.24% YoY)**. Contracts take **67 days**, versus **75** a year ago: **eight days faster**, despite the release's erroneous 'up from' wording. Condo cash share **49.4%**. Reported distressed sales **0.5% of all Miami closed residential sales**, not condo-only.

**Meaning:** a buyer's market and mildly lower condo prices persist, without evidence here of a broad forced-sale wave. Lower YoY inventory and faster contracts must travel with the stress observation. August's saved **12.1 months / $408K /66 days** are **as originally published**, not revised in this September release; no precise MoM trend is inferred. Issuer commentary also gives the opposite sign to NAR's national sales YoY; that borrowed national line is excluded. No statewide Florida figure or multi-county FHA-approval ratio adopted.

### 6. FHA's score-model change has a dated implementation rule

[HUD Mortgagee Letter 2026-11, October 8](https://www.hud.gov/sites/default/files/hudclips/documents/2026-11hsgml.pdf), **PRIMARY PDF**, pages 1–4.

Effective for case numbers assigned **January 1, 2027 onward**: FICO 10T and VantageScore 4.0 join Classic FICO. Tri-merge remains required; numeric minimums remain **500**, with **580** for maximum financing and 500–579 generally limited to **90% LTV**. For each submitted model, use middle of three scores/lower of two; take the lowest selected submitted-model score per borrower, then the lowest borrower score for the transaction. A lender may submit one or more model types, using the same types for all borrowers.

**Meaning:** future score-stratified origination comparisons need a model/vintage label. **Limits:** not a numeric credit-floor cut, not automatic approval, not a change to today's MBA delinquency numerator, and not the already-captured NY Fed measurement switch or September FHFA order. No present HOM-02 or A1 regrade.

### 7. HUD opens a conditional financing route for build-to-rent communities

[HUD Mortgagee Letter 2026-12](https://www.hud.gov/sites/default/files/hudclips/documents/2026-12hsgml.pdf), **PRIMARY PDF**, all five pages read. **No visible issuance date**; newly discovered October 19, not represented as an October 19 announcement. Letter says effective immediately until changed.

HUD accepts eligible purpose-built rental communities with **five or more units** on a cohesive contiguous site: Section **221(d)(4)** for new construction; **223(f)** for acquisition/refinancing where certificate of occupancy is **less than three years** before application. Professional management and cohesive rental collateral are required. Market-rate underwriting uses at least **7% vacancy** or a higher market assumption. Initial operating-deficit escrow is at least the greater of **3% of loan amount or four months' debt service**.

**Meaning:** a financing counterweight for qualifying new rental supply. **Limits:** not blanket relief for old apartment loans or scattered rental houses; eligibility is not a funding commitment. No partial collateral releases during the insured term. Do not infer that Lennar/Millrose transactions qualify or occurred. Publication-date gap retained.

### 8. Faster mortgage-rate series improved, then partly reversed

[Mortgage News Daily index](https://www.mortgagenewsdaily.com/mortgage-rates/mnd), **PRIMARY**, fetched October 19; page explicitly last updated **10/19/26**. Thirty-year fixed: **7.45% [10/14] →7.33% [10/15] →7.37% [10/16] →7.40% [10/19 reading]**. October 19 is a dated observed update, not certified end-of-day.

**Meaning:** there was rate relief after the mortgage survey window, followed by a partial reversal. **Limits:** this is MND's daily index, not Freddie PMMS, MBA contract rates, a tradable price or a new A2 print. No new mortgage/Treasury spread calculated from this different instrument.

### 9. loanDepot added uncommitted repo capacity, including conditional REO collateral

[loanDepot 8-K, signed/filed October 7; agreement October 2](https://www.sec.gov/Archives/edgar/data/1831631/000183163126000111/ldi-20261002.htm), **PRIMARY via SEC web**, Item 1.01.

Nomura facility **up to $125M**, **uncommitted**, for residential loans and, subject to conditions, REO interests; scheduled expiry **September 30, 2027** unless extended/terminated. Margin deficits must be cured on buyer request; default can accelerate repurchases. **No actual emergency draw, covenant breach or lender loss is established.** This financing agreement alone fires none of HOMER's servicer stress classes. The whole six-name SEC census was not completed: the SEC submissions endpoint returned 403; this is a bounded headline/source sweep, not a new full-watch 'all clear'.

## Dedupe, rejected leads and unresolved source access

| Candidate / lane | Disposition |
|---|---|
| October NAHB HMI 29 / cutters 43% | Already in morning L725 report; new WALTER SIG-W-20261019-004 receives that existing grade, no repeat grade |
| HY 331bp / liquidity rung | SIG-W-20261019-003 INFO only; upstream LIQUID/RED/REGINALD judgment, no direct housing loss conclusion |
| Indianapolis office correction | SIG-W-20261019-007 confirms HOMER's earlier decline. Named correction COR-20261019-07 receipted NO-OP, with prior owner commits cited |
| UWM $2.05B rescue | Already captured in August servicer review; not new distress. Original issuer announcement gives expected rights-offering expiry **11/12 17:00 ET**, pricing window **10/27–11/09**. Registered verification clock only; completion/current final terms not verified from a prospectus |
| Pennymac Q3 | Issuer event page confirms **10/29**; source for next owned servicing read, not a new earnings print |
| Redfin 'single-family rental on decline' | Rejected as current news: **January 29, 2026**, based on **2024 Census** stock data, despite prominent current homepage placement |
| GlobeSt October 16 MF geography story | Its 7.69% / Freddie 0.8% cut does not supersede HOMER September headline. The recovered October 15 Trepp primary does not itself verify the GlobeSt geography/concentration details; no secondary named-loan map adopted |
| ATTOM Sept/Q3; ICE Sept First Look; GSE September; October Apartment List | No decisive newer grading print recovered in the bounded sweep. ATTOM access remains unresolved, not proven unpublished; future clocks unchanged |
| Florida statewide owner dependency | Florida Realtors Sept/3Q issuer release dated10/16 found at https://www.prnewswire.com/news-releases/flas-housing-market-continues-recent-trends-in-sept-and-3q-2026-302911329.html . CORAL owns the statewide refresh. HOMER demoted its historical August statewide citation and routed the new source address without publishing a replacement statewide figure |
| Miami website address | `www.miami.realtor` DNS failed. Working issuer archive at miamire.com led to miamirealtors.com source via web. A dead alias does not mean a dead publisher |

Novelty test searched current HOMER ledgers/reports/docket/board log, then AGENTS/BOARD/PROME for distinctive source URLs and object phrases, excluding archives and processed mail. The seven principal new-report/document URLs had no current match before integration. Absence from that scan is a bounded search result, not proof nobody has ever seen the news. Source extracts and raw-response/text hashes are in `reports/2026-10-19_sweep_evidence/manifest.json`; blocked shell responses are separately labelled from successful web-served issuer evidence.

## State, continuity and delivery

**No new formal resolver print changes the morning kill counts:** thesis 0/5 killed, handle 19/25, review November 20. Added evidence is mechanism/context, not a threshold retune or a new independent root. Future policy and servicing dates belong on the existing owner docket; source-definition mismatch belongs in the Trepp row. Cross-domain findings go to WALTER's routing lane and the NEXUS brief; no office/other-desk records edited.

**Final lifecycle, reconciled in the October 19 documentation audit:** inbox at sweep start was **top-level 0 / WALTER 3**; later digest SIG-W-20261019-009 made **four total**. All were integrated before filing; final census **0/0**. The initial three were sender-uncommitted at first read, then tracked at WALTER commit `666b5eb5d`. Owner integration `076910b8f` preceded filing `3c7e5fb3a`; digest integration `cf1443a51` preceded filing/delivery `2f9b4117c`. No live cross-terminal transport is verified. No pull, stash, reset or push; PROME coordinates reviewed persistence.

**Will decision required: none.**

## Validation and consumer routing

Source URL/object search preceded integration. Required before persistence: changed workbook TSV column widths, current STATUS byte tier, saved-source hashes, correction receipts and weekday claims. No auto-memory written. Miami supply12.1→12.3 consumer check found CORAL current citations and unrelated percentage/source-snapshot hits; only CORAL receives a consumer packet. Zillow1962→1932 hits were dated July BOARD/consumption records, not current figures to overwrite. No MoM decline inferred across rental vintages.

Durable WALTER and CORAL packets were committed at `3c7e5fb3a`; WALTER's BOARD SIG-W-20261019-009 explicitly records reading and routing the owner report with caveats. CORAL consumption and PROME exact-version consumption remain unverified. Full source access gaps and exact final checks are carried in `PROME/inbox/2026-10-19_from-HOMER_domain-sweep-nine-new-reads.md` (or its `processed/` successor).

Author validation completed: **20 raw-response/text hashes matched**, modified workbook/docket rows have the required column counts, Miami909/904 rounds to0.6% and67vs75 is eight days faster. STATUS **22,602B** is below the22,785B soft tier after archiving aged narrative and closed implementation receipts verbatim. Weekday/read-cap/corrections checks passed within their stated perimeter; no NAMED correction remains unreceipted. The self-consumer scan's August PRICING observation is now explicitly historical/superseded; its remaining long prior-header echo is already labelled PRIOR HEADER VERBATIM and is not a live September claim. No auto-memory, rule change or new predictive instrument.

**Subsequent documentation maintenance:** `reports/2026-10-19_documentation-audit.md` maps all nine reads to their workbook homes. Durable mechanisms, counterevidence and policy changes are now KB-HOMER-034–038 in `workbook/KB_LIVE.tsv`; the frozen parent-era KB is unchanged. The byte count above records the sweep commit, not a perpetual current-size claim.
