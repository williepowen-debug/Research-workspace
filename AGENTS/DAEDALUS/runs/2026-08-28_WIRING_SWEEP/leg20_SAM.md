# Leg ⑳ Boot-Sequence Audit — SAM (Japan / BOJ / JGB / carry)

Read-only static audit + one write-free execution (`boot.py --tools`). Repo root
`/home/willi/Research-workspace`. Today 2026-08-28. `git status --short AGENTS/SAM/`
was clean before AND after the run.

## 1. Boot steps as CLAUDE.md declares them (§SPAWN PROTOCOL, lines 20-40)

| # | Claim (verbatim, truncated) | Instrument |
|---|---|---|
| 0 | `git pull` — sync from GitHub | git |
| 1 | Read `thesis/THESIS.md` — core thesis, channels, conviction, thresholds | manual Read |
| 2 | Read `STATUS.md` — current state: prices, probabilities, position, dashboard | manual Read |
| 3 | Read `docket/CALENDAR.md` — upcoming dates, auctions, releases, thresholds | manual Read |
| 4 | Read `thesis/timeline/TIMELINE.md` — narrative progression, branch points | manual Read |
| 5 | Read `MEMORY.md` — CHANGES SINCE + NEXT SESSION items | manual Read |
| 6 | Scan `thesis/PREDICTIONS.tsv` — flag predictions due/stale; read calibration preamble | manual Read (no script) |
| 7 | Market refresh — "Runs the full automated sweep" via `boot.py` (14 boot-wired scripts, see §2) | `scripts/boot.py` |
| — | WALTER inbox glob + board_log append | manual/git mv |

## 2. `boot.py` BOOT_SEQUENCE (14 wired scripts) — static trace

| Script | Claim | Delivered verdict | Evidence |
|---|---|---|---|
| `thresholds.py` | FX/oil/**JGB** threshold monitor, breaches + near-miss | **SUBSTITUTED** (JGB legs only) | `thresholds.py:53-58,217-220` — JGB 10Y/30Y/40Y rows are printed as `⚪ MANUAL CHECK` static labels ("threshold X.XX% — check manually via web"); no live yield value is fetched or compared here despite being formatted identically to the live FX/oil rows. FX/oil legs (USDJPY/FXY/BZ=F) are live and DELIVERS. |
| `usdjpy.py` | USDJPY history + at-a-glance, MOF-touch marking | **DELIVERS** (with an honest self-reported gap) | `usdjpy.py:341-407` — explicitly does NOT use mtime staleness (documented rejection, `usdjpy.py:126-130,342-345`); uses an hourly-vs-daily disagreement alarm instead. If the hourly fetch returns an empty frame (no exception), it prints `⚠️ hourly cross-check UNAVAILABLE — L3 test (a)... NOT EVALUATED` (`usdjpy.py:388-392`) rather than staying silent — this is a SILENT-class failure mode that was deliberately closed 2026-08-17 per its own comment. |
| `jgb_yields.py` | Daily JGB yield curve, MOF CSV | CANNOT-JUDGE | grep-level only (`except...return None` at :54,56); not fully traced — no time in budget to verify gating logic end-to-end. |
| `jgb_auctions.py` | MOF auction results, auto-probe lookback | CANNOT-JUDGE (partial trace favorable) | `jgb_auctions.py:62-98` shows a deliberately FAIL-LOUD design distinguishing `absent` vs `error:*` (own comment names this the inverse of a sibling cpi_japan.py bug that served stale data as fresh) — promising, but full path not traced. |
| `boj_ois.py` | BOJ hike pricing, cumulative + per-meeting marginal + unpriced room | CANNOT-JUDGE (partial trace favorable) | `boj_ois.py:37-41` — staleness explicitly keyed to CONTENT VINTAGE not mtime, matching fleet PAT-044; asserts cumulative basis every run and hard-stops if absent (:23). Not fully traced past line ~450. |
| `cftc_jpy.py` | CFTC JPY COT positioning vs Jul-2024 peak | **DELIVERS**, on a documented RETIRED basis | `cftc_jpy.py:40-56` — `JUL_2024_PEAK_NET = -180000` is admitted-wrong (true extremum -188,077 per an 8/11 falsifier pass) and kept ONLY as a display basis; comment states "ALL CONTRACT GATES UNAFFECTED." Contract/alert thresholds (`WARN_NET=-150000`, short-cover %) are separate constants and unaffected. Prints unconditionally (no silent branch found). |
| `rate_differential.py` | SAM-41 rate-differential bar (newest script, Aug 27) | CANNOT-JUDGE | Not read this pass — flagged as a gap below (highest-priority follow-up: newest, least fleet-reviewed script in the sequence). |
| `mof_flows.py` | MOF weekly International Transactions in Securities | CANNOT-JUDGE | grep only; own comment at :229 flags idempotent-by-period design ("a revised week is never re-read and the TSV silently keeps" [old value]) — worth a full trace, not done this pass. |
| `xccy_basis.py` | JPY cross-currency basis proxy, CME futures | CANNOT-JUDGE | grep-level only. |
| `gpif_flows.py` | GPIF portfolio/flows | CANNOT-JUDGE (partial trace favorable) | `gpif_flows.py:35` documents a KNOWN GAP (portfolio-holdings Excel logged not parsed) in the file itself rather than hiding it; `:311` prints an explicit "between release windows, not stale" line rather than a bare silence. |
| `trade_balance_japan.py` | Japan trade balance, Phase 1 lag-test feed | CANNOT-JUDGE | grep-level only; own comment at :464 flags a literal hardcoded date going "stale silently and still exits 0" as a known risk class — not verified whether guarded. |
| `cpi_japan.py` | Japan CPI (National + Tokyo) via e-Stat API | CANNOT-JUDGE (partial trace favorable) | `:212` — explicit comment that STATUS=1 "no data" from a stale area code is a SUCCESS-shaped empty response, and the file has a dedicated `_report_staleness()` (:468) rather than silently reusing a cache. Not fully traced. |
| `catalyst_countdown.py` | Docket countdown, flags imminent + 🔴 priority | **SILENT (latent)** | `catalyst_countdown.py:116-143` — past-dated rows (`edate < today`) are collected into `past` but are **only ever printed when `upcoming` is empty** (and then only the single most recent one, line 140-142). If CATALYSTS.tsv ever accumulates an unpruned overdue row while other rows are still upcoming, it is silently dropped from every boot print — no "N stale/overdue" line. **Currently NOT tripped**: `docket/CATALYSTS.tsv` has 0 past-dated rows as of 2026-08-28 (verified: `awk` filter on col 1 < today = 0 rows). Also note :83 "Accurate only within HOLIDAY_COVERAGE_MAX_YEAR; beyond it this silently over-counts" — but this IS guarded by a loud `holiday_coverage_warning()` (:67-77), so that half is not a live gap. |
| `fxy_options.py` | FXY options OI, weekly, auto-skip if today's row exists | CANNOT-JUDGE (partial trace favorable) | `:335-354` shows a documented multi-layer fallback chain for spot price (falls to `previousClose` tagged `# STALE: prior session`) — the fallback is labeled in-band, not hidden. Not fully traced. |

**Step 6 (PREDICTIONS.tsv scan) has NO instrument at all.** `grep -rn "PREDICTIONS" AGENTS/SAM/scripts/*.py` returns zero script that reads `thesis/PREDICTIONS.tsv` (only an unrelated comment in `subagent_memory_roll.py`). The claim "flag any predictions due for resolution or gone stale" over **70 rows** (`thesis/PREDICTIONS.tsv` = 71 lines / 74,161 B) is entirely manual eyeballing every boot, with no gate, no due-date scan, no count check. This is not SILENT in the strict per-step sense (there's no script to go silent) — it is **CANNOT-JUDGE by design**: nothing mechanically verifies the scan happened or was complete. Compare to the file's own preamble, which records a real historical instance of exactly this failure mode: a stale "4 OPEN" count survived across 5 surfaces for 6 days (2026-08-07→08-13) until a later session recomputed it from the file (`PREDICTIONS.tsv` preamble line 1, "STANDING GUARD: a prediction registered AFTER the closeout sweep is precisely the one the sweep cannot see — re-run the count from the file, never re-read the row").

## 3. Collapse-mode filter (boot.py without `--verbose`)

`boot.py:271-291` shows scripts' output is filtered to lines matching a fixed `key_markers` tuple before being shown; a script with no matching line prints only `✓ ran cleanly, no alerts`. Checked: every alert-class line found in the traced scripts (`🔴`, `🟠`, `🟡`, `⚠️`) is covered by the emoji markers in the tuple, so none of the SILENT/SUBSTITUTED content identified above is being masked further by the collapse filter itself — the gaps are upstream of collapse mode, inside the per-script logic.

## 4. Read-cap leg — boot-mandated whole-file reads (steps 1–6)

Cap: OVER-CAP ≥ 54,250 B (25,000 tok × 2.17 B/tok); NEAR-CAP 32,550–54,250 B.

| File | Boot step | Bytes | Verdict |
|---|---|---|---|
| `thesis/THESIS.md` | 1 | 67,478 | **OVER-CAP** |
| `STATUS.md` | 2 | 79,059 | **OVER-CAP** |
| `docket/CALENDAR.md` | 3 | 33,306 | NEAR-CAP |
| `thesis/timeline/TIMELINE.md` | 4 | 95,716 | **OVER-CAP** (worst of the six) |
| `MEMORY.md` | 5 | 35,846 | NEAR-CAP |
| `thesis/PREDICTIONS.tsv` | 6 | 74,161 | **OVER-CAP** |
| *(context)* `CLAUDE.md` itself | — | 32,853 | NEAR-CAP |

**4 of 6 sequential boot-mandated reads are individually over the single-Read cap**; combined steps 1–6 total ≈385.6 KB (~178K tokens) before any market-refresh output is even produced. None of the six carries a rotation/archive discipline analogous to DAEDALUS's own `read_cap_check.py` convention (no `archive/STATUS_ARCHIVE_*` equivalent found for SAM's STATUS.md; SAM's `MAINTENANCE.md`/`METSUKE_MEMORY.md`/`NEXUS_BRIEF.md` are larger still but are NOT boot-mandated, so out of scope here). This is the single most consequential finding: every numbered claim in §1 steps 1, 2, 4, 6 ("core thesis," "current state," "narrative progression," "flag any predictions due") is a claim of FULL comprehension made against a file each individually too large for a whole single-Read.

## 5. `corrections_boot_check.py`

**NO.** `grep -n "corrections_boot_check" AGENTS/SAM/CLAUDE.md AGENTS/SAM/scripts/boot.py` returns nothing. SAM's boot sequence does not invoke the fleet R1-corrections check at all (contrast DAEDALUS's own charter, which wires it at step 5b).

## 6. Execution transcript

- `git status --short AGENTS/SAM/` → clean, both before and after.
- `boot.py` writes: static grep of `boot.py` shows it does not itself write files (`open(` only used for a read at :43), but it `subprocess.run`s each of the 14 BOOT_SEQUENCE scripts, several of which write to `workbook/*.tsv` (`usdjpy.py:write_tsv`, `cftc_jpy.py:append_tsv`, etc.) and hit live network endpoints (Yahoo Finance, CFTC, MOF, e-Stat). Per rule 3, the full sequence was **NOT executed**.
- Ran only `boot.py --tools` (its own docstring: "Inventory-only mode: what tooling exists, no network, no writes" — verified true, `tool_inventory()` only globs+reads `.py` files). Output: 19 tools on disk, 14 boot-wired, 5 manual-only-by-design (bis_gli, grade_8_14_branch, kura_proposal_roll, mof_exceedance, subagent_memory_roll) — **0 orphans, 0 missing, rc=0**. Confirms the drift gate is currently clean and the CLAUDE.md MANUAL-ONLY row (5 scripts) matches disk reality exactly.
- Post-run `git status --short AGENTS/SAM/` → still clean. No checkout needed.
- Ran from repo root (`/home/willi/Research-workspace`), confirming the documented cwd-proof invocation form works as stated.

## 7. Three most consequential findings

1. **Read-cap failure across the whole boot spine.** 4 of the 6 sequentially-mandated whole-file boot reads (THESIS.md 67.5K, STATUS.md 79.1K, TIMELINE.md 95.7K, PREDICTIONS.tsv 74.2K) individually exceed a single-Read cap, with the other 2 (CALENDAR.md, MEMORY.md) both in the NEAR-CAP band. No rotation discipline exists on these surfaces. Every "read X, get Y" claim in CLAUDE.md's boot steps 1,2,4,6 is unverifiable as stated. (§4)
2. **`thresholds.py`'s JGB legs are placeholder text dressed as monitored data.** The three thresholds CLAUDE.md's own KEY THRESHOLDS table calls out by name (JGB 10Y >2.40%, JGB 30Y >4.0%, implicitly 40Y) print as `⚪ MANUAL CHECK ... check manually via web` in the same visual format as the live FX/oil rows, with no live yield pulled or compared inside this script — even though a separate boot-wired script (`jgb_yields.py`) does fetch that data elsewhere in the same run. A reader scanning `thresholds.py`'s output alone would reasonably believe JGB thresholds were being actively monitored inline; they are not. (§2, row 1)
3. **Step 6 (PREDICTIONS.tsv, 70 rows) has zero instrumentation.** No script anywhere in `scripts/` reads `thesis/PREDICTIONS.tsv`. "Flag any predictions due for resolution or gone stale" is pure unmechanized human attention over a 74KB/71-row file that is itself OVER-CAP for a single Read — compounding finding #1. The file's own preamble documents a real, dated instance of this exact failure (a stale open-prediction count surviving across 5 surfaces for 6 days, 2026-08-07→08-13). (§2, footer note)

## 8. What this audit could NOT see

- 8 of 14 boot-wired scripts (`jgb_yields.py`, `jgb_auctions.py`, `boj_ois.py`, `rate_differential.py`, `mof_flows.py`, `xccy_basis.py`, `gpif_flows.py`, `trade_balance_japan.py`, `cpi_japan.py`, `fxy_options.py`) got only a grep-level pass or partial read, not a full static trace to a verdict — marked CANNOT-JUDGE above rather than guessed. `rate_differential.py` (SAM-41, newest script, built 2026-08-27) is the highest-priority gap: it is both the least fleet-reviewed and directly feeds a named prediction bar.
- Could not execute the live boot sequence (network + TSV writes forbidden by the execution gate), so no CURRENT-STATE verdict on what actually prints today for the CANNOT-JUDGE scripts — this audit is static-trace only for everything except `--tools`.
- Did not check whether `docket/CATALYSTS.tsv` and `docket/CALENDAR.md` (the two "must not diverge" twins per CLAUDE.md :140) are actually in sync — out of scope for this leg.
- Did not check downstream consumption (leg ㉒ territory): what a SILENT/SUBSTITUTED value here actually feeds into (cross-agent escalation, STATUS write-back) — flagged per-finding above where visible, not chased further.
