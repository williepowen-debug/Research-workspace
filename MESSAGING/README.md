# Direct Agent Messaging v1 — Design Package

**Status:** LIVE — FIRST COHORT (activated 2026-07-14, Will-approved): PROME → BRENT and PROME → SAM only; all other routes fail closed (`config.yaml` `write_mode: cohort`). Fleet-wide expansion remains gated on clean first-cohort exception reporting. *(Header reconciled 2026-07-25 — the pre-activation wording had outlived the activation; flagged by the external system report §3.2, see `AUDITS/2026-07-25_system_report_CONSUMPTION.md`.)*  
**Prepared:** 2026-07-13  
**Scope:** Direct agent-to-agent inbox traffic. WALTER's external-signal lane remains native.

This package translates the one-week compatibility baseline into a concrete direct-messaging contract. It does not change boot behavior, inbox behavior, WALTER routing, or canonical research ownership merely by existing.

## Package map

- `DIRECT_MESSAGING_V1_SPEC.md` — normative contract: identity, envelope, obligations, receipts, lifecycle, ownership, validation, and compatibility.
- `DIRECT_MESSAGE_TEMPLATES.md` — copyable ACTION, INFO, and receipt templates.
- `DIRECT_MESSAGE_EXAMPLES.md` — realistic PROME/NEXUS, PROME/SAM, and PROME/BRENT examples.
- `IMPLEMENTATION_PLAN.md` — build order, acceptance tests, rollout, and rollback.
- `IMPLEMENTATION_STATUS.md` — completed code, locked safety boundary, and remaining activation gates.
- `RATIFICATION.md` — Will's approved defaults and the remaining activation gate.
- `schemas/` — machine-readable v1 front-matter contracts.
- `tools/validate.py` — read-only validator.
- `tools/msg.py` — authoring/receipt engine; live writes allowlisted to the first cohort only (all other sender/recipient pairs fail closed).
- `config.yaml` — committed activation gate (`write_mode: cohort` — PROME → BRENT/SAM only since 2026-07-14).
- `tests/` — validator and compatibility fixtures.

## Supersession note

`MESSAGING/DESIGN_RATIONALE.md` remains the historical architecture rationale. Its evidence and general systems principles remain useful, but its WALTER-centered pilot framing is superseded by this package in three respects:

1. WALTER is a specialized external-signal router, not the general agent-to-agent transport.
2. Direct peer/PROME inbox messaging is the first live implementation target.
3. Rollout is network-wide for new direct messages with a compatibility window, not a week-long seven-agent pilot.

## Ratification boundary

Will ratified the recommended defaults in `DIRECT_MESSAGING_V1_SPEC.md` §16 on 2026-07-13 (see `RATIFICATION.md`). **First-cohort activation followed 2026-07-14** (Will-approved; root `CLAUDE.md` §Data Hygiene carries the fleet-facing canon). Both live routes completed full accept → integrate → receipt cycles on the 7/14 activation messages (BRENT and SAM). Expansion beyond the first cohort remains gated: clean exception reporting on the cohort, then Will approval per route.
