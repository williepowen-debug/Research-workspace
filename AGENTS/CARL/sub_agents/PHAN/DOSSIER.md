# PHAN DOSSIER — Phantom Debt & Shadow Credit

> **What this is.** PHAN (Phantom Debt / Shadow Credit monitor) was **demoted from full sub-agent to dossier on 2026-07-10** (DAEDALUS CARL sub-agent audit, Will-approved). This file is the **single entry surface** for the phantom-debt domain going forward. It is not a live dashboard: it carries PHAN's durable analytical assets (frameworks, thresholds, open predictions, transmission pathways) at their original vintages, each fact stamped with its own as-of date and file:line origin. No new analysis is authored here — this is transcription-with-provenance.
>
> **Domain scope** *(carried from CLAUDE.md:5,7)*: phantom debt / shadow credit — the $400B+ in consumer borrowing invisible to credit bureaus. BNPL stacking, cash-advance / earned-wage-access (EWA) apps, fintech-lender ("cockroach") health, regulatory visibility changes (CFPB 1033), and phantom-DTI impact on mortgage underwriting (→ HOMER).
>
> **Refresh model.** No standing sessions. Refreshed by **ad-hoc CARL spawns** against this dossier (per CARL SPAWN_PROTOCOL templates). **Next natural catalyst:** Affirm / Klarna Q2 prints, ~Aug-2026. See §8 Refresh Protocol.
>
> **⚠️ Vintage warning.** The legacy identity surfaces (CLAUDE.md, STATUS.md) are FROZEN at their Apr-2026 build vintage and carry a Klarna narrative that has since been **REFUTED at parent** (Klarna Q1-2026 profitable, CARL May-14). Do not cite any "Current" value in this dossier as live — see §6 SUPERSEDED AT PARENT.

---

## 1. Header / orientation

| | |
|---|---|
| **Agent** | PHAN — Phantom Debt & Shadow Credit Monitor |
| **Status** | DEMOTED TO DOSSIER 2026-07-10 (was: full sub-agent, reports to CARL via State Vectors) |
| **Domain** | Phantom Debt / Shadow Credit / Non-Bank Lending *(CLAUDE.md:7)* |
| **Parent system of record** | CARL — `workbook/BNPL_STRESS.tsv` (44 rows), `KB.tsv` (KB-CARL-228 ALLY-analog), KB-CARL-028/138/139 *(CLAUDE.md:158-179)* |
| **Legacy last session** | 2026-04-17 (STATUS.md:2) |
| **Live append surfaces (this dir)** | `workbook/COCKROACH.tsv`, `workbook/REGULATORY.tsv` — see §5 |
| **Frozen surfaces (this dir)** | CLAUDE.md, STATUS.md, `workbook/{VX,ML,FLOW,PREDICTIONS,PROVIDER}.tsv` |

---

## 2. Frameworks (durable analytical assets)

The reason PHAN survives as a dossier: three analytical assets that exist nowhere else at parent, or in more detail than parent holds.

### 2a. Phantom-DTI Gap framework (35% apparent → 47% real)

*Carried from STATUS.md:110-121 + CLAUDE.md:54-58,144. This is PHAN's core original framework.*

The hidden risk to HOMER's housing vector:
- Consumer shows **35% DTI** to the mortgage underwriter.
- Actual DTI including BNPL / cash advances: **47%** — a **~12pp gap**.
- Only **Affirm** reports to credit bureaus (2 of 3). Klarna, Afterpay, Zip, Sezzle **do not report**.
- Lenders now scanning bank statements for BNPL debits (workaround).
- HUD investigating BNPL impact on FHA underwriting (RFI, 2025-06-24 — see §5 REGULATORY).
- **FHA borrowers (11.52% DQ) are MOST exposed** — lowest income, highest BNPL usage. *(as-of Apr-2026 vintage; verify at parent before citing the 11.52% figure)*

**Cross-agent signal — PHAN → HOMER:** phantom debt inflates apparent housing affordability. When payments resume/increase, the "surprise" defaults are amplified by invisible obligations. *(STATUS.md:121)*

### 2b. CFPB Rule 1033 death — carried VERBATIM

*Transcribed verbatim from STATUS.md:92-108 (DAEDALUS audit: the best writeup of this fact anywhere in the fleet). Vintage: Apr-17-2026. The 1033-death is a durable regulatory fact; the PHAN-P03 confidence note is a legacy self-mark, unresolved — see §4.*

> **CFPB 1033: WHAT HAPPENED (Updated Apr 17)**
>
> **Original plan:** CFPB Rule 1033 would force largest banks to share consumer financial data by Apr 1, 2026. BNPL providers (as card issuers per CFPB interpretive rule) would be covered. This would have created a "visibility shock" — suddenly phantom debt becomes visible.
>
> **What actually happened:**
> 1. Banking groups sued to block the rule
> 2. Federal judge enjoined enforcement (Sep 2025)
> 3. Trump administration's CFPB questioned its own funding mechanism
> 4. Aug 2025: CFPB issued ANPRM on "reconsideration"
> 5. Apr 1, 2026: Deadline passed with rule unenforced
> 6. **NEW (Apr 2026): CFPB chief legal officer Mark Paoletta filed motion to WITHDRAW Rule 1033** — CFPB now calling its own rule "unlawful and should be set aside" [Mitchell Sandler Apr 2026, Cozen O'Connor]
>
> **Status escalation: ON HOLD → EFFECTIVELY DEAD.** This is now worse than an injunction — the agency itself is moving to kill it.
>
> **CARL implication:** The visibility shock is NOT COMING via regulation. It will come via defaults — larger and more sudden. $40-60B distressed BNPL accumulates unchecked. Prediction PHAN-P03 should move confidence 75% → 90%.

### 2c. Transmission pathways (FLOW-PHAN-01..06) — with breakpoints + lags

*Carried from `workbook/FLOW.tsv` (the canonical workbook version, which holds the breakpoint/lag/mechanism columns). FLOW-06 ALLY-analog trigger detail exceeds what parent KB-CARL-228 holds — carried in full. Vintage: FLOW-01..05 Apr-2026 build; FLOW-06 new 2026-04-17.*

| ID | Name | Breakpoint (becomes critical when…) | Lag | Confidence | Status | Cross-domain |
|---|---|---|---|---|---|---|
| **FLOW-PHAN-01** | Shadow → Visible Credit Transmission | Shadow credit capacity exhausted; consumer must choose what to default on | 6–12 mo | HIGH 75% | MONITORING | CARL |
| **FLOW-PHAN-02** | BNPL Stacking Cascade | BNPL payments exceed 15% of income | 3–6 mo | HIGH 80% | ACTIVE | Consumer spending, Credit cards |
| **FLOW-PHAN-03** | Payday Debt Trap Cascade | Consumer in perpetual rollover (>6 consecutive months) | Immediate trap | HIGH 75% | MONITORING | Consumer savings, Bank overdrafts |
| **FLOW-PHAN-04** | Fintech Cockroach Cascade | Multiple fintech failures; funding-market stress | 3–9 mo | HIGH 85% | ACTIVATING | CARL (all vectors), Bank credit |
| **FLOW-PHAN-05** | PHAN-to-CARL Transmission | Shadow-credit stress appears in traditional metrics | 6–12 mo | HIGH 80% | ACTIVATING | CARL (credit exhaustion) |
| **FLOW-PHAN-06** | BNPL Composition-Masking → ABS Surprise (ALLY Analog) | Provision growth >30% YoY **AND** ABS WA FICO declining **AND** macro shock (gas >$4.50 / UI exhaustion) | 3–9 mo | MED-HIGH 65% | EARLY | LIQUID (ABS repricing), REGINALD (bank ABS exposure), CARL |

**FLOW-PHAN-06 full detail** *(FLOW.tsv:7 — carry fully, exceeds parent KB-228):*
- **Pathway:** BNPL originator tightens underwriting (headline DQ improves) → lower-quality cohorts routed to ABS trusts → ABS WA FICO declines → provisions grow faster than DQ (leading indicator) → ABS performance worsens as macro pressures hit tail → structured-credit repricing → LIQUID/REGINALD vectors fire.
- **Mechanism:** Composition masking at BNPL level mirrors ALLY auto — headline clean (DQ declining) but hidden mix downgrade in ABS structures and provision divergence betrays loading. When macro shock hits (gas, UI, food), the tail performs worse than headline DQ implied.
- **Trigger:** Provision divergence from DQ headline — NOW ACTIVE per legacy vintage (Affirm +40% YoY provisions vs DQ improvement).
- **Evidence (Apr-17 vintage):** Affirm provisions +40% YoY; ABS FICO 672 (lowest since 2022-A trust); ALLY analog with 6-month lag expectation. ⚠ Affirm quarterly figures now owned at parent — see §6.

> **⚠ Numbering divergence (transcription note):** The legacy STATUS.md:157-194 prose used a *different* FLOW numbering — its FLOW-PHAN-03 was "Cockroach Cascade" and FLOW-PHAN-04 was "Phantom DTI → Mortgage Surprise" (🟡 LOADING, 6–18mo lag), a pathway not present in FLOW.tsv. The table above follows the **FLOW.tsv canonical numbering** (which carries the breakpoint/lag columns). The STATUS "Phantom DTI → Mortgage Surprise" pathway is preserved by §2a above. Do not treat the two numbering schemes as reconciled — they were divergent at freeze.

---

## 3. Thresholds (bands durable; "Current" = build-vintage snapshot, not live)

*Carried from CLAUDE.md:61-69. Bands + sources are durable. The original "Current" column was hardcoded in the instructions file and rots independently of STATUS (DAEDALUS audit finding). Each snapshot value below is **re-labeled as a build-vintage reading with its as-of date** — none is live.*

| Metric | Snapshot value (as-of) | Yellow | Orange | Red | Source |
|---|---|---|---|---|---|
| BNPL Stacking | 63% *(CFPB Jan-2025)* | >35% | >45% | >55% ✅ | CFPB |
| Cross-Firm Stacking | 32% *(CFPB Jan-2025)* | >20% | >25% ✅ | >35% | CFPB |
| Affirm 30+ DQ | 2.3% *(Affirm Q4 FY25, 2025-09-30)* ⚠§6 | >3% | >4% | >6% | Affirm SEC |
| Klarna Credit Loss Provision | 0.65% *(Klarna Q4-25, 2025-12-31)* ⚠**REFUTED §6** | >0.60% ✅ | >0.80% | >1.0% | Klarna 20-F |
| BNPL Late Payment Rate | 34–41% *(ABA 2024)* ⚠§6 | >25% | >35% ✅ | >45% | ABA |
| Fintech Failures (cumulative) | 3 *(CURO/Tricolor/Synapse, ≤Apr-2026)* | 2 | 3 ✅ | 5+ | Public |
| Phantom DTI Gap | ~12pp *(35%→47%, CARL est)* | >5pp | >10pp ✅ | >15pp | CARL est |

> ✅ marks the band the snapshot value had tripped **at build vintage**. These check-marks are frozen — re-evaluate against live parent data before citing any as "breached now."

---

## 4. Open predictions (7 rows — ⚠ UNRESOLVED, resolution is CARL's)

*Carried from `workbook/PREDICTIONS.tsv`. All 7 made 2026-04-09 (P03/P07 confidence-upgraded Apr-17). **All marked ⚠ UNRESOLVED — do NOT resolve or re-mark from this dossier.** A future CARL spawn resolves these and flags outcomes to CARL parent (see §8). Confidences are the April marks.*

| # | Prediction | Conf (Apr) | Timeframe | Resolution status |
|---|---|---|---|---|
| **PHAN-P01** | BNPL stacking >70% | 60% | H2 2026 | ⚠ UNRESOLVED — was 63% at build; no reporting = no constraint on growth |
| **PHAN-P02** | Klarna credit losses >1.0% | 65% | FY2026 | ⚠ UNRESOLVED — ⚠ **premise (rising Klarna losses) refuted at parent §6**; still CARL's to formally resolve |
| **PHAN-P03** | CFPB 1033 enforcement delayed beyond 2026 | 90% | EOY 2026 | ⚠ UNRESOLVED — upgraded 75%→90% Apr-17 (CFPB moved to withdraw rule) |
| **PHAN-P04** | At least 2 more fintech failures | 60% | 2026 | ⚠ UNRESOLVED — 3 already (CURO/Tricolor/Synapse); FloatMe/Current = investigations, not failures |
| **PHAN-P05** | BNPL-linked mortgage defaults identifiable in FHA data | 50% | Q3–Q4 2026 | ⚠ UNRESOLVED — HUD RFI signals awareness; low confidence |
| **PHAN-P06** | NY passes first comprehensive BNPL licensing law | 55% | 2026 | ⚠ UNRESOLVED — proposed 2026-04-09 |
| **PHAN-P07** | Cash-advance AG enforcement expands to 5+ states | 75% | 2026 | ⚠ UNRESOLVED — upgraded 65%→75% Apr-17 (CO active, CT enacted, FloatMe/Current investigations; 12 state laws, ~20 pending) |

---

## 5. Live ledger index (append targets for ad-hoc spawns)

Two workbook TSVs **stay LIVE** as append surfaces — DAEDALUS audit flagged both as unique fleet assets that exist nowhere at parent. A future ad-hoc spawn appends here (do not freeze these):

| Ledger | Role | State | Contents at freeze |
|---|---|---|---|
| **`workbook/COCKROACH.tsv`** | Fintech-failure / distress tracker | 🟢 **LIVE** | 8 rows: CURO (FAILURE 2024-06-30), Synapse (FAILURE 2024-07-01), Tricolor (FAILURE 2025-03-01, bank contagion), Upstart (RETREAT 2025-12-31), Klarna (CLASS_ACTION 2025-12-15 + DISTRESS 2026-02-19), FloatMe (DISTRESS 2026-04-01), Current (DISTRESS 2026-04-01) |
| **`workbook/REGULATORY.tsv`** | 1033-death + 12-state EWA-law timeline | 🟢 **LIVE** | 16 rows: CFPB 1033 arc (RULE 2024-10-22 → ANPRM 2025-08-22 → injunction 2025-09-01 → MISSED deadline 2026-04-01 → WITHDRAWAL 2026-04-01); EWA state laws (CO HB25-1020 live 2026-01-01; CT Oct-2025); AG actions (NY_AG DailyPay/MoneyLion; DC_AG EarnIn; FTC Brigit); 8-court TILA "finance charge" ruling |

**Frozen-vintage ledgers** (carried into this dossier, no longer maintained — see §6/§7 for where their facts now live): `VX.tsv` (16 vectors), `ML.tsv` (11 master-log entries), `FLOW.tsv` (6 pathways → §2c), `PREDICTIONS.tsv` (7 → §4), `PROVIDER.tsv` (34 provider-metric rows → largely superseded at parent, §6).

---

## 6. ⛔ SUPERSEDED AT PARENT — do NOT cite from here

*These facts are now owned by CARL parent surfaces. The legacy PHAN values below are frozen and, in the Klarna case, **refuted**. Cite the parent surface, not this dossier.*

| Fact | Legacy PHAN value (frozen) | Canonical owner / correction |
|---|---|---|
| **Klarna Q1-2026 profitability** | STATUS.md asserts Klarna FY2025 net loss, provisions "rising," "narrative cracking," Elliott $6.5B lifeline | ⛔ **REFUTED — Klarna Q1-2026 PROFITABLE** (CARL parent, May-14-2026). The legacy Klarna deterioration narrative is wrong. |
| **Affirm quarterlies** (GMV, DQ, provisions, ABS FICO) | 2.3% DQ, $214.2M provisions (+40% YoY), ABS WA FICO 672, GMV $13.8B | **KB-CARL-228 + CARL `workbook/BNPL_STRESS.tsv`** canonical |
| **Klarna quarterlies** (provisions, revenue, class action) | 0.65% provisions, $1.08B rev, case 25-cv-07033 | **KB-CARL-228 + `BNPL_STRESS.tsv`** canonical |
| **BNPL late-payment rate** | 41% (ABA) | Owned at parent — verify current figure at CARL |
| **CC 90+ DQ** | 12.70% (STATUS.md:156 uses this as the phantom-debt multiplier base) | **Parent now 13.1%** — use CARL's figure |
| **ALLY-analog conclusion** (composition-masking) | FLOW-PHAN-06 + SV-PHAN-2026-04-17-01 | **KB-CARL-228** canonical; §2c here retained only as the *mechanism/trigger* framework, not for the Affirm data points |

---

## 7. Sources + cadence

*Carried from CLAUDE.md:72-84 + STATUS/ML source citations.*

| Source | Frequency | Covers |
|---|---|---|
| CFPB BNPL Reports | Periodic | Stacking, usage patterns, market size |
| Affirm (AFRM) earnings | Quarterly (FY Q3 ~May) | GMV, DQ, Card growth, credit performance |
| Klarna (KLAR) financials | Quarterly | DQ, provisions, class-action status |
| NY Fed QHDC | Quarterly | Household debt (misses phantom) |
| State AG announcements | Ongoing | EWA / cash-advance enforcement |
| **NCLC court tracker** | Ongoing | EWA "finance charge" rulings (8-court TILA line) |
| CFPB Rule 1033 status | Ongoing | Open-banking enforcement timeline |
| FICO | Periodic | BNPL score adoption (FICO 10 / 10 T BNPL) |
| **Richmond Fed EB** | Periodic | BNPL research — **EB 26-05 key** (KB-CARL-028: BNPL late 34%→41%) |
| **New Economy Project** | Ongoing | NYC cash-advance fee tracking ($650M+ drain) |
| **Chime regulatory tracker** | 2026 | State EWA-law count (12 enacted, ~20 pending) |

**Catalyst cadence:** Affirm FY Q3 ~May, Q4 ~Aug; Klarna quarterly ~mid-quarter-close+6wk. **Next natural refresh trigger:** Affirm / Klarna Q2 prints, ~Aug-2026.

---

## 8. Refresh protocol (how an ad-hoc spawn uses this dossier)

A CARL-directed ad-hoc spawn against the phantom-debt domain should:

1. **Read this DOSSIER** (not the frozen CLAUDE.md/STATUS.md) for framework, thresholds, open predictions, and the two live ledgers.
2. **Append new events to the live TSVs only** — `workbook/COCKROACH.tsv` (new failures/distress/class actions) and `workbook/REGULATORY.tsv` (new EWA laws, AG actions, 1033 developments). Do not revive the frozen TSVs.
3. **Update the as-of stamps** in §3 (thresholds) and §6 (superseded) if a value the dossier snapshots gets a fresh parent reading.
4. **Resolve predictions at CARL, not here** — if a §4 prediction resolves, flag the outcome to CARL parent (CARL owns the resolution; this dossier's §4 stays ⚠ UNRESOLVED until CARL records it). Per DAEDALUS audit, no sub-agent due-scan machinery reaches these — resolution is a deliberate spawn action.
5. **Route findings to CARL** via the normal SV/handoff channel; CARL's `BNPL_STRESS.tsv` + KB-CARL-228 remain the system of record for Affirm/Klarna quarterlies.

---

*PHAN dossier assembled 2026-07-10 by MOLD (DAEDALUS editor), from PHAN's Apr-2026 frozen surfaces. Transcription-with-provenance — no new analysis. Legacy identity surfaces (CLAUDE.md, STATUS.md) frozen same day; COCKROACH.tsv + REGULATORY.tsv stay live. Provenance and refutations per DAEDALUS audit `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`.*
