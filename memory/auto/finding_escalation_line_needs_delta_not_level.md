---
name: finding_escalation_line_needs_delta_not_level
description: "An escalation trigger that quotes a LEVEL fires on the standing state — escalation semantics require a DELTA from the registered state (RED/BROCK register, 7-fold day-one fire)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 82f86d84-3685-42a6-90f9-2b7b8add7baa
  modified: 2026-07-31T15:55:41.669Z
---

**The failure (2026-07, RED→BROCK PC redemption register):** RED's 7/24 ownership rec proposed an escalation line as "≥2 vehicles gated simultaneously." BROCK adopted it verbatim and it **fired 7-fold on day one** — the condition described the register's *standing world* at registration, not a change in it. BROCK correctly refused to fire it; a second trigger (BRK-30) had the same too-easy-to-fire shape the same day. The co-author of the "pattern" was the assigning agent (RED), not just the owner.

**Why:** an escalation line exists to signal *deterioration from the state you registered*. A level threshold is satisfied by the registered state itself whenever the world is already past it — so it either fires instantly (noise) or gets waived (goalpost erosion). Both outcomes destroy the line's meaning.

**How to apply:** when writing (or reviewing) any escalation/alert line, ask: *would this fire on day one against the state we are registering right now?* If yes, it is a standing-state descriptor, not a trigger. Re-shape it as an event/delta: (a) **spread** — the condition appears somewhere it wasn't (new entity crosses); (b) **growth** — the measured quantity exceeds ~100% of a frozen registration baseline; (c) **policy/behavior reversal under load** — an actor tightens while its own pressure metric is at-or-above its registered level. Related: [[finding_threshold_spec_fails_before_world]], [[finding_policy_day_print_counts_in_sustain_window]], [[finding_state_token_sweep_all_surfaces]].
