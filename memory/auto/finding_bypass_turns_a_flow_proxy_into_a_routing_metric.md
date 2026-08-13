---
name: finding_bypass_turns_a_flow_proxy_into_a_routing_metric
description: "A flow-through-a-node metric (chokepoint transits, port calls, pipeline throughput) silently stops measuring LOSS and starts measuring ROUTING the moment a bypass exists. The instrument stays correct and the reading stays fresh — only the MEANING moves. Verify bypass status as a separate fact, on its own cadence."
metadata:
  node_type: memory
  type: finding
---

**The pattern (2026-08-13, BRENT).** BRENT's thesis v5.4 promoted *"transits through the Strait of Hormuz"* to **the** adjudicator of whether the corridor was still impaired. Low transit counts were read — implicitly, never explicitly — as **barrels not reaching the market**. Re-verifying the desk's stalest large ledger row found the **ADCOP Habshan–Fujairah pipeline, the UAE's primary Hormuz bypass (1.5M bpd), was OPERATING**, not offline as the ledger had asserted for 118 days: UAE crude+condensate ran **~3.7 mb/d** in June with Abu Dhabi loadings **~4.0 mb/d**, and the source named the bypass itself as the enabling route. You cannot load ~4 mb/d out of Abu Dhabi with the 1.5M bypass down *and* the strait impaired.

⇒ **`barrels through the node` ≠ `barrels lost`.** The transit series was never wrong, never stale, and never mis-sourced. **What changed was what a low reading MEANT** — it had become a measure of **access cost and routing**, not of net supply loss.

**Why this is nastier than an instrument failure.** Every guard people build points at the *instrument*: is it reachable, fresh, correctly specified, within its staleness budget? **All of those pass.** The metric keeps printing clean numbers on schedule, and the interpretation rots silently underneath — there is no error, no gap, no stale flag, nothing to alert on. A freshness check cannot catch a meaning change ([[finding_freshness_check_cannot_catch_a_fresh_lie]]), and an instrument probe explicitly checks the instrument and *never* whether the level still means anything.

**The generalisation.** Any metric of the form *"flow observed at a specific place"* is a proxy for *"total flow"* **only while that place is the sole path.** The moment a substitute path exists — and substitute paths are built precisely *because* the chokepoint is stressed, so the correlation is adverse — the proxy quietly re-bases. This covers chokepoint transits, port calls, pipeline throughput, a single terminal's loadings, a border crossing, one exchange's volume, one venue's order flow.

**How to apply:**
1. **Name the bypass set when you register the metric**, not when it surprises you. "This measures total flow *provided* routes {A, B, C} remain the only ones" — written into the row, so a later reader sees the assumption instead of inferring it.
2. **Verify bypass status as a SEPARATE fact on its own cadence.** It is not part of the metric's own freshness check and will never be caught by one. Bypass capacity changes on a **construction/repair** timescale (months), so a slow re-check is enough — but it must exist.
3. **Watch the aggregate that the bypass would show up in.** Here the tell was national export volumes staying near normal while the chokepoint reading collapsed. **A node metric and a total-flow metric disagreeing is the signature**, and it is cheap to monitor.
4. **A bypass usually makes a falsifier CONSERVATIVE, not wrong** — reopening still shows up as flow returning to the node. Do not rush to re-level the test; re-levelling is a new registration with base rates, not maintenance.
5. ⚠️ **Expect the correction to cut against your own book.** This one shrank the desk's own thesis: the supply-loss reading died, while the premium/access-cost reading — the one the thesis actually rested on — survived untouched. **The finding surfaced only because a stale-row re-verification queue forced a look at the biggest carried assertion**, which is the argument for having such a queue at all ([[finding_dated_carry_item_has_no_expiry_check]]).

**Sibling, and the distinction is the point:** [[finding_proxy_segment_masks_trigger_series]] is a proxy measuring the **wrong segment** — bad substitution, fixable by picking the right series. **This is the opposite:** the *right* series, correctly measured, whose **referent moved underneath it**. No better series exists; what is needed is a stated scope condition and a periodic check that the condition still holds. Related: [[finding_threshold_level_is_a_measurement_not_a_constant]], [[finding_claim_outlives_its_discredited_instrument]].
