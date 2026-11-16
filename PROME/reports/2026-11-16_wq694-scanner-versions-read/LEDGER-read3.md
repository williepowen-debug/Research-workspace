# WQ-694 scanner fix f1c4b98198: third and last bounded read

Reader: independent subagent, 2026-11-16. Scope: `git diff f1c4b98198~1 f1c4b98198 -- AGENTS/WALTER/tools`. Fixtures under `/tmp/tmp.bHTURxKDHq` (fix and parent copies of `intake_scan.py`, `intake_cadence.py` and the test files, taken by `git show`; my cases in `mine/r3.py` and `mine/diffrun.py`). Nothing in either repository was edited, staged or committed; the real lane was read with `git status`, `git log`, `git rev-parse` and one JSON read; the scanner was never run against the real lane or the real seen file.

## Summary

1. **3 BLOCKING, 4 NON-BLOCKING.** All three BLOCKING need a precondition absent today: B-1 (git cannot read the lane repository) is NEW, made silent by the side change; B-2 (headlines shown twice as NEW after a history outage) is NEW, caused by the hold; B-3 (first mark with no pointer while history is unreadable) is pre-existing, an uncovered leg of F1.
2. **F1 CLOSED for the shape it names** (CE13 rebuilt: the middle run's headline is now presented, VERIFIED), **with two adjacent legs NOT CLOSED**: B-1 (history fails without being reported as an error) and B-3 (no prior pointer, so nothing to hold).
3. Two collector runs a day are safe on this code on the ordinary path (readable full linear clone that git can open): the fix is byte-identical in output to its parent over 40 seeded runs; the declared limits remain B2 (a persistently unreadable committed version, which now holds the pointer for good) and F2 (a side-branch merge), and to them add B-1 (a repository git refuses to read reads as empty history, silently) and B-2 (after any history outage, some headlines are shown NEW a second time).

## BLOCKING findings

### B-1. NEW: a lane repository git cannot open reads as "empty history", and the side change removed the last loud line, so replaced versions are lost with no health line
- **Claim:** `_lane_history` treats ANY non-zero exit of `git rev-parse --verify -q HEAD` as an empty repository (`({}, None)`). An empty repository exits 1; a corrupt HEAD, or git refusing the repository (the "detected dubious ownership" class, plausible after a machine or user change), exits 128. Before the fix, the marked path then failed with "marked commit ... not in lane history ... UNKNOWN". The side change (`if not hist.get(path): return [], None`) makes that lookup return nothing and no error. Result: no UNKNOWN line, the scan looks clean, the mark is NOT held (no version error), it moves the pointer and stores no commit (`version_commit` finds none), and after git works again the replaced version is never read. Failure reported as clean plus a lost headline. VERIFIED.
- **Artifact:** `AGENTS/WALTER/tools/intake_scan.py`, `_lane_history` (the `rev-parse --verify -q HEAD` branch, pre-existing) and `superseded_versions` (the new `if not hist.get(path)` line).
- **Command:** `/tmp/tmp.bHTURxKDHq/mine/r3.py`, cases R5f (every `_git` call returns rc 128 with the dubious-ownership message), R5g (real git, `.git/HEAD` overwritten with `garbage`), R5h (pointer on 11-19, two runs on 11-20 while refused). Shape for R5f/R5g: run 11-20 "A", mark (commit stored); run "MID HIT" (NEW_WATCH_HIT); run "C"; break git; scan; mark; repair; scan. Run with `PYTHONPATH` = fix and = parent. Also `git rev-parse --verify -q HEAD` in an empty repo (rc 1) and with a corrupt HEAD (rc 128).
- **Observed:** Fix, R5f and R5g: scan health has only the "rewritten by the collector after --mark ... re-scanning it whole" line, no UNKNOWN line; `MID HIT new? False`; mark prints `last_marked_batch -> data/2026-11-20/news.json`, pointer `{batch, sha 51ab8f06ae22}` with no commit; scan after repair `new=[]`, health clean, `MID HIT new? False`. Fix, R5h: health shows nothing beyond the three fixture lines (fully silent). Parent, all three: the MED line `marked commit ... not in lane history: versions replaced by a later same-day run are UNKNOWN` (loud once; the parent still moved the pointer, the N1 class). Real lane today: `rev-parse --is-shallow-repository` = false and `git log` works, so the precondition is absent (VERIFIED).
- **Proposed change:** In `_lane_history`, treat only exit 1 of `rev-parse --verify -q HEAD` as an empty repository and raise the "lane history unreadable" error on any other non-zero exit (or on stderr text), so the hold and the UNKNOWN line apply.

### B-2. NEW: after a history outage, headlines that were shown NEW and marked during the hold, then replaced by a later same-day run, are shown NEW a second time
- **Claim:** While held, the pointer stays at the old day, so every scan re-reads every later day's CURRENT file; keys reconcile to exactly those current keys. When a later same-day run replaces a file, the earlier file's headlines (already shown NEW and marked) drop out of the seen set at the next mark. After repair, the first scan reads every replaced version of every day since the held pointer (no resume cut on intermediate days) and presents those headlines as NEW again. The parent, in the same sequence, shows each once. This is the fail-safe direction (a repeat, never a loss), but it is "shown twice as new across scan cycles". VERIFIED.
- **Artifact:** `intake_scan.py`, `main` mark branch (the new `if version_errs and last_marked:` hold, with `new_seen` built only from the scan's `recs`), and `_version_plan` (`sup(p)` with no `after` for days after the pointer).
- **Command:** `r3.py` case R3: mark 11-19; break history (`extensions.partialClone`); for 11-20, 11-21, 11-22: run with "X <day>" hit, scan, mark, run with "Y <day>" hit, scan, mark; repair; scan; mark; scan. Count of NEW appearances per key.
- **Observed:** Fix: each mark prints `last_marked_batch HELD at data/2026-11-19/news.json ...`; first scan after repair `new=['news:WATCH_HIT:5399b126b77b', ...67de1712cf3d, ...f92795fb9a90]` = X 11-20, X 11-22, X 11-21; tally `{X keys: 2 each, Y keys: 1 each}`. Parent: every key 1. After the post-repair mark both are clean (no third appearance).
- **Proposed change:** While held, keep in the seen set every key presented since the held pointer (do not drop keys during a hold; reconcile only on the first mark after the hold clears), or accept the repeat and say so in the HELD line ("headlines already routed during the hold may be shown again").

### B-3. Pre-existing, uncovered leg of F1: with no pointer yet, a mark while history is unreadable is silent, stores no commit, and the B1 middle run is then lost
- **Claim:** The hold needs `last_marked`. With none (first install, or a lost seen file), `_version_plan` returns `[saved]` with no errors, so the scan prints no UNKNOWN line, the mark stores the pointer with sha only, and after repair the bytes fallback resumes after the LAST identical-bytes version: empty, non-empty, empty on one day loses the middle run with no health line. Same in the parent; not introduced by the fix, but F1's text ("a --mark run while the lane history could not be read ... wrote the pointer WITHOUT the commit field") still holds on this leg. VERIFIED.
- **Artifact:** `intake_scan.py`, `_version_plan` (`if not hi or not lo ...: return [saved], errs` with `errs` empty) and the `main` mark branch (`if version_errs and last_marked:`).
- **Command:** `r3.py` case R2: no seen file; run 11-20 empty; break history; scan; mark; repair; run "MID HIT"; run empty; scan.
- **Observed:** Fix and parent alike: install scan health has no UNKNOWN line; mark prints `last_marked_batch -> data/2026-11-20/news.json`, pointer `{batch, sha 763183bb59af}` with no commit; scan after repair `new=[]`, `MID HIT new? False`, no health line.
- **Proposed change:** When the mark would store a pointer and `version_commit` returns None because history is unreadable, refuse the mark (or store no pointer) and print the UNKNOWN line; the cheaper alternative is F1's own proposal (bytes fallback resumes after the FIRST match).

## NON-BLOCKING findings

### N-1. The hold is permanent whenever the version error is not a clone problem, and the printed remedy is then wrong
- **Claim:** Any version error holds the pointer, and the hold preserves the old commit, so an error that recurs (marked commit amended or rebased away, the earlier N-a shape; a committed version unreadable, the B2 shape) holds the pointer for good: loud on every scan, the catch-up range grows by a day each day, and the HELD line says "repair the lane clone, then scan and mark again", which cannot clear either case. Not lossy and not silent (the parent was loud once, then silent and lossy). VERIFIED.
- **Artifact:** `intake_scan.py`, `main` hold branch and its HELD message.
- **Command:** `r3.py` R4 (amend the marked commit, expire reflog, gc, two more days of scan and mark) and R6 (`_show` returns None for 11-20 versions; two scan/mark cycles).
- **Observed:** Fix R4: both marks `HELD at data/2026-11-20/news.json ... (marked commit 2a6a1239c9 ... not in lane history)`; batches grow `[11-20, 11-21]` then `[11-20, 11-21, 11-22]`. Fix R6: both marks `HELD at data/2026-11-19/news.json ... unreadable from lane history`. Parent R4 and R6: pointer moves, next scan clean.
- **Proposed change:** Name the exit in the HELD line by error type (clone problem: repair; marked commit gone or version unreadable: the operator step that clears it), so the declared B2 limit has a written way out.

### N-2. The bytes fallback still resumes after the LAST match; the live seen file is still sha-only, and a hold keeps it sha-only
- **Claim:** F1's proposed change (resume after the FIRST match) was not taken. A sha-only pointer on the same day as an empty, non-empty, empty sequence still loses the middle run silently, with or without a history error. The live seen file today has `last_marked_sha 24770f8d7bf1` and no `last_marked_commit`; its marked version has 198 items, so identical bytes recurring is unlikely, and the next readable mark stores a commit. VERIFIED (fixture), INFERRED (live likelihood).
- **Artifact:** `intake_scan.py`, `superseded_versions` `elif after_sha:` branch; `AGENTS/WALTER/registry/intake_seen.json` (read only).
- **Command:** `r3.py` R1b (mark 11-20 empty, strip the commit, break, mark, repair, MID HIT, empty, scan); read of the live seen file and of `data/2026-11-16/news.json` item count.
- **Observed:** Fix and parent: `MID HIT new? False`, no health line. Fix's mark while broken printed HELD and kept `{batch, sha}` with no commit. Live: 198 items.
- **Proposed change:** Adopt F1's first-match rule in the bytes fallback.

### N-3. The duplicate UNKNOWN line grows by one per held day
- **Claim:** Each later day's lookup appends the same lane-wide error string, so a hold of n days prints about n+1 identical MED lines (the earlier N-b, now growing). Cosmetic. VERIFIED.
- **Artifact:** `_version_plan` (`sup(p)` per day) and the health loop in `main`.
- **Command:** `r3.py` R3.
- **Observed:** 2, 2, 3, 3, 4, 4 identical `lane history unreadable (OSError: lane clone is shallow or partial ...)` lines across the six held scans.
- **Proposed change:** De-duplicate version errors before printing.

### N-4. A day file that exists but was never committed gives no versions and no line, and a mark on it stores sha only
- **Claim:** With the newest `news.json` untracked at mark time, the scan is clean (correct: no committed version exists to have been replaced), and the mark stores the pointer without a commit; once the lane commits it and runs twice more, the bytes fallback applies (N-2 shape). Same in the parent; the side change does not alter this case. Whether the real lane ever holds an uncommitted `news.json` was not established; `git status --porcelain` on it is empty today. VERIFIED (fixture), NOT CHECKED (lane practice).
- **Artifact:** `superseded_versions` (new early return), `version_commit`.
- **Command:** `r3.py` R5c.
- **Observed:** Fix and parent: scan clean, pointer `{batch, sha 763183bb59af}` with no commit, later `MID HIT new? False`.
- **Proposed change:** None needed beyond N-2's; note it as part of the bytes-fallback limit.

## Checks that passed

| Check | Command | Result |
|---|---|---|
| F1 / CE13 rebuilt (pointer 11-19 with commit; 11-20 empty; partial-clone flag; mark; unset; MID HIT; empty; scan) | `r3.py` R1, fix and parent | Fix: mark prints `HELD at data/2026-11-19/news.json`, pointer batch, sha and commit unchanged; scan after repair lists `data/2026-11-20/news.json@c19040824d78`, `MID HIT new? True`; next mark moves to 11-20 with a commit, next scan clean. Parent: pointer moved with no commit, `MID HIT new? False`. VERIFIED |
| Hold (a), loss side: replaced versions never shown are suppressed after repair? | `r3.py` R1, R3 | No loss: every version of every day since the held pointer is read after repair. VERIFIED |
| Hold (b), several days unreadable | `r3.py` R3 | Every scan prints the UNKNOWN MED line (duplicated, N-3); every mark prints HELD with the same pointer; batches grow one day per day; first scan after repair reads all versions (B-2 repeats). VERIFIED |
| Lane directory not a git repository | `r3.py` R5d | Fix: MED `lane history unreadable (OSError: lane is not a git clone)` and the mark HOLDS. Loud. VERIFIED |
| Author suites | `python3 -m unittest test_intake_versions test_intake_catchup` in copies | Fix 40/40 OK; parent 39/39 OK; the fix's V14 against the parent's scanner FAILS (as the commit says); the fix's catch-up suite (with `git init`) passes against the parent too. VERIFIED |
| Ordinary path identical to parent | `mine/diffrun.py` seeds 0 to 39, fixed git dates, 1 to 3 runs a day over four days, random scan and mark | 293 output lines each (175 scans, 118 marks, 29 scans with replaced versions, 0 HELD, all 118 marks stored a commit); `diff` of the two outputs empty (batches, NEW, suppressed, health, receipt, pointer, seen keys). VERIFIED |
| Lane written | workspace `git status --short` before and after; lane only read | Only pre-existing dirty paths owned by others (`delivery_log.tsv`, `ORCH_LOG.tsv`, `HEARTBEAT.md`); none mine. VERIFIED |

## Not checked

- A real 60 s git timeout and a real `--depth` shallow clone (I used the partial-clone flag and an rc-128 mock); both reach the same `err` path by code. INFERRED.
- Real "dubious ownership": simulated by a `_git` mock returning rc 128 with that message, plus a real corrupt HEAD; I did not create a repository owned by another user.
- F2 (side-branch merge): not re-tested; this diff does not touch it.
- The hold combined with `--through` naming an older batch, and the cruise and GPU queues during a hold: not run.
- Text (non-JSON) layout of the HELD line beyond the last printed line.
- Whether the collector ever leaves an uncommitted `news.json` in the lane (N-4).
