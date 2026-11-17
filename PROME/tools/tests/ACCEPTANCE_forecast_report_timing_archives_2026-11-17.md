# Forecast scorer: timing that does not trust the call's own date, archived calls read, first-logged score shown

Written before the edit, 2026-11-17 (session prome-19, desktop). DOCKET row dated 2026-11-18, "OUTSIDE AUDIT 2026-11-16, PROME'S OWN REPAIRS", items 1 to 3 (the audit's items 3, 4 and 5 in its forward form). `reads: 3` (the ceiling: read 1 REJECT 3 blocking; read 2, fix diff only, REJECT 1 blocking; read 3, the second fix diff only, commissioned 2026-11-17 09:47 ET; § Result). No further read without Will's named authorization.

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

## Result

**Read 1** (Agent-tool helper `scorer-reader`, Opus, read-only, its own fixture repositories; ledger copied whole: `PROME/reports/2026-11-17_forecast-scorer-repair/LEDGER_read1.md`), on commit 6348385696: **REJECT, 3 blocking, 7 not blocking.** All three failed in the dangerous direction.

| Blocking finding | What PROME changed |
|---|---|
| ❌1 Open-type statuses outside the scorecard's six open prefixes (STUCK, AT-RISK, FROZEN-PENDING, NEEDS_VERIFY ...) came back UNMAPPED and were counted as decided in the git record, pulling known dates early. On the live run CARL CRL-21 was put in report 1's closed population though its owner resolved it 2026-11-06. | `is_decided`: a committed version is decided only on HIT, MISS, PARTIAL, NO-VERDICT, ANNULLED, RESOLVED-UNTYPED, or an UNMAPPED status whose token begins RESOLVED. The forward table now holds 23 calls, not 22. |
| ❌2 The git record was keyed by row ID alone, so a reused or rewritten ID merged two calls; a new call logged after its outcome under an old ID read BEFORE. Live: BRENT BRT-27 and BRT-28 (rewritten 2026-06-08), LABOR LAB-01 and LAB-02 (reused 2026-03-06). | `same_call` and `current_call`: the record restarts where the prediction text changes at its start (word-sequence similarity of the first 12 words under 0.5) together with the probability or the Date_Made date. Restarted rows are listed in the report. The live run lists exactly those four. |
| ❌3 A version whose header had no status column still supplied a probability, against this file's own missing-information rule. | A version with no status column or no confidence column is skipped whole. |

PROME's first form of the ❌2 fix (any Date_Made change, or character similarity under 0.5) was wrong in both directions and was caught by PROME's own new cases and a look at the live list before any read: it missed an unrelated rewrite, and it restarted 17 rows, among them a resolved row whose text the owner had replaced with an archive pointer (FALCON FAL-06, which then read BORN-DECIDED) and rows whose Date_Made had been corrected (SAM-04, BRK-03). The form above is the second.

**After the fix, live run 2026-11-17:** selftest 40 of 40; 651 rows, 272 scored; 23 scored calls known after 2026-11-05, all BEFORE; 4 rows listed as reused or rewritten; first-logged Brier 0.241 against 0.223 scored, gain over the hit-rate baseline +0.008 first-logged and +0.027 scored; 38 of 272 revised.

**Declared residue, 2026-11-17 (read 1's flags that are not fixed).**
- A probability put back to an earlier value after the outcome reads BEFORE and counts as not revised (CARL CRL-03, 04, 07, 08, 09, 11, 16, 21 and BROCK BRK-22; each one the reader opened is a WQ-112 first-call restoration). The tool cannot tell a sanctioned restoration from another post-outcome edit.
- One ID repeated inside a single file is counted twice (behaviour from before this repair).
- The number of rows dropped as repeats across files is printed only as notes, never as a count, and nothing is printed when it is 0 (A9 asks for the number).
- Dates are committer dates; a rebase can move one later. None of 1,024 ledger commits is affected today (the reader's count).
- Report text a reader with no coding background could misread: the standing line "scored on the latest pre-outcome probability" is not true of restored rows; nothing says a lower Brier is better; nothing says a first-logged value can itself date from after the outcome; BORN-DECIDED is not explained. **These are settled before report 2 is issued** (DOCKET row).
- The selftest has no built case for an ID in both a live and an archive file or for a row rotated into an archive; the reader ran both in a fixture and they pass.
- The fixture recipe in PROME's brief was incomplete: a fixture also needs `scripts/orch_*.py` and the tool run from inside the fixture directory.
- New with the ❌2 fix: a reused ID that keeps both the earlier call's probability and its Date_Made date is not detected; the 12-word window and the 0.5 threshold are PROME's choices, not measured.

**Read 2** (the same reader, the fix diff 6348385696..c5aec45139 only; ledger `PROME/reports/2026-11-17_forecast-scorer-repair/LEDGER_read2.md`): **REJECT, 1 blocking, 3 not blocking.** It confirmed by running that read 1's three blocking findings are fixed (11 of 272 scored rows changed class or value between the two commits, each from one of the three fixes).

| Blocking finding | What PROME changed |
|---|---|
| ❌1 The fix to read 1's first finding overcorrected: a FINAL status outside the scorecard's map that does not begin RESOLVED (LIKELY MISSED, KILLED, GRADED-MIXED, DEFECTIVE-INSTRUMENT) was now read as open. ZHAO ZHA-09, first committed 2026-07-09 already carrying its own resolved date 2026-07-04, flipped from BORN-DECIDED to BEFORE. A fix for a blocking finding opened a hole of the same class. | `is_decided` takes the version's own resolved date: an UNMAPPED status is decided when its token begins RESOLVED or that version carries a resolved date (the reader's scan of the real history: open-type statuses carry an empty date, final ones a date). The known date is now also bounded by the earliest resolved date a decided version carried, in case the live date was moved later. ZHA-09 reads BORN-DECIDED again; the live report's printed text is byte-identical to the previous run. Selftest 47 of 47. |

**Declared residue from read 2 (not fixed).**
- A reused ID whose old and new calls share a template (the first 12 words score 0.5 or higher) still reads as one call; the reader's fixture overwrote a 5-year auction call with a 7-year one. No real reuse is missed today. The reader's tighter rule (a different call when the text changes at all and Date_Made moves) restarts the same four live rows; it is NOT adopted in this episode and is the first thing to weigh at the next touch.
- A row whose text is replaced by an archive pointer and whose value is re-marked in the same commit is listed as reused and reads BORN-DECIDED (the loud direction; no real row today).
- A ledger that held its probability only in the prediction text and gained a confidence column in the deciding commit reads BORN-DECIDED, because versions without that column are skipped (the loud direction; follows this file's own rule; no real row today).
- New with this fix: REGINALD REG-02's FROZEN-PENDING with a date counts as decided (as it did before read 1); an inline-date ledger with a non-map status and any date in its outcome cell counts as decided.

**Read 3** (the same reader, the second fix diff c5aec45139..78994ce38a only; ledger `PROME/reports/2026-11-17_forecast-scorer-repair/LEDGER_read3.md`): **ACCEPT, 0 blocking, 2 not blocking.** It compared all 272 scored rows across the two commits: 4 changed, all in report 1's closed population, none moving into or out of the forward table (ZHAO ZHA-09 back to BORN-DECIDED; CREED PRED-CREED-009 from BEFORE to AFTER, which the reader checked in that row's history and calls a true catch; REGINALD REG-09 and REG-10 class unchanged, known date earlier). The live report is unchanged. Asked which commit is safer, it answered 78994ce38a. **No edit was made to the tool after this read.**

**Declared residue from read 3 (not fixed).**
- A still-open status outside the map that carries a date reads as decided (FROZEN-PENDING and NEEDS_VERIFY versions; on ledgers that keep the date inside the outcome cell, a dated progress note counts). The reader's fixture: such a row, later graded with its probability raised after the outcome, lands in report 1's closed population and is not shown as AFTER. Exposure today is zero (no scored row changes population). The reader's one-line narrowings (apply the date rule only on ledgers with a resolved-date column, or never count tokens containing PENDING, NEEDS, STUCK, HELD or RESOLVING) are NOT adopted in this episode: the read budget is spent, and a further fix would be unread.
- The carried date is the first date anywhere in a resolved-date cell, even when the cell holds a paragraph; a reference or target date there moves the known date earlier (mostly the loud direction; in the case above it hides the row). No real case found.

**Completion note, 2026-11-17 09:53 ET (PROME prome-19).**
- IMPLEMENTED: `PROME/tools/forecast_report.py` at 78994ce38a: archive ledgers of BOND, VULCAN and WATT read by pattern and counted once; timing classes from each row's git record with Date_Made never used as a bound; the first-logged Brier beside the scored one; reused or rewritten row IDs restarted and listed; a fixture-root variable for tests.
- TESTED: selftest 47 of 47; live run rc 0 (651 rows, 272 scored, 23 forward calls all BEFORE, 4 restarted rows listed, 2 LOOK rows; first-logged gain +0.008 against +0.027 scored).
- INDEPENDENTLY VERIFIED: read 3 ACCEPT with 0 blocking on the final text, after two rejections that each found real faults in the dangerous direction; the reader built four fixture repositories and its own counterexamples.
- STILL UNRESOLVED: every item in the three residue blocks above. The ones that could change what a reader concludes: a restored probability reads as not revised; a template-sharing ID reuse is not caught; a dated still-open status reads decided; the report text does not say that a lower Brier is better or that a first-logged value can itself date from after the outcome. BOND, VULCAN and WATT have not confirmed their archive layouts or counts. The report-text items are carried on the forecast report 2 row (DOCKET, 2026-12-04) and are settled before that report is issued. Report 1 is not reopened.
