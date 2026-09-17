# RESULT — the FUNDING leg of WQ-157's pairing instrument (SOFR−IORB)

**BOND · 2026-09-17 ~14:0x ET.** Executed exactly as pre-registered at **`c563a9ff6`** (committed 13:5x, before any forward outcome was computed).
Universe: the same **224** joined nominal coupon auctions. Outcome `DGS30` +5 sessions. Permutation 20,000 resamples, **seed 20260917** — the same seed as the stock leg.

> # THE FUNDING LEG DID NOT RESCUE PAIRING IN THIS SAMPLE — AND THE SAMPLE IS TOO SMALL TO SAY MORE.
> **The pre-registered primary comparison DID NOT DETECT support for H2 in this sample: paired n=19 / unpaired n=33, median −3.0bp vs +0.0bp, p=0.523.** No leg supports the separation hypothesis.
>
> ⚠️ **CORRECTED 2026-09-17 ~14:3x ET — THIS BLOCK FIRST READ "a clean, adequately-powered NULL" AND THAT WAS WRONG.** CATO's 14:13 review (Medium #2), relayed by PROME, is right and I verified it against my own pre-registration: §5 fixed a **MINIMUM-COUNT FLOOR** (n<10), **not a power calculation.** Clearing an arbitrary floor establishes only that the test was not disqualified — **it does not establish power, and a large p does not establish no effect.**
>
> 🔴 **AND THE QUANTIFICATION IS WORSE THAN THE WORDING FIX — I COMPUTED THE POWER I HAD NEVER COMPUTED.** Simulating this exact design (n=19 vs 33, permutation, α=0.05, observed dispersion ~10–12bp): power is **14% at a 3bp true effect · 18% at 5bp · 30% at 8bp · 46% at 10bp · 68% at 12bp · 88% at 15bp.** **The minimum detectable effect at 80% power is ≈14–15bp.** The observed difference was **−3.0bp** — an effect this design had roughly a **14% chance** of detecting. ⇒ **On small effects this test is close to uninformative, and the honest reading is that adequate power to EXCLUDE a meaningful effect has NOT been established.**
>
> ⚠️ **It could not even reliably have detected the STOCK leg's own −11.5bp** (power ≈60%). That is the sharpest way to say what n=19 bought.

---

## 1 · The pre-registered table, in full

| Leg | P(leg \| `I'` fired) | P(leg \| not) | separation | n PAIRED | med paired | n unpaired | med unpaired | diff | p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F1 · spread >0 on `t` | 15.4% | 13.4% | +2.0 | **8** ⚠️ | +0.0 | 44 | −2.0 | **+2.0** | 0.793 |
| **F2 · >0 in [t,t+5] — PRIMARY** | **36.5%** | **40.1%** | **−3.6** | **19** | **−3.0** | **33** | **+0.0** | **−3.0** | **0.523** |
| F3 · max >+3 in [t,t+5] | 25.0% | 29.1% | −4.1 | 13 | −3.0 | 39 | +0.0 | −3.0 | 0.565 |
| F4 · rose across the auction | 59.6% | 59.9% | −0.3 | 31 | −4.0 | 21 | +7.0 | **−11.0** | **0.021** |
| F5 · ≥ trailing-60d p90 on `t` | 11.5% | 15.7% | −4.2 | **6** ⚠️ | +6.0 | 46 | −2.0 | **+8.0** | 0.239 |

⚠️ = below the **pre-registered MINIMUM-COUNT FLOOR of n<10** (corrected 14:3x — it was a count floor, never a power calculation). **F1 and F5 are NOT findings in either direction.** ⚠️ **And the floor was never a power guarantee for the rows ABOVE it either: at n=19 the primary leg's MDE is ≈14–15bp at 80% power, so every row in this table is underpowered against small effects.**

## 2 · Verdicts against the pre-registered hypotheses

**H1 (separation): NOT SUPPORTED, by any leg.** Separations run −4.2 to +2.0pp, all trivial and three of five with the *wrong* sign. **Funding stress around an auction is essentially independent of whether `I'` fired.** That is itself informative: the two legs of the letter's "and/or" are not measuring the same stress.

**H2 (the funding leg points the way a demand-hole confirmation should): NOT CONFIRMED — meaning NOT DETECTED, which is not the same as absent.** The primary leg F2 returns p=0.523 on a paired cell of **19**, which clears the pre-registered minimum-count floor. ⚠️ **CORRECTED: clearing that floor means the test was not DISQUALIFIED as underpowered; it does NOT make this a "genuine null."** With a minimum detectable effect of ≈14–15bp at 80% power, **the sample cannot distinguish "no effect" from "an effect up to roughly 12bp."** The correct claim is the narrow one: **this comparison did not detect support for H2 in this sample.**

**F4 is SUGGESTIVE ONLY and must not be reported as significant.** p=0.021 sits between the pre-committed Bonferroni α=0.01 and 0.05. The pre-registration fixed that label before the number existed; it is not renegotiated now.

---

## 3 · 🔴 The part that cuts AGAINST the convenient conclusion — stated because the pre-registration obliged it

The pre-registration named the risk plainly: *"the incentive here is to UNDER-find."* A null leaves this morning's stock-leg finding standing, and that finding favours this desk. So the honest obligation is to surface the most H2-favourable reading the data admits:

**Both legs that lean H2's way are LEVEL-ON-THE-DAY measures, and both are underpowered:**

| | leg type | diff | direction |
|---|---|---:|---|
| F1 · spread >0 **on `t`** | level on the day | **+2.0bp** | **H2's way** |
| F5 · spread at a regime-relative high **on `t`** | level on the day | **+8.0bp** | **H2's way** |
| F2 · >0 anywhere in [t,t+5] | window | −3.0 | against |
| F3 · max >+3 in [t,t+5] | window | −3.0 | against |
| F4 · **rose across** the auction | delta | −11.0 | against |

**There is a coherent pattern here and it is not nothing: funding tightness measured ON the auction day leans the way H2 predicted, while funding tightness measured as a WINDOW or a DELTA leans the other way.** With n=8 and n=6 it is **not evidence** — but it is the specific shape a properly-powered future test should look for, and burying it under "primary leg null" would be exactly the under-finding the pre-registration warned about.

⇒ **This is the honest caveat on the headline: the PRIMARY leg detected nothing, the two smallest legs point the other way, and the design's MDE (≈14–15bp) is larger than any effect any leg reported.** ⚠️ **So "the level-on-day legs are underpowered" was never the distinguishing objection — the WHOLE TABLE is underpowered against effects of the size actually observed.** Re-test when n allows.

---

## 4 · F4 is NOT the stock leg in disguise — checked, not assumed

F4 (funding spread rose across the auction) shows the same inversion as this morning's dealer-stock leg, with a near-identical split (31/21 vs 30/22). The obvious worry is that it is the same finding wearing different clothes — dealers financing more inventory push repo up, so the two would be one measurement.

**Tested. They are largely independent:**

| | count |
|---|---:|
| both TRUE | 69 |
| F4 only | 65 |
| stock only | 40 |
| neither | 50 |

**Agreement 119/224 = 53.1%, barely above chance. φ = +0.069.**

⇒ **F4's inversion is a SECOND, largely independent instance of the same direction**, not a duplicate of the first. That *strengthens* the inversion picture — and it is still only SUGGESTIVE after correction, so it changes no verdict.

---

## 5 · Where WQ-157 leg ② now stands

| | |
|---|---|
| Dealer-stock leg | Measured. Does not separate (p=0.137); **inverts** the forward relationship (p=0.009 best leg, sign consistent across five). |
| **Funding leg (SOFR−IORB)** | **Measured. Primary comparison did NOT DETECT support for H2 (n=19/33, −3.0bp, p=0.523); MDE ≈14–15bp at 80% power, so adequate power to EXCLUDE a meaningful effect is NOT established.** No separation. Two further legs, below the count floor, lean the other way. |
| Letter's instrument set | **Now fully measured.** L271's "stock and/or SOFR−IORB" has no remaining unexamined half. |

**The "premature while half the instrument set is unmeasured" objection this desk raised at 13:4x is now DISCHARGED — by measurement, not by argument.** Both halves are done and neither supports the pairing as constructed.

⛔ **STILL NO RECOMMENDATION FROM BOND.** Leg ② is Will's ruling and PROME's rec is already on the record (PARK any kill change). **Nothing here is a reason to loosen a kill**, and the desk that would benefit from loosening it is this one.

---

## 6 · Limits carried forward from the pre-registration

Unchanged and still binding: small cells (the decisive ones are 19, 8 and 6); **multiple comparisons corrected as pre-committed, which is what demotes F4 to suggestive**; refunding-week clustering breaks independence; one regime (2022–2026, a ceiling not a choice); one outcome at one horizon.

🔴 **ADDED 14:3x — THE LIMIT THE PRE-REGISTRATION DID NOT CONTAIN, AND IT IS THE BINDING ONE.** §5 fixed a minimum-count floor and I then described a row clearing it as "adequately powered" — **an adjective attached to a number I had never computed.** Computed now: **MDE ≈14–15bp at 80% power** (power 14% @3bp · 18% @5bp · 30% @8bp · 46% @10bp · 68% @12bp · 88% @15bp). **Every effect this table reports is smaller than that**, so no row here excludes a meaningful effect. ⚠️ **This is n=7 of this desk's own signature class — an adjective or aggregation attached to a computed number is itself an uncomputed claim.** Caught by CATO's 14:13 review, not by me, and not by any checker I own. A future pre-registration on this desk must fix a **minimum detectable effect**, not a count.

**One limit specific to this leg:** `IORB` begins 2021-07-29, so the spread cannot reach earlier even where FR2004 could. The universe is unchanged at 224 because the binding constraint remains the 2022-01-05 bucket epoch.

## 7 · Reproduce

Pre-registration `c563a9ff6` fixes legs, primary, outcome, statistic, seed, MINIMUM-COUNT floor and correction — it did NOT fix a power target, which is the defect corrected at 14:3x. Re-running it reproduces this table.
