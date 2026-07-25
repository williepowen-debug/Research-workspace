---
name: finding_redated_falsifier_inherits_premise
description: "When you re-date a falsifier/prediction because a catalyst moved, it silently inherits the premise that forced the re-date — re-audit the CHANNEL and the premise, not just the calendar row; an inbound date correction is the trigger to re-audit the whole object."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7beb44e-7301-4b3e-b05f-59099c68ca43
  modified: 2026-07-24T22:19:07.419Z
---

A falsifier that gets **re-dated** carries forward the assumption that justified the new date. Fixing the date is not fixing the object.

**The case (RED, 2026-07-24).** CHG-028 is a **core/services** stagflation falsifier. RED re-dated it from the June CPI to the July CPI (8/13) *because* "the $100 oil spike lands in that print." CARL then falsified the premise — CPI measures the **monthly average**, and June ran downhill while July climbed from a lower base, so July energy prints negative MoM and the oil actually lands in the **August** print. But re-pointing the date at ~9/10 would still have been wrong: the August print tests the **headline-energy** line, while oil→core (airfares, freight-embedded goods, services ex-shelter) is a **2-6 month** channel. **A core-transmission falsifier cannot resolve on the first headline-energy print in any month.** The date error was caught by a counterparty; the **channel** error was found only because the correction forced a re-read of the whole object — and it was the more serious of the two.

**Why:** re-dating feels like a small mechanical edit, so it gets done as a calendar-row update rather than a re-derivation. The premise that motivated the move never gets stated explicitly, so it never gets tested. Compounding: a falsifier can also be **non-discriminating** at its new date — here, rockets-and-feathers means the August energy line prints hot in *both* the escalation and de-escalation branch, so a "hot" reading would have carried almost no information.

**How to apply:**
- When any inbound correction moves a dated row you own, treat it as a trigger to re-audit **premise + channel + discriminating power**, not just the date. Write the premise down as a sentence; if you can't state it, it isn't pre-registered.
- Ask of the new date: *does the instrument that prints on that date actually measure the mechanism this falsifier is about?* Headline vs core, level vs average, index vs name, stock vs flow.
- Ask: *does this test fire in more than one branch?* A signal that fires in every branch is not evidence — pre-register it as the null.
- **Verify a date in the same pass that creates the dated row** — not "at next boot." A row marked `[DATE EST — verify]` is a row that will be cited before it is verified. In the 2026-07-24 case five such rows were created and verification deferred; when it was actually run hours later, **3 of 4 were wrong**, including one figure the whole fleet had inherited from a single unverified source. Deferred verification is how an assumed cadence becomes a pre-registration by default (see [[finding_threshold_spec_fails_before_world]] — thresholds usually fail on their spec, not on the world).
- Check the publisher's *own* calendar, and expect access friction: some agencies (e.g. bls.gov) return HTTP 403 to both automated fetchers and browser-UA curl, so find the accessible mirror (an OMB/White House-style consolidated schedule) rather than concluding the date can't be checked.
- Related: [[feedback_dont_bank_unpassed_forecast]], [[finding_catalyst_vs_consequence_conflation]], [[finding_level_conditional_probability_remarking]].
