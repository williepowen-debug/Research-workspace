---
name: asymmetric-records-need-reconciliation
description: "agent records \"I did/asked/delivered X\" but never diffs the counterparty's state; the loop rots silently — reconcile at boot"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7d6bcdae-4f87-4acf-a2e1-838edc9299fd
---

**Fleet-level class-of-bug, named by PROME 2026-07-03 after 3 agents hit it the same day.** An agent writes a record asserting "I did / asked for / delivered / am awaiting X," but the confirmation loop *from the counterparty's side* is never structurally checked — so the record and reality drift apart silently.

Same-day instances: DAEDALUS HANDLE_SWEEP banners said "DRAFT" after items were dispositioned 7/1; WALTER's LIAISON manifest said RED/REGINALD "awaiting Turn N" when both had already closed/archived the channel from their side; PROME's ACTIVE_DECISIONS write-back gap after cross-agent dispositions (PAT-032). **B1 (WALTER delivery) is the same shape at the messaging layer:** WALTER logs "delivered" but the recipient's §8.1 consume-step never fires, so the loop stays open (~220 handoffs delivered-but-unconsumed; RED red-teamed on partial WALTER input for weeks).

**Mechanism:** asymmetric records with no reconciliation check. **Fix (always the same):** at boot, DIFF your records against the counterparty's *actual* state — your own "I did X" note is not evidence the loop closed. WALTER already has one instance built right: the `delivered_but_unconsumed` doctor check IS that reconciliation (it's *why* B1 was visible at all; only adoption of the consume-step stalled).

**Corollary — a self-audit that reads an agent's own summary docs inherits their staleness.** WALTER's 2026-07-03 arch/infra audit flagged the bot-token, the auto-memory index, and the LIAISON threads as "stalled" — all three were stale (handled / trimmed / archived-from-the-other-side); the audit had read WALTER's own STATUS/MEMORY, which had drifted. Ground-truth-verify each "stalled" finding against the live artifact (tree, file, data, counterparty state) before treating it as live work. Will's "is this still relevant?" caught all three.

**Discipline:** any doc recording a cross-agent action ("sent", "delivered", "awaiting", "dispositioned", "flagged", "DRAFT→shipped") needs a boot-time reconciliation against the other side. The write is a claim, not a confirmation. Cross-fleet pattern → encode in DAEDALUS's meta-agent lane. Related: [[finding_board_lags_agents_not_vice_versa]], [[feedback_suspect_fresh_pull_over_curated_record]], [[finding_freshness_audit_vs_caught_up]].
