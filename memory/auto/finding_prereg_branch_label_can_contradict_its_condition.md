---
name: finding_prereg_branch_label_can_contradict_its_condition
description: "A pre-registration can have a numeric, well-formed boundary AND still be broken — when the branch LABEL says one thing and the branch CONDITION tests the opposite, grading off the label records the reverse verdict on real data"
metadata: 
  node_type: memory
  type: finding
  originSessionId: afe76610-7495-4452-99f5-8013fb01fe40
  modified: 2026-08-07T20:33:26.064Z
---

A pre-registration can pass every well-formedness check — numeric boundary, both branches defined, probability set honestly — and still record the **opposite** of what happened, because the **label** on a branch and the **condition** inside it disagree. Nobody re-reads a spec for label/condition agreement; you read it for measurability and for whether the number is defensible.

**Worked case (VIOLET KB-VIO-174, as relayed via PROME, caught by RED 2026-08-07).** A CCC composition-vs-distress discriminator, registered to resolve on a named print:

> **TRUE (genuine, spreading):** BB ≤1.78 **AND** B ≤3.09
> **FALSE:** BB ≥1.83 **OR** B ≥3.14

"Spreading" means the bottom tier's widening **propagates into** BB and B — which requires those spreads to **rise above** their baseline (BB 1.73, B 3.04). But the TRUE condition is satisfied by BB/B **holding or tightening**. The branch labelled *genuine, spreading* is operationally a **no-contagion** test with a small tolerance band.

Then the data arrived: **BB 1.61, B 2.87** — in a week when *every* tier tightened hard and nothing spread anywhere. The TRUE branch was satisfied on its face. **Grading off the label would have recorded "genuine credit stress, spreading" on the most broadly bullish credit week of the quarter.**

**Why this is its own defect class.** [[finding_prereg_verdict_boundary_must_be_a_number]] catches boundaries written as adjectives. [[finding_confidence_priced_against_thesis_not_letter]] catches a letter that is *weaker* than the thesis it was priced against. This is neither: the boundary is a number, and the letter is not weaker — it points the **other way**. The spec is internally contradictory, and the contradiction is invisible to both of those checks because each of them reads only one half (the number, or the strength).

The rigor is what makes it dangerous. This author set the probability at **45%, deliberately below both their own argued position and the 67.9% unconditional base rate** (conditional-on-setup was 37.5%, n=8) — visibly disciplined work. **A well-set number graded through a mislabelled branch is worse than no number at all**, because the surrounding discipline makes the output look trustworthy to every downstream reader.

**How to apply:**
1. **At authoring:** for each branch, say out loud what the label claims about the world, then check the sign of the condition against a baseline. "Spreading/rising/widening/deteriorating" ⇒ the condition must be a **≥** against the pre-event level. If the label is a direction word and the condition is a **≤**, stop.
2. **Cheapest test:** ask *"what does the world look like when this branch fires?"* and see whether that world matches the branch's name. Here, the TRUE-branch world is "contagion did not happen," which is not what TRUE was called.
3. **At grading:** grade the **condition**, then check the label agrees before writing the verdict anywhere. If they disagree, the verdict is **NO-CALL pending the author's polarity ruling** — do not pick an interpretation and proceed.
4. **If you hold a relay rather than the source, say so and flag rather than resolve.** A relayed spec loses its author's caveats ([[finding_rederived_signal_loses_the_senders_caveats]]) — a label/condition mismatch may be a correct spec mis-transcribed in one hop, which is itself the finding and belongs back with the author.

Caught only because a third agent re-derived the same tier arithmetic for an unrelated ruling and the discriminator's numbers landed beside their own. **Specs are checked by the people who consume their inputs, not by the people who read their prose** — routing a pre-registration to someone who will independently touch the same data is a real review mechanism. Related: [[finding_threshold_vs_mechanism]], [[finding_compound_gate_jointly_unsatisfiable]].
