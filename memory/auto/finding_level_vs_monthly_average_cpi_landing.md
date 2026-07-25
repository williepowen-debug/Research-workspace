---
name: finding_level_vs_monthly_average_cpi_landing
description: "\"X lands in the <month> print\" must be computed on MONTHLY AVERAGES against the prior month's average — never off a month-end level or a peak-to-trough level move; a spike into a falling month can print negative MoM."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7beb44e-7301-4b3e-b05f-59099c68ca43
  modified: 2026-07-24T22:19:25.273Z
---

**Any claim of the form "the shock lands in the \<month\> print" is a monthly-average claim, not a level claim.** CPI, PPI and most official series measure the **average over the reference month**. A price that ends the month at a record can still print **negative MoM** if the prior month ran *downhill* from a higher start.

**The case (2026-07, three agents independently).** Brent settled >$100 for the first time on 7/23 and the US pump crossed $4.00 — and RED, CARL and HENRY all separately wrote that "the oil lands in the July CPI (8/13)." It doesn't:

| Series | June | July | July MoM |
|---|---|---|---|
| Retail gasoline (FRED **GASREGW**) | avg **$4.050** (ran 4.305 → 3.831) | avg **~$3.95** | **≈ −2.6%** |
| Spot Brent (FRED **DCOILBRENTEU**) | avg **$85.40** (n=22, ran 98.29 → 70.46) | avg **$83.3-85.0** (n=23) | **−0.4% to −2.5%** |

June ran downhill all month; July climbed from a lower base. **Near-identical monthly averages, opposite trajectories** — the spike landed in the *August* print instead. Note the level framing fails twice over: "oil +$24" was true as a **level move** and approximately **zero** as CPI-relevant monthly inflation.

**Why:** level moves are what the tape shows and what headlines quote, so they're what gets written into decision trees. The averaging step is invisible until someone computes it — and it can flip the sign, not just the magnitude.

**How to apply:**
- Before writing "X lands in month M's print," compute **avg(M) vs avg(M−1)** from the underlying weekly/daily series. Run the sensitivity on the remaining unobserved weeks; if the sign is robust across plausible paths, say so.
- **Corroborate off a second series at a different layer** where possible — the retail-price version depends on a pass-through lag; the spot-commodity version doesn't. Agreement across layers is real independence, not a relay.
- A **soft print produced by base effects is arithmetic, not evidence** — pre-register it as a non-event so nobody scores it as a broken mechanism (the base-effect-scored-as-mechanism trap).
- The corollary for policy trees: **the operative print for a decision is the last one before that decision**, not the next one the decision-maker sees.
- Related: [[feedback_yoy_baseeffect_use_multiyear_stack]], [[finding_number_carries_threshold_unit_source]], [[finding_redated_falsifier_inherits_premise]], [[feedback_single_month_subcomponent_skepticism]].
