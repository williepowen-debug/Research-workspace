---
name: finding_settle_basis_trigger_needs_a_post_close_observer
description: "A trigger that resolves on a SETTLE or CLOSE cannot be collected by a session that runs before that close — so a correctly registered, correctly detected, correctly flagged gate can resolve into an empty room and sit ungraded for days. The surface stays fresh and merely early, so no staleness or freshness check can see it. Match the session clock to the resolution basis of every gate you are carrying."
metadata:
  node_type: memory
  type: finding
---

**What happened (VIOLET, 2026-08-20, discovered two days late).** Two Will-ratified gates were carried at "session 1 of 2, resolves today":

- **`KB-VIO-190`** — re-arm PROME's rising-vol design commission on MOVE closing **≥72.41 for 2 consecutive sessions**.
- **`KB-VIO-188`** — COR1M first-tell, **≥8.43 on 2 consecutive SETTLE closes** (settle basis explicitly, ticks excluded).

The 8/18 session booted **pre-open**, read both gates correctly, wrote *"both resolve today"* on the dashboard as its #1 priority — and closed out **before the closes that would resolve them**. MOVE printed 74.98 that afternoon, **completing the re-arm**. Nobody collected it for two days; the commission it unblocked had already been open 18 days.

**The registration was sound. The detection was sound. The SESSION TIMING silently defeated both.**

**Why no existing check catches it.** Every staleness, freshness and ledger guard asks *"is this surface old?"* The surface was **fresh** — written that morning, hours before the print. It was not stale; it was **early**. **A surface can be perfectly current and still be structurally incapable of holding the answer**, and nothing in a boot or closeout sequence compares the wall clock to the *resolution basis* of the gates being carried.

**The rule.** A registered line carries a **basis** (settle / close / intraday / report-release), and that basis implies **an observation window the observer must actually be inside**. Before closing out, ask of every armed gate: *does it resolve after I will be gone?* If yes, either stay for the print, or hand the next session an explicit instruction naming the clock — **"boot after 16:15 ET or you cannot grade this"** — not merely the gate's state.

**Generality.** This is not a data problem and not a market-hours problem; it is a **collection** problem, and it applies to any desk holding a close-basis, settle-basis or scheduled-release trigger (COT and other Friday releases, EOD settlements, post-close filings, T+1 prints). It is the same family as *an obligation that lives only on a row that gets pruned dies with that row* — **pruning has a trigger and grading has none** — but with a different mechanism: here the obligation survives, and the observer is absent.

**n=2 on one desk in three sessions**, different mechanisms both times, and both times **the detection was never the gap — the collection was.** Flagged to PROME as a possible fleet-general shape rather than proposed as a mechanism.

Related: [[finding_instrument_cadence_cannot_resolve_the_claims_window]] · [[finding_dated_carry_item_has_no_expiry_check]] · [[finding_record_of_an_action_is_not_the_action]] · [[finding_threshold_level_is_a_measurement_not_a_constant]]
