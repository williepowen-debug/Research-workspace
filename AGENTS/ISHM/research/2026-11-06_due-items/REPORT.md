# November 6 due items — S&P final, computer imports, Parker, ATA, calendar, survey calibration

**Read November 6, 2026.** PROME assignment under Will's word of 2026-11-06 15:24 ET (one bounded session, $0, no paid data, no trade). Figures keep their reference period, release date and basis. No live prices are cited, because nothing here needed one. Sources: `sources/manifest.jsonl` and the snapshots beside it.

## Assessment

Two source gaps closed on the same day. The original October S&P final says orders and output both slowed from September, so the frozen toward-real test is **NOT-MET**, no longer CANNOT-FIRE. The Census history file reproduces the mixed-vintage quarter to within rounding, so the J1 import leg no longer carries a vintage caveat; September computer imports rose **+150.96% y/y** on a single current vintage. Parker adds strong orders, with a Filtration Group caveat on the backlog. No score, band, gate or threshold moved. **R1 now has no live named print**, and the letter forbids rolling it automatically, so that goes to PROME as a decision.

## 1. L899 S&P final — original release recovered

PRIMARY-VERIFIED: S&P Global US Manufacturing PMI, October 2026, FINAL, embargoed to 09:45 EST November 2, SA diffusion points, data collected October 9-27. The portal link https://www.pmi.spglobal.com/Public/Home/PressRelease/2851b1ead435484bb938294bf3d8bcfd returned HTTP 200 `application/pdf` on November 6 (403 on November 4), 2 pages, sha256 eee11a7a…afd292. The issuer's public index lists that exact ID as "S&P Global US Manufacturing PMI", November 2 14:45 UTC. Headline 54.9 agrees with the commentary PDF already on file. ⚠️ The PDF's creation stamp is October 28, before the embargo; that is a production clock, not a publication date. The body's "input cost inflation surged higher in September" is quoted as printed; its context is the October release.

| Frozen R1 branch (wording unchanged) | Grade | Decisive text, page 1 unless noted |
|---|---|---|
| Toward real end-demand: orders faster than September AND output faster AND demand broadened beyond precautionary stockbuilding | **NOT-MET** (was CANNOT-FIRE) | "both registered slower growth rates compared to September"; new work rose "at the slowest rate since March". Two necessary legs fail, so the third cannot rescue it. The release cites "generally stronger market demand" but makes no claim of broadening beyond stockbuilding, and still reports "some reports of clients seeking to secure orders and lock in prices" |
| Toward borrowed / rolling over: orders contracting AND input stocks rising AND rise tied to precautionary buying | **NOT-MET** (unchanged; direction now known) | Orders rose. Input inventories rose, "modest growth recorded for a seventh successive month" (page 2). Buying was tied to securing stock and prices, "as firms sought to secure stock and present prices wherever possible", but the necessary contraction leg fails |

The October referent is now fully graded. R1 stays "mixed, selective upturn". No P1 routing, because no branch fired.

Other final composition, for owners: output prices highest since September 2022; input costs highest since May; supplier lead times longest since August 2022; backlogs up an eighth month, steepest since April; hiring steepest in five and a half years, since April 2021; new export business up fractionally, first rise since June 2025, tariffs limiting gains. Demand "especially for AI-related goods and equipment" is the chief economist's characterisation, with no measured AI share.

## 2. Computer imports — single current vintage

PRIMARY-VERIFIED: Census `https://www.census.gov/foreign-trade/statistics/historical/imports_enduse.xlsx`, HTTP 200 November 6 (403 on November 4), sha256 b17704c2…8e97b9, 54,234 rows, January 1994 to September 2026, end-use codes 21300 COMPUTERS and 21301 COMPUTER ACCESSORIES, dollars. It reconciles to FT-900 Exhibit 8, which the workbook labels "Part A: Seasonally Adjusted"; the file itself carries no adjustment label, so the SA basis is inferred from that match. The API still redirects to Missing Key and no key was created.

| Measure, computers plus accessories, nominal | Single vintage November 6 | November 4 mixed vintage | Difference |
|---|---:|---:|---|
| Q2 2026 | $150,332.7M | $150,333M | rounding |
| Q3 2026 | $193,386.7M | $193,387M | rounding |
| Q3 vs Q2 | +28.639% | +28.639% | none |
| January-September 2026 | $486,110.3M | $486,110M | rounding |
| January-September 2025 | $249,334.4M | $249,334M | rounding |
| YTD y/y | +94.963% | +94.963% | none |
| **September 2026 vs September 2025** | **$72,631.9M vs $28,941.9M, +150.96%** | not available | new |
| **Q3 2026 vs Q3 2025** | **$193,386.7M vs $89,136.9M, +116.95%** | not available | new |

The only monthly difference is May, $50,148.1M vs $50,149M, which is separately rounded components. J1's import leg no longer needs its mixed-vintage caveat. The physical-demand contraction warning stays NOT-MET. Imports are nominal, not deflated, and not AI-only. VULCAN owns the thesis verdict; a timing surge ahead of tariffs or supply limits is not ruled out by this count.

## 3. Parker-Hannifin FY2027 Q1 — eight cells

PRIMARY-VERIFIED: release November 5, 2026, quarter ended September 30, issuer-hosted Exhibit 99.1. Corporate NSA. Full cells in `companies/PH.md`.

| Cell | Read |
|---|---|
| Orders / backlog | Rolling 12-month orders +13% vs rebased FY26 Q4 +12%. North America +11% (+9%), International +14% (+10%), Aerospace +14% (+18%). Backlog record $13.7B vs $12.8B June 30. ⚠️ Filtration Group closed August 13, inside the quarter; the backlog is not split, and the orders note excludes divestitures but is silent on acquisitions. Organic backlog growth is NOT-STATED |
| Guidance | Organic growth 7.5-10.5% vs 5.5-8.5%, the only like-for-like sales raise. Adjusted margin 27.7-28.1% vs 27.5-27.9%. Adjusted EPS $36.45-37.25 vs $34.25-35.25 and reported sales 16-19% vs 5.5-8.5%, ⚠️ new ranges include Filtration Group, old ones excluded it |
| Price vs volume | Sales $5,992M, +18%; organic +11.5%, acquisitions +7%. Split NOT-STATED. Organic: NA +9.4%, International +11.6%, Aerospace +13.9% |
| Tariff | IEEPA returns to customers reduced sales $27M, partly offset by $6M received from the government, $21M net adjustment. Refund accounting, not incremental tariff cost. Incremental cost NOT-STATED |
| Inventory | Own inventories $3,640M vs $3,166M June 30, includes acquired stock; operating cash use $232M. Customer destocking NOT-STATED |
| AI / grid | NOT-STATED in the release. Call transcript not read: no free transcript found, and Quartr is off limits |
| Capex | Q1 $109M vs $89M. FY27 about $625M vs FY26 actual $459M, includes Filtration Group; prior guide not in the August exhibit |
| Key sentence | "We experienced increased demand across all market verticals, resulting in double-digit organic sales growth and record backlog levels." |

Cycle read: firmer than Emerson on breadth. It qualifies itself in two places: aerospace orders slowed on the same 12-month basis, and International is APAC +23% against EMEA +4% and Latin America -1%. No conclusion comes from the basis change; +13 vs +12 is on one method.

## 4. ATA September tonnage

ATA's public news and data pages still show the September advance as newest (114, SA, 2015=100, October 20). ATA states subscribers receive the monthly report on the first Friday, which is today, and that report is paid. **No public final exists at this check; none was bought.** Row retired as instructed. The ledger's successor pointer now names the next public ATA release, which normally restates September; that date is an availability check, not an issuer date.

## 5. Bellwether calendar audit

| Company | Issuer page, November 6 | Result |
|---|---|---|
| GE Aerospace | HTTP 200; newest event is the Q3 webcast (file names 10202026) | No date shown |
| 3M | HTTP 200; newest earnings October 20; November 4 Investor Update is not earnings | No date shown |
| Caterpillar | investors.caterpillar.com HTTP 200; Upcoming Events empty | No date shown |
| Emerson | HTTP 200; newest November 4 | No date shown |
| Parker | HTTP 200; newest November 5 | No date shown |
| Deere | HTTP 200; earnings section empty in fetch | No date shown; November 12 row unchanged |
| Honeywell | HTTP 403; search of issuer domains found only prior-year notices | UNKNOWN, not "unannounced" |
| Union Pacific | HTTP 403 after a timeout; search of issuer domains found only prior-year notices | UNKNOWN, not "unannounced" |

**No date promoted.** Prior-year notices show Honeywell announced on January 2, 2026 and Union Pacific on January 20, 2026, which is why a November page is expected to be silent, but that pattern dates nothing. Recheck folded into the existing December 31 calendar row, so no new row was added.

## 6. Survey-band calibration — proposal only, nothing registered

Scope is the two survey candidates. Script `survey_calibration.py`, output `SURVEY_CALIBRATION.json`, no network.

| Candidate | Sample | Result | Reading |
|---|---|---|---|
| ISM new orders minus inventories <0 for two first-published prints | 60 months January 2021-December 2025 | 22 negative months; 15/59 pairs (25.4%); 3 episodes | Too short: essentially one cycle. Current +4.1 (October). 17/60 months at or above it |
| Same, >0 twice (recovery side) | same | 30/59 pairs (50.8%); 5 episodes | Common, so weak as a signal |
| Regional ≥3 of 5 negative, two panels (deterioration) | complete panels to October 2026 | 74/268 (27.6%) full; 42/119 (35.3%) recent; 72/251 (28.7%) ex-pandemic | Unchanged in substance; reproduces the frozen counts. September and October are 1 of 5, so not met |
| Regional ≤1 of 5 negative, two panels (recovery side, new) | same | 134/268 (50.0%); 61/119 (51.3%); 121/251 (48.2%) | True about half of all pairs, so it barely discriminates. ⚠️ September and October do satisfy it; that is a description, not a fire, because nothing is registered |

⚠️ **ISM history source:** DBnomics mirror, free, SECONDARY-SOURCE, indexed January 7, 2026, ends December 2025, and is not a paid product. Control, read directly from ISM-authored PR Newswire tables: December 2025 first-published new orders 47.7 and inventories 45.2, and that release's November comparators 47.4 and 48.9, all match the mirror exactly. The January 2026 table then shows December revised to 47.4 and 45.7, which moves the spread from +2.5 to +1.7. So a revision of about 0.8 points exists, and near-zero spreads can change sign. Two months verify the mirror for those months only; its vintage elsewhere is UNKNOWN. The mirror's PMI headline series reads about 10, not a PMI, and is rejected. ISM PDFs for 12 tested months returned 404.

**Recommendation: register no survey band.** The recovery candidates fire about half the time, the ISM sample is one cycle, and Will asked for fewer rules. Remaining gaps: ISM before 2021 and January-August 2026 (ISM's monthly PR Newswire releases are readable by ordinary GET, tested on December 2025 and January 2026; February-August were not read and nothing depends on them today), and first-release history generally. Calibration row re-dated to the January 29, 2027 R0 review.

## Scores, bands, gates, thresholds moved

**None.** Mechanism scores stay 18/35 raw and 13/25 shared-root. ISM <47 is unchanged and NOT-FIRED on 55.5. The one grade change, R1 toward-real CANNOT-FIRE to NOT-MET, is what the frozen letter requires once composition is recovered. J1 and J2 conditions are unchanged. No prediction row was added.

## Limits

Parker's transcript, price/volume split and organic backlog are not available. Honeywell and Union Pacific dates are UNKNOWN because their pages refused access. VX-ISH-08 stays unscored and outside this assignment. AAR-BREADTH's unparsable release date stays UNKNOWN until December 2.
