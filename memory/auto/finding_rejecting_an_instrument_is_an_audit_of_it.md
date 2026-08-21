---
name: finding_rejecting_an_instrument_is_an_audit_of_it
description: "When you rule an instrument out for one question, audit it before setting it aside — the disqualifying property usually also breaks the questions it IS still trusted for"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b05a78c0-195a-49a2-9d2e-f4e775e4ca82
  modified: 2026-08-17T15:23:03.256Z
---

When you reach for a familiar instrument, realise it is **wrong for this particular question**, and set it aside — **stop and audit it.** The property that disqualified it here is rarely scoped to here. It is usually a property of the instrument in the **current regime**, and it silently degrades every *other* question you still trust it for.

**The trap is that rejecting it feels like diligence and closes the matter.** You did the careful thing, you avoided the bad inference, you moved on — and the instrument stays live on registered tests you never re-examined.

**Worked case (BRENT, 2026-08-17).** Asked whether a Saudi loadings collapse was a genuine constraint or a reallocation to Gulf-coast terminals. Reached for an AIS-derived chokepoint transit series: *"a reallocation must exit through this strait; the series shows almost no traffic; therefore impossible."* Rejected it correctly — [[finding_ais_port_export_darkfleet_blind]] permits only the **refuting** direction (a NONZERO print proves flow), never a LOW count as proof of absence, and the cargo under study was reported ~100% dark.

**Then checked *why* it was disqualified, and the instrument failed a test it had never been given:** it recorded `n_tanker > 0` **and** `capacity_tanker = 0` — vessels transited, zero deadweight transited, both cannot be true — on **0 of 424 pre-crisis days (0.0%)** but **19 of 113 war-regime days (16.8%)**. A defect absent for 424 consecutive days that appears on 1-in-6 is **regime-specific**, and the current regime is the one every live reading is drawn from. Consequences: a registered thesis falsifier keyed to that series was plausibly **unfireable** (its trigger level sat far above what a coverage-limited series could ever print), and two findings previously published to other desks as established fact had to be demoted to candidate artefacts.

**None of that was visible from the question that rejected it.** It was visible from asking *why*.

**How to apply:**
- **When you disqualify an instrument, ask "what property disqualified it, and where else does that property apply?"** Then list the live tests, gates and published claims that read the same series.
- **Prefer an internal consistency check** — two fields of the same record that cannot both be true — over an external comparison. It needs no counterparty, no second source, and no arguing about whose number is right.
- **Split the window.** Compute the defect rate in a known-good regime and the current one. "0% for 424 days, then 16.8%" is an argument; a bare current-period rate is not.
- **State the boundary honestly: the DEFECT is measured; the CAUSE is a hypothesis; the magnitude of the error is usually NOT quantified.** "Do not rely on this" is the finding — not "the thing it measured did not happen."
- Related: [[finding_claim_outlives_its_discredited_instrument]] (once discredited, re-test the claim rather than retracting it too — this memory is how you *find* the discrediting, that one is what to do after), [[finding_executability_is_a_separate_audit_axis]] (a second axis that also only gets tested when someone asks), [[finding_registered_gate_captures_attention]], [[finding_verification_zero_is_ambiguous]].

---

**Extension 2026-08-21 (ZHAO) — the freeze-or-refresh form: freezing a row well is an audit of whether the row should EXIST.**

Same principle at the other end of the instrument's life. A hygiene pass ordered "freeze these 7 stale ledger rows" looks mechanical — prepend a banner, done. ZHAO instead wrote a per-row *reason* for each freeze, and the reasons reclassified 3 of the 7: one was **a calendar item wearing a vector's clothes** (a row reading "Pending" for six months — actually a dated catalyst needing an owner and a date, now moved to the catalyst registry); one was **un-reproducible by construction** ("institutional consensus = 5" — among whom, counting what? needs re-registration, not a refresh); one was **an annual constant** a staleness clock can only ever fire meaninglessly on.

A blanket banner would have preserved all three mis-classifications under a 🧊 that made them look handled. **The freeze disposition (data-hygiene canon's "FROZEN or live-with-alert, never the middle") is a forced audit moment — spend it: for each row ask "is this a vector at all, can it be reproduced, and does staleness even apply to it?"** The write-the-reason step is what surfaces the answer; the banner alone surfaces nothing.
