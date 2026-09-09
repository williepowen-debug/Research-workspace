# Boot hardening — implementation evidence

Owner: PROME · Date: 2026-09-09

Will authorized implementation with “ok lets do it.” Scope and reviewed
invariants: [implementation record](../plans/2026-09-09_boot-hardening.md).

VERIFIED in code and fixtures: bounded digest-checked document pages, an exclusive
boot-attempt receipt with saved verdict replay, complete child-check logs with
explicit omitted-warning previews, runtime evidence beside every due row, and
literal-file stage → commit → verify → safe-push sequencing. BOOT/CLOSEOUT and
both skill copies carry the commands; the manuals remain authoritative.

VERIFIED host observation at 2026-09-09T20:58:41Z: two Codex processes were visible
outside the sandbox, both with cwd `/home/willi`; Claude inventory returned no
sessions. The default managed Codex daemon control socket was absent (ENOENT).
These observations do not identify desks or active turns. The native same-minute
ListAgents requirement remains unchanged; no desk was launched or messaged.
Official transport reference: [Codex App Server](https://learn.chatgpt.com/docs/app-server).

## Validation

- New boot/presence tests: 11 passed; page reconstruction, changed source,
  repeated/in-flight/interrupted gate claims, fourth warning retention, exact cwd,
  parent metadata, stale/future/wrong-host/malformed inventory and process-only gaps.
- New Git tests: 6 passed in temporary repositories, including index-lock failure,
  pre-commit-hook failure, strict verification failure, failed status, rejected
  directory/symlink scopes, literal wildcard filename and foreign staged changes.
- Existing session tests: local socket fixtures require host permissions;
  the remaining dashboard CLI fixture needed the current `heartbeat_errors` field.
  That fixture was corrected without changing dashboard production behavior.
- Existing session regression: all 35 tests passed after that fixture correction.
  Total: 52 tests across the three relevant suites.
- Live host snapshot at 2026-09-09T21:16:05Z additionally saw one Claude session
  in another workspace. The presence view retained all nine due rows, including
  the previously hidden RED D:L275, and assigned no unrelated session to a desk.
  Snapshot verdict: [complete due-row evidence](2026-09-09_boot-hardening-presence.txt).
- Boot-closeout symmetry and root/PROME skill parity passed. Spawn-list frozen
  vintage selftest passed all seven cases; diff whitespace check passed. The
  mirror-map scan found only the earlier boot report's historical command receipt,
  which remains accurate and is intentionally preserved.
- Independent PLAN and RESULT reads completed. RESULT found one defect: Unicode
  and JSON escaping could enlarge a character-bounded page. Corrected once by
  bounding serialized text; the new CLI fixture reconstructs escaped/Unicode
  content over every page. No other correctness/safety blocker was found.
- Fleet closeout: [saved verdict](2026-09-09_boot-hardening-closeout-gate.txt).
  The pre-existing due-today DOCKET check remains BLOCKED for L235/L253/L266/L268/L275,
  matching the earlier [closeout record](2026-09-09_closeout.md). No new coverage
  or completion is asserted to make it pass. This authorized implementation is
  saved with the operational failure disclosed; it is not a fleet operational PASS.

No BOARD-advancing boot gate was rerun. GATES/DOCKET, decisions and market regime
are unchanged: this task produced no owner grade, broker receipt or new market
observation. Future boot uses the guarded command in BOOT.md; relevant operational
follow-through remains in SCRATCH and the existing ledgers.

## Declared residue

UNKNOWN: complete correspondence to Will's actual open windows, pending his answer
and a usable discovery endpoint. Process sightings alone cannot resolve it.
Loaded thread metadata is scoped to one server; missing rows never prove absence.

The retry receipt relies on reusing the chosen run directory; it cannot prevent
an operator from invoking the raw advancing gate. `/tmp` evidence is machine-local;
copy relevant receipts into a durable report before a machine switch or cleanup.
The Git wrapper still shares its intent file and moving HEAD with other callers;
existing coordination remains required. The existing message-file read emits a
ResourceWarning under the test warning policy; it does not change test outcomes.
Generic Codex skill validation rejects the existing Claude `user-invocable`
frontmatter key. That native field is preserved; YAML and root/PROME parity were
validated separately. This change does not install Codex hooks or start a daemon.
