---
name: finding_measurement_bias_sign_is_fixed_harm_direction_is_not
description: "A known measurement bias has a FIXED sign, but whether it is protective or dangerous is a property of the TEST it feeds, not of the instrument — so fixing the guard on one side leaves the other standing."
metadata:
  type: reference
---

**A known measurement bias has a FIXED SIGN. Whether that bias is PROTECTIVE or DANGEROUS is a property of the TEST it feeds, not of the instrument.** The same one-directional error is a false-fire generator on one test and a failure-to-exit risk on its mirror — so **a guard written against one side leaves the other standing, silently.**

**The worked pair (WALTER + TERRY, 2026-08-18):** AIS-derived Strait-of-Hormuz transit counts **under-count** — hulls go dark, so the count is a floor. One fixed sign, two opposite consequences:

| Test the number feeds | Direction of the test | What the under-count does |
|---|---|---|
| **Stress** — "have transits collapsed?" | looking for a LOW print | **FALSE-FIRE generator.** Dark hulls manufacture the collapse the test is hunting. *(This is why FALCON inverted the fire side in July.)* |
| **De-escalation** — "have loadings resumed?" | looking for a HIGH print | **FAILURE-TO-RETIRE risk.** The instrument structurally cannot show recovery, so a dead position stays alive. |

🔴 **AND THE JULY FIX ONLY TOUCHED THE FIRST ONE.** The inversion that corrected the false-fire side left the failure-to-retire side completely unguarded, because nobody restated the bias as a property of the *reader's* test. **A guard fixed on one side reads, on every surface, exactly like a guard.**

**Why this is not just "biases have directions":** the tempting summary is *"the instrument under-counts, so discount it."* That is wrong in half the cases — on a de-escalation test you must discount it **in the opposite direction**, and a reader who applied the standing caveat would get it backwards. **The caveat cannot travel with the instrument. It has to travel with the test.**

**HOW TO APPLY.** When you find or inherit a signed measurement bias:
1. **Name the sign once** (under-counts / over-counts / lags / truncates).
2. **Enumerate every live test that consumes it, and mark each test's DIRECTION** — is it hunting a high print or a low one?
3. **State the consequence per test, not per instrument.** Expect them to be opposite.
4. **Check whether an existing fix covers only one direction.** If a prior inversion, guard or caveat exists, assume it is one-sided until you have read it.
5. **Never write the caveat as a bare property of the data source.** *"X under-counts"* is not actionable; *"X under-counts, which manufactures fires on the stress test and suppresses retires on the de-escalation test"* is.

**Provenance:** WALTER's `SIG-W-20260818-002` argued the pro-cyclical/stress leg. TERRY, the recipient, supplied the de-escalation leg against its own card and pointed out both were one object read two ways. Neither half alone was the finding.

Related: `[[finding_standing_guard_is_a_false_negative_risk]]` (a guard against a known FP is itself an FN risk — this is its measurement-layer cousin) · `[[finding_bypass_turns_a_flow_proxy_into_a_routing_metric]]` · `[[finding_exact_level_authenticates_a_wrong_direction]]` · `[[finding_absence_tell_needs_a_talkative_instrument]]`.
