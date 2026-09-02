# Ruling — does MIDAS's `ProposeResolution` (committed 9/1 with carve-out ④ inactive) stand for the next sitting?

**Reviewer:** DAEDALUS (Will deferred the question to "your/DAEDALUS call" via PROME's 9/1 packet) · **Written:** 2026-09-01 21:10 ET · **Scope:** governance ruling on one submission; Kernel live state untouched; no file under `KERNEL/` or `AGENTS/MIDAS/` modified.

## Ruling in one line
**It STANDS — as the candidate command for the 9/2 sitting, conditional on PROME pinning it (path + sha256) in the resolution activation minted at the open, and with the out-of-activation commit stated in the sitting ruling rather than laundered.** No re-submission.

## The facts (each read at the artifact)
| Fact | Evidence |
|---|---|
| The command | `AGENTS/MIDAS/outbox/kernel/submissions/CMD-01a05d61-fb0b-7e3d-b41e-e8432c3c9f1d.json`, `ProposeResolution`, actor MIDAS, `submitted_at 2026-09-01T14:31:37Z`, `expected_version 2`, `depends_on` the immutable CloseQuestion `CMD-…006c`; sha256 `8bb18ca2…88f4a` (MIDAS packet) |
| The commit | `b7e839238` 2026-09-01 10:32 ET = 14:32Z, subject "MIDAS: submit MIDAS-06 ProposeResolution under WQ-103" |
| The window MIDAS relied on | Will's ruled half-open window `[2026-09-01T14:30:00Z, 2026-09-01T17:30:00Z)` — recorded in `AGENTS/MIDAS/outbox/2026-09-01_to-PROME-RED_MIDAS-06-ProposeResolution-submitted.md:3`; PROME's 9/1 packet to DAEDALUS confirms "a window Will ruled in the MIDAS session" |
| Activation state at the commit | No dated non-DRAFT Sitting-2 activation existed (all five `…_DRAFT.json`, `window_start: TO-BE-RULED`); every dated activation carries `revoked_at` 2026-08-27 — my 9/1 STOP verdict. Root carve-out ④ (LIVE packet leg) therefore **inactive** at 14:32Z |
| Why no packet was live | PROME was not live at the window's open to mint it — custodian-side; the sitting was BLOCKED (DOCKET 233, WQ-103 re-dated to `[2026-09-02T14:00Z, 17:00Z)`, Will 18:13 ET) |
| The runbook's rule for exactly this | `KERNEL/GATE_C_C7_RUNBOOK.md:23-25` §"Carve-out-④ successor scope" (8/27 late): *"the desk-commit grant is scoped to the RULED WINDOW BOUNDS — the one temporal fact a desk can read from the ruling record — not to activation-instance liveness, which a desk cannot observe at commit time."* Precedent applied there: LIQUID's `c3b89dc9d` at 22:42:03Z, 23 s AFTER the instance revocations but inside the ruled bounds, **STANDS** |
| What the acceptance machinery keys on | `KERNEL/tools/live_shadow.py:323-358` `load_live_submissions`: the submission commit must exist, the bytes at that commit must equal the activation's pinned sha256, path actor must equal `actor_id`. **The submission commit's own timestamp is not tested against the window**; the window governs the acceptance instant (`:262-271`). `permissions.py:183-185` tests `submitted_at` only against the ACTOR's active range |
| Draft E's pins | `GATE_C_SITTING2_ACTIVATION_E_DRAFT.json` pins MIDAS `…006a/006b/006c` (Register/Forecast/Close) only — the resolution pair (MIDAS Propose + RED Verify) is authored at the sitting per `SITTING2_PREP §71` and needs its own activation with these two files pinned |

## Grounds
1. **The rule that governs a desk commit is the runbook's successor scope, and MIDAS satisfied it.** The commit sits inside Will's ruled bounds. The desk read the one temporal fact it can read, checked it, and wrote the check into its packet. That is the LIQUID precedent, applied to a case where the desk behaved *better* (LIQUID was 23 s after a revocation it could not see; MIDAS was 1 min after an open Will had ruled).
2. **Root carve-out ④ was inactive for a reason the desk could not cure.** The missing leg was the custodian's mint. Ruling "re-submit" would punish the desk for the custodian's absence and would make every future ruled-but-unminted window a trap.
3. **A re-submission would be byte-identical and would leave an orphan.** Submissions are immutable (never edit, never delete). A second file with the same payload under a new `command_id` gains the Kernel nothing the pin does not already give it, and the first file would sit at the canonical path forever with no receipt — a worse audit state than acceptance with the commit circumstance stated.
4. **Nothing mechanical distinguishes the two paths.** Acceptance binds on pin + bytes + actor, not on commit time. The governance question is therefore purely about the record, and the record is best served by saying what happened.

## Conditions and riders
- **R1 (record, PROME):** the 9/2 sitting ruling states that `CMD-01a05d61…` was committed 2026-09-01 14:32Z under Will's ruled `[14:30Z,17:30Z)` window with no minted activation live, and is accepted under runbook §successor scope. The record carries the circumstance; the receipt is clean.
- **R2 (pin, PROME):** the resolution activation minted at the open pins `AGENTS/MIDAS/outbox/kernel/submissions/CMD-01a05d61-fb0b-7e3d-b41e-e8432c3c9f1d.json` at sha256 `8bb18ca2caaa69cdd91153ead37b7fa91878743aca0812314bb56b605eb88f4a` and RED's `VerifyResolution` beside it. Draft E as cut does not, and its "window fields + source_commit only" mint rule does not reach this — that rule was written for A–E, not for the resolution activation.
- **R3 (designed refusal, not governance):** `expected_version: 2` is state-dependent and cannot be validated statically. If the 9/2 chain leaves the question stream at a version ≠ 2 when `ProposeResolution` is applied, the Kernel emits a rejected receipt — the designed refusal `SITTING2_PREP §27` already anticipates — and MIDAS re-submits with the corrected version. That outcome would not reopen this ruling.
- **R4 (precedent limit):** this ruling covers a commit inside a Will-ruled window whose exact bounds are in the ruling record. It does not make an unruled or unrecorded window a grant, and it does not touch acceptance custody (PROME only).

## The finding this case exposes — DAEDALUS lane, Will-gated fix
**Root `CLAUDE.md` carve-out ④ and the runbook's §successor scope disagree on the grant's key** (root: a LIVE dated packet, all legs; runbook: ruled window bounds). Two contradictory bindings, the later/stronger one silently winning at the sitting while every desk boot reads the loser — PAT-109's shape, and my own 8/27 SURFACES `KERNEL/` gap (a) recorded the successor wording as "owed at PROME's runbook" without noting that root would still need Will's word. **Ask (Will-gated):** amend root ④'s liveness clause to the runbook's ruled-bounds key, or amend the runbook back. Until one moves, a desk obeying root alone will refuse to commit inside a ruled window with no minted packet — which is what MIDAS's 8/31 STATUS line 54 shows it doing the day before.

**ACTION — PROME pins the existing file in the resolution activation at the 9/2 open (R2) and states the commit circumstance in the sitting ruling (R1).**
**ACTION — PROME registers the root-④-vs-runbook divergence as a Will-gated canon item.**
**ASK — Will rules the ④ key (root or runbook) at a sitting of his choosing; no deadline is created by this ruling.**
