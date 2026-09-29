# CRE case seed, notes (DRAFT, 2026-09-29)

Companion to `2026-09-29_cre-case-seed.tsv`. WALTER drafted this read-only from repo files, with no web access. It is a seed; CREED will own the real ledger.

**Conventions.** Cases are sorted by the date of their first distress event (not the loan origination date). Cases where that date is UNKNOWN come last (CASE-0051 to 0058). `vintage_year` holds both the build year and the loan year where the files give them. "Derived" means arithmetic on figures in the files; a desk derivation is labelled as the desk's. Nothing was averaged or picked when files disagree; both sides are in the row.

## 1. Counts (58 cases)

| Cut | Count |
|---|---|
| **City** | Chicago 9 (+ Lombard 1, Rosemont 1) · New York 5 · Seattle 4 · Houston 3 · LA County 7 (Los Angeles, West Hollywood, Hollywood, Santa Monica, Beverly Hills, Glendale, Bellflower) · Inland Empire 3 (Moreno Valley, Ontario, Chino) · Boston area 3 (Boston, Cambridge, Somerville) · SF Bay 3 (San Carlos, South San Francisco, Danville) · San Diego County 2 (San Diego, Escondido) · DC area 2 · one each in Coral Gables, Baltimore, St. Louis, Atlanta, Wauwatosa, Galveston, Dallas, New Hartford NY, Las Vegas, New Orleans, Fresno, Denver, Philadelphia, a Concord (city not stated) and one multi-city hotel loan |
| **Property type** (by the first word of the type cell) | Office 21 · UNKNOWN 14 · Retail 8 (4 malls) · Life science 6 · Land 3 · Hotel 3 (incl. the 22-hotel loan) · Multifamily 2 · Mixed-use 1 |
| **Trigger** | UNKNOWN 32 · MATURITY_DEFAULT 9 · OTHER 8 (mostly lease-up failure on new builds) · FRAUD_OR_LEGAL 5 (all Nano/Stupin-network) · OPERATING_SHORTFALL 2 · TENANT_EXIT 2 · RATE_RESET 1 |
| **Latest status** | DEFAULT 13 · SOLD 13 · SPECIAL_SERVICING 12 · REO 8 · UNKNOWN 6 · FORECLOSED 3 · WATCHLIST 1 · MODIFIED 1 · RECEIVERSHIP 1 |

## 2. Repeats (listed only, not interpreted)

| Repeat | Cases |
|---|---|
| **Lender Bank OZK** | 0002, 0006, 0009, 0018, 0019, 0020, 0021, 0022, 0025, 0026, 0027, 0028, 0029, 0030, 0031 (15) |
| **Lender Nano Banc** | 0010, 0012, 0013, 0016, 0017 (5) |
| **Preferred Bank (PFBC) senior ahead of Nano** | 0010, 0013, 0016 |
| **WAL pleaded collateral (Cantor/Stupin complaint)** | 0012, 0013, 0016, 0017 |
| **Sponsor Sterling Bay** | 0006, 0018, 0022, 0031 |
| **Borrower 601W Companies** | 0032, 0033 |
| **Blackstone, in three different roles** | 0001 (sponsor that handed back keys), 0032 (BXMT as lender), 0035 (equity sponsor and borrower) |
| **Beacon Capital (BCSP 8)** | 0004, 0007, 0021 |
| **Affinius Capital (formerly Square Mile)** | 0003 (borrower walking away), 0025 (sponsor JV member) |
| **Touchstone/Portman sponsor, Lionstone LP** | 0029, 0030 |
| **Special servicers** | K-Star 0014, Rialto 0023, Midland 0039. There are no repeats among the rowed cases. K-Star also serviced Starwood's unrowed $577M loan. |
| **Houston Galleria-area office, sole tenant left** | 0005 (Bechtel), 0023 (Enbridge) |
| **Built 1972-1982** | 0005, 0008, 0023, 0032, 0033, 0034 |
| **Loan vintage 2022** | 0021, 0026, 0029, 0030, 0035, 0058 |
| **New build, vacant since delivery (2023-25)** | 0018, 0021, 0026, 0029, 0030, 0058 |
| **Same Trepp August special-servicing batch** | 0041-0047 |
| **Same OZK Q2 foreclosure month (June 2026)** | 0029, 0030, 0031 |

## 3. Cases held only in desk files, with no BOARD signal carrying them

- **OZK desk** (some are also in REGINALD's 9/26 dossier `reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md`): 0002 8150 Sunset · 0003 Columbus Center (a **Florida** case, absent from CORAL) · 0004 Lafayette Centre · 0006 Lincoln Yards land · 0007 AMA Plaza · 0009 760 Aloha · 0018 1229 W Concord · 0019 Baltimore Peninsula · 0020 1650 Euclid · 0021 Portal 405 · 0022 Pacific Center · 0025 10 Prospect (BOARD mentions this credit only under the wrong label, see §5) · 0026 The Jack · 0027 Wauwatosa hotel · 0028 Sullivan Courthouse · 0031 1050 Brickworks · 0058 Spur Phase I.
- **CREED** (incl. its packets to CORAL and REGINALD): 0001 1740 Broadway · 0008 BofA Plaza LA · 0010 Blackhawk Plaza · 0015 BofA Plaza St. Louis · 0041 Project James · 0042 111 Livingston · 0043 60 Madison · 0044 BXHPP 2021-FILM · 0045 Regency New Orleans · 0046 Fresno Fashion Fair · 0047 Harlem USA · 0048 315 S Beverly · 0049 La Terraza · 0050 100 Summer St · 0051 Glendale Plaza · 0056 Republic Plaza · 0057 Four Penn Center.
- **REGINALD KB:** 0024 Concord Tech Center · 0053 401 S State · 0054 311 S Wacker. BOARD mentions 0055 175 W Jackson only as context.

## 4. Candidates seen but not rowed (why in brackets)

- Austin 526-unit apartment complex, $61.1M purchase (2024), ~$50.2M loan, $9.5M opening bid. SIG-W-20260626-024 (no name or address in any file)
- Orlando / "large Florida hotel portfolio" loan, delinquent May 2026 and cured June 2026. SIG-W-20260819-023, KB-CREED-025 (Trepp gives no name, CUSIP or address; **Florida**)
- Starwood Capital $577M / 65-hotel loan, early 2025, K-Star, modified 2025-09. SIG-W-20260507-004 (no property name)
- S2 Capital, 5 North Texas multifamily properties, $311M. SIG-W-20260704-005; HOMER `workbook/MULTIFAMILY.tsv` (a portfolio with no properties named)
- Pinnacle Group, ~93 NYC rent-stabilized buildings, Flagstar debt >$564M, sold for $451.3M on 2026-03-31. KB-FLG-067, FLG `reports/2026-09-27_WQ312_Q2_workout_rows.md` R7 (a borrower relationship, not a single property; press-grade)
- Yitzy Klor condo-deconversion default, $51M, 137 units in 7 Chicago towers, CoreVest / RWT trustee. SIG-W-20260828-048, KB-CREED-031 (a portfolio)
- KREF Boston life-science REO, ~$37M expected loss. SIG-W-20260511-025 (unnamed)
- STWD $347M foreclosure resolution. SIG-W-20260511-012 (unnamed)
- Chicago $167M CMBS office foreclosure. ML-REG-126, KB-WAL-068 (unnamed)
- San Carlos life-science loan, $63.6M, paid off in Q2 with a $14.8M charge-off. KB-OZK-231, KB-BRK-300 (unnamed; possibly 777 Industrial, but that is not stated)
- OZK Boston office exit, $9.36M (Q4-25). REGINALD q2_OZK.md (unnamed)
- July Trepp named-but-unaddressed loans: Chicago office tower, Seattle office portfolio, Times Square x2, NC/NV showroom. CREED `research/2026-08-13_NEWS_SWEEP_PLAN.md` l.23 (no names)
- Large Times Square loan cured in August. CREED `catchups/2026-09-02.md` (unnamed; a cure)
- One Riverway, Houston, loan renegotiation (2025 per the video). WALTER `registry/BATCH_MANIFEST.tsv` BM-20260929-09 item 6 (not verified)
- Laguna Beach building (Zions first lien, deeds assigned to Nano) and the Sand City "eco-resort" land ($37M Nano loan). CREED Nano research notes §2a (no address; loan performance unknown)
- Bioterra (San Diego, $203M, vacant; no primary source), IQHQ RaDD ($915M, 97% vacant, extended; pass-rated), Campus at Horton ("potential foreclosure"), Wilderness Labs Boulder ("default"). KB-OZK-030/057, 028/138/206, 140/141, 204 (no default event, or a one-word mention)
- Ameriprise building (97% severity), 4 Overlook Point (96%). ML-REG-053 (no city, loan or date)
- Kodak plant Rochester ($0.45/SF), Progressive HQ Ohio ($10.53/SF). ML-REG-068 (auction marks with no loan)
- 100 Pratt Street E (-$138.9M) and 1 Light Street (-$87.3M), Baltimore. SIG-W-20260426-009 (tax-assessment cuts, not loan events)
- Washington 1000 / 1000 Olive Way, Seattle, vacant since 2024. SIG-W-20260727-028 (no loan event)
- 55 Broad Street. SIG-W-20260420-008 (a $500M RXR recap; the files show no distress event)
- Legacy archive `REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009` (dated 2026-01-27, which CREED deliberately did not import): Gas Company Tower + 777 S Figueroa (LA, ~$784M, receiver); One Pierrepont Plaza (Brooklyn, $148M, special servicing); Pembroke Lakes Mall (**Broward FL**, $260M, maturity default, value $159M); NY Times Building floors 29-51 ($515M, special servicing Nov 2025); One New York Plaza ($835M, special servicing Dec 2025); Hughes Center (Las Vegas, $325M, special servicing); Pinnacle II (Burbank, $87M, Warner Bros vacated); Wells Fargo Center / 333 S Grand (LA, note listed); plus unnamed DC and Bethesda portfolios
- Excluded as not distress: Fort Lauderdale W Hotel $115M refi (SIG-W-20260626-013, counter-evidence); 110 Tower, Fort Lauderdale, sold 2026-09-24 at -21% as a performing sale; the Fort Lauderdale "75% vacant" new building (SIG-W-20260929-013, unnamed anecdote)

## 5. Contradictions between files

1. **"Cambridge Courthouse" label (a WALTER error, it seems).** SIG-W-20260704-004 calls OZK's $169M Boston life-science credit "Cambridge Courthouse". The OZK desk says that credit is 10 Prospect St, Somerville (KB-OZK-195/235). Sullivan Courthouse, Cambridge is a **separate** $156.4M office credit that was recapitalized in Q2 (KB-OZK-231). Earlier, KB-OZK-189 had named 808 Windsor / Boynton Yards and a 12/18/25 maturity. Both are corrected: 12/18/25 is the Baltimore land loan's maturity.
2. **3000 Post Oak.** 2014 price $170M (Trepp) vs $175M (X/Nightingale). Trust loss "$64.8M" (CREED vulnerability map, secondary, source not found) vs $80M - $11.4M = $68.6M gross. Trepp says title passed on the 2024 default; the video (SIG -015) describes an "April handback" with no year given.
3. **Baltimore Peninsula land.** KB-OZK-119 says deed-in-lieu in Dec 2025 and that OZK owns 235 acres. The Q2-26 management comments (via REGINALD's dossier) show a $40.0M nonaccrual loan still in buyer talks ("otherwise take title").
4. **Lincoln Yards land.** KB-OZK-208 has a $38M writedown on $128M (~30%), a deed-in-lieu in Mar 2025 and a later contract to JDL. REGINALD's dossier has an unnamed "Chicago land (Q3-25) sold at carrying $83.95M, -34% vs ~$128M". KB-OZK-126 says "sold at book". Whether these are the same asset is not stated.
5. **The Jack's originator.** KB-OZK-193 says Mack Real Estate Credit Strategies ($90M, Feb 2022). KB-OZK-207 says Claros Mortgage Trust originated it, then assigned it to OZK.
6. **Chapter Buildings.** SIG -704-004 says a ground-lease assignment-in-lieu was recorded the week ending 7/2/26. The OZK management comments say "foreclosed June 2026". Building II is ~154K SF (SIG) or 149K SF (dossier). The $196.2M figure (SIG) is the 2022 total: $106.9M + $89.3M commitments. KB-OZK-114 lists "Chapter Building: $106.9M" as if it were a single figure.
7. **Pacific Center.** Sale date is 2026-01-05 (KB-OZK-031/153) or 2026-01-07 (KB-OZK-199, TRD). Size is 500K SF or a 690K SF Phase 1. It was first read as a loss realization, then corrected to a par exit on the $0.10B funded balance.
8. **1229 W Concord.** A "$125M construction loan ($65M per TRD)" is commitment vs outstanding. Size is 284K-320K SF. Carrying is $50M (Q1) vs $47.5M (6/30, after a $2.5M write-down).
9. **Wauwatosa hotel.** The same March 2026 appraisal gives LTV 96% (Q2 management comments via dossier) vs 103% (archived REGINALD STATUS).
10. **175 W Jackson.** Sold for $41M, an 87% markdown from $306M (SIG -624-004), vs "~70-80% discounts" (ML-REG-074).
11. **Chino lien.** 12233 Central Ave (WAL complaint) vs 12125 Central Ave (debtor filing). The 65.91% TIC match is unverified.
12. **Alessandro Plaza size.** ~119K SF (Registry headline) vs 84K SF (a Registry sale listing, probably a different perimeter).
13. **Aon Center.** The BOARD signal says the extension outcome is uncertain. CREED THESIS/FLOW (7/27) say "Aon + Seattle recaps FAILED" and cite no Aon source.
14. **Galveston price.** A circulating $1,475,000 / $3.79/SF was rejected. The 7/2 re-verify confirms ~$3.3M hammer / ~$3.475M all-in.
15. **Two different "Bank of America Plaza" buildings.** One is downtown LA (CASE-0008: $400M, 44% loss, sold 6/16/26); the other is St. Louis (CASE-0015: ~$9.5M+ sale, June 2026). Do not merge them.
16. **S2 Capital (unrowed).** $311M across 5 North Texas properties (SIG -704-005) vs HOMER's row: 20 DFW/Phoenix properties, $140M of DFW foreclosures on 6/22, $250M of CMBS to special servicing on 5/28, and ~1/3 of ~$900M of Texas CRE flagged for July auctions.
