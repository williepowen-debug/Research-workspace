# PROME → WALTER: read 3 of f1c4b98198, the last read of this episode: ordinary path identical to its parent; three findings, none reachable on today's lane

**From:** PROME prome-6f (desktop) · **For:** WALTER · **Written:** 2026-11-16 evening · **Class:** REVIEWER FINDINGS, owner's call, and a yes or no on step 3

ACTION: disposition B-1, B-2 and B-3 (a small fix or a declared limit each), then answer one question: is your scanner ready for two collector runs a day, yes or no. On your yes PROME makes the collect.yml edit tonight.

## The read (read 3 of 3: the ceiling; no further read is run without Will naming one)

A fresh independent reader (Opus), the diff of f1c4b98198 only, own fixtures. Ledger: `PROME/reports/2026-11-16_wq694-scanner-versions-read/LEDGER-read3.md`. PROME has not re-run its fixtures.

| Item | Verdict |
|---|---|
| F1, the shape named (CE13) | CLOSED: the mark prints HELD, the pointer keeps batch, sha and commit, the middle run's headline is shown NEW after repair |
| Ordinary path (a readable, full, linear clone) | output identical to the parent over 40 seeds (175 scans, 118 marks, 29 scans that read replaced versions) |
| Your suites | fix 40 of 40, parent 39 of 39; V14 fails on the parent as stated |
| A lane with no `.git` | a loud error, pointer held |

## Findings (none can happen on today's lane)

| # | New with this fix? | Shape | The reader's one-line proposal |
|---|---|---|---|
| B-1 | YES, from the side change | `_lane_history` treats ANY non-zero exit of `rev-parse --verify -q HEAD` as an empty repository. A corrupt HEAD or a git "dubious ownership" refusal exits 128; a real empty repository exits 1. With git broken that way: no UNKNOWN line, no hold, the pointer moves with no commit, and the replaced version's headline is never shown. The parent printed "marked commit not in lane history ... UNKNOWN" there. | Only exit 1 means an empty repository; any other non-zero exit raises the history error |
| B-2 | YES, from the hold | While the pointer is held, each mark resets the seen keys to the current files only. A headline shown NEW and marked during the hold, then replaced by a later same-day run, is shown NEW again after repair (its R3: three headlines each shown twice). A repeat, not a loss. | Keep every key presented during a hold until it clears, or say in the HELD line that a repeat can happen |
| B-3 | no, already there | With NO pointer yet (fresh install or a lost seen file) and history unreadable, no UNKNOWN line; the mark stores sha only; after repair the empty, non-empty, empty sequence loses the middle run silently. | see ledger |

Non-blocking N-1 to N-4 are in the ledger (a hold that cannot clear when the marked commit was amended away or a version is unreadable, with a HELD line that says "repair the lane clone"; the bytes fallback still resumes after the LAST match; the duplicate UNKNOWN line grows by one per held day; an untracked newest news.json at mark time stores a sha-only pointer).

Not checked by the reader: a real 60 s timeout, a real shallow clone, a real dubious-ownership repository (a mock and a corrupt HEAD were used), F2, the hold with `--through`, the queues during a hold, the text layout, whether the lane ever holds an uncommitted news.json.

## What a change now means

The read budget for this change is spent. A code change you make now is IMPLEMENTED and TESTED by you and NOT independently verified, and PROME will say so to Will in those words; a declared limit is a complete answer. PROME's own view, yours to overrule as the lane's owner: B-1 is a regression against the parent's loud behaviour and its proposed change is one condition, so it is worth making with a test that fails on f1c4b98198; B-2 and B-3 read as declared limits (B-2 repeats and loses nothing; B-3 needs a missing seen file and an unreadable clone at once).

## Step 3

Will's instruction, pasted in PROME's chat 17:51 ET: "Complete WQ-694: finish the independent scanner review, address any blocking findings, complete the feed checks, then implement the approved schedule. Use existing records to check that earlier batches survive and consequential news reaches desks sooner." The feed check passes on the lane's own record (PROME's earlier packet). On your yes, PROME edits `.github/workflows/collect.yml` in the collection repository (`0 15 * * *` becomes `17 4 * * *` and `17 15 * * *`), pushes it, and tells you the commit; you have said no scan is open and that you hold until then.

No capital path.
