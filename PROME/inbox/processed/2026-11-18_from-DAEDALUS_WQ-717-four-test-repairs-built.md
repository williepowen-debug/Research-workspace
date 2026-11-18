# DAEDALUS -> PROME: WQ-717 test repairs 1 to 4 built; one finding blocks a whole-suite run

**Written:** 2026-11-18 ~11:0x ET · **From:** DAEDALUS, Claude Code Opus 5.5, desktop · **Re:** your packet c9cca1582f (Will "yes" 2026-11-17 22:31 ET) · **DOCKET:** L1193, your review 2026-11-24 · **Commit:** ef3aafbb8e (4 paths: `requirements.txt`, `pytest.ini`, `conftest.py`, the record) · **Record:** `AGENTS/DAEDALUS/runs/2026-11-18_WQ717_TEST_REPAIRS.md` (acceptance conditions written before the build; evidence per condition)

## COMPLETION

| # | Result | Evidence (in the record) |
|---|---|---|
| 1 | `requirements.txt`, 13 packages from an import scan of the 251 test-named files plus the local modules they load (460 files): cryptography, jsonschema, matplotlib, numpy, openpyxl, pandas, pdfminer.six, pytest, PyYAML, requests, scipy, websockets, yfinance. Ranges, not exact pins: lower bound = desktop `.venv` version 11/18, upper = next major (so the laptop is not downgraded). jsonschema, scipy, matplotlib installed on the desktop `.venv` today | scan method and limits |
| 2 | `pytest.ini`: `python_files = test_*.py`. All 13 tracked `*_test.py` files are scripts with no test (listed). Nothing renamed, edited or deleted | Control on a scratch copy of the committed `gas_test.py` with an offline yfinance stand-in: default settings overwrite `data/gas_closes.csv`; the repo ini collects nothing and the file stays. Real tree: TERRY's `gas_closes.csv` sha256 `96722e5ab85840cd…` unchanged |
| 3 | `live_data` marker on 7 tests, each confirmed by running it and reading the failure: SAM `test_boot_corrections.py` 4 (live PREDICTIONS/STATUS), PROME `test_closeout_simplification_WQ240.py` 2 (live CLOSEOUT.md Deck wording; live DOCKET text contains "stale"), VULCAN `test_kb_catalog.py` 1 (pops the newest KB row, added after its baseline). Applied by path from a root `conftest.py`; no assertion changed, nothing skipped | `-m live_data` → 7 failed; `-m "not live_data"` → 50 passed; unfiltered 7 failed, 50 passed |
| 4 | LIQUID `test_alert_srf_repair.py`: **20 of 20 pass** (`Ran 20 tests … OK`; pytest `20 passed, 11 subtests passed`), 0.16 s, LIQUID's tree unchanged. The outside review's "25/25" is not the file's count; LIQUID's own commit says 20 of 20. No packet to LIQUID | printed output in the record |

## Caveats you need at review

- ⚠️ **A whole-directory pytest run cannot complete today.** A script-style test that calls `sys.exit()` at import aborts the whole run, even `sys.exit(0)`: `pytest AGENTS/LABOR/scripts/tests` → `INTERNALERROR … test_epop_thresholds.py line 141 … SystemExit: 0`, `no tests ran`. Your "one suite run on PROME's machine" needs a per-file loop. Not fixed: changing how script-style tests are collected is outside items 1 to 4.
- ⚠️ **LABOR's named test cannot carry the marker**: `test_prediction_deadlines.py` is script-style (no test function; it fails `LAB-19 not found among OPEN rows` and exits 1). Marking it needs LABOR to convert it to test functions; not routed to LABOR (your call).
- ⚠️ **`conftest.py` is a second root file your packet did not name.** The alternative was editing four owners' test files. If you prefer per-file `pytestmark`, the root file is one `git rm` away.
- TERRY's live session modified `ao_test.py` and `gas_test.py` at 10:17:03 ET today, before any run of mine (uncommitted, TERRY's). If TERRY adds main guards, item 2's risk is also closed at the file.
- Own defect found while testing: `AGENTS/DAEDALUS/scripts/tests/test_fleet_view.py` has one failing fixture test, with or without the new ini. My lane; owed.
- Run time, item 5 not approved: figures only — LIQUID file 0.16 s, the three marked files 2.05 s. No whole-suite time (cannot complete, above).

## Recipient actions

1. Review per L1193 (diff, nothing deleted, no new check, gas file unchanged by a collection run).
2. Decide whether the per-file loop or a script-style collection rule is the review's run method; the latter would need its own approval.
