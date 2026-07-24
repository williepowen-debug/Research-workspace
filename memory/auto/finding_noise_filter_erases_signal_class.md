---
name: finding_noise_filter_erases_signal_class
description: "Before widening a noise filter to cut a detector's false positives, check whether the true positives live in the noise you're filtering — events often cluster on the very dates the filter excludes; prefer a persistence/duration rule, and score FP per-episode not per-day"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 47e2a106-60c8-40b1-a48e-cd9334cb7b94
  modified: 2026-07-24T01:32:40.406Z
---

When a threshold detector fires too often and the false positives look like calendar/seasonal artifacts, the reflex is to widen the exclusion filter. **Check first whether the true positives sit inside the window you are about to exclude.** Stress events frequently cluster on exactly the dates a "noise" filter removes, because the calendar effect and the event share a cause. Widening the filter then deletes the event class the detector exists to catch — while the FP rate improves, which makes it look like the fix worked.

**Preferred alternative: a persistence rule** (require N consecutive qualifying observations). Noise from settlement/calendar effects is typically a one-period artifact that reverses; a genuine event persists. Persistence separates them without touching the dates.

**Also: score false positives per EPISODE, not per observation.** If one true event spans many days, per-day scoring silently inflates the true-positive count and flatters the detector. The decision is made once per episode, so that is the unit.

**Why:** LIQUID's funding-seizure gate (2026-07-23) arms on SOFR99−IORB ≥+30bp with quarter/month-end excluded. Backtesting it, 5 of 6 surviving false positives were tax-date and year-end turn effects leaking past the ±2-business-day window — so adding quarterly corporate tax dates was the obvious fix. **It would have destroyed the only true positive in the sample.** Sep-15 is a corporate tax date, and the Sep-2019 repo seizure was *caused* by that tax drain plus a large Treasury settlement: the +250 / **+690** / +290bp prints on 9/16-18 all sit inside a tax-date window. The "fix" cut the event from 8 days/690bp to 3 days/70bp. A persistence leg (≥2 consecutive non-calendar days) instead removed 4 of 5 FPs, left the true positive fully intact, and cut episode-level FP 62%→25%. Separately, the inherited ~20% FP figure turned out to be per-day scored; per-episode it was 62%, because the one real event supplied 8 of 21 qualifying days.

**How to apply:** before widening any exclusion filter, list the known true positives and check how many fall inside the proposed exclusion — if any do, reject the widening outright. Reach for a persistence/duration requirement instead. Quote FP rates per-episode and say which unit you used. And when the sample contains only one true positive (common for rare-event detectors), say so loudly: no FP rate computed against n=1 is a statistical estimate, and any tuning that is not *mechanistically motivated* — a reason the filter separates noise from signal, independent of the data — is overfitting. Related: [[finding_sustain_count_role_discriminating_power]], [[finding_threshold_vs_mechanism]], [[finding_calibration_discount_regime_conditional]].
