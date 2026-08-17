# Silent-Fallback-Green Sweep 2026-08-17 — raw reader reports (PAT-100 companion)

**Fan-out:** 4 readers (1: FORGE/DEWEY/BOND/ORACLE/SHADE/MIDAS · 2: VIOLET/TERRY/HENRY/REGINALD · 3: SAM/HAWK/FALCON/MARCO/LABOR/CARL · 4: boot-wrapper swallow layer). Reader-3's full table lives at `sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` (reader-authored file, DAEDALUS dir). This file preserves the raw deliveries + every NOT-READ list. Commission: PROME 8/17 packet (SAM cpi_japan exhibit).

**Reader ops:** readers 1 & 4 idled holding, delivered on chase (the standing floor); reader 3 delivered unprompted with a persisted file; reader 3 re-tasked once (fxy_options NOT-READ closure).

**Synthesis verifications performed by DAEDALUS before acting (PAT-032 discipline):**
- 9-wrapper stderr-discard: CONFIRMED — exact string in BRENT/CARL/HAWK/SAM/OTTO; semantic variants in MARCO(:141)/VIOLET(:102)/REGINALD(:54)/LABOR(:61, drops stderr even on its own rc=2 alert path).
- CARL `gas_tracker.py:44` FRED-key WARN to stderr + rc0: CONFIRMED.
- HENRY `boot.py` credit-leg filter lacks `⚠`: CONFIRMED (markers tuple :148) + `if code != 0 and not out` partial-failure gate :142.
- SAM boot summary rc-only green "✅ All scripts completed successfully": CONFIRMED (:277).

---

## Reader-3 raw delivery (fetcher clusters: SAM/HAWK/FALCON/MARCO/LABOR/CARL)

TALLY (14 of 15 traced): 5 CLASS-HIT · 3 DISTINGUISHED (2 with a class-hit sub-path) · 6 FAIL-LOUD · 1 NOT READ.

CLASS-HIT: CARL/housing_pulse.py · CARL/gas_tracker.py · HAWK/thresholds.py · HAWK/war_monitor.py · SAM/jgb_auctions.py
DISTINGUISHED: MARCO/h2a_pull.py (best in set) · LABOR/warn_texas.py (--raw sub-path hits) · SAM/usdjpy.py (h.empty sub-path hits)
FAIL-LOUD: FALCON/hormuz_transit_watch.py · LABOR/form4_scanner.py · SAM/mof_flows.py · SAM/cftc_jpy.py · MARCO/google_trends_pull.py · LABOR/job_postings_tracker.py

Sweep-level finding: the boot COLLAPSE layer is part of the rendering surface — CARL's `KEY_MARKERS` (boot.py:52) lacks "ERROR" and misses `(AAA unavailable…)`, deleting CARL's two loudest failure renderings from the boot brief. A script-only fix will not reach CARL.

TOP 3 BY FLEET RISK (reader-3's ranking):
1. CARL/housing_pulse.py — boot-wired, rc=0 always; lines 220-227 print FOUR HARDCODED figures every run in live-table format, three undated (`Fannie MF DQ: 0.74% (last known)`, `CMBS MF DQ: 7.15% ATH (Trepp Mar)`, `FL Condo: 13.2mo`, `Existing Home Sales: 3.98M SAAR`); failed FRED series prints unmarked `ERROR` that CARL's filter DELETES while the hardcoded literal survives on the substring "RED". Plus `check_fannie_mf` HTML regex can render a fabricated `MF Serious DQ: X.XX% [RED]` threshold state.
2. SAM/jgb_auctions.py — INVERTED form: serves a false NEGATIVE. `except Exception: return None` (64-69) collapses timeout/DNS/500 into the 404 branch; probe prints `No auction results found in the last 8 days.` + rc=0, byte-identical to a quiet week. This is the grading instrument for the 8/20 JGB 20Y auction = SAM's promoted Pillar-2 adjudicator. Second defect: parse fallback (101-107) grabs any "Year" row and stamps the PROBED date (174) — wrong-date row can enter JGB_AUCTIONS.tsv under `✅ Orderly`.
3. HAWK/thresholds.py + war_monitor.py — `regularMarketPrice or previousClose` (:46) silently serves yesterday's close forced to `(+0.00%)`, price line filtered from the collapsed brief; `--quick` computes cache vintage (:141) that main() never prints. war_monitor: feeds.reuters.com NO LONGER RESOLVES (live-verified URLError; BBC 200 same run), hidden by bare `except: return []` (:131); any partial-source run byte-identical to full coverage; with `--save` a network outage writes baseline D/C/B into SCENARIO_HISTORY.tsv permanently. HAWK feeds BRENT on a live GATE-FALCON-001 R3 HOLD.

Exemplars to cite in fix packets (in-fleet, no invented standard): FALCON/hormuz_transit_watch.py (data's own date + age + ⚠️ STALE tag + distinct rc per failure mode) · LABOR/form4_scanner.py (standing `found | parsed | unparsed` line every run) · MARCO/h2a_pull.py (stamps `via=wayback | snap=<ts>` into the ARTIFACT header — downstream inherits source-mode).

rc=0 does no work in 4 of 5 CLASS-HITs (housing_pulse, gas_tracker, war_monitor, jgb_auctions).

Proposed refinement to `finding_fail_loud_on_incomplete_data` (reader-3, flag only — SAM owns the file): the class definition does not obviously cover the INVERTED cases — jgb_auctions/war_monitor serve a stale VERDICT ("no auction", "status quo holding"), not stale data; a fetch failure rendered as a data verdict is the same defect with the sign flipped, and the more dangerous half because a negative reads as reassurance.

NOT-READ (reader-3): SAM/fxy_options.py (630 lines, not reached; SAM boot whitelist carries three markers for it — re-tasked 8/17, addendum pending). cpi_japan.py excluded per scope.

## Reader-4 raw delivery (boot-wrapper swallow layer) — delivered on chase

[Preserved verbatim below]

Per-wrapper verdicts (22 wrappers): SWALLOWS — SAM, CARL, BRENT (mitigated, best rc design: tri-state OK·FINDINGS·FAIL rc2, refuses bare all-clear when findings exist — but rc-0-with-warning still ✅), HAWK (rollup `extract_alerts` keyed on 🔴/🟠/ALERT/CRITICAL/WARNING drops ⚠️ → "✅ No alerts" prints over a warned run), LABOR (rc 0,2=OK), MARCO (partially hardened post-H-2A; `lines[-4:]` truncation drops early ⚠️ when >4 marker lines), OTTO (rc 0,1=OK), VIOLET, HENRY (credit filter omits `⚠` — drops `⚠ FLAGS:` and `DISPERSION: ERROR`; `if code != 0 and not out` lets partial-output failure pass), OZK (discards rc AND stderr AND non-JSON stdout; all failure modes → one "⚠️ price fetch failed"; stale-but-parseable JSON renders as live prices, no vintage). EXIT-CODE-ONLY — REGINALD (full stdout passthrough, stderr dropped on rc0). PRESERVES — CORAL (only capture-based wrapper appending stderr unconditionally), TERRY (advisory by design), WATT/VULCAN/MIDAS (marker contract; power_watch/metals legs rc-only), FERT (verified BY EXECUTION: ⚠️ staleness line surfaced verbatim, verdict flipped to REVIEW rc=1 — the only fleet pattern where a fetcher caveat provably reaches the operator's verdict line), LIQUID (in-process; footer prints `{ERRORS} fetch errors`, rc1 on errors), RED (⚪ no-data visually distinct), ZHAO (per-line ⚠️ but NO global verdict, always rc0). NO-WRAP — CREED, YEYOU.

THE SYSTEMIC FINDING: nine wrappers share one semantic line — `if returncode != 0 and stderr: output += STDERR` — stderr is DELETED when rc==0, before any filter runs; no marker list can rescue it. Confirmed producers on the deleted path: CARL gas_tracker.py:44, consumer_pulse.py:37, housing_pulse.py, thresholds.py, BRENT thresholds.py:67 — all print `WARN: FRED_API_KEY not found…` to stderr then return 0; CARL and BRENT boots render "✅ All scripts completed successfully."

Correction to the commission's premise (verified): SAM's collapse filter DOES contain ⚠️ (:227) — cpi_japan's stdout warning survives into the collapsed BODY; the real swallow is (a) the boot summary table + final green line are pure-rc, (b) the stderr gate. Plus a producer-side manufactured green: transient e-Stat failure → `fetch_series()` `{}` → `append_tsv` 0 → `✓ CPI.tsv up to date (no new prints)` (:442) over a FAILED fetch, rc0. The credential path was hardened to rc1 on 8/4 (:434); the transient path was NOT.

8/16 marker-contract fix verified GOOD by execution: WATT/VULCAN/MIDAS/FERT `run_alert()` test `"⚠️" in out` (VS16, hex e2 9a a0 ef b8 8f); ledger_staleness emits the identical codepoint. FERT boot RUN live: staleness ⚠️ surfaced verbatim, verdict REVIEW rc=1. Contrast: HENRY credit_monitor emits bare `⚠` U+26A0 no-VS16 — would fail the run_alert contract if ever wired to one.

NOT-READ (reader-4): LIQUID boot L300-530 (fetch-error path/collapse/footer read only) · HENRY boot L150-460 (fetcher legs + main read only) · ZHAO/RED mid-file band tables (fetch/error/render paths only) · fetcher scripts SAMPLED not exhaustive — stderr-writer list is a LOWER BOUND (30+ files incl. FORGE/tools/market-data/fetch.py) · WATT/MIDAS/VULCAN boots not executed (network+writes); verdicts from code + FERT live run of byte-identical run_alert.

Urgency (reader-4): 1. CARL+BRENT (ahead of SAM — warning only on deleted stderr, full green board with every FRED series dead) 2. HENRY credit leg (MARCO's collapse() whitelist bug unrepaired, feeds a live position's kill line) 3. SAM cpi_japan transient path 4. OZK 5. HAWK rollup contradiction.

Generalizable fix, proven in-fleet: adopt the WATT/VULCAN/MIDAS/FERT contract — relay stdout AND stderr unconditionally, verdict from marker-present never rc; producers owe one canonical line (`SOURCE: LIVE|CACHED asof <date>`).

---

## Reader-3 addendum (re-task closure): SAM/fxy_options.py — CLASS-HIT (6th)

Appended by reader-3 to `sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` before idling. Headlines: ① stale-spot anchor risk on the 25d RR thesis-side verdict, no marker; ② truncated-expiry axis — `except: continue` (406-407) drops failed expiries, `Expiries scanned: N` counts survivors as a fact about the scan, headline can silently re-anchor tenor (disclosed via DTE in header, not flagged); ③ **fabricated-signal path: missing `openInterest` column → 0 → `pc_ratio=999.0` → `999.00x 🔴 Put-heavy (bearish)` — a boot-whitelisted 🔴 manufactured from absent data; 1 sentinel row LIVE in FXY_OPTIONS.tsv**; ④ partial pull can block its own retry via `_has_today_row` skip (checked NOT currently live — the 48 blank-vol rows are legacy schema, verified before writing); ⑤ every degraded path rc=0. Revised reader-3 tally: 15/15 traced — 6 CLASS-HIT · 3 DISTINGUISHED · 6 FAIL-LOUD.

## Reader-1 raw delivery (FORGE/DEWEY/BOND/ORACLE/SHADE/MIDAS) — delivered on chase

Tally: 13/13 traced (static traces, read-only — no live execution; verdicts satisfy trace-completeness, not the ★ watched-line bar). 5 CLASS-HIT · 4 DISTINGUISHED · 4 FAIL-LOUD.

CLASS-HIT:
- **BOND/data/refresh_auction_history_prome-spawned.py — reader-1's worst-in-set.** `_cmt_for` serves most-recent-prior CMT close with UNBOUNDED lookback and records NO DATE anywhere — same-day and 90-day-old closes write byte-identical `cmt_close_prior_day,tail_vs_cmt_bps` CSV cells feeding BOND's auction-tail instrument; console `[refresh] wrote v2 -> …` rc=0 both. Plus its OWN docstring GOTCHA #1 names the empty-200 trap and the code has no guard — `out.to_csv` overwrites v1 with an empty file BEFORE validation, then enrich_v2 KeyErrors (data destroyed, then a confusing traceback). Plus 4×429 on FRED → `obs=[]` → all-null tail column at rc=0.
- **FORGE/tools/news-sweep/sweep.py — highest reach.** Cron M-F 8:30 ET, routes into every agent's inbox, unconditionally overwrites shared latest.json/latest.md. All-feeds-down prints `✅ Sweep complete: 0 total, 0 actionable, 0 KNOWN, 0 noise` rc=0 — same ✅ as a healthy 143-article run. Per-source bozo errors go to stderr, never counted. No failure counter exists in the summary at all.
- **SHADE/research/FABN_PEER_SPREAD_NPORT_2026-07-27.py** — ① curve backfill ≤5d prior, key is the PERIOD never the source date — identical line either way, feeding `>>> ATHENE PEER PENALTY: +43.2bp`; ② partial curve defeats the emptiness test (`if not curve[pe]` only checks empty) — 2Y+30Y-only lands and `tsy()` interpolates a 7Y benchmark between them; ③ §1 `if not raw: break` truncates enumeration uncounted. The number exists specifically to REFUTE an incentive-flagged source.
- **FORGE/tools/market-data/fetch.py** — scoped to `snapshot`: `display_snapshot` drops the As-of stamp entirely (price/prices/fred DO stamp vintage incl. `⚠stale`); `--json` snapshot compacts to `{"p","chg"}` also stripped; cache hits logged only to logs/market_data.log. TTL-bounded ≤1hr caps severity. Also: FRED/EIA failure renders `ERROR` line but rc=0 (only --history has the rc=3 guard — that guard is the model); `--delta` silently drops below-threshold tickers.
- **FORGE/tools/market-data/dashboard.py** — `_date_stamp` returns "" for every price row (price branch never sets `entry["date"]`) — blank As-of whether live/cached/prior-close while the docstring asserts "intraday-live"; corrupt last_run.json → `except: pass` → `--cron` prints NOTHING, identical to a quiet run. Bonus defects: `entry["change"]=pd.get("change")` but fetch.py returns `change_pct` — the Δ column is silently None EVERY run; `--tier`/`--agent` + save runs a second full fetch.

DISTINGUISHED: ORACLE/kalshi.py (markers in default line; but no-trade market prints `0.0%` as a probability and logs 0.0 to the TSV defeating the None filter; `--log` writes only successes with no failure account — 12-of-12 vs 12-of-18 indistinguishable; THIN_VOLUME dead code) · BOND/monitors/fr2004_fetch.py (near-exemplary; STALE banner stderr-only + rc0 — a stdout-capture path keeps the confident table and loses the warning) · DEWEY/ofr_stfm.py (**counter-example the class is defined against** — docstring names the trap, source-mode `[Final→…, then Preliminary (98 obs)]` in the default line; gap: cmd_gate rc0 on all-ERROR) · FORGE/market-data/vix_futures.py (as_of in the headline, probe-don't-calculate; residual: a 6d-old settlement prints as confidently as same-day, no age marker).

FAIL-LOUD: MIDAS/cot_gold.py (**best-in-fleet** — rc=3 stale-vintage WAIT, rc=2 reconciliation fail, built FROM finding_partitioned_source_returns_stale_window_at_200; one PAT-074 nit: without `--expect` the line still reads "(as-of Tuesday, in-row verified)" — green words certifying a check that only runs when --expect is passed) · FORGE/filing-watch/poll_edgar.py (errors reach stdout+artifact+rc; notes: headline count prints before error block; corrupt seen_filings.json → every filing isNew — false flood) · DEWEY/fetch_url.py (exemplary distinct-rc negatives; residual: `_decompress` OSError returns still-compressed bytes → garbage → primary-grade `NO MATCH … HTTP 200` — right rc, wrong reason) · DEWEY/trace_bond.py (refuses to invent a price by design).

NOT-READ (reader-1): no live execution (mandate) · news-sweep/config.py + market-data/config.py dependency modules (out of scope, no verdict change) · flagged adjacent: WATT power_watch.py imports eia_fetch_facets from fetch.py and inherits its cache layer — sweep next.

Reader-1 top-3: 1. BOND refresh_auction (stale value in a PERSISTED artifact with no vintage field at all + documented-unguarded empty-200 overwrite) 2. news-sweep (reach) 3. SHADE FABN (wrong number exactly where independence was the point).

Reader-1 cross-cutting (for PATTERNS): the recurring gap in all 5 CLASS-HITs is NOT a missing warning — it is a warning that exists on stderr/docstring/comment while stdout, the WRITTEN ARTIFACT, and rc all stay green; 3 of 5 also OVERWRITE their output artifact with the degraded result so the state persists past the run. The two clean counter-examples (cot_gold, ofr_stfm) both put source-mode in the default line AND spend an exit code on staleness. Suggested standard: any fetch tool with a fallback must (i) carry served vintage/source-mode in its non-verbose default line AND in any file it writes, (ii) reserve a distinct nonzero rc for "served, but not fresh."

## Reader-2 raw delivery (VIOLET/TERRY/HENRY/REGINALD) — delivered unprompted

Tally: 13/13 traced end-to-end, ZERO edits; only execution = offline re-run of VIOLET's KEY_MARKERS filter over synthetic lines to PROVE the SHOWN/HIDDEN claims. 5 CLASS-HIT · 7 DISTINGUISHED · 1 FAIL-LOUD.

CLASS-HIT:
- **REGINALD/scripts/insider.py — reader-2's worst-in-set.** `✅ No open market insider purchases across any thesis name.` is the IDENTICAL output of a working scan and a total EDGAR outage, rc=0, every boot — on the desk's thesis-CHALLENGE detector whose null state is load-bearing evidence FOR staying short. UA is `research@example.com` = the documented EDGAR-403 class. Second leg: parse failures counted into `total_noise`, inflating "Routine"/deflating "Buys" — partial parse outage reads as CONFIRMED routine activity.
- **HENRY/scripts/gamma_flip.py — CLASS-HIT at the caller** (CLI is DISTINGUISHED: prints `src=cboe`/`src=yfinance`). HENRY boot.py:121-131 never prints `r['source']` — silent demotion to the source this file documents as having zeroed 97% of the ^SPX chain renders byte-identical. MIN_CONTRACTS=400 vs healthy ~6,000 — a 90% degraded chain passes. Number publishes to PUBLISHED.tsv for other agents' gates. One-line fix: add `src={r['source']}` to boot.py:131.
- **VIOLET/scripts/fred_fetch.py (partial leg)** — failed series' row VANISHES from the table while the 🟢 BLOCK-LIFTED verdict prints regardless of completeness, rc=0. ★ Verified by executing VIOLET's collapse filter: `[ERROR]` lines HIDDEN, cache-mode line HIDDEN, verdict SHOWN. Losing BB silently deletes the CCC-BB dispersion line (a registered gate leg). Two-party defect: script omits rows without a completeness statement AND consumer's marker list hides the evidence. Shared-helper note: imported only by analog_pull.py; other fleet `fred_fetch` symbols are the UNRELATED FORGE fetch.py function — a live name-collision trap for symbol sweeps.
- **VIOLET/scripts/skew_trajectory.py** — `extract_window` has no proximity guard: when the 2014-15 yfinance leg fails, episodes 1-2 silently re-anchor to the FIRST 2018 date; `df.empty: continue` prints NOTHING. Overwrites the dated research artifact unconditionally — the degraded run becomes the citable record. `load_all_data()` inherited by regime_termination.py. Fix = one assert on |actual−fire| ≤ N days.
- **VIOLET/scripts/vix_options.py** — missing/headerless ledger and empty `tk.options` render the byte-identical benign `· no change in VIX_OPTIONS.tsv` line (SHOWN at boot); healthy run's Forward OI line simply ABSENT — distinguishable only by absence, the exact finding_silent_blank_evades_review shape its own docstrings warn about for OTHER guards.

DISTINGUISHED (exemplars starred): ★ VIOLET/move.py (fallback prints `⚠️ FALLBACK [UNCORROBORATED — known-unreliable source]` + vintage + "Do NOT bank a threshold on this"; all-dark = 🔴 rc=2; gap: boot omits --strict so rc carries no info — text saves it via KEY_MARKERS) · VIOLET/thresholds.py (walked-back m1m2 prints its own settle date + computed lag `[settle 2026-08-12 — T-5 vs row date]`; STALE-COLUMN GUARD writes NULL loudly; gaps: `{key}_error` never rendered in text path; unconditional `✓ no threshold breaches` — hidden by boot filter, misleads direct CLI only) · VIOLET/cftc_cot.py (report_date IS the freshness; soft spot: hand-rolled weekday heuristic ignores the 15:30 ET post) · ★ TERRY/chain_fetch.py (**the TTL answer done right**: `Spot: 87.21 (as-of 2026-08-17 14:49 (cached))` — ORIGINAL pull time + "(cached)" appended, rides into --json as spot_asof; missing venv FATAL rc=2) · ★ TERRY/paper_book_mark.py (prior mark kept, labelled `[UNMARKED (FETCH-ERROR:…)] ⚠ STALE 21bd`, mark_asof NOT advanced so the staleness clock runs on truth; rc=0 even at 100% fail — count line carries it) · TERRY/snapshot.py (per-ticker ERROR rows; flags FORGE fetch.py cache-hit invisibility downstream) · TERRY/options/partb_realized_moves.py (skipped-by-name; skip line far up-screen from the summary table).

FAIL-LOUD: REGINALD/kre_float.py (price leg loud in BODY — but `main()` returns on failure WITHOUT nonzero exit, so boot prints ✅ KRE Float OK; corrupt state file swallowed → renders as "First reading — saving as baseline", byte-identical to a genuine first run, delta/shrinkage verdict silently skips).

NOT-READ (reader-2): none — all 13 traced; 3 non-assigned callers read to resolve behavior (VIOLET/HENRY/REGINALD boots) + grep-level FORGE fetch.py cache layer.

Reader-2 top-3: 1. insider.py 2. gamma_flip@caller 3. fred_fetch partial leg.

Reader-2 cross-cutting (n=4): move.py/chain_fetch/paper_book_mark/partb all render fallback correctly and were ALL built or hardened AFTER a live incident of this exact class — **the hits are the surfaces that have not yet had their incident.** Second pattern (n=3: insider, kre_float, partb): unmistakable error in the BODY + rc=0, under boots that key ✅/❌ on rc — the loud text and the green verdict coexist in the same run.
