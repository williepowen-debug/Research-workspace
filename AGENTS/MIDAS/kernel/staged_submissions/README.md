# MIDAS — STAGED KERNEL SUBMISSIONS (Increment 2). NOT SUBMITTED, NOT LIVE COMMANDS.

**Authored 2026-08-27 evening ET / 2026-08-28 02:05Z.** Byte-frozen MIDAS-06 command
candidates. `submitted_at` = `2026-08-28T02:05:10.565544Z` on all three.
**Source commit pinned in every `native_ref`: `80c6346c58166a13839fc246b87a51eef8bf86f1`.**

⛔ **A command exists only at `AGENTS/MIDAS/outbox/kernel/submissions/` (C1 contract).**
This directory is a planning staging area so the activation document can pin exact
sha256 values **before** Will rules the window, without creating live commands.
**Root carve-out ④ activates at the ruling and is scoped to the ruled window bounds**
(`GATE_C_C7_RUNBOOK.md` § "Carve-out-④ successor scope"), so nothing here is copied to
the submission path or committed there until then — that copy is runbook step 1, in-window.
Nothing here is readable by any live-shadow mode: `load_live_submissions` reads only the
activation-pinned `AGENTS/` submission paths from a named commit.

## The three commands (activation 1 — exactly the 3-command cap)

| File | Type | sha256 | bytes |
|---|---|---|---|
| `CMD-019306a1-4c00-7000-8000-00000000006a.json` | RegisterQuestion | `20b200ff2d01d62389e3b708cb7f12481606aa7b7017adc48168cd36e5a9037c` | 6452 |
| `CMD-019306a1-4c00-7000-8000-00000000006b.json` | SubmitForecast (←…6a) | `9ccbde6d4e334b462a0d9ca26157efed6f79b3b046a8ad160a0646593a8fee0d` | 2986 |
| `CMD-019306a1-4c00-7000-8000-00000000006c.json` | CloseQuestion (←…6a) | `6dace933866f2126b6fd9ad5a29e9f6097bf6415941d99718d4fcbf05854e32a` | 1192 |

`question_id` `Q-019306a1-4c00-7000-8000-00000000006a` · `forecast_id` `F-019306a1-…-6a` ·
`correlation_id` `gate-c-midas-06-increment2`.
**Activation 2 (Monday, post-publication): `ProposeResolution` + `VerifyResolution`.**
`ProposeResolution` is **deliberately not authored yet** — its `outcome_value` and
`resolution_evidence_refs` are unknowable until the 2026-08-28 DFII10 observation
publishes Mon 2026-08-31 ~16:15 ET. Authoring it tonight would mean inventing a reading.

## Named independent verifier: **RED**

`independent_verifier_actor_id: "RED"` — replaces the grants-draft sentinel
`TO-BE-NAMED-BY-MIDAS-AUTHORING--FAILS-CLOSED-UNTIL-REPLACED`. RED is a registered actor,
is not MIDAS (proposer ≠ verifier), is the fleet's QC/reviewer seat, and is the
precedent from SAM-33. PROME recomputes the grants hash and pins it in the resolution
activation. **PROME is deliberately NOT named** — it is the acceptance custodian, and
custodian-as-verifier would collapse two separations into one actor.

## Native companion — why it exists

`AGENTS/MIDAS/workbook/MIDAS-06_KERNEL_NATIVE_COMPANION.json`, pointers `/question`
`/forecast` `/close`, cited as a second `native_refs` entry beside the `TSV_RECORD_ID`
entry, per the runbook's **Submission authoring requirement**. It is not decoration:
`MATERIAL_FIELDS` reconciliation is keyed by **payload field name**, and a TSV row
supplies only its own column names (`id`, `made`, `channel`, …), so a bare TSV ref
matches zero material fields and fails `NATIVE_RECORD_MISMATCH` on every one.

## Verification run at authoring (re-runnable)

- `core.validate_command` → **OK on all three** (no findings).
- `native.verify_native_references` against a real git boundary → **no findings on all
  three**; every material field reconciles to the pinned native bytes.

## The frozen letter governs

MIDAS-06 is under Will's row-68 **NO EDIT** ruling. This question is a faithful binary
projection of a **four-branch** letter and changes none of its terms. The mapping is
stated in `resolution_rule`: **(a)→YES · (b)→NO · (c)→AMBIGUOUS · (d)→AMBIGUOUS.**
⚠️ `forecast_family` is a schema **const** (`BINARY_PROBABILITY`), so the probability
`0.45` is **P(branch (a)) as recorded in the letter on 2026-08-07** — the letter's own
registered distribution is P(a)~0.45 / P(b)~0.20 / P(c)~0.15 / P(d)~0.20, i.e.
**P(NO)=0.20, NOT 1−0.45.** Any two-outcome Brier/log score against this row is wrong.
`information_as_of` is **2026-08-07**, the registration date, because the figure is
transcribed from the frozen letter and was **not** computed tonight — by 8/27 gold had
already cleared the branch-(a) gold leg by 5.93% and DFII10 stood 6bp under the binding
leg, so a probability formed tonight would be a nowcast wearing a forecast's costume.
