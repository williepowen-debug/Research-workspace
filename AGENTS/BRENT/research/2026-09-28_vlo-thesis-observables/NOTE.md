# VLO thesis: what would show it weakening, and how fast would we see it

**2026-09-28, BRENT, Will-approved bounded measurement (scope item 3: ≤1 hour, free sources, run after the current-state updates).** Clock 18:20–18:22 ET by `date`, well inside the hour. **$0.**

**What this does NOT do (per the scope):** infer ban effects, breach dates or an exit threshold from correlation. Noise figures describe **detectability only**. They are not thresholds. **Result: partly conclusive.** The observables and their latencies are clear. Effect sizes under a policy change are **not** measurable from this history.

**Data:** EIA v2 API daily spot, 2021-06-01 → 2026-09-22 (EIA's latest print, pulled 9/28), 1,323 matched dates. Series: NYH ULSD `EER_EPD2DXL0_PF4_Y35NY_DPG` · USGC ULSD `EER_EPD2DXL0_PF4_RGC_DPG` · Brent `RBRTE` · WTI `RWTC`. Raw file: [csv](eia_spot_2021-06_to_2026-09-22.csv); [script](pull_eia_spot.py) (writes to the session scratchpad; the copy here is the output).

**The VLO thesis, as the card states it** (TERRY card §8, BRENT's verbal falsifier): *"the crack IS the thesis"*. It is falsified by *"distillate crack rolls over hard; refiner runs destroyed by higher crude or demand destruction."* No numeric exit exists. That rule is TERRY's proposal, now commissioned (WQ-329 / DOCKET L535).

## Proxy definitions (explicit)

| Proxy | Formula | Unit | Why |
|---|---|---|---|
| **Gulf diesel margin** | USGC ULSD spot × 42 − WTI Cushing spot | $/bbl | Closest free proxy to a Gulf Coast refiner's diesel margin (VLO's system is Gulf-heavy). Crude leg is WTI Cushing, not the refiner's actual slate |
| **NYH diesel margin (Brent)** | NYH ULSD spot × 42 − Dated Brent | $/bbl | Waterborne/Atlantic basis |
| **NYH diesel margin (WTI)** | NYH ULSD spot × 42 − WTI Cushing | $/bbl | Spot twin of the F1 futures instrument (HOX26×42 − CLX26); same hub, spot rather than November |
| **Hub spread** | NYH ULSD − USGC ULSD | ¢/gal | Barrels trapped on the Gulf (export curb) should cheapen USGC vs NYH, widening this. Direction only; Colonial pipeline and Jones-Act limits govern how far |

## Current readings (EIA spot, latest 9/22)

| Proxy | 9/22 | 2026 YTD min / median / max | 2021-06…2025 p10 / median / p90 | 1-day Δ sd (Mar–Sep 2026) | 5-day Δ sd |
|---|---|---|---|---|---|
| Gulf diesel margin | **$113.25** | 25.1 / 63.9 / 114.5 | 18.0 / 28.1 / 55.5 | $5.07 | $8.83 |
| NYH margin vs Brent | $95.40 | 25.1 / 59.3 / 102.4 | 17.1 / 28.7 / 54.8 | $4.78 | $8.87 |
| NYH margin vs WTI | $113.88 | 31.4 / 67.3 / 121.7 | 20.2 / 32.6 / 59.8 | $4.95 | $8.86 |
| Hub spread NYH − USGC | **1.5¢** | −4.8 / 8.0 / 25.7 | 3.9 / 7.0 / 18.0 | 4.03¢ | 7.73¢ |

**Readings:**
- Diesel margins sit near their 2026 highs and about **2× the 2021–25 p90**.
- The hub spread is at the **bottom decile**: the Gulf is not trapped today; exports are pulling Gulf barrels. It fell from 17.2¢ (9/16) to 1.5¢ (9/22), a move that **predates** the 9/22 ban talk.
- Daily changes of the hub spread and the Gulf margin correlate at −0.24 (weak).

## ★ THE TABLE: what would show the VLO thesis weakening, and when we would see it

| # | Observable | Weakening looks like | Weakening mode it detects | Source · earliest visibility | Noise / caveat |
|---|---|---|---|---|---|
| 1 | **NYMEX HO crack, named month** (HOX26×42 − CLX26; F1's instrument) | Falls and stays down over several sessions, not one print | Any: crude-led squeeze, US policy, demand | yfinance intraday / settle-window proxy, **same day** (CME settle blocked on this box) | Spot-twin 1-day sd ≈ $5, so **F1's $1.23 cushion is inside one day's noise**. A single close means little. NYH-delivered, so it can lag Gulf harm |
| 2 | **Hub spread NYH − USGC ULSD** | **Widens** from ~1.5¢ (Gulf cheapening relative to NY) | **US export curb / ban** (barrels stranded on the Gulf) | EIA daily spot, **~4 business days' lag** (9/22 visible 9/28) | sd 4¢/day, 7.7¢/5d. Confounded by NYH-specific squeezes and Colonial (Oct-2022 went to 140¢ on an NYH squeeze) |
| 3 | **Gulf diesel margin** (USGC ULSD × 42 − WTI) | Falls while hub (#2) widens ⇒ Gulf-specific harm | Export curb; also a crude-led squeeze if WTI rises faster | EIA daily spot, ~4 business days' lag | sd $5/day, $9/5d. A WTI crude leg, not VLO's slate |
| 4 | **EIA weekly distillate exports** | Drop from 1.3–1.6 mb/d, **sustained over several weeks** | Voluntary curb or ban taking effect | WPSR Wed 10:30 for the week ending the prior Fri (**~5 days**) | Weekly range 1,331–1,935 kb/d in the last 8 weeks. **One week proves nothing** |
| 5 | **PADD 3 distillate stocks** | Build against the seasonal norm (44.4 M on 9/18; 2020 high 62.4 M) | Stranded barrels, i.e. the storage-fill path | WPSR weekly, ~5 days | Seasonal and turnaround-driven builds look the same |
| 6 | **Refinery utilization (US / PADD 3)** | Run cuts beyond turnaround season | "Runs destroyed": the storage-full stage, or margin collapse | WPSR weekly, ~5 days | Autumn turnarounds cut runs every year; 94% on 9/18 |
| 7 | **Distillate product supplied, 4-week YoY** | Sustained decline | Demand destruction (Path B) | WPSR weekly, ~5 days | Wholesale balance, not consumption (LESSONS #9) |
| 8 | **Policy act** (an executive order or IEEPA declaration; DOE voluntary-curb terms; refiner statements) | An order, or refiners agreeing to curbs | Export restriction | News: **session sweeps same day**; intake lane ~1 day (once-daily cadence; WALTER R3 9/28; terms landed d5d8c9e) | Talk ≠ order. Trump on record 9/22 and 9/27; no order as of 9/28 |
| 9 | **VLO vs XLE / VLO vs crack** | VLO lags the crack or XLE on margin news | Market pricing any mode | Intraday | Confounded: VLO tracked crude, not the crack, since 9/23 (TERRY rule-#23 read, corr +0.51 with USO) |
| 10 | **VLO Q3 results** | Realized Gulf margins and export volumes | All modes, realized | Quarterly; **late October (date not verified)** | Slowest; too late for a policy move |

**How fast, in one line:**
- a policy act is visible the same day (#8);
- futures margins react the same day but are noisy (#1);
- Gulf-specific evidence lags ~4 business days (#2–3);
- physical confirmation takes ~1–3 weekly prints, i.e. 1–3 weeks (#4–7);
- realized results arrive after about a month (#10).

**What "weakening" needs, descriptively:** agreement **across** rows (e.g. #1 down + #2 widening + #4 falling) beats any single row, because every single row has a confounder listed.

## 2022 comparison: DESCRIPTIVE ONLY (confounded; nothing inferred)

| Window | Hub spread start → max → end (¢) | Gulf margin start → max → end ($/bbl) | Confounders that dominate |
|---|---|---|---|
| Jun 1 – Jul 8 2022 (White House weighs export limits) | 12.5 → 12.5 → 7.0 | 57.5 → 75.1 → 48.4 | Broad summer crack collapse; crude fell; recession pricing |
| Aug 4 – Sep 1 2022 (Granholm letter 8/18) | 8.7 → 32.5 → 32.5 | 44.6 → 73.5 → 50.0 | Low NE inventories building into autumn; Colonial allocation |
| Sep 20 – Nov 15 2022 (limits floated in Oct) | 7.5 → **140.3** → 130.3 | 54.0 → 104.1 → 53.1 | **NYH distillate squeeze** (record-low NE stocks), Hurricane Ian, the run-up to the Russian product embargo |

In 2022 nothing was imposed. The hub spread's biggest move was an NYH squeeze, the **opposite** mechanism to Gulf trapping. **2022 gives no usable estimate of a ban's effect.**

## Limitations

- Spot proxies, not VLO's realized margins or crude slate.
- EIA spot lags ~4 business days.
- The noise statistics come from a high-volatility 2026 regime.
- There is no ICE gasoil feed, so the US-vs-world diesel spread, the most direct ban signal, **cannot be measured** here. It is listed for the paid-data question, which is deferred.
- **No exit threshold, breach date or ban-effect size is derived from anything above.**
