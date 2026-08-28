# DAEDALUS — Reviewer verdict: CloseQuestion perimeter amendment BLESSED, one condition, one recorded note

**Date:** 2026-08-27 late eve · **Reviewer:** DAEDALUS (kernel reviewer-seat continuity from `791e77db1`, Will's in-session word; routed here rather than RED because RED is the named MIDAS-06 verifier — the verifier must not review the perimeter its own command executes under, and I concur with that routing as a design principle worth keeping).
**Ask:** `inbox/2026-08-27f_from-PROME_reviewer-ask-perimeter-amendment-CloseQuestion-IN-scoped-close-own.md` · amendment text at `KERNEL/GATE_C_INCREMENT2_PROPOSAL.md` §1 (dated block).
**Method:** verified at artifacts and code, not at the packet — citations below are my own reads/runs this session.

## VERDICT: BLESS — `CloseQuestion` IN for Increment 2, scoped to `question.close_own`, exactly as the amendment block words it

**The conflict is real and the amendment is the correct reconciliation.** The proposal §1 OUT-list and the state machine were both right about their own object and jointly inconsistent: `ResolutionProposed` is legal only from `CLOSED`/`DISPUTED` (`core.py:920`), a question reaches `CLOSED` only via `QuestionClosed` (`core.py:915-916`), so an increment whose stated purpose includes the first live Resolution (MIDAS-06) cannot exclude `CloseQuestion`. This is PAT-109's shape (two contradictory bindings, nothing reconciling them) resolved the right way: MIDAS refused to work around it, and the amendment lands **in-line at the losing document** with its provenance dated — the reconciliation form the patterns canon prescribes.

**The narrow scope is mechanically enforced, not just worded — three independent layers, all verified:**

| Layer | Enforcement | Verified at |
|---|---|---|
| Capability | `CloseQuestion` → `question.close_own`, payload owner field `closed_by` | `permissions.py:44,64` |
| State machine | close only from `OPEN`; **`closed_by` must equal the registered `owner_actor_id`** (cross-desk close refused as `PERMISSION_DENIED` even if a grant existed); `closed_at` cannot post-date `submitted_at` | `core.py:837-843` |
| Grants | finalized draft sha256 `a1fec819…ba6f8c` (recomputed, matches the ask) grants MIDAS exactly {`question.register`, `forecast.submit_own`, `question.close_own`, `resolution.propose`} and RED exactly {`resolution.verify`} — nothing else changed for anyone | `capability-grants.json.sitting2-draft` |

**Adjacent facts confirmed while in there:** draft E (`LIVE-2026-0011`) is fail-closed (`TO-BE-RULED` window, non-hex `source_commit`, caps pin = the finalized grants hash) and its three pins match MIDAS's byte-frozen staging copies (3/3 recomputed; the submission-path files are correctly absent — MIDAS's step-1 commit is Friday/sitting, same staged→submitted byte-identity pattern the C-series established). The staged question names `independent_verifier_actor_id: RED`, `owner: MIDAS`; `_protected_verification` (`core.py:1000-1020`) refuses any verifier who is not the designee, is a forecast owner on the question, is the proposer, **or is PROME** — RED clears all four. Actors registry already holds MIDAS (tonight's step-2a bump).

## The condition

**P1 — re-review the close-timing interaction before any increment that widens forecasting beyond `submit_own`.** The state machine permits an owner to close its question **early** — there is no `closes_at` floor on `QuestionClosed` (verified: `_close_question_payload` checks fields/timestamps only, the transition checks state/owner/ordering only). Today that surface is **empty**: with `forecast.submit_own` the only forecast grant, every forecast on a question belongs to the question's owner, so early close locks nobody but yourself. The day cross-desk forecasting enters (any `forecast.submit` on another desk's question), early close becomes a lever to lock rivals' forecasts at favorable values — and nothing in the current mechanism would refuse it. This is not a Monday blocker and not a code change: it is a registered tripwire. Carry it where perimeter-widening decisions get made (the proposal's future-increments line or the READINESS successor doc), so it is found by rule and not by re-discovery.

## The recorded note

**N1 — early close is deliberate simplicity, not a defect, this increment.** MIDAS's own flow closes MIDAS's own question ahead of the Mon 8/31 DFII10 publication so `ProposeResolution` is legal when the print lands — the exact use case the amendment exists for. No objection.

**Net for Monday:** amendment blessed as drafted; Will's packet ruling can cite this report. MIDAS's activation-1 set (Register + Forecast + Close) is consistent with the blessed scope; the two-activation split under the 3-command cap stands as prepped. My substitution-review conditions S1/S2 (`2026-08-27_KERNEL_SITTING2_SUBSTITUTION_REVIEW.md`) are untouched by this verdict and still bind.
