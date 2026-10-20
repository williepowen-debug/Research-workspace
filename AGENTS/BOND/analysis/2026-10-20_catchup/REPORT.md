# BOND catch-up — October 20, 2026

**Capture:** 11:55–11:57 ET; OpenAI Codex, session `01a15a02-565d-76c1-9d89-07653c5d3b62`. Scope: Will's instruction to catch BOND up to live news and files. Primary bytes and retrieval receipts → `raw/manifest.json`, `raw/extra-manifest.json`; computations → `derive.py`, `derived.json`. Live source frontiers differ: Treasury October19; ICE/FRED October19; ACM October16; FR2004 October7; repo October19; vendor October20 intraday. No current claim below is an executable quote.

## Judgment

**The long end still clears at expensive yields; credit deterioration is the more persistent warning.** Monday partially reversed last week's Treasury rally, while CCC spreads widened further even as headline HY tightened. Dealer Treasury and credit stocks moved in opposite directions in their latest lagged week. Neither a generalized dealer retreat nor a U.S. funding seizure is established. Composite remains **17/35**; auction counter **2**. No research threshold or score changes. Existing approval reconciliation changes the recorded posture, not a trade: WQ357 already approved selling the remaining TBT five on October15; October20 FORGE still shows five, with no sale fill evidenced. NO-ADD stands. BOND executes nothing.

## 1. Treasury curve: official primary is newer than the mirror

| Official Treasury close, % | Oct14 | Oct15 | Oct16 | Oct19 |
|---|---:|---:|---:|---:|
| 2Y | 4.82 | 4.77 | 4.74 | 4.77 |
| 5Y | 5.00 | 4.91 | 4.89 | 4.94 |
| 10Y | 5.19 | 5.10 | 5.09 | 5.15 |
| 20Y | 5.57 | 5.48 | 5.47 | 5.53 |
| 30Y | 5.52 | 5.43 | 5.43 | 5.48 |
| Real 10Y | 2.84 | 2.78 | 2.74 | 2.80 |
| Real 30Y | 3.24 | 3.18 | 3.16 | 3.21 |
| 10Y nominal minus real | 2.35 | 2.32 | 2.35 | 2.35 |

Source: [Treasury nominal](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv), corresponding real CSV, retrieved October20. Monday 10Y **+6bp = real +6 + fitted-par compensation 0**; 30Y **+5 = real +5 + compensation 0**. October14→19 nominal 10Y −4 = real −4 + compensation0; 30Y −4 = real −3 + compensation−1. Nominal-minus-real is fitted-par subtraction, not pure inflation expectations. The October15 rally is now confirmed at **−9bp** in both 10Y and 30Y, rather than left provisional at vendor ~−10.

FRED's DGS/DFII set still ends October16: **5.09 / 5.43 / 2.74** for 10Y/30Y/real10. Do not date these October19 or combine October19 breakeven with October16 nominal. Treasury 2026-file scan through October19: 30Y≥5.00 **89/200** observations, trailing run **73**; real10≥2.50 trailing run **27**. These counts use published sessions, inclusive ≥; not calendar days. The existing FRED-keyed sustain gate remains MET independently; primary-frontier counts do not back-score it.

Vendor October20 at 11:40 ET: 5Y4.918 / 10Y5.109 / 30Y5.430; ^VIX17.88. These are evolving Yahoo bars, not official closes or gate inputs. CBOT vendor strip captured 11:55: November implied3.920 vs EFFR3.88 = +4bp, approximately16% of one +25bp step for October28 under the hold-or-hike assumption; peak available strip4.650 in September2027. Not CME settlement, FedWatch, OIS or ORACLE odds.

ACM issuer workbook independently re-pulled, matching HENRY's repair: October16 fitted10Y5.066819 = expected-rate4.310617 + premium0.756202%. October7→16 delta **−20.597bp = expected +2.261 + premium −22.858**. This is the model's accounting, not causal identification of buybacks versus haven demand. Kim-Wright1.0729% ends October9; different model/window. [NY Fed workbook](https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls).

## 2. Credit: lower-quality tail worsens while index pauses

| ICE OAS, bp (FRED mirror) | Oct14 | Oct15 | Oct16 | Oct19 |
|---|---:|---:|---:|---:|
| HY | 325 | 323 | 331 | 329 |
| CCC | 1282 | 1278 | 1297 | 1310 |
| B | 329 | 326 | 335 | 336 |
| BB | 199 | 197 | 203 | 200 |
| BBB | 104 | 105 | 106 | 108 |
| IG | 84 | 84 | 85 | 87 |

Source: `raw/BAML*.json`; [HY series](https://fred.stlouisfed.org/series/BAMLH0A0HYM2). October19 changes: **−2/+13/+1/−3/+2/+2bp** in table order. CCC−BB widens to **1110bp**. HY is21bp below350 and +66 from the263 anchor, **9–34bp short** of BOND's338–363 credit-equity band. The >320 sustain's three October14–16 cells are325/323/331 (WALTER delivery); RED/REGINALD/LIQUID own their consequences. No new index-short sizing authority follows.

The cash ETF proxy has also weakened: HYG/IEF z20 **−1.85 at October19 close**, **−1.79 October20 intraday**; LQD/IEF −1.32 / −0.93. Cash spreads were widening while the proxy fell: **co-movement, not an independently confirmed synthetic-leading-cash divergence**. HYG is cash credit, and duration mismatch with IEF remains a confound. True CDX and VIOLET's option-skew leg remain unobserved here. `cdx-proxy.txt` preserves the run.

[SIFMA October14 release](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics): total corporate issuance through September **$2,195.1B, +24.5% YoY**. That is lagged aggregate supply, not a live October HY-access test. The detailed download opens a contact form; no submission made. A comprehensive current pulled-deal census remains missing. October20 [Axios](https://www.axios.com/2026/10/20/ai-debt-coreweave-goldman) relays Goldman's view that CoreWeave can use project financing despite expensive unsecured bonds. The note itself and new financing terms were not obtained; this is counter-hypothesis context, not evidence that current financing is available at a particular cost.

## 3. Dealer stocks: Treasury rebuild, credit reduction

| NY Fed net Treasury stock, $B | Sep30 | Oct7 | Weekly change |
|---|---:|---:|---:|
| 7–11Y | 38.599 | 38.492 | −0.107 |
| 11–21Y | 56.961 | 57.842 | +0.881 |
| >21Y | 37.502 | 38.750 | +1.248 |
| Long-end total | 133.062 | 135.084 | +2.022 |
| 3–6Y | 52.885 | 54.933 | +2.048 |
| 6–7Y | 23.304 | 20.460 | −2.844 |

Primary: `fr2004_fetch.py`, live series break resolved dynamically; complete output `raw/fr2004.json`. **One total build after declines does not meet two consecutive builds**; stock score stays2. The11–21Y bucket rose in the week containing the October1 buyback. That weak test does not support a simple claim that dealers reduced that bucket to sell into the operation; offsetting flows and seller identity remain unobserved. It cannot establish who sold the specific bonds.

LIQUID's October19 primary-backed inventory report: four below-IG corporate buckets fell **$4.959B→$2.164B, −$2.795B/−56.36%**, same September30→October7 week. BOND consumes that corporate figure from its owner, not as an independent pull. Treasury up while credit down is **selective net-position adjustment**, not uniform balance-sheet retreat. Net stocks cannot distinguish long sales, shorts, hedges, customer distribution or capacity refusal. HYG/JNK share creations reported October16 counter a universal-redemption claim but do not identify settled cash flows. Evidence `AGENTS/LIQUID/research/2026-10-19_sweep/REPORT.md` via BOARD SIG-W-20261019-010.

NY Fed October19: SOFR3.87, IORB3.90, spread **−3bp**; SOFR99th3.95, **+5bp** over IORB; volume$2,888B. These public observations show no acute median repo stress. LIQUID remains partially instrumented: private collateral, lender decisions and offshore basis are not cleared. Its LIQ-07 no-reserve-accompaniment result is not no possible funding loop; not a grade of BOND's separate September23 UNGRADED funding window.

## 4. Buybacks and near-term supply

[Treasury November dealer agenda](https://home.treasury.gov/system/files/221/Dealer-Agenda-November-2026.pdf), released October16, discussion page3: asks about larger buybacks' market-function/intermediation effects and future changes; separately asks about structural demand and future auction sizes. **No explicit 20Y-suspension proposal, new cap, yield target or adopted coupon cut.** Responses due October26 noon; meetings October29–30. November4 remains F1/F3 decision event. Consultative questions are not adopted policy.

October15 same-day-close bracket completed without altering the old dig: yield paid over interpolated curve **+10.3bp**, versus prior close+1.3 and vendor operation-window adjusted+11.4. Positive discount survives both contemporaneous comparisons. Rough30% DV01 offset remains the prior defined September10–October15 sample, not a continuously updated market-wide share. `buyback_bracket.py`, `buyback-bracket.json` preserve calculation. F2 carrier: five recorded stepped-up ops OFF-THE-RUN; nothing overdue; next October27.

Issuer schedule PDF visually checked by column: nominal20Y reopening **October21**, 5Y TIPS **October22**, 2Y **October26**, 5Y **October27**, FRN **October28**, 7Y **October29**; November nominal refunding November9/10/12. Feed checker alone verified nothing today; this is a separate issuer-calendar verification, not a silent rc0 upgrade. Preserve frozen October15 bars: 20Y I'<57.96; OLD indirect<52.47 AND dealer>17.59; BTC<2.36. TIPS OLD indirect<51.43 AND dealer>25.42; BTC<2.10; no I'. All percentages competitive accepted. Use manual frozen2dp comparator until the already-disclosed grader tie-band defect is repaired; no tool or threshold change this session. Treasury/Fed/ECB issuer calendars reconfirmed October28 FOMC and October29 ECB; UK Budget October28 is HANS-owned, prior official reference retained.

## 5. France and euro rates

Bundesbank fitted10Y **3.48% October20**, five-session change **−1bp** from October13. Eight prospective WQ400 observations October9–20: **0/8 meet** >3.25 AND strict rise>17bp. HANS's secondary OAT/Bund screen directly fetched: October19 **142.3bp**, October20 row **150.8bp** (OAT4.93/Bund3.42 rounded legs). Bond-fixing/final-close clock unverified; do not recompute precise spreads from rounded legs or substitute the Bundesbank fitted yield. Reuters October20 search text reports OAT4.96 intraday; direct body inaccessible. These are different times/bases, not conflicting same-clock observations. No new primary-confirmed BOND capital gate; VX19 stays3, HANS's existing T10 remains its owner's call. Do not invent a bank-funding transmission from sovereign widening.

WALTER's Eurostat September-final2.5% core print is the **first of two qualifying finals**, not a new fire; next October flash November4, final November18. Weekend France unrest is carried with source disagreement (550K Interior/800K organisers); the recycled Macron phrase dates2018. Neither a government collapse nor a dated censure vote is established by that packet. Political details are context, not BOND's new research lane.

## Forecast and remaining limits

**BND-32 registered October20, before October21 deadline:** 65% that October28 Treasury2s30s does **not steepen** versus October27 (delta≤0bp). Base rate: **5/6** completed2026 decision days non-steepening; raw changes −1,−5,−4,−15,+15,−8bp. Six is the minimum allowed sample; confidence is discounted from83% because a hold is largely priced, events differ and the sample is small. Not a trade edge claim or policy-channel attribution; full mutually exclusive branches and publication deadline in prediction ledger.

Remaining actual gaps: true CDX/options leg; synchronized CPI-morning TIPS; current pulled-deal/issuer-access census; private funding/offshore basis; original-vintage reconstruction for owner first-publication tests; future auction outcomes and November4 policy choices. Full-fleet discovery/native transport is unavailable in exposed tools; durable completion does not claim recipient consumption. Foreign WALTER dirty paths defer pull; no edits there. No new instrument, monitoring cadence, threshold, trade or external send.

## Existing R3 registrar carry recovered
The October1 verdict packet had been moved to processed without a located owner answer. BOND now answered every rejection/replacement by name in `PROME/inbox/2026-10-20_from-BOND_R3-watch-terms-disposition.md`: seven clean topic terms adopted/retained, noisy pulled-deal-query landing declined. No config change or real-recall guarantee claimed; no new feed or gate. Optional `workbook/LEDGER_GLOB` is absent; the standard runner still executes its ledger nudge, and KB/VX/FLOW were refreshed directly.

Read-cap pass identified prior rotation advisories. Rotated 10 completed docket rows verbatim to `domain/sources/2026-10-20_completed-catalysts.tsv`; no unresolved/future event removed. MEMORY remains unchanged at24,635B; its existing rotation advisory is noted for routine upkeep. Desk charter33,325B is outside the current manifest checker perimeter; this session explicitly read it, and did not alter charter instructions during research.

## Final selected macro-calendar pass
Issuer BLS/BEA/Treasury schedules checked throughNovember10: added missing GDP/PCE October29, ECI October30, borrowing November2, JOLTS November3, productivity November5, jobs November6, CPI November10 to the existing docket and STATUS twin (KB497). BLS GET403 was overcome by successful web issuer reads; transcribed schedule fields and BEA raw receipts saved. This is not a certificate of every minor/weekly release. Pre-closeout four-component check and post-update boot recompute each returnedrc0.
