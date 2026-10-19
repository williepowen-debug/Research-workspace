# WAL — Q2 → Q3 → guided Q4 earnings bridge

**October 19, 2026, after close.** Will authorized the first ranked follow-up in `2026-10-19_next-understanding-options.md` by asking to start it now. This completes the bounded public-source pass, continuing the saved Stage1/full-read work. It does not commission the wider mortgage, borrower, recorder or litigation investigations. Call answers remain future evidence.

**Judgment:** Q3 credit evidence remains favorable relative to the frozen bear tests, but the profit improvement is modest after a consistent visible-gain screen. The revised income/expense guidance is approximately neutral at mechanical midpoints, conditional on unchanged accounting bases. The most useful earnings question is how management gets operating expenses below Q3 while maintaining recurring fee earnings. Neither an earnings collapse nor a clean acceleration has been established.

## Evidence and reproducibility

All amounts below are **USD millions**, except EPS. Primary sources:

- [Q3 issuer release, SEC EX99.1, accession 0001628280-26-066286](https://www.sec.gov/Archives/edgar/data/1212545/000162828026066286/pressrelease-9302026.htm): current comparative income statements, earnings-credit/referral table, non-GAAP reconciliations, reclassification paragraph. Local `sources/2026-10-19_Q3/pressrelease-9302026.htm`.
- [Q3 issuer presentation, EX99.2](https://www.sec.gov/Archives/edgar/data/1212545/000162828026066286/walq32026earningspresent.htm): slides 4, 11 and **17**; slide17 visually re-read for this pass. Management outlook is annual; Q4 NII is described separately as flat to slightly up from Q3, assuming one further 25bp December hike.
- [FY2025 issuer release, SEC EX99.1, accession 0001628280-26-003507](https://www.sec.gov/Archives/edgar/data/1212545/000162828026003507/pressrelease-12312025.htm): annual bases **NII 2,864.8; noninterest income 678.2; expense 2,111.7; deposit expense 630.5; expense excluding deposits 1,481.2**. Newly retrieved HTTP200; bytes/hashes/UTC receipt in `sources/2026-10-19_earnings-bridge/`. These unrounded-to-billions source amounts replace the deck's rounded labels for the calculations; management has not supplied a precise guide-basis reconciliation.

Calculator `scripts/earnings_bridge_20261019.py` parses saved primary HTML, independently ties fee/expense components, pretax, tax, nine-month totals and ECR totals, and writes `research/2026-10-19_earnings-bridge.json`. Source table numbers there are zero-based BeautifulSoup locators. **26 accounting checks passed; nine protected files unchanged.** One duplicate-label parsing error was caught by the component tie and corrected before results were written. The web reader could open FY2025 but not Q3; the saved actual Q3 SEC bytes remain available, not an unavailable disclosure.

Reuse: October14 WAL conditional bridge and REGINALD public FY2027 test/review. Neither is a fresh post-print consensus estimate. The old script/output remains intact; it was not rerun through today's reclassification. No new peer/funding study or analyst-model request.

## What produced the actual earnings change?

| Line | Q2 | Q3 | Effect on pretax profit |
|---|---:|---:|---:|
| Net interest income |796.9|807.6|+10.7|
| Commercial banking income/related fees |73.1|78.7|+5.6|
| Mortgage origination/sale |53.4|55.7|+2.3|
| Net servicing revenue |31.3|23.8|−7.5|
| Securities-sale gains |3.0|16.8|+13.8|
| Net fair-value adjustments |8.3|0.5|−7.8|
| BOLI + equity income + other fees |29.7|31.1|+1.4|
| Deposit-cost expense |179.2|165.4|+13.8|
| Operating expense excluding deposit costs |404.1|429.7|−25.6|
| Consolidated credit provision |80.4|80.0|+0.4|
| **Pretax profit** |**332.0**|**339.1**|**+7.1**|

Revenue +18.5 less expense +11.8 gives PPNR +6.7. Lower provision adds0.4. Tax expense falls63.2→61.9, adding1.3 to net income despite higher pretax earnings. Net income and common net income both rise8.4, to277.2 and266.9 respectively. Printed diluted EPS rises2.36→2.45; diluted shares108.0→107.8 also help. We use the issuer's printed EPS; rounded income/share/award figures are not an exact reconstructed EPS denominator. Effective tax falls about19.0%→18.3%, so it is inappropriate to annualize the headline EPS change as entirely operating growth.

The25.6 operating-expense increase contains **21.8 salary/benefits**,3.7 data processing,1.6 legal/professional/director fees and other net changes−1.5. There is no disclosed quantified temporary-compensation add-back. No salary, legal or servicing cost is removed as a presumed one-off.

## A like-for-like visible-gain screen

| Diagnostic | Q2 current presentation | Q3 |
|---|---:|---:|
| Reported PPNR |412.4|419.1|
| Less securities gains + net fair-value adjustment lines |11.3|17.3|
| PPNR after those two exclusions |401.1|401.8|
| Less consolidated provision |80.4|80.0|
| **Pretax after those two exclusions** |**320.7**|**321.8**|

Thus6.0 of the7.1 pretax improvement is the change in the two visible gain lines; the remainder is1.1. This is **an accounting diagnostic, not normalized EPS, an issuer adjusted measure or proof those gains never recur**. Sale gains can accompany balance-sheet repositioning and hedge effects; mortgage valuation/hedge effects can sit inside servicing and other lines. The screen leaves those unknown embedded effects in earnings. Removing equity income too, or adding back costs, would require a separate justified assumption and is not done here.

Q3 reclassifies customer back-to-back swaps, risk-participation agreements and FX into commercial fees, without changing income/equity. **Q2 FV is now8.3 versus12.8 in the old October14 screen.** Comparisons use today's reclassified quarters on both sides; old8.98 annualized screen is not carried forward. Aggregate commercial fees are consequently not a pure cash-service-charge series.

Mortgage revenue falls84.7→79.5 despite origination gains rising2.3, because servicing falls7.5. Q3 MSR cash collections/runoff, valuation, hedge P&L and expense allocation are not separately reconciled in these materials. The Q2 net-mark reconstruction in REGINALD's prior work is historical Q2 evidence, not a Q3 adjustment. Servicing declines do not by themselves prove underlying cash franchise deterioration.

## Earnings credits: three lines, one cost

| Embedded ECR/referral location | Q2 | Q3 | Pretax effect of change |
|---|---:|---:|---:|
| Reduces interest income |52.5|56.7|−4.2|
| Reduces commercial fees |8.4|8.6|−0.2|
| Included in deposit-cost expense |173.3|158.4|+14.9|
| **Total** |**234.2**|**223.7**|**+10.5**|

Other deposit-cost expense rises5.9→7.0, so the expense line falls13.8 rather than14.9. All of these effects are already in the actual earnings bridge. **Adding the10.5 ECR reduction to the reported profit change would double-count it.** Deposit interest expense also rises370.5→382.5 and is already inside NII. Gross line effects do not measure the net economics of displaced deposits, asset changes and funding replacement; that attribution and peers remain REGINALD-owned.

## What revised annual guidance implies for Q4

Formula: FY2025 actual × (1 + guided annual growth) − actual9M2026. This is **conditional residual arithmetic**, not management's Q4 forecast; guide rounding, exclusions and bases require confirmation. No invented correlation among range endpoints.

| Item | Revised annual guide | 9M actual used | Implied Q4 if same basis |
|---|---:|---:|---:|
| NII |+11–12%|2,370.8|**809.128–837.776**|
| Noninterest income, literal GAAP basis |+18–21%|658.0|**142.276–162.622**|
| Total noninterest expense |+7–10%|1,752.8|**506.719–570.070**|
| Expense excluding deposits |1,600–1,650|1,244.9|**355.1–405.1**|
| Deposit-cost expense |650–675|507.9|**142.1–167.1**|

**NII:** residual809–838 is consistent with the separate flat-to-slightly-up commentary relative to807.6; the exact upper range depends on how the rounded guide is intended. No independent rate forecast is introduced.

**Fees need a basis answer:** the literal GAAP residual is below Q3's206.6. If, solely illustratively, FY2026/YTD guidance excludes the Q1 securities gain50.5 while retaining the same678.2 FY2025 denominator, Q4 residual instead becomes **192.776–213.122**. The adjusted EPS reconciliation removes that Q1 gain; it does **not** explicitly prove this is the fee-guide basis. Other exclusion or denominator choices would produce different numbers. We do not select a fork, infer a fee collapse, or label192.8–213.1 management guidance. Ask for the actual fee-guide reconciliation in dollars.

**Costs are the strongest reconciliation question:** even the upper1,650 expense-ex-deposit guide leaves Q4 **405.1**, below Q3's429.7 by **24.6**, or5.7%. The lower guide endpoint implies355.1, a74.6 decline. Management says it is tracking the **upper end**, so the24.6 step-down is the relevant first question. Repeating Q3's429.7 would give full-year1,674.6,24.6 above that upper guide, if definitions match. Total expense guidance similarly implies at least25.030 below Q3's595.1. These are required reductions under the literal interpretation, **not an established miss**: call may identify temporary costs, seasonality or an adjusted guide basis. The salary spike21.8 is close in size but has not been attributed to a temporary item, and its reversal alone would not quite explain24.6.

Expense components imply total Q4 cost497.2–572.2; annual percentage guidance implies506.719–570.070. Their feasible intersection exists. Component endpoints are not necessarily intended to occur together; use neither the gap nor rounding to declare guidance internally inconsistent.

## Did the revision itself cut expected profit?

Mechanical midpoints, holding FY2025 bases and guide definitions consistent:

| Annual change versus prior guide midpoint | Pretax effect |
|---|---:|
| NII midpoint13%→11.5% |−42.9720|
| Fee midpoint15%→19.5% |+30.5190|
| Expense midpoint9%→8.5% |+10.5585|
| **Net** |**−1.8945**|

Using the dollar component cost ranges instead, unchanged ex-deposit midpoint and lower deposit midpoint imply12.5 cost savings and **+0.0470** net pretax change. Both methods indicate approximately flat net midpoint economics. The difference reflects rounded, overlapping guide representations; do not blend them or count both cost benefits. Midpoints are an analyst convention, not management expectations, and this comparison says nothing about whether current consensus has already priced it. Without fresh basis-matched post-print forecasts, **no demonstrated expectations gap** remains the conclusion. A lower NII growth guide alone is insufficient evidence of a similar EPS guide cut.

## Tax, provision and shares: do not smuggle in an EPS forecast

- Nine-month effective tax is167.2/902.4≈18.53%. If **full-year** tax were exactly19%, Q4 tax would be **0.19×Q4pretax +4.256**. At unchanged339.1 pretax that is68.685, about20.25%, rather than61.9 in Q3. If19% instead describes only a Q4 planning rate, that extra catch-up does not follow. The guide says approximately19%; neither exact outcome is promised.
- NCO guidance25–35bps, tracking the upper half excluding fraud, is a realized-loss guide. It is **not** a provision forecast. Q3 loan provision80.8 includes reserve build35.0 above NCO45.8; HTM reserve release0.8 makes consolidated provision80.0. Do not substitute NCO for provision or subtract losses twice.
- Repurchases reduce shares, but Q4 average diluted shares/participating-award allocation are not guided. No current option valuation, share-count trajectory or fresh consensus estimate is assumed.
- Sensitivity only: **10 of quarterly pretax earnings ≈$0.075/share** after19% tax at107.8 diluted shares, before changes in award allocation and other deductions. This works in either direction. Neither annualizing2.45 nor stripping selected gains yields a validated forward EPS forecast.

## Tomorrow's call: precise questions to append to the existing read-sheet

These refine Stage1 earnings questions6/7 and the full-read earnings question; they do not replace the leading **$99M appraisal/status/reserve** and **explicit new Office migrations** questions. No external question has been sent.

1. **Expense basis and step-down:** Is1,600–1,650 annual expense excluding deposits directly comparable to reported9M1,244.9? If so, what reduces Q4 to≤405.1 versus429.7 in Q3? Quantify temporary compensation, accrual timing, hires, legal/OREO costs and recurring run rate. How much of21.8 salary/benefit growth reverses, and when? If adjusted, reconcile every exclusion in dollars.
2. **Fee-guide denominator/numerator:** Does18–21% use FY2025 GAAP678.2 and FY2026 GAAP noninterest income? Which securities gains, marks or other items are excluded from each year? Give comparable9M and implied Q4 dollars; explicitly reconcile the Q1 gain50.5 and YTD gains70.3. What portion of commercial78.7 is recurring service charges versus customer derivative/FX results?
3. **Mortgage cash and hedge bridge:** Reconcile23.8 servicing revenue to recurring fees/early payoffs, MSR runoff, mark, hedge P&L and sales; locate associated servicing/hedge costs. What explains7.5 sequential decline? What Q4 origination volumes/margins and servicing assumptions support the fee guide?
4. **Net optimization economics:** Reconcile the10.5 reduction across all three ECR/referral locations with replacement funding costs and asset balances, without double-counting13.8 expense savings. Provide net recurring pretax contribution and implementation costs. Route funding/cohort interpretation to REGINALD.
5. **Provision/tax/share bridge:** What Q4 reserve-build assumptions accompany upper-half core NCO guidance? Is~19% tax full-year or Q4 exit rate; any benefit or true-up expected? What diluted-share/award assumptions support the outlook after repurchases?

**Unavailable versus adverse:** observed cost growth, lower servicing, lower NII guide are findings. Guide exclusions, expense reversals, Q3 MSR mark/hedges and future provision/tax/share count are unknowns. Missing answers are not zero costs, no hedges, a guide miss or a new credit loss. If call is silent, carry those items as PENDING-10-Q where that filing can answer; management-only forward assumptions remain UNANSWERED rather than presumed forthcoming in a filing.

## Authority, persistence and closeout

Frozen grades, WAL01/02 priors, registered scenario weights, EV/PT, score and all trade/account rules remain unchanged. Positions are not re-underwritten: Fidelity70P and65P retain accepted October19 evidence and outstanding card/execution issues; Robinhood-only81.90×3/December4 rules do not migrate. No order, external send, helper or background job. Current runtime remains Codex/OpenAI; exact model variant/native session identity unavailable. No verified native transport to supplied PROME/TERRY thread IDs; saved packets establish persistence, not recipient consumption or closeout acknowledgment. Foreign dirty work requires pull/push deferral; exact-path local commits only.

## COMPLETION — WAL — 2026-10-19
STATUS: ✅ DONE — bounded earnings bridge; call answers pending future event.
CHANGED: This report, reproducible calculator/JSON, FY2025 source archive, owned state/KB, dated PROME and owner packets.
RESULT: Pretax rose7.1M; visible-gain-screen increase1.1M. Literal cost guide requires≥24.6M Q4 ex-deposit cost decline; guide midpoint net roughly flat.
GAPS: Guide basis, MSR cash/mark/hedges, cost persistence and forward assumptions await call; native recipient transport/consumption UNKNOWN.
WILL_NEEDS: None; Will authorized this bounded follow-up. Existing broker dependencies stay with PROME/TERRY.
FOLLOW-UP: October20 noonET call using five earnings questions plus unchanged credit lead; later10-Q cross-check where applicable.
