---
name: finding-rebased-metric-check-made-date
description: "Before re-basing an open prediction onto a better metric, test whether the NEW metric was already satisfied at the original Made_Date — if it was, the prediction is retired with no credit, not re-based, or you launder a likely-miss into a hit (OTTO-04, 2026-07-25)"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 53f77d69-be8e-4391-a23f-6461969b9141
  modified: 2026-07-26T00:36:40.511Z
---

Re-basing an open prediction onto a better-measured metric is often the right call — the original measure can turn out biased, unpublished, or unobtainable. **But the re-base must be gated on one test: was the new metric already satisfied on the prediction's `Made_Date`?** If it was, the claim has **zero forecasting content** on the new measure, and carrying it forward converts a likely miss into a recorded hit.

**Why (OTTO-04, 2026-07-25).** OTTO-04: *"2022-vintage subprime CNL exceeds 25% by Sep 30"*, made **2026-02-23**, resolving on the Fitch blended subprime index. Two things then went wrong with the measure: the blend was composition-biased (anchored down by Santander's dominant low-loss deals, tracking to ~24.3% = a miss), **and** it became unobtainable (no Fitch-direct access; the free trade-press mirror decayed to March data; S&P returned 403, KBRA's data was paywalled). Will directed re-basing onto the deep-subprime 10-D tranche OTTO could actually pull — analytically the right measure, since the thesis was always about deep-subprime impairment.

The check caught the problem: on the re-based metric, **EART 2022-3 was already at 25.90%** on the 10-D filed **2026-01-28**, and EART 2022-2 crossed 25% within days of the Made_Date. **The re-based claim was true before it was written.** Scoring it CONFIRMED would have been [[feedback_forward_discovery_prediction_spirit]]'s known-unknown trap running in reverse — instead of archaeology retroactively confirming a claim, a metric swap prospectively confirming one.

**Disposition that keeps the book honest:**
1. **Re-base the tracked METRIC** — that part is legitimate and usually urgent (the old series may be dead).
2. **Resolve the PREDICTION on its original ratified measure** — here falsified-on-metric / confirmed-on-substance.
3. **Take no calibration credit either way**, and say so explicitly in the row and the scoreboard, because "substance confirmed" reads as a win to anyone scanning.
4. **Open a genuinely forward replacement** on the new metric — pick a threshold the series has *not* yet crossed, ideally near-coin-flip so the row carries calibration information. (OTTO-34: EART 2022-3 CNL ≥29.0% on the Dec-2026 filing, 60%, against a 27.58% baseline decelerating .37→.30pp/mo.)

**How to apply.** Whenever you change an open prediction's measure, threshold, or data source: pull the new series back to the original `Made_Date` and check where it stood. Cheap — one query. If the claim was already true, the honest move is **retire and replace, not re-base**. Record the reasoning where the scoreboard is read, not only where the row lives; a hit-rate table with an unexplained generous entry is worse than a lower number.

**Generalises to:** switching a KPI definition mid-quarter, changing a benchmark index mid-evaluation, moving a threshold from a blended to a component measure, or any "the old metric was flawed" correction on a live claim. The flaw being real does **not** make the swap scoring-neutral.

Related: [[feedback_prediction_canonical_measure]], [[feedback_forward_discovery_prediction_spirit]], [[finding_discovery_instrument_defines_the_claim]], [[finding_threshold_spec_fails_before_world]], [[feedback_dont_bank_unpassed_forecast]].
