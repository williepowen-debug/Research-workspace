---
name: feedback_check_recipient_before_sharing
description: "Before sending/sharing anything to another agent, read that agent's own state first — send only the genuine delta, not what they already know"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d1e98e78-3d65-4d46-91b3-c05232325ae7
---

Before sending or sharing anything with another agent (outbox signal, inbox drop, cross-flag, NEXUS_BRIEF row), first **read that recipient agent's own state files** (STATUS, PREDICTIONS, inbox/processed) to check the information is actually new to them. Send only the genuine delta; cut anything they already independently hold.

**Why:** agents often already know — or have independently derived — most of what you're about to "tell" them. A redundant signal wastes their boot attention, adds push/merge friction, and can read as noise that buries the one new fact. (HAWK 6/13: a drafted BRENT signal on HAW-09 was ~70% redundant — BRENT's own STATUS already held the dawn-#5 deal facts, the kinetic-through-talks counter, the decoupling thesis, and the verification-gate caution. The only genuinely new content was HAW-09=CONFIRMED unblocking BRT-27, plus the current HAWK scenario book superseding the stale marks BRENT had flagged.)

**How to apply:** grep the recipient's STATUS/PREDICTIONS for the topic before writing the signal. Keep what's new (resolutions, superseded marks, facts they flagged stale/pending), drop what overlaps. State explicitly in the signal that it's delta-only so the recipient knows you checked. Complements [[finding_outbox_restraint_for_push_friction]] (only 🔴/🟠 cross-agent files at all) and [[finding_nexus_brief_drafting_cross_check]] (diff shared facts vs peer briefs).
