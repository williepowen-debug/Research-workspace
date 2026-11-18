# WQ-717 part 1 — four test repairs (DAEDALUS build, PROME review D:L1193 2026-11-24)

**Written:** 2026-11-18 ~11:0x ET · DAEDALUS, Claude Code Opus 5.5, desktop (DESKTOP-BC6EF81) · **Authority:** Will "yes" 2026-11-17 22:31 ET (WQ-717, PROME packet c9cca1582f); Will "ok go" 2026-11-18 10:18 ET to this session's order. Item 5 (pre-push suite) and any GitHub Actions workflow NOT approved, not started.

## Acceptance conditions (written before any repository file was created)

| # | Condition | From |
|---|---|---|
| C1 | Root `requirements.txt` lists every third-party package the test files import, derived from the imports (not from the review), with versions stated or the reason not | packet item 1 |
| C2 | No `*_test.py` file is collected by a directory pytest run; no file renamed, edited or deleted; every excluded file listed | packet item 2 |
| C3 | Collecting cannot overwrite TERRY `data/gas_closes.csv`: shown by a directory collection over `AGENTS/TERRY/research/2026-11-06_coupling-test/` with the file's hash unchanged | packet item 2 + PROME review list |
| C4 | Each named live-data test confirmed by running it; confirmed ones carry a `live_data` marker; no assertion changed, no test deleted or skipped; marked tests still run and still fail when the data has moved | packet item 3 |
| C5 | LIQUID `test_alert_srf_repair.py` re-run with packages installed; counts reported as printed | packet item 4 |
| C6 | No new check, gate or rule; no charter or root `CLAUDE.md` edit; zero dollars; no desk file edited | packet Limits |

## Findings during scoping (before build)

**Imports (C1).** AST scan of the 251 tracked test-named files, following the local modules they import (by import statement and by `.py` path strings), 460 files scanned. Third-party packages found: cryptography, jsonschema, matplotlib, numpy, openpyxl, pandas, pdfminer (pdfminer.six), pytest, requests, scipy, websockets, yfinance; PyYAML reached through `MESSAGING/tests/test_msg.py` → `MESSAGING/tools/msg.py` (subprocess, not caught by the AST scan; its own `MESSAGING/requirements.txt` already names it). `newsweep_config` is a file outside the repository (`Research-Intake/`), not a package. Missing from the desktop `.venv` before this session: jsonschema, scipy, matplotlib — installed 11/18 (4.26.0, 1.18.1, 3.11.2).

**Item 4 (C5) — DONE before build.** `cd AGENTS/LIQUID/scripts && .venv/bin/python -m unittest test_alert_srf_repair -v` → `Ran 20 tests in 0.057s` `OK`; pytest → `20 passed, 11 subtests passed in 0.13s`. Wall time 0.16 s. LIQUID's tree unchanged by the run (porcelain hash compared). ⚠️ The outside review expected "25/25"; the file has 20 test functions and LIQUID's own commit 3f8693dcce says "20 of 20 OK". 20 is the printed count. No packet to LIQUID (no failure).

**Item 2 scoping.** All 13 tracked `*_test.py` files contain no test function and no TestCase: they are research or tool scripts (list in the result section). Separately, 44 `test_*.py` files have no pytest-collectable test by a grep heuristic (`def test_` / `TestCase`); most are script-style tests that run their checks at import. Not fenced (outside item 2's scope; they are tests).

**Item 3 confirmation (C4), each run alone with pytest, tree unchanged apart from a FALCON file its own live session wrote:**

| Named | File | Result | Live-data cause (confirmed) |
|---|---|---|---|
| SAM boot_corrections | `AGENTS/SAM/scripts/tests/test_boot_corrections.py` | 4 failed, 18 passed | ContextTests read live PREDICTIONS/STATUS: `'3 OPEN' not found in "PREDICTIONS: 1 OPEN from 35…"`, `KeyError: 'SAM-28'`, `STATUS missing current dated session` |
| LABOR prediction_deadlines | `AGENTS/LABOR/scripts/tests/test_prediction_deadlines.py` | script-style; `1 FAILED`; under pytest `INTERNALERROR> SystemExit: 1` | `LAB-19 not found among OPEN rows` — live ledger moved |
| PROME closeout | `PROME/tools/tests/test_closeout_simplification_WQ240.py` | 2 failed, 21 passed | (a) asserts live `PROME/CLOSEOUT.md` text "Decision Deck … PAUSED BY WILL (WQ-460)"; Deck retired since (WQ-693). (b) fixture test, but the generator renders live `PROME/DOCKET.tsv`, whose text now contains "the stale-item cut", tripping `assertNotIn("stale", …)` |
| PROME closeout (others) | `test_closeout_declarations_readonly_boot.py` 16 passed · `test_orch_closeout.py` 27 passed | pass | not marked (no live-data failure shown) |
| VULCAN | `AGENTS/VULCAN/scripts/test_kb_catalog.py` | 1 failed, 11 passed | sandbox copies the live desk; test pops the LAST company row, now KB-VULCAN-417 (added 11/10, after the migration baseline), so its removal is not a "loss" |
| VULCAN (others) | `test_boot_edgar.py` 7 passed · `test_validate_workbook.py` no tests · `tools/test_edgar_watch.py` script-style `SystemExit: 0` | — | not marked |

⚠️ **Finding beyond scope (for PROME, not built): a whole-directory pytest run cannot complete today.** A script-style test that calls `sys.exit()` at import aborts the entire run, even `sys.exit(0)`: `pytest AGENTS/LABOR/scripts/tests` → `INTERNALERROR> … test_epop_thresholds.py, line 141 … SystemExit: 0` `no tests ran`. So "one suite run on PROME's machine" needs a per-file loop (or `python -m unittest` / direct execution for the script-style files) until owners convert those files or a collection rule is ruled. The LABOR live-data test is script-style and cannot carry a pytest marker without its owner converting it.

## Result

**Files (three new root files, nothing else in the repository changed by this build):** `requirements.txt` (item 1; Will's word covers it), `pytest.ini` (item 2, the root collection config PROME's packet names as the lighter route; also registers the item-3 marker), `conftest.py` (item 3: attaches the marker by path). ⚠️ `conftest.py` is a second root file the packet did not name; it was chosen because the only alternative that attaches a marker is editing four owners' test files (SAM, PROME, VULCAN, LABOR). PROME may prefer the per-file form at review.

**Versions (C1).** Ranges, not exact pins: lower bound = the desktop `.venv` version on 11/18, upper bound = next major (MESSAGING's style), so the laptop is not downgraded by an install. pdfminer.six has a date-based version: lower bound only. pytest is listed because tests import it.

| Condition | Verdict | Evidence |
|---|---|---|
| C1 | MET | 13 packages; scan method above. Limit: imports loaded by `subprocess` or computed paths are found only by hand (PyYAML was) |
| C2 | MET | `python_files = test_*.py`; 0 tracked `*_test.py` contains a test. Excluded (13): HANS `scripts/pmi_ism_lead_test.py`; LABOR `tools/indeed_lead_test.py`; MARCO `scripts/floor_controlled_test.py`; OTTO `research/2026-10-19_L708/equity_test.py`; REGINALD `research/KRE/reports/2026-11-02_kre-stress-test-rebuilt/source/scripts/stress_test.py`; TERRY `research/2026-10-23_KRE-QQQ-report/episode_study/flip_test.py`, `research/2026-11-05_catch-up/refunding_card_test.py`, `research/2026-11-06_coupling-test/{ao,cpc,econ,gas,u30}_test.py`; VIOLET `research/2026-11-06_close/putcall_test.py`. A file named explicitly on the command line is still collected (pytest's rule) |
| C3 | MET | Real tree: `pytest --collect-only` over the coupling-test dir from root and from inside it → `no tests collected`; `gas_closes.csv` sha256 `96722e5ab85840cd…` before = after. Control on a scratch copy of the COMMITTED `gas_test.py` with an offline yfinance stand-in: empty ini → file overwritten (`,UNG,NG=F 2020-12-04,1.0…`); repo ini → `no tests collected`, file still `ORIGINAL` |
| C4 | MET (3 of 4 named desks); LABOR NOT MARKABLE | 7 tests marked. On SAM+PROME+VULCAN files: unfiltered `7 failed, 50 passed`; `-m live_data` `7 failed, 50 deselected`; `-m "not live_data"` `50 passed, 7 deselected`; `--strict-markers` accepted. No assertion changed; nothing skipped. LABOR's test is script-style (no test function, `sys.exit` at import): a pytest marker cannot attach; owner conversion needed — routed to PROME, not to LABOR directly |
| C5 | MET | 20 of 20 (above) |
| C6 | MET | no check/gate/rule added (a marker and a collection pattern only); no charter, root `CLAUDE.md` or desk file edited; $0 |

**Side observations (not built, for PROME):**
- Whole-directory pytest runs abort on script-style tests that `sys.exit()` at import (above). The one-suite review run needs a per-file loop.
- TERRY's live session modified `ao_test.py` and `gas_test.py` at 10:17:03 ET today (before any run of mine; uncommitted, TERRY's). If TERRY adds a main guard, item 2's risk is also fixed at the file; the collection rule stays harmless.
- Own defect found: `AGENTS/DAEDALUS/scripts/tests/test_fleet_view.py::FleetView::test_foreign_inbox_rename_with_arrow_subject` fails on its own temp-repo fixture, with or without the new ini (so not caused by this build); `fleet_view.py` unchanged since df9430b596 (11/09). Owed in own lane.
- Run time (item 5 is not approved, figure only): LIQUID file 0.16 s; the three marked files 2.05 s. No whole-suite time measured (cannot complete; above).
- PROME's count 251 test-named tracked files confirmed by the same `git ls-files` pattern.
