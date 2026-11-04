# November 4 backlog — equipment pairing, Emerson and October rail

**Read November 4, 2026.** Bounded continuation of existing work on Will's direct instruction. Survey grades are carried unchanged from L899; no calibration, new study or framework. Recovery/authority: BOOT_RECOVERY.md. Sources and vintages: sources/manifest.jsonl, WEB_M3_FACTS.json, IMPORT_QUARTER_INPUTS.json, DOMESTIC_CALCULATIONS.json and RAIL_BATCH.json.

## Assessment

The evidence for actual equipment buying is stronger: domestic core orders/shipments, imported computer hardware and real equipment investment all rose in Q3 on the named accepted vintages. Emerson adds automation volume growth and positive orders across its groups. October-ending rail weeks remain positive against their prior-year comparators. This is counterevidence to an imminent goods-demand collapse; it does not prove durable, broad private end demand, identify the AI share of imports or clear financing stress. R1 and the inherited ISM trigger are not re-graded here.

## 1. Factory orders — September full report, November 3 10:00 EST

PRIMARY-VERIFIED Census release **CB 26-170 M3-2(26)-09**, https://www.census.gov/manufacturing/m3/prel/pdf/s-i-o.pdf . Figures nominal USD millions; SA unless named otherwise. Primary PDF text, page/section headers and unit columns checked through web. Direct PDF/XLSX GET returned 403; the screenshot adapter returned no inspectable image. No local raw Census PDF or visual inspection is claimed. FRED values observed by boot agree with core and headline levels but are not the primary authority.

| Metric | September full | August in full | Grade / revision |
|---|---:|---:|---|
| Total factory orders | 677,247 | 665,004 | +1.8% m/m; total advance existed, so this read is not certified as the first estimate |
| Shipments | 668,454 | 659,631 | +1.3% m/m |
| Inventories | 976,044 | 972,304 | +0.4%; inventories/shipments 1.46 vs 1.47, less aggregate overhang pressure |
| Durable orders | 345,672 | 339,185 | +1.9%, revised from advance 345,371/+1.8% |
| Core nondefense ex-aircraft orders | 88,185 | 87,616 | +0.6%, revised from September advance 88,039/+0.5% |
| Core nondefense ex-aircraft shipments | 86,125 | 85,074 | +1.2%, level revised from advance 86,052 |
| Computers/electronics orders | 31,266 | 31,015 | +0.8%; not the narrower computers-only row |
| Electrical/appliance/component orders | 18,854 | 18,908 | −0.3%; no broad electrical-order surge |
| Computers/electronics shipments | 34,707 | 34,238 | +1.4%; Table 1, PDF page 6 |
| Electrical/appliance/component shipments | 18,685 | 18,686 | 0.0% at published precision; Table 1, PDF page 6 |

Core values are in **Table 5, PDF page 10**, separate SHIPMENTS and NEW ORDERS sections (not Table 6 as WALTER's preliminary note suggested). Its last percent column is **year-to-date y/y**, not September y/y. September NSA core orders 92,843 vs September 2025 81,501 = **+13.92%**; core shipments 90,967 vs 81,756 = **+11.27%**. The table's **10.9% / 8.8%** are January–September NSA comparisons. Both are retained with the correct periods; neither is mixed into SA month-to-month growth.

September/ August core levels are recorded as REVISED-2026-11-03, retaining every September ADVANCE and earlier August vintage. August core revisions versus October 27 are orders −17 and shipments +61 USD millions. July core 86,295/84,506 is unchanged from the saved comparison. Quarterly SA sums: Q3 orders 262,096 vs Q2 252,895 = **+3.638%**; shipments 255,705 vs 246,014 = **+3.939%**. Q3 comes from November 3 primary; Q2 remains the October 26 saved FRED mirror (same Q2 totals used October 31). This is a named mixed-vintage calculation, not a single November 3 historical pull.

## 2. Computer imports paired with domestic equipment — existing J1

PRIMARY-VERIFIED BEA/Census FT-900 **BEA 26-47 / CB 26-178**, November 4 08:30 EST. https://www.bea.gov/sites/default/files/2026-11/trad0926.xlsx and trad0926.pdf . **Exhibit 8, PDF page 22**, visually inspected from a local render and reconciled to workbook **sheet 8, rows 82–83**, including column headers and Census-basis note. Units are nominal USD millions, **SA**, imported goods, not domestic production or AI-only spending.

| End-use category | September B | August revised C | September change D | Jan–Sep 2026 E | Jan–Sep 2025 F |
|---|---:|---:|---:|---:|---:|
| Computers | 41,721 | 34,166 | +7,555 | 296,678 | 148,680 |
| Computer accessories | 30,911 | 25,197 | +5,714 | 189,432 | 100,654 |
| Combined | **72,632** | **59,363** | **+13,269 (+22.35%)** | **486,110** | **249,334** |

August was 59,356 in the October 6 original release: revision **+$7M**, preserved separately. Do not add computers' and accessories' gains to every capital-goods category: other categories fell. Semiconductors are a distinct import category; they are not added to this pre-existing two-category J1 instrument. Domestic M3 computers/related, broad electronics and FT-900 end-use categories have different boundaries; no dollar import share or AI allocation is calculated.

Quarter reconstruction uses each named issuer release, not a fabricated current-history series: April 52,331 (July 7 revised); May 50,149 (August 4 revised); June 47,853 (August 4 initial); July 61,392 (October 6 revised); August 59,363 (November 4 revised); September 72,632 (November 4 initial). **Q2 150,333; Q3 193,387; +28.639% q/q nominal SA.** Source files and exact cell addresses are in IMPORT_QUARTER_INPUTS.json; earlier accepted workbook reused rather than re-pulled. This is a mixed-dated-vintage reconstruction. Annual revisions can alter history; a single November 4 current-history reconstruction remains unavailable. Nominal commodity seasonals and prices are not deflated.

Paired year-over-year check uses the **same January–September period and SA nominal basis**, not YTD imports against monthly domestic growth: imports +94.963%; domestic core orders +10.723%, shipments +8.634%. Domestic January–June/2025 baseline is the frozen October 26 FRED mirror, updated with July–September November 3 primary values; imported YTD is directly in November 4 Exhibit 8. This matched-period cross-check is ARTIFACT-VERIFIED with mixed vintages, not all-current primary history. The separate September NSA domestic y/y figures above are not presented as its counterpart.

| Existing J1 leg, Q3 vs Q2 | Accepted observation | Result |
|---|---|---|
| Domestic core orders / shipments | +3.638% / +3.939% nominal quarter growth | Rising |
| Imported computers + accessories | +28.639% nominal quarter growth on named mixed issuer vintages | Rising |
| BEA information-processing equipment | +37.4% real q/q **SAAR**, October 29 ADVANCE, carried from completed primary grade; equipment overall +20.9% SAAR | Rising |

**J1 physical-demand contraction warning: NOT-MET.** All three leg directions are positive on accepted vintages. SAAR and simple q/q magnitudes are not comparable; this conjunction tests signs, not additive dollar totals. Domestic orders do not capture imported GPU/server buying. The import-confound is supported, but the AI/financing thesis verdict remains VULCAN's, and an AI-specific causal allocation is not proved. No gate is registered by this result; no revision to the frozen J1 rule.

## 3. Emerson — fixed eight-cell company read

PRIMARY-VERIFIED continuing operations, FY2026 Q4 ended September 30, released **November 4 06:55 EST**. Issuer release https://ir.emerson.com/news-events/press-releases/detail/649/emerson-reports-fourth-quarter-and-full-year-2026-results-provides-initial-2027-outlook and its linked earnings presentation (archived). Corporate data NSA; underlying metrics are non-GAAP and exclude currency/significant acquisitions/divestitures; orders/backlog figures below exclude AspenTech. Same eight cells in companies/EMR.md; no perimeter change.

| Cell | Accepted read |
|---|---|
| Orders/backlog | Trailing-three-month underlying orders **+14% y/y** vs prior Q3 +7%; all groups grew. Backlog ex-AspenTech **$8.2B**, +11% y/y, **flat vs June**; GAAP backlog $9.6B includes $1.4B AspenTech (slides 5/7/23) |
| Guidance | FY2026 adjusted EPS $6.59 vs August guidance about $6.55; initial FY2027 sales/underlying growth about 5%, adjusted EPS about $7.25. New fiscal year, not a same-period guidance raise (slides 4/11) |
| Price vs volume | Q4 underlying sales **+7% = volume +4 points, price +3**; revenue $5.201B; adjusted segment EBITA margin 29.1%, +160 bp; price-cost/cost reductions outpaced inflation (slide 7 visually checked) |
| Tariff cost/recovery | Net IEEPA refund benefit $9M Q4 / $91M FY, excluded in adjusted reconciliations; refund net of charitable contribution, **not incremental tariff cost** (slide 14 / release reconciliation) |
| Inventory/destocking | Release balance-sheet inventories $2.432B vs FY2025 $2.213B (+9.9%). Customer destocking NOT-STATED in reviewed release/slides. Own inventory balance is not customer inventories |
| AI/grid line | Power, LNG and aerospace/defense lead projects; about $575M Q4 project wins, about 75% growth verticals. Explicit AI/data-center sales figure NOT-STATED. Power is not automatically grid-only; WATT owns that interpretation. FY2026 growth verticals 27% of sales grew 21%, other automation 73% was flat (slides 5/6) |
| Capex plan | FY2026 capex $443M vs $431M; FY2027 guidance about **$0.5B** (~13% higher), not a cut; release FCF reconciliation / slide 22 |
| Cycle implication | Real automation volume and broader Q4 orders strengthen equipment evidence, but project concentration, flat sequential backlog and weak Europe/China prevent a national broad-demand conclusion |

## 4. October rail — complete five-week issuer batch

All five direct AAR press releases and linked weekly PDFs recovered by ordinary GET. Dated release bodies reconcile to **PDF page 1**, U.S. reporting-railroad perimeter; NSA counts, FIRST-PUBLISHED (no revision flagged). **The PDF footnote excludes U.S. operations of CPKC, CN and GMXT.** North American/Canadian/Mexican totals are excluded from this test. These are weeks ending in October, not exact October 1–31 calendar-day totals. October 17 was already accepted; it was checked/reused, not appended as another vintage.

| Week ending / release | Carloads | y/y | Containers/trailers | y/y | Total y/y | Growing commodity groups |
|---|---:|---:|---:|---:|---:|---:|
| Oct 3 / Oct 7 | 230,711 | +2.4% | 299,001 | +7.4% | +5.1% | 7/10 |
| Oct 10 / Oct 14 | 232,004 | +3.4% | 302,252 | +10.4% | +7.2% | 8/10 |
| Oct 17 / Oct 21 | 232,120 | +3.5% | 308,015 | +12.6% | +8.5% | 9/10 |
| Oct 24 / Oct 28 | 234,826 | +3.6% | 303,677 | +11.3% | +7.8% | 8/10 |
| Oct 31 / Nov 4 | 233,816 | +3.0% | 280,264 | +3.9% | +3.5% | 7/10 |

Five-week sums: **1,163,477 carloads + 1,493,209 intermodal = 2,656,686**. Latest four weeks: **932,766 + 1,194,208 = 2,126,974**. Four-week y/y sign is positive because **each matched week** is positive; no exact aggregate y/y percentage or prior-year denominator is fabricated from rounded growth rates. Latest week's slower growth is not a month-to-month seasonally adjusted contraction. Grain/coal softness exists alongside metals/chemical/motor-vehicle growth. All are volumes, not freight rates.

**J2 four-week rail-deterioration condition: NOT-MET.** Cass's prior September shipments +1.9% y/y and Class 8 caveat remain carried, next Cass November 13. No freight-to-credit causal claim, calibration run or RED probability re-mark. LIQUID/RED keep the funding/credit verdict; freight and computer imports may share a hardware/import cycle.

## Remaining limits and follow-ups

- **Current-vintage detailed import history / direct September import y/y:** Census-linked imports_enduse.xlsx returns direct GET 403; API returns an HTML “Missing Key” response despite HTTP 200. No Census key exists in the current environment/root .env. We did not create credentials or bypass access controls. The mixed-vintage quarter and matched-period YTD calculations above are usable with their disclosed basis; a single-current-vintage reconstruction and direct current-history monthly y/y remain unverified. Narrow retry **November 6**, retained on the catalyst ledger. No invented monthly comparator.
- **AAR October-edition exact publication day:** still UNKNOWN. Saved PDF creation metadata October 12 is not publication evidence and is not substituted. Existing September breadth read is retained. Revisit with the next scheduled rail batch **December 2**; this metadata gap does not block the five weekly volume grades.
- **Emerson:** customer destocking and quantified AI/data-center share are NOT-STATED in reviewed primary materials, not failed retrievals; no separate sourcing project. Next-quarter issuer date not announced in reviewed material; existing **November 6 calendar audit** now includes EMR.
- **S&P original-source retry November 6 and PH November 5 remain byte-for-byte unchanged.** No survey re-fetch/re-grade. Calibration and equity thermometer are out of this assignment and remain clearly carried, without new dates or framework work.

The four backlog release groups are dispositioned and consumed catalyst rows retired. Raw/adjusted mechanism scores stay **18/35 / 13/25**: hardware/project strength and rail recovery reduce collapse concern, but price/timing/concentration and incomplete broad-demand proof remain. This is a descriptive judgment, not a probability or new threshold.
