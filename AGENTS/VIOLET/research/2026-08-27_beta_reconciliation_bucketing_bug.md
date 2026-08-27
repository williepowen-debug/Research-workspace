# β reconciliation — KB-VIO-208 (0.500 @ 21-35 DTE) vs the packet's 0.274

**Run date:** 2026-08-27
**Purpose:** Adjudicate the pre-deployment discrepancy KB-VIO-208 disclosed:
> *"my VIXCS post-mortem registered 0.274 (21-35) / 0.505 (11-20) / 0.591 (≤10) from an OPTION-IMPLIED construction, n=246. These are VX FUTURES settle-to-settle, n=1040-3240, R²=0.71-0.87. THE SHAPE AGREES; THE LEVEL DISAGREES MATERIALLY at 21-35 (0.500 vs 0.274). Different instruments, different samples. I am NOT overwriting the registered figure by preference — reconciliation is a pre-deployment owed item."*

**Verdict:** 🎯 **No genuine discrepancy — the packet's 0.274 was a bucketing bug.** The "21-35 DTE" bucket in the 2026-07-30 packet had no upper cap; it pooled 136 observations at DTE > 60 (β ≈ 0.16) into the labeled bucket. Correctly-capped 21-35 on the same 12-month M1-only sample = **β 0.529**, consistent with KB-VIO-208's 13-year 0.500.

**Also corrected:** KB-VIO-208's own description of the comparator as *"OPTION-IMPLIED construction"* is wrong. The n=246 packet used `VX_M1_HISTORY.tsv` — **VX futures M1 settle vs VIX spot**, not options. **Both figures are futures-settle β.** The comparator label needs a KB correction.

---

## Two axes could differ; both isolated

| Axis | KB-VIO-208 method | Packet's method |
|---|---|---|
| **Sample period** | 2013-05-20 → present (28,583 contract-days) | 2025-08-01 → 2026-07-29 (248 daily obs of M1) |
| **Contract mix** | All contracts per date, bucketed by DTE at pair start | M1 only, bucketed by front-contract DTE |
| **DTE anchor** | prev-row DTE | (see below — turns out to be curr-row DTE) |
| **DTE bounds** | closed intervals (≤10, 11-20, 21-35, 36-60, 61-90) | (see below — turns out to be UNCAPPED at the top for 21-35 label) |

### Hold sample-period constant (all-contract on M1 window)

`AGENTS/VIOLET/workbook/VX_TERM_HISTORY.tsv` restricted to 2025-08-01 → 2026-07-29, all contracts:

| Bucket | β | R² | n |
|---|---|---|---|
| ≤10 | 0.683 | 0.845 | 75 |
| 11-20 | 0.560 | 0.903 | 72 |
| **21-35** | **0.478** | 0.866 | 115 |
| 36-60 | 0.343 | 0.791 | 178 |
| 61-90 | 0.256 | 0.779 | 231 |

**Isolating sample period does not explain the gap.** β at 21-35 stays near 0.5 on the 12-month sample.

### Hold contract-mix constant (M1-only on KB-VIO-208 full window)

VX_TERM_HISTORY.tsv 2013-05-20 → present, M1 only:

| Bucket | β | R² | n |
|---|---|---|---|
| ≤10 | 0.697 | 0.882 | 887 |
| 11-20 | 0.653 | 0.872 | 1014 |
| **21-35** | **0.534** | 0.703 | 1258 |
| 36-60 | 0.428 | 0.777 | 148 |
| 61-90 | 0.438 | 0.785 | 12 |

**Isolating contract mix does not explain the gap either.** β at 21-35 stays near 0.5.

### Reproduce packet-method (M1-only on M1 window)

Same VX_TERM_HISTORY restricted to 2025-08-01 → 2026-07-29, M1 only:

| Bucket | β | R² | n |
|---|---|---|---|
| ≤10 | 0.738 | 0.903 | 64 |
| 11-20 | 0.560 | 0.903 | 72 |
| **21-35** | **0.533** | 0.843 | 89 |

**Even the exact packet method (M1-only, 12-month window) gives β 0.533 at 21-35 DTE, not 0.274.**

The packet's n=200 at 21-35 also does not match my n=89. Difference of ~110 observations in the same bucket, same file, same window.

---

## What actually reproduces the packet's numbers

Load `VX_M1_HISTORY.tsv` directly and OLS its own columns:

- **Total n=246, pooled β 0.345** ← exact packet match
- **≤10 DTE (anchor: curr row), n=19, β 0.591** ← exact packet match
- **11-20 DTE (anchor: curr row), n=27, β 0.505** ← exact packet match
- **21-35 DTE capped, n=47-48, β 0.531** ← NOT the packet's number
- **DTE ≥ 21 UNBOUNDED, n=201, β 0.279** ← matches packet's β 0.274 / n=200 to within rounding

**The packet's "21-35 DTE" bucket had no upper cap.**

The uncapped pool at DTE ≥ 21 grabs 136 observations at DTE > 60 (β 0.161) and 18 obs at 36-60 (β 0.408), which drag the aggregate from 0.531 down to 0.279. **It is a mislabeled bucket, not a measurement.**

### DTE distribution in VX_M1_HISTORY.tsv (auditable)

| Bucket | rows | % of file |
|---|---|---|
| ≤10 | 19 | 7.7% |
| 11-20 | 27 | 10.9% |
| 21-35 | 48 | 19.4% |
| 36-60 | 18 | 7.3% |
| >60 | 136 | 54.8% |

**55% of the file is DTE > 60.** That is the second finding: `VX_M1_HISTORY.tsv` is not a pure M1 series — a majority of its rows carry front-contract DTEs above what a monthly rollover would place M1 at. This should be looked at separately (either the fetch logic or the roll definition), but it does not affect the β verdict here.

---

## Cross-checks on the reconciled β

### Time slicing (all-contract, 21-35 DTE, 2-year windows)

| Window | β | R² | n |
|---|---|---|---|
| 2013-2014 | 0.447 | 0.812 | 198 |
| 2015-2016 | 0.478 | 0.737 | 256 |
| 2017-2018 | 0.397 | 0.819 | 253 |
| 2019-2020 | 0.488 | 0.598 | 244 |
| 2021-2022 | 0.549 | 0.869 | 244 |
| 2023-2024 | 0.575 | 0.737 | 241 |
| 2025-2026 | 0.487 | 0.870 | 179 |

**β at 21-35 DTE has been in a 0.40-0.58 band for 13 years.** The current-window number sits at 0.49. No structural break.

### VIX-level slicing (all-contract, 21-35 DTE, full window)

| Spot VIX at pair start | β | R² | n |
|---|---|---|---|
| 0-14 | 0.455 | 0.770 | 538 |
| 14-18 | 0.531 | 0.846 | 487 |
| 18-25 | 0.546 | 0.867 | 404 |
| 25+ | 0.462 | 0.590 | 186 |

**β is essentially flat across VIX buckets.** Not regime-dependent.

---

## Canonical β to carry (all figures at 21-35 DTE)

Adopt **KB-VIO-208's tenor gradient as canonical** because it has 100–1000× the sample size per bucket and 13-year coverage:

| Bucket | β | R² | n |
|---|---|---|---|
| ≤10 | 0.643 | 0.806 | 1040 |
| 11-20 | 0.653 | 0.872 | 1014 |
| **21-35** | **0.500** | 0.706 | **1615** |
| 36-60 | 0.448 | 0.773 | 2487 |
| 61-90 | 0.327 | 0.621 | 3240 |

**The gradient's shape is unchanged from what the packet reported** (β falls monotonically with tenor). **Only the level at 21-35 DTE moves.** All downstream conclusions that used the gradient — that TRY-VIOLET-VIXCS at ≤10 DTE bought maximum β and minimum probability; that a 30-60 DTE tenor delivers ~0.32-0.45 β into a spot move where the signal's edge lives — **survive intact.** They rested on the *gradient*, not on 0.274 vs 0.500.

---

## What needs correcting in the record

1. **KB-VIO-208 comparator label:** "OPTION-IMPLIED construction" → "M1 futures-settle β on 2025-08-01 → 2026-07-29 with an uncapped 21-35 DTE bucket." Same instrument as KB-VIO-208 itself; different (mislabeled) bucketing. Correct the KB row.
2. **Publisher-side correction to TERRY:** the n=246 packet (`AGENTS/TERRY/inbox/processed/2026-07-30_from-VIOLET_beta-derived-independently-your-028-was-the-right-number-for-the-wrong-tenor.md`) reported β 0.274 at 21-35 DTE. On correct capping, β at 21-35 DTE on that same 12-month M1 sample is 0.529 — **within noise of KB-VIO-208's 0.500 on 13 years and 1,615 obs.** Send a correction packet; the packet's *tenor-gradient conclusion* survives, its *point estimate at 21-35* does not.
3. **Auto-memory candidate:** *"a labeled bucket must be capped at BOTH ends; an unbounded top matches everything above it and quietly weights the pool toward the longest tenors, which for a series with a strong tenor gradient will pull the label toward the extreme it is furthest from."* Same family as `[[finding_output_shape_implies_more_than_the_measurement]]` and `[[finding_asymmetric_rigor_counterparty_claims]]` (verify the number you retract on).

---

## Notes on the retraction chain

The 8/27 finding is the **second** correction of the VIXCS-era β number. The chain:

1. **Original (TERRY, pre-VIXCS):** 0.28. Adopted on relay by VIOLET across five surfaces. Wrong tenor.
2. **VIOLET, 2026-07-30:** derived 0.274 at 21-35 DTE from M1_HISTORY.tsv. Corrected the "wrong tenor" issue (the position was ≤10 DTE, β ≈ 0.6). **But the 0.274 was itself wrong** due to an uncapped bucket.
3. **VIOLET, 2026-08-27 (this):** correctly-capped bucket gives 0.529 on the same M1 sample; KB-VIO-208's 0.500 on 13 years is canonical.

**The published Artifacts (`vol_cheatsheet.html`, `violet_operating_picture.html`) — checked briefly — do not carry the 0.274 figure explicitly; they were updated at the 8/1 refresh past the "0.28 → ~0.6 at ≤10 DTE" fix.** They are not stale on this axis but should be verified on any subsequent refresh.

*The generalizable lesson: `[[finding_asymmetric_rigor_counterparty_claims]]` — verify the number that makes you retract — got its second live instance in 30 days.*
