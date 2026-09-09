# Presence and file activity — implementation record

Owner: PROME · Date: 2026-09-09

Will approved “Okay go ahead” after the proposal to add file activity first,
then identify the PROME and SAM sessions. SAM has independent dirty work; it is
read-only input. No desk files, runtime settings, messaging or launches change.

## Plan for independent cold read

- Add a bounded `desk_activity.py` reader using literal, NUL-delimited Git status
  and desk-subject commit history. Report dirty/untracked filenames and the last
  matching self-commit with its recorded timestamp. This proves pending work in
  a directory, not its author or live session state. Ignore mtime as a freshness
  authority. Failures/omitted paths are visible, never interpreted as inactivity.
- Support an explicit machine-local snapshot file for comparisons. Hash bounded
  regular pending files without following symlinks; save hashes, metadata and
  observation timestamps only. First observation is a baseline, not a new edit.
  Later content/status differences mean “changed between observations”; paths
  leaving the dirty set mean “no longer pending,” never inferred deletion or
  completion. Large/unreadable/changing files remain unmeasured. Atomic snapshot
  replacement with a lock; reject wrong-repo/host/version/future/invalid baseline.
  No background watcher or daemon. The boot default can show pending files and
  commits without writing a comparison snapshot.
  Live-trial clarification: a complete path inventory can retain explicit null
  fingerprints for unmeasured files; those contents are never compared as unchanged
  or changed. Structural scan failures preserve the baseline. This allows large
  files to remain visible without preventing comparisons of other measured files.
- Add a small read-only Codex identity adapter. Environment CODEX_THREAD_ID
  identifies the calling session, corroborated against exact canonical cwd in
  the local metadata store when available. Optional explicitly supplied SQLite
  store opens mode=ro and selects only allowlisted identity/cwd/archive/time/parent
  metadata, never prompts, titles, transcripts or credentials. Stored rows are
  candidates, not live sessions; no newest-row-wins assignment. Helpers remain
  distinct via parent metadata. Missing schema/store/session => UNKNOWN.
- Extend session_presence.py with a per-desk overview (runtime, stored identity,
  file activity) above its complete due-row view; include explicit --desk values
  so PROME and SAM can be inspected without a due row. Existing direct report()
  tests remain isolated from Git/filesystem discovery. Capture each desk once,
  reuse evidence for all its rows, preserve all existing UNKNOWN and no-spawn
  boundaries. Add CLI options for explicit activity snapshot and metadata store.
- Update SESSION_PILOT.md and a concise HANDOFF pointer; the existing BOOT gate
  already invokes session_presence.py, so no canon or skill command change needed.
  Save tested live PROME/SAM observation and limitations in a result report.

## Acceptance

Temporary Git fixtures cover dirty tracked files, new/untracked, staged rename,
deletion, unusual literal names, foreign-authored commit touching a desk, ignored
files, read failure, restored mtime/content change, first/repeated/changed snapshot,
and clean/no-longer-pending transition. Snapshot lock/corruption/foreign provenance
must not silently advance the baseline. SQLite fixtures cover exact cwd, self ID,
multiple candidates, helpers, wrong/missing schema, missing db without creation.
CLI fixture includes SAM with no due row and file evidence despite runtime UNKNOWN.
Run relevant existing boot/session regressions. Compare live snapshots without
modifying SAM. No BOARD-advancing gate rerun.

## Review and residue

PLAN cold read: `activity_plan_review`, no blocking findings. Declared warnings:
retain baseline provenance, leave missing parentage UNKNOWN, and distinguish
content hashing from metadata-only reads while excluding sensitive/runtime paths.
RESULT cold read: one blocking finding, corrected once — failed enumeration no
longer emits a false self-commit change; comparisons return UNKNOWN and preserve
the baseline. Added failure fixture passes. Declared RESULT warning: working-tree
fingerprints plus status do not detect index-only content changes with unchanged
status. Runtime working/idle visibility may remain UNKNOWN
where no supported endpoint is available. File activity and stored metadata never
grant native spawn authority. Local SQLite schema is an optional compatibility
adapter, not a stable public runtime API; schema drift must fail visibly.
