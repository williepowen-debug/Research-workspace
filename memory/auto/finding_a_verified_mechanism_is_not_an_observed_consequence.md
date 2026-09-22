---
name: finding_a_verified_mechanism_is_not_an_observed_consequence
description: "You verify a defect's MECHANISM at the code or the letter, then report its worst plausible CONSEQUENCE as though you had observed it. The mechanism is real and the report is still false. The consequence needs its own observation — usually at the rendered/consumed surface, not the code path — and it is often blocked by something else that makes the harm never occur."
symptoms: "this means the tool has been publishing a wrong number | so it authorises spawning a desk that didn't need it | that is a third distinct failure mode | the guard is disarmed so the value reaches the dashboard | I traced the code path and it yields X | reviewer said 'repair-worthy defect, not an observed consequence' | I said 'has been' when I had only established 'would'"
metadata:
  node_type: memory
  type: feedback
---

**Verifying a MECHANISM is not observing a CONSEQUENCE.** You read the code, reproduce the bad value, confirm the logic — all correct — and then write the sentence one step further than the evidence goes: *"so it has been publishing a wrong level"*, *"so it authorises a spawn that wasn't needed"*. **The mechanism claim is true and the consequence claim is unverified.**

**n=3 in a single session (PROME, 2026-09-21/22), all three caught by reviewers, never by the author:**

| claimed | actually |
|---|---|
| a commit-matcher's blind spot *"fails in the direction that authorises spawning a desk that didn't need it"* | the classifier compares last-commit to the **row start**, not to today, so the class was ACTIVE either way — **no class flip, no mis-spawn** |
| two post-settle price reads 68¢ apart are *"a THIRD distinct shape"* | the prior case's reads were **also post-settle**; read TIME had been conflated with value BASIS — **same mechanism already adjudicated** |
| a parser yields `26` from a contract label, so the dashboard *"has been publishing 26"* | the tile-map never produces that tile at all (separately docketed) — **the 26 reaches no surface** |

🔑 **The shape: the mechanism is upstream and cheap to verify; the consequence is downstream and requires a different instrument.** Code-path tracing answers *can this happen*. Only the rendered, consumed, or graded surface answers *did it*. The author stops at the first because it is the part they just proved.

⚠️ **This is not a reason to suppress the finding.** All three defects were real and two are worth repairing. The failure is purely in the sentence's reach — and the cost is real, because a reviewer who checks the consequence and finds nothing has reason to discount the mechanism too.

**How to apply:**
- Write the mechanism and the consequence as **two separate claims with two separate confidence tokens.** VERIFIED for what you traced; INFERRED or UNKNOWN for what follows from it.
- **Before writing "has been" / "is publishing" / "authorised", name the instrument that would show it and run it.** For a render, run the renderer. For a classifier, call it on the real row. For a grade, read the graded artifact.
- **Ask what else stands between the mechanism and the harm.** Twice here the harm was blocked by an unrelated defect or by a comparison that made the difference irrelevant. A bug can be real and permanently inert.
- **Docket it on the mechanism** — "repair-worthy on mechanism, no observed consequence" is a complete and honest row, and it survives review. A row claiming unobserved harm gets the whole finding discounted.
- The author is the worst detector of this: the charitable reading of your own catch is that it matters. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`

Related: [[finding_output_shape_implies_more_than_the_measurement]], [[finding_verified_figures_do_not_verify_the_shape_claim]], [[finding_record_of_an_action_is_not_the_action]], [[finding_asymmetric_rigor_counterparty_claims]], [[finding_gate_pass_is_not_evidence_it_found_the_best_reason]].
