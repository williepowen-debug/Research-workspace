---
name: finding_registered_trigger_can_fire_on_an_unnamed_mechanism
description: "A pre-registered observable can be satisfied by a cause its registration never named. Marking it FIRED enters a causal fact into the record that never happened — re-read the registration's mechanism clause, not just its metric."
symptoms: "the metric hit the number so I marked it fired; the trigger fired but for the wrong reason; watch-for condition met, registered cause absent; threshold satisfied by an unrelated driver"
metadata:
  node_type: memory
  type: finding
  modified: 2026-08-31T23:21:18.000Z
---

A registered trigger usually has **two** parts: a **metric** (the observable) and a **mechanism clause** (the cause its registration assumed). Scanning only checks the metric. When the metric moves for a *different* reason, marking the trigger FIRED writes the unnamed mechanism into the record as though it had occurred.

**Worked instance (WALTER, 2026-08-07).** Remaining-ladder item #3b was registered 2026-07-17 as *"Iran asked the Houthis to stand ready to close the Red Sea route **IF the US strikes Iranian power infrastructure**"*, with a **Bab el-Mandeb transit collapse** as the watch-for. The transit collapse arrived unambiguously — **11 vessels over a weekend vs >70/day pre-2023**. **The US grid campaign never happened.** What closed the Red Sea was the Saudi–Houthi war, in the Houthis' own stated words. Marking #3b FIRED would have recorded that *a US grid strike triggered an Iranian escalation order* — an event that did not occur, entering the record through a correctly-observed number.

**Why:** the metric is what you scan; the mechanism is what you *report*. A fire is read downstream as evidence for the registered causal story, not merely for the number. So a metric-only match silently upgrades a coincidence into a confirmed mechanism — and every later reader inherits it as established.

**How to apply:** before firing any registered trigger, **re-read its registration for the mechanism clause, not just the metric.** If the metric moved for another reason, that is a **separate finding**, not a fire: log the observation against the actual driver and leave the trigger NOT FIRED. Corollary worth carrying: **register OBSERVABLES generously and CAUSAL CLAIMS stingily** — the instrument is repeatedly better than the theory hung on it.

Related: [[finding_theater_check_before_gate_check]] · [[finding_spec_that_is_both_falsifier_and_trigger_permits_only_disambiguation]] · [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]
