---
name: finding-rising-stock-flat-inflow-means-slower-outflow
description: "A rising STOCK measure diverging from a flat/falling reported measure looks like hidden deterioration but is not evidence of it until you decompose the stock into inflow and outflow — a rising stock with flat inflow means the DRAIN slowed, not that failure accelerated. Ask what empties the stock, and whether that rate changed."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 8d29eb7a-a690-4165-acd1-10f1c645b638
  modified: 2026-08-13T11:43:08.643Z
---

**A stock and a flow are different claims, and a divergence between them is ambiguous by construction.** Any stock obeys `Δstock = inflow − outflow`. So a stock that rises while some reported flow measure falls has *two* possible causes — more coming in, or less going out — and they carry opposite meanings. Reading the divergence as deterioration silently assumes the outflow rate is constant. **It usually isn't, and the thing that changed the outflow is often the very reported measure you're contrasting it against.**

**The instance (2026-08-12, DEWEY C3 for CARL's masking framework).** CARL's thesis: issuer-reported credit metrics are "masked" — clean on the surface while the underlying deteriorates. The apparent proof was a large, six-quarter divergence: **bureau credit-card 90+ delinquency rose +199bps (11.13% → 13.12%) over exactly the window in which bank-reported card charge-offs fell 80bps.** Textbook masking signature, measured on primary data.

The decomposition killed most of it. The bureau also publishes the **flow into 90+**, which had been **flat at 6.93–7.18% for eight quarters**. Inflow flat + stock rising ⇒ **outflow slowed**. And the drain was identifiable: FFIEC's Uniform Retail Credit Classification requires open-end (credit-card) loans be charged off at **180 days past due** — a charge-off removes the balance from the bank's book but it *persists in the bureau's 90+ bucket*. Bank charge-off **dollars had fallen 17%**, so the stock was emptying more slowly. The divergence was mostly plumbing.

**The check that made it decisive was the historical analog on the SAME measure:** in the GFC that inflow rose *monotonically* 5.51% (2006Q1) → 10.96% (2009Q4) — no plateau. So "flat inflow" wasn't merely benign, it was the specific thing that had NOT been true in the episode being analogized to.

**Why:** stock measures are seductive because they're the headline (delinquency *rates*, inventory *levels*, backlog, headcount, case counts). They move slowly and look like accumulation of a real underlying process. But they integrate two rates, and a policy/accounting/procedural change to the outflow term moves the stock with no change in the underlying at all. A thesis built on a stock divergence can be entirely correct about the arithmetic and entirely wrong about the mechanism.

**How to apply:**
- Before treating a stock divergence as evidence of anything, **ask what empties the stock, and whether that rate changed.** Write `Δstock = inflow − outflow` explicitly and put a number on each term you can get.
- **Hunt for the published inflow series.** Sources that publish a delinquency/inventory stock very often publish the transition/flow alongside it (NY Fed HHDC p.12 = 90+ share, p.14 = flow into 90+). The flow is the less-cited and more informative series.
- **Name the mechanical drain.** Mandatory charge-off rules, write-off policies, statute-of-limitations purges, resolution/discharge timelines, reporting-retention windows. If one exists, the divergence is partly mechanical until you bound how much.
- **Run the analog on the same measure, not the same story.** "The GFC also had a big stock divergence" is not the test; "the GFC's *inflow* was rising monotonically and ours is flat" is.
- Cuts both ways: a *falling* stock with flat inflow means the drain sped up — which is exactly how genuine deterioration gets flushed off a reported surface and looks like improvement.

**SECOND INSTANCE, and it adds a selection trap (2026-08-13, DEWEY CARL-DR-1).** Same decomposition, different book: Fannie Mae's single-family serious-delinquency *rate* was **flat at 0.58%**, while the underlying flow showed **additions +7.7% YoY** and the ending stock **+7.9%**. The rate held only because removals absorbed the inflow — of which 38,150 loans were removed by *modification/workout* and 14,885 by *sale*. **The reported rate was the net of a deteriorating inflow and a large discretionary removal channel, and the inflow was the honest series.**

**The trap: you can only run this decomposition where the publisher ITEMISES REMOVALS — and that is not randomly distributed.** Fannie discloses a full flow table (beginning / additions / removals by type / ending) because it is a conserved GSE under disclosure obligations no private lender carries. Most issuers publish the *stock* only. So:

- Where the decomposition is **possible**, the entity is typically the most transparent in its class — and transparent entities tend to have **smaller** artifacts, because disclosure disciplines the behaviour.
- **Measurability is therefore correlated with the effect being small.** A modest measured artifact in the most transparent book is **weak evidence** about the least transparent ones, and reporting it as a class-wide result inverts the inference. In the live case the measured wedge (~22.5bps) came in below a pre-registered kill threshold (~50bps) — and the correct call was *"this is one leg, and selection runs against the kill,"* not *"the artifact is small."*
- **Corollary worth acting on:** before commissioning a census of this shape, ask **which entities publish a removals table at all.** That question determines where the thing can ever be *measured* rather than *asserted*, and it is far cheaper to answer than the census.

Related: [[finding_cross_entity_comparison_needs_same_perimeter]] (its "test the stock-vs-flow twin" limb, pointed at one entity across time) · [[finding_gross_flow_cannot_test_a_net_claim]] · [[finding_ratio_gauge_denominator_branch]] (sibling: the OTHER way a headline ratio moves without the underlying moving) · [[finding_composition_mask_unmask_discriminator]] · [[finding_registry_names_a_concept_tool_resolves_an_instrument]] · [[finding_verification_zero_is_ambiguous]] (kin: a check certifies its SCOPE, not your capability) · [[finding_private_by_construction_unverifiable]]
