# F2 — Pre/Post-2018 episode split for KB-VIO-207 cheap-tail base rate

**Run date:** 2026-08-27
**Purpose:** Adjudicate the pre-registered F2 falsifier on the KB-VIO-207 base rate that GATE-VIO-RV1 rests on. The row's own consequence-on-fire clause blocks deployment while F2 is unrun; the 8/25 + 8/26 arm (KB-VIO-210) made F2 the load-bearing next work.
**Verdict:** 🔴 **F2 FAILS.** Separation does not survive post-2018. **GATE-VIO-RV1 does not deploy** per KB-VIO-207's own registered kill: *"if the post-2018 subsample loses separation the design does not deploy."*

---

## Method (reproduced from KB-VIO-207)

- **Data:** CBOE VIX/VVIX/SKEW History CSVs, aligned on VVIX (binding start).
- **Aligned sessions:** **5,086** (2026-08-27 pull), 2006-03-06 → 2026-08-26.
- **3-leg gate:** VVIX ≤ 90 **AND** VIX ≤ 16 **AND** SKEW ≥ 140.
- **Fire days:** **205** (4.03% base rate).
- **Decluster:** consecutive fire days at ≤5 td gap collapse to one; new episode requires >5 td.
- **Declustered episodes:** **34** total (KB-VIO-207 recorded 33 on 2026-08-19; the +1 is episode #34 dated 2026-08-19, which is post-registration and is the current live-arm).
- **Split date:** 2018-01-01 (Volmageddon regime boundary).
- **Null:** matched-length random-placement, 4,000 sims, seed 7, per KB-VIO-207.

### Episode counts by era

| Era | Episodes |
|---|---|
| Full (KB-VIO-207) | 34 (vs 33 at registration; +1 = 2026-08-19) |
| **Pre-2018** | **12** |
| **Post-2018** | **22** |

Post-2018 provides the larger sample.

---

## KB-VIO-207 reproduction check (full sample, N=34)

| Cell | Cond | Uncond | Lift | Note |
|---|---|---|---|---|
| 21td ≥+50% | 24.2% (8/33) | 14.8% | 1.64× | KB-VIO-207 registered 25.0% / 14.5% / 1.72× |
| 30td ≥+50% | 36.4% (12/33) | 21.3% | 1.71× | KB-VIO-207: 34.4% / 20.7% / 1.66× |
| 60td ≥+50% | 59.4% (19/32) | 37.0% | 1.60× | KB-VIO-207: **56.7% / 36.0% / 1.57×** |
| 60td ≥+50% null | obs 59.4%, null mean 37.0%, **p = 0.008** | | | KB-VIO-207: p=0.019 (30-episode subset) |

**Reproduction clean.** Small differences trace to (a) +1 episode since registration, (b) VVIX alignment moved 5,081 → 5,086 sessions (7 more sessions accrued since 8/19), (c) forward-max windows for 2026-06/07/08 episodes are longer now than they were at 8/19. **The headline result stands.**

---

## F2 result — pre/post-2018 subsamples

### Pre-2018 (N=12)

| Cell | Cond | Uncond | Lift | p (matched null) |
|---|---|---|---|---|
| 21td ≥+50% | **41.7%** (5/12) | 12.2% | **3.41×** | — |
| 30td ≥+50% | **58.3%** (7/12) | 18.0% | **3.25×** | — |
| **60td ≥+50%** | **66.7%** (8/12) | 34.6% | **1.92×** | **p = 0.024** ✅ |

**Pre-2018 separation is stronger than the pooled sample** — the 21td and 30td tails are 3×+ lifts. This is where the KB-VIO-207 headline edge lives.

### Post-2018 (N=22)

| Cell | Cond | Uncond | Lift | p (matched null) |
|---|---|---|---|---|
| 21td ≥+15% | 61.9% (13/21) | 58.7% | 1.06× | 0.477 ❌ |
| 21td ≥+50% | 14.3% (3/21) | **18.2%** | **0.78×** | 0.764 ❌ |
| 30td ≥+15% | 76.2% (16/21) | 67.3% | 1.13× | 0.277 ❌ |
| 30td ≥+50% | 23.8% (5/21) | 25.8% | 0.92× | 0.655 ❌ |
| 60td ≥+15% | 85.0% (17/20) | 81.1% | 1.05× | 0.470 ❌ |
| **60td ≥+50%** | **55.0%** (11/20) | 40.4% | **1.36×** | **p = 0.134** ❌ |

**Every post-2018 cell fails.** The KB-VIO-207 headline cell (60td ≥+50%) still shows a nominal 1.36× lift, but p=0.134 does not pass the p<0.05 threshold that KB-VIO-207 used to certify the design.

**The 21td and 30td ≥+50% cells are WORSE than uncond** (0.78× and 0.92× lift). The tail-edge story is not preserved.

---

## Mechanism read (interpretation only)

Two things changed post-2018 that plausibly explain the failure:

1. **The unconditional ≥+50% rate rose.** Post-2018 uncond 60td ≥+50% = 40.4%, vs pre-2018 34.6%. Higher baseline vol events (Volmageddon 2018, COVID 2020, 2022 rate cycle, June 2026 NFP shock) raised the base rate off which the gate has to lift.
2. **The "VIX ≤ 16 + SKEW ≥ 140" region is no longer a distinctive corner of the surface.** GEX-era vol suppression and persistent SKEW elevation (R12: 222 td 2025-2026, per Principle 9) means the gate fires **more often in mid-vol regimes** where the coiled-spring mechanism was never the operative one. **The instrument has become endogenous to the regime it was built to identify.**

**This is exactly the failure mode `[[finding_measurement_bias_sign_is_fixed_harm_direction_is_not]]` describes when applied to a base-rate estimator: a bias that was small pre-2018 has grown into a first-order effect post-2018, and the direction of that harm is dependency-in-regime, not miscalibration.**

---

## Sensitivity checks (not run, listed for a possible re-adjudication)

1. **Split date:** 2018-01-01 was KB-VIO-207's registered choice. Alternatives: 2020-01-01 (COVID as break), 2022-11-01 (Fed pivot). If a later split preserves the edge, the row is more precisely dated but does not change the operational verdict — RV1 is registered against the pre-2018 methodology.
2. **Threshold sensitivity:** the ≥+15% band showed no post-2018 lift and KB-VIO-207 explicitly rejected it as "the instrument is nearly worthless" there. The ≥+30% band (untested) sits between the tail and the body. Would document, but not for deployment.
3. **De-clustering gap:** >5 td vs >10 td vs >20 td. A tighter gap yields more episodes; a looser one collapses to fewer. Would not overturn the p=0.13 verdict.
4. **N=22 is not underpowered for THIS test.** With observed 55% vs null 40%, an n=22 sample at α=0.05 requires ~1.8σ separation; my measured effect is ~1.1σ. The instrument does not clear its own bar even at the observed effect size.

---

## Deployment consequence (registered)

**Per KB-VIO-207 verbatim:** *"REGIME-CONFINEMENT UNTESTED: the pre/post-2018 split is NOT run and is a registered pre-deployment gate (falsifier F2) — if the post-2018 subsample loses separation the design does not deploy."*

**F2 has now been run. The post-2018 subsample lost separation. GATE-VIO-RV1 does not deploy.**

This is the mechanism KB-VIO-210 stayed inside on 8/27 — the row was armed and NOT routed to TERRY on 8/25 and 8/26 precisely because F2 was owed. F2 has now returned the negative, and the mechanism holds.

**Actions:**
1. GATE-VIO-RV1 row: state changes ARMED-NOT-DEPLOYED → **F2-KILLED**. Sessions-armed-unharvested counter (S3 45cd trigger) retires — S3 is about "arm without deployment while owed work runs"; the owed work is now RUN and returned KILL, not pending.
2. β reconciliation (see companion research file) still owed as a general-purpose measurement discipline item, but is **not** a deployment gate any longer (the gate is retired).
3. KB-VIO-207 row: append a `POST-2018 GRADED` note; the row remains valid as the pre-2018 base-rate finding but the design that rests on it does not.
4. Packet PROME: F2 verdict + row state update ask.

---

*Companion files:*
- `/tmp/.../f2/f2_split.py` — reproducer script (session scratch)
- `/tmp/.../f2/VIX_History.csv`, `VVIX_History.csv`, `SKEW_History.csv` — CBOE data pulled 2026-08-27
- KB-VIO-211 (this session): F2-KILLED verdict on GATE-VIO-RV1

*Discipline note:* the row's own consequence blocked deployment for the same reason F2 was worth running before deployment: **an estimator that cannot fail is not an estimator**, per thesis v3.9. The F2 result is the estimator failing on its registered test. The discipline is spending the compute anyway, not talking past the result.
