---
name: finding_float_precision_empties_the_tie_set_and_voids_the_operator
description: A threshold test on a decimal-published series, computed in binary float, has an EMPTY tie set — so ≤ and < become indistinguishable and boundary rows are decided by a ~1e-14 residual, not by the declared operator.
symptoms: "recomputing the base rate under both operators gives the same answer"; "the registered partition doesn't reproduce under either tie convention"; "cause UNKNOWN, docketed"; "strict and non-strict agree"; "self-consistent and reproduced by its own code but nobody else can reproduce it"
metadata:
  type: reference
---

A series published to N decimals has a natural resolution (2dp in percent ⇒ exactly 1bp). Differences of such values are **exact integers** in that unit. Computed in binary float they are not: `(5.25 − 5.35) × 100` = `−10.000000000000009`.

**Consequence, and it is a change of kind rather than a rounding nuisance: no value is ever exactly ON a threshold.** The tie set goes **empty**, `≤` and `<` become indistinguishable, and every boundary row is classified by the **sign of a ~1e-14 representation residual** — a quantity with no meaning in the domain.

**THE TELL, and it costs one line:** recompute any registered base rate under **both** operators. **If the answer does not change, the tie set is empty** — and on an integer-valued statistic an empty tie set means you are comparing floats, not units. A partition that collapses to identical numbers under all operator combinations is the signature.

**Fix:** compute in integer units — `round(Δ × 100)`, or `Decimal` — **before** comparison, and declare the precision on the card beside the operator. **Declaring the operator alone is not enough; it can be silently unenforced.**

**Why nothing catches it:** the number is self-consistent, reproduced by its own code, and passes structural checks — schema validators check shape and explicitly *not* value domains. It is invisible until someone independently rebuilds the computation.

**Measured instance (RED-FT-11, 2026-09-06).** Registered partition `4/68/8` was **neither strict nor non-strict** — a coin flip over **32 of 80 windows (40%) sitting exactly on a boundary, splitting 16 in / 16 out**. True partition `5/71/4`. Tie atoms were large (one leg held 11 of 80) and within a single leg the residual sign went **both ways**. **The most-wrong cell was the NO-VERDICT / silence rate: 10.0% registered against 5.0% true** — the counterparty had ranked that cell above the tie convention precisely because *"a quiet instrument and a broken one look identical from outside."*

⚠️ **A desk can hold two precision conventions at once and declare neither:** the same registration family had its partition computed unrounded and its base rate rounded. **Exposure is any trigger comparing a float-computed delta of a decimal-published series against a threshold at that series' own precision** — OAS, yields, breakevens, index levels.

Related: [[finding_loadbearing_number_must_be_reproducible]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_output_shape_implies_more_than_the_measurement]]
