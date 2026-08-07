---
name: finding_named_risk_underweighted_is_its_own_error
description: Naming a risk then pricing it low is a distinct failure from missing it — audit whether your probability matches the caveat you already wrote
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f37d1164-d8c9-455c-bad6-85db2526d26c
  modified: 2026-08-07T20:28:36.367Z
---

When a forecast fails, the reflex post-mortem is *"what did I miss?"* — but the more common and more
correctable failure is that **you named the mechanism, wrote it down, and then priced it too low.** These
are different errors with different fixes, and collapsing them into "I missed it" hides the one you can act on.

**Worked case (SAM, 2026-08-07).** SAM held a carry-convexity thesis whose grade rested on CFTC positioning
fuel. On 8/2 and again on 8/4 SAM wrote, explicitly, that `SAM-22`'s mechanism — *intervention forces mass
cover* — was one of **two named paths** by which the grade could die, and stamped the grade itself
**PROVISIONAL** because the fuel measurement predated the intervention. Then SAM registered the resolver with
**45%** on the thesis-favourable branch and **~25%** on the branch that mechanism implied. It fired: positioning
went 90.8% → 25.3% of peak in one week. **The mechanism was not missed. It was documented, flagged, and
under-weighted.**

**Why it happens:** writing the caveat *discharges the felt obligation*. Once the risk is named on the page it
feels handled, and the probability gets set by the frame you are already carrying rather than by the caveat you
just wrote. A PROVISIONAL stamp and a confident modal lean can coexist in one document without either author or
reader noticing the contradiction.

**The check, before registering any probability:**
- Grep your own recent work for the caveats **you** wrote about this call. For each, ask: *does my number
  reflect this, or merely sit next to it?*
- If a document calls a grade **PROVISIONAL / CONDITIONAL / UNCONFIRMED**, that word should be visible **in the
  probability**, not only in the prose. A provisional grade with a confident modal lean is the tell.
- Ask which branch you would have to be *surprised* by. If a named, written-down mechanism firing would not
  surprise you, it is not a ~25% branch.

**What this does NOT license:** inflating tail probabilities generally, or retro-fitting after the outcome.
The discipline is to reconcile *at registration time* — and to keep the resolver frozen and run on the letter
afterwards regardless. In the worked case the surrounding process held (frozen resolver, book flat, $0 at risk);
it was only the number that was wrong.

Related: [[finding_confidence_priced_against_thesis_not_letter]] · [[finding_priced_probability_destroys_surprise_room]] ·
[[feedback_dont_bank_unpassed_forecast]] · [[finding_standing_guard_is_a_false_negative_risk]]
