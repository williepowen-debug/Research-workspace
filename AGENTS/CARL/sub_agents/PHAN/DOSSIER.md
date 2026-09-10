# PHAN DOSSIER — Phantom Debt & Shadow Credit

> **What this is.** PHAN (Phantom Debt / Shadow Credit monitor) was **demoted from full sub-agent to dossier on 2026-07-10** (DAEDALUS CARL sub-agent audit, Will-approved). This file is the **single entry surface** for the phantom-debt domain going forward. It is not a live dashboard: it carries PHAN's durable analytical assets (frameworks, thresholds, open predictions, transmission pathways) at their original vintages, each fact stamped with its own as-of date and file:line origin. No new analysis is authored here — this is transcription-with-provenance.
>
> **Domain scope** *(carried from CLAUDE.md:5,7)*: phantom debt / shadow credit — the $400B+ in consumer borrowing invisible to credit bureaus. BNPL stacking, cash-advance / earned-wage-access (EWA) apps, fintech-lender ("cockroach") health, regulatory visibility changes (CFPB 1033), and phantom-DTI impact on mortgage underwriting (→ HOMER).
>
> **Refresh model.** No standing sessions. Refreshed by **ad-hoc CARL spawns** against this dossier (per CARL SPAWN_PROTOCOL templates). **Next natural catalyst / ad-hoc spawn trigger:** Affirm / Klarna Q2 prints, ~Aug-2026. See §8 Refresh Protocol.
>
> **Last ad-hoc pass:** **2026-09-10** (2nd ad-hoc, live-data — see the dated section immediately below). Prior: 2026-07-10 (ledger-hygiene only, no web data) — 7 predictions **dispositioned** (§4; ledger `workbook/PREDICTIONS.tsv`), FLOW-numbering divergence **reconciled** (§2c, TSV wins). See §9 change history.
>
> **⚠️ Vintage warning.** The legacy identity surfaces (CLAUDE.md, STATUS.md) are FROZEN at their Apr-2026 build vintage and carry a Klarna narrative that has since been **REFUTED at parent** (Klarna Q1-2026 profitable, CARL May-14). Do not cite any "Current" value in this dossier as live — see §6 SUPERSEDED AT PARENT.

---

## 2026-09-10 pass (2nd ad-hoc, +62d) — WQ-209, PROME-spawned under CARL's card
*Live-data pass. Every figure primary or named-secondary, each dated. **Predictions re-marked, NOT resolved — CARL disposes (§8.4).** `COCKROACH.tsv` + `REGULATORY.tsv` unfrozen per their own dated trigger (docket row 2026-09-08); DATA clock advanced 2026-07-10 → 2026-09-10. Full dispositions + gaps: `outbox/2026-09-10_PHAN-to-CARL_dossier-pass.md`.*

| Gate print | Volume | Headline credit | The leg that actually matters |
|---|---|---|---|
| **Affirm FQ4-26** — 10-K FYE 2026-06-30, filed 2026-08-27 (SEC XBRL, primary) | GMV **$50.2B FY26, +37% YoY**; Q4 $14.1B, +36% | 30+ DQ ex-Peloton **2.5% @ 6/30/26** — *down* from the 2.7–2.8% of the prior three quarters, *up* from **2.3%** a year earlier | **Allowance $563.3M = 5.89% of loans HFI vs 5.65% FY25 (+24bp)** while loans HFI grew +36.1% to $9.561B. Provision **$796.7M vs $616.7M = +29.2%**. NCOs **$611.6M vs $500.8M = +22.1%** |
| **Klarna Q2-26** — press release 2026-08-18 (primary) | GMV **$36.6B, +18% YoY** (U.S. +27%) | Provisions **0.52% of GMV** vs 0.56% Q2-25; U.S. Fair Financing 30+ DPD **−20bp QoQ** | Net income **+$9M** (vs −$53M Q2-25); FY26 GMV guide **CUT to $149–151B** from >$155B |

⚠️ **FLOW-PHAN-06 DOWNGRADED — trigger ACTIVE → PARTIAL (1 of 2 legs).** The 7/10 trigger sentence (*"provisions +40% YoY vs DQ improvement"*) does not survive a named basis: FY26 provision **+29.2% is BELOW GMV +37% and below loans +36.1%**. What survives is the **allowance-RATE** leg (5.65% → 5.89%) — forward expected loss per dollar of book rose while the headline DQ fell. `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` — never quote "provisions outpacing volume" without saying *vs GMV or vs loans, Q4 or FY*. Q4-only provision growth is reported at **+42%** but that is **SECONDARY** (analyst read of the supplement); ⛔ **SEARCH-NOT-FOUND — the primary `Affirm FY Q4 2026 Earnings Supplement, August 27 2026` (`investors.affirm.com/static-files/c160ce8f-a9b5-4896-b8ed-6544ac430809`) timed out on two fetch attempts; all FY figures above come from the 10-K XBRL instead.**

🔴 **The biggest item this pass is not a BNPL print — it is an instrument refutation sitting under CARL's own threshold.** NY Fed Liberty Street Economics, Aug-2026, *"How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures"*: the credit-card 90+ **STOCK** delinquency rate (12.8%, vs 7.6% in Q3-2022) is driven by charged-off balances **staying on credit reports longer** — only ~**40%** of borrowers' charged-off debts were still being reported one year later in 2004–2012, **80% by 2024**. Exclude charged-off balances and the stock rate **"falls in line with both our flow delinquency rate and the Call Report delinquency rate"**; the flow rate is *"elevated but has been largely stable since 2024."* ⇒ **CRL-05 (CC 90+ DQ vs the 13.74% GFC peak) is instrumented on a series whose rise is substantially a reporting-DURATION artifact, not incidence.** This inverts PHAN's own framing in one direction and confirms it in the other: BNPL **under**-reports obligations, while the bureau stock series **over**-reports realized stress. **CARL must grade it; it belongs in RED's counter-log.** `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`

| Threshold (§3 row) | 7/10 vintage | **9/10 live** | Band |
|---|---|---|---|
| BNPL late-payment rate | 34–41% (ABA 2024) | **47%** — 34% ('24) → 41% ('25) → **47% ('26)** [LendingTree BNPL Tracker, n=2,060, fielded 3/17–23/26, pub 8/19/26] | 🟠 → 🔴 **FIRST RED BREACH (>45%)** |
| BNPL stacking, 2+ at once | 63% (CFPB Jan-25) | **63%** flat; **25% hold 3+** (was 23%) [LendingTree, n=2,049, fielded 3/3–6/26] | 🔴 held — **P01's >70% not reached** |
| Affirm 30+ DQ | 2.3% (Q4 FY25) | **2.5%** @ 6/30/26 | 🟢 under the >3% yellow |
| Klarna credit-loss provision | 0.65% (Q4-25) | **0.52% of GMV** (Q2-26) | 🟢 under the >0.60% yellow |
| Fintech failures (cumulative) | 3 | **3 — explicit DID_NOT_APPEAR null** (Parker Ch-7 5/7/26 = B2B, out of scope per 7/10; Solid Ch-11 = Apr-**2025**, pre-window; BlockFills = crypto) | 🟠 unchanged |
| Phantom-DTI gap | ~12pp | **not refreshed** — ⛔ SEARCH-NOT-FOUND: any *2026 FHA Mortgagee Letter or HUD final guidance on BNPL*. The 2025-06-24 RFI's comment period closed **2025-08-25**; nothing issued since | 🟠 carried, stale |

**Transmission into CARL's consumer thesis (the finding, not a restatement).** BNPL is now load-bearing for **necessities**: **54% of users agree they need these loans "to make ends meet"** (62% of parents with children <18, 59% of millennials), **29% have used BNPL for groceries** (25% in '25, **14% in '24**), 13% for rent [LendingTree, n=2,049, fielded 3/3–6/26]. That is the same bottom-cohort the **$4.146 pump** (CARL 9/5) and the food/tariff squeeze run through. ⭐ **The load-bearing point for the thesis: the late rate went 41% → 47% across a year in which payrolls were REVISED UP (July −23K → +21K, BLS 9/4) and LABOR's T-03 did not fire.** Shadow-layer deterioration is **not waiting on an employment break** — that is the rot-not-detonator reading of "Beneath the Ice," evidenced on a series CARL does not currently carry. It cuts the other way too: **V16's drop-back branch can resolve DOWN at the ~10/2 NFP and this series would still be deteriorating**, so the branch is not a referendum on the consumer leg.

**Also moved:** **P07 → 88% (trending HIT)** — **Colorado AG Weiser sued Activehours Inc. d/b/a EarnIn on 2026-08-27** (3.1M CO transactions Jan-2023→Jul-2025, ~$300M advanced, >$16M collected in tips + expedited-transfer fees, **average APR ~388%**); narrow state-AG count now **NY + MN + DC + CO = 4 of 5**, 3.7 months of window left. **P04 → 12% · P05 → 15% · P02 → 2% (recommend MISS at FY-close) · P03 → 97% · P01 → 25%.** **Furnishing moved:** Affirm now furnishes all pay-over-time products to **Experian and TransUnion** (loans issued from 4/1/25 and 5/1/25 respectively) — the §2a *"only Affirm reports, 2 of 3"* line is still directionally right but is no longer a static fact. **Klarna's U.S. pay-in-4 furnishing is CONTRADICTORY across secondary sources — UNKNOWN, do not cite either way.**

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

*Carried from STATUS.md:110-121 + CLAUDE.md:54-58,144. This is PHAN's core original framework. **`[as-of Apr-2026 unless noted]`** — the gap structure is durable, but the point-in-time claims below (11.52% FHA DQ, "lenders now scanning," "only Affirm reports") are build-vintage; verify at parent before citing as current.*

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

> **✅ Numbering RECONCILED (2026-07-10 ad-hoc pass) — TSV numbering WINS.** The `workbook/FLOW.tsv` scheme is canonical: it carries the breakpoint/lag/mechanism columns and the complete 6-pathway set, so the dossier and all pointers cite **TSV IDs only**. The legacy STATUS.md:161-195 prose used a *shorter, divergent* numbering; crosswalk of the divergent prose IDs → canonical TSV IDs:
>
> | Frozen STATUS prose ID | Prose name | → Canonical TSV ID |
> |---|---|---|
> | FLOW-PHAN-01 | Shadow → Visible Credit Cascade | FLOW-PHAN-01 (agree) |
> | FLOW-PHAN-02 | BNPL Stacking Cascade | FLOW-PHAN-02 (agree) |
> | FLOW-PHAN-03 | Cockroach Cascade | **FLOW-PHAN-04** (Fintech Cockroach Cascade) — *renumbered* |
> | FLOW-PHAN-04 | Phantom DTI → Mortgage Surprise | **no TSV ID** — distinct pathway, preserved as the §2a framework (not a canonical FLOW row) |
>
> TSV FLOW-PHAN-03 (Payday Debt Trap), -05 (PHAN-to-CARL), -06 (Composition-Masking) have **no prose twin** — prose-only readers were missing three pathways. Basis for TSV winning: it is the more complete and structurally richer surface. The TSV is **not** renumbered (per demotion terms); the frozen STATUS prose stands as-is under its FROZEN banner — this crosswalk is the reconciliation of record. Cite TSV IDs going forward.

---

## 3. Thresholds (bands durable; "Current" = build-vintage snapshot, not live)

*Carried from CLAUDE.md:61-69. Bands + sources are durable. The original "Current" column was hardcoded in the instructions file and rots independently of STATUS (DAEDALUS audit finding). Each snapshot value below is **re-labeled as a build-vintage reading with its as-of date** — none is live.*

| Metric | Snapshot value (as-of) | Yellow | Orange | Red | Source |
|---|---|---|---|---|---|
| BNPL Stacking | 63% *(CFPB Jan-2025)* | >35% | >45% | >55% ✅ | CFPB |
| Cross-Firm Stacking | 32% *(CFPB Jan-2025)* | >20% | >25% ✅ | >35% | CFPB |
| Affirm 30+ DQ | 2.3% *(Affirm Q4 FY25, 2025-09-30)* ⚠§6 | >3% | >4% | >6% | Affirm SEC |
| Klarna Credit Loss Provision | 0.65% *(Klarna Q4-25, 2025-12-31)* ⚠**REFUTED §6** | >0.60% ✅ | >0.80% | >1.0% | Klarna 20-F |
| BNPL Late Payment Rate | **47% (2026)** — 34% ('24) → 41% ('25) → **47% ('26)** | >25% | >35% | **>45% 🔴 BREACHED 2026-08-19 (first time)** | **LendingTree BNPL Tracker** *(⚠️ source corrected at the parent 2026-09-10: the band cell said **ABA** and the parent STATUS row said **CFPB**; the reachable 34/41/47 SERIES is LendingTree's, and CARL's KB-CARL-028 credits the 34→41 step to the Richmond Fed. Three surfaces, three different named sources, one survey house. Cite LendingTree.)* |
| Fintech Failures (cumulative) | 3 *(CURO/Tricolor/Synapse, ≤Apr-2026)* | 2 | 3 ✅ | 5+ | Public |
| Phantom DTI Gap | ~12pp *(35%→47%, CARL est)* | >5pp | >10pp ✅ | >15pp | CARL est |

> ✅ marks the band the snapshot value had tripped **at build vintage**. These check-marks are frozen — re-evaluate against live parent data before citing any as "breached now."
>
> ⚠️ **REFRESHED 2026-09-10 — five of seven rows have live 9/10 readings; see the `2026-09-10 pass` section at the top of this file for the sourced values.** Headline moves: **BNPL late-payment rate 34-41% → 47% = FIRST RED-band breach (>45%)**; Affirm 30+ DQ 2.3% → **2.5%** (green); Klarna provision 0.65% → **0.52% of GMV** (green); stacking **63% flat**; fintech failures **3, explicit DID_NOT_APPEAR null**. Phantom-DTI gap **not refreshed** (no HUD/FHA guidance exists to measure it against).

---

## 4. Open predictions (7 rows — DISPOSITIONED 2026-07-10 ad-hoc pass)

*Carried from `workbook/PREDICTIONS.tsv` (the ledger of record — this table mirrors it). All 7 made 2026-04-09 (P03/P07 confidence-upgraded Apr-17). **Dispositioned 2026-07-10** by a CARL-directed ad-hoc pass, evidence-gated to own files + CARL parent STATUS/KB/CHANGELOG (no web pulls). **All 2026 windows are still open**, so no clean HIT/MISS is possible (year not closed); the pass re-marks confidence where a premise moved, notes each success/failure mode, and flags DATA-NEEDED where resolution requires a not-yet-published figure. Next data event: Affirm/Klarna Q2 ~Aug (ad-hoc spawn trigger, §8).*

| # | Prediction | Conf (Apr → 7/10) | Timeframe | Verdict + basis (2026-07-10) |
|---|---|---|---|---|
| **PHAN-P01** | BNPL stacking >70% | 60% → 60% | H2 2026 | **OPEN** — H2 window just opened; no fresh stacking print in-file (63% at build). DATA-NEEDED: BNPL stacking update H2 2026 |
| **PHAN-P02** | Klarna credit losses >1.0% | 65% → 12% → **6%** | FY2026 | **MIXED (MISS-lean hardened)** — premise REFUTED (Klarna Q1-2026 profitable) **+ Q1 actual provision 0.55% of GMV** (reported May-18) is below even the 0.80% band → >1.0% remote. DATA-NEEDED: Q2 provision ~Aug-20 |
| **PHAN-P03** | CFPB 1033 enforcement delayed beyond 2026 | 90% → **96%** | EOY 2026 | **OPEN — tracking HIT** — mechanism LOCKED (REGULATORY.tsv 2026-04-01 WITHDRAWAL; 2026 enforcement essentially impossible). Formal resolution EOY 2026 |
| **PHAN-P04** | At least 2 more fintech failures | 60% → **45%** | 2026 | **OPEN** — 0 confirmed NEW 2026 *failures* in-file (FloatMe/Current = distress/investigations, not failures); half the window elapsed at zero. DATA-NEEDED: H2-2026 failure confirmations |
| **PHAN-P05** | BNPL-linked mortgage defaults identifiable in FHA data | 50% → **40%** | Q3–Q4 2026 | **OPEN** — window just opened; parent notes HUD BNPL RFI **STALLED** (no final guidance) → identifiability delayed. DATA-NEEDED: FHA/HUD BNPL-attribution data |
| **PHAN-P06** | NY passes first comprehensive BNPL licensing law | 55% → n/a | 2026 | **MIXED — fact TRUE, no forecasting credit** — NY BNPL Act was **SIGNED 2025-05-09** (predates the 4/9 forecast; authored blind to it). DFS rules proposed 2026-02-23. New calibration mode: authored-blind-to-existing-fact |
| **PHAN-P07** | Cash-advance AG enforcement expands to 5+ states | 75% → **80%** | 2026 | **OPEN — trending HIT** — **Minnesota AG sued Brigit 2026-06-10** → narrow count NY+MN+DC ≈ 3; court rulings vs EWA in 7 states; wave accelerating. DATA-NEEDED: state-AG count H2 2026 |

> **⚠️ RE-MARKED 2026-09-10 (2nd ad-hoc pass, live data). Confidence moved on six of seven rows; NONE resolved here — CARL disposes (§8.4). Ledger of record `workbook/PREDICTIONS.tsv` carries the full dated notes.**
>
> | # | 7/10 | **9/10** | One-line basis |
> |---|---|---|---|
> | P01 stacking >70% | 60% | **25%** | 63% flat across two independent vintages (CFPB Jan-25, LendingTree Mar-26); H2 window ~2/3 elapsed with no series trending to 70% |
> | P02 Klarna losses >1.0% | 6% | **2%** — *recommend CARL resolve **MISS** at FY-close* | Two 2026 quarters printed **0.55% then 0.52% of GMV, both falling** — roughly half the threshold, with Klarna profitable in both |
> | P03 1033 delayed past 2026 | 96% | **97%** — tracking HIT | Rule still enjoined and under agency reconsideration; no 2026 enforcement path exists. ⚠️ **UNRESOLVED CONFLICT:** one secondary tracker says CFPB *withdrew* its vacatur request and reopened rulemaking rather than vacating — this does **not** change the verdict but does contradict the framing of our own 2026-04-01 WITHDRAWAL row. ⛔ SEARCH-NOT-FOUND: `openbankingtracker.com/guides/section-1033-status` returned HTTP 429 on fetch |
> | P04 ≥2 new fintech failures | 45% | **12%** | Zero in-scope **consumer** fintech failures in 8.3 of 12 months (see the DID_NOT_APPEAR null in `COCKROACH.tsv`) |
> | P05 BNPL-linked FHA defaults identifiable | 40% | **15%** | No FHA guidance, no furnishing mandate, window half elapsed — **the data required to identify them does not exist**, so the prediction cannot come true on schedule regardless of the underlying stress |
> | P06 NY BNPL licensing law | MIXED | **MIXED (unchanged)** | Resolved 7/10; no new information |
> | P07 AG enforcement ≥5 states | 80% | **88%** — trending HIT | **Colorado AG sued EarnIn 2026-08-27** ⇒ narrow count NY+MN+DC+CO = **4 of 5**, 3.7 months left |

> **Calibration modes logged (per row, in TSV Notes):** P02 = premise-refutation (built on a losing-Klarna prior parent overturned); P04 = distress≠failure discriminator; P05 = RFI-awareness ≠ data-availability; P06 = proposed≠passed; P07 = definitional-precision (AG-enforcement vs state-laws not disambiguated at authoring). P01/P03 unresolvable-in-file (window open / durable regulatory fact).

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
| **Affirm quarterlies** (GMV, DQ, provisions, ABS FICO) | 2.3% DQ, $214.2M provisions (+40% YoY), ABS WA FICO 672, GMV $13.8B | **KB-CARL-228 + CARL `workbook/BNPL_STRESS.tsv`** canonical. *[2026-07-10 news sweep found fresher Q1-2026 actuals: 30+ DPD **2.8%** (flat YoY), allowance $512M = **6.0%** of loans HFI — route to CARL for KB-228]* |
| **Klarna quarterlies** (provisions, revenue, class action) | 0.65% provisions, $1.08B rev, case 25-cv-07033 | **KB-CARL-228 + `BNPL_STRESS.tsv`** canonical. *[2026-07-10 news sweep: Q1-2026 provision **0.55% of GMV** (reported May-18), US 30+ DPD improved 36bps from Q2-25 peak, profitable — route to CARL]* |
| **BNPL late-payment rate** | **47% (2026, LendingTree Tracker pub 2026-08-19)** | ✅ **Verified and superseded at the parent 2026-09-10** — STATUS row updated 41%→47%, band **🔴 breached**, attribution corrected off CFPB. KB-CARL-439. |
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

**Catalyst cadence:** Affirm FY Q3 ~May, Q4 ~Aug; Klarna quarterly ~mid-quarter-close+6wk. **Next natural refresh trigger:** **Affirm FQ4-2026 earnings CONFIRMED 2026-08-20 after close** (TipRanks/MarketBeat, news sweep 7/10); Klarna Q2 ~mid-Aug. *(Supersedes the earlier "~Aug-13" estimate.)*

---

## 8. Refresh protocol (how an ad-hoc spawn uses this dossier)

A CARL-directed ad-hoc spawn against the phantom-debt domain should:

1. **Read this DOSSIER** (not the frozen CLAUDE.md/STATUS.md) for framework, thresholds, open predictions, and the two live ledgers.
2. **Append new events to the live TSVs only** — `workbook/COCKROACH.tsv` (new failures/distress/class actions) and `workbook/REGULATORY.tsv` (new EWA laws, AG actions, 1033 developments). Do not revive the frozen TSVs.
3. **Update the as-of stamps** in §3 (thresholds) and §6 (superseded) if a value the dossier snapshots gets a fresh parent reading.
4. **Resolve predictions at CARL, not here** — if a §4 prediction resolves, flag the outcome to CARL parent (CARL owns the resolution; this dossier's §4 stays ⚠ UNRESOLVED until CARL records it). Per DAEDALUS audit, no sub-agent due-scan machinery reaches these — resolution is a deliberate spawn action.
5. **Route findings to CARL** via the normal SV/handoff channel; CARL's `BNPL_STRESS.tsv` + KB-CARL-228 remain the system of record for Affirm/Klarna quarterlies.

---

## 9. Change history (ad-hoc pass log)

| Date | Pass | What changed |
|---|---|---|
| **2026-07-10** | **DOSSIER assembly** (MOLD / DAEDALUS editor) | Dossier assembled from PHAN's Apr-2026 frozen surfaces (transcription-with-provenance, no new analysis). Legacy CLAUDE.md/STATUS.md frozen same day; COCKROACH.tsv + REGULATORY.tsv kept live. |
| **2026-07-10** | **1st ad-hoc pass** (CARL-directed, ledger-hygiene only, no web data) | **(1)** 7 predictions dispositioned (§4 + `workbook/PREDICTIONS.tsv`): all 2026 windows still open → P02 **MIXED** (premise refuted, Klarna Q1 profitable), P03 re-marked 90%→96% (tracking-HIT, 1033 withdrawn), P04 60%→45%, P05 50%→40%, P06/P07 held, P01 held; calibration mode logged per row. **(2)** FLOW-numbering divergence (§2c) **reconciled — TSV numbering wins** (canonical crosswalk added; prose FLOW-PHAN-03→TSV-04, prose FLOW-PHAN-04→§2a framework/no TSV ID); TSV not renumbered. **(3)** Live ledgers COCKROACH.tsv + REGULATORY.tsv verified readable, headers clean, untouched. Header + §4 truth-stamped. |
| **2026-07-10** | **Staleness sweep** (CARL-directed, tag-don't-refresh, no web) | 6 rows STALE-tagged: 4 REGULATORY (1033 arc superseded by 4/1 WITHDRAWAL; HUD RFI ACTIVE vs parent STALLED) + 2 COCKROACH (both Klarna rows, deterioration REFUTED). §2a given `[as-of Apr-2026]` section tag. Retirement candidates listed (SCHEMA.tsv; CARL_HANDOFF — keep, load-bearing). |
| **2026-09-10** | **2nd ad-hoc pass** (WQ-209, PROME-spawned under CARL's card; live data, +62d since 7/10) | **(1)** Dated `2026-09-10 pass` section added at top — Affirm FQ4-26 + Klarna Q2-26 both worked from primaries (Affirm 10-K XBRL; Klarna press release). **(2)** 🔴 **FLOW-PHAN-06 trigger DOWNGRADED ACTIVE → PARTIAL (1 of 2 legs)** — FY26 provision +29.2% is *below* GMV +37%; only the allowance-RATE leg (5.65%→5.89%) survives. **(3)** 🔴 **NY Fed Liberty Street (Aug-26) refutes the basis of CARL's CC 90+ instrument** — the stock rate's rise is substantially a charge-off REPORTING-DURATION artifact (40%→80% still reported at 1yr, 2004-12 vs 2024); routed to CARL + RED. **(4)** §3 refreshed: **BNPL late rate 41% → 47% = first RED-band breach**; Affirm DQ 2.5%; Klarna 0.52%; stacking 63% flat. **(5)** Six predictions re-marked (§4), none resolved. **(6)** `COCKROACH.tsv` + `REGULATORY.tsv` **UNFROZEN per their own dated trigger**, +1 event row each, **explicit DID_NOT_APPEAR null recorded for new consumer-fintech failures**, DATA clock advanced to 2026-09-10. **(7)** Inbox drained: **empty (0 packets) — a true null, recorded**. |
| **2026-07-10** | **News sweep** (CARL-directed, web, last-30d) — SV-PHAN-2026-07-10-01 | **P06 CORRECTED** → MIXED: NY BNPL Act **SIGNED 2025-05-09** (predates the forecast → authored-blind-to-existing-fact); DFS rules proposed 2026-02-23 — REGULATORY.tsv +2 corrective rows, old 4/9 row STALE-tagged. **P07 → 80% trending HIT**: Minnesota AG v. Brigit 2026-06-10 (adds MN to NY/DC) — REGULATORY.tsv +1 row. **P02 → 6%**: Klarna Q1-2026 provision 0.55% GMV (May-18). **Affirm/Klarna Q1 actuals** (2.8% DQ/$512M; 0.55%) routed to CARL KB-228 (§6). **P04:** Parker/Hokodo 2026 failures found but B2B/out-of-consumer-scope → not counted, not appended. Furnishing≠visibility (Senate probe May-2026) reinforces P03/§2a. Affirm FQ4 earnings confirmed **2026-08-20** (§8). All figures year-verified 2026. |

---

*PHAN dossier assembled 2026-07-10 by MOLD (DAEDALUS editor), from PHAN's Apr-2026 frozen surfaces. Transcription-with-provenance — no new analysis. Legacy identity surfaces (CLAUDE.md, STATUS.md) frozen same day; COCKROACH.tsv + REGULATORY.tsv stay live. Provenance and refutations per DAEDALUS audit `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`. Predictions dispositioned + FLOW numbering reconciled 2026-07-10 (§9).*
