---
name: finding_blended_index_masks_bifurcation
description: "A weight-blended aggregate (HY OAS, headline CPI, index breadth) hides tail bifurcation; measure sub-tier dispersion on a multi-month window, not the headline on a 5-day one"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4472d6d3-eb59-4266-a975-b0bdada7f704
symptoms: "the gap is narrowing so it must be improving; the index is at its low so credit is repairing; deceleration read as a turn; headline at a yearly best while the tail sets records; second derivative improving while the level has not crossed zero; a summary statistic moving the comfortable way while its own components do not"
---

A weight-blended aggregate **structurally hides bifurcation** — the healthy majority dominates the average and masks a diverging tail. Glancing at the headline reads "calm" when the components are splitting K-shaped.

**Why:** HENRY called junk credit "in good shape" off HY OAS 275bps (tight). Will recalled reading that credit was bifurcating and pushed for a double-check. It was: over 1yr, CCC (distressed tail) was the ONLY rating tier that *widened* (+27bps) while IG/BB/B/blended-HY all compressed (−16/−27/−41/−52). The blended HY index looked pristine *because BB/B dominate it by weight*. Two methodology traps: (a) used CCC−HY where HY *contains* CCC (diluted the signal); the clean gauge is CCC−**BB** (distressed vs quality, no overlap). (b) read a 5-day window (flat) on a quarters-long trend — the bifurcation only shows on a multi-month lookback.

**How to apply:** When an aggregate looks calm but the backdrop says it shouldn't, decompose into sub-tiers and measure the *dispersion between best and worst*, on the timescale the divergence actually moves (months, not days). Pick sub-components with NO overlap (CCC−BB, not CCC−HY). Generalizes beyond credit: headline CPI vs core/shelter split, index level vs breadth/advance-decline, aggregate delinquency vs subprime tail. Reinforces [[feedback_single_month_subcomponent_skepticism]] (timescale discipline) and the decompose-ratios-into-components feedback. Trigger to re-check: a user recalling prior reading that contradicts your "all calm" — treat it as a real signal to verify, not noise.

---

## EXTENSION 2026-09-02 — the class is wider than a weight-blend: **any summarising statistic can move the comfortable way while its subject has not turned.** n=2 in one night, two desks, two asset classes, unrelated instruments.

The original entry covers **aggregation** masking (a weight-blend hides a diverging tail). Tonight produced a **second, distinct mechanism** with the identical failure signature — and the shared feature is not how the statistic is built, it is **which direction the misread points.**

**Instance A — OTTO, subprime auto ABS (a DERIVATIVE, not an aggregate).** The 10-D panel's matched-collection-month YoY gap narrows monotonically: BROAD **+1.92 → +1.63 → +1.00**, DEEP **+2.29 → +1.85 → +1.21**. Nothing is masked and nothing is blended — every deal is reported singly, by tier, on the month the documents disclose. But **30 of 30 deal-months are still worse than a year ago and no tier has crossed zero.** The series is *deceleration of deterioration*. It will be read as a turn, because a falling number in a distress metric reads as improvement.

**Instance B — LIQUID, corporate high yield (an AGGREGATE — the original mechanism, independently re-instanced).** HY OAS printed **260 on 8/28**, a new 2026 minimum landing exactly on a pre-registered `<260` re-kill line with **0bp of margin**, now 265. Headline: credit is repairing. Underneath, **CCC/BB set four consecutive fresh three-year maxima** (6.739 → 6.840 → 6.855 → **6.901**, max of a 786-obs series since 2023-09-04), and the index's entire move off its own low **was the tail**: HY +5bp while **CCC +23bp** and BB +2bp.

**What makes them one class, and it is not the arithmetic.** In both, the statistic is *honest* — nobody is managing a denominator (that is [[finding_composition_mask_unmask_discriminator]]) and no difference is cancelling a common-mode move (that is [[finding_spread_metric_blind_to_common_mode]]). The statistic simply **summarises**, and summarising discards exactly the thing under test. The operative property:

> **The comfortable misread is the one that licenses action.** "The gap is narrowing" licenses standing down a downgrade leg; "the index is at its low" licenses closing a credit hedge. The correct read licenses nothing — it says *keep waiting*. So the error is not symmetric: it is systematically biased toward doing something.

**How to apply — write the caveat INTO the surface, not onto the dispatch.** This is the transferable half, and it came from LIQUID: *"a caveat that has to be remembered by every downstream reader fails silently."* A note attached to the packet protects the first reader and nobody after. With n=2 across unrelated instruments, put it in the cell:
1. **Name the quantity in the row label.** Not "YoY gap" but "YoY gap (DECELERATION — no tier has crossed zero)". Not "HY OAS at 2026 low" but "HY OAS at 2026 low; CCC/BB at a 3-year MAX".
2. **Carry the level beside the derivative, always** — the count that has not turned (30 of 30) travels in the same cell as the rate that has.
3. **State what would actually constitute the turn**, so the threshold is pre-committed rather than declared once the series is comfortable: a tier crossing zero; the tail compressing with the index.
4. **Check the direction of the misread.** If the comfortable reading is also the actionable one, escalate the labelling — that is where the cost lands.

⚠️ **Downstream spec consequence, generalisable: a leg that can be satisfied by DECELERATION alone is a different test from one that requires a TURN, and the difference only becomes visible once the series gets close.** Raise it with the consuming desk *before* the series arrives, not after — at that point the spec question looks like special pleading. (OTTO → CARL, V2 L1, raised 2026-09-02 ahead of a ≤9/10 grade sitting, on LIQUID's prompt.)

*Provenance: OTTO s021 + LIQUID, 2026-09-02, independently observed the same night; LIQUID identified the shared class and the write-it-into-the-surface remedy. Promotion flag to PROME per the extension rule — **n=2 (new mechanism), plus the original HENRY/Will instance = 3 total**.*

