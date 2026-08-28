# OZK Problem Book — 11-Credit Deep Dive (Q1 2026)

**Date:** 2026-04-22 | **Thread:** REGINALD deep-dive #1 post-Q1 print | **Source Q1 Analysis:** `Q1_2026_ANALYSIS.md`
**Scope:** All 11 RESG problem credits aggregating $719M ($240M substandard non-accrual + $329M substandard accrual + $150M foreclosed)

---

## TL;DR

1. **10 of 11 credits now sponsor-identified with MED-HIGH confidence.** Only Boston Life Sci $169M remains ambiguous (top candidates: 10 Prospect Somerville or 808 Windsor Boynton Yards).
2. **Expected loss across $719M = $211-291M** (blended 29-40% severity) using 2025-2026 comparable distressed CRE transaction data.
3. **ACL $628M covers 2.2-3.0x the disclosed EL — adequate today.** But if problem book migrates to ~$1.4B over next 2-4 quarters (~~credible given 37.6% hidden CRE baseline + remaining life sci pipeline~~ ⚠️ **see the premise note below — this migration premise LOST one of its two supports**), coverage collapses to 1.1-1.5x → **implies $150-300M reserve build required through 2026.**

> ⚠️ **PREMISE NOTE (2026-08-28 sweep) — the `$150-300M reserve build` in item 3 rests on a migration premise that has lost half its support, and the figure is NOT re-derived here.**
> The `37.6%` hidden-CRE baseline is **RETRACTED** (four independent paths; live **9.35% [Q2-26]**, *below* the screen's own >20% flag for two straight quarters; rank 5th of 14, "worst in screen" formally retracted by REGINALD 8/13). → `LESSONS.md` §Hidden CRE Methodology.
> **What this does and does not do:**
> - ⛔ It does **not** falsify the $150-300M figure. `finding_claim_outlives_its_discredited_instrument` — a dead instrument is not a dead claim. The **second** support (life-sci pipeline) is untouched, and the Q2 print supplies *direct* migration evidence the ratio never did: **classified+criticized $1,215M→$1,282M while RESG shrank $27.8B→$25.7B**, NPA **+31.9% QoQ**, OREO **+93%**.
> - ⚠️ It **does** mean the number is now **single-supported and un-recomputed.** It has not been re-derived since the premise changed, and it must not be quoted as though both supports stand.
> - ⛔ **Scope fence:** MI3 measures CRE **not secured** by real estate. Every credit in this document is **secured** — the 11-credit roster, severities and the $211-291M EL in item 2 are **untouched** by the retraction.
> **Owed:** re-derive item 3 off the Q2 migration evidence directly, retiring the ratio as an input. Logged to `TODO.md`; **no number moved this session.**
4. **Critical new signal — Lionstone wind-down (Seattle):** The forcing function on the Chapter Buildings recap isn't sponsor distress — it's **Ameriprise exiting the entire U.S. RE advisory business and divesting Lionstone's $5.5B book.** LP-side dissolution as a credit trigger is a new pattern we haven't been tracking.
5. **OZK workout-tempo tell (Schaffer's Mill):** $34M Lake Tahoe credit has been substandard **6+ years** on a revolver, with interest/fees exceeding principal paydown. **OZK's true charge-off lag is measured in years, not quarters** — consistent with the "reservoir thesis."
6. **Position read:** ***[DEAD 2026-08-23 — every leg named in this doc is expired; the Aug-21s lapsed worthless at the 8/21 OPEX and OZK holds no options. Credit analysis below is unaffected and current.]*** Not enough here to change the thesis. $45P May remains too tight (resolution tempo Q2-Q3); **the credit that matters for loss severity is Sullivan Courthouse + Boston Life Sci + the Chicago Concord Place marks,** not the smaller credits. The Seattle Chapter Buildings LOI at 50-60% close probability is a coin-flip catalyst for Q2 credit trajectory direction.

---

## 1. CREDIT INVENTORY — Sponsor Map

| # | OZK Disclosure | Balance | LTV | Sponsor Identified | Project | Confidence |
|---|---|---|---|---|---|---|
| **1** | Boston Office | $156.4M | 95% | **Leggat McCall + Related Beal** (historical; now equity-out) | **Sullivan Courthouse / 40 Thorndike**, Cambridge, MA (422K SF, 100% vacant) | ✅ HIGH |
| **2** | Baltimore Land | $40.0M | 53% | **Goldman Sachs + Sagamore (Kevin Plank)** | **Baltimore Peninsula** (235 acres, deed-in-lieu Dec 2025) | ✅ HIGH |
| **3** | Seattle Pioneer Sq Office ("Other"/debt-on-debt) | $25.9M | 100% | **"The Jack" / Urban Visions** ✅ **7/18 CONFLICT RESOLVED: not a conflict — a timing difference. Atrium's $56M "deployed" (Q4'25 vintage) = the pre-charge-off balance; $56.2M Q4'24 − $27.7M Q1'26 charge-off − $2.6M paydown = $25.9M (Q1'26 10-Q). The Jack is a NOTE-ASSIGNMENT / debt-on-debt credit → OZK discloses it in the "Other" Call Report category (10-Q: $25.9M "Other" nonaccrual, $0 ALL, 30-59 DPD — matches exactly). Atrium's $16.1M reserve was pre-charge-off; the charge-off realized it, remaining $25.9M carried at as-is appraisal w/ no ALL. [KB-207]** | 74 S Jackson St, Pioneer Square | ✅ HIGH (restored 7/18) |
| **4** | Wauwatosa Hotel | $17.9M | 103% | **HKS Holdings LLC** (Milwaukee local developer) + Concord Hospitality (operator) | **Renaissance Milwaukee West Hotel**, 2300 N Mayfair Rd (196 keys, opened Aug 2020 into COVID) | ✅ HIGH |
| **5** | Boston Life Science | $169.3M | 91% | **Magellan + RAS + Cypress + Affinius JV** (✅ RESOLVED 4/23 via UCC-1 Bk 85169 Pg 222 — see §2 #5; roster row reconciled 7/6) | **10 Prospect St, Somerville / USQ Parcel D2.1** (SPV: 31 Union Square D2.1 Owner LLC) | ✅ HIGH |
| **6** | Seattle U District Office | $76.4M | 83% | **Touchstone (URG) + Portman Holdings + Lionstone Investments (LP)** | **Chapter Building I** — 4530 12th Ave NE Seattle (240K SF office) | ✅ HIGH |
| **7** | Seattle U District Life Sci | $50.4M | 73% | Same as #6 | **Chapter Building II** — 4536 Brooklyn Ave NE (149K SF life sci/R&D) | ✅ HIGH |
| **8** | Lake Tahoe SF Lots | $33.9M | 93% | **New Martis Partners / MA Partners** (Carey Richards affiliate) | **Schaffer's Mill**, Truckee CA, Martis Valley (475 acres — exact match; ~100 units remaining) | ✅ HIGH |
| **9** | LA Land (foreclosed) | $54.5M | 86% appr | **Townscape Partners (Tyler Siegel/John Irwin) + TPG Angelo Gordon** (AG-SCH entity) | **8150 Sunset Blvd**, LA — 2.5 acres, Frank Gehry-designed 249 units + 65K SF retail entitled. OKO Group failed buyer. | ✅ HIGH |
| **10** | Chicago Life Sci (foreclosed) | $50.0M | 68% appr | **Sterling Bay** (relationship fully collapsed) | **1229 W Concord Place** — **320K SF** lab [corrected 284K→320K, 7/4 web verify], 100% vacant, deed-in-lieu Mar 2026 | ✅ HIGH |
| **11** | Santa Monica Office (foreclosed) | $45.1M | 90% appr | Private creative office developer (not institutional) | **1650 Euclid Street** — 65K SF creative office, 15% leased | ✅ HIGH |

**Combined book value: $719.8M.** Sponsor-identified with HIGH confidence: **$719.8M (100%)** — all 11 rows now HIGH (#3 The Jack restored to HIGH 7/18 once the Atrium "conflict" resolved to a timing difference). [Recomputed 7/6 with #5 at HIGH ($693.9M/96%); 7/18 with #3 at HIGH.]

---

## 2. PER-CREDIT DOSSIER

### #1 — Sullivan Courthouse / 40 Thorndike ($156.4M)
- **Asset:** 422K SF mid-rise office redevelopment in East Cambridge
- **Cycle status:** Delivered into 28%+ Cambridge lab vacancy + 24% Class A office. OZK took $72.4M charge-off Q4 2025 on $300M original basis. Bank is dual-tracking title acquisition.
- **Current status [web-verified 2026-07-04]:** Loan **came due Jan 2026**; extension talks with **Leggat McCall + Granite + CBRE Global Investors FAILED.** OZK "dual-tracking" — working the sponsors while preparing to take title if no fresh capital (Gleason: "you pay, you stay; you don't pay, you don't stay"). **Fire-sale prospect ~50% of the ~$380M cost (~$190M).** Boston-metro book now ~$1.4B active (Jan'26; the "$1.1B Greater Boston" figure is **2024-vintage**).
- **Comp read:** One Lincoln (1.1M SF Boston) cleared Mar 2025 at $400M = -56% vs 2006 basis. 99 Bedford St cleared Nov 2025 at -63%. Fully-vacant Boston office severity 55-63%.
- **Expected loss this credit:** $60-80M additional charge-off (on top of $72M already taken). Total loss trajectory $130-150M of $300M original = 43-50% severity.
- **Timing:** OZK already moved to title. Resolution 2H 2026.

### #2 — Baltimore Peninsula ($40M Land)
- **Asset:** Undeveloped land from 235-acre Kevin Plank / Goldman Sachs waterfront redevelopment
- **Cycle status:** OZK took deed-in-lieu Dec 2025. Multiple buyers engaged per Gleason. Completed phase ($189M separate) extended through 2028 with Hines as asset manager.
- **Comp read:** Entitled mixed-use land severity 30-50% in non-gateway markets; Baltimore waterfront unique but not gateway.
- **Expected loss this credit:** Current mark at 53% LTV implies ~$75M fair value. Likely sale $30-45M = $10-20M loss IF clean sale. Additional $4.6M charge-off flagged at Q4 2025.
- **Timing:** Management says "active buyer discussions" — resolution 2H 2026.

### #3 — Seattle "Pioneer Square" Office ($25.9M) — SPONSOR: "The Jack" / Urban Visions (HIGH CONFIDENCE, confirmed 2026-04-23 PM)
- **Asset:** **"The Jack"** — 74 S Jackson St, Seattle WA 98104 (Pioneer Square). 145,500 SF, 8-story, class A office + ground retail + rooftop terrace. TCO June 2023. Architect Olson Kundig / GC JTM Construction. **100% vacant since delivery** (JLL marketing 150,776 SF across 11 spaces).
- **Sponsor:** **Urban Visions** (Seattle local developer).
- **OZK origination history:** Urban Visions took original $90M construction loan from **Mack Real Estate Credit Strategies** (Feb 2022 close, JLL-arranged). OZK later took out Mack with $72.5M commitment (exact OZK origination date not yet pinned; King County Recorder search would resolve).
- **Confirmation chain:** Bisnow Sep 2025 ("Cutting its losses") explicitly names The Jack / Urban Visions / 74 S Jackson as OZK's substandard credit. Balance math reconciles exactly: $56.2M (Q4 24 outstanding) − $27.7M (Q1 charge-off) − $2.6M (sponsor paydown) = $25.9M (Q1 26). See KB-OZK-193.
- **Context:** Migrated from substandard accrual to substandard non-accrual Q1 26 after $27.7M charge-off + $2.6M sponsor paydown. Carrying = 100% as-is appraisal Dec 2025. 57 DPD at 3/31/2026.
- **⭐ 7/18 reconciliation (Q1'26 10-Q + Atrium KB-207):** The Jack is disclosed by OZK in the **"Other" loan category** — i.e. it's a **note-assignment / debt-on-debt credit** (part of the ~$490M RESG debt-on-debt book, 10-Q line disclosure), not a directly-originated CRE loan. The 10-Q's "Other" nonaccrual line = **$25.9M, $0 ALL, 30-59 DPD** — matches this credit exactly. **This resolves the 7/6 "conflict":** Atrium's $56M deployed / $16.1M reserve is the ~Q4'25 pre-charge-off state ($56.2M Q4'24 balance); the Q1'26 $27.7M charge-off realized the reserve, leaving $25.9M carried at as-is appraisal with no further ALL — textbook OZK collateral-dependent treatment. **Original-lender attribution:** SEVEN_CREDIT §2 says Mack Real Estate Credit Strategies (JLL-arranged Feb 2022 construction loan); Atrium says "originated by **Claros Mortgage Trust** before collateral assignment to OZK." Given the "Other"/debt-on-debt classification confirms a note-assignment channel, Atrium's Claros-assignment framing is likely the operative one (Mack may have been the original *construction* lender, Claros an intermediate note-holder). Minor open thread; does not affect the figures. **Significance: The Jack is the one *identified* debt-on-debt credit that has already gone bad — a leading tell on the ~$490M note-assignment book that also holds Affinius/SqMile 777 Industrial ($95M) + Southline.**
- **Comp read:** Seattle office vacancy 27.1% (highest US). Stabilized suburban office clearing $240-445/SF; vacant/stressed implied $100-180/SF.
- **Expected loss this credit:** Already at 100% LTV means no further value destruction absent market re-rating. Additional loss on sale likely $3-8M. Cumulative severity on original $72.5M commitment ≈ 38% realized (~$27.7M) with ~$25.9M remaining at risk.

### #4 — Renaissance Milwaukee West Hotel (Wauwatosa, $17.9M)
- **Asset:** 196-key Marriott Renaissance, 12 stories, on Mayfair Mall ground lease. Opened Aug 2020 — never recovered from COVID ramp.
- **Sponsor profile:** HKS Holdings (Milwaukee local developer). NOT institutional (not Apple, Summit, Pebblebrook). Listed for sale via Hunter Hotel Advisors Sep 2025.
- **Cycle status:** 103% LTV on Mar '26 appraisal means **OZK is the borrower now**. 77 days past due, matures Feb 2026. Ground lease with Mayfair Mall (Marcus/Brookfield) constrains buyer pool — mall itself is distressed retail.
- **Comp read:** Select-service / upscale flag hotels in secondary markets opening into COVID have cleared at 40-50% of replacement cost.
- **Expected loss this credit:** Sale band $15-20M gross → $14-18M net to OZK. Additional $2-4M charge-off likely at sale. Existing $5.6M reserve covers most of it.
- **Source:** Bisnow Jan 22 2026 ("Bank OZK Is Cutting Its Losses") — direct confirmation of OZK-Renaissance Milwaukee linkage.

### #5 — Boston Life Sci ($169.3M) — ✅ RESOLVED HIGH (2026-04-23 PM: 10 Prospect Street / USQ Parcel D2.1 / Magellan JV confirmed via UCC-1 filing)

**Verdict:** **Candidate A — 10 Prospect Street, Somerville** is the $169M Boston Life Sci substandard credit. HIGH confidence. Confirmed via post-maturity UCC-1 financing statement filing at Middlesex South Registry of Deeds, Book 85169 Page 222, filed Jan 29 2026.

**Dispositive evidence:**
- **UCC-1 Financing Statement filed Jan 29 2026** (Doc #9975, Book 85169 Page 222) at Middlesex South ROD
- **Debtor:** 31 UNION SQUARE D2.1 OWNER LLC (31 Union Square, Somerville MA 02143) — the parcel-level SPV for USQ Parcel D2.1
- **Secured Party:** Bank OZK (Legal Notices: PO Box 8811, Little Rock AR 72231; filer contact: elizabeth.strickland@ozk.com)
- **Collateral:** "All assets of the Debtor, whether now owned or hereafter acquired, as more particularly set forth and described in that certain MORTGAGE, SECURITY AGREEMENT, ASSIGNMENT OF RENTS AND FIXTURE FILING dated as of December 31, 2020" — original lien recorded Book 76638 Page 224
- **Property:** 10 PROSPECT ST, Somerville MA

**Interpretation of the Jan 29 2026 UCC-1 filing:**
A new UCC-1 filed six weeks after the Dec 18 2025 disclosed maturity is a **classic early-workout re-perfection**. OZK is nailing down lien priority across UCC systems before any enforcement action. Not foreclosure initiation — but an aggressive move to ensure the bank's security interest is bulletproof if enforcement becomes necessary. Consistent with 46 DPD at 3/31/2026 posture: loan is stressed, bank is locking in collateral position, but active foreclosure hasn't been triggered.

**Maturity-mismatch issue resolved:**
The underlying lien instrument is dated **December 31, 2020** (not Feb 1, 2021 as prior research concluded — Feb 1, 2021 was the press/closing announcement, not the docs date). Dec 31, 2020 + 5yr term = Dec 31, 2025. OZK's disclosed **Dec 18, 2025 maturity** is within normal docs-language variance of that 5yr anniversary (stated maturity dates are often ~2 weeks before the anniversary for month-end reasons). Clean fit.

**Asset specs (corroborated 2026-04-23 PM from original Mortgage body text, Bk 76638 Pg 224):**
- **Address:** 10 Prospect Street, Somerville MA 02143 (Union Square redevelopment, Parcel D2.1)
- **Size:** 194,033 SF NRSF total — 173,099 SF Lab/Office (89%) + 12,044 SF Retail (6%) + 8,890 SF Arts & Creative (5%). NOT pure spec lab — mixed-use with retail + A&C components.
- **Delivered:** 2024
- **Tenant status:** Unleased as of Oct 2025 (Bisnow)
- **Original OZK loan:** **$119,200,000 exactly** — primary-source confirmed from Promissory Note description in Mortgage body page 6 ("ONE HUNDRED NINETEEN MILLION TWO HUNDRED THOUSAND AND NO/100 DOLLARS"). Documents dated Dec 31, 2020; recorded Jan 7, 2021; closing/press date Feb 1, 2021.
- **Structure:** Construction mortgage under MA Ch 106 §9-334. **Explicitly "Not a Revolver Facility"** — principal repaid cannot be reborrowed. Implies $169M outstanding reflects original principal + capitalized reserves/fees/extensions, not a follow-on facility.
- **Lien priority:** First and prior; no construction had commenced prior to mortgage = clean priority vs mechanics liens.
- **Guarantor:** Exists (defined in unrecorded Loan Agreement; sponsor-principal level typical for CRE construction).
- **OZK counsel:** King & Spalding LLP (Erik F. Andersen).
- **Body-text confirmation scope:** mortgage body pages 1-10 + 20-22 reviewed; stated maturity date, interest rate, and extension provisions are in the **unrecorded** Promissory Note + Loan Agreement — not obtainable from registry.

**Sponsor JV:** **Magellan Development Group + RAS Development + Cypress Equity Investments + USAA/Affinius Capital** (corrected from prior REGINALD files which incorrectly listed "Cathartes" — see KB-OZK-194). Confirmed per Commercial Observer Feb 2021, Magellan Development press release, BLDUP.

**Sponsor-stack implications for severity:**
Magellan is a large Chicago mixed-use developer (Aqua Tower, Vista Tower). Affinius (formerly USAA Real Estate) is an institutional LP with ~$80B AUM. Cypress Equity is a mid-size mixed-use developer. **This is a well-capitalized institutional JV.** Extension / sponsor capital infusion probability is materially higher than with a typical local Boston JV. Biases severity toward the **lower end** of the 25-40% band (~$40-50M loss) assuming workout path, not forced note sale.

**Balance math — $119M origination → $169M outstanding:**
+42% growth over ~5 years. Likely mechanism: interest reserves originally funded at ~$15-20M were exhausted during rate spike (2022-2023), with subsequent accretion via reserve replenishment + extension fees being capitalized to principal. Prior REGINALD work flagged "$2.6B sponsor extraction" across OZK's RESG book 2023-2025 — Candidate A would have participated in this. Loan may also have been upsized mid-construction.

**808 Windsor / Boynton Yards is NOT this credit:**
Leggat McCall + DLJ + Deutsche Finance America $246M loan (Dec 22 2021) is still an OZK origination but does NOT appear in the Q1 2026 problem book. Could be performing, or classified but below Figure 24 disclosure threshold. **Separately watchable** as a non-named potential-stress credit.

**Cross-reference hygiene:**
- **50 Prospect / 20 Prospect Street** (residential, Union Sq) — separate OZK $120M loan, 25-story 450-unit residential tower. NOT a life sciences asset, NOT this credit. Don't conflate.

**Comp read (unchanged):** Alexandria South Boston lab site Mar 2025 cleared -57% vs 2018 basis. Blackstone BXLS VI ($6.3B Mar 2026) deploying into distressed basis; BioMed/Alexandria NOT buying spec lab. Expected distressed buyer universe: Blackstone, Fortress, Oaktree, SVP, Brookfield.

**Expected loss (revised — narrowed band):** $35-55M loss (from prior 25-40% / $40-65M) on a workout-path resolution. Institutional JV capacity argues for workout attempt before note sale.

**Follow-up value-adds:**
- **Book 76638 Page 224 pull** (original Dec 31, 2020 Mortgage / Security Agreement) — would confirm original loan amount, stated maturity, rate, extension provisions. Not required for verdict; confirmatory only.
- **Any subsequent modifications / extensions** recorded at Middlesex South between 2021 and Dec 2025 — would trace the accretion path.

**KB:** KB-OZK-195 (primary verdict), KB-OZK-194 (sponsor correction), KB-OZK-189 (Q1 26 substandard row — status update needed).

### #6 & #7 — Chapter Buildings I + II, Seattle U District ($127M combined)
- **Asset:** Two towers, 12-story office (Chapter I, 240K SF) + 10-story life sci (Chapter II, 149K SF), connected by pedestrian plaza. Three blocks from UW, one block from U-District Light Rail.
- **Sponsor:** Touchstone (Urban Renaissance Group, Seattle) + Portman Holdings (Atlanta) + Lionstone Investments (Houston LP).
- **🔴 CRITICAL FORCING FUNCTION:** **Parent Ameriprise announced Nov 2024 exit from U.S. real estate advisory business, divesting Lionstone's $5.5B book.** Three Austin assets already transferred to DivcoWest. Chapter Buildings recap is LP-side distress, not sponsor distress.
- **LOI buyer (not publicly named):** Likely candidates: **Blackstone BXLS VI** (just closed $6.3B life sci fund Mar 2026, actively deploying), BioMed Realty (post-$14.6B recap), Longfellow, Harrison Street, or DivcoWest (already a Lionstone transferee).
- **Leasing:** No major tenants 20 months post-delivery. UW's 133K SF lease went to the Gateway Building (different property) — confusion opportunity for bulls.
- **Recap close probability: 50-60%.** Gleason's "executed LOI" language is harder than "in discussion." Blackstone actively deploying. But 27.6% lab vacancy + 28% office vacancy makes "as-stabilized" LTVs optimistic.
- **If LOI closes:** $127M upgrades to accrual. Credit cures. OZK Q2/Q3 credit trajectory improves materially.
- **If LOI fails:** OZK takes title (Gleason said "prepared to"). "As-stabilized" LTVs 73/83% imply as-is value 55-65% of stabilized → loss severity $15-30M on $127M.
- **Cross-signal for BROCK:** Ameriprise/Lionstone wind-down is a new LP-distress pattern — track for other Ameriprise-affiliated real estate funds with upcoming maturities.

### #8 — Schaffer's Mill, Truckee CA ($33.9M)
- **Asset:** 475 acres (exact OZK disclosure match), Martis Valley, Truckee. Originally entitled 2004 as "Timilick"; rebranded 2011 by New Martis Partners / MA Partners.
- **Inventory:** ~100 units remaining (218 original SF custom lots + 188 Mountain Lodge townhomes; ~75% sold by 2025).
- **Why stuck 6+ years at substandard:** Slow absorption (~8-9 closings/yr), TRPA + Martis Valley Community Plan entitlement layering, custom-lot pricing needs amenity buildout. OZK kept advancing on a revolver (why outstanding $34M with $9.4M unfunded).
- **Recovery:** Short sale pending. Management says net ≈ carrying value. Realistic: 15-30% severity = $5-10M loss (matches $8.7M reserve already taken).
- **🔴 Thesis tell:** **OZK holds workout losers on revolvers for 6+ years rather than force charge-off.** Pace of interest + fees > principal paydown. OZK's charge-off lag is measured in years, not quarters. Reinforces reservoir thesis.

### #9 — 8150 Sunset Boulevard, LA ($54.5M Foreclosed)
- **Asset:** 2.5-acre Sunset Strip parcel — the old "Garden of Allah" / Lytton Savings Bank site. Fully entitled 2016: Frank Gehry-designed 249 units (28 affordable) + 65K SF retail.
- **Prior sponsor:** **Townscape Partners** (Tyler Siegel + John Irwin) — JV with TPG Angelo Gordon as "AG-SCH 8150 Sunset Owner LP"
- **OZK originated:** $63.5M construction loan 2021 → took title March 31 2023 (LA Superior Court ruling 23STCV21644). **Oldest foreclosed RESG asset.**
- **Failed buyer:** **OKO Group (Vlad Doronin)** — under contract 2023-2024, walked with $12M forfeited earnest money + extension fees. OKO separately distressed: investors suing Sept 2025 over stalled Fort Lauderdale tower.
- **Why contracts keep failing:** (a) Entitlement risk on condo conversion (approvals are for rental, conversion requires re-entitlement); (b) Dropping Gehry triggers CEQA; (c) LA luxury condo pricing cracked (Oceanwide cleared at ~50c on cost); (d) 65K SF retail component = dead weight.
- **Recovery:**
  - Base case: $45-55M clearing (minimal additional loss)
  - Bear case: $30-40M (Gehry scrapped, re-entitled as multifamily rental) → $15-25M further loss
  - Bull case: $60M+ (luxury developer accepts affordable units) → OZK books gain on forfeited earnest money
- **Severity verdict:** Low-variance position in RESG foreclosure stack. Not where the big loss lives.

### #10 — 1229 W Concord Place, Chicago ($50.0M Foreclosed)
- **Asset:** **320K SF** fully vacant lab building — the **sole completed Lincoln Yards building**. [size corrected 284K→320K, 2026-07-04 web verify]
- **Sponsor:** **Sterling Bay + Harrison Street** JV (JPMorgan investment arm also an investor); OZK relationship collapsed. **Same sponsor pair as San Diego Pacific Center** — see the Sterling Bay pattern in `WEAKNESSES.md` C7.
- **Path:** Original $65M loan → sponsor short sale failed Q1 → OZK took **deed-in-lieu March 2026**. **OZK plans to reposition lab→traditional office** (leadership: "an office use in particular is absolutely an executable transaction") — life-science re-tenanting buildout too costly.
- **Comp read:** OZK's own Lincoln Yards northern acres cleared Sep 2025 at $84M/$126M loan basis = -33%. Concord Place currently marked at 68% of May '25 appraisal (~$74M).
- **⭐ 7/18 — the separate $128M Lincoln Yards LAND loan VERIFIED [KB-208, was unverified]:** This is a **distinct Sterling Bay credit** from the Concord *building* above (= the "$126M basis / northern acres" comp). Facts pinned via Bisnow/TRD/Crain's: OZK loan originated **Dec 2019**, **~27 acres** northern Lincoln Yards (former A. Finkl & Sons steel site), **modified 6×**, writedown $21M (Oct 2024) → **$38M (Mar 2025)**, **deed-in-lieu March 2025**, now under contract to **JDL Development**. Severity ~30% ($38M / $128M) on the land — a **realized Sterling Bay Lincoln Yards severity comp**. Atrium's "2024 foreclosure" label was off by a year (2024 = first writedown; deed-in-lieu = Mar 2025). **Already resolved pre-Q1'26 → NOT a live roster credit**; it's a historical severity datum, not incremental to the $719.8M book. [[finding_deep_research_stale_vintage_headline]]
- **Expected loss:** Sale likely clears below $40M = 55-60% loss vs original loan (Chicago life-sci supply doubling through 2026; Fulton Labs 400 N Aberdeen only >30% leased since 2022). *Office-pivot may alter severity math — monitor.*
- **Additional charge-off:** $10-15M likely on resolution.

### #11 — 1650 Euclid Street, Santa Monica ($45.1M Foreclosed)
- **Asset:** 65K SF creative office, 15% leased
- **Sponsor:** Private creative office developer (not institutional). Sponsor stopped paying; OZK took title Q1 26 with $5M additional charge-off.
- **Context:** Santa Monica availability 34.6%; creative office (converted warehouses/lofts) has been hit hardest in the LA office pullback.
- **Comp read:** Westside LA land is holding value ($13.9M/acre Pico trade 2025), but DTLA/Hollywood stalled entitled parcels have cracked 45-68%. Creative office occupies middle — likely 40-50% severity.
- **Expected loss:** $15-25M additional on sale (bringing total to $20-30M charge-offs vs original ~$55-60M loan).

---

## 3. EXPECTED LOSS ROLL-UP vs ACL COVERAGE

### Per-credit EL estimates

| # | Credit | Q1 Balance | Severity Band | Loss $ (mid) |
|---|---|---|---|---|
| 1 | Sullivan Courthouse (post-charge-off) | $156.4M | 40-50% | **$70M** |
| 2 | Baltimore Peninsula | $40.0M | 25-50% | $15M |
| 3 | The Jack (Seattle) | $25.9M | 15-30% | $6M |
| 4 | Renaissance Milwaukee West | $17.9M | 15-25% | $4M |
| 5 | Boston Life Sci (TBD) | $169.3M | 25-40% | **$55M** |
| 6+7 | Chapter Buildings (blended LOI close/fail) | $126.8M | 10-20% weighted | **$20M** |
| 8 | Schaffer's Mill | $33.9M | 15-30% | $8M |
| 9 | 8150 Sunset | $54.5M | 0-30% | $10M |
| 10 | 1229 W Concord Place | $50.0M | 25-35% | **$15M** |
| 11 | 1650 Euclid Santa Monica | $45.1M | 35-50% | $19M |
| | **Total $ EL (mid)** | **$719.8M** | **~30%** | **~$222M** |

**Range (agent comp work):** **$211-291M** blended expected loss across identified problem book.

### Reserve adequacy

| Metric | Value | Read |
|---|---|---|
| OZK ACL Q1 26 | **$628.5M** | — |
| EL on current disclosed problem book | **$211-291M** | 2.2-3.0x coverage |
| Q1 26 Provision | $41.9M | — |
| Q1 26 NCOs | $45.3M | 0.57% annualized |
| **Implied scenario if problem book doubles to $1.4B (migration wave):** | | |
| EL at doubled book | **$420-580M** | 1.1-1.5x coverage — thin |
| Required reserve build over 4 quarters | **$150-300M** | ~$38-75M/quarter incremental provision — 2-3x Q1 26 pace |

**Reserve adequacy verdict:**
- **TODAY:** $628M ACL is sufficient. OZK is not under-reserved on the disclosed problem book.
- **12-MONTH FORWARD:** If the past-due doubling ($207M → $465M QoQ) continues its leading-indicator pattern and the problem book migrates to $1.0-1.4B by Q4 26, the **reserve build pace must accelerate 2-3x.** This is the structural headwind on 2026 earnings we should be modeling.
- **Gleason's FY guide of ~50bps NCO is consistent with $211-291M loss bucket realization spread over 2026-2027.** It does NOT bake in a migration wave.

---

## 3A. REST OF PROBLEM BOOK — THE UNMAPPED ~$496M

*Added 2026-04-23 after Q1 Mgmt Comments + Financial Supplement re-scan (Spawn audit).*

The 11 credits above total **$719.8M** of the **$1,215M** total classified+criticized book reported in the Q1 26 Financial Supplement (p.4). That leaves **~$495M unmapped** at the project level. Characterizing this gap matters for (a) sizing the migration wave risk (§3), (b) deciding whether the next research push should prioritize MassLandRecords-style forensic project-ID work vs waiting for the May 1-10 Call Report.

### Reconciliation to $1,215M

| Tier | Total (Supp p.4) | Named in §1 | Gap | Gap character |
|---|---|---|---|---|
| Special Mention | $397M | $0 | **$397M** | **Fully opaque** — not itemized in earnings release, Figure 24, or supplement. First resolvable at Q1 Call Report (FFIEC RC-N, ~May 1-10). |
| Substandard Accrual | $367M | ~$330M (#5, #6, #7, #8) | ~$37M | Likely small-ticket RESG accrual credits under Figure 24's reporting threshold. |
| Substandard Non-Accrual | $297M | ~$240M (#1, #2, #3, #4) | ~$57M | Same pattern — sub-threshold RESG names not individually disclosed. |
| Foreclosed Assets | $154M | $149.6M (#9, #10, #11) | ~$4M (immaterial) | Likely rounding / small carrying-value adjustments. |
| **Total** | **$1,215M** | **$719.8M** | **~$495M** | |

### What the gap is, and what it isn't

**82% of the gap ($397M) is Special Mention** — the lightest classification tier (30-89 day past-due or "potential weakness" flag before formal substandard). OZK does not publish a Special Mention roster. The Q1 Call Report (RC-N) will itemize by asset class and geography but typically not by borrower. Project-level identification of Special Mention credits is essentially impossible before forensic work on individual CMBS / county record filings.

**The remaining ~$98M ($57M substandard non-accrual + $37M substandard accrual + $4M foreclosed) is sub-threshold RESG.** Likely a long tail of $5-15M credits collectively not disclosed. Individually small; collectively material only if they migrate as a cohort.

### Non-RESG blind spot (possibly zero, possibly not)

Figure 24 and the "problem credits" narrative in Mgmt Comments cover **RESG only**. Mgmt Comments does not publish a separate classified-asset roster for CIB, Community Banking, or Indirect RV & Marine. The press release and call narrative *imply* these segments are clean, but imply is not disclose.

- **CIB ($6.2B, 18.8% of loans):** Jake Munn's Q1 comments highlighted pricing compression (Fund Finance, LFG) but **did not disclose any CIB classified assets**. If CIB contained meaningful problem credits, they would likely appear in Figure 24 under RESG-adjacent framing or in MD&A footnotes — neither does.
- **Indirect RV & Marine:** NCO 0.42% is super-prime clean (per prior KB), strongly implies minimal classified exposure.
- **Community Banking:** No commentary.

**Working baseline:** non-RESG classified is <$50M. Upside risk if CIB lines tracked separately in the 10-Q / Call Report show larger classified balances.

### What this means for research prioritization

1. **Do NOT chase the $397M Special Mention bucket through forensic research** — labor-to-signal ratio poor. Wait for Q1 Call Report (~May 1-10) to pick up whatever it discloses, then triage.
2. **The ~$98M sub-threshold RESG tail is probably not actionable.** No single credit is large enough to change severity math. If Q2 26 shows a migration cohort emerging (more names appearing in Figure 24), revisit.
3. **Boston Life Sci #5 sponsor ID (TODO #1) remains the highest-value forensic target** — one credit, $169M outstanding, material to thesis.
4. **Non-RESG classified blind spot is worth one pass at the 10-Q (~May 5)** to verify the zero-substandard-in-CIB implication. 30-minute check, not a research project.

### Data-quality caveats

- The $719.8M "named" total includes Seattle U Dist Office ($76.4M) and Life Sci ($50.4M) outstanding balances from Figure 24; if you include their unfunded accrual commitments ($30.5M + $38.9M), the named total rises to $828M. That version of the math shrinks the gap to ~$387M.
- Prior versions of this file and TODO.md used $719M — mathematically consistent with outstanding-only treatment of Seattle U Dist. **Do not compare this $495M gap to "$496M" in older docs without checking which outstanding basis was used.**

---

## 4. CROSS-AGENT SIGNALS

### 🔴 To BROCK — NEW pattern: LP-dissolution as credit trigger
**Signal:** Ameriprise exiting U.S. RE advisory business, divesting Lionstone's $5.5B book, is the forcing function on OZK's Chapter Buildings recap — not sponsor distress. Recommend BROCK screen other Ameriprise-affiliated RE funds (and peer advisors rumored to be consolidating: e.g., Clarion, Invesco RE, Nuveen) for upcoming loan maturities where LP-wind-down could be the credit event.

### 🟠 To CREED — Boston life sci concentration confirming
**Signal:** OZK's Boston life sci problem book now includes $156M Sullivan (office, severe) + $169M new substandard Q1 26 (candidate 10 Prospect or 808 Windsor — both are post-2021 spec lab). Cambridge lab vacancy **28.8% record high.** Alexandria's own dispositions (-57% vs 2018 basis on S. Boston sale Mar 2025) confirms market-wide severity. Cross-reference CREED CMBS life sci DQ data for Boston-MSA trajectory.

### 🟠 To CARL — Not firing this thread
Consumer / auto thread unaffected. OZK indirect RV/Marine NCO 0.42% (prime/super-prime clean). Cross-agent confirmation: the OZK problem book is **100% CRE-driven**, zero consumer-credit bleed.

### 🟡 To LIQUID — Confirming OZK offensive FHLB signature
Nothing new this thread. Still confirms OZK's $350M Other Borrowings is offensive carry trade, not funding-stress (unlike MTB/CFG/PNC).

### 🟡 To FORGE — Position note
⏹️ ***[dated-tag 2026-08-23 — the two bullets below are HISTORICAL duration reasoning for legs that have all expired. Preserved as the record of why the Aug tenor was chosen; not a live read.]***

- **$45P May 15:** Expiry too tight. Per comp work, major loss realizations pace Q2-Q3-Q4 2026, not May. Roll to Aug or Sep merits analysis (separate Thread 3).
- **$42.5P Aug:** Correct duration. Aug captures (a) Q2 reserve build acceleration confirmation, (b) IQHQ maturity, (c) Chapter Buildings LOI close/fail.

---

## 5. OPEN QUESTIONS / FOLLOW-UPS

1. **Boston Life Sci $169M disambiguation** — Check Middlesex County ROD for OZK mortgage assignments post-Q4 2025; 10-Q (~May 5) may disclose in MD&A footnotes; Q2 earnings call (late Jul) is last resort.
2. **Seattle Pioneer Square "The Jack"** — Verify project ID via King County records; could also be a different Pioneer Square submarket credit.
3. **Chapter Buildings LOI buyer identity** — Watch Blackstone BXLS VI press / BioMed Realty press / DivcoWest for Seattle lab acquisition announcements Q2-Q3 26.
4. **Affinius Oct 2026 $2.7B bond maturity** — NOT mentioned on OZK Q1 call. CALENDAR had this tagged to OZK. CREED follow-up: is OZK actually exposed to this credit or is this a false flag from prior research?
5. **Schaffer's Mill 6+ year workout datapoint** — Update `workbook/KB.tsv` with OZK charge-off tempo observation. Feeds "reservoir thesis" structural framing.
6. **IQHQ separate** — Aug 2026 maturity is Thread #2 (scenario-modeled separately). Not in this $719M problem bucket yet (still passing).

---

## 6. UPDATES REQUIRED TO OTHER FILES

- [ ] **`Q1_2026_ANALYSIS.md` §1a/1b/1c tables** — append sponsor column with findings from this deep dive
- [ ] **`OZK/STATUS.md`** — add sponsor IDs to Five RESG Problem Credits section (currently last updated Apr 7, pre-Q1 print)
- [ ] **`OZK/GEOGRAPHY/EXPOSURE_MAP.md`** — update LA section with 8150 Sunset specific parcel ID; Seattle section with Chapter Buildings identity; confirm "The Jack" vs Pioneer Square nomenclature
- [ ] **`OZK/LIFE_SCI/STATUS.md`** — add 1229 Concord foreclosure (Chicago, not SD — different list), flag Boston $169M candidate list
- [ ] **`OZK/workbook/KB.tsv`** — new rows for (a) Renaissance Milwaukee West HKS Holdings, (b) Chapter Buildings + Lionstone wind-down, (c) 8150 Sunset / Townscape / OKO Group failed buyer, (d) Schaffer's Mill / New Martis / OZK 6-year workout tempo observation
- [ ] **`workbook/OTTO_INTEL.md` OR `CREED/`** — cross-agent signal on Ameriprise/Lionstone LP wind-down as new credit pattern
- [ ] **`STATUS.md` (root REGINALD)** — OZK bank line can reference this file for problem book detail; matrix score doesn't change

---

*Deep dive complete. All sponsor IDs sourced via external research agents Apr 22 2026; comp data sourced from 2025-2026 distressed CRE transaction record. Boston Life Sci #5 remains the only material ambiguity.*
