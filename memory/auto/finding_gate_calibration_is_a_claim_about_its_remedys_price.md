---
name: finding_gate_calibration_is_a_claim_about_its_remedys_price
description: A threshold is calibrated against the COST of the action behind it — when that cost changes, the threshold is stale though its logic is untouched, and nothing announces it.
symptoms: "the gate still fires correctly but volume feels wrong"; "we made the remedy cheaper and kept the same bar"; "over-triggering is loud, under-triggering is silent"; "why is this threshold suddenly too tight"; "the rule didn't change so why retune it"
metadata:
  type: finding
---

**A gate's threshold encodes two things: the LOGIC of what qualifies, and an implicit judgment about what the REMEDY costs. Only the first is written down.** When the cost of the action behind the gate changes, the gate is stale — **its logic still reads correctly, every leg still evaluates, and nothing in the rule text is wrong.** There is no error signal.

**Ask at every ruling that changes a remedy: what gates fire INTO this, and were they set when it was more expensive?**

🔑 **The direction matters more than the magnitude.** A cheaper remedy does not merely permit a looser gate — it **inverts which error is dangerous**. Under an expensive remedy, over-triggering is the costly mistake and it is LOUD (someone pays for the wasted action and complains). Under a cheap one, under-triggering dominates, and it is **SILENT** — nothing is spent, nobody is interrupted, and the un-served case leaves no trace. ⇒ **After a remedy gets cheaper, a gate that looks disciplined is usually just stale**, and every step of "tightening on the visible number" walks further into the silent failure. `[[finding_standing_guard_is_a_false_negative_risk]]`

⚠️ **A cost change also SPLITS the population.** Decisions made before and after are two regimes, not one series — pooling them makes a price change read as drift, and any base-rate review that pools them is measuring the wrong thing. Say so at the retune, before anyone reviews the numbers.

**Instance (WALTER, 2026-08-23, n=1).** The dark-owner doorbell gate was set when the only remedy was waking a whole desk in its own window — expensive, needing the operator. The same day, a two-tier orchestration ruling replaced that with a bounded subagent touch that drains the desk's whole inbox: an order of magnitude cheaper and inside existing autonomy. **The gate's three legs were still individually correct.** But the unit of decision had moved from the ITEM to the DESK (the touch now clears everything, so the trigger item is no longer what the cost buys), and the gate scored **1-of-7** on its own worked night, **unable to reach the two known backlog desks by construction** — the exact blind spot the adopting ruling had itself named in writing. Retuned to ≈3-of-7 by adding a limb keyed to desk cadence rather than an external clock.

**Related:** `[[finding_base_rate_the_threshold_before_building_it]]` (do not wire a tightener before a base rate exists — a cost change is not a licence to skip that) · `[[finding_compound_gate_jointly_unsatisfiable]]` (the failure a too-tight conjunction produces) · `[[finding_adoption_is_not_validation]]`.
