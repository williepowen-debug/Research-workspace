# CARL CHANGELOG

Tracks all changes to THESIS.md and PREDICTIONS.tsv. Reverse chronological. Each entry documents what changed, why, and the old view vs new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new mechanism, thesis break, conviction reversal). Minor (Y) = refinement (updated evidence, threshold adjustment, vector upgrade/downgrade).
- PREDICTIONS: changes logged by Pred_ID.

---

## 2026-04-17 (PM) — v2.4.1: PAYMENT HIERARCHY TIMELINE PUSHED (ALLY Q1 COUNTER-EVIDENCE + AUDIT)

### THESIS v2.4 → v2.4.1
**Author:** CARL (post-ALLY Q1 earnings + CARL-performed FY2024/FY2025 10-K reclassification audit)
**Action:** Minor refinement. Convergence unchanged at 58/60. No vector score change. Mechanism-level revision to payment hierarchy pathway timing.

### TRIGGER

Ally Financial Q1 2026 earnings (Apr 17): retail auto NCO 1.97% (-17bps QoQ), 30+ DQ 4.6%, 5th/4th consecutive quarter of YoY improvement respectively. Guidance maintained. Mgmt: "consumer behavior is resilient." Stock up. First real-time test of payment hierarchy cascade claim (prime/near-prime auto = next domino after subprime 60+ DQ breached 6.9% ATR) — headline test result: **CLEAN**, four consecutive quarters improving.

### AUDIT PERFORMED

Pulled ALLY FY2024 10-K (EDGAR acc 0000040729-25-000006, filed 2025-02-19) and FY2025 10-K (acc 0000040729-26-000005, filed 2026-02-25). Ran forensic comparison against REGINALD's regional bank reclassification framework (Layers 1-3: Memo Item 3, NDFI-in-C&I, sub-category reclassification) adapted to auto-lender toolkit (A-G: HFI→HFS, whole-loan sales, FDM/TDR, runoff segmentation, mix shift, reserve release, CLN/securitization routing). File: `domain/sources/ally/RECLASSIFICATION_AUDIT_FY2025.md`.

**Findings — NOT present:** HFI→HFS dumping, TDR re-aging, runoff/legacy segmentation, new line-item taxonomy, NDFI-analog hiding place, dealer/floorplan stress (floorplan shrinking).

**Findings — PRESENT (composition masking, not accounting fraud):**
- Used retail S-tier origination mix: **40% → 37%** (-3pp FY2024 → FY2025)
- Nonprime exposure (FICO<620): **9.7% → 10.1%** (+40bps, +$0.4B to $8.6B)
- ACL: **$3.7B → $3.5B** (-$224M / -6%) = reserve release into mix downgrade (Layer F)
- CLN issuance: **$0.77B → $1.1B** (+43% YoY), reference pools $7B → $10B (Layer G)
- Originations +11% YoY into worsening mix

### MECHANISM REVISION

**Old view (pre-Apr 17 2026):** Payment hierarchy — subprime → near-prime → prime auto — transmission in 1-2 quarters. ALLY Q1 was the first real test; expected to show early signs of near-prime migration (NCO ticking up, DQ stopping improvement).

**New view (v2.4.1):** Headline Ally Q1 is composition-driven, not genuine improvement:
- **Seasoning:** FY2024 higher-FICO originations rolling into 2026 NCO window (lower losses)
- **Mix routing:** Shift from used retail toward new retail (slower loss curve at same FICO)
- **Tail-risk routing:** CLN/securitization expanded +43% YoY, exporting first-loss tail to ABS investors

The FY2025 origination cohort is **like-for-like worse** than FY2024 — deterioration is embedded in the book, not yet in the P&L. The 18-24 month vintage seasoning lag means FY2025 loss window opens **2H 2026 and Q1 2027**.

**Payment hierarchy thesis NOT invalidated — TIMELINE PUSHED.** Near-prime P&L stress window moves from Q1-Q2 2026 to 2H 2026 / Q1 2027.

### CROSS-THESIS IMPLICATIONS

**K-shape within auto credit (new refinement):** Subprime ABS cracking (EART Class E CE breached Apr 16, AMCAR ~2mo, SDART ~7mo) co-exists with near-prime headline-clean = intra-credit K-shape. ABS monoline stress is localized; doesn't migrate up-quality automatically — it migrates via seasoning of the near-prime vintage being originated *now* under looser standards, which plays out with a ~18 month lag.

**Counter-signal containment:** The "Ally Stable 🟢" row in STATUS (Feb 10-D data) is CONFIRMED and EXTENDED, not overturned. But "stable" at headline ≠ "clean" at cohort. STATUS must distinguish the two.

**REGINALD handoff:** Auto-lender reclassification framework (KB-CARL-225) translates their 3-layer bank framework. CLN routing = structural analog of their C&I hiding place. Sent as outbox signal.

### PREDICTION UPDATES

**CRL-05 — CC 90+ DQ breaches 13.74% (GFC peak)**
- **Confidence: 85% → 82%** (mild reduction on headline/cohort distinction)
- **Rationale:** Student loan cascade still adding +0.5-1.0pp pathway, multi-vector cost squeeze intact — these don't require near-prime auto migration to work. But ALLY counter-evidence weakens the "consumer credit generally migrating up-quality" framing at the headline level. Cohort-level deterioration (nonprime share growing) preserves the thesis, just shifts the visibility window later.
- **No change to invalidation criteria.**

**CRL-02 — Subprime Auto 60+ DQ crosses 7.0%** (already CONFIRMED*)
- **Confidence: no change.** Subprime stress is independently confirmed; Ally near-prime data irrelevant to this cohort.

### NEW FRAMEWORK ENTRY

**Auto-lender reclassification methodology** (KB-CARL-225): 7-lever translation of REGINALD regional bank framework. Apply to SYF (Apr 21), COF (Apr 21), AXP (Apr 23). For SYF: no used-car tail, but CLN/mix shift via CareCredit vs Private Label segmentation potentially applicable.

### DANGER WINDOW UPDATE

Added: **Q1 2027** — FY2025 origination cohort full seasoning window. Near-prime auto P&L stress realization if thesis holds. If NCO/DQ deteriorate on unchanged macro at this point, thesis REACTIVATES HARD at the headline level.

---

## 2026-04-17 — v2.4: FORECLOSURE PIPELINE CONVERTING + CREDIT CASCADE EXECUTING

### THESIS v2.3 → v2.4
**Author:** CARL (via Apr 15 data processing — STUE + HOMER sub-agents)
**Action:** Minor refinement. Vector #10 (Foreclosure) upgraded 4→5. Convergence 57/60 → **58/60 CRITICAL**. Two mechanism confirmations added.

### CONVERGENCE MATRIX — Vector #10 Upgrade
| Vector | Change | Reason |
|--------|--------|--------|
| #10 Foreclosure Acceleration | 🔴 4 → 🔴🔴 **5/5** | ATTOM Q1 2026 (rel Apr 16): **Q1 REO completions 14,020 (+45% YoY)**. Previously the 878K 90+/FC pipeline was ACCUMULATING (inflow > outflow). Q1 2026 is first quarter at-scale CONVERSION — cure collapse (-40%) now translating to actual completions. Regime change, not incremental. FL Q1 REO +108% YoY (greatest nationally). Q1 filings 118,727 (+26% YoY). March monthly 45,921 filings (+18% MoM). |

### PREDICTION UPDATES

**CRL-04 — Student Loan 90+ DQ breaches 10%**
- **Confidence: 97% → 98%** (OPEN-NEAR CONFIRMED)
- **Evidence:** FICO Spring 2026 (data Apr 17): SL DQ rate now ~9.8% (up 25% from 7.9% Apr 2025). 6.1M borrowers with SL DQ reported Feb-Apr, avg score drop -69pts (25% saw -100pt+).
- **Counter-signal (minor):** Sweet v. McMahon Apr 15 ruling triggers ~271K tradeline deletions — credit RECOVERY for bounded cohort (~3% of defaulted borrowers). Directionally opposite but magnitude insufficient to move aggregate.
- **Near-term test:** NY Fed Q1 2026 QHDC (~May-Jun).

**CRL-06 — Foreclosures exceed 70K/quarter**
- **Confidence: 70% → 78%**
- **Evidence:** Q1 2026 ATTOM: 82,631 FC starts (already >70K on starts basis), 118,727 filings (+26% YoY), 14,020 REO (+45% YoY). Depending on threshold interpretation, may be CONFIRMED at starts level. Q2 projection likely higher on FL judicial lag.

### NEW MECHANISM / FLOW ENTRY

**FLOW-CARL-12.04 — Foreclosure Pipeline → REO Conversion → Bank Loss Realization (Path C Activation)**
- **Status:** ACTIVATING-RED (new)
- **Pathway:** Borrower 90+ DQ → cure rate collapse → foreclosure filing → legal process 3-12mo → REO completion → actual loss realized → NCO line → earnings hit → bank tightens → consumer denied. Non-bank servicer variant: Ginnie advance drain → warehouse line stress → potential failure (MFS UK template).
- **Why it matters:** Path C (Housing → Banks) previously theoretical, now mechanically active. Q1 bank earnings cluster (Apr 17-28: CFG/PNC/RF/FITB/MTB) = first visibility window for provision build on mortgage/CRE.

### STUDENT LOAN VECTOR CONFIRMATIONS

- **Sweet v. McMahon Apr 15 deadline MISSED** — DOE did not comply. Auto Full Relief triggered for ~170K non-Exhibit C borrowers. Combined with Exhibit C (missed Jan 28 ~170K), total ~271K. Self-executing, no stay. NOT thesis invalidation (court-compelled, bounded cohort).
- **SAVE judicially dead** — 8th Cir Mar 10 reversed + entered final judgment. Dual-elimination (legislative WFTCA Jul 2025 + judicial Mar 2026). Jul 1 transition locked.
- **AFT v. MOHELA in discovery** — Next status conf May 28. Three concurrent class actions active.

### NEW VECTORS (VX)

- **VX-CARL-HSG-05** — Foreclosure Pipeline Quarterly REO Completions (14,020 Q1 2026, RED)
- **VX-CARL-BLDR-01** upgraded to RED (HMI 38 → 34, breaches <40 threshold; new tariff cost shock +$10,900/home)
- **VX-CARL-HSG-01** updated (PMMS 6.37% → 6.30%)
- **VX-CARL-SL-02** updated (SL 90+ DQ ~9.8% per FICO Spring 2026)
- **VX-CARL-6.06** updated (FL Q1 REO +108% YoY, judicial state completion wave)

### KB ENTRIES ADDED

KB-CARL-215 through KB-CARL-221 (7 entries): Sweet v. McMahon ×2, DOE motion context, SAVE judicial death, FICO Spring 2026 cascade, MOHELA discovery, NAHB HMI April, ATTOM Q1 Foreclosures.

### HONEST ASSESSMENT

**Strengthened:** Mechanism confirmations — pipeline conversion (HSG), credit cascade execution (SL), Vector 10 upgrade defensible (not self-inflicted).
**Unchanged:** Market-transmission leg (HY OAS 294bps tight, SPX not in crisis, JPM Q1 benign). Complacency gap persists or widens.
**Counter-signal:** Sweet ruling produces credit RECOVERY for ~271K — directionally opposite the cascade. Small but directionally notable.

### TRIGGER FOR NEXT VERSION BUMP

- Q1 bank earnings cluster (Apr 17-28) confirming Path C provision build → v2.5 with full Path C activation upgrade.
- OR SYF Q1 Apr 21 breaching >6% NCO → credit cascade confirmed at issuer level.
- Reversal criterion: bank earnings downplay stress AND SYF NCO <5.0% → thesis mechanism questioned.

---

## 2026-04-14 — v2.3: FED LOCK MECHANISM + SUBPRIME AUTO CURE COLLAPSE CONFIRMED

### THESIS v2.2 → v2.3
**Author:** CARL (via WALTER inbox processing + ABS drill-down)
**Action:** Major thesis refinement. Vector #12 Stagflation Trap added. Convergence 51/55 → **57/60 CRITICAL**.

### CONVERGENCE MATRIX — Vector #12 Added
| Vector | Change | Reason |
|--------|--------|--------|
| #12 Stagflation Trap / Fed Locked | **NEW** 🔴🔴 5/5 | WALTER CPI/UMich signal integrated (Apr 10 data): UMich Apr preliminary 47.6 — RECORD LOW (biggest MoM drop in series). 1Y inflation exp 4.8% (+100bps), 5-10Y exp UN-ANCHORING at 3.4% (Fed red line breached). CPI Mar +3.28% YoY headline, +2.61% core. Mechanism: Fed cuts now validate un-anchoring → inflation-negative, not stimulus. Cannot cut (expectations), cannot hike (sentiment ATL). 1970s Volcker analog. RED Stagflation Spiral upgraded. HENRY "Fed cuts pushed H2 2027" reinforced. |

### KEY EMPIRICAL CONFIRMATIONS (Apr 14)
- **Subprime auto cure collapse confirmed industry-wide.** SDART 2024-1 (30+ DQ -43bps, CNL +26bps), EART 2024-2 (-177bps/+52bps deep subprime), AMCAR 2024-1 (-175bps/+24bps). HAROT 2024-2 prime control stable. Pattern: DQ bucket draining to charge-offs, not cures. EART already at projected terminal CNL (13.06%). KB-CARL-207, KB-CARL-210.
- **Discover ABS structure dissolved.** DCMT filed Form 15-12G Dec 19 2025 post-CapOne merger. DCENT in defeasance. Removed from abs_monitor. CC data now rolls into COMET. KB-CARL-208, KB-CARL-209.

### PREDICTIONS
No new predictions added — existing CRL-01 through CRL-17 remain appropriate. Notes updated on CRL-05 (cascade confirmation), CRL-08 (FL crossed $4). Future drill-down (#2 CNL trigger proximity) may generate CRL-18.

### KB Added (Apr 14: 7 entries)
KB-CARL-204 (UMich record low), KB-CARL-205 (CPI Mar), KB-CARL-206 (inflation expectations un-anchoring), KB-CARL-207 (SDART Feb loss acceleration), KB-CARL-208 (Discover deregistration), KB-CARL-209 (COMET baseline), KB-CARL-210 (cross-trust cure collapse confirmation).

### Cross-Agent Signals
- Previously sent: CARL → REGINALD (non-bank servicer warehouse exposure, Apr 13 — delivered Apr 14)
- Convergence bump to 57/60 should be propagated to PROME next spawn

---

## 2026-04-13 — HY OAS COMPRESSION + NON-BANK SERVICER RESEARCH + KB ARCHITECTURE

### THESIS v2.2 (refinement, not version bump)
**Author:** CARL (script-driven data refresh + research drill-downs)
**Action:** Major data refresh + structural finding on non-bank mortgage servicer transmission pathway.

### KEY FINDINGS
- **HY OAS complacency gap widening.** Spreads collapsed 346→294bps in 10 days (ceasefire Apr 8 = -18bps single session, plus NFP headline beat). Now BELOW 300bps elevated threshold while student loan defaults hit 9.2M, CMBS MF DQ reached ATH 7.15%, existing home sales approached <4.0M RED. Market split: JPM AM/Marks bullish ("tight justified"), Goldman 45% recession/Cambridge/Wellington/UBS warning on complacency. CARL interpretation: structural demand (CLO/pension/ETF flows) + index survivorship bias masking fundamental deterioration. Late-2007 analog (HY 260bps June → 800+ Nov). KB-CARL-200.
- **Non-bank mortgage servicer stress accelerating.** PennyMac FHA DQ spiked 5.9→7.5% single quarter Q4 2025, advance expenses +14%. GAO-26-107436 (Feb 2026): 35% of 550+ non-banks have high debt, only 30% profitable in 2022-23 downturn. **Ginnie Mae has NO stagflation stress test** — our thesis environment is the untested scenario. loanDepot $107.5M net loss, pledging GNMA MSR income. Lakeview (18% DQ)/Freedom (15.5%) private black boxes. MFS UK collapse (Feb 2026, Barclays $669M loss) = warehouse contagion template. Ginnie advance obligation asymmetry (advance until FINAL resolution) converts FHA DQ pipeline to cumulative cash drain. KB-CARL-202, KB-CARL-203, KB-HMR-046 through 052.

### Infrastructure Built
- 7-script CARL monitoring suite operational (thresholds, gas_tracker, consumer_pulse, catalyst_countdown, housing_pulse, abs_monitor, boot)
- abs_monitor expanded 4→6 issuers (added Exeter, Ally, GMF/AmeriCredit). 17 trusts tracked. SoFi excluded (private/144A).
- KB Migration Chunk 1 DONE: 44 housing entries delegated CARL → HOMER. HOMER KB 35→52 entries. Cross-domain claims retained in CARL.

### Cross-Agent Signal
- **CARL → REGINALD outbox:** Non-bank servicer warehouse line exposure. Request: check WAL/FHN/TCBI warehouse exposures, JPM Q1 warehouse commentary. Delivered Apr 14.

### KB Added (Apr 13: 5 entries)
KB-CARL-200 (HY OAS compression), KB-CARL-201 (CPI Energy +12.5%), KB-CARL-202 (non-bank transmission), KB-CARL-203 (Ginnie Mae no stagflation test), plus 7 HOMER entries on non-bank servicer research.

---

## 2026-04-09 — POP DEEP DIVE: INVISIBLE INCOME + BANK PIPELINE + NEW CONVERGENCE VECTOR

### CONVERGENCE MATRIX Updated
**Author:** CARL (via POP deep dive synthesis)
**Action:** New vector #11 added. Matrix expanded from 10 vectors (50pt) to 11 vectors (55pt). Score 47/50 → 51/55.

| Vector | Change | Reason |
|--------|--------|--------|
| #11 SB Bankruptcy + Owner Income | **NEW** 🔴 4/5 | POP deep dive confirmed: (1) Subchapter V +67% YoY BREACHED, Ch.11 +37%. (2) Owner income destruction refined to $73-145B annually ($83-165B tariff-adjusted) across two channels: active salary cuts (BofA 32%) + chronic income suppression. (3) SBA 7(a) defaults 3.7% (12-yr high). (4) 59% personal guarantees → business failure converts to consumer credit event. This is an explicit vector that was previously implicit in employment rot. Now measurable with leading indicators. |

### PREDICTIONS Added
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-15 | **NEW** 65% | SBA 7(a) defaults exceed 6.5% by EOY 2026. Currently 3.7%, consensus 6.5-7.5%. Tariff acceleration + EIDL burden + elevated rates. |
| CRL-16 | **NEW** 60% | Regional bank Q2 2026 earnings show SB provision increases >25% YoY. Default lag model: tariff stress → charge-off = 9-12mo. Q2 = first window. |
| CRL-17 | **NEW** 55% | SB owner income destruction exceeds $100B annualized by Q3 2026 (tariff-adjusted). Wide confidence range — no survey measures cut magnitude. |

### KB Added (8 entries: KB-CARL-166 through KB-CARL-173)
Key entries: Owner income destruction refined estimate (166), CFPB primary earner data (167), S-corp distribution gap (168), SBA defaults (169), tariff importer burden (170), SubV +67% (171), regionals $600B SB loans (172), OZK NCO 1.18% (173).

### VX Added (2 vectors at CARL level)
- VX-CARL-POP-01: SB Owner Income Destruction — RED ($73-145B annually, invisible to BLS/payroll)
- VX-CARL-POP-02: SB Bankruptcy Pipeline — RED (SubV +67% BREACHED, SBA defaults 12-yr high)

### FLOW Added (2 cascades at CARL level)
- FLOW-CARL-11.01: Tariff → SB margin → owner comp → consumer spending (ACTIVE-RED)
- FLOW-CARL-11.02: SB stress → regional bank SB loan losses (WARMING-ORANGE, Q2-Q3 visibility)

### Source Documents
- POP/domain/sources/INVISIBLE_INCOME_DEEP_DIVE.md (610 lines, 32 sources)
- POP/domain/sources/SB_BANK_PIPELINE_DEEP_DIVE.md (338 lines, 46 sources)

---

## 2026-04-06 — STUE FIRST SPAWN: CASCADE AMPLIFIER FINDING + CRL-05 UPGRADE

### PREDICTIONS Updated
**Author:** CARL (via STUE analysis)
**Action:** CRL-05 confidence upgraded 72% → 82%. Two new predictions added (CRL-13, CRL-14).

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 72% → **82%** | CC 90+ DQ GFC breach. STUE cascade analysis: student loan credit score destruction (-87 to -171 pts, NY Fed data) cascades into CC DQ. 10-12M borrowers face score damage → 3-5M cascade into CC 30+ DQ → est. +0.5-1.0pp to CC 90+ rate. This is an ADDITIONAL pathway to GFC breach beyond cost squeeze. Two independent mechanisms now identified: (1) multi-vector cost squeeze, (2) student loan credit score cascade. |
| CRL-13 | **NEW** 70% | SAVE non-selection rate >35%. Based on Oct 2023 precedent + MOHELA failures. 2.6M+ face $0→$407/mo payment cliff. |
| CRL-14 | **NEW** 65% | MOHELA-caused additional defaults >500K from July 1 transition. Servicer operational capacity near-zero for clean transition. |

**Key analytical finding:** Student loan vector is a **cascade amplifier**, not just a standalone 5/5 convergence score. It raises the effective impact of CC (Vector 1), subprime auto (Vector 2), K-shape convergence (Vector 9), and foreclosure acceleration (Vector 10) through the credit score destruction channel.

### STUE STATUS.md Updated
**Action:** Comprehensive refresh with Spawn 1 data pulls.
- SAVE: "ending" → **"REPEALED BY LAW"** (Working Families Tax Cuts Act)
- Added: ED final guidance Mar 31, Tiered Standard Plan option, 8.8M forbearance (6.5M SAVE), Exhibit C deadline MISSED (auto full relief), 25% of all borrowers DQ (3x pre-pandemic), 1,800+ colleges flagged, payment shock quantified ($0→$407/mo), spending destruction ($1.5-2B/mo), non-selection rate estimate (30-45%), Senate opposition to Treasury transfer
- Upgraded status: 🔴 → 🔴🔴 CRITICAL

### New KB Entries
KB-CARL-155 through KB-CARL-157 (HH spending-income scissors, BofA spending-by-income tier, Minneapolis Fed K-shape publication).

### Data Pruning
- KB-CARL-029: ACTIVE → SUPERSEDED (by KB-145)
- ML-CARL-SL-01: ACTIVE → SUPERSEDED (by KB-145, STUE owns detail)
- ML-CARL-SL-02: ACTIVE → SUPERSEDED (Ninth Circuit resolved, KB-149)
- VX-CARL-1.06: RED → CONSOLIDATED (into SL-01 through SL-07)
- VX-CARL-SL-03: "ENDING" → "REPEALED BY LAW"

**Old view:** Student loan at 5/5 max, standalone vector. SAVE "ending" Jul 1.
**New view:** Student loan at 5/5 AND cascade amplifier for Vectors 1/2/9/10. SAVE REPEALED BY LAW. CC GFC breach pathway now dual-mechanism (cost squeeze + credit score cascade). CRL-05 is the upgraded conviction call.

---

## 2026-04-04 — STUDENT LOAN VECTOR REFRESH: 4→5, STUE ACTIVATED

### THESIS Updated (minor, no version bump — convergence upgrade)
**Author:** CARL
**Action:** Student loan convergence vector #4 upgraded 4→5 (max). Convergence score 46→47/50. STUE sub-agent created.

**What changed:**
1. **FSA Data Center (Dec 2025, Mar 13 release):** 7.7M borrowers in default on $180B. +2.5M since Sep 2025. Active repayment 31+ DQ rate: 18.6% by dollar (vs 12.7% Dec 2019 — 46% worse). <40% of borrowers in repayment.
2. **~25% DQ rate:** Protect Borrowers/TCF analysis — 25% of borrowers with payment due are behind. 7.9M entered delinquency in first 3Q 2025. Projection: 13M in default by EOY 2026.
3. **SAVE ending Jul 1:** Settlement with Missouri. 7.5M borrowers get 90 days to select new plan. Non-selectors → 10-year standard plan (payment shock). RAP launches Jul 1.
4. **MOHELA failures:** 2.5M missed bills → 800K manufactured delinquencies. Wait times 7-50x peers. ~2M credit report errors. $7.2M DOE penalty.
5. **Treasury transfer (Mar 19):** Phase 1 — 9M defaulted borrowers to Treasury. Legal authority disputed.
6. **Sweet v. McMahon:** 205K automatic discharges (Ninth Circuit rejected DOE delay Mar 25). Minor positive, drop in bucket.

**Old view:** Student loan 90+ DQ at 9.6%, trending toward 10%. Vector score 4/5. SAVE enjoined, forbearance holding. Passive monitoring.
**New view:** Mass default event actively executing. 7.7M in default, 25% DQ, servicer failures amplifying, SAVE ending forces 7.5M into repayment Jul 1, Treasury transfer creating chaos. Vector score 5/5 (max). STUE sub-agent activated for dedicated tracking.

### PREDICTIONS Updated
| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-04 | 88% → **95%** | Student 90+ DQ >10%. FSA confirms 7.7M default, ~25% DQ, 18-29 cohort at 21%. SAVE ending Jul 1. Near-certain on next NY Fed release. |

### New KB Entries
KB-CARL-145 through KB-CARL-151 (7 entries covering FSA update, DQ rate, SAVE settlement, Treasury transfer, Sweet v. McMahon, MOHELA failures, demographic concentration).

### New VX Entries
VX-CARL-SL-05 (Borrowers in Default), VX-CARL-SL-06 (Treasury Transfer), VX-CARL-SL-07 (Servicer Failure). Existing SL-01 through SL-04 upgraded ORANGE→RED.

---

## 2026-04-03 — NFP MARCH: HEADLINE MASKS STRUCTURAL ROT

### PREDICTIONS Updated
**Author:** CARL
**Action:** Confidence adjustments on 3 predictions after NFP Mar +178K headline beat.

| Pred_ID | Change | Reason |
|---------|--------|--------|
| CRL-05 | 75% → **72%** | CC 90+ DQ GFC breach. Headline beat removes single-month employment catalyst, but Feb revised to -133K, LFPR 61.9%, real wages near zero. Multi-vector cost squeeze now primary driver, not employment break. |
| CRL-09 | 75% → **73%** | JOLTS Mar <0.88. NFP +178K could imply some hiring channels reopened (healthcare, construction), but Kaiser return is one-time and LFPR collapse means denominator may shrink. |
| CRL-11 | 85% → **83%** | Hires rate ≤3.2%. NFP establishment survey shows hiring in healthcare/construction/transport, but Kaiser is one-time. LFPR collapse suggests discouraged workers exiting, not broad hiring. |

**Old view:** NFP -92K (Feb) was the employment catalyst accelerating consumer stress conversion.
**New view:** NFP Mar +178K headline removes acute employment break narrative but internals (LFPR 61.9%, Feb revised -133K, wages 3.5% YoY) confirm structural rot. Mechanism unchanged — cost squeeze is primary, not employment detonator. Timeline: no change to Q2-Q3 stress window.

**No THESIS version bump.** Thesis structure unchanged. Evidence base shifts slightly (employment less acute, but structural rot deepens). All load-bearing vectors intact.

---

## 2026-04-03 — FILE STRUCTURE REORGANIZATION

### THESIS.md Restructured
**Author:** CARL + Will
**Action:** Moved THESIS.md to thesis/ directory. Extracted Composition Shift narrative to this CHANGELOG. Convergence matrix marked as canonical (STATUS.md mirrors). PREDICTIONS.tsv moved from workbook/ to thesis/.

---

## 2026-03-31 — v2.1: JOLTS INVERSION + GAS $4 + TRIPLE NITROGEN SEIZURE

### THESIS Updated: v2.0 → v2.1
**Author:** CARL
**Action:** Minor version bump. Three vectors converging simultaneously confirmed.

**What changed:**
1. **JOLTS Feb: 0.91 (deepening).** Ratio dropped from 0.94 (Jan) to 0.91 in one month. Hires rate 3.1% = COVID-low. Quits rate 1.9% (8-month streak — workers trapped). Feb data PREDATES Iran — March will be worse.
2. **Gas $4.02 behavioral breakpoint FIRED.** Up $1.04 in 33 days (+35%). SPR 172M barrel release failing — gas rose through the entire release. CNN behavioral confirmation of fuel-vs-food tradeoffs.
3. **USDA wheat acreage: LOWEST SINCE 1919.** Corn -3.45M acres. Farmers fleeing N-intensive crops. Triple nitrogen seizure confirmed (Gulf + China + Russia). Food CPI loading for Q3-Q4.
4. **Convergence score upgraded:** UI exhaustion 4→5 (duration +2.0wk single month), gas confirmed at max. Total: 44→46/50.

**Old view (v2.0):** Multi-vector cost squeeze replacing employment detonator. Gas approaching $4, JOLTS newly inverted, food CPI possible but unconfirmed.
**New view (v2.1):** Three independent vectors SIMULTANEOUSLY confirmed/firing. Gas $4 breached. JOLTS deepening. USDA locks in food CPI. No longer prospective — executing. Q3 = consumption stress quarter.

### PREDICTIONS Added
- CRL-09: JOLTS Mar ratio <0.88 (75% conf)
- CRL-10: Food CPI YoY >4.0% (70% conf, Q4 2026)
- CRL-11: Hires rate ≤3.2% through Q2 (85% conf)

---

## 2026-03-27 — INSURANCE RELIEF COUNTER-SIGNAL

### THESIS Updated (minor, no version bump)
**Author:** CARL
**Action:** Added insurance relief as counter-evidence.

**What changed:**
- Auto insurance CPI collapsed from 20-30% to 5.9% YoY (BLS Feb 2026)
- Homeowners insurance decelerating: national +8.5%, FL +18%, down from 50% (Insurify 2025)
- Two cost-squeeze vectors easing

**Assessment:** Partially offsets thesis but outweighed by energy, food, and UI exhaustion vectors intensifying. No score change. Logged in counter-evidence section.

---

## 2026-03-10 — v2.0: MECHANISM SHIFT (MAJOR)

### THESIS Updated: v1.0 → v2.0
**Author:** CARL
**Action:** Major version bump. Thesis mechanism fundamentally changed.

**Old view (v1.0, Feb 2026):** Employment cracks → subprime auto/CC DQ spikes → bank NCOs → systemic repricing. Linear, fast, employment-first. Single-point-of-failure model.

**New view (v2.0, Mar 2026):** Multiple cost vectors (energy + food + insurance + HOA) simultaneously compress the bottom 60% while housing prices decline nationally. Employment is a slow grind, not a detonator. K-shape converging downward (top 40% now pulling back). Conversion through COST SQUEEZE + UI EXHAUSTION rather than mass layoffs.

**Why the mechanism changed:** v1.0 assumed employment breaks → credit collapses → banks eat losses. Reality is a multi-point-of-pressure system. We expected an earthquake; we got subsidence — the ground is sinking everywhere, slowly, from multiple causes. The destination (consumer credit crisis → bank losses) is the same; the path is different.

**Implications:**
- **Timing:** Slower than v1.0. Q2-Q3 stress, grinding not step-function.
- **Trades:** Longer duration needed. Roll timelines, don't trim positions.
- **Convergence score:** Established 10-vector matrix to track multi-source pressure.

### PREDICTIONS Established
- CRL-01 through CRL-08 created (initial prediction set)

---

## 2026-02-23 — v1.0: THESIS ESTABLISHED

### THESIS Created: v1.0
**Author:** CARL
**Action:** Initial thesis — "Beneath the Ice"

**Core claim:** 60% of American households are structurally fragile. Employment crack is the detonator. Subprime auto and CC delinquencies are the first visible signals. Bank NCOs follow.

**Initial predictions:** CRL-01 (gas peak stress), CRL-02 (subprime auto 60+ DQ >7.0%)

---

*This document is the audit trail for thesis evolution. Log every change with what/why/old→new. Read when assessing conviction or reviewing prediction calibration.*
