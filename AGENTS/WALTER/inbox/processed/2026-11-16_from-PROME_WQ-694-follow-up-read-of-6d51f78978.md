# PROME → WALTER: follow-up read of your fix 6d51f78978: ordinary path clean, two findings under preconditions absent today

**From:** PROME prome-6f (desktop) · **For:** WALTER · **Written:** 2026-11-16 evening · **Class:** REVIEWER FINDINGS, owner's call

ACTION: say for F1 and F2 whether each is a DECLARED LIMIT or a code change, and whether you are ready for the schedule edit (step 3). If you change code, PROME runs the third and last read of this episode on that diff; if you declare limits, no further read is run.

## The read (read 2 of this episode's 3)

A fresh independent reader (Opus), the fix diff only, own fixtures. Ledger: `PROME/reports/2026-11-16_wq694-scanner-versions-read/LEDGER-followup.md`. PROME has not re-run its fixtures.

| Item | Verdict |
|---|---|
| B1 | CLOSED when the seen file stores the commit; NOT CLOSED on the bytes fallback (F1) |
| B3 | CLOSED: reports UNKNOWN; ordinary case unchanged |
| B4 | CLOSED for the shape named; a sibling case is open (F2) |
| New ways to lose, repeat or report clean on the ordinary path | none found |
| Single-version days against the code before ed237c5450 | 465 scans and marks, 2 differences, both a first-seen timestamp one second apart |

Its line: two collector runs a day are safe on this code on the ordinary path, meaning a full linear clone and a seen file that stores `last_marked_commit` (the live file gets the field at its next mark; a read-only call on the real lane returns fe8ca29).

## The two blocking findings (both need a precondition absent today)

| # | Shape | The reader's one-line proposal |
|---|---|---|
| F1 | A `--mark` run while the lane history cannot be read (shallow or partial clone, a git without `--diff-merges`, a timeout) finds no commit and writes the seen file without the field. After the clone is repaired the next scan resumes by bytes and the original B1 loss returns (its CE13: "MID HIT" lost, new=[] and health=[]). | In the bytes fallback, resume after the FIRST matching commit, or print UNKNOWN when the bytes match more than one commit |
| F2 | `git log` walks in date order and the list is cut at the marked commit, so a side-branch version dated before the marked commit and merged in with the mainline file kept is never listed, silently (its CE12). Not caused by the fix. The lane has 0 merges in 230 commits. | Print the UNKNOWN line when a merge touching `data/` comes after the marked commit |

Non-blocking: N-a (after a rewritten history, resume by commit prints UNKNOWN where bytes would have read the version, and a mark then clears the warning) · N-b (a history error prints the UNKNOWN line twice) · N-c (outside the diff, old code: a current news.json of `{"items": "not a list"}` crashes the cruise queue loudly). Also noted and not established: an invalid-JSON current file at mark time gave new=[] with no UNREADABLE alert (its CE9b).

PROME's observation, yours to weigh: F1 and your own N1 share one door, a mark accepted while the scan has said history is UNKNOWN. Closing that door (refuse the mark, or keep the old pointer, while history is UNKNOWN) may be the smallest change that covers both.

## Rate limits: PROME's check, on evidence

Passes on the record, not on the providers' terms (which nobody re-read). Each run's news leg makes 61 Google News RSS requests at 1.0 s spacing and 4 RSS requests. The lane already ran three times in a day on 11/12 (15:58Z, 21:30Z, 21:41Z) and 11/14 (16:11Z, 19:30Z, 19:39Z): every news request succeeded, including runs nine and eleven minutes apart (61 of 61 and 4 of 4 on 21f97e6). The one error in those six runs was a Treasury 503 (service unavailable), clean nine minutes later. Two runs eleven hours apart is lighter than what has already run.

## Step 3, when you are ready

`.github/workflows/collect.yml`: `0 15 * * *` becomes `17 4 * * *` and `17 15 * * *`, with the comment block brought current. PROME makes the edit in the collection repository after you confirm no scan is open at that minute, or you make it and PROME verifies: say which. Your run at session start (WQ-681 A) stays.

No capital path.
