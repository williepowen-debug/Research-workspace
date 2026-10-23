# KRE/QQQ negative-correlation episodes — mechanical study (TERRY, data 2006-06-22 → 2026-10-22, 5116 bars)

Rule: signal = first close with 20-session correlation of daily returns ≤ −0.24; re-arms only after it closes back above 0. Outcomes from the signal close. yfinance auto-adjusted closes. Small sample: every row is one episode.

**Episodes found: 14** — 13 completed plus the current one (signalled 2026-10-22, threshold -0.2357).

## Every episode

| Signal | Direction | 10y over prior 20d | VIX | KRE +20 | QQQ +20 | Ratio +20 (divergence dir.) | Class @20 | KRE +40 | QQQ +40 | Both fell ≥5% (40d) | Both rose ≥5% (40d) | First day both ≤−1% | Corr > 0 after |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---:|---:|
| 2013-07-25 | KRE over QQQ | +0.07 pts | 13.0 | -0.3% | +1.6% | -1.9% | FLAT | -4.0% | +5.7% | no | no | 15 sessions | 10 sessions |
| 2016-12-06 | KRE over QQQ | +0.57 pts | 11.8 | +2.3% | +3.7% | -1.4% | FLAT | +3.3% | +7.8% | no | no | — | 15 sessions |
| 2017-06-15 | KRE over QQQ | -0.05 pts | 10.9 | -0.5% | +2.4% | -2.8% | FLAT | -5.5% | +2.4% | no | no | 39 sessions | 39 sessions |
| 2017-11-29 | KRE over QQQ | +0.00 pts | 10.7 | -0.2% | +2.1% | -2.3% | FLAT | +5.4% | +10.8% | no | YES | — | 20 sessions |
| 2019-02-27 | QQQ over KRE | -0.02 pts | 14.7 | -10.1% | +2.7% | +12.4% | CONTINUED | -3.1% | +9.9% | no | no | 6 sessions | 3 sessions |
| 2020-07-28 | QQQ over KRE | -0.06 pts | 25.4 | +5.8% | +11.3% | +4.9% | CONTINUED | -8.3% | +2.9% | no | YES | 29 sessions | 30 sessions |
| 2020-11-11 | KRE over QQQ | +0.24 pts | 23.5 | +9.3% | +4.4% | +4.7% | CONTINUED | +24.4% | +8.7% | no | YES | — | 18 sessions |
| 2021-01-06 | KRE over QQQ | +0.11 pts | 25.1 | +4.5% | +7.4% | -2.7% | FLAT | +19.1% | +0.4% | no | YES | 14 sessions | 16 sessions |
| 2021-03-30 | KRE over QQQ | +0.31 pts | 19.6 | +2.3% | +7.9% | -5.1% | SNAP-BACK | +3.8% | +6.3% | no | YES | 16 sessions | 14 sessions |
| 2021-06-14 | QQQ over KRE | -0.13 pts | 16.4 | -5.3% | +5.3% | +10.1% | CONTINUED | -1.6% | +6.6% | no | no | — | 23 sessions |
| 2024-03-18 | QQQ over KRE | +0.05 pts | 14.3 | -3.0% | -1.5% | +1.6% | FLAT | +7.9% | +1.9% | no | no | 30 sessions | 11 sessions |
| 2024-07-05 | QQQ over KRE | -0.02 pts | 12.5 | +12.3% | -9.6% | -24.1% | SNAP-BACK | +20.6% | -4.0% | no | no | 13 sessions | 19 sessions |
| 2024-12-05 | QQQ over KRE | -0.25 pts | 13.5 | -7.9% | +0.7% | +8.6% | CONTINUED | -1.8% | +1.1% | no | no | 9 sessions | 2 sessions |
| 2026-10-22 | KRE over QQQ | -0.21 pts | 19.0 | — | — | — | nan | — | — | — | — | — | — |

## Summary over the 13 completed episodes (current one excluded)

| Outcome at +20 sessions | Count |
|---|---:|
| CONTINUED | 5 of 13 |
| FLAT | 6 of 13 |
| SNAP-BACK | 2 of 13 |

| Within 40 sessions (n = 13 complete) | Count |
|---|---:|
| Both KRE and QQQ fell ≥5% at some point | 0 |
| Both rose ≥5% at some point | 5 |
| A day with both ≤ −1% occurred | 9 (median 15 sessions in) |
| Correlation back above 0 within 20 sessions | 10 of 13 |

| Median from signal | +5 | +10 | +20 | +40 |
|---|---:|---:|---:|---:|
| KRE | -0.2% | +0.5% | -0.2% | +3.3% |
| QQQ | +1.4% | +2.3% | +2.7% | +5.7% |
| Ratio, divergence direction | -1.2% | -1.7% | -1.4% | -2.4% |

## Split by rate direction (10y change over the 20 sessions before the signal)

| 10y | Episodes | Class @20 (C/F/S) | Both fell ≥5% in 40d | Both rose ≥5% in 40d |
|---|---:|---|---:|---:|
| Falling | 6 | 4/1/1 | 0 of 6 | 1 of 6 |
| Rising | 7 | 1/5/1 | 0 of 7 | 4 of 7 |

**Current episode:** signalled 2026-10-22, corr -0.24, direction KRE over QQQ, 10y -0.21 pts over the prior 20 sessions, VIX 19.0. Sessions observed since signal: 0.

## Sensitivity — same rule at other thresholds (completed episodes only)

| Threshold | Episodes | Class @20 (C/F/S) | Both fell ≥5% in 40d | Both rose ≥5% in 40d |
|---:|---:|---|---:|---:|
| -0.15 | 16 | 4/9/3 | 0 | 6 |
| -0.20 | 13 | 3/7/3 | 0 | 5 |
| -0.24 | 13 | 5/6/2 | 0 | 5 |
| -0.30 | 10 | 3/5/2 | 0 | 4 |
