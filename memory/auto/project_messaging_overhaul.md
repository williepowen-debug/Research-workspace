---
name: Messaging system overhaul pending
description: Don't invest in inbox/outbox/HERMES hygiene — file-based messaging is being replaced
type: project
originSessionId: b00607de-f192-4622-ad82-473ddbff96a1
---
File-based inter-agent messaging (inbox/, outbox/, HERMES courier) is being overhauled. Will flagged this on 2026-04-14.

**Why:** The current protocol has known friction points — HERMES schedule gaps, audit trail breaks when agents pull from peer outboxes directly, manual file moves for processed state. Will plans to replace it, likely as part of broader phone signal architecture work (see project_phone_signal_architecture.md).

**How to apply:** When noticing messaging-hygiene gaps (e.g., signal read ahead of HERMES delivery, `inbox/processed/` not populated, `outbox/delivered/` lag), note the gap but don't spend effort patching it within the current protocol. Flag it, let it ride, and catch it cleanly in the new system.

**Still valid behavior:**
- Writing to outbox/ for cross-agent signals (format survives the overhaul)
- Reading inbox/ at session boot
- Deferring inbox processing unless spawned for it

**Not worth doing under current protocol:**
- Manually moving signal files into inbox/processed/ to patch audit trail
- Scripting HERMES replacements
- Enforcing strict delivery-state discipline

**SCOPED EXCEPTION (2026-06-17 — WALTER Routing v2):** the WALTER signal-*delivery* lane is now an explicit, narrow exception to "don't invest in inbox infra." WALTER writes a per-recipient, **create-only** handoff to `AGENTS/{RECIPIENT}/inbox/WALTER/` on every dispatch (recipient moves to `processed/` on consume — they never touch the same file), logged in `routed/delivery_log.tsv`, with git-derived delivered/consumed **telemetry** in `walter_doctor.py`. Canonical: `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.2. This is deliberately scoped to the WALTER→recipient delivery lane and does NOT revive general inbox/outbox/HERMES hygiene — the rest of this memory still stands. The earlier caution was about *unguarded* inbox infra; the telemetry is the guard, so the reversal is safe. Confirmed intentional by Will. Related: [[project_walter_cop_direction]].

Date logged: 2026-04-14. Scoped-exception added 2026-06-17.
