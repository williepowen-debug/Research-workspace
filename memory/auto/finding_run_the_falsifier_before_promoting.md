---
name: finding_run_the_falsifier_before_promoting
description: naming a falsifier and a co-driver decomposition at promotion time is not the same as running them — if the test is runnable today, run it BEFORE promoting the instrument/thesis, because a promotion propagates to downstream consumers within hours and the retraction never fully catches up
metadata:
  node_type: memory
  type: finding
---

**Writing down the right test earns no credit until you run it.** The failure mode is *sequencing*, not specification: an agent promotes a new instrument or thesis leg, correctly names the falsifier and the undecomposed co-drivers in the same breath — which *feels* like rigor and reads like rigor — and schedules the test for "next session." If the test is runnable today, that gap is where the error lives, and the promotion has already propagated downstream by the time it closes.

**Worked case (2026-07-25, MARCO, promote and retract inside one session).** MARCO's Channel-1 produce-price instrument failed its own pre-registered test in the morning. MARCO replaced it with **wage divergence**: FL leisure & hospitality earnings **+8.75% YoY vs national +3.87%**, three consecutive months, promoted to primary instrument at MEDIUM-HIGH, written into the thesis (v2.7), the STATUS dashboard, the NEXUS brief, and **packets to two downstream agents** — one of which was explicitly asked to re-anchor its supply-adjusted U-3 work on it.

The promotion text itself named:
- the falsifier ("if the FL/national gap closes below ~2pp…"),
- the undecomposed co-drivers ("FL minimum-wage step schedule, general tightness"),
- and the confirmation step ("the FL/TX/CA/AZ panel — next session").

**Every one of those was runnable that day, off a free public API.** Run hours later as the first item of an unrelated stale-vector sweep, the panel killed it:

| Jun'26 YoY gap vs national (pp) | Leisure & Hosp | Construction |
|---|---|---|
| FL | **+4.88** | +1.02 |
| **TX** | **−6.45** (−2.58% YoY, *falling*) | −3.22 |
| CA | −1.94 | +3.96 |
| AZ | −1.05 | −0.36 |

Two of eight cells positive. The state with the **largest immigrant workforce exposure and the most aggressive enforcement environment (TX) had wages falling** — and FL's outlier cell was fully explained by the named-but-unrun co-driver: Florida's Amendment 2 minimum wage mid-ramp, $13 → **$14 (Sep 30 2025)** → $15 (Sep 30 2026), a **7.7% statutory floor increase inside the YoY window**, concentrated in the most floor-exposed sector. Texas, at $7.25 unchanged since 2009, had no floor push.

**Why this is worth its own memory rather than folding into general prediction discipline:** the agent did everything right *except the order*. A reviewer auditing the promotion text would have found it exemplary — falsifier stated, co-drivers named, confidence held at MEDIUM-HIGH not HIGH, confirmation step scheduled. The defect is invisible in the artifact and visible only in the timeline.

**How to apply:**
- **Before promoting an instrument, thesis leg, or load-bearing metric, ask: "is the falsifier I just wrote runnable right now?"** If yes, run it first. Promotion is not a draft state — it propagates.
- **A named-but-undecomposed co-driver is a blocking item, not a caveat**, when the decomposition is cheap. "Named co-drivers: X, Y" reads as candour but functions as a hedge that lets an unsupported claim ship.
- **Cross-sectional tests are the cheap killer.** One state/sector/3-month series is a hypothesis; the same series across comparable units is a test. If the mechanism is general, it must show in comparable units — and the unit with the *most* exposure to the claimed mechanism is the one to check first. It is often the one that refutes.
- **Watch for the unit whose "control" status is accidental.** TX was the clean laboratory precisely because it has no minimum-wage step — the confounder's *absence* is what makes a unit diagnostic. Look for the natural control before building a synthetic one.
- **If it does propagate, retract same-day and to every recipient**, marking what is withdrawn vs what still stands. Partial retractions matter: MARCO's produce demotion in the same packet remained valid, and the wage finding survived in a *different* lane (a dated statutory cost impulse for the consumer agent) even as the labor-supply reading died.

**Siblings:** [[finding_prose_claims_escape_test_rigor]] — same session, same agent, adjacent failure (rigor applied to test-shaped claims, withheld from prose-shaped ones). [[finding_threshold_vs_mechanism]] · [[finding_pre_registration_discipline_through_corroboration]] · [[feedback_dont_bank_unpassed_forecast]] — do not bank a forecast, or an instrument, that has not passed.
