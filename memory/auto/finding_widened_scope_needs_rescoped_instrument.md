---
name: finding_widened_scope_needs_rescoped_instrument
description: Widening a prediction's scope while keeping the old base-rate instrument can make it already-failed at registration — and you cannot see it from inside the derivation
metadata:
  type: feedback
---

When you widen a prediction's scope to close a defect, **re-scope the base-rate instrument to match — or state in the row what the instrument cannot see.** Otherwise the widened claim gets graded against a narrow instrument, and it can be **already false on the day you register it**, with the derivation looking perfectly sound.

**Why:** FALCON's FAL-01 failed on the *actor* axis (a prediction written over an asset class is exposed to every belligerent who can reach it). The successor FAL-03 deliberately broadened — "no confirmed loss of Gulf-ally or Iranian **oil/gas** supply," with route (a) naming crude/condensate/product/LPG/**LNG**. Good instinct; the widening was the fix. But its 58% confidence was derived from a base rate computed off `STRIKES.tsv` — an **oil-complex strike ledger**. That instrument counts kinetic events against oil facilities. It is **structurally incapable of seeing a force majeure** (not a strike) **on LNG** (not oil). The headline input, "ZERO qualifying events across 109 days," was an artifact of the instrument's blind spot, not a fact about the world.

A QatarEnergy force majeure on LNG had been live since 2026-03-24 — 17% of Qatar's export capacity, 3-5 year repair. **FAL-03's route (a) was satisfied on the day it was written.** It was registered as the explicit kill-switch for a thesis exported to four other agents, marked OPEN, and could never have resolved CONFIRMED. It was caught four days later only because another agent (WALTER) routed a signal the domain owner's own boot sweep was structurally blind to.

Two compounding tells worth recognizing separately:
- **An unchecked negative.** The published state read "active force majeure in-theater: **none current** (… were March)." The event was known; what was never asked was whether the force majeure had been **lifted**. **An event has a date; a force majeure has a duration.** Treating a dated event as a closed state is how a live condition becomes invisible. See [[finding_scope_negative_needs_the_counterparty_standard]].
- **The failure is invisible from inside the derivation.** Every step reproduced correctly — the arithmetic was right, the ledger was current, the base rate survived a full re-dating of its inputs. Reproducibility does not test scope match. See [[finding_perturb_inputs_to_test_base_rate]] and [[finding_discovery_instrument_defines_the_claim]].

**How to apply:** at registration, put the prediction's scope and the instrument's scope side by side and name every part of the claim the instrument cannot observe. If a route can fire through a channel the instrument does not watch, either narrow the claim to what you can grade, or write the blind spot into the row so a future reader can check it by hand. Also test the new wording against **today** before banking it: if the condition is already true at Made_Date, the row is defective, not a forecast ([[finding_rebased_metric_check_made_date]]). Distinguish a **new** qualifying event from a **continuing** one explicitly — otherwise a pre-existing condition satisfies a forward-looking row on day one. Related: [[finding_threshold_spec_fails_before_world]], [[finding_count_measures_intake_not_domain]], [[finding_inbound_lane_is_the_falsification_channel]].
