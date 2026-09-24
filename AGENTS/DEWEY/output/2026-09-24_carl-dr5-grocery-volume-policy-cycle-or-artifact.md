# CARL-DR-5 — Is the grocery-volume decline POLICY, CYCLE, or a MEASUREMENT ARTIFACT?
**Date:** 2026-09-24 | **Mode:** Thesis | **Confidence:** Medium on policy (magnitude arithmetic, primary data) · Medium on the national cross-check (primary, but the series measure different things) · Low on the cross-state test (experimental series, low power)
**Commission:** CARL-DR-5, CARL packet 2026-08-15 (Will-approved), due 2026-08-29, delivered 26 days late. Status request: CARL 2026-09-11. Run as a PROME-spawned L0 drain (prome-26). Engine: DEWEY `scripts/` primary pull plus targeted fetches. No fan-out.

## Key Finding

**The evidence leans toward a SUBSTITUTION / MEASUREMENT ARTIFACT. POLICY is ruled out as the dominant driver on magnitude, and CYCLE is not supported.** The panel figure that started this (NielsenIQ unit sales −1.8% to −2.2% YoY, Feb–Jun 2026) is not matched by the total-economy measure. **BEA real spending on food and beverages bought for home was −0.7% to +0.8% YoY over Feb–Jul 2026, and +0.6% in June.** The shortfall sits in traditional grocery stores (Census NAICS 4451 deflated by food-at-home CPI: −1.6% to −1.7% real), while the channels the panel covers partly or not at all are growing: general-merchandise stores +3.5% to +4.5% nominal, Sam's Club transactions +7.0%, Costco US comparable sales ex-gas +5.6%. SNAP benefits fell $1.01B a month YoY (June 2026, −13.0%). Even at dollar-for-dollar pass-through that is 0.77% of at-home food and beverage spending, under half of a 1.8pp decline. At the literature's pass-through rate (0.5–0.6) it is about 0.4–0.5pp, roughly a quarter. **Leg 1's by-state test does not exist in the form commissioned (there is no public state unit-volume series). The closest public substitute, Census's experimental state retail sales for food and beverage stores, shows no relationship with either SNAP loss or unemployment change across 51 states (R² = 0.003), but that test has low power.**

⚠️ **One sub-datum in the commission does not survive:** *"volume decline now outweighs price ⇒ nominal grocery sales are FALLING."* That claim is **SEARCH-NOT-FOUND in the Bain/NIQ primary release** (which gives units −1.8% and prices +2–3%, implying nominal roughly flat to +1%) and is **contradicted by Census** (grocery stores nominal +0.97% Jun, +0.52% Aug YoY) and **by BEA** (off-premises food and beverages nominal +2.97% Jun). Strike it separately, whatever the grade.

## §1 — Resolution-path audit (first paragraph, as the commission required)

| Leg-1 input | Public? | What exists | Verdict |
|---|---|---|---|
| SNAP participation and benefits by state, monthly | ✅ | USDA FNA "SNAP Data Tables", state files with June 2025 / May 2026 / June 2026 columns; national monthly FY23–FY26 (data as of 2026-09-11) [PRIMARY] | Usable. ~3-month lag. The state file carries only the latest month and its year-ago comparison; a full state monthly history is in the FY69–current zip |
| Grocery **unit volume** by state | ❌ | NielsenIQ / Circana are subscription. Bain/NIQ publishes only 2 regions in press coverage (West −3.0%, Northeast −1.3%, June) [NEWS: Food Dive 2026-07-27] | **Does not exist publicly.** Not substituted with state food CPI, as instructed |
| Closest public substitute | ⚠️ | **Census Monthly State Retail Sales (MSRS), NAICS 445 food & beverage stores**, on FRED as `MSRS<ST>445`: YoY % change, nominal, not seasonally adjusted, *experimental*, blended from survey, administrative and third-party data, through May 2026 (FRED last updated 2026-08-20) [PRIMARY-experimental] | A **nominal sales-growth** series, not unit volume and not a price series. National price moves cancel in a cross-state comparison, so the cross-section is interpretable. It **excludes supercenters and clubs (NAICS 455)**, so it is bound to one channel |
| SNAP redemption dollars by state | ⚠️ | Annual retailer-redemption summaries only. Not monthly | Not used |

## §2 — Leg 3 first: magnitude (does the arithmetic settle it?)

| Quantity | Value | Source |
|---|---|---|
| SNAP benefits issued, June 2025 | $7,793,348,293 | FNA national monthly table, data as of 2026-09-11 [PRIMARY] |
| SNAP benefits issued, June 2026 (preliminary) | $6,781,046,574 | same |
| **Change** | **−$1.012B per month (−13.0%)**, ≈ −$12.1B annualised | derived |
| Persons, June 2025 → June 2026 | 41,678,341 → 36,352,716 (−5.33M, −12.8%) | same |
| Average benefit per person | $186.99 → $186.53 (flat) | same |
| ⇒ **The cut is eligibility/participation, not benefit level.** 15 straight monthly declines in participation, Apr 2025 → Jun 2026 (national monthly table) | | derived |
| Off-premises food & beverage PCE, June 2026 | $1,573.1B SAAR = **$131.1B per month** | BEA via FRED `DFXARC1M027SBEA` [PRIMARY] |
| SNAP loss as a share of that | **0.77%** | derived |
| SNAP loss as a share of Census grocery-store sales ($77.0B, Jun) | 1.32% (upper bound; grocery stores are not the only SNAP channel) | FRED `RSGCS` [PRIMARY] |

**Share of food spending that follows a SNAP dollar.** Hastings & Shapiro estimate the marginal propensity to consume SNAP-eligible food out of SNAP benefits at **0.5–0.6** (much higher than out of cash) [ACADEMIC: *AER* 108(12):3493–3540, 2018].

| Assumed pass-through | Effect on at-home food $ | Share of a 1.8pp decline |
|---|---|---|
| 0.3 | −0.23pp | 13% |
| **0.5–0.6 (literature)** | **−0.39 to −0.46pp** | **21–26%** |
| 1.0 (dollar for dollar, a ceiling) | −0.77pp | 43% |

**Leg-3 verdict: POLICY cannot be the dominant driver of a ~2% national decline.** Even the ceiling is under half. It is a **real, material minority contributor** (about a quarter at the central estimate).
⚠️ Caveats that could move this: (i) the panel counts **units**, not dollars. Low-income baskets likely carry more units per dollar, so SNAP's share of *units* could exceed its share of dollars. This is unmeasured, and a 1.5× unit weighting would lift the ceiling to about 65%. (ii) People who leave SNAP entirely lose the whole benefit, not a marginal dollar, so pass-through for leavers may exceed 0.6. (iii) June 2026 FNA data are preliminary.

## §3 — Leg 1: the cross-state discriminator, on the substitute instrument

**Test.** For 51 states (50 plus DC): y = average MSRS-445 YoY for Feb–May 2026 (the window Bain says the decline accelerated). Policy regressor = SNAP benefit $ lost per resident per month (June 2025→June 2026, FNA state file ÷ FRED `<ST>POP` 2025). Cycle regressor = change in state unemployment rate, May 2026 vs May 2025 (FRED `<ST>UR`).
**Predictions.** Policy-dominant ⇒ a negative slope on SNAP loss of about −0.22pp per $/capita (pass-through 0.55 ÷ ~$249 food-store sales per capita per month, from `RSDBS`). Cycle-dominant ⇒ a negative slope on ΔUR.

| Regressor | Pearson r (t) | Spearman ρ (t) |
|---|---|---|
| SNAP $ lost per capita per month (range $0.19–$11.55) | −0.00 (−0.02) | +0.15 (+1.03) |
| SNAP benefit % change | +0.01 (+0.09) | −0.19 (−1.36) |
| ΔUR, pp (range −1.0 to +1.3) | +0.05 (+0.36) | +0.13 (+0.95) |
| **OLS on both** | b_SNAP = −0.021 (t −0.15), b_ΔUR = +0.28 (t +0.39), **R² = 0.003** | ex-AZ: R² = 0.004 |

**Result.** Neither channel predicts where food-store sales weakened. The biggest SNAP loser, Arizona (−51.9% benefits, $11.55 per capita), shows food-store growth of −0.12% (0.9pp below the state mean; the policy slope predicts about 1.9pp below). The weakest state, Iowa (−4.22%), had a small SNAP loss ($1.20) and falling unemployment.
⚠️ **Low power, so read this as "no gradient seen", not "gradient refuted".** The policy-predicted slope (−0.22) sits about 1.4 standard errors from the estimate (−0.021 ± 0.14). MSRS is noisy (state range −4.2% to +10.8%), nominal, NSA, experimental, includes liquor stores, and excludes supercenters and clubs, so state differences in channel shift confound it. The SNAP change is measured June/June, a month after the y window.
**Regional cross-check (n=2, illustrative only):** Bain/NIQ West −3.0%, Northeast −1.3%. SNAP $ lost per capita: West $2.78, Northeast $2.10, South $3.68 (largest, with no published NIQ figure), Midwest $2.47. The ordering is consistent on two points, but n=2, and NIQ's regional definitions were not verified against Census regions.

## §4 — Leg 2: the substitution control

| Measure | Latest | Basis | Source |
|---|---|---|---|
| NIQ panel units | Jan +1.7%, Feb −2.0%, Apr −2.2%, May −1.9%, Jun −1.8% YoY; "consistently across US regions" | units, NIQ-measured outlets | Bain PR 2026-07-16 [INSTITUTIONAL, primary release via PR Newswire]; monthly figures from Food Dive 2026-07-27 [NEWS] |
| **BEA real off-premises food & beverages** | Feb −0.67%, Mar +0.54%, Apr +0.25%, May +0.82%, **Jun +0.59%**, Jul +0.01% YoY | chained 2017 $, SAAR, all outlets, includes alcohol | FRED `DFXARX1M020SBEA` [PRIMARY] |
| Census grocery stores (4451) ÷ CPI food at home | **Jun −1.69%, Aug −1.57%** real YoY (nominal +0.97% / +0.52%) | SA $, grocery stores only | `RSGCS` ÷ `CUSR0000SAF11` [PRIMARY] |
| Census general-merchandise stores (455, incl. supercenters and clubs) | **+3.49% Jun, +4.54% Aug** nominal YoY | SA $, food and non-food | `RSGMS` [PRIMARY] |
| Circana (PLMA) units, 6 months to 6/14/2026 | store brands +0.2%, national brands −0.5% ⇒ **total ≈ −0.3%** (derived at 23.8% store-brand unit share); store-brand unit share **23.8%, record** | units, Circana multi-outlet, food and non-food | PLMA release 2026-07-08 [INSTITUTIONAL] |
| Sam's Club U.S., 13 weeks to 7/31/2026 | comp ex-fuel **+4.4%**, **transactions +7.0%**, ticket −2.5%; "increased transactions and total unit volumes with strength in grocery" | company | WMT 8-K EX-99.1, 2026-08-20 [PRIMARY] |
| Walmart U.S., same period | comp +2.6%, transactions +1.5%, eCommerce contribution ~510bp | company | same [PRIMARY] |
| Costco, 4 weeks to 8/30/2026 | US comp **+9.0%**, ex-gas/FX **+5.6%** (Labor Day shift −<75bp) | company | Costco IR release [PRIMARY]; traffic +3.3% and food & sundries "low single digits" from the call per secondary coverage [NEWS] |
| Channel coverage of NIQ's xAOC | Costco, Aldi, Trader Joe's reported **not measured** (estimated) | — | cpgdatainsights.com / Bedrock vendor-education pages [UNVERIFIED] |

**Reading (INFERRED, not established):** two syndicated panels differ by more than 1pp over overlapping windows (NIQ ≈ −1.2% average Jan–Jun excluding March, which was not published; Circana ≈ −0.3% H1). The total-economy real series is flat to up. The weakness is concentrated in the traditional-grocery channel, and the value, club and online channels are gaining trips and units. That is the pattern the commission's §2 described: *measured volume falls because where and what people buy moved.* Three further mechanisms push panel **unit counts** down without cutting consumption: club and bulk packs (fewer units per volume), online baskets (smaller unit counts; Bain names this), and GLP-1 users buying less (Bain: 30–40% of users say they are cutting grocery purchases). That last one is a real consumption change, but it is neither policy nor cycle.

## §5 — Cycle check (national)

| Measure | Value | Source |
|---|---|---|
| Unemployment rate | 4.3% (Aug 2025) → **4.1% (Aug 2026)**, falling | `UNRATE` [PRIMARY] |
| Food services, real | nominal +5.85% Aug YoY ÷ food-away-from-home CPI +3.37% ⇒ **≈ +2.4% real** (Jun ≈ +1.3%) | `RSFSDP`, `CUSR0000SEFV` [PRIMARY] |
| Cross-state ΔUR vs food-store sales | no relationship (§3) | derived |

A household in cyclical food retrenchment does not usually raise real restaurant spending about 2%. **CYCLE (labour-market demand destruction) is not supported.** ⚠️ Bain's own driver ranking puts **the March gasoline spike (+20%)** above SNAP as "more importantly". That is an energy terms-of-trade squeeze, neither CARL's policy nor its cycle branch, and FERT's charter does not cover it (FERT is the supply and cost-push half). If CARL treats a fuel-driven squeeze as "cycle", the grading changes. That mapping is CARL's call.

## Counter-Evidence

- **Against the artifact reading:** BEA's off-premises food estimate is itself built largely from Census retail sales with product-line shares. It is not an independent volume measurement, and it includes alcohol. Its YoY was −0.67% in Feb 2026, the month NIQ says the slide accelerated. The Census 4451 decline (−1.6% real) is a full-universe count of grocery stores, not a panel, so part of the weakness is real **for that channel**. Walmart U.S. transactions rose only +1.5%, and its store (non-eCommerce) contribution was roughly −2.5pp (2.6% comp minus ~510bp eCommerce). Supercenter floors are not booming.
- **Against "policy is minor":** the unit-weighting and full-benefit-loss caveats in §2 could roughly double policy's share. Bain names SNAP as "one key factor". Participation has fallen 15 months running, so the effect is still building.
- **Against the cross-state null:** low power (§3). The null cannot distinguish "no policy effect" from "policy effect masked by channel shift". States where SNAP leavers shifted to supercenters would show weaker 445 sales for artifact reasons.
- **Payroll datum (BLS USDL-26-1291: warehouse clubs & supercenters −21K):** sits awkwardly beside Sam's transactions +7% and Walmart eCommerce +24%. **INFERRED:** employment in that line is not a demand proxy (automation, fulfilment mix). Not tested here.

## Source Quality Assessment

All the load-bearing numbers come from primary sources (FNA, BEA, Census, BLS via FRED; WMT 8-K; Costco IR; the Bain release on PR Newswire) and can be reproduced from the series IDs above. Weak points: the NIQ monthly and regional splits come through trade press (Bain's own site and USDA/FNA blog returned 403); NIQ channel coverage is [UNVERIFIED]; MSRS is experimental; NIQ March 2026 was not found.

## §6 — ⭐ Second deliverable: does demand-side food justify a standing agent?

**Answer: NO standing agent. There is recurring public depth, but it is a six-series national panel that fits inside CARL's existing monthly cadence. The piece that would justify a separate desk (unit volume by channel and state) is subscription-only.**

| Instrument | Cadence | Lag | Access | Geography |
|---|---|---|---|---|
| Census MARTS/MRTS: 4451 grocery, 455 general merch, 722 food services | monthly | ~2 wks | free (FRED) | national |
| BEA PCE real off-premises food & beverages | monthly | ~4 wks | free | national |
| BLS CPI food at home / away from home | monthly | ~2 wks | free | national + 4 regions |
| USDA FNA SNAP persons and benefits | monthly | ~3 mo | free | **state** |
| Census MSRS 445 (experimental) | monthly | ~3 mo | free | **state**, YoY % only |
| Issuer disclosures (COST monthly; WMT, TGT, KR, DG, DLTR, BJ quarterly) | monthly/qtr | days | free | national |
| PLMA/Circana store-brand releases | semiannual | ~3 wks | free summary of paid data | national |
| NIQ / Circana panel units by channel | weekly | days | **subscription** | any |
| USDA ERS Food Expenditure Series | annual | ~1 yr | free | national |

A standing desk would mostly re-derive what CARL already watches. The one discriminating instrument (panel units by channel) is the paid tier. **FERT boundary respected:** nothing here touches fertiliser, ag inputs or food CPI cost-push.

## References (accessed 2026-09-24)

- USDA FNA SNAP Data Tables: https://www.fna.usda.gov/pd/supplemental-nutrition-assistance-program-snap. Files `snap-4fymonthly-9.xlsx`, `snap-persons-9.xlsx`, `snap-benefits-9.xlsx` (data as of 2026-09-11) [PRIMARY]
- FRED series: RSGCS, RSDBS, RSGMS, RSFSDP, CUSR0000SAF11, CUSR0000SEFV, DFXARC1M027SBEA, DFXARG3M086SBEA, DFXARX1M020SBEA, UNRATE, MSRS<ST>445 (51), <ST>UR (51), <ST>POP (51) [PRIMARY]
- Bain & Company with NielsenIQ, press release 2026-07-16: https://www.prnewswire.com/news-releases/us-grocery-slowdown-enters-a-new-phase-as-stretched-consumers-buy-less--bain--company-analysis-302827894.html [INSTITUTIONAL]
- Food Dive, "Grocery volumes contract for fifth consecutive month", 2026-07-27: https://www.fooddive.com/news/grocery-unit-sales-decline-bain-nielseniq/825711/ [NEWS]
- Walmart 8-K EX-99.1, 2026-08-20: https://www.sec.gov/Archives/edgar/data/0000104169/000010416926000145/earningsreleasefy27q2.htm [PRIMARY]
- Costco August sales release: https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-August-Sales-Results/default.aspx [PRIMARY]
- PLMA, 2026-07-08: https://www.plma.com/article/store-brands-continue-gains-unit-sales-and-shares [INSTITUTIONAL]
- Hastings & Shapiro (2018), *AER* 108(12): https://www.aeaweb.org/articles?id=10.1257%2Faer.20170866 [ACADEMIC]
- xAOC coverage: https://www.cpgdatainsights.com/get-started-with-nielsen-iri/xaoc-and-mulo/ [UNVERIFIED]

**Reproduction recipe (§3):** `fred_pull.fetch("MSRS<ST>445")`, averaged over 2026-02..05. SNAP $ lost per capita = (June 2025 − June 2026 benefits from `snap-benefits-9.xlsx`) ÷ `<ST>POP` 2025 × 1000. ΔUR = `<ST>UR` May 2026 − May 2025. Pearson, Spearman (rank) and OLS on 51 rows; ex-AZ variant.

## Process Report

**Searches run:** ~10 web searches and 8 fetches; ~180 FRED pulls (3 × 51 state series plus 12 national). Primary pull = spine; no fan-out (two interpretive legs plus arithmetic, sized per protocol).
**Data gaps:** state unit volume (does not exist publicly); NIQ March 2026 print; NIQ South/Midwest regions; NIQ channel coverage at a primary; SNAP by state for Feb–May at state granularity (the zip was not opened; only the June/June columns were used).
**Source frustrations:** bain.com, usda.gov blog and grocerydive.com returned 403 with both user agents. The fna.usda.gov xlsx returned 0 bytes to curl with a browser UA but downloaded with `fetch_url.headers_for` (worth a `--download` flag; BACKLOG candidate). FRED search API returned nothing for a food-only off-premises series, so BEA's food-plus-beverages series was used with an alcohol caveat.
**Confidence:** Medium overall. The policy ceiling is robust; the artifact lean rests on four sources agreeing in direction that measure different things.
**If I had more time/tools:** open the FY69–current state zip to rebuild a monthly state SNAP panel aligned to the MSRS window; pull BEA's food-only line (NIPA table 2.4.3U) to drop alcohol; get NIQ's regional definitions.
**Suggestions:** a `fetch_url.py --out FILE` binary-download mode.
