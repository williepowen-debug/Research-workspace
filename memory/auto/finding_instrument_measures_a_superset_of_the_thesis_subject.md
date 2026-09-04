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

**Instance (BOND, 2026-09-02, n+1):** TreasuryDirect files 2-Year FLOATING RATE NOTES as `securityType Note · originalSecurityTerm 2-Year` — indistinguishable from nominal 2Y notes on every field BOND's auction grader keyed on; only `floatingRate=Yes` separates them. 43 FRN rows sat in the nominal-2Y benchmark pool for the tool's whole life; the 2Y indirect MIN, dealer MAX and 15th-pctile bar were all set by FRN prints, and the desk had written a rationale for why the 2Y dealer distribution was "genuinely that wide." **Tell that finally surfaced it: the 2Y window filled 12 slots in 5 months while every sibling tenor took 11–12 — a composition anomaly visible only when windows were printed side by side.** Contaminated bars were LOOSER, so every grade cleared them and no verdict changed — the superset failed silent in the direction of no alarm. Fix: filter on the primary's own type flag, with a raise when the flag list is unavailable.


**Instance (ORACLE, 2026-09-04, n+2) — the superset is over TIME, not composition, and the error direction is FIXED.**

Two desks were carrying a "September Fed" probability that no September contract ever printed. Prediction venues list **three** different Fed-hike contracts and they are routinely confused:

| contract | 9/1 value | what it prices |
|---|---:|---|
| **September MEETING** — *the claim's actual subject* | **54.5%** | a hike **at** that meeting |
| by-**October** cumulative | **64.5%** | a hike **by** then (Sept **or** Oct) |
| **2026 aggregate** | **71.5%** | a hike **anywhere** in the year |

BOND STATUS carried *"Sept HIKE ~65–68% priced"* — bracketing the **by-October cumulative**, matching no September contract on either venue. Measured against the instrument distribution: `KL = 0.061 bits`. Every structural check passed: the series was real, live, deep, correctly quoted, freshly dated. **Only the noun was wrong.**

- **⭐ The temporal superset has a FIXED ERROR SIGN, which the composition form does not.** A cumulative by-date contract is `P(event by T₂) ≥ P(event at T₁)` **by construction** — so a cumulative read as point-in-time **always reads too hawkish/too high, never too low.** You do not need a composition pull to know the direction; you need only to notice the preposition. **"by" vs "at" is the entire check.**
- **It recurred at a second desk three weeks after being ruled at the first.** ORACLE ruled the identical mislabel on NEXUS's board 8/18 (a `71.5%` *aggregate* carried as Sept-specific); NEXUS corrected it in place 8/28. BOND then reproduced the same error class independently on 9/1. **Two desks, same defect, no contact between them ⇒ this is a property of how the numbers are PUBLISHED, not of either desk's care.** Venues name all three contracts "Fed rate hike"; the distinguishing word is a preposition in the question text, which is exactly the part a relay drops.
- **The contrast case in the same session shows what this defect is NOT.** A separately relayed figure — *"Fed 50bp CUT, CME ~74.5% for September"* — sat `KL = 6.619 bits` from the instrument, **~108× further**, with the sign inverted (both venues priced any-cut at ≤1%). **A superset mislabel is a small-KL error that survives review precisely because it is nearly right; a transcription/direction error is a large-KL error that anyone checking would catch.** Ranking the two in bits is what separated "wrong contract, right story" from "not this universe" — and they need opposite remedies: relabel vs re-verify at source.

> ★ **Extension to the rule: when the instrument is a by-date or cumulative contract, read the PREPOSITION before the number.** "by" ⇒ superset over time ⇒ biased high. State the horizon in the same breath as the figure — *"52.5% at the September meeting"*, never a bare *"52.5% Fed hike"* — because a bare figure has no horizon attached and the next reader will supply the wrong one.
