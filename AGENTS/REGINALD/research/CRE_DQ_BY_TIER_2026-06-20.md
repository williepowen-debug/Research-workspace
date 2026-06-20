# CRE-DQ-by-Tier Drill — Is the OZK-sized tier creeping on the CRE channel?

**Date:** 2026-06-20 | **Trigger:** SIG-W-20260618-009 (Trepp Q1 Call Reports — megabanks $100B+ CRE-DQ fell 1.9%→1.5% resolving office; smaller regionals $16-40B ticked UP) | **Resolves:** the 6/19 open question — does the OZK-sized tier have a CRE-specific delinquency creep that my 6/8 NCO-by-name cut missed? | **Method:** 3 parallel primary pulls + adversarial verify (workflow `wf_4d7841e8-c1d`)

---

## Pre-registered classification rule (fixed BEFORE data)

- **Primary metric:** CRE/construction *delinquency* direction QoQ (Q4'25→Q1'26) — past-due 30-89 + 90+ + nonaccrual, OR disclosed CRE criticized/classified. **NOT** total-loan NCO (the lagging metric the 6/8 decomp already cleared).
- **In-tier watchlist trio ($16-40B):** OZK (~$42B), BKU (~$35B), SBCF (~$21B). Reference: EGBN (~$11B, below-tier, max-CRE), middle ($60-90B: WAL/SSB/VLY/ZION), megabank ($100B+: CFG/MTB).
- **Per-bank class:** CREEP / FLAT / RESOLVING.
- **Verdict buckets:** (a) **TIER-CREEP CONFIRMED** — ≥2 of 3 in-tier CREEP while megabank RESOLVES; (b) **OZK-IDIOSYNCRATIC** — only OZK creeps, peers flat/resolving; (c) **MIXED**.

---

## Verdict: asset-size tier-creep NOT confirmed → refines to a **CRE-CONCENTRATION cohort**

In-tier trio: **OZK CREEP / BKU RESOLVING / SBCF FLAT** = 1 of 3 CREEP → fails the ≥2 bar → mechanically **(b) OZK-IDIOSYNCRATIC** by the asset-size test.

But the signal sorts cleanly by **CRE-concentration, not asset size**: the two highest-CRE names (OZK RESG-heavy; EGBN 547% CRE / DC-office) **both creep**; the diversified peers (BKU, SBCF) are flat-to-resolving. So the precise read is a **concentration-cohort creep**, not a uniform $16-40B tier wave. Megabank tier **RESOLVING confirmed** (Trepp's 1.9→1.5% corroborated at issuer level). **Confidence ~0.55**, conditional on the Q2 falsifier below.

**This RECONCILES rather than contradicts the 6/8 NCO finding:** NCO (lagging) is benign cohort-wide **and** CRE-DQ (leading) creeps at the CRE-concentrated names — the same reservoir pipeline at different stages. The 6/8 "cohort NCO decelerating" and SIG-009 "CRE-DQ ticking up" are both true; they measure different buckets.

---

## Per-bank evidence (decisive figures primary-verified)

### In-tier ($16-40B)

**OZK ~$42B — CREEP, CRE-specific ✅ (the canary).** Total loans past due **doubled** $207M (0.64%) → $465M (1.41%) QoQ; **88% is 5 RESG/CRE loans** ($409.5M): *"Five RESG loans accounted for the vast majority of our past due and nonperforming loans… $409.5 million, or 124 of the total 141 bps of loans past due"* (Q1-2026 Management Comments, p.22). Roster all CRE: Boston Office $156.4M, Boston Life-Sci $169.3M, Baltimore Land $40M, Seattle Pioneer Sq Office $25.9M, Wauwatosa Hotel $17.9M. Classified+criticized $984M→$1,215M (+23.5%). NCO benign **0.57%** (lagging, in-line w/ guide). NPL fell $341M→$297M **only** because 2 credits foreclosed (Chicago Life-Sci, Santa Monica Office) — NPA actually **rose** $402M→$451M. Consumer clean (Indirect RV/Marine 30+DPD 0.28%). **Reservoir/migration signature confirmed.**
> **⚠️ Data-sourcing find (durable):** Bank OZK (CIK 0001569650) files **NO SEC 10-Q/10-K/8-K** — deregistered SEC periodic reporting after its 2017 holding-co merger (verified 3 ways: submissions API = only third-party 13F/13G; browse-edgar type=10-Q = zero; full-text 10-Q hits all belong to other filers naming OZK as lender). Primary CRE-DQ = **FDIC Call Report (FFIEC RC-N, due ~May 1-10)** + earnings release + **Financial Supplement + Management Comments** (archived: `AGENTS/OZK/raw/Q1_2026_mgmt_comments.pdf` Fig 23/24, `…financial_supplement.pdf`). No formal RC-N past-due-by-category table in these docs — CRE attribution rests on the unambiguous Fig 23/24 RESG narrative (88% named RESG/CRE).

**BKU ~$35B — RESOLVING, CRE-specific ✅.** Every CRE nonaccrual bucket flat-to-down: NOO $67.3M→$66.9M, **construction CRE $29.7M→$0**, OO $23.7M→$20.2M; total nonaccrual $372.6M→$274.7M; criticized/classified **−12.2%** ($1,198.5M→$1,052.3M); NPA 1.08%→0.79%. (10-Q accession 0001504008-26-000043, self-verified.)

**SBCF ~$21B — FLAT, cre_specific ✗ (broad).** Criticized/classified **exactly flat 2.82% = 2.82%** sequentially (verbatim). Nonaccrual rose +32% ($72.0M→$95.0M) but **broad**: Residential +$9.2M and C&I +$4.5M rose as much as CRE-NOO +$8.2M; **construction CRE FELL**; two collateral-backed commercial credits, "no credit loss" expected; NCO 11bps. (8-K 0001628280-26-027918 + 10-Q 0001628280-26-031220, self-verified.)

### Below-tier reference

**EGBN ~$11B (max-CRE, DC-office) — CREEP, CRE-specific ✅ (independent confirmation).** Income-producing CRE nonaccrual **+23%** ($62.5M→$76.7M); construction-CRE&resi nonaccrual **+61%** ($17.4M→$28.0M); total NPLs $106.9M→$128.8M (+20%); NPA 1.04%→1.31%. Driver verbatim: *"the migration of one previously substandard-rated CRE office relationship to nonaccrual status during the quarter."* Coverage ACL/NPLs **149%→114%**. NUANCE: shallower criticized bucket FELL (IPRE crit $559.7M→$457.1M) — disposition working AND the worst office credit migrating PAST criticized DOWN into nonaccrual (pipeline advancing, not clean resolution). (10-Q 0001050441-26-000066, self-verified.)

### Megabank ($100B+) — RESOLVING (confirms Trepp 1.9→1.5%)

- **CFG ~$220B — FLAT (resolving on loss + YoY).** CRE NCO rate flat 0.64% QoQ, **down YoY** from 0.77%; total-loan NCO decelerating 5 straight qtrs. **Honest caveat:** CRE *nonaccrual* leading bucket ticked **+10% QoQ** ($618M→$679M) on a shrinking CRE book (−$642M) — resolves on losses + YoY, not on every QoQ metric. (8-K 0000759944-26-000070, self-verified.)
- **MTB ~$210B — RESOLVING.** Total nonaccrual −19% YoY; mgmt narrative explicitly names CRE-nonaccrual decline; CRE NCO 0.34→0.31%. Caveat (from 6/8): aggressive CRE ACL release −31% vs loans −10% into the maturity wall. (8-K 0000036270-26-000025, self-verified.)
- **ZION ~$90B — RESOLVING.** CRE a net recovery (−$1M) Q1'26; total NCO 0.03%. (Verified 6/8, not re-curled.)

### Middle ($60-90B) — MIXED, not broadly stressed

- **WAL ~$83B — CREEP but IDIOSYNCRATIC-OFFICE.** Other CRE-NOO nonaccrual $228M→$263M (+15.4% QoQ); GCO $27.7M "primarily office." Concentrated in the $99M late-April **life-science Class-A office sponsor walk-away** (pass→substandard in one quarter, sponsor election — same mechanic as OZK/IQHQ). **Single-name/sector, NOT a tier or concentration effect** — tagged idiosyncratic so it is not read as middle-tier creep. (10-Q drilled 5/21.)
- **VLY ~$62B — RESOLVING.** CRE non-accrual falling, concentration ratio edged down to ~329% RBC, ACL 1.19→1.18%. *(relayed from prior research, NOT re-curled this session.)*
- **SSB ~$65B — FLAT/benign-migration.** Classified $2.5B (3.6% assets), **88% accrual / 99% current**, rate-shock reclassification, NCO 9bps — a leading-label move, not delinquency. *(relayed, NOT re-curled this session.)*

---

## Adversarial pass (skeptic, conf 0.5 MIXED) — accepted caveats

The skeptic genuinely tried to refute the idiosyncratic read and surfaced holes I'm carrying forward, not suppressing:

1. **🔑 BKU "resolution" is read off LAGGING buckets (non-accrual + criticized) — its 30-89 *past-due* leading line was NOT pulled.** OZK proves past-due leads non-accrual by 1-2 quarters; BKU could be clearing 2024-vintage office while 2026 past-due quietly builds. **This is the defined falsifier.**
2. N=3 in-tier is a stress-selected watchlist sample, not a representative draw from Trepp's full $16-40B universe — can't fully refute a tier aggregate with it.
3. **Basis mismatch:** OZK (Mgmt-Comments narrative, no RC-N) vs peers (10-Q non-accrual) vs Trepp (Call-Report tier aggregate) — three measurement bases compared as if equivalent.
4. Criticized *migration* (SSB rate-shock, AMTB special-mention up, SBCF NPL up) may be the leading creep an NCO-by-name cut structurally can't see; "flat criticized" ≠ no creep.
5. SBCF cre_specific=false is absence-of-read, not evidence-of-absence.

These don't overturn the concentration-cohort read (OZK + EGBN both primary-confirmed CRE-led creep; BKU CRE nonaccrual unambiguously down on every bucket including the leading construction line→$0), but they cap confidence at ~0.55 and define the Q2 test.

---

## 🎯 Defined falsifier (Q2 prints, ~Jul 30+)

**Pull BKU's 30-89 *past-due* (leading) bucket.** If it rises while non-accrual stayed flat → BKU is also in reservoir-lag → read shifts from "concentration-cohort" toward "down-tier CRE-creep." If past-due flat-to-down → genuine resolution, isolates OZK+EGBN as concentration-driven. Also watch: SSB/AMTB criticized→NCO conversion (the SIG-008 synchronization bar), OZK FFIEC RC-N for a formal past-due-by-category confirmation of the 88%-CRE attribution.

---

## Thesis effects

- **WAL — UNCHANGED.** CRE creep is idiosyncratic-office (primary-confirmed), not a tier/concentration effect. The 6/8 "WAL idiosyncratic" read survives the CRE-DQ channel test. EV $68.93 / PT $50-68 / Bear-medium 25 / REG-24 70% / REG-25 75% / positions all **UNCHANGED**.
- **SIG-009 — re-classified.** Trepp tier signal is REAL but the mechanism is **CRE-concentration sorting, not asset size**; for our watchlist it manifests at OZK + EGBN (concentrated), not BKU/SBCF (diversified). Not a WAL reweight.
- **OZK — reservoir corroborated** (cross-agent flag to OZK; OZK-domain, not a REGINALD reweight): CRE-DQ creep primary-confirmed CRE-led; EGBN independently shows the same concentration pattern.
- **EGBN — watchlist refresh.** Fresh CRE nonaccrual creep (IPRE +23%, constr +61%, NPA 1.04→1.31%, coverage 149→114%) — update Matrix/STATUS EGBN row.
- **6/19 open question — RESOLVED-RECONCILED.** Leading-DQ-vs-lagging-NCO by CRE-concentration; not a contradiction. No reweight.

*Companion: `research/COHORT_NCO_DECOMP_2026-06-08.md` (the NCO-by-name cut this reconciles with).*
