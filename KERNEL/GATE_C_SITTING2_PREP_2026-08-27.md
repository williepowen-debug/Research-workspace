# Gate C Sitting 2 prep — Monday 2026-08-31 post-16:15 ET

**Prepared:** 2026-08-27 ~20:1x ET by PROME (custodian; builder — NOT reviewer), on Will's in-session word *"PROME-side kernel prep fire."* **Canonical plan:** `PROME/DOCKET.tsv` row 233 (the pause disposition's precondition list). **This document:** the executed PROME-side prep + the precondition scoreboard + what remains and whose it is. Nothing here processes a real record or writes a live result — planning documents and fixture-only runs throughout.

## 0. Precondition scoreboard (row 233's ①–⑦, as of this document)

| # | Precondition | State | Whose move |
|---|---|---|---|
| ① | Reviewer blessing of the **substitution rule** (corrected CREED 111-116 + LIQUID pair are NEW files exceeding R3's subset-only delta baseline) | **✅ DISCHARGED 2026-08-27 ~21:44 — DAEDALUS ran the review as NAMED SUBSTITUTE on Will's in-session word (*"can you review KERNEL now?"*, recorded in the report header; seat eligibility = the 8/26 "RED or DAEDALUS, never PROME" ruling). Substitution rule BLESSED with the rule stated precisely + TWO CONDITIONS: **S1** — every future refused→corrected substitution gets a machine-produced per-pair field diff IN the sitting transcript (discharged for THIS set by the report's own diffs); **S2** — a superseded command_id appearing in any future activation draft is a STOP (supersession map in the report §1; 0004/0006 stay never-reused). Also: LIQUID 23s timing commit STANDS as-is (§4 consumed — rule-executability defect, successor wording owed, see runbook §Carve-out-④ successor scope) · F3 ENDORSED, suite 212 re-run by reviewer · 12/12 pins + 16/16 native refs independently re-derived. Report: `AGENTS/DAEDALUS/reports/2026-08-27_KERNEL_SITTING2_SUBSTITUTION_REVIEW.md` (`791e77db1`); RED stand-down packet in its inbox | Done — PROME verified at the artifact ~21:5x (rule-2 pass: commit real, packet delivered, evidence table reconciles with prep §3) |
| ② | Resolution-family grants bump | **DRAFTED, fails closed** — `KERNEL/policies/capability-grants.json.sitting2-draft` (sha256 `e27c15fb…ac372` at cut; recompute after finalization). See §2 for the `question.close_own` catch and the verifier sentinel | PROME finalizes after MIDAS authors (verifier name); lands at the sitting under Will's activation |
| ③ | F3 fixture answer | **ANSWERED at fixture level** — §1 below | Done; reviewer may endorse |
| ④ | Companion runbook SENTENCE | **DONE** — `GATE_C_C7_RUNBOOK.md` §Submission authoring requirement (2026-08-27 evening edit) | Done |
| ⑤ | MIDAS authors its commands | **WAITING on MIDAS's boot** — packet confirmed in its inbox (`2026-08-27_from-PROME_kernel-increment-2-is-GO…`); MIDAS is on Will's Friday spawn slate | Will (spawn) → MIDAS |
| ⑥ | Fresh Will-ruled window | **AT THE SITTING** | Will |
| ⑦ | REG-01 `opens_at` backdating | **RESOLVED 8/27 evening** — was already BLESSED in RED's Increment-2 review §6.3 with the discriminator: *"a question is INELIGIBLE iff its resolution condition is already satisfied or its outcome already knowable at submission — attested by the submitter."* REG-01 passes; no re-cut. (The question had been re-raised because the answer lived on a third surface — packet §0 + RED report — while the ruling record and transcript were the surfaces grepped.) | Done |

## 1. F3 — ANSWERED: a mismatched VerifyResolution is REFUSED, and the refusal is itself durably recorded

**Question (packet §0):** does acceptance REFUSE a `VerifyResolution` whose `verified_outcome_value` differs from the proposed value, or RECORD the mismatch?

**Answer, from a real fixture run (not a grep):**

- The suite already carries the exact fixture: `KERNEL/tests/test_lifecycle.py::test_verification_disagreement_must_use_dispute` — register → close → propose YES → verify with `verified_outcome_value: NO`. **Re-run live 2026-08-27 evening: OK.** The outcome document carries `reason_code: TRANSITION_FORBIDDEN` with the message **"disagreement must use DisputeResolution"** (`KERNEL/tools/core.py:872-874`).
- **No `ResolutionVerified` event is written; the question stays `RESOLUTION_PROPOSED`.** The refusal is not silent: the writer constructs a durable **REJECTED receipt** (`writer.py::build_rejected_receipt`, `command_result: "REJECTED"` + the reason code) — in live shadow that receipt lands additions-only at `KERNEL/audit/commands/`. So the mismatch **is** recorded — as a refusal receipt, never as acceptance.
- **The sanctioned disagreement path is `DisputeResolution`** (→ `DISPUTED`), from which a fresh `ProposeResolution` is legal — also fixture-covered (`test_dispute_requires_reproposal_before_verification`, and the dispute path requires matching `resolution_id`).
- **Sitting consequence:** if Monday's verifier disagrees with MIDAS's proposed MIDAS-06 outcome, the sitting sees a REJECTED receipt on screen — that is a **designed refusal, not a stop-condition defect**; the disposition is a `DisputeResolution` command (which is OUTSIDE the currently drafted command set, so a live disagreement = pause-and-rule, exactly like tonight's stops).

## 2. Grants draft (②) — what it adds, and the catch caught at draft time

`capability-grants.json.sitting2-draft` = the live grants (Increment-2 bumps landed 8/27, live hash `6e73c29e…60de` verified == draft) **plus**:

- **MIDAS:** `question.register` · `forecast.submit_own` · **`question.close_own`** · `resolution.propose`
- **Verifier sentinel:** `resolution.verify` granted to actor `TO-BE-NAMED-BY-MIDAS-AUTHORING--FAILS-CLOSED-UNTIL-REPLACED` — **proven to fail closed** against the live actors registry (`PermissionRegistry.from_documents` → `CAPABILITY_REGISTRY_INVALID: unknown actor_id`, run 8/27 evening). Replace with the `independent_verifier_actor_id` MIDAS names at authoring; recompute the file hash; pin that hash in the resolution activation.

**The `question.close_own` catch (F1-class, caught in prep instead of live):** `ProposeResolution` is legal only from state `CLOSED` or `DISPUTED` (`core.py:857-858`), and a question reaches `CLOSED` only via a `QuestionClosed` event — i.e. MIDAS's Monday flow structurally includes a **`CloseQuestion` command** before `ProposeResolution`, and `CloseQuestion` requires `question.close_own` (`permissions.py` COMMAND_PERMISSIONS). That grant was on nobody's Monday list. It is in the draft now. **Consequence for MIDAS's authoring:** the MIDAS-06 command set is Register → (Forecast) → **Close** → Propose → Verify — 4-5 commands, i.e. **two activations** under the 3-command cap.

## 3. Activation drafts (the Increment-2 book, re-cut per the mid-sitting ruling's R1-R4)

Four drafts cut 8/27 evening, **generated programmatically from the on-disk submission bytes** (sha256s recomputed at generation, not transcribed): `GATE_C_SITTING2_ACTIVATION_{A,B,C,D}_DRAFT.json`.

| Draft | activation_id | Commands | Notes |
|---|---|---|---|
| A | LIVE-2026-0007 | CREED 111 (Q) · 112 (F←111) · 113 (Q) | corrected set, companions pinned inside the command files |
| B | LIVE-2026-0008 | CREED 114 (F←**113, cross-activation**) · 115 (Q) · 116 (F←115) | R4's cross-activation dependency first-live-test now lives at B's 114←113 |
| C | LIVE-2026-0009 | LIQUID Q (…2ec64473) · LIQUID F (…c3af5d65) · REG a1 (Q) | LIQUID pair = corrected files (LF fix) |
| D | LIVE-2026-0010 | REG a2 (F←**a1, cross-activation**) · a6 (Q) · a7 (F←a6) | |

- **Fail-closed state:** `window_start`/`window_end` = `TO-BE-RULED`, `source_commit` = `TO-BE-RECUT-AT-MINT` (non-hex — cannot validate). Mint-time byte-diff discipline vs these drafts = the two window fields + `source_commit`, nothing else (F2 rider).
- **Policy pins:** current live `actors.json` `ad16ca28…aa20f` + live grants `6e73c29e…60de` for A-D (submission-family commands need no new grants). The **resolution activation(s)** (E, and F if the verify rides separately) pin the finalized sitting2 grants hash instead — cut after MIDAS authors; ids LIVE-2026-0011+ reserved.
- **Id hygiene:** tonight consumed 0002/0003/0005 (all affirmatively revoked 22:41:40Z); 0004/0006 were ruled-named but never minted — **never reused regardless**; Monday starts at 0007.
- **R1-R4 carry forward as ruled:** four distinct ids, four affirmative closes (R1) · identical policy pins across A-D, divergence = STOP (R2) · per-activation delta = command subset + activation_id + event_ids subset + source_commit re-cut ONLY (R3 — **the corrected files EXCEED this baseline, which is exactly precondition ①'s blessing ask**) · a dependency refusal at a cross-activation edge is a HELD SITTING, not a reshuffle (R4).

## 4. Step-1 state: ALREADY DONE for all twelve — verified at the bytes

All 12 corrected commands **already sit at their C1 submission paths, byte-identical to their frozen staging copies** (PROME diff-verified 8/27 evening, all 12 `identical`):

- CREED 111-116: outbox commit `8dc211f94` at **22:38:23Z — in-window** (window [21:45, 23:45Z), pre-revocation).
- REGINALD a1/a2/a6/a7: outbox commit `e4a51fb35` at 22:07:14Z — in-window; REGINALD independently re-verified byte-intact at its 8/27 boot (its packet `2026-08-27e`).
- LIQUID corrected pair: outbox commit `c3b89dc9d` at **22:42:03Z — 23 seconds AFTER the 22:41:40Z revocations** (inside the ruled window bounds, after the instances were revoked). ⚠️ **Flagged for the reviewer, not adjudicated here:** the files are inert (nothing accepts a command without a future activation; the ledger accepted zero events tonight) and byte-identical to their reviewed staging copies — but the commit's timing relative to the affirmative close belongs in the reviewer's read of carve-out ④'s condition. Old superseded files (CREED 101-106, LIQUID …01a044fc pair) also remain at the submission paths as immutable history; **no Monday activation references them.**

**Material simplification if the reviewer blesses the substitution:** Monday's runbook step 1 (desk commits) is already satisfied for the Increment-2 book — CREED/LIQUID/REGINALD need not attend the sitting; only MIDAS's own step-1 commit (its commands, at its Friday boot or at the sitting) remains.

## 5. What remains, and whose it is

1. ~~**RED (or DAEDALUS):** bless the substitution rule (①) + the LIQUID timing note (§4)~~ **✅ DONE 8/27 ~21:44 — DAEDALUS as named substitute (scoreboard ①); S2 stop-check rides step 2 of the runbook at mint.**
2. **Will, Friday:** spawn MIDAS (⑤ — authors commands + names the verifier). *(RED's Friday spawn is no longer kernel-critical — its kernel leg is discharged and a stand-down packet sits in its inbox; RED spawns on its own docket's merits.)*
3. **PROME, after MIDAS authors:** finalize the grants draft (replace the sentinel, recompute hash), cut activation drafts E(/F) for the MIDAS set + resolution pair, re-point `authorization_ref`s if a fresh Monday packet is cut.
4. **Will, Monday post-16:15:** the window, in his words, canonical form — then runbook steps 0-9 per activation.
