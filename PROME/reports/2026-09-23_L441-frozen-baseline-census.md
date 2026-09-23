# L441 census — frozen denominators / baselines on the comparison side, fleet-wide · 2026-09-23

**Commissioned by** PROME `prome-68` (DOCKET L441, due 9/24). **Enumerated by** a read-only Explore sweep (Opus, 2026-09-23 ~11:0x ET), applying the row's DISCRIMINATOR: flag the yardstick, never the ratified line. The body below is the sweep's report VERBATIM.

**PROME verification at the artifact before filing (11:0x ET), all VERIFIED at the line:**
- `FORGE/tools/market-data/vix_futures.py:39` `AVG_STEEPNESS = 5.6`
- `AGENTS/HAWK/scripts/thresholds.py:39` `BRENT_PEAK = 116.38  # Post-strike peak (Apr 2026)`
- `scripts/validate_all_baseline.json` `"swept": "2026-09-10"`, `"C2_kb_stale_by": 534`
- `AGENTS/WAL/scripts/derived_drift_check.py:193` `BASE_DRIFT, BASE_REVIVED = 12, 68 # RE-BASELINED 2026-08-28`
- `AGENTS/FALCON/scripts/hormuz_transit_watch.py:58` `BASELINE = 88`

**Headline:** no exact HANS-pattern instance (a hardcoded seasonal norm with a GATE reading the gap). **Two live YARDSTICKs:**
- FORGE `vix_futures.py`'s contango average, which is **PROME's** own tool, consumed by VIOLET.
- HAWK's frozen Brent peak.

Two governance counters are built the same way: DAEDALUS/PROME `validate_all`, and WAL's drift check. **Done-when per L441:** each holder recomputes from source, or declares the constant with a vintage AND a re-check date.

---

I found two live derived metrics in the dangerous class, where the hardcoded constant sits on the comparison side (both at FORGE/VIOLET), plus two governance counters built the same way. Nothing matches the HANS pattern exactly (a hardcoded seasonal norm with a gate reading the gap). The HANS fix itself holds: `82.0` now appears in HANS scripts only in comments and in `test_hans.py`.

### Census table

| # | file:line | desk | metric | frozen constant / vintage | fresh side | live threshold or gate reading it | verdict | conf |
|---|---|---|---|---|---|---|---|---|
| 1 | `/home/willi/Research-workspace/FORGE/tools/market-data/vix_futures.py:39`, used at `:142` and `:165` | FORGE (consumed by VIOLET) | M1:M2 VIX contango classification `BELOW_AVG` | `AVG_STEEPNESS = 5.6`, described as the "historical avg". No window, no vintage in the code. Added 2026-04-15 (commit 673c068ca). Source is KB-VIO-025 (2026-04-15). | daily CBOE settle steepness, both strict and roll-adjusted | VIOLET boot prints `adj['classification']` (`AGENTS/VIOLET/scripts/thresholds.py:599`). No GATES.tsv row (SEARCH-NOT-FOUND). | **YARDSTICK**. VIOLET already recorded that the static bands are "regime-blind" (KB-VIO-032). The rolling percentile it asked for is SEARCH-NOT-FOUND in `AGENTS/VIOLET/scripts`. | VERIFIED |
| 1b | `/home/willi/Research-workspace/AGENTS/VIOLET/scripts/thresholds.py:58` | VIOLET | `m1m2_adj_pct` colour band, green edge | `"green": 5.6`, the same carried average used as a band edge | `m1m2_adj` from #1 | the boot colour classification at `:527` | **YARDSTICK** (inherits #1). The other edges (8.99 and 12.0) are lines. | VERIFIED |
| 2 | `/home/willi/Research-workspace/AGENTS/HAWK/scripts/thresholds.py:39`, used at `:118` and `:178/188` | HAWK | Brent "vs Peak" distance (%) | `BRENT_PEAK = 116.38`, "Post-strike peak (Apr 2026)". No re-check date. | live BZ=F price from yfinance | Runs every HAWK boot (`scripts/boot.py:43`). It appends to `PRICE_BREACHES.tsv`, but that file is banner-FROZEN and its last row is 2026-04-20. No gate reads it. | **YARDSTICK**. Nothing updates the peak if price later exceeds it. BRENT STATUS quotes a different peak ("~$110 Apr 7"). I did not check whether 116.38 has since been exceeded. | VERIFIED at the line; staleness INFERRED |
| 3 | `/home/willi/Research-workspace/scripts/validate_all.py:753-757` plus `scripts/validate_all_baseline.json`, compared at `:500` and `:642` | PROME/DAEDALUS (governance) | C2 count of KB rows past Stale_By; D1 count of desks over read-cap budget | `C2_kb_stale_by: 534`, `D1: 6`, `"swept": "2026-09-10"`. It has a vintage but no re-check date. `--rebaseline` exists. | live counts | the validate_all verdict. FINDINGS fires only on a rise above the baseline. | **YARDSTICK (governance)**. Clearing old rows lets the same number of new ones go unflagged. | VERIFIED |
| 4 | `/home/willi/Research-workspace/AGENTS/WAL/scripts/derived_drift_check.py:193`, compared at `:223` | WAL (governance) | derived-drift and revived-claim counts | `BASE_DRIFT, BASE_REVIVED = 12, 68`, "RE-BASELINED 2026-08-28". The rule is "re-baseline on each sweep", with no date. | live scan counts | WAL boot step 4c (`AGENTS/WAL/CLAUDE.md:59`) prints ✓ when at or below the baseline | **YARDSTICK (governance)**. Same failure path as #3. | VERIFIED |
| 5 | `/home/willi/Research-workspace/AGENTS/FALCON/scripts/hormuz_transit_watch.py:58`, used at `:146/149` | FALCON | Hormuz transits as % of pre-war baseline (the "15/88" figure) | `BASELINE = 88`. Provenance pinned 2026-07-27: trailing-12-month median of the same series over the closed window 2025-02-28..2026-02-27. | newest PortWatch daily count | Display only. The alert uses band transitions on the raw count (`BAND_EDGES`), not the %. | **DECLARED**. A closed pre-war window cannot drift. It has no re-check date, which the row's done-when asks for. | VERIFIED |
| 6 | `/home/willi/Research-workspace/AGENTS/SAM/scripts/cftc_jpy.py:57`, used at `:310` | SAM | net short as % of the historical record | `REFERENCE_NET = -188077` (record low of 2007-06-26, "reviewed August 2026") | weekly CFTC net position | Display only. `WARN_NET` compares the raw net. | **DECLARED**. It fails loud: a new record shows as more than 100%. | VERIFIED |
| 7 | `/home/willi/Research-workspace/AGENTS/HAWK/scripts/war_monitor.py:48`, used at `:213` and `:329/331` | HAWK | scenario-shift interpretation | `SCENARIO_BASELINE {"D":82,"C":12,"B":6}`, FROZEN 2026-07-12, banner dated 2026-09-02 | keyword signals | The interpretation line only. The baseline cancels out (new = baseline + shift), so in practice this is a keyword-delta check. | **DECLARED** (a historical artifact per its banner) | VERIFIED |
| 8 | `/home/willi/Research-workspace/AGENTS/BRENT/scripts/cot_grade.py:90` | BRENT | `BASE_8WK = 122904.5` | trailing-8-week median over 2026-06-16..08-04, frozen | none: "DISPLAY-ONLY (never compared)" | none | **DECLARED**. The bars next to it are LINE. | VERIFIED |

**SOURCED** (the norm is recomputed at runtime), all verified at the line:
- HANS `fetch_eu.py:286-438`: `agsi_norm`, the template fix. It needs 5 years of AGSI history or it fails closed.
- DEWEY `gie_pull.py:141-163`: same-date comparison against prior years.
- MIDAS `metals_watch.py:189-214, 543`: LME copper stocks against a live 2-year median.
- FALCON `bypass_watch.py:102, 130`: base is the last 60 days of data.
- HENRY `credit_monitor.py:160`: volume against a 20-day average.
- BRENT `refiner_ratios.py:91`: 6-month mean and standard deviation.
- BRENT `eia_weekly.py:356`: prior-year weeks.
- SAM `cpi_japan.py:493`: an earlier instance of this class ("typical 30-40bp"), already fixed.
- SAM `fxy_options.py`: self-calibrates on 60 days.
- LIQUID `sofr_dispersion.py`: rolling z-score.
- CREED `s8a_relative.py`: live distribution.
- BOND `grade_auction.py`: corpus median and mean.
- VULCAN `edgar_watch.py:314, 366`: median lag from history.
- LABOR `state_claims_breadth.py`: YoY.
- WATT `power_watch.py:365`: window median.
- LABOR `job_postings_tracker.py`: the Feb-2020 = 100 index base is defined by the source.

**LINE, count only:** about 18 lines ruled out along the way (not a full list). They sit in BRENT `cot_grade`, MIDAS `grade_cot3`, SAM (`grade_8_14_branch`, `cftc_jpy` DRIFT_BAR and WARN_NET, `usdjpy` range, `jgb_auctions` BTC, `mof_flows` ladder), HENRY VOL_SURGE, VULCAN BREADTH_COLLAPSE_PP, CREED bands, HAWK price ladder, BRENT eia CUSHING/UTIL, HANS boot bands, WATT LMP bands, the other VIOLET BANDS, OTTO CONFIRM/REFUTE, and the TERRY/FLG Q1 grade anchors.

### Nearby findings outside the class
- **HAWK `sanctions_tracker.py:24`, `:300-303`:** `BASELINE_METRICS` is labelled "placeholder". It is the displayed value itself, not a yardstick, but alerts fire from it on every boot (`boot.py:47`). That is a frozen value presented as live.
- **CARL `abs_monitor.py:280-283`:** prints hardcoded Jan-2026 ABS values as "context". `ABS_BASELINE.tsv` is banner-FROZEN 2026-07-10.
- **OTTO `severity_divergence.py:66`:** `R0 = 27.05%` appears only in the docstring. Code use is SEARCH-NOT-FOUND.
- **FLG TRIGGERS T-07:** the "baseline $14.24" ladder has no script implementing it (`14.24` is SEARCH-NOT-FOUND in `*.py`).
- **CREED-T-03:** its baseline is disputed in the registry and awaiting Will (KB-CREED-024). It lives in the registry only.
- **MARCO `statcan_travel.py:55`:** `BASELINE` is a reproduction fixture, not a comparison.

### Commands (run from `/home/willi/Research-workspace`; `archive/`, `_archive/`, `__pycache__`, tests, runs and research were excluded with `grep -v -E '/(archive|_archive|__pycache__|tests?|runs|research)/|test_'`)
```
grep -rnE -i '(norm|baseline|5.?yr|five.?year|seasonal|typical|normal|denominator|base.?rate|pre.?war|...)' --include='*.py' --include='*.sh' --include='*.js' AGENTS FORGE/tools scripts PROME/tools | grep '[0-9]'
grep -rnE -i '([A-Za-z_]*(norm|baseline|base|avg|average|mean|5yr|seasonal|typical|normal|denom|ref|hist|median|prior|pre_?war|ttm|trend|expected|par)[A-Za-z_0-9]*|"[^"]*(norm|...)[^"]*")\s*[:=]\s*[-+]?[0-9]+' <same dirs>
grep -rnE '^\s*[A-Z][A-Z0-9_]{2,}\s*=\s*[-+]?[0-9][0-9_]*(\.[0-9]+)?\s*(#.*)?$' --include='*.py' <same dirs> | grep -iE 'norm|base|avg|mean|median|seasonal|typical|hist|ref|pre-?war|5.?y|ttm|vs|20[0-9]{2}-'
grep -rnE -i '(norm|baseline|avg|average|mean|seasonal|typical|normal|5yr|five|median|ref)[A-Za-z_]*\s*=\s*\{' --include='*.py' <same dirs>
grep -rnE -i '(5|five)[- _]?(yr|year|y)[- _]?(avg|average|mean|median|norm|range|seasonal)|seasonal (norm|avg|average)' --include='*.py' --include='*.sh' <same dirs>
grep -rnE -i 'pre-?war|pre-?crisis|pre-?strike|peacetime|pre-?covid|feb.?2020' --include='*.py' <same dirs>
grep -rnE '^\s*[A-Z_]*(PEAK|TROUGH|HIGH|LOW|START|ENTRY|ANCHOR|SPOT)[A-Z_]*\s*=\s*[0-9]' --include='*.py' <same dirs>
grep -rnE -i '\b(baseline|BASE_[A-Z]+|KNOWN_[A-Z]+|EXPECTED_[A-Z]+)\b\s*[:=]\s*[0-9]' and '(>|>=)\s*(baseline|base|BASE_[A-Z_]+)\b' --include='*.py' <same dirs>
grep -nHiE 'norm|baseline|avg|average|mean|median|5.?yr|seasonal|typical|vs ' AGENTS/{HANS,REGINALD,CREED}/registry/THRESHOLDS.tsv AGENTS/{FLG,FERT}/workbook/TRIGGERS.tsv AGENTS/TERRY/grade_config.json
grep -nE -i 'm1m2|contango|peak|derived_drift|validate_all' PROME/GATES.tsv   # 0 hits
grep -rnE '14\.24' --include='*.py' AGENTS scripts FORGE                        # 0 hits
```

What the census doesn't cover: markdown metric definitions that no script implements, the TSV workbooks under `data/` and `outputs/`, and shell and JS files beyond the keyword greps.