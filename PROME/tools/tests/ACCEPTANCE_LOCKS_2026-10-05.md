# Locks safeguards implementation — acceptance, 2026-10-05

Authority: Will, this session, “Okay can you please work on implementing the fixes?” Scope: corrected v4 bundle, one bounded fleet-safeguard implementation; no boot-consumption default change, no domain launches, no trade work. Earlier bundle assessments are source feedback, not completion verification of this corrected implementation.

reads: 3

- 2026-10-05 plan read: read-only `locks_review`; no blocking findings after adding conditional legacy fallback. Reader's counterexample: active default prepare-commit-msg must be preserved, not just commit-msg/pre-push. Existing server constraints must be preserved; live baseline is no protection/no rulesets.
- 2026-10-05 result read: same read-only reviewer independently ran fixtures. One blocker: identical fleet command with wrong timeout/async metadata was called installed. Corrected by replacing only matching fleet-owned hook metadata; unrelated configuration preserved. Narrow third read justified because correcting async/timeout changes the lifecycle of a blocking safeguard; it is not a cosmetic edit. Native config race with noncooperating writer remains declared residue, not claimed prevented.
- 2026-10-05 narrow final read: reviewer independently verified timeout 1 becomes 150, async removed, unrelated settings preserved, backup exact, second install byte-idempotent. No consequential code blockers remain; review episode closed at three reads. IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED for corrected code; runtime/other-host residue reported separately.

## Plan and invariants (written before implementation)

- Native commit-msg: measure first nonblank paragraph after Git whitespace cleanup, preserving comment lines/leading indentation; join lines with single spaces; count Unicode code points after NFC independently of locale. Block >100. Read, UTF-8, Git cleanup and interpreter errors fail closed with an explicit diagnosis. Preserve the documented conservative editor-comment limitation; never claim exact editor-cleanup equivalence.
- Native pre-push: allow new refs/fast-forward commits; deny deletion/non-fast-forward; missing ancestry is UNKNOWN and denied. Supports zero IDs of either Git hash length. No assertion that a fast-forward push using --force is detected. --no-verify remains a client bypass.
- One installer shared by banner/safe-push: resolve real root; verify repo fingerprint and executable hooks; do not replace an existing hooksPath or active default hooks. Existing conflicting setup is warned at boot and aborts safe-push. Repeated installation is idempotent. Git config lock races are loud and retriable, never silently called installed. Install explicitly on current clone before removing Claude subject inspection. Keep legacy subject script available for fallback/history rather than break existing reference tests by moving it.
- Banner: bounded unshallow attempt, captured return code and rechecked shallow state; failed/remaining/unknown shallow state withholds ahead/behind numbers. No checkout, pull, merge or environment rebuild.
- Pipeline warning: exit 0 with valid event-specific JSON additionalContext, no permissionDecision. Error advice uses the same channel. Preserve recognizer and its warning-only decisions; selftests assert stdout semantics as well as rc/stderr.
- Python claim-check: hoist escaped expression literal into mark variable; retain existing selftests. Actual Python 3.11 is reviewer-reported unless directly available here.
- Claude wiring: fingerprint-scoped commands in root/PROME/user settings; merge into existing settings, preserve unrelated configuration and clock/validator timeouts. Keep a conditional legacy subject guard when effective hooksPath or executable native hook coverage is unverified, so another clone's custom hook configuration does not lose existing protection. User-level installation on current host only with backup; other host not claimed installed. Same commands at user/project scopes need merge/deduplication validation, checked by a launch probe if executable runtime permits. No research session launches.
- GitHub: inspect existing rules and install master protection denying force updates/deletion, covering admins, linear-history OFF, retaining direct fast-forward pushes. No required PR/checks/reviews or bypass list added. Surface plan/permission limitations rather than weaken settings. Read back actual protection after successful mutation.

## Neighbour acceptance

1. Ordinary: short/exact100/101 -m and -F; multiline paragraph and body boundary; normal/new-branch/fast-forward pushes; clean installer idempotence; claim/pipeline selftests.
2. Overlap: comment-leading verbatim/default message; multiline indentation; decomposed NFC/C locale; existing custom and default executable hooks; inherited settings with identical commands.
3. Wrong owner: dispatcher inert in unrelated repo/no Git repo; no changes to domain paths, unrelated user settings or other machine.
4. Missing information: message missing/unreadable/invalid UTF-8, interpreter missing, unknown ancestry, unshallow failing or still shallow, install config failure. Permission payload has no approval decision.
5. Concurrent activity: installer config-lock failure/race explicitly reported; pre-push server race covered by server protection/ordinary no-force rejection; tests never mutate live Git refs. No new board consumption or detached-HEAD repair.

## Validation and completion

Run meaningful fixtures in disposable repositories under ResourceWarning-as-error; current code is copied into fixtures. Record IMPLEMENTED, TESTED, INDEPENDENTLY VERIFIED and STILL UNRESOLVED separately. Plan/result independent reviews are required by PROME/CLAUDE.md for this broad shared-control repair; helper is read-only and is not a domain desk launch. No change is called independently verified from author tests alone.
