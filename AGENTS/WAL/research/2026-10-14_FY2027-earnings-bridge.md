# WAL FY2027 earnings bridge — October 14, 2026

**Result:** roughly $11 sustainable annual EPS needs about **$67M more pretax earnings per quarter** than a conservative Q2 gain screen. Roughly $8 needs about **$33M less** than that screen. Both paths have attainable arithmetic; neither is established by current operating evidence. No demonstrated expectations gap yet. These are WAL conditional component mixes, not a retrieved analyst model, issuer FY2027 guidance, or Q3 forecast.

Authority: Will's authorization to work on the proposed follow-ups. Reuse the completed October13 hedge study, September28 rate analysis and REGINALD's integrated funding report (31c02fd74); funding/peer ownership remains REGINALD's. The October13 quote/consensus snapshot retains its original date and EPS-basis/update-date gaps. Vendor FY2027 EPS was 11.04928 (Yahoo,13 analysts) /10.99 (Nasdaq,10); no matched analyst component forecast obtained. Frozen frames, canonical valuation probabilities/targets and predictions are unchanged.

## Starting earnings and quality screen

Directly read Q2 10-Q income statement and Note13 EPS, accession0001628280-26-051418, filed July31. All operating amounts below are **USD millions per quarter**. Source extract and numerical receipt: `../sources/followup_2026-10-13/Q2_earnings_primary_extract.md`, `earnings_bridge_2026-10-14.json`; reproducible with repo `.venv/bin/python3 AGENTS/WAL/scripts/earnings_bridge_20261014.py`.

| Item | Q2 reported | Q2 gain screen | Conditional $11 support | Conditional $8 pressure |
|---|---:|---:|---:|---:|
| Net interest income, already net of interest credits | 796.9 | 796.9 | 876.9 | 781.9 |
| Non-interest income, already net of fee credits | 198.8 | 183.0 | 193.0 | 183.0 |
| Operating expense excluding deposit costs | 404.1 | 404.1 | 424.1 | 412.1 |
| Deposit-cost expense | 179.2 | 179.2 | 176.2 | 184.2 |
| PPNR | 412.4 | 396.6 | 469.6 | 368.6 |
| Provision | 80.4 | 80.4 | 86.0 | 85.4 |
| Pretax income | 332.0 | 316.2 | 383.6 | 283.2 |
| Annual EPS under the common assumptions below | 9.46 | 8.98 | 11.00 | 7.99 |

**Common assumptions:** 19% tax; quarterly deductions7.1 NCI +3.2 preferred dividends +3.3 participating stock awards;108M diluted shares; four identical quarters. Formula: `4 × [pretax × 0.81 − 13.6] /108`. Actual Q2 tax was63.2 and ordinary earnings255.2, giving reported diluted EPS2.36, or9.44 from annualizing the rounded EPS. The19% approximation/rounding explain the small difference; the model is not a restatement of GAAP EPS. Future tax, NCI, participating awards, shares, seasonality and transition timing are unknown.

The screen removes **3.0 securities-sale gain +12.8 net fair-value gain adjustments**, rather than assuming they recur indefinitely. This is **not issuer adjusted EPS** and does not prove the gains are nonrecurring: derivatives/covered-call or mortgage economics may generate future gains and offsetting losses. It retains11.9 equity-investment income,10.8 BOLI and12.5 other income; removing equity income too gives annual EPS8.63. No legal-cost addback:32.8 legal/professional/director fees are not established as exceptional or ending. Fee and mortgage production are cyclical, and the aggregate screen is not all recurring income.

Q2 fee/mortgage lines:63.1 service fees,53.4 origination/sale,31.3 servicing. Evaluate future servicing valuation, hedging, origination margins, volume and servicing expense together. Higher GAAP revenue supported by favorable MSR/FV marks is weaker evidence of durable production growth than a disclosed volume/margin bridge, but cannot be dismissed automatically.

**No funding double count:** Q2 ECR/referral234.2 comprises52.5 reducing interest income,8.4 reducing fee income,173.3 in deposit expense. The179.2 deposit-cost line adds5.9 other costs. The first two are already in the NII and fees above. REGINALD owns whether actual deposit optimization/replacement funding improves these economics; this note does not subtract234.2 again or add the favorable rate sensitivity on top of an assumed NII improvement.

## What each path requires

**$11 support:** versus the screen, NII+80 (10.0%), fee/mortgage/other+10, ex-deposit expense+20, deposit-cost expense−3, provision+5.6. Net pretax improvement67.4. This demonstrates that benign credit plus moderate operating growth could support consensus without a miraculous reserve release. It does **not** establish feasibility. For scale,6% asset growth at constant earnings mix gives NII844.7; another32.2 quarterly NII is equivalent to approximately13.3bp additional annual net yield on a6%-larger Q2 average earning-asset base. This is a first-order diagnostic, not a reported NIM forecast; rates, tax-equivalent yields, mix and fees complicate the translation. Actual retained assets, spread and all-in replacement costs must substantiate it. The primary Q2 financial guide was FY2026, not a FY2027 EPS promise.

**$8 pressure:** NII−15, ex-deposit expense+8, deposit-cost expense+5, provision+5, fees flat gives pretax−33.0. Persistent moderate operating deterioration could reach this case without a new giant credit charge. Conversely, a single $33M provision in one quarter does not establish four-quarter persistence. Stable/improving NII after all three ECR lines, credible production fees and declining credit costs undermine this path.

The prior note's **~$102M quarterly recurring gap** was from future FY2027 consensus11.05 to8; it remains arithmetically correct. The new **~$33M** is from the current Q2 gain screen8.98 to8. Different starting points: a bearish case could combine **missing anticipated growth** with modest deterioration. No observed evidence presently measures the full forward shortfall.

| Sensitivity, holding everything else fixed | Effect |
|---|---:|
| $10M quarterly recurring pretax change | ~$0.30 annual EPS |
| $10M one-time new provision | ~$0.075 quarter EPS |
| Shares106M rather than108M at $11 target | Required pretax uplift falls from67.3 to60.5M/quarter |
| 10bp sustained net yield on fixed91,661M average earning assets | ~$0.69 annual EPS |

Buybacks help per-share earnings but use capital and cannot alone turn~9 into11 on these inputs. Securities AOCI does not mechanically enter EPS: use the already completed rate/hedge interpretation, not EVE as an income or TBV forecast. A$99M charge-off can consume existing allowance; only **incremental new provision** belongs in a new EPS expense bridge. If99M were entirely new provision, the approximate one-quarter EPS effect would be0.74, a hypothetical upper-scale calculation, not a measured expected charge.

## Evidence that decides

**Later October14 peer test consumed:** REGINALD's `../REGINALD/reports/2026-10-14_WAL_2027_earnings-path-test.md` (source commit423e52e6844f46cd73f02e3215c1fbf0bea0e852) adds a public-revenue reverse expense budget and stronger two-sided operating evidence. Its conditional budget and this component-mix bridge are complementary, not the same model: its vendor revenue differs from this gain-screened illustrative mix, while tax/share/deduction assumptions are comparable. WAL independently reproduced the sensitivity arithmetic and checked the decisive parent mortgage/MSR/ECR passages against the preserved primary filing. Review receipt → `2026-10-14_REGINALD-earnings-test-review.json`. Funding interpretations/figures remain REGINALD-owned. The parent mortgage result improved sequentially and the servicing valuation/hedge effects substantially offset; the narrower bank RC-P decline is not evidence of an aggregate parent mortgage decline. This narrows the proposed mortgage follow-up to remaining bank/parent classification, servicing residual/costs and persistence rather than rebuilding the completed Q1/Q2 component work. Borrower/loss attribution remains open. No demonstrated gap or model/score/weight/target/rule change.

**October14 FFIEC integration:** `2026-10-14_FFIEC-deep-read.md` and the expanded Q3 worksheet supply historical credit, mortgage and capital comparisons. June bank NDFI nonaccrual122.456M is a troubled-loan balance, not a new provision. Funded plus unused NDFI20696.307M is contractual face exposure, not expected loss. Bank mortgage income45.723M fell26.936M QoQ but rose5.27%YoY; neither that decline nor a bank/parent classification mismatch is established as recurring parent earnings drag. Bank CET1/RWA is a separate entity/basis from parent EPS/TCE. No new FFIEC balance is inserted into the component scenarios above without attributed losses, accounting reconciliation and evidence of persistence. The screen and conditional arithmetic are unchanged.

Use `2026-10-14_Q3-earnings-quality-credit-read.md` and its blank actuals worksheet at the existing October19 release/October20 call and later10-Q. Support for11 needs identifiable recurring NII/fee improvement after funding effects, contained recurring costs, sufficient capital retention and manageable credit. Support for8 needs a persistent weaker earnings guide/actual mechanism, not only a known AFS mark, quarterly appraisal charge or missing webcast. Credit cure, no explicitly identified new office migrations, a benign $99M appraisal and repeatable operating improvement materially weaken the bearish thesis.

**Judgment:** we now know which growth assumptions matter, but not what the market assigns to them. The October13 price73.73 at~6.7×vendorFY2027EPS already shows a discount. No component consensus, market required return, probability distribution or price-implied earnings path was identified. This conditional bridge supplies questions to test, not proof of mispricing. No target/weight/score change or trade construction referral.

Primary [Q2 SEC filing](https://www.sec.gov/Archives/edgar/data/1212545/000162828026051418/wal-20260630.htm); prior verified [Q2 guide slide17](https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/walq22026earningspresent.htm); REGINALD `reports/2026-10-13_WAL_rate-funding-reconciliation.md`; original October13 vendor receipt. Latest issuer guidance access result is documented separately below.
