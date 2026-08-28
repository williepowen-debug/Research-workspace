# FHA PARTIAL-CLAIMS LEG — THE DEFERRAL WEDGE WENT INTO REVERSE

**Date:** 2026-08-27 | **Mode:** Thesis | **Confidence:** High (the flow decomposition, the mechanism, the foreclosure counter-test, and the FY2024 partial-claim counts — all HUD primary, re-verified, and reproducible) / **Medium** (the SDQ-relevant share of partial claims, which is bounded not measured) / **NOT-AVAILABLE** (FY2025–26 partial-claim counts — HUD withdrew the disclosure)
**Commission:** PROME re-commission of the CARL-DR-1 FHA/VA leg, Will-approved in-session 2026-08-19 · **Consumers:** CARL (action) · WALTER (ledger) · PROME (info)

> ⚠️ **Filename note:** the commission specified `output/2026-08-19_carl-dr1-fha-partial-claims-leg.md`. Delivered 8/27, so the file carries the delivery date per the `INDEX.tsv` convention. Same slug otherwise.

---

## Key Finding

**The FHA recognition artifact is real, it is roughly an order of magnitude larger than the Fannie leg — and it is currently running BACKWARDS.**

FHA's reported serious-delinquency rate rose **+226bps YoY, from 4.27% to 6.53%** (May 2025 → May 2026). **79% of that deterioration is a slower drain, not more borrowers falling behind.** Over the same fiscal half-year, new 90+ delinquencies rose only **+8.3%** while **outflow fell 33.1%** — from 349,308 exits to 233,613. The outflow-to-inflow ratio, stable at **0.95** across all four quarters of FY2025 (range 0.77–1.08), collapsed to **0.51** in FY26Q1 and **0.63** in FY26Q2.

**The cause is documented, dated, and mechanical.** FHA's COVID-era loss-mitigation options (COVID-19 ALM, COVID-19 Recovery, FHA-HAMP) **expired September 30, 2025**. From October 1, the new permanent waterfall requires a **three-month Trial Payment Plan** before any permanent home-retention option, and the loss-mitigation documents take effect **"no later than the first Day of the second month following the final TPP month."** That is a **~5-month minimum pipeline** from intervention to cure, against a COVID-era path that could execute a partial claim directly. HUD's own footnote confirms the accounting consequence: **"Included in the delinquency counts are loans under active consideration for loss mitigation foreclosure avoidance."** Loans in the pipeline stay delinquent.

**So the deferral machine did not get better at hiding delinquency — it got throttled, and the reported number jumped because the hiding stopped.** The cumulative outflow shortfall versus the FY2025 baseline is **158,587 loans = 191bps** of the 8.32M active portfolio, sitting in the reported SDQ count that the prior regime's drain rate would already have removed.

**For CARL's kill condition this is decisive in the unwelcome direction, and it is MEASURED, not inferred.** HUD publishes partial-claim completion counts by type for FY2021–FY2024. In **FY2024 alone, 406,623 partial-claim-involving home-retention actions completed** (323,920 stand-alone partial claims + 82,703 Recovery Modifications that include one) on a 7.81M-loan book. On the *same construction* as Fannie — workout removals ÷ book, per half-year — that is **260bps, versus Fannie's 22.5bps. The FHA leg is 11.6× the Fannie leg.** For FHA to stay under CARL's ~50bps threshold, **fewer than 19.2% of partial claims would have to be curing loans that were seriously delinquent.** **Under three of the four plausible aggregation rules the class-wide condition breaches; only "best leg" preserves the kill — and "best leg" selects Fannie precisely because Fannie publishes the flow decomposition that made it measurable.** The selection effect I flagged in DR-1 is now quantified.

⚠️ **And the disclosure that makes this measurable has been withdrawn.** The count-by-type exhibit exists in the **FY2024** Annual Report to Congress and **was dropped from the FY2025 edition**, which reports only home-retention *rates* and redefault rates — no raw counts. So the FY2024 figure above is, as of now, **the most recent measurable vintage of the largest recognition-artifact channel in US consumer credit**, and the series went dark in the year the mechanism changed.

---

## 1. The measurement

FHA publishes a monthly stock (Table 1) and a quarterly inflow (Table 2), which supports the same beginning/additions/removals decomposition I ran on Fannie. Stock at fiscal-quarter ends, on the **SDQ perimeter** (90+ plus in-foreclosure plus in-bankruptcy — so transitions *into* foreclosure net out rather than reading as exits):

| FHA fiscal qtr | New 90+ (inflow) | SDQ start | SDQ end | Δ stock | **Outflow** | **out/in** |
|---|---:|---:|---:|---:|---:|---:|
| FY25 Q1 (Oct–Dec 24) | 202,210 | 324,070 | 370,511 | +46,442 | 155,768 | 0.77 |
| FY25 Q2 (Jan–Mar 25) | 179,273 | 370,511 | 356,245 | −14,267 | 193,540 | 1.08 |
| FY25 Q3 (Apr–Jun 25) | 158,059 | 356,245 | 346,363 | −9,882 | 167,941 | 1.06 |
| FY25 Q4 (Jul–Sep 25) | 196,833 | 346,363 | 369,197 | +22,834 | 173,999 | 0.88 |
| **FY26 Q1 (Oct–Dec 25)** | 219,641 | 369,197 | 477,476 | **+108,279** | **111,362** | **0.51** |
| **FY26 Q2 (Jan–Mar 26)** | 193,591 | 477,476 | 548,816 | **+71,340** | **122,251** | **0.63** |

**FY2025 baseline out/in = 0.949** across four quarters (0.77–1.08). FY26Q1's 0.51 sits far outside that range. Applying the baseline to FY26 H1 inflow gives an expected outflow of 392,200 against an actual 233,613 — a **shortfall of 158,587 loans = 191bps** of the 8,323,271-loan active portfolio.

**The like-for-like YoY attribution (same fiscal half, one year apart):**

| | FY25 H1 | FY26 H1 | change |
|---|---:|---:|---:|
| Inflow (new 90+) | 381,483 | 413,232 | **+8.3%** |
| Outflow (all exits) | 349,308 | 233,613 | **−33.1%** |
| Stock change | +23,700 | +173,426 | |

The stock grew **147,444 more** in FY26 H1 than FY25 H1. **21.5% of that is higher inflow; 78.5% is lower outflow.** In portfolio bps: inflow term **38bps**, outflow term **142bps**.

*Robustness: run on the narrower 90-day-only perimeter the answer is 193bps and a 78.8/21.2 split — the finding does not depend on the perimeter choice. Both LPT reports overlap at May 2025 (90-day 3.39%, IIF 8,020,755) and agree exactly, so the two vintages splice cleanly.*

⚠️ **`[[finding_rising_stock_flat_inflow_means_slower_outflow]]`** — the same signature I found on bank cards in the C3 run, here far more extreme. **A reader taking FHA's +226bps SDQ move as a pure credit signal is reading a pipeline change as borrower behaviour.**

⚠️ **THIS SUPERSEDES MY OWN PRIOR FRAMING, and I would rather say so than let it stand.** `output/2026-07-24_fha-va-loss-waterfall.md` reported *"FHA DQ is rising sharply… SDQ +212bps YoY"* and framed the rise through a student-loan-defaulter channel. **The level was right; the cause was not established, and this report shows ~79% of the move is a drain artifact.** The student-loan mechanism may still contribute to the *inflow* term (+8.3%), which is the smaller half. **Anyone carrying the 7/24 framing should re-rate it.** *(A different figure in that report — the MBA NDS 11.52%/11.88% series — is NOT superseded here: it is a different series on a different perimeter, and my own 7/25 synthesis already flagged it as 403'd and unverified at primary. Do not reconcile the two.)*

## 2. Why — the mechanism, at primary

- **COVID-19 ALM, COVID-19 Recovery Options and FHA-HAMP expired 2025-09-30**; servicers had to migrate to the new waterfall from **2025-10-01** (ML 2025-12 moved this forward from ML 2025-06's original 2026-02-02 date), with full implementation required no later than **2025-12-30**.
- **A three-month Trial Payment Plan is now mandatory** before any permanent home-retention option: *"A Trial Payment Plan (TPP) is a payment plan for a period of three months, or six months for Non-Borrowers Who Acquired Title through an Exempted Transfer"*, and *"The Mortgagee must ensure the Borrower successfully completes a TPP"* [PRIMARY: HUD ML 2025-12].
- **Completion does not immediately cure**: *"Upon the Borrower's successful completion of a TPP, the Mortgagee must prepare the Loss Mitigation documents to be effective no later than the first Day of the second month following the final TPP month"* [PRIMARY: same]. **Three months of trial plus up to two more months to effectiveness ≈ a five-month pipeline.**
- **Loans in that pipeline are counted delinquent**: *"Included in the delinquency counts are loans under active consideration for loss mitigation foreclosure avoidance"* [PRIMARY: FHA LPT Table 1, footnote a].
- **Repeat access was tightened**: home-retention options limited to **one in 24 months** (previously one in 18; the COVID waterfall had no such limit) [PRIMARY: ML 2025-12; NCLC].

**The observed shape matches the mechanism quarter by quarter.** FY26Q1 (Oct–Dec 25) is the quarter in which trials start and none complete → outflow 0.51. FY26Q2 (Jan–Mar 26) is when the first cohort completes and documents take effect → partial recovery to 0.63, still well below the 0.95 baseline. **This is a predicted signature, not a fitted one.**

## 3. The counter-hypothesis, tested and refuted

An obvious alternative: the drain slowed because FHA **stopped foreclosing** (a moratorium or servicing slowdown), which would produce the same stock build with a completely different meaning. **It is refuted.**

| | FY25 H1 | FY26 H1 | change |
|---|---:|---:|---:|
| Foreclosure starts | 39,762 | 53,238 | **+33.9%** |
| Foreclosure claims paid | 6,805 | 8,208 | **+20.6%** |
| In-foreclosure stock (May) | 31,078 | 45,847 | **+47.5%** |

**Foreclosure accelerated.** And it is far too small to matter to the drain either way: claims are **3.5% of total FY26 H1 outflow**, and the extra claims YoY explain **1.2%** of the 117,977-loan outflow shortfall. The collapse is in the **cure** channel, not the terminal channel.

## 4. The Fannie-comparable wedge — MEASURED

Fannie's 22.5bps is arithmetically **workout removals ÷ book**: 38,150 ÷ ~16.95M = 22.5bps (this reconciles exactly, which confirms I have the construction right). The FHA-comparable quantity is **partial-claim removals ÷ book, per half-year** — and HUD publishes the numerator.

**Exhibit II-3, "Home Retention Options by Type and Count FY 2021 through FY 2024"** [PRIMARY: FHA Annual Report to Congress on the MMI Fund, FY2024, p.34 — **I re-pulled and verified this table directly**, it is not taken on report]:

| Home retention option | FY2021 | FY2022 | FY2023 | **FY2024** | Total | Share |
|---|---:|---:|---:|---:|---:|---:|
| COVID-19 Stand-alone Partial Claim | 317,440 | 249,224 | 237,088 | **323,920** | 1,127,672 | 64% |
| COVID-19 Recovery Modification (**including a Partial Claim**) | 94 | 152,046 | 66,278 | **82,703** | 301,121 | 17% |
| Stand-alone Modification (no Partial Claim) | 99,060 | 49,897 | 4,949 | 12,957 | 166,863 | 9% |
| HAMP | 61,542 | 46,305 | 22,818 | 3,141 | 133,806 | 8% |
| Advance Loan Modification | 1,310 | 33,769 | 4,660 | 2,702 | 42,441 | 2% |

**FY2024 partial-claim-involving actions = 323,920 + 82,703 = 406,623**, on the Sep-2024 book of 7,808,911 loans:

| | value |
|---|---:|
| Annual rate | **521 bps/yr** |
| **Half-year equivalent (the Fannie basis)** | 203,312 loans = **260 bps** |
| Stand-alone partial claims only, half-year | 207 bps |
| **Fannie SF, same construction** | **22.5 bps** |
| **Ratio** | **FHA is 11.6× Fannie** |
| Share of partial claims that must be NON-seriously-delinquent to keep FHA under 50bps | **80.8%** |

**The one residual caveat, stated precisely:** Fannie's 38,150 were workout removals from the *seriously delinquent* flow specifically. FHA's 406,623 counts partial claims at **any** delinquency stage, so the SDQ-specific subset is **≤** the raw count. The honest form of the finding is therefore: *the FHA leg breaches 50bps unless fewer than 19.2% of partial claims cure a seriously-delinquent loan.* Against an FHA 90+ inflow running ~380–410K per half-year and partial claims at ~203K per half-year, a sub-20% SDQ-relevant share is not credible — but it is **not directly measured**, and I am not claiming it is.

⚠️ **Two integrity notes on this exhibit, both of which I would want flagged if I were the reader:**
1. **HUD's own narrative contradicts its own table on the same page.** The text says *"roughly 810,000 Stand-alone Partial Claims since the beginning of the pandemic in March of 2020"* while Exhibit II-3 totals **1,127,672** stand-alone partial claims for FY2021–24 alone — a *shorter* window. The two cannot both be counting the same thing; the most likely reconciliation is **actions vs unique borrowers** (repeat partial claims to the same borrower were permitted under the COVID waterfall). **I use the table, because the wedge needs ACTIONS.** Anyone citing "810,000" for a flow calculation is using the wrong quantity.
2. **The FY2025 edition of the same report DROPPED this table**, publishing only home-retention *rates* by origination cohort and redefault rates. **The disclosure that makes the largest consumer-credit recognition artifact measurable was withdrawn in the year the mechanism changed.** FY2026 counts do not exist yet (that edition publishes ~Nov 2026). `[[finding_retired_threshold_has_no_publisher]]`

## 5. ⚠️ The aggregation question — DR-1's spec defect, made concrete

CARL's kill is **class-wide**; DR-1 never says how legs aggregate. **The same two measurements produce opposite verdicts under different rules:**

Using the measured legs — Fannie **22.5bps** (16.95M loans) and FHA **260bps** (8.32M loans):

| Aggregation rule | Class-wide wedge | Verdict vs 50bps |
|---|---:|---|
| (a) book-size weighted | **100.7 bps** | **BREACHES — no kill** |
| (b) unweighted mean of legs | **141.2 bps** | **BREACHES — no kill** |
| (c) worst leg | **260.0 bps** | **BREACHES — no kill** |
| (d) best / most-transparent leg | 22.5 bps | supports the kill |

*(Even on the deliberately conservative reading where only ~20% of FHA partial claims cure a seriously-delinquent loan — the threshold share — rule (a) still lands at ~50bps, i.e. exactly at the kill line rather than comfortably inside it.)*

**Only (d) preserves the kill — and (d) selects Fannie precisely because Fannie is the book that publishes a flow decomposition.** That is the selection effect I flagged in DR-1 ("the wedge is measurable at Fannie BECAUSE it publishes a flow decomposition, so a small wedge in the most transparent book is weak evidence about the least transparent ones"), now with a number attached. **I am not picking a rule. CARL and Will should rule on it, and the ruling should be made before the next leg is measured rather than after** — an aggregation rule chosen once the numbers are visible is chosen to fit them. `[[finding_unnamed_instrument_makes_a_threshold_a_family]]`

## 6. The removal-by-sale channel — ANSWERED, and the answer is a clean negative

In DR-1 I flagged a mechanism CARL's scope list omitted: **nonperforming/reperforming loan SALES**, which remove delinquent loans from the reported book entirely rather than deferring them (14,885 loans at Fannie in H1-2026). **The FHA analog exists, is active, and does NOT sit in the same position of the waterfall — so it is not a competing recognition artifact.**

- HUD's Distressed Asset Stabilization Program (DASP) is dormant under that name; the **Federal Register final rule 89 FR 99705 (Docket FR-6051-F-03), effective 2025-01-10**, converted the pilot into a permanent **Single Family Sale Program** [PRIMARY].
- It is running with real volume as the **HUD-Held Vacant Loan Sale (HVLS)**: **HVLS 2026-1, sale date 2025-12-09 — 1,061 loans, $146.9M UPB, $321.3M updated loan balance, winning bids $192.8M (65% of ULB)** [PRIMARY: HUD sale-results summary]. Prior sales HVLS 2025-3 (~1,874–1,945 loans) and 2025-2 (~1,600 loans).
- ⚠️ **The decisive scope point:** these sales cover notes **already assigned to HUD after an insurance claim has been paid.** Those loans left *Active Insurance in Force* at claim time. **So HVLS does not remove loans from the denominator or the delinquency numerator of the reported FHA rate** — unlike Fannie's NPL/RPL sales, which remove loans from a *reported performing-book* delinquency measure.

**Conclusion for CARL's scope list: at FHA the removal-by-sale artifact does not exist in the form it takes at Fannie.** FHA's recognition artifact is concentrated almost entirely in the **deferral** channel (partial claims), which is what makes it so large. That is a structural difference between the two books and it cuts against treating the legs as interchangeable.

**VA — the purchase channel CLOSED in 2025.** VA stopped accepting new **VASP** (VA Servicing Purchase) submissions and trial payment plans effective **2025-04-30**, with already-accepted trials running through **2025-08-31** (VA Circular 26-25-2, dated 2025-04-23) [INSTITUTIONAL — consistent across NCLC, Consumer Finance Monitor and Alston; **the circular PDF was not fetched directly**, so treat the dates as corroborated-but-not-primary]. Direction matters: VA's removal channel shutting in mid-2025 pushes reported VA delinquency **up** for the same reason FHA's is up — a closed cure/removal channel, not worse borrowers. My 7/24 report established VA is the milder leg on level (PFSI VA 60+ 1.7% vs FHA 8.0%), so FHA carries the class weight; **VA volumes remain unmeasured.**

---

## Counter-Evidence

1. **The strongest argument against reading this as "masking": it is the opposite of masking right now.** Reported FHA SDQ currently **overstates** deterioration relative to the prior regime's measurement basis. Anyone using this report to argue "FHA is hiding distress" has it backwards for the current period. The correct statement is that FHA *has the capacity* to hide distress on a ~190bps scale, and that capacity was recently interrupted.
2. **Credit genuinely is deteriorating too.** Inflow rose 8.3% YoY, foreclosure starts +33.9%, in-foreclosure stock +47.5%. The drain explains 79% of the *stock* move, not 100%, and the 21% inflow term is real.
3. **The 24-month repeat limit shrinks the machine's future capacity.** Borrowers who have used a home-retention option cannot be re-deferred for two years. If the wedge is a stock of deferrals, that stock now has a *harder* ceiling than under the COVID waterfall — which argues the wedge narrows from here regardless of the transition.
4. **My 191bps is a disruption measure, not a steady-state wedge.** It says how much the drain under-performed its own baseline, which is not identical to "how much delinquency is hidden." The §4 bound is the closer comparison, and it is a bound.
5. **The FY2025 baseline has real dispersion** (0.77–1.08 across four quarters). A 0.51 reading is outside it, but a four-quarter baseline is thin, and FY25Q1's 0.77 shows the ratio can run low without a policy change.
6. **The inflow series may not be perfectly comparable across the October 2025 change.** ML 2025-12 altered claim-type definitions and reporting requirements. I used only the raw "New 90+ Delinquencies" count, the least definition-sensitive column, but a reporting change affecting *when* a loan is counted 90+ would contaminate both sides of the decomposition. Not tested — flagged.
7. **Urban Institute's standing caution applies** (from my 7/24 report): none of five leading hypotheses fully explains the FHA DQ rise. This report adds a large mechanical term; it does not claim to close the question.

**What would disprove the central finding:** published FHA loss-mitigation completion counts showing partial claims *did not* fall in FY26 Q1–Q2. That single series would settle it, and it is the one thing I could not reach.

---

## Source Quality Assessment

**High** on the load-bearing decomposition: every figure is from HUD's own monthly credit report or the operative Mortgagee Letter, and the arithmetic is reproducible from two published tables. The May-2026 and June-2025 report vintages **overlap and agree exactly** at May 2025, so the splice is verified rather than assumed. The mechanism is quoted verbatim from ML 2025-12. The foreclosure counter-test is from the same report's Table 4.

**Gaps, stated plainly:**
- **FY2025 and FY2026 partial-claim counts — GENUINELY UNAVAILABLE, not merely unfetched.** The FY2025 Annual Report dropped the count-by-type exhibit; the FY2026 edition publishes ~Nov 2026. So the current-period flow cannot be measured from published data at all, which is precisely why §§1–3's drain decomposition carries this report.
- **The SDQ-relevant share of partial claims** — bounded (must be <19.2% for the leg to clear 50bps), not measured.
- **Partial-claim notes-receivable STOCK in $** — does not appear to exist as a standalone published line. HUD's FY2025 financial-statement audit (HUD OIG) reports a **material weakness in loans-receivable accounting that combines HECM Secretary-held notes and Single Family partial claims** and does not split them.
- ⚠️ **A trade-press figure of "343,801 partial claims valued at more than $7.7 million" (attributed to HUD OIG 2026-KC-0005, 2026-06-25) was DELIBERATELY NOT USED.** The report title/number/date check out on oversight.gov but the PDF was unreachable, and the dollar figure is internally implausible by ~1000× (343,801 × ~$22k ≈ $7.6 **billion**). Flagged rather than passed through. Do not cite it without the primary document.
- **VA / VASP volumes** — not measured; the wind-down dates are corroborated but not primary-fetched.
- **Whether a loan is formally reported delinquent throughout a TPP** — I did not find explicit reporting-code language. I relied instead on two documented facts (documents not effective until up to two months after the final TPP month; HUD counts active-loss-mit loans as delinquent), which establish the *timing* without needing the reporting code. Stated as such rather than asserted.

**Explicit negatives:** HUD's LPT series contains **no** loss-mitigation-by-type table (checked all six tables plus the figure). Older LPT reports are **not** at the current URL pattern — the naming changed from `FHALPT-Month YYYY.pdf` to `FHALPT_MonYYYY.pdf`, and pre-2026 issues were reachable only via the Wayback Machine.

---

## References

- **FHA Single-Family Loan Performance Trends, May 2026 Credit Risk Report** (HUD/FHA, Office of Risk Management; source line dated June 2026) — Tables 1–4 — https://www.hud.gov/sites/default/files/Housing/documents/FHALPT_May2026.pdf
- **FHA Single-Family Loan Performance Trends, June 2025** (source line July 2025) — Table 1, for the FY2024–25 stock history — via Wayback: `web.archive.org/web/20250929172530if_/https://www.hud.gov/sites/dfiles/Housing/documents/FHALPT-June2025.pdf`
- **HUD Mortgagee Letter 2025-12**, *Updates to Servicing, Loss Mitigation, and Claims* — TPP definition and standard, effectiveness timing, 24-month limit — https://www.hud.gov/sites/dfiles/OCHCO/documents/2025-12hsgml.pdf
- HUD Mortgagee Letter 2025-06 (superseded effective date) — https://www.hud.gov/sites/dfiles/OCHCO/documents/2025-06hsgml.pdf
- NCLC Digital Library, *Seven Key Changes to the FHA Waterfall* [INSTITUTIONAL — used for corroboration of the TPP and 24-month changes, never as a figure] — https://library.nclc.org/article/seven-key-changes-fha-waterfall
- **FHA Annual Report to Congress on the Financial Status of the MMI Fund, FY2024** — **Exhibit II-3, p.34**, the partial-claim counts (re-pulled and verified directly, not taken on report) — https://www.hud.gov/sites/dfiles/Housing/documents/2024FHAAnnualReportMMIFund.pdf
- FHA Annual Report to Congress on the MMI Fund, **FY2025** — checked and confirmed to **omit** the count-by-type exhibit — https://www.hud.gov/sites/dfiles/Housing/documents/2025FHAAnnualReportMMIFund.pdf
- Federal Register final rule **89 FR 99705**, Docket FR-6051-F-03, *FHA: Single Family Sale Program*, effective 2025-01-10
- HUD **HVLS 2026-1 Sale Results Summary** (sale date 2025-12-09) [PRIMARY]
- HUD OIG, *Audit of FHA's FY2025 Financial Statements* — loans-receivable material weakness (HECM + partial claims combined, not split)
- VA Circular **26-25-2** (2025-04-23), VASP wind-down [INSTITUTIONAL — corroborated across NCLC / Consumer Finance Monitor / Alston; circular not fetched directly]
- Prior DEWEY work relied on rather than re-derived: `output/2026-07-24_fha-va-loss-waterfall.md` (MMI capital ratio, FHA/VA severity split, nonbank servicer map); `output/2026-08-13_carl-dr1-recognition-artifact-census.md` (the Fannie leg and its construction)

**Reproduction recipe:** fetch the LPT PDF with a browser UA; extract Table 1 / Table 2 / Table 4 with `pdfminer.six` using `LAParams(line_margin=0.3, char_margin=2.0, boxes_flow=0.5)` and page indices 2 / 3 / 6 — the default layout parameters flatten the columns into an unusable single stream. Stock = rate × Insurance-in-Force; outflow = inflow − Δstock; FHA fiscal quarters are Oct–Sep.

---

## Process Report

**Searches run:** primary-pull-led per Engine sizing — HUD is a publisher, not a search problem, so the spine was three HUD documents plus one Wayback retrieval, with two targeted WebSearches to date the policy change and one WebFetch to corroborate it. One sub-agent on the partial-claim source hunt (budget + DATA-RETURN guardrails stated). **The verdict came entirely from the primary pull; the fan-out was never the right tool for this one.**

**What worked / didn't:**
- **The decisive move was recognising that HUD publishes a stock and a flow in the same report**, which supports the identical decomposition CARL's construction requires — without needing the partial-claim counts I went looking for. The commission framed this as "quantify the partial-claim wedge"; the data supported a better question, *what happened to the drain*, and answered it.
- **`pdfminer` default layout parameters destroy these tables** — columns emit as one long numeric stream with no row keys. Tuned `LAParams` recovered them, and I validated the reconstruction by checking that SDQ = 90-day + foreclosure + bankruptcy on **all 13 rows** before using a single figure. That check is what makes the table trustworthy; without it I would have been aligning columns by eye.
- **Cross-vintage verification paid off**: the June-2025 and May-2026 reports overlap at May 2025 and agree to the digit, which is what licenses the spliced baseline.
- **My own fixed `pdf2text.py` and `fetch_url.py --status` were used throughout** — the `--status` sweep found the current-vs-archived URL split in four calls.

**Data gaps:** partial-claim counts (flow) and receivable stock; DASP/SFLS status; VA/VASP; TPP delinquency reporting code.

**Source frustrations:** HUD's LPT archive is not addressable — the filename convention changed and old issues 404 at both current path patterns, so historical vintages require the Wayback Machine. That is a real recurring obstacle for any FHA time series and is going to BACKLOG.

**On the sub-agent leg:** one source hunt ran under DATA-RETURN + budget guardrails and returned the FY2021–24 count table, the FY2025 omission, the HVLS status and the VASP wind-down. **I re-pulled Exhibit II-3 at primary before using it**, per the standing rule that a load-bearing number the fan-out returns gets a primary attempt — which is how the 810,000-vs-1,127,672 internal contradiction surfaced. The agent also **caught and refused to pass through** a trade-press "$7.7 million" figure that is implausible by ~1000×; that is the behaviour the guardrails exist to produce, and it saved a fabricated-looking number from reaching CARL.

**Errors caught in-run (2):**
1. **I initially ran the decomposition on the 90-day-only bucket**, which leaks: a loan entering foreclosure exits the 90-day bucket without leaving delinquency. Re-ran on the full SDQ perimeter so those transitions net out. The answer barely moved (193 → 191bps, same 78/22 split) — but I would have been defending a number with a known leak in it, and the robustness check is now part of the finding rather than a hope.
2. **I nearly reported the outflow collapse without testing the foreclosure-moratorium alternative**, which produces an identical stock build with an opposite meaning. Table 4 refutes it decisively (starts +33.9%). Had I skipped it, the report's central causal claim would have rested on the policy timing alone.

**Confidence:** High on §§1–3. Medium on §4 (bounded, not measured — and labelled that way throughout). The aggregation table in §5 is arithmetic on stated inputs, not a claim.

**If I had more time/tools:** the HUD OIG report **2026-KC-0005** (*HUD Did Not Correctly Service all Due and Payable Partial Claims*, 2026-06-25) — the one document likely to carry a partial-claim-specific stock figure; hudoig.gov URLs guessed at returned 410/404 and it needs the real permalink. Second: any SFDMS/NSC interim extract carrying FY2026 loss-mit completions, which would confirm §§1–3's drain collapse **by name** rather than by elimination.

**Suggestions:** (a) a `scripts/` helper for HUD LPT retrieval + table extraction with the tuned `LAParams` — this is now the second FHA run to hit the same PDF wall and the table reconstruction is fiddly enough to be worth encoding once; (b) the general lesson worth carrying beyond this report: **when a commission asks for a specific quantity, check whether the publisher's data supports a decomposition that answers the underlying decision better** — the drain question was both more answerable and more decision-relevant than the wedge question as posed.
