# PHAN FRAMEWORKS — the durable analytical assets (DOSSIER §2, rebuilt)

> **What this is.** The frameworks that justify PHAN's existence as a domain — the material DAEDALUS's 2026-07-10 audit found *"exists nowhere else at parent, or in more detail than parent holds."* Split out of `DOSSIER.md` §2 on **2026-09-11**: the rebuilt section is ~2× its old size and `DOSSIER.md` sits under a 32,550 B whole-read cap. `DOSSIER.md` §2 keeps a substantive summary and points here.
>
> **⚠️ REBUILT 2026-09-11 — THIS IS THE OBLIGATION CARL ASSIGNED ON 2026-07-31 AND IT WAS 42 DAYS LATE.** `KB-CARL-367` closes with *"CLAUDE.md K-SHAPE phantom line updated 7/31; **PHAN owns the sec.2 rebuild**."* CARL updated its own surface that day; PHAN's surfaces kept the old premise through three subsequent passes (9/10, 9/11 AM, 9/11 PM) because **the assignment was recorded only in CARL's KB and PHAN's boot never reads it.** `[[finding_transfer_completes_only_when_the_receiver_encodes]]` — with PHAN on the receiving end. The structural fix is §2f.
>
> **Basis of the rebuild:** `AGENTS/DEWEY/output/2026-07-28_c4-phantom-debt-magnitude.md` (DEWEY C4, run 2026-07-28; PHAN-proposed, Will-gated; consumers named as *"CARL · PHAN dossier §2 · LIQUID"*) → `KB-CARL-367`. Read at the source 2026-09-11, not relayed through the KB summary.
>
> **Read-mode:** read whole when working a framework; grep otherwise. No read-cap budget claim on grep terms (READ_CAP rule-8 mode ruling).

---

## 2.0 ⛔ THE HEADLINE NUMBER CHANGED. LEAD WITH THE FORK, NOT A POINT ESTIMATE.

**PHAN's old identity line — *"the $400B+ in consumer borrowing invisible to credit bureaus"* — is dead.** It was never a measured figure; it was the top of a wide range, and the range only survives under a definition that counts **unpaid medical bills**, which are not credit.

| Definition | Total | Composition |
|---|---|---|
| **BROAD** (incl. provider-held unpaid medical bills) | **~$176–216B**, central **~$195B** | medical ~85% · BNPL ~15% · EWA negligible |
| **CREDIT-ONLY** (excl. provider-held unpaid bills) | **~$30–60B** | BNPL-dominant |

**The definitional fork moves the answer ~4×; the estimation error moves it far less. So the fork IS the finding — never publish a point estimate without it.** The same trap sits one level down inside BNPL, where a definition choice moves the answer **8×**: broad (incl. longer-term interest-bearing POS installment) **$25–33B** vs **pay-in-4 only $3.6–4.8B**.

**Component build** *(DEWEY C4 §1)*:

| Component | Low | High | Basis |
|---|---|---|---|
| BNPL (broad) | $25B | $33B | ~60–65% measured |
| EWA / cash advance (**stock**, not flow) | ~$1B | ~$3B | inferred — **no published stock figure exists** |
| Medical — bureau-invisible | ~$150B | ~$180B | illustrative, **not co-vintaged** |

### ⭐ The metric that should REPLACE the stock estimate

The medical component is the bulk of the total **and the weakest number in it** — it subtracts a **June-2023** numerator ($49.2B visible) from a **December-2021** denominator ($220B) **across two different universes** (bureau tradelines vs household self-report). It is illustrative, not measured, and no co-vintaged estimate exists.

**Prefer the CFPB flow gap: ~$80.46B/yr of new medical debt accrues against only ~$36B/yr appearing on consumer reports — a ~2.2× invisibility rate**, co-vintaged, from a single primary. [PRIMARY: CFPB final rule preamble, 90 FR 3276, 2025-01-14]

> **Honest statement on the medical share, to be used verbatim rather than paraphrased:** *the invisible share is large, on the order of three-quarters, and cannot currently be pinned tighter.*

⚠️ **Two sign errors that circulate and must never be repeated:**
- **The "$88B (2021)" medical figure is the VISIBLE number**, not the invisible one — CFPB's estimate of medical debt **on** credit reports as of June 2021. Anyone citing it as phantom debt has the sign backwards.
- **CFPB expressly rejected $220B as the affected inventory**, writing that *"the CFPB's $50 billion estimate is a better approximation of the relevant inventory of medical debt."*

⚠️ **Vintage, stated plainly:** *anyone quoting a "2026 phantom debt number" is quoting 2021–2023 data.*

---

## 2.1 ⭐ THE FOUR VISIBILITY LAYERS — the structural core, and the biggest upgrade in this rebuild

**"Phantom" is not one thing, and visibility is not binary.** There are **four independently binding layers**. A loan can be furnished and still be absent from every aggregate statistic *and* invisible to underwriting. `[[finding_visibility_is_layered_not_binary]]`

| Layer | What it gates | BNPL status |
|---|---|---|
| **1. Furnished to any bureau** | the data exists at all | **Affirm: YES** — all pay-over-time products, Experian from 2025-04-01, TransUnion from 2025-05-01. **Klarna: term loans ONLY — explicitly NOT pay-in-4.** Afterpay / PayPal / Zip: no evidence |
| **2. In the CORE file** | a lender can see it on a full pull | **Partly** — bureaus built **specialty** files; CFPB: *"may not be reflected in traditional credit reports and credit scores"* |
| **3. In EQUIFAX** | whether it reaches the **NY Fed QHDC** and the aggregate statistics | **Affirm furnishes Experian + TransUnion, NOT Equifax** *(probable, not established — no Affirm or Equifax statement either way)* |
| **4. SCORED** | whether it constrains new credit | **NO.** Klarna verbatim: *"will have no impact on your FICO / Vantage score and will only be visible to you at this time"* |

### **Essentially all BNPL clears layer 1 and fails layer 4.**

⛔ **THE TRAP — you cannot use one furnishing list for both operations.** *"Invisible to the QHDC"* needs the **Equifax** furnisher list; *"invisible to lenders and scores"* needs a **different** one. Conflating them double-counts or under-counts depending on direction.

**This inverts the instruction PHAN itself wrote into the C4 prompt.** The prompt said *"the phantom total must exclude anything now being furnished."* Applied literally, that deletes **Affirm's ~$16.5–17.5B — the single largest book** — from a total whose entire purpose is to measure what lenders cannot see, **even though none of it is scored and probably none of it reaches Equifax.** The instruction conflated layer 1 with layer 4. **PHAN's old §2a line *"only Affirm reports, 2 of 3 bureaus"* is a layer-1 fact being used to carry a layer-3/4 implication — that is the same error in miniature.**

⚠️ **Unresolved source conflict, carried rather than papered over:** on whether furnished BNPL is visible to a lender pulling a full report — [PRIMARY] **Experian** says *"visible to lenders who request to view it"*; [INSTITUTIONAL] **American Banker** says *"only visible to consumers… not to other lenders"*; **Klarna's** own language says visible *"only to you."* These may all be right **about different bureaus**. Not resolved.

### 2.1.1 Layer 4 is now opening — and it is opening the WRONG WAY for the thesis

**FICO Score 10 BNPL / 10 T BNPL** went live **Fall-2025** — the first mechanism that could move BNPL across layer 4. Two qualifiers, both adverse to the visibility-shock story:
1. **Adoption is slow by design** — offered *alongside* existing scores at no extra cost, and FICO 8 (2009) remains dominant.
2. **In FICO's own testing, "consumers with five or more Affirm loans typically saw their scores INCREASE or remain stable."**

⇒ **If crossing layer 4 raises heavy users' scores, visibility arrives as a non-event or a tailwind, not a shock.** See §2.4.

---

## 2.2 Phantom-DTI Gap framework — RE-BASED

*PHAN's core original framework. The **mechanism** is durable and is retained. The **magnitude premise** attached to it was tested by DEWEY C4 and did not survive.*

**The mechanism (unchanged, and still the reason this matters to HOMER):**
- A consumer shows **35% DTI** to the mortgage underwriter.
- Actual DTI including BNPL / cash advances is higher — the obligations are real, owed, and not in the file the underwriter reads.
- Lenders' workaround is scanning **bank statements** for BNPL debits.
- HUD has an open **RFI** on BNPL in FHA underwriting (2025-06-24). **Still no final guidance or Mortgagee Letter as of 2026-09-11** — only an MBA comment letter asking FHA to standardise the BNPL debt definition.
- **Cross-agent → HOMER:** phantom debt inflates apparent housing affordability; when payments resume or step up, "surprise" defaults are amplified by obligations that were never in the file.

### ⛔ The "~12pp gap" (35% → 47%) and "bottom-60 leverage 20–30% higher" — NOT SUPPORTED AS STATED

**Denominator discipline first, because it decides the answer** *(DEWEY C4 §4; QHDC 2026:Q1, balances as of 2026-03-31)*:

| Denominator | Value | Phantom (broad ~$195B) | Phantom (credit-only ~$45B) |
|---|---|---|---|
| (A) Total household debt | $18.80T (**72.5% housing**) | 1.0% | 0.24% |
| (B) Non-housing | $5.162T | 3.8% | 0.9% |
| **(C) Unsecured base — card + other ← USE THIS** | **$1.812T** | **10.8%** | **2.5%** |
| (E) Card only | $1.25T | 15.6% | 3.6% |

**(A) understates the ratio 10.4× versus (C).** A phantom-debt ratio quoted against *total household debt* is arithmetically true and analytically meaningless — nearly three-quarters of that denominator is mortgages.

**Verdict:** against the correct unsecured base the broad figure gives **~11%** and the credit-only figure **~2.5%**. The 20–30% band is reachable only by **stacking two things**: the **broad** definition (counting unpaid medical bills as leverage) **and** a strong assumption that phantom debt is concentrated in the bottom 60%. That concentration is plausible but **unmeasured** — no source decomposes phantom debt by income quintile, and **KFF finds 0.3% of adults hold over half of all medical debt, which cuts AGAINST simple bottom-60 concentration.**

> ### ✅ REVISED PREMISE — cite this, not the old one
> **Bottom-60 leverage is plausibly 5–20% higher than reported, not 20–30%. The upper half of that range requires counting unpaid medical bills as debt; the credit-only figure is low single digits.**

---

## 2.3 ⛔ DE-DOUBLE-COUNTING RULES — operational, apply before any number leaves PHAN

*These are the errors that actually occur in this domain. The first one is an order-of-magnitude error and it is the most common.*

1. **STOCK vs FLOW is the largest single error.** The headline *"BNPL ~$70B (2025)"* is **annual transaction volume**, not a stock — summing it into a stock denominator **overstates ~23×**. Same trap downstream: the PayPal–Blue Owl **"$7B"** is a **two-year purchase flow**; CFPB's **$45.2B** is **2023 originations**, routinely misquoted as a current balance. It is neither.
2. **Balance sheets capture only ~half of BNPL.** Affirm's on-balance-sheet gross HFI was **$8,573M** against an **$18.4B** platform portfolio — **47%**. ~$9.8B is sold or off-balance-sheet and **still owed by consumers**. Systemic, not Affirm-specific: Klarna offloaded $1.6B in Q4-25; PayPal sold ~$7B of US pay-in-4 to Blue Owl. **Any estimate built from balance sheets alone understates by roughly half.**
3. **Never add credit-card-converted medical debt.** 17% of adults carry health-care debt **on a credit card** (KFF), plus CareCredit/Synchrony — already inside the $1.25T card aggregate. Adding it double-counts against both the card total and any survey-based medical figure.
4. **Medical trades are excluded from the QHDC BY RULE** — *"Our analysis excludes… medical trades"* — **even when they sit on the Equifax report.** So *"missing from the QHDC"* ≠ *"not furnished."* **Two independent blind spots, not one.**
5. **Unbilled self-pay obligations are NOT credit.** Including them converts "phantom credit" into "unpaid bills" — this is the §2.0 fork.
6. **Third-party collections sit outside the QHDC balance total.** Counting a collection tradeline *and* the original obligation double-counts.
7. **Survey shares are not mutually exclusive.** Consumers use multiple providers; KFF's medical categories overlap and **do not sum**.

### 2.3.1 The G.19 ↔ QHDC reconciliation does NOT work — publish no gap number

Like-for-like (**NSA, March 2026**): G.19 total **$5,074.6B** vs QHDC non-housing **$5,162B** → QHDC exceeds G.19 by **~$87B (+1.7%)**. **This must never be published as a phantom-debt gap:**
1. **The sign is wrong.** A furnishing gap predicts lender-surveyed G.19 **>** bureau-read QHDC. The observed sign is the opposite.
2. **FATAL — the blind spot is common-mode, so differencing CANCELS it.** The Fed says so itself: *"many of the major BNPL lenders are newly established non-bank lenders, where there is more limited coverage. Moreover, the G.19 is not currently able to separately track the volume of originations and outstanding balances of such loans."* [PRIMARY: Federal Reserve G.19 Technical Q&A #19] **Both series miss the same lenders.** `[[finding_spread_metric_blind_to_common_mode]]`
3. **Known wedges exceed the residual and run both ways** — charge-offs inflate QHDC, student loans deflate it, category mismatches and QHDC-only exclusions have no G.19 analogue.

---

## 2.4 ⚠️ THE TRANSMISSION PREMISE IS THE WEAKEST PART OF THE THESIS — three independent hits

PHAN's frameworks all terminate in one claim: **invisible → visibility arrives → sudden adverse repricing.** That claim, not the magnitude, is what makes the domain matter. It is now taking fire from three directions that arrived separately and have never been read together:

| # | Hit | What it attacks |
|---|---|---|
| **1** | **Duarte, Fonseca, Kohli & Reif** (Illinois/NBER, **Jan-2026**) — RD on the April-2023 $500 threshold: deletion cut reported medical collections **61%**, yet *"no evidence of benefits over the subsequent two years, ruling out even small effects"*, and medical debts *"regardless of size, add minimal incremental information for default prediction beyond standard credit report variables."* | **If right, the ~$170B medical block is a MEASUREMENT gap, not a credit-risk gap** — and "lenders are flying blind" fails at its core. |
| **2** | **Richmond Fed EB 26-05** (Feb-2026): pay-in-4 outstanding **$3.02B**, *"no clear evidence of elevated stress to date"*, card debt *"roughly 400 times larger"*; BNPL charge-offs **1.83% (2023)** vs card **4.19% (2023Q4)**; deep-subprime/no-FICO users repaid **96%** of the time. | The **magnitude and severity** of the BNPL leg. *(Answers a narrower question — pay-in-4 only. Against it: LendingTree has late-at-least-once at 34% → 41% → **47%**.)* |
| **3** | **FICO Score 10 BNPL** (§2.1.1, added by this rebuild, 2026-09-11) — heavy BNPL users' scores typically **rise** when BNPL is scored. | **The repricing DIRECTION.** Crossing layer 4 may be a tailwind, not a shock. |

⇒ **Recommended disposition: a single consolidated memo to RED, not three scattered flags.** Hits 1 and 2 are already staged; hit 3 is new. **None of them touches the magnitude arithmetic in §2.0 — they attack the step that turns magnitude into consequence**, which is the step FLOW-PHAN-01 and FLOW-PHAN-05 both rest on.

### Counter-counters, retained for symmetry
- **Secular decline predates policy:** share of consumers with a medical collection fell **20% (2017) → 14% (Mar-2022)**, independent of the reporting changes. Some "growing phantom" is an old trend, not new policy.
- **The geography could reverse:** **15 states covering 37.7% of the US population** currently ban medical debt from credit reports; if the Oct-2025 FCRA-preemption interpretive rule (90 FR 48,710) carries and *ACA Int'l v. Fulford* (D. Colo.) goes that way, those laws fall and up to 37.7% of the population moves **back toward visibility** — the opposite of the consensus direction.
- **And the other way:** state laws are actively converting **visible** debt into **invisible** debt. Urban Institute **excluded seven states' medical debt data** from its 2025 *Debt in America* update because of these statutes. **The phantom is becoming geographically concentrated.**

---

## 2.5 🔻 THE SINGLE MOST IMPORTANT OPEN QUESTION — unanswered, and it is PHAN's

> **Is longer-term BNPL already inside the existing aggregates?**
>
> Richmond Fed (EB 26-05) asserts that longer-term BNPL loans *"are reported to credit bureaus… largely captured by credit scores and aggregate consumer credit statistics."* **UNVERIFIED.** DEWEY C4 flags it as *"the single most important open question for downstream use."*
>
> **Why it is load-bearing:** if true, **~$16B of the ~$29B BNPL central is already counted**, and treating it as hidden **double-counts** — roughly halving the BNPL component of the credit-only total.
>
> **It is answerable**, it sits squarely in PHAN's domain, and it has been open since **2026-07-28**. **Registered here as the top research item for the ~11/05–11/20 gate.**

---

## 2.6 Transmission pathways FLOW-PHAN-01..06

*Canonical numbering is `workbook/FLOW.tsv` (TSV wins — reconciled 2026-07-10; the crosswalk of the divergent legacy STATUS prose IDs lives in `PASSES.md`).*

| ID | Name | Breakpoint (becomes critical when…) | Lag | Conf | Status |
|---|---|---|---|---|---|
| **FLOW-PHAN-01** | Shadow → Visible Credit Transmission | Shadow credit capacity exhausted; consumer must choose what to default on | 6–12 mo | HIGH 75% | MONITORING ⚠️ **§2.4** |
| **FLOW-PHAN-02** | BNPL Stacking Cascade | BNPL payments exceed 15% of income | 3–6 mo | HIGH 80% | ACTIVE |
| **FLOW-PHAN-03** | Payday Debt Trap Cascade | Consumer in perpetual rollover (>6 consecutive months) | immediate trap | HIGH 75% | MONITORING |
| **FLOW-PHAN-04** | Fintech Cockroach Cascade | Multiple fintech failures; funding-market stress | 3–9 mo | HIGH 85% | **ACTIVATING — see below** |
| **FLOW-PHAN-05** | PHAN-to-CARL Transmission | Shadow-credit stress appears in traditional metrics | 6–12 mo | HIGH 80% | ACTIVATING ⚠️ **§2.4** |
| **FLOW-PHAN-06** | BNPL Composition-Masking → ABS Surprise (ALLY analog) | Provision growth >30% YoY **AND** ABS WA FICO declining **AND** macro shock (gas >$4.50 / UI exhaustion) | 3–9 mo | MED-HIGH 65% | **TRIGGER ACTIVE / BREAKPOINT NOT MET** |

⚠️ **FLOW-PHAN-01 and -05 both terminate in the transmission premise that §2.4 attacks.** Their HIGH 75–80% confidences were set in Apr-2026, before any of the three hits. **They are not re-priced here — PHAN proposes, CARL disposes — but they should not be cited at those confidences without §2.4 attached.**

**FLOW-PHAN-04 — observed one step further along than previously (2026-09-11 PM):** Coastal Financial (CCB) took a **$68.8M credit expense** on a *"single, isolated CCBX partner relationship"*, swinging to a **$42.1M** quarterly net loss, stock **−43.5% in one session**; upstream, LendingPoint drew a **six-class KBRA downgrade** and a **$40.2M-vs-$63.2M** BDC markdown. **The cascade's bank-contagion step is now evidenced at a listed bank.** ⛔ Both logged **DISTRESS, not FAILURE** — the P04 count stays 3. Full rows in `workbook/COCKROACH.tsv`.

**FLOW-PHAN-06 full detail** *(exceeds parent KB-228 — carried here in full):*
- **Pathway:** BNPL originator tightens underwriting (headline DQ improves) → lower-quality cohorts routed to ABS trusts → ABS WA FICO declines → provisions grow faster than DQ (leading indicator) → ABS performance worsens as macro pressure hits the tail → structured-credit repricing → LIQUID/REGINALD vectors fire.
- **Mechanism:** composition masking at the BNPL level mirrors the ALLY auto analog — headline clean, hidden mix downgrade in the ABS structures, provision divergence betraying the loading.
- **Trigger (provision divergence from DQ headline): ACTIVE**, re-verified at SEC primaries 2026-09-11 — FY26 quarterly provision YoY **+1.8% → +40.0% → +33.5% → +42.5%**, Q4 outpacing Q4 GMV (+36%) by 6.5pp, NCO YoY accelerating monotonically to **+36.9%** while headline 30+ DQ *fell* to 2.5%. ⚠️ **Test this QUARTERLY, never on the FY aggregate** — the FY total (+29.2%) sits below the bar only because Q1 was flat, and reading it that way produced a wrong PARTIAL downgrade on 9/10.
- **Breakpoint: NOT met.** Leg 1 ✅. **Leg 2 (ABS WA FICO) WEAKLY MET AT BEST** — AFRMT 2026-4/5 (2026-09-09) at **670** vs 672 at AFRMT 2025-1, *but* Grade-A share **rose** 34.8%→36.7% and required CE **fell** at every class, which is the opposite of the routing prediction. Leg 3 ❌ (gas $4.277 vs $4.50). ⛔ Never splice the **amortizing** shelf's 681 (AAST 2026-X1) into the **revolving** master-trust series.

---

## 2.7 CFPB Rule 1033 — carried VERBATIM (audit must-carry)

> ⛔ **READ THE STATUS LINE BELOW FIRST.** The block that follows is an **Apr-2026 artifact**, retained verbatim because the DAEDALUS audit designated it a must-carry (*"the best writeup of this fact anywhere in the fleet"*). **Its framing was corrected on 2026-09-11 and is NOT current.**
>
> ### ✅ CURRENT STATUS (2026-09-11): **ENJOINED + UNDER RECONSIDERATION — not agency-withdrawn.**
> The CFPB **withdrew its request that the court vacate** Rule 1033 and **reopened the rulemaking** (ANPRM 2025-08-22, comments closed 2025-10-21; reconsideration covers the "representative" definition, **data-access fees**, and the security/privacy cost-benefit). The April-2026 compliance date is **stayed**, not killed. ⚠️ **"EFFECTIVELY DEAD" overstated it: a rewritten, fee-permissive 1033 is a live 2027+ branch** — and a fee-permissive rewrite would weaken phantom-debt visibility *even once effective*. Verified at three independent law-firm secondaries 2026-09-11.

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

⛔ **Two numbers in the verbatim block above are now wrong and must not be lifted from it:** the **"$40-60B distressed BNPL"** figure was derived from the refuted $400B base (see §2.0 — credit-only phantom debt **in total** is ~$30–60B, so a *distressed subset* of $40–60B is internally incoherent), and the **"EFFECTIVELY DEAD"** status is superseded above.

---

## 2.8 🔻 STRUCTURAL FIX OWED — why this rebuild was 42 days late

The rebuild was assigned in `KB-CARL-367` on **2026-07-31** and discovered on **2026-09-11**, by a gap review rather than by any mechanism. **PHAN had no way to know.** The assignment was written into CARL's KB Notes column; PHAN is dossier-mode, boots only on ad-hoc spawns, and reads its own directory. Three PHAN passes ran in between and none could have caught it.

**This will recur for any future CARL→PHAN assignment unless something changes.** Options for CARL/Will, in ascending cost:
1. **A standing `OWED.md` in PHAN's own directory** that CARL writes to when it assigns PHAN work — cheapest, and it puts the obligation on the surface PHAN actually reads.
2. **Route assignments as inbox packets** (`AGENTS/CARL/sub_agents/PHAN/inbox/`) — the lane exists, has a step-0 boot scan, and was built for exactly this in Aug-2026. **KB-367 should have been a packet.**
3. A boot-time grep of CARL's KB for `PHAN` in the Notes column — most robust, most machinery.

**Recommendation: (2), because the lane already exists and already has an enforced read step.** The Aug-2026 inbox build gave every CARL sub-agent an inbox precisely because *"the layer used to be write-only upward"* — and this is that failure, in the direction the build was meant to fix.


---

## 2.9 Sources + cadence (moved from `DOSSIER.md` §7, 2026-09-11, read-cap reclaim)

*Reference: which source answers which question, and on what cadence. Consulted when sourcing a figure, not at boot.*

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
