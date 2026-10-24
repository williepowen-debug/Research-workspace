# LIQUID — 2026-10-23 evening grade (owed 10/23 row)

**Session:** Fri 2026-10-23 21:59 ET boot (Will, "catch up on owed work"), Claude Code / Opus 5.5. No `git pull` needed (0 incoming commits; dirty tree = NEXUS only). All reads below taken 22:00–22:15 ET 10/23.

## 1. Credit — FRED ICE BofA OAS, FIRST-PUBLISHED (`fetch.py fred <id> --first-published`), 10/22 observation, bp

| Series | 10/16 | 10/19 | 10/20 | 10/21 | **10/22** | d/d |
|---|---:|---:|---:|---:|---:|---:|
| IG (BAMLC0A0CM) | 85 | 87 | 87 | 88 | **89** | +1 |
| BB (BAMLH0A1HYBB) | 203 | 200 | 202 | 198 | **210** | +12 |
| B (BAMLH0A2HYB) | 335 | 336 | 338 | 332 | **346** | +14 |
| CCC (BAMLH0A3HYC) | 1,297 | 1,310 | 1,327 | 1,307 | **1,340** | +33 |
| HY (BAMLH0A0HYM2) | 331 | 329 | 333 | 327 | **340** | +13 |

Derived [10/22]: HY−IG 251 · CCC−BB 1,130 · CCC−B 994. BBB not pulled this session.

- **WQ-444 >320 sustained run:** 7 consecutive strictly >320.0 (10/14–10/22). Last reset 316 [10/13]. MET (sustained), unchanged state; no new route (routed 10/19).
- **REG-T-04 (REGINALD's, >350 ×3):** 340 is 10bp under; run 0 of 3. Earliest fire = observations 10/23 · 10/26 · 10/27 all >350, the last of which publishes ~10/28 (T+1).
- **GATE-HY-REKILL:** NOT FIRED 0 of 2 (80bp above 260).
- **069 L1:** BB 210 ≤ 220 strict-greater line → NOT MET (10bp under).
- **072:** IG 89 not > 94; basis 251 not < 180 → QUIET.

## 2. Funding — NY Fed markets API (primary), read 10/23 ~22:05 ET; IORB 3.90%

| Date | SOFR | 1st | 25th | 75th | 99th | Vol $B | SOFR99−IORB |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10/21 | 3.88 | 3.83 | 3.86 | 3.93 | 3.96 | 2,942 | +6 |
| **10/22** | **3.90** | 3.83 | 3.88 | 3.95 | 3.98 | **2,945** | **+8** |

EFFR 3.88% [10/22]. SRF (repo operation results, all legs): $0.001B [10/22], **$0 [10/23]** (both overnight ops). RRP $0.351B [10/22] → **$0.200B [10/23]**. **079 NOT ARMED** (+8 vs ≥+30).

## 3. Dealer positioning — CFTC TFF futures-only raw `FinFutWk.txt`, Last-Modified 2026-10-23 19:28:16Z (= as first published)

`SOFR-3M - CHICAGO MERCANTILE EXCHANGE`, as-of **Tue 10/20**: Lev long 1,111,517 − short 3,484,557 = **net −2,373,040**; w/w **−127,533** (a BUILD; prior −2,245,507 [10/13]). OI 12,982,053; Lev spreading 2,668,797. **W1 NOT MET:** 576,960 short of ≤ −2,950,000; the w/w is the wrong sign for the > +300,000 cover leg. Columns: index 14/15/16 = Lev long/short/spread (same mapping as the 10/9 grade). **076 = MET 2 of 3 unchanged (W2 + W3), same un-re-armed episode; no write-up owed.**

## 4. H.8 — release 2026-10-23, federalreserve.gov `releases/h8/20261023/` (primary), SA, $B, week ending Wed 10/14

| | Small domestic (Table 8) 10/7 → **10/14** | Large domestic (Table 6) 10/7 → **10/14** |
|---|---|---|
| Borrowings | 307.3 → **316.4** (+9.1, +2.96%) | 1,062.4 → **1,066.8** (+4.4) |
| Deposits | 5,688.4 → **5,695.4** (+7.0) | 12,441.0 → **12,466.2** (+25.2) |
| Cash assets | 482.1 → **494.2** (+12.1) | 1,397.2 → **1,384.8** (−12.4) |

Small-bank borrowing now 316.4 vs 314.8 [9/30] (10/7 revised 307.4 → 307.3, 9/30 314.9 → 314.8). Deposits and cash rose with it, so this is not a deposit-replacement signature on one week. No LIQUID threshold.

⚠️ **Instrument trap (new):** `https://www.federalreserve.gov/releases/h8/current/h8.htm` served a **September 25, 2015** release at HTTP 200 (796,000 B, cache-busting query did not change it). `releases/h8/current/default.htm` and the dated `releases/h8/20261023/` both served 10/23/2026. Read H.8 from the dated path. (Same class as KB-LIQ-139/141/142 access traps; a 200 is not a current page.)

## 5. AI-infra CDS — DTCC SEC cumulative credits (`scripts/dtcc_cds_probe.py`), 10/23 file; flat-hazard approximation, not ISDA

| Name | 5Y (Dec-2031) 10/23 | Note |
|---|---|---|
| **NVIDIA** | **disseminated 128bp [18:00Z]**; upfronts ≈ 125–130bp (12 NEWT prints) | **WALTER 027's "over 120" CONFIRMED at the DTCC tape**; ~1.5× the ~82bp July record (press); VULCAN had 117 [10/22] |
| META | disseminated 121 / 127bp; upfronts ≈ 120–130bp | 10Y (Jun-2036) ≈ 163bp |
| ORACLE | upfronts ≈ 308–321bp | consistent with PROME ELLISON packet's 314 [10/22]; no conflict |
| COREWEAVE | 18.79–19.29pt ≈ 1,133–1,155bp (cpn 500) | 069 L2 stays FIRED |

No LIQUID gate moves: NVDA/META are AA-area issuers widening, not IG names at BB-like spreads (072 leg 1/4 unchanged).

## 6. 069 L4 — raw closes 10/23 (yfinance `auto_adjust=False`)

CRWV 54.24 (−2.46%) · APLD 18.25 (−4.40%) · IREN 24.91 (−2.37%) · NBIS 158.74 (−0.27%). No name ≤ −15% → **L4 NOT FIRED 10/23**. ORCL 126.16 (+0.49%). HYG 77.05 / JNK 92.52.

## 7. Not done this session

- Rated-CCC (XCCC) composition **refresh**: `bondbloxxetf.com` returned HTTP 403 from this box (10/23 ~22:10 ET, curl). STATUS line seeded from DEWEY's 10/22 holdings parse; refresh owed (WQ-516 A, DOCKET L829 checks 10/30).
- 10/23 observation of everything FRED/NY Fed publishes Monday 10/26.
