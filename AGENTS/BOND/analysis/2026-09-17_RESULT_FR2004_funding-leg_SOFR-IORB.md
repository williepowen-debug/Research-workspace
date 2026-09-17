# RESULT — the FUNDING leg of WQ-157's pairing instrument (SOFR−IORB)

**BOND · 2026-09-17 ~14:0x ET.** Executed exactly as pre-registered at **`c563a9ff6`** (committed 13:5x, before any forward outcome was computed).
Universe: the same **224** joined nominal coupon auctions. Outcome `DGS30` +5 sessions. Permutation 20,000 resamples, **seed 20260917** — the same seed as the stock leg.

> # THE FUNDING LEG DOES NOT RESCUE PAIRING.
> **The pre-registered primary leg F2 is a clean, adequately-powered NULL: paired cell n=19, median −3.0bp vs +0.0bp unpaired, p=0.523.** No leg supports the separation hypothesis. **H2 — the claim that would have rescued pairing — is NOT confirmed.**

---

## 1 · The pre-registered table, in full

| Leg | P(leg \| `I'` fired) | P(leg \| not) | separation | n PAIRED | med paired | n unpaired | med unpaired | diff | p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F1 · spread >0 on `t` | 15.4% | 13.4% | +2.0 | **8** ⚠️ | +0.0 | 44 | −2.0 | **+2.0** | 0.793 |
| **F2 · >0 in [t,t+5] — PRIMARY** | **36.5%** | **40.1%** | **−3.6** | **19** | **−3.0** | **33** | **+0.0** | **−3.0** | **0.523** |
| F3 · max >+3 in [t,t+5] | 25.0% | 29.1% | −4.1 | 13 | −3.0 | 39 | +0.0 | −3.0 | 0.565 |
| F4 · rose across the auction | 59.6% | 59.9% | −0.3 | 31 | −4.0 | 21 | +7.0 | **−11.0** | **0.021** |
| F5 · ≥ trailing-60d p90 on `t` | 11.5% | 15.7% | −4.2 | **6** ⚠️ | +6.0 | 46 | −2.0 | **+8.0** | 0.239 |

⚠️ = below the **pre-registered power floor of n<10**. **F1 and F5 are UNDERPOWERED and are NOT findings in either direction** — that floor was fixed before the numbers precisely so a small cell could not be read as a result.

## 2 · Verdicts against the pre-registered hypotheses

**H1 (separation): NOT SUPPORTED, by any leg.** Separations run −4.2 to +2.0pp, all trivial and three of five with the *wrong* sign. **Funding stress around an auction is essentially independent of whether `I'` fired.** That is itself informative: the two legs of the letter's "and/or" are not measuring the same stress.

**H2 (the funding leg points the way a demand-hole confirmation should): NOT CONFIRMED.** The primary leg F2 returns p=0.523 on a paired cell of **19** — above the power floor, so **this is a genuine null, not an underpowered one.** That is the strongest form a null can take here and it is the headline.

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

⇒ **This is the honest caveat on the headline: the null is clean for the PRIMARY leg, and the two underpowered level-on-day legs point the other way.** Re-test when n allows.

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
| **Funding leg (SOFR−IORB)** | **Measured. Primary leg a clean adequately-powered NULL (p=0.523). No separation. H2 not confirmed.** Two underpowered level-on-day legs lean the other way. |
| Letter's instrument set | **Now fully measured.** L271's "stock and/or SOFR−IORB" has no remaining unexamined half. |

**The "premature while half the instrument set is unmeasured" objection this desk raised at 13:4x is now DISCHARGED — by measurement, not by argument.** Both halves are done and neither supports the pairing as constructed.

⛔ **STILL NO RECOMMENDATION FROM BOND.** Leg ② is Will's ruling and PROME's rec is already on the record (PARK any kill change). **Nothing here is a reason to loosen a kill**, and the desk that would benefit from loosening it is this one.

---

## 6 · Limits carried forward from the pre-registration

Unchanged and still binding: small cells (the decisive ones are 19, 8 and 6); **multiple comparisons corrected as pre-committed, which is what demotes F4 to suggestive**; refunding-week clustering breaks independence; one regime (2022–2026, a ceiling not a choice); one outcome at one horizon.

**One limit specific to this leg:** `IORB` begins 2021-07-29, so the spread cannot reach earlier even where FR2004 could. The universe is unchanged at 224 because the binding constraint remains the 2022-01-05 bucket epoch.

## 7 · Reproduce

Pre-registration `c563a9ff6` fixes legs, primary, outcome, statistic, seed, power floor and correction. Re-running it reproduces this table.
