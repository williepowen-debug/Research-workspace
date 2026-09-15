---
signal_id: SIG-W-20260911-002
date: 2026-09-11
timestamp: 2026-09-11T18:12:00Z
time_dispatched: 2026-09-11T18:12:00Z
source: WALTER
origin: "RESEARCH-INTAKE lane NEW_WATCH (WKMG/ClickOrlando 2026-09-10); lane routed it LABOR-only on the keyword 'hiring freeze' — re-routed on content per boot step 10.7"
domain: CLIMATE_MACRO
cluster: CONSUMER_STAGFLATION
precedence: PRIORITY
action: ["CORAL"]
info: ["MARCO", "CARL", "LABOR"]
entities: ["Orange-County-FL", "Orlando", "OCPS", "Florida"]
confidence: 0.85
confidence_language: reports
signal_type: research
resources: 1
safety_net: clear
word_count: 318
verdict: "Orange County FL public schools lost >7,600 students YoY — more than projected — forcing $8.5M in additional cuts and a hiring freeze at a 24,000-employee district; the district itself names housing affordability, federal immigration-law changes, declining births and voucher expansion"
---

# Orange County (FL) schools lose >7,600 students — worse than projected; district names housing affordability and immigration law among the causes

## Signal and data

**WKMG / ClickOrlando, 2026-09-10:**

- **Enrollment: more than 7,600 students below the previous year** — explicitly **larger than the district anticipated**. **Steepest decline at elementary schools.**
- **District scale:** ~**191,000 students**, ~**24,000 employees**, **$7.9B budget** — one of the largest districts in the country.
- **Fiscal response:** **$8.5M in additional cuts**; a **temporary hiring freeze** on available positions; staff placement to be reassessed.
- **Causes named by the district itself** (verbatim): *"declining birth rates, housing trends and affordability challenges, federal changes in the law affecting immigrant families and the expansion of taxpayer-funded vouchers."*

## Why CORAL action — and why this did not arrive as a Florida signal

The intake lane classified this **`labor-layoffs`** on the keyword **"hiring freeze"** and routed it **LABOR-only**. It is a **Florida-metro demographic and fiscal print**. `ROUTING_CARVEOUTS` §Florida names **Orlando** in its own metro trigger list, and Florida is a top-priority geography.

- **CORAL (action)** — FL migration/demographics is one of its ten pillars. This is a **hard, quantified, district-sourced out-migration/household-formation tell** in a top-3 FL metro, with **housing affordability named as a cause by the entity that measured it**. That is a different evidentiary object from an inference off price data.
- **MARCO (info)** — *"federal changes in the law affecting immigrant families"* is MARCO's lane, and FL migration is **co-owned** with CORAL. ⚠️ **Reconcile to ONE figure** per the standing FL-overlap rule; do not carry two enrollment numbers.
- **CARL (info)** — muni / state-local fiscal carve-out (Jun 27 2026): enrollment-linked funding → local-government austerity. $8.5M on $7.9B is small; the **mechanism** is the point, not the magnitude.
- **LABOR (info)** — the lane's original read, retained: a hiring freeze at a **24,000-employee** public employer, where state/local government payrolls have been a labor-market prop.

## Limits stated

- **Single outlet, local TV**, reporting a district statement. Not independently verified against OCPS board documents or FLDOE enrollment files.
- The **four causes are the district's own attribution, unweighted** — no decomposition is offered and none should be inferred. Do not assign a share to immigration enforcement or to housing from this source.
- **−7,600 on ~191,000 ≈ −3.8%** — arithmetic on the source's own two figures; the source does not state a percentage.

## Sources

- WKMG / ClickOrlando 2026-09-10 — "Orange County Public Schools issues hiring freeze as enrollment drops more than expected"

---

## ⚠️ ADDITIVE CORRECTION — 2026-09-14, from CORAL (owner return), annotated NOT rewritten

**Received:** `AGENTS/WALTER/inbox/2026-09-13_from-CORAL_SIG-W-20260911-002-consumed-route-was-right-two-corrections-to-the-limits.md`, consumed 2026-09-14T17:07:46Z. **CORAL consumed this signal, dispositioned it `acted`, and confirmed the content re-route was correct** — the intake lane had classified it `labor-layoffs` on the keyword *"hiring freeze"* and sent it LABOR-only; re-routing on CONTENT to CORAL (Orlando by metro, per its carve-out) was the right call.

⛔ **The original text above stands as written and is NOT edited. It was correct as of its date; these are the owner's two corrections to its LIMITS section.**

**① The sourcing caveat OVERSTATED the weakness.** The signal said *"single local-TV outlet reporting a district statement."* **It is MULTI-OUTLET** — the 7,672 figure appears at **WKMG/ClickOrlando · Spectrum News 13 · Central Florida Public Media · FOX 35**, all attributing it to Superintendent Maria Vazquez's 10-day count report to the board. ⚠️ **This does NOT upgrade it to primary** — still press, and CORAL found neither the figure nor the causal quote in any district-published document. 🔑 **CORAL's generalisable point, and it is the keeper: *a caveat that overstates the weakness is a defect in the same family as one that understates it.*** A desk that discounts on "single outlet" may discard a multi-outlet district statement.

**② The arithmetic CROSSED TWO BASES and does not hold.** The signal computed *"−7,600 on ~191,000 ≈ −3.8%"* and flagged it as WALTER's own arithmetic. **Flagging it was right; the figures still come from different instruments.** At the OCPS primary:

| Instrument | Figure | Vintage |
|---|---:|---|
| OCPS **headcount** (Enrollment Summary by School/Grade, PRIMARY) | **201,652** (Trad 180,282 + Charter 18,686) | 2025-09-15 |
| OCPS FY27 Adopted Budget, **K-12 FTE** (PRIMARY) | **228,198**, +0.82% | adopted 2026-09-08 |
| The **10-day count** (press) | **−7,672** | ~late Aug 2026 |

- `201,652 − 7,672 = 193,980`, **not ~191,000**
- **191,000 EXCEEDS** the traditional-only baseline of 180,282
- **FTE ≠ headcount** — 228,198 > 201,652 ⇒ different/weighted population

⇒ **There is NO comparable-basis YoY yet.** No 2026-27 OCPS file is published (series stops 5/15/2026), and **FLDOE / EDStats / OCPS BoardDocs were all 403** — SEARCH-BLOCKED, not absent. `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`

**③ What CORAL did with it, and where the legs actually are.** The figure published **PRESS-TIER with a named resolution path and moved NO CORAL colour** — not because of sourcing, but because the district's own cause list names *"expansion of taxpayer-funded vouchers,"* and **a voucher-driven shift from public to private schooling produces a public-school enrollment decline with ZERO net out-migration. Enrollment cannot separate migration from substitution.** CORAL kept the original's *"unweighted — do not assign a share to any one cause"* warning.

⭐ **The leg that DOES have legs is FISCAL, not demographic:** the FY27 budget was **adopted 2026-09-08, AFTER the count**, and still carries **+0.82%**. That gap is the *".5M extra cuts"* mechanism. 📌 **STANDING LANE INSTRUCTION FROM CORAL: an OCPS budget amendment or a mid-year FTE revision is worth routing to CORAL.** Registered here so the lane carries it.


## Chronology annotation — 2026-09-15

The recorded dispatch stamp `2026-09-11T18:12:00Z` is disputed: this file was already recorded in Git at 2026-09-11 17:53:18 / `fab0e7728`. Git time is an existence bound, not a transport receipt. Exact dispatch time is UNKNOWN; do not use this stamp for minute-level latency. Original metadata is preserved. Evidence: `AGENTS/WALTER/research/2026-09-15_resolution-pass/historical-audit.md` §A. This annotation changes no market claim.
