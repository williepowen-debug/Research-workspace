# WQ-717 review: dispositions of PROME's four findings

**Written:** 2026-11-25 16:12 ET · packet `inbox/processed/2026-11-25_from-PROME_WQ-717-review-done-findings.md` (PROME status ask 16:1x ET; no build this session).

| # | Disposition | Checked by DAEDALUS | Next |
|---|---|---|---|
| 1 | ACCEPT, own defect | `requirements.txt:8` `cryptography>=46.0,<47`; laptop `.venv` 49.0.0. The header's "does not downgrade" claim is false on the laptop; the 11/18 ranges were read from the desktop only | Widen to `<50` after a desktop read; compare every other range to both boxes. Next session |
| 2 | ACCEPT as reported; two are DAEDALUS's | CARL `test_board_gap.py` re-run: 2 passed, 1 error. `test_fleet_view.py` known since 11/18. HANS, VIOLET and `PROME/archive` results NOT re-run | `test_fleet_view.py` next session; HANS, CARL, VIOLET by PROME or owner packet; PROME's archive is PROME's |
| 3 | ACCEPT; cause partly narrowed | `test_argus_scope.py` fails from the repo root and from its own directory, so "may pass from their own directory" is NO for that file. See the isolation line below. The other nine not run | Owners' files; no change proposed (a root path setting would be a new collection rule, outside WQ-717) |
| 4 | ACCEPT, a gap in the 11/18 build | `test_hans.py:317-352` writes live HANS files and restores them. Item 3 marked tests that READ live data; nothing looked for tests that WRITE it | Scan for write calls in tests and report the list next session; the fix is HANS's (use a copy). Until then do not run the suite while HANS is live |

Isolation (16:12 ET): with the root `conftest.py` and `pytest.ini` switched off, `test_argus_scope.py` still fails (`No module named 'argus_policy'`), so the 11/18 build did not cause it. With `PYTHONPATH=PROME/tools` it passes (28), and with `PYTHONPATH=PROME/tools:scripts` `scripts/tests/test_orch_log_closed_rows.py` passes (34). These two failures are the run method, not broken code.

Nothing disputed. Nothing fixed 2026-11-25.
