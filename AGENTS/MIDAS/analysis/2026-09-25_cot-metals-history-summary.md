# COT history summary — legacy futures-only, 2010-01-05 → 2026-09-15

Built 2026-09-25 by MIDAS subagent from CFTC `deacot{2010..2026}.zip` (annual.txt; 2026 file stamped 2026-09-17). Extraction by CONTRACT CODE, columns mapped by HEADER NAME, per-row reconciliation: OI == TotRept+NonRept (both sides) AND TotRept == NC+Spread+Comm (both sides). Scratch only — not committed.

Percentiles: linear interpolation (type 7). Percentile rank = % of all rows (incl. latest) with value ≤ latest; `<` also shown. Weekly change = Δ net/OI in percentage points between consecutive rows; sd = sample sd.

## SILVER (code 084691)

- n = 872 weekly rows, 2010-01-05 → 2026-09-15; reconciliation failures 0; duplicate dates 0; missing weeks 0 (only holiday-shifted 6/8-day pairs)
- latest 2026-09-15: net/OI **24.41%** (net NC 25,326 / OI 103,745); percentile rank 59.9 (≤) / 59.7 (<)
- min -13.64% on 2018-09-04; max 48.57% on 2017-03-07
- net/OI percentiles: p1 -7.50 · p5 0.59 · p10 4.53 · p25 12.41 · p50 21.29 · p75 29.02 · p90 34.69 · p95 38.19 · p99 44.06
- weekly Δ (pp): p5 -5.25 · p25 -1.98 · p50 -0.09 · p75 +1.89 · p95 +5.52 · sd 3.42 · n 871
- OI context: min 95,684 (2011-12-06), max 244,196 (2018-08-21), p50 154,094, latest 103,745

## PLATINUM (code 076651)

- n = 872 weekly rows, 2010-01-05 → 2026-09-15; reconciliation failures 0; duplicate dates 0; missing weeks 0 (only holiday-shifted 6/8-day pairs)
- latest 2026-09-15: net/OI **23.24%** (net NC 15,220 / OI 65,478); percentile rank 28.7 (≤) / 28.6 (<)
- min -13.31% on 2018-09-04; max 73.68% on 2012-10-16
- net/OI percentiles: p1 -8.47 · p5 2.07 · p10 9.05 · p25 21.10 · p50 35.58 · p75 51.90 · p90 62.74 · p95 66.31 · p99 70.06
- weekly Δ (pp): p5 -8.40 · p25 -2.64 · p50 +0.10 · p75 +2.77 · p95 +7.97 · sd 5.05 · n 871
- OI context: min 27,646 (2010-07-20), max 105,936 (2020-01-21), p50 66,816, latest 65,478

## PALLADIUM (code 075651)

- n = 872 weekly rows, 2010-01-05 → 2026-09-15; reconciliation failures 0; duplicate dates 0; missing weeks 0 (only holiday-shifted 6/8-day pairs)
- latest 2026-09-15: net/OI **-24.84%** (net NC -4,150 / OI 16,707); percentile rank 20.0 (≤) / 19.8 (<)
- min -62.46% on 2023-09-05; max 73.43% on 2014-09-16
- net/OI percentiles: p1 -57.32 · p5 -50.01 · p10 -43.12 · p25 -12.95 · p50 35.10 · p75 56.40 · p90 63.92 · p95 66.11 · p99 69.98
- weekly Δ (pp): p5 -8.21 · p25 -2.32 · p50 -0.01 · p75 +2.15 · p95 +7.32 · sd 4.58 · n 871
- OI context: min 5,875 (2022-08-30), max 45,440 (2014-07-29), p50 22,118, latest 16,707

## GOLD (code 088691)

- n = 872 weekly rows, 2010-01-05 → 2026-09-15; reconciliation failures 0; duplicate dates 0; missing weeks 0 (only holiday-shifted 6/8-day pairs)
- latest 2026-09-15: net/OI **56.19%** (net NC 230,338 / OI 409,899); percentile rank 99.1 (≤) / 99.0 (<)
- min -8.21% on 2018-10-09; max 57.67% on 2024-09-17
- net/OI percentiles: p1 -0.68 · p5 9.60 · p10 16.18 · p25 27.05 · p50 36.69 · p75 42.38 · p90 48.88 · p95 51.92 · p99 56.17
- weekly Δ (pp): p5 -5.46 · p25 -1.91 · p50 -0.03 · p75 +1.78 · p95 +5.80 · sd 3.31 · n 871
- OI context: min 326,052 (2026-06-02), max 796,883 (2020-01-14), p50 473,982, latest 409,899
## Cross-checks & caveats

- **Gold vs frozen reference** `AGENTS/MIDAS/sources/cot_gold_history_2010_2026.tsv` (n=868, 2010-01-05→2026-08-18): all 868 common dates match EXACTLY on OI, NC long, NC short, net NC, and net/OI (|Δ| ≤ 0.001pp); 0 mismatches. This build adds 4 later rows (08-25, 09-01, 09-08, 09-15).
- **History last row == live deafut.txt** (vintage 2026-09-15) for all four metals, identical figures.
- **Contract codes / names constant 2010–2026**: each code maps to exactly one name across all 17 files (084691 SILVER - COMMODITY EXCHANGE INC.; 076651 PLATINUM - NEW YORK MERCANTILE EXCHANGE; 075651 PALLADIUM - NEW YORK MERCANTILE EXCHANGE; 088691 GOLD - COMMODITY EXCHANGE INC.). No code discontinuity found.
- **Micro variants exist and are excluded by code**: 084694 MICRO SILVER (5 rows, 2026 file only; absent from the current live file), 088695 MICRO GOLD (163 rows 2020–2026); also Coinbase gold products 088LM1, 180LM9. A name-substring filter would have pulled these in.
- **Contract-size changes are NOT verifiable from the COT file** (it carries no contract spec). net/OI is a ratio in contracts, so a size change would not rescale it, but would alter who can trade (participation mix). Not checked against exchange rulebooks here.
- **Palladium is regime-split, not one distribution**: net/OI yearly mean +2.8…+62.7% in 2010–2021 (0 net-short weeks through 2020), then net short every week of 2022–2024 (yearly means −27.6/−49.1/−43.9), 50/52 weeks in 2025, 28/37 in 2026. Full-window percentiles are a mixture; on 2022-01-04→2026-09-15 only (n=246) the latest −24.84% ranks 65.4 (≤), p50 −36.82. Band drafting should choose the window deliberately.
- **Platinum drifted down**: yearly means 51–60% (2010–2014) vs 13–25% (2022–2026); full-window percentile rank 28.7 overstates how low today is vs the recent regime.
- **Palladium OI is thin** (latest 16,707; min 5,875 on 2022-08-30): one large trader shifts net/OI several pp. Weekly Δ sd 4.58pp.
- Gold latest (56.19%) sits at the full-window 99.1 percentile rank; max 57.67% (2024-09-17).
