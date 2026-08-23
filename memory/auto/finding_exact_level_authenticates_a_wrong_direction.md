---
name: finding-exact-level-authenticates-a-wrong-direction
description: "A claim of the form '<metric> at <level>, <direction>' can be exactly right on the level and inverted on the direction — and the precision of the level is what stops anyone checking the direction. Verify the two halves SEPARATELY; a one-word trend adjective usually carries a window choice nobody stated."
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
