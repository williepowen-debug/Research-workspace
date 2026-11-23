# REGINALD -> PROME: Florida flood, which banks' commercial real estate is most exposed (DOCKET 2026-11-24 FLORIDA FLOOD TRANSMISSION SWEEP, lane 4)

**Written:** 2026-11-23, session from 16:34 ET (`date`), PROME prome-77 task on Will's word (16:26 and 16:33 ET). Claude Code, Opus 5.5, session id not exposed. Lane: banks only. Insurance, HOAs and condo law are CORAL's; CRE collateral and CMBS are CREED's; home values are HOMER's. The harness refused a separate report file (as on 11/23 morning), so this memo carries the full read. Data and scripts: `AGENTS/REGINALD/reports/2026-11-23_florida-flood-bank-exposure/` (`sodagg.py`, `rank.py`, `table_rows.txt`).

## 1. Ranked table (listed banks)

**Sources and dates.** Deposits and branches: FDIC Summary of Deposits, 6/30/2026 (`api.fdic.gov/banks/sod`, pulled 11/23 16:43 ET; 4,283 Florida branches, $876.6B). Balance sheet: Call Report 6/30/2026 through FDIC BankFind (pulled 16:44 ET). **9/30/2026 is not yet in BankFind, and I did not pull Q3 10-Q ratios, so every ratio is 6/30.** Basin (flooding observed or warned): Brevard, Seminole, Volusia, Lake, Putnam, Flagler; $47.1B of deposits, 371 branches. Southeast (Flood Watch Tue evening 11/24 to late Wed 11/25): Palm Beach, Broward, Miami-Dade, Martin, St. Lucie, Indian River; $368.2B, 1,462 branches. CRE uses the interagency basis: construction, multifamily, non-owner-occupied nonresidential and RCON2746, divided by Tier 1 plus Tier 2 capital. Supervisors screen at 300% for CRE and 100% for construction. Problem loans means 30 to 89 days past due, plus 90 or more days, plus nonaccrual, over gross loans.

| Rank | Ticker | Basin $B (branches) | Basin share of deposits | Southeast $B (branches) | SE share | CRE / capital | Construction / capital | Multifamily / capital | Problem loans | Why |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SBCF** Seacoast | 2.09 (15) | **12.4%** | 7.43 (37) | 44.2% | 230% | 40% | 22% | 0.81% | The only listed bank in both the flooded basin and the watch area; 2025 residential originations 31.3% in its five Treasure Coast and Brevard counties (HMDA, my 11/18 read); county CRE NOT DISCLOSED |
| 2 | **USCB** U.S. Century | 0 | 0% | 2.48 (10) | **100%** | **347%** | 13% | **102%** | 0.15% | Whole franchise in Miami-Dade and Broward, above the 300% line. Its 10-K confirms Association lending but does not size it. CORAL (9/28, 11/06): the "condo commercial" $68.7M line is NOT the association book |
| 3 | **AMTB** Amerant | 0 | 0% | 8.23 (22) | **98.4%** | 218% | 49% | 24% | **2.96%** | Highest problem-loan ratio of the listed southeast names; already matrix 5 on non-CRE credit |
| 4 | **BKU** BankUnited | 0.10 (2) | 0.3% | 19.83 (38) | 68.2% | 201% | 17% | 32% | 2.44% | Largest listed southeast dollars. $21.3M of CRE 30 to 89 days late at Q3, location unknown (my 11/06 read). HOA deposits $2.4B (CORAL) |
| 5 | **OPHC** OptimumBank | 0 | 0% | 1.22 (4) | 100% | **504%** | 33% | 38% | 1.20% | Highest CRE intensity of any listed name; small ($1.4B of assets) |
| 6 | BPOP (Popular Bank, US sub) | 0 | 0% | 3.95 (12) | 33.1% | 311% | 74% | 113% | 0.68% | A third of the US sub; small against the parent |
| 7 | HOMB (Centennial) | 0.02 (1) | 0.1% | 2.88 (20) | 14.7% | 258% | 88% | 40% | 0.72% | |
| 8 | SSB SouthState | 1.38 (13) | 2.4% | 3.62 (21) | 6.4% | 282% | 40% | 37% | 0.72% | Second-largest listed basin dollars, small share |
| 9 | VLY Valley | 0.16 (3) | 0.3% | 3.94 (14) | 7.2% | 327% | 35% | 127% | 1.23% | |
| 10 | FHN First Horizon | 0.12 (3) | 0.2% | 5.68 (26) | 8.3% | 153% | 17% | 39% | 0.97% | |
| — | FLG Flagstar | 0 | 0% | 3.32 (25) | 4.9% | 332% | 14% | 269% | 5.58% | Its stress is New York multifamily, not Florida |
| — | TFC Truist | 7.97 (52) | 1.9% | 22.79 (128) | 5.4% | 74% | 13% | 15% | 1.25% | Largest basin dollars of any bank, an immaterial share |
| excluded | NEWT Newtek | 0 | 0% | 2.22 (1) | 100% | 231% | 49% | 72% | 10.74% | One booking branch in Miami-Dade and a national SBA lender, so its deposit geography says nothing about where its collateral is |

The big national banks hold 3% or less of their deposits in these counties: Bank of America $7.7B basin and $57.0B southeast, Wells Fargo $7.2B and $40.0B, JPMorgan $5.7B and $45.7B.

**Unlisted banks with the heaviest exposure (Call Report only, no 10-Q):**

| Bank | Basin share | SE share | CRE / capital | Construction / capital | Problem loans |
|---|---|---|---|---|---|
| Mainstreet Community Bank of Florida (DeLand), $0.79B, 8 branches | 92.1% | 0% | 292% | **97%** | 1.27% |
| United Southern Bank (Lake County), $0.73B, 12 branches | 95.2% | 0% | 224% | 53% | 1.67% |
| Intracoastal Bank (Flagler), $0.52B | 100% | 0% | 301% | 71% | 0.13% |
| Sunrise Bank, $0.29B | 52.6% | 0% | 387% | 53% | 0.11% |
| One Florida Bank, $0.62B | 34.2% | 0% | 298% | 38% | 0.19% |
| City National Bank of Florida (owned by BCI of Chile), $21.37B | 0% | 96.7% | 272% | 46% | 1.02% |
| Ocean Bank, $6.19B | 0% | 99.7% | **528%** | 38% | 0.51% |
| Banesco USA, $4.28B | 0% | 82.7% | 221% | 24% | 0.55% |
| International Finance Bank, $1.32B | 0% | 90.6% | 448% | 31% | 0.48% |
| Pacific National Bank, $1.31B | 0% | 98.5% | 360% | 64% | 0.07% |

**What I could not size, and why:** (a) **CRE by county, for every bank.** No Call Report or 10-Q schedule carries it; HMDA covers home loans only, and CRA data cover small-business loans only. (b) **Condo-association loans.** All seven Florida 10-Qs CORAL read (11/06) disclose none. (c) **Flood insurance on collateral.** No filing quantifies it. (d) **Q3 2026 figures.** Not posted in BankFind, and the FFIEC 9/30 bulk file was not kept on this laptop. (e) **Damage by county.** That is CORAL's read. ⚠️ **Deposits show where a bank operates, not where its loans sit. The table maps where exposure could be; it is not a loss estimate.** Unknown geography stays unknown, never zero (CATO 11/23, FF23-1).

## 2. Mechanism, honestly

| Channel | How it reaches the bank | When it would show | Evidence today |
|---|---|---|---|
| Deposits | Households and associations draw savings for repairs, then insurance and aid money lands as deposits | Weeks; net usually an inflow after the first month | None read. After Michael (2018), the three most concentrated local banks' deposits rose 9% to 11% the next quarter |
| Borrower cash flow | Businesses close and tenants leave; owners pay from reserves or stop paying | 1 to 2 quarters: first as 30 to 89 days past due and as payment deferrals | None |
| Uninsured collateral damage | Standard property policies exclude flood. Commercial NFIP cover caps at $500,000 per building and is required only inside the mapped flood zone, on federally regulated loans. Damage outside the zone or above the cap is a hole in the collateral | 2 to 4 quarters: impairment, then modification, then charge-off | Unknown. The owner's equity absorbs it before bank principal; the bank is hit only where the loan-to-value was thin |
| Insurance repricing at renewal | Higher premiums cut net income, so property value and debt coverage fall | 1 to 3 years, at each renewal | A pre-existing Florida pressure (CORAL). Seacoast's 10-K names "significantly higher property and casualty insurance premiums" |
| Condo special assessments | A flood repair bill lands on top of post-Surfside reserve and inspection bills; owners pay or sell; the association borrows against its fees | Months to years | Pre-existing (CORAL). Association loans are secured by fee income; the bank-relevant risk is unit-owner mortgages and condo prices (HOMER and CORAL) |

**What past floods did to the most exposed banks (FDIC Call Report series, pulled 11/23):**

| Event | Banks (deposit share in hit counties) | Credit path, quarter before to six quarters after | Deposits |
|---|---|---|---|
| Ian, 9/28/2022 (Lee, Charlotte) | FineMark 65%, Sanibel Captiva 100%, Charlotte State 94%, Englewood 98%, Edison National 100% | Past dues up by at most 0.6pp for one quarter (Englewood 0.00 → 0.64 → 0.12%); nonaccruals 0 to 0.1%; net charge-offs 0.00% to 0.10% | Not separable from 2023 rate moves |
| **Ian in the St. Johns basin, 2022: the floods whose Lake Harney, Sanford and DeLand records this event is breaking** | Mainstreet Community, Surety, Intracoastal, United Southern, Mount Dora, Community Bank of the South, Sunrise | Past dues stayed under 2% and fell back. Nonaccruals were flat except Surety (0.91% → 1.44% at 12/31/2022, back to 0.48% a year later). Charge-offs about zero | Flat |
| Michael, 10/10/2018 (Bay, Gulf, Jackson, Calhoun) | Summit 85%, PeoplesSouth 67%, First National Bank Northwest Florida 100%, Peoples Bank of Graceville 100% | Nonaccruals flat or falling; charge-offs 0.00% to 0.13% | Rose: Summit +9%, PeoplesSouth +11%, FNB Northwest Florida +11% in Q4 2018 and +33% by 9/30/2019 |

⚠️ **Limits on the analog.** Ian and Michael were wind and storm-surge events with wind insurance paying out and federal aid flowing. This is a slow inland river flood, where insurance cover is thinner, and **no federal declaration exists for it.** OpenFEMA at 16:45 ET 11/23 lists only DR-4955 and EM-3655 (Hurricane Isaias), both in the Panhandle and Big Bend, none in my twelve counties. The analog covers 16 banks, with Call Report figures as filed.

**My standing reads:** BANK-ABSENT (HY cross-check, 11/20) and the Florida frame's NO TRANSMISSION FINAL (11/06). **Nothing here changes either.** The ranking shows where exposure would sit, with no loss, past-due, provision or deposit evidence attached. The market reads it the same way. From the 11/18 close to the 11/23 close (vendor bars, read 16:47 ET), the Florida names moved with the regional-bank index: AMTB −2.66%, SBCF −1.90%, VLY −1.84%, SSB −1.63%, BKU −1.42%, KRE −1.39%, USCB +0.25%, OPHC +0.36%.

## 3. Forward view (projection, not evidence; unscored and not registered)

- **Expected, about 80%:** at the Q4 releases (late January 2027) and the 12/31 Call Reports (filed by 1/30/2027), no listed bank in the table reports a flood-attributed rise in past dues, nonaccruals or charge-offs large enough to name. At most there is a qualitative weather line in the allowance discussion. Why: the Ian-basin and Michael histories above, clean Q3 credit at the Florida names, and collateral damage hitting owner equity before bank principal.
- **Meaningful alternative, about 20%:** Seacoast, or a southeast name if Tuesday and Wednesday's rain floods commercial districts in Miami-Dade, Broward or Palm Beach, names a storm reserve overlay or a payment-deferral programme in Q4. That would be a reserve signal, not yet a loss, and it would move Seacoast from an exposure map to an observation.
- **Tail, under 5%:** a basin community bank shows a past-due jump at the 12/31 Call Report. Mainstreet in DeLand is the one to watch: construction loans equal 97% of its capital. The first public sight would be February 2027.
- **Prints:** the FDIC Quarterly Banking Profile on Wed 11/25 **cannot show the flood**: it covers 9/30 and serves only as the pre-flood baseline. The watches on Tue 11/24 to Wed 11/25 decide whether the southeast names move from watch to flooded. A federal declaration window runs to about 12/07 (CORAL). Then come the Q4 releases (late January) and the 12/31 Call Reports in BankFind (about February).
- **What would change my mind:** (1) a federal major disaster declaration with Individual Assistance in basin or southeast counties; (2) CORAL or CREED naming flood-damaged commercial property with an identifiable bank lender; (3) any listed name announcing a disaster deferral programme or a flood provision; (4) past dues above 1% of loans at Seacoast or a basin bank at 12/31; (5) named association-deposit outflows at BKU or USCB.

## 4. What I need from the other desks (packets not sent; PROME's synthesis can route)

- **CORAL:** a county or ZIP damage map with homes, condos and commercial separated; NFIP take-up in the flooded basin; any named association with a flood repair assessment; whether the southeast watch flooded commercial cores.
- **CREED:** named CRE or CMBS collateral in the twelve counties that took water, with the current lender or servicer, and which of it is bank-held rather than CMBS.
- **HOMER:** listings, price cuts and failed sales in Brevard, Seminole and Volusia against the pre-flood baseline, with condos separate.

## 5. Inbox, WQ-735, other

- **Inbox drained, 5 items:** WALTER SIG-W-20261123-001 (Nvidia), -002 (HY 376), -003 (correction) INFO_ONLY or INTEGRATED; -017 (St. Johns gauges) INTEGRATED here. Logged in `board/BOARD_LOG.tsv` and moved to `processed/`. PROME WQ-735 actioned (below), moved to processed.
- **WQ-735 reply:** **I switched 2 scripts** to `research-bot/1.0`: `insider.py` (FDIC fdicconnect route parsed: cert 110, 471 disclosures, CLEAR; rc 1 is the standing insider-buy alert, 61 fetched, 0 failed) and `darkpool.py` (FINRA short volume parsed). `settled_bars.py` was not switched (Nasdaq did not pass). **One reading is now unavailable, and the name is not the cause:** chartexchange answers the honest name with 308 → `/exchange-volume/`, a page move, not a refusal (followed by curl: HTTP 200, no challenge). The parser finds no off-exchange figure, so off-exchange share reads NO DATA for all 6 tickers. Parser repair is deferred, and I did not switch back to the old name.
- **Not reached:** Q3 10-Q CRE ratios for the listed names; a re-read of USCB's 10-K association language at primary (relied on CORAL 11/06); Seacoast's 2022 Ian deferral disclosure; whole boot reads of CALENDAR and ROADMAP (grep-scoped for Florida items this session); boot.py, the VX ladder and the price-threshold run (only the FL tape and KRE were priced). Tomorrow's REG-T-04 grade is untouched.

## COMPLETION — REGINALD — 2026-11-23
STATUS: ⚠️ PARTIAL
CHANGED: PROME/inbox/2026-11-23_from-REGINALD_florida-flood-bank-exposure.md, AGENTS/TERRY/inbox/2026-11-23_from-REGINALD_florida-flood-bank-exposure.md, AGENTS/REGINALD/{STATUS.md,MEMORY.md,workbook/KB.tsv,board/BOARD_LOG.tsv,scripts/insider.py,scripts/darkpool.py,reports/2026-11-23_florida-flood-bank-exposure/*}, inbox items to processed/
RESULT: Ranked 13 listed and 10 unlisted banks by 6/30/2026 SOD deposits in 6 basin and 6 southeast counties. Seacoast is the only listed bank in the flooded basin (12.4%, $2.09B); USCB 100% SE at CRE 347% of capital, AMTB 98.4%, OPHC CRE 504%, BKU 68.2%. Ian (2022, same St. Johns records) and Michael (2018) left the most concentrated local banks' charge-offs at 0.00% to 0.13%, so BANK-ABSENT and NO TRANSMISSION stand; forward view about 80% no nameable Q4 flood credit effect.
GAPS: County CRE undisclosed at every bank (deposit map only); Q3 ratios not in BankFind; association loans unsized; damage map is CORAL's; CALENDAR and ROADMAP grep-scoped, not whole-read (battery-bounded session).
WILL_NEEDS: None.
FOLLOW-UP: CORAL damage map, CREED named collateral, HOMER values into PROME's synthesis; Q4 releases late Jan 2027 and 12/31 Call Reports ~Feb 2027 for the Seacoast and Mainstreet reads; chartexchange parser repair (page moved).
