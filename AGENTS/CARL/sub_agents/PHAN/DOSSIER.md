# PHAN DOSSIER — Phantom Debt & Shadow Credit

> **What this is.** PHAN (Phantom Debt / Shadow Credit monitor) was **demoted from full sub-agent to dossier on 2026-07-10** (DAEDALUS CARL sub-agent audit, Will-approved). This file is the **single entry surface** for the phantom-debt domain going forward. It is not a live dashboard: it carries PHAN's durable analytical assets (frameworks, thresholds, open predictions, transmission pathways) at their original vintages, each fact stamped with its own as-of date and file:line origin. No new analysis is authored here — this is transcription-with-provenance.
>
> **Domain scope** *(carried from CLAUDE.md:5,7)*: phantom debt / shadow credit — consumer borrowing invisible to credit bureaus. ⛔ **The legacy `$400B+` figure in this line is REFUTED — see §2a: ~$176–216B broad, ~$30–60B credit-only, medical ~85% of it.** BNPL stacking, cash-advance / earned-wage-access (EWA) apps, fintech-lender ("cockroach") health, regulatory visibility changes (CFPB 1033), and phantom-DTI impact on mortgage underwriting (→ HOMER).
>
> **Refresh model.** No standing sessions. Refreshed by **ad-hoc CARL spawns** against this dossier (per CARL SPAWN_PROTOCOL templates). **Next natural catalyst / ad-hoc spawn trigger:** **Affirm FQ1-27 + Klarna Q3-26, ~2026-11-05 to 11-20** — the last pass before five PHAN rows come due 12/31. *(The Aug-2026 Q2 trigger this line used to name FIRED and was worked on 9/10.)* See §8.
>
> **Last ad-hoc pass:** **2026-09-11** — three passes in one day: (3rd) closed the 9/10 SEARCH-NOT-FOUND gaps and **restored FLOW-PHAN-06 to ACTIVE**; (4th) a **domain news sweep** that filled the ABS leg-2 gap and found two bank-contagion cockroaches the fleet did not have; (5th) **the §2 FRAMEWORK REBUILD — `$400B+` retired, `FRAMEWORKS.md` created**, discharging a CARL assignment 42 days late. Prior: **2026-09-10** (2nd ad-hoc, live-data). **⚠️ Dated pass narratives now live in `PASSES.md` — grep it, do not read it whole (read-cap split, 9/11).** Prior: 2026-07-10 (ledger-hygiene only, no web data) — 7 predictions **dispositioned** (§4; ledger `workbook/PREDICTIONS.tsv`), FLOW-numbering divergence **reconciled** (§2c, TSV wins). See §9 change history.
>
> **⚠️ Vintage warning.** The legacy identity surfaces (CLAUDE.md, STATUS.md) are FROZEN at their Apr-2026 build vintage and carry **TWO refuted claims, not one**: ① the Klarna deterioration narrative (**REFUTED** — Klarna Q1-2026 profitable, CARL May-14) and ② **the `$400B+` phantom-debt headline, which those files assert 9 times and which is REFUTED by `KB-CARL-367` (~$176–216B broad / ~$30–60B credit-only).** Because they are frozen they are **not** being edited; this banner is the maintained correction. **⛔ Do not lift the domain-scope, "Why This Domain Matters", or "Key Concepts" magnitude lines from CLAUDE.md, nor the STATUS.md masthead/§BNPL Outstanding rows.** See §2a and §6.

---

## CURRENT STATE — as of 2026-09-11 (3rd ad-hoc pass)

*Headline state only. **Reasoning, sourcing and the superseded calls live in `PASSES.md` — grep it, never read it whole.** Predictions: `workbook/PREDICTIONS.tsv` is the ledger of record; §4 mirrors it. **PHAN proposes, CARL disposes.***

| Threshold (§3) | Live | Band | Vintage |
|---|---|---|---|
| BNPL late-payment rate | **47%** (34 '24 → 41 '25 → 47 '26) | 🔴 **RED breach, first ever** (>45%) | LendingTree Tracker, n=2,060, fielded 3/17–23/26, pub 8/19/26 |
| BNPL stacking, 2+ at once | **63%** flat; 25% hold 3+ | 🔴 held — P01's >70% not reached | LendingTree, n=2,049, fielded 3/3–6/26 |
| Affirm 30+ DQ (ex-Peloton) | **2.5%** @ 6/30/26 | 🟢 under >3% yellow | Affirm 10-K, filed 8/27/26 |
| Klarna credit-loss provision | **0.52%** of GMV | 🟢 under >0.60% yellow | Klarna Q2-26 release, 8/18/26 |
| Fintech failures (cumulative) | **3** — explicit DID_NOT_APPEAR null | 🟠 unchanged | `COCKROACH.tsv` |
| Phantom-DTI gap | ~12pp — **NOT refreshed** | 🟠 carried, stale | no HUD/FHA BNPL guidance exists to measure against |

**🔴 FLOW-PHAN-06 trigger = ACTIVE** (restored 9/11 — the 9/10 PARTIAL was a **period-basis error**: a quarterly trigger tested on an FY aggregate). Quarterly provision YoY **+1.8% → +40.0% → +33.5% → +42.5%**, Q4 beating Q4 GMV by 6.5pp; **NCO YoY accelerating monotonically +12.6→+16.5→+22.2→+36.9% while headline DQ FELL** — the stronger evidence, and not in the trigger. ⚠️ **BREAKPOINT NOT MET, do not let ACTIVE travel as breakpoint-fired:** leg 2 (ABS WA FICO) **weakly met at best** — 670 vs 672, but Grade-A share ROSE and CE FELL at every class, opposite the routing prediction; leg 3 (gas >$4.50) not met. ⛔ Never splice the amortizing shelf's 681 into the revolving series. ✅ **ACCEPTED BY CARL 2026-09-11** (`KB-CARL-458`, commit `a585b5ccf`) — CARL re-verified FQ1–FQ3 independently at SEC XBRL and restored the trigger. ⚠️ **FQ4 +42.5% is labelled PHAN-DERIVED, not CARL-verified**: Affirm's fiscal Q4 has no standalone XBRL duration frame, so it exists only by differencing FY against the nine-month. **Two CARL-verified quarters above the bar, not three — do not report three.** CARL is taking the **NCO re-instrumentation** to the ~11/12 gate as a spec change rather than deciding it at closeout. *Detail → `FRAMEWORKS.md` §2.6.*

**🔴 Instrument refutation standing at parent (9/10):** NY Fed Liberty Street 8/11 showed CARL's CC 90+ **stock** series rises substantially on charge-off **reporting duration** (40%→80% still-reported at 1yr). CARL closed **CRL-05 `NO-VERDICT-BY-BASIS`** and registered **CRL-30** on the flow rate. ⛔ **Never re-arm anything on 13.74%.**

**Predictions (none resolved here):** P01 25% · P02 **2%, MISS-at-FY-close recommended, disposition still owed at CARL** · P03 **98%** tracking HIT · P04 12% · P05 15% · P06 MIXED · P07 88% trending HIT (state-AG count **4 of 5**: NY+MN+DC+CO).

**Two live corrections to carry:** ① the **38% BNPL-for-gasoline** figure is **Protect Borrowers / Data for Progress** (n=438 likely voters, fielded 7/2–5/26) — ⛔ **never merged into the LendingTree series**, which publishes no gasoline figure and reads groceries **29%** where PB reads **46%**. ② Rule 1033 is **ENJOINED + UNDER RECONSIDERATION**, not agency-withdrawn — a rewritten, fee-permissive rule is a live 2027+ branch that our old "EFFECTIVELY DEAD" framing (still carried verbatim in §2b by audit design) concealed.

**🟠 Two new DISTRESS entries (9/11 PM sweep) — first bank contagion since Tricolor, and the fleet had ZERO coverage of either:** **LendingPoint** (KBRA cut six classes May-26; MidCap marked $40.2M vs $63.2M cost) and **Coastal Financial (CCB/CCBX)** — Q2-26 net loss **$42.1M** on a **$68.8M credit expense** for *"a single, isolated CCBX partner relationship"*; stock **−43.5% in one session**. ⚠️ The LendingPoint↔Coastal link is **named by Fintech Business Weekly, NOT company-confirmed**. **Both DISTRESS, not FAILURE — count stays 3, P04 stays 12%.** → CARL to route REGINALD/LIQUID via WALTER. *Rows → `COCKROACH.tsv`.*

**⚠️ Counter-thesis (route to RED):** **FICO Score 10 BNPL** — in FICO's own testing, users with 5+ Affirm loans typically saw scores **increase or stay stable**. If crossing the scoring layer *raises* scores, the visibility shock is a non-event. **Third independent hit on the transmission premise** — with the NBER medical-debt RD and Richmond Fed. *→ `FRAMEWORKS.md` §2.4.*

**Next gate: ~2026-11-05 to 11-20** — Affirm FQ1-27 + Klarna Q3-26. The last pass before five PHAN rows come due 12/31.

### 📌 OWED / ASSIGNED WORK — check this block at every boot

*Created 2026-09-11 because the §2 rebuild sat **42 days** unseen: CARL assigned it in its own KB Notes column (`KB-CARL-367`), a surface no PHAN session reads. **An obligation recorded where the obligee does not travel is not an obligation.** `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`*

| Item | Owner | Raised | State |
|---|---|---|---|
| **§2 framework rebuild** (phantom-debt magnitude/composition) | PHAN | 2026-07-31 (`KB-CARL-367`) | ✅ **DONE 2026-09-11** — `FRAMEWORKS.md` |
| **Closeout protocol rebuild** (no git step; frozen/dead targets) | PHAN | 2026-09-11 | ✅ **DONE 2026-09-11** — §8 |
| **Is longer-term BNPL already in the aggregates?** (~$16B of ~$29B BNPL central) | PHAN | 2026-07-28 (DEWEY C4) | 🔻 **OPEN — top research item for the ~11/12 gate** |
| **Consolidated transmission-premise memo → RED** (3 independent hits) | PHAN | 2026-09-11 | 🔻 **OPEN** |
| **ABS tracking series** (WA FICO + grade mix + CE per deal — leg 2 has no instrument) | PHAN | 2026-09-11 | 🔻 **OPEN** |
| **P02 resolve MISS at FY-close** (recommended 9/10) | **CARL** | 2026-09-10 | ⏳ awaiting CARL |
| **P04 successor proposal** (failure-count measures a legal event, not the mechanism) | PHAN→CARL | 2026-09-11 | 🔻 **OPEN** |
| **Route CARL→PHAN assignments as inbox packets, not KB Notes** | **CARL/Will** | 2026-09-11 | ⏳ recommended — `FRAMEWORKS.md` §2.8 |
| **Sub-agent closeout template has no git step** (all 7) | **CARL** | 2026-09-11 | 📤 **packet sent** — I cannot edit sibling agents |
| **`read_cap_check.py` cannot evaluate sub-agents** (7 invisible) | **DAEDALUS** | 2026-09-11 | 📤 **packet sent** |
| **FLOW-PHAN-06 → re-instrument onto NCO growth?** | **CARL** | 2026-09-11 | ⏳ CARL taking it to the ~11/12 gate (spec change, needs a sitting) |
| **⚠️ CARL records ABS WA FICO as "untested since 672"** — the **PM sweep packet fills it** (670, AFRMT 2026-4/5) and is **unprocessed in CARL's inbox** | **CARL** | 2026-09-11 | ⏳ PRIORITY-1 next CARL session |

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

## 2. Frameworks — ⚠️ REBUILT 2026-09-11 · full text now in **`FRAMEWORKS.md`**

*The durable analytical assets — the reason PHAN survives as a dossier. **Rebuilt 2026-09-11 against `AGENTS/DEWEY/output/2026-07-28_c4-phantom-debt-magnitude.md` (→ `KB-CARL-367`), discharging an obligation CARL assigned on 2026-07-31 that ran 42 days late.** The section roughly doubled and moved to **`FRAMEWORKS.md`** (same directory) under the read cap. Summary below is load-bearing; detail, sourcing and the de-double-counting rules are there.*

### ⛔ 2a. The headline number changed — `$400B+` is DEAD

| Definition | Total | Composition |
|---|---|---|
| **BROAD** (incl. provider-held unpaid medical bills) | **~$176–216B** (central ~$195B) | **medical ~85% · BNPL ~15% · EWA negligible** |
| **CREDIT-ONLY** (excl. unpaid bills — *bills are not credit*) | **~$30–60B** | BNPL-dominant |

**Lead with the FORK, never a point estimate — the definition moves the answer ~4×, far more than the estimation error.** Inside BNPL a second fork moves it **8×** (broad $25–33B vs pay-in-4-only $3.6–4.8B). ⭐ **Prefer the CFPB FLOW gap over any stock estimate: ~$80.46B/yr accruing vs ~$36B/yr reaching reports = a ~2.2× invisibility rate**, co-vintaged, single primary [90 FR 3276, 2025-01-14]. ⚠️ *Anyone quoting a "2026 phantom debt number" is quoting 2021–2023 data.*

⛔ **`"bottom-60 leverage 20–30% higher than reported"` — NOT SUPPORTED.** Against the correct unsecured base ($1.812T card+other) the broad figure gives **~11%**, credit-only **~2.5%**. ✅ **Revised: 5–20%**, and the upper half requires counting unpaid medical bills as debt. *(Quoting phantom debt against **total household debt** understates the ratio **10.4×** — 72.5% of that denominator is mortgages.)*

### ⭐ 2b. The four visibility layers — visibility is NOT binary

**furnished → in the core file → in Equifax (what the QHDC reads) → scored.** Four independently binding gates: a loan can be furnished and still be absent from every aggregate statistic *and* invisible to underwriting. **Essentially all BNPL clears layer 1 and fails layer 4.**

- **Affirm:** furnishes all products to **Experian + TransUnion**, **not Equifax** *(probable)* ⇒ its **~$16.5–17.5B — the largest book — likely never reaches the QHDC.**
- ✅ **Klarna (resolves the 9/10 UNKNOWN): term loans ONLY, explicitly NOT pay-in-4**; verbatim *"no impact on your FICO / Vantage score… visible only to you."*
- ⛔ **You cannot use one furnishing list for both operations** — "invisible to the QHDC" needs the *Equifax* list, "invisible to lenders" a different one. PHAN's old *"only Affirm reports, 2 of 3"* line is a **layer-1 fact carrying a layer-3/4 implication**.

### ⚠️ 2c. The transmission premise is the weakest part of the thesis — three independent hits

Everything terminates in *invisible → visibility → sudden adverse repricing*. That step, not the magnitude, is under attack: ① **Duarte/Fonseca/Kohli/Reif (NBER Jan-2026)** — medical debts *"add minimal incremental information for default prediction"* ⇒ measurement gap, not credit-risk gap · ② **Richmond Fed EB 26-05** — pay-in-4 just $3.02B, no clear stress · ③ **NEW 9/11 — FICO Score 10 BNPL raises heavy users' scores**, so crossing layer 4 may be a *tailwind*. **None touches the magnitude arithmetic; all three attack the step that turns magnitude into consequence** — the step **FLOW-PHAN-01 and -05** rest on, both still priced at Apr-2026 confidences. → **one consolidated memo to RED.**

### 🔻 2d. The top open research question — unanswered since 2026-07-28

**Is longer-term BNPL already inside existing aggregates?** Richmond Fed asserts it is; **UNVERIFIED**, and DEWEY calls it *"the single most important open question for downstream use."* If true, **~$16B of the ~$29B BNPL central is already counted** and treating it as hidden double-counts. **Registered as the top research item for the ~11/05–11/20 gate.**

### 2e. Also in `FRAMEWORKS.md`
**Phantom-DTI → HOMER** (mechanism intact, magnitude re-based) · **7 de-double-counting rules** (⛔ #1: headline "BNPL $70B" is *annual volume*, not stock — **~23× overstatement**; ⛔ #2: balance sheets capture only **~47%** of BNPL) · **why G.19↔QHDC yields NO publishable gap** (common-mode blind spot, sign inverted) · **FLOW-PHAN-01..06** with breakpoints · **CFPB 1033 verbatim must-carry** + its corrected status · **§2.8 the structural fix owed** (why this rebuild was 42 days late).

## 3. Threshold BANDS (durable) — live values are in CURRENT STATE above

*Bands + sources are durable; they are the registered trip levels. **The live reading for each row lives ONCE, in the CURRENT STATE block** — the old "Current" column here was a hardcoded second copy that rotted independently (DAEDALUS audit finding), and keeping two copies is what let the BNPL row sit at 41% for three weeks after 47% published.*

| Metric | Yellow | Orange | Red | Source |
|---|---|---|---|---|
| BNPL Stacking | >35% | >45% | >55% | CFPB |
| Cross-Firm Stacking | >20% | >25% | >35% | CFPB |
| Affirm 30+ DQ | >3% | >4% | >6% | Affirm SEC |
| Klarna Credit-Loss Provision | >0.60% | >0.80% | >1.0% | Klarna 20-F |
| **BNPL Late-Payment Rate** | >25% | >35% | **>45%** | **LendingTree BNPL Tracker** |
| Fintech Failures (cumulative) | 2 | 3 | 5+ | Public |
| Phantom-DTI Gap | >5pp | >10pp | >15pp | CARL est |

> ⛔ **SOURCE ATTRIBUTION — the BNPL late rate is LendingTree's.** Three surfaces once named three different houses for one series: this band cell said **ABA**, CARL's STATUS row said **CFPB**, and `KB-CARL-028` credits the 34→41 step to the **Richmond Fed**. The reachable 34/41/47 series is **LendingTree's**. *(Corrected at the parent 2026-09-10.)*
>
> ⛔ **The 38% "BNPL for gasoline" figure is NOT on this series** — it is Protect Borrowers / Data for Progress (n=438 likely voters, fielded 7/2–5/26). **LendingTree publishes no gasoline figure**, and the two houses read groceries **29% vs 46%**. Never splice.
>
> ⚠️ **Klarna's 0.65% and Affirm's 2.3% are SUPERSEDED at parent** — see §6; live readings in CURRENT STATE.

## 4. Open predictions (7 rows — DISPOSITIONED 2026-07-10 ad-hoc pass)

*Carried from `workbook/PREDICTIONS.tsv` (the ledger of record — this table mirrors it). All 7 made 2026-04-09 (P03/P07 confidence-upgraded Apr-17). **Dispositioned 2026-07-10** by a CARL-directed ad-hoc pass, evidence-gated to own files + CARL parent STATUS/KB/CHANGELOG (no web pulls). **All 2026 windows are still open**, so no clean HIT/MISS is possible (year not closed); the pass re-marks confidence where a premise moved, notes each success/failure mode, and flags DATA-NEEDED where resolution requires a not-yet-published figure. Next data event: Affirm/Klarna Q2 ~Aug (ad-hoc spawn trigger, §8).*

*The **2026-07-10 verdict table** (Apr→7/10 confidences + each row's dispositioning basis) moved to **`PASSES.md`** on 2026-09-11 under the read-cap remedy — grep it there. Current marks are the 9/10 re-mark table below, as amended by the 9/11 P03 move.*

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
| **⭐ PHANTOM-DEBT MAGNITUDE — the domain's headline claim** | **`$400B+` invisible to bureaus** (CLAUDE.md ×5, STATUS.md ×3, PROVIDER.tsv ×2, and the DOSSIER domain-scope line until 2026-09-11) | ⛔ **REFUTED — `KB-CARL-367` (DEWEY C4, 2026-07-31): broad ~$176–216B, credit-only ~$30–60B (an order of magnitude smaller), composition medical ~85% / BNPL ~15% / EWA negligible.** Prefer the CFPB **flow** gap (~$80.46B/yr vs ~$36B/yr, ~2.2×). Full rebuild → **`FRAMEWORKS.md` §2.0**. *(This row was MISSING from this table until 2026-09-11 — the largest supersession in the domain was the one the supersession table did not list.)* |
| **"distressed invisible" $40–60B** | PROVIDER.tsv:26, derived as *"10–15% DQ on $400B"* | ⛔ **DEAD — built on the refuted base.** Credit-only phantom debt **in total** is ~$30–60B, so a *distressed subset* of $40–60B is internally incoherent. Do not cite. |
| **CC 90+ DQ** | 12.70% (STATUS.md:156 uses this as the phantom-debt multiplier base) | **Parent now 13.1%** — use CARL's figure |
| **ALLY-analog conclusion** (composition-masking) | FLOW-PHAN-06 + SV-PHAN-2026-04-17-01 | **KB-CARL-228** canonical; §2c here retained only as the *mechanism/trigger* framework, not for the Affirm data points |

---

## 7. Sources + cadence → **`FRAMEWORKS.md` §2.9**

*Moved 2026-09-11 (read-cap). Source table + catalyst cadence live there. **Next catalyst: Affirm FQ1-27 + Klarna Q3-26, ~2026-11-05 to 11-20.***

## 8. Refresh protocol — BOOT and CLOSEOUT. **This is PHAN's only live protocol.**

> ⛔ **`CLAUDE.md` §"On Session End" is SUPERSEDED (2026-09-11).** Its step 1 points at the frozen `STATUS.md`; its step 2 routes to a `SHARED/` directory that does not exist; and it has **no git step at all**, so a session following it commits nothing and reaches nobody. Use this section. *(The defect is not PHAN-specific — all seven CARL sub-agents share the same skeleton. Routed to CARL 2026-09-11.)*
>
> **⚠️ Run the CLOSEOUT half at EVERY session end, not just end-of-day** (`[[feedback_intra_day_closeout_discipline]]`). **2026-09-11 ran five passes in one day**; an intermediate pass that skips write-back hands the next one a stale header over newer content.

### BOOT

1. **Read this DOSSIER** — the **CURRENT STATE** block first (live summary), then the **📌 OWED / ASSIGNED WORK** block. Not the frozen `CLAUDE.md`/`STATUS.md`.
2. **Step-0 inbox scan** — `find inbox -maxdepth 2 -name "*.md" -not -path "*/processed/*" -not -name "README.md"`. Anything present is UNPROCESSED by definition. *(⚠️ The `-not -name "README.md"` matters — `inbox/README.md` is permanent, and without it every scan reports 1 packet and the count stops meaning anything. Caught by running this step against itself, 2026-09-11.)* ⛔ **Use the lane-descending form, never `ls inbox/*.md`** — `inbox/` has sub-lanes (`inbox/WALTER/`), and the flat glob silently excludes a whole live lane. **⚠️ AGE IS A FINDING:** PHAN may go a quarter between sessions, so a packet can sit for weeks while *looking* delivered. **Older than ~30d ⇒ telling the sender outranks actioning the packet.**
3. **`FRAMEWORKS.md`** when working a framework · **`PASSES.md`** by grep for a specific dated pass. Neither is a boot whole-read.

### CLOSEOUT — write-back

4. **Append new events to the live TSVs only** — `workbook/COCKROACH.tsv`, `workbook/REGULATORY.tsv`. Advance BOTH clocks in the two-clock header, and **record an explicit `DID_NOT_APPEAR` null when a sweep found nothing** — a stale DATA clock is otherwise ambiguous between "no events" and "nobody looked." Do not revive the frozen TSVs.
5. **Update the as-of stamps** in the CURRENT STATE block, §3 (thresholds) and §6 (superseded). ⛔ **Update CURRENT STATE IN PLACE — do not append a new section to this file** (read cap; §8.1).
6. **Resolve predictions at CARL, NOT here.** PHAN re-marks confidence and recommends; **CARL disposes.** §4 stays ⚠ UNRESOLVED until CARL records it.
7. **Route findings to CARL** — an **outbox packet** at `outbox/<date>_PHAN-to-CARL_<subject>.md` **AND** a delivery copy into `AGENTS/CARL/inbox/` (root carve-out ①: a packet you authored into another agent's inbox is yours to commit **and you must**). ⛔ **NOT `../SHARED/`, which does not exist.** ⚠️ **A packet CARL has not graded is not a delivered finding** — say so in the report rather than implying it landed.
8. **Inbox RE-scan** — repeat step 2. **The boot scan is a SNAPSHOT**: packets landing mid-session are invisible for the rest of it and nothing re-checks. Advisory, never blocking. *(Pattern borrowed from TERRY and REGINALD, both of which added it after being bitten.)* File consumed packets with **`git mv`** to `inbox/processed/`, never bash `mv`. Anything deliberately not actioned gets a dated **PARKED** note.
9. **Update the 📌 OWED block** — close what you did, add what you or CARL now owe. **This is the step that would have caught the 42-day §2 miss.**
10. **Read-cap check** — the fleet script **cannot evaluate sub-agents** (`read_cap_check.py --agent PHAN` → `CANNOT-EVALUATE: no charter at AGENTS/PHAN/CLAUDE.md`; it resolves `AGENTS/<NAME>/`). So check locally:
    ```
    for f in DOSSIER.md FRAMEWORKS.md PASSES.md; do
      printf "%-16s %6s B %s\n" "$f" "$(stat -c%s $f)" \
        "$([ $(stat -c%s $f) -le 32550 ] && echo OK || echo '⛔ OVER 32,550')"; done
    ```
    **Only `DOSSIER.md` is a whole-read and therefore capped**; `FRAMEWORKS.md` (read-when-working) and `PASSES.md` (grep) carry no cap claim — measured anyway so drift is visible. **Over cap ⇒ rotate to `PASSES.md`, never delete.**
11. **Git — the step `CLAUDE.md` never had.** All ops from repo root (`cd "$(git rev-parse --show-toplevel)"`).
    - **Modified:** `git commit AGENTS/CARL/sub_agents/PHAN/<file> -m "PHAN: <subject>"` — path-scoped, no separate staging.
    - **New:** `git add <specific files> && git commit <same specific files> -F /tmp/msg.txt` — explicit paths, **never** `git add` a directory.
    - ⛔ **Never `git reset HEAD`** (shared index — global unstage) and **never `git commit --amend`**.
    - ⛔ **Never a pathspec-less commit** — it sweeps whatever another session has staged. *(Live on 2026-09-11: PROME had a file staged while PHAN committed.)*
    - **Subject ≤100 chars**; receipts and figures go in the body (heredoc to a file).
    - **Push:** `bash scripts/safe-push.sh`. ✅ **The receipt is the line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).`** — a log tail or a bare `Pushed.` is **not** a receipt. Non-ff ⇒ `git pull --rebase --autostash` after the dirty-path overlap check; **never force**.
12. **Auto-memory** (only if a transferable lesson was earned) — write/extend under `memory/auto/`, then `python3 scripts/memory_index_check.py --strict --slug <name>` and **self-commit the file** (root carve-out ③ makes this mandatory: an index row pointing at an uncommitted file is worse than no memory).

### 8.1 Where things live — keep `DOSSIER.md` under the cap

| File | Role | Read mode |
|---|---|---|
| **`DOSSIER.md`** | CURRENT STATE · OWED · thresholds · predictions mirror · superseded · this protocol | **whole read — capped 32,550 B** |
| **`FRAMEWORKS.md`** | the durable analytical assets (rebuilt §2) | read when working a framework |
| **`PASSES.md`** | dated pass narratives, newest first | **grep only** |

**Write each pass narrative to `PASSES.md`; update CURRENT STATE in place here.** Appending a dated section to this file is what pushed it to **126% of cap** on 2026-09-11.

---

## 9. Change history → **`PASSES.md`**

*The per-pass change table moved there 2026-09-11: §9 and `PASSES.md` were the same artifact kept twice. **9 passes logged; most recent 2026-09-11 (five in one day).** `grep -A3 '2026-09' PASSES.md`.*

---

*PHAN dossier assembled 2026-07-10 by MOLD (DAEDALUS editor), from PHAN's Apr-2026 frozen surfaces. Transcription-with-provenance — no new analysis. Legacy identity surfaces (CLAUDE.md, STATUS.md) frozen same day; COCKROACH.tsv + REGULATORY.tsv stay live. Provenance and refutations per DAEDALUS audit `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`. Predictions dispositioned + FLOW numbering reconciled 2026-07-10 (§9).*
