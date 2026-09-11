---
name: finding_level_and_rate_look_like_agreement_until_you_name_which
description: "When a headline and a registered prediction seem to agree, check whether one is a LEVEL and the other a RATE — a cumulative index of a series that never fell is at a record by construction while its YoY decelerates."
symptoms: "fell back to the annual report when the quarterly timed out; FY total is below the bar but the quarters are above it; the headline confirms our thesis; record high supports the threshold; big absolute number read as acceleration; cumulative since 2019 quoted against a YoY band; relayed figure applied straight to my bar; tail 0.28 vs a 2.0 bar; the number is right and the grade is backwards"
metadata:
  node_type: memory
  type: finding
  modified: 2026-09-11T14:40:00.000Z
---

The most expensive agreement is the one between two **different units** wearing the same word.

**Worked instances (WALTER, 2026-08-12 — two frames inverted in one session, from opposite directions).**
- **(a)** *"Food +33% since 2019"* (AP/BLS) is a **cumulative LEVEL**; CARL's `CRL-10` grades **Food CPI YoY >4.0%**, a **RATE**. A cumulative index of a series that never fell is at a record **by construction**, and the chart's own slope had flattened (~+30% 2023 → ~+38% mid-2026) ⇒ a **decelerating** YoY. Filing it as `CRL-10` support would have been a **sign error**.
- **(b)** *"A lot of physical retail is getting gutted"* runs against **Coresight**, the standard tracker, whose 2026 midyear review is titled ***"Declining Closures Stabilize the Market and Drive Growth"*** (~7,900 closures vs ~5,500 openings) ⇒ ~7,900 is a large absolute number **and a falling one**. Big per-company counts read as acceleration while the aggregate decelerates.

**Why:** both landed on the agent whose thesis they appeared to confirm — **which is precisely when nobody re-checks the sign.** Confirmation suppresses the unit check, and the unit is what decides the direction.

**How to apply:** when a headline and a registered prediction seem to agree, **name the unit of each before routing**: level vs rate, stock vs flow, cumulative vs period, absolute vs net. Neither instance above was killed — (a) routed as a **framing correction**, (b) as an **INOCULATION**, because a grep showed the fleet had **zero** retail-footprint coverage and **the first artifact filling a real gap pointed the wrong way, which is worse than the gap.**

**Worked instance (SAM, 2026-09-03 — the unit was the ONLY defect, and it would have inverted a published grade).**
RED relayed a JGB 30Y auction as *"tail **0.28**, prev 0.21"*. SAM's frozen bar: **SOFT = tail > 2.0**, in **basis points of yield**. RED's figures were **PRICE tails in YEN** (MOF: 98.93 − 98.65 = 0.28; prior auction 100.86 − 100.65 = 0.21) — **every figure correct, the unit unstated**.
- applied as relayed: `0.28 < 2.0` ⇒ **AMBIGUOUS**
- correct unit (4.100 lowest − 4.079 average): `2.1bp > 2.0bp` ⇒ **SOFT**

**Same auction, same publisher, opposite verdicts** — and both readings agreed on *direction* ("the tail widened"), which is what let the mismatch pass a sanity check.

🔑 **The new half this instance adds: a caveat about PROVENANCE does not insure against an error of DIMENSION.** The sender did everything the discipline asks — labelled the figures INFERRED/relayed, named the unchecked primary document exactly, and explicitly **refused to grade** the recipient's rail. **The defect would still have propagated**, because provenance discipline and unit discipline are *independent* controls and only the first one has a ritual. ⇒ **A relay tier tells you how much to trust the number; it says nothing about whether the number is commensurable with your bar.**

**How to apply (additive):** before a relayed figure touches a registered bar, state the bar's unit and the figure's unit **as two separate sentences**. For anything with a native dual representation — bond tails (price yen vs yield bp), spreads (bp vs %), FX (pips vs figures), yields (level vs change) — **the publisher's own field label is the authority, not the sender's shorthand.** And when a relayed figure sits *near* a bar, that proximity is itself the trigger to check the unit: SAM's true margin was **0.1bp on a 2.0bp bar**, so nothing about the arithmetic looked wrong either way.

**Worked instance (PHAN, 2026-09-11 — same unit, same publisher, same series: the AGGREGATION WINDOW was the only defect, and an unreachable primary is what chose it).**
PHAN's `FLOW-PHAN-06` trigger is authored on **quarterly** provision growth (*"Affirm +40% YoY provisions vs DQ improvement"*). On 9/10 the FQ4 earnings supplement timed out twice, so the pass fell back to the **10-K's fiscal-year** aggregate and downgraded the trigger ACTIVE → PARTIAL on `provision +29.2% < GMV +37%`.
- FY basis: **+29.2%** ⇒ below the >30% bar ⇒ **PARTIAL**
- Quarterly basis (10-Qs differenced against the 10-K): **+1.8% → +40.0% → +33.5% → +42.5%** ⇒ three straight quarters above the bar, **Q4 outpacing Q4 GMV by 6.5pp** ⇒ **ACTIVE**

Same company, same filings, same unit (% YoY), **one flat quarter** deciding the verdict.

🔑 **The new half: a fetch failure silently picks your basis for you.** The earlier instances are all about a *borrowed* figure whose unit went unstated. Here nothing was borrowed and nobody relayed anything — **the desk had authored the trigger's basis itself and still tested the wrong window**, because the reachable fallback document published only the other one. No relay tier, no provenance caveat and no confirmation bias was involved; **the available data substituted its own aggregation window for the registered one, and that substitution never surfaces as a decision anyone makes.** The 9/10 pass even wrote *"never quote provisions outpacing volume without saying vs GMV or vs loans, Q4 or FY"* — **it named the exact hazard in the same paragraph in which it fell to it**, which is `[[finding_naming_a_caveat_can_substitute_for_fixing_it]]` landing on the period axis.

**How to apply (additive):** when a primary is unreachable and you fall back, **state the registered rule's period basis and the fallback document's period basis as two separate sentences before grading** — the fallback is presumed to be on the WRONG basis until shown otherwise. And prefer **reconstructing** the registered basis over re-basing the rule: quarterly figures are usually recoverable by differencing interim filings against the annual (FY − 9-month = Q4), which needs no secondary at all. Corollary for the *authoring* side: **a trigger that names a growth rate must name its period in the same sentence**, or the first fetch failure re-bases it silently.

Related: [[finding_cross_entity_comparison_needs_same_perimeter]] · [[finding_measure_actionable_not_gross_rate]] · [[finding_number_carries_threshold_unit_source]] · [[finding_normalization_choice_picks_opposite_winners]]
