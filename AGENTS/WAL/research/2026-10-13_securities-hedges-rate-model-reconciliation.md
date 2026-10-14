# WAL securities, hedges and rate-model reconciliation

**As-of:** October 13, 2026, evening ET. **Owner:** WAL. **Authority:** Will's direct assignment and steering; PROME assignment in REGINALD's October 13 inbox. **Scope:** specialist supplement to REGINALD's funding/peer work; no new prediction, monitor, grading rule, valuation or trade action.

**Assessment:** positive modeled net interest income (NII) and negative economic value of equity (EVE) are compatible. WAL can earn more over the next year while the present value of its longer-lived assets falls relative to liabilities. The June 30 model already includes hedges. The stronger claim that rising rates necessarily weaken both sustainable earnings and equity is unsupported: the same +100bp ramp gives NII **+3.2%** but broader pretax earnings-at-risk (EaR) only **+0.8%**. Conversely, positive NII does not immunize tangible equity or establish funding resilience. [Q2 10-Q Item 3 pp.88–89; Q2 deck slide 11]

**Source recovery:** fresh direct SEC retrieval succeeded after sandbox DNS failure and an approved network retry. Full filing identity verified: `wal-20260630.htm`, accession **0001628280-26-051418**, quarter June 30, filed July 31. Relevant tables/sections were read, not a fresh full-filing review. Saved factual extracts and reproducibility receipt: `sources/2026-10-13_Q2_rate-securities-hedges_extract.md` and `sources/2026-10-13_rate-reconciliation_receipt.json`. Raw HTML retained locally in gitignored `sources/q2_2026/`. Original September 28 table is reused and independently reproduced. [SEC retrieval October 13]

## 1. Reconciliation with REGINALD

Read before overlapping research: `AGENTS/REGINALD/reports/2026-10-13_WAL_rate-funding-reconciliation.md`, its source receipt, scope-clarification packet, and PROME's assignment. REGINALD's report was an actively staged working artifact when read; findings here are a coordinated supplement, not independent blind convergence. Funding composition, peer comparisons, WQ-318 baseline and bank cohort remain REGINALD-owned.

| Item | Reconciliation / disposition |
|---|---|
| NII shock +5.9%, ramp +3.2%, EVE shock −4.4% at +100bp | **AGREE; now freshly verified** in the Q2 primary. REGINALD's retrieval gap is closed for these cells. |
| Broader EaR +0.8% under the +100bp ramp | **AGREE; independently verified** at SEC deck slide 11. NII and EaR percentages have different bases; their difference is not a dollar cost. |
| ECR/referral costs across three income-statement lines | **AGREE; verified** at Q2 10-Q p.83. The $52.5M interest-income reduction is already in NII. Do not subtract all $234.2M again. |
| Detailed hedge figures were March 31 historical evidence | **No disagreement with its vintage label.** Add June 30: AFS hedged amortized cost $3,482M; cumulative basis adjustment −$73M; aggregate designated interest-rate notional $5,706M. The March −$41M/$5,708M cells are not June figures. |
| Security composition and collateral headroom unverified at June 30 | **New primary evidence supplied below.** Effective duration and September positions remain unavailable; June disclosed capacity is not an independently stress-tested liquidity total. |
| Generic assumed duration 3–5 years / 90bp mark range | Keep labeled **ASSUMED diagnostic**. Neither maturity buckets nor aggregate hedge notional turns it into net measured duration. Do not tighten its range by a notional-based subtraction. |
| My September 28 inference linked EVE closely to AOCI and scaled +100bp ramp to a 25bp Fed move | **Qualification owed by WAL.** EVE is whole-balance-sheet value, not the AOCI channel alone. A Fed move on one date is not a 12-month parallel ramp; a move embedded in the forward-curve baseline is not an incremental surprise. Dated qualification appended to the original research; numbers and frozen tests preserved. |

Source: REGINALD owner artifact read October 13; Q2 primary as specified in each section. Packet asks REGINALD to integrate the June source supplement and identify any remaining source disagreement; its receipt/consumption is not assumed.

## 2. What the models measure

| Measure | Verified June 30 result | Horizon / perimeter / caveat |
|---|---|---|
| Dynamic NII, instantaneous sustained parallel shock | −200bp: −8.6%; −100: −5.2%; +100: +5.9%; +200: +11.8% | Next 12 months versus forward-curve base; variable loans reset on their contractual indexes with caps/floors; assumed prepayments and balance-sheet seasonality. |
| Dynamic NII, gradual parallel ramp over 12 months | −200bp: −5.1%; −100: −2.7%; +100: +3.2%; +200: +6.3% | Gradual timing explains why the +100bp benefit is below the shock result. Neither is a Q3 forecast. |
| Broader EaR, ±100bp ramp | +0.8% in each direction | Pretax NII plus specified rate-sensitive non-interest income/expense, including mortgage and deposit costs; not GAAP EPS, and not a symmetric NII response. |
| EVE, instantaneous sustained parallel shock | −200bp: +4.4%; −100: +2.7%; +100: −4.4%; +200: −10.5% | NPV of estimated asset, liability and off-balance-sheet cash flows; uses non-maturity deposit terminal-life/attrition assumptions. No disclosed base EVE dollar amount obtained. |

[Q2 10-Q Item 3 pp.88–89; deck slide 11, independently read October 13]

**Why opposite signs are possible:** floating assets and pay-fixed/receive-floating asset swaps can lift near-term income when short rates rise. Longer-dated fixed cash flows can still lose present value, and the modeled change in liability value need not offset them. Accounting is a third object: AFS residual unrealized marks enter AOCI, fair-value hedge benchmark changes enter earnings with offsetting hedge results, and ordinary HTM market marks do not automatically reduce GAAP equity. EVE includes more than securities and supplies no accounting-equity conversion. **Do not apply −4.4% to tangible common equity or add EVE, AFS marks and NII percentages.** [Q2 Notes 2/12; Item 3; specialist inference from those definitions]

Item 3 explicitly says hedges' NII/EVE effects are incorporated in the model. A second hedge offset applied to the published sensitivities would double-count. The issuer reports exposures within its limits, but does not supply enough limit values/model inputs to independently test the risk appetite or reproduce its ALM engine. [Q2 Item 3 pp.88–89]

## 3. Securities actually disclosed at June 30

Parent consolidated basis, **$M**; these are not REGINALD's bank-cohort cells. [Q2 Note 2 p.13, balance sheet p.5]

| AFS type | Amortized cost | Fair value | Net fair value less cost |
|---|---:|---:|---:|
| CLO | 3,218 | 3,221 | +3 |
| Agency/GSE commercial MBS | 523 | 514 | −9 |
| Corporate debt | 229 | 222 | −7 |
| Private-label residential MBS | 1,289 | 1,136 | −153 |
| Agency/GSE residential MBS | 7,767 | 7,428 | −339 |
| Tax-exempt | 860 | 794 | −66 |
| U.S. Treasuries | 5,583 | 5,494 | −89 |
| Other | 78 | 71 | −7 |
| **Total** | **19,547** | **18,880** | **−667** |

Gross unrealized losses **$686M**, gross gains **$19M**; their net is the $667M existing pretax gap. It is not a new Q3 loss. MBS fair value **$9,078M**, **48.1%** of AFS; CLOs **17.1%**, Treasuries **29.1%**. Product labels alone do not reveal each security's coupon/reset timetable or effective duration. [Note 2; ratios derived October 13]

HTM gross amortized cost **$1,676M**, fair value **$1,497M**, net valuation gap **$179M**; net balance-sheet carrying amount **$1,662M** after **$13.8M** ACL, so the net carrying gap is **$165M** at printed whole-million precision. HTM consists of tax-exempt cost **$1,517M** and private-label residential MBS **$159M**. Do not call $165M the gross cost/fair-value gap. [Q2 Note 2; balance sheet]

**Measured effective duration: NOT DISCLOSED in the reviewed Q2 securities, hedges, MD&A investment and market-risk sections; full-text “duration” hits concern mortgage derivatives and litigation.** Note 2 p.17 gives contractual maturities, including AFS cost **$7,187M** after ten years plus **$9,579M** MBS presented separately. Those sum to **85.8%** of AFS cost, but are not a duration estimate: prepayment, floating coupons, optionality and hedge allocation matter. Securities hedge tenors, key-rate sensitivities, convexity and full portfolio coupon split were not obtained. **No replacement duration or net mark forecast is invented.** [Q2 Note 2 p.17; full-text search October 13]

## 4. Hedges: coverage and accounting, not blanket protection

| June 30 disclosure | What it establishes | What it does not establish |
|---|---|---|
| AFS hedged amortized-cost basis **$3,482M**, cumulative adjustment **−$73M**, included in that basis | Selected AFS benchmark exposure has fair-value hedges. Basis is **17.8%** of total AFS cost, a comparison of matched carrying bases. | Not 17.8% of DV01, not the securities-only swap notional, and not a uniform reduction to the whole book's mark. |
| Loans hedged carrying basis **$1,798M**, adjustment **−$42M**; qualifying debt **−$396M**, adjustment **+$8M** | Hedges span assets and liabilities with different directions. | Aggregate designated notional **$5,706M** cannot all be allocated to AFS. |
| Asset swaps receive variable SOFR plus adjustment and pay fixed; debt swaps receive fixed/pay variable | Selected assets are economically converted toward floating; debt hedges have the opposite cash-flow direction. | No proof of complete protection against yield-curve shape, spread widening, prepayments, basis or counterparty/collateral demands. |
| Q2 AFS swap gains **$33.0M**, hedged-item losses **$31.9M** in interest income | Net **+$1.1M** for these reported fair-value changes; benchmark-offset accounting is visible. | Not the complete swap coupon carry, not a net portfolio total return, and not an extra offset to add to already-reported NII. |
| **$1.3B** AFS Treasury swaps terminated in H1 with securities sold; **none terminated in Q2** | The major cited Treasury hedge termination occurred in Q1. H1 securities termination gains **$18.7M** are already included in the reported sale gains. | Do not carry terminated hedges as current coverage or add their gains to the security-sale total. |
| **$2.0B** loan portfolio-layer swaps terminated in H1, none Q2; **$1.5B** designated layer remains | Hedge composition changed despite relatively stable total notional since March; discontinued loan basis continues amortizing. | Cannot infer the economic hedge coverage change from aggregate notional alone. |
| Nondesignated forward, futures, locks and customer swaps | Mortgage/MSR and customer economic hedges are separate. Collateral pledged for derivatives **$261M** at June 30. | Large gross notionals are not spare securities protection; collateral posted is a stock, not unused capacity. |

[Q2 Note 12 pp.41–45; 17.8% ratio derived from $3,482M/$19,547M]

**Two-sided inference:** selected benchmark risk is demonstrably hedged, weakening a wholly unhedged fixed-bond story. Yet most AFS cost is outside this disclosed hedged carrying amount, and net duration remains unknown. Fair-value accounting offsets only designated risk; a hedge does not guarantee a smaller net AOCI loss under every shock. This qualifies the September 24 non-gating frame annotation's unconditional wording that hedged AFS makes the mark smaller; **the annotation and all frozen grading rules are left intact**, with this research as the current interpretive caveat.

## 5. Assumption tests and falsifiers

This is a public-disclosure diagnostic, not a reproduction or recalibration of the issuer's proprietary model. No observed assumption breach is asserted. [Q2 Item 3/deck slide 11; WAL calculations October 13]

| Test | Result now | Existing disclosure that can resolve it |
|---|---|---|
| **Deposit repricing:** NII non-term beta product range 45–86%, mean 53%; EaR ECR 70%, weighted non-maturity/ECR 59% | Definitions reproduced. These are distinct populations; do not replace one with another. Lower Q2 versus Q1 assumptions are favorable inputs, not measured causal evidence of cheaper future deposits. | Q3 release costs/credits and call explanation; later Item 3 revised product/ECR betas. A single quarter cannot identify beta without matched market-rate path, timing and product mix. |
| **Higher pass-through:** extra 10 percentage points of beta on a constant **$54,184M Q2-average IB deposit balance**, +100bp rate increase | Static extra annual interest cost **$54.184M** under an immediate shock; **$27.092M** over a linear one-year ramp (average shock 50bp). Additional 20 points doubles those figures. This isolates pricing, excludes volume changes and is not applied to the issuer's 53% mean, whose population differs. | REGINALD's funding remix baseline; Q3 average/ending deposits, product costs, replacement borrowings and repricing lag. Forward modeled NII base **N0 is undisclosed**; exact breakeven beta cannot be solved. |
| **ECR sensitivity:** constant Q2-average **$31.6B** credit/referral-related balances, additional 10 points of beta | **$31.6M** annual extra cost for a +100bp shock, **$15.8M** for a linear ramp, under uniform repricing assumptions. This block may overlap IB deposits; **do not sum with the preceding perturbation** or assign all costs outside NII. | Q3 three accounting cost lines, average ECR balances and revised ECR beta. [Q2 release average ECR balance; REGINALD source verification] |
| **SOFR/Fed Funds basis and curve shape:** deck says 67% of earning assets variable, 53% reprice to SOFR; variable liabilities equal 87% of earning assets, primarily modeled to Fed Funds | A short-rate rise need not match a long-end rise. SOFR/Fed Funds divergence or different reset lags can narrow expected asset/liability repricing benefit. Public data do not identify a net hedge-adjusted basis DV01. | Q3 loan yields, deposit/borrowing costs, asset mix and Item 3; market paths alone cannot identify WAL's realized exposure. |
| **Nonlinearity and timing** | At +200bp EVE falls 10.5%, versus 8.8% if the +100bp loss were doubled; marginal second 100bp costs another 6.1pp. Downside NII is asymmetric too. Neither a 25bp Fed step nor a nonparallel 90bp long-rate move can simply be read off these rows. | Q3 actual marks/model and balance-sheet changes. Do not extrapolate linearly outside disclosed scenarios. |
| **Dynamic growth/optimization** | Exact growth, reinvestment and optimization inputs not disclosed. If lower-cost asset runoff accompanies moved deposits, lower deposit totals may improve economics; retained assets financed at higher all-in cost could erode them. | REGINALD owns this test. Existing print/call then 10-Q: moved deposits and assets, retained customer/fee economics, replacement amount/rate, cash and usable collateral. |
| **EVE deposit duration and asset prepayments** | Assumed non-maturity terminal lives, attrition, pricing and prepayments are stated; numerical schedules unavailable. Faster deposit attrition or changed MBS cash flows can alter EVE even if near-term NII remains positive. | Q3 Note 2/12/Item 3, named model changes; absence leaves net duration UNKNOWN. |
| **Mortgage and credit effects** | EaR partly addresses mortgage/servicing costs; NII simulation explicitly excludes secondary credit deterioration. A rate-beneficial NII path can coexist with weaker pretax income after provisions. | Existing Q3 mortgage fee/valuation lines and credit grading frames. Count provision once inside earnings, not again in equity. |

**Algebraic boundary:** under a fixed matched deposit population D and incremental beta Δβ, shock benefit becomes `0.059 × N0 − D × 0.01 × Δβ`; a linear ramp becomes `0.032 × N0 − D × 0.005 × Δβ`. This is only a first-order single-variable diagnostic; N0 and the issuer's matched modeled D are unavailable, so no break-even beta or percentage reduction of the published sensitivity is claimed. The reported Q2 NII ×4 is not substituted for the forward dynamic base.

## 6. Source supplement for REGINALD's funding baseline

June 30 10-Q pp.34/86–87 newly resolves the report's historical-headroom gap: **FHLB capacity $14,006M − advances $5,800M − letters of credit $1,869M = available credit $6,337M**; **FRB $18,362M**, undrawn; warehouse lines **$2,050M**, undrawn and uncommitted. FHLB short/long-term advances use the same collateral pools. Management reports **$23.1B** liquid assets: FRB cash **$4.8B** plus securities **$18.3B** not then encumbered. [Q2 Note 8 pp.34–35; Liquidity p.86]

These are issuer-disclosed June conditions, not September headroom or independently tested operational access. **Do not add cash, unpledged securities, FHLB, FRB and warehouse amounts into a stress buffer without collateral/haircut/access reconciliation.** Parent-only liquidity runway is management's **over-12-month** analysis assuming no subsidiary dividends, no new debt/equity and no stockholder dividends; it is not the bank's cash balance. REGINALD owns integration and any matched liquidity total. [Q2 pp.86–87]

The Q2 10-Q confirms its **1.78%** total-deposit interest cost on **$83,535M Q2-average deposits**, versus **1.80% on $82,092M H1 averages**. This is an interval distinction, not disagreement. The filing gives reciprocal deposits **$15.2B** in MD&A p.82, but named CDARS **$2.1B** + ICS **$11.8B** on p.87 sum to **$13.9B**. The filing supplies no reconciliation of that $1.3B difference in the reviewed sections. Preserve REGINALD's bank-regulatory reciprocal figure; do not silently replace it with the named-program subtotal. [Q2 pp.82/87]

## 7. Parent common-equity bridge and two-sided conclusion

June parent AOCI is **−$451.2M**, including AFS **−$447.5M**. Q2 total OCI was **+$4.3M**, including AFS net **+$5.2M** after **−$0.7M** sale-gain reclassification. H1 total OCI was **−$107.0M**. Existing AFS marks are already in the opening equity stock; realized gains/losses require matched AOCI reclassification. [Q2 Note 11 p.40]

**Q2 common-equity flow tie-out at printed $0.1M precision:** common income **$258.5M − $45.9M dividends − $2.3M buybacks + $13.1M stock grants − $0.5M withheld stock + $4.3M OCI = +$227.2M**. The parent total-equity statement rises **$7,908.1M → $8,135.3M**, also $227.2M, with preferred and noncontrolling balances unchanged. This explains **$16.9M** of REGINALD's $18.7M difference between $210.3M retention and the rounded TCE rise. Rounded intangibles/tax adjustment contributes about another **$2M**: **$6,677M + $227.2M + ($646M−$644M) + ($3M−$3M) ≈ $6,906M**, within rounding. Exact unrounded TCE adjustments are not claimed. [Q2 equity statement p.8; Q2 release non-GAAP TCE table, Q1 comparison; REGINALD October 13 report]

**Forward bridge:** June TCE **$6,906M** + subsequent income available to common − common dividends/repurchases + change in AOCI + other common-equity movements − change in net intangibles + change in related tax adjustment. Divide by actual ending common shares. Q3 funding costs, hedge/security realized results and incremental credit provision enter through income; never add them again. CET1 stays separately matched by legal entity, regulatory deductions and RWA; EVE is neither GAAP capital nor CET1. No precise Q3 equity/capital forecast follows. [Q2 non-GAAP definition; Note 11/12; REGINALD capital-perimeter reconciliation]

| Evidence for pressure | Evidence for resilience |
|---|---|
| Existing AFS net loss $667M; HTM gross valuation gap $179M; EVE downside accelerates at +200bp. Large MBS exposure leaves prepayment/long-rate/spread risk, with net duration unknown. | Selected AFS benchmark risk has demonstrated hedge offsets; published whole-balance-sheet NII is asset-sensitive, and broader EaR is approximately neutral. |
| Higher all-in repricing, unfavorable remix or mortgage/credit expense could overwhelm the modest modeled broader earnings benefit. Q3 actual positions/optimization economics are not public yet. | Q2 common-equity growth was $227.2M after payouts; issuer disclosed June liquidity and borrowing capacity. Neither Q2 evidence nor reported deliberate optimization establishes deposit flight. |

**Most decision-changing unknown:** September 30 hedge-adjusted securities exposure and actual all-in deposit-remix economics together: does book-value pressure coexist with durable operating earnings, or does costly funding replacement join the marks? NII alone does not answer it. [WAL synthesis October 13]

**Resolver:** the already-announced **Monday October 19 after-close** release/deck and **Tuesday October 20 noon ET** call supply NII/NIM, three ECR/referral lines, mortgage revenue, optimization, funding changes, AOCI/TBV, credit expense and payouts. The subsequent Q3 10-Q supplies updated securities mix, hedge basis/notional, AOCI/equity, collateral and Item 3. Filing date remains unknown; existing 10-Q window/statutory backstop and all frozen N1–N4/credit tests stand. [KB-WAL-217 issuer date verification October 9; owner frames]

**Obtainable now:** June primary verification is completed; no repeat funding/peer sweep is warranted. Public June disclosures do not supply the duration/model inputs needed for a net September mark. **Wait for the existing Q3 disclosures for those inputs.** Current consensus/expectations and a net loss-versus-earnings valuation sufficient to demonstrate a pricing edge have not been established; no TERRY construction recommendation or trade execution follows. Frozen frames and prediction grades are unchanged.
