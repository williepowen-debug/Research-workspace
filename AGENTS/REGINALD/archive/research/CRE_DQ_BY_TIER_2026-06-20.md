# CRE-DQ-by-Tier Drill — Is the OZK-sized tier creeping on the CRE channel?

**Date:** 2026-06-20 | **Trigger:** SIG-W-20260618-009 (Trepp Q1 Call Reports — megabanks $100B+ CRE-DQ fell 1.9%→1.5% resolving office; smaller regionals $16-40B ticked UP) | **Resolves:** the 6/19 open question — does the OZK-sized tier have a CRE-specific delinquency creep that my 6/8 NCO-by-name cut missed? | **Method:** 3 parallel primary pulls + adversarial verify (workflow `wf_4d7841e8-c1d`)

---

## Pre-registered classification rule (fixed BEFORE data)

- **Primary metric:** CRE/construction *delinquency* direction QoQ (Q4'25→Q1'26) — past-due 30-89 + 90+ + nonaccrual, OR disclosed CRE criticized/classified. **NOT** total-loan NCO (the lagging metric the 6/8 decomp already cleared).
- **In-tier watchlist trio ($16-40B):** OZK (~$42B), BKU (~$35B), SBCF (~$21B). Reference: EGBN (~$11B, below-tier, max-CRE), middle ($60-90B: WAL/SSB/VLY/ZION), megabank ($100B+: CFG/MTB).
- **Per-bank class:** CREEP / FLAT / RESOLVING.
- **Verdict buckets:** (a) **TIER-CREEP CONFIRMED** — ≥2 of 3 in-tier CREEP while megabank RESOLVES; (b) **OZK-IDIOSYNCRATIC** — only OZK creeps, peers flat/resolving; (c) **MIXED**.

---

## Verdict: SEVERITY-GRADED tier-wide CRE-DQ leading-creep (direction tier-broad, severity concentration-graded); WAL unchanged

After pulling the **leading bucket (30-89 past-due) for all three in-tier names** (6/20 PM, closing the adversary's hole on both BKU and SBCF rather than waiting for Q2), the pre-registered binary (tier-creep vs OZK-idiosyncratic) proves too coarse. **Every in-tier watchlist name's CRE leading bucket ticked up** — OZK CREEP (material) / BKU MIXED (small) / SBCF MIXED (small) — plus below-tier EGBN. The honest read is a **severity-graded tier-wide leading-creep:**

- **Direction: tier-BROAD.** All 3 in-tier names (OZK/BKU/SBCF) + EGBN show **CRE-*specific*** leading-bucket creep (at SBCF, total past-due *fell* while CRE past-due rose — pointedly CRE). → **SIG-009 / Trepp's "down-tier CRE-DQ creeping" is directionally CORROBORATED — more than the first-pass read**, which only pulled the peers' *lagging* buckets and read them clean (the methodology miss the adversary caught).
- **Severity: steeply CONCENTRATION-graded.** Material + named-loan + reservoir-confirmed at the high-CRE names (OZK 1.41% past-due in 5 named loans; EGBN nonaccrual +23-61%, NPA 1.04→1.31%, coverage 149→114%); **small + lumpy + collateral-backed + ZERO loss-content** at the diversified names (BKU CRE 30-89 at 0.34% of book; SBCF 0.18%; both criticized-flat, NCO benign 11bps).

So SIG-009's "tier creeping" is **directionally confirmed**, but the **loss-relevant magnitude is concentrated** at the high-CRE names. Megabank tier **RESOLVING confirmed** (Trepp's 1.9→1.5% corroborated at issuer level). **Confidence ~0.6** on the severity-graded framing. **WAL is separately middle-tier idiosyncratic-office → UNCHANGED, no reweight** — this whole drill is the $16-40B down-tier; WAL's office creep is single-name (the $99M life-sci walk).

**This RECONCILES rather than contradicts the 6/8 NCO finding:** NCO (lagging) is benign cohort-wide **and** CRE-DQ (leading) creeps at the CRE-concentrated names — the same reservoir pipeline at different stages. The 6/8 "cohort NCO decelerating" and SIG-009 "CRE-DQ ticking up" are both true; they measure different buckets.

---

## Per-bank evidence (decisive figures primary-verified)

### In-tier ($16-40B)

**OZK ~$42B — CREEP, CRE-specific ✅ (the canary).** Total loans past due **doubled** $207M (0.64%) → $465M (1.41%) QoQ; **88% is 5 RESG/CRE loans** ($409.5M): *"Five RESG loans accounted for the vast majority of our past due and nonperforming loans… $409.5 million, or 124 of the total 141 bps of loans past due"* (Q1-2026 Management Comments, p.22). Roster all CRE: Boston Office $156.4M, Boston Life-Sci $169.3M, Baltimore Land $40M, Seattle Pioneer Sq Office $25.9M, Wauwatosa Hotel $17.9M. Classified+criticized $984M→$1,215M (+23.5%). NCO benign **0.57%** (lagging, in-line w/ guide). NPL fell $341M→$297M **only** because 2 credits foreclosed (Chicago Life-Sci, Santa Monica Office) — NPA actually **rose** $402M→$451M. Consumer clean (Indirect RV/Marine 30+DPD 0.28%). **Reservoir/migration signature confirmed.**
> **⚠️ Data-sourcing find (durable):** Bank OZK (CIK 0001569650) files **NO SEC 10-Q/10-K/8-K** — deregistered SEC periodic reporting after its 2017 holding-co merger (verified 3 ways: submissions API = only third-party 13F/13G; browse-edgar type=10-Q = zero; full-text 10-Q hits all belong to other filers naming OZK as lender). Primary CRE-DQ = **FDIC Call Report (FFIEC RC-N, due ~May 1-10)** + earnings release + **Financial Supplement + Management Comments** (archived: `AGENTS/OZK/raw/Q1_2026_mgmt_comments.pdf` Fig 23/24, `…financial_supplement.pdf`). No formal RC-N past-due-by-category table in these docs — CRE attribution rests on the unambiguous Fig 23/24 RESG narrative (88% named RESG/CRE).

**BKU ~$35B — MIXED (lagging RESOLVING, leading TICKING UP) — softened from RESOLVING after the 6/20 PM past-due test.** *Lagging buckets resolving:* every CRE nonaccrual bucket flat-to-down — NOO $67.3M→$66.9M, **construction CRE $29.7M→$0**, OO $23.7M→$20.2M; total nonaccrual $372.6M→$274.7M; criticized/classified **−12.2%** ($1,198.5M→$1,052.3M); NPA 1.08%→0.79%. **BUT the LEADING bucket (the adversary's hole, tested 6/20 PM from the same 10-Q age-analysis table) is building:** CRE **30-89 past-due +50%** ($15.6M→$23.4M; the freshest 30-59 jumped $0.75M→$23.4M), 90+ +16% ($26.4M→$30.6M), **total CRE past-due +29%** ($42.0M→$54.0M, 0.62%→0.78% of CRE book) — *while* nonaccrual + criticized fell. The reservoir-lag divergence (leading up / lagging down) IS present at BKU, same shape as OZK but **~30× smaller** (0.34% of book vs OZK's 1.41% in 5 named loans) and the 30-59 bucket is lumpy/quarter-end-timing-prone (60-89 emptied to $0 — non-monotonic). **Weak trigger: softens BKU from a clean counter-vote to a watch; does NOT promote to "tier-wide creep" (magnitude + lumpiness).** (10-Q accession 0001504008-26-000043, age-analysis table self-verified 6/20 PM.)

**SBCF ~$21B — MIXED / CRE-specific early-creep (revised from FLAT after the 6/20 PM past-due test).** *Lagging context (drill):* criticized/classified **exactly flat 2.82%**; NCO 11bps; two collateral-backed commercial credits, "no credit loss" expected. **BUT the CRE-specific leading bucket is building** (6/20 PM, age-analysis table summed across Portfolio+Acquired+PCD pools): CRE+construction **30-89 accruing past-due +132%** ($5.38M→$12.48M) — the seasoned **60-89 component jumped $0.5M→$7.8M** (less timing-noise than 30-59). It's **CRE-specific, not broad**: *total* accruing past-due FELL ($32.9M→$28.2M — C&I −$4.6M, resi −$2.1M) while CRE past-due rose. CRE+constr nonaccrual also +21% ($46.1M→$55.8M). **BUT tiny absolute level** — CRE 30-89 is 0.08%→0.18% of the ~$6.95B CRE book; no loss content; post-Villages acquired pools add migration lumpiness. (10-Q 0001628280-26-031220, age-analysis self-verified 6/20 PM.)

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

At the adversarial stage these didn't overturn the (then-current) concentration-cohort read and capped confidence at ~0.55. **They then drove the leading-bucket test (next section), which broadened the verdict to severity-graded tier-wide leading-creep (conf 0.6)** — i.e. the adversary's "criticized migration / leading bucket not pulled" critique proved right when BKU + SBCF 30-89 were actually pulled.

---

## 🎯 Defined falsifier — TESTED 6/20 PM on BOTH diversified peers (Q1 data) → broadened the read

The adversary's hole: peers judged on *lagging* buckets only. Closed it the same session (Will-directed) by pulling the **30-89 past-due leading bucket from both BKU's and SBCF's Q1 10-Q age-analysis tables** — Q1 already carries it, no need to wait for Q2.
- **BKU:** CRE 30-89 **+50%** ($15.6M→$23.4M) *while nonaccrual fell* — clean reservoir-lag divergence. Lumpy (60-89 emptied to $0).
- **SBCF:** CRE 30-89 **+132%** ($5.4M→$12.5M, incl. a seasoned 60-89 build $0.5→$7.8M) AND nonaccrual +21% — and CRE-*specific* (total past-due FELL, CRE rose).

**Both diversified in-tier peers show a CRE leading-bucket tick** → the down-tier creep is **tier-broad in direction**, not confined to the 2 high-CRE names. That **lifts** SIG-009 corroboration (vs the first-pass "peers clean") — but both peers sit at **trivial absolute levels** (0.18-0.34% of CRE book, criticized-flat, zero NCO), so severity stays concentration-graded. Net: verdict moved "concentration-cohort, peers clean" → **"severity-graded tier-wide leading-creep"**; confidence 0.5→0.6; WAL / no-reweight unchanged.

**Residual Q2 watch (~Jul 30):** (1) do the BKU + SBCF leading ticks BUILD (real down-tier creep) or REVERT (quarter-end / acquired-pool lumpiness)? (2) does the OZK/EGBN named-loan creep CONVERT to realized NCO + specific reserves? (3) SSB/AMTB criticized→NCO (SIG-008 synchronization bar). (4) OZK FFIEC RC-N for a formal past-due-by-category confirmation of the 88%-CRE attribution.

---

## Thesis effects

- **WAL — UNCHANGED.** CRE creep is idiosyncratic-office (primary-confirmed), not a tier/concentration effect. The 6/8 "WAL idiosyncratic" read survives the CRE-DQ channel test. EV $68.93 / PT $50-68 / Bear-medium 25 / REG-24 70% / REG-25 75% / positions all **UNCHANGED**.
- **SIG-009 — re-classified.** Trepp tier signal is REAL but the mechanism is **CRE-concentration sorting, not asset size**; for our watchlist it manifests at OZK + EGBN (concentrated), not BKU/SBCF (diversified). Not a WAL reweight.
- **OZK — reservoir corroborated** (cross-agent flag to OZK; OZK-domain, not a REGINALD reweight): CRE-DQ creep primary-confirmed CRE-led; EGBN independently shows the same concentration pattern.
- **EGBN — watchlist refresh.** Fresh CRE nonaccrual creep (IPRE +23%, constr +61%, NPA 1.04→1.31%, coverage 149→114%) — update Matrix/STATUS EGBN row.
- **6/19 open question — RESOLVED-RECONCILED.** Leading-DQ-vs-lagging-NCO by CRE-concentration; not a contradiction. No reweight.

*Companion: `research/COHORT_NCO_DECOMP_2026-06-08.md` (the NCO-by-name cut this reconciles with).*
