# REGINALD — Gate C Increment 2 STAGED SUBMISSIONS · NOT SUBMITTED, NOT LIVE COMMANDS

**Authored:** 2026-08-27, REGINALD, in its own lane, on PROME's prep ask.
**Status:** BYTE-FROZEN and committed here for pinning. ⛔ **Nothing here is a live command.**

## ⛔ Why these are NOT in `outbox/kernel/submissions/`

Root `CLAUDE.md` **carve-out ④** permits a domain agent to commit a canonical command at
`AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json` **only after Will approves and
activates a bounded Gate C pilot window.** That has not happened for Increment 2. Copying
these bytes to that path is **runbook step 1, in-window** — not prep. This directory is a
planning staging area so the activation document can pin exact sha256 values *before* the
ruling without creating live commands. Same posture as `KERNEL/rehearsals/c7_staged_submissions/`.

**A command exists only at the submission path (C1 contract), and REGINALD authors and
commits its own file there itself, in-window.**

## The pins

**Source commit for every `native_ref`:** `fb108a9f62956a858ffd93427a849d69d59ba331`
**`submitted_at` (all four):** `2026-08-27T20:52:40.008185Z`
**Byte convention:** UTF-8, keys sorted, compact separators (`,` `:`), single trailing `\n` — matching the C7 rehearsal files.

| Command file | Type | Pred | Bytes | sha256 |
|---|---|---|---:|---|
| `CMD-019306b4-1a00-7000-8000-0000000000a1.json` | RegisterQuestion | REG-01 | 7215 | `c702ec942ae5db162a02a7f14ee4b1f64e7a61886a1bdf3fc9ec9fc0131ea02a` |
| `CMD-019306b4-1a00-7000-8000-0000000000a2.json` | SubmitForecast | REG-01 | 2524 | `81d2a01db60910cb88ffb79f403c536058c8da29aa2705769746d4ac477e52fd` |
| `CMD-019306b4-1a00-7000-8000-0000000000a6.json` | RegisterQuestion | REG-06 | 7979 | `bef71f7a000419d7d57d4d7bc92f9f6213bd8ce336d58edb9d722fccf28b7d9c` |
| `CMD-019306b4-1a00-7000-8000-0000000000a7.json` | SubmitForecast | REG-06 | 3153 | `f6334b33b2fcfbf98f13211ad6d80744bc26841a6705065d1ca16c81be068f1c` |

**Companions** (the structured material fields; the 10-column TSV cannot hold them):
`AGENTS/REGINALD/kernel/REG-01_KERNEL_NATIVE_COMPANION.json` · `..._REG-06_...json`

## Verification actually run (not asserted)

- **Schema shape** — all four: required top-level fields present, no extras, `command_id` matches the UUIDv7 pattern, `command_type` in enum, payload satisfies `question.schema.json` / `forecast.schema.json` `required` with **zero extra properties**. PASS ×4.
- **`KERNEL/tools/native.verify_native_references`** against `SubprocessGitBoundary` — the Kernel's own code, not a reimplementation. **PASS ×4, zero findings**: every `native_ref` resolves at the pinned commit, every `raw_record_sha256` matches the selected bytes, and **every MATERIAL field in each payload matches the cited native records**.
- Hashes were computed with the Kernel's own `_tsv_select` / `_json_pointer_select`, so byte selection cannot diverge from what acceptance will do.

## Selection — 2 of 4 open rows, and the two rejections are the honest part

**SUBMITTED:**

- **REG-01** — *Office CMBS DQ stays >10% through 2026*, **0.90**, resolves `FIXED_DEADLINE` 2027-01-01. Verifier **CREED** (owns the series). Crisp, binary, instrumented (`OFFICE-CMBS-DQ-TREPP`), with the three substitution traps written into `resolution_rule`: not Fitch overall, not special servicing, not the all-property rate.
- **REG-06** — *at least one of EGBN/WAL completes a capital raise*, **0.10**, resolves `FIXED_DEADLINE` 2027-01-01. Verifier **RED**. Binary, EDGAR-verifiable, with five exclusion categories defined so an ordinary financing or an M&A share issuance cannot fake a distress signal.

⚠️ **REG-06's confidence was deliberately re-marked 50% → 10% in `3ae52ac59368a0a386fc4d578af4a929e73fa538`, BEFORE this file was authored.** Reason, and it is a perimeter fact rather than a preference: **`AmendForecast` and `WithdrawForecast` are explicitly OUT of Increment 2**, so anything submitted is frozen with **no in-perimeter correction path**. Submitting a probability I already believed stale would have been the exact failure the ledger exists to prevent. The TSV cell and the payload now both read 10%.

**NOT SUBMITTED — deliberately, per PROME's "do not manufacture one":**

- ⛔ **REG-03** (*"$936B maturity wall forces recognition wave"*, 70%) — **not resolvable as written.** *"Forces a recognition wave"* names no metric, no bar and no instrument: it is a **threshold FAMILY, not a threshold** — the same defect BOND ruled `VX-BND-18`'s escalation leg ungradeable for on 8/23, and which I corrected on my own surfaces today. It also carries an **unreconciled three-way figure discrepancy** flagged in its own Notes ($936B here vs $875B on STATUS vs CREED's CMBS-only >$100B / $76.6B-hard). Registering it would require inventing a resolution condition the desk has never held. **Re-spec first; then it is a candidate.**
- ⛔ **REG-07** (*SSB NPL migration >0.5% from substandard*, 68%) — **two blockers.** (i) The metric is **ambiguous between a rate and a level**: the claim says *migration >0.5%* while its own invalidation says *"NPLs stay <0.3%"* — different objects, and registering it would freeze the ambiguity. (ii) Its confidence is flagged **`OVER-CONFIDENT-PENDING-REMARK`** as of 2026-08-27 with the Q2 leg fully in and disconfirming; unlike REG-06 it has a **pending data event** (the Q3 print), so the re-mark belongs there, on purpose, with the data. **Candidate for a later increment after the Q3 print and a metric re-spec.**

## ⚠️ One judgment call flagged for RED/PROME rather than decided quietly

**REG-01's `opens_at` is `2026-02-23` — before submission.** The C7 precedent does the same (SAM-33 opens 2026-06-30, submitted 2026-08-27), and I read the no-backfill rule as *"already-resolved history does not enter"*: **REG-01 is OPEN, unresolved, and its outcome is genuinely undetermined until 2026-12-31.** REG-06 opens `2026-07-01`, the true start of its H2 window. **If Increment 2 wants `opens_at ≥ ruling date`, REG-01 needs re-cutting and I would rather be told than assume.**

## Provenance of the numbers

Both probabilities are the desk's registered confidences at the pinned commit — `90%` and `10%` read straight out of `PREDICTIONS.tsv`, verified in-place by the selector above. **No figure here was created for the Kernel.**
