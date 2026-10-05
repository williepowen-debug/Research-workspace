# Locks safeguards — implementation and deployment receipt, 2026-10-05

Authority: Will requested implementation after the consolidated v4 bundle review. Purpose: PROCESS, the explicitly requested fleet safeguard bundle. No research desk launched, no trade action, no boot/board-consumption default changed. The read-only independent reviewer required by repository governance is recorded in the acceptance file.

**IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED** for the corrected code. **INSTALLED** on the desktop and GitHub as detailed below. Laptop-local installation remains **UNKNOWN / NOT PERFORMED HERE**.

## Changes

- Native commit-msg checks the entire first paragraph, Unicode/NFC and locale-independent length. Read/decoding/Git cleanup/interpreter failures deny the commit with a diagnosis. Comments retained conservatively; editor comment stripping can still cause a false block.
- Native pre-push denies non-fast-forward updates/deletion and refuses unknown ancestry. It does not detect a force flag on a fast-forward push; client hooks remain bypassable with --no-verify.
- Shared installer validates executable hooks, preserves an existing conflicting hooksPath or any active default executable hook, and is idempotent. Safe-push now resolves the root from desk directories and aborts if installation is unverified. Installer lock failures are reported; a noncooperating concurrent config writer remains a race, not claimed prevented.
- Banner captures unshallow failures and rechecks shallow state; unreliable graph counts become unknown instead of a false all-clear. It does not change checkout/environment state.
- Pipeline warning/error JSON carries additionalContext with no permissionDecision. Warning-only behavior is unchanged. Two stale selftest expectations were reconciled with the current shared recognizer, which was not modified: the original HEAD wrapper/recognizer baseline already failed those two cases (34/36), verified separately in `/tmp/pipeline-baseline-8pm66hhn`.
- Claim-check removes the pre-3.12 f-string backslash expression. Existing weekday selftests unchanged.
- Root/PROME/user Claude commands are fingerprint-scoped. Conditional legacy subject inspection remains available in clones whose native hook installation is unverified; the legacy script is retained. Clock timeout 5 and validator timeout 90 retained. User settings merge preserves unrelated configuration and repairs matching fleet-owned hook metadata with an exact backup.

## Validation

- `python3 -W error::ResourceWarning PROME/tools/tests/test_locks_safeguards.py`: **14 tests passed**, disposable fixture snapshots only. Includes the independent reviewer's active default prepare-commit-msg and stale timeout/async counterexamples.
- Pipeline selftest **36/36** and weekday claim-check selftest **36/36** passed locally on Python 3.12.3. Direct 3.11.15 compatibility evidence is supplied by the original reviewer, not a local interpreter run.
- Shell syntax and `git diff --check` passed.
- Read-only reviewer completed plan, result and narrow corrected-installer verification; no consequential code blockers remain. Acceptance: `PROME/tools/tests/ACCEPTANCE_LOCKS_2026-10-05.md`, reads 3.

## Deployment

- Host verified as `DESKTOP-BC6EF81`. Effective local Git config readback: `.git/config`, `core.hooksPath=scripts/githooks`; no active default hooks existed before installation.
- Desktop `~/.claude/settings.json` installed and second run reported already installed. Exact original backup: `/home/willi/.claude/settings.json.fleet-backup-1d56588c582047bcb1825c2c2dc9a62a`. Original preferences and other top-level keys retained.
- Actual tool-free Claude launch probes in an isolated fixture: agent-subdirectory, unrelated repo and repo-root all returned rc 0 / PROBE_OK. Banner executed once from the desk, zero times in unrelated repo, and once from root despite identical user/project command entries. No real desk session or owner files used. Evidence: `/tmp/locks-launch-probe-kgpgodl5/desk-unrelated-receipt.json`, `receipt.json`, `*.stdout`; initial sandbox probes timed out, then the permitted normal-access probes succeeded.
- GitHub baseline: master unprotected (404), rulesets empty, admin capability available. Applied and fresh-read verified: enforce_admins true; allow_force_pushes false; allow_deletions false; required_linear_history false; required status checks/reviews/restrictions null. Direct fast-forward pushes retained. No dangerous test push attempted against the real master branch. Repository administrators can still change policy.

Primary API contract: [GitHub branch protection](https://docs.github.com/en/rest/branches/branch-protection). Claude decision contract: [hook decision control](https://code.claude.com/docs/en/hooks#pretooluse-decision-control).

## Other machine

After pulling these changes on the laptop, from repository root:

```bash
bash scripts/install-git-hooks.sh
python3 scripts/install-claude-hooks.py
```

The server protection already applies to both machines. Local settings/configuration do not travel via Git. Existing unrelated boot state and earlier review records are excluded from the implementation commit; no full session closeout is claimed by this receipt.

## Subsequent verification supplied by Will, 2026-10-05

Will pasted the reviewer's report of testing a clean checkout of implementation commit `2a72c60bc`, rather than this receipt. Reviewer reports: all 14 safeguard tests pass; claim-check on Python 3.11 passes 36/36; pipeline selftest passes 36/36; native install is idempotent; subject boundaries/multiline/comment/multibyte cases behave as intended; missing message/no argument refused; push ancestry/deletion cases behave as intended; advisory payload has no permissionDecision; all settings commands are scoped and retain conditional fallback. This supplies clean-checkout Python 3.11 evidence for the actual committed implementation; it is reviewer-performed, not a local 3.11 run. No new repair or commissioned review round follows from this sourced receipt.

Reviewer confirms the agreed editor-comment limitation and warns to install on the laptop immediately after pulling: a custom hooksPath or active default hook deliberately prevents installation and makes safe-push abort until the conflict is resolved. Laptop configuration remains UNKNOWN from this desktop.

Reviewer cannot inspect GitHub settings. PROME therefore obtained another direct GET of `repos/williepowen-debug/Research-workspace/branches/master/protection` using the authenticated GitHub CLI. Observed projection:

```json
{"deletions":false,"enforce_admins":true,"force_pushes":false,"linear_history":false,"required_pull_request_reviews":null,"required_status_checks":null,"restrictions":null}
```

This is settings readback, not a prohibited test push. No code, local configuration or server settings changed during this subsequent verification.
