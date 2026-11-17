# Packages the fleet's test files need

Written 2026-11-17 by PROME (outside audit 2026-11-16, item 15; DOCKET row dated 2026-11-18). A list, not an installer: nothing here installs anything, and no agent creates an environment on a machine without Will's word.

**How it was built:** every tracked file named `test_*.py`, `*_test.py` or `conftest.py` (251 files on 2026-11-17) was scanned for its import lines; standard-library modules and the repository's own modules were removed. `pytest` is listed as the runner: one test file imports it, and the audit reports 78 test files failing on a fresh install for want of one package.

| Package | In the desktop `.venv` on 2026-11-17 |
|---|---|
| pytest | 9.1.1 |
| pandas | 3.0.2 |
| numpy | 2.4.4 |
| requests | 2.33.1 |
| yfinance | 1.2.0 |
| openpyxl | 3.1.5 |
| cryptography | 46.0.6 |
| scipy | MISSING |
| matplotlib | MISSING |
| websockets | 16.0 |

**Known gaps by machine:** the laptop had no `pytest` in `.venv` or in system Python on 2026-11-16 (seen by PROME). The desktop's system Python has no `pytest`; its `.venv` does.

**Limits:** an import inside a function or behind a try block is counted like any other; a package a test reaches only through a script it calls is not seen; versions are what this machine has, not a tested minimum. The 78-file figure is the auditor's and was not reproduced.
