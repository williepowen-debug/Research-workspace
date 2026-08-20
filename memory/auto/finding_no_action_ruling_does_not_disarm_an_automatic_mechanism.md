---
name: finding_no_action_ruling_does_not_disarm_an_automatic_mechanism
description: A ruling to take NO ACTION binds the humans, not the machinery — "ride to expiry" is not "expires worthless"; check what fires on its own
metadata:
  type: feedback
---

**A decision to take no action governs what PEOPLE do. It does not disarm a mechanism that acts BY ITSELF — and the ruling's own wording will read as if it covered the outcome.**

**The case (TERRY, 2026-08-20, the session before 8/21 OPEX).** Will ruled a `VLY $14P` position **LAPSE** on 8/14: *"ride to expiry, no action, no re-present."* Six days later VLY closed **`$14.12`, 0.85% above the strike.** A long put finishing **$0.01 ITM is exercised BY EXCEPTION automatically.** So the ruling would be **satisfied in full — nobody took any action — and the position would still convert to SHORT 100 shares over a weekend for ~$1 of intrinsic.**

**⇒ "RIDE TO EXPIRY" AND "EXPIRES WORTHLESS" ARE DIFFERENT CLAIMS.** The ruling makes only the first. Everyone reads it as both, because a lapse ruling *feels* terminal.

**And the surrounding record encouraged the mistake:** the branch was carried in the tasking as a *"known-accepted ~2% EbE"* tail. **Measured against the underlying's own tape it base-rated at `21.1%`** (52/247 days ≤ the −0.92% needed), with the name down 5 of 5 sessions. **A tail nobody re-measures drifts from tail to coin-flip in silence** — the ruling was correct when made and the *probability under it* moved by an order of magnitude.

**Why:** rulings are written about **intent** ("we will not act on this"), while the costly outcomes are produced by **standing automatic machinery** that never reads the ruling — broker exercise-by-exception, auto-renewal, auto-scaling, a cron, a retry policy, a default-on setting. **Nothing in the decision loop is wired to the mechanism**, so the gap is invisible from both ends: the approver believes it is closed, and the desk holding it believes it is ruled.

**How to apply:**
1. **On any "no action / let it lapse / let it ride" disposition, ask the separate question: *what happens ON ITS OWN if nothing is done?*** Name the automatic mechanism explicitly. If none exists, say so — that is also an answer.
2. **Re-measure the "it won't reach it" branch against the instrument, near the deadline** — not against the estimate that was current when the ruling was made. Base-rate it (`[[finding_base_rate_the_threshold_before_building_it]]`).
3. **Pre-register the write-back for the branch the ruling did not contemplate — BOTH directions, including the NON-fire**, so a flagged branch that doesn't happen gets closed out loud instead of rotting into a permanent open question.
4. ⛔ **This is NOT grounds to re-present a settled ruling.** The ruling stands. You are recording an uncontemplated branch, not reopening a decision — and flagging it the session BEFORE, never the Monday after.

**Sibling axis:** `[[finding_guard_scope_expires_at_the_fill]]` (a guard's SCOPE — entry-side vs post-fill) is the same family seen from the other side: there a spec did not reach far enough; here a ruling reaches the people but not the machine. Also `[[finding_dated_carry_item_has_no_expiry_check]]` — a carried assertion is a string, and reading it never evaluates it.
