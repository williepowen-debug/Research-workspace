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

---

## Facet added 2026-08-24 (PROME, live instance): n+1 — **the SAME mechanism fired for 51× the money, on a position that never entered the decision loop at all**

**What happened.** The instance above is the `VLY $14P` — flagged the session before OPEX, watched, and worth **~$1,400** if it converted. On that same 2026-08-21 expiration a **`QQQ $713` CALL**, bought that morning for **$174.66**, closed at **$713.44 — $0.44 ITM — and was auto-exercised by exception into 100 shares at exactly $713.00 = a −$71,300.00 debit** in a Traditional IRA holding **$17,115.01** of cash. Fidelity sold 77 shares at $708.25 the next morning to cover, leaving the 23 the cash could fund. Total cost ≈ **−$679**; the *scary* number was never a loss, it was a purchase.

**⇒ THE COVERAGE HOLE IN THIS MEMORY'S OWN REMEDY, and it is the point of the facet.** Rule 1 above says *"on any no-action / let-it-lapse disposition, ask what happens ON ITS OWN."* **That trigger is wired to the DECISION LOOP — so it can only fire on a position that reached a disposition.** The QQQ call was never ruled on, never on a PROME rail, and `FORGE/STATUS.md` records the whole class as *"Will-direct, short-dated, **on no PROME rail and owned by no agent**"* — and, on the 8/14 capture, *"the class is EMPTY."* **The fleet's EbE watch was scoped to the position the fleet could SEE.** ⛔ **A remedy attached to the decision loop cannot cover what never entered the decision loop** — and the un-ruled position is exactly the one nobody re-measures.

**⇒ SECOND, AND IT IS THE SIZING LESSON: magnitude is set by the CONTRACT, not by the attention.** Attention tracked the $1,400 item; the contract sized the $71,300 one. **A long option's premium is not a proxy for the obligation it can convert into — here 408:1** ($174.66 → $71,300). **The obligation is never balance-checked**, because exercise is not an order: buying power is verified once, at entry, against the *premium*. Nothing checks whether the account can settle the *strike*. In a cash account or IRA — where carrying a debit is not permitted at all — the broker's sell-to-cover is not a risk decision, it is forced.

**⇒ THIRD: the direction generalizes past puts.** The record above is a long PUT converting to short stock. This is a long **CALL** converting to **long stock and a cash debit**. Same machinery, opposite sign, and the call case is the one that produces a *debit the account cannot fund* rather than a position it cannot hold.

**Added to "How to apply":**
5. **Run the question against the BOOK, not against the ruling list.** Once per expiration week: *which contracts expire this Friday, and what does each become on its own if untouched?* — asked of every open contract, including the ones on no rail and owned by nobody. **The positions with no owner are the ones with no watcher.**
6. **Size the tail by the STRIKE, not the premium.** `100 × strike` is the real number a long option can hand you. Compare it to settleable cash before expiration day, not after.
7. **Near-the-money on expiration day is the whole exposure.** $0.44 separated "lose $174.66" from "owe $71,300." **A cheap option that is nearly ATM into the close is not a small position** — it is a coin flip between nothing and full notional, and no account surface warns you which way it landed until the shares appear.
