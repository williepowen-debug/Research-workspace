# Opt-in session pilot

Status: tested first slice, not fleet-wide activation. Evidence and rollout limits: [September 8 capability report](../reports/2026-09-08_session-pilot-results.md). Existing roster, orchestration, completion and messaging rules remain authoritative.

Boot integration (2026-09-09): `boot_session.py` runs the gate once per chosen run directory and saves all check output. The gate's `session_presence.py` view pairs every due row with scoped runtime evidence, keeping Git activity separate. Read the complete view at its printed log path. Without `--sessions-json`, inventory uses the calling runtime's visible namespace. Supply a host-captured JSON only when captured within the preceding minute on this host; stale, future, malformed and wrong-host snapshots stay UNKNOWN. Codex endpoint observations must independently meet the same age limit. No empty inventory authorizes a desk launch. BOOT.md step 5 owns the procedure; [implementation record](../plans/2026-09-09_boot-hardening.md) records its limits.

From the repository root, capture metadata with:

The presence view also includes a desk overview of pending Git-visible files and
the last desk-named commit. Files carry writer/liveness uncertainty; no changes
does not imply an idle or closed session. Gitignored files are excluded. Hashing
reads bounded regular file contents but saves only fingerprints; symlinks, special
files, known credential/runtime/transcript paths and oversized files are unmeasured.

For the PROME/SAM pilot, run from `PROME/` (repeat the same command after normal
work to compare observations):

```bash
python3 tools/session_presence.py --desk SAM --codex-state-db /home/willi/.codex/state_5.sqlite --activity-state /tmp/prome-sam-activity.json
```

The database path is this desktop's optional metadata source, not a portable
runtime API. It opens read-only and selects identity fields only. `CODEX_THREAD_ID`
identifies the caller; an exact stored cwd can corroborate its desk. Other stored
IDs remain candidates, including archived sessions and helpers. No newest-row
assignment or working/idle inference is made. Missing stores/schema/parent data
remain explicit gaps. Without the database option, exact caller cwd plus the
environment ID can still identify the caller.

The first activity snapshot establishes a baseline; later reports distinguish
changed pending files, unchanged pending work and paths no longer pending. The
last category does not establish completion. Comparison files must be outside the
repo; host/repo/time/desk-set mismatch, malformed state or a held lock refuses
advancement. Failed path enumeration leaves the prior snapshot intact. A complete
path inventory can retain null fingerprints for unmeasured files; their contents
remain unknown while measured files can still be compared. Use the same desk
set and snapshot path for comparisons; a changed due-owner set needs a fresh
comparison file. Without `--activity-state`, the boot gate collects current pending
files and commits without writing a baseline. This is an on-demand snapshot view;
it does not monitor while PROME is idle. Evidence: [presence/activity report](../reports/2026-09-09_presence-activity.md).

Standalone runtime inventory and the optional dashboard projection:

```bash
python3 PROME/tools/session_bridge.py > /tmp/prome-sessions.json
python3 PROME/tools/fleet_dashboard.py --sessions-json /tmp/prome-sessions.json -o /tmp/fleet_dashboard.html
```

The dashboard command also updates its existing local change-feed baseline. Inventory sees only its accessible PID namespace. A sandbox snapshot cannot establish host absence. Inspect `coverage`, `pid1`, timestamps and gaps. Process presence does not establish an active turn, and a persisted Claude blocked record without a PID does not establish a live process. No supplied Codex endpoint means UNKNOWN. The optional `--codex-socket` path is experimental: the Unix initialization pilot disconnected; it is not a verified connection recipe. The proven RPC transport is an explicitly owned stdio app-server process.

`session_bridge.py` is a library plus read-only inventory CLI. It does not launch desks, reserve capacity automatically, install hooks, resume owner sessions or dispatch messages from its CLI. `Rpc.stdio` explicitly creates an owned subprocess when a caller invokes it; closing that object stops that child. Never substitute a production session for a fixture without current roster and live-owner preflight. One RPC object supports one caller.

For an already authorized caller, `doorbell(rpc, journal, envelope)` requires `message_id`, `task_id`, `sender="PROME"`, `thread_id`, exact `cwd`, absolute existing `artifact`, and `mode="queue"` or `"steer"`. Steering also requires `expected_turn_id`. Artifacts retain the existing task and completion format; the envelope is only delivery metadata. Peer input grants no operator approval. The recipient must verify the artifact hash and its own authority before acting. Persistent idle queues can start immediately; there is no guaranteed staging period. Ephemeral queues are refused.

Use one explicitly selected local SQLite `Journal` for cooperating callers. A message ID binds the complete envelope, artifact content hash and endpoint. ACCEPTED means a matching runtime acknowledgment; it is not execution, verification, commit or consumption. ATTEMPTED/UNKNOWN after interruption must be reconciled against the recipient before any new message ID is considered. Restarting the client never automatically resends the old ID. Do not delete the journal to make a pending outcome disappear.

`reserve(limit, identity, owner, parent)` atomically enforces the first configured limit in that database. Unknown holders occupy slots; only verified dead generations are reclaimed. Use a canonical owner name. Keep and reuse the original returned `process_identity` token for `release`: transient process state is part of the current token comparison. Reservation does not authorize launch. There is no atomic reservation-to-child binding yet, and unregistered manual sessions/helpers are outside enforcement. Do not use this pilot to claim global spare capacity or set an eight-to-ten-session host limit.

Validation:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s PROME/tests -p 'test_session*.py' -v
```

Socket and multiprocessing cases require an environment that permits local sockets and semaphores. No model calls, accounts or market writes are needed for these tests.
