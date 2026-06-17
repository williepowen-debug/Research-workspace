---
name: walter-cop-architecture-direction
description: "WALTER is evolving from inbox router to COP integrator — Will wants \"outputs in the open\" via a shared surface, not point-to-point inbox messaging"
metadata: 
  node_type: memory
  type: project
  originSessionId: b22a8af7-fe5d-4831-ba3c-935744429d5c
---

WALTER's architecture is shifting from point-to-point inbox routing toward a Common Operating Picture (COP) model where agent outputs are visible in a shared location.

**Why:** Will questioned whether the inbox system is optimal. Inbox model silos information — you have to read 15 inboxes to see everything. Will wants transparency and shared awareness.

**How to apply:** When working on WALTER, design around the three-layer hybrid (COP shared surface + signal archive + push notifications for urgent only). Don't build out the full inbox/outbox infrastructure — it may be replaced. Treat this as iterative, not waterfall. Research continues. Key models: Military COP (layered views, J3 integrator), Blackboard Pattern (shared knowledge base, agents read/write without knowing each other), IC Dissemination ("discover broadly, retrieve selectively").

**SCOPED SUPERSESSION (2026-06-17 — WALTER Routing v2):** the "don't build out the full inbox/outbox infrastructure" caution is superseded **ONLY** for a narrow WALTER signal-delivery lane: per-recipient, **create-only**, per-signal handoff files in `AGENTS/{RECIPIENT}/inbox/WALTER/` + `delivery_log.tsv` + git-derived telemetry in `walter_doctor.py` (canonical `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.2). This fixed the "in BOARD ≠ received" gap (BRENT SIG-W-20260610-001 was BOARD-only, delivered to nobody). It is additive to BOARD (BOARD stays the shared COP-style archive) — NOT a return to point-to-point inbox messaging, and it does not revive general inbox/outbox/HERMES infra. The three-layer hybrid still holds; this just makes the "push to the agent who needs it" leg real and audited. Confirmed intentional by Will. Related: [[project_messaging_overhaul]].

Decision made 2026-04-07 in Telegram conversation with Will. Scoped-supersession added 2026-06-17.
