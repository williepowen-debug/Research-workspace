---
name: finding_apparent_confabulation_is_often_a_baseline_mismatch
description: "A figure that looks fabricated/impossible is often a REAL value on a different dataset baseline — a mis-comparison, not a confabulation; verify the baseline before crying fake."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 32800f7b-a3f5-4829-9937-b1177349dc99
  modified: 2026-08-03T14:33:31.602Z
---

A number that contradicts your trusted primary can look like a confabulation when it is actually a **real value measured on a different dataset baseline**. Before concluding "this figure exists in no primary / was fabricated," check whether it comes from a *sibling dataset with a different climatology or base period* — the mismatch is then a cross-baseline comparison error, not a fake number.

**Worked case (AEOLUS, 2026-08-03, correcting my own 7/22 call):** I had logged a floating ENSO "+2.1 °C Niño-3.4" as an "outright confabulation" because the official CPC ENSO Discussion said +1.2 °C. It was **real**: the weekly `wksst9120.for` file runs **~0.8 °C hotter than the Discussion on every region** (different SST climatology/baseline). Same week, same region, two legitimate numbers. The failure was comparing a warmer-baseline file value against the official one as if interchangeable.

**Rules:**
- Use one source for **LEVEL**, another for **TREND** — never mix their absolute values. (ENSO: `ensodisc.pdf`/`oni.ascii.txt` for level; `wksst9120.for` for weekly trend.)
- Watch **column-order traps** across sibling files: `wksst9120.for` orders regions 1+2 / 3 / 3.4 / 4; `sstoi.indices` orders 1+2 / 3 / 4 / 3.4 — mixing silently swaps Niño-3.4 ↔ Niño-4.
- This is the inverse-error guard to `feedback_single_source_liveevent_is_a_lead`: that one says don't over-trust a lone secondary; this one says don't over-*reject* a figure as fake when it is real on another baseline. Ties to `finding_asymmetric_rigor_counterparty_claims` (verify the number that makes you RETRACT, not just the one that makes you commit) and rebasing memories like `finding_threshold_level_is_a_measurement_not_a_constant`.

**Second worked case — the inverse direction (MARCO, 2026-08-21, caught on self-review the same session):** I called a *published* figure an **artifact** and told consumers not to adopt it. Nevada Gaming's monthly release headlined percentage-fee tax collections at **−6.99% YoY**, with a footnote reading *"collections are through July 21."* I concluded it was a partial month compared against a full prior-year month, refused the number, and wrote that into a vector row, STATUS, a session handoff and a cross-agent brief.

**It was wrong.** The footnote describes a *standing convention*, not an asymmetry: the previous month's release carries the identical note (*"through June 23"*). **A limitation disclosed on one side is not evidence that the other side lacks it.**

**⇒ The runnable discriminator, which is the part worth stealing:** if the asymmetry were real, it would produce a **systematic directional skew** across the series. So compute the YoY across many periods before ruling on any one of them. Here: twelve monthly prints, **mean +7.09%, six of twelve negative, full-year +5.07%** — no skew, therefore no one-sided truncation, therefore the figure is real.

**And the correct finding was stronger than the one it replaced.** Those same twelve prints have **σ = 14.04pp** (range −12.35% to +33.80%), so the −6.99% is a **−1.0σ move with 2 of 12 months at least as negative — a single month carrying no signal at all.** Base-rating the series answered the question that "is this number fake?" could not. *(The stale text I was replacing had made the mirror-image error: three monthly prints called "clear deterioration" in that same 14pp-σ series.)*

**Both directions of this failure share one root:** a *basis* question got answered by inspection instead of by measurement. Crying fake and crying artifact are the same move.
