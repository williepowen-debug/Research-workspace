# WATT — The winter demand test: does the demand half of the P1 trigger carry information on its own?

**Written:** 2026-11-19, WATT (Claude Code, Opus 5.5, laptop), PROME task letter of 2026-11-19 10:46 ET, read 10:46 ET. **Commission:** WQ-704, Will "yes" 2026-11-16 23:20 ET (brief `inbox/processed/2026-11-16_from-PROME_research-commission-WQ-704.md`). **Cost:** $0. **Moves:** no score, band, gate, threshold, prediction letter or charter line.
**Reproduce:** `python3 AGENTS/WATT/research/2026-11-19_winter_demand_test.py` (main tables; output `..._output.json`) and `... --conditional` (peak-hour tercile tables; output `..._conditional.json`), from the repo root. Inputs are files already held in `AGENTS/WATT/sources/` plus EIA-930 demand pulled 2026-11-19 10:47 ET into `sources/2026-11-19/`.

## The answer

**No: as written, the demand half does not separate stress from an ordinary cold morning.** In winter it is met in about one hour in five and on four days in five, almost always at the morning (07–09 ET) or evening (18–21 ET) peak, because it only asks whether this hour's load beats the highest load of the previous 24 hours, and every colder-than-yesterday peak does that. In the two calm windows held (autumn 2025, November–December 2025), once load level and hour of day are held roughly fixed, hours that met it spiked no more often than hours that did not. In the one window with real stress (autumn 2026) it did carry information: all seven hours averaging $1,000 or more were hours that met it, and among the highest-load peak hours it separated 12.5% from 0%; but that is three episodes, and plain high load picked out the same seven hours. **In winter the price half (two consecutive 5-minute prints at $1,000 or more) does all of the separating; the demand half acts as a peak-hour filter that vetoes overnight price-only runs.** It has vetoed one run in the data held (November 1, 2026, 00:25–00:35 ET), and the cause of that run is still unknown, so whether the veto was right is unknown.

**What this cannot answer:** whether PJM prices spike on cold winter peaks. No winter hour in the price data held averaged $500 or more (November–December 2025 maximum $387.89). The winter that matters, January 2025 (record 144,420 MW on January 22, 14Z, demand half met at 100.9%), needs the PJM price feed, which has refused the fleet's key since 2026-11-16 14:12 ET (WILL_QUEUE row 695).

## The rule tested

P1 letter (STATUS § EXIT, THESIS): EEA2-or-higher posting, OR real-time PJM-RTO LMP ≥ $1,000 for 2 or more consecutive 5-minute intervals AND (an emergency posting OR demand ≥ 97% of the trailing peak). **Demand half, exactly as the instruments compute it** (`power_watch.py` `read_pjm_demand`, `tape_scan.py`): EIA-930 PJM hourly demand divided by the highest of the 24 hourly values before it, rounded to 1 decimal place, met at ≥ 97.0.

**Hour convention:** EIA-930 hour stamps are UTC and it is not settled whether a stamp marks the start or the end of the hour; `tape_scan.py` grades both. Every table below is computed both ways: **HB** (EIA stamp = start of the price hour) is shown first, **HE** (EIA stamp = end of the price hour) in brackets where it differs.

## Data

| Window | Price series | Demand series | Status |
|---|---|---|---|
| Sep 1–Oct 28, 2025 | PJM Data Miner 2 `rt_hrl_lmps` PJM-RTO, verified hourly, n=1,392 | EIA-930 PJM, pulled 2026-10-29 | Held, `sources/2026-10-29/` |
| Sep 1–Oct 28, 2026 | same, n=1,392 | same | Held, `sources/2026-10-29/` |
| Nov 1–Dec 31, 2025 | same, n=1,465 (fall-back hour included) | EIA-930, pulled 2026-11-19 | Held, `sources/2026-11-05/` + `sources/2026-11-19/` |
| Oct 23–Nov 14 11:00 ET, 2026 | DM2 5-minute PJM-RTO, verified where held (to Nov 12), unverified otherwise; 6,480 prints | EIA-930, pulled 2026-11-19 | Held, `sources/2026-10-29/`, `2026-11-05/`, `2026-11-11/`, `2026-11-14/` |
| Dec 2, 2024–Feb 28, 2025 | **none held** | EIA-930, pulled 2026-11-19 | Demand half only |
| Nov 1–Nov 19 (14Z), 2026 | **none after Nov 14 11:00 ET** (key refused) | EIA-930, pulled 2026-11-19 | Demand half only |

Sep 1, 2025 and 2026 hours before 20 prior demand hours exist are excluded (the first ~20 hours of each file): this drops the Sep 1, 2026 evening ($847 and $877 hours) from the autumn-2026 tables.

## 1. How often the demand half is met

| Window | Hours with a reading | Met | Share | Days | Days with at least one met hour |
|---|---:|---:|---:|---:|---:|
| Sep 1–Oct 28, 2025 | 1,372 | 223 | 16.3% | 58 | 46 |
| Sep 1–Oct 28, 2026 | 1,372 | 230 | 16.8% | 58 | 38 |
| Nov 1–Dec 31, 2025 | 1,465 | 328 | 22.4% | 61 | 47 |
| **Dec 2, 2024–Feb 28, 2025** | 2,136 | 468 | 21.9% | 90 | **72** |
| Nov 1–Nov 19, 2026 (to 09:00 ET) | 447 | 109 | 24.4% | 20 | 17 |

**Where in the day (EPT hour):** Nov–Dec 2025, 69 of 328 met hours fall at 07–09 and 144 at 18–21, together 65%; Dec 2024–Feb 2025, 121 and 187 of 468, together 66%. The autumn shape is single-peaked (most met hours 15–21).

**This week:** the first cold mornings of the season met it at 103.0% (Nov 17 13Z, 106,646 MW), 99.5% (Nov 18 13Z, 106,151 MW) and 98.5% (Nov 19 13Z, 104,521 MW); at boot today (10:46 ET) the 14Z hour stood at 97.1% (101,491 MW). Prices for those hours: UNKNOWN (key refused).

## 2. Price outcome with and without the demand half (all hours)

Price outcome = the hourly verified average reaching the level. ⚠️ An hourly average understates 5-minute spikes: the October 27, 2026 18:00 hour averaged $720 while containing a 5-minute run above $1,000 that fired the letter. These tables test the demand half against hourly price stress, not the exact 5-minute letter (section 4 does that, on a short window).

| Window | Price level | Hours at level | With demand half met | P(level \| met) | P(level \| not met) | Plain high load, same count of hours |
|---|---|---:|---:|---:|---:|---:|
| Autumn 2026 | ≥ $1,000 | 7 | 7 [HE 5] | 3.0% [2.2%] | 0% [0.17%] | 7 of 7 |
| Autumn 2026 | ≥ $500 | 17 [18] | 14 [12] | 6.1% [5.2%] | 0.26% [0.52%] | 14 [16] |
| Autumn 2026 | ≥ $200 | 47 [48] | 33 [32] | 14.4% [13.9%] | 1.2% [1.4%] | 29 [31] |
| Autumn 2025 | ≥ $500 | 1 | 1 | 0.45% | 0% | 1 |
| Autumn 2025 | ≥ $200 | 10 | 4 [3] | 1.8% [1.3%] | 0.52% [0.61%] | 7 |
| **Nov–Dec 2025** | ≥ $500 | **0** | — | — | — | — |
| **Nov–Dec 2025** | ≥ $200 | 16 | 8 [10] | 2.4% [3.0%] | 0.70% [0.53%] | 7 |

"Plain high load, same count" = the N highest-load hours of the window, where N is the number of hours that met the demand half (230 in autumn 2026, 223 in autumn 2025, 328 in Nov–Dec 2025): how many of the price hours a plain load ranking catches with the same number of firings.

**Read:** in autumn 2026 the demand half and plain high load catch the same seven $1,000 hours. Across all hours the demand half "carries information" mostly because it is a high-load, peak-hour flag. In winter 2025 its best hours were cold mornings that topped out at $240–$388: the season's five highest hours were 07:00 ET on Nov 18 ($388, met 98.4% [101.6%]), Nov 17 ($379, 104.1%), Dec 15 ($347, 98.9% [102.4%]), Dec 16 ($327, not met 91.9% [95.7%]) and 17:00 on Dec 8 ($321, 102.7%). On the 47 days it was met, the median of the day's highest price in met hours was $69.89.

## 3. Holding hour and load fixed: does the demand half add anything?

Peak hours only (07–09 and 17–21 ET), split into thirds by load. Cells: hours at the price level / hours, met versus not met. HB first, HE below.

| Window, level | Load third | Met | Not met |
|---|---|---|---|
| Autumn 2026, ≥ $1,000 | high (100.3–149.9 GW) | **7/56 (12.5%)** | **0/97 (0%)** |
| | HE | 5/43 (11.6%) | 2/110 (1.8%) |
| Autumn 2026, ≥ $500 | high | 11/56 (19.6%) | 3/97 (3.1%) |
| | HE | 9/43 (20.9%) | 6/110 (5.5%) |
| Autumn 2026, ≥ $500 | middle (89.6–100.3 GW) | 2/88 | 0/65 |
| Autumn 2025, ≥ $200 | high (97.5–122.4 GW) | 3/76 (3.9%) | 3/77 (3.9%) |
| | HE | 2/59 (3.4%) | 4/94 (4.3%) |
| **Nov–Dec 2025, ≥ $200** | high (106.9–135.7 GW) | 4/96 (4.2%) | 2/67 (3.0%) |
| | HE | 4/94 (4.3%) | 2/69 (2.9%) |
| **Nov–Dec 2025, ≥ $100** | high | 15/96 (15.6%) | 13/67 (19.4%) |
| | HE | 15/94 (16.0%) | 13/69 (18.8%) |

Low and middle thirds carry no hour at $1,000 in any window. At $200, the autumn-2026 middle third has 9/88 met against 3/65 unmet [HE 12/74 against 1/79], the same direction as the high third; every other low or middle cell holds at most 3 hours at $200.

**Read:**
- **Autumn 2026 (stress present):** within the high-load peak hours the demand half concentrates the spikes, under both conventions. INFERRED mechanism: it measures load running above yesterday's, which is when committed generation falls short of a load the day-ahead plan underestimated. ⚠️ The seven $1,000 hours are three episodes (Sep 16, 2 hours; Sep 17, 2 hours; Oct 13, 3 hours), not seven independent observations.
- **Calm windows, including the only winter held:** no separation (3.9% versus 3.9%; 4.2% versus 3.0% on 6 hours; 15.6% versus 19.4%, the wrong way). On an ordinary cold morning, meeting the demand half says nothing beyond "this is a high-load peak hour".

## 4. The exact 5-minute letter, Oct 23–Nov 14, 2026

6,480 prints; 541 hours with a demand reading; demand half met in 121 (22.4%).

| Hour (ET) with 2+ consecutive 5-min prints ≥ $1,000 | Demand half | Posting | Letter |
|---|---|---|---|
| Oct 27 18:00 | 97.9% [99.8%] met | none | FIRED (graded Oct 29) |
| Oct 27 19:00 | 99.8% [100.3%] met | none | FIRED |
| Nov 1 00:00 | 92.6% [91.1%] not met | none | NOT fired: price half only; cause unknown (KB-WATT-192) |

Price-half runs occurred in 2 of 121 met hours (1.7%) and 1 of 420 unmet hours (0.24%). One fire episode and one veto: too few to measure anything beyond "the veto happened overnight, where the demand half almost never passes".

## What is established, inferred and unknown

| | Statement | Basis |
|---|---|---|
| ESTABLISHED | The demand half is met in 22–24% of winter hours and on 72 of 90 days of the 2024–25 winter, 47 of 61 days of Nov–Dec 2025 and 17 of 20 days of Nov 2026 | EIA-930, computed here, both conventions identical for the count |
| ESTABLISHED | About two thirds of winter met hours sit at 07–09 or 18–21 ET | same |
| ESTABLISHED | Nov–Dec 2025 held no hour averaging ≥ $500; maximum $387.89 (Nov 18 07:00 ET) | DM2 verified hourly, held |
| ESTABLISHED | In calm windows, with hour and load held to thirds, met and unmet peak hours spike at about the same rate | Section 3 |
| ESTABLISHED, small n | In autumn 2026 the demand half concentrated the $1,000 hours within high-load peak hours (7/56 versus 0/97, HB) | Section 3; three episodes |
| INFERRED | It works, when it works, as a load-surprise flag (load above yesterday's), not a level-of-stress flag | Mechanism reading of the rule and of section 3 |
| INFERRED | In winter the letter is effectively the price half restricted to peak hours | Sections 1 and 4 |
| UNKNOWN | Whether a winter cold snap produces $1,000 runs at peak, and whether the demand half separates them | No winter stress in held prices |
| UNKNOWN | Whether the Nov 1, 2026 veto was right | Cause of the run unknown |
| UNKNOWN | 5-minute behaviour inside winter-2025 hours (hourly averages can hide runs) | 5-minute retention is about 49 days; only hourly is reachable for 2025 |

## What the PJM key would add (WILL_QUEUE row 695)

1. **The 5-minute tape from Nov 14 10:00 ET to now**, which includes the season's first cold mornings (Nov 17–19, demand half met at 103.0%, 99.5%, 98.5%). These are the ordinary cold mornings the commission asks about, observed at the letter's own resolution. The verified 5-minute feed is retained at least 49 days, so this stays reachable until about early January.
2. **Verified hourly prices for Jan–Feb 2025**, the record-cold week (144,420 MW on Jan 22) and the only winter stress within reach. Reach is not tested: a 2024 request was refused on Oct 29 as spanning the archive boundary (KB-WATT-186), so Jan 2025 is probably, not certainly, reachable. Dec 2024 may not be.
3. Nothing in this test needs a paid source. No open public source holding PJM hourly real-time LMP was found on this desk's list; the EIA ICE file is a daily on-peak average with about a 12-day lag and cannot see an hour.

## For the trigger (no change made)

The evidence does not argue for removing the demand half (in winter it passes at nearly every peak, so it costs little, and it removes overnight runs) or for tightening it (no winter stress to tune on). It does change how a demand-half reading should be described: **a met demand half on a winter morning is not a stress reading, and should never be reported as one.** STATUS already says the letter is "price-gated this season" (KB-WATT-206); this document measures that. If Will wants a demand half that carries stress information on its own, a level test against PJM's own seasonal peak forecast (about 147,500 MW for this winter, PJM's Nov 5 outlook, KB-WATT-195) would be the candidate; it is untested and would be a new rule, so this desk does not propose it now (Will, 2026-10-31: fewer rules).

## Trade-assessment handoff (WQ-696)

**This supports no investment implication.** It is a measurement of this desk's own instrument: it says a "demand half met" reading on a winter morning carries no information about price stress beyond "it is a cold peak hour", so nobody should treat it as an early-warning signal. It says nothing on whether PJM will spike this winter, because no winter stress sits in the data within reach. **Horizon** for the open question: December 2026–February 2027. **What would change this:** a winter window in which met peak hours carry $1,000 runs at clearly higher rates than unmet peak hours at the same load (testable on the Nov 14–now tape and on Jan 2025 once the key works). **Unknown:** winter spike behaviour at peak; the Nov 17–19 tape. No packet to TERRY: there is nothing in this for a trade.

## Sources

- PJM Data Miner 2, `rt_hrl_lmps` (pnode PJM-RTO, verified hourly), pulled 2026-10-29 and 2026-11-05; `rt_fivemin_hrl_lmps` and `rt_unverified_fivemin_lmps`, pulled 2026-10-29 to 2026-11-14. Files named in the Data table.
- EIA-930 (EIA API v2 `electricity/rto/region-data`, respondent PJM, type D), pulled 2026-10-29 and 2026-11-19 10:47 ET.
- KB-WATT-186 (autumn year-over-year), 192 (Nov 1 run), 195 (PJM winter outlook), 206 (30 of 154 hours), 220 (tape scan).
