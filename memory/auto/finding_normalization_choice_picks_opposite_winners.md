---
name: finding-normalization-choice-picks-opposite-winners
description: "Absolute-change and proportional-change lenses can name OPPOSITE winners off the exact same numbers, so 'X led the move' is unfalsifiable unless it states its normalization. Require a real signal to register on BOTH; when the two disagree, the disagreement IS the finding — grade it as no-clean-signal, not as whichever lens flatters the thesis."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 5326c084-a5ab-4d66-9293-f42709ed8d2f
  modified: 2026-07-27T18:23:09.173Z
---

Given a fixed set of levels moving together, **which component "led" depends entirely on the normalization you pick, and the two standard ones routinely disagree.**

**Worked instance (BROCK, 2026-07-27, HY tranche OAS, FRED/ICE BofA).** Two-session move 7/22→7/24:

| | Δ bp | Δ % of own level |
|---|---|---|
| HY | +11 | +4.10% |
| BB | +11 | **+7.01%** ← largest |
| B | +11 | +3.86% |
| CCC | **+15** ← largest | +1.53% |

**Absolute bp says CCC led. Proportionally BB moved 4.6× more than CCC.** Opposite winners, same four numbers. A fleet claim of "parallel widening / CCC-led" was an **absolute-bp artifact**; the proportional read said the move was high-quality-led, i.e. rates/beta rather than credit-quality repricing.

**The operational rule that fell out of it:**

> **A real signal registers on BOTH normalizations. When they disagree, the disagreement IS the finding — grade it "no clean signal," never "bear on the lens that agrees with me."**

Use a **ratio/dispersion** test as the tiebreak, because it is normalization-free in the direction that matters: quality-recognition *expands* the risky/safe ratio. In the instance above the CCC/BB ratio **compressed** 6.25×→5.93× across exactly the sessions that produced the whole move ⇒ beta, not recognition. Note the levels-gap and the ratio can also disagree (CCC−BB gap widened 807→828 while the ratio went 5.98→5.93) — that is the same trap one layer up, and it resolves the same way: **both, or neither.**

**Generalizes to** any decomposition where components sit at very different levels — credit tranches, sector spreads, regional NCO/DQ rates, index constituents, cohort delinquencies, YoY vs pp comparisons. **The bigger the level dispersion between components, the more violently the two lenses diverge** (BB at 157bp vs CCC at 981bp is a 6× level gap, which is why +11 vs +15 flipped to +7.01% vs +1.53%).

**Hygiene:** every "X led the move" claim — yours or an inbound one — must carry its normalization, or it cannot be checked and should not be propagated. This is a *stated-method* requirement, not a preference.

Distinct from [[finding-composition-mask-unmask-discriminator]] (there the *reporting entity* manages the base to hide deterioration; here nobody is hiding anything — the *analyst's* lens choice manufactures the conclusion). Related: [[finding-number-carries-threshold-unit-source]], [[finding-blended-index-masks-bifurcation]], [[finding-level-vs-monthly-average-cpi-landing]].
