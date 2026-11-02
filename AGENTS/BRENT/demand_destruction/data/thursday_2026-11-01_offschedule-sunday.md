PREAMBLE: unshallowed=n detached=n ff=0 venv=rebuilt head=8379e8a

# BRENT — Thursday EIA Publication Fallback (OFF-SCHEDULE FIRE)

**Run timestamp:** 2026-11-01 ~21:33 ET (2026-11-02 02:33 UTC, `date -u` at run), AUTONOMOUS, PROME/scheduler-fired.

## ⚠️ TIMING ANOMALY — READ FIRST

This run fired on **Sunday evening 2026-11-01 ET**, not the registered **Thursday 14:15 ET** slot (`trig_01ALYRXtjDGbfHeubqdvyJdf`, cron `15 18 * * 4` UTC). It is not merely the known +1h DST-drift case documented in `SCHEDULED_RUNS.md` (crons not yet re-set for EST, routines firing ~1h early in local time) — the actual calendar weekday does not match Thursday at all. This is recorded as an observation of the firing itself; no root-cause determination is made here (outside this routine's scope — record + flag only, per root CLAUDE.md Critical Rule framework and this routine's own text). Flagged to PROME below.

This anomaly has **no bearing on the data-freshness conclusion**: regardless of what day it is, the question answered below is simply "has anything newer than the last recorded observation been published," and that question was checked directly against EIA primary sources.

## CORE WEEKLY OBSERVATION: NO NEW CORE OBSERVATION

Week ending **2026-10-23** remains the latest published WPSR observation and is already fully recorded (`data/eia_2026-10-28.md`, confirmed again by the two 2026-10-29 Thursday-fallback runs). This run neither duplicates nor supersedes that observation.

**Confirmation method — `eia_weekly.py` (LOCAL mode; no EIA/FRED API key present this session, `env_doctor FAIL` persists per the boot hook):**
```
Source: LOCAL (eia_2026-10-28.md)
Week ending: 2026-10-23
Released: 2026-10-28
Coverage: COMPLETE dated observations
```
Exit code 0 — no FINDINGS (missing/stale/mixed inputs).

**Cross-checked directly against EIA primary, live this run:**
| Source | Week ending returned | Key figures | vs. recorded (`eia_2026-10-28.md`) |
|---|---|---|---|
| `ir.eia.gov/wpsr/table1.csv` | 10/23/26 | Commercial crude (ex-SPR) 410.625M; SPR 282.583M | MATCH exactly |
| `ir.eia.gov/wpsr/table4.csv` | 10/23/26 | Cushing 26.970M (prior wk 27.594M) | MATCH exactly |
| `eia.gov/petroleum/supply/weekly/pdf/highlights.pdf` | 10/23/26 (PDF metadata creation 2026-10-27 16:46 ET) | Crude 410.6M, Gasoline 209.2M, Distillate 102.8M, SPR 282.6M, refinery util 93.1% (4-wk), gasoline product supplied 4-wk 8,629 kb/d vs 8,688 kb/d ya | MATCH (rounding only) |
| `eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls` (GASREGW/retail primary) | Latest row 10/26/2026, release 10/27/2026 | (price cell not machine-extracted this pull; date confirms no newer retail print) | Date MATCHES prior $4.269/gal (10/26) observation — no newer retail week |

No field was missing, stale, or mixed-week. No fill from another period was performed. No BRT-xx row was graded, resolved, or re-marked by this routine.

## SUPPORTING-FILE SWEEP (vs. last Thursday 2026-10-29 fallback)

| File | Prior state (10/29 fallback) | This run | Change? |
|---|---|---|---|
| `eia.gov/petroleum/supply/weekly/` landing page | blank-template, no release date shown | Same — fields blank; "Previous Issues" list shows 2026-10-21 as the newest entry link, which lags the known 10/28 release; template issue, not a new-data signal | No improvement |
| `highlights.pdf` | 403 (10/29 ~14:1x run) / was 200-but-undecodable Wednesday | **200, readable this run** — content confirms week 10/23, no new week | **IMPROVED access**, same underlying data |
| `ir.eia.gov/wpsr/table1.csv`, `table4.csv` | not separately logged 10/29 1415et run (GASREGW fallback used instead) | 200, both readable, week 10/23 | Consistent |
| `eia.gov/petroleum/supply/weekly/pdf/table1.csv` | — | 404 | Confirms this is not the correct primary path (ir.eia.gov/wpsr/ is); no regression, just a wrong guess this run |
| `ir.eia.gov/wpsr/table11.csv` (retail detail) | 403 | 403 | No improvement |
| GASREGW / retail workbook (`pswrgvwall.xls`) | keyless fallback stable, latest row 10/26 | latest row 10/26/2026, release 10/27/2026 | No new weekly print (next retail release expected Monday, has not occurred as of this run's clock) |
| Direct FRED path | blocked, `env_doctor FAIL` | still `env_doctor FAIL` per boot hook this session | Unchanged, long-standing, out of this routine's scope |

**No newly available supporting file is recorded this run beyond the `highlights.pdf` access-state change noted above (same data, not new data).**

## REGISTERED ALERT LINES — RE-CHECKED, NONE NEWLY CROSSED

All six EIA-sourced registered lines (Cushing <20.0M, weekly crude draw >5.0M, refinery util >95%, GASREGW >$4.00, SPR, gasoline 4-wk YoY/BRT-31) retain their 2026-10-23/10-26 vintage values exactly as carried in `TRACKER.md`'s REGISTERED ALERT LINES block as of the October 29/30/November 1 entries. None crossed. BRT-31 week-three figure (gasoline 4-wk YoY −0.6762% exact, NON-QUALIFYING) is reported only, not graded, consistent with the prediction-row fence in this routine's prompt.

## FLAG

Flag packet written to `PROME/inbox/` (see outbox note below) covering: (1) no new core observation, (2) the off-schedule Sunday-evening fire anomaly, (3) the `highlights.pdf` access-state improvement (informational, no data change).

**Record + flag only. No gate graded, no capital action, no BRT-xx row resolved by this routine.**
