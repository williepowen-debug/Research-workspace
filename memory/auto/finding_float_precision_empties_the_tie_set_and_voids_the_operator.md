---
name: finding_float_precision_empties_the_tie_set_and_voids_the_operator
description: A threshold test on a decimal-published series, computed in binary float, has an EMPTY tie set — so ≤ and < become indistinguishable and boundary rows are decided by a ~1e-14 residual, not by the declared operator. Test it with an exact-boundary FIXTURE; an unchanged partition alone proves nothing.
symptoms: "recomputing the base rate under both operators gives the same answer" (a PROMPT, not a verdict — see the correction); "the registered partition doesn't reproduce under either tie convention"; "cause UNKNOWN, docketed"; "strict and non-strict agree"; "self-consistent and reproduced by its own code but nobody else can reproduce it"
metadata:
  type: reference
---

A series published to N decimals has a natural resolution (2dp in percent ⇒ exactly 1bp). Differences of such values are **exact integers** in that unit. Computed in binary float they are not: `(5.25 − 5.35) × 100` = `−10.000000000000009`.

**Consequence, and it is a change of kind rather than a rounding nuisance: no value is ever exactly ON a threshold.** The tie set goes **empty**, `≤` and `<` become indistinguishable, and every boundary row is classified by the **sign of a ~1e-14 representation residual** — a quantity with no meaning in the domain.

**THE VALID TEST — a POSITIVE FIXTURE, not an inference from absence.** Construct an observation sitting **exactly on the boundary at the declared precision** and verify it classifies the way the operator says. That is the only check that distinguishes "the operator is enforced" from "the operator is unenforceable."

⚠️ **The tempting shortcut is INVALID and this memory previously stated it as a rule.** *"Recompute under both operators; if the answer does not change, you are comparing floats"* — **false.** An unchanged answer proves only that the tie set is empty **on this sample**, and a tie set can be empty for a perfectly ordinary reason: with integer observations `[1, 3]` and threshold `2`, both `<2` and `≤2` return one hit and nothing is wrong. **Empty-because-float and empty-because-no-observation-is-there are indistinguishable from the unchanged answer alone.** Treat an unchanged partition as a **prompt to run the fixture test**, never as a defect flag. *(Corrected 2026-09-06 by CODEX review, hours after the flawed form was published to three desks — an inference-from-absence, which is the very class this memory sits beside.)*

**Fix:** compute in integer units — `round(Δ × 100)`, or `Decimal` — **before** comparison, and declare the precision on the card beside the operator. **Declaring the operator alone is not enough; it can be silently unenforced.**

**Why nothing catches it:** the number is self-consistent, reproduced by its own code, and passes structural checks — schema validators check shape and explicitly *not* value domains. It is invisible until someone independently rebuilds the computation.

**Measured instance (RED-FT-11, 2026-09-06).** Registered partition `4/68/8` was **neither strict nor non-strict** — a coin flip over **32 of 80 windows (40%) sitting exactly on a boundary, splitting 16 in / 16 out**. True partition `5/71/4`. Tie atoms were large (one leg held 11 of 80) and within a single leg the residual sign went **both ways**. **The most-wrong cell was the NO-VERDICT / silence rate: 10.0% registered against 5.0% true** — the counterparty had ranked that cell above the tie convention precisely because *"a quiet instrument and a broken one look identical from outside."*

⚠️ **A desk can hold two precision conventions at once and declare neither:** the same registration family had its partition computed unrounded and its base rate rounded. **Exposure is any trigger comparing a float-computed delta of a decimal-published series against a threshold at that series' own precision** — OAS, yields, breakevens, index levels.

Related: [[finding_loadbearing_number_must_be_reproducible]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_output_shape_implies_more_than_the_measurement]]
