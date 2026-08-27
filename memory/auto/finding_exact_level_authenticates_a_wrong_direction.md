---
name: finding-exact-level-authenticates-a-wrong-direction
description: "A claim of the form '<metric> at <level>, <direction>' can be exactly right on the level and inverted on the direction — and the precision of the level is what stops anyone checking the direction. Verify the two halves SEPARATELY; a one-word trend adjective usually carries a window choice nobody stated."
symptoms: level is right but the day/trend direction is inverted · a percentage next to a price answers a different question than its column · "buffer above the line" printed as a day change · recomputing the number confirms it and the claim is still wrong · period-over-period figure differenced against the wrong prior session · same metric on three surfaces with three values
metadata: 
  node_type: memory
  type: finding
  originSessionId: 8d29eb7a-a690-4165-acd1-10f1c645b638
  modified: 2026-08-13T02:02:34.755Z
---

**A number and a trend are two claims, and they fail independently.** Written together — *"TTF at €59 and falling"*, *"unemployment at 4.3% and rising"*, *"spreads at 340bp and widening"* — they read as one fact and get checked as one fact. But the level comes from a print and the direction comes from a **window the writer chose and did not state.** The level being verifiable to the cent is exactly what stops a reader from separately interrogating the adjective.

**The instance (2026-08-12, DEWEY DR-4).** WALTER commissioned a European-energy study around an explicit central puzzle: *"THREE-PLUS impaired channels with **TTF at €59 FALLING**."* Verified against the tape:

- **The level was exact.** TTF settled **€59.07 on 2026-07-31**, the day the commission was written.
- **The direction was inverted.** July ran **+38.1%** (€42.78 → €59.07); the series was **+83.3% year-on-year**; and 7/31 sat **five sessions after a 52-week high of €63.58**.
- "Falling" was true only on a ~one-week window — a pullback off a 52-week high, inside a violent up-move.

**The consequence was not cosmetic: the entire study existed to resolve a paradox that did not exist.** "Impaired supply channels but calm prices" is a genuine puzzle; "impaired channels and a price up 83%" is just coherent. Correcting one word dissolved the framing question and replaced it with a better one (*given the price HAS repriced, what breaks?*) — which turned out to have an alarming answer the original framing would never have reached.

**Why the precision is the trap.** A wrong level gets caught: it fails a spot-check. An exact level *passes* the spot-check, and the reader — having verified something — moves on. The adjective is never independently tested, and it propagates: the same phrasing had travelled from the domain owner's state file into a second agent's context file and into the commission, unchallenged, because at every hop the number checked out.

**How to apply:**
- **Verify level and direction as two separate claims.** Confirming the level tells you nothing about the trend, and vice versa.
- **A trend adjective is a window claim — demand the window.** "Falling over what?" Compute at least two horizons (e.g. 1w and 1m/1y). If they disagree in sign, the adjective is a window choice and must be written as one.
- **Check position within range, not just recent change.** "Falling" five sessions after a 52-week high is a materially different statement from "falling" at 52-week lows. Percent-of-trailing-high is a cheap, decisive discriminator.
- **This is highest-yield on inherited framing.** Premises in a commission, task packet, or thesis header are the *least*-checked text in a workflow — they arrive as the reason for the work rather than as part of it. Treat baked-in urgency and baked-in direction as **premises to re-verify, not conclusions to act on.**
- **When you find one, fix your own copy and flag the owner's — do not edit theirs.** And say so in the ledger: a directional error in a scoping premise propagates to every downstream consumer of that commission.

Related: [[finding_relayed_level_predates_the_event]] (sibling: the level itself predates the event) · [[finding_deep_research_stale_vintage_headline]] · [[finding_normalization_choice_picks_opposite_winners]] (the same disease in a different parameter — the unstated choice picks the answer) · [[finding_new_pin_needs_trajectory_before_level_read]] · [[feedback_verify_state_before_propagating]]

---

**Instance 2026-08-23 (PROME) — the scope widens: the unchecked half need not be a TREND adjective. It can be a RELATIONAL claim.** MIDAS reported *"the fleet memory says **90–93%** while HEARTBEAT §8 and BOND's §6 say **87–93%** — a drift to reconcile."* PROME opened both files, confirmed both figures exist exactly as quoted, labelled the result **"PROME-verified"**, and sent BOND a 🟠 defect report against BOND's own work.

**Both levels were right. The word "drift" was wrong.** They are two constructions — BOND's own §3.4(c), twelve lines above the section PROME was reading: *"87–93% (univariate) or 90–93% (currency-stripped)."* ⇒ **the two verified numbers authenticated an unverified claim ABOUT THEIR RELATIONSHIP.** Confirming that two figures differ verifies the **surface**, not the **claim** — and a discrepancy report is exactly the format in which nobody re-reads the adjective, because the numbers are right there and they check out.

⚠️ **Generalised: the pattern is `<verifiable> + <unverifiable-in-the-same-glance>`, and the trend adjective is only its commonest costume.** Others seen: *"X and rising"* (window), *"A vs B, a drift"* (same-construction assumption), *"delivered"* beside a correct filename (`[[finding_record_of_an_action_is_not_the_action]]`). **Name which half you checked.** Root cause of this instance → `[[finding_summary_section_merges_what_the_body_separates]]`.

---

**Instance 2026-08-27 (REGINALD) — a third costume: the number is CORRECT, and it is in the WRONG SLOT.** Not a level+adjective, not a relational claim. A figure that is arithmetically right, freshly computed, and answers **a different question than its position says it answers.**

My bank dashboard's threshold row read **`WAL $78.72 [Thu 8/27 CLOSE, +0.08%]`** and the headline said **"`REG-T-02` UN-FIRED at the settled close: WAL $78.72, +0.93%."** The settled tape: WAL closed **$78.71**, and against the prior close of **$79.60** the day was **−$0.89 / −1.12%.** **The stock fell 1.12% and my surface said it rose.**

**`+0.93%` was a real, correctly-computed number** — the **buffer above the $78 trigger** ($0.72/78.00). It was printed where the **day change** goes. The sibling row failed the same way for a different reason: KRE's `+0.04%` was a true day change **against the wrong day** (it differenced the 8/25 close; 8/26 had been skipped).

**Every check it faced passed.** The level beside it was right to the cent. The arithmetic was right. The sign was plausible. Recomputing the figure would have *confirmed* it — because the figure was never wrong. Only asking *"what question does this number answer?"* catches it.

**The consequence was directional, not cosmetic.** The surface read *"WAL closed up, buffer intact"* on the day WAL printed the **deepest intraday breach of the entire cycle** ($77.13, below the trigger) and closed **0.91% from firing.** The desk's single most-watched threshold had its story inverted while every number on the row was defensible.

**How to apply:**
- **Verify a number is in the slot it belongs in, not just that it is true.** Ask what question the position claims it answers, then check it answers *that* one. A units/basis check catches this; a recomputation never will.
- ⚠️ **Watch for figures that are dimensionally identical and semantically different.** "Distance to a threshold" and "change since prior close" are both *a small signed percentage beside a price*. Nothing in the layout distinguishes them, so the swap is invisible and survives review.
- **For any period-over-period figure, name the reference point, not just the period.** "+0.04%" hid a skipped session; "vs the 8/26 close" would not have.
- **Duplicating a metric across surfaces is the delivery mechanism.** The same value lived on three of my surfaces and had drifted to **three different answers** (74.33 / 74.36 / 74.35) — in a cell that had already diagnosed duplication as the drift vector and then drifted anyway. **One owner, pointers elsewhere.**

Related: [[finding_distance_to_a_threshold_is_a_claim_about_its_basis]] (the sibling: quoting "X% away" without its basis) · [[finding_output_shape_implies_more_than_the_measurement]] · [[finding_derived_metric_across_vintages_biases_toward_stale_leg]]

