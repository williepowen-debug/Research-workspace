# Sticky credit after a VIX fade, and VIX options into 12/16

**Asked by:** Will, 2026-11-25 19:58 ET ("Yes go ahead" on options 1 and 3 of VIOLET's 18:44 ET list).
**Written:** 2026-11-25, 20:04 ET (from `date`). Exploratory and unscored; no threshold, score or letter changed. KB-VIO-410.

## 1. Does credit that stays wide after a VIX fade predict a second vol leg?

**Method:** `sticky_credit.py` (rules fixed in its docstring before outcomes were read; output in `output.txt`).
- **VIX spikes since 1990:** a peak of 25 or more, at least 1.5 times the 20-session low, followed within 5 sessions by a 50% give-back. That gives 29 episodes at least 30 sessions apart.
- **Credit:** Baa minus 10-year Treasury (FRED BAA10Y), the only free daily credit spread back to 1990. FRED's ICE HY series now begins 2023-11-27, so HY is a cross-check only.
- **Classes:** STICKY means credit widened 5bp or more and had given back 25% or less of that widening on the fade day. FADED means a 50% or larger give-back, or no widening at all.

**Live case:** VIX low 19.30 [11/12], peak 35.89 [11/20], fade day 26.62 [11/23], 56% given back. Baa-10Y widened 13bp, with 15% given back at the fade and 0% on 11/24. HY widened 56bp, with 23% given back at the fade and 7% on 11/24. **STICKY on both series.**

| Next 20 sessions after the fade day | STICKY (n=18) | MIXED (n=4) | FADED (n=7) |
|---|---:|---:|---:|
| A close at 90% or more of the old peak (live: 32.30) | 6/18 | 2/4 | 2/7 |
| A close above the old peak (live: 35.89) | 3/18 | 1/4 | 1/7 |
| Back within 25% of the pre-spike low (live: 23.45) | 12/18 | 3/4 | 6/7 |
| Median VIX on day 20 as a share of the peak (live: 0.72 = 25.8) | 0.72 | 0.74 | 0.60 |

**Read:**
1. **Sticky credit is the normal state a few days after a VIX peak** (18 of 29 episodes), because credit lags vol (`research/credit_vix_lag/`). On its own it is not a warning.
2. **It does not predict a second leg.** A near-retest came in 6 of 18 sticky cases (33%) against 2 of 7 faded (29%). That is no separable difference at these sample sizes.
3. **It predicts a slower fade.** The median day-20 VIX is 72% of the peak with sticky credit against 60% with faded credit, and a full fade came in 12 of 18 against 6 of 7.

## 1b. Consequence for prediction 2' (VIX above 25 on each of the 10 closes 11/27 to 12/10)

The live bar is 25 / 35.89 = **0.697 of the peak**. I scaled it to each episode's peak and asked whether every close from F+3 to F+12 stayed at or above 0.697 × P, the live session spacing.

| Class (fade day at 70% of peak or higher; live 0.74) | Held all 10 |
|---|---:|
| STICKY | **5/10** (1998-09, 1999-08, 2007-08, 2007-11, 2022-05) |
| MIXED | 2/4 |
| FADED | 1/5 |
| All fade depths, STICKY | 6/18 |

**This disagrees with my earlier "about 88% to fail."** That figure came from the inversion sample (day-7 VIX under 31: held 0 of 6, since 2009). The two lenses differ:
- **The inversion lens** keys on the absolute VIX level, uses 2009 onward and has n=6.
- **This lens** scales to the peak, uses 1990 onward and has n=10. Its held cases cluster in 1998 to 2008, a slower-fading era.

**Revised view (unscored): 2' fails about 75%, from about 88%.** VIX at 25 or under by 12/02 stays at about 60%. VIO-PRED-11 (a close above 35.89 by 12/16): 3 of 18 sticky cases set a new high within 20 sessions (17%), so I hold about 22%; the registered 50% is frozen.

**Caveats:**
- **Wrong credit series:** Baa-10Y is investment grade and carries Treasury-curve noise; it is not HY. On the 2023-to-2026 HY overlap the class changes for 2024-08 (Baa STICKY, HY FADED, 62% given back), so the classification depends on the series.
- **Overlapping, hand-built sample:** the episode rules are mine, and the samples are small and overlapping.
- **Scaled bar:** the 0.697 bar is scaled to each peak, while 2' is an absolute 25. In this live case the two coincide.

## 3. VIX options positioning (`vix_options.py`; yfinance)

- **Open interest:** a snapshot shows the prior session's end-of-day open interest, so the 15:37 ET boot snapshot carries 11/24 and the 11/23 snapshot carries 11/20 (no snapshot was taken on 11/24). OCC posts 11/25 overnight.
- **Volume:** full-day 11/25 volume, from a 20:02 ET re-run. That re-run wrote OI 0 over the good OI (the known after-hours artifact; `_daily_log.py` does not treat 0 as null). I restored the OI fields from HEAD by hand and kept the new volumes. The defect is open.

| Expiry | Open-interest change, 11/20 to 11/24 EOD (two sessions) | 11/25 volume, calls / puts | Most active strikes, 11/25 |
|---|---|---|---|
| Dec 16 | calls +25,752 (to 2,975,408); **puts +167,241** (to 2,398,590) | 248,235 / **344,659** (C/P 0.72) | puts 18, 20, 21, 17, 19 (0.05 to 0.79); calls 25, 40, 29, 30, 42.5, 55 |
| Jan 20 | calls +30,472; **puts +93,194** | 103,313 / **235,610** (C/P 0.44) | puts 19, 20, 22; calls 35 (21,075), 60, 34, 85 |

**Read:**
- **Flow leaned to the downside strikes** on a day VIX rose 7%. Put open interest grew about 4.6 times as much as call open interest over 11/23 and 11/24 (260,435 against 56,224), and 11/25 put volume ran 1.4 times calls in Dec and 2.3 times in Jan.
- **That fits a market leaning toward the fade.** The direction is not established, because volume and open interest do not show who bought and who sold.
- **Upside interest has not gone away:** the Jan 35 calls were the most active Jan strike. The after-hours implied-vol fields are unusable (placeholder values).
- **Pricing:** the Dec 18 to 21 puts priced 0.13 to 0.79 against Dec futures at 25.03 [11/25 settle], so a settlement under 21 is priced as unlikely.

## Owners

Credit levels: LIQUID. Dealer gamma: HENRY. Nvidia: VULCAN. Trade construction: TERRY (not routed; no structure, and the view revision is unscored).
