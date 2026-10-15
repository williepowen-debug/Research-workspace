# Ally Financial–Carvana Forward Flow Arrangement: Structure, Exposure, and Contagion Risk

## Executive Summary

The Ally-Carvana forward flow relationship is one of the most consequential bilateral arrangements in U.S. auto finance. Ally has purchased approximately $19 billion of Carvana-originated used auto loans since Carvana's 2017 IPO, representing 42% of Carvana's cumulative $46 billion in originations. As of Q3 2025, the commitment was upsized to $6 billion through October 2027. The arrangement is structured as a **true sale without recourse**—meaning Ally bears the credit risk outright after purchase—but the opacity of key contract terms (33 redacted metrics in SEC filings) and Ally's minimal public disclosure of Carvana-specific credit performance create significant analytical blind spots for investors in both companies.[^1][^2]

***

## 1. Structure: The Master Purchase and Sale Agreement (MPSA)

### How the Forward Flow Works

The arrangement operates under a **Second Amended and Restated Master Purchase and Sale Agreement** between Carvana Auto Receivables 2016-1 LLC (as Transferor), Ally Bank, and Ally Financial Inc. (as Purchasers). The original MPSA dates to December 2016, and has been amended at least ten times since, with five amendments in 2022-2023 alone.[^3][^4][^5]

The operational flow is as follows:

1. Carvana originates auto loans through its online platform (99% of applications approved within 2 minutes).[^3]
2. Each quarter, Carvana sends Ally a "tape" of loans it wants Ally to purchase under the forward flow commitment.[^6]
3. Ally examines the tape against its own internal "buy box" criteria and purchases qualifying receivables.[^6]
4. Bridgecrest Credit Company (owned by Ernest Garcia II, father of Carvana's CEO) retains servicing rights on the loans post-sale.[^4]

### Who Bears Credit Risk?

**Ally owns the loans outright after purchase.** Carvana's SEC filings explicitly state that it "completes loan sales **without recourse** for their post-sale performance and makes customary representations and warranties as part of each sale". This is a true-sale structure—once Ally purchases the receivables, Carvana has no obligation to repurchase or cover losses if borrowers default.[^7][^8]

However, the phrase "customary representations and warranties" is critical. While the specific reps and warranties are heavily redacted in public filings, they typically cover:

- Accuracy of loan data (borrower income, FICO, employment verification)
- Compliance with stated underwriting criteria
- Title perfection and lien status
- No fraud in origination

If loans were originated with materially inaccurate borrower data or did not meet the agreed eligibility criteria, Ally could theoretically demand repurchase under rep-and-warranty breach provisions. This is the standard remedy in forward flow and whole loan sale agreements across auto finance.

### Ally's Buy Box and Eligibility Criteria

Ally applies its own underwriting filter to Carvana's tape, mimicking its standard dealer-channel buy box. According to a former Ally executive interviewed by In Practise, the approximate FICO distribution Ally accepts from Carvana is:[^6]

- ~10% at or below 620 FICO
- Majority in the 620–700 FICO range
- A significant chunk in the 700–750 range

Critically, **Ally does not purchase Carvana's deep subprime paper** (FICO 567–584). When asked about that range, an Ally executive stated plainly: "We don't go down there". This means the riskiest ~44% of Carvana's securitized loan book (non-prime tranches with weighted-average FICOs of 567–584) flows to ABS markets and other buyers, not to Ally.[^3]

### Performance Triggers and Renegotiation

The specific performance triggers, delinquency thresholds, and loss caps in the MPSA are **redacted** in Carvana's SEC filings. Carvana has redacted 33 different metrics it deems "not material" and "private or confidential," including FICO distributions, LTV ratios, and loan size parameters.[^3]

What is known:

- The commitment is structured as a **12-month rolling agreement** that requires periodic renewal/amendment. The most recent upsizing (to $6B through October 2027) was announced in Carvana's Q3 2025 earnings call.[^2]
- Each amendment resets the commitment amount and period, giving Ally a natural exit ramp at each renewal date.
- In practice, Ally has already demonstrated the ability to reduce purchasing volume without formally terminating the agreement. In 2024, an Ally executive confirmed: "We've pulled back from them pretty significantly in 2024", citing capital constraints and underperformance of older vintage loans.[^3]
- Ally's pullback reduced purchases from $3.6B in FY2023 (~60% of Carvana originations) to ~$2.9B annualized in the first 9 months of 2024 (~35% of originations).[^3]

### Recourse If Loan Quality Deteriorates

Ally's primary protections include:

- **Buy box discipline**: Ally can tighten eligibility criteria at each tape submission, refusing to purchase loans that don't meet its standards.
- **Volume discretion within commitment**: While Ally commits to purchase "up to" a stated amount, the wording gives discretion around the pace and composition of purchases.
- **Rep-and-warranty breach**: If Carvana's origination data proves materially inaccurate (e.g., fabricated income verification, which Hindenburg alleged based on Wells Fargo's prior due diligence concerns about "pay stubs that looked like someone built them in Microsoft Word"), Ally could seek repurchase remedies.[^3]
- **Non-renewal**: Ally can simply decline to renew or reduce the commitment size at each annual reset.

***

## 2. Volume Allocation: Ally vs. ABS vs. Other Buyers

### Cumulative Allocation (Since 2017 IPO)

Of $46 billion in Carvana-originated used vehicle loans since becoming publicly traded:[^1]

| Channel | $ Billions | % of Total Originations |
|---|---|---|
| Ally Financial (forward flow) | $19B | 42%[^1] |
| Public ABS securitizations | $11B | 24%[^1] |
| Carvana held-for-sale (on balance sheet) | $0.7B | ~2%[^1] |
| Other / unaccounted | ~$15B | ~33%[^1] |

The ~33% "unaccounted" portion includes loans that have been paid off, refinanced, defaulted, or sold to unnamed third parties not captured in public disclosures.[^1]

### Recent Quarterly Breakdown (Q3 2025)

In Q3 2025, Carvana sold $3.3 billion in finance receivables:[^9]

| Channel | Amount | % of Q3 Sales |
|---|---|---|
| Ally Financial | $1.2B | ~36% |
| ABS (Purchaser Trusts) | $1.0B | ~30% |
| Other third-party fixed pool sales | $1.1B | ~33% |

The "other third parties" are significant and partially opaque. In 2024, Hindenburg identified Cerberus Capital Management (via "Towd Point Auto" trusts) as a likely buyer, which is notable because Carvana board member Dan Quayle is Chairman of Cerberus Global Investments. Carvana claimed this buyer was an "unrelated third party" and a "large, name-brand asset manager".[^3]

### Evolving Ally Concentration

Ally's share of Carvana's loan sales has varied significantly:

| Period | Ally Share of Carvana Originations |
|---|---|
| FY 2021 | ~29%[^3] |
| FY 2023 | ~60%[^3] |
| 9M 2024 | ~35%[^3] |
| Q3 2025 | ~36%[^9] |

From Ally's perspective, Carvana-sourced loans represented **11% of Ally's total auto originations** as of Q3 2025. However, this figure uses all originations (new, used, lease) as the denominator. **Excluding new vehicle and lease originations, Carvana represents approximately 17% of Ally's used auto book**—a significant single-originator concentration for the largest bank auto lender in the U.S.[^1]

### Carvana's Expanded Loan Sale Partnerships (2025)

In Q3 2025, Carvana announced it had secured agreements for the sale of up to **$14 billion in future loan principal**, including the upsized $6B Ally commitment through October 2027 plus "two other agreements totaling $8 billion". This represents a material diversification of funding sources beyond the historical Ally dependency, though the identity of the other two counterparties has not been disclosed.[^2]

***

## 3. Contagion Path: If the Gotham/Hindenburg Thesis Validates

### The Short-Seller Allegations

On January 28, 2026, Gotham City Research published a report titled "Carvana: Bridgecrest and the Undisclosed Transactions and Debts," alleging that Carvana overstated its 2023–2024 earnings by more than $1 billion through a network of related-party entities controlled by Ernest Garcia II (DriveTime, Bridgecrest, GoFi). CVNA shares fell 14.2% on the day.[^10][^11]

Key Gotham allegations relevant to Ally:

- **Loan-level intermingling**: Gotham alleged evidence of accounting irregularities and loan-level intermingling between Carvana, DriveTime, and Bridgecrest.[^10]
- **Inflated gain on loan sales**: The report suggested Carvana's gain-on-sale margins were boosted by related-party dynamics rather than arm's-length economics.[^9]
- **DriveTime's $1B+ negative operating cash flow** during 2023-2024, funded by increasing debt rather than Garcia family equity.[^12][^13]
- **Predicted 10-K delay and auditor resignation**: Gotham predicted Carvana's 2025 10-K would be delayed, 2023/2024 financials restated, and auditor Grant Thornton would resign.[^9]

This followed the September 2024 Hindenburg Research report, which made overlapping claims about subprime loan quality, related-party transactions, and Ally's pullback.[^3]

### Does Ally Face Direct Credit Losses?

**Yes, but the degree depends on which allegations prove true.** The analysis branches into several scenarios:

**Scenario A: Loan quality is as represented to Ally (Gotham thesis limited to DriveTime/Bridgecrest accounting)**

If the earnings manipulation is confined to related-party transaction pricing (warranty commissions, wholesale vehicle sales to DriveTime, servicing fee structures), Ally's credit exposure is unchanged. Ally owns the loans, they perform based on underlying borrower credit quality, and the related-party dynamics don't directly affect loan-level cash flows. In this scenario, Ally's losses are the normal credit losses already provisioned for (retail auto NCO rate of 188 bps in Q3 2025).[^14]

**Scenario B: Loan origination quality is worse than represented (underwriting fraud)**

This is the more dangerous scenario for Ally. Hindenburg cited a former Wells Fargo senior manager who described concerns about Carvana's origination practices, including pay stubs that "looked like someone built it in Microsoft Word". If borrower income, employment, or identity data was systematically fabricated or inadequately verified at origination, then:[^3]

- Ally's actual credit risk is higher than its buy-box criteria intended
- Default and loss rates on Carvana-sourced loans would exceed Ally's models
- Rep-and-warranty breach claims would be Ally's remedy, but Carvana's ability to honor repurchase demands depends on its own financial health

**Scenario C: Bridgecrest servicing manipulation (extend-and-pretend)**

Bridgecrest, as servicer, controls loss recognition timing on Ally's loans. Carvana's loan extensions in subprime ABS deals more than doubled from 1.97% to 4.18% over the past year—the largest increase among all 23 issuers tracked by S&P, versus an industry average that actually *declined*. If Bridgecrest is granting extensions to mask delinquencies rather than recognizing them:[^3]

- Ally's actual delinquency and loss experience on Carvana-sourced loans may be artificially depressed
- When extensions can no longer mask performance, losses would crystalize in a compressed timeframe
- This is the classic "cliff risk" in servicer-controlled portfolios

### Would Ally Pull the Forward Flow?

**Ally has already demonstrated the ability and willingness to reduce volume.** The pullback from $3.6B in 2023 to ~$2.9B annualized in 2024 showed that Ally can throttle purchases without formally terminating the relationship. An Ally executive described the approach as "buying a little bit to keep the relationship there, keep the relationship strong, but we have pulled back in a pretty significant way".[^3]

The subsequent upsizing to $6B through October 2027 in Q3 2025 complicates this narrative. However, the "up to" language in forward flow commitments gives Ally discretion on actual purchase volume. The key risk factors for a full pullback include:[^2]

- Regulatory pressure (OCC or Fed concern about single-originator concentration)
- Material deterioration in Carvana-sourced loan performance versus Ally's broader book
- Reputational risk from association with a company facing fraud allegations
- An SEC enforcement action or formal investigation against Carvana

A complete termination of the forward flow would be devastating for Carvana. As one analyst noted: "Carvana's growth appears highly dependent on the forward-flow agreement with Ally... Without it, both sales and gross profit drop rapidly". Over 90% of Carvana's earnings are linked to loan sales.[^15][^1]

### Disclosure Risk for Ally

**Ally does not separately identify Carvana-sourced loans in its delinquency, charge-off, or credit quality disclosures.** Carvana loans are aggregated within Ally's "Non-OEM-franchised dealers and automotive retailers" category, which comprised 22% of total originations in 2024. This means investors cannot independently assess the performance of Ally's Carvana-sourced portfolio relative to its broader book.[^16][^1]

The potential earnings impact if the thesis validates:

- Ally's consumer automotive portfolio had $83.8B outstanding at year-end 2024, with a 3.8% allowance for loan losses ($3.17B).[^16]
- If Carvana-sourced loans represent ~11-17% of the relevant portfolio (~$9-14B), and loss rates are materially worse than the 2.2% consolidated NCO rate, the incremental provision could be significant.
- A YouTube-based analysis by an independent research firm estimated that 2022-vintage Carvana loans would create EPS headwinds for Ally in "second half 2026 and 2027".[^17]

***

## 4. Historical Disclosure: Ally's 10-K and Earnings Calls

### What Ally's 10-K Says (and Doesn't Say)

Ally's 2024 10-K (filed February 2025) does not mention Carvana by name in its risk factors, credit quality discussions, or counterparty concentration disclosures. Key observations:[^16]

- **No named originator disclosure**: Unlike some banks that disclose large single-counterparty concentrations, Ally aggregates Carvana within broader categories.
- **Origination mix tables** show "Non-OEM-franchised dealers and automotive retailers" at 22% of 2024 originations ($8.8B), but Carvana is not broken out.[^16]
- **Credit quality tables** present FICO distributions, vintage analysis, and geographic concentration—but never by origination source or dealer name.[^16]
- **Provision for credit losses** in consumer auto rose from $1.04B (2022) to $1.60B (2023) to $1.90B (2024), reflecting deteriorating trends across the portfolio, but Carvana's contribution is opaque.[^16]

### Earnings Call Commentary

Ally management has been notably circumspect about Carvana on earnings calls. The Q3 2025 call focused on:

- Retail auto NCO rate of 188 bps (up 13 bps QoQ)[^14]
- Retail auto coverage ratio flat at 3.75%[^14]
- Originated yield of 9.72% (down 10 bps)[^14]
- An $5B retail auto credit risk transfer (CRT) transaction executed in August 2025[^14]

No specific Carvana discussion was included in the prepared remarks or Q&A from the Q3 2025 call transcript. The CRT transaction is notable—Ally used it to transfer risk on $5B of retail auto loans, generating ~20 bps of CET1 capital. Whether this included Carvana-sourced loans is not disclosed.[^14]

### The Disclosure Gap

The critical disclosure gap is this: **Ally is one of the few major bank auto lenders with a double-digit concentration in loans originated by a single non-OEM counterparty, yet it provides zero public granularity on the performance of those loans.** Analysts and investors must rely on:

- Carvana's own ABS trust reports (which only cover the ~24% of originations securitized, not the Ally portion)[^1]
- Carvana's quarterly 10-Q disclosures on loan sale volumes
- Third-party estimates from firms like BNP Paribas (which estimated Ally historically funded ~50% of Carvana originations)[^18]

If the Gotham/Hindenburg thesis gains regulatory traction, Ally could face pressure from the OCC, Fed, or analysts to provide Carvana-specific credit disclosures—a development that could be either reassuring (if performance is in-line) or destabilizing (if it reveals elevated stress).

***

## Risk Matrix Summary

| Risk Factor | Probability | Severity for Ally | Mechanism |
|---|---|---|---|
| Normal credit losses on Carvana book | High | Moderate | Already provisioned; NCOs tracking elevated but manageable |
| Carvana origination fraud (rep/warranty breach) | Low-Moderate | High | Repurchase demands vs. Carvana's ability to pay |
| Bridgecrest extend-and-pretend unwind | Moderate | High | Compressed loss recognition, reserve inadequacy |
| Forward flow non-renewal | Low (near-term) | Low for Ally, existential for CVNA | Ally loses origination volume but sheds risk |
| Regulatory forced disclosure of Carvana concentration | Moderate | Moderate | Market repricing of Ally's risk profile |
| SEC action against Carvana affecting servicing continuity | Low | Very High | Servicer disruption on Ally's owned loans |

***

## Analytical Conclusion

The Ally-Carvana forward flow is a **true sale, no-recourse structure** where Ally bears all credit risk post-purchase. Ally's primary protections are its buy-box discipline (excluding deep subprime), annual renewal optionality, and rep-and-warranty provisions. The arrangement's opacity—driven by Carvana's aggressive redaction of contract terms and Ally's decision not to disclose Carvana-specific performance—creates a two-way information asymmetry that disadvantages investors in both companies. The $6B upsized commitment through October 2027 suggests Ally management remains comfortable with the relationship, but the Gotham City report's allegations about loan-level intermingling and Bridgecrest servicing practices introduce tail risks that are difficult to quantify from public filings alone.

---

## References

1. [Carvana Loan Breakdown: $46B Originations and $20B Outstanding](https://www.linkedin.com/posts/bill-ploog-91538618_where-are-all-the-carvana-loans-left-hand-activity-7411561200217600000-apUg) - Carvana's growth appears highly dependent on the forward-flow agreement with Ally set to renew in 10...

2. [Carvana's Earnings Call: Record Growth and Optimistic Outlook](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/35838798/carvanas-earnings-call-record-growth-and-optimistic-outlook/) - Carvana set new records in Q3 with retail units sold reaching 155,941, marking a 44% increase. Reven...

3. [Carvana: A Father-Son Accounting Grift For The Ages](https://hindenburgresearch.com/carvana/) - [1, 2] In 2023, Carvana sold $3.6 billion of loans (“receivables”) to Ally Financial through its for...

4. [Omnibus Amendment No. 2 to the Ally Flow transaction](https://contracts.justia.com/companies/carvana-co-5715/contract/315598/) - Omnibus Amendment No. 2 to the Ally Flow transaction from CARVANA CO. filed with the Securities and ...

5. [Third Amendment to the Second Amended and Restated Master Purchase and Sale Agreement, dated March 24, 2023, among Ally Bank, Ally Financial Inc. and Carvana Auto Receivables 2016-1 LLC](https://contracts.justia.com/companies/carvana-co-5715/contract/1237497/) - Third Amendment to the Second Amended and Restated Master Purchase and Sale Agreement, dated March 2...

6. [CarMax: Funding Model vs. Carvana's Forward-Flow Edge](https://inpractise.com/articles/carmax-funding-model-vs-carvanas-forward-flow-edge) - Read CarMax: Funding Model vs. Carvana’s Forward-Flow Edge on In Practise

7. [[PDF] united states securities and exchange commission - Fortune](https://fortune.com/company-assets/838/quartr/quarterly-report-10-q-02470-2025-05-07-08-40-15.pdf) - The. Company completes loan sales without recourse for their post-sale performance and makes customa...

8. [cvna-20210930 - SEC.gov](https://www.sec.gov/Archives/edgar/data/1690820/000169082021000310/cvna-20210930.htm) - ... forward flow arrangement without recourse to the Company for their post-sale performance. Throug...

9. [Carvana Crashes 14% After Gotham City Alleges $1 Billion ... - Fintool](https://fintool.com/news/carvana-short-seller-gotham-attack) - Gotham City Research alleges Carvana overstated earnings by $1B+ through related-party deals with Dr...

10. [Carvana Co. (CVNA) Class Action Investigation | BFA](https://www.bfalaw.com/cases/carvana-class-action-lawsuit) - BFA is investigating whether Carvana violated the federal securities laws by making false and mislea...

11. [Carvana shares fall 14% following short-seller accusations - CNBC](https://www.cnbc.com/2026/01/28/carvana-shares-fall-14percent-following-short-seller-accusations.html) - Carvana shares closed Wednesday at $410.04, down 14.2% following short-seller accusations of the onl...

12. [Carvana: Dissecting the Gotham Short Report](https://swany407.substack.com/p/cvna-gotham) - The short report presented allegations regarding DriveTime's financial results and leverage, Carvana...

13. [CVNA down 20% on the day after Gotham City Research claims fraud.](https://www.reddit.com/r/wallstreetbets/comments/1qpjuyr/cvna_down_20_on_the_day_after_gotham_city/) - They're also alleging ties between GoFi and Carvana - a claim that Hindenburg didn't make, and somet...

14. [$ALLY Ally Financial Q3 2025 Earnings Conference Call - YouTube](https://www.youtube.com/watch?v=tA7fM9FIYlw) - 10/17/2025 Q&A: 25:04 Ally Financial Inc., a digital financial-services company, provides various di...

15. [Carvana Rides $9 Billion Loan Engine as Used-Car Demand Stays ...](https://finance.yahoo.com/news/carvana-rides-9-billion-loan-190331823.html) - In the first nine months of 2025, Carvana originated $9 billion in loans and reported continued acce...

16. [[PDF] 2024 ANNUAL REPORT](https://www.ally.com/content/dam/pdf/investor-relations/2024-10k.pdf) - Prior period results for 2023 and 2024 have been retrospectively adjusted to reflect a change in the...

17. [Carvana, Ally Financial, And Collapsing Consumer Lending ...](https://www.youtube.com/watch?v=Zx2jCWezWms) - Carvana, Ally Financial, And Collapsing Consumer Lending? (Impact On Economy) $CVNA $ALLY $SOFI. 867...

18. [Carvana Extends Loan Sale Deal With Ally, Refuting Short Report](https://www.bloomberg.com/news/articles/2025-01-06/carvana-extends-loan-sale-deal-with-ally-refuting-short-report) - Carvana Co. said it has reestablished an agreement with Ally Financial Inc. to sell the lender up to...

