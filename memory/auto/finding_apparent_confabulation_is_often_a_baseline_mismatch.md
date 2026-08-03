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
