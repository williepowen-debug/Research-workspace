# PRE-REGISTRATION — CRE-exposure cross-sectional test of the information-channel hypothesis

**Written:** 2026-08-20 Thu ~10:5x ET by TERRY. **COMMITTED BEFORE ANY CORRELATION WAS COMPUTED OR ANY CRE FIGURE WAS LOOKED UP.**
**Test proposed by:** CREED (cross-session, 2026-08-20), who also supplied the caution that forced this file.

> ⚠️ **The whole point of this document is its COMMIT TIMESTAMP.** If the thresholds below were written after seeing the result they are worthless. The git history is the evidence. `[[finding_prereg_verdict_boundary_must_be_a_number]]`

## The hypothesis under test

**H_info:** the broad regional-bank underperformance beginning 2026-08-14 is an **information-channel reprice** to the July Trepp CMBS print (HOMER-sourced 8/12, CREED-graded 8/13, **series-maximum $3.96B in matured-balloon newly-delinquent balances, +131% vs June**) — i.e. the market re-rating CRE credit risk two days before the move.

**Why it needs testing rather than dismissing:** CREED's `FLOW-CREED-02` speed class (`QUARTERS`, MAT→VAL→FND) governs the *fundamental* channel — appraisals, marks, provisions. **Equities reprice on expectations, so a QUARTERS mechanism class does not by itself exclude a fast information response.** The dates are consistent (print 8/12-13, move 8/14).

⚠️ **DISCLOSED CONFLICT: H_info, if true, revives `TRY-FIRE-001`, a card I own.** I raised it against myself and did not adopt it. **This pre-registration exists specifically because a number attached to a self-serving hypothesis is more tempting than the hypothesis alone** — CREED's warning, adopted verbatim.

## The prediction that discriminates

If **H_info** is true, the move is a **CRE re-rating**, and a CRE re-rating **must discriminate by CRE exposure**: banks with heavy CRE concentration should fall materially more than CRE-light banks.

If the move is a **factor/flow/rotation** event, returns should be **roughly uncorrelated with CRE exposure**.

**Prior evidence, already in hand and already weak against H_info (CREED's point):** the move is **10 of 10 names down, median −4.91%**. A CRE-information event should sort the cohort, not take all of it.

## PRE-COMMITTED DECISION RULE — thresholds fixed before observation

**Statistic:** Spearman rank correlation ρ between (CRE concentration rank) and (return rank, most-negative = most CRE-exposed under H_info), across the 10 names: OZK · PNFP · KEY · ZION · FHN · VLY · RF · HBAN · CFR · WAL, over **2026-08-14 → 2026-08-20**.

**Secondary:** spread between the mean return of the **3 most** and **3 least** CRE-concentrated names.

| ρ | verdict |
|---|---|
| **ρ ≤ +0.20** | ✅ **H_info KILLED on evidence.** The move does not discriminate by CRE exposure. Fifth door closed. |
| **+0.20 < ρ < +0.60** | ⚠️ **NO VERDICT.** n=10 cannot separate these. **This band is deliberately WIDE and it is the expected outcome.** |
| **ρ ≥ +0.60 AND top-3/bottom-3 spread > 2.0pp** | 🔴 **H_info SURVIVES.** Both legs required — the correlation alone is not enough. |

⛔ **BINDING, and written before the result: a NO-VERDICT does NOT revive `TRY-FIRE-001`.** Under n=10 with SE ≈ 0.33 under the null, anything below +0.60 is noise-compatible. **A weak positive is not evidence; it is the absence of evidence with a number attached.** The card's disposition is unchanged by any outcome in the middle band.

⛔ **The thresholds may NOT be adjusted after observation.** If they turn out to be badly chosen, that is recorded as a defect of this pre-registration — the test is re-run fresh on new data, never re-scored on the same data.

## DATA PROVENANCE — the binding constraint

**CRE concentration figures are REGINALD's, and I will not estimate them.** CREED's instruction, adopted: *"REGINALD owns those figures — don't estimate them yourself."*

Acceptable sources, in order:
1. A CRE-concentration figure **published by REGINALD** in its own files, cited to the row.
2. A **primary regulatory** source (FDIC/call-report CRE-to-risk-based-capital), pulled and named.

⛔ **NOT acceptable:** my own recollection of which banks are "CRE-heavy," any ranking I could construct from general knowledge, or a proxy invented to make the test runnable. **`[[finding_unnamed_instrument_makes_a_threshold_a_family]]` — an unnamed instrument lets me pick the flattering member after the fact.**

**If no acceptable source is available to me, the correct outcome is NOT to run the test.** It is to hand this specification, unrun, to REGINALD — which still converts an open question into a defined experiment and is a better deliverable than a number I cannot source.

## What either outcome buys

- **KILLED** → a **fifth closed door**, on the tape rather than on a qualitative speed class. Stops REGINALD spending its spawn re-testing a door already shut, and sharpens the ask to *"the answer is somewhere none of us has looked."*
- **NO VERDICT** → the honest and expected result at n=10. The ask is unchanged.
- **SURVIVES** → a **REGINALD question**, not a TERRY green light. `TRY-FIRE-001` still needs all three pre-registered build conditions (named mechanism · ~3 more sessions · credit confirms or vehicle changes) and root rule #6 at entry. **This test can never, on its own, fire anything.**

---
*TERRY proposes only. Nothing here moves money or a threshold.*
