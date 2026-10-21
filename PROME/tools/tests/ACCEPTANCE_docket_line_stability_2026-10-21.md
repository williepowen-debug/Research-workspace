# ACCEPTANCE — DOCKET line-number stability guard (SCRATCH owed item 0, 2026-10-21)

**Origin:** Will 2026-10-20 22:13 ET, verbatim *"ok check"*, approving the item after PROME found that DOCKET rows are cited by physical line number (L#) while nothing stops a commit from shifting them. `PROME/tools/docket_row_cap.py` has the only ROWS-REMOVED test, and it is DORMANT: `DOCKET_ROW_CAP_BYTES` is unset, so it never runs. Even if it were active, it pairs rows by position, so a mid-file insert, a swap and a delete+append all pass it (tested 10/20, `memory/2026-10-20.md`).
**Written before the code** (WQ-229). Process change 2 of this session (ceiling 3).

## Defect, in its own terms
A DOCKET citation `L<n>` names a row by its physical line. If a commit moves the content of any existing row to a different line, every citation of that row and of every row after it silently points at a different obligation. No reader can tell, because the row it lands on is a well-formed row.

## Acceptance conditions (properties, not symptoms)
- **P1 — identity:** after any commit the guard admits, every line number that existed in the base still addresses the same row, either unchanged or edited in place.
- **P2 — refusal:** a commit that leaves the content of a base row at a different line number than in the base is refused (rc 1) and the refusal names the line. This includes a mid-file insert, an insert before the last line, a swap, delete+append, a mid-file delete and an EOF delete.
- **P3 — always on:** the guard needs no configuration and has no dormant state. It runs on every commit that includes `PROME/DOCKET.tsv`, independent of the row-cap policy.
- **P4 — fail closed:** if the base blob or the candidate cannot be read, the result is rc 2 and the hook refuses the commit. rc 2 is never read as clean.
- **P5 — admits the legitimate forms:** any number of in-place edits, EOF appends, both together, and a no-op all pass (rc 0).
- **P6 — what is checked is what is committed:** `--staged` reads the index (`git show :PROME/DOCKET.tsv`, GIT_INDEX_FILE-aware), so `git commit <path>` is checked on exactly the content it commits.
- **P7 — no silent escape:** a sanctioned renumbering, such as an archival rotation Will approved, passes only when `DOCKET_LINE_SHIFT_APPROVED=<record>` is set. The pass prints a ⚠️ line naming that record. `--no-verify` stays forbidden by the hook text.

## Neighbours (WQ-229 five categories)
- **Ordinary:** in-place edit plus EOF append passes (P5).
- **Overlap:** an insert combined with an in-place edit of the next row must still be refused, because a later shifted row is still detected. Repeated identical lines in the base (blank lines, repeated comments) must not produce false MOVED findings: only base lines that occur exactly once are position keys.
- **Wrong owner:** the hook runs for every committer on this machine, any desk or runtime. The account-number guard must still run first on every commit, with ordering unchanged.
- **Missing information:** no DOCKET at the base rev, or the file absent from the index, gives rc 2 (P4).
- **Concurrent activity:** an unstaged working-tree edit must not affect a `--staged` verdict (P6).

## Known limit (declared, not hidden — restated after independent read 1)
Any displacement where EVERY moved row is also edited is invisible: an insert followed by edits to every later row, a swap of two rows that are both edited (CX2, kept as a test that documents the limit), or a whole-file reformat that changes every row's bytes. The hook runs only inside `git commit` against HEAD, so a `pull --rebase` replay or a merge that re-orders two desks' concurrent EOF appends is not checked; `--base HEAD^2` / `--base ORIG_HEAD` detects it when run by hand. The guard protects line identity, not row content.

## Test file
`PROME/tools/tests/test_docket_line_stability.py`: pure scan cases plus throwaway-repo hook cases.

## Reads
- **reads: 1.** Independent read 1, 2026-10-21 08:2x ET (general-purpose, Opus, own counterexamples; replayed 300 real DOCKET commits, 0 flagged): **HOLD, 1 ❌ · 7 ⚠️**.
  - ❌-1 (CX1) a CRLF flip in the same commit hid a mid-file insert. **FIXED** after the read: one trailing CR per row is ignored. CX1 is now a refused test; the CRLF flip alone passes. The reader had tested this exact fix on a copy (20/20 suite, 656 findings on CRLF+insert against the live docket).
  - **State:** IMPLEMENTED · TESTED (23 + 28 pass). The ❌ fix came after the final read, so it is **NOT independently verified**. Read 2 remains available inside the ceiling if Will wants it.

## Declared residue (WQ-178, 2026-10-21 — ⚠️ not fixed)
- ⚠️-2 a swap with both rows edited is admitted (CX2): now in the known-limit text and kept as a test.
- ⚠️-3 a rebase or merge of concurrent EOF appends can move a just-cited row without the hook running: declared in the limit. A `safe-push.sh` / recovery-path run with `--base ORIG_HEAD` would be a further process change, for a later session.
- ⚠️-4 the escape accepts any non-blank value and persists for the shell. Candidate fix: require an existing ruling-record path.
- ⚠️-5 the hook reads rc 0 as clean with no sentinel (fail-open only with a fake `python3` that exits 0).
- ⚠️-6 rare false refusals: an edit making a row identical to another unique row; an amend that drops a just-appended row (hint: `--base HEAD^`).
- ⚠️-7 an intentional `git rm`/`git mv` of the docket gets "could not run — fix the check" (misleading). Separately, and pre-existing, the account guard is skipped silently if `python3` is absent.
