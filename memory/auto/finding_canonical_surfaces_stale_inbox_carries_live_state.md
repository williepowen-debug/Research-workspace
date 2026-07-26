---
name: finding_canonical_surfaces_stale_inbox_carries_live_state
description: "cold-recovery benchmark (SAM 7/25) — every canonical surface can be internally consistent yet superseded; the decision-critical live fact sat ONLY in an unprocessed inbox packet, so any state card/summary/projection built from canonical files alone is confidently wrong; require a pending-inputs section"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9a0babb3-91ac-4b25-bdc8-888f8cc149af
  modified: 2026-07-26T03:01:54.297Z
---

State-recovery benchmark v0 (2026-07-25, SAM, `PROME/research/2026-07-25_state-recovery-benchmark-SAM.md`): a cold reader recovered SAM's canonical state near-perfectly (~175k tokens, zero material errors) — and the single most decision-relevant fact was on NO canonical surface. The Jul-21 JPY COT rebuild (−152,125, 875 contracts from SAM's registered −153K re-fire line) lived only in an unprocessed NEXUS inbox packet; every SAM-owned surface still carried the superseded "STALL at 68.1%" read, internally consistent across STATUS/THESIS/BRIEF/ledger.

**Why:** between sessions, the world moves through the INBOX first. Canonical surfaces record *graded* state; the inbox carries *landed-but-ungraded* state. "All surfaces agree" therefore measures write-back discipline, not currency — an agent's files can be flawlessly self-consistent and two prints behind the world.

**How to apply:** (1) any state card, dashboard panel, summary, or projection generated from canonical files MUST carry a pending-inputs/ungraded-inbox section — this welds the P2 state-card build to the P1/P5 exception queue (DISPOSITIONS ledger, `AUDITS/2026-07-25_system_report_DISPOSITIONS.md`); (2) when judging an agent "current," check inbox mtimes against its last session, not just surface consistency; (3) keep inbox-drain early in every boot sequence — the benchmark's cold reader found the live fact only because it read the inbox before declaring itself booted. Related: [[finding_inbound_lane_is_the_falsification_channel]], [[finding_ledger_drift_behind_narrative]].
