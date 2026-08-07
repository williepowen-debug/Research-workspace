---
name: finding_gross_flow_cannot_test_a_net_claim
description: "A gross flow (hires, inflows, new orders) can rise without limit while the net count is flat or negative — match the measure to the claim, and base-rate any proxy/target disagreement before deciding whether it is a measure problem or a regime finding."
metadata:
  type: feedback
---

**If your thesis is about a NET count, a GROSS flow cannot falsify it.** Gross inflows can rise without limit while the net is flat or negative, provided outflows keep pace. Where both sides of the identity are published, using one without the other is a choice — make it a stated one.

**Incident (LABOR, 2026-08-04 → 08-07).** A bull-side thesis kill had a leg denominated in **JOLTS gross hires >5.5M**, and a frozen grading card scored a convergence vector off **gross-hires bands**. Hires printed **5,348K, +96K** — the band was graded, the vector was cut, and the write-up said *"the gap is closing from the hiring side."* Three days later, while revising the gate, the other side of the identity got computed: **separations rose +91K to 5,351K, so JOLTS NET was −3K.** Hires and separations rose together — **churn, not net hiring.** The thesis was a claim about net employment; the test was arithmetically incapable of answering it.

**The second half is the part that nearly got missed — and it inverts the obvious conclusion.**

The instinct after such a catch is *"gross and net decouple, so the gross proxy is bad."* **Measured, that is false.** Gross hires rose in **66 months since 2015** and net was ≤0 in only **2 of them (3%)**; direction of gross agreed with direction of net **73%** of the time. **The proxy is usually serviceable — and the two exceptions in eleven years were the two months just graded.**

**That is a far more valuable finding than "the measure is bad."** Rare-in-general **and happening right now** is a **regime** finding and belongs in the thesis. Common-in-general is a **measure** finding and belongs in the spec. **They call for opposite actions**, and you cannot tell which you have without the base rate.

**How to apply:**
1. **Before denominating a threshold in a flow, write down whether the claim is about a GROSS flow or a NET stock/count, and match them.** "Employment is not growing" is a net claim.
2. **When both sides of an identity are published, compute both.** JOLTS publishes hires *and* separations; ISM publishes sub-indexes *and* the headline; fund data publishes inflows *and* redemptions.
3. **When a proxy and its target disagree, base-rate the disagreement before interpreting it.** Compute how often the divergence occurs historically and *when* — if the exceptions cluster on your current dates, you have found a regime, not a broken instrument.
4. **Do NOT quietly restore a score the corrected measure would justify on the day the correction favours your book.** Record the defect, leave the score, and **pre-commit the corrected re-grade to the next release before the data exists** ([[feedback_dont_bank_unpassed_forecast]]).
5. **Keep the composition counter visible.** Here the separations rise was **quits-driven** — voluntary churn is worker confidence, not distress — so "net ≤0" did not straightforwardly mean "still frozen." **High-churn/zero-net is a third state**, distinct from both frozen and thawing, and no vector or gate had a name for it beforehand. When a corrected measure produces an unfamiliar reading, check whether you lack a *category*, not just a number.
6. **Structural enforcement beats a counting rule.** The revised gate makes its realized-net leg **mandatory** (`A AND (B OR C)`) rather than requiring "N of M with at least one net" — the constraint is then unfalsifiable by leg-counting.

Related: [[finding_n_of_m_test_needs_intentions_realized_balance]] · [[finding_proxy_segment_masks_trigger_series]] · [[finding_threshold_spec_fails_before_world]] · [[finding_spread_metric_blind_to_common_mode]] · [[finding_measure_actionable_not_gross_rate]] · [[finding_compound_gate_jointly_unsatisfiable]]
