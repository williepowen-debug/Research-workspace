# WAL rate sensitivity and funding reconciliation

**Dated:** October 13, 2026 evening ET. **Authority:** Will and `inbox/2026-10-13_from-PROME_Will-directed-WAL-rate-funding-reconciliation.md`. Bounded reconciliation; WAL owns its specialist judgments and frozen grading frames.

## What we can establish now

WAL's positive net interest income sensitivity is real counterevidence to a generic rising-rates earnings squeeze. The stronger conclusion that its overall earnings benefit equally is unsupported. Its Q2 issuer deck provides the missing comparison: under the same gradual100bp rise, next12-month NII increases3.2%, while broader earnings-at-risk increases only0.8%. WAL describes the latter as approximately neutral because ECR deposit costs and mortgage banking revenue reduce asset sensitivity. Rates can therefore support earnings while securities marks reduce tangible equity.

**Primary verification updated after WAL supplement:** fresh SEC Q2 release/deck text plus direct inspection of the original Q2 HTML downloaded by WAL. Hash matches its receipt: `63f0a86758850f7c833bfe111d86dbd7bb9810b0ea6ce0550cc841e0b66ad85f`,6,664,360bytes. Item3, Notes2/8/11/12, equity and liquidity sections now close the June source gaps. This is coordinated reuse of one original filing, not an independent second retrieval or a complete new whole-filing review. Initial retrieval failures remain in the receipt; the initial report version is `f1b7b525b`. WAL supplement version read: `03e60dc0e`. Receipt: `domain/sources/2026-10-13_WAL_rate-funding-reconciliation-receipt.json`.

| Measure at June30 | Finding | Verification and interpretation |
|---|---|---|
| NII, +100bp gradual ramp | +3.2% | Fresh Q2 deck slide11: dynamic balance sheet, forward-curve base, gradual parallel move over12months. |
| Broader earnings-at-risk, same ramp | +0.8%; −100bp also +0.8% | Same primary slide. Defined as pretax NII adjusted for rate-sensitive non-interest income/expense, rather than GAAP net income or EPS. Different denominators prevent subtracting these percentages to estimate dollar costs. |
| Asset/liability repricing | 67% of earning assets variable;53% reprice to SOFR; variable liabilities equal87% of earning assets, primarily modeled to Fed Funds; non-maturity deposits including ECRs have59% beta | Same primary slide. The87% is a ratio to earning assets, not a share of liabilities. Actual SOFR/Fed Funds/curve paths and timing matter. |
| Instantaneous +100bp shock | NII +5.9%; EVE −4.4% | Directly reproduced at Q2 Item3 pp88–89 after the supplement. Hedges are already included in the model; do not add a second hedge offset. |
| Deposit model assumptions | Average non-term NII beta53%; ECR beta70%; all non-maturity/ECR weighted beta59% | Directly verified at Q2 Item3;70%/59% include mortgage-warehouse ECRs reducing interest income. Different populations/definitions; do not substitute one beta for another. |

Sources: [Q2 deck, slides7–11,14,17](https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/walq22026earningspresent.htm), [Q2 release, average balances and earnings-credit classification](https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/pressrelease-6302026.htm), [Q2 10-Q locator](https://www.sec.gov/Archives/edgar/data/1212545/000162828026051418/wal-20260630.htm), [Q1 original filing](https://www.sec.gov/Archives/edgar/data/1212545/000162828026033054/wal-20260331.htm). Existing owner study: `../WAL/research/2026-09-28_preprint-inputs-rates-consensus-short-interest.md`.

## Securities and hedges

NII measures income earned over a future period. EVE measures the present value of estimated whole-balance-sheet cash flows, including liabilities and off-balance-sheet items. AOCI records specific accounting marks. AFS marks, EVE percentage changes and NII percentage changes cannot be added as loss estimates. No disclosed EVE dollar base was obtained, so applying −4.4% to GAAP tangible equity would invent a denominator.

Direct Q2 Note2 inspection verifies parent AFS fair value$18,880M against$19,547M amortized cost: a$667M existing pretax gap ($686M gross losses less$19M gains). HTM gross amortized cost$1,676M versus$1,497M fair value gives a$179M gap; net carrying value$1,662M after$13.8M allowance gives a$165M gap at printed precision. These bases must remain distinct when comparing the bank-level cohort. The release independently confirms parent AOCI−$451M, TCE net of intangible tax$6,906M and TBV$63.24. Existing AFS loss recognition is already in equity.

**June composition verified:** AFS fair value comprises CLOs$3,221M, agency commercial MBS$514M, corporate debt$222M, private-label residential MBS$1,136M, agency residential MBS$7,428M, tax-exempt$794M, Treasuries$5,494M and other$71M. MBS totals$9,078M/48.1% of AFS. HTM cost consists of tax-exempt$1,517M and private-label residential MBS$159M. Security labels, floating coupons and optionality prevent treating this as one fixed Treasury bond.

**June hedges verified:** Q2 Note12 shows pay-fixed/receive-variable asset swaps and opposite-direction debt swaps. Hedged AFS amortized cost is$3,482M with−$73M cumulative basis adjustment,17.8% of total AFS cost. Aggregate designated fair-value interest-rate notional$5,706M spans loans, securities and debt; neither figure is net duration/DV01 coverage. Q2 AFS swap gains$33.0M offset hedged-item losses$31.9M, net+$1.1M already in interest income, excluding any interpretation as complete swap carry/portfolio return. Customer back-to-back and mortgage/MSR derivatives are separate. H1's cited$1.3B Treasury swap termination occurred in Q1, with no Q2 termination; do not carry sold/terminated positions as current protection.

**Still unavailable:** measured effective securities duration, full security/hedge tenors and key-rate schedules, and September30 positions. Full-text duration hits concern mortgage derivatives and litigation; no measured securities duration was obtained in the reviewed Q2 sections. Contractual maturity buckets cannot fill this gap. Selected benchmark risk is demonstrably hedged, while protection against curve shape, credit spreads, prepayments and basis remains incomplete or unquantified.

The earlier$382–636M after-tax WAL sensitivity used the **bank's** June30 AFS book, assumed duration3–5years, a90bp parallel shock and25% tax relief. It remains a diagnostic, not a measured loss estimate. On the rounded **parent** AFS value the same assumptions give$382.32–637.20M. That arithmetic does not improve the missing duration/hedge inputs. The Q3 Treasury move was nonparallel; the actual loan/deposit index paths are not represented by a single5Y yield change.

## Funding pressure and resilience

| June30 or Q2 evidence | Pressure | Resilience and qualification |
|---|---|---|
| Parent deposits$81,874M, down$849M QoQ; NIB$27,820M, down$258M | Deposits fell while HFI loans grew$1,807M; borrowings rose$626M to$6,236M. | Release attributes the decline to deliberate higher-cost deposit optimization. NIB share remained34.0%; total deposits still grew$10,767M YoY. Neither the attribution nor these aggregates identifies every depositor's behavior. |
| IB deposit cost2.74%, down1bp; average total interest cost of deposits1.78%; NIM3.53% | Interest cost alone omits other funding costs. | Securities yield rose5bp to4.64%; NII increased$30.6M to$796.9M. These are realized Q2 results, rather than proof of Q3 resilience. |
| Average ECR-related balances$31.6B; period-end$29.9B | A large funding block carries credits/referral costs; NIB is not necessarily free funding. | Q2 optimization can remove expensive balances without creating a run. Its Q3 economics and residual customer balances remain unknown. |
| Earnings-credit/referral costs$234.2M vs$214.3M Q1 | Includes$52.5M reducing interest income,$8.4M reducing fees and$173.3M in deposit costs. | The$52.5M is already in NII. Do not subtract the entire$234.2M from reported NII again. Other deposit-related costs add$5.9M to the$173.3M expense subtotal, reaching the$179.2M deposit-expense line. |
| Frozen bank-level funding cohort: uninsured38.1%, brokered18.8%, reciprocal$15.16B, FHLB$5.80B | Funding composition merits attention; FHLB rose$0.60B QoQ. | These are existing June30 regulatory bases, not newly fetched data or additive independent risk buckets. Named FHLB balances establish borrowing, not purpose or remaining capacity. No observed Q3 deposit flight is established. |

The separate accounting cost channels matter. The Q1→Q2 increase in earnings-credit/referral costs was$19.9M;$3.8M of it already reduced NII. Subtracting only the$16.1M increase outside NII from the$30.6M NII increase leaves$14.5M before other operating changes. This is an explanatory identity, not a replacement PPNR measure. Actual Q2 PPNR was$412.4M, up$18.4M versus Q1 excluding its$50.5M securities-sale gain.

WAL's reported September16 plan to move about$4B of deposits off balance sheet, including about$2.5B in Q3, is secondary transcript evidence awaiting original webcast verification. The primary Q2 deck independently confirms the optimization strategy and reduced deposit-growth outlook. Q3 should identify moved balances, associated asset movement, fees/credits forgone and replacement funding. A smaller deposit balance can be favorable if it removes low-return funding and related assets; expensive replacement without sufficient asset benefit would cut the favorable NII/EaR result.

**June liquidity verified at Q2 p86:** FHLB capacity$14,006M less$5,800M advances and$1,869M letters of credit leaves$6,337M available; FRB credit$18,362M is undrawn. Warehouse capacity$2,050M is undrawn and uncommitted. Management identifies$23.1B liquid assets ($4.8B FRB cash plus$18.3B unencumbered securities). These are issuer-disclosed June conditions, not September operational capacity. Do not add the assets and borrowing capacities without confirming collateral overlap, haircuts and access. Negative securities marks can reduce usable collateral even when CET1 excludes AOCI. Weekly H.8 borrowers remain unnamed.

**Funding definition gap retained:** Q2 p82 reciprocal deposits$15.2B differ from p87 CDARS$2.1B plus ICS$11.8B=$13.9B. No reconciliation was obtained. Preserve the existing bank-regulatory reciprocal total and record the named-program subtotal separately; do not silently replace it. The interest-cost1.78% uses Q2 averages, whereas the filing's H1 value1.80% covers a different interval.

## Parent earnings and tangible equity bridge

Use the parent's$6,906M June30 TCE as the opening stock. Add actual subsequent income available to common shareholders, subtract common dividends and repurchases, add the **change** in parent AOCI and other common-equity movements, then reconcile intangibles and related taxes. Divide by the actual ending share count. Future earnings already include the relevant funding costs, realized hedge/security results and new provisions; adding them again would double-count.

The Q2 equity statement now completes the common-equity flow at printed$0.1M precision: common income$258.5M − common dividends$45.9M − repurchases$2.3M + grants$13.1M − stock withholding$0.5M + OCI$4.3M = +$227.2M. Preferred and noncontrolling balances are unchanged. The rounded TCE bridge is$6,677M +$227.2M + about$2M net-intangible/tax change ≈$6,906M. Thus$16.9M of the earlier$18.7M residual is explained by grants/withholding/OCI; the rest is the rounded intangible/tax movement. No unrounded precision or Q3 retention forecast is implied. A quarterly after-tax mark above that historical$210.3M flow could overwhelm it under fixed-flow assumptions, even with positive earnings. Conversely, effective hedges and durable earnings could offset a smaller mark.

Keep CET1 separate. The parent release reports$7,267M CET1 and11.0%; the frozen bank cohort reports$7,651.672M and11.58%. Those are different legal entities. Its opted-out bank AFS mark is not an automatic CET1 deduction. Realization, retained earnings, deductions and RWA require their own matched bridge. No precise Q3 parent capital ratio or earnings offset can be estimated from the available sensitivities. Cantor residuals/protective liens stay within the existing loan/classified totals; no new allowance or exposure is added here.

## What could change the investment case

**Most consequential unknown:** whether optimization and asset repricing preserve earnings after **all** deposit costs and mortgage revenue, while the securities book incurs its actual mark. AOCI weakness alone confirms book-value pressure, but does not establish funding distress or mispricing. Favorable NII alone does not establish resilient overall earnings.

The next existing disclosure is **Monday October19 after close**, WAL's Q3 release/deck, followed by the **Tuesday October20 noon ET** call (date already primary-verified by the WAL desk, KB-WAL-217). Read NII/NIM, interest deposit costs, the three earnings-credit/referral cost lines, ECR balances, funding-remix reconciliation, cash/borrowings, AOCI/TBV, payouts, new credit expense and guidance together. A disclosed explanation of cash versus deposit movements could distinguish optimization from unwanted replacement borrowing.

The later Q3 10-Q supplies securities composition/marks, hedge designation and amounts, collateral capacity, AOCI/equity roll-forwards and the revised Item3 model. Actual filing date is unknown; existing owner window/deadline remains unchanged. November7 bank-level retrieval checks completeness and funding/capital bases. Nothing here rewrites WAL's existing N1–N4 or WQ318 conditions: the frozen observation lines still grade as written, and these findings explain them.

| Result in those disclosures | Implication |
|---|---|
| Limited net marks, durable adjusted operating earnings and an explained optimization with usable liquidity | Weakens a joint rates-plus-funding bear mechanism. |
| Large net marks plus hotter all-in deposit costs, adverse EaR/guidance changes or expensive replacement funding beyond the explained optimization | Strengthens the joint mechanism; then quantify loss/earnings/capital relative to expectations. |
| Lower TBV but resilient earnings/funding | Book pressure with earnings resilience; revalue sustainable returns rather than declaring a funding crisis. |
| Missing optimization or hedge reconciliation | Keep attribution and net exposure UNKNOWN; silence does not establish either branch. |

**Investment judgment:** mixed and bounded. The issuer's nearly neutral broader earnings model and Q2 cost/earnings results weaken the claim that higher rates necessarily damage both equity and earnings. Securities and funding composition preserve a plausible pressure channel. Current comparable consensus, actual marks and a sustainable parent earnings valuation are insufficient to establish a pricing edge. No TERRY construction recommendation follows.

**Where further work stands:** June primary verification is now complete for the stated model, composition, selected hedges, disclosed capacity and common-equity flows. The source gap closed when WAL supplied its original download; direct inspection agrees with its supplement. Public disclosures still lack the effective duration and proprietary model inputs needed to forecast the net September mark. Actual Q3 positions and deposit-remix economics await the scheduled disclosure. No repeated June or peer/funding sweep is warranted; this focused pass stops here.
