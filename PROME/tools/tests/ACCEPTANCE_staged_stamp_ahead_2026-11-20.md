# Acceptance — the commit hook flags a clock stamp that is ahead of the clock, 2026-11-20

reads: 1 of 3 (one result read; no plan read)

Authority: WQ-713 (Will 2026-11-17 20:42 ET, "yes go ahead"), DOCKET L1188 item 1: the commit hook flags a clock stamp in staged text that is later than the commit time. Only that; not every approximate time. The existing hook (`scripts/githooks/pre-commit`) is extended by one call to a helper, `PROME/tools/staged_stamp_check.py`.

Defect: a stamp typed from narrative instead of taken from `date` runs ahead of the wall clock, by 20 to 40 minutes at worst, and is committed as a record of when something happened (`memory/auto/finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock.md`, n=5; three more on 2026-11-20). A time that has not happened yet cannot be a record.

Written before any edit.

Properties:
1. Ordinary: a line ADDED in the staged change that holds a full stamp, an ISO date directly followed by a clock time with its zone (`2026-11-20 13:45 ET`, also EST or EDT, or `2026-11-20T18:45Z` with optional seconds), whose instant is more than 2 minutes and at most 24 hours later than the moment of the commit, is printed to the committer with its file and the stamp, and the words that a scheduled time may be ignored. The commit proceeds.
2. Overlap:
   - a stamp at or before the commit time, or within 2 minutes after it, prints nothing;
   - a stamp more than 24 hours ahead prints nothing: that is a calendar entry, not a drifted stamp;
   - a time with no ISO date directly before it (`14:28 to 14:30 ET`, `Fri 11/20 16:05 ET`, `13:1x ET`) prints nothing;
   - a stamp with no zone prints nothing (its instant is not known);
   - lines removed by the change and unchanged context lines are not read;
   - the hook's existing checks (account numbers, DOCKET line stability) return what they returned before, in the same order, and the stamp check never changes the hook's exit code.
3. Wrong owner: N/A. The check reads whatever is staged by whoever commits; it names the file, never an author.
4. Missing information: no Python, no helper file, a helper crash, a binary file or undecodable bytes in the staged change, an empty staged change: the commit proceeds and the existing checks are unaffected. A helper failure prints at most one line.
5. Concurrent activity: N/A. The helper reads the index once and writes nothing.

Declared limits before the build:
- It flags; it does not refuse. A printed line can be ignored.
- A same-day scheduled time written as a full stamp (`2026-11-20 16:05 ET` in a plan) is flagged too. The message says a scheduled time may be ignored.
- Approximate and partial forms are not read at all, by the row's own words.
- The hook runs only where `core.hooksPath` points at `scripts/githooks`, and a commit made with `--no-verify` skips it.

## Disposition 2026-11-20 13:26 ET (WQ-229 states)

IMPLEMENTED · TESTED (25 of 25) · INDEPENDENTLY VERIFIED by one Opus reader, before the hook was edited, for every property except the one failure below: in a throwaway repository with the real guards, the candidate hook matched the live hook on exit code and existing messages for an ordinary commit, an account-guard refusal, DOCKET edited in place and with rows moved, the helper missing, and a helper that exits 1, raises or is killed; a real commit with a stamp 29 minutes ahead printed the flag and succeeded. · STILL UNRESOLVED: the fix below is unreviewed, and the residue.

The reader's one failure, FIXED AFTER THE READ and therefore NOT independently verified: an added line whose own text starts with `++` shows in the diff as `+++ ...` and was read as a file header, so its stamp was missed and a following stamp could be pinned on the wrong file. The helper now treats `+++ ` as a header only before a file's first hunk. Three fixtures cover it (the author's own, not a reader's). The hook file is installed exactly as the reader read it.

Declared residue (reader's flags, none fixed):
- A helper that fails before its own error handling (replaced by a broken file, or killed) prints more than one line; the exit code stays 0. Property 4's "at most one line" holds only for failures inside the helper.
- Full forms not read: seconds on an Eastern stamp (`13:45:10 ET`), a one-digit hour, fractional seconds or a numeric offset on a UTC stamp, a double space after the date.
- Plain `ET` in the repeated hour of the autumn clock change is read as daylight time; a wrong `EDT` or `EST` label is taken at its word.
- When the account-number guard refuses a commit, the stamp check does not run.
- Not tested: Python older than 3.9, the 20-second diff timeout, commits made with `-a` or with paths, merge commits, quoted or non-ASCII paths.
- Cost: about 0.05 seconds a commit with nothing staged; a 50 MB staged change took 2.5 seconds and about 390 MB of memory.
