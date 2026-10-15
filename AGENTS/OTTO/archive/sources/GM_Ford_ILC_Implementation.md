# GM Financial Bank & Ford Credit Bank: Implementation Plans and Strategic Analysis

## Timeline and Implementation Status

### Ford Credit Bank

Ford Credit CEO Cathy O'Callaghan disclosed that "it will take about a year to put the people, systems, and processes in place to begin taking deposits". This puts the estimated deposit-taking launch around **Q1 2027**, roughly 12 months from the January 22, 2026 approval date. The FDIC order itself requires the bank to be established within 12 months (by January 22, 2027), or the approval expires.[^1][^2]

O'Callaghan explicitly described a phased product rollout: the bank will "start small and grow over time — much like Ford Credit did when it began in 1959 with 12 people". The sequencing is:[^2]

1. **Phase 1** (Year ~1): Online savings accounts via website and mobile app
2. **Phase 2** (subsequent months/years): Certificates of deposit
3. **Phase 3**: Indirect auto financing through Ford dealers[^2]

No specific Year 1/Year 2/Year 3 deposit balance targets have been publicly disclosed as of February 2026.

### GM Financial Bank

GM Financial has not disclosed a specific deposit-taking launch date. GM CFO Paul Jacobson acknowledged on the Q4 2025 earnings call (January 27, 2026) that "it'll take some time" to get the bank operational. Susan Sheffield, GM Financial's President and CEO, described the bank as complementary to existing funding and noted it would ramp "as it gets up and running".[^3]

GM Financial Bank's President and CEO will be **Bill Donnelly**, who brings more than 30 years of banking experience. GM Financial CEO Dan Berce (at the time of the January 2025 refiling) described the bank's purpose as providing "stable, cost-effective funding".[^4]

Both companies are in a **pre-opening buildout phase** — hiring staff, building technology platforms, developing compliance frameworks, and preparing for the mandatory FDIC pre-opening visitation that must yield satisfactory findings before deposit insurance becomes effective.

***

## Deposit Strategy

### Product Architecture

Both banks will follow a **digital-first, branchless model** — deposits gathered exclusively via bank website and mobile application. There will be **no retail branch presence**. This mirrors the Goldman Sachs Marcus model: online-only, high-yield savings and CDs, no checking accounts.[^5][^6][^1]

| Feature | Ford Credit Bank | GM Financial Bank |
|---|---|---|
| **High-yield savings** | Yes[^1][^2] | Yes — explicitly confirmed by Susan Sheffield[^3] |
| **CDs / time deposits** | Yes — Phase 2[^2] | Yes[^1] |
| **Brokered deposits** | Not explicitly confirmed | **Yes** — Sheffield: "they are high yield savings account and broker deposits"[^3] |
| **Demand/checking accounts** | No | No |
| **Physical branches** | No[^2] | No |
| **Deposit listing services** | Not disclosed | Yes — "arrangements with listing services"[^7] |
| **Target depositors** | Consumers nationwide[^1] | GM employees/retirees, dealer principals/employees/customers, GM customers, GMF loan/lease customers, individuals with no GM relationship[^7] |

Susan Sheffield's comment on the GM Q4 2025 earnings call is the most specific public statement from either company about deposit strategy. She explicitly confirmed both **high-yield savings accounts and brokered deposits** as the two deposit channels. The brokered deposit channel is notable — it allows rapid scaling by purchasing deposits through third-party deposit brokers rather than relying solely on organic retail deposit gathering.[^3]

GM Financial Bank will also use "many marketing channels and have arrangements with listing services", suggesting the bank intends to list its rates on deposit aggregator platforms (similar to how Marcus by Goldman Sachs and other online banks attract rate-sensitive depositors through comparison sites).[^7]

### Ford Interest Advantage — The Existing Quasi-Deposit Base

Ford Credit already operates a deposit-like program called **Ford Interest Advantage (FIA)**, which consists of floating rate demand notes. Critically, these are **not FDIC-insured bank deposits** — they are unsecured debt obligations of Ford Motor Credit Company. The current yield is approximately 3.92%.[^8][^9]

FIA balances have grown substantially:

| Year | FIA / Retail Deposit Balance |
|---|---|
| 2022 | $14.3B[^10] |
| 2023 | $17.2B[^10] |
| 2024 | $18.3B[^10] |

Ford Credit Bank will likely **cannibalize a portion of the FIA base** by offering FDIC-insured savings accounts that are inherently safer for depositors. Transitioning even a fraction of the existing $18.3B FIA base into insured deposits would give Ford Credit Bank a significant head start relative to a greenfield online bank. This is a structural advantage GM Financial does not possess — GM has no equivalent retail demand note program.

### Target Deposit Base Size

Neither company has disclosed specific deposit base targets. However, comparisons to existing auto-industry ILCs provide a reference frame:[^11]

- **Toyota Financial Savings Bank**: $7.6B in deposits
- **BMW Bank of North America**: $8.1B in deposits

Both Toyota and BMW's ILCs have been operating for years. Ford and GM, given their vastly larger captive finance operations ($143.6B and $114.3B in outstanding debt respectively), could plausibly target deposit bases multiples of these figures at maturity — but the ramp will take years. IBAT President Christopher Williston predicted the banks will need to "offer high yield savings rates to flighty depositors to fund risky loans", implying aggressive rate-competitive deposit gathering.[^12]

***

## Strategic Rationale — What Executives Have Said

### Cost of Funds Advantage

This is the **primary stated rationale** for both companies. Every public statement from Ford and GM executives centers on lowering funding costs.

**Ford Credit CEO Cathy O'Callaghan**: "This is a long-term strategic initiative that will expand our capabilities, enabling us to offer additional savings options to customers, which will over time **help lower our cost of funding** as well as broaden our financing offerings".[^2]

**GM Financial CEO Dan Berce** (January 2025): "GM Financial Bank will directly support our business model by providing **stable, cost-effective funding**".[^4]

**GM CFO Paul Jacobson** (Q4 2025 earnings call): "Once launched, this bank will enable them to accept deposits, providing another source of stable and diversified funding over time. We also expect this to **lower the cost of funds** and enhance their ability to offer more competitive auto loans to customers".[^3]

**GM Financial President Susan Sheffield** (Q4 2025 earnings call): "[The bank] will allow us to offer depository products and another source of funding to help us **bring down the cost of funds somewhat**… complementary to our footprint, it's not going to replace how we fund the business, but will be complementary to it and allow us to bring down the cost of funds in the basis points over time".[^3]

### Cost Savings Quantified

When a Citi analyst on the GM Q4 2025 call pressed on whether the savings would be "meaningful, like 100 basis points," Sheffield responded: **"Probably not that much. It just depends on the rate environment, but it's going to help us be more competitive"**. This suggests the expected cost-of-funds benefit is likely in the **tens of basis points** rather than a full percentage point — at least initially as the deposit base scales. However, on a debt complex of $114.3B (GM) or $137.9B (Ford), even 20-30bp of blended savings translates to hundreds of millions in annual interest expense reduction.[^3]

The underlying math is straightforward:[^13]

- **GM Financial's interest expense**: $6.0B in 2024, up from $2.9B in 2022 — reflecting the toll of higher rates
- **Ford Credit's public term funding need**: $24-30B annually in 2025
- FDIC-insured deposits (currently ~3.5-4.0% for high-yield savings) are structurally cheaper than unsecured term debt or ABS, particularly during periods of credit stress

### Reducing ABS/Warehouse Dependency

Neither company has **explicitly** stated that reducing ABS or warehouse dependency is a primary motivation. However, the strategic logic is implicit in every statement about funding diversification.

Ford Credit's current funding mix is heavily concentrated in capital markets:[^13]

| Funding Source | Amount | % of Total |
|---|---|---|
| Term Unsecured Debt | $59.2B | 41% |
| Term ABS | $60.4B | 42% |
| Retail Deposits / FIA | $18.3B | 13% |
| Other / Equity | $15.7B | 4% |

Over 83% of Ford Credit's funding comes from term debt and ABS markets. GM Financial's reliance is similarly heavy — $49.6B secured debt and $64.7B unsecured debt totaling $114.3B. The deposit channel creates a **third, structurally different funding pillar** that is less volatile than capital markets issuance and doesn't require the extensive structuring costs of ABS.[^13]

GM described the bank as providing "stable and diversified funding through deposit products". The word "diversified" is the operative signal — both companies are building optionality for environments where ABS spreads widen or unsecured issuance becomes expensive.[^14]

### Serving Subprime Borrowers

Neither company has **explicitly** framed the ILC as a vehicle for serving subprime borrowers that banks won't touch. However, the broader auto lending market context is relevant:

- Deep-subprime originations reached 14.2% of total auto loan volume in September 2025, up 170bp year-over-year[^15]
- Captive finance companies (including GM Financial and Ford Credit) are growing fastest among lender types, with their incentive being to "move inventory"[^15]
- GM Financial's Q4 2025 U.S. retail loan share of total GM business dropped to 31% (from 43% in Q4 2024), driven by "type and level of incentive programs offered"[^16]

The ILC structure gives captives cheaper funding to support the full credit spectrum — including near-prime and subprime borrowers where bank lenders have been more cautious. But this has not been positioned publicly as a primary rationale.

***

## Competitive Positioning

### Versus Existing Auto ILCs

Ford and GM enter a space where Toyota and BMW already operate established industrial banks. There are currently 24 industrial banks in the United States.[^14]

| ILC | Total Deposits | Parent Finance Arm Debt |
|---|---|---|
| Toyota Financial Savings Bank | $7.6B[^11] | ~$125B (Toyota Motor Credit) |
| BMW Bank of North America | $8.1B[^11] | ~$95B (BMW Financial Services) |
| Ford Credit Bank (projected) | TBD | $137.9B |
| GM Financial Bank (projected) | TBD | $114.3B |

Ford and GM's captive finance operations are larger than Toyota's and BMW's, suggesting their banks could eventually grow to substantially larger deposit bases. The competitive dynamic, however, is about deposit pricing — all these banks must offer rates competitive with online savings leaders (Marcus at ~3.65% APY, Ally at ~3.50% APY) to attract retail depositors.[^17][^6]

### Pricing Strategy

No explicit pricing strategy has been disclosed. However, the structural dynamics point toward:

- **High-yield savings rates competitive with Marcus/Ally** — necessary to attract deposits in a digital-only, no-branch model
- GM Financial's explicit confirmation of brokered deposits suggests willingness to pay market rates for rapid scale[^3]
- IBAT's Williston predicted they'll need "high yield savings rates to flighty depositors"[^12]
- J.D. Power's Roosen noted the ILC structure gives automakers "a much lower cost of funds, which can be passed on to their future customers" through more competitive auto loan rates[^14]

### Are They Targeting Segments Monolines Are Exiting?

There is **no explicit public statement** from either company about targeting segments where monolines or other lenders are pulling back. The stated positioning is broader: funding diversification and cost reduction to support the existing auto lending business model.

That said, the strategic timing is notable. With vehicle affordability at crisis levels (average new vehicle near $50,000), 47.5% of borrowers on terms exceeding 72 months, and traditional banks increasing their share of new-car lending at captives' expense in some quarters, having a cheaper and more stable funding base positions Ford and GM to maintain aggressive lending through credit cycles — precisely when bank lenders and monolines tend to retreat.[^18][^16]

### Pending Competitors

The ILC landscape is expanding beyond auto. Pending applications include:[^5]
- **Nissan** — filed June 2025[^19]
- **PayPal** — filed December 2025[^20]
- **Affirm** — filed January 2026 (Nevada charter)[^21]
- **Stellantis** — also submitted an ILC charter request in 2025[^14]

This growing pipeline suggests Ford and GM's approvals have opened a regulatory pathway that other large commercial and fintech companies intend to follow.

***

## Key Unknowns and Gaps

Several critical details remain undisclosed as of mid-February 2026:

- **Specific deposit targets**: Neither company has published Year 1/2/3 deposit balance targets
- **Deposit rate commitments**: No specific APY or pricing relative to peers has been announced
- **Staffing/headcount**: The number of bank employees being hired in Salt Lake City is not public
- **Technology vendors**: Core banking platform selections for the deposit side have not been disclosed (GM Financial's FDIC order requires a proprietary core banking platform for deposits)[^7]
- **Ford Credit Q4 2025 earnings call**: Ford's Q4 2025 results were released February 10, 2026, but detailed ILC implementation commentary from that call was not available for this analysis[^22]
- **Ford Interest Advantage migration**: Whether and how Ford plans to transition FIA holders to insured bank deposits has not been addressed publicly

The Ford Credit Q4 2025 earnings call transcript would likely contain additional implementation details, particularly regarding how the bank interacts with the existing $18.3B FIA program.

---

## References

1. [FDIC Approves the Deposit Insurance Applications for Ford Credit ...](https://www.fdic.gov/news/press-releases/2026/fdic-approves-deposit-insurance-applications-ford-credit-bank-salt-lake) - The FDIC approval orders expire if Ford Credit Bank and GM Financial Bank are not established within...

2. [FDIC Conditionally Approves Ford Credit Industrial Bank](https://www.fromtheroad.ford.com/us/en/articles/2026/fdic-conditionally-approves-ford-credit-industrial-bank) - Following conditional approval from the FDIC and Utah Department of Financial Institutions, Ford Cre...

3. [$GM General Motors Q4 2025 Earnings Conference Call - YouTube](https://www.youtube.com/watch?v=c3kFjIxKbcY) - company operates through GM North America, GM International, Cruise, and GM Financial segments. It m...

4. [GM Financial Submits Application For Industrial Bank Charter](https://www.gmfinancial.com/en-us/company/newsroom/jan-2025-ILC-update.html) - GM Financial Receives Approval to Establish a Bank. In January 2026, GM Financial received FDIC appr...

5. [FDIC conditionally approves Ford, GM ILC charters - Banking Dive](https://www.bankingdive.com/news/fdic-conditionally-approves-ford-gm-ilc-charters/810377/) - Both automakers must stand up their respective banks within 12 months. After that, they must maintai...

6. [Marcus by Goldman Sachs Bank Review 2025](https://www.nerdwallet.com/banking/reviews/goldman-sachs-bank) - Marcus by Goldman Sachs offers good savings accounts with no fees. Keep in mind that there are no ch...

7. [[PDF] GM Financial Bank, Salt Lake City, UT - FDIC](https://www.fdic.gov/bank-examinations/gm-financial-bank.pdf) - The Bank will fund its lending activities through a combination of savings and time deposit products...

8. [[PDF] Ford Motor Credit Company LLC](https://www.ford.com/finance/content/dam/ucl/brandsites/pdf/Ford_Motor_Credit_FIA_Prospectus.pdf) - You can obtain current Note investment information by calling toll-free 800-462-2614 or by visiting ...

9. [Ford Interest Advantage | Investor Center](https://www.ford.com/finance/investor-center/ford-interest-advantage/) - Explore what makes our program a smart choice: Minimum balance requirement of just $1,000. Fast and ...

10. [f-20241231 - SEC.gov](https://www.sec.gov/Archives/edgar/data/37996/000003799625000013/f-20241231.htm) - Retail Deposits / Ford Interest Advantage, 14.3, 17.2, 18.3. Other, 2.7, 1.4, 1.2 ... (a)Total share...

11. [Largest U.S. Banks by Total Domestic Deposits in 2025 | MX](https://www.mx.com/blog/biggest-us-banks-by-deposits/) - TOYOTA FINANCIAL SAVINGS BANK, $7,600,225. 177. BYLINE BANK, $7,584,919. 178. CENTIER BANK, $7,527,9...

12. [FDIC Approves Carmakers' Bids to Establish Banks](https://ibat.org/fdic-approves-carmakers-bids-to-establish-banks/) - Ford Credit Bank and GM Financial Bank, both to be chartered in Utah, will focus on auto lending. Fo...

13. [FDIC Greenlights Ford and GM Industrial Banks in Historic Approval](https://fintool.com/news/ford-gm-industrial-bank-fdic-approval) - GM Financial's interest expense hit $6.0 billion in 2024, up from $4.7 billion in 2023 and $2.9 bill...

14. [Ford and GM get approval to launch banks: What it means for you](https://thehill.com/business/5712194-ford-gm-banks-financing-cars/) - Ford and GM have cleared a key regulatory hurdle to launch their own banks · The new industrial bank...

15. [Longer Loan Terms: Impact on Car Buyer Behavior - Jupiter Chevrolet](https://www.jupiterchev.com/blogs/6872/longer-loan-terms-impact-on-car-buyer-behavior) - Lenders, including captive finance companies like GM Financial, are offering extended terms to move ...

16. [GM Financial net income up 10.6% YoY in 2025 | WardsAuto](https://www.wardsauto.com/news/gm-financial-net-income-up-106-yoy-in-2025/810901/) - For all of 2025, retail auto loan and lease originations for the captive finance company totaled $55...

17. [Ally Bank Vs. Marcus By Goldman Sachs](https://www.bankrate.com/banking/ally-bank-vs-marcus-by-goldman-sachs/) - Both Ally Bank and Marcus by Goldman Sachs offer strong yields and minimal fees, making them excelle...

18. [Ford and GM win approval to launch new car loan banks - USA Today](https://www.usatoday.com/story/cars/research/car-loans-financing/2026/01/26/gm-ford-new-credit-bank-institutions/88361663007/) - Car loans for Ford and GM models may be easier to get from new banks that the automakers are now cle...

19. [Nissan submits application to form Nissan Bank in the US](https://www.fintechfutures.com/bankingtech/nissan-submits-application-to-form-nissan-bank-in-the-us) - The Japanese car manufacturing giant has submitted its application to the Federal Deposit Insurance ...

20. [BPI and ICBA Comment on PayPal Bank's Application for Deposit ...](https://bpi.com/bpi-and-icba-comment-on-paypal-banks-application-for-deposit-insurance/) - Today, however, the loophole allows large national and international financial and commercial firms ...

21. [Affirm applies for a bank charter - eMarketer](https://www.emarketer.com/content/affirm-applies-create-affirm-bank-us) - With an ILC charter, Affirm may lower its funding costs and cut out fees paid to sponsor banks. It c...

22. [Ford Reports Fourth-Quarter, Full-Year 2025 Financial Results](https://www.barchart.com/story/news/140804/ford-reports-fourth-quarter-full-year-2025-financial-results) - Wall Street expects AMD to report earnings of $1.10 per share for Q4, representing 25% growth from $...

