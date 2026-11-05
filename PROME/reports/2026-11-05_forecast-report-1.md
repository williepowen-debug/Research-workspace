# Forecast report 1, 2026-11-05

**WQ-619 A.** This first report tests whether the fleet's calls grade consistently. It ranks no desk. Generator: `python3 PROME/tools/forecast_report.py`, on DAEDALUS's `scorecards/LEDGERS.tsv` and status map, four desks added locally, no ledger edited.

## Record-interpretation check

Two blind reads by a reader who saw row text only, never the tool's verdict. They check how the records read; they do not verify that any event happened.

| Read | Rows the tool had decided | Agreed on whether the event happened | Reversed | Reader could not confirm |
|---|---:|---:|---:|---:|
| Random 60 terminal rows | 47 | 42 | 0 | 5 |
| All 48 decided calls priced under 50% | 48 | 46 | 0 | 2 |

Eight rows sit in both reads. Stated probability matched on every row where the tool read one; the tool declined two MIDAS PROVISIONAL rows the reader could price. Five of the seven unconfirmed rows are text-limited: bare "CORRECT" or "MISS", an archived prediction, or a cell cut by the test's own length cap.

⚠️ This shows the rows read one way. It is not verification of the events or of the owners' grades: the reader checked no primary source. **IMPLEMENTED · TESTED (selftest 10 of 10, two blind reads of the output) · NOT INDEPENDENTLY VERIFIED as code.**

## Timing check, was the probability on record before the outcome could be known?

Will's bounded check, 2026-11-05 15:48 ET. Method and row-level results: `PROME/reports/2026-11-05_forecast-timing/` (`timing_check.py`, `rows.json`). For each scored row, the first date Git shows that exact probability, on the ledger row or on a desk line naming the row, against the earliest outcome date found in the row (Outcome cell or resolved date, on or after Date_Made). VERIFIED means the probability is on record at least one calendar day earlier. No probability was reconstructed or backfilled.

| Timing | Rows | Of which revised |
|---|---:|---:|
| VERIFIED before the outcome date, on the ledger row | 88 | |
| VERIFIED before the outcome date, on a desk line naming the row (weaker: same ID and percentage on a line) | 67 | |
| **VERIFIED total** | **155** | **22** |
| Same day, order within the day not shown | 19 | 2 |
| Probability first appears after the earliest outcome date found | 26 | 6 |
| No outcome date readable in the row | 14 | 1 |
| Probability not found in Git history | 6 | 3 |
| **Timing uncertain total** | **65** | **12** |

| Cut | Calls | Brier | Hit-rate baseline | Gain | Bootstrap 95% range |
|---|---:|---:|---:|---:|---|
| All scored | 220 | 0.228 | 0.250 | +0.022 | −0.005 to +0.044 |
| VERIFIED timing only | 155 | 0.233 | 0.250 | +0.017 | −0.017 to +0.046 |
| VERIFIED, ledger row only | 88 | 0.226 | 0.245 | +0.020 | −0.029 to +0.057 |
| Timing uncertain only | 65 | 0.216 | 0.243 | +0.026 | −0.019 to +0.062 |
| VERIFIED, without RED's owner-clarified rows | 140 | 0.235 | 0.250 | +0.015 | −0.021 to +0.046 |
| All, without the one midpoint row (RED-24) | 219 | 0.228 | 0.250 | +0.022 | −0.005 to +0.045 |

**Reading.** Excluding the uncertain rows does not change the fleet conclusion: a small positive gain whose range includes zero. It does change two probability groups on verified rows:

| Stated, VERIFIED rows only | Calls | Mean stated | Came true |
|---|---:|---:|---:|
| Under 30% | 17 | 17% | 12% |
| 30–49% | 30 | 39% | 40% |
| 50–69% | 55 | 59% | 47% |
| 70–89% | 48 | 77% | 71% |
| 90%+ | 5 | 92% | 40% |

The 50–69% group loses its match, and 90%+ falls on 5 calls. The midpoint row changes nothing.

⚠️ **Limits.** The outcome date is a proxy: the earliest date written in the row, not a verified public-release time, so an outcome could have been knowable earlier than any date in the cell. "After" is not proof of hindsight either: some dates are the registration date quoted back or a window start (OTTO-29, OTTO-30, REG-15), and MAR-10 and MAR-15 show a resolved date before their Date_Made, the March ledger rollout placeholder. A commit before the outcome does not exclude partial information already in the tape; a late revision inside a live window is allowed by the scoring rule. Example: OTTO-30 stood at 60%, was revised to 12% on 7/25, and missed on 8/14, so the score reads the 12%, not the 60%.

**Correction owed:** report 2 leads with the VERIFIED rows and shows all rows beside them. No ledger is changed.

## Result, all scored rows

Updated 2026-11-05 15:0x ET: 22 RED rows joined on RED's own convention line (a7efebead); those 22 rest on the owner's later statement, not an independently verified outcome, and were not in the blind reads.

**Rows read:** 508 across 31 desks, as of 2026-11-05. Open 142 · HIT 150 · MISS 120 · PARTIAL 13 · NO-VERDICT 22 · ANNULLED 28 · RESOLVED-UNTYPED 9 · UNMAPPED 24.
**Scored:** 220 of 270 decided calls carry a usable probability; 50 do not. 33 decided rows took their direction from the Outcome cell, the status alone said RESOLVED.
**Not read:** CARL and MARCO sub-agent ledgers, NEXUS markdown monitors, TERRY CALIBRATION.tsv, ORACLE, REGINALD's EGBN research copy; CORAL and SHADE have no ledger.

**Fleet Brier 0.228** on n=220. Always saying 50%: 0.250. Always saying the fleet hit rate (52%): 0.250. The second is the fairer baseline; beating it is what would show the percentages add information. Neither is a skill claim while calls overlap.
**Gain over the hit-rate baseline:** +0.022, bootstrap 95% range -0.005 to +0.044, treating calls as independent, which overstates certainty because many calls share one root.
Scored on the latest pre-outcome probability (WQ-112), which measures the final forecast; it may differ from the original early judgment, which stays preserved in each row.
**Disclosures:** 1 probability range(s) converted to a midpoint (RED-24); 22 scored rows take the event outcome from a later owner clarification, not from an independently verified outcome.

| Stated | Calls | Mean stated | Came true | 95% interval |
|---|---:|---:|---:|---|
| Under 30% | 24 | 19% | 12% | 4% to 31% |
| 30–49% | 38 | 39% | 37% | 23% to 53% |
| 50–69% | 90 | 58% | 56% | 45% to 65% |
| 70–89% | 58 | 76% | 71% | 58% to 81% |
| 90%+ | 10 | 93% | 60% | 31% to 83% |

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
| RED | 28 | 5 | 22 | 22 | 0 | 0 | 0 | 1 |
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
| RED-08: no instrument named, paper TRUE and physical FALSE, unreadable by RED's own line | 1 | None owed |
| Decided calls with no usable percentage: HENRY 33 (UNSCORED-AS-MADE), FERT 6, MIDAS 5, YURI 4, CREED 1, VIOLET 1 | 50 | Forward only, no backfill |
| Other untyped or unmapped terminal rows | 32 | Owner's next session |
| Shared-root calls | not machine-readable | Stated in Notes by owner; report 2 reads them |

## Report 2, December

Mean stated beside observed rate in each group · ranges converted to midpoints, with and without them · owner clarifications kept apart from independently verified outcomes · blind reads described as record-interpretation checks · a few examples, where available, of a recorded lesson changing a later comparable forecast. First candidate: LABOR held threshold calls at or under 60% on 11/5, citing its 0-for-6 record at 60% and above.

## Learning line, from report 2

Each resolved miss gets one line in the desk's own row: what surprised the desk, and what changes in its next comparable forecast. Report 2 also shows each desk's no-verdict rate.
