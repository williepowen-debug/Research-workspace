# LIQUID after-close read, 2026-10-22 (PROME prome-e7 spawn, WQ-481 A)

Written 2026-10-22 from ~19:36 ET. Observation dates in brackets; retrieval times noted where they matter. No threshold, trade or sizing change.

## 1. Credit, FRED ICE BofA OAS, FIRST-PUBLISHED (bp = percent x 100)

Two methods, same answer: `fetch.py fred <ID> --first-published` (realtime window) and a direct FRED API call with `output_type=4` (initial release only), both run 2026-10-22 ~19:28 ET. Latest-revised (`boot.py`) equals first-published on every date below.

| Obs | HY | IG | BBB | BB | B | CCC |
|---|---|---|---|---|---|---|
| 10/13 | 316 | 83 | 103 | 191 | 317 | 1,267 |
| 10/14 | 325 | 84 | 104 | 199 | 329 | 1,282 |
| 10/15 | 323 | 84 | 105 | 197 | 326 | 1,278 |
| 10/16 | 331 | 85 | 106 | 203 | 335 | 1,297 |
| 10/19 | 329 | 87 | 108 | 200 | 336 | 1,310 |
| 10/20 | 333 | 87 | 108 | 202 | 338 | 1,327 |
| 10/21 | 327 | 88 | 109 | 198 | 332 | 1,307 |

The 10/22 observation is not yet published (FRED ICE posts T+1). Derived [10/21]: HY-IG basis 239; CCC-BB 1,109; CCC-B 975.

**HY >320 sustained (WQ-444: three consecutive eligible published observations strictly >320.0, non-latching):** **6 consecutive first-published observations >320.0, 10/14 through 10/21 (325 / 323 / 331 / 329 / 333 / 327), VERIFIED.** Last reset 316 [10/13]. 10/19 upgrades from INFERRED to VERIFIED (329); 10/20 is 333 on my basis (the 332 relay was off by 1). State MET (sustained), unchanged. The HY >320 send was already routed 10/19; no new send.

## 2. Funding tape

| Item | Reading | Basis / source |
|---|---|---|
| SOFR | 3.88% [10/21]; 3.88% [10/20]; 3.87% [10/19] | NY Fed reference-rate API, primary. 10/22 SOFR publishes 10/23 ~08:00 ET |
| SOFR - IORB | -2bp [10/21] (IORB 3.90%, FRED IORB, unchanged through 10/23) | date-matched |
| SOFR 75th / 99th - IORB | +3 / +6bp [10/21]; +3 / +6bp [10/20]; +2 / +5bp [10/19] | NY Fed percentiles (revisable) |
| SOFR volume | $2,942B [10/21] | NY Fed |
| EFFR | 3.88% [10/21], 99th 3.94%, $110B | NY Fed |
| SRF (standing repo, all legs) | $0.001B [10/22, 13:30 op, Treasury leg, at 4.00%] · $0 [10/22 08:15 op] · $0 [10/21 both ops] | NY Fed repo operation results, primary |
| SRF correction | The $0.067B on 10/20 that STATUS carried as SRF usage was a **Small Value Exercise** (2-day term operation, $100M limit, operational test), not demand. NY Fed operation note, read 10/22. Self-correction; it never fed a grade (SRF line is >$50B) |
| RRP | $0.351B [10/22]; $0.237B [10/21] | NY Fed |
| Reserves (H.4.1, released 10/22) | **$2,962.607B week average, week ended Wed 10/21 (-$59.533B); $2,969.522B Wednesday level** | federalreserve.gov H.4.1 primary. $162.6B above the $2.8T line (average) |
| TGA (H.4.1) | $952.002B week average (+$68.629B); $945.153B Wednesday | the TGA build accounts for most of the reserve drop |
| Primary credit (H.4.1) | **$9.169B Wednesday 10/21** (from $11.044B 10/14); week average $8.935B (-$2.377B) | primary; no registered LIQUID line; REGINALD's ~$12.9B "notable" line is descriptive, not a gate |
| Repo (H.4.1, "Others") | $67M Wednesday, the SVE term repo | primary |

**Treasury auction 10/22, 5Y TIPS, CUSIP 91282CRR4, $26B (TreasuryDirect TA_WS, updated 14:49 ET):** high yield 2.367%; bid-to-cover 2.41x; competitive accepted $25,676.7M: indirect 62.04% / direct 32.44% / primary dealers 5.53%; 68.33% allotted at the high. No failure on my letter (BTC >= 2.0). Indirect above 55%. Tail UNGRADED: no when-issued source reachable.

**Not reachable tonight:** ICI money-fund assets for the week ended 10/21 (ici.org returned Access Denied); 10/22 SOFR (publishes 10/23).

## 3. Dealer positioning, NY Fed Primary Dealer Statistics (SBN2024, $ millions, as-of Wednesday)

| as-of | IG corp >10y (G10) | IG corp 5-10y (G5L10) | below-IG >10y | below-IG 5-10y |
|---|---|---|---|---|
| 9/16 | -9,286 | +564 | +666 | -1,282 |
| 9/23 | -8,189 | +1,176 | +747 | -916 |
| 9/30 | -9,570 | +847 | +1,330 | -298 |
| 10/7 | -10,665 | **-1,462** | +626 | -1,466 |
| 10/14 | -10,307 | **-1,717** | +627 | -2,186 |

The as-of 10/14 print published 10/22 and is read here as first published (API pull 2026-10-22T23:29Z). The as-of 10/7 value matches my 10/19 read (-1,462), so no revision is visible.

**GATE-LIQ-076 W2 MET:** G5L10 below -800 on two consecutive weekly as-of dates (10/7, 10/14), strict. This is the first W2 fire since registration (7/11). Dealers moved from net long +$847M to net short $1,717M in IG 5-10y in two weeks. Net position is a stock, not gross selling or a refusal to bid.

## 4. AI-credit evidence

**CoreWeave bonds, HYG fund-evaluated vendor prices, holdings file "as of Oct 21, 2026"** (receipt `hyg-coreweave-receipt.json`):

| Bond | Price | YTW | Prior fund evaluations |
|---|---|---|---|
| 9.25% June 1, 2030 | 85.76 | 14.44% | 85.76 / 14.41% [10/14]; 84.49 / 14.93% [10/16] |
| 9.00% Feb 1, 2031 | 81.75 | 14.91% | 81.70 [10/14]; 79.84 [10/16] |
| 9.75% Oct 1, 2031 | 81.74 | 15.12% | 80.50 [10/16] |
| 9.625% July 15, 2032 | 80.04 | 14.91% | 77.03 [10/14]; 79.21 [10/16] |

Limits: vendor evaluations, not TRACE trades; the file itself says the vendor price may not be as of the date shown; the 2030 line shows exactly 85.76 on both the 10/14 and 10/21 files, which may be a stale vendor price. The holdings file has no CUSIP column. CUSIP for the 2030 notes: NOT ESTABLISHED on a primary from this box. A broker factsheet (fundsupermart, secondary) lists ISIN USU2069EAA83, which by its U-prefix is the Reg S line, not the 144A line.

**CDS, DTCC Public Price Dissemination (SEC-regime cumulative credit files, free), `dtcc_cds_probe.py` / `crwv_cds_grade.py`.** Disseminated spreads are as printed; upfront conversions are flat-hazard approximations (r 4%, R 40%), not ISDA.

| Name, standard 5Y (Dec 2031) | 10/19 | 10/20 | 10/21 |
|---|---|---|---|
| Oracle (100bp coupon) | — | disseminated 342bp [13:36Z]; upfront 8.45-9.98pt -> ~305-346bp | disseminated 320bp [16:36Z], 315bp [18:02Z]; upfront 8.50-8.87pt -> ~306-316bp |
| Meta (100bp coupon) | disseminated 105bp [15:51Z]; upfront -> ~101-110bp | disseminated 111bp [18:01Z]; upfront -> ~110-114bp | upfront 0.25-0.49pt -> ~105-111bp (one 2,000,000 print at 1.73pt / ~139bp is an outlier) |
| CoreWeave (500bp coupon) | 16.22pt [20:29Z] -> ~1,010 / 1,025bp | 18.08pt [16:42Z, capped] -> ~1,083 / 1,100bp | no standard 5Y print |

Meta upfronts are below 1.5pt, so their SIGN is not knowable from the unsigned field; the disseminated spreads (105, 111) carry the read. Oracle upfronts are 8-10pt, sign not in doubt.

**Meta vendor levels reconciled as far as the tape allows:** DTCC prints put Meta 5Y at 105-114bp on 10/19-10/21. Markit's "record 114.5bp, +7.3bp" (Reuters) fits the top of that range on 10/20-10/21. ICE's "as much as 8.9bp to ~119.3bp" (Bloomberg, 10/22) is an intraday 10/22 high. These are two vendors at two moments, close versus intraday; they do not establish a disagreement. The 10/22 DTCC file publishes ~20:15 ET and was not yet available when this table was built.

**Oracle rating ladder (GATE-LIQ-069 L5):** S&P BBB- [7/9 cut] stands; Moody's Baa2 negative and Fitch BBB stable per secondary search 10/22; no October action found. R1 NOT FIRED; no index-ejection event. Agency-primary re-verification still NO_INSTRUMENT.

**Data-centre CMBS/ABS AAA spread:** no dated clearing level reachable (Trepp, Intex and Bloomberg are paid). Best dated anchors, all via DEWEY's v2 report: Lambda-tenant (Pevco) $301M SASB AAA guided S+225 [~9/22, GlobalCapital headline] and NOT SOLD as of 10/21 (Bloomberg via ASR); generic CREFC floating-SASB AAA S+175 [10/16], 3-month average S+159; Barclays AAA DC floating SASB ~165bp [~9/14].

**Cohort equity, raw vendor closes [10/22]:** CRWV $55.60 (-10.06%), IREN $25.51 (-8.37%), APLD $19.09 (-9.01%), NBIS $159.17 (-7.23%); ORCL $125.54 (-2.78%), META $648.85 (-6.98%). No cohort name at or below -15%.
