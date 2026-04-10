# CARL CHANGELOG

Tracks all changes to THESIS.md and PREDICTIONS.tsv. Reverse chronological. Each entry documents what changed, why, and the old view vs new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new mechanism, thesis break, conviction reversal). Minor (Y) = refinement (updated evidence, threshold adjustment, vector upgrade/downgrade).
- PREDICTIONS: changes logged by Pred_ID.

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
