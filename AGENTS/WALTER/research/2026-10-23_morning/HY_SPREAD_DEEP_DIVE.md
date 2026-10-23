# High-yield spread: where it stands — 2026-10-23 (WALTER, at Will's ask 10:32 ET)

Router's synthesis, not a grade. LIQUID owns spreads and funding; REGINALD/LIQUID own REG-T-04; RED owns FT-02/FT-07; BROCK owns private credit and leveraged loans. Data: FRED ICE BofA OAS series via `fetch.py` (`fred_fetch`, LATEST-REVISED, 786 observations 2023-10-24 → 2026-10-22, pulled 14:3xZ 10/23). The 10/22 HY bar is identical on the first-published basis (340). The 10/12 Columbus bar (311) is a non-session forward-fill.

## 1. Levels and moves (bp; 10/22 observation)

| Series | Level | 1 day | 5 sessions | 21 sessions | 63 sessions | 1-year percentile | 3-year percentile | 1-year range |
|---|---|---|---|---|---|---|---|---|
| HY (all) | **340** | +13 | +17 | **+67** | +59 | 99th | 86th | 260 – 346 |
| BB | 210 | +12 | +13 | +51 | +40 | 99th | 87th | 150 – 222 |
| B | 346 | +14 | +20 | +68 | +49 | 94th | 85th | 270 – 377 |
| CCC | **1,340** | +33 | +62 | **+247** | +339 | **100th** | **100th (3-year high)** | 838 – 1,340 |
| IG | 89 | +1 | +5 | +12 | +8 | 96th | 62nd | 73 – 94 |
| HY effective yield | 8.14% | | | +46bp vs 9/23 | +97bp vs 7/27 | 97th | 94th | |

## 2. Path

- 8/28 low 260 → 280 [9/24] → 324 [10/1] → 303 [10/6] → 331 [10/16] → 327 [10/21] → **340 [10/22]**: +80bp in eight weeks.
- The Iran-war shock peaked at **346 [3/30/2026]** and was back to 285 by late April; today is level with that peak.
- The CCC tier has risen almost every fortnight since April: 908 [4/27] → 1,034 [7/31] → 1,128 [9/25] → 1,253 [10/9] → 1,340 [10/22].
- Last close above 350: 353 [5/9/2025]. REG-T-04-style fires (third consecutive close >350) in the 3-year window: 10/26/2023, 1/4/2024, 1/15/2024, 8/6/2024, 4/7/2025.

## 3. Base rate (thin, stated as such)

Distinct prior episodes in the 3-year window where HY widened ≥60bp in 21 sessions: two. 8/5/2024 (yen-carry unwind) started at 393 and had already peaked; 3/13/2025 (tariffs) started at 340, exactly today's level, and peaked at 461 on 4/7/2025. **n = 2. This is not a probability.** It says only that a 21-session move this size has not, in this window, stopped short of 350.

## 4. What is driving it (sources and limits)

- **Weakest-first and broad:** every rated tier is near its one-year wide; CCC leads, and IG barely moved (+12bp in 21 sessions), so the HY−IG gap is ~251bp. This is a credit-quality repricing, not a rates move (the 10-year fell to ~4.95% on 10/22 as HY widened).
- **New-issue market shut (Bloomberg 10/21, via a syndicated copy; full article not read):** US high-yield sales ~$51B in September vs ~$7B in October to date; more than $5B of US and European debt sales put off this month, at least seven issuers (AVI-SPL $690M leveraged loan dropped; Freddie Mac >$440M MBS postponed; Circet €3B refinancing postponed); high-grade still clearing (Walmart and Kimberly-Clark ~$8B the same Monday).
- **AI concentration (unverified):** Connect CRE (10/21) says AI-related HY spreads widened 25bp in one day to a record 360 while non-AI moved 2bp, but names no index and no date ("last week"). It cannot explain 10/22 and is carried as color. LIQUID has no sector-breadth instrument. Same piece: CoreWeave 5-year CDS past 1,100bp, CoreWeave 9.625% 2032s ~79, SoftBank CDS +24bp to 424 (all unsourced).
- **Fund flows:** high-yield fund outflows reported for the weeks ending 9/30 (~$1.33B, BofA) and about 10/21 (~$1.68B, Lipper, global dataset, week unclear).
- **CCC yield, two indices:** Bloomberg CCC yield 15.7% (four-year high) vs FRED ICE CCC & lower effective yield ~18% [10/20–10/21] — different index families; not interchangeable.
- **Not yet in the plumbing (LIQUID, 10/22):** SOFR−IORB +2/+3bp, standing repo ~$0, reserves $2.96T; LIQ-07 resolved S2 "spreading-ordinary-repricing" (10/16). Banks: REGINALD's 10/22 read "HY widening not yet in bank instruments" (SIG-W-20261022-012); CREED: the CRE channel is the 10-year rate, not HY (SIG-W-20261022-015).

## 5. Trigger board

| Trigger | Line | State | Distance |
|---|---|---|---|
| REG-T-04 issuance freeze (REGINALD/LIQUID/Will) | > 350, 3 consecutive closes | not fired | 10bp; earliest fire = Tue 10/27 close, published ~Wed 10/28 (FOMC day) |
| RED-FT-02 / REG-T-03 | > 320 × 3 | fired (10/16 obs) | exits < 300 / ≤ 300 × 5, 40bp away |
| RED-FT-07 CCC | > 930 | firing-banked | — |
| Safety net | HY +25bp in one session | not met (+13) | — |
| LIQUID X1 HY leg | > 280 | met, 19+ consecutive | — |

## 6. Open questions for the owners

1. Is the 10/22 +13bp broad or AI-concentrated? No instrument on the fleet answers it (LIQUID NO_INSTRUMENT). An ICE sector sub-index or a few-name basket would.
2. The volume side of "issuance freeze" (Oct ~$7B vs Sep ~$51B) is ahead of the price trigger. Does REGINALD/LIQUID read the freeze as already under way?
3. Leveraged loans (BROCK): AVI-SPL's pulled $690M loan is one data point; is the loan market shutting with bonds?
