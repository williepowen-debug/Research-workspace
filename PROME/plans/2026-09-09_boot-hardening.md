# Boot hardening — approved implementation record

Owner: PROME · Date: 2026-09-09

Authorization: Will's “ok lets do it” after the boot-feedback proposal. Scope:
bounded reads, session evidence beside dated obligations, one BOARD-advancing
gate attempt per boot, and stop-on-failure Git persistence. No runtime launch,
daemon installation, hook activation, domain edits or change to spawn authority.

## Plan and invariants for cold read

1. Add `tools/boot_read.py`: one UTF-8 document per call, bounded character
   pages, source SHA-256 and explicit continuation; continuing requires the
   same digest. Long lines also split; changes between pages refuse continuation.
2. Add `tools/boot_session.py`: caller chooses one local run directory per
   boot and reuses it on every retry. Exclusive creation claims the attempt
   BEFORE starting `prome_gate.py boot`; save complete output and return code.
   Existing completed attempts return the saved verdict; interrupted/in-progress
   attempts return UNKNOWN without rerunning. Bind receipt to repository.
   No automatic retry of BOARD. Existing standalone checks remain available.
3. Add a read-only presence view using existing `session_bridge.py` metadata
   and `spawn_list.collect`, keeping Git activity separate from runtime evidence.
   Boot captures a local snapshot unless a fresh host JSON snapshot is supplied.
   Matching exact canonical desk cwd + fresh runtime session metadata can show
   a session observed; process cwd alone cannot identify active turns. Stale,
   malformed, missing endpoint, wrong-host or incomplete inventories remain
   UNKNOWN. Empty lists NEVER authorize a spawn. Parent/helper identifiers are
   retained when available. No claim of complete host visibility.
4. Gate dispatcher saves complete child output under the boot run directory;
   previews explicitly identify omitted flags and their log. Presence beside
   EVERY due row is saved in full with a visible pointer, including successful
   advisory checks. No change to blocking/advisory classes or due-row selection.
5. Extend `commit_check.py commit` with opt-in `--stage` and `--push`:
   exact literal file paths only; existing path verification preserved. Failed
   stage stops commit and push; failed commit or verification stops push. Push
   still uses existing ff-gated safe-push. No rollback/reset of others' index.
6. Update BOOT/CLOSEOUT and both boot/closeout skill copies, Git cookbook and
   session-pilot pointer. Keep manuals authoritative and skills ordered indexes.
   Add concise continuity entry and implementation evidence report.

## Proposed manual text

BOOT context: “On a runtime without confirmed context injection, explicitly
read root CLAUDE.md, PROME/CLAUDE.md and USER.md. Do not assume Claude hooks ran.”

BOOT reads: “Use `python3 PROME/tools/boot_read.py <path>` from repo root for
bounded document reads. Follow every continuation with its digest until EOF;
changed-source refusal means restart that document. Run one page per tool output.
Truncated output is an incomplete read, never evidence of EOF.”

BOOT gate: “Use `python3 PROME/tools/boot_session.py --run-dir
/tmp/prome-boot-<session-id>` from repo root. Choose that directory once per
boot and reuse it on retry. The receipt prevents another BOARD-advancing attempt;
interrupted attempts require inspection of saved logs and independently runnable
checks, never a new run directory to bypass the guard. A supplied `--sessions-json`
must be a fresh same-host session_bridge snapshot. Local fallback coverage stays
explicit; presence evidence never replaces the same-minute native spawn preflight.”

CLOSEOUT persistence: “Use `commit_check.py commit --stage --push -F <msgfile>
-- <exact paths>` for one batch. Each step must succeed before the next runs;
a failed stage, commit or verification never proceeds to push. For multiple
commits omit --push until the final successful batch. On failure inspect state;
do not reset, sweep, or amend.”

## Validation

Fixtures: page reconstruction/long lines/source change; repeated and concurrent
boot attempts/incomplete receipt; fourth advisory flag retained; presence empty,
stale, future, malformed, wrong host, exact cwd, parent/helper and process-only;
Git stage/commit/verify failure prevents downstream steps, and real temporary Git
repository proves foreign staged files remain outside a successful exact commit.
Run existing session and relevant gate tests, skill parity and syntax validation.
Test the live read-only presence view; do not rerun the real advancing boot gate.

## Host evidence and limitations

VERIFIED at 2026-09-09T20:58:41Z: elevated session_bridge saw two Codex processes
with cwd /home/willi, no Claude sessions, and no supplied Codex endpoint. Default
Codex daemon control socket is absent on host (daemon version returned ENOENT).
Actual open-window comparison is pending Will's answer. Process sightings do not
identify desks or active turns. Implementation can be verified with fixtures;
complete manual-session coverage cannot yet be claimed.

## Review residue

Plan read: independent `boot_plan_review`, 2026-09-09. Blocking constraint adopted:
Git operations use literal pathspecs, refuse directory/symlink scopes, parse NUL
receipts and stop on failed status. Actual wildcard-neighbor fixture passes.

Declared plan residue (2026-09-09): manual host visibility is unverified; the
retry guard protects reuse of one chosen run directory, not arbitrary raw gate
invocations; shared Git intent/HEAD coordination remains necessary. No claim of
global exactly-once execution or concurrent-commit transaction isolation.

Result read: independent `boot_result_review`, 2026-09-09. One blocking finding:
raw character pages could expand through Unicode/JSON escaping. Fixed in one
pass by bounding serialized text and testing CLI reconstruction, including
escaped controls and Unicode. All 11 boot/presence fixtures pass after the fix;
the six Git fixtures and 35 existing session tests pass. No further rule amendment
or review round was needed. SYSTEM tool pointers follow the BOOT procedure change.

Declared result residue (2026-09-09): plan residue above persists; the existing
message-file ResourceWarning is nonblocking. Generic Codex skill validation rejects
the pre-existing Claude `user-invocable` key; native frontmatter and mirror parity
are checked separately. The operational closeout gate still flags pre-existing
due-day items; implementation and gate evidence are retained in the result report.
