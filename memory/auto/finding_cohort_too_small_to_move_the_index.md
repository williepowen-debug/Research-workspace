---
name: finding_cohort_too_small_to_move_the_index
description: "Before attributing an index move to a named cohort, compute the widening that cohort would need given its index WEIGHT — the loudest cohort is often too small to be the driver"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e63e533e-a4cd-4206-bda7-e32734df44b3
  modified: 2026-07-30T20:44:45.443Z
---

Before attributing an aggregate index move to a named cohort, do the weight arithmetic **first**: `required cohort move = index move ÷ cohort weight`. If the answer is implausible, the cohort is not the driver — no matter how much stress it is visibly under.

**Worked instance (LIQUID, 2026-07-30).** HY OAS widened +19bp and the whole fleet's live narrative was AI-capex credit — Oracle CDS at a record, NVDA CDS at a record, CoreWeave sweetening a $2.6B loan by ~+140-165bp all-in the day before commitments closed. Every visible sign said "AI credit is doing this." But AI/data-center HY is only **~4-6% of index market value**, so for that cohort *alone* to produce +19bp it would have to widen **+320 to +475bp**. It widened maybe +50-120bp. **Ceiling on its contribution: 3-6bp of the 19.** The actual driver was broad developed-market beta — confirmed independently by Euro HY (which has ~zero AI-infra issuance) widening 0.84x the US move.

**Why:** stress is *salient* where it is loudest, but an index is a *weighted average*. Those two facts routinely point at different cohorts, and the salient one wins every narrative contest because it comes with headlines, records, and named issuers. The arithmetic is one division and it is decisive; skipping it means an attribution built entirely on availability. Both things were true at once here — AI credit was genuinely the epicentre, moving **~8x the index** at issuer level, *and* it was negligible in level contribution. **Leading in MAGNITUDE ≠ driving the LEVEL**, and a good attribution has to say both.

**How to apply:**
- Run the division before writing any attribution narrative, not after. It is cheap enough that there is no excuse for ordering it second.
- State the cohort weight and its source explicitly — the estimate carries the whole conclusion, so an unsourced weight makes the finding unreproducible.
- When the arithmetic rules a cohort out, do **not** conclude the cohort is fine. Report both legs: "epicentre of stress, negligible driver of the index." Collapsing to either half alone is wrong.
- Corollary for the other direction: if a *small* cohort genuinely could produce the move, that implies a violent cohort-level repricing that should be independently visible at issuer level — go look for it, and treat its absence as a refutation.
- Sanity-check the aggregate against its components: weighted component moves should reconcile to the index move within a small residual. A large residual means the weights, the components, or the story is wrong.

Related: [[finding_blended_index_masks_bifurcation]] · [[finding_decouple_idiosyncratic_from_systemic_leg]] · [[finding_normalization_choice_picks_opposite_winners]] · [[finding_proxy_segment_masks_trigger_series]] · [[finding_loadbearing_number_must_be_reproducible]]
