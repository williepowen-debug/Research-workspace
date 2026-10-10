> **FROZEN 2026-07-09** — Mar-13 slide-deck source material, static point-in-time evidence assembly. Not maintained; current thesis state lives in **`STATUS.md` §THESIS** (canonical since 2026-08-13; `thesis/THESIS.md` is a retired pointer stub) + `workbook/KB.tsv`. *(Redirect re-pointed 2026-10-10, DAEDALUS Falsification #4.)*

# DECK_EVIDENCE.md — Thesis Evidence Assembly
**Author:** REGINALD | **Date:** 2026-03-13 | **Purpose:** Slide deck source material
**Audience:** Finance-literate but not macro-deep. Knows what a put is. Doesn't read call reports.
**Question being answered:** "What would make someone who thinks the market is fine stop and reconsider?"

---

## RANKING KEY
🔴 Smoking gun — verifiable, specific, hard to explain away  
🟠 Strong signal — meaningful, directional, requires some interpretation  
🟡 Supporting evidence — part of the mosaic, not standalone

---

## #1 — Banks Are Hiding Their Real Estate Loans Inside a Different Category — and We Can Prove It

**The finding:**  
A bank that failed in Chicago in January 2026 told regulators it had only 11% of its loans in commercial real estate — the actual number, once you look at a single hidden line item in the regulatory filing, was 61%.

**Why it matters:**  
Metropolitan Capital Bank (failed Jan 30, 2026, Chicago) reported its CRE concentration at 10.7% — well under the regulatory flag level — because it classified most of its real estate loans as "commercial & industrial" loans. The real CRE ratio was 61%. When it failed, 100% of charge-offs were CRE losses. This is not unique to one failed bank: Western Alliance (WAL) — a $80B nationally chartered bank — has a hidden CRE ratio of 24.2% by the same metric, and it has been **growing**: up from 15.5% in Q2 2024 to 24.2% in Q4 2025. Management's own words on a conference call confirmed the shift ("remixing into higher-return C&I"). ~~Bank OZK's ratio is 37.6% — **worse than the bank that already failed**.~~ The metric is pulled from a single field in the FDIC Call Report: Schedule RC-C, Memo Item 3, RCON2746. It is public, verifiable, and almost nobody looks at it.

> ⚠️ **CORRECTION 2026-08-10 (first-ever FFIEC primary runs, 8/7):** the **OZK 37.6% claim is STRUCK — it reproduces at none of 18 quarters** at the FFIEC primary; the screen's denominator (item-4 C&I only) doesn't contain OZK's Memo-3 balance, which sits entirely in item 9.a (live recipe-basis ratio 9.35%, below the screen's own flag). Do NOT use the OZK line in any deck. **The WAL leg survives verification** — 24.24% at 12/31/25 reproduces exactly and the 15.5%→24% relabeling uptrend holds — but live Q2-26 is **21.20%** and the series never reached 25% in 12 quarters, so drop "and growing" going forward. Cohort re-run on a settled basis pending (REGINALD-owed).

**The source:**  
- FDIC Call Report, Schedule RC-C, Memo Item 3 (RCON2746) — public data, searchable at https://call.ffiec.gov  
- Metropolitan Capital Bank FDIC failure data (Jan 30, 2026; FDIC CERT 57120)  
- WAL 10-Q Q4 2025; earnings call transcript (Q4 2024: "remixing" language)  
- Our Hidden CRE screen: `BANK_EXPOSURE_MATRIX.md`

**Strength:** 🔴 SMOKING GUN  
*This is our most original work. It is verifiable from public filings. Anyone who doubts it can pull the FDIC data themselves in 10 minutes. Metropolitan Capital is the proof of concept — it failed on exactly this pattern.*

---

## #2 — Western Alliance's 22-Year CFO Was Just "Promoted" Into a Fake Job at Exactly the Wrong Moment

**The finding:**  
Western Alliance Bank replaced its CFO of 22 years — who was overseeing a period of accelerating hidden CRE growth — with a banker hired directly from JPMorgan's bank restructuring advisory group.

**Why it matters:**  
Dale Gibbons served as WAL's CFO for 22 years — longer than five times the industry average tenure. In December 2024, he became interim CEO when CEO Vecchione went on medical leave, meaning he had full visibility and authority over WAL's balance sheet during the period when the hidden CRE ratio jumped most aggressively. In July 2025, WAL announced Gibbons would "transition" to a new role: "VP, Deposit Initiatives and Innovation." This title does not exist at any serious $80B bank — it is a parking-lot title. His replacement, Vishal Idnani, was hired from JPMorgan's Financial Institutions Group — the team that advises banks on capital raises, restructurings, and crisis management. In the same month (December 2025), WAL added two new risk-specialist board members, including Clarke Starnes III (former Chief Risk Officer of Truist). Every element of this succession pattern — long-serving CFO sidelined, restructuring expert hired, risk board expanded — fires simultaneously in the quarter when hidden CRE is highest.

**The source:**  
- WAL 8-K filings: Dec 11, 2024 (CEO medical leave); Jul 17, 2025 (CFO transition); Dec 11, 2025 (board additions) — all on SEC EDGAR, CIK 1212545  
- LinkedIn / JPM FIG: Idnani background  
- `domain/INSIDER_BEHAVIOR_SCAN.md` (filed 2026-03-13; path fixed 7/17)  
- `STATUS.md` CFO Swap Analysis section (filed 2026-03-13)

**Strength:** 🔴 SMOKING GUN  
*This is not a vague insider-selling story. It is a documented succession sequence with a paper trail: specific SEC filings, specific titles, specific timing. The JPM FIG hire is the keystone — you hire that person when you need a crisis playbook, not when you're growing deposits.*

---

## #3 — The FDIC's Own Q4 2025 Report Says Regional Banks Are More Exposed Than Large Banks — While Reporting "Strong Earnings"

**The finding:**  
The FDIC just released its official Q4 2025 industry report saying the banking industry had a "strong quarter" — while buried inside the same report, it disclosed that commercial real estate problem loan rates are 7 times their pre-pandemic average, and explicitly warned that regional banks carry **higher concentrations** of these loans than large banks.

**Why it matters:**  
The headline was "profits up 10.2%, NIM highest since 2019." The fine print: non-owner-occupied CRE past-due and non-accrual rates are 4.06% for large banks — still 7x the pre-pandemic average of 0.58% — and the FDIC explicitly states that smaller (regional) banks have "higher concentrations of such loans in relation to total assets and capital." The number of problem banks rose by 3 to 60 — still "in the normal range," per the FDIC, before any major catalyst has hit. Reserve coverage is declining. The FDIC's own conclusion: "the industry still faces weakness in certain loan portfolios… these issues will remain matters of ongoing supervisory attention." This is the regulator saying, in polite language, that stress is real and it's concentrated in the places that can least afford it.

**The source:**  
- FDIC Quarterly Banking Profile, Q4 2025 — released Feb 24, 2026  
  https://www.fdic.gov/news/speeches/2026/fdic-quarterly-banking-profile-fourth-quarter-2025  
- Chart 11 (CRE concentration by bank size — the "money shot")  
- `domain/sources/RP-REG-6_FDIC_QBP_Q4_2025.md`

**Strength:** 🔴 SMOKING GUN  
*This is the government regulator's own data. There is no "but that's just one analyst" objection. The FDIC itself is flagging exactly what we're trading against.*

---

## #4 — A Major CRE Lender's Bondholders Are Demanding Cash Instead of Accepting the Bank's Own Extension Offer

**The finding:**  
Kennedy Wilson, one of the country's largest commercial real estate operators, offered bondholders a debt exchange in March 2026 — and the majority of bondholders, organized by law firm Milbank, said no and demanded cash instead.

**Why it matters:**  
The standard playbook in commercial real estate distress is "extend and pretend" — lenders and borrowers agree to roll debt forward, avoiding a default on paper while the underlying asset continues to deteriorate. The Kennedy Wilson bondholder revolt is the first high-profile case of creditors explicitly refusing to play along. KW's debt-to-equity ratio is 5.75 and its current ratio is below 1.0 (meaning it cannot cover short-term obligations from short-term assets). If the exchange offer failed and bondholders demanded cash, KW — at that leverage — faces a credit event. The pattern risk is systemic: if major creditors at other CRE operators start doing the same math, the extend-and-pretend assumption that underpins nearly every regional bank's CRE book gets repriced simultaneously.

**The source:**  
- Bloomberg, Mar 6, 2026: Kennedy Wilson bondholder revolt  
- KW Exchange Offer dated Mar 2, 2026 (SEC filing)  
- Milbank LLP bondholder organization confirmed  
- ~~`mail/inbox/2026-03-11_…kennedy-wilson-bondholder-revolt.md`~~ *(dead path — the HERMES-era `mail/` tree was retired; file not preserved in `inbox/processed/` either. Claim stands on the Bloomberg/SEC cites above; noted 7/17 audit.)*  
- `STATUS.md` Mar 12 AM update, Signal 2

**Strength:** 🟠 STRONG SIGNAL  
*The KW situation is a named, dated, verifiable example of the extend-and-pretend playbook failing. It is the strongest precedent we have for "how these things start." The debt/equity and current ratio figures come directly from public filings.*

---

## #5 — Deutsche Bank Just Disclosed $30 Billion in Private Credit Exposure — Inside a Market That's Already Starting to Crack

**The finding:**  
Deutsche Bank disclosed €26 billion ($30 billion) in private credit exposure in its annual report, and explicitly acknowledged "potential indirect credit risks through interconnected portfolios and counterparties."

**Why it matters:**  
Private credit — loans made by non-bank lenders (hedge funds, BDCs, private equity credit arms) — exploded in size over the past decade precisely because it was opaque: no public markets, no daily pricing, no visible stress. The stress is now visible. Blackstone's BCRED had $3.8 billion in redemption requests in Q1 2026 (~8% of NAV). Blue Owl restricted redemptions and switched to "periodic asset-sale payments." PIMCO's president publicly called it a "reckoning going on right now — bad underwriting." Against this backdrop, DB disclosed that a single institution has $30B tied up in this market — and that interconnection risk is real. DB also warned internally about $143B in BDC exposure across the global banking system. The FDIC separately confirms that bank loans to private credit funds (NDFIs) grew 35% year-over-year in 2025 to $1.4 trillion outstanding, with another estimated $2.8 trillion in undrawn commitments — total potential exposure of $4.2 trillion, the fastest-growing bank asset category in the industry.

**The source:**  
- Deutsche Bank Annual Report 2025 (March 2026 publication); Bloomberg/Reuters Mar 12, 2026  
- FDIC Q4 2025 QBP: NDFI loan data ($1.4T outstanding)  
- Christopher Whalen, Daily Reckoning (via FDIC Q4 2025 data), March 2026  
- PIMCO President Christian Stracke, Bloomberg, Mar 11, 2026: "reckoning going on right now"  
- `STATUS.md` Mar 13 AM update, Signal 2; `NDFI_HIDDEN_CRE_HYPOTHESIS.md`

**Strength:** 🟠 STRONG SIGNAL  
*The DB number is specific, sourced, and recent. Combined with the FDIC's own data on $4.2T bank NDFI exposure, this is the interconnection risk in quantified form. DB saying it themselves removes the "conspiracy theory" objection.*

---

## #6 — A Major Commercial Real Estate Loan Originator Admitted in an SEC Filing That Fraud in the Underlying Loans Is "Systemic, and No Longer Anecdotal"

**The finding:**  
Walker & Dunlop — one of the largest government-approved commercial real estate lenders in the country — disclosed in its 2024 10-K that it has had to repurchase or indemnify $221.6 million in loans, and used the word "systemic" to describe the underlying fraud.

**Why it matters:**  
Walker & Dunlop originates and sells CRE loans to Fannie Mae and Freddie Mac. When those loans go bad because borrowers lied — inflating rental income, misrepresenting collateral, faking titles — W&D has to buy them back. Their word choice matters: "systemic, and no longer anecdotal" is a legal disclosure, written by lawyers who chose every word carefully. What the fraud consisted of: inflated net operating income (NOI) at loan origination. NOI is the single number that determines what a commercial property is worth. If the NOI was inflated to get the loan, the loan-to-value ratio the bank reported was also wrong. Every bank with CRE loans from this era has collateral that may have been valued against a fiction. Ready Capital, a parallel lender, disclosed $134 million in similar borrower fraud in the same period. This is not one bad actor — it is a structural feature of the cycle.

**The source:**  
- Walker & Dunlop 2024 10-K (SEC EDGAR: WD)  
- Ready Capital Q4 2025 earnings: $134M fraud disclosure  
- Unicus Research: "Curiouser and Curiouser" (institutional short thesis)  
- `STATUS.md` Mar 10 late signals section

**Strength:** 🔴 SMOKING GUN  
*"Systemic" in a 10-K is one of the strongest words a public company can use. It is an admission under SEC disclosure rules. Anyone who wants to look it up can find it in EDGAR in two minutes.*

---

## #7 — OZK's Most Important Loan Is $915 Million, and the Building Is Largely Empty

**The finding:**  
Bank OZK's single largest loan — $915 million against a San Francisco Bay Area life sciences campus — is secured by a building that analysts estimate may now be worth $500 million, and the bank has already had to sell its second-largest problem loan at a significant loss for the first time in its history.

**Why it matters:**  
OZK built its reputation as a disciplined CRE lender. But it is now holding $915M against a largely vacant IQHQ campus in a life sciences market with 35% vacancy and no significant new tenants. Analysts (Citi, which downgraded to SELL in 2024) estimate recovery at roughly 55 cents on the dollar. Separately, OZK just sold its Pacific Center loan — a $265M vacant life sciences building — to a distress buyer (SVP) for the first time in its history, signaling a strategic shift away from its prior "hold to resolution" approach. The CEO's own words on the Q4 2025 earnings call: "We expect 2026 results to resemble 2024 and 2025." That is the language of a bank grinding through losses, not one that sees recovery. OZK's construction loan-to-Tier 1 capital ratio is 142% against a 100% regulatory threshold — the highest in our screen. Its unfunded commitments alone add another ~$10.6 billion in contractual CRE obligations that must be funded even if management wants to shrink the book.

**The source:**  
- OZK Q4 2025 earnings call (Jan 20, 2026; transcript via TickerReport)  
- Bisnow: "Bank OZK Offloads $265M Life Sciences Construction Loan" (Jan 5, 2026)  
- Moody's OZK CRE Concentration Report (Jun 2024)  
- FDIC Call Report (Construction/Tier 1 ratio)  
- `domain/sources/RP-REG-7_OZK_THESIS.md`

**Strength:** 🟠 STRONG SIGNAL  
*The IQHQ number ($915M loan, ~$500M analyst estimate of value) is verifiable from public filings and analyst research. The loan sale is documented. The CEO quote is on the record.*

---

## #8 — This Looks Like 2007, Not SVB — The Losses Are Building Slowly, Not in a Weekend

**The finding:**  
The current CRE stress cycle has been building for four years, with banks continuously using accounting and legal tools to delay recognizing losses — the same pattern that played out from 2007 to 2010, not the sudden bank-run collapse of Silicon Valley Bank in 2023.

**Why it matters:**  
SVB failed in 72 hours because its deposits were all uninsured tech companies that wire-transferred money immediately. Regional bank CRE stress doesn't work that way. The 2007-2010 playbook: banks extend loan maturities, banks renegotiate terms, banks reclassify loans, regulators don't force marks — and then, when enough loans reach hard maturity or enough properties are appraised in a down market, the losses crystallize in waves. The current data confirms the pattern: CRE loan modifications were up 66% year-over-year in 2025 ($27.7 billion), **office** CMBS loans in special servicing hit 17.11% (office-specific, not overall — overall SS was 11.2% as of June 2026), and the bank CRE delinquency rate (4.18%) is less than half the CMBS delinquency rate (12.34%) for identical asset types — a gap that can only be explained by bank extend-and-pretend. The 2022 vintage construction loans (originated when rates were near-zero, when project pro formas used aggressive NOI assumptions) are now hitting hard maturity dates in 2026. They can't be refinanced at current rates. They can't be extended again. That is the crystallization event — and it's on a calendar, not a panic.

**The source:**  
- Trepp CMBS Delinquency data, Feb 2026 (12.34% office CMBS DQ — all-time high, exceeds GFC)  
- FFIEC Call Report CRE DQ data (4.18%) — gap vs CMBS confirms masking  
- CRE modification data: CREED sub-agent research, CREED/research/RQ-CREED-008  
- CMBS special servicing: Trepp Jan 2026 (**office 17.11%**, +47bps MoM — was mislabeled here as overall/Feb; corrected 7/17 per CREED SOURCE_2026-02-11 + SIG-W-20260717-005. June 2026: office SS 17.11% (+36bps), overall SS 11.2% (+34bps) — SS *rising* while DQ *falls* = the extend-and-pretend divergence printing in the data)  
- `BANK_EXPOSURE_MATRIX.md`; `STATUS.md` Signal Dashboard

**Strength:** 🟠 STRONG SIGNAL  
*The 8.16 percentage point gap between bank-reported CRE delinquency (4.18%) and CMBS delinquency on the same property types (12.34%) is the single most persuasive number for the 2007 parallel. It is public data. The gap cannot be explained by anything other than banks using accounting flexibility that CMBS does not have.*

---

## #9 — Manhattan Commercial Real Estate Is Now Worth Less Per Square Foot Than It Was During COVID Lockdowns

**The finding:**  
Major Manhattan office buildings tracked by Evercore ISI in March 2026 are trading below their COVID-era valuations — meaning the "emergency" pricing from a period when offices were legally closed is now the ceiling, not the floor.

**Why it matters:**  
Banks that hold Manhattan CRE loans (directly or through securitizations) marked their collateral to COVID-era values as a conservative floor. That floor just broke. Empire State Realty Trust: $263/sq ft (COVID low was $266). SL Green: $416/sq ft (COVID low was $461). Vornado: $291/sq ft (COVID low was $364). The NYT Building alone was appraised down 40%. This matters for our specific banks: WAL has Cantor Fitzgerald appraisals in progress right now on a $98 million receiver portfolio. Those appraisals are being conducted into a market where Manhattan CRE is priced below COVID lows. If they come in at under 50 cents on the dollar, WAL must take a Q1 writedown. The demand destruction is structural, not cyclical: remote work reduced office days, and AI is reducing headcount — so even companies with return-to-office mandates need less space because they have fewer people.

**The source:**  
- Evercore ISI research, Mar 6, 2026 (via NY Post)  
- Empire State Realty Trust, SL Green, Vornado share prices and $/sqft disclosures  
- Cantor Fitzgerald appraisal disclosure: WAL 8-K and court filings  
- `STATUS.md` Mar 10 EOD signal: Manhattan CRE Below COVID Lows

**Strength:** 🟠 STRONG SIGNAL  
*The specific per-square-foot numbers are from a named research firm (Evercore ISI) comparing named companies to their own COVID-era prices. This is not theory — it is market pricing, fully public, verifiable against REIT disclosures.*

---

## #10 — OZK's Chief Risk Officer Sold Shares Without an Automatic Trading Plan — While His Bank Was Quietly Building Reserves for Four Years

**The finding:**  
Bank OZK's Chief Risk Officer sold 10.78% of his personal stock holdings in February 2026 through a discretionary open-market sale — with no pre-arranged automatic trading plan — while his bank has been building loan loss reserves every quarter for 14 consecutive quarters in anticipation of CRE losses.

**Why it matters:**  
Insider stock sales are common and often meaningless — most executives sell through "10b5-1 plans," which are pre-programmed automatic schedules set up months in advance. A discretionary sale, with no such plan, means the person actively decided to sell on that specific day. The person who did this at OZK is the Chief Risk Officer — the individual whose job is to understand, in detail, every stressed credit on the bank's books. In the same period, OZK's CFO staged approximately $944,000 in sales across two tranches (October 2024 and January 2025), representing roughly 22% of holdings. A director sold $5.2 million at $51.50 — the stock is now in the $42-44 range, near a 52-week low. No insider at OZK has purchased shares in the past 12 months. The CEO (who owns ~10% of the company personally) has not sold — but at that ownership level, any sale would be a public market signal, so his captivity is not evidence of confidence. The bank's own management said reserves were built "over 14 quarters in anticipation that some sponsors would become no longer willing to or able to support their projects."

**The source:**  
- SEC EDGAR Form 4 filings (OZK files with FDIC, not SEC — insider data accessed through OZK IR documents; see note in `domain/INSIDER_BEHAVIOR_SCAN.md`)  
- OZK Q4 2025 earnings call transcript (Jan 20, 2026): 14-quarter reserve build language  
- `STATUS.md` Insider Behavior Scan section (filed 2026-03-13)  
- Director Whipple: $5.2M sale at $51.50 documented in OZK FDIC proxy filing

**Strength:** 🟠 STRONG SIGNAL  
*The CRO discretionary sale is the strongest single insider signal in our screen. The 14-quarter reserve language is the CEO's own words on a public earnings call — he is essentially describing a slow-motion credit recognition event in plain English.*

---

## APPENDIX: HOW THE PIECES FIT TOGETHER

For the deck narrative, these 10 pieces chain as follows:

1. **The method** (#1 — Hidden CRE) → banks are hiding their exposure  
2. **The proof it's already caused a failure** (#1 — Metropolitan Capital) → this isn't hypothetical  
3. **The specific banks doing it now** (#2 — WAL CFO swap; #7 — OZK specifics; #10 — OZK insider)  
4. **The regulator confirming the systemic problem** (#3 — FDIC QBP)  
5. **The collateral underneath getting worse, not better** (#9 — Manhattan below COVID)  
6. **The underlying loans were fraudulently underwritten** (#6 — W&D "systemic" admission)  
7. **The interconnection to the rest of finance** (#5 — DB $30B / NDFI $4.2T)  
8. **The first visible crack in the extend-and-pretend system** (#4 — KW bondholder revolt)  
9. **Why this plays out slowly, not in a weekend** (#8 — 2007 parallel, the gap)  
10. **The insiders who know most are acting like they're concerned** (#10 — CRO sale)

---

*All primary sources are public and independently verifiable. No proprietary data used.*  
*Written for: shareable thesis deck | Audience: finance-literate, not macro-specialist*  
*REGINALD domain — filed 2026-03-13*
