# DEEP-RESEARCH PROMPT C2 — score-cascade attribution: does student-loan DQ CAUSE the CC breach?
**From:** CARL (slate T1-1; STUE-proposed; Will-gated) · **Suggested queue:** second of the CARL series · **Parent context:** CARL STATUS student-loan rows (CRL-04 CONFIRMED 10.3%) + `thesis/PREDICTIONS.tsv` CRL-05 + ROADMAP INVESTIGATIONS BACKLOG "Score-cascade-into-CC quantification" (the pre-existing spec, Jun-9)
**Deliver-by:** **~8/8** — before the NY Fed Q2 HHDC (~Aug-15), CRL-05's breach window.

## The question
Of the −62/−69pt average score drop hitting ~7-9M student-loan-delinquent borrowers since repayment resumption, **how much incremental CC/auto 90+ DQ does it CAUSALLY produce, on what lag — and is that increment enough to push CC 90+ (Q1: 13.1%) over the 13.74% GFC breach by Q3?**

## Required sub-answers (4)
1. **The attribution coefficient:** score-band migration → CC 90+ transition probability (base-rate CC DQ at FICO ~580 vs ~680; how much DQ a −69pt shift mechanically adds for a cohort of this size). Sources: FICO research, NY Fed Liberty Street transition matrices, VantageScore migration studies.
2. **The lag structure:** score drop → CC delinquency conversion timing (and the mediating step: issuer line cuts / CLI denials on score triggers — CFPB line-management data).
3. **The arithmetic:** cohort size × coefficient → expected CC 90+ delta in pp; compare against the 0.64pp gap to breach. Explicit: does the cascade ALONE close the gap, or does breach require additional deterioration in the non-SL population?
4. **Adversarial leg — the confound:** SL-delinquent borrowers were disproportionately already-stressed; how much of any observed CC deterioration is shared-income-shock rather than score-mechanism? What natural experiment separates them (e.g., Sweet-cohort tradeline DELETIONS as the reverse shock)?

## Run notes
- **Carve-outs (DEWEY scripts):** NY Fed HHDC quarterly series (transition rates, by-cohort where public); any FRED consumer-credit pulls. The fan-out owns: FICO/Vantage research discovery, academic cascade literature, adversarial verify.
- **Engine sizing:** broad literature + data reconciliation → full fan-out justified.
- **Completeness-critic:** 4 sub-answers.
- **On-return chain:** → WALTER routing; consumers = **CARL** (CRL-05 pre-positioning ahead of ~Aug-15 — this decides breach-with-mechanism vs coincidence) + STUE (cascade thread) + REGINALD (card-issuer read-through).
