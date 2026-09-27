# Nano Banc failure (9/25/2026): the primary documents
**Date:** 2026-09-27 (Sun) | **Mode:** Thesis | **Confidence:** High on the regulatory record (every order read in full at the issuer) · Medium on the court record (see §4 tiers) · the P&A agreement is NOT YET PUBLISHED
**Commission:** PROME `17a205519` (`prome-09`, Will-directed; Will present) · packet `inbox/2026-09-27_from-PROME_nano-banc-primary-documents-pull.md` · **Research only: no card, no trade.**
**Shared fact base:** `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1 (not re-derived here). **Loss severity / implied haircut = REGINALD's figure** (`AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md`). This file carries no second number and supplies only the document inputs.

---

## Key finding

**The regulators' own orders describe two different failures in sequence.**
- **2021–22 was governance and insider dealing.** The Fed's 2022 cease-and-desist cites "unsecured loans made to shareholders" and Section 23A/23B / Regulation W violations, and freezes all insider and CRE lending.
- **2026 was capital and credit.** The March 2026 consent order covers CRE plus "unsecured loans to finance real estate", classified assets, late loss recognition, CECL, and wholesale funding.
- **The seizure rests on capital alone.** The 9/25 order cites tangible equity of **$5.644M = 0.82% of assets on 9/22/2026**, below the 3% statutory floor, and the missed 120-day deadline. It makes **no governance or fraud finding**.
- **"Self-dealing" appears only in the DFPI press release.** None of the nine DFPI orders or the five Fed orders uses the phrase, or names a borrower, a counterparty or a loan amount.
- **The FDIC has not published the purchase-and-assumption agreement.** No loss-share is stated anywhere.
- **The Material Loss Review is mandatory and belongs to the Fed Board OIG** ($114M > $50M, 12 U.S.C. 1831o(k)). Nothing is posted yet.

---

## Corrections this pull makes to fleet surfaces (verified at the issuer)

| Claim on a fleet surface | What the primary says | Source |
|---|---|---|
| "Fed C&D issued March 4, 2025" (REGINALD `ML-REG-044`; WAL `FRAUD/STUPIN_CRE.md:94`) | **No such action exists.** March 4 is the *announcement* date of the **2021** Written Agreement (dated 2/24/2021). March 2025 is when the 1/18/2022 C&D was **terminated** (effective 3/20/2025, announced 4/1/2025). The claim reverses the direction: the Fed *lifted* an order that month | Fed PRs `enforcement20210304a`, `enforcement20250401a`; H.2 wk ending 4/5/2025 |
| "Feb 2021 Fed action (CRE concentration)" (PROME plan §1; American Banker 9/25) | Narrower than stated. The 2/24/2021 Fed **Written Agreement** is a broad safety-and-soundness agreement with 14 provisions (board oversight, governance review, internal controls, credit risk, **CRE concentrations**, ALLL, capital, liquidity, earnings, audit, dividends, debt, management notice). CRE is one provision, not the subject. DFPI issued a **parallel §580 order the same day** (2/24/2021) | `enf20210304a1.pdf`; DFPI `NANO-BANC-FIN-CODE-580-ORDER.pdf` |
| "the 2024 Final Order" (`dfpi.ca.gov/wp-content/uploads/2024/09/Final-Order.pdf`) | **It is the 3/6/2026 capital consent order.** Only the upload folder is dated 2024/09. It is word-for-word identical to Exhibit B of the 9/25 possession order | DFPI enforcement page; possession order Exh. B |
| "Gressak … $15.5M PPP fraud; fine + ban" | The **$15.5M is the CARES-Act funds (PPP + EIDL + Restaurant Revitalization) received by an entity group he partly owned**. It is not a fine, and not all of it is alleged to be fraudulent ("certain of the applications", "a portion of the funds"). **The fine was $75,000** plus a lifetime ban (Fed, effective 11/1/2024). His full name is **Anthony R. Gressak III** | `enf20241112a1.pdf` pp.3, 5 |
| "Fed terminated its enforcement action in April 2025" (DFPI PR) | Only the **2022 C&D** was terminated (3/20/2025). **No termination of the 2021 Written Agreement appears in any Fed release**, and the C&D says it "does not supersede" the WA (¶19). The WA may still have been in force at failure; this is **unresolved** | `enf20220118a1.pdf` ¶19; Fed PR indexes 2021–2026 |
| "insider trading risks" (DFPI PR 9/25, describing the 2022 Fed action) | The Fed order concerns insider **transactions** (Reg O credit to insiders, 23A/23B affiliate dealing), not insider *trading* | `enf20220118a1.pdf` |
| Total assets "$736M" (FDIC) vs "$690M" (DFPI) | Both are right at different dates: **$736M at 6/30/2026** (Call Report), **$690.9M at 9/22/2026** (the bank's books, possession order Exh. A). For scale, **$909M at 9/30/2025** (Fed Large Bank List). ⇒ ~$218M (−24%) of shrinkage in the final 12 months | FDIC PR; DFPI Exh. A; Fed LBR 20250930 |

---

## 1. DFPI (California): nine documents

Docket per `dfpi.ca.gov/enforcement_action/nano-banc/` [PRIMARY]. dfpi.ca.gov returns 403 to curl, so the PDFs were fetched with a browser-class client (WebFetch) and text-extracted; sha256 hashes are recorded in the Process Report.

| Date | Document | Statute | Signed |
|---|---|---|---|
| 2021-02-24 | Order (bank consented) | Fin. Code §580 | Prosperi, Dep. Commissioner |
| 2021-12-15 | Order to Cease and Desist | §581 | Prosperi |
| 2022-05-02 | Order (consented; **supersedes** the two 2021 orders) | §580 | Prosperi |
| 2022-09-14 | Consent Order v. Anthony Gressak | §585 | not on the enforcement page; found by search |
| 2022-09-29 | Consent Order v. Mark Troncale | §585 | same |
| 2025-04-10 | Termination of the 5/2/2022 Order (replaced by an **MOU effective 3/25/2025**) | — | Mohseni by Prosperi |
| **2026-03-06** | **Consent Order: capital / sell / liquidate** | §580 | Mohseni by Prosperi |
| **2026-09-25** | **Order Taking Possession of Property and Business** | §592(a)(b)(c)(d)(e)(1) | Mohseni |
| 2026-09-25 | Order of Liquidation | §603 | Mohseni |
| 2026-09-25 | Tender of Appointment as Receiver to FDIC | — | listed; not extracted |

### 1a. Order Taking Possession, 9/25/2026 (the seizure). This is what the regulator actually found
- **Equity:** "As of September 22, 2026, the Bank's tangible shareholders' equity had dropped to approximately $5,644,000, which is 0.82% of its total assets. That amount is insufficient to support the Bank's approximately $685,207,000 in total liabilities." (§I.C)
- **Forward losses:** "Due to the condition of its assets, the Bank is projected to continue to realize losses in the immediate future, further depleting its capital and rendering it unable to support its operations on an ongoing basis." (§I.D)
- **The missed order:** the 3/6/2026 Order "required the Bank to, within 120 days of the Order, raise and maintain its tangible shareholders' equity ratio to equal to or greater than nine and one-half percent (9.5%), to enter into a definitive agreement to merge or sell the Bank, and/or to voluntarily liquidate. The Bank has failed to comply with this requirement and therefore is in violation of the Order." (§I.E)
- **Ultimate findings:** "A. The Bank's tangible shareholders' equity is less than three percent (3%) of the Bank's total assets. B. The Bank has inadequate capital. C. The Bank is conducting its business in an unsafe or unsound manner. D. … due to its present financial condition. E. The Bank has violated the Order issued pursuant to Financial Code section 580." (§II)
- **No governance, insider or fraud finding appears in the order.**

**Exhibit A: balance sheet at 9/22/2026, "according to the books of the Bank" ($000).** This is the latest balance sheet anywhere in the public record, 84 days after the 6/30 Call Report that the shared fact base uses.

| Assets | $000 | | Liabilities & equity | $000 |
|---|---:|---|---|---:|
| Cash and due from | 230,859 | | Total deposits | 626,777 |
| FHLB/FRB stock | 5,965 | | FHLB borrowings | 50,000 |
| Investment securities | 39,679 | | Other liabilities | 8,430 |
| **Loans held for sale** | **97,080** | | **Total liabilities** | **685,207** |
| Loans and leases | 322,082 | | Contributed capital | 127,222 |
| ACL | (9,191) | | ESOP comp. (APIC) | 1,323 |
| Net loans | 312,891 | | **Retained earnings** | **(122,000)** |
| Accrued interest | 816 | | Unrealized G/L | (884) |
| Intangibles | 17 | | **Total equity** | **5,661** |
| Other assets | 3,561 | | | |
| **Total assets** | **690,868** | | | |

What the balance sheet shows (DEWEY arithmetic on the exhibit; not the order's words):
- **Tangible equity ratio:** (5,661 − 17) / (690,868 − 17) = **0.817%** ✓ matches the order.
- **Cash was 33% of assets** ($230.9M). The bank was holding liquidity against a deposit bleed.
- **$97.1M of loans had been moved to held-for-sale**, 23% of all loans. The bank was trying to sell loans before the seizure.
- **ACL was 2.85% of held-for-investment loans**, against a 6/30 noncurrent ratio of 25.7% (plan §1).
- **Deposits fell $59M in 84 days** ($686M at 6/30 → $627M at 9/22, −9%).
- **Equity went $39M → $5.7M in one quarter.** The shared fact base's 6/30 equity figure ($39M) is therefore **stale by ~$33M**. The Q3 loss is not in any Call Report.
- **Other liabilities were only $8.4M.** No large litigation liability (e.g. an arbitration award against Nano) was **carried on the bank's books** at 9/22. See §4 for what that means for the $1.34B award.
- ⚠️ **Denominator note for REGINALD / CREED (the one shared figure):** the FDIC's "$476M purchased / remainder retained" is framed on the **6/30** $736M balance sheet. On the **9/22** books ($690.9M), $476M purchased leaves **~$215M**, not ~$260M. Which denominator the retained pool is measured against moves the implied haircut. **This file does not compute it; REGINALD owns it.** The P&A agreement (§3) will settle it.

### 1b. Consent Order, 3/6/2026 (the capital order)
- **Consented:** the Board "executed a Waiver and Consent to the issuance of an order … dated March 6, 2026."
- **¶1, within 120 days** (deadline ≈ **7/4/2026**, DEWEY arithmetic), do one or more of: "(A) Increase the tangible shareholders' equity ratio to equal to or greater than nine and one-half (9 ½) percent … in addition to a fully funded allowance for credit losses"; "(B) Enter into a definitive agreement to merge the Bank … or to sell the Bank to an acquirer acceptable to the Commissioner"; "(C) Provide a plan acceptable to the Commissioner to voluntarily liquidate."
- **¶5 funding:** "a detailed plan to reduce deposit concentration levels and reduce reliance on wholesale non-core deposits … limits for each deposit vertical as well as an aggregate limit for wholesale funding."
- **¶6–7 reserves:** "assessing the overall reasonableness of the ACL relative to key credit metrics such as adversely classified assets, past due and nonaccrual loans, and actual loss histories", then independent CECL validation "to ensure that the model appropriately captures the idiosyncratic risk of the Bank."
- **¶8 CRE:** "Reducing the Bank's CRE concentrations and concentrations in unsecured loans to finance real estate, to a level that is commensurate with the current Board approved limits and risk appetite", plus a 60-day plan "to reduce the level of adversely classified assets."
- **¶9 workouts (the loss-recognition clause):** workout plans "formally approved by the Board of Directors before modifications are granted"; "Ensure timeliness of loan risk rating migration and loss recognition are applied consistently to both secured and unsecured loans"; "Maintain an internal risk rating and accrual/non-accrual designation that accurately and consistently reflects the risk in the loan workout arrangement"; apply "Call Report instructions in designating loan accrual status."
- **¶11–12 management:** an acceptable CEO, chief credit officer and CFO; 30 days' notice and non-objection before any board or executive change.
- **The order has no recitals or findings.** The "why" has to be read from the operative terms. The **$75.3M net loss is cited only in the press release.**
- *Inference (DEWEY, not the order's words):* ¶9 is written the way examiners write it when they have found **late downgrades, late loss recognition and questionable accrual status on modified loans**. That bears on question (c): the reported noncurrent path may *lag* the true deterioration.

### 1c. Order, 5/2/2022 (supersedes both 2021 orders). The only DFPI order with insider language
- Signed by an "acting board." ¶2: a majority-independent board (independent = <10% owner and unrelated to any ≥10% holder).
- ¶4: remediate findings of "the third-party independent report conducted by Sullivan & Cromwell LLP dated August 19, 2021" and the "Report of Examination issued January 20, 2022."
- ¶5 **affiliate transactions:** comply with FRA §§23A/23B and Regulation W.
- ¶6 **insider transactions:** controls on "financial transactions between the Bank and its senior executives, directors, and/or any entities which they control"; Reg O and Fin. Code §1360; an annual list of insider-controlled entities; loan write-ups must disclose "how such loan would impact the financial interests of any senior executives, directors"; reviewers must disclose "any financial relationship with the borrower or guarantor."
- ¶8: controls on the "Business expense process, including the use of corporate credit cards", compensation, and the wire room.
- ¶10 CRE: reduce CRE "including unsecured loans to finance real estate"; appraisals before credit decisions; "improve the accuracy of loan grades, especially for those credits that have been identified by third-party consultants as classified or impaired."
- ¶12: tangible equity ≥ 9½%. ¶22 cites the Fed C&D of 1/18/2022.
- **Terminated 4/10/2025** on the strength of an MOU effective 3/25/2025. DFPI stepped down to an informal action **eleven months before** it issued the capital order.

### 1d. Cease and Desist, 12/15/2021
- ¶3: on 12/13/2021 DFPI "was notified that the shareholders of the Bank's holding company made changes" without the required 30-day notice: "(a) removal of six directors; (b) placement on administrative paid leave of two executive officers; (c) appointment of five individuals as directors; (d) appointment of an individual as chairman and chief executive officer."
- ¶5: this violated Fin. Code §1171 (five-director minimum). ¶6: the acts "may weaken the condition of the Bank." No individuals are named.

### 1e. Order, 2/24/2021 (the first DFPI action)
Consented. ¶3 independent governance review · ¶7 CRE concentration plan · ¶9 tangible equity ≥8.5% through 6/30/21, then ≥9% · ¶5E "due diligence processes for investment purchases" · ¶16 references the **Fed Written Agreement** among the Bank, Nano Financial Holdings, **Allegiant United Holdings LLC** and FRB San Francisco.

### 1f. The two former executives
- **Anthony Gressak, 9/14/2022 (§585 prohibition):** co-purchaser in 2018; 50% owner of Allegiant United Holdings (AUH), a "significant shareholder" of Nano Financial Holdings; chief credit officer from 5/21/2018; "acting interim CEO" April–late 2021; resigned 2/22/2022. **Sole charge:** "In 2020, Gressak approved a monetary transfer to a Nano Banc employee that was characterized as a salary advance although it inaccurately contained repayment terms typical of a loan." Neither admits nor denies.
- **Mark Troncale, 9/29/2022 (removal as President + prohibition):** co-purchaser; the other 50% of AUH; President from 5/21/2018. **Charge:** "in September 2021, Troncale approved a payroll advance reimbursement modification for a Nano Banc employee and was aware that the employee was intending to use the modification to mislead another financial institution regarding the employee's income in order for the employee to obtain better loan terms." Neither admits nor denies.
- ⇒ **Both 50% owners of the controlling shareholder were barred by 2022.** The DFPI charges are narrow employee-advance matters, not insider CRE lending.
- **Makhijani, Continuum, Honarkar, Stupin and Chung appear in NONE of the nine DFPI texts** (full-text search).

### 1g. The seizure press release, 9/25/2026 [PRIMARY, read in full]
- Grounds: "Nano Banc's failure to comply with DFPI's latest enforcement order related to its deteriorating financial condition, as well as a multi-year pattern of executive mismanagement and regulatory violations."
- "Starting in 2020, DFPI discovered significant risk management weaknesses and violations of law, including repeated unauthorized changes to the board and C-suite and **executive self-dealing resulting in financial deterioration**."
- "In March 2026, after Nano Banc reported a net loss of roughly $75.3 million, DFPI issued an order requiring the bank to significantly increase and maintain its available capital … Nano Banc failed to successfully take any of the available actions. Furthermore, its shareholders' equity fell below a statutory minimum of 3 percent."
- "The FDIC has accepted a bid from Sunwest Bank (Sandy, Utah) to assume **all deposits, including all uninsured deposits**, and a substantial portion of its assets." ⇒ The ~57% uninsured share (plan §1) took no loss. The DIF absorbed it through least-cost resolution.
- "In 2022, the Federal Reserve (Fed) took enforcement action related to concerns over governance, compliance, and insider trading risks at Nano Banc. In April 2025, the Fed terminated its enforcement action." (See the Corrections table: "insider trading" should read insider *transactions*, and only the C&D was terminated.)
- DFPI "is also considering additional steps to address risks associated with uninsured deposits and to hold accountable executives that grossly mismanage state-chartered banks." Its framing closes on "Last month, DFPI made a formal submission opposing a federal proposal to weaken oversight over bank management."
- ⚠️ **"Self-dealing" is a press-release characterization with no supporting finding in any published order.** The closest published findings are the Fed's (§2b, §2c): unsecured loans to shareholders, 23A/23B violations, and undisclosed capital-raise commissions.

---

## 2. Federal Reserve (primary federal regulator; state member bank, RSSD 3635029)

Complete list per the Fed press-release indexes 2020–2026, Fed site search ("Nano Banc", 202 hits, paged through 120) and H.2 releases [PRIMARY]. **No Fed release in 2026 through 9/24 mentions Nano.**

| # | Action | Dated / announced | Docket | Status |
|---|---|---|---|---|
| A | **Written Agreement** (FRBSF with Allegiant United Holdings LLC, Nano Financial Holdings Inc., Nano Banc) | dated 2021-02-24 · announced 2021-03-04 | 20-023-WA/RB-HC, 20-023-WA/RB-SM | **No termination found** |
| B | **Order to Cease and Desist Issued Upon Consent** (Board; FDI Act §8(b)(1),(b)(3)) | effective & announced 2022-01-18 | 22-001-B-HC, 22-001-B-SM | **Terminated 2025-03-20**, announced 2025-04-01 |
| C | Gressak: prohibition + $75,000 civil money penalty (§8(e), 8(i)) | effective 2024-11-01 · announced 2024-11-12 | 24-026-CMP-I / 24-026-E-I | final |
| D | **James T. Chung** (director, 2018–2022): prohibition (§8(e)) | same | 24-028-E-I | final |

### 2a. Written Agreement, 2/24/2021
Signed by CEO Mark Rebal, Chairman Randy Rector, and Allegiant members Rebal, Mark Troncale and Anthony Gressak.
- ¶2 board oversight: a plan to "improve the Bank's condition and maintain effective control over … capital, earnings, liquidity, commercial real estate ("CRE") concentrations, internal controls, and audit", including "risk limits including, but not limited to, the CRE lending strategy" (p.2).
- ¶3: an independent third party "to assess the effectiveness of the Bank's corporate governance, board and management structure, and staffing needs" (p.3).
- ¶5: "segregation of duties and dual controls"; "timely and accurate preparation of the Bank's … Call Report"; "improved due diligence processes for investment purchases" (p.4).
- ¶7 concentrations: "a written plan … to strengthen the Bank's management of CRE concentrations, including steps to reduce the risk of the Bank's CRE concentrations" with "a schedule … and timeframes for achieving the reduced levels" (p.5).
- ¶8 ALLL (including "the reliability of the Bank's loan grading system"); ¶9–10 capital, plus a bar on buying or selling assets >5% of total assets without approval; ¶11 liquidity; ¶12 earnings; ¶13 audit; ¶14–15 no dividends, holding-company debt or redemptions; ¶16 §32 notice before new directors or senior officers.
- **No findings narrative and no borrower names**, which is standard for a WA.

### 2b. Cease and Desist, 1/18/2022. The Fed's only stated findings about the bank
Signed by Mark Troncale (President) and Ann Misback (Board). Recitals:
- "following the execution of the Written Agreement, the Reserve Bank conducted a targeted examination of the Bank that identified additional safety and soundness deficiencies at the Bank, **including with respect to unsecured loans made to shareholders of Nano Financial**" (p.2).
- "the Bank is currently operating without a permanent Chief Executive Officer, and Chief Financial Officer, and a sufficient number of board members, which are vital to the safe and sound operations of the Bank" (p.2).

Operative provisions:
- ¶4 Reg O plan.
- ¶5 an independent "Insider Transaction Review" of all insider credit over the prior 2 years, "including but not limited to any loan or personal expense paid to an insider through a corporate credit card".
- ¶6 remediate insider credit "made on preferential terms or presenting more than the normal risk of repayment".
- ¶8–9 **lending freeze:** "the Bank shall not directly or indirectly approve, extend, modify or renew any covered loan … without prior approval from the Reserve Bank." Covered loans include loans to shareholders and insiders **and** CRE, C&I and CRE-financing loans.
- ¶10(c): "**correct the violations of sections 23A and 23B and Regulation W cited in the most recent Report of Examination**" (p.10). This is an explicit statement that affiliate-transaction violations were cited.
- ¶19: "This Order does not supersede the Written Agreement … dated February 24, 2021" (p.14).

No borrower names or amounts.

### 2c. Gressak (C) and Chung (D), effective 11/1/2024. The only published insider-enrichment findings
Gressak (all "WHEREAS", consented without admitting or denying):
- "Gressak organized and voted in favor of shareholder action that caused the Bank to install a new Chief Executive Officer and slate of directors without providing prior notice to the Board of Governors or the Reserve Bank, in violation of the Written Agreement" (p.2). This is the December 2021 event in §1d.
- "as a part of the Company's approximately **$37 million capital raise in 2020**, Gressak and the other founders of the Bank formulated a plan pursuant to which they would receive a commission on the investments, despite that the subscription agreement executed by investors indicated that Bank executives would receive no commissions" (p.2).
- "Gressak received **$194,704.67** in commissions for obtaining capital investments, including $100,000 that he caused the Bank to advance him two months before the capital was funded, in violation of … Regulation O"; he "concealed his commission from the Reserve Bank and the Bank's and the Company's boards" (p.3).
- "on March 24, 2020, Gressak participated in the approval of a **$148,000** employee payroll advance to an executive officer of the Bank, in violation of Regulation O, which permitted the employee to inflate his income to a lender" (p.3).
- He was "a partial owner of a group of corporate entities that received approximately **$15.5 million** in funds provided for by the … CARES Act … (PPP), economic injury disaster loan program, and the Restaurant Revitalization Fund"; "from March 2020 to February 2022, Gressak participated in making materially false representations in connection with certain of the applications for these funds and improperly accepted a portion of the funds for personal expenses" (p.3).
- **Penalty:** lifetime prohibition + **$75,000** CMP (p.5).

Chung: same CARES entity group; "participated in making materially false representations … and improperly used a portion of the funds for unauthorized expenses" (p.2). Prohibition only.

**Makhijani: NOT FOUND in any Fed release** (press indexes 2020–2026: 0 hits).

### 2d. Other Fed context [PRIMARY]
- Fed membership approved 2018-08-03 (H.2 wk ending 2018-08-04).
- Nano Financial acquired 100% of Commerce Bank of Temecula Valley (Board letter 2018-09-26).
- **Large Bank List 9/30/2025: Nano Banc, RSSD 3635029, consolidated assets $909M.**

---

## 3. FDIC: resolution terms

**Press release, 9/25/2026 [PRIMARY]**
- "The FDIC entered into a purchase and assumption agreement with Sunwest Bank of Sandy, Utah to assume substantially all deposits and acquire certain assets of Nano Banc."
- "As of June 30, 2026, Nano Banc reported total assets of $736 million and total deposits of $686 million. … It will also purchase approximately $476 million of the failed bank's assets. The FDIC will retain the remaining assets for later disposition. The FDIC preliminarily estimates that the failure will cost the Deposit Insurance Fund approximately $114 million. The estimate is expected to change over time as retained assets are sold."
- **No loss-share is mentioned.** The press release, the failed-bank page and the FAQ are all silent. The "~$260M retained" figure is American Banker's arithmetic (736 − 476), not an FDIC statement.

**Failed-bank page and FAQ, 9/25/2026 [PRIMARY]**
- The holding company is **Nano Financial Holdings, Inc.** (7755 Irvine Center Dr., Irvine). It is "not included in the closing of the bank or resulting receivership."
- "If you received notice that the FDIC retained your loan…" confirms that some borrowers' loans stay with the receiver.
- **Claims:** Proof of Claim to FDIC as Receiver for Nano Banc, 600 N. Pearl St., Suite 700, Dallas TX 75201 (or the FBCSC portal).
- **Class claims are not accepted.**
- **Priority:** "Depositors · General Unsecured Creditors · Subordinated Debt · Stockholders" (after administrative expenses).
- **No claims bar date is published yet.**

**P&A agreement: NOT YET POSTED (checked 9/27 ~12:3x ET).**
- The failed-bank page carries no agreement link.
- Guessed URLs on the FDIC's pattern (`/bank-failures/purchase-assumption-agreement-nano-banc-irvine-ca.pdf` and variants) return 404.
- **Precedent for timing:** Metropolitan Capital (closed 1/30/2026) has its P&A at `/bank-failures/purchase-assumption-agreement-metropolitan-capital-bank-trust-chicago-il.pdf`, with a server `last-modified` of **2026-02-12**, 13 days after closing. `last-modified` is only an upper bound on first posting. On that analog, expect the Nano P&A around **~10/05–10/09**. It will show the asset schedule (what Sunwest bought vs what the FDIC kept), the bid premium or discount, and whether any loss-share exists.
- **WATCH_FOR for WALTER:** `purchase-assumption-agreement-nano-banc`.

---

## 3b. Material Loss Review (MLR)

- **Statute [PRIMARY: 12 U.S.C. 1831o(k), FDI Act §38(k) as amended by Dodd-Frank §987]:**
  - (k)(1): "If the Deposit Insurance Fund incurs a material loss with respect to an insured depository institution …, the inspector general of the appropriate Federal banking agency shall— (A) make a written report to that agency reviewing the agency's supervision of the institution …, which shall— (i) ascertain why the institution's problems resulted in a material loss to the Deposit Insurance Fund; and (ii) make recommendations for preventing any such loss in the future."
  - (k)(2)(B): "material loss" means any estimated loss in excess of "(iii) $50,000,000, if the loss occurs on or after January 1, 2014, provided that if the inspector general … certifies … that the number of projected failures … will be greater than 30 …, then the definition … shall be $75,000,000 for a duration of 1 year."
  - (k)(3)(B) deadline: "during the 6-month period beginning on the date on which it becomes apparent that the present value of the outlays of the Deposit Insurance Fund … will exceed the present value of receivership dividends."
  - (k)(4): disclosed on FOIA request without the usual excisions, except the names of non-insider customers.
  - Copies go to the Comptroller General, the FDIC, **the state supervisor (DFPI)**, and any Member of Congress on request.
- **Responsible IG:** for a state member bank, the "appropriate Federal banking agency" is the Board of Governors (12 U.S.C. 1813(q)(3)(A)). ⇒ **OIG for the Board of Governors of the Federal Reserve System and the CFPB.**
- **Triggered:** $114M preliminary > $50M, and also > the contingent $75M. The estimate would have to fall by more than 56% to drop below $50M.
- **Status 9/27: nothing posted.**
  - The OIG Ongoing Work page and report list (current through 9/1) do not mention Nano.
  - The only failed-bank item there is a *Nonmaterial* Loss Review of Small Business Bank ($5.7M DIF loss).
  - This is expected two days after the failure.
- **Precedent:** OIG 2024-SR-B-004, *MLR of Heartland Tri-State Bank* (closed 7/28/2023, FDIC estimate $54M). The OIG "received notice that Heartland's failure would result in a material loss" on 8/9/2023; the report was issued **2/7/2024**, about 6 months from notice. It covers about 6 years of supervision and states: "This review fulfills a statutory mandate and does not serve any investigatory purpose."
- ⇒ **Nano MLR expected ~late March to mid-April 2027** (DEWEY inference from the precedent; not a published date). Consistent with PROME's ~2027-03-25 DOCKET row. The review will cover the Fed's supervision **including the 3/20/2025 C&D termination**.

---

## 4. Courts

Sources are court filings retrieved from **CourtListener RECAP** (`storage.courtlistener.com/recap/<path>`, cited per row) [PRIMARY: filing text]. News is tagged. PACER was not used directly; CourtListener throttled at 50 req/hr and PacerMonitor returned 429.

### 4a. Honarkar v. Makhijani et al.: JAMS No. 5220003126 (consolidated with 5200001122), Arbitrator Hon. David A. Thompson (Ret.)
- **Parties:** Mohammad Honarkar and 4G Wireless, Inc. (individually and derivatively for MOM AS/BS/CA Investco LLC) v. Mahender Makhijani; Continuum Analytics, Inc.; the MOM Investor Group and Manager LLCs; **and Nano Banc** (counsel: Hunton Andrews Kurth).
- **Where the text is:** the Partial Final Award (5/23/2025) and the confirming judgment are **Exhibit 1 to *Marcil v. Nano Banc***, C.D. Cal. 8:26-cv-01143, dkt 1-1 (RECAP `gov.uscourts.cacd.1019661.1.1.pdf`). The Partial Interim Award (2/21/2025) is D. Del. 25-10321 dkt 30-1 (`gov.uscourts.deb.195943.30.1.pdf`).
- **The liability holding (Partial Final Award p.35), verbatim:** "In summary, the record is replete with evidence Nano acted in concert with, and was aware of, the MOM Respondents' fraudulent inducement. The Arbitrator therefore finds **Nano jointly and severally liable with the MOM Respondents for conspiracy to commit and aiding and abetting the commission of the fraudulent inducement**. As a consequence, the Arbitrator again finds Claimants are entitled to the alternative remedies of: (a) damages, the specific amount of which will be determined after an accounting is completed; or (b) rescission …"
  - ⇒ **Nano was not itself held to have fraudulently induced Honarkar.** That holding is Makhijani/Continuum/MOM Members'. Nano's liability is **conspiracy and aiding-and-abetting**, jointly and severally.
- **Footnote 29:** "This finding may also constitute a basis for the MOM JV Entities to **set aside the Nano Loan documents** (including the loan agreement, the deeds of trust, and the subsidiary LLC membership interest assignments)". The award also calls the Nano Loan documents invalid for lack of authority (§III.A.1). ⇒ **The $20M Nano Loan, a receivership asset, is exposed to rescission.**
- **What the arbitrator found the bank itself did** (pp.12, 34–35):
  - It issued an LOI for "a $20 million loan (the 'Nano Loan') to the MOM JV Entities, entities that had not yet been formed", to help pay off the LoanCore loan (refinance date **June 8, 2021**).
  - It placed the proceeds in Continuum's account "knowing Continuum was not the borrower".
  - The June 7, 2021 loan-committee memo "falsely stated" the reason.
  - Gressak "overrode opposition" from other officers.
  - "Nano did not record the Nano Loan deeds of trust encumbering the MOM JV Entities' properties until **March 2022**". It "only publicly recorded these deeds of trust **after receiving a Cease and Desist Order from the Federal Reserve**" (i.e. after 1/18/2022).
  - When Honarkar asked for a list of outstanding loans in December 2021, the list sent to him had "the Nano Loan … conspicuously absent."
- **The insider web (p.12), verbatim:** "Nano was founded by, among others, Continuum's legal owner, Shyam, along with several of Continuum's largest investors (**Gerald Marcil, Andrew Stupin, and Bhajneet Singh Malik**), all of whom provided millions in seed capital, remain shareholders in Nano, and **have borrowed over $100 million from the bank**." "Makhijani is one of Nano's largest referral sources and is also involved in the bank's management." The award cites Nano's own designated witness for this.
- **Money assessed against Nano so far:**
  - **Partial Final Award (5/23/2025):** fees and costs of $9,197,426.31; "Nano is jointly and severally liable (with the other Respondents) for **only $5,229,185.14**" (¶IV.14). Damages, restitution and punitive damages were **reserved for the Final Award**, after an accounting.
  - **Partial Interim Award (2/21/2025):** "Nano is liable to the MOM JV Entities for conversion and violation of Section 496". Derivative damages estimated at $45.0M–$169.8M, but "**Nano is only responsible for $21 million of the total ($20 million Nano Loan plus $1 million for the Tesoro Loan)**." Condition: "Respondents may only be liable for the $20 million Nano Loan to the extent the MOM JV Entities remain as the borrowers, their properties are encumbered by the Nano deeds of trust …". §496 trebling "to be determined"; punitive damages found warranted against "Respondents" (Nano included), with the amount deferred.
  - The Partial Final Award **omitted** these derivative findings as stayed by the MOM bankruptcy. That bankruptcy was dismissed 8/18/2025 (§4b).
- **Confirmed as a court judgment:** OC Superior Court 30-2023-01323759-CU-OR-CJC (Hon. Bradley Erdosi); judgment filed **12/5/2025** against the respondents "and Nano Banc"; 10% post-judgment interest. Nano's own brief calls it "confirmed by judgment … on December 5, 2025" (8:26-cv-01143 dkt 32) [PRIMARY].
- **The ~$1.34B Final Award (May 2026):**
  - Bloomberg reporting (Claims Journal, Yizhu Wang, 6/1/2026) [INSTITUTIONAL]: "has led to a roughly $1.34 billion arbitration award … Real estate owner Mohammad Honarkar was 'fraudulently induced' into doing business with financier Mahender Makhijani". **The article does not mention Nano.**
  - A government detention memo in *U.S. v. Makhijani* (8:26-mj-00387 dkt 11, 6/10/2026) [PRIMARY; image-only PDF, read from the rendered page and **DEWEY-verified by eye**]. At p.3, lines 6–9: "In May 2026, an arbitrator awarded approximately $1.34 billion to defendant's former business associate stemming from legal proceedings against defendant and his affiliated entities." At p.9 (page ID #116): "awarded $1.34 billion resulting from arbitration against defendant and others". **Neither passage names Nano.**
  - "$650M+ punitive" and "Nano jointly liable … fraud, oppression, and malice" for the *Final* Award trace only to a newsletter (The Promote) [UNVERIFIED].
  - Laguna Beach Indy (6/19/2026) reports $1.34B including $650M+ punitive [NEWS].
  - Advocacy pages ("Save Laguna" on Issuu) headline Nano "found guilty of Fraud" [UNVERIFIED].
  - ⛔ **Nano's allocation under the Final Award is NOT FOUND.** No confirmation or vacatur petition for it was found. **This is the largest open item for the receivership.**
  - Whatever it is, the bank carried **$8.4M of total "other liabilities" on 9/22/2026** (§1a). So any Final-Award share beyond that was either not accrued, contested or settled.
- **The H1-2026 accrual reversal (lead, unresolved).**
  - REGINALD's Call Reports show accrued expenses (RC-G 1.b) of $44.1M at 12/31/25 falling to $4.2M at 6/30/26, and a *negative* Q2-26 non-interest expense (−$7.2M).
  - **No settlement, release or payment explaining it was found in any filing reached.**
  - Candidates, in DEWEY's order of plausibility, **none verified**:
    - reversal of a litigation accrual after the **12/18/2025 *Security National* defense judgment** (a $37M Nano loan; SNG won $83.25M against the other defendants; timing fits a year-end accrual released in H1-26);
    - payment or bonding of the **Axos v. Nano** verdict (C.D. Cal. 5:19-cv-02092-JGB; jury 5/7/2025; Nano ordered to pay ~**$14M** [NEWS: Law360]; 9th Cir. 25-5563 pending);
    - a Honarkar fee-judgment payment ($5.23M + interest);
    - whatever sits behind the *Marcil v. Nano* entries "Terminate Civil Case" (6/23/2026) and "Dismiss Case" (9/2/2026) (content unread).

### 4b. MOM Investcos Chapter 11: Bankr. D. Del. 25-10321 (BLS), Judge Brendan L. Shannon (**closed; answers WAL O3**)
- **Filed 2/28/2025** (MOM Investcos); the SPEs (Hotel Laguna, Tesoro Redlands DE, Aryabhata, Laguna HI/HW, Masters Building, and others) filed 3/10/2025. CRO Mark Shinderman; claims agent Stretto.
- **DISMISSED 8/18/2025: "Order Dismissing Chapter 11 Cases", dkt 769**, on Honarkar's emergency motion (dkt 611, filed 6/27/2025). CourtListener marks the case terminated 10/20/2025. The MOM *Members'* own Ch.11s (25-10510/-512/-513) were dismissed 5/5/2025.
- **The "$382M" is not liabilities.** It is "an approximated $382 million undistressed value based on appraisals versus $194 million in first-lien secured debt", management's figure, which the CRO did not verify (Shinderman amended first-day decl. ¶44, dkt 152). MOM CA Investco's own schedules show **liabilities $17,273,786.00 and assets $26,330,719.37** (dkt 319).
- **First liens (Shinderman ¶38; ≈$192M):** Enterprise B&T ~$72.2M (several SPEs; NODs Feb 2025) · Preferred $39.0M (Tesoro Redlands) + $28.5M (Aryabhata) · **Banc of California $27.0M (Hotel Laguna, value $82.0M)** · Wilshire Quinn $12.55M · PMF CA REIT $6.54M · Lone Oak $6.5M. Cantor IV/V loans ">$92.5 million", "half … unsecured".
- **Nano in the case:**
  - The petition lists "Nano Banc … Bank loans — **Contingent Unliquidated Disputed**", with no amount.
  - Nano held the debtors' operating accounts (¶33).
  - **The $20M Nano Loan is in neither the CRO's first-lien table nor MOM CA's Schedule D.** It is secured by pledged membership interests in 689 South Coast Hwy LLC, Laguna HI, Laguna HW and The Masters Building, plus "abundance of caution" DOTs.
  - **Current balance: NOT FOUND.**
- After dismissal some SPEs refiled in C.D. Cal. (existence only): Tesoro Redlands DE 8:25-bk-12319 · Aryabhata 8:25-bk-12554 · Duplex at Sleepy Hollow 8:25-bk-12892. Adversary *Honarkar v. MOM CA Investco* 25-50959 (constructive trust).

### 4c. Bank suits against the Stupin/Marcil web: Nano is a **lienholder, not a defendant**
- ***Western Alliance Bank v. Cantor Group V, Marcil, Stupin*:** LA Superior **25STCV24263** (filed Aug 2025), removed as adversary **8:26-ap-01076-SC** (6/25/2026); WAL moved to remand 7/27/2026.
  - Balance "$98,643,500".
  - WAL's Claim No. 5 in the Stupin Ch.11 (8:26-bk-11202-SC, petition 4/17/2026) is **~$173,021,165.87**.
  - Receiver over Cantor V: Chris Neilson (Trigild).
  - Nano appears only as holder of the senior DOTs the doctored title policies omitted (§4x, O1).
- ***California Bank & Trust (Zions) v. Stupin, Marcil, Shyam*:** LA Superior **25STCV30165**, removed as adversary 8:26-ap-01060-SC (5/7/2026); Zions moved to remand 6/1/2026. It records a **Nano leasehold DOT on 535 S Coast Hwy, Laguna Beach, $7,000,000 (rec. 2/28/2019), "assigned to Cantor V" 8/23/2021 and "assigned back to Nano Banc on May 6, 2022"**, and a Cantor V DOT "assigned to Nano Banc". Zions' credit loss is $50M [NEWS: Bloomberg via Claims Journal].
- ***Marcil et al. v. Nano Banc, Makhijani, Continuum*:** C.D. Cal. **8:26-cv-01143-JFW** (filed 5/11/2026, civil RICO). **Nano is also Marcil's LENDER:**
  - a **$19,184,817.74** loan (Dec 2024; amended 9/12/2025; $100,498/mo) and an **$8,500,000** loan (Mar 2019; amended 9/16/2025; $41,832/mo);
  - **Nano noticed default and acceleration 5/1/2026** and Marcil stopped paying;
  - a 12/16/2024 Indemnity Agreement (Marcil indemnifies Nano for Honarkar-consent claims) with releases;
  - request to deposit payments with the court denied 6/5/2026 (dkt 46).
  - Later entries (titles only; **content not read**): "Terminate Civil Case" 6/23 · amended complaint 6/30 · "Preliminary Injunction" 7/22 · "Dismiss Case" 9/2 · "Bond" 9/16.
- ***Security National Guaranty v. Makhijani et al.*:** OC 30-2023-01347034, judgment **for Nano** on derivative claims, 12/18/2025. Jury verdicts: Makhijani $9.25M + $7M punitive; Marcil $9.25M + $15M punitive. Appeal status unknown.

### 4d. The criminal case: *United States v. Mahender Kalicharan Makhijani* (C.D. Cal.)
- Complaint **8:26-mj-00387** (6/8/2026; 18 U.S.C. §1344(1), 2(b)); arrested 6/10/2026.
- **Indictment 8:26-cr-00087-DOC** (6/17/2026; 14 counts; Judge David O. Carter).
- Not-guilty plea to all counts 7/6/2026 (dkt 40). **Trial CONTINUED from 8/11/2026 to 1/12/2027** (answers WAL O2). Stipulation dkt 48 (8/4), minute order dkt 45 (7/24), order dkt 52 (8/5): "Trial continued to 1/12/2027 at 08:30 AM … Status Conference continued to 11/30/2026" [PRIMARY: docket-entry text, DEWEY-verified]. Bond reconsideration granted 8/17 (dkt 86): "ordered detained pending trial". No verdict, plea agreement or restitution order through 8/18/2026 (dkt 89); later entries unchecked.
- DOJ: "Bank #1" advanced "nearly $100 million" to Cantor Group V; the title policies were falsified Sep 2024–Apr 2025. The Real Deal identifies Bank #1 as Western Alliance [NEWS]; DOJ does not.
- **Nano filed as a non-party** (Decl. of Stephanie Yonekura, Hogan Lovells, dkt 19, 6/12/2026):
  - a Travelers check for $618,495.05 payable to "Grothendieck Group LLC and Nano Bank";
  - Grothendieck held a **$5.8M Nano loan** (opened 10/21/2020, closed 8/16/2023) with "Mahender Makijani … listed as the owner/authorized signer" and Stupin as sponsor;
  - "Nano would not endorse the check since it has no current relationship."
- The government's fund-flow table (dkt 11 p.4) places Cantor IV/V, Alessandro Group, Continuum and Makhijani accounts at an unnamed "**Bank #5**". **Whether that is Nano is UNVERIFIED.**
- **No charges found against Stupin, Marcil, Shyam, or any Nano officer.**

### 4e. What passes to the FDIC as receiver (successor to Nano's claims *and* liabilities, 12 U.S.C. 1821(d)(2)(A))
| Matter | Nano's side | Amount / status (latest filing read) |
|---|---|---|
| Honarkar judgment (OC 30-2023-01323759) | judgment debtor | $5,229,185.14 J&S + 10% from 12/5/2025; **Final-Award share unknown**; interim-award derivative exposure $21M (trebling open) + punitive |
| Nano Loan ($20M, 6/2021) to MOM JV entities | lender | balance unknown; **set-aside exposure** (award fn.29) |
| Marcil loans ($19.18M + $8.5M) | lender, in default since 5/1/2026 | RICO counterclaim pending (8:26-cv-01143) |
| Stupin-web borrower Ch.11s (Plaza Continental · Chino Central · Alessandro · Raymond · Ramanujan · Ynez Shops · Stupin) | secured creditor | §4x. Ontario hearing **9/29/2026** |
| Axos v. Nano (5:19-cv-02092) | judgment debtor (~$14M [NEWS]) | 9th Cir. 25-5563 pending |
| Security National v. Makhijani | prevailing defendant | 12/18/2025 |

- **No FDIC substitution or §1821(d)(12) stay request is on any docket reached** (as of 9/27; the bank closed 9/25).
- Claims against Nano now go through the administrative claims process, and **the bar date is not yet published**.
- ⇒ **By the statutory priority (depositors before general unsecured), with the DIF showing a ~$114M loss, the Honarkar judgment and any Final-Award share rank behind the FDIC's subrogated deposit claim and will recover little or nothing.** DEWEY reading of 12 U.S.C. 1821(d)(11); not legal advice.

### 4x. For WAL: O1–O3

**O1: were Nano's four deeds of trust on WAL's collateral still Nano's at 9/25/2026?** (WAL `research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §2, §6)

| # | DOT (face) · property · county | State | Evidence (tier) | As of |
|---|---|---|---|---|
| 1 | $9.72M · 23750 Alessandro Blvd, Moreno Valley · Riverside · **1st** | **UNKNOWN, leaning still-Nano and not foreclosed.** The owner, **Alessandro Group LLC, filed Ch.11 on 8/18/2026** (C.D. Cal. Bankr. **8:26-bk-12516-SC**, Judge Clarkson), reportedly "to halt California property foreclosures" after "scheduled trustee sales". **The foreclosing beneficiary is not confirmed as Nano.** WAL's complaint ¶52 records an NOD on 5/20/2025 without saying under which DOT | Docket exists, last entry a 9/25/2026 MOR [PRIMARY-index]; purpose and $9M balance [UNVERIFIED: search snippets of a paywalled post] | 8/18/2026 |
| 2 | $4,333,151.35 · 3700 Inland Empire Blvd, Ontario · San Bernardino · 2nd (behind Preferred) | **STILL NANO.** "subject to two liens: (1) a lien in favor of Preferred Bank, which is owed approximately $23,131,053 and (2) **a lien in favor of Nano Banc, which is owed approximately $5,131,969**." "In December 2025, Nano Banc obtained the appointment of Douglas Wilson as a rents and profits receiver … pending a nonjudicial foreclosure proceeding. The Debtor's chapter 11 petition was filed on March 30, 2026, to prevent the foreclosure sale from proceeding." Nano still filed as "Creditor Nano Banc" on **9/11/2026** (Doc 90) | *In re Plaza Continental Group LLC*, **8:26-bk-10986-MH**, Doc 88 (status report, 9/8/2026) [PRIMARY] | 9/11/2026 |
| 3 | $5.99M · 12233 Central Ave, Chino · San Bernardino · 2nd | **STILL NANO.** "The Property is encumbered by liens in favor of **Western Alliance Bank and Nano Banc** in the total estimated amount of approximately $19.1 million." Also: "In February 2025, Preferred Bank, **which was then the senior lender**, obtained an appraisal … as-is value of approximately $29 million." Broker estimate now "between $23.5 million and $26.5 million" | *In re Chino Central Group, LLC*, **8:26-bk-10925-SC**, Doc 122 (8/26/2026) [PRIMARY]. ⚠ The filing's address is 12125 Central Ave (Chino Towne Center, a 65.91% TIC interest), not 12233. Same owner; likely the same center; **not verified** | 8/26/2026 |
| 4 | $8.0M · 9826 Cedar St, Bellflower · Los Angeles · 2nd | **UNKNOWN.** No NOD, trustee-sale notice or bankruptcy found for Cedar Street Group LLC. (*Bellflower Cedar, LLC*, 2:24-bk-11656, is a different property.) LA County RR/CC: "Our office does not provide online access to real estate records or indexes." | — | — |

- **No assignment of any of the four to WAL, no reconveyance and no trustee's deed was found.**
- ⇒ **WAL's state (a) "WAL already bought Nano's liens" is contradicted for Ontario and Chino.** Nano was still the lienholder, actively litigating, less than three weeks before failure.
- **State (b) holds for those two:** they pass to the receiver.
- **Chino inference (DEWEY; not stated in any document):** "Preferred … was then the senior lender" (2/2025), and the current liens are "Western Alliance Bank and Nano Banc". So **WAL appears to have bought Preferred's senior Chino loan**: $19.1M − Nano's ~$6M ≈ $13M, which matches WAL's Q1-26 10-Q: "management completed the purchase of a $13 million non-performing senior lien loan during the three months ended March 31, 2026" [PRIMARY: EDGAR `wal-20260331.htm`]. **On Chino, WAL is now senior and Nano (→ FDIC) is junior to it.**
- A second senior-note buyer is **not** WAL. On 2460 S. Grove Ave, Ontario (WAL complaint loan 35), "The senior lienholder is Conejo Loan Investors, LLC, which purchased the loan from Preferred Bank, and which is owed approximately $10.3 million" (*In re Conejo Riverside Group*, 8:26-bk-11647-MH, Doc 77, 9/8/2026) [PRIMARY].
- **Both the Ontario and Chino debtors are investigating avoidance of the Cantor Group V liens that WAL holds as pledgee** (Docs 88, 122) [PRIMARY].
- The Ontario docket also shows "the Debtor has asserted claims for **lender liability** and Nano Banc has asserted claims for breach of lending documents" (Orange County Superior; stayed). That is a claim **against the receivership asset**.
- **Other Stupin-web debtors where Nano is a creditor** (C.D. Cal. Bankr.) [PRIMARY-index]: Raymond Group LLC (8:26-bk-10834; Nano 2nd lien owed ~$4,532,415 behind BofA ~$17,329,603) · Ramanujan Group · Ynez Shops · Andrew & Julie Stupin (8:26-bk-11202, filed 4/17/2026).
- **FDIC-retained vs Sunwest: no per-loan evidence.** The FAQ says only that "Certain lines of credit have been transferred to Sunwest Bank." *Inference:* nonperforming liens inside borrower Ch.11s, one carrying a lender-liability counterclaim, are the class the FDIC typically retains. **The P&A asset schedule (§3) will settle it.**
- **Observable in 2 days:** the Plaza Continental stipulation hearing (Nano is a stipulating party with Preferred) is **Tue 9/29/2026 1:30 pm, Ctrm 6C, Judge Houle**. A substitution or appearance by "FDIC as Receiver for Nano Banc" (or by Sunwest) on 8:26-bk-10986 answers Ontario. Watch 8:26-bk-10925 (Chino) and 8:26-bk-12516 (Moreno Valley) the same way.
- **The recorder check a human can do in ~2 minutes (DEWEY could not):**
  - Riverside (`webselfservice.rivcoacr.org`) and San Bernardino (`arcselfservice.sbcounty.gov`) both run Tyler Self-Service behind a Google reCAPTCHA. Scripted searches return HTTP 500. **DEWEY did not attempt to get around it.**
  - Name Search "NANO BANC", 01/01/2025–09/25/2026; look for ASSIGNMENT OF DEED OF TRUST / SUBSTITUTION OF TRUSTEE / NOTICE OF TRUSTEE SALE / RECONVEYANCE / TRUSTEE'S DEED.
- **Recording-date corrections** (WAL complaint ¶¶75, 81, 86; the dates on WAL's §2 table are the DOT *dates*): Ontario recorded **1/13/2023** · Chino **6/30/2023** · Bellflower **9/27/2024**.

**O2 (Makhijani criminal docket):** indictment 8:26-cr-00087-DOC. **Trial continued from 8/11/2026 to 1/12/2027** (dkt 52). No plea agreement, verdict or restitution order. Detail in §4d.

**O3 (MOM Investcos Ch.11):** D. Del. 25-10321 (BLS). **Dismissed 8/18/2025, "Order Dismissing Chapter 11 Cases", dkt 769**, on Honarkar's motion (dkt 611); CourtListener marks it terminated 10/20/2025. Detail in §4b.

---

## 5. The three questions: answered / not answered

### (a) Did the regulators' orders name CRE concentration as the cause, or governance/self-dealing? **ANSWERED: both, in sequence. Neither was named as the *cause* of failure; the seizure order names capital only.**
| Period | What the orders target | Strongest verbatim |
|---|---|---|
| 2021 (Fed WA + DFPI order, both 2/24/2021) | Broad condition: governance review, internal controls, **CRE concentration as one of ~14 items**, capital ≥8.5–9% | "steps to reduce the risk of the Bank's CRE concentrations" (WA ¶7) |
| Dec 2021–2022 (DFPI C&D; Fed C&D 1/18/2022; DFPI 5/2/2022) | **Governance and insider/affiliate dealing** | "unsecured loans made to shareholders of Nano Financial" (Fed C&D recital); "correct the violations of sections 23A and 23B and Regulation W" (¶10(c)) |
| 2022–2024 (individual orders) | Founders' self-enrichment | $194,704.67 undisclosed capital-raise commissions; $148,000 Reg O payroll advance; $15.5M CARES-funds entity group (Gressak, Fed 11/2024) |
| 2025 | **De-escalation.** Fed C&D terminated 3/20/2025; DFPI 2022 order replaced by an MOU (3/25/2025) | — |
| 3/6/2026 (DFPI consent order) | **Capital, credit quality, loss recognition, funding** | "CRE concentrations and concentrations in unsecured loans to finance real estate"; "timeliness of loan risk rating migration and loss recognition" |
| 9/25/2026 (seizure) | **Capital only** | "tangible shareholders' equity is less than three percent (3%)"; "violated the Order" |

- "Self-dealing" is the DFPI **press release's** word only.
- The only *adjudicated* finding that the bank itself joined the fraud is the **arbitrator's** (§4a), not a regulator's.
- **So what:** the regulatory record supports REGINALD's reading, "origin governance/fraud, mechanism capital". It does **not** support a claim that examiners diagnosed CRE concentration as the failure cause.

### (b) The largest exposures by counterparty, and are they in the retained pool? **PARTLY ANSWERED: several exposures are named with amounts; which pool holds them is NOT ANSWERED (it awaits the P&A asset schedule).**
| Counterparty / cluster | Nano exposure (face or stated balance) | Nature | Source (tier) |
|---|---|---|---|
| **Founder-shareholders Shyam (Continuum), Marcil, Stupin, Malik: aggregate** | "**have borrowed over $100 million from the bank**" | insider-affiliated borrowers | Partial Final Award p.12, citing Nano's own witness (PRIMARY, arbitral finding) |
| Marcil entities | **$19,184,817.74 + $8,500,000** | lender; in default since 5/1/2026; RICO suit against Nano | 8:26-cv-01143 (PRIMARY) |
| MOM JV entities (Honarkar / Continuum JV; Laguna Beach) | **$20M Nano Loan** (6/2021) | pledged LLC interests + DOTs; **set-aside exposure** | award (PRIMARY); balance NOT FOUND |
| Stupin-web property LLCs (DOTs on WAL/Preferred collateral) | $9.72M Moreno Valley (1st) · **~$5.13M owed** Ontario · $5.99M face Chino · $8.0M face Bellflower · **~$4.53M owed** Raymond Group · $7.0M Laguna leasehold (535 S Coast Hwy) · $5M Ramanujan [NEWS] | NPL / in borrower Ch.11s | §4x, §4c (PRIMARY except Ramanujan) |
| Honarkar / 4G (claimant) | Nano owes $5.23M J&S + Final-Award share (unknown) | a *liability*, not an exposure | §4a |

- **These identified items total ≈ $93M of face or stated balance** (DEWEY sum, excluding the "$100M+" aggregate they partly overlap): Marcil $27.7M + MOM $20.0M + Stupin-web DOTs $45.4M. That equals **≈ 29% of the $322M held-for-investment book at 9/22** (a further $97M was held for sale).
- ⚠️ **Overlap and staleness warning:** face amounts are at origination, only two rows are current balances, and the "$100M+" insider figure contains some of the other rows. **Do not add them.**
- **Retained pool: NOT ANSWERED.** No per-loan evidence exists yet. *Inference:* nonperforming, litigated liens inside borrower Ch.11s, with set-aside and lender-liability claims attached, are the asset class the FDIC typically keeps rather than sells to an acquirer.
- **Two observables:** the **P&A agreement** (expected ~10/05–10/09) and the **9/29 Ontario hearing** (who appears for Nano's lien).
- **For CREED's collateral read:**
  - The Chino filing gives a live mark on a Nano-lien property: a Feb-2025 as-is appraisal of ~$29M against a 2026 broker range of **$23.5–26.5M** (−9% to −19%), with liens of ~$19.1M (WAL senior + Nano junior).
  - Hotel Laguna: $27.0M first lien (Banc of California) against an $82.0M value, per the MOM Ch.11 CRO table.
  - These are debtor-side figures, not FDIC marks.

### (c) The fraud timeline vs the noncurrent migration: which came first? **ANSWERED (medium confidence): the insider/fraud conduct came first by three to four years. The noncurrent wave coincides with the fraud being *exposed and litigated* (spring 2025), not with the conduct itself.**
| Date | Event | Source |
|---|---|---|
| 2018 | Allegiant (Gressak/Troncale/Rebal) and founders buy Commerce Bank of Temecula Valley → Nano Banc | Fed 2018 letter; DFPI PR |
| 2020 | $37M capital raise with undisclosed founder commissions; $148K Reg O advance; CARES-funds misrepresentations begin | Fed Gressak order |
| 2/24/2021 | Fed Written Agreement + DFPI §580 order | §1e, §2a |
| **6/7–6/8/2021** | **$20M Nano Loan** funded to not-yet-formed MOM JV entities, proceeds to Continuum; false committee memo | award |
| Dec 2021 | Unnoticed board/CEO coup → DFPI C&D (12/15) | §1d |
| 1/18/2022 → Mar 2022 | Fed C&D (insider loans, 23A/23B); Nano **records** the MOM DOTs only afterwards | §2b; award |
| 2019–2024 | Stupin-web DOTs originated: 9/2019 · 1/2023 · 6/2023 · 9/2024 | WAL complaint |
| Sep 2024–Apr 2025 | Title-policy falsification scheme (the WAL "Bank #1" loans) | DOJ (via detention memo / news) |
| 2023–H1 2024 | Noncurrent **4.5–6.0%** of loans: chronically impaired | REGINALD §2 (Call Reports) |
| H2 2024 | $33.4M of nonaccrual assets **sold** → noncurrent **0.2% at 12/31/24** (report amended 4/18/2025) | REGINALD §2 |
| **2/21/2025** | Partial interim award: Nano liable (conversion, §496; $21M share) | D. Del. dkt 30-1 |
| 2/28/2025 | MOM Investcos Ch.11 | §4b |
| 3/2025 | noncurrent 1.8% | plan §1 |
| **5/20/2025** | **Nano records NODs** on Stupin-web properties (Ontario; Moreno Valley NOD same date, DOT unconfirmed) | WAL complaint ¶¶52, 78 |
| 5/23/2025 | Partial final award (conspiracy / aiding-abetting) | award |
| **6/2025** | **noncurrent 10.2%** (the break) | plan §1 |
| Aug–Oct 2025 | WAL sues Cantor V (8/18); MOM Ch.11 dismissed (8/18); public bank-fraud disclosures (Zions $50M) | §4c |
| 12/2025 | Honarkar judgment (12/5); *Security National* defense verdict (12/18); Nano rents receiver (Ontario); noncurrent **24.3%** | §4a, §4x |
| 2025 FY | Net loss −$75.3M = **legal $46.3M (61%)** + provision $16.7M (22%) + DTA write-off | REGINALD §1 |
| 3/6/2026 | DFPI capital order | §1b |
| 3–8/2026 | Stupin-web borrowers file Ch.11 to stop Nano's foreclosures; Makhijani arrested (6/10); Nano defaults Marcil (5/1) | §4 |
| 9/22 → 9/25/2026 | Equity 0.82% → seizure | §1a |

- **Reading:** the conduct (2020–2021) preceded the credit break by ~4 years. During that gap the book was impaired but not collapsing, and was once cleaned by a sale.
- The break (Q2-2025, 1.8% → 10.2%) lands **in the same quarter as Nano's own NODs on Stupin-web collateral and the partial interim and final awards**. That is roughly five months **before** the fraud became public through other banks (Aug–Oct 2025).
- ⇒ **Nano's book broke when the syndicate's fraud surfaced, and Nano, as the syndicate's own bank, saw it first.**
- **Capital, however, was killed mostly by litigation cost** (REGINALD: legal 61% of the 2025 loss). **The DIF loss (~$114M) will be set by asset marks** on the same collateral.
- **Why only medium confidence:**
  - the Call Reports do not name which loans went noncurrent in Q2-2025;
  - the 3/6/2026 order's ¶9 implies **loss recognition was running late**, so the true deterioration may **precede** the reported path;
  - the award's footnote 29 means some "loans" may not be enforceable assets at all.


---

## Counter-evidence

- **Against "fraud-born, idiosyncratic":**
  - The **March 2026 order is a textbook CRE/credit order**: concentrations, classified assets, workouts, CECL, wholesale funding. It says nothing about fraud.
  - The 2021 WA already listed CRE concentration.
  - A 76%-real-estate book at 322% (446% incl. MI3) CRE-to-capital (REGINALD §2) would be vulnerable without any fraud.
  - Nano **won** *Security National* (12/2025), and the arbitration findings come from **one forum and one arbitrator**, drawing on an advocacy-heavy record.
- **Against "credit killed it":**
  - REGINALD's income statement puts **61% of the 2025 loss in legal expense**.
  - The seizure order finds capital, not asset quality, and says the bank was "projected to continue to realize losses" because of "the condition of its assets". That points at credit, so the documents cut both ways.
- **Against the insider-lending story:**
  - The published *regulatory* findings on insiders are small: $194,704.67 of commissions, a $148,000 advance, and CARES-funds misrepresentations by entities outside the bank.
  - The **"over $100 million" of insider-web borrowing is the arbitrator's finding, not a regulator's.** No published order quantifies insider credit.
  - The Fed **terminated** its insider-focused C&D in March 2025, which reads as examiner satisfaction on that front **18 months before failure**. The Fed OIG MLR is the instrument that will test that decision.
- **Against the timeline reading in (c):** the timing is a coincidence of quarters, not a loan-level link. The Q2-2025 noncurrent jump could equally reflect **examiner-forced reclassification** (the 3/2026 ¶9 language) catching up on loans that had been bad for longer.
- **What would disprove the (c) reading:** loan-level data (the MLR, the P&A asset schedule, or FDIC loan-sale offering memoranda) showing the Q2-2025 noncurrent additions were **not** Stupin/Continuum-web credits.

## Source quality assessment

| Leg | Quality | Notes |
|---|---|---|
| DFPI (9 orders + PR) | **High** | Read in full at the issuer; sha256 recorded; the 3/6/2026 order is confirmed identical to the possession order's Exhibit B |
| Fed (4 actions, statute, OIG) | **High** | Issuer PDFs; H.2 cross-checks. **One gap:** the 2021 WA's termination status |
| FDIC | **High, but incomplete** | PR, failed-bank page and FAQ read in full; **P&A not yet published** |
| Arbitration award | **High on text, medium on weight** | The award text itself, via a court exhibit (RECAP). It is one arbitrator's findings; Nano contested them |
| Bankruptcy / civil dockets | **Medium-high** | Filing texts via RECAP. Several late docket entries were read by **title only** (Marcil dkt 48–72; Alessandro, Chino) |
| $1.34B Final Award | **Medium on existence, NOT FOUND on Nano's share** | Bloomberg via Claims Journal [INSTITUTIONAL]; gov't memo wording not DEWEY-verified |
| Axos ~$14M, Ramanujan $5M, "Bank #1 = WAL" | **Low (news)** | Law360 / Real Deal, paywalled or 403 |

## References (accessed 2026-09-27)

**DFPI** (enforcement page `https://dfpi.ca.gov/enforcement_action/nano-banc/`)
- Seizure PR: https://dfpi.ca.gov/press_release/california-seizes-nano-banc/
- Possession: https://dfpi.ca.gov/wp-content/uploads/2026/09/Nano-Banc-Order-Taking-Possession.pdf
- Liquidation: https://dfpi.ca.gov/wp-content/uploads/2026/09/Nano-Banc-Order-for-Liquidation.pdf
- Tender (listed, not read): https://dfpi.ca.gov/wp-content/uploads/2026/09/Nano-Banc-Tender-of-Appointment-as-Receiver-to-FDIC.pdf
- 3/6/2026 consent order: https://dfpi.ca.gov/wp-content/uploads/2024/09/Final-Order.pdf
- 4/10/2025 termination: https://dfpi.ca.gov/wp-content/uploads/2024/09/Termination-of-Order_Nano-Banc-Redacted.pdf
- 5/2/2022 order: https://dfpi.ca.gov/wp-content/uploads/sites/337/2022/05/Nano-Banc-FC-580-Order-5.2.22.pdf
- 12/15/2021 C&D: https://dfpi.ca.gov/wp-content/uploads/sites/337/2021/12/Nano-Banc-Financial-Code-581-Order-to-Cease-and-Desist.pdf
- 2/24/2021 order: https://dfpi.ca.gov/wp-content/uploads/sites/337/2021/02/NANO-BANC-FIN-CODE-580-ORDER.pdf
- Gressak: https://dfpi.ca.gov/wp-content/uploads/sites/337/2022/09/Consent-Order-Gressak-Anthony.pdf
- Troncale: https://dfpi.ca.gov/wp-content/uploads/sites/337/2022/09/Consent-Order-Troncale-Mark.pdf

**Federal Reserve**
- WA: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20210304a.htm (PDF `files/enf20210304a1.pdf`)
- C&D: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20220118a.htm (`files/enf20220118a1.pdf`)
- C&D termination: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20250401a.htm · H.2: https://www.federalreserve.gov/releases/h2/20250405/default.htm
- Gressak / Chung: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20241112a.htm (`files/enf20241112a1.pdf`, `enf20241112a2.pdf`)
- Large Bank List 9/30/2025: https://www.federalreserve.gov/releases/lbr/20250930/lrg_bnk_lst.txt
- MLR statute: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section1831o · 12 U.S.C. 1813: https://www.law.cornell.edu/uscode/text/12/1813
- OIG: https://oig.federalreserve.gov/reports/work-plan.htm · Heartland MLR: https://oig.federalreserve.gov/reports/board-material-loss-review-heartland-tri-state-bank-feb2024.htm

**FDIC**
- PR: https://www.fdic.gov/news/press-releases/2026/sunwest-bank-assumes-all-deposits-and-certain-assets-nano-banc-irvine
- Failed-bank page: https://www.fdic.gov/bank-failures/failed-bank-list/nano-banc
- FAQ: https://www.fdic.gov/bank-failures/frequently-asked-questions-nano-banc-irvine-ca
- Metropolitan P&A (timing precedent): https://www.fdic.gov/bank-failures/purchase-assumption-agreement-metropolitan-capital-bank-trust-chicago-il.pdf

**Courts (CourtListener RECAP, `https://storage.courtlistener.com/recap/…`)**
- Marcil v. Nano dkt 1-1 (award + judgment): `gov.uscourts.cacd.1019661/gov.uscourts.cacd.1019661.1.1.pdf`; dkt 29–32 (loans, Nano brief)
- D. Del. 25-10321: dkt 30-1 (interim award) `gov.uscourts.deb.195943.30.1.pdf` · dkt 152 (Shinderman) · dkt 319 (schedules) · dkt 611 · dkt 769 (dismissal)
- Plaza Continental 8:26-bk-10986 dkt 88: `gov.uscourts.cacb.2042304/gov.uscourts.cacb.2042304.88.0.pdf`
- Chino Central 8:26-bk-10925 dkt 122: `gov.uscourts.cacb.2041790/gov.uscourts.cacb.2041790.122.0.pdf`
- Conejo Riverside Group 8:26-bk-11647-MH dkt 77 (filed 9/8/2026; retrieved via CourtListener; RECAP path not recorded — search the case number)
- D. Del. 25-10321 dkt 769 (dismissal, filed 8/18/2025), verified by DEWEY: `gov.uscourts.deb.195943/gov.uscourts.deb.195943.769.0.pdf`
- U.S. v. Makhijani 8:26-mj-00387 (dkt 11, 19): `gov.uscourts.cacd.1023892.*`; 8:26-cr-00087-DOC
- WAL v. Cantor Group V verified complaint (25STCV24263): via https://frankonfraud.com/wp-content/uploads/2025/10/Gerald-Story.pdf (third-party host) and WAL's copy (Bloomberg document host), per WAL `research/2026-09-27_…` §2

**News / institutional**
- American Banker, 9/25/2026 21:17 ET: https://www.americanbanker.com/news/embattled-california-bank-is-latest-to-fail
- Claims Journal / Bloomberg, 6/1/2026: https://www.claimsjournal.com/news/national/2026/06/01/337887.htm
- Laguna Beach Indy ($1.34B): https://www.lagunabeachindy.com/news/laguna-beach-property-owner-awarded-1-34b-arbitration-in-fraud-case/article_e83c066d-a23c-4ea9-9099-e0339c1d5a0f.html
- Polsinelli 10/15/2025 (MOM dismissal): https://www.polsinelli.com/news/polsinelli-represents-mo-honarkar-4g-wireless-in-dismissal-of-bankruptcy-cases

**Fleet files cited (not re-derived)**
- PROME plan §1
- REGINALD `reports/2026-09-27_nano-banc-failure-forensics.md` (Call Report anatomy, legal-expense split; uncommitted at read time)
- WAL `research/2026-09-27_nano-banc-receivership-stupin-recovery.md`

## Process report

- **Engine sizing:** document retrieval across four independent source families. **No `/deep-research` fan-out.**
  - Four targeted Opus sub-agents (DFPI · Fed · courts · O1 recorder/liens), all DATA-RETURN.
  - DEWEY ran the FDIC leg directly and verified the load-bearing quotes of every leg against the downloaded texts (grep on the extracted PDFs).
  - About 90 minutes wall-clock.
- **What worked:**
  - WebFetch binary-saves dfpi.ca.gov PDFs that return 403 to curl.
  - CourtListener RECAP holds the award text as a court exhibit.
  - The possession order's **Exhibit A (9/22 balance sheet)** was the single highest-value document in the pull. It postdates every Call Report.
- **What did not work:**
  - County recorders: Riverside and San Bernardino run Tyler Self-Service behind a reCAPTCHA, and LA has no online index. **Not circumvented.** A human 2-minute check is specified in §4x.
  - CourtListener's 50 req/hr cap and PacerMonitor's 429 (docket-entry texts unread).
  - Bloomberg Law, Law360 and the Real Deal are paywalled or 403.
  - The Makhijani detention memo is image-only.
  - The Fed enforcement-search app is JS-backed (press-release indexes and H.2 used instead).
- **Data gaps:**
  - ⛔ Nano's share of the ~$1.34B Final Award.
  - The FDIC P&A (not yet posted) and therefore the retained-pool composition.
  - The claims bar date.
  - The current balance of the $20M Nano Loan.
  - What drove the H1-2026 accrual reversal.
  - Whether the 2021 Fed WA was ever terminated.
  - Moreno Valley / Bellflower lien status.
  - Whether "Bank #5" is Nano.
- **Confidence:** High on the regulatory record and the question (a) answer; medium on (b) and (c); the P&A-dependent items are unknown.
- **If I had more time or tools:** a PACER account (full docket-entry texts); a human recorder search; the P&A once posted (re-run §3 and §5(b)); OCR on the detention memo.
- **Suggestions (BACKLOG candidates):**
  - (1) `recap_pull.py`, a CourtListener RECAP search-and-download helper with throttle-aware backoff (this run hit the cap in ~40 minutes);
  - (2) a WebFetch-binary fallback for dfpi.ca.gov-class 403 hosts;
  - (3) a watch for the `fdic.gov/bank-failures/purchase-assumption-agreement-<slug>.pdf` pattern.
- **Reaped:** all four sub-agents stopped at closeout after their returns were salvaged; none wrote under `AGENTS/`.
