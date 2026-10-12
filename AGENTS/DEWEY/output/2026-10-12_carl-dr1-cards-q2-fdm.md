# CARL-DR-1 card leg — Q2 disclosures exist; the causal delinquency wedge does not

**Date:** 2026-10-12 | **Mode:** Thesis | **Commission:** CARL-DR-1 card leg / PROME L567 | **Status:** Q2 pull delivered; Q3 refresh pending publication, existing deliver-by 2026-11-13. **Confidence:** High (issuer disclosures and arithmetic); NOT COMPUTABLE (class-wide causal delinquency suppression).

## Key finding

All three named issuers publish the requested loan-modification disclosures. Their disclosed recent modified-card cohorts contain **$3.182B / $971M / $264M classified current** at June30, 2026 (Capital One / Synchrony / Bread). These are observable balances, **not estimates of delinquency hidden by modification**. No filing supplies the untreated counterfactual or the complete class-wide overlap map required to score CARL's50bp kill. Q3 filings had not appeared in the issuer submissions feeds at this10/12 pull.

Scope is credit cards only: Capital One's reporting segment also contains personal loans, which are removed below; Synchrony's commercial-credit and installment categories are removed. No mortgage/auto figures are added and CARL's frozen household-credit grading card is untouched.

## Evidence — keep enrollment, period-end cohort and total book separate

All dollar entries below are **millions**, as of or for the period ending **June30, 2026**. "Q2" means three months; "H1" means six. Primary sources: [Capital One10-Q, filed7/28](https://www.sec.gov/Archives/edgar/data/927628/000092762826000089/cof-20260630.htm), [Synchrony10-Q, filed7/23](https://www.sec.gov/Archives/edgar/data/1601712/000160171226000033/syf-20260630.htm), [Bread10-Q, filed7/28](https://www.sec.gov/Archives/edgar/data/1101215/000110121526000074/bfh-20260630.htm); read directly from SEC10/12.

| Metric / basis | Capital One | Synchrony | Bread |
|---|---:|---:|---:|
| Q2 modification-period amount |1,077|537|89|
| H1 modification-period amount |2,109|1,153|196|
| Recent modified-card cohort: current balance |3,182|971|264|
| Same cohort:30+ days delinquent |714|288|61|
| Same cohort:90+ days delinquent |333|132|23|
| Same cohort:total balance |3,896|1,259|325|
| Total card-book denominator |266,789|94,233|17,808|
| Current cohort / card book, derived basis points |119.27|103.04|148.25|

The **last row is a scale comparison**, not a causal wedge or a class-wide bound. All current program balances could include borrowers who would already be current without relief. Disclosures can exclude older modification cohorts, exited programs and temporary relief below the accounting threshold. Numerator definitions differ; no pooled average is presented. **Capital One includes international cards in this table**, so it is not a US-only perimeter. Its domestic-only current cohort is $3,098M against $259,005M = **119.61bp**; domestic-only Q2/H1 modification amounts are $1,008M/$2,001M.

**Capital One:** Note4 Tables4.7/4.9/4.10, printed pp95–101. Q2=1,008 domestic+69 international; H1=2,001+108. Recent-cohort current=3,098+84; total=3,743+153. Its rolling12-month performance table differs from current-period modification amounts. The denominator is259,005+7,784; personal loans are excluded throughout. Discover acquisition/pre-closing cohorts are included in disclosures and complicate comparisons. Domestic interest reductions averaged15.42 percentage points inQ2; modifications enter credit-quality/allowance estimates. Subsequent defaults were178 inQ2 and365 inH1 across domestic/international cards; default includes90+ delinquency, charge-off or nonaccrual. Already-defaulted entrants are excluded from that subsequent-default definition. These are default amounts, not rates. [Capital One source above.]

**Synchrony:** Note4, pp47–48. Q2=341 long-term+196 short-term; H1=739+414. These amounts use **enrollment-date balances**. Performance covers loans modified within12months and still in a program: current915+56, delinquent227+61. Current status requires full minimum-payment catch-up or re-aging after three monthly program payments. Long-term modifications reduce interest rates by97% **relative**, not97 percentage points. Long-term card modifications defaulted/charged off88 inQ2 and166 inH1;62% of short-term-modified loans completed required payments/exited duringH1. Neither denominator is a matched untreated cohort. [Synchrony source above.]

**Bread:** Note2, pp38–40. The89/196 amounts are **June-end balances of modifications undertaken duringQ2/H1 that remain in programs**, including interest/fees, not enrollment flows. The12-month still-program cohort has325 total,264 current and61 delinquent. H1 subsequent-default balances total26. Temporary relief can delay delinquency/charge-off progression and may fall outside disclosed modifications. Separately reported re-aging is3.2% forQ2 and3.3% forH1 of total card-and-other loans; it returns affected balances to current. That metric overlaps relief/modifications in an unquantified way and cannot be added to the cohort ratio. [Bread source above.]

## What the card leg can and cannot establish

The mechanisms are visible: rate/payment relief, re-aging and slower delinquency progression. Their presence does not establish delayed **loss recognition**: lifetime expected losses can still enter the allowance while an account is reported current. Reported delinquency and accounting recognition must be tested separately.

No public table found identifies all balances that changed from30+/90+ to current *because* of relief, how long that classification effect lasted, or the overlap with older programs/re-aging. Therefore neither "less than50bp" nor "more than50bp class-wide" follows from the119/103/148bp scale figures. CARL owns the combined six-leg assessment and kill disposition; this card pull does not grade it.

## Counter-evidence and first observable tells

Program balances remaining delinquent, defaults after modification, and required actual payments before re-aging argue against treating every modified balance as hidden distress. Conversely, incomplete temporary-relief/older-cohort coverage prevents the measured cohort from being a complete ceiling on masking. Disclosure is not absence of risk, but zero measured counterfactual effect is not proof of zero effect either.

The available tells are **cohort current/30+/90+ mix**, subsequent-default/charge-off amounts, and program enrollment/exit patterns, kept on their own cohorts and clocks. A default amount from a12-month cohort must not be divided by a six-month enrollment flow to manufacture a rate. A future rise in these tells would need comparison with ordinary portfolio quality and composition before attribution.

## Source quality, reproduction and process

CIKs were verified against SEC's ticker map: **COF927628, SYF1601712, BFH1101215**. SEC submission feeds supplied accession, primary document, report date and filing date; Q2 primary documents were downloaded in full, filing identity checked, and relevant tables/definitions parsed with separate card rows. Extracted source tables, metric definitions and SHA-256 of full downloads live at `research/2026-10-12_cards/`. Reproduction: retrieve the exact linked filings and use the numbered notes/tables/pages above; sums and ratios are explicit here. No XBRL tag or similarly named exhibit silently substitutes for the primary filing.

**Process:** one issuer-identity pull, three submission feeds, three full10-Q downloads, targeted note/table reads; no fan-out. Web could not open Capital One's8.3MB filing due its size limit; direct SEC retrieval succeeded. Known trap caught before delivery: Capital One "Total credit card" includes personal loans. Gaps: class-wide counterfactual, program overlap and Q3 publication. **Q3 follow-up is the existing commissioned refresh**, not a new program: replace each issuer's Q2 extract when its actual September30 report is filed and deliver byNovember13; do not guess future values or close that obligation today.
