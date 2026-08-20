# FLG — THESIS

**Version: v0.1 — SKELETON, NOT A THESIS** · **Authored: 2026-08-20** (DAEDALUS, at build) · **Owner from first live session: FLG**

> ⚠️ **This document does not yet contain a thesis, and it must not be cited as one.** It is the structured set of **open questions** the desk was built to answer, plus the seed evidence bearing on each. A thesis-of-record (v1.0) is authored by FLG at its first live session, **after** the seed is re-verified at primaries and the construct-validity question below is answered.
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
| 3 | **CRE concentration** | Multifamily + construction + non-owner-occ NFNR / total risk-based capital vs the SR 07-1 300% line | **REPORTED 327.5%, MIRROR-grade** (KB-FLG-002). ⚠️ Contested by the construct-validity question below |
| 4 | **Nonaccrual formation** | Constrained borrowers stop performing | **REPORTED 4.88%, cohort-worst, MIRROR-grade** (KB-FLG-003) |
| 5 | **Reserve adequacy** | ACL must cover recognised nonaccruals | **REPORTED 29% coverage, cohort-thinnest, MIRROR-grade** (KB-FLG-004) |
| 6 | **Capital** | Losses exceed reserves → capital event | **NOT REACHED. No evidence at build.** Do not assume stage 6 from stages 3–5 |

**Read the state column honestly:** stages 1 and 2 — *the causal front end, and the reason this is a separate desk* — are **entirely un-instrumented**. Stages 3–5 are inherited numbers. The desk currently owns a conclusion without the mechanism that produces it.

---

## The three open questions (in priority order)

### Q1 — Is the concentration ratio measuring risk, or measuring a shrinking denominator? 🔴 **BLOCKING**

CRE concentration = CRE / total risk-based capital. FLG's book contracted **−28.8% in loans and −21.1% in assets** over eleven quarters (KB-FLG-005). If the easier-to-exit assets ran off first and multifamily is the stickiest leg, **the ratio rises while absolute CRE risk falls.**

- **Resolves by:** pulling the CRE composition (construction / multifamily / non-owner-occ NFNR, as dollar levels) and total risk-based capital across the same 12 quarters, and reading whether the numerator moved.
- **Blocks:** every concentration threshold. Nothing registers until this is answered.
- **Status:** routed to REGINALD 2026-08-20 as a question about **its** instrument. **Not a refutation** — REGINALD's v2.0 validated its channel-1 arithmetic to −9.4pp against a disclosed figure, which is better discipline than the question presumes.
- *(PAT-090 inverted; `finding_normalization_choice_picks_opposite_winners` — where the disagreement between two normalizations IS the finding.)*

### Q2 — Has the deleveraging already bottomed? 🔴 **LIVE, one print from resolution**

Total loans QoQ, eleven quarters: `−0.1, −2.9, −1.1, −10.9, −5.8, −3.0, −4.0, −1.9, −3.5, −0.6, **+0.9**`.

**Q2-2026 is the first positive quarter in the series**, and the prior four decelerate monotonically toward zero (KB-FLG-014, first-hand recomputation — all eleven cells reproduce against `total_loans_k`).

- **Resolves by:** the Q3-2026 Call Report, ~2026-11-14. A second positive quarter fires `EXIT_PROTOCOL.md` **K-1 — the thesis-kill.**
- **This is the desk's most important near-term fact and it points against the bear case.** It was found at build, on the same day the cohort ranked FLG worst.

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

1. Q1 answered with the CRE composition series.
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
