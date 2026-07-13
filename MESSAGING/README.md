# Direct Agent Messaging v1 — Design Package

**Status:** IMPLEMENTATION-READY PROPOSAL — NOT YET LIVE  
**Prepared:** 2026-07-13  
**Scope:** Direct agent-to-agent inbox traffic. WALTER's external-signal lane remains native.

This package translates the one-week compatibility baseline into a concrete direct-messaging contract. It does not change boot behavior, inbox behavior, WALTER routing, or canonical research ownership merely by existing.

## Package map

- `DIRECT_MESSAGING_V1_SPEC.md` — normative contract: identity, envelope, obligations, receipts, lifecycle, ownership, validation, and compatibility.
- `DIRECT_MESSAGE_TEMPLATES.md` — copyable ACTION, INFO, and receipt templates.
- `DIRECT_MESSAGE_EXAMPLES.md` — realistic PROME/NEXUS, PROME/SAM, and PROME/BRENT examples.
- `IMPLEMENTATION_PLAN.md` — build order, acceptance tests, rollout, and rollback.

## Supersession note

`MESSAGING/DESIGN_RATIONALE.md` remains the historical architecture rationale. Its evidence and general systems principles remain useful, but its WALTER-centered pilot framing is superseded by this package in three respects:

1. WALTER is a specialized external-signal router, not the general agent-to-agent transport.
2. Direct peer/PROME inbox messaging is the first live implementation target.
3. Rollout is network-wide for new direct messages with a compatibility window, not a week-long seven-agent pilot.

## Ratification boundary

Before implementation changes live behavior, Will should ratify the decisions listed in `DIRECT_MESSAGING_V1_SPEC.md` §16. Ratification should then be recorded in the repository's canonical decision surface and reconciled with root instructions.

