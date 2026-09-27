> **Evidence file for `reports/2026-09-27_nano-banc-failure-forensics.md` §1/§5.** Written 2026-09-27 by a read-only Opus research agent for REGINALD; filed verbatim. REGINALD re-verified at primary: the Fed enforcement CSV (4 Nano rows; C&D 2022-01-18, terminated 2025-03-20) and the DFPI 3/6/2026 order text ("unsecured loans to finance real estate", §A). ⚠️ **The "~$260M retained" figures below are SUPERSEDED** by the 9/22/26 base (~$215M) in the main report §3. Do not cite them.

# Nano Banc (cert 58590 / RSSD 3635029): enforcement history, FIRREA claims, syndicate recoveries

Compiled 2026-09-27 (Sun) by a read-only REGINALD research agent. Tags: **P** = primary (regulator, court or SEC document); **P-host** = a primary document read through an advocacy host; **S** = secondary press. "Derived" = my own arithmetic.

---

## §0 Headline findings

1. **The KB's "Fed Cease and Desist Order against Nano Banc on March 4, 2025" is CONTRADICTED.** The Fed's own enforcement database has no Nano action dated 2025-03-04. That date is the **Issuu upload date** ("Published on Mar 4, 2025") of SaveLaguna's copies of Fed documents. In March 2025 the Fed actually **terminated** its C&D (effective 2025-03-20).
2. **The "$108M combined BANC + EFSC" figure is mis-transcribed.** Reuters (10/20/2025, S) says **Banc of California, Enterprise Bank & Trust *and Nano Banc*** sued Stupin over loans "worth a combined $108 million". So it covers **three** lenders, and Nano Banc is one of them. No SEC filing by BANC or EFSC names this exposure.
3. **Nano was a LENDER to the syndicate and was also found liable to Honarkar.**
   - Nano was a lender: the $19MM and $8.5MM Marcil loans, the $27M 901 Ocean loan to Stupin's Coastline, and a ~$20M loan against MOM JV assets.
   - Nano was also a respondent held liable, in a JAMS interim award (2/21/2025), for conspiracy to commit and aiding and abetting fraudulent inducement.
   - Receivership turns all of these claims against Nano into general unsecured claims behind a depositor class that is itself expected to lose about $114M. **Expected recovery for those claimants is close to zero.**
4. **New primary facts since the October 2025 disclosures:**
   - Makhijani was **indicted on 14 counts** (C.D. Cal. 8:26-cr-00087, 6/17/2026). He is detained, and trial is set for **2027-01-12**.
   - Andrew and Julie Stupin filed **Chapter 11** (Bankr. C.D. Cal. 8:26-bk-11202, 4/17/2026).
   - WAL filed a **§523 non-dischargeability** complaint against the Stupins (9/15/2026).
   - WAL wrote off $26.1M of its $98.5M Cantor V loan in Q1-26.

---

## §1 Enforcement history: Fed and DFPI

Where I looked:
- Fed enforcement-action CSV, `federalreserve.gov/supervisionreg/files/enforcementactions.csv`, pulled 2026-09-27. Grepping for nano, allegiant, gressak, chung, makhijani, stupin and marcil returned **exactly 4 Nano rows**.
- DFPI order PDFs and the DFPI press release of 9/25/2026.

| # | Date (effective) | Agency | Type | Respondent | Substance | Termination | Source (P) |
|---|---|---|---|---|---|---|---|
| 1 | 2021-02-24 (announced 2021-03-04) | Fed / FRB-SF | **Written Agreement** (Dkt 20-023-WA/RB-HC, -SM) | Allegiant United Hldgs, Nano Financial Hldgs, Nano Banc | Board oversight; independent governance review; **CRE concentrations** (reduction plan); credit risk; ALLL; capital; 30-day notice before new directors or senior executive officers | **None shown in the Fed CSV** (blank at 2026-09-27) | https://www.federalreserve.gov/newsevents/pressreleases/enforcement20210304a.htm · PDF `/files/enf20210304a1.pdf` |
| 2 | 2021-02-24 | DFPI | Consent order, Fin. Code §580 | Nano Banc | Tangible shareholders' equity (TSE) ≥8.5% through 6/30/21, then ≥9%; 30-day advance notice of board and executive changes; earnings plan | Superseded in practice by #5 | https://dfpi.ca.gov/wp-content/uploads/sites/337/2021/02/NANO-BANC-FIN-CODE-580-ORDER.pdf |
| 3 | 2021-12-15 | DFPI | **Cease & Desist**, Fin. Code §581 | Nano Banc | Shareholders removed 6 directors, installed a new chair and CEO, and put 2 executives on leave without the notice #2 required (DFPI was notified 12/13/21) | n/a | https://dfpi.ca.gov/wp-content/uploads/sites/337/2021/12/Nano-Banc-Financial-Code-581-Order-to-Cease-and-Desist.pdf |
| 4 | 2022-01-18 | Fed | **Cease & Desist** on consent (Dkt 22-001-B-HC, -SM) | Allegiant, NFH, Nano Banc | Recites a targeted exam finding "unsecured loans made to shareholders of Nano Financial"; bank had no permanent CEO or CFO and too few directors; ordered qualified management and directors | **Terminated 2025-03-20**, announced 2025-04-01 | https://www.federalreserve.gov/newsevents/pressreleases/enforcement20220118a.htm · https://www.federalreserve.gov/newsevents/pressreleases/enforcement20250401a.htm |
| 5 | 2022-05-02 | DFPI | Consent order, Fin. Code §580 | Nano Banc | **TSE ≥9.5%**; responds to the Report of Examination issued 1/20/2022 | Not stated | https://dfpi.ca.gov/wp-content/uploads/sites/337/2022/05/Nano-Banc-FC-580-Order-5.2.22.pdf |
| 6 | 2022-09-13/14 | DFPI | **Prohibition** on consent, Fin. Code §585 | Anthony Gressak (50% owner of AUH; CCO 2018–21; acting interim CEO 4/21 to late 2021; resigned 2/22/2022) | Barred from participating in any California-licensed bank without approval | n/a | https://dfpi.ca.gov/wp-content/uploads/sites/337/2022/09/Consent-Order-Gressak-Anthony.pdf |
| 7 | 2024-11-01 (announced 11/12) | Fed | **Prohibition + $75,000 CMP** (Dkt 24-026-CMP-I / -E-I) | Anthony R. Gressak III | Breached #1 WA notice clause; took $194,704.67 undisclosed capital-raise commissions, including a $100K bank advance (Reg O); approved a $148K payroll advance (Reg O); outside entities received **~$15.5M** of PPP, EIDL and RRF funds on false representations | n/a | https://www.federalreserve.gov/newsevents/pressreleases/enforcement20241112a.htm · `/files/enf20241112a1.pdf` |
| 8 | 2024-11-01 (announced 11/12) | Fed | **Prohibition** | James T. Chung (former director) | Fraudulently obtained CARES Act loans and grants | n/a | same release, `/files/enf20241112a2.pdf` |
| 9 | 2026-03-06 | DFPI | Consent order, Fin. Code §580 | Nano Banc | Within **120 days**: TSE ≥9.5% (on top of a fully funded ACL), OR a definitive merger or sale agreement, OR a voluntary liquidation plan. Also liquidity and contingency-funding plan, deposit-concentration and wholesale-funding reduction, CECL validation, reducing CRE and **"unsecured loans to finance real estate,"** workout and accrual discipline | Superseded by closure | https://dfpi.ca.gov/wp-content/uploads/2024/09/Final-Order.pdf (the URL path says 2024; the document is dated **March 6, 2026**) |
| 10 | 2026-09-25 | DFPI | **Possession / closure**; FDIC appointed receiver | Nano Banc | Shareholders' equity fell below the **3% statutory minimum**; failed to comply with #9; prior net loss ~$75.3M | n/a | https://dfpi.ca.gov/press_release/california-seizes-nano-banc/ |

No Fed or DFPI action was found against Makhijani, Stupin or Marcil as institution-affiliated parties.

### Verdicts on each claim

| Claim | Verdict | Basis |
|---|---|---|
| "Fed Cease and Desist Order against Nano Banc on **March 4, 2025**" (KB, sourced to Issuu) | **CONTRADICTED** | Not in the Fed CSV. Issuu pages https://issuu.com/savelaguna/docs/federal_reserve_nano_banc_order_to_cease_and_desis and …/federal_reserve_nano_banc_order_of_prohibition_and both show **"Published on Mar 4, 2025"** as the upload date. The KB took the upload date as the order date. The real Fed C&D is 2022-01-18, and the Fed **terminated** it on 2025-03-20. |
| Fed action Feb 2021 (CRE concentration) | **VERIFIED, with nuance** | Written Agreement 2021-02-24 (#1). It covers CRE concentration **plus** governance, credit, ALLL and capital. It is a WA, not a C&D. |
| DFPI C&D Dec 2021 | **VERIFIED** | #3, dated 12/15/2021 |
| Fed C&D Jan 2022 (insider lending / governance), terminated April 2025 | **VERIFIED** | #4. Termination is **effective 2025-03-20** and was **announced 2025-04-01**; DFPI's "April 2025" is the announcement date. The insider element is "unsecured loans to shareholders." |
| Co-founder / interim CEO Gressak fined and banned 2024 ($15.5M PPP fraud) | **VERIFIED, with nuance** | #7. The CMP is **$75K**. The $15.5M is what his *outside entities* received under PPP, EIDL and RRF; it is not a fine amount. |
| DFPI March 2026 order demanding 9.5% tangible equity | **VERIFIED** | #9, dated **2026-03-06**. 9.5% TSE, or sell, or liquidate, within 120 days (about 2026-07-04, derived). |
| *(not in either fact base)* | NEW | DFPI 5/2/2022 order already required 9.5% TSE (#5). DFPI barred Gressak separately in 9/2022 (#6). Chung was also barred (#8). |

---

## §2 FDIC receivership and claims against Nano (FIRREA)

**Status.**
- FDIC was appointed receiver on 2026-09-25 (P). The Fund number is 10555 (FDIC failed-bank CSV, P).
- The DIF cost estimate is **~$114M** (P). FDIC says the estimate "is expected to change over time as retained assets are sold" (ABA Banking Journal 9/26, S).
- Sunwest assumed about $605M of deposits and $227M of loans (Sunwest release, S/issuer) and bought about $476M of assets (FDIC, P).
- FDIC keeps about **$260M** of assets. Derived: $736M − $476M; American Banker 9/25 gives the same figure (S).
- The holding company, Nano Financial Holdings, is **not** in receivership (FDIC page, P).

**Claims bar date: NOT YET PUBLISHED as of 2026-09-27.**
- Looked at: https://www.fdic.gov/bank-failures/failed-bank-list/nano-banc, the FAQ https://www.fdic.gov/bank-failures/frequently-asked-questions-nano-banc-irvine-ca, and the press release. None gives a bar date.
- The FDIC page does give the filing channel (P): Proof of Claim through the FBCSC portal, NonDepClaimsDal@FDIC.gov, or mail to 600 N. Pearl St. Ste 700, Dallas TX 75201.
- It also states: "the Receiver will not accept a claim filed on behalf of a proposed class… EACH individual or entity must file a separate claim."
- Statute: the bar date must be **no less than 90 days after first publication** of the notice to creditors (12 U.S.C. §1821(d)(3)(B)(i)). **My estimate**, not published: late December 2026 to early January 2027.

**Mechanics, with statute cites:**

| Issue | Rule | Implication for Honarkar, Marcil, WAL or ZION claims against Nano |
|---|---|---|
| **(a) Claims process** | The receiver succeeds to all of the bank's rights and liabilities (§1821(d)(2)(A)). Notice is published and mailed (§1821(d)(3)(B)–(C)). The receiver has 180 days to allow or disallow a claim (§1821(d)(5)(A)). A late claim is disallowed with finality (§1821(d)(5)(C)); the narrow exception is no notice (§1821(d)(5)(C)(ii)). After disallowance or the 180 days, the claimant has **60 days** to sue in federal district court or continue a pre-receivership suit; otherwise the disallowance is final (§1821(d)(6)). There is **no court jurisdiction** over claims against the bank's acts or assets outside this process (§1821(d)(13)(D)). | Anyone holding a pending suit or arbitration award against Nano **must file an administrative claim by the bar date**, or lose the claim, even if the suit is already pending. |
| **(b) Priority / depositor preference** | Order of payment (§1821(d)(11)(A)): (i) receiver's administrative expenses → (ii) **deposit liabilities** → (iii) other general or senior liabilities → (iv) subordinated debt → (v) shareholders. The FDIC page restates this order (P). Recovery is capped at what the claimant would get in a straight liquidation (§1821(i)(2)). | FDIC stands in the depositor class (it is subrogated to the deposits Sunwest assumed) and **already expects to lose ~$114M**. General unsecured creditors are paid only if the depositor class is paid in full. **So a judgment or award creditor such as Honarkar should expect roughly $0**, unless the loss estimate falls to zero, which a $114M hole on a $736M bank makes very unlikely. Secured positions and valid set-offs are outside this waterfall. |
| **(c) Pending lawsuits** | The receiver may obtain a mandatory stay of up to **90 days** for any judicial action (§1821(d)(12)). FDIC is substituted as a party and may remove to federal court within 90 days (§1819(b)(2)(B)). | Known pending matters with Nano as a party (below) will be stayed or substituted and pushed into the claims process. |
| **(d) D'Oench / §1823(e)** | An agreement that diminishes the receiver's interest in an asset is unenforceable unless it is (A) in writing, (B) signed at the time by bank and obligor, (C) approved by the board or loan committee and minuted, and (D) kept continuously as an official bank record (§1823(e)(1)). The same test bars such agreements as the basis of a claim (§1821(d)(9)(A)). The common-law doctrine is *D'Oench, Duhme & Co. v. FDIC*, 315 U.S. 447 (1942); whether it survives *O'Melveny & Myers v. FDIC*, 512 U.S. 79 (1994) is split across circuits, but the statutory bar is unaffected. | This is the main shield against **borrower** lender-liability theories built on side promises, for example Marcil's challenge to enforcement of the $19MM and $8.5MM loans. Pure tort claims such as Honarkar's aiding-and-abetting award are not "agreements," but they still fall into the (b) waterfall. |
| **Does Sunwest take on litigation?** | The Nano purchase-and-assumption (P&A) agreement is **not yet posted** (checked FDIC pages 2026-09-27). FDIC's standard P&A (§2.5 "Borrower Claims") says the assuming bank does **not** assume any liability to borrowers "related in any manner to any loan"; those stay with the receiver. General litigation liabilities are also normally not assumed. | Assume Sunwest takes on **no** Nano litigation liability until the posted P&A shows otherwise. The PR Newswire release discloses no loss-share and no liability details (S). **Re-check once the P&A is posted.** |

**Known proceedings with Nano Banc as a party (P, CourtListener / PACER index):**
- *Marcil et al. v. Nano Banc, Continuum Analytics, Makhijani*, C.D. Cal. 8:26-cv-01143, filed 2026-05-11.
  - The dispute is Nano's **$19MM loan (dated 12/9/2024) and $8.5MM loan** to Marcil entities.
  - On 6/5/2026 the court denied the injunction against Nano's default remedies, referred all claims to a judicial referee under CCP §638, and **stayed and administratively closed** the case.
  - Later entries: "Bond" on 9/16, and a docket short-description "Dismiss Case" on 9/2 whose substance I could not see.
- *U.S. v. Makhijani*: Nano filed a declaration as a non-party on 6/12/2026 (Dkt 19).
- *MOM CA Investco* Ch. 11 (D. Del. 25-10321): Nano was an active creditor, and on 6/9/2025 responded (Dkt 505) to Honarkar's objection to the Tesoro sale.
- *Stupin* Ch. 11: Nano is a listed **creditor** (Dkt 338, 9/11/2026).
- **Nano's claim against the Stupin estate is an asset.** It now belongs to the FDIC-receiver, or to Sunwest if that loan was sold.

---

## §3 Syndicate recoveries

| Item | Latest status (dated) | Tag and source |
|---|---|---|
| **WAL: Cantor Group V LLC** note-finance revolver | $98.5M moved to nonaccrual at 9/30/2025 with a $29.6M specific reserve. **$26.1M charged off in Q1-26** after updated as-is appraisals and "expected duration of the resolution process." **No further charge-off in Q2-26.** WAL holds a limited and a full guaranty from "two ultra-high net worth individuals" that apply in cases such as fraud. | P: WAL 8-K 10/16/2025 https://www.sec.gov/Archives/edgar/data/1212545/000162828025045169/wal-20251016.htm ; 10-Q Q2-26 (filed 7/31/2026) https://www.sec.gov/Archives/edgar/data/1212545/000162828026051418/wal-20260630.htm |
| WAL litigation | The LA Superior Court case **25STCV24263** (filed 8/2025) is against Cantor V and the guarantors. On 8/24/2026 WAL won **relief from stay** in the Stupin Ch. 11 to proceed with it (Dkt 306). On 9/15/2026 WAL filed a **§523 non-dischargeability complaint** against Andrew and Julie Stupin, adversary 8:26-ap-01096 (Dkt 346). | P: Bankr. C.D. Cal. 8:26-bk-11202 via CourtListener |
| **Criminal case** | DOJ says Makhijani "controls Cantor Group V." "Bank #1," which advanced nearly $100M and sued in LASC in 8/2025, matches WAL. The alleged fraud is falsified title policies from 9/2024 to 4/2025. Timeline: arrested 6/10/2026; 14-count indictment 6/17/2026 (bank fraud, 18 USC 1344); not-guilty plea 7/6; detention upheld 8/17; **trial 2027-01-12**, status conference 2026-11-30. | P: USAO-CDCA release 6/10/2026 (FHFA-OIG mirror) https://www.fhfaoig.gov/sites/default/files/Orange-County-Man-Arrested-on-Federal-Criminal-Complaint-Alleging-He-Defrauded-Bank-Out-of-Nearly-$100-Million.pdf ; docket 8:26-cr-00087 |
| **ZION (CB&T)**: two related C&I revolvers to two "related commercial borrowers" that financed mortgage origination and purchase | Full ~$60M provision and **$50M charged off in Q3-25**. Zions sued the guarantors. The 10-K (2/24/2026) repeats "legal action… to pursue recovery… from the guarantors." In the **Q2-26 10-Q** the NDFI net charge-off ratio for 2026 year-to-date is "—" (nil), and **no recovery is disclosed**. **Zions never names Cantor or Stupin in any filing**; EDGAR full-text search for "Cantor" and "Stupin" in ZION filings returns 0 hits. The name link is **S** (Reuters, CNBC 10/2025). On 5/7/2026 Zions **removed its guarantor suit** into the Stupin Ch. 11 (adversary 8:26-ap-01060, Dkt 45). | P: 8-K 10/15/2025 https://www.sec.gov/Archives/edgar/data/109380/000010938025000118/zion-20251015.htm ; 10-K FY25; 10-Q Q2-26 https://www.sec.gov/Archives/edgar/data/109380/000010938026000111/zions-20260630.htm |
| **Stupin personal Ch. 11** | Filed 4/17/2026 (8:26-bk-11202-SC). Official unsecured creditors' committee is active. Bar-date notice filed 6/19/2026 (Dkt 105). Broker retentions were filed in 9/2026, which means assets are being sold. August monthly operating report filed 9/24/2026. **No plan on file as of 9/26.** | P: CourtListener index |
| **BANC / EFSC exposure** | **No SEC disclosure found.** EDGAR full-text search for Stupin, Cantor, Marcil, Honarkar, "MOM CA" and "Hotel Laguna" (2025-06 to 2026-09-27) returns no BANC or EFSC hits; ZION hits appear only under generic language. Both are "Real Property Lenders" to MOM debtor entities (MOM Dkt 394, 5/13/2025, P). BANC filed a statement in the MOM case on the DIP and dismissal motions. Enterprise Bank & Trust has a receiver on Duplex at Sleepy Hollow (Bankr. C.D. Cal. 8:25-bk-12892, P). | P (court); absence checked via EDGAR FTS |
| **"$108M combined"** | The only source is Reuters 10/20/2025 (S), and it covers **BANC + Enterprise Bank & Trust + Nano Banc**. Those three suits were filed April–August 2025. Adding PMF CA REIT (~$7M) gives five suits and about $115M; with WAL and ZION the total exceeds $270M. **No primary source splits the $108M by bank.** | S: https://www.investing.com/news/stock-market-news/investor-behind-zions-western-alliance-bad-loans-is-tied-to-270-million-in-troubled-debt-4297601 |
| **Nano's own syndicate book** (lender side) | **$19MM** (12/9/2024) and **$8.5MM** loans to Marcil entities (P, 8:26-cv-01143 Dkt 30, 46). **$27M** loan to Stupin's Coastline on 901 Ocean, Santa Monica: default notice 5/2025, ~$24M owed, receivership sale at **$26M** in 6/2026 (S, LA Business Journal). **~$20M** loan against MOM JV assets (P-host: JAMS award as summarized; the award is not court-verified). | mixed |
| **Honarkar vs Makhijani / Continuum / Nano** | JAMS No. 5220003126. The partial interim award of **2/21/2025** found Nano liable for **conspiracy to commit and aiding and abetting fraudulent inducement**, with damages or rescission "in amounts to be determined." A partial final award followed on **5/23/2025**. **I found no court confirmation of the award or dollar judgment against Nano.** | P-host: https://issuu.com/savelaguna/docs/jams_arbitration_no._5220003126_partial_interim_aw ; jusmundi index (returned 403) |
| **MOM CA Investco Ch. 11** (D. Del. 25-10321-BLS) | Filed 2/28/2025. **Dismissed by order (Dkt 769) at the 8/18/2025 hearing**; docket closed 10/20/2025. "$382M" is the debtors' estimate of the properties' **undistressed value**, not debt (S). The properties went to state-court receiverships. Hotel Laguna receivership sale had bids due 12/11/2025 (S, elevenflo). | P: CourtListener; S: https://elevenflo.com/blog/mom-ca-investco-chapter-11-bankruptcy |

### Does Nano's receivership change WAL's or ZION's recovery prospects?

Only at the margin.
- **Where the claims sit.** WAL's claims are against Cantor Group V, the Stupin and Marcil guarantors (now inside Stupin's Ch. 11, where WAL is pressing non-dischargeability) and the pledged CRE loans. Zions' claims are against the guarantors, with its suit removed into the same Ch. 11. **Neither bank's recovery runs through a claim against Nano.**
- **Shared collateral.** Nano matters as a **competing lienholder**. Its liens (the $19M and $8.5M Marcil loans, ~$20M on MOM assets, 901 Ocean) keep the same priority under the FDIC-receiver or a loan buyer (§1821(d)(2)(A)). A receiver focused on liquidation may force sales of the ~$260M it retained sooner or cheaper, which could squeeze WAL's junior positions.
- **Suing Nano.** Any aiding-and-abetting or lender-liability claim WAL or ZION might bring against Nano now sits behind a depositor class expected to lose $114M, so it is worth roughly zero.
- **Net.** The recovery drivers are still the Stupin estate, collateral realizations and possible criminal restitution. Makhijani's trial is 1/12/2027.

---

## §4 Press on cause of failure (all S)

| Date | Outlet | What it adds |
|---|---|---|
| 2026-09-25 | American Banker (Ebrima Santos Sanneh), https://www.americanbanker.com/news/embattled-california-bank-is-latest-to-fail | 6th failure of 2026. Recaps enforcement: Feb 2021 CRE; ">half of $886M loans CRE at 12/31/2020"; Dec 2021 C&D; Jan 2022 insider transactions and expenses. Gressak ban. **Does not name Stupin, Marcil, Makhijani or Honarkar.** FDIC retains ~$260M. |
| 2026-09-26 | ABA Banking Journal, https://bankingjournal.aba.com/2026/09/nano-banc-in-california-closed-by-regulators/ | Numbers only; no cause given. |
| 2026-09-25 | PR Newswire / Sunwest, https://www.prnewswire.com/news-releases/fdic-appoints-sunwest-bank-as-nano-bancs-acquiring-institution-302890681.html | $605M deposits and $227M loans assumed; Sunwest's 6th FDIC-assisted deal. |
| 2026-09-25 | DFPI release (**P**), see §1 #10 | Cause: failed to comply with the 3/2026 order; multi-year mismanagement and self-dealing; ~$75.3M net loss; equity below 3%. **Also silent on the syndicate.** |
| 2026-06-11 | American Banker (Kate Berry), https://www.americanbanker.com/news/california-financier-arrested-for-100-million-bank-fraud | Makhijani arrest. Says Makhijani controlled Cantor V and Continuum, with a $25M warehouse line "extended to $100M" at WAL. Names WAL, Zions and Preferred Bank; **not Nano.** |
| 2026-06 | LA Business Journal, https://labusinessjournal.com/real-estate/mdni-wins-ocean-avenue-deal/ | Nano's $27M 901 Ocean loan to Coastline (Stupin): default, receivership, $26M sale. |

**No regulator or press source ties Nano's failure causally to the Stupin/Makhijani book.** Nano's losses on that book (Marcil loans, 901 Ocean, MOM) are plausible contributors to the ~$75.3M loss, but that link is **inference**. The March 2026 order's focus on "unsecured loans to finance real estate" and on workout and accrual practices is consistent with it, but it is not proof.

---

## §5 Could NOT verify

1. The Nano P&A agreement terms and the claims bar date (not posted as of 2026-09-27).
2. Whether the Fed's 2/24/2021 Written Agreement was ever terminated. The Fed CSV shows a blank termination date; it may have been superseded by the 2022 C&D without a separate termination notice.
3. Any dollar award or confirmed judgment against Nano in the Honarkar arbitration. I also could not read the 5/23/2025 partial final award (jusmundi returned 403).
4. The per-bank split of the Reuters "$108M." Any BANC or EFSC charge-off tied to Stupin (none in filings; earnings-call transcripts not checked).
5. The ~$20M Nano loan on MOM assets, which rests only on the award as hosted on Issuu. Elevenflo's "Nano ~$100M+ secured debt" is **S and unreconciled**; treat it as unreliable.
6. The substance of the "Dismiss Case" (9/2/2026) and "Bond" (9/16/2026) entries in Marcil v. Nano (only PACER short descriptions were visible).
7. The WAL v. Cantor Group V adversary 8:26-ap-01076: CourtListener metadata is inconsistent (index date 3/18/2026, before the 4/17 petition). Nature not confirmed.
8. Any ZION recovery or reserve release after Q3-25 beyond the nil 2026 NDFI charge-off figure.
9. The Stupin claims bar-date itself; the notice was filed 6/19/2026 but the date was not visible.
10. The Zions-to-Nano deed-assignment allegation (elevenflo, S only).
