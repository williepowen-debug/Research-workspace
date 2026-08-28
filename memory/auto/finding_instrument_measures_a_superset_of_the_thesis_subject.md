---
name: finding_instrument_measures_a_superset_of_the_thesis_subject
description: "A kill/threshold whose named instrument measures a SUPERSET of the thing the thesis is about passes every structural audit — the series is real, the count is real, the anchor is real — and fires on movement in the part you never cared about. Only a composition pull sees it."
symptoms: "kill leg looks gradeable but fires on the wrong thing; total-vs-component; the metric moved but not the part my thesis is about; falsifier nearly fired and I could not say why it felt wrong; aggregate improved while the component was flat; mix shift read as a trend"
metadata:
  type: feedback
---

**A falsification leg can name a real series, in a real ledger, with a real threshold and a real N-period count — and still be measuring the wrong thing, because the series it names CONTAINS the thesis's subject rather than BEING it.**

Every structural check passes. The cell is populated, the instrument exists, the count is present, the anchor type is right, the data is fresh. **There is nothing for a scanner, a linter, or a row-level reviewer to flag.** The defect is only visible if you pull the *composition* of the named series and ask what share of its movement belongs to the thing you are actually claiming.

## Measured instance (FLG, 2026-08-28, at the primary)

A thesis about **NYC rent-regulated multifamily** carried a thesis-kill:

> `loans_qoq_pct > 0` for 2 consecutive filed quarters — *i.e. "the deleveraging stopped, the bear case is wrong."*

It had been flagged by the fleet architect and by the coordinator as **"one print from firing."** At the primary:

| Book | 6 months | |
|---|---:|---|
| **Multi-family** — *the thesis's actual subject* | **−7.08%** | still running off hard |
| Commercial & industrial | **+21.99%** | +$3.3B on $4.8B of new originations |
| **Total loans** — *the named instrument* | **+0.42%** | ⚠️ **turned positive** |

**The kill was one quarter from retiring a rent-regulated-multifamily thesis on the strength of commercial-and-industrial loan growth.** The two books have nothing to do with each other; one merely contains the other in the aggregate.

## Why it survives review

- **It is not a missing instrument.** The named series existed, was populated, and was correctly cited — so it is invisible to the "leg has no metric surface / `UNGRADEABLE`" class of finding, which is the check most likely to be pointed at a kill rail.
- **The aggregate is usually the *better-known* number.** Total loans is the headline; the component needs a filing pulled apart. **The more canonical the series, the likelier it is to get named for a claim it does not fit.**
- **A mix shift reads as a trend.** The aggregate genuinely moved. Nothing is stale, nothing is mis-parsed, nothing disagrees.

## ⚠️ Check the DIRECTION of the error — it decides who ever notices

Here the defect made the kill **EASIER** to fire, so the rail was biased toward **retiring a live thesis**. That is the silent direction: a thesis killed early just looks like discipline, and **nobody files a complaint about a falsifier that worked.** The mirror case (an instrument that makes a kill harder) produces a thesis that never dies, which at least eventually attracts suspicion. See `[[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]]` — the sign is fixed, but which direction is *dangerous* belongs to the test it feeds.

## How to apply

> ★ **For every threshold, ask: does the named instrument measure the SAME PERIMETER as the claim — or a superset that contains it?** If a superset, either re-point the instrument at the component, or state explicitly what share of the aggregate the subject is and what movement in the remainder would false-fire it.

- **The tell is a noun mismatch between the claim and the cell.** Claim says *multifamily / rent-regulated / this segment / this counterparty*; cell says *total / aggregate / portfolio / index*. **Read the two nouns side by side — that comparison is the whole check, and it takes seconds.**
- **Run it when you write the leg, not at audit.** At audit the cell looks finished, which is exactly the state that stops re-derivation.
- **A composition pull is the only test.** No amount of freshness, reproducibility or format checking reaches it — the number is correct, current and reproducible, and still wrong for the claim.
- **Aggregates that improved deserve the split by default.** In the same filing, an improving *total* net-charge-off rate concealed a **flat-YoY multifamily** rate; the improvement was composition, not repair. **Same defect class, applied to a read instead of a kill.**

**Related:** `[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]` is the case where the instrument is ABSENT; this is the harder case where it is PRESENT and wrong-by-superset. `[[finding_cross_entity_comparison_needs_same_perimeter]]` is the cross-sectional twin (same metric, different entities); this is the within-entity form (same entity, wrong subset). `[[finding_composition_mask_unmask_discriminator]]` is the tool. `[[finding_verified_figures_do_not_verify_the_shape_claim]]` — verified numbers do not verify what they are claimed to be about.
