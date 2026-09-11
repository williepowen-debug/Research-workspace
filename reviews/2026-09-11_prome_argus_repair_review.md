# Review of PROME's ARGUS repair

**Reviewed commit:** `c64cf4e9c10de066016ea0cfffb2d23cab5a8780`.

**Verdict: PARTIAL FIX; original finding F1 remains OPEN.** All twelve shipped regression tests pass. The simple original fixture now works, and inbound-mail attribution is improved. Additional isolated Git fixtures still reproduce missing pending changes and incorrect ownership. No operational files were edited.

## Blocking: committed paths lose their pending changes

**VERIFIED.** `PROME/tools/argus_scope.py`, `scope()`, returns `sorted(pend - paths)` for pending work. A path committed earlier in the session and edited again before closeout belongs to both sets, so its pending label disappears. The root ARGUS instructions select `git diff <watermark>..HEAD` for its remaining committed label. That diff excludes the new edit.

Using the new test suite's throwaway-repository helpers:

1. Commit the initial PROME closeout.
2. Commit a change to `PROME/STATUS.md`.
3. Append a pending closeout correction to the same file.
4. Run `scope()`.

Observed: committed `['PROME/STATUS.md']`; pending `[]`.

**Required correction:** preserve both kinds of change for overlapping paths. Count unique paths for the size threshold, but do not deduplicate away a required comparison. Add a regression for a committed-then-edited file and verify that the auditor's prescribed read includes the pending content.

## Blocking: PROME's local ARGUS definition is unchanged

**VERIFIED.** The repair changes `.claude/agents/argus.md`, but not `PROME/.claude/agents/argus.md`. The local file still instructs ARGUS to inspect only `git diff <watermark>..HEAD`. PROME's documented launch directory is `PROME/`; leaving its local definition behind fails the repository's copy-consistency contract. This review did not launch a Claude session to test runtime definition precedence.

**Required correction:** reconcile both agent definitions and check that the actual launch path receives the pending-work read instructions.

## Additional scope defects

**VERIFIED in throwaway repositories:**

- A different desk's pending edit to `memory/auto/violet.md` appears in ARGUS's pending list. `PENDING_EXTRA = ('memory/auto/',)` admits the entire shared directory. The test that excludes another desk's *committed* memory does not establish correct attribution of its *pending* memory.
- Two new files inside `PROME/new_reports/` are reported as the directory alone because `git status --porcelain` does not request all untracked files. With one committed tool file, the reported total is two rather than three, incorrectly selecting SKIP. The prescribed new-file read also receives a directory.
- An untracked daily closeout log at `memory/2026-09-11.md` is absent from scope, even though CLOSEOUT explicitly requires PROME's daily-log output to travel in its commit batch.

Use file-level, NUL-delimited Git output and an explicit pending-change ownership record for shared locations. Avoid treating directory membership as authorship.

The original intervening-domain-commit watermark issue is also unchanged: `find_watermark()` still special-cases only literal HEAD. It remains a limitation of the advertised post-closeout behavior.

## Response assessment

PROME correctly acknowledged the findings and accurately reported that the other three implementations were untouched; their files have no diff from the original audit boundary. The three open items are recorded in the repair commit body. Their absence from the inspected HANDOFF/SCRATCH is not proof that no tracking exists elsewhere, but the commit body alone is a weak next-session work queue.

“None has lost real data” is stronger than this review establishes. The supported statement is “no real data loss has been demonstrated”; neither audit inspected the hosted tap history.

Leaving the other repairs for a bounded next session is reasonable. Closing F1 is not yet justified. Complete and test this repair before treating ARGUS's pre-commit verdict as coverage of the pending closeout.
