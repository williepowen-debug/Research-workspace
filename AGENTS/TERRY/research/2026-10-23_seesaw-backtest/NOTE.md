# See-saw strategy model backtest — 2026-10-23 (Will-requested)

**MODEL, not fills.** Black-Scholes, no skew; KRE IV = scale × VIX, QQQ IV = scale × VXN (base 1.35 / 0.88, loosely calibrated to 10/23 quotes; sensitivity 1.1/0.75 and 1.6/1.0). Each leg: put 3% OTM, 60 DTE, rolled under 21 DTE; friction 5% (KRE) / 1% (QQQ) per buy and per sell; fractional contracts; $1,000 start ($500 per leg); marked at the 10/22 close. Data: yfinance closes `px.csv` (KRE/QQQ 121 bars, VIX 123, VXN 121, from 2026-05-01; VIX forward-filled to KRE/QQQ dates). Script `seesaw_bt.py`; full output `RESULTS.txt`.
Strategies: **hold** both legs · **rebalance** (Will's "sell buy sell buy": back to 50/50 whenever KRE/QQQ moves ≥3% since the last swap) · **harvest** (sell half a leg at +50% on its red day, park cash, redeploy to the other leg after the ratio turns 3% on that leg's green day).

Robust across all three IV settings: start date dominates (windows from 9/23 or later +24% to +156%; from 7/1 or 8/24 mostly −19% to −81%). In the trending window from 10/6, hold > rebalance > harvest every time (base +116.5 / +82.5 / +75.9). From 8/24, harvest best every time (−19 to −27 vs hold −47 to −56). Rebalance traded 20–32 times from 7/1–8/24 with ~$100–140 friction per $1,000. Harvest from 7/1 is FRAGILE (−61% to +56% across IV settings) — threshold path-dependence; do not cite one figure.

## Timing-signal test (11:3x ET) — MODEL, same pricing method
Entry: put 3% OTM, 60 DTE; exit after 20 sessions; friction 1% QQQ / 5% KRE each way. Entries every session 2024-01-02 → 2026-09-24 (685 per leg; 852 bars from 2023-06-01 for the 120-day vol percentile and 20-day average). ⚠️ Overlapping 20-session holds ⇒ effective independent N ≈ n_days/20 (e.g. QQQ "cheap AND stretched up" 81 days ≈ 4 episodes). Sample is mostly a bull tape.
| Leg | Condition at entry | n days | mean | median | win % |
|---|---|---|---|---|---|
| QQQ | all | 685 | −22.5% | −69.8% | 23 |
| QQQ | vol ≤25th pct AND ≥+2% above 20d avg | 81 | −13.5% | −72.4% | 30 |
| QQQ | vol ≥75th pct AND ≤−2% below 20d avg | 85 | −36.9% | −87.0% | 20 |
| KRE | all | 685 | −6.0% | −55.2% | 33 |
| KRE | vol ≤25th pct AND ≥+2% above 20d avg | 66 | +29.9% | −12.0% | 42 |
| KRE | vol ≥75th pct AND ≤−2% below 20d avg | 73 | −37.8% | −87.9% | 22 |
Readings 10/22 close: VXN 28.72 = 90th pct (120d), QQQ −4.44% vs 20d avg; VIX 19.03 = 93rd pct, KRE +3.47% vs 20d avg. Winning start dates 9/23 and 10/6: VXN 8th/12th pct, QQQ +3.29%/+3.86% vs 20d avg.
