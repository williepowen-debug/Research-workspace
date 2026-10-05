# Acceptance — docket row cap: staged mode reads its policy from the index (CATO PR1)

**Defect (CATO `AGENTS/CATO/runs/2026-10-05_1743_prome-commit-review.md` PR1, VERIFIED by CATO; re-read by PROME prome-95 2026-10-05 18:1x ET at `PROME/tools/docket_row_cap.py:54–62,139–148,156–159`):** `--staged` takes the docket candidate from the index (`:PROME/DOCKET.tsv`) but the cap from the WORKING-TREE `scripts/harness_caps.env`. The pre-commit hook runs `--staged`, so a commit's row and the policy governing it can come from different versions: an unstaged removal or raise of the cap lets an over-cap row commit while the committed policy forbids it; an unstaged tightening wrongly blocks a valid commit. Pre-activation repair: the cap is unset today (no production over-cap commit established).

**Authority:** Will 2026-10-05 18:06 ET, in session, relaying CATO's report: *"Okay PROME can you look into these"*. Purpose class: PROCESS. This is the session's one process change (WQ-299 R1). No cap number is chosen or set by this repair.

## Acceptance conditions (written before the edit)

A1. With `--staged`, the policy (`DOCKET_ROW_CAP_BYTES`) is read from the SAME index the docket candidate comes from (`git show :scripts/harness_caps.env`, honouring `GIT_INDEX_FILE`). Working-tree mode (no `--staged`: the PostToolUse save hook and the closeout gate's worktree row) keeps reading the working-tree file.
A2. Unchanged committed policy + an over-cap staged row ⇒ refused (rc 1), whatever the unstaged policy file says: unstaged key REMOVED, unstaged cap RAISED.
A3. An unstaged TIGHTER cap does not block a staged row that is within the indexed cap.
A4. A deliberately STAGED policy change is evaluated with its candidate: policy and docket staged together ⇒ the staged policy governs (raise ⇒ allowed; key removal ⇒ dormant with the notice; tighten ⇒ refused).
A5. Missing information is distinguished: key absent from the indexed file ⇒ dormant (rc 0, notice says the source); policy file not in the index at all ⇒ dormant, same rule as an absent working-tree file, notice names the index; policy blob present but unreadable / not UTF-8 / conflicted (unmerged stages) / malformed value ⇒ rc 2, and the hook refuses. Never a silent default.
A6. Pathspec commits (`git commit <path>`, git's temporary index) and an explicit alternate `GIT_INDEX_FILE` keep the behaviour: the policy comes from the index the commit is built from.
A7. `--cap N` still overrides any configured value in both modes.
A8. No cap value is set anywhere by this repair; `scripts/harness_caps.env` is unchanged.

## Neighbour categories (WQ-229 — considered, not performed mechanically)

- **ordinary:** A2 baseline (unchanged policy rejects oversize row).
- **overlap:** A4 (policy + docket in one commit); a partially staged policy (index differs from both HEAD and the working tree).
- **wrong owner:** A2/A3 — another session's unfinished, unstaged edit to the shared policy file (CATO's scenario).
- **missing information:** A5 (unset key, absent file, unreadable/conflicted blob, malformed value).
- **concurrent activity:** A6 (temporary index of a pathspec commit; alternate `GIT_INDEX_FILE`).

## Review

Consequential (a commit gate) ⇒ an independent reader devises at least one counterexample of its own before this is called fixed. Completion note distinguishes IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED.

## Record

- **Read 1 (independent, Opus, 2026-10-05 ~18:10 ET):** verdict YES, correct for the defect; 20+ own counterexamples through the real hook (`commit -a`, `--only`/`--include`, hunk-level partial staging, subdirectory cwd, linked worktree, sparse checkout, skip-worktree/assume-unchanged, textconv, CRLF, executable bit) — none admitted an over-cap row the indexed policy forbids or read policy and rows from different versions. ⚠️ C5/C7: a policy committed as a symlink or submodule was read as link/commit text ⇒ dormant (fail-open). **Fixed after read 1:** staged mode now accepts only a single regular-file index entry (mode 100644/100755, exact path) and returns rc 2 otherwise; the directory-named-path case (C6) now reports "not a single file" (read 1 observed "is in the index but unreadable" for a single file under the directory; rc 2 refused either way). Test `test_non_regular_policy_entry_in_index_is_unknown`. Read 2 = changed-portion check of that edit.
- **Declared residue (not fixed here; C9/C10 and C6 predate this repair, C17 is a behaviour change this repair introduced):** C9/C10 — `parse_cap` treats a BOM-prefixed, space-indented, `KEY = N` or `export KEY=N` line as an unset key ⇒ dormant with the notice, in both modes · C6 — working-tree mode crashes (`IsADirectoryError`, exit 1, reads as a finding rather than UNKNOWN) if the policy path is a directory · C17 — with both the docket and the policy removed from the index, the new code reports dormant (rc 0) where the old reported rc 2 "not in the index"; consistent with A4/A5 because the dormant check precedes the candidate read, and noted so the change of return code is not a surprise · A6 alternate-`GIT_INDEX_FILE` is tested by calling the tool directly; the reader's C4b/C4c covered git's own temporary index through the hook.
- **Read 2 (same independent reader, changed-portion, ~18:12 ET):** ❌ 0. C5 symlink (mode 120000), C6 directory (one or two files under it) and C7 submodule (mode 160000) all rc 2 and refused through the real hook; regular files at 100644 and 100755 enforce normally; sibling paths with a tab, quote or accent never reach the parser under either `core.quotePath` setting (a CAPS_ENV renamed to such a path would need the compare revisited). Two wording ⚠️ on this Record (C17's heading, C6's quoted message) fixed after read 2 — record wording only, no code. **State: IMPLEMENTED · TESTED (28 docket-cap tests; 39 closeout + 14 locks + 46 boot + 33 repeat-boot + 17 orch suites OK) · INDEPENDENTLY VERIFIED (reads 1–2) · STILL UNRESOLVED: the declared residue above; the cap number and activation remain Will's.**
