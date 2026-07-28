---
name: finding_gate_bias_is_placement_error_compare_to_margin
description: A known bias in a threshold is a PLACEMENT error and only binds near the boundary — quantify it in the metric's own units and compare to the realized margin before discounting a verdict
metadata:
  type: feedback
---

When you know a gate is mis-specified — bar set too strict, a leg wrongly conjunctive, a criterion wrong-signed — the reflex is to discount its verdict wholesale. **Don't. Quantify the defect in the measured quantity's own units, then compare it to the margin the print actually cleared by.** A mis-specified threshold is almost always a **placement** error, and placement errors only bind **near the boundary**.

Worked case (BOND, 2026-07-28 7Y auction, `BND-13`): the gate was known pre-print to be biased toward NOT firing, and the downstream consumer had been told to discount a no-fire. At resolution the two legs needed **opposite treatment**:

- **Indirect leg** — the placement error was **0.82pp** (trailing-12 minimum 56.42% vs the better-supported 15th percentile 57.24%). The print cleared by **~13pp**. A 0.82pp placement error cannot manufacture a thirteen-point margin ⇒ **the measurement stands independent of where the bar sits.** Discount the gate, not the number.
- **Dealer leg** — cleared by **0.032pp**. Genuinely knife-edge ⇒ **full discount applies.** (It was also the wrong-signed leg, so deleting it *strengthened* the same verdict — worth checking, because a defect can point either way.)

**Why:** "the gate is biased, so this result is weak" is true only in the neighbourhood where the bias could have flipped the outcome. Applied uniformly it destroys real information — and it destroys it *asymmetrically*, because the results furthest from the boundary are exactly the most informative ones. It also hands you a permanent excuse to disregard any verdict you dislike.

**How to apply:** at resolution, (1) state the **margin on every leg**, not just the branch that fired — "B fired" and "B fired by 0.032pp on one leg" are different facts and only one is honest; (2) express the known defect in the same units as the margin; (3) discount per-leg, never per-verdict; (4) say explicitly whether you would have graded the same way under the *corrected* spec — if yes, the defect was non-binding and should stop being cited as a caveat.

Related: [[finding_run_the_falsifier_before_promoting]] · [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_threshold_spec_fails_before_world]] · [[finding_threshold_level_is_a_measurement_not_a_constant]] · [[finding_resolvability_defect_is_status_not_confidence]]
