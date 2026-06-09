---
name: feedback-outbox-restraint-for-push-friction
description: "Only write to other agents' outboxes when truly critical — every outbox file adds push/merge friction Will has to absorb"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c1b747ad-fd4a-4e8e-a0ec-942958580e87
---

Only write cross-agent outbox files (`AGENTS/<OTHER>/outbox/*.md` or own `outbox/to-<OTHER>*.md`) when the signal is of **utmost importance** — a 🔴 thesis-breaking event, a position-trigger fire, or a cross-agent threshold breach that materially changes another agent's read. Default to NOT sending.

**Why:** Each outbox file becomes a tracked-file diff in the shared working tree, adding friction every time Will pushes/merges — extra files to review, extra commits to sequence, more surface area for cross-agent push-train conflicts. The cumulative cost across many agents and many sessions is non-trivial; Will absorbs it personally.

**How to apply:**
- **Send only if:** signal is genuinely actionable for the recipient AND not already implicit in their own data sources AND can't wait for next closeout's `NEXUS_BRIEF.md` refresh.
- **Don't send for:** independent corroboration of something the recipient already has, probability nudges (e.g. "your conf 35% should be 45%"), "FYI" routing, or anything that's just being a good neighbor.
- **Default channel for steady-state cross-agent signal** = `NEXUS_BRIEF.md` SENDING/WAITING-FOR tables (already in closeout step 12). Outbox is reserved for acute time-sensitive material.
- **Test before writing:** "If I don't send this, does the recipient miss a decision they need today?" If no → don't send.

**Validated:** Jun 9 2026 — I proposed an outbox to HAWK flagging Iran-Israel halt warrants HAW-09 upward revision. Will declined: HAWK can derive the same conclusion from their own monitoring, and the outbox file would just add push friction. Correct call.

Related: [[feedback_defer_push_coordinate]], [[project_messaging_overhaul]], [[feedback_cross_agent_inbox_writes]]
