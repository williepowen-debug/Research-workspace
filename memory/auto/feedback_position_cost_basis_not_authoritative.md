---
name: position-cost-basis-not-authoritative
description: Never cite position cost-basis / P/L from STATUS or state-file figures as authoritative — confirm with Will; recorded fills can be wrong and even fail to reconcile
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9fe6fa60-1e2d-4ddd-baf5-e13312cf2917
---

Never cite position **cost-basis or P/L** from a STATUS / state-file figure as authoritative. Confirm against Will's ground truth before using it in any R:R, P/L, or exit-decision framing.

**Why:** 2026-05-28 — SAM's STATUS recorded a "$57.48 blend" (from per-tranche fills 8 @ $57.36 + 5 @ $57.66) that didn't even reconcile (a blend can't exceed both component prices). Will's ground-truth avg cost was **$58.32**. The error flipped live P/L from +0.4% to **−1.1%** and R:R from 1:1.86 to 1:1.13 — materially changing the position read. Recorded fills drift from reality; state files are a convenience copy, not the broker.

**How to apply:** this is the position-level corollary of root CLAUDE.md rules #3 (agent data can be hallucinated — verify) and #4 (prices must be live — never cite from STATUS). When a decision turns on entry price, blended cost, or unrealized P/L, treat the state-file number as a prompt to confirm with Will, not as the answer. Relates to [[feedback_exit_recommendations_need_mark_context]] (surface the execution mark before close-now recommendations).
