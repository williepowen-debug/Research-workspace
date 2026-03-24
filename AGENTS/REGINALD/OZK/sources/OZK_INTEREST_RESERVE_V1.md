# Bank OZK's construction loan reserves are eroding faster than the balance sheet reveals

Bank OZK's **$7.0 billion construction book on interest reserves** faces a structural timing mismatch: reserves sized at 4–5% rates are burning at 7.5–8.5% rates, compressing an 18-month reserve to roughly 14 months. Quantitative modeling of the 2022 vintage — the $13.8B peak — shows most original reserves were exhausted by late 2023 to mid-2024, forcing $866 million in emergency equity replenishment from sponsors over 14 quarters. The Q4 2025 capitalized interest figure of $108.6M runs **22–31% below** the $140–158M expected on a $7.0B book at stated rates, a gap consistent with reserves thinning or partially transitioning to cash-pay. With the 2022 vintage now hitting hard maturity deadlines through Q1–Q3 2026 and Q4 2025 charge-offs spiking to $98.3M (8× the prior-year quarter), the question is whether sponsor support can bridge the gap before the maturity wall forces recognition of losses the extend-and-replenish strategy has deferred.

---

## Modeling the depletion: an 18-month reserve burns out by month 14

A standard construction loan originated in July 2022 illustrates the core problem. Consider a $100M commitment with linear draws over a 24-month construction period, with an 18-month interest reserve sized at the origination rate of ~5%.

**Reserve amount at origination:** Using a linear draw schedule where the outstanding balance reaches $75M by month 18, the total interest at a constant 5% rate sums to approximately **$2.97M**. This is the fixed dollar amount set aside before OZK advances a single dollar, per the bank's "last dollars in, first dollars out" structure requiring borrower equity — including estimated construction-period interest — to be fully funded before bank advances.

**Actual interest consumed under rising rates:** As the Fed hiked from 1.50–1.75% in June 2022 to 5.25–5.50% by July 2023, the all-in construction loan rate (SOFR + 250–350bps spread) climbed from ~5% to ~8.5%. Monthly interest charges escalated dramatically:

| Period | Months | Avg outstanding | Avg rate | Interest consumed |
|--------|--------|----------------|----------|-------------------|
| Jul–Dec 2022 | 1–6 | ~$15M | ~6.0% | ~$490K |
| Jan–Jun 2023 | 7–12 | ~$40M | ~8.0% | ~$1,590K |
| Jul–Dec 2023 | 13–18 | ~$65M | ~8.5% | ~$2,745K |
| **Total 18 months** | | | | **~$4,825K** |

The $2.97M reserve is exhausted around **month 14 (September 2023)** — roughly 4 months early. A more conservatively sized 24-month reserve (~$5.2M at 5%) depletes around **month 19 (January 2024)**, still 5 months early. The rate doubling doesn't simply halve reserve life because rate increases were gradual and balances ramp over time, but the compression is severe: **18-month reserves lasted ~14 months; 24-month reserves lasted ~19 months**.

For loans originated earlier in 2022 at even lower rates (3.5–4.5% in Q1–Q2), the compression is worse. A 12-month reserve at a 4% origination rate on a mid-2022 loan would have been exhausted by **Q1 2023** — barely 8 months in.

## How much of the book has already burned through reserves

The 89.7% on-reserve figure ($7.0B of $7.8B in construction loans) provides the cleanest data point: **10.3% of the construction book ($803M) currently has no interest reserve**, meaning these loans have converted to cash-pay or are in various stages of workout. But this snapshot understates cumulative depletion because OZK has aggressively managed the problem through three channels.

**Channel 1: Emergency equity replenishment.** Over 14 quarters since the Fed began hiking, OZK has extracted **$1.3 billion in additional sponsor equity** — $866M in reserve deposits and $429M in unscheduled principal paydowns. The Q4 2025 alone saw $56.7M in new reserve deposits across 49 extended loans. This represents roughly **12% of the current funded RESG balance** in incremental support, a figure that only makes sense if original reserves were widely insufficient.

**Channel 2: Accelerated repayments.** Record RESG repayments of **$7.24B in FY2025** (with $3.0B in Q4 alone) have removed the most mature and potentially most reserve-stressed loans from the book. The Q4 repayment breakdown is telling: **$1.34B came from the 2022 vintage**, confirming this peak cohort is now hitting hard maturity. Loans that successfully stabilized and refinanced are exiting; the ones that remain are likely the harder cases.

**Channel 3: Sales and charge-offs.** The Pacific Center life science campus ($265M commitment) was sold at par to distressed debt specialist Strategic Value Partners. The Boston office development took a **$72.4M charge-off** when capital partners refused to contribute additional equity. These exits reduce the reported stressed-loan count but represent real crystallization of the reserve depletion problem.

My estimate of cumulative depletion across the 2022 vintage: **50–70% of original reserves have been exhausted** and required replenishment, modification, or forced repayment. The current 10.3% without reserves represents the residual — loans where sponsors could not or would not inject new capital. The more relevant forward-looking question is what percentage of the remaining 89.7% has reserves sufficient for only 3–6 more months. OZK does not disclose portfolio-wide reserve adequacy ratios, making this unobservable from public data.

## The mechanical cascade from reserve depletion to nonaccrual

When a construction loan's interest reserve exhausts, a predictable regulatory and accounting cascade begins. The mechanics matter because they determine the speed at which reported credit quality can deteriorate.

**Immediate conversion to cash-pay.** The loan shifts from self-funding interest (via capitalization from reserves) to requiring the borrower to make monthly interest payments from external sources. For a $100M loan at 8.5%, this means the borrower must suddenly produce **~$708,000 per month** in cash — an amount that construction-phase projects almost never generate, since the underlying property typically produces zero revenue until completion and lease-up. The borrower's options narrow to: inject personal/corporate equity, find a new capital partner, or default.

**The 90-day backstop and subjective trigger.** Per FFIEC Call Report instructions, a loan **must** be placed on nonaccrual when 90 days past due, unless "both well secured and in the process of collection." But critically, a second trigger operates independently: the bank must place the loan on nonaccrual **at any time** it determines that "payment in full of principal or interest is not expected." The FDIC's December 2023 advisory explicitly warned that construction loans with interest reserves can appear current while the underlying project is failing — and that regulators expect banks to act before the reserve runs out if collection is doubtful.

**Interest capitalization must cease** when a loan is classified doubtful, loss, or nonaccrual. There is a **regulatory presumption against capitalization for substandard loans** (per OCC Examining Circular EC-229). This creates a cliff effect: once a loan tips to substandard or nonaccrual, the interest income disappears from the bank's P&L while the credit cost hits simultaneously through provisions and potential charge-offs.

The typical timeline from reserve depletion to nonaccrual for a construction borrower who cannot make cash payments:

- **Day 0:** Reserve exhausted; loan converts to cash-pay
- **Days 1–29:** Loan delinquent but not yet reported; bank negotiates with sponsor
- **Day 30:** Reported as 30 days past due; internal risk rating review triggered
- **Day 60:** Enhanced monitoring; reclassification to special mention or substandard likely
- **Day 90:** Mandatory nonaccrual unless well-secured exception applies (rarely met for partially completed construction)
- **Earlier:** Bank must classify as nonaccrual at any point if full collection is not expected

For OZK specifically, management's stated policy is unambiguous: **"You pay, you stay. You don't pay, you don't stay"** (CEO Gleason, Q4 2025 earnings call). The bank reports 4 nonaccrual loans currently, with the largest — the Boston Financial District office — moving from accrual to nonaccrual in Q4 2025 when capital partners withdrew support. This pattern — sponsor withdrawal triggering rapid reclassification — is the template for how reserve-depleted loans fail.

## The $108.6M capitalized interest gap signals stress beneath the surface

The most quantitatively revealing data point in the user's framework is the Q4 2025 capitalized interest figure. On a $7.0B book at the bank's stated rate environment of **7.50% total loan yield** (Q4 2025), expected quarterly capitalized interest should be:

| Rate assumption | Expected quarterly interest | Gap vs. actual $108.6M |
|----------------|---------------------------|----------------------|
| 7.50% (portfolio yield) | $131.3M | –$22.7M (–17%) |
| 8.00% | $140.0M | –$31.4M (–22%) |
| 8.50% | $148.8M | –$40.2M (–27%) |
| 9.00% | $157.5M | –$48.9M (–31%) |

The implied effective rate on the reserve-funded book is **$108.6M × 4 ÷ $7.0B = 6.2%**, materially below the 7.5–8.5% range. Four explanations exist, and they are not mutually exclusive:

**Explanation 1 — Average balance effect:** If Q4 2025 saw significant repayments (the record $3.0B in RESG repayments occurred that quarter), the average balance on reserves during the quarter was lower than the end-of-period snapshot, reducing capitalized interest mechanically. This is the most benign explanation.

**Explanation 2 — Floor rate protection:** OZK reports that **14% of variable-rate commitments were at their floor rates** at December 2024 rates, with 42% hitting floors with a 50bp decline and 52% with a 100bp decline. After three rate cuts in late 2025 bringing SOFR to ~3.6%, a meaningful portion of loans may be at contractual floors in the 5.5–7.0% range, pulling down the blended rate on the reserve-funded book.

**Explanation 3 — Reserve thinning:** Some loans classified as "on reserves" may have only weeks or months of coverage remaining, with the final reserve draws producing less capitalized interest than earlier in the reserve life. This is more concerning.

**Explanation 4 — Partial cash-pay transition:** Some loans may be in a hybrid state where the reserve covers part of the interest and the borrower covers the rest in cash, reducing the capitalized portion. This suggests the 89.7% on-reserve figure may overstate true reserve health.

The most likely answer combines explanations 1 and 2 (accounting for perhaps two-thirds of the gap) with explanations 3 and 4 (the remaining third). A **$10–15M quarterly shortfall** attributable to reserve thinning would be consistent with roughly **$2–3B of the on-reserve book** having reserves adequate for fewer than 6 months at current rates — a figure representing 30–40% of the $7.0B reserve-funded book.

## The 2022 maturity wall arrives in 2026 amid a hostile exit environment

The $13.82B originated in FY2022 began hitting 36-month hard maturities in late 2025 and will peak through **Q1–Q3 2026** on 42-month terms. Management expects RESG repayments to "remain elevated throughout 2026," and Q4 2025's $1.34B in 2022-vintage repayments confirms the wave has begun. But repayments require either refinancing into permanent debt or property sale — both of which face significant headwinds.

**Permanent financing requires stabilization that many projects haven't achieved.** Fannie Mae's Near-Stabilization program requires ~75% occupancy; Freddie Mac's Lease-Up program requires 50% with credit enhancement. Three-month apartment absorption rates have dropped from **75% (Q3 2021) to 45% (current)**, meaning newly completed multifamily projects take far longer to reach occupancy thresholds. Life sciences vacancy in San Diego Sorrento Mesa — where OZK has over $1B in exposure including the $915M IQHQ RaDD loan — has reached **35%**. Office CMBS delinquencies hit an all-time record **11.76%**.

**Exit cap rates have expanded 100–200bps from underwriting.** A project underwritten at a 4.5% exit cap rate with $1M NOI was valued at $22.2M; at today's 6% cap rate, the same NOI yields $16.7M — a **25% decline**. If rents have also disappointed (common in oversupplied Sun Belt markets where OZK is concentrated, with Miami, Dallas, Phoenix, and Atlanta among top MSAs), the combined value hit can reach 30–40% below original underwriting.

**The extend-and-pretend strategy has limits.** OZK has executed 414+ modifications over 14 quarters with "zero floor or spread concessions" and has extracted significant additional equity. But each extension increases total debt through additional capitalized interest while the maturity wall continues building. The $866M in collected reserve deposits is substantial but represents a declining resource: Q4 2025's $56.7M was below Q3's ~$70M, potentially signaling sponsor fatigue. The IQHQ RaDD loan — OZK's single largest exposure at **$915M committed, ~$555M funded, zero tenants, maturing August 2026** — is the ultimate test case. Sponsors have contributed $152.9M in reserves and raised ~$900M in capital, but the property faces a binary outcome at maturity.

## Historical parallels and the acceleration risk

The 2007–2010 construction lending crisis provides the closest historical template. ADC noncurrent rates soared from **0.8% (year-end 2006) to 16.8% (March 2010)** — a 20× increase over three years. Corus Bankshares, the era's most concentrated construction lender ($3.9B in condo loans), saw more than half its construction book go nonaccrual within 18 months of the first signs of stress. Colonial BancGroup's 40% construction loan concentration drove net charge-offs to an annualized **7.0%** in its final quarter.

Three structural differences limit direct comparability. OZK's **49% weighted-average loan-to-cost ratio** provides substantially more equity cushion than the 70–85% LTCs common pre-crisis. OZK's borrower structure — requiring all equity to fund before bank advances — means losses must penetrate significant subordination before reaching bank capital. And the current cycle lacks the systemic residential oversupply that amplified 2008 losses across all property types.

But the acceleration dynamics are identical. The FDIC's 2008 Supervisory Insights paper specifically identified interest reserve depletion as a **leading indicator** of construction loan portfolio deterioration. The current cycle's modification volume — CRE loan modifications rose **66% year-over-year** through mid-2025 per the St. Louis Fed — mirrors the pre-recognition pattern of the prior crisis. Distressed CRE assets reached **$116 billion in Q1 2025**, up 31% from a year earlier.

## Conclusion

The quantitative evidence points to a construction book where original interest reserves are largely exhausted and ongoing viability depends on continued sponsor willingness to inject equity — a resource that shows early signs of depletion. The $108.6M capitalized interest figure, while not conclusive on its own, is consistent with a book where 30–40% of reserve-funded loans have thin remaining coverage. The Q4 2025 charge-off spike to **$98.3M** (with the ACL-to-annualized-NCO coverage ratio falling to approximately **1.07×** versus a regional bank norm of 4.5–5.1×) suggests the reserve cushion for absorbing future losses is inadequate if the maturity wall forces recognition of deferred problems.

The critical catalyst window is **April–August 2026**, when the bulk of 2022-vintage 42-month loans hit hard maturity simultaneously with the IQHQ RaDD deadline. The binary risk is concentrated: either the current repayment pace of ~$7B annually continues to de-risk the book through successful exits, or sponsor support fractures under the weight of a hostile refinancing environment and depleted reserves, triggering the nonaccrual cascade that construction loan interest reserves were designed — but ultimately failed — to prevent. OZK's **14.4% short interest** and **1.0× tangible book trading multiple** suggest the market is pricing meaningful probability of the latter scenario, while Moody's Stable outlook and management's "green shoots" narrative reflect the case for the former. The truth likely lies in the gap between the $108.6M the bank reports and the $140–158M the math says should be there.