---
name: WALTER COP Architecture Direction
description: WALTER is evolving from inbox router to COP integrator — Will wants "outputs in the open" via a shared surface, not point-to-point inbox messaging
type: project
---

WALTER's architecture is shifting from point-to-point inbox routing toward a Common Operating Picture (COP) model where agent outputs are visible in a shared location.

**Why:** Will questioned whether the inbox system is optimal. Inbox model silos information — you have to read 15 inboxes to see everything. Will wants transparency and shared awareness.

**How to apply:** When working on WALTER, design around the three-layer hybrid (COP shared surface + signal archive + push notifications for urgent only). Don't build out the full inbox/outbox infrastructure — it may be replaced. Treat this as iterative, not waterfall. Research continues. Key models: Military COP (layered views, J3 integrator), Blackboard Pattern (shared knowledge base, agents read/write without knowing each other), IC Dissemination ("discover broadly, retrieve selectively").

Decision made 2026-04-07 in Telegram conversation with Will.
