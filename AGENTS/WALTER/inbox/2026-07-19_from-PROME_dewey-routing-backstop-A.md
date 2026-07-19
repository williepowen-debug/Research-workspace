# WALTER role change — DEWEY routing: from primary router → ledger/audit owner + backstop (Will-approved 2026-07-19)

**From:** PROME (Will-directed, in-session) · **For:** WALTER (wire into your boot/doctor at next boot) · **State:** NEW
**Companion:** DEWEY change-packet `AGENTS/DEWEY/inbox/2026-07-19_from-PROME_constrained-B-routing-change.md`

---

## What changed and why

DEWEY report routing had a **latency gap**: reports delivered in Will's async side-windows sat unrouted in `WALTER/inbox/DEWEY/` until you (or PROME) next booted, because you weren't live when they landed (prompts 11 + 13, 7/10). Will chose **Constrained B + A backstop**:

- **DEWEY now delivers at write-time** — the main DEWEY session writes create-only POINTER stubs directly into each named recipient's inbox (`AGENTS/<RECIPIENT>/inbox/…_from-DEWEY_…`) alongside the report and your handoff. Zero async gap.
- **You shift from primary router → ledger/audit owner + backstop.** You are no longer the delivery path; you are the safety net and the record.

## Your role now (the A backstop)

At boot, scanning `WALTER/inbox/DEWEY/` for NEW handoffs (your existing spawn-protocol step):
1. **Ledger (unchanged):** log/close the `DEEP_RESEARCH_FLAGGED_LOG` row for the REQ flag; do the NEW→ROUTED→PROCESSED move on the handoff.
2. **Verify delivery (NEW):** for each recipient named in the handoff's `Route as:` block, confirm DEWEY's create-only stub actually landed in that recipient's inbox. **If any route is undelivered, YOU deliver it** (the same create-only stub) — you are the fallback if DEWEY's write failed or a session died mid-delivery.
3. **Liveness flag (NEW):** any handoff still NEW / with an undelivered route beyond ~1 day → surface it in `walter_doctor` (or your boot liveness check) so it can't rot silently. PROME's boot scan of `WALTER/inbox/DEWEY/` remains the final net.

## Boundary notes

- DEWEY does NOT close ledger rows — that stays yours (audit chokepoint preserved).
- This is a **routing/ownership** change only; it does not touch your BOARD spec, the RESEARCH-INTAKE lane, or your signal-judgment mandate. Significance-gating of DEWEY reports isn't needed — the batch is pre-vetted top-N by construction.
- Wire it however fits your architecture (boot step + doctor predicate). Write a one-line ack to `outbox/` when done so PROME can close the PENDING-CONSUMPTION row.
