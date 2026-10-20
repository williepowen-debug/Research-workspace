# THE AI-CREDIT GUARANTEE WEB — who legally bears credit risk, where the cross-links are, and what binds first

**Date:** 2026-08-02 | **Mode:** Thesis | **Confidence:** High on filed figures (all SEC-primary, pulled this session) / Medium on the announced-not-filed layer / Medium on the S&P action (secondary — see Source Quality)
**Commission:** WALTER DR-1, ledger `REQ-DEWEY-20260731-001` (Will-approved slate 7/30) | **Deadline:** ~8/8 — delivered 8/2
**Consumers:** VULCAN (action) · LIQUID / BROCK / HENRY (info)

---

> ## 🔴 ADDENDUM 2026-08-02 (same session, ~2h after first delivery) — I CLOSED MY OWN DATA GAP AND IT PRODUCED THE LARGEST NUMBER IN THIS DOMAIN
>
> My Process Report flagged ORCL's *"lease commitments that have not yet commenced"* as an unextracted gap. **I went back for it. It is $260 billion**, and it changes the weight of this report's central claim — so it is stated here at the top rather than buried in a revision note.
>
> > "As of May 31, 2026, we had **$260 billion of additional lease commitments, substantially all related to data center arrangements**, that are generally expected to **commence between the first quarter of fiscal 2027 and fiscal 2029** and for terms of **fifteen to nineteen years**, that **were not reflected on our consolidated balance sheet** as of May 31, 2026 or in the maturities table above. These additional lease commitments include **a lease for which we have guaranteed up to $3.3 billion of the lessor's borrowing, which matures in September 2026.**" [PRIMARY: ORCL FY2026 10-K, Note 9 / Commitments]
>
> **Three consequences:**
> 1. **The obligations substrate is far larger than the first pass concluded, and it is overwhelmingly ORCL's.** $260B off-balance-sheet dwarfs META's ~$41B RVGs (6×), ORCL's own $129.5B of debt (2×), and NVIDIA's entire filed guarantee book (74×). **My original framing — "large but sitting at ORCL (rating) and META (RVG)" — understated ORCL by an order of magnitude.** The verdict direction is unchanged and strengthened; the magnitude was wrong.
> 2. **There IS a filed guarantee in the AI chain after all — just not NVIDIA's.** ORCL has **guaranteed up to $3.3B of a lessor's borrowing, maturing September 2026.** That is a real, filed, third-party credit guarantee with a near-term date, and it is ~94% the size of NVIDIA's entire guarantee book. **It is the most concrete near-dated item this run found and nobody was tracking it.**
> 3. **It explains the S&P action far better than the debt alone.** A BBB- issuer with −$23.7B FCF is contractually committed to $260B of 15-to-19-year data-center leases that begin hitting the balance sheet **in FY2027 — i.e. now.**
>
> **Also newly extracted, same gap-closing pass:**
> - **ORCL's capitalized leases more than doubled:** total operating lease liabilities **$30,190M** (from $13,450M, **+124%**); total finance lease liabilities **$7,701M** (from $2,934M, **+162%**) — **$37.9B combined, +131% YoY**. ROU assets obtained in exchange for lease obligations in FY26: **$18,246M** operating + **$4,946M** finance. Weighted-average operating lease term **12 years at 5.7%**.
> - **⇒ ORCL's total obligation stack is ~$167B on balance sheet ($129.5B debt + $37.9B leases), plus $260B committed off it.**
> - ORCL's unconditional purchase obligations are **"primarily related to data center power arrangements"** — power is contracted as a credit obligation, echoing CoreWeave's power-cost hedging covenant.
> - **Subsequent to 2026-05-31, ORCL entered an additional $19B of unconditional purchase commitments** for cloud infrastructure, commencing FY2027, five-year term — i.e. the commitment stack grew again after the balance-sheet date.
> - **CRWV RPO = $98.8B** unsatisfied as of 2026-03-31 (36% recognized within 24 months, 39% months 25–48). Against $24.9B of debt and 65% of revenue in two customers.
>
> *Method note, stated against myself: this was in the filing the whole time and my first pass cited the MD&A cross-reference instead of following it into Note 9. **A "data gap" I could close in four minutes was not a gap, it was an unfinished read.** The lesson is narrower than "read more" — when a filing's MD&A says "refer to Note N," the number is in Note N, and stopping at the cross-reference produces a confident report with a hole in it.*

> ## 🔴 ADDENDUM 2 (2026-08-02, same session) — I READ THE DDTL 4.0 CREDIT AGREEMENT, AND IT CORRECTS MY OWN HEADLINE MECHANISM
>
> The agreement is filed — **Exhibit 10.1 to CRWV's 8-K of 2026-03-31** (acc. `0001769628-26-000129`), 545KB of text, **124 redactions** under Item 601(b)(10). I had called it "the highest-value unread document in this domain." Having read it, **it does not say what I said it says**, and the correction runs against my own most-promoted finding.
>
> ### ❌ What I got wrong
> I wrote — and routed to VULCAN as action-relevant — that CoreWeave's *"borrowing base is tied to GPU depreciable cost, so if server useful lives compress or GPU carrying values fall, borrowing capacity contracts mechanically,"* calling it "a filed, hard link between VULCAN-07/08 and financing capacity" and "the cleanest transmission channel found in this run." **That over-read the 10-Q's summary.** The agreement's actual terms:
>
> - **The advance rate is 90% of COST, not of carrying value.** *"**'Funding Date GPU Amount'** shall mean… the sum of (a) the product of (x) **90%** and (y) **Funding Date Capital Expenditures**"* — where Funding Date Capital Expenditure is the **aggregate purchase price** of Infrastructure plus installation costs (sub-caps redacted). **That is a point-in-time loan-to-cost test struck at funding. A later fall in GPU carrying value does NOT mechanically shrink an already-drawn facility.**
> - **Depreciated value enters in exactly one narrow place:** `Permitted Transferred Equipment` requires that *"the purchase price… is calculated based on a **net depreciated fair market value**"* — i.e. only for equipment **transferred in** from affiliates, not for the book generally.
>
> ### ✅ What the binding mechanism actually is — cash flow, not asset value
> All three debt-sizing definitions (`Commitment Termination`, `Delayed Tranche`, `Top-Up Debt Sizing Amount`) resolve to the same test: **Projected Debt Service Coverage Ratio ≥ 1.20:1.00**, measured **for each Monthly Date from the calculation date through Term Maturity**, as set forth in the **Base Case Model**. Separately, the maintenance covenant is **DSCR ≥ 1.15:1.00** on the trailing three fiscal months, as of any Monthly Date, commencing after the Commitment Termination Date.
>
> **⚠️ Two different DSCR numbers, and my report carried only one.** The 8-K summary gives 1.15x; **the 1.20x sizing test is stricter, applies earlier, and is the one that governs how much can be drawn.**
>
> **A forward-looking prepayment trigger I had no visibility into:** a **"Negative NOI Event"** — if projected Net Operating Income for a Delayed Data Center Site is projected below $0, loans must be repaid **two calendar months *before* the first negative month**, in an amount that restores projected NOI to ≥$0. **This bites on a projection, not on a realized breach.**
>
> ### 🔑 The real transmission channel is POWER, not depreciation
> The `Top-Up Model Adjustment Criteria` specify exactly what the Base Case Model is re-marked for: (a) actual interest-rate hedge strike rates and prevailing SOFR on unhedged amounts, and (b) **power** — *"starting with the **Modeled Power Costs**, with adjustments based on (i) the actual quantum and strike price for such Power Costs as per the applicable **Permitted Commodity Agreement(s)** and (ii) for all other unhedged power costs, the greater of (1) the average actual Power Costs for the most recently completed three calendar [months]…"* There is a dedicated **§5.25 Power Cost Protection** covenant requiring commodity hedges over at least [*] of modeled energy utilization, a defined term **"Excess Unhedged Power Costs"**, and **§5.23** requiring interest-rate hedges on **≥95%** of anticipated floating principal within 45 days of the Commitment Termination Date.
>
> **⇒ Power price → Modeled Power Costs → Projected DSCR → borrowing capacity and mandatory prepayment. That is the filed, mechanical link — and it runs to WATT/AEOLUS, not to the depreciation question.** The DR-2 link I claimed is real only in the weak, one-time sense that cost at funding sets the 90% advance.
>
> ### 🔴 "Non-recourse" is not symmetric — the parent is wired in three ways
> 1. **`Cash Trap Event` = (a) a material breach of the Master Services Agreement giving rise to termination rights by [*] or the Borrower under §11b of the MSA; *or* (b) **Parent becomes subject to a Bankruptcy Event.*** On a Cash Trap Event, cash is diverted to the Cash Trap Account at position **seventh** in the monthly waterfall. **A CoreWeave *parent* bankruptcy traps cash inside the "non-recourse" SPV.**
> 2. **A `Limited Guarantee` from the Parent** for specified **"bad acts"** (Exhibit 10.2) — standard bad-boy carve-outs, which is what the 10-Q's "customary non-recourse carve-out obligations" refers to.
> 3. **Change-of-Control cascades the full chain:** Parent → **CoreWeave Debt Holdco I, LLC** → Pledgor (**CCAC VIII Holdco LLC**) → CCAC VIII, each requiring 100% ownership.
>
> ### The counterparty is redacted, and the facility is built around one contract
> The customer is `[*]` **throughout** — including the defined term **`"[*] Purchase Order"`** and the acceptance of Infrastructure by `[*]` under the **Master Services Agreement**. The 8-K states the facility was entered *"primarily to finance capital expenditures required to perform **a customer contract**"* — **singular**. So an $8.5B facility is sized off, and cash-trapped by, **one redacted counterparty's MSA.** Given Customer A is 45% of CRWV revenue, the identity is inferable but **not filed — I am not asserting it.**
>
> *Method note: this is the second correction this session where the primary document contradicted a summary I had relied on — first the MD&A cross-reference hiding $260B, now a 10-Q covenant summary that compressed "purchase price of eligible assets… depreciable cost… projected debt service coverage… project-level conditions" into a list, from which I promoted the wrong element to headline. **The 10-Q sentence was accurate; my ranking of its clauses was not.** `[[finding_verify_reader_before_source]]` — but pointed at a summary rather than a tool.*

## Key Finding

**The headline guarantee is not filed anywhere, and the thing that actually binds is not a covenant — it is a rating threshold that has already been crossed.** NVIDIA's *entire* filed facility-lease-guarantee exposure, across all counterparties, is **$3.5B gross / ~$2.8B net of escrow** [PRIMARY: NVDA FY26 10-K + Q1 FY27 10-Q] — roughly **1.4% of the $250B OpenAI backstop reported on 2026-07-27**, which appears in **no** NVIDIA filing and which NVIDIA's own most recent 10-Q does not mention at all. Meanwhile the real, filed obligations substrate is large but sits elsewhere: **META has ~$41B of off-balance-sheet residual value guarantees and explicitly no financial covenants**; **ORCL carries $129.5B of debt against a −$23.7B annual funding gap**, and its revolver covenant (interest coverage ≥3.0x) is nowhere near binding at **7.83x** — but **S&P's 4x leverage trigger is already breached in S&P's own FY27 forecast (mid-4x)**, which is why ORCL sits at **BBB-, one notch above junk**, and why ORCL's 10-K warns a downgrade would raise **collateral and credit-support requirements** and affect **data-center lease terms**.

**For VULCAN's decision: the credit-contagion frame does not weaken — but it relocates.** It is not a vendor-guarantee story (NVDA's exposure is de minimis and unsigned). It is a **rating-migration story at ORCL** and an **off-balance-sheet residual-value story at META**, with the genuine cross-collateral machinery ring-fenced inside CoreWeave's non-recourse SPVs where the *lenders*, not the parent, hold the asset risk.

---

## Evidence

### 1. The NVDA→OpenAI $250B structure: announced, not filed — and the gap is ~70×

| What | Amount | Source | Date |
|---|---|---|---|
| Reported NVDA→OpenAI lease/debt backstop | **~$250B** ("in talks") | [NEWS: WSJ via CNBC/Yahoo/Tom's Hardware] | 2026-07-27 |
| Reported additional chip-purchase financing | up to ~$350B (discussed) | [NEWS: same cluster] | 2026-07-27 |
| **NVDA's total FILED facility-lease guarantees, all counterparties** | **$3.5B max gross** | [PRIMARY: NVDA FY26 10-K, acc. 0001045810-26-000021] | filed 2026-02-25 |
| — less partner escrow | −$712M → **~$2.8B net** | [PRIMARY: same] | |

NVDA's filed language, verbatim and **identical in both the FY26 10-K and the Q1 FY27 10-Q** (i.e. unchanged as of the 2026-04-26 balance-sheet date):

> "In fiscal year 2026, we entered into agreements to guarantee partners' facility lease obligations in the event of their default **in exchange for warrants**. The maximum gross exposure under all agreements is **$3.5 billion**, which is reduced as the partners make payments to the lessors over terms ranging from 5 to 7 years. The partners have placed **$712 million in escrow** to mitigate our potential exposure. The guarantees, **classified as credit derivatives** with changes in fair value recognized in Other income (expense), net, **were not material**."

Three structural points a consumer should not miss:
- **The counterparties are unnamed "partners," plural.** Nothing ties this $3.5B to OpenAI specifically.
- **NVDA books these as credit derivatives, not contingencies** — so they are already fair-valued through earnings, and NVDA states the amounts are immaterial.
- **The escrow is the tell.** Partners posting $712M against $3.5B is a ~20% first-loss cushion. Nothing of that shape has been reported for the $250B structure.

**On the OpenAI relationship itself, the filings are weaker than the press:** NVDA's FY26 10-K says twice — once as a risk factor, once in Liquidity — *"We are **finalizing** an investment and partnership agreement with OpenAI. There is **no assurance** that we will enter into an investment and partnership agreement with OpenAI or that a transaction will be completed."* **The Q1 FY27 10-Q (filed 2026-05-20) does not mention OpenAI at all** — 0 occurrences, verified against controls (the same document returns hits for "Revenue" and the guarantee note, so this is a true negative, not a failed read).

**Timing reconciles this without any contradiction, and that is the point:** the $250B was reported **2026-07-27**, ten weeks *after* NVDA's last periodic filing. **The first filing that could capture it is NVDA's Q2 FY27 10-Q, due ~late August 2026.** Until then, the correct statement for any downstream model is: *the $250B is an unexecuted negotiation, and NVIDIA has filed no obligation resembling it.*

The reported mechanism, if it is ever signed, is **credit substitution**: OpenAI lacks an investment-grade rating, so NVIDIA's balance sheet would stand in for one, letting lenders price the debt against NVIDIA's credit rather than the borrower's [NEWS: CNBC 7/27]. That is the single highest-value thing to watch for in the August 10-Q — **not the headline number, but whether any of it lands in the "credit derivatives" line, and whether an escrow/first-loss cushion travels with it.**

### 2. ORCL: the binding constraint is the rating, not the covenant

*All figures [PRIMARY: ORCL FY2026 10-K, acc. 0001193125-26-277521, filed 2026-06-22, FY ended 2026-05-31] unless noted.*

**The covenant, located and quantified.** ORCL's Revolving Credit Agreement carries exactly one financial maintenance covenant:

> "the ratio of 'Consolidated EBITDA' to 'Consolidated Net Interest Expense' … **shall not be less than 3.0 to 1.0** at the end of any fiscal quarter"

ORCL states it "was in compliance with all debt-related covenants at May 31, 2026." Computing the headroom from the FY26 statements:

| Component | FY2026 ($M) |
|---|---|
| Operating income | 20,606 |
| + Depreciation | 7,623 |
| + Amortization of intangibles | 1,671 |
| **= EBITDA (GAAP proxy)** | **29,900** |
| Interest expense | 4,599 |
| − Interest income | 780 |
| **= Net interest expense** | **3,819** |
| **Coverage** | **7.83x** vs 3.00x floor |

**Headroom:** EBITDA would have to fall **−61.7%**, or net interest rise **+161% (+$6.1B)**, before this covenant binds. Even assuming the entire FY26 issuance were fully seasoned with zero of its coupon already in FY26 interest expense — a deliberate worst-case bound — coverage only falls to **~4.82x**. ⚠️ **This is a GAAP proxy: "Consolidated EBITDA" and "Consolidated Net Interest Expense" are defined *in the credit agreement*, not by GAAP, and those definitions typically permit add-backs that would raise the ratio further.** So 7.83x is if anything conservative. **Conclusion: the revolver covenant does not bind in FY2027 on any plausible path.**

**What does bind is the rating.** [INSTITUTIONAL/NEWS — see Source Quality] On **2026-07-09** S&P lowered ORCL to **BBB-/A-3 from BBB/A-2**, outlook stable — the lowest investment-grade tier, one notch above sub-IG — citing AI-datacenter capital intensity, cash burn, and OpenAI concentration, and stating S&P-adjusted leverage reaches **mid-4x in FY2027 against a 4x downgrade trigger.** That threshold is *already* breached prospectively, whereas the contractual covenant is at less than half its limit. **The rating is the live constraint by a wide margin.**

And ORCL itself documents the transmission, in its own risk factors:

> "A downgrade could also reduce our access to, or increase the cost of, commercial paper or other short-term financing, **affect the terms or availability of certain long-term commitments (including data center leases)**, limit eligibility to contract with certain customers, and **increase collateral, letter of credit or other credit support requirements under certain contractual arrangements.**"

This is the closest thing in the entire chain to a cross-default link: **not a cross-default clause, but a rating-triggered collateral-call channel**, disclosed by the issuer, at an issuer one notch from losing IG.

**Why the pressure is structural, not cyclical — the funding gap:**

| FY2026 flow | $B |
|---|---|
| Cash from operations | **+32.0** |
| Capital expenditures | **−55.7** |
| **Free cash flow** | **−23.7** |
| Funded by: net senior notes | +42.7 |
| Mandatory Convertible Preferred | +5.0 |
| Short-term financing related to capex (vendor/supplier financing) | +3.3 |
| Ampere and other investment sales | +4.9 |

ORCL issued **$43.0B par of senior notes in FY2026** (vs $14.0B in FY2025) across 13 tranches at a **~5.62% weighted-average coupon**, ranging 4.45% (Sep 2030) to **6.85% (Feb 2066)**. Total indebtedness **$129.5B**, maturing CY2026→CY2066. Interest expense rose **+28.5% YoY** ($3,578M → $4,599M). Carrying value of senior notes and other LT borrowings **$128.1B against a $114.4B fair value** — ⚠️ *do not read that ~11% discount as pure credit: these are very long-duration fixed-rate notes in a rising-long-rate tape, and the FY2025 ratio was similar ($90.3B vs $81.3B). The discount is mostly duration.*

**The concentration is real but invisible where you would look for it.** ORCL's **remaining performance obligations jumped $138B → $638B** in one year — a **4.6×** increase "primarily attributable to certain significant cloud contracts" — with only **12% expected to convert to revenue in the next twelve months**. S&P estimates **roughly half of that $638B is OpenAI** [secondary]. Yet ORCL's 10-K states: *"**No single customer accounted for 10% or more of our total revenues** in fiscal 2026, 2025 or 2024."* **Both statements are true and they do not conflict** — the revenue-concentration disclosure keys on *recognized revenue*, and the backlog has barely begun converting. **Any screen for customer concentration that reads the revenue-concentration line will return a clean result on the most concentrated backlog in the company's history.** ORCL discloses the exposure in prose instead:

> "The economic returns on these investments are dependent on customer demand and **the ability of our key customers to meet their contractual obligations.**"

**A financing-mix signal that post-dates the 10-K and confirms the read:** on **2026-06-23** — two weeks after the 10-K, two weeks *before* the downgrade — ORCL filed a 424B5 supplementing a **$20B at-the-market common-equity program**, adding **15 new sales agents** to the original 5 [PRIMARY: acc. 0001193125-26-278585]. Combined with the $5.0B Mandatory Convertible Preferred in FY26, **ORCL's financing mix is rotating from debt toward equity and hybrids exactly as the rating hits its floor.** That is what a company does when it is out of debt headroom at an acceptable rating, and it is a leading indicator the covenant math will never show.

### 3. META: the largest off-balance-sheet guarantee in the chain, and zero covenants

*[PRIMARY: META Q2 2026 10-Q, acc. 0001628280-26-050705, filed 2026-07-30, period ended 2026-06-30]*

| Item | Amount |
|---|---|
| May 2026 senior unsecured notes issued | **$25.00B** par, six series, 4.55%–6.45%, maturing 2031–2066 |
| — net proceeds | **$24.91B** |
| Total notes outstanding | **$84.00B** (from $59.00B at 2025-12-31) |
| Future interest obligations | $4.40B short-term + **$84.98B long-term** |
| Capex, six months | **$50.92B** |
| Cash from operations, six months | +$64.09B |
| **Residual value guarantees — Venture 1** | **~$28B aggregate threshold**, declining over time |
| **Residual value guarantees — Venture 2** (closing Q3 2026) | **~$13B maximum aggregate** |

Two findings matter more than the headline raise:

**(a) There are no financial covenants at all.** META states plainly: *"**We are not subject to any financial covenants under the Notes.**"* Unsecured, pari passu across series, redeemable at META's option. **There is nothing here to bind.** Any model looking for a covenant tripwire at META is looking for something that does not exist — the discipline is entirely rating- and market-access-driven.

**(b) ~$41B of residual value guarantees is the real obligations substrate — and it is off balance sheet.** The Venture-1 data-center campus leases *commence in 2029* with an aggregate initial lease commitment of **~$12.31B** (four-year initial terms, renewable to 20 years), against which META has provided RVGs with an **~$28B aggregate threshold**. A second venture closing in Q3 2026 adds **~$13B**. **These are contingent obligations tied to the residual value of data-center assets** — i.e. META has written what is economically a put on data-center property values, at a scale ~11× NVIDIA's entire filed guarantee book. **Note the maturity mismatch: the notes fund capex today; the RVG exposure peaks from 2029.**

> **⚠️ Confirmed a suspected relabeled-number trap, negative result.** The commission cites "META's $24.9B raise." CoreWeave's *total debt* is **$24,859M** — a near-identical figure. I checked whether these had been conflated somewhere upstream: **they have not.** META's $24.91B is the genuine **net proceeds** of a $25.00B par issue, stated in META's own cash-flow discussion. The collision is coincidence. Both figures stand.

### 4. CoreWeave: where the cross-collateral machinery actually is — and it is ring-fenced

*[PRIMARY: CRWV Q1 2026 10-Q, acc. 0001769628-26-000222, filed 2026-05-08, period ended 2026-03-31]*

**Total debt $24,859M**, up from $21,373M at 2025-12-31 (**+16% in one quarter**); non-current portion $17,312M. Interest expense **+103% YoY**. The delayed-draw term-loan stack, with stated rates:

| Facility | Maturity | Rate | Outstanding ($M) |
|---|---|---|---|
| DDTL 1.0 | Mar 2028 | **15%** | 1,438 |
| DDTL 2.0 | Aug 2030 | 11% | 4,425 |
| DDTL 2.1 | Mar 2031 | 9% | 3,000 |
| DDTL 3.0 | Aug 2030 | 9% | 1,700 |
| DDTL 4.0 *(non-recourse)* | Mar 2032 | 7% | 1,260 |

**The DDTL 4.0 structure is the answer to "where are the cross-collateral links."** An **$8.5B** facility (≈$4.5B floating at SOFR+2.25%, ≈$4.0B fixed at UST+2.00%), MUFG as administrative agent, drawable through 2027-06-30 — held not at CoreWeave but at a subsidiary, **CoreWeave Compute Acquisition Co. VIII, LLC ("CCAC VIII")**. It is:

- **Secured** by first-priority pledges of *the equity interests of CCAC VIII* **and substantially all of CCAC VIII's assets**;
- **Non-recourse to the parent**, "except for limited guarantees related to customary non-recourse carve-out obligations";
- **Debt-sized against "the depreciable cost of computing equipment, projected debt service coverage and project-level conditions."**

**That third clause is the most important sentence in this report for VULCAN.** CoreWeave's borrowing capacity is a direct function of **GPU depreciable cost**. If server useful lives shorten or GPU carrying values fall, the borrowing base contracts *mechanically* — no covenant breach required. **This is a hard, filed link between the depreciation question (VULCAN-07 / commission DR-2) and financing capacity in the AI-credit chain**, and it is the cleanest transmission channel found in this run.

Additional binding terms — and unlike ORCL and META, **these actually bind now**:
- **Restricted-cash maintenance**: forward-looking three-month coverage of scheduled interest, principal, swap settlements and opex.
- **Mandatory hedging**: interest-rate hedges covering **≥95%** of anticipated floating borrowings, **plus power-cost hedging requirements** — a filed acknowledgment that power price is a credit variable.
- Standard incurrence covenants (additional debt, liens, distributions, asset sales, affiliate transactions, mergers).
- 0.50% undrawn fee; $142M capitalized deferred financing costs.

**Counterparty concentration is the tail risk:**

| | Q1 2026 | Q1 2025 |
|---|---|---|
| Customer A, % of revenue | **45%** | 72% |
| Customer B, % of revenue | **20%** | <10% |
| Accounts receivable | A 39% · B 17% · C 22% (**78% in three**) | A 68% · D 11% |

**Two customers are 65% of revenue against $24.9B of debt.** Diversification is improving (A: 72%→45%) but the absolute concentration remains extreme relative to the leverage.

**CoreWeave is also a lender**, which is the vendor-financing leg pointing the other way: a **$305M** senior secured delayed-draw facility to a data-center service provider at **13.00%** for seven years, secured on the provider's critical infrastructure. Plus JV exposure of **$95M** (contingent-consideration guarantee) + $32M lease prepayment + **up to $200M** of construction funding if the JV cannot secure third-party financing.

---

## The chain, assembled

| Node | Filed obligation | Off balance sheet | Security | Financial covenant | What binds first |
|---|---|---|---|---|---|
| **NVDA** | $3.5B gross guarantees ($712M escrowed) | — | Warrants received; escrow | — | Nothing. Immaterial and unsigned. |
| **META** | $84.0B notes | **~$41B residual value guarantees** | **Unsecured** | **None — stated explicitly** | Rating / market access only |
| **ORCL** | $129.5B debt + **$37.9B capitalized leases**; −$23.7B FCF | **$260B data-center lease commitments** (commence FY27–FY29, 15–19yr terms) **+ $3.3B guarantee of a lessor's borrowing, matures Sept 2026** | Unsecured | EBITDA/net-int ≥3.0x — **at 7.83x** | **The S&P 4x leverage trigger — already breached prospectively at BBB-** |
| **CRWV** | $24.9B debt, 7–15%; $98.8B RPO | — | **Secured SPV, non-recourse *except* a parent "bad acts" Limited Guarantee — and a parent Bankruptcy Event triggers a Cash Trap** | **Sizing: Projected DSCR ≥1.20x** (Base Case Model) · **maintenance DSCR ≥1.15x** · advance **90% of COST** at funding · ≥95% rate hedge · §5.25 power hedge | **DSCR failing on power costs or customer-contract cash flows** — plus a Negative-NOI forward prepayment trigger |

**The off-balance-sheet column is the story.** On-balance-sheet, the four names look like ordinary levered technology issuers. The AI-specific exposure lives almost entirely in the column that no leverage ratio computes: **ORCL's $260B of committed-but-uncommenced data-center leases is 2× its entire funded debt**, and it begins converting **in FY2027**.

**Who legally bears the credit risk?** It is stratified, and the answer inverts the headline. The *vendor* (NVDA) bears almost none of what is claimed. The *hyperscalers* bear it through unsecured debt with no covenants and large off-balance-sheet residual-value guarantees (META). The *intermediary* (ORCL) bears it as counterparty concentration in a backlog its own concentration disclosure cannot see, disciplined by a rating rather than a contract. The *pure-play* (CRWV) has pushed it into SPVs the lenders secure and size off **projected cash flow (DSCR 1.20x/1.15x), not asset value** — they have priced that at 7–15%, and the ring-fence is **one-way**: a parent bankruptcy traps the SPV's cash, while SPV losses stay off the parent (bad-acts guarantee aside).

---

## Counter-Evidence

**Arguing against the credit-contagion frame:**
1. **No covenant in this chain is close to binding.** ORCL 7.83x vs 3.0x; META has none; NVDA's guarantees are immaterial. The only live constraints are CoreWeave's borrowing base and restricted cash — at the smallest entity. A model expecting a covenant cascade will wait a long time.
2. **ORCL remains investment grade with a *stable* outlook**, and its coverage is strong on the contractual test. BBB- is not distress.
3. **Every issuer here retains market access on evidence, not assertion** — META raised $25B in May 2026, ORCL $43B across FY26, CoreWeave grew debt 16% in a quarter, all at completed pricings.
4. **The $250B is not an obligation.** Treating it as one would be the single largest error available in this domain right now. It is a reported negotiation with no filed counterpart.
5. **META's $41B RVG is a *threshold*, not an expected loss** — it declines over time, and payment requires META to terminate or decline renewal *and* other conditions to be met. Maximum exposure ≠ expected exposure.
6. **HENRY's equity-side leg is already falsified 2-2** (GOOGL/META punished, MSFT/AMZN rewarded), so an equity-de-rate thesis does not get support from this substrate either.

**Arguing for it:**
1. **The rating threshold is already breached prospectively** (mid-4x vs 4x) at an issuer one notch above sub-IG, and ORCL discloses that a downgrade triggers collateral and credit-support calls and affects data-center lease terms. That is a real, filed, non-linear channel.
2. **ORCL's −$23.7B annual FCF gap is structural** and must be refinanced at rating-linked pricing (revolver margin 87.5–150bp *by rating*).
3. **CoreWeave's borrowing base is levered to GPU depreciable cost** — a mechanical, covenant-free tightening channel if useful lives compress.
4. **Concentration is genuinely mismeasured**: ~50% of a $638B backlog vs a "no customer ≥10% of revenue" disclosure.

**What would disprove the finding:** NVDA's Q2 FY27 10-Q (~late Aug 2026) disclosing an executed OpenAI guarantee at anything near $250B with no escrow or first-loss cushion would overturn the "de minimis and unsigned" conclusion outright. Conversely, ORCL's Q1 FY27 10-Q (~Sept 2026) showing the RPO converting on schedule with S&P-adjusted leverage under 4x would remove the only threshold in the chain that is currently breached.

---

## Source Quality Assessment

**Strong.** Every load-bearing figure in §§1–4 is **[PRIMARY]** — pulled from SEC filings this session via `scripts/edgar_doc.py` and `scripts/fetch_url.py`, with accession numbers and period-end dates stated inline. Nothing load-bearing rests on a republisher.

**The one weak link, flagged explicitly:** the **S&P downgrade** (BBB-/A-3, 2026-07-09, mid-4x vs 4x trigger, ~half of RPO attributed to OpenAI) is **[NEWS/INSTITUTIONAL], secondary — n=5 consistent outlets, but I could not read S&P's own release.** `spglobal.com` is a **true bot-block** (403 even with a declared browser UA — not UA-fixable; verified again this session, and the new helper now refuses that host by design rather than retrying). **Per PROME's 2026-07-31 ruling this is exactly the paste-path case: if the precise S&P language is decision-load-bearing for VULCAN, Will pastes the page.** The direction and the date are corroborated across five outlets and are consistent with ORCL's own disclosed rating-sensitivity language, so I am comfortable citing it as secondary — but **the "roughly half of RPO is OpenAI" figure is S&P's estimate relayed by press, and should not be treated as an ORCL-disclosed number.** ORCL names no customer anywhere in the 10-K.

**The $250B reporting** is **[NEWS]** — WSJ-originated, relayed by CNBC/Yahoo/Tom's Hardware/TNW. Consistent across outlets, all tracing to one WSJ report. Single-origin, and labeled as such: **it is a lead, not a fact.**

---

## References

*SEC primaries (all fetched 2026-08-02):*
- NVDA FY2026 10-K — acc. `0001045810-26-000021`, filed 2026-02-25, FY ended 2026-01-25
- NVDA Q1 FY2027 10-Q — acc. `0001045810-26-000052`, filed 2026-05-20, period ended 2026-04-26
- ORCL FY2026 10-K — acc. `0001193125-26-277521`, filed 2026-06-22, FY ended 2026-05-31
- ORCL 424B5 (ATM equity) — acc. `0001193125-26-278585`, filed 2026-06-23
- META Q2 2026 10-Q — acc. `0001628280-26-050705`, filed 2026-07-30, period ended 2026-06-30
- CRWV Q1 2026 10-Q — acc. `0001769628-26-000222`, filed 2026-05-08, period ended 2026-03-31

*Reproduction recipe (no ephemeral paths cited):*
```
python3 AGENTS/DEWEY/scripts/edgar_doc.py doc --cik <CIK> --accession <ACC> --grep "<term>"
python3 AGENTS/DEWEY/scripts/fetch_url.py "https://data.sec.gov/submissions/CIK<10-digit>.json" --raw
```
CIKs: NVDA 0001045810 · ORCL 0001341439 · META 0001326801 · CRWV 0001769628.
Covenant-headroom arithmetic: EBITDA = operating income + depreciation + intangibles amortization; net interest = interest expense − interest income; all four inputs from the FY26 income statement and cash-flow statement.

*Secondary:*
- [S&P downgrade to BBB-/A-3, 2026-07-09](https://www.heise.de/en/news/S-P-downgrades-Oracle-to-BBB-only-one-notch-above-junk-level-11363472.html) · [Yahoo Finance on the downgrade](https://finance.yahoo.com/markets/stocks/articles/oracle-stock-shrugs-off-p-185346661.html) · [S&P's own release (paywalled/bot-blocked — not read)](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101695609)
- [CNBC: NVDA/OpenAI $250B backstop talks, 2026-07-27](https://www.cnbc.com/2026/07/27/nvidia-and-openai-in-talks-for-up-to-250-billion-dollar-ai-backstop.html) · [Tom's Hardware](https://www.tomshardware.com/tech-industry/data-centers/nvidia-weighs-250-billion-guarantee-so-openai-can-lease-softbanks-10-gigawatt-ohio-campus) · [Yahoo/Reuters](https://finance.yahoo.com/technology/ai/articles/nvidia-talks-openai-guarantee-250-233930971.html)

---

## Process Report

**Searches run:** Two WebSearch queries only (the $250B structure; the ORCL rating action). Everything else was direct EDGAR retrieval — 6 filings dumped and grepped locally. **Engine sizing per my own rules: this was correctly a primary-pull run, not a fan-out.** DR-1 is almost entirely data class (c) — single-name issuer-filing detail — which the fan-out structurally cannot reach. A 5-angle harness would have returned the same press cluster I got in one search and none of the covenant text, the RVG disclosures, or the CCAC VIII structure. The verdict lived in the footnotes, as it usually does.

**Explicit negatives (per the commission's standing discipline — what I searched for and could NOT find):**
- **NVDA: no filed OpenAI guarantee, at any size.** "OpenAI" appears 2× in the FY26 10-K (both hedged "no assurance") and **0× in the Q1 FY27 10-Q**, verified with positive controls on the same document.
- **No cross-default clause linking any two of these four issuers.** I searched for cross-default / cross-collateral language in all four; what exists is *intra*-entity (CCAC VIII's own covenants) and *rating-triggered* (ORCL's collateral/credit-support clause). **There is no filed contractual link between NVDA, ORCL, META and CRWV.** The web is economic and rating-mediated, not contractual — that is a substantive negative and it materially weakens any "contagion by contract" framing.
- **ORCL names no customer.** No OpenAI mention, no ≥10% customer, FY24–FY26.
- **META: no financial covenants**, searched and confirmed by explicit statement rather than absence.
- **Could not read S&P's own release** — see Source Quality.

**Data gaps:** ~~(1) ORCL's *lease commitments not yet commenced*~~ **— CLOSED same session, see the ADDENDUM at the top: $260B, plus a $3.3B lessor-borrowing guarantee maturing Sept 2026. It was the largest number in the domain and I had shipped without it.** ~~(3) CoreWeave's RPO~~ **— CLOSED: $98.8B.** **Still open:** (2) AMD's vendor-financing disclosures and the other neoclouds (NBIS/APLD/IREN/CIFR) — scope was already large and the four named anchors carry the verdict; flagged below as follow-on.

⚠️ **What the gap-closing pass says about the first pass, stated plainly:** both closed gaps were *in filings I had already pulled*. The ORCL figure sat behind an MD&A cross-reference ("refer to Note 9") that I cited without following. **Neither was a data-availability problem; both were unfinished reads** — and the larger one would have left this report understating the central exposure by roughly an order of magnitude. **A gap I can close in four minutes should be closed before delivery, not logged as a limitation.** Logging it made the report look rigorous about its own limits while shipping a hole.

**Source frustrations:** `spglobal.com` remains a hard bot-block. EDGAR's XBRL context header (thousands of `us-gaap:`/`xbrli:` tokens) swamps naive greps on the raw text extract — dumping to a file and filtering the header out is materially more reliable than grepping through the tool, and I switched approach after two wasted calls.

**Confidence in findings:** **High** on everything filed — these are direct quotations and arithmetic from primary documents, with accessions and dates. **Medium** on the S&P leverage trigger (secondary, though corroborated n=5 and consistent with ORCL's own language). **Medium** on the $250B characterization — single-origin WSJ reporting; my claim is only that *it is not filed*, which is a primary-verified negative and does not depend on the report being accurate.

**If I had more time/tools:** pull ORCL's Note 9 not-yet-commenced lease figure; extend the map to AMD + the four listed neoclouds; and read the actual DDTL 4.0 credit agreement exhibit rather than the 10-Q summary, which would give the precise borrowing-base formula tying advance rates to GPU depreciable cost — the highest-value unread document in this domain.

**Suggestions:** ⚠️ **A real find for the fleet, worth routing beyond this report:** ORCL's revenue-concentration disclosure ("no customer ≥10%") returns *clean* on what is plausibly a ~50%-concentrated backlog, because the disclosure keys on recognized revenue while the exposure sits in RPO. **Any agent screening for customer concentration via the standard disclosure will get a false negative on exactly the AI-era contracts we care about — read RPO and the prose, not the concentration line.** This generalizes past ORCL and I am promoting it to auto-memory.

**Follow-on prompts this run generated** (slate-mined from gaps, adversarially filtered — decision-real and primaries-exist, not already-answered):
1. **NVDA Q2 FY27 10-Q read, ~late Aug 2026** — does any part of the $250B land in the credit-derivative guarantee line, and does an escrow travel with it? *Cheap, dated, high-value; this is the falsifier for §1.*
2. **The DDTL 4.0 credit-agreement exhibit** — extract the advance-rate formula against GPU depreciable cost. *This is the mechanical link to DR-2 and is currently summarized, not read.*
3. **ORCL Note 9 not-yet-commenced lease commitments** vs META's ~$41B RVG — the off-balance-sheet leg, currently half-measured.
