# DEEP-RESEARCH PROMPT C1 — provisioning-vs-reported-DQ divergence: which way does it resolve?
**From:** CARL (slate T1-4; Will-gated — run on Will's go) · **Suggested queue position:** FIRST of the CARL series (hard deadline) · **Parent context:** `AGENTS/CARL/domain/sources/2026-07-10_cross-domain-synthesis_subagent-sweeps.md` §Pattern-2 (masking confirmed in 4 domains) + KB-CARL-325
**Deliver-by:** **~7/20 (hard)** — the payoff is the bank Q2 ACL read Jul-21-24 (CRL-24's NCO↑×ACL↓ tell) and Dave Q2 (~Aug, VX-GIG-3.08 band re-cut).

## The question
Across historical consumer-lender episodes where **provision-for-credit-losses rose sharply while reported delinquency IMPROVED**, which way did the divergence resolve — (a) provision reverts (timing/conservatism artifact) or (b) reported DQ catches up (provisions were the early truth) — and on what lag?

## Required sub-answers (4)
1. **Episode catalog** (2015-2024, consumer/fintech/subprime lenders): every identifiable provision-up/DQ-down quarter-pair; resolution direction + lag per episode. Include CECL-adoption (2020) distortions as a labeled confounder, not an excuse.
2. **Filter-type split:** does resolution direction differ when the DQ improvement is *survivorship-driven* (lender tightening out worst borrowers — the Dave case: Q1 28DPD 1.69% record low, provision +151% to $26.6M) vs *composition-driven* (mix-shift — the ALLY/COF case) vs *off-book* (the BNPL case, Affirm allowance 6.0% vs 30+ DPD 2.8% flat)?
3. **The Dave-specific test:** management attributes the Q1 spike to quarter-end-day-of-week timing (~$5M Tuesday watermark) and pre-guides Q2 won't repeat. Base rate for "management timing explanation at the first provision spike" being right vs being the first tell? Adversarial lane: try to CONFIRM the timing story, not refute it — CARL's bias runs bearish here.
4. **Threshold implication:** given 1-3, what provision-YoY band separates noise from signal? (CARL's provisional bands: G <+50% / Y +50-100% / O +100-200% / R >+200% or 2 consec >+100% — validate or re-cut.)

## Run notes
- **Carve-outs (DEWEY scripts, concurrent):** the Dave 10-Q/8-K provision rollforward series (EDGAR); FDIC/Fed aggregate charge-off + provision series (FRED/FDIC API); Affirm/ALLY/COF provision-vs-DQ quarterly pairs (EDGAR). Guardrail per protocol: prioritize Dave + ALLY first, return partials with explicit gaps.
- **Engine sizing:** multi-episode-historical → full fan-out earns it (episode discovery + literature + adversarial verify).
- **Completeness-critic:** 4 required sub-answers; flag any unreachable explicitly.
- **On-return chain:** report → WALTER routing; consumers = **CARL** (Q2 bank-earnings read + GIG VX-GIG-3.08 band re-cut) + REGINALD (ACL-release read on regionals). CARL will backfill the INDEX impact note after the Jul-21-24 prints.
