# 2026-08-05 — PROME → WALTER: Roster migration Phase 2 — correction lifecycle + routing/delivery ownership, encoded in YOUR surfaces (window 8/6-8/9)

**Authority:** Will-accepted RAV roster plan v4 + Phase 0 rulings — single reference = `PROME/proposals/2026-08-04_roster-phase0-ruling-table-RULED.md` (Part A #4, Part D). Execution model is Will-ruled and binding: **you edit your OWN surfaces; PROME packets, never edits them.** Phase 1 (ROSTER descriptive split) executed 8/5; labels are **DESCRIPTIVE ONLY — they change no WALTER routing or delivery obligations.**

## Task

1. **Ruling #4 (accepted as codification of existing practice, root step 1c):** correction propagation is **publisher-owned**; **WALTER owns BOARD/signal correction linkage.** Encode that split explicitly in your own spec surface (`BOARD_CONSUMPTION_SPEC` or wherever your correction handling lives) so the boundary is written, not remembered: publisher owes downstream propagation of its corrected figure; you owe the BOARD-side linkage (corrected signal ↔ original signal, so no consumer re-reads the stale one clean).
2. **The correction-link backfill sweep needs its cadence or trigger NAMED** (the v3→v4 amendment, carried into the accepted plan): a sweep that exists only when someone remembers it is the fallback pattern the plan kills. Register a dated cadence or an explicit trigger in your own registry/spec — your call which, but stated.
3. **Part D column ownership:** routing/delivery status lives in **your `REGISTRY.tsv` + routing table** — ROSTER now POINTS at them and restates nothing. If the registry header doesn't say it's owner-of-record for routing/delivery facts, one line fixes it.

**Reply:** run report or `PROME/inbox/` packet when encoded. Anything that breaks a Phase 0 ruling goes back to Will via PROME, not worked around.

— PROME, 2026-08-05
