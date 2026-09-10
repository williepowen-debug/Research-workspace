# IS THE AI ORDER BOOK CARRYING PHANTOM DEMAND? — REQ-DEWEY-20260829-001
**Date:** 2026-09-02 | **Mode:** Thesis | **Confidence:** MEDIUM-HIGH (decomposition + base rate — primary, reproducible) · MEDIUM (turbine read — primary filings, deciding number undisclosed) · LOW (memory contract-vs-spot discrimination — paywalled)
**Flag ID:** `REQ-DEWEY-20260829-001` (WALTER ledger — **WALTER closes the row, not DEWEY**)
**Recipients:** VULCAN · ZHAO · WATT (action) — HENRY · VIOLET · NEXUS · LIQUID (info) — PROME (pointer)
**Commission:** WALTER → DEWEY, 2026-08-28 20:5x ET (Will-directed). Deadline 2026-09-08.

> ## ⛔ ERRATUM — 2026-09-10 (DEWEY, self-applied). ONE CELL OF §2.5 WAS WRONG. THE REPORT'S FINDINGS ARE UNAFFECTED.
>
> **As shipped, §2.5 claimed the phrase *"primarily related to the procurement of memory"* exists in NO NVDA primary document — a "VERIFIED absence" across all three Q2 FY27 primaries. THAT IS FALSE FOR ONE OF THE THREE.**
>
> **The phrase exists verbatim, 1 hit, in 8-K Exhibit 99.2** (`q2fy27cfocommentary.htm`, CFO Commentary of Colette M. Kress, accession `0001045810-26-000073`, Item 2.02, filed 2026-08-26): *"Our commitments increased from $119 billion last quarter to $279 billion, primarily related to the procurement of memory."* **Found by VULCAN 2026-09-06; re-verified at EDGAR by DEWEY's own pull 2026-09-10.** Routed as `SIG-W-20260908-001` / `COR-20260908-01`.
>
> **The other two cells stand, both re-confirmed 2026-09-10:** Ex-99.1 press release — 0 hits. 10-Q — 0 hits; it says *"primarily memory AND manufacturing facilities."*
>
> **Mechanism of the error, stated because it is the useful part:** `scripts/edgar_doc.py doc` **without an explicit `--doc` returns only the FIRST document in an accession, with no warning and no list of the others.** I ran the 8-K check, the helper handed me Ex-99.1, and I recorded that clean result as *"the 8-K."* The scan was clean against the wrong referent. `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — and the irony is exact: §2.5 exists to catch an attribution nobody opened, and was itself an attribution I had not opened. Logged to `scripts/BACKLOG.md` as a build item.
>
> **⚠️ WHAT DOES NOT CHANGE, and it is nearly everything:** the source-absence verdict FLIPS; **the inability to size the memory leg HOLDS.** Neither document discloses a memory-only dollar amount or share, so a memory-only reconciliation of the $279B remains **not computable** — which is the load-bearing conclusion §2.5 fed into. $119B→$279B stands. The §2.1 decomposition (~2-year horizon extension = 100% of the +$160B in FY28-29; ~45%/qtr near-term acceleration like-for-like), the GEV slot-reservation finding, and the ON Semi base rate **never depended on the attribution** and are untouched (VULCAN concurs, KB-VULCAN-147).
>
> **🔑 The sharper finding that replaces the dead one:** *two NVDA documents filed the same day attribute the same $119B→$279B differently — the NARROW memory attribution lives in a FURNISHED exhibit (the 8-K states the press release and CFO Commentary are "furnished and shall not be deemed filed" for Section 18), while the BROADER "memory and manufacturing facilities" wording lives in the FILED 10-Q.* **Prefer the filed wording where they disagree; quote the CFO line as CFO commentary, never as the filing's operative words.** (VULCAN's formulation, adopted.)


## 0. PRE-REGISTRATION — written 2026-09-02 19:28 ET, BEFORE any evidence was gathered
*(Commission requirement: "Write down, before gathering evidence, what would show the order book is CLEAN.")*

**What would show the order book is CLEAN (any of these, and I commit to reporting them if found):**

| # | Clean-book observable | Where it would show |
|---|---|---|
| C1 | NVDA's committed procurement, phased by year, sits **at or below** credible announced industry memory capacity for those same years | 10-Q phasing vs Samsung/SK Hynix/Micron/CXMT capex + wafer-start guidance |
| C2 | Memory **contract prices sit at or below spot** (no sustained contract-over-spot premium), i.e. buyers are not paying up to lock supply | DRAM/HBM contract vs spot series |
| C3 | Turbine/memory contracts carry **high cancellation penalties or non-refundable deposits** — a backlog that costs real money to walk away from is not a queue position | GEV / Siemens Energy / MHI contract terms; NVDA supplier-obligation language |
| C4 | Turbine backlog **coverage ratios are flat or falling** relative to delivery capacity, and slot dates are being pulled forward not pushed out | GEV/SE backlog vs revenue-recognition schedules |
| C5 | The 2021-22 analogue **fails structurally** — that cycle's driver (broad consumer/auto electronics, allocation-era distributor stocking, many small buyers) has no counterpart in a market with ~5 buyers on multi-year contracts | Base-rate leg |
| C6 | The commitment jump is explained by a **disclosed accounting/scope change** (new commitment types brought in-scope, a re-measurement, prepayment reclassification) rather than incremental ordering | 10-Q footnote text, prior-period comparatives |
| C7 | Order growth is matched by **deployed** capacity growth (installed MW, racks shipped, revenue recognized) at a stable ratio — orders and deployment growing together is demand, not phantom | Hyperscaler capex actuals vs NVDA revenue |

**What would show a PHANTOM:** sustained contract-over-spot premium; committed procurement above credible deliverable capacity; cheap/no-penalty cancellation; backlog growing faster than deliveries with slot dates slipping; buyers ordering above stated need (Bernstein) with no offsetting scarcity rationale.

**Declared search bias:** the commission arrived with a direction baked in (two same-day signals, a fleet that had never recorded the mechanism). If every confound found points one way, that is a fact about the search. I will state explicitly which legs returned CLEAN evidence.

*(Sections below written after evidence gathering.)*

---

## 1. KEY FINDING

**The $119B → $279B jump is real, like-for-like, and primary-verified. Decomposed, TWO things happened at once — the commission's framing assumed it would be one or the other.** (1) **The horizon extended by ~2 years:** 100% of the $160B increase sits in FY2028–FY2029, building a forward ordering ladder that did not exist one quarter earlier. (2) **Near-term ordering ALSO accelerated ~45% per quarter** on a like-for-like basis ($31.7B/qtr → $46.0B/qtr) — the raw "near-term bucket fell $3B" reading is a **perimeter error**, because that bucket covers 3 quarters in the Q1 filing and 2 in the Q2 filing (§2.1).

**The discriminating instrument the commission asked for exists, and it is in the primary:** NVIDIA's own 10-Q discloses that this commitment class is, "in certain instances," **cancelable, reschedulable, or adjustable "prior to placing firm orders."** The $279B is explicitly **not** a firm-order book — and **NVIDIA does not quantify what share IS firm.** That undisclosed split is the single largest gap in this report and it is structural: the number does not exist in public filings.

**On the phantom question the primary evidence cuts BOTH ways and I am reporting the clean side as prominently as the phantom side**, per the pre-registration: every NVIDIA-internal over-commitment gauge that exists moved in the CLEAN direction this quarter (excess-inventory-obligation accrual DOWN 22%, inventory provisions down as a share of revenue, inventory flat against sales, gross margin up, customer prepayments up 17×, customer concentration down).

---

## 2. THE PRIMARY SPINE — NVIDIA supply & capacity commitments, five vintages

All figures from SEC filings, CIK 0001045810. **Accession numbers and URLs in §7.**

| As of (balance-sheet date) | Supply / capacity commitment | Stated phasing | Filing |
|---|---|---|---|
| Jul 27, 2025 (Q2 FY26) | *total* future commitments, all categories, $30.9B in remainder-FY26 + $6.6B FY27 + $3.9B FY28 + $2.7B FY29 + $1.4B FY30 | near-term concentrated | 10-Q 2025-08-27 [PRIMARY] |
| Oct 26, 2025 (Q3 FY26) | **$50.3B** | "substantially all will be paid through fiscal year 2027" | 10-Q 2025-11-19 [PRIMARY] |
| Jan 25, 2026 (FY26 10-K) | **$95.2B** | "substantially all will be paid through fiscal year 2027" | 10-K 2026-02-25 [PRIMARY] |
| Apr 26, 2026 (Q1 FY27) | **$119B** | **$95B in remainder-FY27**; balance across FY2028–FY2031 | 10-Q 2026-05-20 [PRIMARY] |
| Jul 26, 2026 (Q2 FY27) | **$279B** | **$92B rem-FY27 · $87B FY28 · $88B FY29 · $6B FY30 · $5B FY31 · $1B FY32+** | 10-Q 2026-08-26 [PRIMARY] |

*(The 10-K figure is the audit Critical Audit Matter's exact number: "the Company's consolidated outstanding inventory purchase and long-term supply and capacity obligations balance was $95.2 billion, of which a significant portion relates to inventory purchase obligations." [PRIMARY, FY26 10-K])*

### 2.1 The composition finding — this is the answer to "the finding is in the phasing"

| Bucket | Q1 FY27 (Apr 26, 2026) | Q2 FY27 (Jul 26, 2026) | Δ |
|---|---|---|---|
| **Current-FY remainder** | $95B | $92B | **−$3B** |
| **FY2028 and beyond** | ~$24B (residual) | $187B | **+$163B** |
| Total | $119B | $279B | +$160B |

**Three consecutive quarters of flat near-term commitment in DOLLARS — $95.2B (Jan) → $95B (Apr) → $92B (Jul)** — while quarterly revenue went $81.6B (Q1 FY27) → $96.2B (Q2 FY27), +18% QoQ and +106% YoY [PRIMARY, Q2 FY27 10-Q].

⚠️ **BUT THAT COMPARISON HAS A PERIMETER ERROR, AND CORRECTING IT REVERSES THE SIGN.** "Remainder of FY27" is a *shrinking window*: from Apr 26, 2026 it covers **3 quarters**; from Jul 26, 2026 it covers **2**. Normalised per quarter:

| Vintage | Near-term bucket | Quarters covered | **Per-quarter run-rate** |
|---|---|---|---|
| Apr 26, 2026 | $95B | 3 (Q2+Q3+Q4 FY27) | **$31.7B/qtr** |
| Jul 26, 2026 | $92B | 2 (Q3+Q4 FY27) | **$46.0B/qtr** |

**Near-term committed ordering ACCELERATED ~45% per quarter.** The raw bucket comparison says "flat"; the like-for-like comparison says "up 45%." `[[finding_cross_entity_comparison_needs_same_perimeter]]` — caught in-run against my own first draft, which had shipped the unnormalised read.

**And the same normalisation applied across the ladder is the single most hoarding-consistent datum in this report, and it comes from a primary:** $92B over 2 quarters = **$46.0B/qtr**, against FY28's $87B over 4 quarters = **$21.75B/qtr**. **The near-term commitment runs at 2.11× the FY28 rate.** Paired with inventories +22.4% QoQ ($25,797M → $31,575M [PRIMARY]), **NVIDIA is itself front-loading.**

⚠️ **The honest counterweight, stated with equal weight:** a near-term bucket *should* run hotter than an out-year bucket, because it contains in-flight orders about to be delivered while out-years fill in as time passes. A ladder built one quarter ago has had one quarter to populate FY28. **2.11× is therefore not by itself evidence of over-ordering** — it is the number that would have to be tracked across the next two or three 10-Qs to become evidence. Which direction it moves is the near-dated test.

**Net on the phasing: near-term ordering DID accelerate (+45%/qtr like-for-like), and the horizon ALSO extended by ~2 years. Both happened. The commission's framing assumed the finding would be one or the other.**

The ladder's shape is itself informative: **$92 / $87 / $88 / $6 / $5 / $1**. It runs hard for three years and then cliffs ~93% into FY2030. That is the shape of multi-year contracted supply agreements with ~3-year terms, not of an open-ended demand extrapolation. It is also the shape a buyer produces when it moves from one-year to three-year coverage in one step.

### 2.3 The cancellation-economics leg — answered from the primary, in both directions

**Identical language appears in every filing back to Q2 FY26** [PRIMARY, four filings checked]:

> "We enter into agreements with our suppliers that allow them to procure inventory based upon our defined criteria, and **in certain instances, these agreements may be cancelable, rescheduled, or adjustable for our business needs prior to placing firm orders.** Changes to these agreements may result in additional costs."

**And the counterweight, from the same filings' risk factors:**

> "The impact of these risks would be amplified by our **non-cancellable and non-returnable purchase orders** placed in advance of our historical lead times… These risks have increased and may continue to increase as our **purchase obligations and prepaids have grown** and are expected to continue to grow and become a greater portion of our total supply." [PRIMARY, Q1 FY27 10-Q risk factors]

⚠️ **The decision-critical quantity is the split between the cancelable and the non-cancellable portion, and NVIDIA does not disclose it.** "In certain instances" is the entire disclosure. This is the single largest gap in this report and it is a **structural** one — the number does not exist in public filings. **[SEARCH-NOT-FOUND → the split is UNKNOWN, not zero and not all.]**

### 2.4 Every NVIDIA-internal over-commitment gauge moved CLEAN this quarter

These are the observables that would deteriorate first if NVIDIA's own book were over-committed. All [PRIMARY, Q2 FY27 10-Q]:

| Gauge | Prior | Jul 26, 2026 | Direction |
|---|---|---|---|
| **Excess inventory purchase obligations** (accrued liability) | $2,739M (Jan 25, 2026) | **$2,138M** | **↓ 22% — falling** |
| Inventory provisions + excess-obligation provisions, H1 | $6.3B H1 FY26 (incl. $4.5B H20) → $1.8B ex-H20 | $2.1B H1 FY27 | ~flat in $, on **2× revenue** ⇒ ↓ as % |
| GM drag from those provisions, H1 | 5.9% (H1 FY26) | **1.0%** | ↓ |
| Inventories | $14,962M (Jul 27, 2025) | **$31,575M** | +111% YoY |
| Inventory ÷ quarterly revenue | 32.0% (Q2 FY26) | **32.8%** (Q2 FY27) | **flat** |
| Gross margin | 72.4% (Q2 FY26) | **75.0%** | ↑ 2.6pts |
| Customer advances (in deferred revenue) | $160M (Jan 25, 2026) | **$2.8B** | **↑ 17.5×** |
| Largest direct customer, % of revenue | 23% (Q2 FY26) | **16%** | ↓ (concentration falling) |

**Two of these are strong clean-book evidence and I flag them as such:**
- **The excess-inventory-obligation accrual FELL while commitments rose 2.3×.** This accrual is the GAAP mechanism by which an over-committed purchase book shows up. It went *down*.
- **Customer advances rose from $160M to $2.8B.** Customers are putting cash down. Prepayment is the opposite of a costless queue position on the *demand* side of NVIDIA's book — though note it says nothing about the *supply* side, which is where the $279B sits.

**Derived ratio (method stated, not a forecast):** Q2 FY27 cost of revenue $24,079M ⇒ annualised COGS run-rate ≈ $96.3B. Total supply/capacity commitment ÷ annualised COGS: **1.45× at Apr 26, 2026 → 2.90× at Jul 26, 2026.** Coverage doubled in one quarter. Interpretation of whether ~2.9× forward coverage is prudent or excessive is **VULCAN's**, not mine; the arithmetic is stated so it can be reproduced.

**Liquidity, for the record only (not a solvency claim, per scope fence):** $56.6B cash + marketable debt securities, $42.8B marketable equity securities at Jul 26, 2026 [PRIMARY].

### 2.5 ⚠️ CORRECTED 2026-09-10 — the quote IS at a primary (a FURNISHED 8-K exhibit). The memory SHARE is still undisclosed, and that is what instrument 2 actually needed.

*(This section as originally shipped claimed a verified absence across all three primaries. One cell was wrong — see the ERRATUM banner at the top of this report for the full record of what was claimed, what is true, and why the error happened.)*

Because the commission builds instrument 2 on it, I chased the phrase through **every primary document in NVIDIA's Q2 FY27 disclosure set**. Corrected results, all three re-verified at EDGAR 2026-09-10:

| Document | Status | Accession | Contains "procurement of memory"? |
|---|---|---|---|
| 10-Q (Q2 FY27) | **FILED** | 0001045810-26-000075 | **No** — says "primarily memory **and manufacturing facilities**" |
| 8-K **Ex-99.2, CFO Commentary** (`q2fy27cfocommentary.htm`) | **FURNISHED** (not deemed filed, §18) | 0001045810-26-000073 | ✅ **YES — verbatim, 1 hit.** ⛔ *Originally reported here as "No." That was wrong.* |
| 8-K Ex-99.1, Press Release (`q2fy27pr.htm`) | **FURNISHED** | 0001045810-26-000073 | **No** — contains neither "memory" nor "279" |


The Ex-99.2 sentence, in full [PRIMARY, NVDA 8-K Ex-99.2, filed 2026-08-26, DEWEY EDGAR pull 2026-09-10]:

> "Our commitments increased from $119 billion last quarter to $279 billion, **primarily related to the procurement of memory**."

The 10-Q's actual words, for the contrast [PRIMARY, Q2 FY27 10-Q, Note 10]:

> "These supply commitments are for our **data center infrastructure systems, primarily memory and manufacturing facilities**, to produce our products for long-term demand across current and future product architectures."

**🔑 What instrument 2 actually needs, and this is unchanged by the correction: NEITHER DOCUMENT DISCLOSES A MEMORY-ONLY DOLLAR AMOUNT OR SHARE.** The commission's cleanest single test — reconcile committed memory procurement against credible industry memory capacity for FY27-29 — **is not computable from either wording**, because the numerator does not exist in the disclosure. A reconciliation run against the $279B total as though it were a memory number **overstates the memory claim by an unknown amount**. That was §2.5's load-bearing output and it survives the correction intact.

**Confidence: VERIFIED (corrected).** ⚠️ **The original "VERIFIED absence" carried a defect the confidence label could not express:** the finding generalised from *one exhibit my helper actually opened* to *"every primary document."* An absence claim is only as wide as the document set genuinely searched, and mine was narrower than the sentence describing it. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` · `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — the 10-Q row carried two independent checks and is right; the two 8-K rows carried one each, and one of those was wrong. *(The phrase was re-asserted as [PRIMARY, 8-K] by one of this run's own sub-agents, which is how I came to check the 8-K at all — and the sub-agent was right.)*

**Consequence, and it is not cosmetic:** the $279B is *not* a memory-only number. Any reconciliation of $279B against memory-industry capacity **overstates the memory claim by an undisclosed amount**, because foundry, CoWoS/advanced-packaging and prepaid capacity reservations sit inside the same total and are not broken out.

---

## 3. THE MEMORY LEG — is the memory market hoarded, and can it deliver?

### 3.1 The market is BIFURCATED, and treating it as one market is the analytical error

| Channel | State | Evidence |
|---|---|---|
| **AI / server / HBM** | **Tight-and-clean** — contracted, LTA-structured, volume-locked | SK hynix: 2026 sold out, ~10 customers on **~5-year LTAs** [PRIMARY, Q2 2026 call]; Micron: entire CY2026 HBM **price AND volume locked**, incl. HBM4 [PRIMARY, FQ1-26 call] |
| **Consumer / module / distributor** | **Hoarding signatures, unwinding since March 2026** | DDR5 retail −7.2% MoM Germany, −20% US, −25–30% China (2026-03-31) while contract held flat [INSTITUTIONAL, TrendForce]; Lenovo CFO: memory inventory ~50% above normal [NEWS, untraced to transcript] |

### 3.2 The contract-vs-spot spread — direction established, LEVEL not established

| Period | Spot | Contract (server DRAM) | Spread |
|---|---|---|---|
| 4Q25 | surging ahead | +45–50% QoQ | spot far above contract (upcycle-normal) |
| Jan 2026 | DDR4 spot peak | +93–98% QoQ (1Q26) | peak premium ~172% [UNVERIFIED, single-source] |
| Mar 2026 | DDR5 retail **rolls over** | held flat | **first divergence** |
| 2Q26 | gains narrow | +58–63% QoQ | compressing from the spot side |
| 3Q26 (Jul–Aug) | sideways; DDR4 $42.50, **+0.93% w/w** | **+13–18% QoQ** | still compressing; both decelerating |

⚠️ **Important instrument correction to the commission's framing.** The commission says "sustained contract-over-spot premia are the classic hoarding tell." **In DRAM the normal upcycle configuration is the reverse — SPOT trades ABOVE contract, and spot LEADS contract by a stated 1–2 months** [INSTITUTIONAL, TrendForce quoting a module executive, 2026-03-31]. The signature to read here is therefore **the compression of the spot premium**, which has fallen monotonically for five months from an extreme to near-stall.

**Two live readings, and I cannot discriminate between them with obtainable data:**
- **Hoarding-unwind:** the March spot break was distributors dumping speculative inventory; with a 1–2 month lead, contract deceleration should show in **4Q26/1Q27**. *Falsifiable and near-dated.*
- **Composition artifact:** spot is a *consumer/module* market and contract is now a *server/LTA* market, so spot has stopped being an instrument for the server market at all. TrendForce attributes the moderation to consumers "reaching their affordability limit," not server destock. `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`

⚠️ **A third instrument caveat that undercuts both:** TrendForce states that **from 3Q26 the source of contract increases shifts to non-LTA customers and incremental supply sold outside LTAs.** The published contract index is therefore drifting toward measuring **the marginal, non-contracted buyer** — precisely the population most likely to be double-ordering. Comparing 3Q26's +13–18% to 1Q26's +93–98% is **not like-for-like: the measured population changed.**

### 3.3 Capacity reconciliation — the deliverability test, with the assumption named

**⚠️ Every figure in this subsection inherits one undisclosed assumption: what share of NVIDIA's commitment is memory.** NVIDIA does not break it out (§2.5). Cases run at 50% / 75% / 90% of the $160B increment.

**Dollar test.** Micron's HBM TAM path $35B (2025) → ~$100B (2028), ~40% CAGR [INSTITUTIONAL — attributed to Micron FQ1-26 prepared remarks/call by this run's memory leg; **DEWEY could not re-verify at the primary**: Micron IR `static-files` returns HTTP 403 / JS-gated to both `fetch_url.py` and direct urllib] interpolates to CY2027 ≈ $69B. NVDA FY28 memory at the 75% case ≈ $37.4B = **54% of CY2027 HBM TAM. PASSES** — NVIDIA is the largest single HBM consumer.

**Bit cross-check — this is the test that bites.** At ~$32/GB for NVIDIA vs ~$38/GB blended [both UNVERIFIED on level; direction independently corroborated by SemiAnalysis's "VVP" pricing note, INSTITUTIONAL], global CY2027 HBM bits ≈ 1.82 EB:
- 75% case → 1.17 EB = **64% of global HBM bits**
- 90% case → 1.40 EB = **77% of global HBM bits → REFUTED**, since Broadcom, AMD and Google TPU allocations are separately contracted and TrendForce names Google TPU as the fastest-growing HBM demand source into 2027.

➡️ **Derived bound: memory is ≤ ~75–80% of NVIDIA's commitment.** This is a constraint the arithmetic produces, not an input.

**Internal consistency check (independent inputs, and they reconcile).** Index 2026 total DRAM bits = 100. HBM share 9% → 13% (2027); total supply growth ~16–17% [IDC] ⇒ 2027 HBM bits = 15.2 ⇒ **HBM bit growth +69% YoY**. TrendForce independently forecasts **HBM demand +68% YoY 2027**. **Agreement to within 1pp from independent sources — announced capacity DOES deliver the 2027 HBM bits.**

**But the residual is the story.** Conventional DRAM 2027 = 117 − 15.2 = 101.8 ⇒ **+11.9% YoY only**. HBM consumes ~3× silicon area per GB; HBM wafer input goes 22% → 30% of total DRAM wafer input in 2027 to yield 9% → 13% of bits. **Every HBM wafer erases ~3× its DDR5-equivalent. The 2027 squeeze is in CONVENTIONAL DRAM, not HBM — and that mechanism is arithmetic, not ordering psychology.**

**FY29 ($88B) is UNKNOWN, not merely uncertain** *(status changed same-day — see the update box below)*. No bit-denominated industry supply forecast for CY2028 or CY2029 was found **by this run**, so the reconciliation above could not be run for that year. The fabs are announced and funded (Samsung P5 2028 + Yongin **pulled forward** to 2029 from 2030-31; SK hynix Yongin Ph.1 cleanroom early 2027, M15X pulled forward; Micron $200B US + $24B Singapore; CXMT to 500 kwspm by end-2028) — the risk is timing/yield, not existence.

### 3.4 ✅ CXMT output in BITS — CLOSED at the primary, 2026-09-02 (updated post-delivery)

> **📌 UPDATE 2026-09-02, after this report was delivered.** I recorded this leg as SEARCH-NOT-FOUND and named the CXMT STAR Market IPO prospectus as the **unchecked fallback**, declining to upgrade to VERIFIED without it. **ZHAO reached it the same day** and closed the leg (`inbox/processed/2026-09-02_from-ZHAO_your-named-fallback-is-reached...`, commit `66ac967a4`). The original text is superseded below rather than deleted, because the *reason* the number is absent turned out to matter more than the absence.

**As originally delivered:** ZHAO's own STATUS recorded VULCAN's CXMT ask at **n=3 (8/3, 8/13, 8/21)**, replied 8/21 with "a disposition, not an answer"; bit-output **"not ZHAO's, UNCHECKED (not 'unavailable')"**, no date promised. This run's independent attempt returned **SEARCH-NOT-FOUND**, **not upgraded to VERIFIED**, and **no proxy was substituted** — per the commission's instruction.

**Now closed — SEARCH-NOT-FOUND → VERIFIED ABSENCE, and the absence is DELIBERATE:**

CXMT STAR Market IPO prospectus, SSE `002170_20260517_MGLN.pdf` (2026-05-17), pulled and text-extracted, 411,324 chars [PRIMARY, via ZHAO]:

> **The unit string 万片 (10,000 wafers — the standard PRC capacity unit) appears exactly THREE times in the entire document, all three inside a profitability SENSITIVITY table as deltas (±2万片/月, −3万片/月). There is no absolute 产能 / 产量 / 销量 figure anywhere in the filing, in wafers OR in bits.**

⇒ **CXMT disclosed ratios and growth rates only, never a level.** That is a materially better answer than "we looked and did not find it," because it says **why** the number does not exist. `[[finding_owner_of_record_means_authoritative_not_correct]]` — redaction suppresses a number's falsifier.

**What the filing DOES disclose (several on a BIT basis)** [all PRIMARY]:

| Figure | Value | Basis |
|---|---|---|
| Capacity utilisation 2023/24/25 | 87.06% / 92.46% / **95.73%** | wafer — **running flat out** |
| Total DRAM sales-volume CAGR 2023→2025 | **+83.98%** | **BITS** (销量按容量口径) |
| DDR-series 2025 volume | **+282.22%** (ASP +61.00%, rev +515.36%) | **BITS** |
| LPDDR-series 2025 volume | **+65.18%** (ASP +24.46%, rev +105.59%) | **BITS** |
| Global DRAM share Q4-2025 | **7.67%** | **REVENUE** (Omdia, cited in-prospectus) |
| Omdia global DRAM content | 2025 **40.16 EB** → 2030 **97.42 EB** | **BITS** |

**✅ My "no HBM project" claim is CONFIRMED at the primary** — I had carried it as *"reportedly."* IPO use of proceeds RMB 29.5bn = **13.0bn DRAM tech upgrade / 9.0bn next-gen DRAM R&D / 7.5bn wafer-line upgrade. No dedicated HBM project.**

⚠️ **But carry ZHAO's qualifier, which cuts against my own framing:** *"no HBM in the IPO projects" is NOT "no HBM ever"* — SemiAnalysis separately models CXMT HBM wafers at **5 → 30 → 55 → 100 kwspm across 2025-2028**. My line "CXMT relieves conventional DRAM only" is a statement about **what this raise funds**, not about CXMT's roadmap. **The analytical point survives for the 2027 window and should not be extended past it.**

⚠️ **BASIS TRAP — a reader guard, because the trap is one hop from my own citation.** I carried SemiAnalysis's **bit-share 9% (2025) → 12% (2027)**, correctly typed. **The figure that has travelled furthest from that same author — "~17% of global DRAM supply by 2028" — is WAFERS, not bits.** Same note, same author, ~5-point basis gap that most relaying outlets erase. Also **strike "30% of global DRAM by 2030"** on sight: unmodelled investor soundbite, no stated basis. And **"350k WSPM, just 25,000 below Micron"** is single-lineage (Citrini, Jul 2026, ~7 relayers) — the 350k level is corroborated, **the 25k gap is not** (SemiAnalysis puts Micron at 385k ⇒ a 35k gap). `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`

⚠️ **AND THE BASE ITSELF IS CONTESTED — this propagates into §3.3.** Omdia **~240k wpm and FLAT through 2026** / SemiAnalysis 265k / Nomura 280k / Reuters ~300k / Counterpoint 320k. **±25% uncertainty before any forecast is applied.** ⇒ **the "CXMT to 500 kwspm by end-2028" figure I cited in §3.3 inherits that spread**, and Omdia's flat-through-2026 view is a live alternative to the ramp I quoted.

**📌 One input I declared absent now exists.** §3.3 says no bit-denominated CY2028/29 forecast was found; the prospectus carries **Omdia global DRAM content 2025 40.16 EB → 2030 97.42 EB, in BITS** — interpolable, and a genuine input to the FY29 test. ⛔ **I am deliberately NOT retro-fitting arithmetic onto it tonight:** it is a **DEMAND/content** series, and the FY29 question is a **SUPPLY** question. Running one into the other is precisely the basis error this section warns about. **Registered as follow-on work** (natural owner: ZHAO or VULCAN), not silently folded into the verdict.

**Fleet state:** the ask is **CLOSED** — ZHAO's answer went to VULCAN 2026-09-02 at **n=4 asks / 30 days**. Nothing owed back to me.

---

## 4. THE TURBINE LEG — and the commission's founding evidence could not be reached

### 4.1 ⛔ THE BERNSTEIN SURVEY: SEARCH-NOT-FOUND — do not carry the 75% / 25% figures

**Neither the primary note NOR a single identifiable republisher could be reached.** 11 distinct query formulations were run: the exact percentages; "ordering more than they need"; "over-ordering" / "double ordering" + Bernstein; three named Bernstein analysts (Chad Dillard, US Machinery; Nicholas Green; Deepa Venkateswaran, Head of Utilities & Clean Energy); a news-domain-restricted pass; and phantom-demand framings.

**Confidence: SEARCH-NOT-FOUND — explicitly NOT upgraded to VERIFIED-absent.** Bernstein research sits behind a subscriber wall this desk cannot reach, so absence of a public trace is weak evidence of absence of the note.

⚠️ **A likely conflation source, flagged but not established:** searches repeatedly surfaced **GE Vernova management speaking AT a Bernstein conference (May 2025)** about slot-reservation deposits. That is a company appearance at a Bernstein *event*, not Bernstein *survey research*. Whether the commission's 75%/25% derives from a garbled transmission of that is **unknown and I am not asserting it.**

**Consequence for the commission:** `SIG-W-20260828-034` is one of the **two** arrivals that made this a commission rather than a note, and its testable claim ("measurable here by equipment class") rests on a survey **this run could not put its hands on.** ⇒ **The "two independent arrivals of the same mechanism" premise is now one verified arrival (NVDA, primary) and one unreached claim.** That materially weakens the convergence case *as constructed* — and it is why the backlog record below matters: **it answers the underlying question without the survey.**

### 4.2 GE Vernova — the headline GW is 54% slot reservations, and the filing says so

**The single most decision-relevant fact in this leg, and it is primary-verifiable:**

> **116 GW "under contract" = ~53 GW firm equipment backlog + 63 GW slot reservation agreements.**

Reconciliation (Q1'26: 44 firm + 56 slots = 100 GW; Q2: 44 + 10 converted + 2 direct − 3 shipped = **53 firm**; slots 56 → **63**; 53 + 63 = **116** ✓). An independent third-party analysis reaches the same 53/63 split — a cross-check with **no free parameter** [`[[finding_crosscheck_with_free_parameter_validates_nothing]]` satisfied].

**Why this is not semantics — three findings I verified myself at the primary today:**

| Check | Result | Where |
|---|---|---|
| Does GEV's audited RPO exclude cancellable orders? | **YES** — RPO excludes "any order that provides the customer with the ability to cancel or terminate **without incurring a substantive penalty**" | [PRIMARY] GEV FY2025 10-K, lines 1841–1846 |
| Does "slot reservation" appear in the 10-Q's backlog/RPO note? | **NO.** It appears exactly **3 times in the entire Q2 10-Q, ALL in the cash-flow discussion** | [PRIMARY] GEV Q2'26 10-Q, verified by grep |
| Does GEV itself say slots may not convert? | **YES, twice, in its own risk factors** | [PRIMARY] GEV FY2025 10-K |

> "We make capacity expansion decisions and supply commitments based on demand forecasts, orders, **slot reservation agreements, and deposits**. If anticipated demand is delayed or does not materialize, orders may be deferred, reduced, or canceled and **slot reservation agreements may not result in orders**." [PRIMARY, 10-K line 980-981]

> "…some counterparties to slot reservation agreements **may not place orders equal to the value of their reservation amount or at all**, and the volume of orders we expect under such agreements may fail to materialize." [PRIMARY, 10-K line 1114]

**So the 63 GW sits OUTSIDE the audited backlog while sitting INSIDE the number management leads with and the press repeats** ("116 GW", "125 GW by year-end"). A reader treating the headline GW as backlog is reading a figure of materially weaker contractual status than the **$176,284M RPO** disclosed alongside it [PRIMARY, Q2'26 10-Q].

### 4.3 Deliveries are not keeping up — they went BACKWARDS

| Year | GW ordered | GW shipped | Book-to-bill |
|---|---|---|---|
| 2023 | 9.5 | 13.8 | 0.69× |
| 2024 | 20.2 | 11.9 | 1.70× |
| 2025 | 29.8 | 15.3 | 1.95× |
| **H1 2026** | **20.1** | **7.5** | **2.68×** |

[PRIMARY, GEV 10-K FY2025 + 10-Q Q2'26; book-to-bill derived]

**Cumulative orders-over-deliveries since 2024: +35.4 GW.** And **H1'26 deliveries FELL YoY: 7.5 GW vs 8.2 GW (−8.5%)** — unit count rose (54 vs 40) but mix shifted hard to small aeroderivatives (26 units vs 10) while HA-class shipments fell (8 vs 13). Management's "20 GW annualised in Q3 2026" is a forward claim the delivered record does not yet contain; annualising H1 gives ~15 GW, **flat on 2025**.

**Slot dates are extending, on management's own account:** Strazik expects to be "more than halfway contracted for **2031**" by year-end; on 2032, "we need more time before we can articulate the timing of contracting."

**Backlog coverage at current delivery rates:** **GEV 3.5 yrs firm / 7.6 yrs incl. slots · Siemens Energy ~4.5 yrs · MHI ~2.2 yrs.**

### 4.4 Cancellation economics — genuinely two-sided, and the decisive number is undisclosed

**Arguing the slots are NOT cheap options:**
- GEV 10-K revenue policy: *"we receive progress collections from customers for large equipment purchases to generally reserve production slots."* [PRIMARY]
- **Power contract liabilities $16,527M (12/31/25) → $27,679M (6/30/26) = +$11,152M, +67.5% in six months** [PRIMARY, both figures verified by DEWEY in the Q2'26 10-Q Note 9 table].
- H1'26 operating cash carries **+$11.8B** of contract liabilities "primarily due to higher down payments on orders **and slot reservation agreements** at Power" [PRIMARY, verified at line 6705].
- Management (Bernstein conference, May 2025): GEV won't "protect any slots with anyone without substantial cash down," averaging **~20% of contract price**. ⚠️ **[UNVERIFIED-secondary on the 20%]** — reached only via a paywalled substack reporting conference remarks; no transcript obtained. **The EXISTENCE of substantial deposits is [PRIMARY]; the 20% magnitude is not.**
- Siemens Energy runs the same economics and names it: FCF "again benefited from **customer advance payments, including reservation fees**" [PRIMARY, Q3 FY26 release].

**Arguing they are options anyway:** GEV's own two risk factors above. The consequence GEV names for itself is not lost revenue but **stranded capacity** — "excess or idle capacity, under-absorption of fixed costs… inventory build and write-downs… impairment of long-lived assets."

⚠️ **THE MOST DECISION-RELEVANT SINGLE NUMBER IN THIS ENTIRE COMMISSION IS NOT DISCLOSED BY ANY OF THE THREE OEMs: the historical slot-to-order conversion rate.** GEV discloses one quarter's conversion (10 GW) with **no denominator**, no cumulative rate, and no cancellation history. No contract language is public; refundability, forfeiture schedule and reschedule rights are unknown for GEV, Siemens Energy and MHI alike. **[SEARCH-NOT-FOUND, structural.]**

### 4.5 The mechanism IS documented — one layer upstream

**Wood Mackenzie: US grid operators/utilities are likely to commit to only ~28% of the 1,066 GW requested for data-centre projects**, because developers *"submit many simultaneous applications across multiple regions only to pick the most viable one."* [INSTITUTIONAL via Bloomberg, 2026-08-12]

**This is the single most important substitute for the unreachable Bernstein survey.** The behaviour the survey allegedly measured at the *turbine* layer is measured, by a different institution with a published denominator, at the *grid-interconnection* layer — and the implied duplication factor there is ~3.6×. It is **not** the same instrument and does not transfer mechanically to turbine orders; it is corroborating evidence that multi-siting/option-taking is an established, quantified behaviour in this buildout.

### 4.6 Counter-evidence — the clean-book case for turbines

1. **Deposits are large and show up in cash** ($11.1B at Power in six months). Forfeiting ~20% of a $300m package ≈ $60m — not free optionality.
2. **Genuine multi-year physical shortage:** ~100 GW of 2025 global orders against est. 60–70 GW/yr industry capacity; prices +195% toward ~$600/kW by end-2027 [INSTITUTIONAL, Wood Mackenzie]. **Pre-ordering at 4–5-year lead times is rational, not speculative.**
3. **Diversified customer base:** GEV ~80% traditional utilities / ~20% data-centre operators, ~100 entities in 26 countries — concentrated speculation is harder to hide in that distribution [NEWS].
4. **Explicit screening at MHI:** *"we are being selective in the projects we contract"* — CFO Nishio [NEWS, 2026-08-13].
5. **Utilities screen downstream:** Exelon cites "transmission security agreements" to weed out speculative projects [NEWS].
6. **Turbines may not be the binding constraint** — Strazik: turbines are "often not the binding constraint on project delivery" (EPC, permitting, fuel compete). If so, slots pulled forward reflect project sequencing, not phantom demand [NEWS].
7. **MHI's book is only ~2.2 years deep** — inconsistent with a market-wide speculative blow-off. **The excess sits where the slot-reservation instrument is most aggressively used, not across the industry.**

**Where the clean case breaks down:** it defends the *deposit* and the *shortage*, **not the conversion**. GEV's own risk factor concedes reservations may not convert; a 20% deposit leaves 80% of the decision open, and for an IPP holding a queue position worth more than the deposit, **forfeiting is a rational outcome rather than a failure.**

---

## 5. THE BASE RATE — the 2021-22 analogue, and it inverts the commission's instrument list

### 5.1 ★ THE HEADLINE BASE-RATE FINDING: the order book is the LAST thing to turn

**Dated sequence of the 2021-23 semiconductor cycle**, with each observable's lead/lag against the first industry-billings YoY decline (Sep-2022 = reference):

| # | Observable | Turned | Lead/lag | Tag |
|---|---|---|---|---|
| **1** | **DRAM/module SPOT price** — "demand for PC DRAM in the spot market began to show signs of bearish movement in early July" | **early Jul 2021** | **−14 months** | [INSTITUTIONAL] TrendForce |
| 2 | DRAM **contract** price (guided −3–8% QoQ for 4Q21) | Sep 2021 | −12 mo | [INSTITUTIONAL] |
| 3 | End-market unit shipments (PC, smartphone) | Q1 2022 | −6 mo | ⚠️ **UNVERIFIED — gap** |
| 4 | **Lead times** — 27.1w May-22 → 27.0w Jun-22, "none posted record-high LTs, perhaps another sign of *peak cycle*" | **May/Jun 2022** | −3 mo | [NEWS] verified at artifact |
| 5 | First major supplier guidance cut (Micron FQ3'22, FY23 WFE capex cut) | 2022-06-30 | −3 mo | [PRIMARY] |
| 6 | Lead times' biggest-ever monthly drop (26.3w → 25.5w) | Oct 2022 | +1 mo | [NEWS] |
| 7 | **Industry billings YoY** — first decline since Jan-2020 | **Sep 2022** | 0 (ref) | [INSTITUTIONAL] ⚠️ snippet-sourced |
| 8 | **Reported contracted backlog PEAKS** (ON Semi LTSA RPO) | **2023-06-30** | **+9 mo** | [PRIMARY] ✅ |
| 9 | **Distributor inventory peaks** (Arrow Sep-23 $5.81bn; Avnet Dec-23 $6.12bn) | **Q3–Q4 2023** | **+12–15 mo** | [PRIMARY] ✅ |
| 10 | Supplier inventory peaks (TI still rising Dec-24 $4.53bn) | **≥Q4 2024** | **+27 mo** | [PRIMARY] ✅ |
| 11 | Explicit contract-renegotiation disclosure (GF 20-F) | Apr 2024 | +19 mo | [PRIMARY] ✅ |

> ⚠️ **THE ACTIONABLE INVERSION, AND IT CONTRADICTS THIS COMMISSION'S OWN INSTRUMENT LIST.** The metrics the commission names — **backlog, book-to-bill, channel inventory, cancellation disclosures** — ran **9 to 27 months LATE** in the reference cycle. **They led in ZERO of 3 well-documented episodes.** The observable that led, in all 3, was **the price of the marginal UNCONTRACTED unit in the most liquid sub-market.**

### 5.2 ★ The contracted-book arc, verified at the SEC XBRL primary by DEWEY today

**ON Semiconductor long-term-supply-agreement remaining performance obligations** — I pulled the full series myself; every value the research leg reported reproduces exactly:

| Date | $bn | Date | $bn | Date | $bn |
|---|---|---|---|---|---|
| 2021-12-31 | 8.6 | 2023-06-30 | **20.0 ← PEAK** | 2025-04-04 | 10.6 |
| 2022-07-01 | 8.8 | 2023-09-29 | 18.4 | 2025-07-04 | 9.6 |
| 2022-09-30 | 14.1 | 2023-12-31 | 16.5 | 2025-10-03 | 8.1 |
| 2022-12-31 | 16.6 | 2024-06-28 | 14.7 | 2025-12-31 | 7.1 |
| 2023-03-31 | 17.6 | 2024-12-31 | 11.9 | **2026-07-03** | **6.1** |

**−69.5% from peak over 12 quarters, still falling today.** [PRIMARY, `data.sec.gov/api/xbrl/companyconcept/CIK0001097864/us-gaap/RevenueRemainingPerformanceObligation.json`, pulled 2026-09-02 — **VERIFIED at artifact by DEWEY**]

**GlobalFoundries aggregate LTA commitment** [PRIMARY, 20-F series]: >$22bn (2022) → >$20bn (2023) → >$14bn (2024) → ~$11bn (2025) = **−50% over 3 years**; the *cash prepayment* book fell **$5bn → $3bn (−40%)**.

⚠️ **CRITICAL CAVEAT — do not quote these as cancellation rates.** Both series decline through **fulfilment** as well as cancellation, and over the same windows ON's revenue was ~$20bn and GF's ~$21bn, so fulfilment plausibly explains a large share. **The drawdown is an UPPER BOUND on cancellation, not a measurement.** **No issuer examined discloses a cancellation rate. [G-1, structural — not closable with public data.]** No split is invented here.

### 5.3 ★ THE MOST TRANSFERABLE FINDING: contract structure was NOT protective in 2021-22

This is the finding that bears hardest on the "our book is contracted, not speculative" defence — which is precisely the defence available to both NVDA and GEV today.

The 2021-22 cycle **did** have take-or-pay equivalents: **non-cancellable/non-returnable orders** (NXP ~$4bn), **binding multi-year minimum-purchase LTSAs with cash prepayments and capacity-reservation fees** (GlobalFoundries **$22bn committed / $5bn prepaid**; ON **$20bn**). **Every one of them was renegotiated to lower price and/or lower volume.** From the filings, verbatim:

> GF 20-F: *"renegotiated a number of LTAs with certain customers … some have **lower pricing or volume commitments** than originally negotiated"*; FY2024: *"renegotiate certain long-term agreements … to reflect **lower volume commitments** and/or longer commitment timelines."* [PRIMARY]

> ON 10-K FY2024: *"The timing, pricing or amounts of products delivered under LTSAs **may be modified or canceled** … the actual revenue recognized for the remaining performance obligations in future periods **may significantly fluctuate** from current estimates."* [PRIMARY]

> GF FY2023: gross margin was *helped* by **"underutilization payments"** — **customers paid to NOT take contracted volume.** [PRIMARY-adjacent]

**"Take-or-pay" is not an exogenous constraint. It is a negotiating position between two parties who both prefer a live customer to a lawsuit.** `[[finding_adoption_is_not_validation]]`

### 5.4 Base rate across episodes (n=3 usable)

| Episode | Inflated-book duration | Magnitude | First observable that turned |
|---|---|---|---|
| **Semis 2021-23** | price signal → book peak **8 quarters**; book still eroding 12q later | Rev −30% to −57%; inventory +77% to +143%; contracted books −50% (GF) / −69.5% (ON) | **Memory spot price, Jul-2021 (−14 mo)** |
| **Telecom 1999-2001** | ~**5-6 quarters** | World semi sales **−32% in 2001** ($204bn→$139bn, worst ever). **Cisco $2.249bn inventory charge Apr-2001**; raw-parts inventory +300% in one quarter; first loss in 11 yrs | **End-customer (carrier) order intake** — which the component layer could not see |
| **MLCC/passives 2017-19** | ~**6-7 quarters** | Yageo ASP **−15% QoQ Q1-19**, guided −10% more; distributor inventory 6-7 months vs 2-3 normal | **Spot/ASP roll-over**, again ahead of any backlog metric |
| *HDD/Thailand 2011-12* | *excluded* | — | **SEARCH-NOT-FOUND** for double-ordering or cancellation data despite targeted search — recorded as a negative result |

**Synthesis [ESTIMATE, n=3]:** inflated book runs **5–8 quarters** from first price signal to peak of the reported book; **peak-of-book → revenue trough is 3–11 quarters, WIDENING WITH CONTRACT LENGTH** (memory 3q, analog 6-7q, LTSA-heavy power semis 10-11q). **Longer contracts do not prevent the drawdown — they stretch it.** That is directly relevant to a market that just extended its ordering horizon by two years (§2.1).

### 5.5 Structural discriminators — argued BOTH ways, as commissioned

**Arguing the analogue HOLDS:**
- **Contract structure:** the 2021-22 book WAS contracted and prepaid and was renegotiated anyway (§5.3).
- **Buyer concentration is NOT a stabiliser.** Auto OEMs were *few*, and their **simultaneous 2020 cancellation is what CAUSED the shortage.** Few buyers = one board meeting moves the whole book. **This directly refutes the intuition that ~5 hyperscalers are safer than thousands of distributors.**
- **Capacity added on an inflated signal arrives AFTER the signal reverses.** Mechanical; always transfers.
- **A distribution channel is not required.** **Cisco 2001 was direct-sales through contract manufacturers — no distributor — and produced the canonical bullwhip.** The "no distributors this time" argument is refuted by the hardest case in the set. *The channel is wherever inventory can sit unobserved.*
- **The financed non-hyperscaler tier** (neoclouds on GPU-collateralised debt) is the structural analogue of the 2021-22 distributor.

**Arguing the analogue FAILS:**
- **Literal double-ordering cannot execute at the GPU** — it requires placing the same order with multiple suppliers, and there is one dominant supplier. **The mechanism does not transfer to the GPU; it RELOCATES to multi-sourced inputs (HBM, MLCC, HDD/SSD, power gear) — which is where it should be hunted.**
- **Buyer balance sheets:** hyperscaler capex is funded from operating cash flow, not a working-capital line. The financing-driven cancellation channel is absent at the top tier.
- **Excess is metered, not stored.** Surplus compute shows up immediately in falling rental/spot prices and utilisation. **This argues the correction surfaces FASTER, not that it is absent.**
- **Hyperscalers have first-party demand telemetry** — the 2021-22 over-orderers were thousands of small buyers with zero end-demand visibility, the textbook bullwhip precondition.
- **Demand type:** 2021-22 was pulled-forward COVID consumer durables with natural mean reversion; AI compute has no demonstrated pull-forward analogue.
- **Prepay coverage may be higher.** GF's was ~23% ($5bn/$22bn). ⚠️ **G-5: the coverage ratio for AI take-or-pay contracts could not be obtained — this is the single most decision-relevant discriminator and it is UNKNOWN.**

⚠️ **The rebuttal that must be carried against the FAILS column:** every one of those arguments has a 2021-22 twin that was **true and still insufficient** — "auto content growth is secular," "our orders are NCNR," "we have $20bn of binding multi-year commitments," "customers have prepaid us $5bn." All true. All followed by a 30–57% revenue drawdown.

### 5.6 ★ The discriminator that decides it

**Where can a buyer place the same order twice?** In 2021-22: everywhere (multi-sourced parts through a fragmented channel). In 2025-26: **not at the GPU — but yes at HBM, HDD/SSD, MLCC, power equipment, and critically at CAPACITY ITSELF**, where the same end-workload can be reserved simultaneously at a hyperscaler, a neocloud and a colo. **That last is the true structural home of double-ordering in this cycle** — and it is exactly the layer where Wood Mackenzie's ~28%-of-1,066 GW finding (§4.5) is measured.

---

## 6. PRE-REGISTRATION SCORECARD — graded against §0, written before any evidence

| # | Clean-book test | Verdict | Evidence |
|---|---|---|---|
| **C1** | Committed procurement ≤ credible capacity | **CLEAN (conditional)** | Dollar test passes (54% of CY2027 HBM TAM at the central case); bit test bounds memory share ≤75-80%; 2027 HBM bit supply reconciles to within 1pp from independent inputs. **FY2029 UNKNOWN — no CY2028/29 bit forecast exists.** |
| **C2** | Contract ≤ spot (no hoarding premium) | **UNDETERMINED** | The commission's premise is inverted for DRAM (spot normally leads *above* contract). Premium has compressed 5 months straight — consistent with BOTH an unwind and a pure consumer-vs-server composition artifact. **Cannot discriminate; the paired contract-LEVEL series is paywalled.** |
| **C3** | High cancellation penalties | **FAILS — and the split is UNDISCLOSED** | NVDA: "in certain instances… **cancelable, rescheduled, or adjustable** prior to placing firm orders," share not quantified. GEV: deposits are real ($11.15B in 6 months) but **GEV's own risk factors say slots "may not result in orders."** Conversion rate undisclosed by all three OEMs. |
| **C4** | Turbine backlog coverage flat/falling, slots pulled forward | **FAILS** | Book-to-bill 0.69× → **2.68×**; cumulative orders-over-deliveries **+35.4 GW** since 2024; **H1'26 deliveries FELL YoY (7.5 vs 8.2 GW)**; slot dates extending into 2031-32. |
| **C5** | 2021-22 analogue fails structurally | **FAILS AS A CLEAN SIGNAL — the analogue substantially HOLDS** | The three intuitive structural defences (few buyers, no distributors, contracted book) are each **directly refuted** by the reference cycle: auto OEMs were few and their simultaneous cancellation *caused* the shortage; Cisco 2001 had no distributor and blew up hardest; every 2021-22 take-or-pay was renegotiated. |
| **C6** | Jump explained by an accounting/scope change | **PARTIALLY — flag it** | NVDA **did** restructure the commitments disclosure between Q1 and Q2 FY27 (prose → a 5-line table; a new "Data center leases not commenced" line appears). **But the "supply and capacity" label is consistent across both**, so the $119B→$279B is like-for-like on the line that matters. Scope *within* that line cannot be ruled out. |
| **C7** | Orders and deployment growing together | **SPLIT BY SECTOR** | **Semis: CLEAN** — revenue +106% YoY, inventory/revenue flat at ~32.8%, GM +2.6pts, customer advances ×17.5, top-customer concentration 23%→16%. **Turbines: FAILS** — deliveries fell YoY while orders ran 2.68×. |

**Score: 1 clean · 1 undetermined · 1 partial · 4 fail — and the failures cluster in POWER EQUIPMENT, not semiconductors.**

---

## 7. VERDICT

### 7.1 The commission's convergence case does not survive as constructed — for a reason worth more than the answer

The commission rests on **"two independent arrivals of the same mechanism, from unrelated supply chains, on the same day."** After primary work:

| Arrival | Status |
|---|---|
| **NVDA memory commitments ($119B→$279B)** | **VERIFIED at the primary.** ⛔ *Corrected 2026-09-10:* the quote used to characterise it ("primarily related to the procurement of memory") **does exist — in the FURNISHED 8-K Ex-99.2, not in the FILED 10-Q, which says "memory and manufacturing facilities"** (§2.5). **The arrival is verified and stays verified.** What §2.5 establishes is narrower and still holds: **the memory SHARE is undisclosed in both, so the memory leg cannot be sized** — and the decomposition shows something more specific than the headline. |
| **Bernstein turbines (75% ordering above need)** | **SEARCH-NOT-FOUND** — neither the note nor a single republisher could be reached (§4.1). |

⇒ **One verified arrival and one unreached claim.** `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]` applies to both halves. **The convergence was the reason this ranked first, and the convergence is materially weaker than it appeared.**

**But the underlying question is answerable without either quote, and the backlog record answers it.**

### 7.2 The answer, split by sector — because the two sectors do not behave alike

**⛔ THE SINGLE MOST IMPORTANT STRUCTURAL FINDING OF THIS RUN: "the AI order book" is not one order book. Treating it as one is the analytical error the commission's framing invites.**

| | **Semiconductors / memory** | **Power equipment / turbines** |
|---|---|---|
| **Order-book quality** | Supply *commitments*, explicitly part-cancelable, share undisclosed | Headline GW is **54% slot reservations sitting OUTSIDE the audited RPO** |
| **Deliveries vs orders** | Revenue +106% YoY; inventory/revenue flat | **Deliveries FELL YoY**; book-to-bill 2.68× |
| **Internal over-commitment gauges** | **All moved CLEAN** (excess-obligation accrual −22%, provisions down, GM up, prepayments ×17.5) | Contract liabilities +67.5%, but **conversion rate undisclosed** |
| **Verdict** | **TIGHT-AND-CLEAN at the contracted core, with ONE hoarding-consistent datum: NVIDIA's own front-loading (near-term run-rate 2.11× the FY28 rate, +45% QoQ like-for-like)** | **QUEUE-POSITION MARKET — not proven double-ordering, but the company's own filings concede reservations may not convert** |

**Where the phantom, if any, actually lives:** not in the GPU (single-source — the 2021-22 mechanism cannot execute there), but in **multi-sourced inputs and, above all, in CAPACITY RESERVATION**, where the same end-workload can be reserved simultaneously at a hyperscaler, a neocloud and a colo. **That layer already has a published measurement pointing at ~3.6× duplication** (Wood Mackenzie: ~28% of 1,066 GW requested likely to be committed).

### 7.3 The discriminating instrument — named, as the commission required

**There IS one, and it is not on the commission's list. The commission's four named instruments were the four that ran 9–27 months LATE in the reference cycle.**

**Watch the price of the marginal UNCONTRACTED unit in the most liquid sub-market**, in this priority order:
1. **Spot / on-demand GPU rental prices** — the direct analogue of DRAM spot (uncontracted, liquid, marginal).
2. **HBM and DRAM/NAND contract-price momentum** — literally the same instrument that led in 2021.
3. **Secondary-market prices for prior-generation accelerators.**
4. *Only then:* lead times, guidance, billings, backlog, inventory.

**Expected lead, from the reference cycle: ~14 months ahead of the first billings decline, ~24 months ahead of the peak of the contracted book.**

**Three near-dated, falsifiable tests this report registers (all observable without new data access):**
- **T1 (memory, ~Nov 2026):** if the spot break was an unwind rather than a composition artifact, **4Q26/1Q27 server-DRAM contract prints come in below the 3Q26 +13–18%.** A re-acceleration falsifies the unwind read.
- **T2 (turbines, GEV Q3'26 10-Q, ~Oct 2026):** **does slot-reservation GW keep growing faster than firm backlog converts?** Q2 already shows gross new slot signings (18 GW) running ~2× conversions (10 GW). Continuation inflates the 116→125 GW headline faster than the audited RPO beneath it.
- **T3 (NVDA, Q3 FY27 10-Q, ~Nov 2026):** **does the near-term per-quarter commitment run-rate keep rising, and does the excess-inventory-obligation accrual stay down?** The 2.11× front-loading ratio is not yet evidence — its *direction over the next two filings* is what converts it into evidence or kills it.

### 7.4 What I am NOT saying

- **Not** that AI demand is unreal — explicitly out of scope, and nothing here tests it.
- **Not** that NVDA's $279B is undeliverable — the dollar test passes; the bit test bounds the memory share but does not refute the total.
- **Not** that a phantom is confirmed. **Consistency is not proof** — as `-045` §3 required. The turbine book is consistent with double-ordering AND with a rational response to a 4–5-year lead-time shortage, and **the number that would separate them (slot-to-order conversion) is not disclosed by anyone.**
- **Not** a threshold, trigger, or position view. Interpretation belongs to VULCAN, WATT, ZHAO, HENRY, VIOLET.

---

## 8. COUNTER-EVIDENCE SUMMARY (consolidated — the strongest case AGAINST a phantom)

1. **Every NVIDIA-internal over-commitment gauge moved clean this quarter** (§2.4). The excess-inventory-obligation accrual — the GAAP mechanism by which an over-committed book surfaces — **FELL 22% while commitments rose 2.3×.**
2. **Customer advances rose $160M → $2.8B (×17.5).** Customers are putting cash down.
3. **Customer concentration FELL** (top direct customer 23% → 16% YoY) — demand broadening, not narrowing.
4. **The memory mechanism is arithmetic, not psychology.** HBM at ~3× silicon area per GB, wafer input 18%→22%→30%, mechanically suppresses conventional bit supply. **The price level needs no hoarding story to explain it.**
5. **Locked volume ≠ double-ordered volume.** Micron locked *price and volume* for all CY2026 HBM; SK hynix has ~10 customers on ~5-year LTAs. **A hoarder pays spot for optionality; these buyers gave up optionality for tenor — the opposite behavioural signature.**
6. **Suppliers are adding capacity hard** (big-3 capex +~340% 2024→2027; Samsung Yongin pulled forward to 2029). Not cartel discipline.
7. **Turbine deposits are real and large** ($11.15B at GEV Power in six months) and **MHI's book is only ~2.2 years deep** — inconsistent with a market-wide speculative blow-off. The excess sits where the slot instrument is used most aggressively, not industry-wide.
8. **Pre-ordering at 4–5-year lead times into a documented physical shortage is rational, not speculative** (~100 GW 2025 orders vs 60–70 GW/yr capacity).
9. **Hyperscalers have first-party demand telemetry** and are funded from operating cash flow — the two preconditions that made the 2021-22 distributor tier fragile are both absent at the top tier.

**Honest self-assessment of my own search bias, per §0:** the pre-registration required me to report clean findings as prominently as phantom findings. **Four of seven clean-book tests failed — but the strongest single evidence set in this report (§2.4, nine gauges) is CLEAN, and the commission's own founding survey could not be found.** I judge the search did not run one-way. The place I am least confident is C2, where I could not obtain the series that would decide it.

---

## 9. SOURCE-QUALITY ASSESSMENT

**Strong [PRIMARY], verified at artifact by DEWEY:** the entire NVDA commitment time series across 5 filings; the cancelability language; all nine §2.4 gauges; GEV's RPO exclusion, both slot risk-factors, the 3-occurrences-all-in-cash-flow grep, contract liabilities $16,527M→$27,679M; the full ON Semi RPO XBRL series; GF's LTA drawdown.

**Weaker, and flagged inline:** HBM TAM path (could not re-verify — Micron IR 403/JS-gated); HBM $/GB by customer ($32/$36/$40, [UNVERIFIED], load-bearing for the bit test); GEV's "~20% cash down" (secondary, paywalled substack); Siemens Energy GW figures ([NEWS] — the Q3 FY26 release contains no GW figures at all); SIA billings and US Commerce RFI (403, snippet-sourced); "2027 sold out" (single-origin, widely relayed).

**Absent entirely:** the Bernstein survey; slot-to-order conversion rates; NVDA's cancelable/non-cancelable split; AI take-or-pay prepay coverage. **CXMT bits — RECLASSIFIED 2026-09-02 from "absent" to VERIFIED ABSENCE AT THE PRIMARY** (ZHAO reached the IPO prospectus I named as the fallback: CXMT disclosed ratios and growth rates only, never a level — §3.4). **CY2028-29 memory bit forecasts — partially available after all** (Omdia 40.16 EB → 97.42 EB, in the same prospectus), but a demand series, not the supply series the FY29 test needs.

**Overall confidence: MEDIUM-HIGH on the decomposition and the base rate (primary, reproducible); MEDIUM on the turbine read (primary filings, but the deciding number is undisclosed); LOW on the memory contract/spot discrimination (paywalled).**

---

## 10. PROCESS REPORT

**Engine sizing:** primary-pull-first per §Engine sizing. DEWEY main session owned the entire NVDA + GEV + ON Semi primary spine (EDGAR `edgar_doc.py` × 7 filings, SEC XBRL companyconcept × 1); three targeted sub-agents (NOT the 5-angle harness) covered the breadth residual: memory market, turbine backlogs, historical base rate. **The verdict lives in the primary pull, as it has on every prior run.**

**Three sub-agent claims caught and corrected at the primary — all three would have shipped as [PRIMARY]:**
1. ⛔ **REVERSED 2026-09-10 — THIS ITEM WAS THE ERROR, NOT THE CATCH.** As shipped: *"primarily related to the procurement of memory" attributed to the 8-K CFO commentary — the 8-K contains neither the word "memory" nor "279."* **The sub-agent was RIGHT and I was wrong.** The phrase is verbatim in 8-K **Ex-99.2**; my helper had returned only **Ex-99.1** and I recorded that clean result as *"the 8-K."* **A correction pass is unreviewed work, and this one inverted a true claim into a false one and shipped it with a [VERIFIED] tag.** `[[finding_a_correction_pass_is_unreviewed_work]]` · `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` — resolving the flag backwards did not merely miss the defect, it **manufactured** one and erased the sub-agent's correct read. See the ERRATUM banner. *(Items 2 and 3 below are unaffected and stand.)*
2. **My own §2.1 first draft** reported "near-term commitments FLAT (−$3B)" — a **perimeter error**: the bucket covers 3 quarters in the Q1 filing and 2 in the Q2 filing. Normalised, near-term ordering **ACCELERATED 45%**. The correction reversed the sign of the finding. `[[finding_cross_entity_comparison_needs_same_perimeter]]`
3. **HBM TAM tagged [PRIMARY, Micron call]** — Micron IR returns 403/JS-shell; downgraded to [INSTITUTIONAL, not re-verified] and logged to BACKLOG.

**Data gaps (looked for, could not find):** Bernstein survey (11 formulations, no note AND no republisher); slot-to-order conversion rate (all 3 OEMs); NVDA's cancelable/non-cancelable split; CXMT absolute bits; paired DRAM contract-LEVEL series; CY2028-29 bit forecasts; AI take-or-pay prepay coverage.

**Source frustrations:** Micron IR `static-files` 403/JS-gated → **BACKLOG'd, with the EDGAR-8-K-exhibit route named as the cheap fix to try first.** SIA + commerce.gov 403. Infineon PDFs 403/unparseable. Quartr MCP requires a Pro subscription this account lacks — **this blocked earnings-call transcripts on both the GEV and the 2021-22 legs, and transcripts are where management concedes conversion rates.** Bernstein/sell-side unreachable by construction.

**If I had more time/tools:** (a) the GEV Q2'26 call Q&A — analysts pressing on slot conversion is the highest-value unreached artifact in this commission; (b) the CXMT Shanghai IPO prospectus for the bits figure; (c) a paired contract/spot DRAM level series to settle C2; (d) spot GPU rental price history, to build the §7.3 leading instrument as an actual series rather than a recommendation.

**Suggestions (routed, not built):** ① **WALTER should tag sell-side-sourced signal claims with whether the desk reached the note or only a republisher** — a commission premised on a survey whose founding evidence is unreachable is an expensive surprise discovered only after commissioning. ② The §7.3 instrument (spot GPU rental prices) has **no owner in the fleet** and is the single highest-value monitoring gap this run surfaced — a candidate for VULCAN or WATT, PROME's call. ③ Test the EDGAR-8-K-exhibit route for memory-maker prepared remarks (BACKLOG'd).

**Completeness-critic pass (which commission sub-answers did I NOT answer?):** Instrument 1 (contract-vs-spot) **PARTIAL — direction only, level paywalled**. Instrument 2 (capacity reconciliation) **ANSWERED, with the memory-share assumption named and bounded**. Instrument 3 (turbine backlogs) **ANSWERED**. Instrument 4 (cancellation economics) **PARTIAL — qualitative from filings; the deciding quantitative number is undisclosed by every issuer**. Instrument 5 (2021-22 base rate) **ANSWERED, and it inverted the instrument list**. The named analogue was used as the backbone, not a footnote, as required. Pre-registration written before evidence. Both scope fences observed (demand-reality not re-litigated; the NVDA aggregate explicitly not treated as the finding).

**Live-desk dependency, per the commission's instruction:** at delivery, **ZHAO's CXMT bits ask was UNANSWERED (n=3) and no proxy was substituted** — I reported it as missing and named the IPO prospectus as the unchecked fallback rather than upgrading to VERIFIED. ✅ **ZHAO reached that fallback the same day and CLOSED the leg** (§3.4) — the answer is that CXMT deliberately discloses no capacity level at all. **Naming the specific unchecked fallback, rather than logging a generic gap, is what made it closable within hours.** **WATT's ERCOT falsifier had not landed** as of this run (no delivery in WATT's outbox), so it was not used.

---

## 11. REFERENCES

### NVIDIA SEC filings (CIK 0001045810) — all accessed 2026-09-02 via `AGENTS/DEWEY/scripts/edgar_doc.py`

| Filing | Period | Filed | Accession | URL |
|---|---|---|---|---|
| 10-Q (Q2 FY2027) | 2026-07-26 | 2026-08-26 | 0001045810-26-000075 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm |
| 10-Q (Q1 FY2027) | 2026-04-26 | 2026-05-20 | 0001045810-26-000052 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm |
| 10-K (FY2026) | 2026-01-25 | 2026-02-25 | 0001045810-26-000021 | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm |
| 10-Q (Q3 FY2026) | 2025-10-26 | 2025-11-19 | 0001045810-25-000230 | https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm |
| 10-Q (Q2 FY2026) | 2025-07-27 | 2025-08-27 | 0001045810-25-000209 | https://www.sec.gov/Archives/edgar/data/1045810/000104581025000209/nvda-20250727.htm |

**Reproduction recipe (no ephemeral paths cited):** `python3 AGENTS/DEWEY/scripts/edgar_doc.py doc --cik 0001045810 --accession <accession>` then grep `"Supply and capacity"` / `"Note 1[0-2] - Commitments"`. All commitment figures above are read from the Commitments and Contingencies note of the named filing; the $95.2B figure is from the FY26 10-K's Critical Audit Matter.

### GE Vernova (CIK 0001996810) — verified at artifact by DEWEY 2026-09-02
| Filing | Period | Accession | URL |
|---|---|---|---|
| 10-Q Q2 2026 | 2026-06-30 | 0001996810-26-000148 | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm |
| 10-K FY2025 | 2025-12-31 | 0001996810-26-000015 | https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm |
| 8-K Q2 2026 press release | — | 0001996810-26-000147 | https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm |

### 2021-22 base-rate primaries — ON Semi RPO series verified at artifact by DEWEY 2026-09-02
- **ON Semiconductor LTSA RPO, full quarterly series** — https://data.sec.gov/api/xbrl/companyconcept/CIK0001097864/us-gaap/RevenueRemainingPerformanceObligation.json
  *(Reproduction: `curl -H "User-Agent: <name> <email>" <url>`, filter `form` starting `10-`, key on `end`.)*
- ON Semiconductor 10-K FY2024 (LTSA modification/cancellation language) — https://www.sec.gov/Archives/edgar/data/1097864/000162828025004557/on-20241231.htm
- GlobalFoundries 20-F FY2022 ($22bn / $5bn) — https://www.sec.gov/Archives/edgar/data/1709048/000170904823000013/gfs-20221231.htm
- GlobalFoundries 20-F FY2023 / FY2024 / FY2025 — .../gfs-20231231.htm · .../gfs-20241231.htm · .../gfs-20251231.htm
- Revenue / inventory series via SEC XBRL companyconcept — Micron 0000723125 · TI 0000097476 · ON 0001097864 · Arrow 0000007536 · Avnet 0000008858

### Memory market [INSTITUTIONAL]
- TrendForce, server DRAM 3Q26 +13–18%, LTAs (2026-07-09) — https://www.trendforce.com/presscenter/news/20260709-13140.html
- TrendForce, HBM bit & wafer shares (2026-06-02) — https://www.trendforce.com/presscenter/news/20260602-13074.html
- TrendForce, DDR5 retail pullback vs stable contract (2026-03-31) — https://www.trendforce.com/news/2026/03/31/news-ddr5-retail-prices-pullback-amid-market-correction-but-industry-players-cite-stable-contract-trends/
- TrendForce spot updates (2026-08-12 · 2026-07-29 · 2026-05-27) — trendforce.com/news/2026/…
- TrendForce, PC DRAM spot bearish from early Jul 2021 (2021-08-10) — https://www.trendforce.com/presscenter/news/20210810-10890.html
- Counterpoint, Q1 2026 DRAM revenue $97B (2026-05-26) — https://counterpointresearch.com/en/insights/global-dram-revenue-surges-to-near-dollar-100-billion-mark-in-q1-2026
- SemiAnalysis, CXMT (2026-06-23) — https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram
- SemiAnalysis via Yahoo, memory ~30% of hyperscaler capex + NVDA "VVP" pricing (2026-04-03) — https://finance.yahoo.com/sectors/technology/articles/memory-consume-30-hyperscaler-ai-135827019.html

### Turbines / power [INSTITUTIONAL + NEWS]
- Wood Mackenzie via Bloomberg, ~28% of 1,066 GW (2026-08-12) — https://www.bloomberg.com/news/articles/2026-08-12/most-electricity-sought-for-ai-data-centers-in-us-will-never-materialize
- Wood Mackenzie, gas turbine prices +195% — https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/
- Siemens Energy Q3 FY2026 earnings release — https://www.siemens-energy.com/global/en/home/press-releases/earnings-release-q3-fy-2026.html
- Utility Dive: GEV 116 GW (2026-07-23) · Siemens ~70 GW (2026-08-10) · MHI 35 GW (2026-08-13) — utilitydive.com/news/…
- electroneconomics, "Slotting In the Future" (53/63 GW split; ~20% cash down) — **[UNVERIFIED, paywalled]** — https://electroneconomics.substack.com/p/slotting-in-the-future-gas-turbine

### Base-rate episodes [NEWS / ACADEMIC]
- Electronics Weekly, lead times Jun-2022 27.0w "peak cycle" — https://www.electronicsweekly.com/news/business/lead-times-fall-by-a-day-2022-07/
- EE Times, 2001 semi sales −32% — https://www.eetimes.com/semiconductor-sales-suffered-worst-decline-ever-in-2001/
- AAA *Issues in Accounting Education*, Cisco $2.249bn charge — https://publications.aaahq.org/iae/article/30/4/329/8090/
- Taipei Times, Yageo MLCC ASP −15% (2018-12-17) — https://www.taipeitimes.com/News/biz/archives/2018/12/17/2003706238
- SIA billings (2026 fetch returned 403; snippet-sourced) — https://www.semiconductors.org/global-semiconductor-sales-increase-0-1-year-to-year-in-august/

### Fleet-internal (state verification, not evidence)
- `AGENTS/ZHAO/STATUS.md` lines 127, 221 — CXMT ask n=3, UNCHECKED, no date promised (verified 2026-09-02, state AT DELIVERY)
- **CXMT STAR Market IPO prospectus, SSE `002170_20260517_MGLN.pdf` (2026-05-17)** — reached by ZHAO 2026-09-02, 411,324 chars extracted; the source of §3.4's VERIFIED ABSENCE. Relayed via `AGENTS/DEWEY/inbox/processed/2026-09-02_from-ZHAO_your-named-fallback-is-reached...md` (commit `66ac967a4`). **[PRIMARY, not independently re-pulled by DEWEY — ZHAO's extraction is the reader of record.]**
