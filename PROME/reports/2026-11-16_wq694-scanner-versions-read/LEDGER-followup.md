# WQ-694 option (a): bounded follow-up read of fix commit 6d51f78978 (B1, B3, B4)

Reader: independent reviewer (Opus), 2026-11-16, about 22:44Z to 23:05Z. Scope: `git diff 6d51f78978~1 6d51f78978 -- AGENTS/WALTER/tools` only. No file in either repository was edited, staged or committed; this ledger is the only write. Fixtures were built under `mktemp -d` = /tmp/tmp.e4XEueaSJY (h.py harness, c1.py to c4.py cases, p4.py differential). My harness reuses the author's test class but clears all three per-process caches (`_HIST`, `_BYTES`, `_VER`) before every scan and every mark, so each call behaves like a fresh process. Nothing was run with `--mark` against the real lane or real state files.

## Summary (three lines)

1. **2 BLOCKING (both need a precondition absent today), 3 NON-BLOCKING.** No new way to lose a headline or show one twice on the ordinary path was found; both BLOCKING items are silent losses on paths the fix did not cover.
2. **B1: CLOSED on the commit path, NOT CLOSED on the bytes fallback** (F1: a mark taken while history reads as an error stores no commit, and the old silent loss returns). **B3: CLOSED** (loud, ordinary case unchanged). **B4: CLOSED for the named shape; a sibling remains** (F2: a side-branch version dated before the marked commit is never read).
3. Two collector runs a day are safe on this code on the ordinary path (full linear clone, and a seen file that carries `last_marked_commit`, which the live file gains at its next mark); B2 (one unreadable committed version holds the pointer for good) is the declared limit, and F1 and F2 need a history error or a merge, neither present today.

## BLOCKING findings

### F1. BLOCKING under a precondition absent today: the bytes fallback still loses the B1 middle run silently, and any mark taken during a history error drops the commit and sends the next scan back to it
- **Claim:** `last_marked_commit` is written only when `version_commit` finds a commit. If the mark process cannot read history (shallow or partial clone, git without `--diff-merges`, a git timeout), it finds none and the seen file is written WITHOUT the field. The next scan after the clone is repaired resumes by bytes, which is exactly the pre-fix B1 rule: empty run marked, non-empty run, empty run on one day loses the middle run with no health line. The scan before that mark DID print the UNKNOWN line, but the later loss is silent. The same fallback covers the live seen file today until its next mark (the author declares this window). VERIFIED.
- **Artifact:** `AGENTS/WALTER/tools/intake_scan.py`, `main` mark branch (`commit = version_commit(...)`; `if commit:` stores it, otherwise the key is absent because `state = {}`), and `superseded_versions` `elif after_sha:` branch (`vers[idx[-1] + 1:]`, resume after the LAST byte match).
- **Command:** `/tmp/tmp.e4XEueaSJY/c2.py`, case CE13: mark 11-19; run 11-20 empty; set `extensions.partialClone`; `--mark --through 11-20`; unset it; run 11-20 with "MID HIT" (NEW_WATCH_HIT); run 11-20 empty; scan. Also CE11 (a fake `git` on PATH that rejects `--diff-merges=first-parent`; the mark stores no commit either).
- **Observed:** Mark while partial: seen file = `{last_marked_batch: data/2026-11-20/news.json, last_marked_sha: 763183bb59af}`, no commit. Scan after the B1 shape: `batches=['data/2026-11-20/news.json'] new=[] health=[]`, `MID HIT new? False`. CE11's mark likewise wrote no `last_marked_commit`. Live lane (read-only call, no mark): `version_commit('data/2026-11-16/news.json', '24770f8d7bf1')` returns `fe8ca29ea89b`, so the next live mark would store a commit and close the today-window.
- **Proposed change:** In the bytes fallback, when the marked bytes occur at more than one commit, resume after the FIRST match (or print the UNKNOWN line), so an ambiguous resume point shows a version twice rather than losing it.

### F2. BLOCKING under a precondition absent today (a merge touching data/): a side-branch version dated before the marked commit is never read
- **Claim:** `git log` without `--first-parent` walks every commit in commit-date order. The resume cut `vers[idx+1:]` assumes that order is the sequence of states the clone's working tree passed through. A version made on a side branch, dated before the marked mainline commit, and merged in with the mainline file kept, sits before the cut and is never listed. `--diff-merges=first-parent` does not help because the merge did not change the file against its first parent. No health line. Not introduced by the fix (the bytes rule cuts at the same place), but it is a sibling of B4 the fix does not close. VERIFIED.
- **Artifact:** `intake_scan.py`, `_lane_history` (the `git log --reverse ... --diff-merges=first-parent` call) and `superseded_versions` (`vers = vers[idx[-1] + 1:]`).
- **Command:** `/tmp/tmp.e4XEueaSJY/c2.py`, case CE12. Main 11-20 "a" at 10:00Z; side branch 11-20 "SIDE HIT" at 11:00Z; main 11-20 "b" at 12:00Z; scan and mark (commit = "b"); `git merge -s ours side` at 13:00Z; main 11-20 "c" at 14:00Z; scan.
- **Observed:** After the merge: `batches=['data/2026-11-20/news.json'] new=[]`, health only the "rewritten" line, `SIDE HIT new? False`. Real lane: 0 merges in 230 commits; `git log` output over `data/` is byte-identical with and without `--diff-merges=first-parent` (VERIFIED, read-only `diff`).
- **Proposed change:** When `git log --merges` shows a merge touching `data/` after the marked commit, print the replaced-versions-UNKNOWN MED line for that day.

## NON-BLOCKING findings

### N-a. Resume by commit is more fragile than bytes when lane history is rewritten; the miss is loud once, then gone after the next mark
- **Claim:** If the marked commit is amended or rebased away, the scan prints "marked commit ... not in lane history ... UNKNOWN" and lists no replaced versions, where the old bytes rule would have found the identical bytes and read them. A mark then succeeds, and the next scan is clean, so the unread version is never named again (the first reader's N1 class). VERIFIED.
- **Artifact:** `intake_scan.py`, `superseded_versions`, the `if after_commit:` branch (returns an error when the commit is absent, never tries the bytes).
- **Command:** `/tmp/tmp.e4XEueaSJY/c1.py` CE2 (amend the marked commit, gc, then two runs; scan; mark; scan) against `/tmp/tmp.e4XEueaSJY/c4.py` CE2b (the same shape with the commit field removed).
- **Observed:** CE2: `batches=['data/2026-11-20/news.json'] new=[]` plus the MED UNKNOWN line; "b HIT" not shown; after the mark `health=[]`. CE2b (bytes): `batches=['data/2026-11-20/news.json@613ca451f2ad', 'data/2026-11-20/news.json']`, "b HIT" NEW.
- **Proposed change:** When the marked commit is not in history, fall back to the bytes rule (first match, per F1) and keep the MED line.

### N-b. A history error prints the same UNKNOWN line twice
- **Claim:** The marked day's lookup and the newest day's lookup each append the same lane-wide error string. Cosmetic. VERIFIED.
- **Artifact:** `intake_scan.py`, `_version_plan` (`marked_sup` error plus `sup(saved)` error), and the health loop in `main`.
- **Command:** `c1.py` CE7 (partial clone flag), `c2.py` CE11 (old git).
- **Observed:** Two identical `lane history unreadable (OSError: ...)` MED lines in each.
- **Proposed change:** De-duplicate the version-error list before printing.

### N-c. Outside the diff, pre-existing: a current news.json of `{"items": "not a list"}` crashes the plain scan in the cruise queue
- **Claim:** `cruise_capital_queue` reads the current file with `.get("items", [])` and iterates a string, raising AttributeError; the whole scan dies (loud, not clean). The pre-feature code (`ed237c5450~1`) has the same read. INFERRED for the old code (read), VERIFIED on the current code (run).
- **Artifact:** `intake_scan.py`, `cruise_capital_queue`, the `versions.append((None, json.loads(...).get("items", [])))` line; `is_cruise_capital_candidate`.
- **Command:** `c2.py` CE9 (first form).
- **Observed:** `AttributeError: 'str' object has no attribute 'get'` from `is_cruise_capital_candidate`.
- **Proposed change:** Read the current file through `_items_from_bytes` (the one readability rule) in both queues.

## Shapes that passed (no loss, no second showing, no silent unknown)

| Case | Script | Result |
|---|---|---|
| The first reader's B1 shape (mark 11-19; empty run marked; non-empty run; empty run; scan; next day) | c1.py CE1 | Middle version `@ae71cf8175a9` listed; "LOST HIT" and its NEW_ALERT count NEW. VERIFIED |
| Mark on the current file whose bytes equal an earlier replaced version (A, B, A) | c1.py CE3 | Stored commit = the third commit (not the first); after the mark nothing re-listed; later C, A lists C once. VERIFIED |
| Mark, then catch-up across two UTC days (empty marked, M, empty, then two runs on the next day) | c1.py CE4 | Batches `[11-20@M, 11-21@X, 11-21]`; M and X NEW; clean after the mark. VERIFIED |
| Upgrade transition: seen file without the commit, two runs, first mark, two more runs | c1.py CE5 | Bytes path read B; first mark stored the commit; next scan listed D only; B not shown again. VERIFIED |
| One commit changes the marked day's file and the next day's file | c1.py CE6 | Both versions listed; "late20 HIT" NEW; clean after the mark. VERIFIED |
| Pointer stops at a replaced version whose bytes recur later (X, unreadable, X, W) | c2.py CE8 | Stored commit = the first X's commit; resume lists the unreadable version and the current file. (The second mark then moves past the unreadable version: the first reader's N4, unchanged.) VERIFIED |
| Partial clone flag set | c1.py CE7 | MED UNKNOWN line. VERIFIED |
| git without `--diff-merges` (fake wrapper) | c2.py CE11 | `git log` fails, MED UNKNOWN line; not silent at that scan (but see F1 for the mark). VERIFIED. Real git here is 2.43.0; the option exists since 2.31 (INFERRED, not looked up) |
| Shallow clone | author's V12 (passes in the 13/13 run) | Not rebuilt by me; code read: `rev-parse --is-shallow-repository` prints `false` on the real lane (VERIFIED), so the ordinary case is untouched. INFERRED |
| Linear history: `--diff-merges=first-parent` changes nothing | real lane, read-only `diff` of the two `git log` outputs | Identical over 230 commits, 0 merges. VERIFIED |
| Single-version days against the pre-feature scanner (`ed237c5450~1`) | p4.py (the first reader's differential, 80 seeds, `last_marked_commit` and `updated` ignored) | 465 scans and marks compared: 2 differences, both a first-seen timestamp one second apart (the clock ticked between the two modules' runs), none in batches, receipt, NEW, suppressed, queues, health or pointer. VERIFIED |
| Author's suite | `python3 -m unittest test_intake_versions` | 13/13 OK. VERIFIED |

Workspace `git status` after all runs: only the pre-existing dirty path(s), none mine. The real lane was read with `git log`, `git rev-parse`, `git status --porcelain` and one in-process `version_commit` / `superseded_versions` call (read-only functions).

## Not checked

- I did not rebuild a `--depth` shallow clone myself (author's V12 covers it; I tested the partial-clone flag).
- A real git timeout (60 s) on the mark path: by code it lands in F1 (no commit stored). INFERRED.
- The cruise and GPU queues under the new shallow/partial error (they now report queue errors); not run.
- B2 and the first reader's N1 to N4: not re-tested beyond what CE2 and CE8 touched; unchanged by this diff.
- An unreadable (invalid JSON) current file at mark time produced `new=[]` with no UNREADABLE alert in my CE9b; this is outside the diff and I did not establish whether that is intended.
- Text (non-JSON) report layout.
