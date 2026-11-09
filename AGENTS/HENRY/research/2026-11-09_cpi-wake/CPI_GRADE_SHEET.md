# HEN-57 grade sheet: October 2026 CPI (BLS, Tue 2026-11-10 08:30 ET)

**Written 2026-11-09 12:1x ET, before the print** (Claude Code, Opus 5.5; PROME due-row wake, DOCKET L775). The letter is frozen at `research/2026-10-29_catchup/PREREG_nov-releases.md` and `workbook/PREDICTIONS.tsv` HEN-57. Nothing here changes it. This sheet only sets up the inputs and the grading procedure.

## The letter (frozen 10/29, quoted, not re-specced)

| Field | Content |
|---|---|
| Grading rule | BLS SA "all items less food and energy" m/m, first print, one decimal: **0.4 or higher = FIRED; 0.3 or lower = NOT FIRED** |
| Expectation | **NOT FIRED, at +0.2%** |
| NO-VERDICT | release postponed beyond 11/10 + 5 business days, series definition change, or first print unreadable at the agency or a mirror. A late grade is NOT NO-VERDICT |

## Inputs as of 11/9 (none moves the letter)

| Input | Value | Source, date | Note |
|---|---|---|---|
| Cleveland Fed nowcast, October | CPI **+0.24%** m/m, core **+0.21%** m/m | clevelandfed.org page, updated 11/09, saved `clevelandfed_nowcast_1109.html` | Unchanged from 10/29 (+0.24 / +0.21). Edge for a one-decimal 0.4 is 0.35: nowcast is 0.14pp under it |
| Consensus | core **0.22%**, headline **0.23%** (September 0.33% / 0.65%) | Bloomberg survey via @DeItaone on X, 11/9; not read at Bloomberg | Secondary relay of a survey |
| Low forecast | Goldman core 0.16% | TradingKey preview, 11/9 | Secondary |
| Year-over-year | may not be published: October 2025 was never collected (2025 shutdown) | FinancialJuice 11/9, **claim, unverified** | Irrelevant to the letter, which grades m/m on a September 2026 base. Other previews quote y/y forecasts anyway |
| Retail gasoline (NSA) | September weekly average $4.355, October $4.310: **−1.0%** | FRED GASREGW, weeks 9/7–9/28 vs 10/5–10/26, own calc | Not seasonally adjusted. October seasonal factors usually expect a fall, so SA gasoline could print near flat. Do not read −1.0% as the CPI gasoline print |
| Futures (10/29 letter) | RBOB −4.06%, heating oil −1.67%, Oct vs Sep monthly averages | vendor, 10/29 | Continuous series, approximate |
| September energy index | +5.20% m/m SA (321.148 → 337.834) | api.bls.gov CUSR0000SA0E | The base the October energy leg falls from |
| Release date | Tue 11/10 08:30 ET | Kiplinger, Bloomberg via X, FinancialJuice (secondaries); bls.gov returns 403 from this box | BLS page re-verify not possible here. DOCKET L775 date (BLS, read 10/21) stands |

**Read before the print:** the energy share should be small or negative after September's +5.2% energy jump, so headline and core should land close together, about +0.2 each. The war fuel path the DOCKET row names (Brent ~$108–110 through 10/21) hit **September**; October retail gasoline eased. The risk to my expectation sits in core (September core was +0.335% unrounded, and the nowcaster undershot September core PCE in the hot direction, DOCKET L774), not in energy.

## Grading procedure at 08:30 ET (primary first)

1. `api.bls.gov/publicAPI/v1/timeseries/data/<id>` for **CUSR0000SA0L1E** (core SA), **CUSR0000SA0** (all items SA), **CUSR0000SA0E** (energy SA), **CUSR0000SAH1** (shelter SA). Positive control: September core from the index = 338.896 / 337.765 − 1 = **+0.335% → 0.3**, which matches the published September 0.3. The API serves indexes, not the published percent; record the index-derived figure and, where press quotes the BLS one-decimal figure, check the two agree. If they disagree, the BLS release text governs: grade it once read and disclose which basis was used.
2. Grade the one-decimal core figure against the letter. Unrounded beside it, not graded.
3. Energy share of the headline: (headline m/m − core m/m × core weight) is approximate without weights. Report energy m/m and headline minus core instead; no relative-importance weights are loaded here.

## Market reaction to log (recorded, not graded)

| Read | Pre-print reference | Where |
|---|---|---|
| December hike odds, fed funds futures own calc | 76% at 15:00 ET 11/6 (ZQZ26 95.985, vendor last). **Rerun at 15:00 ET 11/10** | `research/2026-11-06_nfp/DECEMBER_HIKE_READ.md` method |
| 2Y par | 4.51% [Treasury 11/6]; HEN-62 needs >4.60 by 11/30 | Treasury par, evening |
| SPX vs map | gamma NEGATIVE on both horizons, flip ~7,660; **put wall 7,500 clean**, call wall 7,700 clean (11/9 ~12:1x ET, chain carries 11/6 trading) | `gamma_flip.py --both`, pre-open 11/10 |
| KRE direction | rate story = KRE up, credit story = KRE down (6/6 finding) | vendor |
| HY OAS | 342bp [FRED 11/6]; the 11/10 cell publishes 11/11 | FRED |

**The asymmetry going in:** since 9/24 the hike path and SPX moved together, and the one exception was the 10/14 CPI day: an inflation print adds hikes and does not cushion stocks. Dealers amplify below about 7,660 and the 7,500 put wall sits about 0.4–0.6% under the 11/9 midday tape. A hot core print is the case where the hike repricing and the dealer amplification point the same way.
