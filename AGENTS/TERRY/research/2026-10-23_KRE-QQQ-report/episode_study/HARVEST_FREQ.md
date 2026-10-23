# Step (b) — sellable drops during past episodes (TERRY; 13 completed episodes; baseline 254 non-overlapping 20-session windows since 2006)

A 'drop' = a 5-session close-to-close fall of at least the threshold, starting and ending inside the 20 sessions after the signal. yfinance auto-adjusted closes. MODEL-free (prices only).

| Threshold (5-session move) | KRE drop: episodes | baseline | QQQ drop: episodes | baseline | BOTH sides dropped at some point: episodes | baseline |
|---:|---:|---:|---:|---:|---:|---:|
| ≥2.0% | 85% (11/13) | 79% | 38% (5/13) | 64% | 38% | 57% |
| ≥2.5% | 77% (10/13) | 69% | 38% (5/13) | 53% | 38% | 44% |
| ≥3.0% | 62% (8/13) | 60% | 31% (4/13) | 45% | 31% | 37% |
| ≥5.0% | 54% (7/13) | 39% | 0% (0/13) | 22% | 0% | 17% |

## Per episode (≥3% drops over 5 sessions, within 20 sessions of the signal)

| Signal | Direction | KRE ≥3% drop | QQQ ≥3% drop | Sessions until corr > 0 |
|---|---|---|---|---:|
| 2013-07-25 | KRE over QQQ | no | no | 10 |
| 2016-12-06 | KRE over QQQ | no | no | 15 |
| 2017-06-15 | KRE over QQQ | yes | yes | 39 |
| 2017-11-29 | KRE over QQQ | no | no | 20 |
| 2019-02-27 | QQQ over KRE | yes | no | 3 |
| 2020-07-28 | QQQ over KRE | yes | no | 30 |
| 2020-11-11 | KRE over QQQ | no | no | 18 |
| 2021-01-06 | KRE over QQQ | yes | yes | 16 |
| 2021-03-30 | KRE over QQQ | no | no | 14 |
| 2021-06-14 | QQQ over KRE | yes | no | 23 |
| 2024-03-18 | QQQ over KRE | yes | no | 11 |
| 2024-07-05 | QQQ over KRE | yes | yes | 19 |
| 2024-12-05 | QQQ over KRE | yes | yes | 2 |

**Runway:** sessions from signal until the 20-day correlation closed back above 0 — median 16, range 2–39; within 20 sessions in 10 of 13.
