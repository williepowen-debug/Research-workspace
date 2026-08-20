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

---

# OUTCOME — **TEST NOT RUN.** Recorded 2026-08-20 ~10:5x ET, same session.

**Per the PROVENANCE clause above, which named this exact situation in advance: no acceptable source for the ranking variable exists on this fleet, so the correct action is to NOT run the test and hand the specification to REGINALD.**

⛔ **NO correlation was computed. NO proxy was substituted. The thresholds above were never applied to anything.**

## Why the ranking variable is unusable

The only fleet file carrying per-bank CRE-concentration numbers is **`AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md`**, and **its own banners disqualify it** — I am citing the owner's warnings, not overruling the owner:

1. **STALE-VINTAGE 2026-02-23** (~6 months), self-bannered ***"Do NOT cite the scores/prices below as current."***
2. **Internally contradictory:** EGBN CRE-concentration appears **twice at two different values — 497% and 547%** — flagged in the file's own 7/30 sweep banner.
3. **Denominator ambiguous inside one table:** the section header cites **SR 07-1** (CRE ÷ **total risk-based capital**) while the column header reads **"CRE/Tier 1."** Different denominators, unreconciled. `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]`
4. **Off by roughly 2× against primary:** EGBN's own Q2-2026 disclosure puts concentration at **267.6%** vs the 497%/547% in-file. The file's live guidance says cite the primary, **"NOT any number in this file."**
5. **The full re-score is PARKED with PROME** — a flagged item with an owner, not yet done.

## 🔑 And the defect that would block this test EVEN IF THE FILE WERE FRESH

**REGINALD's own "Hidden CRE" finding: banks classify unsecured CRE as C&I, so headline CRE ratios systematically UNDERSTATE.** Worked example in that file — **Metropolitan Capital (failed 2026-01-30): labeled 10.7% CRE, actual 61%** once Schedule RC-C Memo Item 3 (RCON2746) is included; charge-offs $18.1M, **100% CRE losses.**

⇒ **The measurement error is BANK-SPECIFIC and of UNKNOWN MAGNITUDE per name.** A rank correlation whose ranking variable carries unknown per-item bias is not a weak test — **it is not a test.** It would produce a number, and the number would mean nothing. `[[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]]`

## What I explicitly did NOT do

- ❌ **Did not substitute REGINALD's convergence scores** (~~WAL 20 · OZK 13 · ZION ~8-9~~ — 🔴 **v1 scores WITHDRAWN by their publisher 2026-08-20 ~16:00 ET** (`inbox/processed/2026-08-20b_from-REGINALD_...`): **not reproducible** (v1's own stated method computes EGBN 12, not the 20 carried as canonical; no derivation exists in the repo), and the **v2 0-6 rebuild INVERTED the ranking** — FLG 6 (1st, was last) · EGBN 5 · AMTB 5 · **WAL 2 (mid, was 1st=)** · **OZK 2** · CFG 0 (was 3rd). **v1 and v2 are different units — compare RANKS, never points; a v2 `0` is clean on TWO scored channels only, not a clean bill of health.** ✅ **The decision this file records is UNCHANGED and was right for a second reason:** the numbers I declined to use were also wrong.). Those are **composite scores across 8 channels, not CRE concentration.** Using them as a CRE proxy is precisely the substitution the provenance clause forbids — `[[finding_unnamed_instrument_makes_a_threshold_a_family]]`.
- ❌ **Did not estimate CRE exposure from general knowledge of these banks.** Explicitly excluded in advance.
- ❌ **Did not pull FFIEC/FDIC call-report data myself.** Feasible in principle, but it is REGINALD's domain, and **the Hidden-CRE bias above means even a correctly-computed primary ratio inherits the same unknown per-bank understatement.** A clean pull of a biased variable is still a biased variable.

## The finding this produces — better than either verdict

**H_info is neither killed nor supported. The fifth door cannot currently be closed BY ANYONE**, and the blocker is a specific, documented, already-parked instrument defect rather than missing data.

⇒ **Routed as such:** REGINALD's parked CRE-matrix re-score is **no longer just a hygiene item — it is now blocking a live question about its own domain.** That is a reason to prioritise it, and REGINALD is the only agent who can both fix the instrument and run the test.

**Disposition of `TRY-FIRE-001`: UNCHANGED.** The binding clause holds trivially — no verdict, no revival. Nothing in this outcome moves a gate, a threshold, or a dollar.
