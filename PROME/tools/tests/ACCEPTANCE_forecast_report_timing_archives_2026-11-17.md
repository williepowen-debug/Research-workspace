# Forecast scorer: timing that does not trust the call's own date, archived calls read, first-logged score shown

Written before the edit, 2026-11-17 (session prome-19, desktop). DOCKET row dated 2026-11-18, "OUTSIDE AUDIT 2026-11-16, PROME'S OWN REPAIRS", items 1 to 3 (the audit's items 3, 4 and 5 in its forward form). `reads: 1` (read 1 commissioned 2026-11-17 on commit 6348385696; result under § Result when it returns).

## The defects, in their own terms

Checked at the code on 2026-11-17 before writing this.

- **D1, timing.** The only timing check is the one-off `PROME/reports/2026-11-05_forecast-timing/timing_check.py`. Its `dates_in(s, made)` keeps an outcome date only when it is on or after the row's own `Date_Made` cell. `Date_Made` is typed by the desk. A call logged after its outcome carries a `Date_Made` later than the outcome, so the outcome date is discarded and the row cannot be classed AFTER. The audit's claim is CONFIRMED. The monthly tool `PROME/tools/forecast_report.py` has no timing check at all, so report 2 would carry none.
- **D2, archives.** The tool reads DAEDALUS's registry plus four named extra ledgers. Resolved calls that a desk rotated into an archive file leave the score. Not registered and not read today: BOND's four `thesis/archive/PREDICTIONS_resolved_*.tsv` (29 rows; the audit's item), VULCAN's three `archive/PREDICTIONS_RESOLVED_*.tsv` (19 rows) and WATT's `workbook/PREDICTIONS_ARCHIVE.tsv` (12 rows). The audit named BOND only; the class is three desks. BROCK's archive is registered and already read.
- **D3, first-logged score.** The report scores each call at its latest pre-outcome probability and shows nothing at the probability first logged.

Scope: `PROME/tools/forecast_report.py` and its selftest. Report 1 (`PROME/reports/2026-11-05_forecast-report-1.md`) and its timing folder are not edited or re-run (Will 2026-11-05). DAEDALUS's registry and scorecard are not edited. No desk ledger is edited.

## Acceptance

Terms. A row's **git record** is every committed version of every prediction ledger of its desk (live and archive) that contains the row's ID, oldest first, each with the commit's Eastern date, the probability the tool reads from that version, and whether that version's status is decided. **Value date** is the first date the probability the report scores with appears in that record. **Known date** is the earlier of the owner's resolved date (the registry's date rule for that ledger) and the first date the row is decided in git.

- A1. A scored row whose earliest git record is already decided is classed **BORN-DECIDED**, whatever its `Date_Made` cell says. This is the audit's case: no record from before the outcome.
- A2. A scored row whose value date is later than its known date is classed **AFTER**, including when `Date_Made` is later than the outcome. `Date_Made` is never used as a bound and never used as evidence of timing.
- A3. Value date equal to the known date is **SAME-DAY**, reported on its own line and never counted as before.
- A4. Value date earlier than the known date, first record not decided: **BEFORE**.
- A5. No committed version holds the row, or none holds the scored probability: **NO-GIT-RECORD**. No resolved date and never decided in git: **NO-KNOWN-DATE**. Both are counted and listed; neither is counted as before.
- A6. A BEFORE row whose outcome cell names a full date earlier than its value date is also listed under **LOOK**, with that date. It is a prompt to read the row, not a verdict: an outcome cell may cite an older reference date. This is the only place free-text dates are used, and no lower bound is applied to them.
- A7. Forward only. The timing table covers rows whose known date is after 2026-11-05, plus rows with no known date. Rows known on or before 2026-11-05 are counted in one line as report 1's closed population and are not classed.
- A8. The report shows, on the same rows, the fleet Brier at the scored probability and at the **first-logged** probability: the probability in the row's earliest git record that carries one, or the oldest `(was X%)` mark in that same cell when the cell already carries one. Rows with no first-logged value are counted and left out of both figures of that pair. The existing headline Brier is unchanged in definition.
- A9. Archive rows of BOND, VULCAN and WATT are read. A row ID present in more than one ledger file of one desk is counted once, the live ledger's row winning; the number dropped is printed. Files read through the archive patterns are named in the report.
- A10. Prediction-named `.tsv` files under `AGENTS/` that the tool does not read are counted in one line with their paths, so a new archive that no pattern matches is visible.
- A11. With history skipped (`--no-history`) the report says the timing table and the first-logged pair were skipped; it never prints an empty table that reads as "no flags".
- A12. Unchanged: probability parsing, the bucket map, the calibration table, desk counts with no desk score, exit code 0 on a completed read, no ledger written.

## Neighbours

- Ordinary: A4, A12.
- Overlap: A9 (one ID in a live and an archive file); a row rotated from the live ledger into an archive keeps its earliest record from the live file (the git record is the union across the desk's files); a row that is both born decided and later than its resolved date is BORN-DECIDED, one class per row.
- Wrong owner: two desks may use the same ID; rows are keyed by desk and ID, and a git record never crosses desks.
- Missing information: A5, A11; a version whose header lacks the status or confidence column contributes no probability and no decided mark for that version.
- Concurrent activity: a row present in the working tree and not yet committed has no git record and is NO-GIT-RECORD, never AFTER; the tool reads history through `git` only and writes nothing but its `--write` and `--sample-out` targets.

## Declared limits (known before the edit)

- An outcome that happened before the owner recorded it, with no full date in the outcome cell, is invisible: the row reads BEFORE. A6 narrows this and does not close it.
- A commit date is when the text entered this repository, not when the desk formed the view. A desk that held a call in another file first reads later than it was; the tool does not search other files.
- The first-logged probability is first-logged in a prediction ledger. A call stated earlier in a STATUS file at another probability is not seen.
- BOND, VULCAN and WATT have not confirmed their archive layouts or counts. BOND holds the audit packet; VULCAN is told in its 11/17 brief and WATT by packet.

Required result: selftest extended with A1 to A6, A8 and the overlap case on built records (no repository needed); a live run on the repository; one independent reader, Opus, devising at least one counterexample of its own, before the repair is called fixed.

## Found while building (2026-11-17, before any independent read)

- **The history reader returned one commit per ledger.** `git log --follow --reverse` gives the creation commit alone (on this machine today, 1 commit of 49 for BROCK's ledger), so every row read NO-GIT-RECORD or was dated to the ledger's first commit. Fixed by reading newest first and reversing in the tool. The closed one-off `timing_check.py` makes the same call; it is not edited or re-run, and what that means for report 1's labels goes to Will as a caveat, not as a reopening.
- **Live run at the implementing commit (6348385696), 2026-11-17:** 651 rows (596 before the repair), 272 scored (244 before); 55 archive rows read from 8 files, none double counted; 22 scored calls known after 2026-11-05, all BEFORE, 2 listed under LOOK (both cite older reference dates); first-logged Brier 0.241 against 0.223 scored on the same 272 calls, hit-rate baseline 0.249; 40 of 272 revised between first logging and scoring. Run time about 16 seconds over 44 ledger files and about 1,200 committed versions.
- **Added for testing:** the environment variable `FORECAST_REPORT_ROOT` points the tool at a fixture repository. Unset, behaviour is unchanged (output compared byte for byte).
