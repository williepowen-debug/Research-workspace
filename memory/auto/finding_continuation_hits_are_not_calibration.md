---
name: finding_continuation_hits_are_not_calibration
description: "A prediction book scoring well on momentum continuations tells you nothing about calibration — count how many entries required predicting a TURN"
symptoms: "prediction book looks good, hit rate is fine, most predictions resolved HIT, calibration seems solid, forward book re-armed, my predictions keep hitting"
metadata:
  node_type: memory
  type: feedback
---

Audit a prediction book by asking of each entry: **did this require predicting a TURN, or was it a momentum continuation?** A book full of continuations resolves HIT at a high rate while testing nothing, because the base rate of "the current trend persists over one period" is already high. **Hit rate is not calibration when the entries are free.**

HANS 2026-08-28 graded three predictions: HNS-02 (ECB holds at 2.25% — held) ✅, HNS-04 (TTF stays above €50 through July — did) ✅, HNS-03 (German Mfg flash PMI prints *below* 50, breaking a two-month expansion streak) ❌ — printed 52.2, missed by 2.2 points at 55% confidence, and the next month printed 54.1. **2-for-3 looks respectable. But the two hits were continuations of live momentum and the single miss was the only entry that required calling a reversal.** The honest score on the thing the book was supposed to test is 0-for-1.

The same audit applied to the *new* book caught it happening again: of four freshly-armed predictions, three were continuations and only one (a "this does NOT keep going" ceiling) could produce an embarrassing result.

**Why:** Predictions are supposed to be costly. A continuation call borrows the trend's own base rate, so it pays out without discriminating between "my model works" and "nothing changed." Worse, a book of them produces a *rising* hit rate exactly while a desk is drifting out of touch — which is the moment the record is most reassuring and least informative. The miss is where the information is, and a book with no turn-calls has designed the information out.

**How to apply:** When arming or reviewing a prediction book, tag each entry **CONTINUATION** or **TURN**, and report the hit rate *separately for each*. Deliberately carry at least one entry that can only resolve MISS if your current core thesis is right — a ceiling, a floor, or an explicit "this does not extend" — so the book contains its own falsifier. When grading, write the continuation/turn split next to the score; never quote a bare hit rate. Related: [[finding_anchor_prediction_to_surprise_not_priced]] (the per-prediction version — key the trigger to the surprise, not the priced outcome), [[finding_self_attack_defends_the_argument_not_the_apparatus]], [[finding_adoption_is_not_validation]].
