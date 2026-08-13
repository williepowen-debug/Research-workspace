# CARL-DR-1 — The recognition-artifact census: quantifying the deferral wedge
**Date:** 2026-08-13 | **Mode:** Thesis | **Confidence:** High (the GSE single-family leg — every figure from the 10-Q, reproducible) / **NOT DELIVERED** (four of six mechanism legs — see §Coverage, and read it before using this)
**Commission:** CARL-DR-1 (Will-approved 7/31) | **Consumers:** CARL action; REGINALD/HOMER/LIQUID/RED info
**Engine:** primary-pull only (Will-ruled). **Hard constraint respected: nothing here touches `AGENTS/CARL/thesis/HHDC_Q2_2026_GRADING_CARD.md`.**

> **⚠️ READ THE COVERAGE SECTION FIRST. This is a ONE-LEG census, not the six-leg census commissioned.** I quantified the GSE single-family book properly and did not reach FHA/VA, auto ABS, cards, BNPL, or private-credit-consumer. The kill condition is **class-wide**; one leg cannot discharge it. What follows is **evidence toward** CARL's pre-registered kill, explicitly not the kill.

---

## Key Finding

**On the largest single consumer-mortgage book in the United States, the loss-recognition-deferral wedge is ~22 bps — below CARL's ~50 bps kill threshold — and it is NOT widening. It was ~25 bps a year earlier.**

But the same filing contains a second finding that cuts the other way, and it is the more important one for the tell-list:

**Fannie's deferral machine is running the same volume at materially deeper concessions with visibly worse outcomes.** Total single-family loss-mitigation volume **fell 4.6% YoY**, while the **deepest** modification category (term extension *and* rate reduction *and* other) rose **+135%** ($375M → $881M), the weighted-average interest-rate reduction deepened from **0.61% → 0.73%**, term extensions run **144 months — twelve years** — and re-defaults on previously modified loans rose **+10.9% YoY**.

**⇒ The wedge is small and stable; the *price* of holding it there is rising fast.** That is what deferral capacity being consumed looks like, and it is the answer to deliverable #2.

---

## Evidence

### (1) The wedge, quantified — Fannie single-family

Fannie's 10-Q discloses the serious-delinquency stock **as a flow decomposition**, which is what makes the wedge computable at all [PRIMARY: FNMA 10-Q, period 2026-06-30, filed 2026-07-29, accession `0000310522-26-000064`, CIK 310522]:

**Single-family SDQ loans (number of loans), six months ended June 30**

| | 2026 | 2025 |
|---|---|---|
| Beginning balance | 97,885 | 97,129 |
| Additions | 96,829 | 89,909 |
| **Removals — modifications and other loan workouts** | **(38,150)** | **(42,153)** |
| Removals — liquidations and sales | (14,885) | (14,043) |
| Removals — cured or <90 days delinquent | (43,364) | (39,749) |
| **Ending balance** | **98,315** | **91,093** |
| **Reported SDQ rate** | **0.58%** | **0.53%** |

Ending SDQ of 98,315 loans at 0.58% implies a book of **~16.95M loans**. The counterfactual — had the workout removals not occurred and those loans remained seriously delinquent:

| | 2026 | 2025 |
|---|---|---|
| Reported SDQ rate | 0.58% | 0.53% |
| Counterfactual SDQ rate | 0.805% | 0.775% |
| **Deferral wedge** | **~22.5 bps** | **~24.5 bps** |

**Two things follow.** The wedge is **below CARL's ~50 bps kill threshold** on this book, and it **did not widen** year-over-year — it narrowed ~2 bps. If deferral were increasingly masking deterioration, this is the number that should be growing. It is not.

**Also note what the same table says about the underlying:** additions to serious delinquency rose **+7.7% YoY** (89,909 → 96,829) and the ending SDQ stock rose **+7.9%** (91,093 → 98,315). **The inflow is deteriorating while the reported rate moved only 5 bps.** Removals — of which workouts are the largest single category — are what absorbed it.

### (2) The tell-list — what moves first, measured

All three from the same filing, same periods:

| Observable | H1-2025 | H1-2026 | move |
|---|---|---|---|
| Total SF loss-mitigation volume | $29,172M | $27,816M | **−4.6%** |
| Contractual modifications (term ext. + rate-reduction categories) | $6,176M | $6,016M | −2.6% |
| **Deepest category** (payment delay + term ext. + rate reduction + other) | **$375M** | **$881M** | **+135%** |
| WA interest-rate reduction, 20/30-yr fixed | 0.61% | 0.73% | **+12 bps deeper** |
| WA term extension, 20/30-yr fixed | 150 months | **144 months** | −6 months |
| Avg. amount capitalized per payment delay | $13,061 | $13,923 | +6.6% |
| **Re-defaults on loans modified in prior 12 months** (Q2) | **$2,078M** | **$2,304M** | **+10.9%** |

**Ranked tell-list for CARL, most-leading first:**

1. **Modification DEPTH, not volume.** Volume is flat-to-down and tells you nothing; the deepest-concession category **more than doubled** while total volume fell. Depth moves before the wedge does, because a servicer holding a fixed cure target must concede more per loan as borrower capacity erodes. **This is the cheapest early warning in the set and it is disclosed quarterly.**
2. **Re-default on modified pools.** +10.9% YoY on roughly flat modification volume — the direct measure of whether deferral is curing or postponing.
3. **SDQ *additions*, not the SDQ rate.** Additions +7.7% YoY while the rate moved 5 bps. The rate is the net of a deteriorating inflow and a large removal channel; the inflow is the honest series.
4. **Removal-mix shift.** Watch workouts vs *liquidations and sales* — a shift toward liquidation means deferral capacity is being declined, not extended.

⚠️ **I did not compute a re-default RATE, deliberately.** The numerator is loans modified in the **prior twelve months** that defaulted; the denominator I have is a **six-month** modification flow. Different perimeters — dividing them would manufacture a number. The level and its YoY trend are what the disclosure supports. `[[finding_cross_entity_comparison_needs_same_perimeter]]`

### (3) The mechanism is real and issuer-attributed — but the worked example is not consumer credit

HOMER's 7/31 finding is confirmed verbatim in the 10-Q: Fannie's **multifamily** SDQ fell to 0.60% from 0.74% *"primarily as a result of a recent modification of a loan portfolio previously in forbearance, as well as foreclosure activity"* while MF credit provision rose. That is an issuer telling you its headline improvement was an accounting event.

**But multifamily is commercial real-estate lending, not consumer credit.** The commission's decision question is scoped to *"US consumer-credit delinquency."* The MF case **demonstrates the mechanism**; it cannot carry the quantification, and it should not be counted in a consumer-credit wedge. The single-family table above is the consumer-credit measurement, and it is a **different and much smaller** effect.

**A mechanism the commission's scope list did not include, and Fannie names it:** *"the volume and pace of any future nonperforming and reperforming loan sales and their impact on … serious delinquency rates."* **Loan sales remove delinquent loans from the reported book entirely** — 14,885 loans in H1-2026 under "liquidations and sales." That is a recognition artifact by *removal* rather than by *deferral*, it is a management lever, and it belongs in the census. It is **not** included in my 22.5 bps wedge, which counts only the workout channel.

---

## Counter-Evidence

1. **The counterfactual is naive and biases the wedge UP.** It assumes every workout-removed loan would otherwise have stayed seriously delinquent. Many would have cured — 43,364 loans cured without a workout in the same period. **So ~22.5 bps is an upper bound**, which strengthens rather than weakens the below-threshold reading.
2. **Modification is not per se an artifact.** Loss mitigation is a decades-old, regulator-encouraged tool. A modified loan that performs for years is a genuine cure, not deferred recognition. The framework needs re-default to distinguish them — which is why tell #2 matters more than the wedge.
3. **One book is not a class.** Fannie SF is the largest single consumer-mortgage book (~17M loans), but the kill condition is class-wide. FHA's partial-claim waterfall in particular is a *structurally different* mechanism (deferral into an MMI receivable) and could be materially larger relative to its book. **Its absence here is the single biggest reason not to treat this as decisive.**
4. **Fannie is a conserved GSE with disclosure obligations no private lender carries.** The wedge is measurable here *because* Fannie publishes a flow decomposition. Books that disclose less could hide more — so a small measured wedge in the most transparent book is weak evidence about the least transparent ones. **Selection runs against the kill.**
5. **The depth signal is not yet a wedge signal.** Deeper concessions and rising re-defaults are consistent with deferral capacity exhausting — but they have not yet moved the reported rate. They may not.

---

## Coverage — 1 of 6 legs delivered. Read this before citing anything above.

| Leg | Status |
|---|---|
| **GSE single-family** | ✅ **quantified at primary** — the wedge and the tell-list |
| GSE multifamily | ✅ mechanism confirmed (HOMER's finding, verbatim in the 10-Q) — **but not consumer credit** |
| **FHA/VA** — partial claims vs serious-DQ; VA post-VASP PCP | ❌ **NOT PULLED.** HUD MLs / Neighborhood Watch not reached. **The highest-value gap** — it is a structurally different mechanism and was already flagged unpulled in my own 7/24 report |
| **Auto ABS** — servicer extension/mod rates | ❌ **NOT PULLED** (OTTO's 7-deal 10-D panel is the hook) |
| **Cards** — re-age / forbearance disclosures | ❌ **NOT PULLED.** One lead found: JPM's Q1-2026 10-Q is the only non-GSE hit in an EDGAR full-text search for *"previously in forbearance"* |
| **BNPL** — deferral-by-invisibility | ❌ **NOT PULLED** (my own C4 flow-gap finding is the hook) |
| **Private-credit consumer** — CRMT as instance of a class | ❌ **NOT PULLED — and BLOCKED BY SEQUENCING.** The commission says *"reference DR-6's output for the CRMT leg."* **DR-6 has not been run** (deadline ~8/22). The dependency cannot be satisfied in this order |

**Against the pre-registered kill condition:** CARL set the kill at *class-wide deferral moving measured DQ by less than ~50 bps.* I measured **~22.5 bps on one leg, not widening.** That is **directionally toward the kill and materially below the threshold on the book measured**, but **four of six legs are unmeasured** and one of them (FHA partial claims) is the mechanism with the most reason to be large. **CARL should not log a scored strike on this alone.** My recommendation is to treat it as one leg banked, and either re-commission the FHA leg specifically or hold the kill until it is measured.

---

## Reproduction

```
scripts/edgar_doc.py search '"previously in forbearance"' --startdt 2026-01-01 --enddt 2026-08-12
scripts/edgar_doc.py doc --cik 310522 --accession 0000310522-26-000064 > fnma_q2.txt
  then grep LOCALLY filtering 'us-gaap:|xbrli:|iso4217'   (per scripts/BACKLOG.md 2026-08-02)
```
Tables used: SDQ *"Delinquency Status and Activity of Single-Family Conventional Loans"* (flow decomposition — the load-bearing one); *"financial impacts of loan modifications and payment deferrals"* (depth); *"amortized cost of HFI loans that defaulted … had received a completed modification or payment deferral in the twelve months prior"* (re-default).
Book size is **derived**: ending SDQ count ÷ reported SDQ rate (98,315 / 0.0058 ≈ 16.95M loans). Fannie states the rate is computed on loan count, so this is internally consistent; it is not a separately disclosed figure.

---

## Process Report

**Searches run:** 1 EDGAR full-text search, 1 10-Q document pull (345KB), local greps. No web search needed — the whole leg is one filing.
**Data gaps:** four mechanism legs (above). Modified-loan re-default *rate* not computable from disclosed perimeters.
**Source frustrations:** none new; the local-grep-with-XBRL-filter recipe from BACKLOG worked first time on a 345KB extract.
**Errors avoided (2, both by stopping rather than computing):** ① I nearly divided a 12-month-lookback re-default numerator by a 6-month modification-flow denominator to produce a "re-default rate." Different perimeters; the number would have looked authoritative and meant nothing. ② I nearly carried Fannie **multifamily** as the census's worked example — it is the commission's own worked example, but MF is commercial real estate and the decision question is scoped to *consumer* credit. Reporting it as a consumer-credit wedge would have overstated the effect by roughly an order of magnitude relative to the single-family measurement.
**Confidence:** High on every figure in §1 and §2 (single filing, primary, reproducible). **Low on the class-wide question**, because I measured one sixth of it.
**If I had more time/tools:** the **FHA partial-claim leg**, without question — it is a different mechanism (deferral into an MMI receivable rather than a term extension), it has been flagged unpulled since my own 7/24 report, and it is the most plausible candidate for a wedge large enough to matter.
**Suggestions:** the SDQ **flow decomposition** is the reusable asset here — most issuers report a delinquency *stock*, and a wedge is only computable where removals are itemised. **Worth checking which other consumer lenders disclose a removals table**, because that determines where this census can ever be quantified versus only asserted.
