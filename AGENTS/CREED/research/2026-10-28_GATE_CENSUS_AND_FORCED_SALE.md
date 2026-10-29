# H2: Forced-sale cluster (T-06 / VX-5.01) and fund-gate census (T-06b / VX-5.03): research helper output

**Run date:** 2026-10-28. Read-only helper; no repo files edited. Nothing here grades a trigger; CREED does that.
**Tiers:** PRIMARY-READ (SEC document opened and read here) · PRIMARY-CITED (a primary named by a secondary, not opened) · SECONDARY · SEARCH-NOT-FOUND (shapes tried are named).
**SEC access:** EDGAR full-text search (efts.sec.gov), data.sec.gov submissions and XBRL `Assets`, and Archives documents, all with UA "Research CREED williepowen@gmail.com".

> ⚠️ **Naming correction to the brief:** the brief says "Blackstone REIT (SREIT)". **SREIT is Starwood Real Estate Income Trust (CIK 1711929). Blackstone's vehicle is BREIT (CIK 1662972).** The 2026-04-29 suspension belongs to Starwood. BREIT was checked separately below.

---

## TASK A: Gate census re-run (window 2026-09-26 to 2026-10-28)

### A0. Positive control: PASS
| Item | Finding | Tier |
|---|---|---|
| Control found by EDGAR full-text search? | **Yes.** The query `"qualifying disability" "accounts having a balance below"` on 424B3 forms dated 9/26 to 10/28 returns exactly 1 hit: the SREIT 424B3 filed 2026-10-16 (acc 0001193125-26-424159). | PRIMARY-READ |
| Is the suspension still in place? | **Yes, as of the 10/16/26 supplement.** It restates the 4/29 amendment: repurchases are limited to death or qualifying disability (≤$5M/mo) and accounts under $5,000 (≤$5M/mo). | PRIMARY-READ |
| Repurchases paid under the restricted plan | Jul-26 ~$4.2M · Aug-26 ~$5.1M · Sep-26 ~$3.7M, "which represented all repurchase requests for such period made upon the death or qualifying disability … and for accounts having a balance below $5,000" | PRIMARY-READ (424B3 10/16) |
| Size | Aggregate NAV ~$7.9B at 9/30/26 (424B3). Total assets **$18.60B** at 6/30/26 (XBRL `Assets`, 10-Q filed 8/12). That is ≥$1.0B on the total-assets fallback basis. | PRIMARY-READ |
| Other SREIT filings in window | 8-K 9/30 (Item 8.01): September distributions only, with no repurchase change. No lifting or modification of the restriction has been filed through 10/28. | PRIMARY-READ |

**Retrieval-shape caveat (KB-CREED-040 holds again):** the phrase union below shows EDGAR full-text search is a weak instrument for this job:
- SREIT's own 424B3 matched only on its exceptions language, not on any "suspend" or "limit" word.
- 424B3s with "repurchase requests" totalled only 14 hits in the window.
- BREIT's monthly 424B3 does not match at all, because it carries no fill statement.

So the census below rests mainly on **reading each named vehicle's own filings since 9/20**, with EFTS as a supplement.

### A1. Method
1. **EFTS phrase union**, forms 8-K, 424B3, 10-Q, SC TO-I, N-23C3A, dated 2026-09-26 to 2026-10-28, each phrase paired with "share repurchase plan" to cut noise. Phrases: suspend · suspended the share repurchase plan · suspension of the share repurchase plan · no repurchase requests will be accepted · amended the share repurchase plan · modify the share repurchase plan · repurchase requests on a pro rata basis · prorated · exceeded the 2% monthly limit · exceeded the 5% quarterly limit · pause · redemption queue · less than all repurchase requests · limit repurchases · repurchase limit · suspend the redemption. A wider unpaired run (27 phrases, including "suspend redemptions", "limit redemptions", "paused", "pro rata basis") returned mostly non-real-estate noise.
   - Real-estate hits: Core University Living, Fidelity Core, Invesco INREIT, Invesco CRE Finance, JLL IPT and Independence Realty all matched on boilerplate ("ability to suspend … at any time") or merger proration (IRT is a listed REIT). Sculptor SDIR matched on "no repurchase requests will be accepted" (a known partial suspension, out of perimeter on size).
2. **Per-vehicle read:** every 8-K, 424B3, 10-Q and SC TO-I filed since 2026-09-20 by 27 vehicles, with every sentence containing repurchas/redemption/redeem/tender/suspend/prorat/queue extracted. Vehicles: BREIT, SREIT, Ares REIT, Ares Industrial, JLL IPT, Nuveen GCREIT, CFIT, Brookfield REIT, KREST, Apollo ARIS, Hines GIT, Invesco INREIT, JPMREIT, Blue Owl Net Lease, C&S IOREIT, EQT Exeter, Cottonwood, North Haven Net REIT, Starwood Credit, FS Credit REIT, Core University Living, Clarion PREIF, Sculptor SDIR, Fidelity Core, PGIM RE Fund, Invesco CRE Finance, and RREEF Property Trust.
3. **Web search** for news of suspend/halt/pause/limit/prorate/redemption-queue events in Sep–Oct 2026, including ODCE funds.

### A2. Result by vehicle (window 9/26 to 10/28)
| Vehicle | Latest repurchase disclosure | Gate? | Tier |
|---|---|---|---|
| **SREIT (Starwood)** | Restricted plan still in force (see A0) | **YES: counted member** | PRIMARY-READ |
| BREIT (Blackstone) | 424B3 10/22 and 8-Ks 9/30, 10/05, 10/15, 10/22 contain no fill-rate statement; no suspension or modification filed. Total assets $90.75B (6/30). | No gate filed. Fill rate UNGRADED, as on 9/26. | PRIMARY-READ (absence of a gate filing) |
| Ares REIT (AREIT) | 8-K 10/15: Q3 requests of $27M "redeemed in full" on 8/1, 9/1, 10/1 | No | PRIMARY-READ |
| Ares Industrial (AIREIT) | 8-K 10/15: Q3 requests of $76M "redeemed in full" | No | PRIMARY-READ |
| JLL IPT | 424B3 10/02: Q3 redeemed ~$75.0M; "We honored 100% of all redemption requests received"; Q4 limit ~$113.7M (5% of NAV) | No | PRIMARY-READ |
| Invesco INREIT | 8-K 10/16: "We fulfilled all repurchase requests that were made" (Q3) | No | PRIMARY-READ |
| FS Credit REIT | 424B3 10/16: "We met 100% of repurchase requests in September" | No | PRIMARY-READ |
| KREST | SC TO-I/A 10/20 (final): Q3 tender expired 10/16; 2,285,571 shares tendered and 2,285,571 accepted at $22.75 | No | PRIMARY-READ |
| **CFIT** | See A3. Q3 repurchases sit at the 5% quarterly limit. | **No (D2: proration at the limit)** | PRIMARY-READ |
| Nuveen GCREIT, Brookfield REIT, Apollo ARIS, JPMREIT, C&S IOREIT, EQT Exeter, Cottonwood, Hines GIT | Monthly transaction-price 424B3 and 8-Ks only. No suspension, amendment or proration statement filed in window. | No gate filed (fill rate unstated) | PRIMARY-READ (absence) |
| Blue Owl NL, North Haven Net, Starwood Credit, Fidelity Core, Clarion PREIF | No repurchase-change filing in window | No gate filed | PRIMARY-READ (absence) |
| Sculptor SDIR | 8-K 10/26: share repurchase plan amended and restated (eff. 10/21) to add new share classes; partial suspension since 4/28. About $94M per 9/26 census, so out of perimeter on size. | Out of perimeter | PRIMARY-READ (8-K) / size SECONDARY (9/26 record) |
| **RREEF Property Trust (DWS), NEW** | 8-K filed 9/18: on **2026-09-15** the board approved a Plan of Complete Liquidation and, "effective immediately, the suspension of … (ii) the Company's share redemption plan". A stockholder vote is expected early 2027. **Total assets $333.6M at 6/30/26 (XBRL).** | **A gate, but OUT OF PERIMETER on size** (<$1.0B). Also arguably a liquidation-driven suspension (compare SSGT III's merger-driven case). | PRIMARY-READ |
| PGIM Real Estate Fund (interval) | N-23C3A 9/29: routine quarterly repurchase offer | No | PRIMARY-READ |

**Non-US, out of perimeter:**
- **Swiss Life REF (DE) European Real Estate Living and Working** (ISIN DE000A2ATC31). Redemptions suspended effective 2026-10-20 at 12:00 for "insufficient liquidity", for up to 36 months. NAV ≈ €762M at end-Sep 2026; GAV not given. German open-end fund, not US. SECONDARY (MTR Legal 10/26, citing the KVG investor notice).
- Prior non-US items (Habona, UBS Euroinvest, DWS grundbesitz) were not re-checked.

**ODCE / private open-end funds:** no primary queue data. Search shapes tried: "ODCE redemption queue 2026", "open-end real estate fund gate withdrawals 2026". The only 2026 figure found is a paywalled IREI June 2026 piece: queues peaked at ~$40–50B, 10–20% of NAV for several large platforms (SECONDARY, not current). **SEARCH-NOT-FOUND for any new ODCE gate since 9/26.**

### A3. Open adjudication: CFIT (Cantor Fitzgerald Income Trust, CIK 1666244)
- **Stated limit** (10-Q for Q2, filed 2026-08-13; PRIMARY-READ): monthly repurchases capped at **2% of the aggregate NAV** as of the prior month-end, and quarterly at **up to 5% of the Company's aggregate NAV** as of the prior quarter-end. Accounts under $2,500 are paid first, then requests are filled pro rata.
- **Limit base:** the Q2 NAV table (same 10-Q) gives a total NAV of $435.66M including OP units. The common-share classes alone sum to about **$219.17M** (185.94 + 0.10 + 24.38 + 8.64 + 0.11). OP units are $216.49M.
  - The 424B3s quote "aggregate NAV" as $435.7M (6/30), $436.9M and **$463.2M (9/30)**. Those totals include OP units.
- **Q3 fills** (424B3s filed 8/14, 9/15, 10/15; PRIMARY-READ):

  | Month | Repurchased | Share of requests honoured |
  |---|---|---|
  | Jul-26 | $4.4M | 37.3% |
  | Aug-26 | $4.4M | 52.3% |
  | Sep-26 | $2.2M | 27.0% |
  | **Q3 total** | **$11.0M** | |

- **Arithmetic (CREED-checkable):** 5% × $219.17M = **$10.96M**, which matches the Q3 total of $11.0M. 2% × $219.17M = $4.38M, which matches the $4.4M paid in each of July and August. September's $2.2M is what remained of the quarterly cap.
  - Q2 shows the same pattern: 561,441 shares × $20.31 = $11.40M, against the 10-Q's own statement that requests "exceeded both its monthly 2% of NAV and quarterly 5% of NAV limits".
- **Reading:** CFIT is **prorating at its stated limits, not below them.** Under D2 that is **not a gate.**
  - The 9/26 concern ("~1%/mo against a 2% limit") came from dividing by the NAV including OP units ($463M). The limit is applied to the Company's common-share NAV.
  - ⚠️ That base is **inferred from the exact arithmetic fit**. The 10-Q does not say in words that OP units are excluded. CREED should treat it as an analytical inference resting on PRIMARY-READ figures.
- **Size leg:** "Total gross assets at Fair Value" was **$1,254,911,089 at 6/30/26** in CFIT's own NAV table (a published GAV), and XBRL `Assets` was $1.19B. **≥$1.0B: passes.** CFIT is therefore a major fund that is **not gating**.

### A4. Open adjudication: Trez Capital (Canada)
- 🔴 **Date defect in CREED's record:** the 5-fund suspension was **2025-08-18**, not 2026-08-17.
  - advisor.ca article dated 2025-08-21 (SECONDARY): announced "Monday" (2025-08-18). It names Prime Trust, Yield Trust, Yield Trust U.S. CAD, Yield Trust U.S. USD, and Private Real Estate Fund Trust.
  - The Bloomberg URL is dated 2025-08-18 (SECONDARY, not opened).
  - Per WOWA, a **further suspension (redemptions and NAV calculations) took effect 2026-02-15** on four mortgage funds, and Prime Trust is "in an orderly capital-return or wind-down process" (SECONDARY, data as of 3/31/26).
  - **SEARCH-NOT-FOUND** for any August-2026 Trez event. Shapes tried: news on "Trez Capital redemptions suspended 2026", "Trez 2026 strategic alternatives wind-down update", and WOWA fund pages. No Trez primary notice was opened.
- **Per-fund size** (WOWA, AUM basis undefined, CAD; SECONDARY):

  | Fund | AUM | Date |
  |---|---|---|
  | Yield Trust U.S. (CAD class) | ~C$1.167B–1.2B | Q1-2026 |
  | Yield Trust | C$785M | undated |
  | Prime Trust | C$252M | 3/31/26 |
  | Yield Trust U.S. (USD class) | C$146M | undated |

  The firm figure is ~C$2.5B fund-level across four trusts.
- **Reading for CREED:**
  - The only candidate over $1.0B is Yield Trust U.S., at ~C$1.17B, roughly **US$0.85B at about 0.72–0.73 USD/CAD**. That is an assumed FX rate, not fetched.
  - Its AUM figure is not a GAV, and a leveraged GAV could be higher; this is unknown.
  - It is a **Canadian mortgage (debt) trust**, not a US equity CRE fund.
  - Its gate began in 2025, before the WQ-100 forward-only date of 2026-09-01. Whether a pre-existing restriction counts is a definitional question for CREED and Will.
  - **The size leg is still ungradeable on a GAV basis.**

### A5. Census count (US major open-end / perpetual-life CRE vehicles gating, as of 2026-10-28)
| # | Member | Gate | Size basis | Evidence |
|---|---|---|---|---|
| 1 | **Starwood REIT (SREIT)** | Suspension effective 2026-04-29, still in force per the 10/16/26 424B3 | Total assets $18.60B (6/30/26) | PRIMARY-READ |

**Count = 1** (unchanged from 9/26). No new US major-fund gate was found since 9/26.
- **CFIT** is resolved as *not a gate* (prorating at its limit, D2).
- **RREEF PT** is a new gate (9/15) but below the size bar ($333.6M).
- **Trez** remains open on size, and its date in CREED's record needs correcting.
- **Ungraded, unchanged:** BREIT and Blue Owl NL (no fill statement), and private ODCE queues.

---

## TASK B: Forced-sale cluster since 2026-08-27 (T-06; VX-5.01)

**Bases are named per row. A lender credit bid is never treated as a price.** "Performing collateral" is read here as income-producing and materially occupied, versus vacant or obsolete. Where occupancy is unknown, it is marked UNKNOWN and not assumed. No source in this table was opened at SEC primary.

### B1. PROPERTY sales, closed, dated on or after 8/27
| Date | Asset | Price | Basis compared (named) | Discount | Collateral state | Tier |
|---|---|---|---|---|---|---|
| **2026-10-27** | **100 Summer St, Boston** (32-story, ~1.1M sf office) | **$260M** foreclosure-auction price (~$236/sf). **Sole bid, by Rockpoint, the existing owner/borrower**; not a lender credit bid. | ① 2019 purchase $806M → **−67.7%** · ② 2019 Wells Fargo loan original principal $470M (current balance UNKNOWN) → −44.7% · ③ assessment $425M → −38.8% | −68% vs purchase | **OCCUPIED: 72% (B&T) / 72% leased (Bisnow).** Tenants: SimpliSafe 150k sf; MA Trial Court 79,424 sf (Feb-2026 lease) | SECONDARY (Banker & Tradesman 10/27; Bisnow / Boston Globe 9/23 on the foreclosure setup) |
| **2026-10-06** | **901 Fifth Ave, Seattle** (540,589 sf office) | **$48.3M** (~$89/sf) | 2019 purchase $305M (JLL) → **−84.2%** | −84% vs purchase | **UNKNOWN** (100% occupied in 2019; no 2026 figure). Deutsche Bank is tagged, but its role is unverified. Buyer identity conflicts (Traded vs Wikipedia). | SECONDARY (CRE News 10/06 snippet; Traded) |
| ~2026-10-20 | **Commercial National Bank bldg, 700 14th St NW, DC** (CASE-159) | **$50.35M**, lender-controlled sale (DekaBank reported) | 2013 purchase $183M → **−72.5%** | −72.5% vs purchase | **UNKNOWN.** Skadden was the major tenant with a lease to 2028 (older, undated secondary). Possibly occupied, not verified. | SECONDARY (WBJ 10/20 via WALTER; buyer CEO quoted). SEARCH-NOT-FOUND for an independent confirmation of the $50.35M / Taicoon. |
| ~2026-09-17 (reported 9/27) | **Plaza 600, 600 Stewart St, Seattle** (CASE-056) | **$12.5M** | 2019 purchase $97M → **−87%** | −87% vs purchase | **UNKNOWN.** Submarket vacancy ~37–43%; the workbook notes a "post-renovation sale". | SECONDARY (Will workbook v4; e-a-a.com 9/27 relay). SEARCH-NOT-FOUND at a primary. |
| ~2026-09-28 | **Valley West Mall, West Des Moines** (CASE-145) | **$11M** (sale after receivership) | U.S. Bank loan: payoff >$43.2M / remaining ≥$41.2M **(2022 figures)** → about −73% to −75% vs a stale loan figure | about −74% vs the 2022 loan | **Obsolete-leaning regional mall** (JCPenney is the sole remaining anchor, lease to 2032); occupancy UNKNOWN | SECONDARY (Bisnow 10/07 via Morningstar; Axios 9/29; Business Record 2022) |
| ~2026-09-01 (reported) | Columbine Place, Denver (17-story) | $3.63M | 2015 loan $15.5M → −76.6% | −77% vs loan | **69% vacant** (distressed, not performing) | SECONDARY (Connect CRE) |
| 2026-09 | 3000 Post Oak, Houston (CASE-001) | Undisclosed; trust proceeds $11.4M | balance $74.58M | ~85% loss | **Vacant**: excluded by T-06's own text | PRIMARY-READ in CREED's record (10-Ds) |
| ≤2026-10-15 | 1099 N Meridian, Indianapolis (CASE-150) | $3M auction (unverified) | 2015 price $23M (unverified) | −87% | 39% occupancy (single social source) | LEAD |
| 2026-09 | 410 Townsend SF (CASE-073) · 1330 Connecticut NW (CASE-082) | $47.4M · $92.3M | prior prices $22M · $86.6M | **gains** | n/a | SECONDARY (workbook) |
| ~2026-09-24 | Baltimore St. Paul St rowhouses (CASE-143) | $1.6M each | no basis | UNKNOWN | small MF/office | SECONDARY |

**Not sales, so excluded:**
- 707 Eleventh Ave (CASE-120): lender transfer, 2026-09.
- 450 Fifth St NW (CASE-139): **lender bought at the 10/28 auction, a credit bid and never a price.**
- 10 Prospect (CASE-024): failed sale, taken into OREO 9/30.
- Symes Building (CASE-141): $2.7M under contract, not closed.

**Before the window (8/27):** BofA Plaza St. Louis (CASE-016) sold in 2026-06, and Hotel Indigo St. Louis (CASE-142) had a receivership sale in 2026-07.

### B2. NOTE sales (a note price is not a property price; each is kept separate)
| Date | Asset | Note price | Basis | Discount | Collateral state | Tier |
|---|---|---|---|---|---|---|
| **≤2026-10-06** | **700 Sixth St NW, DC** (CASE-161) | **$79.5M** (Assembly/FitzWalter, then deed-in-lieu from Affinius) | balance $145.8M per deed records (orig. $140M, Principal) | **−45.5% vs balance** | **79% leased, 7.8-yr WALT (JLL loan marketing, spring 2026), so OCCUPIED** | SECONDARY (Bisnow 10/06; TRD 4/15/26) |
| **2026-10-19** | **Wells Fargo Center South, LA** (CASE-155) | **$115M** (Kam Sang affiliate) | $290M loan per broker; current UPB unverified | about −60% vs the stated loan | ~42% occupancy (broker): partly occupied, weak | PRIMARY-CITED (Newmark release) / SECONDARY (price: CRE News 10/23, TRD 10/19) |
| 2026-08 (exact day UNKNOWN, possibly before 8/27) | 225 Bush St, SF (CASE-138) | $221.0M (Flynn, then deed-in-lieu) | note face $350M (appraisal $153M, May-2025) | −36.9% vs face; **above** the 2025 appraisal | ~57% (undated JLL listing) | SECONDARY (Connect CRE 10/01 via Morningstar / SFBT) |
| 2026-02 (out of window) | 330 S Wells, Chicago | $15M / −47% unverified | n/a | n/a | 97% occupied (2023) | SECONDARY; price SEARCH-NOT-FOUND |

### B3. Evidence summary (not a grade)
Since 2026-08-27, these are the sales more than 30% below a named basis **where the collateral has a documented occupied/performing status**:
1. **100 Summer St, Boston: property sale, 2026-10-27.** 72% occupied. −67.7% vs 2019 purchase and −44.7% vs original loan principal.
   - **Caveat:** it was a sole bid by the defaulted owner at its own foreclosure auction. CREED must decide whether that is an arm's-length clearing price.
2. **700 Sixth St NW, DC: NOTE sale, ≤2026-10-06.** 79% leased (spring 2026). −45.5% vs loan balance.
   - **Caveat:** a note sale, not a property sale.

**Borderline:** Wells Fargo Center South (note sale 10/19) is −60% vs a broker-stated balance, at about 42% occupancy. Whether that counts as performing is CREED's call.

**Occupancy UNKNOWN, cannot be classed:** 901 Fifth Seattle (10/06, −84%), Commercial National Bank bldg DC (~10/20, −72.5%), Plaza 600 Seattle (~9/17, −87%). If any of them is shown occupied, the set grows.

**Excluded as vacant, obsolete or distressed:** 3000 Post Oak, Columbine Place, Valley West Mall (obsolete-leaning retail), 1099 N Meridian (LEAD).

**Count: 1 qualifying property-sale comp in documented-occupied collateral (100 Summer, 10/27), plus 1 qualifying note-sale comp (700 Sixth NW, ≤10/06).** That is 2 if note sales are admitted and 1 if they are not. A further 3 sales of more than 70% vs purchase price have unknown occupancy.
- **Basis warning (trap #2):** every large discount above is measured against a **2013–2019 purchase price**, not a loan balance. The only loan-based ones are 700 Sixth (balance) and 100 Summer (original principal). A purchase-price decline is not a lender loss.
- Every row in Task B is SECONDARY or weaker.

## Source list (opened or cited)
- SEC (PRIMARY-READ):
  - SREIT 424B3 0001193125-26-424159 (10/16) and 8-K 0001193125-26-408572 (9/30)
  - CFIT 10-Q 0001193125-26-349682 (8/13) and 424B3s filed 2026-07-16, 08-14, 09-15, 10-15 (incl. 0001193125-26-422934)
  - RREEF PT 8-K 0001542447-26-000110 (9/18)
  - KREST SC TO-I/A 0001193125-26-426067 (10/20)
  - AREIT 8-K 0001628280-26-066024; AIREIT 8-K 0001628280-26-066025; JLL IPT 424B3 0001314152-26-000200; INREIT 8-K 0001756761-26-000144; FS CREIT 424B3 0001628280-26-066170; SDIR 8-K 0001914496-26-000156
  - XBRL `Assets` for SREIT, BREIT, RREEF PT, CFIT
- Web (SECONDARY):
  - [advisor.ca Trez 2025-08-21](https://advisor.ca/news/industry-news/trez-capital-announces-temporary-fund-redemption-suspensions/), [WOWA Trez Prime](https://wowa.ca/mortgage-investment-entity/trez-capital-prime-trust), [WOWA Trez Yield US](https://wowa.ca/mortgage-investment-entity/trez-capital-yield-trust-us), [Bisnow Trez](https://www.bisnow.com/news/national/capital-markets/trez-capital-indefinitely-freezes-fund-redemptions-weighs-strategic-alternatives-130617)
  - [MTR Legal Swiss Life 10/26](https://www.mtrlegal.com/en/swiss-life-suspends-real-estate-fund-redemptions/)
  - [Banker & Tradesman 100 Summer 10/27](https://bankerandtradesman.com/rockpoint-buys-back-tower-at-68-percent-discount/), [Bisnow 100 Summer foreclosure](https://www.bisnow.com/news/boston/office/32-story-downtown-boston-office-tower-heading-to-foreclosure)
  - [CRE News 901 Fifth 10/06](https://crenews.com/2026/10/06/seattle-office-property-sells-at-major-discount/), [Traded 901 5th](https://traded.co/deals/washington/office/sale/901-5th-avenue/)
  - [Bisnow 700 Sixth DIL](https://www.bisnow.com/news/washington-dc/office/office-building-near-capital-one-arena-sells-deed-in-lieu-of-foreclosure), [TRD 700 Sixth loan 4/15](https://therealdeal.com/national/washington-dc/2026/04/15/downtown-dc-loan-sale-latest-sign-of-markets-struggles/)
  - [TRD WFC South 10/19](https://therealdeal.com/la/2026/10/19/distressed-downtown-office-tower-loan-sells/), [CRE News WFC South 10/23](https://crenews.com/2026/10/23/290mln-loan-on-l-a-office-tower-sells-for-115mln/)
  - [Connect CRE Return to Lender 10/01](https://www.connectcre.com/stories/return-to-lender-week-of-oct-1-2026/)
  - [Axios Valley West 9/29](https://www.axios.com/local/des-moines/2026/09/29/valley-west-mall-sale-threshold)
  - [e-a-a Plaza 600](https://www.e-a-a.com/seattle-office-tower-loses-87-percent-in-shocking-sale/), [Connect CRE Columbine Place](https://www.connectcre.com/stories/17-story-denver-office-tower-trades-for-3-6m/)
