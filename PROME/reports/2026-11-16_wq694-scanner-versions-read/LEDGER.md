# WQ-694 option (a): independent read of commit ed237c5450 (intake_scan reads replaced versions)

Reader: independent reviewer (Opus), 2026-11-16, about 22:00Z to 22:40Z. Scope: `git diff ed237c5450~1 ed237c5450` only. No file in either repository was edited, staged or committed. All fixtures were built under `mktemp -d` (/tmp/tmp.ZJbj7dsdWJ). Throwaway scripts there: harness.py, ce.py, ce2.py, ce3.py, p4.py.

## Summary (three lines)

1. **4 BLOCKING, 4 NON-BLOCKING.** One BLOCKING case (B1) can happen with today's collector and clone. The other three (B2 to B4) need a precondition that does not hold today: an unreadable committed version, a shallow clone, or a merge commit.
2. **P1 FAILS** (B1, silent loss; B2 to B4 under their preconditions). **P2 FAILS** (B1, B3 and B4 are silent). **P3 HOLDS.** **P4 HOLDS.**
3. Moving the collector to two runs a day is safe on the ordinary path: two or three runs a day, marks between any of them, catch-up across days. Every such test passed. One rare silent-loss case (B1) remains: a zero-headline run, then a non-empty run, then another zero-headline run on the same UTC day, with the mark on the first. Fix B1, or accept it by name, before the move.

## What the code actually does

For each day the scan covers, the code runs `git log --reverse --diff-filter=AM --name-only -- data` once per process in the lane clone. That gives every commit that added or modified a `data/<day>/news.json`. The bytes of each commit's version come from `git show <commit>:<path>`. Any version whose 12-hex sha1 differs from the working-tree file becomes an extra batch `<path>@<sha12>`, placed just before that day's file.

- **Marked day.** Only versions after the **last** commit whose bytes match the stored `last_marked_sha` are kept. If no commit has those bytes, a MED line says UNKNOWN.
- **Every other day in range.** Every replaced version is included.
- **Cruise and GPU queues.** Both read every replaced version of every day from their baselines.
- **The mark.** It stores the path without `@` plus the sha of the batch the pointer stopped at. Bytes are matched by content hash only; the stored pointer holds no commit id.

## Findings

### B1. BLOCKING, reachable today: a replaced version is lost silently when the marked bytes come back later the same day
- **Claim:** The resume point is the LAST commit whose bytes equal `last_marked_sha`. If a later run writes bytes identical to the marked version, every version between them is skipped. No health line appears. VERIFIED.
- **Artifact:** `AGENTS/WALTER/tools/intake_scan.py`, `superseded_versions`, line 250 (`vers[idx[-1] + 1:]`); `rewritten_marked`, line 325 (current bytes equal the marked bytes, so no re-scan). Collector: `/home/willi/Research-Intake/scripts/fetch_newsweep.py`, line 226. news.json is `{"by_class": ..., "items": ...}` with no run stamp, so every zero-headline run writes the same bytes.
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce.py`, case CE2. Steps: mark 11-19; run 11-20 with no items; mark through 11-20; run 11-20 with one NEW_WATCH_HIT ("LOST HIT") and one NEW_ALERT; run 11-20 with no items; scan; then run 11-21 and scan again.
- **Observed:** `e1==e2 True`. The scan gives `batches ['data/2026-11-20/news.json'] new []` with no version or UNKNOWN health line. The next-day scan gives `batches ['data/2026-11-21/news.json'] new []`. The watch hit and the alert count are never shown. Real lane, read-only: none of the 128 committed news.json versions is empty, and no two share a sha. The case is rare but has no guard.
- **Proposed change:** Store the marked version's commit id in the pointer and resume after that commit, not after the last commit with matching bytes.

### B2. BLOCKING under a precondition absent today: a held pointer becomes permanent, and on every later two-run day the alert-count prompt points at the wrong version
- **Claim:** A committed version that fails the readability rule holds the pointer before it forever, because a committed version can never be repaired. While the pointer is held, the newest day is an "other day", so all of its replaced versions are re-listed with no after-filter. On each later day with two runs, two things happen. First, the first run's NEW_ALERT/NEW_WATCH count comes back as NEW under `@<sha>`, which is a second showing. Second, the second run's count key is the plain path, already seen, so it is suppressed and lost. Title-keyed WATCH_HIT and DEVELOPMENT keys are not affected. VERIFIED.
- **Artifact:** `intake_scan.py`, `mark_pointer`, lines 433 to 446; `_version_plan`, lines 396 to 399 (`sup(p)` and `sup(saved)` with no after-filter); `collect_alerts`, line 565 (plain count key for the current file).
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce2.py` case CE6, and `/tmp/tmp.ZJbj7dsdWJ/ce3.py` case CE6c. In CE6c, 11-20 commits `{"items": "not a list"}` and then a good file. On each of 11-21, 11-22 and 11-23: run 1 (one NEW_ALERT), scan and mark, then run 2 (one NEW_ALERT), scan.
- **Observed:** On each day, NEW is `news:NEW_ALERT:data/<day>/news.json@<run-1 sha>` and the suppressed list holds `news:NEW_ALERT:data/<day>/news.json` (run 2's count). The stored pointer stays at `data/2026-11-19/news.json`, and the batch list grows to 8. In CE6, the suppressed record reads `2 NEW_ALERT item(s) — read data/2026-11-21/news.json`. The collector writes `json.dumps` atomically, so it does not produce an unreadable version today. The author's own test V6 builds exactly this state. The old code already lost run 2's count under a held pointer; the second showing of run 1's count is new.
- **Proposed change:** Do not let an immutable committed version hold the pointer: record it as UNREADABLE and advance past it. Also key count records by content sha rather than by the plain path.

### B3. BLOCKING under a precondition absent today: in a shallow clone, replaced versions are silently invisible
- **Claim:** In a shallow clone, every replaced version older than the shallow boundary is missing from `git log`. That day then looks like a single-version day, and no UNKNOWN line appears. VERIFIED.
- **Artifact:** `intake_scan.py`, `_lane_history`, lines 195 to 219. There is no `--is-shallow-repository` check.
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce2.py`, case CE3. Two runs on 11-20 after a mark on 11-19, then `git clone --depth 1` of the fixture lane, then a scan of that clone.
- **Observed:** The full clone gives `['data/2026-11-20/news.json@4bbe617512f5', 'data/2026-11-20/news.json']`. The shallow clone gives `['data/2026-11-20/news.json'] new []` with no version or UNKNOWN health line. The real lane is not shallow (`git rev-parse --is-shallow-repository` returns false) and is not a partial clone (no `extensions.partialClone`). A future clone made on another machine, for example the laptop, could be either.
- **Proposed change:** If the clone is shallow or partial, print the replaced-versions-UNKNOWN MED line.

### B4. BLOCKING under a precondition absent today: a version created by a merge commit is never listed
- **Claim:** `git log --name-only` lists no files for merge commits, so a news.json version that exists only in a merge result is never read once a later run replaces it. No line reports this. VERIFIED.
- **Artifact:** `intake_scan.py`, line 206. The log command has no `--diff-merges` or `-m`.
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce2.py`, case CE7. A branch and master each change 11-20; the merge is resolved with new content ("MERGED ONLY"); then one more run; then a scan.
- **Observed:** The batches are three `@` versions plus the current file. `news:WATCH_HIT:fc81243c4d50` ("MERGED ONLY", merge version sha 51fe07e872cf) is absent from NEW. The real lane has 0 merge commits (`git log --merges`, 230 commits). The collector commits linearly under `concurrency: group: collect`.
- **Proposed change:** Use `--diff-merges=first-parent` (or `-m`) in the history log, or print UNKNOWN when a merge touches `data/`.

### N1. NON-BLOCKING: a mark is accepted after the scan reported versions UNKNOWN, and after it the warning disappears
- **Claim:** Version errors appear only as health lines; they are not bound into the receipt, and the pointer is not held. A mark therefore moves past a day whose replaced versions were UNKNOWN. The next scan is clean and the lost versions are never named again. The scan itself was loud once. VERIFIED.
- **Artifact:** `intake_scan.py`, `main`, lines 937 to 938 (health only) and lines 940 to 985 (mark).
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce2.py`, case CE8. Mark at 11-20 run 1; two more runs; history squashed and pruned (the marked version is gone); scan; mark; scan.
- **Observed:** The first scan shows the MED line `marked version ef20b946ca2a ... not in lane history: ... UNKNOWN`. The mark returns 0. The scan after it shows `after mark health []`.
- **Proposed change:** Hold the pointer at, or refuse the mark for, a day whose replaced versions are UNKNOWN, or put the version errors into the receipt.

### N2. NON-BLOCKING: the same headline in two versions gives two identical NEW records in one scan
- **Claim:** A title present in a replaced version and in the current file produces the same WATCH_HIT key twice in one scan's NEW list. It does not come back across cycles. The lane's documented path to this is a news_seen.json write failure: "these headlines may repeat next run", in `fetch_newsweep.py` at line 235. VERIFIED.
- **Artifact:** `intake_scan.py`, `collect_alerts`, line 585 (one record per item) and `main` (NEW records are not deduplicated by key within one scan).
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce.py`, case CE5.
- **Observed:** `new ['news:WATCH_HIT:7116abcdd2d3', 'news:WATCH_HIT:7116abcdd2d3', ...] count of dup key 2`. After the mark: `new []`.
- **Proposed change:** Deduplicate NEW and suppressed records by key within one scan.

### N3. NON-BLOCKING, unreachable today: a pointer with no stored sha reads no replaced versions of the marked day and says nothing
- **Claim:** `marked_sup` requires `marked_sha`. A seen file in the old format (pointer but no sha) gets no replaced versions for the marked day and no UNKNOWN line. In CE4, the watch hit from run 2 is lost. This is the pre-change behaviour, unchanged. VERIFIED (fixture). Unreachable today: the live `registry/intake_seen.json` carries `last_marked_sha 24770f8d7bf1` (VERIFIED, read-only).
- **Artifact:** `intake_scan.py`, line 386.
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce3.py`, case CE4.
- **Observed:** `batches ['data/2026-11-20/news.json'] new ['news:WATCH_HIT:8dbc6058e033']`. The run-2 hit `bf1c365741a4` is absent, and the health output has no version line.
- **Proposed change:** When `last_marked_sha` is missing, print the UNKNOWN MED line for the marked day.

### N4. NON-BLOCKING: a held pointer whose path equals the current file's path is stored with the current file's sha, so the pointer moves past an unreadable version
- **Claim:** The mark tests `if ptr in receipt_shas` before the held-pointer branch. When `mark_pointer` returns the stored pointer unchanged, meaning "held", and that plain path is also today's current batch, the mark stores the current file's sha. The pointer then moves past the unreadable version, and the output does not say "held". Nothing readable is lost, because every batch was shown under the quoted receipt. However, this contradicts acceptance condition A6 ("pointer stops"), and the unreadable version is named only once. VERIFIED.
- **Artifact:** `intake_scan.py`, lines 962 to 970.
- **Command:** `/tmp/tmp.ZJbj7dsdWJ/ce2.py`, case CE6b. This is V6's end state followed by one more mark.
- **Observed:** After the repair run, the mark prints `last_marked_batch -> data/2026-11-04/news.json`, and the stored sha changes from `2fd0b68df104` (v2) to `b44a56e726a9` (the current file). The `news:UNREADABLE:...@<v3>` key is dropped at the following mark.
- **Proposed change:** Branch on "held" (ptr equals the stored pointer) before the receipt lookup, and say so in the output.

## Counterexamples that passed (P1 held in these)

| Case | Script | Result |
|---|---|---|
| Three versions in one day, scan and mark after each run | ce.py CE1 | Each run's hit and alert count are NEW once; the final scan has none. VERIFIED |
| Three versions, mark at the middle one, then run 3 plus a new day | ce.py CE1b | Run 3 and the next day are NEW; runs 1 and 2 are not repeated. VERIFIED |
| Same headline in two versions, across cycles | ce.py CE5 | No re-alert after the mark (see N2 for the duplicate within one scan). VERIFIED |
| Seen file marked on a clone that is ahead, scanned on a clone that is behind, then pulled | ce3.py CE9 | Behind: MED "not in lane history ... UNKNOWN" plus a re-scan, NEW = []. After the pull: NEW = []. No loss and no second showing in this shape. VERIFIED |
| Late run crossing UTC midnight | collector code | The collector fixes the day at run start (`fetch_newsweep.py` lines 119 and 223), and runs are serialized (`collect.yml` `concurrency: group: collect`), so a day's file is never committed after the next day's. INFERRED, not run |
| Lane clone behind the remote: who fetches | intake_scan.py docstring, lines 10 to 14 | The scanner never fetches. WALTER's boot step runs `git -C /home/willi/Research-Intake pull --ff-only`. A stale clone scans consistently and catches up after a pull (see CE9). INFERRED from the docstring; CE9 VERIFIED |
| Long history: cost and bounds | real lane | One `git log` over `data/` (230 commits) takes 0.03 s. `git show` takes about 1.6 ms each and is cached per process. A full read-only real scan took 0.14 s. The queues re-read every version since their baselines on each scan, which grows linearly and stays small. VERIFIED |

## P3: every lane command (VERIFIED)

The new code calls `subprocess` only through `_git` (line 191: `git -C <LANE> ...`, args as a list, no shell). There are three call sites, and all three are read-only:

1. `rev-parse --verify -q HEAD` (line 203)
2. `log --reverse --format=C %H --diff-filter=AM --name-only -- data` (line 206)
3. `show <commit>:<path>` (line 226)

`intake_cadence.py` has no `subprocess`. None of the three refreshes the index or creates objects. The one way `git show` could write is a lazy fetch in a partial clone, and the real lane is not a partial clone.

Real-data run (read-only mode only):

- Command: `cd /home/willi/Research-workspace && python3 AGENTS/WALTER/tools/intake_scan.py --json`, with a marker file touched just before.
- Afterwards: `find /home/willi/Research-Intake -newer marker` returned nothing (`.git` included). Lane `HEAD` and `status --porcelain` were unchanged. md5 of `registry/intake_seen.json`, `cruise_capital_review.json` and `gpu_finance_review.json` was unchanged.
- Output: batches `['data/2026-11-16/news.json']`, NEW `[]`. The GPU queue shows the 4 candidates from version `217375e0a199` (11/12, commit f9cd0f7), which matches the author's note.

## P4: single-version days (VERIFIED)

Method: a differential run of the prior scanner (`git show ed237c5450~1:...`) against the new one. Both used the same git fixture lanes with one version per day, separate seen files, 40 random seeds, and random runs, scans, marks and marks without `--through` (`/tmp/tmp.ZJbj7dsdWJ/p4.py`).

Result: 225 scans compared on batches, receipt, NEW, suppressed, both queues, queue errors and health, plus the seen file after each mark. There were **0 differences**.

Caveat: a lane that is not a git clone now gets MED lines and per-day queue errors. This is intended (A5/A9) and is not covered by this differential.

## Item 4: real-lane version counts (VERIFIED, read-only `git log`)

| Day | Committed versions |
|---|---|
| 2026-11-12 | 6999c2d 15:58Z (sha 2083ac620d04, 210 items) · f9cd0f7 21:30Z (217375e0a199, 118 items) · cb07a16 21:41Z (2626d8016c2e, 6 items) |
| 2026-11-14 | 309af00 16:11Z · 21f97e6 19:30Z · 6fd4b59 19:39Z |
| 2026-11-13 | 2 versions |
| 2026-11-15 | 1 version |
| 2026-11-16 | 1 version |

The author's claim (three versions each on 11/12 and 11/14) is confirmed.

## Author's suites (VERIFIED, run with python3 -m unittest)

- test_intake_versions: 9/9
- test_intake_catchup: 26/26
- test_cruise_capital_review: 15/15
- test_gpu_finance_review: 3/3

The workspace `git status` was identical before and after the runs.

## Not checked

- I did not reproduce the A10 smoke run (a scratch seen copy with the pointer at 11/13 e1bd850 and at 11/12).
- I did not check whether the replaced 11/12 and 11/14 versions' ordinary headlines were read in the 11/12 to 11/14 sessions. The author also leaves this open. Only the queues read days before the live pointer; the scan does not.
- A real git timeout or failure was not exercised, apart from the author's mock in V5.
- A partial (blobless) clone, where `git show` would fetch and write objects: not run. The real lane is not partial.
- The cruise queue fold across versions: covered only by the author's V8 and V9; I ran no independent case.
- The text (non-JSON) report layout was not reviewed.
- The install case (no pointer, newest batch only) does not read the newest day's replaced versions. This is by design, and I did not test it further.
