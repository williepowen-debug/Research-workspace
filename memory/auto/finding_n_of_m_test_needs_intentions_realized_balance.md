---
name: finding_n_of_m_test_needs_intentions_realized_balance
description: An N-of-M gate whose conditions are mostly survey/intentions data can clear its bar without any realized count confirming — tag each condition INTENTIONS or REALIZED at registration and require one from each side.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f1644531-5f14-4570-9621-6bb672464d7b
  modified: 2026-08-07T19:00:26.828Z
---

When you pre-register a test that fires on **N of M conditions**, the bar is only as good as the *mix* of what M contains. **If most conditions are survey, openings, or announcement data, the gate can clear entirely on the intentions layer — the layer that moves first and reverses most.**

**Incident (LABOR, 2026-08-05 → 08-07).** A frozen grading card pre-registered implication I-1 (*"the freeze is intact and deepening"*) as failing if **≥2 of four** landed: JOLTS hires >5.3M · NFP ≥150K · ISM employment ≥50.0 · Challenger AI-share collapsing. Two landed — **JOLTS hires and ISM employment** — so the rule fired and, per the card's own pre-commitment, the agent called a labor-market thaw that week. **Within 48 hours the realized data contradicted it: payrolls printed −23,000 with 103,000 of downward revisions, and ISM *Services* employment fell back into contraction.**

**The logic and the discipline were both fine. The condition set was not.** 🔧 **Classification corrected two days later, and the correction makes this sharper.** The first write-up counted the gross-hires condition as *intentions*, which is wrong — a hires count is **realized**. The honest split is **two-dimensional**: one survey diffusion index and one announcement tally (both INTENTIONS), one net payroll count (REALIZED-NET), and one gross-flow count (REALIZED-GROSS). **Of the two conditions that actually landed, one was an intentions measure and the other was a gross flow standing in for a net claim — and the net was negative that month** ([[finding_gross_flow_cannot_test_a_net_claim]]). **Neither was a realized NET count, which is the only kind that can confirm the thesis had ended.** A one-axis INTENTIONS/REALIZED rule would still have passed this test; the two-axis version is what catches it.

**Why this is easy to build by accident:** intentions data is abundant, prints early, and prints often — so it dominates any condition set assembled from "what will I be able to observe that week." Realized counts are scarce and late. **Availability, not evidentiary weight, selects the conditions.**

**How to apply:**
1. **Tag every condition on BOTH axes at registration, in the artifact — `INTENTIONS`/`REALIZED` *and* `GROSS`/`NET`.** If the tags are lopsided on either axis, the bar is lopsided.
2. **Require that at least one condition which is *both* REALIZED *and* NET be among those clearing the bar.** A gate that can fire without one is measuring sentiment about the thing, or gross churn in it, but not the thing. **Prefer structural enforcement to a counting rule:** make the realized-net leg *mandatory* — `A AND (B OR C)` — so no combination of the others can substitute for it.
3. **Write the failure mode on the card as a one-line pre-mortem** — *"this test can be cleared without any realized count confirming"* — which is checkable at freeze time, before any data exists.
4. **Weight by reversal rate, not availability.** In this incident the two intentions inputs both moved materially within one month (one openings series revised up 82K; one survey sub-index swung 51.2 → 47.4).
5. **Do NOT un-say a call the rule correctly produced.** Retro-rescuing a conclusion because the next print disagreed is precisely the improvisation pre-registration exists to prevent. **Fix the instrument for next time; leave the graded call standing** — and record the design defect where the next card author will read it.

**Mirror failure:** [[finding_compound_gate_jointly_unsatisfiable]] — a gate whose legs combine to ~0% in the state it exists to detect. This is the opposite end of the same axis: a gate that fires **too easily, on one layer of evidence**. Both come from not base-rating the condition set jointly at registration.

Related: [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_threshold_spec_fails_before_world]] · [[finding_proxy_segment_masks_trigger_series]] · [[feedback_single_month_subcomponent_skepticism]]
