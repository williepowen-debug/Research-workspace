# Which desks carry forecasting edge: per-desk score

**Repo:** williepowen-debug/Research-workspace · **Pinned commit:** `62d7a18480` (master, 2026-11-17 19:28 ET) · **Checked:** 2026-11-18, read-only, full-history clone in scratch. Nothing in the repository was edited, committed or pushed.

**Method.** I ran the repo's own scorer (`PROME/tools/forecast_report.py`) at the pin and reused its own readers, so every desk score below uses exactly the calls, outcomes and probabilities the fleet report uses. For each desk I computed the score twice: at the probability **first logged** in the ledger's git history, and at the **scored** probability (the latest mark before the outcome, which is what the fleet report uses). The baseline is the fleet report's own: "always say the hit rate". For a desk, that is the desk's own hit rate. A gain above zero means the desk's percentages told hits from misses better than a flat guess at its usual hit rate would have. The 95% ranges are bootstrapped with the tool's seed (619).

Supporting files in `forecast-audit/per-desk/`: `per_desk.tsv` (the table below), `scored_calls.tsv` (one line per scored call: desk, outcome, first and scored probability, dates, flags), and the two scripts.

## Bottom line

1. **No desk shows forecasting edge that clears zero.** Not at the first-logged probability, and not at the scored one. The best-looking desks (ZHAO, BOND, CRUISE, HANS) have ranges that still include zero.
2. **One desk is reliably worse than its own base rate: CARL.** It gave its calls an average 70% at first logging and 3 of 13 came true. Its range is entirely below zero at the first-logged probability (−0.50 to −0.03).
3. **The two biggest desks point in opposite directions.** BOND (32 calls) is the strongest large desk, at +0.034, and none of its probabilities were revised. SAM (32 calls) is below its base rate at first logging (−0.038): its hits and misses got the same average probability, 61%. Late revisions lift SAM to −0.010.
4. **Most of the fleet's late-revision gain comes from five desks:** LABOR, ZHAO, SAM, OTTO and CARL. LABOR goes from −0.094 at first logging to +0.028 scored, mostly by marking calls down weeks before they failed.
5. **Fourteen of the 25 scoring desks have under 10 scored calls.** Their numbers say nothing. Even at 30 calls, a desk needs a gain of about +0.04 before its range clears zero. A typical real edge (+0.02 to +0.03) would need roughly 60 to 150 graded calls per desk to show.
6. **Eight desks have graded calls but no probabilities, so they cannot be scored at all:** HENRY (38 decided calls), VULCAN (17), WATT (10), MIDAS (7), FERT (6 of 8), YURI (5), VIOLET (3) and CREED (1 of 10).

## 1. Scorer state at the pin

| Item | 11/16 (pass 5) | Now (`62d7a18480`) |
|---|---|---|
| BOND's archived resolved calls | Not read; 23 scorable calls missing | **Fixed.** Four BOND archive files are read, plus VULCAN's and WATT's archives (8 files, 56 rows). BOND now has 32 scored calls |
| First-logged score | Not in the tool | **Added on 11/17.** The tool prints it fleet-wide: +0.008 first-logged, +0.027 scored, on 274 calls. My rebuild matches both figures |
| Per-desk score | Not printed | Still not printed, **on purpose**. The tool's header says per-desk Brier is withheld under WQ-619 A ("the first report proves grading consistency, no desk ranking"). This report is an outside read and does not change that ruling |
| Fleet score | 242 calls, +0.025 | 274 calls, **+0.027 (range +0.005 to +0.046)** |

**One gap in the new first-logged reading.** BRENT moved its ledger from `workbook/` to `thesis/` on 6/1 as a delete plus a new file, not a rename, so git's rename tracking doesn't follow it. The tool therefore starts 16 BRENT calls on 6/1 instead of 3/6–3/7 and misses five early values: BRT-02 70%, BRT-03 60%, BRT-04 80%, BRT-05 70%, BRT-15 85%. They were raised within about nine hours of first writing. I used the 3/6 values below. The effect is small: BRENT goes from −0.006 to −0.015 first-logged, and the fleet figure stays at +0.008. No other desk has this gap among the calls checked in pass 5.

The tool also now correctly separates reused IDs (LAB-01, LAB-02, BRT-28 were different calls under the same ID). Pass 5's first-probability table had merged those, so the tool's handling is the better one.

## 2. Per-desk scores

"Gain" is the score improvement over always saying the desk's own hit rate. Zero means no information beyond the base rate. "Avg first % on hits / misses" shows whether the desk gave higher numbers to the calls that came true. The "no prior record" column counts the 11 calls from pass 5 that were logged after their outcome was known.

### Desks with 10 or more scored calls

| Desk | Calls | Came true | Avg first % on hits / misses | Gain at first-logged (95% range) | Gain at scored (95% range) | Calls revised | No prior record | Reading |
|---|---:|---:|---|---|---|---:|---:|---|
| BOND | 32 | 18 | 65 / 54 | **+0.034** (−0.019 to +0.065) | +0.034 (same) | 0 | 0 | Best large desk. Positive and unrevised, but not proven |
| SAM | 32 | 16 | 61 / 61 | **−0.038** (−0.127 to +0.019) | −0.010 (−0.098 to +0.046) | 4 | 1 | First calls didn't separate hits from misses. Revisions only partly repair it |
| BRENT | 22 | 18 | 71 / 69 | −0.015 (−0.080 to +0.027) | −0.006 (−0.070 to +0.038) | 5 | 1 | Most calls came true, but the numbers barely tell which |
| RED | 22 | 9 | 49 / 40 | +0.014 (−0.074 to +0.071) | +0.014 | 1 | 1 | Slightly positive, wide range |
| BROCK | 16 | 9 | 57 / 52 | +0.006 (−0.089 to +0.053) | −0.012 | 3 | 0 | Flat. Its revisions made it worse |
| HAWK | 16 | 7 | 51 / 56 | −0.071 (−0.235 to +0.019) | −0.067 | 1 | 1 | Gave misses higher numbers than hits. Without HAW-03, −0.029 |
| LABOR | 14 | 4 | 62 / 57 | **−0.094** (−0.324 to +0.043) | **+0.028** (−0.186 to +0.142) | 6 | 0 | Biggest late repair in the fleet |
| ZHAO | 14 | 6 | 64 / 43 | **+0.062** (−0.075 to +0.115) | **+0.110** (−0.011 to +0.164) | 6 | 1 | Best separation of hits from misses at first call. Closest to clearing zero |
| CARL | 13 | 3 | 73 / 70 | **−0.239 (−0.500 to −0.029)** | −0.190 (−0.441 to +0.011) | 1 | 0 | **Only desk reliably worse than its base rate.** Calls about 70%, right 23% of the time |
| OTTO | 13 | 5 | 65 / 61 | −0.057 (−0.264 to +0.041) | −0.011 | 5 | 1 | Revisions carry most of the score. Without OTTO-09, −0.085 first-logged |
| CRUISE | 11 | 6 | 65 / 50 | +0.054 (−0.083 to +0.100) | +0.054 | 0 | 2 | Positive, but 2 of 11 calls were logged after the outcome. Removing them *raises* it to +0.073 |

### Desks with under 10 scored calls: too few to say anything

| Desk | Calls | Came true | Gain at first-logged | Gain at scored |
|---|---:|---:|---:|---:|
| CREED | 9 | 6 | −0.114 | −0.077 |
| MARCO | 9 | 8 | +0.001 | −0.011 |
| REGINALD | 9 | 6 | −0.021 | −0.008 |
| HANS | 7 | 4 | +0.089 | +0.143 |
| FALCON | 6 | 3 | +0.006 | +0.006 |
| OSPREY | 6 | 3 | +0.051 | +0.057 |
| OZK | 6 | 2 | +0.036 | +0.036 |
| AEOLUS | 5 | 5 | −0.155 | −0.160 |
| LIQUID | 4 | 3 | −0.013 | −0.013 |
| FERT, FLG, HOMER | 2 each | 1, 2, 1 | — | — |
| CORAL, WAL | 1 each | 0, 0 | — | — |

These are listed for completeness only. AEOLUS shows how little small samples say: all 5 of its calls came true, so its own base rate is 100%, and any stated probability below 100% scores "worse than the base rate". That reflects the yardstick, not the desk's skill.

### Fleet

| | Calls | Gain at first-logged (95% range) | Gain at scored (95% range) |
|---|---:|---|---|
| All scored calls | 274 | +0.008 (−0.014 to +0.026) | +0.027 (+0.005 to +0.046) |
| Without the 11 calls with no prior record | 263 | +0.009 | +0.029 |

## 3. Where the late-revision gain comes from

43 of 274 scored calls were revised between first logging and scoring. Summed improvement in Brier points, by desk (a positive number means the revision helped):

| Desk | Revised | Net help | Main rows |
|---|---:|---:|---|
| LABOR | 6 | +1.71 | LAB-06 80%→20% three days before it failed; LAB-02 65%→10% and LAB-03 65%→7%, 24 and 62 days out |
| SAM | 4 | +0.89 | SAM-23 75%→30% and SAM-26 70%→25%. The ledger shows these values only after the outcome, because of the 9/9 rewrite. Pass 5 found SAM-23's 30% in SAM's STATUS before the outcome. SAM-26 was not checked |
| ZHAO | 6 | +0.67 | ZHA-03 65%→25% and ZHA-15 55%→18%, 48 and 18 days out |
| CARL | 1 | +0.64 | CRL-08 85%→28%, four days before it failed |
| OTTO | 5 | +0.60 | OTTO-30 60%→12%, 20 days out; OTTO-04 75%→62% on the day it resolved |
| HANS, CREED, REGINALD, HAWK, OSPREY, RED | 8 | +0.95 | HNS-07 65%→30%; PRED-CREED-006 65%→30% |
| BRENT | 5 | +0.21 | Raised within hours of first writing on 3/6–3/7; BRT-15's raise to 90% hurt |
| BROCK, MARCO, AEOLUS | 8 | −0.43 | Revisions that made the score worse |

The pattern: the desks whose scored numbers look acceptable mostly got there by **marking failing calls down as the outcome approached**. That is reasonable updating, but it is not early warning. The fleet's stated goal is to see stress before consensus, and that skill shows up in the first-logged column, where no desk clears zero.

## 4. What this can and cannot tell you

- **No desk is proven good, one is proven bad.** CARL's first-logged calls are reliably worse than a flat guess. Every other desk's range includes zero.
- **Calls are not independent.** Many calls on one desk share a root (SAM's Gulf calls, BRENT's Hormuz calls). The ranges treat each call as independent, so they are too narrow, and the true uncertainty is wider than shown.
- **Small samples cut both ways.** A desk like HANS (+0.089 on 7 calls) or ZHAO (+0.062 on 14) may be genuinely good. These numbers cannot tell that apart from luck.
- **Grading choices still move single desks.** Report 1's verification found rows scored against the desk's own record (BRT-22, BRT-23, BRT-28, OTTO-06, REG-10). These are left as the tool scores them. BRENT is the desk most affected: rescoring BRT-23 on the letter of the claim would add a hit.
- **"First-logged" means first in a prediction ledger's git history.** A view stated earlier in STATUS or a Markdown file is not seen. For rows migrated from Markdown in March, the true first call may be earlier.
- **Forecasts are one output.** This says nothing about a desk's research, monitoring or trade ideas, only about whether its stated percentages carried information.

## Hand to PROME (copy as is)

> An outside read-only scoring of every forecast ledger at `62d7a18480` (11/17 19:28 ET) produced per-desk scores at first-logged and scored probability, using `forecast_report.py`'s own readers and baseline (each desk's own hit rate). This does not change WQ-619 A's no-ranking rule for the report itself. Will decides whether a per-desk view enters report 2 or later. Forward-looking items only; no historical reconstruction is asked.
>
> 1. **First-logged score misses BRENT's pre-6/1 history.** BRENT's ledger moved from `AGENTS/BRENT/workbook/PREDICTIONS.tsv` to `AGENTS/BRENT/thesis/PREDICTIONS.tsv` on 6/1 (`3fcce675a4`) as a delete plus an add, so `git log --follow` in `file_history` starts at 6/1. Five calls lose their first value (BRT-02 70%, BRT-03 60%, BRT-04 80%, BRT-05 70%, BRT-15 85%, all from `dec1eff0d5` on 3/6). Fleet effect is nil at three decimals. Consider adding the old path to the registry history, or reading every path a desk's ledger has had.
> 2. **No desk's forecasting gain clears zero at the first-logged probability; CARL's is reliably below zero** (13 calls, 3 came true at an average 70% first-logged; gain −0.239, range −0.500 to −0.029). If CARL's first-call probabilities feed any decision, flag it to the desk as a calibration issue, going forward.
> 3. **Late revisions carry the fleet's scored gain.** 43 of 274 scored calls were revised; LABOR, SAM, ZHAO, CARL and OTTO account for most of the improvement. Report 2 already prints first-logged next to scored for the fleet. If Will approves a per-desk view, print both columns per desk, with the number of calls, and mark desks under 10 calls as "too few to score".
> 4. **Eight desks can never be scored as they log today:** HENRY, VULCAN, WATT, MIDAS, YURI, VIOLET (no probabilities), FERT (6 of 8 decided calls without one), CREED (1 of 10). Ask Will whether these desks should start attaching a probability to new calls.
> 5. **Sample size:** at about 30 calls, a desk needs a gain of roughly +0.04 before it is distinguishable from zero. If per-desk skill is a goal, more and smaller, independent calls per desk are needed, not more calls on one theme.
> 6. **SAM-26 (70%→25%) shows its scored value in the ledger only after the outcome,** because of the 9/9 rewrite. Please confirm a pre-outcome record in SAM's STATUS, as was found for SAM-23.
