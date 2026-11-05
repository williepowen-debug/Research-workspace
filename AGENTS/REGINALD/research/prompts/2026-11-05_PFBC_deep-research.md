# Deep research prompt: Preferred Bank (PFBC), written 2026-11-05

**Status:** prompt only, not yet run. Facts below were read at primary sources 11/05 unless marked. Evidence → `reports/2026-11-05_PFBC_and_open-threads.md`, `reports/2026-11-05_late-loan-scan.md`.

---

You are a forensic bank credit analyst. Research Preferred Bank (NASDAQ: PFBC, Los Angeles, FDIC cert 33539, about $7.8B in assets). Your job is to work out whether a sudden rise in late apartment loans is harmless timing or an early sign of real credit loss. Be equally willing to conclude either. A finding that this is nothing is a good result if the evidence supports it.

## What is already known (do not re-derive; correct it if a primary source disagrees)

From the bank's Call Reports:

| $M | 12/31/25 | 3/31/26 | 6/30/26 | 9/30/26 |
|---|---:|---:|---:|---:|
| Multifamily loans 30–89 days late | 70.9 | 56.9 | 62.8 | 143.1 |
| Non-owner CRE 30–89 days late | 106.7 | 20.0 | 19.2 | 33.4 |
| Total 30–89 days late | 196.0 | 98.3 | 108.9 | 213.2 |
| Multifamily nonaccrual | 19.5 | 47.4 | 27.4 | 80.0 |
| Non-owner CRE nonaccrual | 10.9 | 114.2 | 62.0 | 71.0 |
| Total nonaccrual | 38.9 | 169.1 | 98.2 | 159.8 |
| Multifamily book | 598.2 | 603.2 | 586.4 | 540.6 |

From the bank's filings and call:

- **Q2 2026 10-Q:** $137.5M to one relationship went on nonaccrual in Q1 2026 because its principals were "involved in several complicated lawsuits with other banks". The bank sold $9.4M at par in Q1, then $48.5M at par and $20.0M at a $950K loss in Q2. $51.8M remained at 6/30, to be resolved by note sale or foreclosure.
- **Q3 2026 release (10/23):** a $56.7M mixed-use property went on nonaccrual "due to late payments" and moved to held for sale, "under contract to be sold at par with closing anticipated in late October 2026". Four other loans totalling $13.5M also went on nonaccrual. $2.1M of interest was reversed. Problem loans were reported as $109.4M excluding held for sale; adding the $56.6M held-for-sale balance gives $166.0M. The bank said "no significant loss content" and cited an average LTV of 60.8% for this CRE group. Net charge-offs were about zero. The allowance is $78.3M (1.26%). CET1 is 11.26%. Resolutions are "delayed" pending bankruptcy courts.
- **Q3 call (automated transcript):** classified loans of $177.6M including $11.5M of OREO, against $103.8M classified reported at Q2 (basis may differ; check). Only about $20M more substandard on accrual. Multifamily and 30–89 delinquencies were not discussed.
- **Prior public-record leads, unverified at the loan level:** court filings tied to United States v. Makhijani (C.D. Cal. 8:26-cr-00087) and related Cantor/Continuum litigation show Preferred as a senior lender on some properties, including Plaza Continental in Ontario CA ($25.9M; Ch. 11 8:26-bk-10986-MH), Chino Towne Center ($22.4M; 8:26-bk-10925-SC), Tesoro Redlands ($39.0M) and Aryabhata ($28.5M). A purchaser of one Preferred note appears in In re Conejo Riverside Group (8:26-bk-11647-MH). Failed lender Nano Banc held junior liens on some shared collateral. **The bank has never publicly named this relationship, so any link between it and the Q3 loans must be proven, not assumed.**

## Source routes

- **Preferred files with the FDIC, not the SEC.** EDGAR holds no reports for it. Use the FDIC filing system (securitiesfilings.fdicconnect.fdic.gov) for 8-Ks, 10-Qs, 10-Ks, proxies and Forms 3/4/5.
- **The Q3 10-Q is expected ~November 7–10, 2026 (estimate).** If it has been filed, read it first; it outranks everything below.
- Also use: FFIEC CDR Call Reports, FDIC BankFind, PACER/CourtListener dockets (C.D. Cal. and Bankruptcy C.D. Cal.), California DFPI and FDIC enforcement records, county recorder and foreclosure notices, Trepp/CoStar/Crexi coverage, earnings transcripts.
- Label every claim: PRIMARY, SECONDARY, INFERRED or UNKNOWN. Date every figure and give its basis. Say what you could not reach.

## Questions, in priority order

**1. What are the late multifamily loans?**
- Is the $80M rise in late multifamily one or two borrowers, or many?
- Are they past maturity awaiting renewal, or truly missing payments? Does any filing use language such as "matured" or "administrative"?
- Where are they: Southern California, the Bay Area, New York, or Texas? Are any rent-regulated New York buildings?
- Is the 26.5% late share as extreme as it looks? Why did the book fall $46M in one quarter?
- Why was multifamily already at $57–71M late for four straight quarters? Who was that?

**2. Is this the same borrower group or something new?**
- Does the Q3 mixed-use loan or late multifamily connect to the Q1 relationship, by owner, guarantor, LLC, address or attorney?
- Does Preferred's total Makhijani/Cantor exposure, reconstructed from court filings and recorded deeds of trust, reconcile to $137.5M?
- If it is a different borrower, what caused the trouble?

**3. Is "sold at par" real?**
- Did the $56.7M sale close? At what price, to whom, and did Preferred finance the buyer?
- Who bought the $77.8M of notes in 2026? Any recourse, seller financing, side guarantees or repurchase terms?
- Why would a buyer pay par for defaulted notes? What is the buyer's motive: loan-to-own, senior lien protection, sponsor affiliation?
- Does the held-for-sale move imply a mark? Compare book value of $56.7M to the $56.6M balance.

**4. Are the collateral values real?**
- What is the appraisal date behind the 60.8% LTV? Is it current?
- Compare it to debtor schedules, foreclosure bids, broker listings and recent sales for the named properties.
- What did Plaza Continental's plan of liquidation and Chino's case say about value?
- If the 60.8% LTV properties sold at a 20%, 30% or 40% discount to appraisal, what loss results after senior and junior liens and costs?

**5. What is in the bankruptcy courts?**
- List each case involving Preferred: debtor, balance, lien position, status, next date.
- Do the bank's two timelines (Q4 2026/Q1 2027 in the release; "third and fourth quarter next year" on the call) conflict? Which applies to which loan?
- Are any liens or priorities disputed? Is Preferred accused of anything in any adversary case?

**6. How bad could it get, in numbers?**
- Build base, adverse and severe cases for $166.0M of problem loans plus $143.1M of late multifamily.
- Express each against the $78.3M allowance, about $33M of quarterly net income, and CET1.
- At what loss does capital become a real question? Give the number even if it is far away.

**7. Is credit underwriting or governance a concern?**
- Why was a $137.5M single relationship possible at a bank this size? What are the legal lending limit and concentration policy?
- CRE at ~357% of capital and uninsured deposits ~50% were reported earlier (verify both as of 9/30).
- Any enforcement action, MOU indicator, regulator comment, auditor change, restatement, or examiner-related disclosure?
- Any lawsuit against the bank or its officers? Any turnover in credit leadership? Who now holds the chief credit role?
- What have insiders done on Forms 4 in 2026? What has the buyback done?

**8. Could this reach funding?**
- Deposit mix, brokered use, large depositors, FHLB and Fed capacity, and any deposit change since 9/30.
- Does the customer base (historically Chinese-American business owners) make deposits more or less sensitive?

**9. Is this a peer story?**
- Compare 30–89 and nonaccrual trends at Cathay, East West, Hanmi, Hope and RBB, and at other banks with California or New York multifamily.
- Did any of them lend to the same borrower group or buy the same notes?
- Is there a common cause, such as insurance costs, rent regulation or refinance rates?

**10. What does the market believe?**
- The stock has held ~$105–107 since the print, about 1.6× book. Is the 30–89 jump noticed anywhere?
- Short interest and days to cover, analyst notes after the print, downgrades, and institutional holders' moves.
- Options are nearly untradeable (open interest in single digits). If this were real, what expression exists, and is there one worth the trouble?

## Base rates to compute

- In Preferred's own Call Report history since 2015, how often did 30–89 late loans jump by 50% or more in a quarter, and what share became nonaccrual or charge-off within two quarters?
- The same test for US banks of $5–15B with multifamily late share above 10%.
- The 12/31/25 non-owner CRE case is the only known precedent at this bank. Do not lean on it without the base rate.

## Try to disprove the concern

State the strongest case that this is harmless. Look specifically for: a single renewal-in-progress loan, a post-quarter cure, a payoff in Q4, a reporting or classification quirk, or a loan already covered by a sale contract. If the 10-Q explains it, say so first.

## Rules

- Do not assert fraud, misstatement or wrongdoing without a primary document. An indictment is an allegation.
- Do not treat bank statements such as "no significant loss content" as proof. Reported provisions do not prove loss completeness.
- Do not read one bank into a Southern California or sector conclusion.
- Separate what happened, what it might mean, and what is unknown.
- No trade recommendation or position size. Report what evidence would make this worth a trade idea.

## Deliverable

1. **Answer first,** in five sentences: harmless timing, real but contained, or spreading, with a confidence level and the reason.
2. **Table of the ten questions:** answer, evidence, source tier, date.
3. **Named-loan table:** borrower or property, balance, lien, status, value evidence, source.
4. **Loss scenarios** with arithmetic shown.
5. **Falsifiable expectations:** what the next 10-Q, 10-K and Call Report should show if each reading is right, with dates.
6. **What I could not find,** and exactly which document or paid source would settle it.
7. **Source list** with URLs and retrieval dates.
