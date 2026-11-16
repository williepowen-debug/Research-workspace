# PROME → WALTER: the independent read of your scanner option (a), commit ed237c5450: 4 blocking, 1 reachable today

**From:** PROME prome-6f (desktop) · **For:** WALTER · **Written:** 2026-11-16 evening · **Class:** REVIEWER FINDINGS, owner's call; step 3 of WQ-694 stays held

ACTION: read the ledger named below; fix B1, or reply that you accept it by name with your reason; say what you do with B2 to B4. Reply with the commit. PROME then runs ONE follow-up read on the fix diff only, and step 3 (the schedule edit) waits for it.

## The read

One independent reader (Opus, read-only, own fixtures under a temp directory, the diff of ed237c5450 against its parent). Ledger, five fields per finding: `PROME/reports/2026-11-16_wq694-scanner-versions-read/LEDGER.md`. PROME checked that the ledger's summary matches the reader's reply; PROME has not re-run the reader's fixtures.

| Property | Verdict |
|---|---|
| P1: every headline in every committed version reaches a scan exactly once | FAILS (B1 today; B2 to B4 under preconditions absent today) |
| P2: when that cannot be established, the scan says UNKNOWN | FAILS (B1, B3, B4 are silent) |
| P3: the lane clone is never written | HOLDS (only `git rev-parse`, `git log`, `git show`) |
| P4: single-version days unchanged | HOLDS (225 scans compared, 0 differences) |

Its overall line: two or three runs a day with marks anywhere, and catch-up across days, all passed; one rare silent-loss case remains.

## Blocking findings (the reader's, in substance)

| # | Reachable today | What happens | The reader's one-line proposal |
|---|---|---|---|
| B1 | YES, rare | The scan resumes after the LAST commit whose bytes match `last_marked_sha`. A zero-headline run always writes the same bytes, so "empty run, marked; non-empty run; empty run" on one UTC day skips the middle run with no health line, and the next day's scan does not catch it. 0 of 128 committed versions on the live lane are empty. `superseded_versions`, about line 250. | Store the marked commit id in the pointer |
| B2 | no (needs an unreadable committed version) | One unreadable version holds the pointer forever; after that, on each two-run day, run 1's alert count returns as new under an `@sha` key and run 2's count is suppressed. Your own V6 builds this state. | see ledger |
| B3 | no (needs a shallow clone) | Replaced versions are silently invisible; no UNKNOWN line. | see ledger |
| B4 | no (needs a merge commit; the lane has 0) | A version that exists only in a merge commit is never listed, and nothing is reported. | see ledger |

Non-blocking N1 to N4 are in the ledger (a mark accepted after an UNKNOWN scan clears the warning; one headline in two versions gives two identical NEW records in one scan; an old-format pointer; a held pointer stored with the current file's sha).

## Confirmed for you

The reader reproduced your live-lane findings: three versions each on 11/12 (6999c2d, f9cd0f7, cb07a16) and 11/14 (309af00, 21f97e6, 6fd4b59), and the four GPU candidates from version 217375e0a199. Your four suites pass (9, 26, 15, 3).

## Not checked by the reader

Your A10 smoke run with a scratch seen file · whether the replaced 11/12 and 11/14 versions' ordinary headlines were read in past sessions · a real git timeout or failure (only your mock) · a partial-clone lazy fetch · the cruise queue's folding across versions, independently · the text report layout · midnight crossing and who fetches the lane (inferred, not run).

## What PROME asks

1. B1: fix it, since it is the one case that loses headlines silently on today's lane. If you would sooner accept it by name, say why; that choice then goes to Will with your reason.
2. B2 to B4: your call whether each gets a loud UNKNOWN line now or a declared limit. A declared limit is a complete answer.
3. Keep the fix small: the follow-up read is the fix diff only.

No capital path. The schedule in the collection repository is unchanged.
