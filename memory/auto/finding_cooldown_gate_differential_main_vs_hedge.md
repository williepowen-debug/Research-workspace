---
name: finding_cooldown_gate_differential_main_vs_hedge
description: "A vol/cooldown gate blocks fresh MAIN-arm capital deployment (paying vega on a new directional bet) — but doesn't block a small pre-approved defined-risk HEDGE with fixed max loss. Different economics, different gate applicability"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f3750516-6bff-44c5-b439-284c3d6ad81f
  modified: 2026-07-24T18:21:46.174Z
---

**Rule:** vol-cooldown gates (e.g., OVX/VIX ratio thresholds gating oil deployments) exist to prevent overpaying vega on fresh MAIN-arm directional capital. A pre-approved defined-risk HEDGE (spread with fixed max loss) has different economics — the vega tax gets ~offset between the long and short legs, and the max-loss is capped regardless of where vol goes. **Gate-unmet correctly doesn't block the hedge fill decision.**

**Why (7/24 BRENT tail-rider fill discipline call):**
- OVX cooldown gate at 7/24 close: OVX 65.75 (p94.3), VIX 17.74, ratio 3.70 (p98.2) — decisively unmet, moved FURTHER from met than 7/23's 3.57
- **If the gate were literally read as "no oil deployment until met":** BRENT tail-rider would be BLOCKED (pass-on-chase absolutist).
- **But the gate was written for the MAIN convex arm** (fresh directional-vol capital — buying outright USO calls when OVX is crisis-priced). Tail-rider was a DIFFERENT instrument: 150/165 USO Sep-18 call spread, pre-approved 7/21 carry, ~$365 max loss defined regardless of OVX print.
- BRENT's read: the short 165C leg offsets rich vega on the long 150C leg (spread mandatory at IV 63.6%); max-loss is capped; the cooldown gate's PURPOSE (prevent overpaying vega on fresh outright bets) doesn't apply to a debit spread with fixed max loss.
- **Discipline call therefore: gate-unmet doesn't block the hedge decision. Fill decision governed by rule #6 (calls on red days, satisfied today = first genuine red day since carry) + fundamentals (both gates fired this week, no de-escalation falsifier).**

**How to apply:**
- **When a vol-cooldown gate is unmet AND a fill decision arises, first classify the instrument: MAIN convex arm (outright directional) vs pre-approved defined-risk hedge (spread with fixed max loss).**
- If MAIN: gate applies, hold.
- If defined-risk hedge with pre-approved carry: gate does NOT block; decide on the hedge's own rules (rule #6 day-color, level trigger if any, thesis intact).
- Publish the differential explicitly in the fill memo so the decision path is auditable — "gate unmet but doesn't apply here because [defined-risk / pre-approved / max-loss capped]".
- BRENT's 7/24 memo: exact template.

**Falsifier / edge cases:**
- If the hedge is NOT pre-approved (fresh idea today at rich vol), the gate arguably DOES apply — the "small hedge" carve-out shouldn't launder a fresh vega-tax purchase.
- If the max loss is small but the FILL cost is a significant fraction of remaining capital fence, gate reconsideration is legitimate.
- If OVX itself is the fundamental driver of the thesis (e.g., "buying oil vol expansion"), gate CANNOT be waived — that's the exact bet the gate is filtering.

**Related:** [[feedback_deploy_on_trigger_not_calendar]] · [[feedback_position_cost_basis_not_authoritative]] · [[finding_vrp_split_rates_vs_singlename]] · [[finding_risk_control_separate_from_sizing]]
