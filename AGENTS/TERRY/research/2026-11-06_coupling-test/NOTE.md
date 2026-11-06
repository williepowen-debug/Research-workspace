# WQ-631 working note: a written test for "downward coupling" on GATE-TERRY-UNG-01

**Written:** 2026-11-06 15:28 ET, TERRY. **Commission:** `inbox/processed/2026-11-06_from-PROME_WQ631-A-coupling-test.md`. **Card changed:** no.
**Proposal:** `PROME/inbox/2026-11-06_from-TERRY_WQ631-coupling-test-proposal.md`.

## What the kill is worth, before any test
Stylized walk: Jan-15 10/12C placed on each year's Dec 4 with spot scaled to $9.40, UNG's real daily path to Jan 8, Black-Scholes at flat 70/76 IV, $1.00 harvest honoured, time stop Jan 8. Marks, not fills; no bid-ask. n = 19 years, 2007-2025 (`econ_test.py`, `data/gas_closes.csv`).

| At $9.40 on 12/4, ×5 | Figure |
|---|---|
| Sell on 12/4 | $202 |
| Hold, mean | $164 |
| Hold, median | $55 |
| Hold beat sell | 7 of 19 |
| Harvested at $1.00 | 3 of 19 |

Hold minus sell by year: 2007 +58 · 2008 −187 · 2009 +326 · 2010 −145 · 2011 −195 · 2012 −195 · 2013 −29 · 2014 −202 · 2015 +20 · 2016 −186 · 2017 −180 · 2018 −203 · 2019 −195 · 2020 −46 · 2021 +33 · 2022 +334 · 2023 +142 · 2024 +325 · 2025 −203.
Spot sensitivity: at $8.50 sell $108, hold mean $61, 2 of 19. At $10.00 sell $279, hold mean $248, 9 of 19.

## Candidates, measured
Outcome: Dec+Jan mean temperature, 8 states (NJ NY PA, IL IN MI OH WI), unweighted, NCEI climdiv `tmpcst` vintage 20261006, linear trend removed (+0.62 F per decade), 1950-2025, n = 76. "Cold" = coldest third, at or below −1.71 F.

| Candidate | Window | Pass | Cold, pass | Cold, fail | Mean gap F (pass − fail) | Gas: hold minus sell, pass vs fail | Verdict |
|---|---|---|---|---|---|---|---|
| (a) 30 hPa 60N < 0 | 11/07-12/03 | 1 of 73 (1968); 0 of 47 since 1979 | n/a | n/a | n/a | n/a | Reject: cannot pass |
| (b) CPC AO ≤ −1.0, 5 straight days | 11/07-12/02 | 39 of 76 | 14 of 39 | 11 of 37 | −1.11, p 0.156 | −$116 vs +$69, gap p 0.037 | Reject: no signal on cold, wrong way on gas |
| (c) CPC 8-14 day, any issue | 11/07-12/03 | 12 of 14 | 4 of 12 | 0 of 2 | −3.41 | n/a | Reject: almost always passes |
| **(c) CPC 8-14 day, issue of 12/3** | one read | **4 of 14** | **3 of 4** | **1 of 10** | **−4.84, p 0.011** | hold lost in all 4 pass years | **Proposed** |

(a) wind: NCEP/NCAR R1 daily mean, zonal mean of 144 longitudes at 60N, `data/ncep_u60.tsv`. 73 of 76 years: 1969-1971 not fetched, the download was stopped by memory pressure at about 15:26 ET. 1968 is pre-satellite. (b) reproduces AEOLUS's 39 of 76 exactly on its own window, 11/07-12/04. Cutting the read at 12/02 for the file's 2-day lag does not change the count.
(c) read: CPC archived `814temp_YYYYMMDD.zip`, 361 issues, 2012-2025, innermost containing polygon at each city. Control: the 2026-11-05 issue reads Philadelphia Above 33, New York near normal 36, Pittsburgh Above 40, Chicago Above 60, Detroit Above 50, Columbus Above 50, matching AEOLUS's prose (KB-AEO-259).

| Year | 12/3 read | Dec+Jan anomaly F | Hold minus sell $ |
|---|---|---|---|
| 2012 | fail | +3.23 | −195 |
| 2013 | PASS | −5.74 cold | −29 |
| 2014 | fail | −0.64 | −202 |
| 2015 | fail | +5.05 | +20 |
| 2016 | PASS | +1.60 | −186 |
| 2017 | PASS | −3.45 cold | −180 |
| 2018 | fail | −0.13 | −203 |
| 2019 | fail | +3.43 | −195 |
| 2020 | fail | +1.64 | −46 |
| 2021 | fail | −0.04 | +33 |
| 2022 | fail | +3.19 | +334 |
| 2023 | fail | +4.39 | +142 |
| 2024 | fail | −2.09 cold | +325 |
| 2025 | PASS | −4.56 cold | −203 |

Read-date sensitivity, same 2-of-3 rule: 11/27 pass 3, cold 2 of 3, fail cold 2 of 11 · 11/28 5, 4 of 5, 0 of 9 · 11/29 5, 4 of 5, 0 of 9 · 11/30 6, 4 of 6, 0 of 8 · 12/1 5, 3 of 5, 1 of 9 · 12/2 5, 3 of 5, 1 of 9 · 12/3 4, 3 of 4, 1 of 10. Requiring all 6 cities gives the same 12/3 result. 2022 passes on reads 11/29 through 12/2; 2024 passes on 11/27 through 11/29. Neither passes on 12/3.

## Limits
- Trials disclosed: 5 AO threshold forms, 3 AO windows, 3 any-issue CPC forms, 2 city rules across 7 read dates, 1 two-of-three-issues form, 3 weak-wind levels at 30 hPa. The p-values are unadjusted. The six cities and the 2-of-3 rule were fixed in code before the first outcome printed. 12/3 was chosen from the card's kill date, not from the results: 11/28 scores better and was not chosen.
- The 8-14 day issue of 12/3 forecasts about 12/11-17, which sits inside the Dec+Jan outcome, so part of the temperature gap is the forecast verifying.
- Dec+Jan is a calendar proxy for the hold window 12/4-1/8.
- CPC archive starts 2012, so 2009 has no read.
- 30 hPa climatology is R1, the live read is GFS. R1 2026 was not read, so no same-model calibration exists. See the AEOLUS packet.
