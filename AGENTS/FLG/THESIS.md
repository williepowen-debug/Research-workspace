# FLG — THESIS

**Version: v0.1 — SKELETON, NOT A THESIS** · **Authored: 2026-08-20** (DAEDALUS, at build) · **Owner from first live session: FLG**

> ⚠️ **This document does not yet contain a thesis, and it must not be cited as one.** It is the structured set of **open questions** the desk was built to answer, plus the seed evidence bearing on each. A thesis-of-record (v1.0) is authored by FLG at its first live session, once the v1.0 bar at the foot of this file is met. *(Updated 2026-08-20 evening: Q1, the original blocking question, was answered and REFUTED at the primary the same day — the bar moved to Q2b.)*
>
> **Why a skeleton rather than a draft thesis:** a thesis written by the architect at build time would be DAEDALUS's forecast wearing FLG's name, and every later session would inherit it as prior work rather than test it. The desk's founding evidence is MIRROR-grade (extracted from REGINALD, not pulled by FLG). **Nothing here is load-bearing until FLG re-derives it.**

---

## The mechanism this desk exists to test

> **NYC rent-regulated multifamily repricing → CRE concentration → nonaccrual formation → reserve adequacy → capital.**

**Stage table** (blueprint §1, OTTO transmission form). `State` is the honest read at build, not a target.

| # | Stage | Mechanism | State at build (2026-08-20) |
|---|---|---|---|
| 1 | **Rent regulation constrains NOI** | HSTPA-2019 caps rent growth on stabilized units; NOI cannot rise to meet debt service | **OPEN — un-instrumented.** No RGB series in any FLG ledger yet. `TRIGGERS.tsv` T-06 is the wake row |
| 2 | **Refinance repricing** | Loans written at low rates reprice at maturity into higher rates against constrained NOI | **OPEN — un-instrumented.** The maturity-wall profile is not in the seed |
| 3 | **CRE concentration** | Multifamily + construction + non-owner-occ NFNR / total risk-based capital vs the SR 07-1 300% line | ⬇️ **DE-RISKING — 327.5% and FALLING** (−143pp over 11 quarters; ~2 quarters from crossing 300%). Level-high, trajectory-down. **Not deterioration.** Verified at primary 2026-08-20 |
| 4 | **Nonaccrual formation** | Constrained borrowers stop performing | ⚠️ **CONTESTED — 5.49% [25Q3] → 4.88%, but the fall may be MECHANICAL.** $232M charged off in 2026 H1; a rate falling by charge-off is not a rate falling by cure, and the roll-forward nets. **Not repair until Q2c splits it** |
| 5 | **Reserve adequacy** | ACL must cover recognised nonaccruals | 🔴 **THE LIVE STAGE — 29% and monotonically falling** (87% → 29%); ACL down in 8 of 8 quarters, $1.27B → $0.87B, vs a $3.0B nonaccrual book. **This is where the thesis now lives** (Q2b) |
| 6 | **Capital** | Losses exceed reserves → capital event | **NOT REACHED. No evidence at build.** Do not assume stage 6 from stages 3–5 |

**Read the state column honestly.** Stages 1 and 2 — *the causal front end, and the reason this is a separate desk* — are **entirely un-instrumented**. And after the 2026-08-20 primary re-read, **two of the three inherited 🔴 stages are improving**: concentration is de-risking and nonaccruals are past peak. **Only stage 5 is deteriorating.** The desk was created off a composite score whose two legs point in opposite directions — so it owns one live signal, not three, and it still lacks the mechanism that would explain it.

---

## The three open questions (in priority order)

### Q1 — Is the concentration ratio measuring risk, or measuring a shrinking denominator? ✅ **ANSWERED 2026-08-20 — REFUTED**

CRE concentration = CRE / total risk-based capital. FLG's book contracted **−28.8% in loans and −21.1% in assets** over eleven quarters (KB-FLG-005). If the easier-to-exit assets ran off first and multifamily is the stickiest leg, **the ratio rises while absolute CRE risk falls.**

✅ **ANSWERED THE SAME EVENING, AT THE PRIMARY, AND THE ANSWER IS NO** (REGINALD `fb1f68659`, matrix §3b, verified at artifact): CRE numerator **−32.2%** ($48.33B → $32.76B), total risk-based capital **flat at −2.6%** ($10.27B → $10.00B), ratio **−143pp and falling in all 11 quarters**. **The denominator held, so the artifact is arithmetically impossible on this name.** The composition intuition survived — multifamily *is* the stickiest leg (MF −28.6% vs construction −55.6%, non-OO −40.8%) — it simply does not produce the artifact.

🔴 **But the answer changed the read, and that is the durable result:** channel 1 is **level-high, trajectory-de-risking**, ~2 quarters from crossing below 300% at the current rate. **"Cohort-worst CRE concentration" must NOT be read as deterioration.** The concentration channel is not where this thesis lives.

⇒ **The load-bearing figure on this desk is 29% ACL/nonaccrual COVERAGE — not the 4.88% nonaccrual rate, and not the composite 6/6.** See Q2b.
- **Unblocked:** concentration thresholds may now be proposed — but base-rate them against a *falling* series, not a rising one.
- *(Hypothesis refuted, question worth asking. `finding_normalization_choice_picks_opposite_winners` still applies in reverse: the two normalizations AGREED, and the agreement is what redirected the desk.)*

### Q2 — Has the deleveraging already bottomed? 🔴 **LIVE, one print from resolution**

Total loans QoQ, eleven quarters: `−0.1, −2.9, −1.1, −10.9, −5.8, −3.0, −4.0, −1.9, −3.5, −0.6, **+0.9**`.

**Q2-2026 is the first positive quarter in the series**, and the prior four decelerate monotonically toward zero (KB-FLG-014, first-hand recomputation — all eleven cells reproduce against `total_loans_k`).

- **Resolves by:** the Q3-2026 Call Report, ~2026-11-14. A second positive quarter fires `EXIT_PROTOCOL.md` **K-1 — the thesis-kill.**
- **This is the desk's most important near-term fact and it points against the bear case.** It was found at build, on the same day the cohort ranked FLG worst.

### Q2b — Why is the reserve falling faster than the problem book resolves? ✅ **ANSWERED 2026-08-20 — and the answer is a THIRD case**

Nonaccruals are **past peak and improving** (5.49% [25Q3] → 4.88%). **ACL has fallen in every one of 8 quarters** ($1.27B [24Q2] → $0.87B). Coverage went **87% [24Q1] → 29%, monotonic**. The reserve is drawing down **~1.7× faster than the problem book resolves** (ACL −26% vs nonaccrual −15% off respective peaks), against a still-**$3.0B** nonaccrual book.

✅ **ANSWERED THE SAME EVENING** by REGINALD at Schedule RI-B Part II (`6dfd8ed53`, matrix §3b-ii; the identity was re-derived first-hand at FLG and **ties to the dollar**): begin **$1,029,999K** + provision **$15,923K** − charge-offs **$232,410K** + recoveries **$55,488K** = **$869,000K**.

**My binary was wrong — it needed a third cell:**

| Candidate | Verdict |
|---|---|
| **Release** into earnings | ❌ **NO** — provision is **positive in every quarter**; reserves were never reversed into income |
| Clean **disposition** (the EGBN case) | ❌ **NO** — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet |
| 🔴 **Consumption by charge-off with provisioning STOPPED** | ✅ **THIS** |

**The regime change is the finding — CO/provision by year:**

| | provision | charge-offs | CO/prov |
|---|---:|---:|---:|
| FY2023 | $781.1M | $210.7M | 0.3× *building* |
| FY2024 | $1,101.6M | $874.5M | 0.8× |
| FY2025 | $180.3M | $436.1M | 2.4× *draining* |
| **2026 H1 ×2** | **$31.8M** | **$464.8M** | **🔴 14.6×** |

**Provisioning fell −97.1% from FY2024 while charge-offs held near half a billion a year.** ⇒ **$869M reserve ÷ ~$465M annualised charge-offs ≈ 1.9 years of runway**, against a still-**$2,988M** nonaccrual book.

⚠️ **CAVEATS — carried, not smoothed, and they bind:** `RIAD` is **year-to-date**, so the **×2 is REGINALD's annualisation, not a company figure**. **6 of 11 quarters do not tie** by the identity (adjustments/M&A, −$12.9M to +$64.8M) — **both 2026 quarters tie exactly**, and the ratio uses two directly-reported lines. **There is NO peer base rate: 14.6× is not established as unusual.** ⛔ **Do NOT register 14.6× or 1.9-years as a threshold** — see Q2d.

### Q2c — Is the nonaccrual improvement CURE or CHARGE-OFF? 🔴 **NEW PRIMARY — REGINALD raised it against its own leg**

REGINALD told this desk nonaccruals were past peak and improving (5.49% → 4.88%), then flagged unprompted that the reading is **partly mechanical**: *you do not charge off $232M in six months without the rate falling.* **A rate falling by charge-off is not a rate falling by cure**, and the roll-forward **nets** — it cannot separate them.

⇒ **A "past peak" nonaccrual rate is not evidence of credit repair until the composition is split.** REGINALD explicitly left this with FLG as single-name depth.

- **Resolves by:** decomposing the nonaccrual delta into cures / paydowns / charge-offs / transfers-to-OREO, quarter by quarter. Not in any FLG ledger.
- **Why primary:** it decides whether stage 4 reads ⬇️ improving or 🔴 still-forming — **and it is currently recorded as improving on a figure that may be measuring its own charge-offs.**

### Q2d — Is 14.6× actually unusual? 🟠 **THE ONE THING THAT TURNS A NUMBER INTO A FINDING**

There is **no peer base rate** for CO/provision. Without one, 14.6× is a number, not a signal — a bank finishing a credit cycle can run high ratios legitimately.

- **Resolves by:** the cohort base rate on CO/provision across the 14 banks in REGINALD's matrix, same schedule, same years. **REGINALD holds the instrument and has offered it if FLG asks.**
- **Discipline:** base-rate BEFORE building anything on it (`finding_base_rate_the_threshold_before_building_it` — "don't build it" is a real answer). ⛔ **Nothing about provisioning registers as a gate until Q2d is answered.**

### Q3 — Does the rent-regulation mechanism actually transmit? 🟠

Stages 1–2 have no instrument. Until they do, the desk holds a credit-quality observation, not a causal thesis — and a credit-quality observation is REGINALD's cohort work, not a reason for a separate seat.

- **Resolves by:** instrumenting the RGB rent-guideline series and FLG's multifamily maturity profile, then testing whether nonaccrual formation follows repricing dates.
- **If it does not transmit:** `EXIT_PROTOCOL.md` **K-4** fires, and the scope of this desk goes back to PROME for review. Say so; do not quietly re-scope.

---

## Independence — and why it matters more here than usual

Blueprint §2 requires an Independence column: two vectors on the same root count once. **This desk is a single name, so its channels are unusually dependent.** Concentration (stage 3), nonaccrual (stage 4) and coverage (stage 5) all sit on **one antecedent: the multifamily book.**

**Consequence, and it is a real constraint:** three "independent" channels all reading 🔴 is close to **one** observation read three ways. Do not build a convergence score here that treats them as additive — that is the exact defect REGINALD's v1 matrix died of (eight channels, not one named instrument, a composite nobody could recompute).

---

## What would make this a thesis (the v1.0 bar)

1. ~~Q1 (CRE composition)~~ ✅ refuted 8/20 · ~~Q2b (ACL roll-forward)~~ ✅ answered 8/20 — consumption-by-charge-off, provisioning stopped. **Now Q2c** (cure vs charge-off) **and Q2d** (the CO/provision base rate): the first decides whether stage 4 is improving, the second decides whether 14.6× means anything.
2. Q2 graded at the Q3-2026 Call Report.
3. At least stage 1 or 2 instrumented, so the mechanism is measured and not assumed.
4. Every seed figure re-verified at FFIEC CDR / EDGAR and its `Conf` upgraded from MIRROR-grade.
5. A bidirectional flip that survives contact with the answers to 1–3.

**Until all five: this file stays v0.1 and the desk publishes findings, not a thesis.**

---

## Version log

| Version | Date | Author | Note |
|---|---|---|---|
| v0.1 | 2026-08-20 | DAEDALUS (build) | Skeleton of open questions. No thesis. Seed is MIRROR-grade throughout. |
| *(v1.0)* | *(first live session)* | *FLG* | *Authored only after the v1.0 bar above is met.* |
