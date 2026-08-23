# WALTER → Will · 2026-08-23 · **Leg 3b re-score: the bar is WRONG, not stale — and the MEDIAN is the wrong statistic**

**Run under your greenlight (relayed by PROME, verbatim *"approve both"*), your sequencing: re-score FIRST, bar work conditional on what it says.** ⛔ **This is a PROPOSAL. I hold no standing permission for `MESSAGING/CROSS_SESSION_MESSAGING.md`; the ≥7d bar stays in force as written until you rule.**

---

## ⚠️ AMENDMENT 2026-08-23 ~19:3xZ — **MY RE-SCORE WAS A NULL TEST, AND THE REAL TEST PARTLY CONTRADICTS THIS PROPOSAL'S TITLE. READ THIS BEFORE §①.**

**PROME's critique, accepted in full: between the 8/22 scoring and my 8/23 re-score, ZERO new observations entered for six of the seven desks** — none of HENRY/BROCK/OTTO/SHADE/CORAL/ZHAO committed on 8/23. **A median over 13-36 observations cannot move when no observation is added.** ⇒ ***"Not one desk's median moved" was guaranteed by construction, not discovered.* The instrument was structurally incapable of detecting the thing it was run to detect** — and I presented it as the proposal's lead evidence. `[[finding_verification_zero_is_ambiguous]]`, committed by me one day after writing that a check certifies its scope and not your conclusion.

**So I ran the test it should have been — a longer baseline, JUN-JUL window vs AUGUST window:**

| desk | Jun-Jul med (n) | Aug med (n) | verdict |
|---|---:|---:|---|
| **HENRY** | **2.0** (18) | **7.0** (2) | 🔴 **SLOWED — and 7.0 PASSES the ≥7d bar** |
| ZHAO | 7 (3) | 18 (1) | SLOWED |
| BROCK | 5.0 (12) | 5.0 (2) | unchanged |
| SHADE | 5.5 (8) | 5.0 (2) | sped up |
| MARCO | 7 (7) | 1 (3) | sped up |
| OTTO | 13.5 (4) | 11 (1) | sped up |
| **CORAL** | 1 (9) | **— (0)** | ⚠️ **NOT COMPUTABLE** |

🔴 **THIS BREAKS THE CLEAN "WRONG, NOT STALE" VERDICT AND I AM WITHDRAWING THE SECOND HALF.** **HENRY genuinely slowed, 2.0d → 7.0d — and on an August window HENRY would PASS ≥7d.** Its all-history median reads 4.0d only because **18 Jun-Jul observations at 2.0d outvote 2 August observations at 7.0d.** ⇒ **There IS a staleness component, my original re-score could not see it, and the title of this document over-claims.**

**What SURVIVES, and it carries the proposal on its own:** **§② — the 8/22 justification used a FREQUENCY and a RECENCY, not the median the rule specifies.** That finding needs no re-score. **The bar is wrong; whether it is ALSO stale is now "partly yes, on HENRY."**

## 🔑 AND THE REAL DEFECT IS A THIRD UNDECLARED PARAMETER — **THE WINDOW**

The rule specifies neither the **statistic** (median vs frequency vs recency — §②), nor the **estimator** (p75 interpolation — §⑥.5), nor the **WINDOW**. **All three are free, and each alone flips verdicts.**

⛔ **And the window cannot simply be fixed to "recent," because the trade-off is worst exactly where the gate matters: CORAL has ZERO computable August gaps — one commit-day all month.** **A recent window collapses to no sample on precisely the dark desks the doorbell exists to catch, while all-history blends regimes and hides a desk that just slowed.** **I do not have a resolution and I am not proposing one** — but any bar Will rules should name its window, or it will be re-litigated the first time two desks are measured differently.

## ① THE ORIGINAL RE-SCORE — **SUPERSEDED BY THE AMENDMENT ABOVE; retained for the record.** Not one desk's cadence moved.

Median inter-session gap (commit-days, authored — the ruled definition), computed **as of 8/22** and **as of 8/23**:

| desk | med @8/22 | med @8/23 | moved? |
|---|---:|---:|---|
| HENRY | 4 | 4 | **NO** |
| BROCK | 5.0 | 5.0 | **NO** |
| MARCO | 6 | 6 | **NO** |
| ZHAO | 6 | 6 | **NO** |
| OTTO | 9.5 | 9.5 | **NO** |
| SHADE | 6.0 | 6.0 | **NO** |
| CORAL | 4.5 | 4.5 | **NO** |

⇒ **The backlog did not move off HENRY and BROCK.** Their medians on the night the rule was written are exactly what they are now, and both fail ≥7d. **Per my own commitment: had this said "stale," I would have stopped here and told you the bar work was solving yesterday's problem. It doesn't, so it isn't.**

## ② WHY THE ≈3-of-7 WAS WRONG — the justification never computed a median

`BOARD_CONSUMPTION_SPEC` line 268, my own text: *"HENRY and BROCK now pass on 3b (53 unfiled / 7 ACTION, **ran 3 days that month**, oldest unintegrated 15d; and 16 / 6, **last run 8/13**)."*

**"Ran 3 days that month" is a FREQUENCY. "Last run 8/13" is a RECENCY. Neither is the MEDIAN the rule went on to specify.**

⚠️ **And both inputs were FACTUALLY CORRECT** — I verified them: HENRY did run exactly 3 days in August; BROCK's last run was 8/13. **Correct inputs, wrong statistic, clean-looking result.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — now inside the justification of the rule that finding was used to audit.

## ③ 🔑 THE REAL DEFECT — **every desk is BURSTY, and the median is dominated by within-burst gaps**

| desk | median | mean | mean/med | longest gap | dark now |
|---|---:|---:|---:|---:|---:|
| HENRY | 4 | 5.7 | 1.4× | 34d | 3d |
| BROCK | 5.0 | 6.8 | 1.4× | 23d | 10d |
| MARCO | 6 | 8 | 1.3× | 39d | 1d |
| ZHAO | 6 | 14.5 | **2.4×** | 107d | 2d |
| OTTO | 9.5 | 11.9 | 1.3× | 36d | 9d |
| SHADE | 6.0 | 13.6 | **2.3×** | 104d | 10d |
| **CORAL** | 4.5 | 14.9 | **3.3×** | **128d** | 20d |

**Desks work in bursts: several consecutive days, then a long silence.** The 1-day within-burst gaps are the MAJORITY OF GAPS; the long silences are the MAJORITY OF CALENDAR DAYS. **A median counts gaps, so it reports the burst and hides the silence.**

⛔ **CORAL is the proof: median 4.5d, longest gap 128d.** The gate's own statistic describes CORAL as one of the most responsive desks on the board. It had been dark 20 days.

⇒ **The gate measures the typical gap while the risk lives entirely in the tail. That is a category error, not a mis-set constant — which is why I am not proposing you simply lower 7d.**

## ④ PROPOSED REPLACEMENT — self-normalising, no universal constant, and it fixes leg 2's perversity

**Replace both legs with one test: is this desk dark for LONGER THAN IS NORMAL FOR ITSELF?**

> **3b (proposed):** an unconsumed `action:` item exists **AND** the desk's **current dark duration exceeds its own 75th-percentile inter-session gap.**

| desk | dark now | own p75 | fires? |
|---|---:|---:|---|
| HENRY | 3d | 8d | no |
| BROCK | 10d | 8d | **FIRE** |
| MARCO | 1d | 9d | no |
| ZHAO | 2d | 11d | no |
| OTTO | 9d | 21d | no |
| SHADE | 10d | 9d | **FIRE** |
| CORAL | 20d | 9d | **FIRE** |

**3-of-7 — the same headline as the amendment projected, but reached honestly and on the desks that are actually overdue *right now*.**

**What it fixes:**
- **Leg 2's perversity is gone.** PROME's finding was that `oldest > median` gets *harder* as a desk darkens. Here the comparison is a desk against **its own** distribution, so a structurally-dark desk isn't penalised for being structurally dark — **OTTO at 9d dark against its own 21d p75 correctly does NOT fire**, and stops "resolving itself by decay."
- **The tail is what's measured**, so CORAL-shaped desks (low median, enormous variance) become visible.
- **No universal constant to calibrate**, so it cannot fall into the trap the ≥7d bar fell into.

## ⑤ ⚠️ AND THE FINDING I DID NOT EXPECT — HENRY'S BACKLOG IS NOT A DARKNESS PROBLEM

**HENRY does not fire, and should not: it booted 3 days ago.** It holds — **whole-inbox, every sender, per PROME's count which I verified: 28 top-level + 53 in `inbox/WALTER/` = 81 UNCONSUMED ITEMS** (I originally reported "6 ACTION," which was my own lane only — **the same lane-vs-whole-inbox undercount I conceded on CORAL, recurring in the same session**). Oldest WALTER item 16d. It **ran 3 days in August** and last booted **8/20**.

⇒ **HENRY boots and does not drain.** A doorbell asks PROME to *wake a desk that is asleep*. **HENRY is not asleep.** Doorbelling it treats the wrong disease, and under the current gate HENRY was the amendment's headline beneficiary. ⇒ **A desk carrying 81 unconsumed items while running three days ago is not a darkness problem at any bar.**

🔑 **The measured backlog has (at least) two distinct causes and the doorbell only addresses one.** I'd flag this as the more valuable half of the re-score: **whatever bar you rule, HENRY's 6 ACTION items are not reachable by any darkness test**, and something else — a consume boot-step, an orchestrated drain — is the instrument for that class.

## ⑥ Carried caveats — none of these are resolved by the above

1. ⚠️ **The commit-days proxy UNDERCOUNTS same-day multi-sessions** (PROME ran 4 sessions on 8/23, scored as 1). **True gaps are shorter, so every median/mean/p75 above is biased HIGH.** For the proposed test this bias is *mild and self-cancelling* (it inflates both the desk's p75 and its measured dark duration) — but it is **not zero**, and I have not quantified it.
2. **n=7 desks, single-repo, and burstiness is measured over each desk's whole history** — a desk that changed working style mid-life has a distribution blending two regimes.
3. ✅ **ESTIMATOR TESTED — no verdict flips.** PROME reproduced the 3-of-7 exactly but with **materially different p75 VALUES** (OTTO 13.5 vs my 21, SHADE 7.5 vs 9, CORAL 8.2 vs 9) — pure percentile-interpolation difference. **I re-ran mine under both nearest-rank and linear interpolation: the verdict set is IDENTICAL under both, zero flips.** ⇒ **the estimator is a real free parameter but is NOT currently load-bearing.** **Declare it in the spec anyway** — two correct implementations already disagree on the values, and that is this weekend's lesson in a new costume.
4. **p75 is a choice, not a derivation.** I picked it because it sits above the burst cluster and below the extreme tail on all seven desks. **p80 or p90 would fire less; I have not argued 75 is optimal, only that it is defensible and that I am not tuning it toward firing more.**
5. **Refusals reported alongside fires** (per `GATE-OP-SCALE-01`'s guard): the proposal fires **3**, refuses **4**, and refuses **HENRY specifically** — the desk with the largest ACTION backlog in the set. **A re-tune that only ever loosens is the quota fingerprint; this one declines the biggest backlog on the board, which is the evidence it isn't that.**

## ⑦ What I am asking for

**Nothing to apply.** Three questions: ① adopt the self-normalising form, keep ≥7d, or something else? ② if adopted, is p75 the right percentile? ③ **§⑤ — does the HENRY class (boots, doesn't drain) get its own instrument, or is it out of scope for the doorbell entirely?**

**Measurement backing:** `research/2026-08-23_leg3b-measured-does-not-reach-its-own-named-beneficiaries.md` · re-score computed this session, authored commits only, per the rule's own 🔴 clause.
