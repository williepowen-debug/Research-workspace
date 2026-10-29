# PHAN DOSSIER — Phantom Debt & Shadow Credit

> **What this is.** PHAN (Phantom Debt / Shadow Credit monitor) was **demoted from full sub-agent to dossier on 2026-07-10** (DAEDALUS CARL sub-agent audit, Will-approved). This file is the **single entry surface** for the phantom-debt domain going forward. It is not a live dashboard: it carries PHAN's durable analytical assets (frameworks, thresholds, open predictions, transmission pathways) at their original vintages, each fact stamped with its own as-of date and file:line origin. Since 2026-09-10, ad-hoc passes also author analysis (reasoning in `PASSES.md`, frameworks in `FRAMEWORKS.md`).
>
> **Domain scope** *(carried from the Apr-2026 charter, `archive/CLAUDE_2026-04_frozen.md` §Role)*: phantom debt / shadow credit — consumer borrowing invisible to credit bureaus. ⛔ **The legacy `$400B+` figure in this line is REFUTED — see §2a: ~$176–216B broad, ~$30–60B credit-only, medical ~85% of it.** BNPL stacking, cash-advance / earned-wage-access (EWA) apps, fintech-lender ("cockroach") health, regulatory visibility changes (CFPB 1033), and phantom-DTI impact on mortgage underwriting (→ HOMER).
>
> **Refresh model.** No standing sessions. Refreshed by **ad-hoc CARL spawns** against this dossier (per CARL SPAWN_PROTOCOL templates). **Next catalysts (confirmed):** **Coastal Q3 10/29 BMO · Affirm FQ1-27 11/05 AMC · Klarna Q3 11/17 BMO**, the last pass before five PHAN rows come due 12/31. See §8.
>
> **Last ad-hoc passes:** **2026-10-28** (CARL hygiene pass, then a Will-directed session: news sweep, file sweep, workbook refresh, closeout rebuild); before it 2026-09-11, 2026-09-10, 2026-07-10. **⚠️ Narratives live in `PASSES.md`: `grep -n '^## 20' PASSES.md` lists them; never read it whole.**
>
> **⚠️ Vintage warning.** The legacy identity surfaces (the Apr-2026 charter, now `archive/CLAUDE_2026-04_frozen.md`, and the frozen `STATUS.md`) stay at their Apr-2026 build vintage and carry **TWO refuted claims, not one**: ① the Klarna deterioration narrative (**REFUTED** — Klarna Q1-2026 profitable, CARL May-14) and ② **the `$400B+` phantom-debt headline, which those files assert 9 times and which is REFUTED by `KB-CARL-367` (~$176–216B broad / ~$30–60B credit-only).** They are history and are **not** edited; this banner is the maintained correction. **⛔ Do not lift the domain-scope, "Why This Domain Matters", or "Key Concepts" magnitude lines from the archived charter, nor the STATUS.md masthead/§BNPL Outstanding rows.** See §2a and §6.

---

## CURRENT STATE — as of 2026-10-28

*One block, updated IN PLACE each pass; the prior snapshot rotates verbatim to `PASSES.md`. Rows behind it: `workbook/PROVIDER.tsv` (metrics), `COCKROACH.tsv`, `REGULATORY.tsv`, `PREDICTIONS.tsv`. **PHAN proposes, CARL disposes.***

| Threshold (§3) | Live | Band | Vintage |
|---|---|---|---|
| BNPL late-payment rate | **47%** LendingTree (34 → 41 → 47); **26% flat** Fed SHED | 🔴 on LendingTree only; 🟡 on SHED. **Basis ruling with CARL** | LT fielded 3/17–23/26, n=2,060 · SHED Oct-25, n≈13k, pub 5/13/26 |
| BNPL stacking, 2+ at once | **63%** flat; 25% hold 3+ | 🔴 held; P01's >70% not reached | LendingTree, fielded 3/3–6/26 |
| Affirm 30+ DQ (ex-Peloton) | **2.5%** @ 6/30/26 | 🟢 | Affirm 10-K, filed 8/27/26 |
| Klarna credit-loss provision | **0.52%** of GMV (Q2-26) | 🟢 | Klarna release 8/18/26 |
| Fintech failures (cumulative) | **3**; none new since 2025 | 🟠 | `COCKROACH.tsv` (null 10/28) |
| Phantom-DTI gap | ⛔ **no valid reading** (legacy ~12pp not supported) | not graded | `FRAMEWORKS.md` §2.2 |

**🔴 FLOW-PHAN-06 trigger ACTIVE, breakpoint NOT met.** Affirm quarterly provision YoY **+1.8 → +40.0 → +33.5 → +42.5%**; NCO YoY **+12.6 → +16.5 → +22.2 → +36.9%** while headline DQ fell. ⚠️ **Two CARL-verified quarters above the bar, not three** (FQ4 is PHAN-derived). Leg 2 UNRESOLVABLE (Will 10/28: do not grade or report); leg 3 (gas >$4.50) not met. NCO re-instrumentation → CARL ~11/12. *`FRAMEWORKS.md` §2.6.*

**Distress, not failure (count stays 3):** **LendingPoint** (KBRA six-class cut, May-26) · **Coastal Financial (CCB/CCBX)**: Q2-26 net loss $42.1M on a $68.8M credit expense, stock −43.5% in a session; **Q3 reports 10/29 before open**. LendingPoint↔Coastal link is Fintech Business Weekly's, not company-confirmed.

**Regulatory:** Rule 1033 **enjoined + under reconsideration** (not withdrawn); the rewrite NPRM has been at OIRA since ~8/6, **unpublished at 10/28**. NYDFS BNPL proposal 7/15, comments closed 9/14, **no final rule**. P07 state-AG count **4 of 5** (NY, MN, DC, CO); Montgomery Co. PA DA v. MoneyLion/Dave (~9/28) is a county suit, counting ruling with CARL.

**Counter-evidence (→ RED, memo OWED):** FICO Score 10 BNPL raises heavy users' scores · Fed SHED late rate flat · LendingTree 10/14: 90% of users who asked got late fees waived or reduced.

**Corrections to carry:** the **38% BNPL-for-gasoline** figure is Protect Borrowers / Data for Progress (n=438), **never spliced** into LendingTree. CARL's CC 90+ **stock** basis is refuted (NY Fed 8/11; CRL-05 voided, CRL-30 on the flow rate): ⛔ never re-arm on 13.74%.

**Next:** Coastal Q3 **10/29** · Affirm FQ1-27 **11/05** after close · Klarna Q3 **11/17** before open · five OPEN rows resolve **12/31** at CARL.

### 📌 OWED / ASSIGNED WORK — check this block at every boot

*Created 2026-09-11 because the §2 rebuild sat **42 days** unseen: CARL assigned it in its own KB Notes column (`KB-CARL-367`), a surface no PHAN session reads. **An obligation recorded where the obligee does not travel is not an obligation.** `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`*

| Item | Owner | Raised | State |
|---|---|---|---|
| **Is longer-term BNPL already in the aggregates?** (~$16B of ~$29B BNPL central) | PHAN | 2026-07-28 (DEWEY C4) | 🔻 **OPEN, top research item for the 11/05 gate** |
| **Consolidated transmission-premise memo → RED** (3 hits); re-price FLOW-PHAN-01/-05, still at Apr-2026 confidences | PHAN | 2026-09-11 | 🔻 **OPEN** |
| **P04 successor proposal** (failure count measures a legal event, not the mechanism) | PHAN→CARL | 2026-09-11 | 🔻 **OPEN** |
| **Coastal (CCB) Q3-26, 10/29 before open**: update the DISTRESS row | PHAN | 2026-10-28 | 🔻 next pass |
| **Name the Klarna FY26 credit-loss source line** for P02 | PHAN | 2026-10-28 | 🔻 at the 11/17 Klarna pass |
| **P02 state conflict**: ledger RESOLVED MIXED 7/10 vs the 9/10 re-mark + MISS ask | **CARL** | 2026-10-28 | 📤 packet sent (replaces the 9/10 ask) |
| **Affirm/Klarna quarterlies have no current parent home** (`KB-CARL-228` STALE, `BNPL_STRESS.tsv` FROZEN) | **CARL** | 2026-10-28 | 📤 packet sent |
| **P01: does PYMNTS 74% (2+ providers in 3 months) count?** | **CARL** | 2026-10-28 | 📤 packet sent |
| **P07: does a county DA suit count toward 5 states?** | **CARL** | 2026-10-28 | 📤 packet sent |
| **BNPL late-rate basis: LendingTree 47% vs Fed SHED 26%** | **CARL** | 2026-10-28 | 📤 packet sent |
| **Published-figures ledger** (record every figure PHAN sends another desk, incl. withdrawn ones; HANS `workbook/PUBLISHED.tsv` pattern) | PHAN | 2026-10-28 | 🔻 next pass (deferred) |
| **Tests for `scripts/closeout_check.py` + `boot_check.py`** (the falsification set as a re-runnable test; HANS `test_hans.py` pattern) | PHAN | 2026-10-28 | 🔻 next pass (deferred) |
| **Tidy:** move `outbox/SV-PHAN-2026-04-17-01.md` → `state_vectors/`; rotate `workbook/PREDICTIONS.tsv` header pass-history (38 comment lines) verbatim to `PASSES.md`, keeping the two clocks | PHAN | 2026-10-28 | 🔻 next pass (low) |
| **FLOW-PHAN-06 → re-instrument onto NCO growth?** | **CARL** | 2026-09-11 | ⏳ CARL at the ~11/12 gate |
| **Sub-agent closeout git step** | **CARL** | 2026-09-11 | ⏳ partial: STUE, DOC, PHAN (`CLOSEOUT.md` + runner, 10/28) have it; GIG, POLLY, POP, META, `SPAWN_PROTOCOL.md` do not. Shared runner for all 7: **proposed to CARL 10/28** (packet) |

*Closed rows (§2 rebuild, closeout rebuild, ABS leg 2, routing rule adopted by CARL 9/11, read-cap script now runs, READS rows, dossier rotation under 75%) → `PASSES.md` (10/28 sections).*

---

## 1. Header / orientation

| | |
|---|---|
| **Agent** | PHAN — Phantom Debt & Shadow Credit Monitor |
| **Status** | DEMOTED TO DOSSIER 2026-07-10 (was: full sub-agent, reports to CARL via State Vectors) |
| **Domain** | Phantom Debt / Shadow Credit / Non-Bank Lending *(Apr-2026 charter)* |
| **Parent system of record** | CARL: `STATUS.md` (BNPL rows), `thesis/PREDICTIONS.tsv`, `workbook/KB.tsv`. ⚠️ `BNPL_STRESS.tsv` FROZEN 6/26; `KB-CARL-228` STALE (4/17) |
| **Legacy last session** | 2026-04-17 (STATUS.md:2) |
| **Live surfaces (this dir)** | `workbook/{COCKROACH,REGULATORY,PROVIDER,PREDICTIONS}.tsv` — see §5 |
| **Frozen surfaces (this dir)** | `STATUS.md`, `archive/` (old charter), `workbook/{VX,ML,FLOW}.tsv`. `CLAUDE.md` is a live charter again since 2026-10-28 |

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

**furnished → in the core file → in Equifax (what the QHDC reads) → scored.** Four independent gates. **Essentially all BNPL clears layer 1 and fails layer 4.** Affirm furnishes to Experian + TransUnion, **not Equifax** *(probable)*, so its ~$16.5–17.5B book likely never reaches the QHDC. Klarna furnishes **term loans only, not pay-in-4**. ⛔ "Invisible to the QHDC" needs the *Equifax* list; "invisible to lenders" needs a different one.

### ⚠️ 2c. The transmission premise is the weakest part of the thesis — three independent hits

The step *invisible → visibility → sudden adverse repricing* (FLOW-PHAN-01/-05, still at Apr-2026 confidences) is attacked by: ① **NBER Jan-2026 (Duarte et al.)**: medical debt adds minimal default-prediction information · ② **Richmond Fed EB 26-05**: pay-in-4 $3.02B, no clear stress · ③ **FICO Score 10 BNPL raises heavy users' scores**. None touches the magnitude arithmetic. → one consolidated memo to RED (OWED).

### 🔻 2d. Top open research question (since 2026-07-28)

**Is longer-term BNPL already inside existing aggregates?** Richmond Fed says yes; **UNVERIFIED**. If true, ~$16B of the ~$29B BNPL central is already counted. → `FRAMEWORKS.md` §2.5; top item for the 11/05 gate.

### 2e. Also in `FRAMEWORKS.md`
**Phantom-DTI → HOMER** (mechanism intact, magnitude re-based) · **7 de-double-counting rules** (⛔ #1: headline "BNPL $70B" is *annual volume*, not stock — **~23× overstatement**; ⛔ #2: balance sheets capture only **~47%** of BNPL) · **why G.19↔QHDC yields NO publishable gap** (common-mode blind spot, sign inverted) · **FLOW-PHAN-01..06** with breakpoints · **CFPB 1033 verbatim must-carry** + its corrected status · **§2.8 the structural fix owed** (why this rebuild was 42 days late).

## 3. Threshold BANDS (durable) — live values are in CURRENT STATE above

*Bands + sources are durable; they are the registered trip levels. **The live reading for each row lives ONCE, in the CURRENT STATE block** — the old "Current" column here was a hardcoded second copy that rotted independently (DAEDALUS audit finding), and keeping two copies is what let the BNPL row sit at 41% for three weeks after 47% published.*

| Metric | Yellow | Orange | Red | Source |
|---|---|---|---|---|
| BNPL Stacking | >35% | >45% | >55% | **LendingTree** (live, Mar-26); CFPB Jan-25 origin |
| Cross-Firm Stacking | >20% | >25% | >35% | CFPB Jan-25 (32%); ⚠️ no reading since |
| Affirm 30+ DQ | >3% | >4% | >6% | Affirm SEC |
| Klarna Credit-Loss Provision | >0.60% | >0.80% | >1.0% | Klarna 20-F |
| **BNPL Late-Payment Rate** | >25% | >35% | **>45%** | **LendingTree BNPL Tracker** |
| Fintech Failures (cumulative) | 2 | 3 | 5+ | Public |
| Phantom-DTI Gap | >5pp | >10pp | >15pp | CARL est. ⛔ basis refuted (`FRAMEWORKS.md` §2.2) |

> ⛔ **SOURCE ATTRIBUTION — the BNPL late rate is LendingTree's.** Three surfaces once named three different houses for one series: this band cell said **ABA**, CARL's STATUS row said **CFPB**, and `KB-CARL-028` credits the 34→41 step to the **Richmond Fed**. The reachable 34/41/47 series is **LendingTree's**. *(Corrected at the parent 2026-09-10.)*
>
> ⛔ **The 38% "BNPL for gasoline" figure is NOT on this series** — it is Protect Borrowers / Data for Progress (n=438 likely voters, fielded 7/2–5/26). **LendingTree publishes no gasoline figure**, and the two houses read groceries **29% vs 46%**. Never splice.
>
> ⚠️ **Klarna's 0.65% and Affirm's 2.3% are SUPERSEDED at parent** — see §6; live readings in CURRENT STATE.

## 4. Predictions — ledger of record `workbook/PREDICTIONS.tsv`

*Mirror only; dated notes live in the ledger, and `scripts/boot_check.py` prints days to each window end. All made 2026-04-09. Re-mark history (7/10 and 9/10 tables, calibration modes) → `PASSES.md`. **CARL resolves.***

| # | Prediction | Mark | Window | State |
|---|---|---|---|---|
| P01 | BNPL stacking >70% | 25% | H2 2026 | OPEN; PYMNTS 74% counting ruling with CARL |
| P02 | Klarna credit losses >1.0% | 2% | FY2026 | ⚠️ ledger RESOLVED MIXED 7/10; the 9/10 re-mark conflicts, ruling with CARL |
| P03 | CFPB 1033 enforcement delayed beyond 2026 | 98% | EOY 2026 | OPEN, tracking HIT |
| P04 | ≥2 more fintech failures | 12% | 2026 | OPEN; zero in-scope failures so far |
| P05 | BNPL-linked FHA defaults identifiable | 15% | Q3–Q4 2026 | OPEN; the data to identify them does not exist |
| P06 | NY comprehensive BNPL licensing | MIXED | 2026 | RESOLVED 7/10 (law signed 5/9/25, before the forecast) |
| P07 | Cash-advance AG enforcement ≥5 states | 88% | 2026 | OPEN; 4 of 5; county-DA ruling with CARL |

---

## 5. Live ledger index (append targets for ad-hoc spawns)

Three workbook TSVs are **LIVE append surfaces**: COCKROACH and REGULATORY (DAEDALUS audit: unique fleet assets), and PROVIDER (unfrozen 2026-10-28, Will-directed). Ad-hoc spawns append here:

| Ledger | Role | State | Contents (as of 2026-10-28) |
|---|---|---|---|
| **`workbook/COCKROACH.tsv`** | Fintech-failure / distress tracker | 🟢 **LIVE** | 12 rows: FAILURE CURO, Synapse, Tricolor (bank contagion) · RETREAT Upstart · Klarna class action + distress · DISTRESS FloatMe, Current, LendingPoint, Coastal/CCBX, EarnIn · DID_NOT_APPEAR null 10/28 |
| **`workbook/REGULATORY.tsv`** | 1033 arc + EWA/BNPL state actions | 🟢 **LIVE** | 25 rows: CFPB 1033 arc (incl. 9/11 CORRECTION, 8/6 NPRM to OIRA); EWA state laws (CO, CT); AG/DA actions (NY, MN, DC, CO, Montgomery Co. PA); NYDFS BNPL proposal 7/15; 8-court TILA ruling; VERIFY sweep lines |
| **`workbook/PROVIDER.tsv`** | Provider + sector metrics (Affirm, Klarna, surveys, phantom-debt size) | 🟢 **LIVE** since 10/28 | 50 rows: 16 current added 10/28 (Affirm FQ4-26 DQ/provision/NCO/allowance, Klarna Q2-26, Fed SHED, LendingTree, PYMNTS, phantom-debt fork, earnings dates); superseded rows Notes-prefixed |

**Frozen-vintage ledgers** (carried into this dossier, no longer maintained — see §6/§7 for where their facts now live): `VX.tsv` (15 vectors; superseded by §3 bands + `PROVIDER.tsv`), `ML.tsv` (11 entries), `FLOW.tsv` (6 pathways → `FRAMEWORKS.md` §2.6). **`PREDICTIONS.tsv` is LIVE** (ledger of record, §4).

---

## 6. ⛔ SUPERSEDED AT PARENT — do NOT cite from here

*These facts are now owned by CARL parent surfaces. The legacy PHAN values below are frozen and, in the Klarna case, **refuted**. Cite the parent surface, not this dossier.*

| Fact | Legacy PHAN value (frozen) | Canonical owner / correction |
|---|---|---|
| **Klarna Q1-2026 profitability** | STATUS.md asserts Klarna FY2025 net loss, provisions "rising," "narrative cracking," Elliott $6.5B lifeline | ⛔ **REFUTED — Klarna Q1-2026 PROFITABLE** (CARL parent, May-14-2026). The legacy Klarna deterioration narrative is wrong. |
| **Affirm quarterlies** (GMV, DQ, provisions, ABS FICO) | 2.3% DQ, $214.2M provisions (+40% YoY), ABS WA FICO 672, GMV $13.8B | ⚠️ **No current parent home:** `KB-CARL-228` STALE (4/17), `BNPL_STRESS.tsv` FROZEN (6/26). Live rows: `workbook/PROVIDER.tsv` (unfrozen 10/28); ruling asked of CARL 2026-10-28. |
| **Klarna quarterlies** (provisions, revenue, class action) | 0.65% provisions, $1.08B rev, case 25-cv-07033 | ⚠️ **No current parent home** (same as Affirm). Live rows: `workbook/PROVIDER.tsv`. |
| **BNPL late-payment rate** | **47% (2026, LendingTree Tracker pub 2026-08-19)** | ✅ **Verified and superseded at the parent 2026-09-10** — STATUS row updated 41%→47%, band **🔴 breached**, attribution corrected off CFPB. KB-CARL-439. |
| **⭐ PHANTOM-DEBT MAGNITUDE — the domain's headline claim** | **`$400B+` invisible to bureaus** (the Apr-2026 charter ×5, STATUS.md ×3, PROVIDER.tsv ×2, and the DOSSIER domain-scope line until 2026-09-11) | ⛔ **REFUTED — `KB-CARL-367` (DEWEY C4, 2026-07-31): broad ~$176–216B, credit-only ~$30–60B (an order of magnitude smaller), composition medical ~85% / BNPL ~15% / EWA negligible.** Prefer the CFPB **flow** gap (~$80.46B/yr vs ~$36B/yr, ~2.2×). Full rebuild → **`FRAMEWORKS.md` §2.0**. *(This row was MISSING from this table until 2026-09-11 — the largest supersession in the domain was the one the supersession table did not list.)* |
| **"distressed invisible" $40–60B** | PROVIDER.tsv:26, derived as *"10–15% DQ on $400B"* | ⛔ **DEAD — built on the refuted base.** Credit-only phantom debt **in total** is ~$30–60B, so a *distressed subset* of $40–60B is internally incoherent. Do not cite. |
| **CC 90+ DQ** | 12.70% (STATUS.md:156 uses this as the phantom-debt multiplier base) | **Cite CARL `STATUS.md`** (12.92% Q2-26 at 10/28; stock basis, level comparisons void, see CRL-30) |
| **ALLY-analog conclusion** (composition-masking) | FLOW-PHAN-06 + SV-PHAN-2026-04-17-01 | `KB-CARL-228` (STALE 4/17) is history; the live mechanism/trigger is `FRAMEWORKS.md` §2.6 |

---

## 7. Sources + cadence → **`FRAMEWORKS.md` §2.9**

*Moved 2026-09-11 (read-cap). Source table + catalyst cadence live there. Next catalysts: CURRENT STATE.*

## 8. Refresh protocol — BOOT here; CLOSEOUT in **`CLOSEOUT.md`**

> **Charter:** `CLAUDE.md` is live again (2026-10-28, Will) and points here; the Apr-2026 charter's boot and closeout steps are archived as history. **Boot = the steps below. Closeout = `CLOSEOUT.md`**, with its runner `scripts/closeout_check.py` (both 2026-10-28, Will-approved). **Run closeout at EVERY session end, including intermediate passes.**

### BOOT

0. **Run `python3 AGENTS/CARL/sub_agents/PHAN/scripts/boot_check.py`** (from any directory; every path is anchored to the repo root). It prints: PHAN's own inbox with packet ages · each prediction's days to window end · the next PHAN docket row · every packet PHAN sent that its recipient has not filed. *(Added 2026-10-28: the old relative `find inbox` counted CARL's inbox when CARL spawned PHAN from `AGENTS/CARL/`.)*
1. **Read this DOSSIER**: CURRENT STATE first, then the **📌 OWED** block. Never the frozen `STATUS.md` or `archive/`.
2. **Inbox packets** (boot_check [1]): read each one. Anything present is UNPROCESSED by definition. **AGE IS A FINDING:** PHAN may go a quarter between sessions; a packet **older than ~30 days ⇒ telling the sender outranks actioning it.** By hand, always anchored: `find "$(git rev-parse --show-toplevel)/AGENTS/CARL/sub_agents/PHAN/inbox" -maxdepth 2 -name "*.md" -not -path "*/processed/*" -not -name README.md`.
3. **`FRAMEWORKS.md`** when working a framework · **`PASSES.md`** by grep only. Neither is a boot whole-read.
4. **Follow up what PHAN sent** (boot_check [4]): for each OWED row marked 📤, a packet still unfiled is **delivered, not actioned**; a filed one is closed only once CARL's `STATUS.md` / `thesis/PREDICTIONS.tsv` actually carries the change. **Due predictions** (boot_check [2]): a row ≤60 days out gets its expectation written **before** the print; a past window goes to CARL for resolution.

### CLOSEOUT → **`CLOSEOUT.md`**

WRITE (ledgers, CURRENT STATE, OWED, predictions, routing, inbox, docket, PASSES) → RUN `python3 AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py` → COMMIT (explicit paths) → PUSH by session type → `--post` → REPORT (findings · checks run/not run/failed · commit vs verified push).

### 8.1 Where things live — keep `DOSSIER.md` under the cap

| File | Role | Read mode |
|---|---|---|
| **`DOSSIER.md`** | CURRENT STATE · OWED · thresholds · predictions mirror · superseded · boot protocol | **whole read — capped 32,550 B** |
| **`CLOSEOUT.md`** + `scripts/closeout_check.py` | the closeout contract and its runner | read at closeout |
| **`FRAMEWORKS.md`** | the durable analytical assets (rebuilt §2) | read when working a framework |
| **`PASSES.md`** | dated pass narratives, newest first | **grep only** |

**Write each pass narrative to `PASSES.md`; update CURRENT STATE in place here.**

---

## 9. Change history → **`PASSES.md`**

*The per-pass change table moved there 2026-09-11: §9 and `PASSES.md` were the same artifact kept twice. **Most recent pass 2026-10-28;** `grep -n '^## 20' PASSES.md` lists every pass (a count written here goes stale).*

---

*Assembly provenance (2026-07-10, MOLD/DAEDALUS) → `PASSES.md` "Dossier provenance".*
