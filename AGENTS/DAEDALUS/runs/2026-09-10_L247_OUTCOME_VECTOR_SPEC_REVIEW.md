# L247 — ADVERSARIAL REVIEW: `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md` (WQ-155 ③ option (a))

**Reviewer:** DAEDALUS (the 8/26 seat rule — DAEDALUS or RED, never PROME, who authored the draft) · **Date:** 2026-09-10 ~11:0x ET
**Subject:** `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md` DRAFT v0.1, §1–§6 plus the §9 declared residue
**Commission:** DOCKET L313 (due 9/12) · packet `AGENTS/DAEDALUS/inbox/2026-09-09_from-PROME_REVIEW-REQUEST-L247-…md` · gate = `KERNEL/GATE_C_C8_RULING_2026-09-02.md` § AMENDMENT (the five-item build-spec gate)
**Delivered:** 2 days early, so the 9/12 TOOLING/WIRING sitting is not the constraint.

---

## VERDICT — **FAIL (bounded remedy), 3 blocking findings**

The spec is well-built and answers all five gate items in order. The arithmetic holds, the K = 2 reduction holds, the carrier choice is right, and the rejected alternatives are named and correctly declined. **It fails on one structural point, not on craft:** the spec's own safety claim — *"the REVIEWER checks that transcription against the pinned bytes at review time; the RENDERER checks structure, never research content"* (§2) — leaves the single research judgement that can silently produce a wrong score (the four-to-three MERGE) guarded by **a one-time human read and nothing else**, when the authority to check it mechanically is already sitting in an accepted, immutable event. That is `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` at the design layer, and the Kernel exists to prevent exactly it.

**The remedy is bounded and fully specified below (F1, F2, F5 — spec edits, hours not days).** PROME may treat a re-submission limited to those three as a **re-check, not a fresh adversarial read**.

> ⚠️ **Seat note on the re-check.** F1's remedy is *my design*. Checking my own fix is the asymmetry I flag at other desks (`finding_verify_recommended_fix_not_just_finding`). **Rec:** I re-check F2 and F5 (pure factual corrections, no design of mine involved); **RED or a cold reader takes F1's leg.** Cheap, and it keeps the seat honest.

**Scope of this review:** §1–§6 and the §9 residue, as asked. **NOT reviewed** (and not claimable from this PASS/FAIL): any code (none exists), the 9/2 ruling itself, the MIDAS-06 grade, whether Will should approve the change.

---

## Verification performed at the artifacts (not from the draft's own account)

| # | Claim checked | Method | Verdict |
|---|---|---|---|
| V1 | MIDAS-06 masses 0.45 / 0.20 / 0.15 / 0.20 and their branch attachment | `git show 80c6346c58166a13839fc246b87a51eef8bf86f1:AGENTS/MIDAS/workbook/PREDICTIONS.tsv`, row `MIDAS-06`, cell-by-cell | **VERIFIED.** All four appear verbatim in one sentence of col 4 (`prediction`): `P(a) ~0.45, P(b) ~0.20, P(c) ~0.15, P(d) ~0.20.` Attached to exactly the branches §1a names. Sum = 1.00 exactly at two decimals. |
| V2 | The pinned row's `raw_record_sha256` | sha256 of the row incl. trailing newline | **VERIFIED** = `bee534444abf570c3e02bb19e0d177627e5d63806a716aa9595641cf7c4ef996` — matches §1a and the accepted event's `native_refs` pin exactly. |
| V3 | Do `YES` / `NO` / `AMBIGUOUS` appear in the pinned row? | case-insensitive scan of all ten cells | **NO — SEARCH-NOT-FOUND.** The row's own words are `NO-CALL, re-derive` (c) and `INDETERMINATE, hold M1 at 3` (d). See **F2**. |
| V4 | Where the four-to-three mapping is actually authorised | accepted event `EVT-…006a` (`QuestionRegistered`) payload | **VERIFIED.** `resolution_rule` states it verbatim: *"(a) -> YES, (b) -> NO, (c) -> AMBIGUOUS, (d) -> AMBIGUOUS."* Payload also carries `forecast_family: BINARY_PROBABILITY` and **no `outcome_vocabulary` key**. |
| V5 | Row status at the pin vs HEAD | `git diff 80c6346c5..HEAD` on that path | **VERIFIED CHANGED.** `status` `OPEN` → `HIT`; `resolution` 1,247 → 5,988 chars. **The frozen-letter portion (prediction + criteria + if_falsified) is byte-identical.** The pin is doing real work — a reviewer verifying against the LIVE file gets the right masses for the wrong reason. |
| V6 | §4's premise that `_calibration` renders one row per version with no ACTIVE filter | `KERNEL/tools/render.py:172-207` read directly | **VERIFIED.** `for version in forecast["versions"]:` — no filter. The §9 fix that replaced the old (vi) premise was correct. |
| V7 | The sibling registry's real wrapper shape | `json.load(KERNEL/policies/projection-exclusions.json)` | **VERIFIED.** Top-level keys: `exclusion_reasons`, `exclusions`, `policy_version` (`kernel.policy.1`), `purpose`, `registry_id`, `schema_version` (**`kernel.projection-exclusions.1`**). See **F4/F5**. |
| V8 | `OUTCOME_VALUES` | `KERNEL/tools/core.py:216` | **VERIFIED** = `{"YES", "NO", "AMBIGUOUS", "ANNULLED"}`. §4's "= {YES, NO, AMBIGUOUS} in v1" is correct. |

---

## FINDINGS

### ❌ F1 — BLOCKING. §4 (ii) validates only the one leg that cannot be wrong; every mis-merge passes the whole matrix.

**The check as written:** `probability_vector["YES"] == that version's scalar probability in Decimal` — *"the declaration may ADD masses, never contradict the accepted event."*

**What it actually constrains.** The accepted event's scalar is `0.45`, which is P(a). So (ii) pins the **(a) → YES** leg — the leg already fixed by the immutable event, i.e. the only leg a transcriber could not get wrong without the event refusing him. The three legs that carry real judgement — where (b), (c) and (d) land — are constrained by **nothing but Σ = 1**.

**Concrete failure that passes every §4 check.** Register the merge as (c) → NO, (b)+(d) → AMBIGUOUS:

```
probability_vector = {"YES": "0.45", "NO": "0.15", "AMBIGUOUS": "0.40"}
```
- Σ = 1.00 exactly ✅ · vocabulary length 3, no dups, all ∈ OUTCOME_VALUES ✅ · keys == vocabulary ✅ · Decimal strings in [0,1] ✅ · (i) event exists ✅ · **(ii) YES == 0.45 ✅** · (iii) no exclusions entry ✅ · (iv) family is BINARY_PROBABILITY ✅
- Renders `brier_score` = ½·[(0.45−1)² + 0.15² + 0.40²] = ½·[0.3025 + 0.0225 + 0.1600] = **0.2425**, not 0.2325.
- A wrong number that **looks right**, in the exact place §4's own opening sentence says the refuse-class exists to prevent: *"the failure it guards is a score that looks right."*

**Worse, and specific to this record:** P(b) and P(d) are **both 0.20**. A (b)↔(d) swap is *arithmetically undetectable at every layer* — same vector, same score, different meaning. Numeric identity is doing the work that a mapping check should do.

**Why "the reviewer checks it" is not the answer.** The reviewer is a one-time event at spec time. The registry entry is durable, is re-read at every render, and will be edited again (a corrected mass, a re-transcription, a second question). §2's division of labour is right in principle; it is misapplied here, because the merge is **not research content** — it is a mapping the Kernel already holds in an accepted event (V4). It is checkable structure that has been mis-classified as judgement.

**Required remedy (buildable today; V4 confirms the input exists).**
1. The entry carries a machine-checkable `outcome_map` beside `probability_vector` — the letter's branch labels, their masses, and their target outcome:
   ```json
   "outcome_map": {
     "a": {"outcome": "YES",       "mass": "0.45"},
     "b": {"outcome": "NO",        "mass": "0.20"},
     "c": {"outcome": "AMBIGUOUS", "mass": "0.15"},
     "d": {"outcome": "AMBIGUOUS", "mass": "0.20"}
   }
   ```
2. §4 gains two REFUSE-class checks:
   - **(v) `VECTOR_MAP_SUM_MISMATCH`** — for every label `k`, `probability_vector[k]` == the Decimal sum of `outcome_map` masses whose `outcome` is `k`; and Σ of all `outcome_map` masses == 1. *(This makes the vector a derived quantity, not a second independent assertion.)*
   - **(vi) `VECTOR_MAP_CONTRADICTS_RESOLUTION_RULE`** — the branch→outcome assignment in `outcome_map` agrees with the accepted question event's `resolution_rule`. v1 may satisfy this by an **exact-string pin** (`resolution_rule_sha256` in the entry, compared to the replayed event's field) rather than by parsing prose — cheap, immutable, and it refuses the moment anyone re-registers a different mapping.
3. §6 gains the matching negative tests: a (b)↔(d) swap and a (c)→NO merge must both REFUSE.

With (v) and (vi), a wrong merge stops being a silent wrong score and becomes a refusal.

---

### ❌ F2 — BLOCKING. "Transcribed from the FROZEN LETTER" is true of the MASSES and false of the LABELS; the reviewer instruction §2 gives cannot be discharged as written.

**Verified (V3):** `YES`, `NO` and `AMBIGUOUS` appear **nowhere** in the pinned MIDAS-06 row. The letter's own vocabulary is `(a)/(b)/(c)/(d)`, with (c) = `NO-CALL, re-derive` and (d) = `INDETERMINATE, hold M1 at 3`. The three-label vocabulary comes from the accepted event's `resolution_rule` (V4), not from the letter.

**Why it blocks.** §2 instructs the reviewer to check the transcription *"against the pinned bytes."* Anyone following that instruction — this review included — finds the masses and **not** the labels, and has no way from the spec to tell whether that absence is a defect or the design. A future re-check (a corrected mass, a second registry entry, a build-time review) will hit the same wall, and the cheapest resolution of the ambiguity is the wrong one: assume the labels are in the letter and stop looking.

**Remedy (two sentences).** §2 and `mapping_note` state the split explicitly: **masses** from the pinned letter (`raw_record_sha256`); **labels and the four-to-three mapping** from the accepted question event `EVT-…006a`'s `resolution_rule`. The reviewer instruction names both artifacts. This is also what makes F1's fix (vi) legitimate rather than invented — the authority already exists and is immutable.

---

### ❌ F5 — BLOCKING (factual, one line each). `kernel.renderer.2` is not the exclusions registry's schema version, and §5 places a renderer version where the registry's identity belongs.

**Verified (V7):** `projection-exclusions.json` carries `schema_version: kernel.projection-exclusions.1` and `policy_version: kernel.policy.1`. `kernel.renderer.2` is the **RENDERER_VERSION**, a different namespace.

- §1a: *"Same class and same discipline as `projection-exclusions.json` (`kernel.renderer.2`, Will-ruled 8/28)"* — **mis-attributes a renderer version to a registry.**
- §5: *"A registry the renderer reads (`kernel.renderer.3`)"* — the parenthetical sits where a reader takes it as the registry's version. The renderer bump `.2 → .3` is itself correct; the placement is not.

**Why it blocks rather than sits in residue:** §9 already flagged the namespace as residue, and residue is not fixed. A builder reading §1a and §5 as written names the new registry after a renderer version, and the namespace forks at birth — the same class as the `read_cap_check` basename collision (two tools, one name, standing rule earned 2026-09-02). Cost to fix: two sentences. There is no reason to carry it into code.

**Remedy.** §1a: *"…as `projection-exclusions.json` (schema `kernel.projection-exclusions.1`, policy `kernel.policy.1`, Will-ruled 8/28)."* §5: *"A registry (`kernel.outcome-vectors.1`) that the renderer — bumped to RENDERER_VERSION `kernel.renderer.3` — reads."*

---

### ⚠️ F3 — DECLARE. The letter's masses carry `~`; the registry declares them exact with `Σ == 1, no tolerance`. Safe here, defective as a rule.

**Verified (V1):** the letter reads `P(a) ~0.45 … P(d) ~0.20` — approximate by the author's own notation. §4 requires `Σ == 1 exactly in Decimal, no tolerance`. So the registry **hardens** an approximate distribution into an exact one. For MIDAS-06 this is harmless (the written figures sum to 1.00) and §1a's `mapping_note` discloses it — that disclosure is the right instinct.

**The class problem.** The next letter whose `~` masses sum to 0.99 or 1.01 cannot be registered at all, and the author's only route to a registrable entry is to **alter a mass** — i.e. to make a right row less right in order to clear a check. `CHECK_STANDARD` §1's last bullet names that condition: *if the only way to clear a flag is to make a right row less right, the CHECK is defective.*

**Remedy (one key, keeps `Σ == 1`).** The entry carries the RAW transcribed masses (`source_masses`) alongside the registered vector, plus `normalization` ∈ {`NONE`, `<declared rule>`}. MIDAS-06 registers `normalization: "NONE"` and the two records agree — the hardening becomes auditable instead of invisible, and a future non-summing letter has a declared, reviewable route instead of a silent edit. Non-blocking: it costs nothing today and prevents a defect that cannot be detected later.

---

### ⚠️ F4 — DECLARE. §4's matrix is incomplete against the sibling registry's own failure modes — §8 asked this directly.

**Verified (V7):** `projection-exclusions.json` carries a top-level **`exclusion_reasons`** object — a *registered enumerated token set with a description per token* — plus `policy_version` and `purpose`. §1a shows only an entry, never a wrapper; §4's registry-level checks name `schema_version` / `registry_id` / `entries` only.

**The gap that matters:** §4 *emits* four new tokens — `VECTOR_EVENT_UNKNOWN`, `VECTOR_CONTRADICTS_EVENT`, `VECTOR_VERSION_UNDECLARED`, `PROJECTION_METADATA_CONFLICT` (plus F1's two) — into the **same `exclusion_reason` column** whose token set the sibling registry governs. Two registries writing unregistered tokens into one column is the fork condition, and it is the same failure the fleet already paid for once (`PATTERNS` Type/Conf forked across 33 rows unnoticed because the vocabulary had no registered home).

**Remedy.** §1a states the full wrapper — `schema_version` `kernel.outcome-vectors.1` · `registry_id` `outcome-vectors` · `policy_version` · `purpose` · **`vector_reasons`** (the enumerated set, description per token, mirroring `exclusion_reasons`) · `entries`. §4 validates that every emitted reason token is a member of that set, and that no token collides with a key of `exclusion_reasons`. Also settle §9's open item explicitly: state per required key whether it is **validated** or **provenance-only** (`forecast_id`, `vector_source.*`, `mapping_note`, `ruled_by`, `ruled_at`, `ruling_record`) — a provenance-only key that a reader assumes is validated is `finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`.

---

### ⚠️ F7 — DECLARE, and new (not in §9). The spec silently changes WHICH outcomes are scorable, for vectored rows only, and `score_basis` does not express it.

**Verified (V6), `render.py:180-192`:** today a realized **AMBIGUOUS** renders **unscored** — `elif outcome in {"YES","NO"}: …score… ; elif outcome is not None: exclusion = f"OUTCOME_{outcome}"`. §4 states that under the spec *"a realized YES/NO/AMBIGUOUS is always covered"* — so a **vectored** row realized AMBIGUOUS **scores**.

That is defensible and probably intended — keeping the AMBIGUOUS mass is the whole reason the vocabulary was admitted. But it produces a new asymmetry the disclosure column does not carry: **two rows both realized AMBIGUOUS, one scored and one not, differing only by registry membership.** §5's "a binary row is a row with no `outcome-vectors` entry" makes it *consistent*, but consistency is not disclosure, and a `score_basis` of `BINARY` on an unscored `OUTCOME_AMBIGUOUS` row does not tell the reader why its neighbour got a number.

**Remedy.** One sentence in §3 or §5 stating it as an intended consequence, and one row in §6's test matrix: a vectored fixture realized AMBIGUOUS scores `½·[0.45² + 0.20² + (0.35−1)²]`; the binary control realized AMBIGUOUS still renders `OUTCOME_AMBIGUOUS`, unscored. Non-blocking; it is a documentation and test gap, not a correctness one.

---

### ⚠️ F8 — DECLARE. §4 (iv) is a check that cannot fire, correctly declared, with no dated retirement carrier.

§4 (iv) — *"the question's `forecast_family` is `BINARY_PROBABILITY` — trivially true in v1 (the schema's `const`)… no token, cannot fail today"* — is honestly declared, which is more than most vacuous legs get. But a leg that cannot fire is **PAT-060**'s class (the same class as the retired utility-L5 "zero YEYOU flags" leg, which is currently a default-zero instrument that can never fire), and the spec's stated retirement condition — *"recorded so the bridge is retired when §1b lands"* — has **no dated carrier**. §7 names a session-keyed DOCKET row (`next-KERNEL-spec-pass`); the retirement of (iv) is not attached to it.

**Remedy.** Either attach (iv)'s retirement explicitly to that DOCKET row, or drop (iv) and record the invariant as a comment. One line. *(Noted for PROME's registry: `next-KERNEL-spec-pass` is one of 7 event-keyed, undated DOCKET rows — see the separate `validate_all` build memo.)*

---

## THE §5 RULING THE SEAT WAS ASKED TO MAKE

**I rule for the SEMANTIC reading. The byte-level reading is rejected.** Four reasons, in order of weight:

1. **The byte-level reading is self-defeating.** Every renderer bump moves the `renderer_version` metadata line. Under a byte-level reading of *"`--check-views` still PASS at the committed `render_as_of` for all prior sittings,"* **no renderer bump is ever possible** — the condition would forbid the entire class of change the 9/2 ruling was written to govern. A reading that voids its own subject is not the reading.
2. **The precedent is real, on the record, and exactly parallel.** `.1 → .2` at Sitting 2 re-rendered the committed views under a ruled activation, and `--check-views` then reproduced the current committed views. The 8/28 chronology row records it. This is the same move at the same layer.
3. **The fifth-view alternative is strictly worse on the spec's own criteria.** `CALIBRATION_MULTICLASS.tsv` is a `VIEW_NAMES` registry change — a *wider* blast radius than an appended column — and it splits calibration across two views, re-creating precisely the cross-row incomparability §3 rejected the unnormalized Brier for. Choosing it would contradict §3 in the same document.
4. **The semantic invariant is the stronger one where it matters.** It fixes the seven cells `(question_id, forecast_id, forecast_version, probability, outcome, brier_score, exclusion_reason)` of **every** binary row — which is the property the 9/2 ruling was protecting. A byte comparison across a header adds nothing to that and costs the change.

> **The ruling carries one CONDITION, and it is not optional.** §6 **test 6's registry-free run is the control that proves reason (4)** — the run WITHOUT `outcome-vectors.json`, asserting that the drift is *exactly* the metadata line plus the appended column and that every row's seven cells are unchanged. It must run **before** the ruled MIDAS-06 change, and its expected drift must be **asserted in the test, not eyeballed in a diff**. Without that assertion the semantic reading is a promise rather than a checked invariant — and "unchanged by construction rather than by promise" is the standard §3 sets for itself two sections earlier.

---

## THE OTHER §8 QUESTIONS, ANSWERED

| §8 question | Answer |
|---|---|
| *Can a registry entry contradict an accepted event and still render (§4 ii)?* | **On the YES mass, no — (ii) is sound and sufficient for that leg.** On the merge, **yes**: see **F1**. The check is correct and its scope is one-quarter of the surface it appears to cover. `[[finding_gate_pass_is_not_evidence_it_found_the_best_reason]]` |
| *Does §3 privilege or penalise the AMBIGUOUS mass in a way the 9/2 word did not intend?* | **No.** ½·Σ(p_k − 1[k=realized])² is symmetric across labels; AMBIGUOUS is treated identically to YES and NO, and I checked the two candidate asymmetries: (1) the merged label carries a larger mass (0.35) only because it is a sum, which is arithmetic, not a scoring preference; (2) the K = 2 reduction is exact, so no binary row inherits anything. **The real asymmetry is elsewhere and the spec does not state it — see F7.** The rejection of binary-on-realized (0.3025) is correct and its stated reason is the right one: 0.45/0.20/0.35 and 0.45/0.55/0.00 must not score alike. |
| *Is §4 complete against the exclusions registry's failure modes plus the new ones?* | **No — F1 (the merge, blocking) and F4 (wrapper + registered token set, declare).** Everything else in the matrix is complete and correctly split between REFUSE and unscored-row, and the §9 fix that replaced the false ACTIVE-filter premise with `VECTOR_VERSION_UNDECLARED` was right (V6). |
| *Which reading of the reproduction condition holds (§5)?* | **Semantic, with the test-6 condition above.** |
| *Verify the MIDAS-06 transcription against the pinned bytes.* | **VERIFIED for the masses (V1, V2); the LABELS are not in the letter (V3) — F2.** |

---

## RESIDUE — declared, not fixed (WQ-178)

- §9's item *"§4 (i) needs an event index `_calibration` does not receive today"* is a real build detail I did not price. It is a plumbing change to `render_views`, not a design defect; it belongs to the code review, not this one.
- I did not review `live_shadow.py`'s mirror-refusal path (`OUTCOME_VECTORS_INVALID`) beyond §5's one-line description — no code exists and the description is consistent with the `PROJECTION_EXCLUSIONS_INVALID` sibling.
- §1b (schema-v2 `MULTI_OUTCOME_PROBABILITY`) is explicitly out of scope and I did not review it. Its Gate-A classification looks right from §1a's account, but that is INFERRED, not VERIFIED.
- §9's *"`YES`-head assumption"* item: F1's `outcome_map` remedy subsumes it — with a map, the scalar's label is derived rather than hardcoded. I did not re-spec §4 (ii) beyond that.
- I did not check whether removing MIDAS-06's exclusions entry (§4 iii) has any consumer outside CALIBRATION.

## What this review does NOT certify

That the build will be correct (no code exists) · that Will should approve the change · that the 9/2 ruling itself is well-formed · that the MIDAS-06 grade (`HIT`, realized YES) is right — I read it as given from the accepted `ResolutionVerified` event, I did not re-adjudicate it · anything about §1b.
