# WQ-158 OUT-OF-SAMPLE PULL — PRE-REGISTRATION (frozen BEFORE any data is pulled)

**Commissioned by Will, 2026-09-03, in-session: *"commission both pulls."*** Unblocks the two BLOCKED rows in `OPEN_ITEMS_2026-09-03.md`.
**This file is committed BEFORE the first filing is opened.** Git timestamp is the proof. Anything added after the data lands is written in a dated ADDENDUM below, never edited into the spec.

## 0. Why this exists
My own `LESSONS #31`: I set thresholds by looking at the numbers already on my register and placing the bar just past them — which produced a level that could not fire (`≥3 consecutive sub-100% quarters`, structurally ungradable on 8 of 9 vehicles) and one 3pp below the panel's observed minimum (`<20% single-quarter satisfaction`). **Re-placing either level off the same panel would repeat the error with more data.** PROME's WQ-158 ruling (2026-09-03): both levels **INERT / UNGRADABLE off this panel**, re-place **only** against an out-of-sample referent.

## 1. ⚠️ THIS IS NOT A BLIND PRE-REGISTRATION, AND I WILL NOT CLAIM IT IS
The BREIT 2022-23 gate episode was heavily covered and **I carry general prior exposure to it.** My 8/13 BRK-02 spec could claim blindness under a C4 metadata-only rule; **this one cannot.** It is a **weak-blind** pre-registration: the *spec* is frozen before the data, but my priors in §4 are contaminated by recollection. **Priors are therefore recorded to be scored as WEAK evidence of calibration, not as a clean forecast.** Stating this now, because discovering it at write-up would be the convenient time to omit it.

## 2. The measure — DECLARED BEFORE THE DATA
- **Satisfaction = shares (or $) ACCEPTED ÷ shares (or $) VALIDLY SUBMITTED, at the same offer, from a filing-primary source.**
- ⛔ **`cap ÷ requests` is NOT satisfaction** — it assumes fill-to-cap. Three vehicles on my own register are contaminated this way; I will not import the error.
- ⛔ **A proration percentage disclosed by the issuer IS satisfaction** and is preferred over anything I compute.
- ⛔ **If a filing discloses only shares repurchased and NOT the amount submitted, satisfaction is NOT COMPUTABLE for that period.** I report **NOT MEASURABLE** and exclude the cell. I do **not** back into it.

## 3. Commensurability — the trap declared in advance
**BREIT and SREIT ran MONTHLY repurchases under a 2%-of-NAV monthly / 5% quarterly cap; BCRED and CCLFX are QUARTERLY.** A "consecutive **quarter**" rule cannot be read off a monthly tender without a stated aggregation. **DECLARED NOW:**
- **Quarterly satisfaction for a monthly-tender vehicle = Σ accepted over the three calendar months ÷ Σ submitted over the same three months.** Not a mean of monthly rates (that would weight a tiny month equally with a large one).
- A quarter with any month NOT MEASURABLE is itself **NOT MEASURABLE**, not partially counted.
- **Monthly rates are ALSO recorded separately**, because the `<20%` level may be reachable monthly and not quarterly — and **which unit the level is stated in is exactly the ambiguity that made my own register ungradable.**

## 4. Priors, recorded before the pull (weak-blind, per §1)
| # | Claim | Prior |
|---|---|---|
| P1 | BREIT shows **≥3 consecutive quarters** of sub-100% satisfaction during 2022-12 → 2023-12 | **85%** |
| P2 | BREIT reaches **<20% satisfaction in at least one QUARTER** (quarterly aggregation, §3) | **40%** |
| P3 | BREIT reaches **<20% in at least one MONTH** | **65%** |
| P4 | SREIT independently shows ≥3 consecutive sub-100% quarters | **75%** |
| P5 | At least one BREIT month is **NOT MEASURABLE** under §2 (submitted amount undisclosed) | **50%** |
| P6 | CCLFX's four offers yield a genuine satisfaction series (submitted amounts disclosed in `N-23C3A`/`N-CSR`) | **55%** |

## 5. Decision rule — FIXED NOW, so the data cannot pick it
| Out-of-sample result | What I recommend to PROME/Will |
|---|---|
| **BOTH levels reached** in the reference episode | Levels are **reachable in a real wrapper-redemption stress**. Keep them as written; my panel's "0 of N" becomes a genuine but **under-powered** negative, and the fix is panel depth, not the levels. |
| **NEITHER reached** | Levels are **unreachable even in the reference stress ⇒ mis-specified.** Re-place at the out-of-sample distribution (I will propose percentiles, **Will rules the number**). |
| **Persistence reached, `<20%` not** | The `≥3 consecutive` leg survives; **`<20%` is too strict** — re-place that leg only. |
| **`<20%` reached, persistence not** | The `<20%` leg survives; **`≥3 consecutive` is the un-gradable one** — and that would confirm the depth diagnosis directly. |
| **Fewer than 3 measurable quarters at BOTH referents** | ⛔ **NO-VERDICT.** The referent cannot grade the levels either, and I say so rather than reaching for a third dataset to get an answer. |

⛔ **I do not set any replacement number in this session.** A threshold level is Will-gated. I measure, I propose percentiles, Will rules.
⛔ **No BROCK vector is rescored on this pull.** It is a spec repair, not evidence about private credit today.

## 6. Sources — named before the pull, so a miss is visible
- **BREIT** — Blackstone Real Estate Income Trust: `data.sec.gov/submissions/CIK<BREIT>.json` → 8-K (Item 8.01 repurchase results) + SC TO / N-2 series, **2022-11 → 2023-12**.
- **SREIT** — Starwood Real Estate Income Trust: same method, same window.
- **CCLFX** — Cliffwater Corporate Lending Fund: **`N-23C3A`** (repurchase-offer notification) ×4 + **`N-CSR`/`N-CSRS`** financial highlights, covering the four offers behind my register's fulfilment series **3.42 → 2.90 → 5.32 → 7.00%**.
- 🔑 **My register's CCLFX cell is a FULFILMENT series, not a satisfaction series** — without the submitted leg it cannot grade a satisfaction threshold at all. **Converting it is the point of this pull, and if the submitted leg is not disclosed the cell stays NOT MEASURABLE and my register says so.**

**— BROCK, 2026-09-03, before the first filing was opened.**
