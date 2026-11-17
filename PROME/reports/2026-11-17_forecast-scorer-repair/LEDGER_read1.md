REJECT — 3 blocking findings (❌), 7 non-blocking (⚠️)

# Independent read 1: forecast scorer repair (commit 6348385696)

Reader: independent, read-only, Opus. Date 2026-11-17 (ET). Subject: PROME/tools/forecast_report.py at commit 6348385696, against PROME/tools/tests/ACCEPTANCE_forecast_report_timing_archives_2026-11-17.md. I did not write the tool. timing_check.py was not run or judged.

Fixtures (temp, outside the repository):
- fx1 = /tmp/tmp.wkBPgLppXH/fx1, built by /tmp/claude-1000/-home-willi-Research-workspace-PROME/479e9a81-91b7-4151-8358-d0090564c4ce/scratchpad/build_fx.py (13 commits, 2026-10-20 to 2026-11-14 UTC; desks AEOLUS, BOND live and archive, BRENT, WATT).
- fx2 = /tmp/tmp.JhnEBNjNC8/fx2 (3 commits, one row ID reused for a new call).
- Per-row dump: scratchpad/dump.py (imports the tool and prints timing() for every row).

## Blocking findings

### ❌ 1. Open-type statuses are read as "decided" in the git record, which moves known dates too early and pushes a forward row out of the table
- **Claim:** acceptance, Terms: known date uses "the first date the row is decided in git"; A7: rows known after 2026-11-05 are classed.
- **Exact artifact:** forecast_report.py line 260: `b = classify(...)[0]`, then `b is not None` is "decided" (line 261). scorecard.bucket (AGENTS/DAEDALUS/scripts/scorecard.py lines 96 to 107) returns "UNMAPPED", not None, for any status outside its six open prefixes (OPEN, ACTIVE, PENDING, MONITORING, ARMED, WATCH). So STUCK, AT-RISK, FROZEN-PENDING, NEEDS_VERIFY, RESOLVING, HELD, STALE and UNQUANTIFIED all count as decided.
- **Verification command:** scratchpad/probe.py and probe2.py on the real repository (each version's status text and bucket; timing() rerun with UNMAPPED treated as open). Fixture fx1 row A-3 (OPEN 2026-11-01, STUCK 2026-11-03, HIT 2026-11-10 with owner date 2026-11-10), then `FORECAST_REPORT_ROOT=fx1 python3 PROME/tools/forecast_report.py` run from inside fx1.
- **Observed result:** 9 scored rows have a version with an UNMAPPED status. The live report is changed in one place. CARL CRL-21's owner date is 2026-11-06, after the cut. Its STUCK commit on 2026-10-26 makes its known date 2026-10-26, so it is counted in "250 scored calls known on or before 2026-11-05 … report 1's closed population". It should be in the forward table, which would then hold 23 rows, not 22. Inside the closed population, with UNMAPPED treated as open, the class changes: RED-19 goes from SAME-DAY to BEFORE (AT-RISK 2026-05-21), ZHAO ZHA-08 from BORN-DECIDED to BEFORE (UNQUANTIFIED 2026-03-08), and ZHAO ZHA-09 from BORN-DECIDED to BEFORE (LIKELY MISSED 2026-07-09, arguably a terminal status). In fx1, A-3 is reported as closed population ("1 scored calls known on or before 2026-11-05") although the owner resolved it on 2026-11-10.
- **Proposed change:** in the git record, count a version as decided only when its bucket is HIT, MISS, PARTIAL, NO-VERDICT, ANNULLED or RESOLVED-UNTYPED, or when it is UNMAPPED and the token starts with RESOLVED. Count other UNMAPPED versions as not decided, and print the number of such rows. Add a selftest case for a STUCK version.

### ❌ 2. The git record is keyed by row ID alone, so a reused or rewritten ID merges two different calls, and a call logged after its outcome reads BEFORE
- **Claim:** A1, A2 and A4 (timing from the row's git record); A8 (first-logged probability).
- **Exact artifact:** forecast_report.py lines 266 to 277 (record = every version that holds the ID) and line 296 (value date = first version with an equal probability).
- **Verification command:** in fixture fx2, R-1 is logged 2026-11-01 "OLD call: CPI above 3" at 60% OPEN and deleted 2026-11-03. On 2026-11-12, "NEW call: payrolls below 100k" is logged under the same ID at 60%, already HIT, with Date_Resolved 2026-11-10. Then the tool and dump.py are run. For the real repository, scratchpad/probe4.py compares each scored row's first-version Prediction text and Date_Made with the current ones, and `git log -S` finds the rewrite commits.
- **Observed result:** in fx2 the new call is classed BEFORE (value date 2026-11-01, known 2026-11-10). BEFORE rows are "not listed", and LOOK does not fire, so a call logged two days after its outcome is invisible. The correct class is BORN-DECIDED. In the real repository the IDs have been reused or rewritten. BRENT BRT-27 and BRT-28 were rewritten from event calls to price-consequence calls in commit bb0b1f907a on 2026-06-08 (subject "scope-narrow — event-shaped → price-consequence"). LABOR LAB-01 was "Shadow payroll gap closes" in 91c301279f (2026-03-04) and is now "Temp YoY stays <-6%", first added in cc0d0ab9e0 (2026-03-06). LAB-02 also changed text. Their first-logged values come from the earlier call: BRT-28 p0 0.45, where the new call's first value was 0.70; LAB-01 p0 0.60, where it was 0.85; LAB-02 p0 0.70. All four rows are in the closed population, so the timing table is not affected today. The first-logged Brier (all history) is wrong by about 0.001 to 0.002 (my estimate from LAB-01 and BRT-28 alone).
- **Proposed change:** start a row's record again when the Prediction text changes beyond a threshold, or when Date_Made changes. Date_Made is used here only to tell calls apart, not as timing evidence. Alternatively, list such rows in their own line (ID REUSED OR CALL TEXT REWRITTEN, read the row) and leave them out of BEFORE. Add the fx2 case to the selftest.

### ❌ 3. A version whose header has no status column still supplies a probability, against the acceptance's own neighbour rule
- **Claim:** acceptance, Neighbours, Missing information: "a version whose header lacks the status or confidence column contributes no probability and no decided mark for that version."
- **Exact artifact:** forecast_report.py lines 252 and 260 to 261. When ist is None the version is marked not decided, but `prob(g(icf), …)` is still recorded.
- **Verification command:** in fixture fx1, BRENT BR-1 has header ID/Prediction/Confidence/Verdict/Outcome on 2026-11-10 with the row already HIT at 60%. On 2026-11-11 the header is renamed to Status, still HIT at 60%, with no resolved-date column. Then dump.py is run. On the real repository, scratchpad/probe3.py counts scored rows that have a no-status-column version carrying a probability.
- **Observed result:** the tool returns BR-1 BEFORE (value date 2026-11-10, known 2026-11-11). Under the acceptance's rule the 2026-11-10 version contributes nothing, so the class is SAME-DAY. The row was in fact decided in its first record. Both errors point the dangerous way. On the real repository, 0 scored rows are affected today (probe3, 2026-11-17).
- **Proposed change:** when ist is None, record probability None as well as not decided (and do the same when icf is None and there is no P(TRUE) fallback, if the rule is meant for both). Add a selftest case.

## Non-blocking findings

### ⚠️ 4. A probability restored after the outcome reads BEFORE, and the "revised" count misses it
- **Claim:** report text: "Value date is the first commit date carrying the probability scored"; "N of the M were revised between first logging and scoring".
- **Exact artifact:** line 296 (first match, not the run in force at the outcome) and line 408 (compares the first and last values only).
- **Verification command:** fx1 row A-5 (60%, then 40%, decided HIT at 40% on 2026-11-10, then put back to 60% on 2026-11-12). probe.py lists the real rows whose scored value disappears and then comes back.
- **Observed result:** A-5 is classed BEFORE and counted as not revised. In the real repository the same shape appears in CARL CRL-03, 04, 07, 08, 09, 11, 16 and 21 and BROCK BRK-22. Every one I read is a sanctioned WQ-112(ii) first-call restoration. Example: CRL-07's cell says "re-marked 2026-09-24 … Scoring mark restored to first-call 80%", AGENTS/CARL/thesis/PREDICTIONS.tsv, read 2026-11-17. For these, BEFORE is a fair label. But the tool cannot tell a sanctioned restoration from a post-outcome edit back to a better old number, and CRL-07 (80, 85, 40, then 80) counts as "not revised".
- **Proposed change:** also compute the start of the last unbroken run of the scored value. When it falls after the known date, list the row under LOOK as RESTORED. Count "revised" as any change in the record, not first against last.

### ⚠️ 5. One ID repeated inside one file is counted twice
- **Exact artifact:** line 211, which only drops a repeat that comes from a different path.
- **Observed result:** in fx1, A-4 written twice in the AEOLUS file is scored twice and listed twice ("AEOLUS A-4, AEOLUS A-4" under BORN-DECIDED). probe3.py found 0 same-desk repeated IDs in the real read (2026-11-17). A9 covers repeats across files only.
- **Proposed change:** count each (desk, ID) once, and print the repeat.

### ⚠️ 6. A9's "the number dropped is printed" is met only as per-row notes
- **Exact artifact:** lines 212 and 354 to 355.
- **Observed result:** fx1 prints "…B-1 already read from AGENTS/BOND/thesis/PREDICTIONS.tsv, counted once" mixed in with the "missing file" notes. No count is printed, and when nothing is dropped (the live run, 2026-11-17) nothing is printed at all.
- **Proposed change:** add one line, "Repeated IDs dropped: N", printed even when N is 0.

### ⚠️ 7. Committer date, not author date
- **Exact artifact:** line 231 (`%ct`).
- **Observed result:** in fx1, A-8's decided commit was authored 2026-11-10 22:30 ET and committed 2026-11-11 (a rebase). The tool reads BEFORE; by author date the row is SAME-DAY. On the real repository, `TZ=America/New_York git log --date=format-local` over the ledger paths found 0 of 1024 ledger commits whose author day and committer day differ (2026-11-17). Risk is low today.
- **Proposed change:** take the earlier of the author and committer dates for decided versions and the later of the two for value versions. Or say in the declared limits that a rebase moves dates later.

### ⚠️ 8. The report text can mislead a reader with no coding background
- (a) Line 369 still says the score uses "the latest pre-outcome probability (WQ-112)". The tool does not check that the value is pre-outcome, and for WQ-112(ii) restorations it scores the first call, not the latest pre-outcome mark (CRL-07 scores 80%; its last mark before the outcome was 40%). This is old text, but it now sits beside a timing table that exists because that assumption can fail.
- (b) The new first-logged paragraph never says that a lower Brier is better, or that a positive "gain" is good.
- (c) The first-logged pair covers all history, including BORN-DECIDED and AFTER rows, so a "first-logged" value can itself be post-outcome. The text says "all history" but not this consequence.
- (d) The BORN-DECIDED label does not say what it means for the reader: there is no record that the call existed before its outcome.
- (e) "250 … closed population" reads as "known before the cut by the owner's date", but finding 1 shows that a stuck-status commit can put a row there.
- The class labels SAME-DAY ("order not shown"), NO-GIT-RECORD and NO-KNOWN-DATE are plain and accurate.
- **Proposed change:** fix (a) to describe the rule the desks follow. Add a short gloss: "lower is better; gain above 0 means better than always guessing the hit rate". Give BORN-DECIDED a one-line meaning.

### ⚠️ 9. The acceptance's required selftest is incomplete
- **Claim:** "Required result: selftest extended with A1 to A6, A8 and the overlap case on built records."
- **Observed result:** the selftest has A1 to A6 and A8, plus "born decided beats AFTER". It has no built-record case for A9's repeated ID across a live and an archive file, and none for a row rotated from the live ledger into an archive (the union across files). Both are new code. I tested both in fx1 and both pass: B-1 live row wins, and B-2 reads BEFORE with value date 2026-11-06 from the live file. The printed count "28" is a sum written into the code, not a count of checks run.

### ⚠️ 10. Fixture harness: FORECAST_REPORT_ROOT is not enough by itself
- **Observed result:** scorecard.py (line 43) runs `git rev-parse` in the current directory and imports scripts/orch_log.py, which imports orch_time and orch_closeout. A fixture that holds only the two files the brief names fails with ModuleNotFoundError. It needs scripts/orch_*.py, and it must be run with the current directory inside the fixture. orch_closeout then resolves from the real PROME/tools through the tool's own directory. The tool's docstring could say so.

## Acceptance conditions: result and method

| Condition | Result | How |
|---|---|---|
| A1 born decided | PASS on clean records; FAIL when the first version has an open-type status not in the bucket list (finding 1) or no status column (finding 3) | ran: fx1 B-3, WATT X-9, A-4; selftest |
| A2 AFTER, Date_Made unused | PASS (Date_Made is not an input to timing(), lines 280 to 313) | read; ran: fx1 A-7 AFTER |
| A3 SAME-DAY | PASS, including a late-night UTC commit read as the Eastern day | ran: fx1 A-1 (2026-11-13 03:00 UTC, read as 2026-11-12) |
| A4 BEFORE | PASS on clean records; FAIL for a reused ID (finding 2) | ran: fx1 X-9, B-2; fx2 |
| A5 NO-GIT-RECORD / NO-KNOWN-DATE | PASS in the selftest; working-tree-only row checked by reading only | selftest; read lines 284 to 287 |
| A6 LOOK | PASS (live: BRK-11, REG-31) | ran: live; selftest |
| A7 forward only | Logic PASS; population wrong by finding 1 (CRL-21) | ran: live, fx1 A-3 |
| A8 first-logged pair | PASS by its definition; values wrong for reused IDs (finding 2); "revised" count understated (finding 4) | ran: live, fx1; selftest |
| A9 archives, live wins, drops printed | Archives read (8 files, 55 rows); live wins; count not printed (finding 6); same-file repeat not covered (finding 5) | ran: live, fx1 B-1 |
| A10 unread prediction files listed | PASS: 29 listed live; with archives turned off in a scratch copy, the 8 archive files appear in the list | ran |
| A11 --no-history says SKIPPED | PASS | ran: live with --no-history |
| A12 unchanged | PASS: the old tool (6348385696^) and a scratch copy of the new tool with archives turned off give identical output, apart from the two new lines; rc 0; no ledger written (git status after each run showed only PROME's own ORCH_LOG / ORCH_INFLIGHT edits, not from this read) | ran: diff |

Verified by running: selftest (PASS 28, rc 0); live run (rc 0, 17.5 s, 651 rows, 272 scored, 22 BEFORE, 0 in every other class, LOOK 2); --no-history; old-against-new diff; fixtures fx1 and fx2; real-history probes (probe.py to probe4.py).

Verified only by reading: Date_Made is not used in timing; a working-tree-only row is NO-GIT-RECORD; the `--follow` without `--reverse` handling.

Not tested: A5 NO-GIT-RECORD for a row present only in the uncommitted working tree (read only); renamed-ledger history through `--follow` (no rename built); a confidence cell holding two percentages (old prob() behaviour under A12, outside the repair).

Process disclosure: my first probe script wrote a 1.7 MB scratch file, rec.pkl, to the repository root (untracked, never staged) at about 09:27 ET on 2026-11-17. I moved it to the scratchpad minutes later. `git status --short` afterwards showed only PROME's own ORCH_LOG.tsv and ORCH_INFLIGHT.md edits. Nothing in the repository was edited, staged or committed apart from this ledger file.
