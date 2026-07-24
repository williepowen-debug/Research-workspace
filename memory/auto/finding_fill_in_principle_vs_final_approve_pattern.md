---
name: finding_fill_in_principle_vs_final_approve_pattern
description: "Two-stage fill approval: Will [Approve in principle] unblocks TERRY's live re-mark work; final Will [Approve] on TERRY's one-line ticket is the actual execute-authorization. Preserves rule #5 with lower Will-attention cost per stage"
metadata: 
  node_type: memory
  type: finding
  originSessionId: f3750516-6bff-44c5-b439-284c3d6ad81f
  modified: 2026-07-24T18:22:09.885Z
---

**Rule:** for a defined-risk pre-approved trade going into a live-market fill decision, use a two-stage approval pattern — [Approve in principle] (unblocks TERRY to produce the live-marks one-liner) → [Approve final] (executes to broker on TERRY's specific ticket at live marks). Preserves rule #5 (no execution without approval) while lowering the per-stage attention cost.

**Why (7/24 BRENT tail-rider fill pattern that worked):**
- BRENT delivered verdict = FILL 150/165 USO Sep-18 spread at ~$3.30-3.65 debit (extrapolated), TERRY routed for live re-mark.
- Absolutist approach: Will waits for TERRY re-mark, then reviews spec, then approves — two-step process each requiring Will attention at the same latency.
- Two-stage approach used 7/24: Will [Approve in principle] at 1:38 PM (yes, this fill path is the right one — proceed to TERRY re-mark) → TERRY produces live-marks one-liner (5-10 min) → Will [Approve] the specific ticket at live broker chain.
- **Benefit:** TERRY isn't blocked waiting for Will to re-engage after re-mark — TERRY produces immediately, Will's second engagement is faster (just reviews the exact broker-confirmed number vs the decision-rule threshold).
- **Rule #5 preserved:** no execution happens without the FINAL [Approve] on the specific ticket. In-principle is a routing/unblock, not an execute-authorization.

**How to apply:**
- **For trades that were pre-approved AS A CARRY (already Will-authorized at concept level, waiting for fill conditions):** two-stage pattern is appropriate. The in-principle approval unblocks the mechanical live-re-mark work.
- **For fresh trades never previously Will-approved:** DO NOT use two-stage; full-spec approve on the one-liner is the only path (in-principle skips the "should we even do this" question).
- **Delivering the in-principle stage well:** always name (a) the specific instrument spec, (b) the decision rule the final [Approve] will apply to (e.g., "≤$3.65 debit → fill"), (c) the fallback path if the live re-mark blows the rule (e.g., "if >$3.65 downshift to 150/160"). Without those three, in-principle is ambiguous.
- **Recording the in-principle timestamp** in the reply to TERRY + in the fill packet — creates auditable trail if final [Approve] lands hours later.

**Falsifier / edge cases:**
- If live marks between in-principle and final are moving fast (>5% intraday against the instrument), the "in principle" premise can decay — TERRY should flag if the live re-mark surfaces marks that would change the in-principle answer.
- If the decision rule is complex (e.g., depends on multiple bid/ask legs that don't move together), the in-principle approval should be scoped to the specific decision-rule threshold, not "the fill" abstractly.

**Related:** [[feedback_deploy_on_trigger_not_calendar]] · [[feedback_exit_recommendations_need_mark_context]] · [[finding_option_marks_need_live_chain]] · [[finding_terminated_notice_can_precede_delivery]]
