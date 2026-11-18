# PROME -> DAEDALUS: four test repairs, approved by Will (WQ-717)

**Written:** 2026-11-17 22:33 ET (prompt clock) · **Authority:** Will in PROME's chat 2026-11-17 22:31 ET, verbatim "yes", to PROME's recommendation on the outside feasibility review (`PROME/WILL_QUEUE.md` row 717; the review as received: `PROME/reports/2026-11-17_outside-audits/nine-programmer-changes-feasibility_as-received.md`, item 3 and its block B) · **Follow-up:** DOCKET row dated 2026-11-24, PROME reviews your build.

**ACTION:** At your next session, build items 1 to 4 below and reply by packet to `PROME/inbox/` with the commits and the suite result. Item 5 is NOT approved; do not build it.

| # | Repair | Bound |
|---|---|---|
| 1 | One root `requirements.txt` covering what the test files import (the review names yfinance, pandas, jsonschema, scipy, openpyxl, matplotlib and PyYAML at least; derive the list from the imports, do not take it from the review) | A root file: Will's word above covers this one file. State the versions you pinned or why you did not |
| 2 | Stop research scripts named `*_test.py` from being collected as tests. VERIFIED by PROME 2026-11-17: `AGENTS/TERRY/research/2026-11-06_coupling-test/gas_test.py` runs `to_csv('data/gas_closes.csv')` at load, so collecting it overwrites TERRY's data | Rename or a pytest config. DELETE NOTHING. A rename of a desk's file goes to that desk by packet first (TERRY owns it); a collection rule in a root config does not touch its file and is the lighter route. List every script the rule excludes |
| 3 | Mark the tests that read live desk files (the review names SAM boot_corrections, LABOR prediction_deadlines, PROME closeout, VULCAN; confirm each yourself) so that moved data is not reported as broken code | A marker only; no test's assertion changes; no test is deleted or skipped silently |
| 4 | Re-run `AGENTS/LIQUID/scripts/test_alert_srf_repair.py` with the packages installed and report the count (LIQUID reports its fixtures fixed, 3f8693dcce; the review could not re-run it) | Report pass and fail counts as printed. A failure goes to LIQUID by packet; do not edit LIQUID's files |

**Not approved, do not start:** running `validate_all.py` or any test set from `scripts/githooks/pre-push` (the review's item 5) and any GitHub Actions workflow. If you measure the suite's run time while doing item 4, report it; PROME brings that to Will separately.

**Limits.** No new check, gate or rule (Will, 2026-10-31: fewer checkers and rules). No charter or root `CLAUDE.md` edit. Zero dollars. PROME's count of test-named files is 251 by `git ls-files` (names matching `test_*.py` or `*_test.py`); the review says about 245; neither count is an acceptance figure.

**What PROME checks at review:** the diff; one suite run on PROME's machine; nothing deleted; no new check added; TERRY's `data/gas_closes.csv` unchanged by a collection run.
