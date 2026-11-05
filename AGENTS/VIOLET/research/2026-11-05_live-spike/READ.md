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
| VIX closed above VIX3M on the day (inverted), VIX lower 20 sessions later | 7 of 8 |

Exceptions at 20 sessions: 1990-07-23, 2020-02-24. 2015-08-21 reached 40.74 before fading. Median S&P +1.67% at 20 sessions. Limits: small sample, one clustered regime mix, today's close unknown, and these are conditioned on a close.

## Close update, 16:51 ET

Close print, Cboe 16:15:01 ET: VIX 28.18, +69.66%, third largest one-day rise of 9,308 sessions; COR1M 22.84, stock vol estimate 59.0. Variance 2.88x = correlation 2.40x and stock variance 1.20x, about 83% correlation by log share; the intraday read holds. Today closed inverted at 0.9067, so the inverted row applies: 8 episodes, all since 2013; VIX lower 5 and 20 sessions later in 7 of 8, higher close within 20 sessions in 4 of 8, exception at 20 sessions 2020-02-24. Of the 16 earlier episodes that closed under 30, 4 later closed at or above 30. Row label corrected: it read "Close under VIX3M", meaning the ratio under 1.000, which is VIX above VIX3M.

## Competing readings

1. Concentration unwind (Path B), leading. 2. Hedges lifted 11/04 then forced back on, inference, no flow data. 3. Credit-led payoff (Path A), weakest so far, and today's overlap with the 10/22 window is coincidence until credit confirms. Tell: broadening into banks, then index credit.

## Recommendations for Will, written 2026-11-05 14:0x ET after closeout (Will "yes to all" 16:41 ET; encoded, KB-VIO-377 and KB-VIO-378)

- **"Credit flat":** HY OAS 5-session change no wider than +25bp, first-published FRED, same 5 sessions as the VIX move. `credit_flat.py`, 93 VIX +30%-in-5-days episodes since 1996, 20-session spacing: HY widened another 50bp+ within 20 sessions in 6 of 52 at or under +25bp, 11 of 40 above it; no difference between the under +10 and +10 to +25 buckets (3 of 31, 3 of 21). Ordinary 5-day HY move: median 11bp, 75th percentile 22bp. Exploratory; raw ICE series not committed.
- **MOVE pause/resume:** retire. Parent commission DOCKET L163 is RESOLVED and GATE-VIO-RV1 is retired, so the line governs nothing. Keep MOVE.tsv, move.py and the convergence vector.
- **Desk CLAUDE.md:** replace the MAIL paragraph and its HERMES cite with what 5a already says; put 5a before 5b without renumbering; change "Position sizing → FORGE" to TERRY.
- **Memory index:** PROME's flow-rule pass, no decision for Will.
