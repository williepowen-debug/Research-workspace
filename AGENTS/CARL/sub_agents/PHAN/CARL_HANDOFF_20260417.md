# PHAN → CARL HANDOFF
**Date:** 2026-04-17 ~17:00 UTC
**Refresh type:** DATA REFRESH (8 days stale → current)
**Confidence range:** 65-90% across findings

---

## TOP FINDINGS (Priority Order)

### 1. CFPB Rule 1033: DEAD, Not Just Delayed — Confidence 90%
**Status change: ON_HOLD → EFFECTIVELY WITHDRAWN**

CFPB chief legal officer Mark Paoletta filed a motion in the pending litigation to WITHDRAW Rule 1033 entirely, stating the rule is "unlawful and should be set aside." This is beyond an injunction — the agency itself is moving to kill its own rule. [Mitchell Sandler Apr 2026; Cozen O'Connor Apr 2026]

**CARL implication:** The phantom debt visibility shock will NOT arrive via regulation. It will arrive via defaults — when it does, it will be sudden and larger than models predict. The $40-60B distressed invisible BNPL pool accumulates unchecked.

**Confidence upgrade recommended:** PHAN-P03 moved 75%→90%.

---

### 2. ALLY Framework Crossover on Affirm — Confidence 65% (partial match) ⭐
**Answer to focus item #6: PARTIALLY CONFIRMED — MECHANISM ANALOG VALID**

Evidence:
- Headline 30+ DQ: 2.3% (improved, declined from 2.4%) — [Affirm Q4 FY2025 / Q2 FY2026]
- **But:** Provision for credit losses Q2 FY2026: **$214.2M (+40% YoY vs $153M)** — [Affirm Q2 FY2026 earnings, Feb 2026]
- **And:** ABS WA FICO in AFRMT 2025-X1: **672** — lowest since 2022-A trust — [Morningstar presale report]
- **And:** Kerrisdale Capital Jan 2026 short report: median borrower FICO 652, 52% of customers below 660 [Kerrisdale]
- **And:** 43% non-prime receivables — management-disclosed [Affirm Q2 2026]

**The ALLY analog:**
- ALLY: headline NCO improving (5 consecutive quarters), but mix downgrade (S-tier -3pp, nonprime +40bps), ACL release (-$224M), CLN issuance +43%
- AFFIRM: headline DQ declining, but ABS FICO declining (lower-quality paper routed to ABS), provision +40% YoY (loading in reserves), median borrower FICO 652

**Mechanism: (b) is primary — tighter underwriting cutting subprime originations while existing tail runs off.** This produces genuine headline improvement but NOT borrower improvement. The tail is running through ABS trusts at lower credit quality. When macro shock hits (gas >$4.50, UI exhaustion, food inflation), the ABS cohorts will perform worse than headline DQ implied.

**(a) Portfolio sale analog (Klarna pre-IPO $26B):** Not confirmed for Affirm. Affirm uses securitization, not outright sale. The routing mechanism differs.

**(c) Securitization routing tail:** PARTIALLY CONFIRMED. ABS WA FICO 672 is the evidence. Not definitive without deal-by-deal comparison, but directionally consistent.

**Low confidence caveat:** Affirm's transaction-level underwriting genuinely differs from FICO-static models. CEO Levchin's "consumer is healthy" claim is not purely spin — Affirm does have real-time underwriting. The 40% YoY provision jump could also reflect GMV growth rather than pure credit deterioration. Need May 7 Q3 results for confirmation.

**Bottom line for CARL:** The ALLY composition-masking pattern HAS an analog in BNPL (Affirm specifically). The headline DQ improvement is real but partial — the tail is loading in ABS structures and provisions. This STRENGTHENS the phantom debt thesis for CARL's convergence matrix.

---

### 3. Affirm Q3 FY2026: CONFIRMED May 7, 2026 After Close — Confidence 99%
**Status change: "~May" → CONFIRMED MAY 7**

[Source: Affirm IR press release, Apr 16 2026 — morningstar.com, stocktitan.net]

Conference call: 2:00pm PT, May 7 2026.

**CARL: Remove research gap item "Affirm Q3 FY2026 earnings (~May)" — update to May 7. Key metrics to watch: DQ trend (will 2.3% hold?), provision QoQ change, ABS issuance activity.**

---

### 4. Klarna: Annual Net Loss, Q1 Guide Missed, Elliott $6.5B — Confidence 80%
**Status: DQ still elevated, fundamentals deteriorating**

- FY2025 net loss (reversed $21M profit in FY2024) [Bloomberg Feb 19 2026]
- Q4 2025 provisions: 0.65% — down from Q3's 0.72% but still +12bps vs prior year's 0.53%
- Q4 revenue: $1.08B (record, +38% YoY) — but Q1 2026 guide: $965M, MISSED analyst expectations
- Stock -15% premarket on Q4 earnings day
- Elliott Management $6.5B involvement — external capital signal [AiInvest Feb 2026]
- Class action: Nayak v. Klarna, 25-cv-07033 (EDNY) — lead plaintiff deadline passed Feb 20 2026; case proceeding to next stage
- Q1 2026 earnings expected ~May 18 (not yet confirmed as of Apr 17)

**PHAN-P02 tracking:** Provisions 0.65%, need 1.0% for prediction to confirm. Trajectory on track.

---

### 5. State EWA Enforcement Wave: New States + Laws — Confidence 85%
**State count now: 12 laws enacted, ~20 pending — CFPB vacuum being filled**

- **Colorado:** HB25-1020 LIVE Jan 1 2026 — first state with EWA licensing ($5-7 fee caps)
- **Connecticut:** EWA law enacted Oct 2025 — $4/advance, $30/month fee cap, classifies as finance charges
- **Colorado 2026 session:** HB26-1046 additional EWA regulation introduced
- **FloatMe, Current:** Under investigation by attorneys for disguised interest rates [ClassAction.org Apr 2026]
- Troutman Pepper AG Monitor Apr 16: confirms state enforcement surge, junk fees priority

**PHAN-P07 upgraded 65%→75%.** 5-state threshold likely breached by EOY 2026 given trajectory.

---

## SPECIFIC ROWS FOR CARL'S BNPL_STRESS.tsv

CARL should update/add the following rows in `workbook/BNPL_STRESS.tsv` (PHAN does not edit this file):

| Row Type | Entity | Metric | Old Value | New Value | Source |
|----------|--------|--------|-----------|-----------|--------|
| UPDATE | Affirm | provision_credit_losses_quarterly | $153M (Q2 FY2025) | $214.2M (+40% YoY) | Affirm Q2 FY2026 earnings Feb 2026 |
| UPDATE | Affirm | ABS_WA_FICO_trend | [not tracked] | 672 (AFRMT 2025-X1, lowest since 2022-A) | Morningstar presale |
| UPDATE | Affirm | Q3_FY2026_earnings_date | ~May 2026 | May 7 2026 confirmed | Affirm IR Apr 16 2026 |
| UPDATE | Klarna | FY2025_net_income | $21M profit (FY2024) | Net loss (FY2025 reversal) | Bloomberg Feb 19 2026 |
| UPDATE | Klarna | Q1_2026_earnings_date | Unknown | ~May 18 2026 (est., not confirmed) | Nasdaq/WallStreetZen |
| UPDATE | Klarna | class_action | Filed Dec 2025 | 25-cv-07033 EDNY — lead plaintiff phase complete, proceeding | Nayak v. Klarna docket |
| ADD | Klarna | elliott_capital | N/A | $6.5B investment — external funding signal | AiInvest Feb 2026 |
| ADD | CFPB | rule_1033_status | ON HOLD | WITHDRAWAL MOTION FILED — effectively dead | Mitchell Sandler Apr 2026 |
| ADD | Colorado | EWA_law_status | Proposed | LIVE Jan 1 2026 (HB25-1020) | Colorado Gen Assembly |
| ADD | Connecticut | EWA_law_status | Unknown | Enacted Oct 2025 ($4/advance, $30/mo cap) | Goodwin Jul 2025 |

---

## PREDICTIONS — CONFIDENCE SHIFTS

| Pred ID | Prediction | Old Confidence | New Confidence | Reason |
|---------|------------|----------------|----------------|--------|
| PHAN-P03 | CFPB 1033 enforcement delayed beyond 2026 | 75% | **90%** | CFPB moved to withdraw own rule — beyond delay to death |
| PHAN-P07 | Cash advance AG enforcement to 5+ states | 65% | **75%** | Colorado live, Connecticut enacted, FloatMe/Current investigations, Troutman monitor confirms surge |
| PHAN-P02 | Klarna credit losses >1.0% | 65% | 65% | On track but not accelerating faster; Elliott capital could slow deterioration temporarily |
| PHAN-P04 | 2 more fintech failures 2026 | 60% | 60% | FloatMe/Current are investigations only, not failures; cockroach count remains at 3+2 distress signals |

---

## CONVERGENCE MATRIX IMPLICATION

No new vector breaches this session. But:

1. **FLOW-PHAN-06 is NEW** — ALLY composition-masking analog in BNPL. Adds ABS structured credit as a secondary transmission path that CARL's convergence matrix doesn't currently capture. Recommend CARL add "BNPL ABS composition degradation" as a sub-vector under the existing ABS tracking in CARL's matrix.

2. **CFPB 1033 death** strengthens the "DELAYED repricing → LARGER SHOCK" thesis component. The bubble grows unchecked until defaults force visibility.

3. **State EWA wave** is double-edged: enforcement pressure could SHRINK phantom credit availability (if EWA apps exit states or restructure), potentially pulling forward the default wave by removing a buffer. This is a potential timeline accelerant not previously modeled.

---

## RESEARCH GAPS (UPDATED)

- [ ] **May 7 Affirm Q3 FY2026** — KEY: will DQ crack? Will ABS FICO trend continue? Will provisions grow further?
- [ ] **May 18 (est.) Klarna Q1 2026** — provisions trend; first full quarter post-guide miss
- [ ] **May 5 Upstart Q1 2026** — approval rate and DQ with new $1.4B revenue guidance
- [ ] Afterpay/Block Q1 2026 — BNPL flow through Cash App (no data)
- [ ] HUD RFI response — were responses received? Any preliminary FHA guidance?
- [ ] AFRMT 2025-X2 or 2026-A deal (when issued) — FICO composition trend confirmation

*PHAN session complete. All findings written to STATUS.md, workbook TSVs, and this handoff. No CARL files edited.*
