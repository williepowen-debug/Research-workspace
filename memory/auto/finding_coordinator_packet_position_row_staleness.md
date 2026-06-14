---
name: finding_coordinator_packet_position_row_staleness
description: "In a coordinator/Orc packet derived from a committed STATUS, the operator-actioned (position/trade) rows are the most likely to be stale vs the live session — assert primary-sourced rows, verify position rows against same-session operator calls before applying"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ba9df9b0-f19f-47c3-94f4-fd590702182d
---

When a coordinator (Orc) hands a domain agent a sweep/amendment packet built off the last **committed** STATUS, the price/yield/spread rows are safe to assert — they're primary-sourced (FRED/yfinance/ICE) and the coordinator can recompute them independently. The **position/trade rows are not**: they get actioned by the operator inside the live agent session, which the coordinator cannot see, so a packet can carry a closed or written-off position as still "live."

6/13/26 case: Orc's Friday-close packet re-marked TEN ($37.11→$38.77 ITM) and treated HYG as an open close/expire decision. But Will had **closed TEN and cut HYG that same LIQUID session** — invisible to Orc, whose packet was built off the 6/12 committed STATUS. LIQUID correctly overrode: didn't write the TEN mark ([[feedback_position_cost_basis_not_authoritative]]), kept HYG written-off. Orc conceded both and banked the rule: tag any position edit "verify against same-session operator calls before applying" rather than asserting it.

**Why:** fresher same-session operator evidence beats a coordinator's stale authority; the loop is working when the domain agent overrides. **How to apply:** receiving a packet — apply primary-sourced data rows on verification; for position/trade rows, reconcile against this session's operator actions FIRST. Sending a packet — flag position rows as "verify live," don't assert them. Sibling of [[feedback_verify_counts_before_propagating]] and [[finding_just_read_artifact_frame_contamination]]; the deviation is also a case of [[finding_subagent_escalation_mode_discriminator]] (money/position = block-and-verify, not default-apply).
