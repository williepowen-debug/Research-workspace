# PHANTOM CONSUMER DEBT — magnitude, bottom-up, reconciled (CARL prompt C4)

**Date:** 2026-07-28 | **Mode:** Thesis | **Confidence:** Medium-High on structure and denominators (primary-verified) / **Low-Medium on the dollar total** (its largest component rests on non-co-vintaged inputs)
**Prompt:** `AGENTS/DEWEY/inbox/2026-07-10_from-CARL_DEEP-RESEARCH-PROMPT-C4-phantom-debt-magnitude.md` (CARL slate T1-3, PHAN-proposed, Will-gated; queued 7/10, run 7/28)
**Consumers:** CARL (thesis premise + K-SHAPE methodology) · PHAN dossier §2 · LIQUID (off-book credit)

---

## Key Finding

**The $150–400B range survives — but only under a definition that includes unpaid medical *bills*, which are not credit. Under a credit-only definition the number collapses to roughly $30–60B, an order of magnitude smaller.** The composition is also nothing like what the range implied: **medical is ~85% of the total and BNPL ~15%**, with EWA negligible as a stock. And the premise the range exists to support — *"true bottom-60 leverage is 20–30% higher than reported"* — **is not supported at the aggregate level** (phantom ≈ **8–11%** of the relevant unsecured base) and reaches the bottom of that band only under a *combination* of the broad definition and a strong-concentration assumption I cannot measure.

**The more important structural result is definitional: "phantom" is not one thing.** There are **four independently binding visibility layers** — furnished → in the core file → in **Equifax** (which is what the NY Fed QHDC reads) → **scored**. A loan can be furnished and still absent from every aggregate statistic *and* invisible to underwriting. **Essentially all BNPL clears layer 1 and fails layer 4.**

---

## 1. The estimate

| Component | Low | High | Basis |
|---|---|---|---|
| **BNPL** (broad — incl. longer-term interest-bearing POS installment) | $25B | $33B | ~60–65% measured |
| **EWA / cash advance** (stock, not flow) | ~$1B | ~$3B | inferred; **no published stock figure exists** |
| **Medical — bureau-invisible** | ~$150B | ~$180B | illustrative, **not co-vintaged** |
| **TOTAL — BROAD** | **~$176B** | **~$216B** | central **~$195B** |
| **TOTAL — CREDIT-ONLY** *(excludes provider-held unpaid bills)* | **~$30B** | **~$60B** | |

**The fork matters ~4× more than the estimation error, so lead with it, not the point estimate.** The same is true one level down inside BNPL, where a definitional choice moves the answer 8×: **broad $25–33B vs pay-in-4-only $3.6–4.8B**.

### The number that should replace the stock estimate

The medical component is the bulk of the total and it is the weakest number in the report. A far better-founded metric exists, and CARL should prefer it: **CFPB priced the flows directly — ~$80.46B/yr of new medical debt accrues against only ~$36B/yr appearing on consumer reports.** That **~2.2× flow gap is a direct measurement of the invisibility rate**, co-vintaged and from a single primary source, rather than a stock subtraction across mismatched vintages and universes. [PRIMARY: CFPB final rule preamble, 90 FR 3276, 2025-01-14]

---

## 2. Why the medical number is weak — stated plainly

The ~$170B invisible figure subtracts a **June 2023** numerator ($49.2B visible) from a **December 2021** denominator ($220B total) **across two different universes** (bureau tradelines vs. household self-report). It is illustrative, not measured. **No co-vintaged estimate exists.** Honest statement: *the invisible share is large, on the order of three-quarters, and cannot currently be pinned tighter.*

**Two premise corrections to the prompt itself:**

- **⚠️ The prompt's "$88B (2021)" is the VISIBLE number, not the invisible one.** It is CFPB's estimate of medical debt **on** credit reports as of June 2021. Anyone citing it as phantom debt has the sign backwards. [PRIMARY: CFPB, *Medical Debt Burden in the United States*, Mar 2022]
- **CFPB expressly rejected using $220B as the affected inventory**, writing that *"the CFPB's $50 billion estimate is a better approximation of the relevant inventory of medical debt."*

**Legal status is settled and the prompt's framing is stale:** the CFPB rule barring medical debt from credit reports was **vacated in its entirety 2025-07-11** (*Cornerstone Credit Union League v. CFPB*, E.D. Tex. 4:25-cv-00016) and — verified against the docket — **not appealed**; the 60-day window lapsed ~2025-09-09. The government has since switched sides, issuing an interpretive rule that **FCRA preempts state medical-debt laws** (90 FR 48,710, 2025-10-28). **15 states covering 37.7% of the US population** ban medical debt from credit reports today; the first preemption test (*ACA Int'l v. Fulford*, D. Colo.) was **unresolved as of 2026-07-08**.

**State laws are actively converting visible debt into invisible debt** — Urban Institute *excluded seven states' medical debt data* from its 2025 Debt in America update because of these statutes. The phantom is becoming geographically concentrated.

---

## 3. The visibility layers — the structural core

| Layer | What it gates | BNPL status |
|---|---|---|
| 1. Furnished to any bureau | data exists | **Affirm: yes** (Experian 2025-04-01, TransUnion 2025-05-01, all products). **Klarna: term loans only — explicitly NOT pay-in-4.** Afterpay/PayPal/Zip: no evidence |
| 2. In the **core** file | lender can see on a full pull | Partly — bureaus built **specialty** files; CFPB: *"may not be reflected in traditional credit reports and credit scores"* |
| 3. In **Equifax** | in the QHDC / aggregate stats | **Affirm furnishes Experian + TransUnion, not Equifax** (probable, not established) |
| 4. **Scored** | constrains new credit | **No.** Klarna verbatim: *"will have no impact on your FICO / Vantage score and will only be visible to you at this time"* |

**⚠️ The trap: you cannot use one furnishing list for both operations.** "Invisible to the QHDC" needs the *Equifax* furnisher list; "invisible to lenders/scores" needs a different one. Conflating them double-counts or under-counts depending on direction.

**This inverts C4's own instruction.** The prompt says *"the phantom total must exclude anything now being furnished."* Applied literally that deletes Affirm's ~$16.5–17.5B — the single largest book — from a total whose purpose is to measure what lenders can't see, even though **none of it is scored and probably none of it reaches Equifax**. The instruction conflates layer 1 with layer 4.

**Source conflict, unresolved and flagged:** on whether furnished BNPL is visible to lenders pulling a full report, [PRIMARY] Experian says *"visible to lenders who request to view it"* while [INSTITUTIONAL] American Banker says *"only visible to consumers... not to other lenders"* and Klarna's own language says visible *"only to you."* These may all be right about **different bureaus**. Not resolved here.

---

## 4. The denominator — and why the thesis premise fails on it

**QHDC 2026:Q1** (balances as of **2026-03-31**, NSA; released 2026-05-12). Q2 not yet released — verified by HTTP status (Q2 path → 302, Q1 → 200), not by a search summary's silence.

| Denominator | Value | Phantom (broad ~$195B) | Phantom (credit-only ~$45B) |
|---|---|---|---|
| (A) Total household debt | **$18.80T** (72.5% housing) | 1.0% | 0.24% |
| (B) Non-housing | $5.162T | 3.8% | 0.9% |
| **(C) Unsecured base — card + other** | **$1.812T** ← **use this** | **10.8%** | **2.5%** |
| (E) Card only | $1.25T | 15.6% | 3.6% |

**(A) understates the ratio 10.4× versus (C).** A phantom-debt ratio quoted against total household debt is arithmetically true and analytically meaningless — 72.5% of that denominator is mortgages.

### Verdict on *"true bottom-60 leverage 20–30% higher than reported"*

**NOT SUPPORTED as stated.** Against the correct unsecured base the broad figure gives **~11%**, the credit-only figure **~2.5%**.

It reaches the bottom of the 20–30% band only by stacking two things: the **broad** definition (counting unpaid medical bills as leverage) **and** an assumption that phantom debt is heavily concentrated in the bottom 60%. That concentration is plausible — KFF finds 0.3% of adults hold over half of all medical debt, which cuts *against* simple bottom-60 concentration — but **I cannot measure it**, because no source decomposes phantom debt by income quintile. Illustratively, if the bottom 60% held ~45% of the unsecured base and ~80% of the phantom, the ratio would be ~19.6%.

**Revised premise, stated explicitly as C4 requires:** *Bottom-60 leverage is plausibly **5–20%** higher than reported, not 20–30%; the upper half of that range requires counting unpaid medical bills as debt, and the credit-only figure is low single digits.*

---

## 5. Counter-Evidence

**1. The strongest counter — invisibility may not matter for credit risk.** Duarte, Fonseca, Kohli & Reif (Illinois/NBER, **Jan 2026**) exploit the April-2023 $500 threshold as a regression discontinuity: deletion cut reported medical collections **61%**, yet they find *"no evidence of benefits over the subsequent two years, ruling out even small effects,"* and that medical debts *"regardless of size, add minimal incremental information for default prediction beyond standard credit report variables."* **If right, the ~$170B is a measurement gap, not a credit-risk gap**, and any thesis that lenders are flying blind on household stress *because of medical invisibility* is materially weakened. This must be read before the number feeds a position.

**2. A sitting Fed publication argues the opposite on BNPL.** Richmond Fed (EB 26-05, Feb 2026) puts pay-in-4 outstanding at **$3.02B** — *"much smaller amounts of outstanding debt and lower default rates… no clear evidence of elevated stress to date"* — with card debt *"roughly 400 times larger."* BNPL charge-offs **1.83% (2023)** vs card **4.19% (2023Q4)**; deep-subprime/no-FICO users repaid **96%** of the time. It is not wrong; it answers a narrower question. **Against it:** LendingTree 2025 finds **41% of users late at least once**, up from 34%.

**3. Longer-term BNPL may already be counted.** Richmond Fed asserts such loans *"are reported to credit bureaus… largely captured by credit scores and aggregate consumer credit statistics."* **Unverified.** If true, ~$16B of the ~$29B BNPL central is already inside existing aggregates and treating it as hidden double-counts. **This is the single most important open question for downstream use.**

**4. Secular decline predates policy.** Share of consumers with a medical collection fell 20% (2017) → 14% (Mar 2022) *independent of* the reporting changes. Some "growing phantom" is an old trend, not new policy.

**5. The geography could reverse.** If ACA wins in Colorado and the Oct-2025 interpretive rule carries weight, 15 state laws fall and up to 37.7% of the population moves *back* toward visibility — opposite the consensus direction.

---

## 6. De-double-counting — the rules that must be applied

1. **STOCK vs FLOW is the largest single error.** Headline BNPL ~$70B (2025) is *annual transaction volume*; summing it into a stock denominator **overstates ~23×**. Same trap one level down: the PayPal–Blue Owl **"$7B"** is a **two-year purchase flow**, not a $7B stock. And CFPB's **$45.2B** is **2023 originations** — routinely misquoted as a current balance. It is neither.
2. **Balance sheets capture only ~half of BNPL.** Affirm's on-BS gross HFI is **$8,573M** against an **$18.4B** platform portfolio — the balance sheet holds **47%**; ~$9.8B is sold/off-BS but **still owed by consumers**. Systemic: Klarna offloaded $1.6B in Q4'25; PayPal sold ~$7B of US pay-in-4 to Blue Owl. **Any estimate built from balance sheets alone understates by roughly half.** *(This corrects my own spine anchor: I had pulled Affirm's net on-BS $8.06B, which is 44% of the true consumer obligation.)*
3. **Never add credit-card-converted medical debt.** 17% of adults carry health-care debt **on a credit card** (KFF), plus CareCredit/Synchrony — already inside the $1.25T card aggregate. Adding it double-counts against both the card total and any survey-based medical figure.
4. **Medical trades are excluded from the QHDC by rule** — *"Our analysis excludes… medical trades"* — **even when they are on the Equifax report.** So "missing from QHDC" ≠ "not furnished." Two independent blind spots, not one.
5. **Category warning:** unbilled self-pay obligations are **not credit**. Including them converts "phantom credit" into "unpaid bills" — this is the fork in §1.
6. **Third-party collections sit outside the QHDC balance total**; counting a collection tradeline and the original obligation double-counts.
7. **Survey shares are not mutually exclusive** — consumers use multiple BNPL providers; KFF's medical categories overlap and **do not sum**.

---

## 7. G.19 vs QHDC — the reconciliation does NOT work. Report no gap number.

Like-for-like (**NSA, March 2026**, both verified by my own `fred_pull.py` run): G.19 total **$5,074.6B** vs QHDC non-housing **$5,162B** → QHDC exceeds G.19 by **~$87B (+1.7%)**.

**This must not be published as a phantom-debt gap, for three reasons:**

1. **The sign is wrong.** A furnishing gap predicts lender-surveyed G.19 **>** bureau-read QHDC. Observed is the opposite.
2. **FATAL — the blind spot is common-mode, so differencing cancels it.** The Fed says so itself: *"many of the major BNPL lenders are newly established non-bank lenders, where there is more limited coverage. Moreover, the G.19 is not currently able to separately track the volume of originations and outstanding balances of such loans."* [PRIMARY: Federal Reserve G.19 Technical Q&A #19] **Both series miss the same lenders.** This is `finding_spread_metric_blind_to_common_mode` exactly.
3. **Known wedges exceed the residual and run both ways** — charge-offs inflate QHDC (banks drop them, bureaus keep reporting them); student loans deflate it; category mismatches (retail revolving) and QHDC-only exclusions (medical, bankruptcy, inactive, no-SSN) have no G.19 analogue.

---

## Source Quality Assessment

**Strong:** QHDC construction and exclusions (NY Fed data dictionary, verbatim); G.19 methodology and its own BNPL coverage admission; Affirm figures (SEC XBRL/EDGAR, pulled directly); the FRED NSA series (my own run); the medical legal chronology (Federal Register + docket-verified); state population share (computed from Census PEP primary, not a secondary claim).

**Weak — and load-bearing:** the medical invisible total (non-co-vintaged, ~4-year-old inputs); all non-Affirm BNPL provider balances (derived); the entire EWA component; Affirm's Equifax non-furnishing (**probable, not established** — no Affirm or Equifax statement either way); FICO/VantageScore model treatment (**[UNVERIFIED]** — no primary reached).

**Anyone quoting a "2026 phantom debt number" is quoting 2021–2023 data.** That is the honest headline on vintage.

---

## Process Report

**Engines:** `/deep-research` **was not available in this session** (absent from the skills list), so this ran on the documented fallback — `scripts/` primary pull as the spine + 4 targeted sub-agent legs. Spine (DEWEY, direct): SEC XBRL via `edgar_doc.py` (Affirm, Dave), `fred_pull.py` (G.19 SA and NSA), plus direct WebSearch/WebFetch on furnishing status.

**Completeness-critic pass — the prompt's 5 required sub-answers:**
1. BNPL outstanding — ✅ answered, both definitions
2. EWA/cash advance — ⚠️ **PARTIAL.** Dave's receivables measured at primary ($279.1M @ 2026-03-31; $297.3M @ 2025-12-31). **No published EWA outstanding-stock figure exists anywhere** — vendor "market size" figures are revenue, not debt, and are unusable. The ~$1–3B is inferred from Dave's scale. **The dedicated EWA leg never delivered** (see below); this component is the weakest in the report and is explicitly banded rather than dropped.
3. Bureau-invisible medical — ✅ answered, with the premise correction
4. De-double-counting + reconciliation — ✅ answered; the G.19 reconciliation is answered **in the negative**, which is the correct answer
5. Denominator implication — ✅ answered; **premise revised downward**

**Two of my own inputs were corrected mid-run, both by a sub-agent, both verified by me afterward:**
- I pulled G.19 **seasonally adjusted at May-2026**; the QHDC is **NSA at March-2026**. Wrong basis for the comparison. Re-pulled NSA myself — the leg's figures matched to the dollar.
- I treated a **zero-hit grep for "credit bureau" in Affirm's 10-Q as a negative**. It is not — furnishing practice is not a 10-Q disclosure item. A [PRIMARY] Richmond Fed source affirms Affirm does furnish. **The leg explicitly refused to conform to my null, which is exactly what it was instructed to do.**

**Sub-agent delivery failure — all four legs went idle without delivering.** Three returned in full only after I messaged them directly; **one (EWA) exited entirely without ever reporting** and did not respond to two recovery requests. Had I accepted the idle notifications as completion, this report would have shipped with three legs silently missing. *(This is `finding_idle_notification_is_not_a_result` recurring at n=4-of-4 in a single session.)*

**Data gaps / frustrations:**
- `newyorkfed.org`, `richmondfed.org`, `federalreserve.gov` and `sec.gov` **all 403 on WebFetch**; **curl/urllib with a browser UA returns 200**. Same class as the known SEC blocker. This blocked the two most important sources in the run.
- **S&P ratings pages 403 even with a declared UA** — a true bot-block, unlike the above (separate finding, routed to Will with the entitlements spec).
- FICO primary unreachable (WebFetch timeout; curl `HTTP/2 INTERNAL_ERROR`).
- CourtListener docket endpoint 403s; the public search API works.
- **Caught and killed a wrong-but-attractive claim:** G.19 `about.htm` states a **December 2010** finance-company benchmark, which would be damning for BNPL coverage. That page is **stale documentation** — Q&A #20 confirms the 2020 Census of Finance Companies completed Aug 2023, benchmarked to June 2021. **Do not cite 2010.**

**Suggestions (→ BACKLOG):** build `scripts/fetch_url.py` — curl + browser UA + HTML→text strip, with an `--http1.1` fallback. This is now the **3rd+ recurrence** of the same 403 class (SEC done; Fed research pages and NY Fed new) and a leg hand-rolled it three times in one session. Also worth adopting as a technique: **establishing "not yet released" by HTTP status** (302 vs 200) rather than trusting a search summary's silence.

**Confidence:** Medium-High on structure, denominators and legal status. **Low-Medium on the headline dollar total** — its largest component is not co-vintaged, and its second-largest is ~35–40% derived.
