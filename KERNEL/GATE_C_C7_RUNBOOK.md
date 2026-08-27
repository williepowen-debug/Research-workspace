# Gate C C7 Pilot Runbook — the attended sitting, step by step

**Prepared:** 2026-08-27 (~16:00Z) · **Companion to:** `GATE_C_C7_ACTIVATION_PACKET_v2.md` · **State:** SETUP COMPLETE — waiting on Will's window ruling; nothing below step 0 runs before it.

## Frozen inputs (all pinned as of this document; re-verify hashes at step 0)

| Input | Value |
|---|---|
| Source commit | `1d9400425f7415083a9ffbd10964670bf255abf2` (verified present) |
| CMD-…033 RegisterQuestion | staged at `rehearsals/c7_staged_submissions/`, sha256 `71996c763e4d4150e4380814f476fe24513f148e335f832fc42f4eb5d7a7bbe2` |
| CMD-…034 SubmitForecast | staged, sha256 `2dd24caee3884198dd440224b209b50e9ab8a52821b170065b06e91b043797e2` |
| `KERNEL/policies/actors.json` | `48dbea3b449f69c47029210499c5182e7b6c97c5b5182dd67301ed0bc5da4db0` |
| `KERNEL/policies/capability-grants.json` | `57c76977cd6d2934b52928acee9786c4ddca90b381b265bbda5618cbba447b2c` |
| `KERNEL/policies/custody-policy.json` | `180c47ee39e494e7998c6039e6d9c43693c3099df76990f04faaab9243e9e849` |
| Event IDs | CMD-…033 → `EVT-019305f8-ec00-7000-8000-000000000033` · CMD-…034 → `EVT-019305f8-ec00-7000-8000-000000000034` |
| Writer | PROME (custody primary; RED dormant; no substitute activation) |
| Activation draft | `GATE_C_C7_ACTIVATION_DRAFT.json` — window fields read `TO-BE-RULED` and fail strict validation until Will's exact UTC bounds replace them |

## The sitting (Will present throughout; any stop condition on screen ⇒ stop, preserve, no disposition without Will)

0. **Preconditions:** Will's ruling recorded with exact half-open UTC window · clean tree (`git status`) · re-verify all six hashes above (`sha256sum`) · `date -u` inside the window at each subsequent step.
1. **SAM commits its commands (C1: the submitting agent authors and explicitly commits its own file):** SAM's session copies the two staged files byte-exact to `AGENTS/SAM/outbox/kernel/submissions/`, verifies both sha256 values, commits with the two explicit pathspecs only (carve-out ④, activated by the ruling). Record the commit SHA = `SUBMISSION_COMMIT`.
2. **PROME mints the activation document:** fill the draft's `window_start`/`window_end` with Will's exact ruled bounds, save as `KERNEL/GATE_C_C7_ACTIVATION_<date>.json`, commit explicit-path (custody record). Any hash drift between draft and live files at this step = stop.
3. **Preflight:** `python3 KERNEL/tools/live_shadow.py --activation <doc> --live-repository-root /home/willi/Research-workspace --submission-commit $SUBMISSION_COMMIT --preflight` — expect rc=0, no `UNKNOWN`, banner shows `LIVE_SHADOW_PREFLIGHT`.
4. **Record pre-apply HEAD** = `BASE`.
5. **Apply:** same invocation with `--apply` — expect exactly the two pinned events + four bannered views, explicit per-file staging paths printed, rc=0.
6. **Idempotent retry:** re-run `--apply` — byte-identical, zero new writes.
7. **Kernel commit (PROME, custody rules):** inspect the exact printed paths (`git status`), run `git_policy_check` additions-only + durable-result checks, then stage and commit ONLY the printed event/receipt/view paths, exact pathspecs. No push during the sitting except by Will's word.
8. **Verify:** `--check-views` (byte-identical PASS) · `--audit-additions --base $BASE --head HEAD` (PASS, protected paths additions-only).
9. **Close the window:** nothing further runs; Will words any push; C8 closeout packet drafted (results, receipts, burden per the pre-named C8 measures, discrepancies, stop dispositions) — **C8 reviewer = RED or DAEDALUS, never PROME** (ruled 8/26).

## Standing refusals that protect the sitting (no action needed, listed so their firing is recognized, not debugged)
Expired/not-yet-started window · root mismatch · any pin drift · writer ≠ custody primary · substitute active · non-canonical timestamp · unknown field set — each refuses BEFORE any write (212-test suite; RED-probed).
