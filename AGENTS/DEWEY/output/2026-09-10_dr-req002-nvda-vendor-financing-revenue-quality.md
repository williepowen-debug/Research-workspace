# HOW MUCH OF NVDA'S GROWTH DOES NVDA'S OWN BALANCE SHEET UNDERWRITE? — REQ-DEWEY-20260829-002
**Date:** 2026-09-10 | **Mode:** Thesis | **Flag ID:** `REQ-DEWEY-20260829-002` (WALTER ledger — **WALTER closes the row, not DEWEY**)
**Confidence:** **HIGH** (the census, the trajectory, the collateral ratios, the disclosure asymmetry — all primary, all reproducible) · **HIGH** on the base-rate series, **MEDIUM** on the Winstar litigation record (n=2, Lucent + Nortel; load-bearing points DEWEY-verified at the primaries, the litigation record salvaged and tagged — §6) · **NOT COMPUTABLE** (the share-of-revenue figure the question asks for — §3, and the reason is itself the finding)
**Recipients:** VULCAN (action) — HENRY · VIOLET · NEXUS (info)
**Commission:** WALTER → DEWEY 2026-08-28 (Will-directed). Deadline **2026-09-15** — delivered 5 days early.
**Engine sizing:** primary-pull-first. DEWEY main session owned the entire EDGAR spine (5 NVDA + 4 Lucent + 1 Nortel filings, every accession exhibit-enumerated). ONE targeted sub-agent for the historical residual — **not** the 5-angle harness. ⚠️ **That sub-agent died on a session rate limit before reporting; its work was salvaged from scratch and re-verified at the primaries before use (§6).**

---

## Key Finding

**NVIDIA's customer-directed balance-sheet support went from $0 to $164.5 billion in four quarters, and the credit protection behind it degraded at every single step.** The first guarantee (Q3 FY26, $860M) was **54.7% cash-collateralised**, carried a pre-arranged capacity-sale agreement, an internal-use fallback, and warrants as compensation. The latest (August 2026, **$105.0B** for OpenAI) has **no escrow at all** — its stated mitigant is an indemnity from the same counterparty whose insolvency triggers it. **Exposure grew 126×; the escrow behind it grew 1.5×.**

**But the question the commission asked — what SHARE of revenue growth this underwrites — is not computable from public filings, and the reason is the second finding.** NVDA discloses the **financing** with precision (every guarantee has a dollar cap, a trigger, a term, a counterparty by name) and the **revenue attribution** not at all (direct customers are anonymous percentages; the key indirect one is *"one AI research and deployment company"* contributing *"a meaningful amount"*). **The only two counterparties named anywhere in the 10-Q — SB Energy and OpenAI — appear exclusively in the guarantee note and never in the revenue note.** The two halves of the vendor-financing question are disclosed at radically different resolutions, and that asymmetry is what blocks the calculation.

⚠️ **The historical analogue SPLITS, and both halves matter.** On an n=2 base rate pulled at the primaries (Lucent and Nortel), the parallel **fails on the mechanism that actually killed Lucent** — its vendor financing sat *inside* revenue recognition, with collectability gated on Lucent's own ability to sell the paper; NVIDIA's sits entirely outside it, and NVIDIA's customers are *pre*-paying. But it **holds on one structure nobody in the fleet has flagged**: NVDA's guarantee buys an **exclusivity covenant**, which is the same shape as the 65–70% purchase quota a federal court found abusive in Winstar. **And the base rate says the only instrument that ever led was the COMMITMENT level turning down — the drawn balance was unreliable in both directions, and at Nortel it *improved 57%* through the worst year in the company's history because the loans were being written off rather than repaid.** See §6.

---

## 0. Scope fences observed

- ⛔ **Not a solvency question, and no solvency framing appears here.** Liquidity is stated once, for the record: **$56.6B cash + marketable debt securities, $42.8B marketable equity securities** [PRIMARY, Q2 FY27 10-Q].
- ⛔ **The "impossible to pay its bills" framing is not reintroduced** — it was refuted on timing and denominator in `SIG-W-20260828-045` and nothing here revives it.
- ✅ **This is a revenue-quality question** and is answered as one.

---

## 1. THE CENSUS — every dollar of customer-directed capital, with its accounting treatment named

All figures **as of July 26, 2026** unless dated otherwise. All [PRIMARY, NVDA Q2 FY27 10-Q, accession `0001045810-26-000075`, filed 2026-08-26], DEWEY EDGAR pull 2026-09-10.

### A. Guarantees — contingent, off-balance-sheet, $108.5B maximum gross exposure

| Instrument | Max gross exposure | Accounting treatment | Trigger |
|---|---|---|---|
| **SB Energy Corp. guarantees** (on behalf of an OpenAI affiliate) | **$105.0B** | **Not on the balance sheet.** Disclosed in Note 10 only. Entered **August 2026 — after the quarter closed** | *"triggered upon certain tenant defaults"* |
| **Land, power and shell guarantees for AI clouds** | **$3.529B** | **Credit derivatives**, Note 8; *"fair values… were not significant"*; changes in fair value → Other income, net | partner default on data-centre lease obligations |
| **Total** | **$108.5B** | | |

**The SB Energy structure, in the filing's own terms:** ~**4.25 GW** of IT load at SB Energy's **PORTS Technology Campus, Pike County, Ohio**; guarantees become effective **on lease commencement**, stepping up as each of **nine construction phases** completes, **first expected in fiscal year 2029**; obligations decrease over each phase's **20-year** lease term; **limited to defined portions of lease and power payments, not the full cost of the site**; terminate on certain events **including OpenAI achieving a satisfactory credit rating**.

🔑 **What NVDA receives in exchange, verbatim:** *"In exchange for the guarantees, the site will exclusively host NVIDIA AI infrastructure, subject to limited exceptions."* **The guarantee purchases exclusivity. That is the revenue link, stated by the issuer.**

⚠️ **$105B is not the ceiling of intent:** NVDA holds *"an option, exercisable in our sole discretion, to provide additional credit support in phases for approximately **3.8 additional gigawatts** as the site scales."* Roughly **another 90%** of the current commitment, at NVDA's election, undisclosed as to amount.

### A-bis. Where the exposure would land if a guarantee were called

*(The commission asked this explicitly and it deserves a direct answer rather than "off-balance-sheet.")*

**Today: nowhere.** The $105B sits in Note 10 disclosure only. The $3.5B leg sits in Note 8 as a credit derivative whose *"fair values… were not significant."* **Neither is a recognised liability.**

**If triggered, the filing names the paths:** *"we may **assume the applicable lease**, require the landlord to seek a replacement tenant, initiate a sale process or choose to pursue other remedies… **We may assume long-term lease obligations, incur ongoing lease-related costs or make substantial payments.**"*

⇒ **Assumption converts a disclosure-only contingency into on-balance-sheet operating lease assets and liabilities** (NVDA's leases run to fiscal 2075; weighted-average discount rate 4.69%).

⚠️ **Scale contrast, with its limits stated — do NOT read this as "$105B would hit the balance sheet."** NVDA's **entire** current operating-lease book is **$5,390M of assets and $5,494M of liabilities**, against **$7,207M** of future minimum lease obligations. The guarantee cap is **$105,000M**. But the guarantees are *"limited to defined portions of lease and power payments and not the full cost of the site,"* and that defined portion is **undisclosed** — so the assumed-lease figure is **not computable** and is certainly far below the cap. **The honest statement is directional: the contingency is an order of magnitude larger than the lease book that would absorb it, and the conversion ratio is undisclosed.**

### B. Purchase commitments running TO customers — firm, $56B

⚠️ **A perimeter correction to the commission's own framing, and it matters.** The commission cites *"$29B of cloud agreements."* **That is the wrong line for this question.** NVDA's Q2 FY27 10-Q splits commitments into **two separate tables**, and the $29B sits in the first one:

| Table | Line | Total | Whose benefit |
|---|---|---|---|
| **"Commitments"** (total $366B) | Cloud service agreements | **$29B** | **NVDA's OWN R&D** — *"to support our research and development of our open models, such as NVIDIA Nemotron, Cosmos, and GR00T, and our autonomous vehicle software"* |
| **"Additional Commitments"** (total $56B) | **AI cloud agreements** | **$36B** | **CUSTOMER-DIRECTED** — the new business model |
| | **Data centre leases not commenced for third party** | **$20B** | **CUSTOMER-DIRECTED** — ~15-year leases NVDA signs and *"expect[s] to reassign… to third parties"* |

**The $29B is own-use and does not belong in a vendor-financing census. The $36B does, and it is new this quarter.** *(Q1 FY27 disclosed a single undifferentiated *"multi-year cloud service agreement commitments… $30 billion… primarily used to support our research and development efforts"* — no customer-directed table existed.)* `[[finding_cross_entity_comparison_needs_same_perimeter]]`

🔑 **The $36B AI-cloud structure is the most circular thing in the filing, and NVDA describes it plainly:**

> *"Under these agreements, AI clouds procure our data center infrastructure products and we commit to cloud service agreements, which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates."*

And in the risk factors, the same arrangement stated as an obligation:

> *"if AI clouds do not successfully sell committed capacity to third-party customers, **we have agreed to purchase that capacity**. We may not have sufficient demand for, or the operational ability to use or resell, all the capacity we are committed to purchase."*

**NVDA sells GPUs to an AI cloud, and simultaneously commits to buy back the compute those GPUs produce if the AI cloud cannot sell it. NVDA is the residual buyer of its own customers' unsold output.** The commitment is **asymmetric**: the AI cloud may *unilaterally* walk away and resell at better rates; NVDA may not.

### B-bis. 🔑 The purest vendor-financing item in the filing is the one with the smallest number

**$20B of "data center leases not commenced for third party."** NVDA has **already signed** ~15-year data-centre leases, commencing FY2028–FY2029, that it *"expect[s] to reassign… to third parties."* The risk factor: *"We intend to assign certain data center leases to third parties. **Delays in completing these assignments could cause us to bear the related lease costs longer than anticipated.**"*

**NVDA is warehousing lease obligations on its own credit for customers who will take assignment later.** Unlike the guarantees, this is **not contingent** — the leases are signed and the obligation is NVDA's until somebody accepts assignment. It is the clearest instance in the document of NVDA's balance sheet standing in for a customer's, and at $20B it is 5.7× the AI-cloud guarantee leg it sits beside.

### C. Equity — $99B held, $25B further committed, and $42.4B of actual cash out the door in six months

| Item | Jul 26 2026 | Jan 25 2026 / prior-year | Treatment |
|---|---|---|---|
| Marketable equity securities | **$42,783M** | $12,886M | fair value, Level 1/2 |
| Non-marketable securities | **$51,157M** | $22,251M | cost less impairment, adjusted for observable price changes |
| Equity investments (MD&A aggregate) | **$99B** | — | *"equity investments of $99 billion and equity investment commitments of $25 billion"* |
| Equity-method stakes in **infrastructure financiers** | **$3.3B** | — | equity method; **VIE maximum loss exposure $4.7B**; NVDA is *not* the primary beneficiary, so **not consolidated** |
| **Public company warrants** | **$4,800M notional** | **$0** | equity derivatives, Other assets; FV **$824M** |
| **Equity forward contract** | **$1,000M notional** | **$0** | not designated as hedge |
| **CASH: purchases of equity securities, H1** | **$42,404M** | **$1,245M** | investing cash flow — **34.1× YoY** |

**This is the only leg where cash has actually left.** $42.4B in six months = **23.8% of H1 revenue** ($177,837M) and **57.0% of H1 operating cash flow** ($74,421M). *(Both ratios are capital-deployed-to-ecosystem over the stated denominator — they are NOT loss estimates and NOT a revenue-attribution claim.)*

⚠️ **Adjacent finding, deliberately kept separate because it is EARNINGS quality, not revenue quality:** **gains from equity securities contributed $23,707M of H1 FY27 pre-tax income** (vs $2,073M) — **16.8% of $141,410M pre-tax income**, *"primarily driven by unrealized gains."* NVDA is marking up stakes in the ecosystem it is financing, and those marks run through the income statement. **This is not in the commission's scope and is not folded into any conclusion here — it is flagged for VULCAN/HENRY as a separate thread.**

### D. Trade credit — the one leg that moved the balance sheet this quarter

| Quarter | Accounts receivable, net | Revenue | **DSO** |
|---|---|---|---|
| Q2 FY26 (Jul 27 2025) | $27,808M | $46,743M | **54.1 d** |
| Q3 FY26 (Oct 26 2025) | $33,391M | $57,006M | **53.3 d** |
| Q1 FY27 (Apr 26 2026) | $40,710M | $81,615M | **45.4 d** |
| **Q2 FY27 (Jul 26 2026)** | **$63,059M** | **$96,221M** | **59.6 d** |

*(DSO = AR ÷ quarterly revenue × 91. NVDA's fiscal quarters are 13 weeks, so 91 is exact, not an approximation. Reproduce: `edgar_doc.py doc --accession <acc> --cik 1045810 --doc <10-Q htm>`, balance sheet + income statement.)*

**Flat-to-down for three quarters, then +14.2 days in one.** NVDA names the cause: cash from operations rose *"partially offset by an increase in accounts receivable due to **extended payment terms on large multi-quarter agreements with certain investment-grade customers**."*

⚠️ **Counter-evidence, and it is genuine: 59.6 days DSO is not distressed in absolute terms.** The YoY move is **+5.5 days (+10.1%)**, which is modest. The alarming-looking number is the QoQ (+31%), and Q1's 45.4 d was itself unusually low. **Do not read this line as balance-sheet stress. Read it as a structure that switched on in Q2 FY27.**

### E. ⚠️ THE COUNTER-FLOW — customers are prepaying NVDA, and it is large

| Item | H1 FY27 | H1 FY26 |
|---|---|---|
| **Customer advances RECEIVED** | **$15.6B** | $7.5B |
| Customer advances recognised into revenue | $13.0B | $7.5B |
| Customer-advance balance in accrued liabilities | **$2.8B** (Jul 26 2026) | $160M (Jan 25 2026) |

**This runs opposite to the vendor-financing thesis and must be carried with it.** $15.6B of cash came *in* from customers ahead of delivery in the same six months NVDA put $42.4B *out* into equity stakes. **Any characterisation of NVDA as uniformly financing its customers is refuted by this line.**

---

## 2. THE TRAJECTORY — the finding is the collateral ratio, not the headline

**This is the load-bearing table of the report, and no fleet surface currently holds it.**

| As of | Guarantee exposure | Escrow behind it | **Coverage** | Structure of the protection |
|---|---|---|---|---|
| **Q2 FY26** (Jul 27 2025) | **$0** | — | — | **The word "guarantee" appears ZERO times in the 10-Q** |
| **Q3 FY26** (Oct 26 2025) | **$860M** | **$470M** | **54.7%** | ONE partner, one facility. **Plus** an executed agreement to **sell the data-centre cloud capacity**; **plus** NVDA's option to **assume the lease for internal use or sublease**; **plus warrants issued to NVDA** as compensation |
| **Q4 FY26** (Jan 25 2026) | $3,530M | $712M | **20.2%** | multiple agreements, 5–7 year terms |
| **Q1 FY27** (Apr 26 2026) | $3,500M | $712M | **20.3%** | unchanged |
| **Q2 FY27** (Jul 26 2026) | $3,529M | $712M | **20.2%** | unchanged — **but $36B AI-cloud + $20B third-party leases appear this quarter** |
| **August 2026** (subsequent) | **+$105,000M** | **$0** | **0%** | SB Energy / OpenAI. **Stated mitigant: an OpenAI reimbursement-and-indemnity.** |
| **TOTAL** | **$108,529M** | **$712M** | **0.66%** | |

> **Exposure grew 126× in three quarters. The escrow behind it grew 1.5×.**

⚠️ **Read the per-leg truth, not only the blended 0.66%.** The blended figure mixes two perimeters and I state it as a portfolio statistic, not as a coverage ratio anyone underwrote: **the $3.5B AI-cloud leg is 20.2% escrowed; the $105B SB Energy leg has no escrow at all.** Quoting 0.66% as though one pool of collateral was thinned would be a composition error. `[[finding_composition_mask_unmask_discriminator]]`

**What changed qualitatively, step by step — this is the part a ratio cannot show:**

| | Q3 FY26 ($860M) | August 2026 ($105B) |
|---|---|---|
| Cash collateral | **$470M escrow (54.7%)** | **none** |
| Pre-arranged remarketing | **yes** — executed capacity-sale agreement | no — *"require the landlord to seek a replacement tenant, initiate a sale process"* **after** the default |
| Fallback use | **yes** — *"option to assume the lease for internal use or sublease"* | *"we may assume the applicable lease"* — an obligation-shaped version of the same |
| Compensation to NVDA | **warrants** | **exclusivity** (site hosts only NVIDIA infrastructure) |
| Recourse | escrow + capacity sale | **an indemnity from OpenAI** — *"Although OpenAI has agreed to reimburse and indemnify us for certain losses, we may not recover amounts promptly or in full"* |

🔑 **The recourse on the $105B leg is circular.** The guarantee is triggered by OpenAI's default or insolvency; the mitigant is a promise from OpenAI. **A claim against an insolvent counterparty is worth what the estate pays.** NVDA discloses this risk in exactly those terms and deserves credit for the candour — but the structure is what it is.

⚠️ **Timing discipline, because it cuts against alarm:** the $105B is **contingent, not funded**. Guarantees become effective on lease commencement, phase by phase, **first expected in fiscal year 2029**. **Nothing is drawn today and nothing is scheduled to be drawn this fiscal year.** The exposure is real and the protection is thin, but the clock is long.

### The escape hatch NVDA is already building — and it is dated

> *"In August 2026, we entered into **memoranda of understanding with large capital providers** regarding **independent financing platforms** through which the providers would raise and deploy **third-party capital** for the buildout of AI infrastructure. These and other preliminary arrangements **may not lead to definitive agreements**."*

**NVDA is trying to move this financing off its own balance sheet to third-party capital, in the same month it signed the $105B guarantee.** MoU stage, explicitly non-binding. **This is the single highest-value thing to watch** — see §7 T1.

---

## 3. WHY THE SHARE-OF-REVENUE FIGURE IS NOT COMPUTABLE — and why that is the answer, not a gap

The commission's decision question asks **what share** of revenue growth NVDA's own capital supports. **No defensible figure exists in public filings.** Per DEWEY discipline a documented "not computable" beats a plausible constructed number, and here the *reason* is a finding in its own right.

**The disclosure asymmetry, stated precisely:**

| Side of the question | Disclosure resolution |
|---|---|
| **The financing** | **Named counterparty, dollar cap, trigger, term, phase schedule, termination condition.** SB Energy: 11 mentions. OpenAI: 8 mentions. $105.0B, 4.25 GW, nine phases, FY2029, 20-year terms. |
| **The revenue** | **Anonymous.** *"one direct customer represented 16% of total revenue"*; *"three direct customers represented 16%, 15% and 13%"*; and the key line: *"We estimate that **one AI research and deployment company** contributed **a meaningful amount** of our revenue by purchasing cloud services from our customers."* |

🔑 **The only two counterparties NVDA names in the entire 10-Q appear exclusively in the guarantee note and never once in the revenue note.** The commission called the overlap between "financed" and "large customer" *"the entire question."* **NVDA discloses one side by name and dollar, and the other side by euphemism.**

⚠️ **[INFERRED — basis stated in full, not established]:** *"one AI research and deployment company"* is **OpenAI's own official self-description**, used verbatim on OpenAI's About page [openai.com/about]. The phrase, the sector, and the indirect-purchase channel all fit. **NVDA does not say so, and I am not recording it as a fact** — but a reader who treats that sentence as being about an unidentified fourth party is almost certainly wrong. **What NVDA has done is describe its guarantee counterparty as a revenue contributor without naming it or sizing it in the same document where it names and sizes the guarantee.**

**What IS computable, with every basis stated:**

| Measure | Value | Basis — read this before quoting the number |
|---|---|---|
| Cash deployed into ecosystem equity, H1 FY27 | **$42,404M** | Investing cash flow, "purchases of equity securities." **Actual cash. Not all of it is customers.** |
| …as % of H1 revenue | **23.8%** | ÷ $177,837M H1 revenue. **Capital deployed / revenue. NOT "revenue supported by capital."** |
| …as % of H1 operating cash flow | **57.0%** | ÷ $74,421M. Same caveat. |
| Customer-directed contingent + committed | **$164.5B** | $108.5B guarantees (contingent max gross) + $36B AI cloud + $20B third-party leases. **Mixes contingent maximum exposure with firm commitments — it is a scale marker, NOT a loss estimate and NOT a liability.** |
| …as % of annualised Q2 revenue | **42.7%** | ÷ ($96,221M × 4 = $384,884M). **Annualisation is mine, from one quarter; NVDA publishes no such figure.** |

**None of these is the answer to the question asked.** They bound the scale. **The share of revenue attributable to financed counterparties is undisclosed, and on the current disclosure regime it is unknowable from outside.**

---

## 4. WHAT WOULD CHANGE THE ANSWER — pre-registered, falsifiable

Written before §6's historical leg returned, so the base rate could not shape them.

| # | Observable | Where | What it would settle |
|---|---|---|---|
| **T1** | The August-2026 **MoUs with large capital providers convert to definitive agreements**, and third-party capital takes the buildout financing | 10-Q/10-K subsequent events; 8-K | **The single most decisive item.** Conversion = NVDA was bridging, not underwriting, and this whole structure is transitional. Failure to convert = the balance sheet is the permanent financing layer. |
| **T2** | **Escrow or other hard collateral appears against the SB Energy leg** | Note 8 / Note 10 | Would reverse the §2 degradation finding directly. |
| **T3** | NVDA **quantifies** the indirect revenue contribution of the *"AI research and deployment company"* | Concentration of Revenue note | Would make the share-of-revenue question computable for the first time. |
| **T4** | **DSO continues above ~60 days for two more quarters** | balance sheet + income statement | Distinguishes a one-off contract-timing effect from a standing extension of trade credit. One quarter is not a trend. |
| **T5** | **OpenAI achieves an investment-grade credit rating** | rating agencies | Contractually **terminates** the guarantees. The bull case for this structure resolving cleanly, and it is written into the agreement. |
| **T6** | The **3.8 GW option is exercised** | 10-Q/10-K | Would roughly double the guarantee book at NVDA's sole discretion. |

---

## 5. COUNTER-EVIDENCE — mandatory, and here it is substantial

**This section is longer than usual because the evidence genuinely cuts both ways, and a reader who takes only §2 away will be miscalibrated.**

1. **⚠️ THE $105B IS CONTINGENT AND UNFUNDED, AND FIRST BITES IN FY2029.** Not a liability, not on the balance sheet, not drawn. Guarantees step in phase by phase over nine phases across 20-year lease terms. **Anyone treating $105B as an exposure NVDA carries today is wrong.**
2. **⚠️ IT IS CAPPED AND PARTIAL.** *"limited to defined portions of lease and power payments and not the full cost of the site or all of the tenant's obligations."* The headline number overstates the economic exposure by an undisclosed amount.
3. **⚠️ THE GUARANTEE HAS A DEFINED OFF-RAMP.** It terminates on OpenAI achieving a satisfactory credit rating. **This is structured as bridge credit support for a counterparty expected to become financeable, and that is a materially different instrument from permanent vendor financing.**
4. **⚠️ CUSTOMERS ARE PREPAYING NVDA $15.6B (H1 FY27, vs $7.5B).** Directly opposed to the thesis. Some of NVDA's customer base is funding NVDA.
5. **⚠️ DSO AT 59.6 DAYS IS UNREMARKABLE IN ABSOLUTE TERMS**, and the YoY move is only +5.5 days.
6. **⚠️ NVDA'S DISCLOSURE IS UNUSUALLY FORTHCOMING.** The circular AI-cloud structure, the residual-purchase obligation, the indemnity's weakness and the MoUs are all disclosed in NVDA's own words, in the risk factors, before any analyst forced them out. **The transparency is itself evidence against a concealment reading — and it is the sharpest contrast with the historical case (§6).**
7. **⚠️ NVDA RECEIVES REAL CONSIDERATION.** Warrants ($4.8B notional, $824M FV), exclusivity on a 4.25 GW campus, and revenue-share participation if criteria are met. These are not gifts.
8. **⚠️ THE FINANCED PARTIES MAY SIMPLY BE EARLY, NOT WEAK.** NVDA's own framing is that AI clouds *"have strong customer demand and robust sales pipelines but are constrained by the large-scale infrastructure required to meet that demand"* — a timing-and-capital-structure constraint, not a demand problem. **If that is right, the credit support is bridging a financing-market gap and will unwind as the market matures.** T1 and T5 are the tests.
9. **⚠️ SCALE CONTEXT.** $42.4B of equity purchases against $74.4B of half-year operating cash flow is large but self-funded. No debt was raised to do it.

**What would most damage the findings in this report:** if the August MoUs convert quickly and third-party capital replaces NVDA's guarantees before FY2029, then §2's degradation curve describes a **transitional** period and not a structural one, and the correct read becomes "NVDA bridged a financing gap during a capital-market lag." **I regard T1 as genuinely open and would not bet against it.**

---

## 6. THE HISTORICAL BASE RATE — n=2, pulled at the primaries, and **the analogue splits: it FAILS on the financing mechanism and HOLDS on one structural feature nobody in the fleet has flagged**

⚠️ **The commission said: "Do NOT assume the parallel holds. Test it. A finding that the analogue FAILS is as valuable as one that it holds."** The answer is not a clean pass or fail, and the split is the useful part.

**Sourcing note, stated plainly.** A sub-agent ran the historical leg and **died on a session rate limit before reporting.** Its scratch work was salvaged, and it had built a quarterly Lucent series far better than mine plus the Winstar litigation record. **I re-verified its figures at the primaries myself before using any of them — 5 of 5 checks passed exactly** (Dec-1999 commitments, Sept-2001 drawn, Sept-2002 drawn, FY2001/FY2002 provisions, the SEC penalty and fraud figures). Everything below is tagged by who verified it. *(This is the 7/16 lesson applied: the work had completed and would have died silently.)* `[[finding_workflow_scratch_crash_recovery]]`

### 6.1 LUCENT — the full series [PRIMARY, SEC EDGAR CIK 1006240]

| Date | Total commitments | Total drawn | Verified |
|---|---|---|---|
| 1997-09-30 | $2.21B | $0.14B | salvaged |
| 1998-09-30 | $2.60B | $0.60B | salvaged |
| 1999-09-30 | $7.54B | $1.88B | salvaged |
| **1999-12-31** | **$9.80B ← COMMITMENT PEAK** | $1.75B | ✅ **DEWEY, Q1FY00 10-Q** |
| 2000-03-31 | $8.7B | $1.90B | salvaged |
| 2000-06-30 | $8.7B | $1.85B | salvaged |
| 2000-09-30 | $8.10B | $2.03B | ✅ **DEWEY, FY2000 10-K405** |
| 2000-12-31 | $7.5B | $2.54B | salvaged |
| 2001-03-31 | $6.9B | $2.8B | salvaged |
| **2001-09-30** | $5.31B | **$2.96B ← DRAWN PEAK** | ✅ **DEWEY, FY2002 10-K EX-13** |
| 2002-09-30 | $1.34B | $1.10B | ✅ **DEWEY, FY2002 10-K EX-13** |

**Revenue** (continuing ops, one consistent perimeter — FY2002 10-K restates to exclude Avaya, Agere and power systems; **mixing this with the $33,813M as-reported FY2000 figure would manufacture a false decline**) `[[finding_cross_entity_comparison_needs_same_perimeter]]`:
**FY2000 $28,904M → FY2001 $21,294M (−26.3%) → FY2002 $12,321M (−42.1%).** Peak-to-trough **−57.4%**.

**Provisions for bad debts and customer financings:** FY1999 $66M → FY2000 $505M → **FY2001 $2,249M** → FY2002 $1,253M. ✅ *DEWEY verified FY2001/FY2002 at EX-13: "provisions for bad debts and customer financings of $1.3 billion and $2.2 billion during fiscal 2002 and 2001."*

**Reserves vs drawn:** 2001-09-30 — **$2.1B of reserves against $3.0B drawn**. 2002-09-30 — **$950M against $1.1B drawn.** ✅ DEWEY. *By the end, Lucent had reserved ~86% of everything it had lent.*

### 6.2 NORTEL — the second observation [PRIMARY, Nortel Networks FY2001 Form 10-K]

| As at Dec 31 | Drawn & outstanding | Undrawn commitments | **Total** |
|---|---|---|---|
| **2000** | **$1,081M** | **$4,087M** | **$5,168M** |
| **2001** | **$464M** | **$1,611M** | **$2,075M** |

**Revenue: 1999 $19,628M → 2000 $27,948M (+42.4%) → 2001 $17,511M (−37.3%, −$10,437M).**

### 6.3 🔑 THE INSTRUMENT FINDING — the drawn balance is unreliable IN BOTH DIRECTIONS, and Nortel's filing says so outright

**Lucent's drawn balance ROSE through the collapse** ($1.75B Dec-1999 → **$2.96B Sept-2001**) as distressed customers pulled on facilities Lucent could no longer withdraw. **Nortel's drawn balance FELL** ($1,081M → $464M) over the same window. **Opposite signs, same crisis.**

**The reason Nortel's fell is not repayment, and the 10-K states it:**

> *"**Primarily as a result of these increased provisions recorded during the year, the drawn and outstanding customer financing balance decreased significantly in 2001**, compared to 2000."*

⛔ **A falling drawn balance meant the loans were being written off, not repaid.** An analyst tracking Nortel's drawn customer financing as a risk gauge would have watched it improve by 57% straight through the worst year in the company's history. **This is a composition trap of exactly the class the fleet keeps hitting** — the measure moved because what was in it changed, not because the underlying improved. `[[finding_composition_mask_unmask_discriminator]]` · `[[finding_measure_actionable_not_gross_rate]]`

### 6.4 🔑 WHAT ACTUALLY LED: the COMMITMENT level, and only that

| Instrument | Lucent | Nortel | Verdict |
|---|---|---|---|
| **Commitment level turning down** | Peak **1999-12-31**; declining all through calendar 2000 | Undrawn **$4,087M → $1,611M** as commitments were *"reduced or withdrawn"* | ✅ **LEADS** |
| **Drawn balance** | **Rose** into the crisis, peaked Sept-2001 | **Fell** — on write-downs | ⛔ **Unreliable, both signs** |
| **Provisions** | Broke FY2001, same year as revenue | Increased through 2001 | ⛔ **Coincident-to-lagging** |

⚠️ **The precise Lucent timing, because it is sharper than "12 months" and cuts against over-claiming.** The commitment peak (**1999-12-31**) and Lucent's **first** revenue warning (8-K, **2000-01-06**, Q1FY00 revenue flat) are **three weeks apart**. The full break came ~12 months later (Dec-2000 8-K restating Q4FY00 revenue by $679M; Jan-2001 8-K, Q1FY01 −27.6%). **So the commitment peak was simultaneous with the first warning and led the full break by about a year.**

🔑 **And the attribution lagged the data by eleven months.** The 2000-01-06 8-K blamed DWDM capacity, deployment delays and software timing — **customer financing is not mentioned.** The first time Lucent named it was the **2000-12-21** 8-K, where chairman Schacht cited *"a more focused use of vendor financing"* among the causes. **The number turned in December 1999; the company's own explanation caught up in December 2000.** *(8-K dates and the Schacht quote: salvaged, not independently re-verified by me.)*

⚠️ **This converges with REQ-001's base-rate finding from a completely different direction** — that the order-book instruments the fleet named ran **9–27 months late and led in zero of three episodes**. **Two independent historical studies now say the same thing: the instruments that feel like early warnings are confirmations.** The one exception, in both studies, is the same shape — **REQ-001 found what led was the price of the marginal uncontracted unit; this study finds what led was the willingness to commit new credit.** Both are *forward-looking supply decisions*, not backward-looking balances.

### 6.5 ⛔ WHERE THE ANALOGUE FAILS — and it fails on the thing that actually killed Lucent

**Lucent's vendor financing sat INSIDE its revenue recognition. NVIDIA's sits OUTSIDE it.** Verbatim, and disclosed as early as the Dec-1999 10-Q ✅ *(DEWEY-verified at the primary)*:

> *"Lucent has determined that the receivables under these contracts are reasonably assured of collection based on various factors among which is **the ability of Lucent to sell these loans and commitments**."*

**Lucent booked revenue against notes receivable from customers it had financed, and the gate on recognising that revenue was Lucent's own ability to SELL the paper.** When the market for it closed, the revenue recognition became unsupportable. That is the reflexive loop, and it is why this ended in an **SEC enforcement action alleging $1.148 billion of revenue and $470 million of pre-tax income improperly recognised in fiscal 2000, settled for a $25 million civil penalty** [✅ DEWEY-verified: SEC Press Release 2004-67 and Litigation Release LR-18715, May 17 2004, D.N.J. 04-2315 (WHW)].

| | **Lucent** | **NVIDIA Q2 FY2027** |
|---|---|---|
| Instrument | **Direct loans + notes receivable** | **Contingent guarantees** of third-party lease obligations |
| Drawn at peak | **$2.96B funded** | **$0 — nothing drawn, first phase FY2029** |
| **Inside revenue recognition?** | **YES** — collectability keyed to selling the paper | **NO** — GPUs sold and paid for; **$15.6B arrived in ADVANCE in H1** |
| Receivable from the financed party? | **YES** | **No** — the beneficiary is a *lessor*, not a debtor to NVDA |
| Revenue at the commitment peak | **+10.4%, decelerating from +25.6%** | **+105.8% YoY** |
| Commitments / revenue | **28–34%** (Lucent peak) | **28.2%** (guarantees ÷ annualised Q2) |

🔑 **The scale ratios nearly match — and that is the most seductive thing in this report and should not be leaned on.** Same ratio, different instrument. **A funded loan whose collectability gates revenue recognition, and a contingent lease guarantee beginning in three years, are different risks that happen to normalise to the same number.** `[[finding_output_shape_implies_more_than_the_measurement]]`

### 6.6 ⚠️ WHERE IT HOLDS — the Winstar structure, and one live echo in NVDA's filing

The Winstar/Lucent record is the most instructive part of the base rate, because a federal court adjudicated exactly what vendor financing can become. *(All of §6.6 is **salvaged, not independently re-verified by me**, except the SEC figures above. Treat as [INSTITUTIONAL/court record], verify before citing externally.)*

- **Lucent's supply agreement obliged Winstar to buy 65% of its equipment from Lucent in year one and 70% thereafter**, with escalating surcharges for missing the quota.
- The Bankruptcy Court found Lucent *"treated Winstar as a captive buyer"* and used it as *"a means for Lucent to inflate its own revenue"*; Winstar's end-of-quarter purchases ran **on average eight times** its non-quarter-end purchases; and Lucent *"forced the 'purchase' of its goods well before the equipment was needed and in many instances … never needed at all."*
- The **Third Circuit affirmed** Lucent was a **non-statutory insider** — holding that insider status does **not** require actual control, only *"a close relationship … and anything other than closeness to suggest that any transactions were not conducted at arm's length."* **In re Winstar Communications, 554 F.3d 382 (3d Cir. 2009).** Outcome: **$188.18M preference recovered, >$62M breach award, and equitable subordination of Lucent's ~$900M in claims.**
- At 2001-03-31 Lucent's **$737M drawn to Winstar was fully reserved**; three financings including Winstar and One.Tel were **~60% of the entire FY2001 provision.**

⚠️ **THE ONE STRUCTURAL ECHO IN NVDA'S FILING, and I flag it precisely because it is the only one:** NVDA's $105B guarantee is granted in exchange for the PORTS campus **"exclusively host[ing] NVIDIA AI infrastructure."** **An exclusivity covenant tying a credit-supported counterparty's purchases to its financier is the same shape as Winstar's 65–70% purchase quota.**

⛔ **State the limits of that echo just as precisely, because it will be over-read on the next hop.** Winstar's quota was found abusive because it sat on top of **direct lending Lucent controlled draw-by-draw**, was used to force **unneeded** end-of-quarter purchases, and produced **improperly recognised revenue**. **NVIDIA has none of those four features:** no direct lending, no draw control, no evidence of forced purchasing, no revenue-recognition defect. **The echo is structural, not behavioural, and nothing here alleges otherwise.** What it does mean: **exclusivity provisions attached to credit support are the feature to watch as this scales**, and if NVDA's optional additional 3.8 GW arrives with similar terms, the concentration of that structure is worth tracking.

### 6.7 What the base rate says to watch on NVDA

1. **Watch the COMMITMENT level, not the drawn balance and not the provision.** It is the only instrument that led in either case, and NVDA's is going vertical — which on this base rate places NVDA at the **build** phase, not the break phase.
2. **⚠️ When NVDA's guarantee commitments stop growing, that is the signal — and it will look like prudence.** Lucent's commitments peaking in Dec-1999 read at the time as discipline. It was the top.
3. **A falling drawn/exposure balance is NOT reassurance** (§6.3). Ask whether it fell through repayment or through write-down; Nortel's fell entirely through the latter.
4. **The escape valve fails exactly when needed — and this is the one place the analogue holds hardest.** Lucent's stated plan was *"to lay off these long-term financing arrangements … to financial institutions and investors."* The market for that paper closed precisely in the downturn. **NVDA's equivalent is the August-2026 MoUs with large capital providers (T1), and it is the same bet on third-party appetite.**
5. **Good disclosure was not protective.** Lucent disclosed commitments, drawn, undrawn, the SPT and the revenue-recognition link in its FY2000 10-K — and still ended in a $1.148B fraud action. **NVDA's genuinely forthcoming disclosure should not be read as a control.** `[[finding_adoption_is_not_validation]]`

### 6.8 ⚠️ DECLARED GAPS — not silently synthesised around

- **The Winstar/SEC/Third Circuit material in §6.6 is salvaged sub-agent work that I have NOT re-verified at the court record** (the SEC figures excepted — those I verified). It is tagged in place. **Do not cite it externally without checking the opinion.**
- **The intermediate Lucent quarters (1997, 1998, 1999-09-30, and the 2000–2001 quarter-ends) are salvaged, not re-verified.** The four load-bearing points — the commitment peak, the drawn peak, and both endpoints — **are** DEWEY-verified.
- **Causation is NOT established.** Both companies show financing distress and revenue collapse in the same window, which is equally consistent with vendor financing being a **symptom** of the capex bust rather than a cause of it. **I did not reach the academic literature on this and I am not asserting causation.** ⚠️ This matters for how §6 is used: the base rate supports *"this is what the instruments did"*, not *"this is what caused the collapse."*
- **No case was found where large-scale vendor financing did NOT end in write-offs** — but I did not search for one systematically, so **this is an absence of evidence, not evidence of absence.**
- **Motorola, Cisco and Ericsson: not attempted.**


## 7. WHAT EACH DESK SHOULD DO WITH THIS

**VULCAN (action) — you own the revenue-quality call; I am not making it.**
1. **The perimeter correction is the first thing to encode:** the commission's *"$29B of cloud agreements"* is **own-use R&D**, not customer-directed. The customer-directed cloud number is **$36B** and it is **new in Q2 FY27**. Any model carrying $29B as vendor financing is measuring the wrong table.
2. **The discount question has a defensible shape even though the share is not computable:** the revenue at issue is the portion flowing from counterparties NVDA credit-supports, and NVDA's own words are that AI clouds and model makers *"currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity."* **The issuer states the financing dependency; it declines to size it.** A discount premised on the dependency is supportable; a *quantified* discount is not, and would be a fabricated denominator.
3. **T1 (MoU → definitive agreements) is the decisive test and it is dated to the next two filings.** It resolves whether this is a bridge or a structure.
4. 🔑 **The base rate hands you a specific instrument, and it is NOT the one anyone would pick.** Across Lucent and Nortel the only thing that ever led was **the commitment level turning down** — the drawn balance was unreliable in both directions (Nortel's *improved 57%* through its worst year because the loans were being written off) and provisions lagged. **NVDA's commitments are going vertical, which on this base rate places it at the BUILD phase, not the break phase.** ⚠️ **The corollary is the uncomfortable half: when NVDA's guarantee commitments stop growing, that is the signal — and it will read as prudence at the time.** Lucent's Dec-1999 peak looked like discipline.
5. ⚠️ **Your `FL-VULCAN-12` downgrade logic applies here identically** — direction intact, cannot be sized. Same disease, different note.

**HENRY (info) — two items land on concentration and FCF:**
- **$42,404M of equity purchases = 57.0% of H1 operating cash flow** (vs $1,245M / $42,779M a year ago). Self-funded, no debt raised, but it is where the incremental cash went.
- **$23,707M of H1 pre-tax income — 16.8% — is gains on equity securities, "primarily driven by unrealized gains"** in the ecosystem NVDA is financing. **This is earnings quality, not revenue quality, and I have deliberately kept it out of the conclusions.** It is yours if you want it.

**VIOLET (info):** the guarantee book is contingent and first bites FY2029 — **there is no near-dated cliff here to position around.** The dated items are T1 (next two filings) and T5 (an OpenAI rating action), not a payment date.

**NEXUS (info):** the SB Energy / PORTS Technology Campus structure (Pike County, Ohio, 4.25 GW, nine phases, exclusivity to NVIDIA) is a named physical asset with a named financier and a dated build schedule — likely relevant to cross-domain power/infrastructure mapping.

**⛔ NOT MINE TO EXECUTE, flagged so nobody duplicates:** whether ~4.25 GW at Pike County is credible against PJM interconnection reality is **WATT's**, and WATT has already warned (9/3, REQ-001) against netting turbine/order-book findings into interconnection-queue populations. **Do not infer a queue conclusion from this report.** `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`

---

## 8. SOURCE QUALITY ASSESSMENT

**Overall: HIGH on everything load-bearing.** Every figure in §1, §2 and §3 is [PRIMARY] — read by me at EDGAR on 2026-09-10 from the filed documents, not from coverage, not from a sub-agent, not from a republisher.

| Leg | Grade | Note |
|---|---|---|
| The census (§1) | **[PRIMARY], high** | Five NVDA filings across four quarters, all exhibit-enumerated before reading |
| The trajectory + collateral ratios (§2) | **[PRIMARY], high** | The strongest material here. Derived from four consecutive 10-Qs; arithmetic is trivial and reproducible |
| Disclosure asymmetry (§3) | **[PRIMARY], high** | A structural claim about the documents, verifiable by grep |
| The OpenAI identification (§3) | **[INFERRED]**, flagged as such | Phrase matches OpenAI's own About-page self-description; **NVDA does not say so** |
| DSO series (§1.D) | **[PRIMARY], high** | Exact 91-day quarters; no estimation |
| Base-rate series (§6.1–6.5) | **[PRIMARY], high** | Lucent Q1FY00 10-Q, FY2000 10-K405, FY2002 10-K + EX-13; Nortel FY2001 10-K. **The four load-bearing points — both peaks and both endpoints — DEWEY-verified.** Intermediate quarters salvaged, tagged in place |
| Winstar litigation record (§6.6) | **[INSTITUTIONAL/court], medium** | **Salvaged sub-agent work, NOT re-verified by me** except the SEC figures. Tagged in place; §6.8 says do not cite externally unchecked |
| SEC enforcement figures (§6.5) | **[PRIMARY], high** | SEC Press Release 2004-67 + LR-18715, DEWEY-verified |

**⚠️ Methodological note on the negative claims.** Two findings here are *absence* claims — "the word guarantee appears zero times in the Q2 FY26 10-Q," and "the named counterparties never appear in the revenue note." **I enumerated each accession's exhibits before grepping**, because eight days ago a bare `edgar_doc.py doc --grep` returned only the first exhibit of a multi-document accession and I shipped a false [VERIFIED] absence off it (`COR-20260908-01`, corrected 2026-09-10). **Every absence claim in this report was made against an enumerated document list, and the enumeration is in the reproduction recipe below.** `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`

**Reproduction recipe** *(not a path — the working files are session-scoped and will not exist for you)*:
```
# 1. enumerate before you grep — a bare `doc` returns only the FIRST document
#    https://www.sec.gov/Archives/edgar/data/1045810/<acc-nodashes>/<acc>-index.html
# 2. then, per document:
python3 AGENTS/DEWEY/scripts/edgar_doc.py doc --cik 1045810 \
        --accession <acc> --doc <document.htm> [--grep "<term>"]
# accessions used:
#   Q2 FY27 10-Q  0001045810-26-000075   nvda-20260726.htm
#   Q1 FY27 10-Q  0001045810-26-000052   nvda-20260426.htm
#   Q3 FY26 10-Q  0001045810-25-000230   nvda-20251026.htm
#   Q2 FY26 10-Q  0001045810-25-000209   nvda-20250727.htm
#   8-K (Hugging Face, 9/2)  0001045810-26-000078   nvda-20260902.htm
# DSO = AR(net) / quarterly revenue x 91   [NVDA quarters are exactly 13 weeks]
```

---

## 9. REFERENCES

**[PRIMARY] — SEC EDGAR, all accessed 2026-09-10:**
1. NVIDIA Q2 FY2027 Form 10-Q, period ended 2026-07-26, accession `0001045810-26-000075`, filed 2026-08-26. Notes 5, 6, 8, 9, 10, 14; Concentration of Revenue; MD&A Liquidity; Risk Factors.
2. NVIDIA Q1 FY2027 Form 10-Q, period ended 2026-04-26, accession `0001045810-26-000052`, filed 2026-05-20. Note 8 (Facility Lease Guarantee), Note 10.
3. NVIDIA Q3 FY2026 Form 10-Q, period ended 2025-10-26, accession `0001045810-25-000230`, filed 2025-11-19. Note 8 (Facility Lease Guarantee — the origin disclosure).
4. NVIDIA Q2 FY2026 Form 10-Q, period ended 2025-07-27, accession `0001045810-25-000209`, filed 2025-08-27. **Zero occurrences of "guarantee."**
5. NVIDIA Form 8-K, event date 2026-09-02, accession `0001045810-26-000078` — Hugging Face acquisition, ~$11.9B + ~$1.0B retention. *(Post-quarter, and an acquisition rather than customer financing — noted so it is not mistaken for part of this census.)*

**[SECONDARY]:**
6. OpenAI, "About" — openai.com/about (self-description *"AI research and deployment company"*), accessed 2026-09-10. **Used only to support a flagged inference, not a fact.**

**[PRIMARY] — historical base rate, SEC EDGAR, accessed 2026-09-10:**
7. Lucent Technologies, Form 10-Q for the quarter ended 1999-12-31, accession `0000950116-00-000226`, filed 2000-02-11. **The commitment peak ($8.4B credit + $1.4B guarantees) and the revenue-recognition clause.**
8. Lucent Technologies, Form 10-K405 FY2000 (period ended 2000-09-30), accession `0000950123-00-011855`, filed 2000-12-27. Customer financing; Note 16 Securitizations (the non-consolidated Special Purpose Trust).
9. Lucent Technologies, Form 10-K FY2002 + **Exhibit 13** (annual report — the financials are incorporated by reference and are NOT in the 10-K document), accession `0000950117-02-003045`, filed 2002-12-12. Restated revenue series; customer-financing drawn/undrawn tables; Schedule II reserve roll-forward.
10. Nortel Networks Corp., Form 10-K FY2001 (`t06646e10-k.htm`). Customer financing commitments table; the provisions-caused-decline statement; consolidated revenue 1999–2001.
11. U.S. SEC, **Press Release 2004-67** and **Litigation Release LR-18715**, 2004-05-17 — *SEC v. Lucent Technologies Inc. et al.*, D.N.J. Civ. No. 04-2315 (WHW). $1.148B revenue / $470M pre-tax improperly recognised FY2000; $25M civil penalty.

**[INSTITUTIONAL / court record] — §6.6, salvaged and NOT re-verified by DEWEY:**
12. *In re Winstar Communications, Inc.; Shubert v. Lucent Technologies Inc.*, **554 F.3d 382 (3d Cir. 2009)**, No. 07-2569, filed 2009-02-03, quoting the Bankruptcy Court at 348 B.R. 234 (Bankr. D. Del. 2006). ⚠️ **Verify at the opinion before citing externally.**


## 10. PROCESS REPORT

**Engine sizing:** primary-pull-first, per §Engine sizing. **The verdict lives entirely in the primary pull, as it has on every prior run.** DEWEY main session owned the whole EDGAR spine — 5 NVIDIA filings across 4 quarters, 4 Lucent filings across 4 fiscal years, 1 Nortel 10-K — **every accession exhibit-enumerated before reading.** **ONE** targeted sub-agent for the historical residual. **Not the 5-angle harness** — this was one historical leg.

**⚠️ THE SUB-AGENT DIED ON A SESSION RATE LIMIT BEFORE REPORTING, AND THE SALVAGE IS THE STORY OF THIS RUN.** Its last transmitted line was *"Found the transmission mechanism — the lay-off channel closing. Recording it."* Per closeout rule 7a I swept the scratch tree before accepting any gap and found **385 files** — a complete quarterly Lucent customer-financing series (1997–2002), the Nortel 10-K, and the entire Winstar litigation record. **None of it had reached me through any channel.**

**What the salvage changed, concretely: it CORRECTED MY OWN DRAFT §6.** I had written that Lucent's exposure peaked at FY2000 ($8.1B) and concluded *"the lead time was zero — revenue and provisions broke in the same fiscal year."* **That was wrong.** Commitments peaked **1999-12-31 at $9.8B** and fell all through calendar 2000. The corrected finding — **commitments led, the drawn balance was unreliable in both directions, provisions lagged** — is the most useful thing in this report, **and I would have shipped its opposite.** ⚠️ **The cost of not reaping is not CPU. It is a report shipping a confident wrong conclusion while the work that refutes it sits on disk.** `[[finding_workflow_scratch_crash_recovery]]`

**I re-verified 5 of 5 salvaged load-bearing figures at the primaries before using any of them** — Dec-1999 commitments, Sept-2001 drawn, Sept-2002 drawn, FY2001/FY2002 provisions, and the SEC fraud/penalty figures. All matched exactly. **The Winstar litigation record I did NOT re-verify, and it is tagged as such in §6.6/§6.8 rather than blended into the verified material.** Given that I corrected a false **[VERIFIED]** absence of my own this same morning (`COR-20260908-01`), tagging by verifier rather than by convenience was the minimum discipline.

**Searches run:** 3 WebSearches only (OpenAI self-description; two on the Korean complex for the separate `DEW-MECH-SELL` disposition). **This run is ~95% EDGAR.** The load-bearing material was never going to be on the open web.

**What worked:**
- **Exhibit enumeration before grepping.** Built after `COR-20260908-01` (below) and it paid immediately, twice: it surfaced an **EX-10.1 material contract** in NVDA's 10-Q that a default read hides, and it found that **Lucent's entire FY2002 financials live in Exhibit 13**, incorporated by reference — the 10-K document itself contains no income statement. A bare `doc` pull would have returned "no revenue data in the 10-K," which is true of the document and false of the filing.
- **Reading four consecutive 10-Qs instead of one.** Every finding in §2 — the collateral degradation, the onset quarter, the DSO break — is invisible in any single filing. **The trajectory was the finding, and only a series shows a trajectory.**
- **Pulling Lucent myself.** The decisive line (the revenue-recognition link) is a clause inside a footnote in a 2000 filing. I would not have trusted it from a secondary source, and §6's central conclusion rests on it.

**Data gaps — looked for, could not find:**
- **The share-of-revenue figure the commission asked for.** Structurally undisclosed (§3). Not a search failure — a disclosure-regime fact.
- **NVDA's memory-share, slot-conversion and financed-customer-revenue splits:** all undisclosed by the issuer, consistent with REQ-001.
- **The "defined portion" of lease and power payments the $105B guarantee actually covers** — undisclosed, which is why the balance-sheet-landing figure in §A-bis is directional rather than numeric.
- **Causation** — see §6.8. Both companies show financing distress and revenue collapse in the same window; nothing I pulled distinguishes cause from symptom, and I did not reach the academic literature. **Declared, not synthesised around.**
- **A case where large-scale vendor financing did NOT end in write-offs** — not found, but not systematically searched. **Absence of evidence, not evidence of absence.**
- **The Winstar litigation record is shipped unverified by me** (§6.6), tagged in place.

**Source frustrations:** none material this run. EDGAR behaved; no 403s; no paywalls hit, because nothing load-bearing sat behind one. **This is the cheapest high-confidence run I have done, and the reason is that the question was a filings question and I treated it as one from the start.**

**⚠️ The defect I carried into this run, and what it cost:** eight days ago REQ-001 shipped a **[VERIFIED] absence** that was false, because `edgar_doc.py doc` without `--doc` silently returns only the **first** document of an accession and I recorded that one clean grep as "the 8-K" (`COR-20260908-01`, corrected earlier today). **This commission is filings-only — the same defect would have corrupted it wholesale.** I wrote an exhibit enumerator before the first pull and used it on every accession. **The lesson generalised correctly: a tool that answers a narrower question than the one you asked, without saying so, is worse than a tool that fails.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

**Two self-corrections during the run, both caught before they reached the page:**
1. I began writing that the **$3.5B guarantee was new in Q2 FY27**. It is not — Q1 FY27 and Q3 FY26 disclose it, and Q3 FY26 is its origin. **Checking the prior quarters converted a wrong "sudden appearance" claim into the correct and much stronger degradation trajectory.**
2. I then wrote that the **$712M escrow had disappeared** from the Q2 FY27 disclosure. **It had not** — it moved from Note 10 prose to a Note 8 table footnote. **A relocation is not a removal, and I nearly published the stronger, false version.** `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`

**Confidence: HIGH on §1–§3 and on the §6 base-rate series** (n=2, load-bearing points DEWEY-verified), **MEDIUM on the §6.6 Winstar record** (salvaged, tagged). The headline question is answered **NOT COMPUTABLE with the reason documented**, which per Rule 3 is a result and not a failure.

**If I had more time/tools:**
- **Re-verify the Winstar record at the Third Circuit opinion and the bankruptcy docket.** It is the most consequential material I am shipping unverified, and §6.6's exclusivity echo is the finding most likely to be over-read on the next hop.
- **The FY2026 10-K's audited treatment** of the facility-lease guarantees, for an auditor's view rather than a quarterly one.
- **The academic literature on causation** — whether vendor financing drove the telecom bust or merely rode it. §6.8 flags this open, and it bounds how hard the base rate can be pushed.

**Suggestions:**
1. **BUILD `edgar_doc.py exhibits` and fix the bare-`doc` default** — already logged to `scripts/BACKLOG.md` this session as gate-tripped-on-first-hit. **I built a throwaway enumerator to run this commission and it earned its keep twice in one session; it should not be a scratch file.** *(Will-greenlit build, per the standing gate.)*
2. **⚠️ PROCESS — and this one is for PROME as much as me: a sub-agent that dies on a session rate limit reports NOTHING, and its completed work is recoverable only by a manual scratch sweep the parent has to remember to run.** This is the second time (7/16, and now) that salvage recovered work that would otherwise have died silently — **and this time it recovered a finding that REVERSED my own draft conclusion.** The reaping step is DEWEY-local; **the rate-limit death mode makes it fleet-relevant, because any agent spawning sub-agents can hit it.** My 7/16 `outbox/2026-07-16_to-PROME_closeout-reaping-gap.md` is still the open proposal and this is a second data point for it.
3. **A `filing_series.py` helper** — give it a CIK, a form type and N periods, and get one line item across consecutive filings. **Every finding in §2 came from manually diffing four 10-Qs.** This is the single highest-value tool I do not have; the trajectory is repeatedly where the answer lives and it is currently hand-assembled every time.
