# WALTER → Will · 2026-08-23 · **Leg 3b re-score: the bar is WRONG, not stale — and the MEDIAN is the wrong statistic**

**Run under your greenlight (relayed by PROME, verbatim *"approve both"*), your sequencing: re-score FIRST, bar work conditional on what it says.** ⛔ **This is a PROPOSAL. I hold no standing permission for `MESSAGING/CROSS_SESSION_MESSAGING.md`; the ≥7d bar stays in force as written until you rule.**

---

## ① THE RE-SCORE ANSWERS IT: **WRONG, not stale.** Not one desk's cadence moved.

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

**HENRY does not fire, and should not: it booted 3 days ago.** It holds **6 unconsumed ACTION items, oldest 16d**, and it **ran 3 days in August**.

⇒ **HENRY boots and does not drain.** A doorbell asks PROME to *wake a desk that is asleep*. **HENRY is not asleep.** Doorbelling it treats the wrong disease, and under the current gate HENRY was the amendment's headline beneficiary.

🔑 **The measured backlog has (at least) two distinct causes and the doorbell only addresses one.** I'd flag this as the more valuable half of the re-score: **whatever bar you rule, HENRY's 6 ACTION items are not reachable by any darkness test**, and something else — a consume boot-step, an orchestrated drain — is the instrument for that class.

## ⑥ Carried caveats — none of these are resolved by the above

1. ⚠️ **The commit-days proxy UNDERCOUNTS same-day multi-sessions** (PROME ran 4 sessions on 8/23, scored as 1). **True gaps are shorter, so every median/mean/p75 above is biased HIGH.** For the proposed test this bias is *mild and self-cancelling* (it inflates both the desk's p75 and its measured dark duration) — but it is **not zero**, and I have not quantified it.
2. **n=7 desks, single-repo, and burstiness is measured over each desk's whole history** — a desk that changed working style mid-life has a distribution blending two regimes.
3. **p75 is a choice, not a derivation.** I picked it because it sits above the burst cluster and below the extreme tail on all seven desks. **p80 or p90 would fire less; I have not argued 75 is optimal, only that it is defensible and that I am not tuning it toward firing more.**
4. **Refusals reported alongside fires** (per `GATE-OP-SCALE-01`'s guard): the proposal fires **3**, refuses **4**, and refuses **HENRY specifically** — the desk with the largest ACTION backlog in the set. **A re-tune that only ever loosens is the quota fingerprint; this one declines the biggest backlog on the board, which is the evidence it isn't that.**

## ⑦ What I am asking for

**Nothing to apply.** Three questions: ① adopt the self-normalising form, keep ≥7d, or something else? ② if adopted, is p75 the right percentile? ③ **§⑤ — does the HENRY class (boots, doesn't drain) get its own instrument, or is it out of scope for the doorbell entirely?**

**Measurement backing:** `research/2026-08-23_leg3b-measured-does-not-reach-its-own-named-beneficiaries.md` · re-score computed this session, authored commits only, per the rule's own 🔴 clause.
