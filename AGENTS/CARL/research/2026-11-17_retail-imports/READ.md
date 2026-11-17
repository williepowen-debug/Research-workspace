# October retail sales and import prices: CARL read (WALTER SIG-W-20261117-004)

**Written:** 2026-11-17 11:58–12:02 ET (`date`), CARL, Claude Code, Opus 5.5 (claude-opus-5-5), desktop; woken by PROME prome-19 (class C8). Derivation: `derive.py` → `pulled.json`, `derived.json` (FRED levels, vintage as published 2026-11-17).

## Sources and access

| Release | Primary read? | How |
|---|---|---|
| Census advance monthly retail, October 2026 (CB26-181, 08:30 ET 11/17) | **Yes** | `census.gov/retail/marts/www/marts_current.pdf`, text extracted; 15 component levels used below matched in the PDF table one for one |
| BLS import and export price indexes, October 2026 (08:30 ET 11/17) | **No: bls.gov returned 403 to an automated fetch; left alone, per root Data Hygiene** | FRED mirror of the BLS series (updated 2026-11-17 07:4x CT). BLS release text, its own rounding and any statement on 12-month changes were NOT read |

## 1. Retail sales (Census, seasonally adjusted, nominal)

| Measure | October m/m | September m/m (current vintage) | Note |
|---|---|---|---|
| Retail and food services | **+0.21%** ($748.2B) | +0.83% | Census: ±0.4%, the 90% interval includes zero; +6.8% y/y |
| Ex motor vehicles and parts (RSFSXMV) | **+0.63%** | +1.07% | |
| Ex autos and gasoline | **+0.52%** | +0.49% | |
| **Control group** (total less autos, building materials, gasoline, food services) | **+0.59%** ($405.5B) | **+0.53%** (first print, 10/15: +0.14%) | +5.6% y/y |
| Control, real (less core goods CPI +0.16%) | about **+0.43%** | | CARL arithmetic; CPI is a price index, not the Census deflator |
| Gasoline stations | +1.52% (+$1.03B) | | October gasoline CPI +1.04%, so volume roughly +0.5% |
| Motor vehicles and parts | **−1.60% (−$2.23B)** | | the whole gap between headline and ex-autos |
| Nonstore | +1.24% (+$1.57B) | | |
| Miscellaneous stores | +4.71% | | small, volatile |
| Health and personal care | +1.48% | | |
| Restaurants and bars | +0.25% | | food-away CPI +0.52%: real about −0.3% |
| Grocery and beverage stores | −0.18% | | food-at-home CPI +0.44%: real about −0.6% |
| Furniture −2.25%, clothing −0.75%, sporting goods −0.69% | | | |

Gasoline stations took **9.17%** of all retail and food-service dollars in October, against **7.52%** in October 2025: 1.65 points of the wallet moved to the pump in a year. Sales excluding gasoline stations rose **+4.9% y/y** against +6.8% total.

**September revision.** Census says the September change was "unrevised from up 0.8 percent" on its rounding. Both the August and September levels were revised up, so on unrounded levels September is +0.83% against +0.77% first printed. **The September control group moved from +0.14% to +0.53%.** My 10/15 read, "the nominal gain is the pump; core goods stalled", does not survive the revision: the crowd-out shows in the wallet share, not in a stalled control group.

## 2. Import and export prices (BLS via FRED, not seasonally adjusted)

| Index | October m/m | September m/m | Sep 2026 vs Sep 2025 | Oct 2026 vs Sep 2025 (13 months) |
|---|---|---|---|---|
| Imports, all | **+1.05%** | +1.06% | +8.1% | +9.2% |
| Imports, fuels and lubricants | +3.56% | +6.33% | +36.5% | +41.4% |
| **Imports ex fuels** | **+0.80%** | +0.51% | +5.9% | +6.7% |
| Imports ex food and fuels | +0.86% | +0.52% | +6.0% | +6.9% |
| Consumer goods ex autos | +0.53% | +0.27% | +2.6% | +3.2% |
| Autos and parts | +0.41% | +0.33% | +1.1% | +1.5% |
| Capital goods | +1.46% | +0.98% | +8.5% | +10.1% |
| Industrial supplies | +1.69% | +2.55% | +20.3% | +22.3% |
| Foods, feeds, beverages | −0.17% | +0.44% | +3.3% | |
| Exports, all | **+1.11%** | +2.40% | +11.8% | +13.0% |
| Exports, fuels | +4.66% | +9.28% | +37.9% | |

**Fuel versus ex-fuel.** The fuel weight the rounded indexes imply is about 9%. Fuel then contributes about **0.32 points** of the +1.05%, ex-fuel about **0.73 points: roughly 70% of October's rise is NOT fuel.** On index rounding alone, ex-fuel is +0.73% to +0.87% and the headline +0.99% to +1.12%; the majority-ex-fuel conclusion holds across that range.

**Year on year.** October 2025 is missing in FRED for every import series except foods (BLS did not publish it), so a true October y/y cannot be computed. The table gives September y/y and a 13-month change instead, labelled as such. Whether BLS published October 12-month rates is unknown: its release text was not reachable.

⚠️ Import price indexes exclude tariffs and duties. A rising index means foreign sellers are charging more in dollars, on top of any tariff, not that the tariff is being passed through.

## 3. What WALTER's card gets right and wrong

| Card claim | Verdict |
|---|---|
| Retail and food services +0.21% m/m to $748.2B | ✅ right |
| **"Ex-autos +0.21%" (RSXFS)** | ❌ **wrong series.** FRED RSXFS is "Retail Trade", which excludes food services and INCLUDES autos (the Census row labelled "Retail", 655,299). **Ex-autos is RSFSXMV: +0.63%.** Autos fell 1.6%, so the card's label hides the main composition fact of the month |
| September revised up to +0.83% | ✅ on unrounded levels; Census's rounded text says "unrevised from 0.8 percent". Both are true |
| Import prices +1.05%, exports +1.11% | ✅ arithmetic right on the FRED levels; BLS's own rounded figure not seen |
| "Whether it is fuel is the first question" | Answered: mostly not fuel |

## 4. Against CARL's written rules

| Rule | Result |
|---|---|
| Docket row 2026-11-17 (control group and T1-a/b/c at one vintage) | **Done** (this file) |
| T1-a grocery vs restaurants, real y/y | **AGAINST:** grocery −1.39% vs restaurants +3.17% ⚠️ October-2025 CPI not published; deflated with an interpolated October-2025 CPI (geometric mean of September and November 2025), labelled, not BLS |
| T1-b general-merchandise share of retail | **AGAINST:** 12.879% (Oct 2025) → 12.487% (Oct 2026), and down from September 12.496% (nominal, no CPI needed) |
| T1-c apparel, real y/y | **FOR, first time:** −0.51% (interpolated CPI, same caveat; tripwire only). Tier 1 turning for the leg is a strengthening, not a confirmation (TRADEDOWN_INSTRUMENTS anti-escape rule) |
| T1 overall | **2 of 3 against.** Leg still has no out-of-sample support; DG Q3 (about December) is the first real test. V8 holds 4 on other evidence |
| CRL-10 (food CPI y/y over 4.0%) | Not moved: food import prices −0.17% m/m. Stays 1% |
| CRL-32 (saving rate at or under 3.8% at 11/25 and 12/23, plus real DPI) | Not graded by this print. A real control group gain of about 0.4% points to positive real goods spending in October, which leans toward a low saving rate if income is flat. Direction only; no re-mark |
| Every other OPEN row (CRL-12, 13, 20, 22, 23, 28, 29, 30, 31, 34, 35, 36) | No instrument touched |
| Score | **53/70 v2.6.6 unchanged.** No vector trigger reads retail sales or import prices directly |

## 5. Consumer and goods-inflation read

1. **October spending was firm, not weak.** The +0.2% headline is autos (−1.6%). Underneath, the control group rose about 0.6% nominal, 0.4% real, after a September revised up to 0.5%. That is counter-evidence to a broad near-term spending break, consistent with the 10/12 scope review. It is aggregate, nominal and has no cohort split: it cannot say whether the bottom 60% is keeping up.
2. **The pump crowd-out is a share story.** Gasoline is 9.2% of the wallet against 7.5% a year ago. Households are paying it and still buying other goods in aggregate; who is drawing down savings to do it is the question CRL-32 asks on 11/25.
3. **The goods-price pipeline is building ex-fuel.** Import prices ex fuel rose 0.8% in October and 0.5% in September, about 6.7% over 13 months; consumer goods ex autos +0.5%. October core goods CPI was only +0.16%. Import prices exclude tariffs, so the rise sits on top of them. This bears on the Fed (V12 already at 5, HENRY's read), not on any CARL threshold. Logged as combo:goods-price-pipeline.
4. **What would move it:** BEA October income and outlays 11/25 (CRL-32 leg 1); Michigan final 11/20; November CPI core goods (pass-through test, mid-December); November retail 12/16 (does the control group hold?); DG Q3 about December (T2-a, the first out-of-sample test of the trade-down leg).

## 6. Not done

- BLS release text not read (403). Its rounded headline, any 12-month statement and its own fuel attribution are unseen.
- Auto dealer weakness not explained (prices versus units; tariff timing). No source read.
