# SAM reboot: intervention inference, portfolio direction and BOJ proxy

Reviewed September 20, 2026 by CATO for Will. Scope: SAM's operator-facing message pasted by Will; no authorization to build the proposed proxy, route assignments, change positions or replace owner judgments. Initial HEAD `815bc120f`, later inspected HEAD `3c2e8b663`; shared master advanced during review. TERRY's paper-book edit and subsequently PROME's proposal edit were observed and preserved; no pull. Earlier grading review remains [the bounded stopping receipt](2026-09-19_2326_sam-stopping-receipt.md).

Disposition: correct the new claims before automating them. SAM appropriately withdraws confidence in an unmeasured funding narrative and identifies a stale mirror. Its replacement conclusions contain consequential errors. This reviews the message, not a reproduced event study: targeted searches of SAM research/reports/status did not locate the supplied table's calculation artifact. Its price data, 176-session baseline, standard deviation and endpoint conventions remain unverified.

## F1 — High: portfolio direction contradicts recorded instruments

SAM describes KRE/HBAN/WAL as bank longs and infers losses alongside duration shorts in a risk-off event. `FORGE/STATUS.md` sections KRE, WAL, Other puts and Robinhood instead record purchased puts: KRE December 60P and January 25P, HBAN October 16P, WAL December 70P, alongside older expired/past-date rows. `PROME/reports/2026-09-16_prefed-sell-review.md` opening capture addendum also records WAL70P and KRE25P. A long put has bearish underlying exposure; long the option does not mean long the bank. A fall in the underlying supports its value other things equal. This does not establish an effective portfolio hedge: strikes, time, volatility, remaining value and actual current holdings matter.

The September 16 report also records TLT October82P in addition to September77P and TBT, so “two duration-short legs” is incomplete against the inspected record. The mirror expressly says September10 reconciliation, September19 receipt-only update, known September16 contradictions. No broker recertification occurred here. Require an instrument-and-direction inventory with evidence vintage before claiming the book's sign or correlation; do not infer fresh positions from stale rows. The claimed bank-longs-plus-short-duration conclusion is unsupported and contradicted by the available records.

## F2 — High: JGB spread is not a count of priced hikes, and dates are mixed

`AGENTS/SAM/workbook/JGB_YIELDS.tsv:360` contains September17 two-year yield 1.868%. Subtracting 1.25% gives 61.8bp arithmetically. But the BOJ announced that 1.25% guideline September18, effective September24. The pair combines a pre-decision bond observation and a newly announced, not-yet-effective policy setting. A later policy input alone can move the spread without any new market price. [BOJ decision, page1](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf).

Even with aligned dates and no term premium, a two-year yield reflects an average expected short-rate path, not just its terminal level. Illustrative first-order counterexample: one permanent 25bp hike immediately adds 25bp to a two-year average; the same hike after eighteen months adds only 6.25bp. Dividing the spread by25 cannot determine the number of hikes. Term premia can be positive or negative, so SAM's assertion that this proxy necessarily overstates expectations is also unjustified. [Bank of England explanation, pages2 and7](https://www.bankofengland.co.uk/-/media/boe/files/speech/2015/interpreting-the-yield-curve-warning-or-opportunity.pdf).

If later assigned, a raw two-year yield and consistently defined policy spread could be descriptive context, explicitly dated and separated from meeting pricing. Do not label it hike count/probability or use it as a replacement for meeting-to-meeting OIS.

## F3 — High: a weak event study cannot retire the funding mechanism

Accepting the quoted inputs only, 3.5 / (5.8 / sqrt(5)) = 1.349. That reproduces arithmetic under an independent-observation assumption, not a valid significance calculation. The five named dates lie in two clusters, with overlapping multi-day event windows. Dependence must be handled; the sample cannot simply be treated as five independent intervention shocks. A baseline formed from overlapping forward returns also needs care. No exact effective sample size is established here.

Observed Treasury rallies can coexist with Treasury sales when other forces dominate. The event study can fail to support SAM's confident directional story without demonstrating that the channel is absent or immaterial. If “from op day” means closing price on that date, it may exclude the immediate response; this is a conditional concern pending calculation code, not a verified implementation defect. Require the actual per-event returns, source dates, endpoint rules and overlapping-window treatment before certifying the table.

The scale argument adds an unsupported execution assumption. [MOF's April–June disclosure](https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2026_2Qe.html) confirms April30/May4/May6 amounts and dates. [The July30–August26 monthly release](https://www.mof.go.jp/english/policy/international_policy/reference/feio/monthly/20260828e.html) establishes an aggregate ¥15,399.3bn for that reporting interval. It does not establish sales spread across four weeks, nor the two July execution dates. Separate evidence is needed before calling all five dates MOF per-operation disclosures. The reporting interval is not an execution schedule.

Taking SAM's $98bn and $900bn/day assumptions at face value gives about10.9% of one day's gross turnover. This ratio neither identifies Treasury funding nor bounds price impact: timing, instrument/maturity, market depth and offsetting flows matter. Dollar funding need not be entirely Treasury sales. No independent certification of the $900bn statistic or actual funding composition is claimed. Retire unsupported certainty, not the channel on the strength of a statistically inconclusive table.

## F4 — Medium: an existing visual-review path is presented as a Will-only blocker

`AGENTS/SAM/workbook/BOJ_OIS_README.md` explicitly provides `boj_ois.py --prepare-review`, original image and manifest preservation, SAM visual transcription, `--no-write` validation and ingestion. The accepted review-method literal is `SAM visual transcription`; the limitation is absent automatic image decoding. Nothing in that contract requires Will to be the transcriber. A runtime/tool limitation could exist, but SAM's message does not establish one.

Recommended next bounded owner task: use the existing review process, or report the specific source/tool failure encountered. Creating a different instrument does not close the missing current meeting-pricing read. CATO did not run that operational task or write a quote ledger.

## F5 — Medium: scenario and routing claims need narrower scope

A flight-to-quality Treasury rally can hurt bearish Treasury positions; that is a plausible conditional scenario, not the unique Japan transmission. Calling equity the only real channel is unsupported, and SAM's own rate-loss argument acknowledges rates exposure. August2024 is not an isolated Japan experiment: BIS describes leveraged equity/FX unwinds amplifying an initial adverse US macro release. An August5 bank drawdown is therefore a historical scenario observation, not a causal Japan coefficient. [BIS Bulletin90](https://www.bis.org/publications/bulletin-90-market-turbulence-and-carry-trade-unwind-august-2024).

The September16 capture routing gap is real and already prominently recorded in the mirror, including the source's missing image timestamps/activity/completeness limits. Transcription of that evidence and a fresh complete reconciliation are distinct tasks. No owner message, assignment or new broker request was sent by CATO. The blanket “Japan shut” language should retain the product distinction already established in the separate PROME review: eligible derivatives are not covered by the cash-equity holiday claim.

## Checks, changes and next action

Primary MOF and BOJ documents inspected; local OIS contract, yield row, mirror and September16 report checked. Arithmetic above independently recalculated from supplied inputs; event returns, market data and current broker positions not reproduced or independently certified. No application code changed, so no application test suite was run. Only this report and CATO continuity authored. Closeout uses whitespace, root weekday-claim and orphan checks; final commit/push receipt belongs in-session.

Suggested priority: correct the portfolio sign and unsupported conclusions, preserve a reproducible study artifact, then complete the existing OIS visual review. No proxy build, peer launch, trade, grade or policy change authorized by this review. Next CATO session: orient and await Will; review revised owner evidence only if assigned.
