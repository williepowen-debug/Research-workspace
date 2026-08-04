# QQQ V-Recovery Cohort — Credit (HY OAS) Conditioning

**Date:** 2026-08-04
**Author:** PROME subagent (sonnet), Will-requested
**Data sources:**
1. **[PRIMARY, live]** FRED series `BAMLH0A0HYM2` (ICE BofA US High Yield Index Option-Adjusted Spread), daily, percent — `https://api.stlouisfed.org/fred/series/observations`, direct HTTPS, key from `FORGE/tools/market-data/.env`. Coverage as pulled: **2023-08-07 → 2026-07-31** (784 obs).
2. **[PRIMARY, via Wayback]** Same series, archived FRED raw-text endpoint: `https://web.archive.org/web/20231212182755id_/https://fred.stlouisfed.org/data/BAMLH0A0HYM2.txt` (`curl --compressed`, `id_` raw modifier retained). Header provenance: `Source: Ice Data Indices, LLC` · `Date Range: 1996-12-31 to 2023-12-11` · `Units: Percent`. Coverage: **1996-12-31 → 2023-12-11** (7,034 obs). Recipe per fleet finding `finding_declared_data_wall_needs_fleet_memory_check` / DEWEY `AGENTS/DEWEY/output/2026-07-16_credit-spreads-march-2023-oas.md`.
**Pull timestamp:** 2026-08-04T18:17:58 UTC (live API pull); Wayback archive pulled same session.

---

## Data-wall finding (kept — fleet-relevant)

**FRED's live `BAMLH0A0HYM2` endpoint has been truncated to a rolling ~3-year window** (a policy change effective April 2026 — the series' own `/fred/series` metadata states *"Starting in April 2026, this series will only include 3 years of observations. For more data, go to the source."*). Confirmed independently via the API (`observation_start=1998-01-01` still returns first-obs `2023-08-07`), ALFRED vintage queries at multiple `realtime_start` dates (all still return `2023-08-07` as first obs — the truncation appears applied retroactively to stored vintages too), and a direct `fredgraph.csv` download (same result). **This is real and reproducible for anyone hitting the live endpoint** — worth keeping visible for other agents rather than silently working around it.

**It is solved, not fatal**, per the fleet's prior recovery (DEWEY, 2026-07-16): the pre-truncation full history (1996-12-31 → 2023-12-11) is recoverable from a Wayback Machine snapshot of FRED's own raw-text export, which is still the primary source (ICE Data Indices via FRED), not a substitute series.

---

## Stitch verification

Overlap window between the two sources: **2023-08-07 → 2023-12-11**.

| Check | Result |
|---|---|
| Overlapping observations | **92** |
| Exact matches | **92 / 92** |
| Max absolute discrepancy | **0.0** (all values identical to 2 decimal places) |
| Mean absolute discrepancy | 0.0 |

Full agreement on the overlap — proceeded to stitch: archive values used for all dates `< 2023-08-07`, live-API values used for `2023-08-07` onward (live series treated as the more current vintage where both exist, though on this overlap they're identical anyway). **Stitched series: 1996-12-31 → 2026-07-31, 7,726 observations, zero gaps in the episode-relevant windows.**

---

## Method (as specified, now runnable on the full cohort)

- OAS level, Δ10td (≈10 trading days), Δ21td (≈21 trading days) computed using **only observations dated on or before the episode's signal date** — no lookahead.
- Trailing-2-year percentile: rank of the signal-date level within the trailing 504 trading days (the stitched series now has full 2-year lookback for every one of the 19 episodes — no truncated windows).
- Pre-registered classification (fixed before viewing results, unchanged from the original spec): **WIDENING** if Δ10td > +10bp · **TIGHTENING** if Δ10td < −10bp · **FLAT** otherwise.

---

## Per-episode table (all 19 + current)

| Signal date | 3d ret % | DD@trough % | Dist vs 252d hi % | Fwd 1w | Fwd 1m | Fwd 3m | Fwd 6m | OAS level (bp) | Δ10td (bp) | Δ21td (bp) | 2y %ile | Class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1999-03-26 | +6.0 | −7.1 | −1.5 | +7.2 | +7.7 | +5.7 | +16.1 | 518 | −11.0 | −3.0 | 71% | TIGHTENING |
| 1999-04-22 | +10.2 | −11.3 | −2.2 | −2.2 | −3.1 | +4.8 | +12.2 | 493 | −25.0 | −29.0 | 66% | TIGHTENING |
| 1999-06-17 | +7.9 | −10.2 | −3.1 | −0.1 | +10.8 | +12.1 | +47.9 | 477 | +8.0 | +8.0 | 64% | FLAT |
| 1999-10-29 | +6.9 | −4.9 | +1.7 | +3.7 | +11.8 | +36.4 | +45.4 | 517 | +23.0 | +10.0 | 69% | WIDENING |
| 1999-12-03 | +7.7 | −5.4 | +1.9 | +1.0 | +11.5 | +41.5 | +18.6 | 491 | −14.0 | −23.0 | 53% | TIGHTENING |
| 1999-12-21 | +7.7 | −2.1 | +5.4 | +3.4 | +7.6 | +27.5 | +10.6 | 468 | −25.0 | −34.0 | 37% | TIGHTENING |
| 2000-01-10 | +7.6 | −9.2 | −2.4 | +1.5 | +7.0 | +8.2 | +2.7 | 481 | +13.0 | −7.0 | 45% | WIDENING |
| 2000-02-02 | +8.0 | −10.6 | −3.5 | +6.6 | +19.6 | −4.0 | −6.7 | 486 | +9.0 | +5.0 | 48% | FLAT |
| 2000-02-24 | +8.2 | −5.6 | +2.2 | −1.3 | +10.4 | −25.4 | −8.9 | 504 | +27.0 | +23.0 | 61% | WIDENING |
| 2000-03-23 | +7.7 | −6.4 | +0.9 | −7.5 | −26.9 | −17.9 | −24.4 | 555 | +36.0 | +61.0 | 86% | WIDENING |
| 2010-05-12 | +7.1 | −10.1 | −3.8 | −5.3 | −6.4 | −6.3 | +10.6 | 618 | +67.0 | +52.0 | 10% | WIDENING |
| 2011-11-30 | +6.6 | −11.2 | −5.3 | +1.2 | −0.6 | +15.5 | +7.7 | 779 | +25.0 | +37.0 | 95% | WIDENING |
| 2014-10-21 | +5.5 | −8.2 | −3.2 | +3.4 | +6.5 | +7.8 | +13.3 | 450 | +13.0 | +48.0 | 55% | WIDENING |
| 2020-11-04 | +6.5 | −11.0 | −5.2 | +1.0 | +6.5 | +15.7 | +16.8 | 479 | −9.0 | −23.0 | 62% | FLAT |
| 2021-03-11 | +6.0 | −10.9 | −5.5 | −1.9 | +6.0 | +7.1 | +19.6 | 352 | 0.0 | +2.0 | 6% | FLAT |
| 2023-05-30 | +5.5 | −4.8 | +0.5 | +1.4 | +4.1 | +7.2 | +11.8 | 458 | −21.0 | +13.0 | 67% | TIGHTENING |
| 2024-11-07 | +5.7 | −3.9 | +1.6 | −0.9 | +1.7 | +3.0 | +0.7 | 273 | −20.0 | −21.0 | 0% | TIGHTENING |
| 2025-05-13 | +5.6 | −9.4 | −4.3 | +0.9 | +3.5 | +12.7 | +20.8 | 309 | −65.0 | −117.0 | 27% | TIGHTENING |
| 2026-06-15 | +7.3 | −7.0 | −0.3 | −4.0 | −5.0 | unresolved | unresolved | 266 | −6.0 | −17.0 | 7% | FLAT |
| **2026-08-04 (current, provisional)** | — | — | — | — | — | — | — | **285** (obs 2026-07-31, stale 4d) | **+12.0** | +10.0 | 44% | **WIDENING (provisional)** |

---

## Split table

| Credit bucket (Δ10td) | n | Fwd-1m median | Fwd-1m count-positive | Fwd-3m median | Fwd-3m count-positive |
|---|---|---|---|---|---|
| **WIDENING** (Δ10td > +10bp) | 7 | +6.5% | 4/7 | +7.8% | 4/7 |
| **FLAT** (−10bp ≤ Δ10td ≤ +10bp) | 5 | +6.5% | 4/5 | +9.6%* | 3/4* |
| **TIGHTENING** (Δ10td < −10bp) | 7 | +4.1% | 6/7 | +7.2% | 7/7 |

\* Fwd-3m for FLAT bucket: n=4 resolved (2026-06-15 excluded — 3m/6m still in the future). Fwd-1m column includes 2026-06-15's resolved −5.0% (n=5).

**Current episode (2026-08-04):** classifies **WIDENING**, Δ10td = +12.0bp — but this rests on the **2026-07-31 print (already 4 calendar days stale as of today)**. 8/1–8/4 are not yet published at FRED; a confirmed update print could move Δ10td back under the +10bp threshold. Treat as provisional until re-pulled.

---

## Finding statement

All three credit buckets show **positive median forward returns at both 1m and 3m** — the QQQ V-recovery pattern (≥+5.5% 3-session snap-back from a shallow, <−16%, drawdown) has historically worked across WIDENING, FLAT, and TIGHTENING credit regimes, with **TIGHTENING the cleanest (7/7 positive at 3m, tightest downside)** and **WIDENING the weakest and most dispersed (only 4/7 positive at both 1m and 3m, including the two worst outcomes in the whole cohort: 2000-03-23 at −26.9%/−17.9% and 2010-05-12 at −6.4%/−6.3%)**. **n=7/5/7 is a real sample for this kind of pattern-cohort work but still thin — treat bucket medians as directional, not as a calibrated edge.** The live signal today provisionally lands in the WIDENING bucket, i.e., the historically weakest and most dispersed regime for this setup — worth flagging precisely because it's the bucket where the pattern has failed outright twice (2000-03-23, 2010-05-12), not because the median is negative (it isn't).

---

## Caveats

1. **Archived data provenance:** the 1996-12-31→2023-12-11 leg is **[PRIMARY via Wayback]** — FRED's own raw-text export, ICE Data Indices as the underlying source, captured intact via `web.archive.org` (`id_` raw snapshot, not the wrapped/bannered view). Not a third-party mirror or reconstruction.
2. **Overlap-verified stitch:** 92/92 exact matches, 0.0 max discrepancy, on the 2023-08-07→2023-12-11 overlap — full confidence in the join.
3. **Current-episode (2026-08-04) classification is provisional**, resting on a 2026-07-31 print stale by 4 calendar days at the time of this pull. Re-run once 8/1–8/4 prints publish before treating WIDENING as final.
4. **FRED's live-endpoint truncation (3-year rolling window, April-2026 policy change) is a fleet-relevant, reproducible finding** — flagged here for visibility, not just worked around; other agents hitting `BAMLH0A0HYM2` (or similar ICE/BofA OAS series) live will hit the same wall and should use the same Wayback recovery pattern.
5. Forward-return figures for all 19 episodes are taken as-given from the pre-built cohort (not re-derived by this subagent); only the OAS conditioning columns (level/Δ10td/Δ21td/percentile/class) were computed independently.
6. 2026-06-15's 3m/6m forward returns are genuinely unresolved (future dates), correctly excluded from 3m tallies, not treated as missing/zero.
7. Bucket sizes (n=5–7) support directional reads, not statistical significance — no p-values or confidence intervals are implied or should be inferred from this table.
