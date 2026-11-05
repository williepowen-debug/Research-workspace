# Forecast report 1, 2026-11-05

**WQ-619 A.** This first report tests whether the fleet's calls grade consistently. It ranks no desk. Generator: `python3 PROME/tools/forecast_report.py`, on DAEDALUS's `scorecards/LEDGERS.tsv` and status map, four desks added locally, no ledger edited.

## Consistency test

Two blind reads by a reader who saw row text only, never the tool's verdict.

| Read | Rows the tool had decided | Agreed on whether the event happened | Reversed | Reader could not confirm |
|---|---:|---:|---:|---:|
| Random 60 terminal rows | 47 | 42 | 0 | 5 |
| All 48 decided calls priced under 50% | 48 | 46 | 0 | 2 |

Eight rows sit in both reads. Stated probability matched on every row where the tool read one; the tool declined two MIDAS PROVISIONAL rows the reader could price. Five of the seven unconfirmed rows are text-limited: bare "CORRECT" or "MISS", an archived prediction, or a cell cut by the test's own length cap.

⚠️ This tests that the rows can be read one way. It does not test that the owners' grades are true: the reader checked no primary source. **IMPLEMENTED · TESTED (selftest 10 of 10, two blind reads of the output) · NOT INDEPENDENTLY VERIFIED as code.**

## Result

**Rows read:** 508 across 31 desks, as of 2026-11-05. Open 142 · HIT 141 · MISS 107 · PARTIAL 13 · NO-VERDICT 22 · ANNULLED 28 · RESOLVED-UNTYPED 31 · UNMAPPED 24.
**Scored:** 198 of 248 decided calls carry a usable probability; 50 do not. 33 decided rows took their direction from the Outcome cell, the status alone said RESOLVED.
**Not read:** CARL and MARCO sub-agent ledgers, NEXUS markdown monitors, TERRY CALIBRATION.tsv, ORACLE, REGINALD's EGBN research copy; CORAL and SHADE have no ledger.

**Fleet Brier 0.228** on n=198. Always saying 50%: 0.250. Always saying the fleet hit rate (53%): 0.249. The second is the fairer baseline; beating it is what would show the percentages add information. Neither is a skill claim while calls overlap.
**Gain over the hit-rate baseline:** +0.021, bootstrap 95% range -0.006 to +0.044, treating calls as independent, which overstates certainty because many calls share one root.

| Stated | Calls | Came true | 95% interval |
|---|---:|---:|---|
| Under 30% | 20 | 10% | 3% to 30% |
| 30–49% | 28 | 39% | 24% to 58% |
| 50–69% | 83 | 55% | 45% to 66% |
| 70–89% | 57 | 70% | 57% to 80% |
| 90%+ | 10 | 60% | 31% to 83% |

## Desk counts, alphabetical. Counts only, no desk score, no ranking

| Desk | Rows | Open | Decided | With a % | No-verdict | Annulled | Partial | Untyped or unmapped |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AEOLUS | 13 | 8 | 5 | 5 | 0 | 0 | 0 | 0 |
| BOND | 8 | 5 | 3 | 3 | 0 | 0 | 0 | 0 |
| BRENT | 31 | 2 | 21 | 21 | 3 | 3 | 2 | 0 |
| BROCK | 32 | 9 | 14 | 14 | 0 | 6 | 1 | 2 |
| CARL | 32 | 12 | 10 | 10 | 4 | 4 | 1 | 1 |
| CREED | 15 | 6 | 8 | 7 | 0 | 0 | 0 | 1 |
| CRUISE | 11 | 1 | 10 | 10 | 0 | 0 | 0 | 0 |
| CYPHER | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |
| FALCON | 7 | 1 | 5 | 5 | 0 | 0 | 1 | 0 |
| FERT | 13 | 1 | 8 | 2 | 0 | 2 | 2 | 0 |
| FLG | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| HANS | 11 | 5 | 6 | 6 | 0 | 0 | 0 | 0 |
| HAWK | 22 | 2 | 15 | 15 | 0 | 3 | 1 | 1 |
| HENRY | 54 | 3 | 33 | 0 | 6 | 0 | 3 | 9 |
| HOMER | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| LABOR | 23 | 8 | 13 | 13 | 0 | 2 | 0 | 0 |
| LIQUID | 11 | 5 | 4 | 4 | 0 | 1 | 0 | 1 |
| MARCO | 16 | 4 | 8 | 8 | 0 | 0 | 1 | 3 |
| MIDAS | 17 | 6 | 5 | 0 | 4 | 0 | 0 | 2 |
| OSPREY | 7 | 1 | 6 | 6 | 0 | 0 | 0 | 0 |
| OTTO | 20 | 6 | 12 | 12 | 0 | 0 | 0 | 2 |
| OZK | 12 | 7 | 5 | 5 | 0 | 0 | 0 | 0 |
| RED | 28 | 5 | 0 | 0 | 0 | 0 | 0 | 23 |
| REGINALD | 28 | 11 | 7 | 7 | 4 | 5 | 0 | 1 |
| SAM | 35 | 1 | 32 | 32 | 0 | 0 | 1 | 1 |
| VIOLET | 6 | 0 | 1 | 0 | 0 | 1 | 0 | 4 |
| VULCAN | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 |
| WAL | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 2 |
| WATT | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| YURI | 7 | 2 | 4 | 0 | 0 | 1 | 0 | 0 |
| ZHAO | 21 | 7 | 11 | 11 | 1 | 0 | 0 | 2 |

## What stays out, and why

| Gap | Rows | Owner fix |
|---|---:|---|
| RED: 23 rows say CORRECT or WRONG against a modal lean, so a row cannot show whether the stated event happened. Excluded rather than guessed | 23 | RED states the convention |
| Decided calls with no usable percentage: HENRY 33 (UNSCORED-AS-MADE), FERT 6, MIDAS 5, YURI 4, CREED 1, VIOLET 1 | 50 | Forward only, no backfill |
| Other untyped or unmapped terminal rows | 32 | Owner's next session |
| Shared-root calls | not machine-readable | Stated in Notes by owner; report 2 reads them |

## Learning line, from report 2

Each resolved miss gets one line in the desk's own row: what surprised the desk, and what changes in its next comparable forecast. Report 2 also shows each desk's no-verdict rate.
