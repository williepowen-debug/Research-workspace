# Gate C Live-Interface Remediation

**Date:** 2026-08-26 (ET; rehearsal clock 2026-08-27 UTC)

**Authorization:** Will, in-session 2026-08-26 — "approved - go ahead with the
build" — against the remediation list in `KERNEL/GATE_C_C7_ACTIVATION_PACKET.md`.

**State:** BUILT AND REHEARSED — INDEPENDENT ADVERSARIAL REVIEW OWED — NOT ACTIVE

**Builder:** PROME (this session). Per the review boundary adopted with the
authorization, the builder may not review its own remediation; the independent
review must run in a separate session, preferably a different lane than the
builder, and not in the same sitting.

## What was built

One explicit live mode; no synthetic refusal was weakened.

| Piece | Commit | Behavior |
|---|---|---|
| `tools/live_grant.py` | `f8560f2c0` | Capability grant mintable only by a validated activation; direct construction fails closed |
| `tools/live_shadow.py` | `f8560f2c0` | The single live interface: `--preflight` (read-only), `--apply` (one attended pass + registered views), `--check-views`, `--audit-additions` (both read-only; window not required) |
| `tools/locking.py`, `tools/writer.py` | `f8560f2c0` | Optional `live_grant` parameter replaces the default live-repository refusal with exact-equality against the granted roots; every no-grant path keeps the existing refusals verbatim |
| `tools/render.py` | `f8560f2c0` | `context_inputs` kwarg: receipts and unprocessed approved submissions join the view source digest without entering replay (readiness property 7) |
| `policies/actors.json`, `policies/capability-grants.json` | `f8560f2c0` | Least-privilege live registries: SAM `question.register` + `forecast.submit_own`; PROME `command.accept`; WILL `policy.override`; RED registered with no grants |
| `tests/test_live_shadow.py` | `f8560f2c0` | Live-mode refusal matrix and acceptance paths; suite 191 → 207 |

## Mapping to the blocked packet's required remediation

1. **One explicit live mode, not a weakened boundary.** `gate_c_boundary.py`,
   `acceptance.py`, `audit.py`, and `projection.py` are untouched and still
   refuse the live repository. The only door is `live_shadow.py`, and the only
   key is a grant that `authorize_live_activation` mints after every check.
   Tests prove the no-grant refusals are intact and that a grant cannot be
   minted directly.
2. **Exact inputs.** The activation document pins the absolute
   `repository_root`, the repository identity, the native `source_commit`, each
   submission's exact path and file SHA-256, the three policy files by path and
   SHA-256, and the complete command→event ID map. The CLI separately requires
   the live root (must equal the pinned root after resolution) and the full
   submission commit (submissions are read from Git at that commit, never the
   working tree). Result and view paths are derived exactly from the granted
   root: `KERNEL/shadow/events/YYYY/MM/`, `KERNEL/audit/commands/YYYY/MM/`,
   `KERNEL/views/`; the store and lock refuse any other target.
3. **Activation document with Will's exact half-open UTC window and command
   IDs.** Live modes capture one real-clock UTC instant — there is no injected
   time argument — and refuse before any write on: absent or unreadable
   document, any field-set or content defect, window not started, window
   closed, revocation passed, root binding mismatch, policy-pin hash mismatch,
   submission absent at the commit, submission byte mismatch, embedded-ID or
   actor/path disagreement. Each is a named subtest case (66 subtest cases
   across two omnibus tests — granularity corrected per the 2026-08-27
   adversarial review, note N1; coverage unchanged).
4. **Writer and repository discipline preserved.** The activation `writer_id`
   must equal the custody policy's primary writer (PROME); an active substitute
   custody window blocks the primary before any write (abort drill, step 2 of
   the transcript). The tool never stages, commits, or pushes — after `--apply`
   it prints the exact per-file paths for the operator to stage explicitly.
   Durable results are additions-only (audited) and `.rw/` remains disposable
   (byte-identical rebuild drill, step 8).
5. **Refusals tested, then the complete C6 rehearsal repeated through the
   exact new interface.** Suite: **207 tests pass** (baseline was 191);
   `compileall` clean. The disposable-clone rehearsal ran the full flow through
   `live_shadow.py` — preflight → custody abort drill → apply → idempotent
   retry → check-views → operator staging → additions-only audit → projection
   delete/rebuild — with the clone playing the live root and the actual live
   repository verified untouched (0 files under live `KERNEL/shadow` and
   `KERNEL/views`). **The full console transcript is durable** at
   `KERNEL/rehearsals/2026-08-26_live-interface-rehearsal-transcript.txt`,
   closing C6's disclosed evidence limitation.
6. **Independent adversarial review — OWED.** Only after that review may a
   fresh C7 packet fix start and end timestamps and request an activation
   ruling.

## Rehearsal evidence (from the durable transcript)

- Rehearsal clone head at start: `f8560f2c0`; SAM-33 submissions committed in
  the clone at `79b533eb107ea2e1db259a84fed0afdffdc49d76`; results committed at
  `5b534e5797e96788803007b1aecd5e3d8440ce5e`.
- Accepted events: `EVT-…033` sha256 `15151286e93b…`, `EVT-…034` sha256
  `fde0558c0e9f…` under `KERNEL/shadow/events/2026/08/`; zero receipts.
- All four registered views rendered with the shadow notice and reproduced
  byte-identically under `--check-views`.
- Abort drill: `CUSTODY_DENIED` on both commands, `durable_outcomes=0`, zero
  files written; removal of the substitute activation restored acceptance and
  the retry returned `EXISTING` results.
- Additions-only audit `PASS` for `79b533eb1..5b534e579`.
- Projection sha256 `87caea97d0ca…` identical before and after deleting `.rw/`.

## Disclosed limitations

- A second `--apply` inside the window re-renders views with its own captured
  instant (an explicit regeneration; time-relative rows may change). A real
  pilot is a single attended apply; `--check-views` verifies against the
  committed `render_as_of`.
- `--check-views` and `--audit-additions` deliberately do not require the
  window: they are read-only closeout verification. `--preflight` and
  `--apply` require it.
- The rehearsal activation names the disposable clone as `repository_root`; a
  leftover rehearsal document cannot authorize the real repository — the root
  binding fails closed on the path mismatch.
- Trusted-history reachability beyond resolving the supplied full commit
  remains the declared limitation recorded at checkpoint 12; unchanged here.
- The grant key restrains accidental construction under the approved
  cooperative-actor threat model (design decision 20); it is not cryptographic
  protection against a malicious direct writer.

## Independent review brief

The reviewer should, at minimum: attempt to reach a live write without a valid
activation document and through every lower-level component directly; attempt
direct grant minting; exercise expired, unstarted, revoked, and boundary-instant
windows; tamper each pinned hash; attempt a rehearsal-style activation against
the real repository root; verify the no-grant refusals still hold across store,
lock, boundary, acceptance, audit, and projection; re-run the 207-test suite and
the disposable rehearsal end to end; and reconcile this record against the
transcript. Only after that review may a fresh C7 packet be prepared.
