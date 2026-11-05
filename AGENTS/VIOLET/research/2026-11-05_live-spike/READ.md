# 11/05 live spike: working read

**Written:** 2026-11-05 13:31 ET. Intraday, not closes. Exploratory: nothing here is pre-registered, and no line, gate or prediction changes. Script: `analogs.py`.

## Correlation did most of the work

VIX squared is about correlation times average stock variance. Ledger `IMPLIED_CORR.tsv`: COR1M 9.53 [11/04] to 18.03 [TICK], stock vol estimate 53.8 to 57.2, VIX 16.61 to 24.30. Variance rose 2.14x: correlation 1.89x, stock variance 1.13x, so about 84% of the log rise is correlation. Stock vol estimate was 51.5-55.5 from 10/29 to 11/04 while VIX ranged 16.61-21.15. The estimate is backed out of VIX and COR1M, so this is a decomposition, not independent evidence.

## Analogs: VIX close +35% or more from a prior close under 20, 20-session spacing, Cboe history

| Outcome | Count |
|---|---:|
| Episodes | 17 |
| VIX lower 5 sessions later | 14 of 17 |
| VIX lower 20 sessions later | 15 of 17 |
| Higher closing VIX within 20 sessions | 11 of 17 |
| S&P higher 20 sessions later | 12 of 16 with data |
| Close under VIX3M on the day, VIX lower 20 sessions later | 7 of 8 |

Exceptions at 20 sessions: 1990-07-23, 2020-02-24. 2015-08-21 reached 40.74 before fading. Median S&P +1.67% at 20 sessions. Limits: small sample, one clustered regime mix, today's close unknown, and these are conditioned on a close.

## Competing readings

1. Concentration unwind (Path B), leading. 2. Hedges lifted 11/04 then forced back on, inference, no flow data. 3. Credit-led payoff (Path A), weakest so far, and today's overlap with the 10/22 window is coincidence until credit confirms. Tell: broadening into banks, then index credit.
