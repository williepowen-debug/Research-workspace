# WQ-694 option (a): the scanner reads replaced versions from lane history — acceptance conditions

Written BEFORE the code (PROME ask, prome-6f message 2026-11-16 17:2x ET; WQ-694 A, Will 2026-11-16 17:18 ET). Finding: `WQ694-STEP1.md` in this folder.

**Defect.** The collector names `data/<UTC date>/news.json` and writes only headlines new since its last run. A second run on the same UTC date replaces the file. Unless WALTER scanned and marked between the runs, the first run's headlines never reach a scan, the cruise queue or the GPU queue, and the collector never re-reports them. Every version stays in the lane clone's git history (2026-11-13: e1bd850 15:18Z, 1f8a9f3 21:08Z).

**Design.** A replaced version is a batch named `data/<day>/news.json@<sha12>`. Its bytes come from `git show <commit>:<path>`; these are committed objects, so they cannot change between the scan and the mark. Count keys take the same `@<sha12>` form that a rewritten marked batch already uses. The stored pointer stays a plain path plus the sha of the version read last. Lane access is read-only (`git log`, `git show`). Nothing pulls, fetches or writes the lane.

| # | Condition | How tested |
|---|---|---|
| A1 | Two runs on one UTC day with no scan between: the scan lists the replaced version first, then the current file. The replaced version's watch hits, developments and count keys come out NEW. | test V1 (git lane) |
| A2 | After A1's mark, the next scan with no new run gives 0 new count keys and does not re-read the replaced version. The pointer is the plain path with the current file's sha. | test V2 |
| A3 | Marked on run 1, then runs 2 and 3 the same day with no scan: the next scan reads run 2 (replaced) and run 3 (current, `@sha` key). After the mark, no re-alert. | test V3 |
| A4 | Catch-up across days: replaced versions of the in-between days and the newest day are read, oldest first, each before its own day's current file. | test V4 |
| A5 | History unreadable, not a git repository, or the marked version missing from history: batches are as before, plus a MED health line saying replaced versions are UNKNOWN. Nothing is skipped silently. An empty repository (no commits) reads as no history. | test V5 |
| A6 | The receipt binds each replaced version's id and sha. A changed receipt still refuses the mark. If the pointer stops at a replaced version, it is stored as (path, that sha), and the next scan resumes after it. | test V6 |
| A7 | No lane write: the lane's HEAD and `git status --porcelain` are unchanged across a scan plus mark. | test V7 |
| A8 | The cruise and GPU review queues also read replaced versions; rows keep their day; identical titles still fold. History errors are reported as queue errors. | tests V8 (cruise), V9 (GPU) |
| A9 | Existing suites pass: catch-up, cruise, GPU, boot repairs. Old fixture lanes that are not git repositories get `git init` only where a queue test asserts no errors. | run |
| A10 | Live lane, read-only: with a scratch copy of the seen file pointed at 11/13 version e1bd850, the scan lists `data/2026-11-13/news.json` (rewritten, 1f8a9f3) and no replaced version. With the pointer at 11/12, the scan lists every day 11/13 to 11/16. The real seen file is unchanged. | smoke, recorded below |

**Out of scope.** The collection repository, its schedule and file layout (step 3 is PROME's, after one bounded independent read). Other lane files (fred, edgar), which are not per-run append feeds.

## Results (walter-5a)

| # | Result |
|---|---|
| A1 to A8 | PASS: `tools/test_intake_versions.py` V1 to V9, 9/9. Against the prior scanner, with the new module attributes created so setUp runs, V1, V3, V4, V5, V6, V8 and V9 FAIL. V2 (no re-alert) and V7 (no lane write) also held before. |
| A9 | PASS: catch-up 26/26, cruise 15/15, GPU 3/3, boot repairs 15/15. The cruise and GPU fixture lanes are now `git init` with no commits, which reads as empty history. |
| A10 | Live lane, read-only, scratch seen copy. Pointer at the 11/13 e1bd850 version (6673b80564be): batches are 11/13 current (rewritten), 11/14@bbc2b5f2175e, 11/14@5e0b36a5cb21, 11/14, 11/15, 11/16. Pointer at 11/12: the same, plus 11/13@6673b80564be first. Lane HEAD and status are unchanged, and the real `registry/intake_seen.json` is byte-identical. |
| Found on the live lane | **11/14 has three committed versions** (309af00 16:11Z, 21f97e6 19:30Z, 6fd4b59 19:39Z), and 11/12 has three (6999c2d 15:58Z, f9cd0f7 21:30Z, cb07a16 21:41Z). **The GPU review queue gains 4 candidates, all from the replaced 11/12 version 217375e0a199**, that the old queue never showed (old 0 open, new 4): Steve Hou on GPU rents; Burry's GPU-depreciation bear case; "CoreWeave closes $2.6 billion GPU-backed loan"; Meta's $420B off-balance-sheet debt. They surface for 7e(g) disposition at the next scan. The cruise queue gains none. Whether the 11/12 and 11/14 replaced versions' ordinary headlines were read in the 11/12 to 11/14 sessions is not established here. |

## Response to the independent read (PROME ledger `PROME/reports/2026-11-16_wq694-scanner-versions-read/LEDGER.md`)

| Finding | Disposition | Evidence |
|---|---|---|
| B1: an empty run, then a non-empty run, then an empty run hides the middle run | **FIXED.** --mark stores `last_marked_commit` (a replaced version's own commit, or the newest commit of the path when its bytes are the marked bytes), and the scan resumes after that commit. A seen file without the field falls back to bytes (V11). The live seen file gains the field at its next mark. Until then it resumes by bytes, and 0 of 128 live versions are empty. | V10 FAILS on ed237c5450 (the middle version is not listed) and passes now |
| B2: an unreadable committed version holds the pointer for good | **DECLARED LIMIT.** The collector serializes before writing and writes atomically (`fetch_newsweep.py` L570 write order); 0 of 128 live versions are unreadable. If one ever appears, its `news:UNREADABLE:<id>` key alerts, and every mark prints the held pointer. Advancing past it, and keying counts by content, is follow-up work, not part of this diff. | ledger B2 |
| B3: a shallow or partial clone hides replaced versions | **FIXED (loud).** History reads as an error, giving the MED UNKNOWN line, when `rev-parse --is-shallow-repository` is true or `extensions.partialClone` is set. | V12 |
| B4: a version made only by a merge commit is never listed | **FIXED.** The log uses `--diff-merges=first-parent` (git 2.43). | V13 |
| N1 to N4 | Carried as follow-ups, not in this diff (the follow-up read covers the fix diff only). | ledger |

Suites: versions 13/13, catch-up 26/26, cruise 15/15, GPU 3/3, boot repairs 15/15. Live read-only scan: lane HEAD, lane status and `intake_seen.json` unchanged.

## Response to the follow-up read (`PROME/reports/2026-11-16_wq694-scanner-versions-read/LEDGER-followup.md`)

| Finding | Disposition | Evidence |
|---|---|---|
| F1: a mark taken while history is unreadable drops the commit field, and the bytes fallback reopens B1. Also read 1 N1: such a mark clears the UNKNOWN warning. | **FIXED (one door, as PROME suggested).** While the scan's replaced-version plan has any error, --mark keeps the old pointer (batch, sha, commit) and prints `last_marked_batch HELD ... UNKNOWN`. Keys still reconcile. A path with no committed version returns no versions and no error, because nothing can have been replaced. That is why the catch-up fixture lane is now `git init` with no commits. | V14 FAILS on 6d51f78978 (pointer moved, no HELD) and passes now |
| F2: a side-branch version dated before the marked commit and merged in is never listed | **DECLARED LIMIT.** The lane has 0 merges in 230 commits. The collector runs one job at a time (`concurrency: group: collect`) and commits linearly. A merge into `data/` needs a hand-made branch in the collection repository, which nobody operates. | follow-up ledger CE12 |
| N-a, N-b, N-c, CE9b | Carried, not in this diff. | ledger |

Suites: versions 14/14, catch-up 26/26, cruise 15/15, GPU 3/3, boot repairs 15/15. Live read-only scan unchanged.
