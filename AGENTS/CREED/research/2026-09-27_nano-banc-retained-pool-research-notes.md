> **CREED research-agent notes (Opus subagent, 2026-09-27), committed verbatim for provenance of `analysis/2026-09-27_nano-banc-collateral-read.md` §1.** Read in full by CREED before commit. Tiers are the agent's own; CREED re-tiered where it cited them. "Coordinator" = CREED.

# Nano Banc (FDIC cert 58590) — retained assets & CRE collateral research

Compiled 2026-09-27 (Sun). Tiers: **PRIMARY-READ** = I opened the regulator/court/issuer document myself; **SECONDARY** = news/aggregator/search snippet; **INFERRED** = my arithmetic or reasoning, basis stated. All $ in thousands ($K) where from FDIC API, else as stated.

---

## Headline findings (read first)

1. **The FDIC has not said what the retained assets are.** Neither the press release nor the failed-bank page nor the FAQ gives an asset breakdown, a loss-share, or a P&A agreement link. The only type clue is the borrower instruction "If you received notice that the FDIC retained your loan…", which confirms that the retained pool includes loans. **No loss-share is mentioned anywhere on the three FDIC pages.** (PRIMARY-READ)
2. **"~$260M retained" is not an FDIC figure.** The FDIC release says only "The FDIC will retain the remaining assets for later disposition." The $260M comes from American Banker/Bloomberg and equals **$736M (6/30/26 total assets) − $476M**. On the DFPI's **9/22/26 balance sheet ($690.9M total assets)** the residual is about **$215M** (INFERRED). Treat $260M as a 6/30-basis derived number.
3. **The DFPI seizure order (PRIMARY-READ) has a 9/22/26 balance sheet.** It shows **$97.1M of loans held for sale** (vs $45.0M at 6/30) and **$322.1M of loans held for investment**, gross, with an ACL of $9.2M. Total loans were about **$419.2M against the $227M Sunwest took**, so **roughly $183–192M of loans were retained** (INFERRED; the basis of the $227M is unknown).
4. **Call report, 6/30/26 (PRIMARY-READ via the API):** nonaccrual loans were **$123.2M**: RE $85.6M (non-owner-occupied nonfarm nonres $74.3M, multifamily $7.3M, construction $4.0M), C&I $4.9M, and "all other loans" $32.7M. P9 (90+ days past due and still accruing) was zero everywhere, and **OREO was zero**. Because Sunwest took the $227M of loans, the retained pool **very likely holds most of the nonaccrual book** (INFERRED, not stated by the FDIC).
5. **The four WAL-complaint Nano DOTs are three retail/office strip centers and one 30-unit apartment building.** Alessandro Plaza, Moreno Valley (~119K SF strip center; owner Ch.11 filed 2026-08-18). Plaza Continental, Ontario (~120K SF office/medical-retail; owner Ch.11 SARE filed 2026-03-30). Chino Towne Center pad, Chino (retail/dental; no distress event found). Cedar Group Apts, Bellflower (30-unit MF, 1964; no sale since 1999). **None has been foreclosed as far as I found.** Two owners are in Chapter 11, and Andrew & Julie Stupin are in personal Ch.11 (8:26-bk-11202-SC, filed 2026-04-17). See the new Q2 priority table.
6. **Named CRE collateral found (older detail):** the Stupin/Marcil/Makhijani-network loans are **Inland Empire / LA-County / East Bay commercial property**. None of them is a Laguna Beach MOM property with a Nano first-lien mortgage. Nano does not appear in the MOM debtors' own list of "Real Property Lenders" (PRIMARY-READ). The Honarkar link to Nano is a **$20M Nano loan** that the arbitrator found was improperly secured by JV assets, plus a later **$19.2M Marcil loan** (12/9/2024).

---

## Q1. What the FDIC says about purchased vs retained assets

| # | Item | Verbatim / figure | Source (URL, date) | Tier |
|---|---|---|---|---|
| 1.1 | Transaction | "The FDIC entered into a purchase and assumption agreement with Sunwest Bank of Sandy, Utah to assume substantially all deposits and acquire certain assets of Nano Banc." | https://www.fdic.gov/news/press-releases/2026/sunwest-bank-assumes-all-deposits-and-certain-assets-nano-banc-irvine (2026-09-25) | PRIMARY-READ |
| 1.2 | Size | "As of June 30, 2026, Nano Banc reported total assets of $736 million and total deposits of $686 million." | same | PRIMARY-READ |
| 1.3 | Purchased vs retained | "Sunwest Bank agreed to assume substantially all deposits at the time of closing. It will also purchase approximately $476 million of the failed bank's assets. The FDIC will retain the remaining assets for later disposition." | same | PRIMARY-READ |
| 1.4 | DIF cost | "The FDIC preliminarily estimates that the failure will cost the Deposit Insurance Fund approximately $114 million. The estimate is expected to change over time as retained assets are sold." | same | PRIMARY-READ |
| 1.5 | Loss-share | **Not mentioned** on the press release, failed-bank page or FAQ. None of the three pages links to a P&A agreement. | 3 FDIC pages (all "Last Updated: September 25, 2026") | PRIMARY-READ (absence on these 3 pages only) |
| 1.6 | Retained-asset type | The only hint is on the failed-bank page: "If you received notice that the FDIC retained your loan, and you have questions, please visit the FDIC Information and Support Center." That confirms loans are among the retained assets. The page has **no breakdown** by loans, OREO or securities. | https://www.fdic.gov/bank-failures/failed-bank-list/nano-banc (2026-09-25) | PRIMARY-READ |
| 1.7 | Lines of credit | FAQ: "Certain lines of credit have been transferred to Sunwest Bank." Also: "Your 1098 reporting will be done by the FDIC or the servicer of your loan." | https://www.fdic.gov/bank-failures/frequently-asked-questions-nano-banc-irvine-ca (2026-09-25) | PRIMARY-READ |
| 1.8 | Loans assumed | "The assumed deposits total approximately $605 million and assumed loans total $227 million." (from Sunwest, not the FDIC) | https://www.prnewswire.com/news-releases/fdic-appoints-sunwest-bank-as-nano-bancs-acquiring-institution-302890681.html (2026-09-25 19:45 ET) | PRIMARY-READ (issuer release) |
| 1.9 | "$260M retained" | American Banker (Bloomberg): FDIC "will retain roughly $260 million of Nano Banc's assets for later disposition". **This number is not in the FDIC release.** It equals 736 − 476. | https://www.americanbanker.com/news/embattled-california-bank-is-latest-to-fail (2026-09-25 9:17pm EDT) | SECONDARY (derived figure) |
| 1.10 | DFPI balance sheet 9/22/26 ($K, Exhibit A to seizure order) | Cash & due 230,859 · FHLB/FRB stock 5,965 · Investment securities 39,679 · **Loans HFS 97,080** · Loans & leases 322,082 · ACL (9,191) · Net loans 312,891 · Accrued int 816 · Intangibles 17 · Other 3,561 · **Total assets 690,868** · Deposits 626,777 · FHLB 50,000 · Other liab 8,430 · Total liab 685,207 · Contributed capital 127,222 · ESOP/APIC 1,323 · **Retained earnings (122,000)** · Unrealized (884) · **Equity 5,661**. My footing check: the assets sum to 690,868 exactly. | https://dfpi.ca.gov/wp-content/uploads/2026/09/Nano-Banc-Order-Taking-Possession.pdf (order dated 2026-09-25) | PRIMARY-READ |
| 1.11 | DFPI findings | "As of September 22, 2026, the Bank's tangible shareholders' equity had dropped to approximately $5,644,000, which is 0.82% of its total assets." "Due to the condition of its assets, the Bank is projected to continue to realize losses in the immediate future…" The bank also failed to comply with the 3/6/2026 §580 order (9.5% tangible equity within 120 days, or sell or liquidate). | same | PRIMARY-READ |
| 1.12 | DFPI press release | "In March 2026, after Nano Banc reported a net loss of roughly $75.3 million, DFPI issued an order…" and "Nano Banc holds total assets of roughly $690 million. The FDIC has accepted a bid from Sunwest Bank … to assume all deposits, including all uninsured deposits, and a substantial portion of its assets." | https://dfpi.ca.gov/press_release/california-seizes-nano-banc/ (2026-09-25; read via WebFetch extraction, since curl returned 403) | PRIMARY-READ (via fetch tool) |
| 1.13 | Retained on the 9/22 basis | 690.9 − 476 ≈ **$215M** (vs $260M on the 6/30 basis) | arithmetic | INFERRED |
| 1.14 | Retained loans | Gross loans 9/22 = 322.1 HFI + 97.1 HFS = **$419.2M**, minus $227M assumed = **~$192M gross / ~$183M net of ACL**. That leaves about $30M of other retained assets (FHLB/FRB stock, part of the securities/cash, other). Caveats: I don't know whether the $227M is book or discounted value, or whether it is dated 9/22 or 9/25. | arithmetic | INFERRED |
| 1.15 | FDIC failures API | The `api.fdic.gov/banks/failures?filters=CERT:58590` query returns 0 rows because the index was built 2026-08-25, before the failure. That is a stale index, not an unpublished record. The institutions API still shows ACTIVE=1 (index built 2026-09-25 11:54Z, before closing). | API, 2026-09-27 | PRIMARY-READ |

Retrieval shapes tried for the P&A agreement and asset detail: press release HTML, failed-bank page HTML (all links enumerated, no P&A/PDF/loss-share link), FAQ HTML (a PDF version link exists, not opened), failures API. nanobanc.com returned 403. **The FDIC normally posts the P&A agreement later, so it is not yet available. That is not the same as unpublished.**

---

## Q2 (priority per coordinator update). The four WAL-complaint Nano DOTs: property type, size, and status after mid-2025

The liens come from the WAL Verified Complaint dated 2025-08-18 (LA Superior). The **case no. 25STCV24263 was supplied by the coordinator**; the copy I read (frankonfraud.com PDF) has a blank "CASE NO." caption. I read the lien and NOD text myself (PRIMARY-READ, third-party-hosted copy).

| Nano DOT | Property / type | Size | Status after mid-2025 | Sources | Tier |
|---|---|---|---|---|---|
| **(a) 23750 Alessandro Blvd, Moreno Valley** ($9.72M, 1st, DOT 8/29/2019; NOD rec. 5/20/2025). Owner: Alessandro Group, LLC | **"Alessandro Plaza"**, a multi-tenant **community retail / strip center** with restaurants, services, dental and professional office. Bondoro: "a strip mall". | **~119,298 SF** (The Registry SoCal headline "119,000 SQFT"; another Registry headline says "84,000 SQFT … Listed for Sale for $14.2MM" / "$15MM", so the sale perimeter probably differs). NMRK leasing brochure (2023): "Space Available ±1,500-40,000 Square Feet", with many "Available" suites, i.e. material vacancy. | **Owner filed Chapter 11 on 2026-08-18**, C.D. Cal. **No. 26-12516** (affiliated debtors noted as Andrew & Julie Stupin); $10–50M assets and liabilities. An X/RK Consultants post says it filed "to halt California property foreclosures". This is **still owner-held and in bankruptcy, not foreclosed** as of the 8/19/2026 alert. The listed-for-sale history ($14.2M–$15M asks) is undated in the snippets. | https://bondoro.com/alessandro-plaza-owner-filing-alert/ (2026-08-19, read); https://morenovalleybusiness.com/wp-content/uploads/2023/10/Alessandro-Plaza-Brochure-NMRK.pdf (Oct 2023, read); theregistrysocal.com (429 on fetch, from search snippets); Yelp tenant listings | SECONDARY (bondoro, brochure read directly = issuer/broker doc) |
| **(b) 3700 Inland Empire Blvd, Ontario** ($4.33M, 2nd behind Preferred $25.9M; NOD on the Nano DOT rec. 5/20/2025). Owner per WAL: Plaza Continental, LLC | **"Plaza Continental"**, an **office/medical + retail center** at 3700–3760 Inland Empire Blvd on I-10. Tenants include realty/mortgage offices and a family medical center. | **~120,000 SF**; ~24% available at filing (elevenflo) | Nano sued Plaza Continental Group LLC in OC Superior on (July 11) 2025 over a $4.3M loan (Law.com Radar snippet). **Plaza Continental Group LLC filed Chapter 11 (SARE) on 2026-03-30**, C.D. Cal. **8:26-bk-10986-MH**, $10–50M. Manager Rafael Duarte (Newport Beach). **No foreclosure sale, receivership or plan as of the 2026-09-08 update.** | https://elevenflo.com/blog/plaza-continental-group-chapter-11-bankruptcy (upd. 2026-09-08, via WebFetch); LoopNet/Showcase (403, from search snippets) | SECONDARY |
| **(c) 12233 Central Ave, Chino** ($5.99M, 2nd behind Preferred $22.4M, DOT 1/26/2023). Owner: Chino Central Group, LLC | Inside **"Chino Towne Center"** (12101–12233 Central Ave, at Central & Philadelphia): a **neighborhood retail center** anchored by CVS (13,013 SF) and 24 Hour Fitness (45,000 SF) plus Chase. The 12233 address itself houses **dental offices** (Aava, Ocean Dental, formerly Coast Dental/SmileCare). | Total center SF **not found**. It is unknown whether Chino Central Group's parcel is the whole center or one pad. The $22.4M Preferred 1st (2016) suggests a sizable parcel (INFERRED). | **No sign of foreclosure, sale, receivership or bankruptcy found** (search only; LoopNet/NMRK pages 403; assessor not reached). The WAL complaint gives no NOD for this DOT. | LoopNet/NMRK listing snippets; bippermedia; Yelp | SECONDARY |
| **(d) 9826 Cedar St, Bellflower** ($8.0M, 2nd behind Umpqua $6.47M; DOT 9/16/2024, rec. 9/27/2024). Owner: Cedar Street Group LLC | **Multifamily**: "Cedar Group Apartments", 30 units, 2 stories, built 1964, pool | **25,024 SF building; 0.91 ac (39,613 SF land); 30 units, 54 bd / 30 ba**; APN 7161-017-007 | Redfin public record (page "Last updated August 2026") still shows **last sale 1999-01-22 for $1,370,000**, so **no recorded sale or foreclosure transfer** in that feed. No NOD for this DOT in the WAL complaint. Liens of $6.47M + $8.0M = **$14.47M on 30 units ≈ $482K/unit**, very high for a 1964 Bellflower asset. That implies **Nano's 2nd is likely deeply under-secured** (INFERRED). | https://www.redfin.com/CA/Bellflower/9826-Cedar-St-90706/home/7547184 (read); apartments.com / LoopNet parcel (snippets) | SECONDARY / INFERRED |

**Related Stupin bankruptcies:** Andrew & Julie Stupin filed a personal **Chapter 11 on 2026-04-17**, C.D. Cal. **8:26-bk-11202-SC** (Judge Clarkson); Zions has an adversary proceeding in it, **8:26-ap-01060**. PacerMonitor PDFs returned an HTML login page, so the schedules were not read. **Stupin's Schedule D/E-F is where Nano's guaranty claims would appear. That goes to the docket agent.** (SECONDARY: bkdata.com, PacerMonitor listing snippets)

**Where these loans sit now (FDIC vs Sunwest):** **not disclosed anywhere I could reach.** All four collateral owners and Blackhawk (Ramanujan) are in default, in NOD, or in Chapter 11. Three of the five borrowers are in bankruptcy, and Nano holds **second liens on 4 of 6** named collateral positions. A purchaser of a "performing-loan" pool would normally exclude such credits, so they **most likely sit in the FDIC-retained pool** (INFERRED; the FDIC has published no asset list). The same applies to the $19.2M Marcil loan (Nano had declared a default; the borrower is suing) and the $20M JV loan found improper in arbitration (INFERRED).

### Nano's ~$20M loan on the Honarkar / MOM side: what is and isn't known
- **Known (SECONDARY):** the arbitrator found a $20M Nano loan was used in place of the promised $30M equity contribution. It was "secured against the JV's own assets" / "assets previously owned by" the Honarkar parties "without their informed consent" (LB Indy 2026-06-19; issuu/TDM summaries of the 2025-02-21 interim award). TRD (2026-06-18) says the funds were "diverted … to … Continuum Analytics". The Zions litigation reportedly found a Laguna Beach building on which it held a first lien had "deeds … assigned to Nano Banc" (Bloomberg via ZeroHedge, 2025-10-17).
- **Not found:** the borrower entity of record, the specific Laguna Beach parcel(s) securing the $20M, the lien position, and the current balance. The MOM debtors' own motions (PRIMARY-READ) **omit Nano from "Real Property Lenders"**. That suggests the $20M was not a recorded first mortgage on the SPE-debtor properties, or had been reassigned or released by 2025 (INFERRED). **Coordinator note:** the Marcil suit alleges the $19.2M Marcil loan (12/9/2024) was used to "clear up" this exposure. If so, the $20M may now be economically embedded in the defaulted Marcil credit rather than being a separate MOM-secured loan (INFERRED from the TRD account of Marcil's allegations).

### 2a. Loans and liens with a named property (Nano as lender)

| Property | Type | City | Nano loan / lien | Lien position | Status (date of fact) | Source | Tier |
|---|---|---|---|---|---|---|---|
| 23750 Alessandro Blvd, Bldgs G,H,I **and** A,B,O,N (owner Alessandro Group, LLC) | not stated. Reuters says the Cantor-case collateral was "store-fronts and office buildings" | Moreno Valley (Inland Empire) | DOT for **$9,720,000**, dated 8/29/2019, recorded 9/9/2019. The same DOT is cited for both building groups, so count it once. | **1st** (per Stewart Title policy cited by WAB) | "Notice of Default and Election to Sell under Deed of Trust recorded on May 20, 2025". The complaint doesn't say which DOT, in the Collateral Loan 33 paragraph | Western Alliance Bank v. Cantor Group V, Marcil, Stupin, **Verified Complaint**, LA Superior Court, dated 2025-08-18, reproduced in https://frankonfraud.com/wp-content/uploads/2025/10/Gerald-Story.pdf (Oct 2025) | PRIMARY-READ (court complaint text, via third-party host) |
| 3700 Inland Empire Blvd (owner Plaza Continental, LLC) | not stated (office per name; INFERRED) | Ontario (Inland Empire) | DOT **$4,333,151.35**, dated 11/10/2022, rec. 1/13/2023 | **2nd** behind Preferred Bank $25.9M (4/7/2022) | "Notice of Default and Election to Sell under Deed of Trust **with regard to the Nano Banc deed of trust** recorded on May 20, 2025". Nano sued Plaza Continental Group LLC on July 11 (2025) in OC Superior Court over "a $4.3 million real estate loan secured for a property in Ontario". | Same WAB complaint; Law.com Radar card https://www.law.com/radar/card/ca-orangecounty-525420-banc-v-plaza-continental-group-llc (page is JS-only, the suit detail is from the search snippet) | PRIMARY-READ (lien, NOD) / SECONDARY (suit) |
| 12233 Central Ave (owner Chino Central Group, LLC) | not stated | Chino (Inland Empire) | DOT **$5,990,000**, dated 1/26/2023, rec. 6/30/2023 | **2nd** behind Preferred Bank $22.4M (2016) | No status given | Same WAB complaint | PRIMARY-READ |
| 9826 Cedar St (owner Cedar Street Group LLC) | apartment complex (Bloomberg via ZeroHedge: "an apartment complex in Bellflower") | Bellflower (LA County) | DOT **$8,000,000**, dated 9/16/2024, rec. 9/27/2024 | **2nd** behind Umpqua $6.47M (2018) | No status given | Same WAB complaint; ZeroHedge repost of Bloomberg (2025-10-17) | PRIMARY-READ / SECONDARY (type) |
| Blackhawk Plaza (owner Ramanujan Group LLC, a Stupin entity) | ~250,000 SF luxury retail center | Danville (Contra Costa, East Bay) | **$5M** loan (2024 origination per elevenflo) | **2nd** behind Preferred Bank ~$31M | Payments stopped Mar 2025. Nano sued in OC Superior Court (summer 2025). Receivership ordered **2026-02-03**. Ramanujan filed Ch.11 **2026-03-18**, C.D. Cal. **8:26-bk-10832-SC**, which stayed the receivership. Liens total $35.8M plus $657,111 of taxes. The debtor intends to sell (KW Commercial/CBRE). 2023 appraisal $57.38M. | danvillesanramon.com 2026-01-21 (Lyman) and 2026-07-02 (Lyman); elevenflo.com/blog/blackhawk-plaza-chapter-11-bankruptcy (2026-03-31, upd. 2026-09-08) | SECONDARY |
| Laguna Beach building (unnamed) | commercial | Laguna Beach | "for one property it [Zions] had a first lien on, a building in Laguna Beach, the deeds were assigned to Nano Banc" | disputed | 2025-10 | Bloomberg via ZeroHedge https://www.zerohedge.com/economics/bizarre-bankruptcy-heart-latest-regional-bank-meltdown (2025-10-17) | SECONDARY (the address was **not found**; I searched but couldn't reach the Zions complaint text) |
| Sand City "eco-resort" (Security National Guaranty / Evariste Group) | entitled beachfront resort land ("$150 million in beachfront property") | Sand City, Monterey County | **$37M** loan by Nano to Evariste (a Makhijani-affiliated entity), taken out ~Aug 2023 "without SNG's knowledge or consent" (per SNG) | not stated | SNG sued 9/2023 (OC Superior Court). Judgment **2025-12-18** (Judge Shawn Nelson): Nano was **not liable** on aiding-and-abetting claims. I found no report of the loan's own performance. | montereycountynow.com (2025, 7/24/25 print); https://www.hunton.com/news/hunton-wins-significant-defense-verdict-for-nano-banc-defining-limits-of-aiding-and-abetting-liability-for-banks | SECONDARY |

### 2b. Loans with borrower named but collateral not identified

| Borrower | Amount | Terms / status | Source | Tier |
|---|---|---|---|---|
| Gerald J. Marcil & Marcil Family Trust | **$19,184,817.74** (loan dated 2024-12-09) | Marcil alleges the proceeds were withdrawn the same day, that the loan was used to "clear up" the Honarkar-arbitration exposure, and that there was an indemnity for Nano's arbitration losses. Nano declared a default and "threatened to foreclose on his real estate portfolio". Marcil v. Nano Banc, **C.D. Cal. 8:26-cv-01143**, filed **2026-05-11**. Nano's filings say Marcil is sophisticated and read the documents. | TRD 2026-06-18 (Keith Larsen) https://therealdeal.com/new-york/2026/06/18/mahender-makhijanis-alleged-con-of-gerald-marcil/ ; the loan date/amount comes from a search snippet of PacerMonitor/Justia (both 403 on fetch) | SECONDARY |
| Andrew Stupin (guarantor) | Nano + Banc of California + Enterprise combined **$108M** | Separate suits filed Apr–Aug 2025. **Nano's own share is not broken out.** | Reuters 2025-10-20 (Gillison et al.), read at https://kfgo.com/2025/10/20/investor-behind-zions-western-alliance-bad-loans-is-tied-to-270-million-in-troubled-debt/ | SECONDARY |
| Founders / insiders (Marcil, Stupin, Shyam, Malik) | "more than $100 million" | "Nano Banc had loaned the founders more than $100 million, according to a March [2025] arbitration filing". Makhijani is "one of the largest referral sources". | Bloomberg via ZeroHedge (2025-10-17); substack repost | SECONDARY (arbitration filing not read) |
| MOM JV side (Makhijani/Continuum) | **$20M** | Per the arbitration: used in place of the promised $30M equity and "improperly secured by assets previously owned by" Honarkar parties "without their informed consent". TRD reports the funds were "diverted … to … Continuum Analytics". The specific collateral parcels were **not identified** in anything I could read. | LB Indy 2026-06-19; TRD 2026-06-18; issuu/Save Laguna summaries | SECONDARY |
| Honarkar personally | unspecified | "Honarkar took out various loans through Nano Banc and Continuum to help with other financial obligations, both personal and professional." | OCBJ 2023-05-15 https://www.ocbj.com/oc-homepage/battle-over-laguna-beach-portfolio-turns-ugly/ | SECONDARY |

### 2c. MOM CA Investco Chapter 11 and the arbitration

| Item | Fact | Source | Tier |
|---|---|---|---|
| Case | **In re MOM CA Investco LLC, et al., Bankr. D. Del. No. 25-10321 (BLS)**, jointly administered. The MOM Investcos filed **2025-02-28**; 20 SPE debtors followed on 2025-03-10 and 2025-03-31. | Doc 394 (filed 2025-05-13) and Doc 280 (filed 2025-04-22), read at https://www.dailydac.com/wp-content/uploads/2025/05/MOM-CA-Investco-LLC-et-al.pdf and https://www.dailydac.com/wp-content/uploads/2025/05/MOM-CA-Investco-LLC.pdf | PRIMARY-READ |
| SPE debtors (property holders) | Retreat at Laguna Villas; Sunset Cove Villas; Duplex at Sleepy Hollow; Cliff Drive Properties DE; 694 NCH Apartments; Heisler Laguna; Laguna Festival Center; 891 Laguna Canyon Road; 777 AT Laguna; Laguna Art District Complex; Tesoro Redlands DE (188-unit apartments, 106 W Pennsylvania Ave, Redlands); Aryabhata Group; Hotel Laguna (ground lease); 4110 West 3rd Street DE; 314 S. Harvard DE; Laguna HI; Laguna HW; The Masters Building; 837 Park Avenue; Terra Laguna Beach (interim). Portfolio = "hotels, an apartment complex, office buildings, other commercial real estate, and individual homes used as luxury vacation rentals"; ~60 SPEs in total. | same | PRIMARY-READ |
| **Nano's position in the case** | The debtors define "**Real Property Lenders**" as "Enterprise Bank & Trust, PMF CA REIT, LLC, Lone Oak Fund, LLC, Wilshire Quinn Income Fund, LLC, Preferred Bank, and Banc of California". **Nano Banc is not on the list, and neither motion mentions it at all** (0 hits). The DIP lender is Specialty DIP, LLC. | same | PRIMARY-READ |
| Nano's claim in the case | **Not found.** I did not reach a claims register (Stretto URL returned 404). A docket agent should check the claims register and Schedule D. | — | not reached |
| ~$382M | "estimated undistressed value of approximately $382 million" (a property **value**, not debt). The petition reported $100M–$500M of assets and liabilities. | bondoro.com/mom-investcos (undated); elevenflo (2026-03-06) | SECONDARY |
| Dismissal | Cases dismissed **2025-08-18** with no confirmed plan (bondoro). Polsinelli (Honarkar counsel) announced the dismissal on 2025-10-15. | bondoro; https://www.polsinelli.com/news/polsinelli-represents-mo-honarkar-4g-wireless-in-dismissal-of-bankruptcy-cases | SECONDARY |
| Interim award | JAMS No. 5220003126 (consol. w/ 5200001122), **Partial Interim Award 2025-02-21**. Per the TDM/issuu summaries: "Claimants have proven their conspiracy to commit and aiding and abetting fraudulent inducement claims against Nano". | issuu / TDM (TDM certificate expired, not read) | SECONDARY |
| Partial Final Award | **2025-05-23** (Jus Mundi listing names Nano Banc as a respondent; the page returned 403). The Save Laguna summary (issuu, posted 2025-11-03, **pro-Honarkar advocacy publisher**) says the award "supports rescission, consequential and punitive damages". **I found no dollar amount for the 5/23/2025 award in any source I reached.** | https://jusmundi.com/… (403); https://issuu.com/savelaguna/docs/honarkar_vs_makhijani_continuum_nano_banc_parital_ | SECONDARY (partisan) |
| Final award | "$1.34 billion award" to Honarkar/4G against "Mahender Makhijani, Continuum Analytics and affiliated entities". **The LB Indy article does not name Nano Banc as liable for the $1.34B.** TRD: "An arbitrator recently awarded a $1.34 billion judgment in favor of Honarkar and against Makhijani." Confirmation in court was pending. | LB Indy 2026-06-19 (Alicia Venter) https://www.lagunabeachindy.com/news/laguna-beach-property-owner-awarded-1-34b-arbitration-in-fraud-case/article_e83c066d-a23c-4ea9-9099-e0339c1d5a0f.html ; TRD 2026-06-18 | SECONDARY |
| Makhijani criminal | Arrested (~June 10–11, 2026) on a federal complaint of ~$100M bank fraud against Western Alliance (title-policy manipulation). Pleaded not guilty (TRD 2026-07-07). | TRD, American Banker, Bisnow (June–July 2026) | SECONDARY |

---

## Q3. Reporting on Nano Banc's CRE book

| Item | Fact | Source | Tier |
|---|---|---|---|
| CRE concentration history | Fed Feb 2021 agreement on CRE concentration risk. At 12/31/2020 "more than half of the bank's then-$886 million of loans were backed by commercial properties". Jan 2022 Fed C&D covered insider lending and CRE underwriting. The Fed terminated its action in Apr 2025. | American Banker 2026-09-25; https://www.federalreserve.gov/newsevents/pressreleases/enforcement20250401a.htm | SECONDARY / PRIMARY-READ (headline only) |
| DFPI 3/6/2026 §580 order, CRE clause | "Reducing the Bank's CRE concentrations **and concentrations in unsecured loans to finance real estate**…" and "Developing and implementing a plan … to reduce the level of adversely classified assets". Also requires loan workouts, accrual status and Call Report accuracy (¶9E: "accurately and consistently apply … Call Report instructions in designating loan accrual status"). | https://dfpi.ca.gov/wp-content/uploads/2024/09/Final-Order.pdf (order dated 2026-03-06; also Exhibit B to the seizure order) | PRIMARY-READ |
| Geography of named problem loans | Moreno Valley, Ontario, Chino (Inland Empire); Bellflower (LA County); Danville (East Bay); Sand City (Monterey); Laguna Beach (OC). All are borrower-network (Makhijani/Stupin/Marcil) credits. | tables above | PRIMARY-READ + SECONDARY |
| Non-credit loss drivers | Axos Bank v. Nano Banc (C.D. Cal. 5:19-cv-02092): **$40M** trade-secret judgment against Nano and ex-employees, Aug 2025 (Law360 headline). 2025 net loss was $75.3M, but the 2025 provision was only $16.7M. **Most of the 2025 loss was therefore not loan provisions** (INFERRED; Q3-25 standalone loss ≈ −$34.1M, which lines up in time with the Axos verdict). | Law360 (2025-08, headline only); FDIC API | SECONDARY / INFERRED |
| OREO | **Zero** on every quarter from 2025Q1 to 2026Q2 (ORE, ORECONS, ORENRES, ORERES, OREOTH all 0). There was no OREO at 6/30. The 9/22 balance sheet has no OREO line (it may sit in "Other assets" $3.6M). | FDIC API | PRIMARY-READ |
| Gressak | Co-founder / interim CEO fined and banned in 2024 over $15.5M of fraudulently obtained pandemic relief funds | American Banker 2026-09-25 | SECONDARY |

---

## Q4. FDIC BankFind financials (CERT 58590), $ thousands

Query: `https://api.fdic.gov/banks/financials?filters=CERT:58590&fields=...&sort_by=REPDTE&sort_order=DESC&limit=6` (run 2026-09-27; index `risview_20260819185831`). **PRIMARY-READ.** All requested field names worked.

### Balances

| Field | Meaning | 2026-06-30 | 2026-03-31 | 2025-12-31 | 2025-09-30 | 2025-06-30 | 2025-03-31 |
|---|---|---|---|---|---|---|---|
| ASSET | Total assets | 736,172 | 859,973 | 875,372 | 908,539 | 931,078 | 996,599 |
| LNLSGR | Gross loans & leases | 478,812 | 510,016 | 541,418 | 581,065 | 612,759 | 655,900 |
| LNLSSALE | Loans held for sale | 45,022 | 8,595 | 0 | 0 | 0 | 0 |
| LNRE | RE loans | 362,642 | 398,062 | 429,497 | 446,924 | 471,940 | 505,323 |
| LNRENRES | Nonfarm nonres | 128,732 | 131,088 | 164,777 | 176,574 | 180,898 | 206,612 |
| — LNRENROT | Non-owner-occ | 126,075 | 128,424 | 162,105 | 173,892 | 178,205 | 203,910 |
| — LNRENROW | Owner-occ | 2,657 | 2,664 | 2,672 | 2,682 | 2,693 | 2,702 |
| LNREMULT | Multifamily | 70,828 | 94,324 | 94,040 | 94,574 | 117,053 | 127,236 |
| LNRECONS | Construction & land | 46,912 | 42,878 | 38,347 | 38,337 | 38,328 | 36,882 |
| — LNRECNOT | Other constr. | 46,912 | 42,878 | 38,347 | 38,337 | 38,328 | 36,882 |
| LNRERES | 1–4 family (incl. HELOC) | 116,170 | 129,772 | 132,333 | 137,439 | 135,661 | 134,593 |
| — LNRERSFM | 1–4 first liens | 92,040 | 103,196 | 102,546 | 106,072 | 104,260 | 106,699 |
| — LNRERSF2 | 1–4 junior liens | 14,590 | 14,889 | 19,603 | 19,980 | 17,139 | 17,275 |
| LNRELOC | HELOC | 9,540 | 11,687 | 10,184 | 11,387 | 14,262 | 10,619 |
| LNREAG | Farmland | 0 | 0 | 0 | 0 | 0 | 0 |
| LNCI | C&I | 28,262 | 40,834 | 41,704 | 101,447 | 105,002 | 132,779 |
| LNOTHER | All other loans | 87,908 | 71,120 | 70,217 | 32,694 | 35,817 | 17,798 |
| LNATRES | ACL | 19,929 | 13,025 | 13,493 | 19,222 | 20,400 | 24,572 |
| ORE | OREO | 0 | 0 | 0 | 0 | 0 | 0 |
| EQ | Equity | 38,810 | 41,196 | 41,534 | 67,141 | 100,894 | 115,675 |
| DEP | Deposits | 685,846 | 789,703 | 732,658 | 755,102 | 804,571 | 870,172 |

My footing checks: LNRE = 128,732+70,828+46,912+116,170 = 362,642 ✓ (6/30). LNRERES = 92,040+14,590+9,540 = 116,170 ✓. LNLSNET 458,883 = 478,812 − 19,929 ✓.

### Noncurrent (nonaccrual + 90+ days past due) by class

| Field | Meaning | 2026-06-30 | 2026-03-31 | 2025-12-31 | 2025-09-30 | 2025-06-30 | 2025-03-31 |
|---|---|---|---|---|---|---|---|
| NCLNLS | Total noncurrent | **123,206** | **104,865** | 131,515 | 89,428 | 62,462 | 11,602 |
| NALNLS | Total nonaccrual | 123,206 | 104,865 | 131,515 | 89,428 | 62,462 | 11,602 |
| P9LNLS | Total 90+ PD accruing | 0 | 0 | 0 | 0 | 0 | 0 |
| NCRE | Noncurrent RE | 85,631 | 104,865 | 110,672 | 67,974 | 62,462 | 11,602 |
| NARE | Nonaccrual RE | **85,631** | **104,865** | 110,672 | 67,974 | 62,462 | 11,602 |
| P9RE | 90+ PD RE | 0 | 0 | 0 | 0 | 0 | 0 |
| NARENRES (=NARENROT) | Nonaccrual nonfarm nonres (all non-owner-occ) | **74,319** | **74,159** | 79,831 | 36,788 | 31,048 | 11,602 |
| NAREMULT (=NCREMULT) | Nonaccrual multifamily | **7,288** | **30,706** | 30,841 | 31,186 | 31,414 | 0 |
| NARECONS (=NARECNOT) | Nonaccrual construction | **4,024** | **0** | 0 | 0 | 0 | 0 |
| NARERES / NARERSFM / NARELOC | Nonaccrual 1–4 fam | 0 | 0 | 0 | 0 | 0 | 0 |
| P9RENRES / P9REMULT / P9RECONS / P9RERES | 90+ PD by class | 0 | 0 | 0 | 0 | 0 | 0 |
| NACI | Nonaccrual C&I | 4,881 | 0 | — | — | — | — |
| NAOTHLN | Nonaccrual all other loans | **32,694** | 0 | — | — | — | — |
| P3RE | 30–89 PD RE | 41,448 (all construction, P3RECONS) | 0 | 0 | 54,348 (all nonres) | 0 | 10,190 |
| P3LNLS | 30–89 PD total | 41,448 | 13,032 | — | — | — | — |
| NTRE (YTD) | Net charge-offs RE | 3,940 | 468 | 4,188 | 4,188 | 3,973 | 1,599 |
| NTLNLS (YTD) | Net charge-offs total | 7,958 | 468 | 29,049 | 17,720 | 11,805 | 1,603 |
| ELNATR (YTD) | Provision | 14,225 | −155 | 16,701 | 11,156 | 6,438 | 424 |
| NETINC (YTD) | Net income | −2,218 | 119 | **−75,316** | −49,525 | −15,387 | −252 |
| IDT1CER | CET1 ratio % | 7.83 | 8.17 | 7.15 | 11.18 | 15.44 | 17.54 |
| RBC1AAJ | Leverage ratio % | 5.04 | 4.79 | 4.77 | 7.23 | 10.20 | 12.08 |

6/30 footing: 85,631 RE + 4,881 C&I + 32,694 other = 123,206 = NCLNLS ✓.

**Ratios at 6/30/26 (INFERRED arithmetic):** nonaccrual share of non-owner-occupied nonfarm nonres = 74,319/126,075 = **58.9%**. Multifamily 7,288/70,828 = 10.3%. Construction 4,024/46,912 = 8.6% (NCRECONR field = 8.58 ✓). Total noncurrent/gross loans = 25.7%.

**Observations (INFERRED):**
- The multifamily nonaccrual fell 30.7 → 7.3 as the MF book fell 94.3 → 70.8 in Q2-26 (−$23.5M). That is consistent with a MF loan being resolved, sold or moved to HFS (HFS rose 8.6 → 45.0). The data doesn't say which.
- The $32,694K "all other loans" nonaccrual at 6/30/26 exactly equals LNOTHER at 9/30/25 (32,694). That suggests a legacy "other loan" block (possibly the "unsecured loans to finance real estate" named in the DFPI order) went nonaccrual in Q2-26. This is unverified.
- 30–89 PD construction was $41.4M at 6/30 (≈88% of the construction book). That is a leading indicator for the retained pool.
- The 2025 loss of −$75.3M against a provision of $16.7M means credit provisioning explains less than a quarter of the 2025 loss.

---

## Gaps / not reached (say which shapes were tried)

- **FDIC P&A agreement / retained-asset schedule:** not linked on the 3 FDIC pages (HTML). The failures API index predates the failure. Not yet posted. Re-check fdic.gov "Bank Failures in Brief" and the P&A agreement posting in about 1–2 weeks.
- **Nano claim in MOM CA Investco:** the Stretto claims-agent URL returned 404 (curl and WebFetch). The two debtor motions read do not mention Nano. The claims register and Schedule D were not reached; this goes to the docket agent.
- **Partial Final Award 5/23/2025 amount:** Jus Mundi 403; the issuu flipbooks are JS-rendered (only the publisher blurb is readable); the TDM certificate had expired. No dollar figure found.
- **Marcil v. Nano Banc (8:26-cv-01143) docket:** PacerMonitor and Justia both 403. The loan amount and date come from the search-result snippet only.
- **Zions complaint (Laguna Beach building assigned to Nano):** address not found. Tried search only.
- **Nano v. Plaza Continental (OC Superior):** Law.com Radar is JS-only; the fact comes from the search snippet.
- **Watch for an unrelated $260M:** a 2025 substack/Bloomberg line says banks are "fighting in court … to at least $260 million in collateral" (the Zions/WAL dispute). That is **not** the FDIC retained figure. Do not conflate them.
