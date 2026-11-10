# 11/10 due rows — DOCKET L575 · L572 · L554 (NEXUS record)

Owner NEXUS. Launched by PROME prome-07 on the desktop after the 11/10 machine switch (Will's task). Claude Code, Opus 5.5. Limits: $0 moved; no threshold, gate letter, band or card changed without Will; live prices only; quiet mode. Session start 2026-11-10T11:09 ET (`date`).

## 1. DOCKET L575 — PRED-41, NY Fed Household Debt and Credit Q3-26

| Item | Value |
|---|---|
| Source | `https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2026Q3.xlsx`, fetched 2026-11-10 11:09 ET, 968,678 B, sha256 f6370608a1e0dcf5e2781afc812fa789ac4d55cae6036361bbf42d41976b72a3 |
| Instrument | sheet "Page 14 Data", "New Seriously Delinquent* Balances by Loan Type", Percent, *90 or more days delinquent, column CC (as the letter specifies) |
| Path in this vintage | 25:Q4 7.13 · 26:Q1 7.10 · 26:Q2 **6.97** (unrevised) · **26:Q3 6.87** |
| Letter edges | ≥ 7.47 HIT · ≤ 6.47 MISS · strictly between ⇒ no crossing on this print |
| Result | **6.87 is inside (6.47, 7.47): no crossing. PRED-41 stays OPEN; the Q4-26 print (expected early February 2027, date unverified) decides.** If Q4 also prints inside, ⚪ NO-VERDICT, closes, non-renewable. If Q4 is never published by 2027-02-28, Q3 is graded alone ⇒ ⚪. |
| Direction | −10 bp q/q, away from HIT (7.47 is 60 bp above); 53 bp above MISS. One print (Disc-B): not load-bearing beyond this letter. Mass-market card stress is NOT breaking on this instrument. |
| Conf | HIT ~20 · ⚪ ~70 · MISS ~10 **held** (no registered rule moves it on an inside print). |
| Wake owed | Q4-26 wake row: PROME registers it (15b), anchor type = expected release, re-dated at the NY Fed announcement. |

## 2. DOCKET L572 — PRED-38, Q3-26 bank net charge-offs on non-bank-finance borrowers

**Grade: ❌ MISS, k = 0.** Letter: one US bank's own Q3-26 release, 8-K or 10-Q attributing ≥ $100.0M of Q3 net charge-offs to non-depository financial borrowers counts; k ≥ 2 HIT · k = 1 ⚪ · k = 0 MISS. Conf was HIT ~35 · ⚪ ~35 · MISS ~30; the outcome the desk gave 30% occurred.

| Coverage layer | Result |
|---|---|
| 10/31 sweep (`research/2026-10-31_owed/PRED38_SWEEP.md`) | k = 0 across 27 banks (BAC, WFC, TFC, HBAN, CFG, … read in full text) |
| 11/9 sweep (`research/2026-11-09_due-rows/PRED38_SWEEP.md`) | k = 0 across 19 more 10-Qs; GS $154M wholesale NCO "substantially all related to other collateralized and corporate loans" — collateral class, unsplit, no NBFI borrower named ⇒ does not count |
| **JPM gap closed today, NEXUS direct read** | 10-Q 0001628280-26-069523 (EDGAR HTML, 11,540,732 B, read locally). "Wholesale credit exposure – industries", nine months to 9/30/26, net charge-offs: Asset Managers **—** · Banks & Finance Companies **8** · Insurance **20** · Securities Firms **—** · Financial Markets Infrastructure **—** · Individuals and Individual Entities 13 · All other 80 · subtotal **561**. Q3 by class: secured by real estate 36 · C&I 196 · **Other —** · total 232. The financial-sector rows total at most $28M over nine months ⇒ **N** |
| Late filers 11/9–11/10 | EDGAR full-text search "net charge-offs", 10-Q, 11/9–11/10: 30 filers, all small banks or consumer lenders. Prosperity (PB) 10-Q text: Q3 NCO **$4.4M**. FNB 9M gross write-offs $56.1M (XBRL) ⇒ Q3 < $100M. Beacon Q3 gross $14.7M. FirstSun $3.6M, INDB $1.7M |
| Universe screen | XBRL frames, CY2026Q3, three write-off tags (gross and after-recovery), every filer ≥ $100M: banks = ALLY, CFG, FCNCA, FITB, HBAN, KEY, MTB, PNC, GS, USB, BAC (filed as "BofA Finance LLC" CIK 70858) — every one read in a sweep, all N; the rest are consumer/card lenders, GSE or insurer (Affirm, Bread, CarMax, Ford Credit, OneMain, Synchrony, Fannie Mae, Prudential). Banks tagging other concepts (JPM, C, WFC, TFC, MS, COF, SCHW) were read directly |

⚠️ Residual scope: non-accelerated filers' 10-Qs are due through ~11/16; a bank that small cannot plausibly hold ≥ $100M of quarterly NBFI net charge-offs, but this is a size argument, not a read. 11/9 helper R-page figures came through a summarizing fetch tool and are not byte-verified; each sits under $100M with its XBRL total. Disc-A: the threshold missed and the mechanism (realized bank losses on NBFI borrowers in Q3 reporting) is absent in the banks' own words — MISS in letter and in spirit. It says nothing about Q4 or about provisions (GS $368M wholesale provision is a provision, not an NCO).

## 3. DOCKET L554 — weekly wake

### 3a. Owed: successor or withdrawal for M-01, M-05, M-04 (Disc-J)

Live and latest-published readings used (fetched 2026-11-10 11:13 ET): FRED HY OAS 3.43 3.40 3.32 3.48 3.42 **3.34 [11/9]** · IG 0.94 0.93 0.91 0.93 0.93 **0.91 [11/9]** · VIXCLS 21.15 20.83 16.61 28.18 25.64 **19.92 [11/9]** · ICSA 189K [w/e 10/31] latest · KRE **$72.50, −1.29% [11/10 11:13 ET, live, vendor via FORGE fetch.py]** · ^VIX **20.82, +4.52% [11/10 11:13 ET, live intraday]**.

| Row | Closed state | Decision | Why |
|---|---|---|---|
| M-01 substance/tape divergence | CLOSED NEITHER 11/5; 60 held EARNED once | **WITHDRAWN → judgment, no number (60 historical)** | A successor would re-read the same ICE HY family that L16 (fired 11/3), M-07 and M-08b already carry — count-once rule (L17) means it adds no independent information. HY has retreated to 334 [11/9] from 348 [11/5]; claims 189K. A successor needs new thresholds, which this task bars without Will. |
| M-05 named-regional/CRE | CLOSED NEITHER 11/5; 48 held EARNED once | **WITHDRAWN → judgment, no number (48 historical)** | KRE $72.50 live sits inside the old 64.02–75.16 band; a re-anchored KRE window is a new threshold (Will's word). PRED-38 MISS today (k = 0) and WAL MI3 below its rail are disconfirming case evidence, not a falsifier. FLG 10-Q (11/6) remains owner-read. |
| M-04 vol/gamma crack | M-04b UP HIT 11/6; 30→34 graded, window CLOSED | **WITHDRAWN → judgment, no number (34 historical)** | The fire was a two-cell spike: VIXCLS back to 19.92 [11/9], below the 22.45 edge; live 20.82. A successor VIX window is a new threshold (Will's word). One repricing class with R4. |

Effect: the matrix now carries numbers only on **M-08 83%** (M-08b, resolves 11/20) and **M-11 51%** (PRED-45 transfer letter, resolves 11/20). Every other row is judgment, no number. The **split 26/41/33** remains "currently un-falsifiable" since L13 exhausted 11/9 (no registered letter can move it); a successor falsifier or a third DFII10 window needs Will's word — packeted to PROME as an ASK, not decided here.

### 3b. Digest intake (BOOT 6) — delta pass, not a full matrix re-sweep

30 briefs (HAWK excluded, no cross-war question) via three fresh-context Opus read-only readers, 10 each; reports in `digest/` here. Pins 27 PASS; UNPINNED SHADE, HOMER, BRENT. NEXUS read the load-bearing owner artifacts directly (FRED cells, NY Fed workbook, JPM and PB 10-Qs, BROCK's 11:13 ET STATUS commit). No matrix cell takes a reader's figure without an owner or primary check; the 11/9 HY 334 that one reader flagged as unverified was confirmed at FRED.

Cross-desk threads no brief joins (logged under WQ-622, not scored; nothing moves a number):

| Thread | Desks and figures |
|---|---|
| Bank lending into private credit / fund finance growing | FLG private-credit loans $1,069M → $2,139M [9/30]; WAL unused commitments +20.8%, mostly PE-fund capacity; Athene SVF II Finco NAV loan $3,097M (+$1,033M Q3, SHADE) |
| IREN GPU financing ↔ Microsoft reassessment | BROCK: IREN GPU Financing 2.0 (IE Mackenzie Compute) held in Blue Owl vehicles (OCIC 370, OTF 180, OBDC 160, OTIC 20 $M commitments; $282.3M funded, $447.7M undrawn to 12/31). Per BROCK's read of the loan agreement (KB-BRK-474, IREN 10-Q Ex 10.1), the collateral **expressly excludes** any Customer Agreement and its receivables, so a Microsoft cut or termination is not a default, acceleration or collateral event on this loan. It reaches the funds only through IREN's own credit (unsecured parent payment guaranty), or by blocking new draws if an acceleration of $250M or more hits a Significant Non-Recourse Subsidiary; whether Hardware 3 (the Microsoft supplier entity) is Significant is UNKNOWN. LIQUID and RED: Microsoft reported reassessing cloud deals (one Bloomberg chain, relay) |
| Private-credit refusal to roll | LIQUID: Hertz rental-car ABS Class B extension refused by Oaktree funds, refinanced 12.46% vs 9.28%; not in BROCK |
| Las Vegas / Nevada / Arizona | MARCO RevPAR −9.02%, NV-01 and AZ-01 CRITICAL; HOMER Las Vegas FMHPI −2.51%; WAL hotel franchise criticized $75M → $185M, Nevada $2.0B commercial |
| One unnamed cross-asset day 11/5 | VULCAN SPY −4.41%, MIDAS S&P −4.36%, ORACLE Fed odds −14 to −17 pts; cause not established anywhere |
| Diesel diversion unrouted | OSPREY 11/9: two of three US-bound diesel cargoes diverted; BRENT's distillate rail does not mention it |

Disc-D counter-signal: the tape retook 59% of the 11/5 fall (HENRY), HY 348 → 334, VIX back under 20, while FLG coverage (30.85%, series low) and HOMER's foreclosure pipeline (882K) worsen. Effective N unchanged: 1 established root (R1) plus R3 and AI Root B candidates; no three-root convergence, no alert.

Unread owner items owed elsewhere: CPI October and HHDC not graded by any desk at read time; CoreWeave and SoftBank 11/10 results not graded (VULCAN, SAM); ZHAO clocks re-suspended 11/9 (ZHA-19/20 lookups 11/10–11/11).

### 3c. Controls

Rotation: STATUS 71% band → §H28 (crc32 f7ff3b2e), §H29 (13805039), §H30 (fce5fbbb), each verified against the committed original; final 22,441 B (69%). PREDICTIONS PRED-38 row → COLD §P9 (crc32 1aaedba2). 0b carried: no letter text changed or registered; PRED-41's n = 1 and Q4 branches re-checked against today's print. 9b residue grep: STATUS rows R3, CARL→REGINALD, FIRED fixed; PREDICTIONS lines 3 and 5 are dated pass headers (RETAINED-HISTORY); CONFIRMED 11/9 line is a fired-leg record, still true.

### 3d. Closing freshness (9c), immediately before commit

Moved during the session: BROCK 11:13 (CRMT eleventh bridge to 11/12 — absorbed in T-15), CARL 11:17 (HHDC Q3 graded: CRL-33 MISSED; flow into 90+ 6.87% Q3, same figure NEXUS read — owner agreement; card 90+ stock 12.90% vs 12.92%), HENRY 11:15 (HEN-57 NOT FIRED; October core CPI +0.3, headline +0.4), VIOLET 11:15 (PRED-07 confirmed on 11/9 history), ZHAO 11:15 (ZHA-19 and ZHA-20 YES at primaries). Board delta-annotated (BROCK, and a header line for CARL/HENRY/ZHAO), not re-swept; CPI is the next boot's read.
