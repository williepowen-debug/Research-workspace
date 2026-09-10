---
name: finding_a_hash_pin_authenticates_the_reference_not_your_agreement_with_it
description: "A sha/hash pin proves the reference document is the one you expected; it never proves your claim AGREES with that document. Pair it with a self-consistency check and a validation matrix reads as complete while any semantically-wrong-but-arithmetically-coherent entry sails through — pin what the human RULED, as bytes, not the document they read."
metadata:
  type: finding
symptoms: "sha256 pin", "resolution_rule_sha256", "no prose parsing", "passes every check and still renders the wrong score", "validation matrix complete", "self-consistent but wrong", "the reviewer checks it at review time", "negative test asserts a token the code cannot emit"
---

**Two checks that feel like validation and are not:**

| Check | What it actually establishes | What people read it as |
|---|---|---|
| **Hash pin** on a reference (`resolution_rule_sha256 == sha256(event.resolution_rule)`) | *"This is the document I expected."* **Identity.** | *"My mapping agrees with the document."* **Agreement.** |
| **Self-consistency** (declared totals reconcile to declared parts) | *"The declaration agrees with itself."* | *"The declaration is correct."* |

**Neither touches semantics, and an error has no motive to be internally incoherent.** A hash pin cannot compare your claim to the document unless something *parses* the document — and parsing natural-language prose at render time is usually (correctly) forbidden as fragile. So the pin sits there looking strong while the semantic step is silently reserved to a human.

**Measured (RED, 2026-09-10, `KERNEL` L247 outcome-vector spec).** A remedy added `outcome_map` + a `resolution_rule_sha256` pin to stop a four-branch→three-label merge being mis-declared. RED's attack: keep the pinned letter's four masses **completely unchanged** (0.45/0.20/0.15/0.20) and have just two branches **trade labels** — (b)→AMBIGUOUS 0.20, (c)→NO 0.15. Result: every branch letter present once ✅ · per-label sums reconcile exactly ✅ · the scalar-equality check passes (YES 0.45) ✅ · Σ = 1.00 exactly ✅ · **the sha is correct, because the rule document was never touched** ✅. The entry **renders 0.2425 for a true 0.2325** — the exact wrong value the remedy's own rationale cited as the thing it was closing. With masses left free as well, the reachable range was **[0.226875, 0.3025]**, the upper bound being the alternative scoring formula the spec had **explicitly rejected**, reached *through* the adopted one.

**The tell that generalises:** the checks pinned *branch (a)* (by scalar equality) and *the arithmetic* (by summation) and **nothing pinned the assignment of the remaining branches** — and the answer depended on exactly that, because those branches carried **unequal** masses. **Ask which degrees of freedom your checks leave, then ask whether the output depends on any of them.** If yes, the matrix is incomplete no matter how many rows it has.

**Corollary found in the same read — a negative test can assert a token the mechanism cannot emit.** The spec shipped a fail-closed case: *"a (b)↔(d) swap ⇒ `VECTOR_RULE_MISMATCH` (the sha pin catches what arithmetic cannot)."* The sha pin **cannot** catch it (it never reads the map), and the swap was **numerically inert** anyway (both masses 0.20). At build time such a test either gets deleted — losing the negative — or **pressures the builder into the very prose parser the spec forbids.** See [[finding_test_the_guard_not_just_the_guarded]] and [[finding_guard_correctness_and_wiring_are_independent]]: write the negative against the mechanism you actually specified, and check the guard *can* fire on the case it names.

**How to apply**

1. **Pin what the human RULED, as bytes — not the document they read.** Have the reviewer do the semantic work once, at ruling time, then freeze *their conclusion* (`outcome_map_sha256`, a ruled mapping blob) and machine-compare exact bytes. No parser needed, and the comparison now guards the property the output depends on.
2. **Keep the reference pin too** — it catches the reference text changing *underneath* an already-ruled mapping, which would silently invalidate the ruling. The two pins answer different questions and both are cheap.
3. **Require every declared category to be inhabited.** A vocabulary label with zero contributing parts and mass `0.00` is how the degenerate cases reach the extreme values.
4. **Say out loud that the residual is human judgment.** These checks authenticate *what someone ruled*, never that they ruled correctly. That limit is unavoidable — but it must be **stated**, not implied away by a check that looks stronger than it is. [[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]] is the same shape: the presence audit passes and the check starves.
5. **When a spec reserves semantics to a reviewer, the reviewer is a load-bearing component.** Name them, give them the addends to recompute, and never describe the automated half as "validated."

Related: [[finding_crosscheck_with_free_parameter_validates_nothing]] (zero unknowns or it is not a test — the closest sibling) · [[finding_adoption_is_not_validation]] · [[finding_gate_pass_is_not_evidence_it_found_the_best_reason]] · [[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]] · [[feedback_behavior_language_over_hash_pinning]] (hash pins decay in prose; here they *over-promise* in code).
