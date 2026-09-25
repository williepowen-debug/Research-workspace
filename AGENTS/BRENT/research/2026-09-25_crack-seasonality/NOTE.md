# Realised crack seasonality, 2010–2025 — input to the WQ-252 month-basis sitting (10/06)

**Written:** 2026-09-25 10:1x–10:3x ET by BRENT (Will-directed: "yes go ahead", item #1 of the data-gap list). **Reproduce:** `.venv/bin/python3 AGENTS/BRENT/research/2026-09-25_crack-seasonality/crack_seasonality.py` (repo root). It writes `monthly.csv` beside this note. **Registers nothing, moves no bar, grades nothing.**

## Question
Boundary #8 (Brent 3:2:1 > $50) and #6 (gasoline crack) are flat bars on a *rolling* front month. The only seasonal evidence on file was the **forward curve** (9/14 pull, TRACKER), which shows what the market *expects*. HENRY's standing caveat: nobody had measured what cracks **actually did** each winter. This note measures it.

## Basis (read before citing any number)
- **EIA daily SPOT, 2010-01-04 → 2026-09-22, 4,155 matched days** [CONF EIA v2 `petroleum/pri/spt`]:
  - `RBRTE` Brent spot
  - `EER_EPMRU_PF4_Y35NY_DPG` NY Harbor conventional gasoline
  - `EER_EPD2DXL0_PF4_Y35NY_DPG` NY Harbor ULSD
- **Why spot:** EIA's front-month futures series (`petroleum/pri/fut`) **end 2024-04-05**, so they cannot cover 2024–26. Spot also has no contract rolls (LESSONS #23).
- ⚠️ **This is not the instrument #8/#6/F1 are specified on.** Those use NYMEX RBOB/HO and Brent futures. NYH conventional gasoline is not RBOB, and the Brent spot/futures gap is extreme right now: 9/22 spot **$114.89** vs BZX26 **$99.25**. **What transfers is the SEASONAL SHAPE, not the levels.**
- Monthly means of daily values, so these are **not settles**. **n = 16 winters.** 2020 (COVID) and 2022 (post-invasion) are regime years, included and flagged.
- 3:2:1 = (2×gas×42 + ULSD×42)/3 − Brent.

## Results (median across 16 years; IQR; count of years negative)

| Crack (spot, Brent basis) | Sep→Dec $ | Nov→Dec % | Nov→Jan % | Read |
|---|---|---|---|---|
| **3:2:1** | **−1.7** [−4.1, −0.3], 12/16 down | **−5.9%** [−24.2, −1.7], 13/16 down | **−10.6%** [−20.8, −0.5], 12/16 down | winter decline is the norm |
| **Gasoline** | **−3.4** [−6.0, −0.8], 13/16 down | −8.4% [−32.8, +2.9], 12/16 down | −15.2% [−24.1, +4.6], 11/16 down | strongest seasonal fall (includes the Sept RVP grade switch) |
| **ULSD** | +0.5 [−2.5, +3.2], 6/16 down | −8.4% [−19.8, −1.3], 12/16 down | −7.5% [−23.9, +5.0], 10/16 down | **rises Sep→Nov** (median +$2.7, 11/16 up), then falls into winter |

**Against today's forward curve** (named contracts):

| Curve | Priced step | Realised history |
|---|---|---|
| 3:2:1, 9/14 pull (TRACKER) | Nov→Jan **−10.3%** (49.14 → 44.06) | median **−10.6%**: the forward prices almost exactly the ordinary seasonal decline |
| 3:2:1, 9/24 settle-proxies | Nov→Dec **−3.6%** (50.12 → 48.32) | inside the realised IQR, milder than the −5.9% median |
| ULSD HO×42−CL, 9/24 settle-proxies | Nov 95.57 · Dec 94.73 · Jan 94.75 ⇒ **flat** | 9/25 ~10:20 ET intraday: 97.64 / 97.66 / 97.59, also flat. The usual −8.4% Nov→Dec is **not priced**. |

## What follows (assessment, for the sitting to weigh)
1. **#8 on a rolling month will drift below $50 on seasonality plus roll alone in most years.** The realised Nov→Jan fall is −10.6% of ~$50 ≈ **−$5**, and 12 of 16 winters fell. So a Dec- or Jan-basis read under $50 is **not evidence that refining stress eased**. Whatever basis 10/06 picks, a crossing should be read within ONE contract month, or against the seasonal norm. This backs WALTER's interim rule (a dispatch ships with its roll decomposition) with realised history rather than the forward alone.
2. **HENRY's caveat is answered on SHAPE, not on level.** The forward curve's slope matches 16 years of realised seasonality in %, so the 9/14 "the forward is the market's seasonal expectation" reading holds. The level still cannot be read off spot history, because the spot/futures basis is extreme now.
3. **F1 (Nov ULSD crack < $95, VLO scale-in filter, HENRY/TERRY) faces no roll step.** I tested whether the Nov→Dec roll would mechanically push F1 down, as history's −8.4% would suggest. **It does not: the Dec and Jan ULSD cracks are priced flat to Nov.** This also means the 9/22→9/24 drop (109.49 → 95.57) is **not** seasonal. It is a same-contract move, and ULSD historically *rises* into October/November.
4. **The flat ULSD forward curve is itself an observation.** The market is pricing no winter diesel-crack decline, against a 12/16-year history of one. That is consistent with distillate stocks at **12% below the 5-yr average** [CONF EIA WPSR wk-9/18]. Not tested further here.

## Limits
- Spot basis ≠ futures basis. n=16. Monthly means, not settles.
- The high-level-years subset (Sep avg > $20, n=4–6) shows larger % falls, but it is dominated by 2022/2023/2025 and is too small to lean on.
- No claim about **why** any single winter moved.
- Registers nothing. The 10/06 month-basis choice is Will's (WQ-252).
