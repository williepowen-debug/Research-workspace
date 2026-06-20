# WAL Stupin/Cantor Deep Dive — Re-Pledging Incident
**Research Date:** 2026-02-28  
**Subject:** Western Alliance Bancorporation (WAL) — Cantor Group V Fraud / Re-Pledging Collateral  
**Relevance:** Memo Item 3 — CRE Loans Reclassified as C&I

---

## Executive Summary

In August 2025, Western Alliance Bank filed suit against **Cantor Group V, LLC** — a California-based real estate investment fund — alleging that the borrower forged title insurance policies to conceal that collateral properties had already been pledged to other lenders. The loan was structured as a **"note finance revolving credit facility"** (classified C&I), but the collateral was commercial real estate loans. WAL disclosed the lawsuit publicly on **October 16, 2025** via 8-K, after Zions Bancorp made a related disclosure that triggered market-wide scrutiny.

The incident is a textbook example of re-pledging risk: a borrower pledges the same CRE collateral to multiple lenders simultaneously, hiding this through forged title insurance. The bank believed it had a first-priority perfected security interest. It didn't.

---

## 1. Loan Size & Total Exposure

**WAL's direct exposure:**
- **$98.5 million** — note finance revolving credit facility to Cantor Group V, LLC
- Secured by pledged commercial real estate loans (largely California commercial properties: storefronts, office buildings)
- Classified as **C&I** (note finance / revolving credit), not CRE — this is the reclassification dynamic
- Placed on **non-accrual** in Q3 2025; $95 million moved to non-accrual status per Q3 earnings call

**WAL's initial position on recovery:**
> "The Bank has a note finance revolving credit facility to Cantor Group V, LLC secured by pledged commercial real estate loans and their cash proceeds. We believe our circumstances are different than other organizations and that our loan to this specific investment vehicle is secured by loans with a perfected interest in the CRE properties."  
— WAL 8-K, October 16, 2025

Translation: WAL was arguing its collateral position was better than Zions' (which had already charged off $50M), but the assertion was speculative at disclosure.

**Peer exposure (same actors, different Cantor funds):**
- **Zions Bancorp (ZION)** via California Bank & Trust: ~$60 million to **Cantor Group II and Cantor Group IV** (originated 2016-2017). Charged off $50 million in Q3 2025.
- **Banc of California (BANC)**: Part of ~$108M in loans to Stupin (as guarantor); sued April–August 2025
- **Enterprise Bank & Trust**: Part of ~$108M to Stupin; sued 2025
- **Nano Banc**: Part of ~$108M to Stupin; sued 2025
- **PMF CA REIT**: Sued Stupin for ~$7M

**Total troubled debt linked to Stupin/Cantor/Continuum ecosystem:**
- **$270+ million** across at least 7 lenders (Reuters review, October 2025)

---

## 2. Write-Downs, Charge-Offs, Reserves

**WAL Q3 2025 (reported October 21, 2025):**
- Established ~**$30 million specific reserve** for Cantor Group V loan
- Total provision for credit losses: **$80 million** (vs. $39.9M in Q2 2025 — doubled)
- Net charge-offs for Q3 overall: $31.1 million / 22 bps of average loans
- The $98M loan was placed on **non-accrual** — all $95M non-accrual increase in Q3 was attributable to Cantor Group V alone
- No charge-off of the principal taken in Q3; reserve was $30M (implying ~30% expected loss rate at that point)

**WAL Q4 2025 update (reported January 27, 2026):**
- Asset quality described as "steady"
- Non-accrual balances still elevated vs. mid-year but management guided for "meaningful improvement expected by end of Q2 2026" — suggesting resolution still pending
- No full charge-off disclosed as of Q4 2025 earnings

**Zions for comparison:**
- Charged off **$50 million** of $60M outstanding in Q3 2025 immediately upon discovery
- Took full provision for the remaining $10M

---

## 3. The Scheme — How It Worked

The Cantor Group structure (relevant entities: Cantor Group II, IV, V — no relation to Cantor Fitzgerald) operated through a parent firm called **Continuum Analytics**, a Newport Beach, CA distressed real estate investment firm.

**Key actors:**
- **Andrew Stupin** — long-time California real estate investor (~50 years in RE), guarantor on loans, one of Continuum's largest investors
- **Gerald Marcil** — co-investor, California real estate developer
- **Deba Shyam** — legal owner/operator of Cantor Group entities, shares Continuum's offices

**The fraud mechanics (as alleged):**
1. Cantor Group borrowed from banks (WAL, Zions/CB&T, others) under note finance/C&I structures, pledging CRE loans and their underlying properties as collateral
2. Banks believed they held **first-priority liens** — verified via title insurance policies
3. Cantor forged or doctored title insurance policies to hide the fact that **other lenders already held senior claims** on the same properties
4. In some cases (Zions), the properties were transferred to affiliated entities or entered foreclosure, making collateral "irretrievably lost"
5. The affiliated entities that became the new senior lenders were the Cantor/Continuum principals themselves — effectively self-dealing at the banks' expense

**WAL vs. Zions distinction:**
- Zions alleged collateral was secretly subordinated and effectively eliminated (charged off $50M immediately)
- WAL argued its structure was different — secured by first-priority interests in the CRE loans themselves (not just underlying properties) — hence WAL only reserved $30M rather than charging off
- This optimism may or may not prove accurate; full resolution pending

---

## 4. Resolution Status & Legal Proceedings

**Civil litigation:**
- **WAL v. Cantor Group V, LLC** — filed August 2025 in Los Angeles County; Ballard Spahr represents WAL; alleges breach of business loan/security agreement, fraud for doctoring title policies
- **Zions/CB&T v. Stupin, Marcil, Shyam** — filed October 15, 2025, LA County; alleges "sweeping betrayal of trust," systematic collateral elimination
- Multiple other civil suits from Banc of California, Enterprise Bank, Nano Banc, PMF CA REIT (2025)
- Cantor's attorney (Brandon Tran) has disputed that loans are in default and denied fraud allegations; claims loan terms were upheld

**Criminal investigation:**
- **FBI searched Continuum Analytics' Newport Beach offices on September 11, 2025** (reported October 30, 2025 via Reuters)
- A **grand jury was convened** (confirmed via October 2 letter from Allen Matkins law firm in California court proceedings)
- Paul Hastings law firm stated it was "working to unravel multiple levels of alleged fraud"
- No charges filed as of research date (February 2026); criminal investigations "do not necessarily mean wrongdoing has occurred"

**Securities class action investigation:**
- Rosen Law Firm and Shamis & Gentile investigating WAL for potential securities fraud claims
- Period under scrutiny: October 2024 – October 2025
- Theory: WAL repeatedly stated "asset quality remained stable" while the Cantor fraud was unfolding; management may have failed to disclose material risk
- Red flags cited: provision increased $31M → $39.9M → $80M over Q1-Q3 2025; REO assets spiked from $8M (mid-2024) to $218M (Q2 2025) before Cantor disclosure

**Q4 2025 guidance on resolution:**
- Management guided for "meaningful improvement in non-accrual balances by end of Q2 2026"
- No timeline for legal resolution; FBI investigation ongoing

---

## 5. "No Further Irregularities" — The Analyst Acceptance Problem

Per BankersGlobe reporting (October 2025), WAL management explicitly told investors and analysts there were **"no further irregularities"** following an internal review of the loan portfolio, stating the Cantor Group V exposure was isolated.

This claim should be treated skeptically for the following reasons:

**Why analysts accepted it at face value — and why that's a problem:**

1. **Disclosure lag precedent**: The Cantor loan was originated years before WAL discovered the fraud (August 2025 lawsuit means discovery predates October disclosure). How long had WAL held this on their books with deteriorating collateral signals?

2. **Same actors, multiple banks**: The Cantor/Continuum/Stupin network already had loans at 7+ institutions simultaneously. If WAL's internal review only looked for "Cantor Group V" exposure, they may have missed related counterparties

3. **REO spike pre-Cantor**: REO assets rose from $8M → $218M between mid-2024 and Q2 2025 — *before* the Cantor disclosure. Management did not explain this spike proactively. Attorneys are now investigating whether this was a separate CRE quality signal that was under-disclosed.

4. **Provision creep**: Provisions rose each quarter through 2025 before doubling in Q3 on the Cantor news — suggesting deterioration was building, not sudden

5. **Structural vulnerability**: WAL's "note finance" C&I classification is precisely the mechanism that allows CRE exposure to be hidden in plain sight. If Cantor was classified as C&I, how many other CRE-backed "note finance" facilities exist in the portfolio?

---

## 6. Thesis Relevance — Memo Item 3

This incident directly illustrates the re-pledging risk at the core of Memo Item 3:

| Memo Item 3 Element | Stupin/Cantor Manifestation |
|---|---|
| Banks reclassify CRE loans as C&I | WAL's Cantor loan was a "note finance revolving credit facility" (C&I) but secured by CRE loans/properties |
| Hidden CRE exposure | $98.5M of effectively-CRE exposure classified outside WAL's reported CRE bucket |
| Re-pledging risk | Forged title insurance to hide senior claims — exactly the re-pledging mechanism |
| "No further irregularities" = no transparency | Management claimed isolated incident; analysts accepted; securities class action launched |
| Growing C&I reclassification ratio (15.5% → 24.2%) | Note finance is a specific sub-category susceptible to this pattern |

**The $2.73B question**: If WAL has $2.73B in what we classify as hidden CRE (Memo Item 3), and even one borrower in that pool could forge collateral documentation for $98.5M undetected for years, then the "stable asset quality" narrative management has been telling is contingent on self-reporting by borrowers — not independent verification.

The FBI investigation and grand jury suggest this isn't an isolated opportunistic fraud but potentially an organized scheme. Multiple Cantor fund numbers (II, IV, V) across multiple banks suggests a serialized playbook.

---

## 7. Key Open Questions

1. **How much of WAL's note finance portfolio has similar structural vulnerabilities?** (first-priority claims verified only by borrower-provided title insurance)
2. **What is WAL's total "note finance" book?** This is the C&I classification used for the Cantor loan — how large is this segment?
3. **Has the FBI investigation produced charges?** If charges are filed against Stupin/Marcil/Shyam, discovery may surface additional bank relationships
4. **Will WAL recover on the $98.5M?** Management's Q4 2025 guidance of "resolution by Q2 2026" — if collateral is found to be defective, expect charge-off of the remaining ~$68M (loan less $30M reserve)
5. **Are there Cantor Group I, III, etc.?** Reuters identified II, IV, and V as the implicated funds; other numbered funds may have relationships with other regional banks not yet disclosed

---

## Sources

- Reuters: "Investor behind Zions, Western Alliance bad loans is tied to $270 million in troubled debt" (Oct 20, 2025)
- Insurance Journal / Reuters: "FBI Searched California Real Estate Firm" (Oct 30, 2025)
- CNBC: "The alleged 'sweeping betrayal of trust' that rocked Zions bank" (Oct 18, 2025)
- WAL 8-K filed October 16, 2025 (EDGAR: 0001628280-25-045169) — Cantor Group V disclosure
- WAL 8-K filed October 21, 2025 (EDGAR: 0001628280-25-045685) — Q3 2025 earnings press release
- WAL Q3 2025 Earnings Call Transcript (Oct 22, 2025) — non-accrual attribution to Cantor Group V ($95M increase)
- WAL Q4 2025 Earnings Call (Jan 27, 2026) — "resolution expected by end of Q2"
- Cantor Fitzgerald statement (Oct 16, 2025) — disavowed any connection to Cantor Group V
- Rosen Law Firm / ClaimDepot: Securities class action investigation announcement
- Law.com Radar: Western Alliance Bank v. Cantor Group V, LLC (Los Angeles County)
- Investing.com: WAL Q3 2025 presentation summary (Oct 22, 2025)
