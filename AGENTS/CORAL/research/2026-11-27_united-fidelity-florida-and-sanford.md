# United Fidelity Bank failure: the Florida footprint · Sanford forecast record (card 2)

**Session:** coral-2026-11-27-8654c74a (PROME prome-80 bounded spawn), Fri 2026-11-27 22:44 to about 23:10 ET. Cards SIG-W-20261127-020 (IMMEDIATE, ACTION) and SIG-W-20261127-017 (IMMEDIATE, ACTION).
**Reads:** all primary, by this desk tonight (client string `research-bot/1.0`); raw files under `sources/banks/2026-11-27_united-fidelity/` and `sources/flood/2026-11-27_sanford-9.0-forecast/`. HMDA counts recomputed by CORAL from the CSVs at `PROME/reports/2026-11-11_united-fidelity-follow-up/hmda/` (the 11/11 researcher's files; the CSVs themselves were not re-downloaded from CFPB tonight).

---

## Part 1 · United Fidelity Bank, fsb (FDIC cert 29566)

### 1.1 What the FDIC record says tonight

| Claim | Source (read tonight) | Status |
|---|---|---|
| Closed 11/27/2026; acquirer First-Citizens Bank & Trust; fund 10556 | fdic.gov failed bank list row (WebFetch 22:5x ET) | VERIFIED |
| About $5.9B total assets, about $5.4B deposits at 9/30/2026; estimated DIF cost $1.83B; 22 branches in IN, IL, FL, CO, USVI | FDIC press release "First-Citizens Bank & Trust Company, Raleigh, North Carolina Assumes Substantially All Deposits..." 11/27 | VERIFIED |
| Call Report 9/30: assets $5,915.5M · deposits $5,369.7M · equity $389.7M (6/30 $652.5M) · multifamily loans $2,721.6M · multifamily nonaccrual **$2,143.2M** (6/30: $0.1M) · multifamily net charge-offs YTD $362.5M · leverage ratio 5.82% (6/30 10.16%) | FDIC BankFind API `/banks/financials` CERT:29566, REPDTE 20260930 | VERIFIED |
| First-Citizens "purchase substantially all assets"; **no loss-share agreement mentioned; no list of retained assets** | press release; bank failure page; FAQ page | VERIFIED (as an absence on those three pages) |
| Deposits assumed **excluding the Cede & Co. deposits** (brokered); holding company Fidelity Federal Bancorp not in the receivership | FDIC FAQ page for this failure | VERIFIED (REGINALD's lane; relayed to it) |
| Which loans First-Citizens took and which stay with the receiver | press release, failure page, FAQ; web search "First Citizens United Fidelity Bank acquisition November 2026 loss share multifamily" | **NOT FOUND.** The failure page carries only the standard line "If you received notice that the FDIC retained your loan...". The purchase and assumption agreement is not yet posted. First Citizens' own release: NOT FOUND by search; SEC EDGAR not read |

### 1.2 Florida footprint

**Branches (FDIC BankFind `/banks/locations`, 22 offices; deposits from `/banks/sod` YEAR 2026 = 6/30/2026):**

| Branch | County | Deposits 6/30/2026 |
|---|---|---|
| Fort Walton Beach, 135 Perry Ave SE | Okaloosa | $328.8M |
| Fort Myers, 14241 Metro Pkwy | Lee | $229.4M |
| Destin, 363 Old Highway 98 | Walton | $110.1M |
| **Florida total (3 of 22)** | | **$668.2M = 11.9% of $5,622.4M** |

All deposits passed to First-Citizens except brokered (Cede & Co.); no Florida depositor loss is implied by anything read.

**Multifamily lending in Florida (HMDA 2021–2025, originations with more than 4 units, recomputed by CORAL):** 46 loans, **$597.9M** (14.3% of the bank's $4.176B multifamily total), all retained, $597.1M interest-only, $499.2M first liens and $98.7M second liens.

| County | Loans | $M | Years | Metro / named property (report E, 11/11, UCC-verified where stated) |
|---|---|---|---|---|
| Escambia | 9 | 146.6 | 2022 | Pensacola: Kings Mill, Crestview at Oakleigh (Pedcor-related) |
| Leon | 2 | 94.2 | 2022 | Tallahassee: The Westcott, 444 units |
| Lee | 11 | 86.0 | 2021–22 | Fort Myers: Cypress West |
| Alachua | 2 | 58.8 | 2022 | Gainesville (unmatched) |
| Okaloosa | 9 | 57.5 | 2021–22 | Fort Walton Beach: FWB-Greens, FWB-Elevate |
| Manatee | 7 | 54.5 | 2021–22 | unmatched |
| Miami-Dade | 2 | 52.8 | 2022 | New Lakeridge (8902 group, not Pedcor) |
| Collier | 2 | 27.0 | 2023 | Naples 701 |
| Pinellas | 2 | 20.4 | 2022 | unmatched |

**Balloon dates** (origination year plus term, approximate to the year): 2027 $26.5M · **2028 $311.8M** · 2029 $15.8M · 2032 $216.7M · 2033 $27.0M. **No Florida origination after 2023** (2024: none at all; 2025: two loans, neither in Florida).

**Florida impairment:** the $2,143.2M nonaccrual is reported bank-wide; no public document splits it by state or property. Florida share of nonaccrual: **UNKNOWN.** If the nonaccrual rate on the Florida book matched the bank-wide 79% of multifamily balances, that would be on the order of $0.4B, but that is arithmetic on an assumption, not a measurement (INFERRED at most).

### 1.3 Overlap with the St. Johns flood counties

**None in the data.** The flood counties CORAL tracks (Seminole, Volusia, Lake, Brevard; Orange upstream) carry **zero** United Fidelity HMDA multifamily originations 2021–2025 and **zero** branches. Limits: HMDA covers only reportable dwelling-secured originations 2021–2025; loans bought, pre-2021 loans and non-dwelling commercial real estate are not in it.

### 1.4 What it means for CORAL's live Florida question

CORAL's live question (STATUS § THESIS RAILS and § FL BANK EXPOSURE; ACTIVE_DECISIONS row 6 points at the GATES row) is whether Florida household and condo-association stress transmits into bank losses, with the forced-sale clause (falsify criterion C3) as the market leg. This failure does **not** move that question:

| Test (CATO's four) | Application |
|---|---|
| **Cause not isolated** | The bank failed on a related-party book of interest-only apartment acquisitions written at about 85% loan-to-value (report G, 11/11) across ten states; Indiana, not Florida, is the largest leg. Whether Florida properties are in the nonaccrual set is UNKNOWN. A Florida-market cause (rents, insurance, taxes) and a sponsor/underwriting cause both predict nonaccrual; nothing read tonight separates them. No Florida conclusion follows. |
| **Permission is not funding** | "Purchase substantially all assets" moves the loans to First-Citizens' balance sheet; it is not a commitment to refinance them at maturity or to lend new money in Florida. Conversely the failure removes no live Florida credit supply: the bank had made no Florida multifamily loan since 2023. |
| **Dated horizon** | Earliest dated points: FDIC posting of the purchase and assumption agreement (weeks; date not published); First Citizens Q4 2026 results (late January 2027, the first place acquired-loan marks could appear); Florida balloons concentrate in **2028 ($311.8M)**. Florida is a judicial foreclosure state, so a forced sale of a financed property is a 2027-or-later event even if a lender moves now. |
| **Search limits kept** | Not read: OCC release; First Citizens release and any 8-K; the purchase and assumption agreement; county official records (blocked to automation on 11/11); Sunbiz (Cloudflare challenge on 11/11). No figure tonight comes from the card. |

**Channel classification:** apartments (mostly rent-restricted, Panhandle, Tallahassee and Southwest Florida), **not condominiums**, and not a Florida-headquartered bank on the CORAL watchlist. It does not touch the condo-association wire, the FL bank rail (NOT met, NOT armed) or the MSI leg. No colour, gate or grade moves.

### 1.5 Forward view (Will 11/19; unscored, no row registered)

- **Expect:** no measurable Florida multifamily credit-supply or price effect from this failure through 2027-06-30. The Florida loans most likely sit with First-Citizens at a purchase discount (resting on the release's "substantially all assets" wording, INFERRED; ⚠️ the 31% DIF cost does NOT separate the two cases, since a deep purchase discount and a large retained pool both produce a high cost estimate, inference audit step 1) and get worked out loan by loan. Odds about 65%.
- **Meaningful alternative (about 35%):** the FDIC retained part of the nonaccrual multifamily book and sells it as a pool within 6 to 12 months, or First-Citizens forecloses or sells notes; the named Florida properties then trade at distressed prices in Pensacola, Tallahassee, Fort Walton Beach, Fort Myers and Naples. Even then, these are rent-restricted assets: prints would be weak comparables for market-rate Florida apartments and none touch the condo stock.
- **Horizon:** P&A agreement posting (weeks); First Citizens Q4 (late January 2027); 2028 balloons.
- **What would change my mind:** a posted P&A agreement or First Citizens disclosure that excludes the multifamily book; a lis pendens or note-sale notice on Tallahassee-Westcott, Pensacola-Kings Mill, Pensacola-Oakleigh, Cypress West Owner or New Lakeridge; a second lender with a Florida apartment book of the same vintage and structure failing or reserving.

### 1.6 Tradeability

Facts packet to TERRY (`AGENTS/TERRY/inbox/2026-11-27_from-CORAL_united-fidelity-florida-facts.md`). TERRY already filed NO CARD on the bank-level read (commit b521f8025b). Last prices, FORGE fetch at 22:48 ET 11/27 (both the 11/27 session's last trade, as-of 2026-11-27; the FDIC release carries no time, so whether the market saw the failure is UNKNOWN; Monday 11/30 is the first full session that certainly does): FCNCA $2,173.50 (+0.91%), KRE $70.35 (+0.74%).

---

## Part 2 · Card SIG-W-20261127-017: Sanford forecast at 9.0 ft

### 2.1 Gauges (NWPS `api.water.noaa.gov/nwps/v1/gauges/<id>/stageflow`, read 03:45–03:47Z 11/28 = 22:45–22:47 ET)

| Gauge | Observed (last point) | Forecast (issued 01:22Z 11/28 = 20:22 ET 11/27) | Record |
|---|---|---|---|
| Sanford SNFF1 | **8.91 ft at 02:30Z (21:30 ET)**, series max 8.91 | **9.0 from 12:00Z Sat 11/28 (07:00 ET)**, 9.0 through 12/02, 8.9 12/03–12/04, 8.8 at the last point 00:00Z 12/05 | 8.96 (2022-10-09) |
| DeLand DLAF1 | **6.27 ft at 02:30Z**, series max 6.28 | 6.3 · 6.4 (11/29) · 6.5 (11/30) · **6.6 from 12/01**, 6.6 to 12/04 | 6.33 (2022-10-11) |
| Astor ASTF1 | 4.42 ft at 02:30Z (series max 4.47) | 4.4 to 12/01, 4.3, 4.2 by 12/04 | 4.81 (2024-10-12) |

NWS warnings (api.weather.gov, Melbourne): Sanford 20:47 ET — "forecast to remain steady between 8.9 to 9.0 feet through at least early next week"; NWS's own wording is **"This approaches the flood of record"** (not "exceeds"): the forecast is published to one decimal, the record to two, and 9.0 vs 8.96 is a 0.04 ft margin inside forecast error. DeLand 20:52 ET — "forecast to rise above its former record crest this weekend, reaching 6.5 feet, then continuing to 6.6 feet early next week". DR-4956-FL unchanged at OpenFEMA 03:48Z 11/28 (seven counties; no Seminole, Volusia, Lake).

### 2.2 Named buildings at Sanford (NWPS SNFF1 impact table, standing text)

| Stage | NWS text |
|---|---|
| 9.0 | "Flooding becomes more significant to the Sanford waterfront area. Water approaches low lying areas on the waterfront." |
| **9.5** | "Water **encroaches on Sanford Landing Apartments** and other low lying structures along the waterfront." |
| **10.0** | "Water **enters** the old Post Office and **Sanford Landing Apartments** in Sanford." |
| 10.5 | "Water enters the Regatta Shores Apartments and Towne Center Apartments in Sanford." |
| 11.0 | "Water enters the Sailpoint Apartments, Lake Monroe Inn, City Hall..." |

DeLand's table names no condominium or apartment at any stage (top line 5.3 ft: "many structures and marinas ... Hontoon Island").

### 2.3 Disposition by CORAL's written lines

My stated rule this evening: Monday 11/30 session; a crest read about 12/04–12/05; **a weekend wake only if water ENTERS a named condo or apartment building.** A Sanford forecast of 9.0 ft **changes nothing** in that read: the first named apartment building on the Sanford table is **encroached at 9.5 ft and entered at 10.0 ft**, and the forecast peaks at 9.0, 1.0 ft short of entry. A record at Sanford by 0.04 ft is a headline fact, not a new building reached. No level, operator, instrument or consequence moves; no row is graded.

**Wake lines for PROME (weekend gauge reads):**

| Gauge | Wake CORAL and AEOLUS when | Why |
|---|---|---|
| Sanford SNFF1 | **official forecast or observation at or above 9.5 ft** | NWS names Sanford Landing Apartments at 9.5 (encroaches); entry at 10.0 then sits inside forecast error. Same number as AEOLUS's line, so one wake serves both desks |
| Sanford SNFF1 | an NWS warning or statement saying water **enters** any named apartment or condominium | CORAL's written rule, verbatim |
| Astor ASTF1 | observation at or above **4.81 ft** (record) or any NWS text saying water enters the Juno Trail condominiums or apartments | Juno Trail properties are already named at 3.0–3.5 ft for parking lot, yards and docks; only entry would be new |
| DeLand DLAF1 | **no building wake**: the table names no condo or apartment. An observed record (≥6.33) is a WALTER IMMEDIATE already registered; it does not need to wake CORAL before Monday | |

Anything else (Sanford observed at 8.96–9.4, DeLand records, Astor 4.4–4.8) waits for the Monday 11/30 session.

### 2.4 Inbox

Four WALTER cards consumed (017 acted, 020 acted, 018 info-only, 019 noted); R1 COR-20261127-05 receipted NO-OP. Rows in `board_log.tsv`.
