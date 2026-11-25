# Digest reader B: REGINALD, BROCK, FLG, CARL, LABOR, ISHM

**Written:** 2026-11-25 16:10 EST · read at HEAD b346e54387 · baseline dc3ec2b130 (2026-11-25 00:37 ET) · model Opus 5.5 · all six briefs read whole, all six STATUS diffs read since baseline; post-brief packets and PROME memos read to test staleness.
**Method limit:** figures below are copied from the desks' files and no primary source was opened. "Brief" = NEXUS_BRIEF.md. "Post-brief" = arrived in the desk's inbox or ledger after its brief was committed.

## Pin check

`python3 scripts/brief_pin_check.py` (repo root): `BRIEF-PIN 0 OK: 31 brief(s) checked ... OK-PINNED 21 · OK-SAME-COMMIT 8 · STALE-PIN 1 · UNPINNED 1.` The STALE-PIN is LIQUID and the UNPINNED is RED, neither in this set.

| Desk | Result | Brief commit | STATUS commit |
|---|---|---|---|
| REGINALD | OK-PINNED 25fca1c9fa | 11/25 09:16 | 11/25 09:15 |
| BROCK | OK-SAME-COMMIT 61ec164802 | 11/25 11:50 | 11/25 11:50 |
| FLG | OK-PINNED 3d1fb88ae2 | 11/25 13:41 | 11/25 13:41 |
| CARL | OK-PINNED 09184a045a | 11/25 09:16 | 11/25 09:16 |
| LABOR | OK-PINNED 24903cfe48 | 11/25 09:15 | 11/25 09:14 |
| ISHM | OK-PINNED 93ddd61f13 | 11/25 11:04 | 11/25 11:04 |

---

## REGINALD

**HEADER:** as of 2026-11-25 09:15 ET, due-row wake D:L514 · pin 25fca1c9fa.

**VIEW**
- Severity stays CONCENTRATED on Q3 levels; the 11/07 L180 BROADER qualifier (weak, foreclosure limb only) stays attached.
- One private bank, United Fidelity, carries about 90% of the industry multifamily past-due rise and most of the CRE charge-off jump. Desk reads it as not transmission, with no listed instrument.
- High yield wide (REG-T-03 and REG-T-04 FIRED) while the bank cross-check is BANK-ABSENT through 11/23; not re-run on the 11/24 cell.

**MOVED SINCE BASELINE**

| Item | Figure, date, basis |
|---|---|
| FDIC Q3 QBP (published 11/24, read at the PDF) | Failures 4 in Q3, all under $1B; 6 YTD; failed assets $1,409M YTD ($892M in Q3). DIF $163.5B, ratio 1.50%, Q3 insurance-loss provision $933M (vs −$287M Q2, not attributed by FDIC). Problem banks 39 (47); their assets not published |
| >$250B nonfarm-nonresidential | noncurrent 2.02% (2.24 Q2); PDNA 2.27% (2.48); non-owner-occupied PDNA 2.781% (3.076; 3.403 Q1) |
| >$250B multifamily noncurrent | **0.85% (0.76 Q2, 0.75 Q1): ROSE.** In the memo and KB ML-REG-323, NOT in the brief or STATUS (flag R1) |
| Coverage | all banks 169.26% (172.70); >$250B 195.30 (195.36, flat); $1-10B 126.73 (150.78), mostly United Fidelity |
| Multifamily PDNA, all banks | 1.40% to 1.74% (+$2.4B); ex United Fidelity 1.41% to 1.43% (memo §3) |
| Unrealized securities losses | $486.0B (QBP p2); reconciles to desk's own $485.7B (11/17 FFIEC bulk) |
| United Fidelity | MF nonaccrual $0.12M [6/30] to $2,143.2M [9/30]; Q3 NCO about $362.5M; allowance $81.7M to $6.3M (BankFind, KB ML-REG-325) |
| REG-03 (70%, H2) | dated attempt: CRE NCO 0.1406% to 0.1992% = 1.417x Q2, under 1.5x, NOT MET, OPEN to Q4 QBP; ex United Fidelity 1.08x (INFERRED) |
| WQ-313 foreclosed NFNR, $10-250B banks | $723.9M, $915.3M, $1,085.6M; second rise YES on the letter; Bank OZK +$128.0M of +$168.6M same-bank; East West +$40.9M; Western Alliance +$37.0M; First-Citizens −$37.0M; 29 banks up, 30 down: CONCENTRATED |
| Seacoast check | **MET** at OpenFEMA: DR-4956 (11/24) names Martin, Palm Beach, St. Lucie. Exposure map, no grade |
| Prices (STATUS) | WAL $70.43, KRE $69.76 [11/24 settled]; REG-T-02 exit 0 of 3, 60 rows; REG-T-01 un-fired |
| HY | 363 [11/23]; 11/24 not posted at 09:10 ET; REG-T-04 exit run 0 |
| Fires, kills, retractions | none new. REG-T-04 fire and REG-37, REG-34 TRUE were in the 11/24 block, inside the baseline |

**CROSS-DOMAIN / CALIBRATION:** CREED-T-03 inputs sent to CREED, not graded by REGINALD. QBP to CREED, HOMER, TERRY, PROME. TERRY: no candidate. Exit-count warning: a CSC default (grace about 12/16) plus the 11/30 index rebalance can lower HY mechanically. Conviction: concentration direction HIGH, timing MEDIUM. The stated uncertainty (bank equity ahead of credit) is an October-era line.

**FORWARD (about 3 weeks):** 11/30 REG-06 next read and index rebalance; CSC grace about 12/16; 12/14 United Fidelity capital plan; Wed 12/16 vendor-guidance comment close, full file 12/17; REG-T-04 exit count (≤330 ×5). Unscored projection: about 75% the Q4 QBP shows no broad large-bank CRE deterioration; alternative is a second named bank with a nine-figure MF nonaccrual jump at 12/31. From 11/24, unscored: about 60% no exit run by 12/11; about 70% bank leg absent through 12/11.

**NEXUS-NAMED:** none in the 11/25 block; no row addresses NEXUS by name.

**STALE FLAGS**
- R1: STATUS says large-bank CRE "fell on every basis" and the memo says "improved on every basis". The same memo's table has >$250B MULTIFAMILY noncurrent up 0.76 to 0.85. True for nonfarm-nonresidential and construction, false for multifamily. The brief omits the multifamily cell. Load-bearing for the NEXUS apartment-loss question.
- R2: HY [11/24] = 372 posted later. REGINALD re-read FRED at 15:37 ET (BOARD_LOG, boot intake b5d6fd46c6, "Boot session only"): exit run 0 through 11/24, both rungs stay FIRED, no new fire. STATUS and brief still carry 363.
- R3: CREED-T-03 GRADED 13:26 ET: **NOT FIRED** (PDNA 2.48 to 2.27 decides; coverage leg MET for the first time; S3 held at 2). Brief still says "CREED grades".
- R4: claims "189K secondary" in the brief is now confirmed at DOL by LABOR (LABOR 189,000; REGINALD BOARD_LOG 020 agrees).
- R5: NEXT DECISION POINT still lists the Q3 QBP "(~11/25)" as ahead; WATCH rows still read October (October 27 P&A, October 30 FHLB, "November7" run). VIEW bullets are October 20 vintage.
- R6: post-brief HOMER corrections unfolded: both October Trepp MF highs are about one loan each (Cove $210M for delinquency, Blackjack $517.7M for special servicing); Fitch review closed, nine affirmed, none cut; Freedom's January 2027 maturity corrected to $540M. No REGINALD-brief figure rests on these (FLG's 9.22% mention does, flag F3).

---

## BROCK

**HEADER:** as of 2026-11-25 11:50 ET, C8 session on WALTER SIG-W-20261125-013 · same-commit pin 61ec164802 · Convergence 58/70, last rescore 9/25.

**VIEW**
- The private-credit managers (OWL, ARES, APO, BX, KKR) are beta, not leading, in the chip-led selloff; one common factor, not five signals.
- Substance firmer than transmission; bank transmission unconfirmed; X1 NOT MET, wrapper NOT ARMED.
- BDC calm is not information either way yet: marks are 9/30; 12/31 marks print February to March.

**MOVED SINCE BASELINE**

| Item | Figure, date, basis |
|---|---|
| Managers vs RSP, three down days 11/20, 11/24, 11/25 (intraday 11:37 to 11:44 ET, not closes) | cumulative residual OWL −0.0, ARES +2.9, APO −2.7, BX −0.5, KKR −1.9 pp; chip loading +0.01 to +0.14; no single day beyond 1.5 sigma; 11/25 alone all five 1 to 3 pp under RSP line (OWL −1.1, ARES −0.8, APO −2.9, BX −1.6, KKR −1.2) (KB-BRK-531). Memo prints ARES −0.8, so "1-3 pp" is a rounded phrase |
| Vs SPY | every manager fell LESS than beta |
| HY | 372 [11/24, FRED, LIQUID's], +9; CCC 1,405 / BB 225; CCC/BB FELL 6.33 to 6.24; X1 test (b) wrong sign again; ladder row 10 NOT FIRED; W3 ≤5.93 leg 0.31 away (KB-BRK-535) |
| AI-infra exposure ledger (Q3 10-Qs) | Managers' own 10-Qs: 0 hits for CoreWeave, GPU, Oracle, Hyperion. Largest named commitment Blue Owl IREN facility $730.0M across four funds. Ares Core Infra CoreWeave $56.0M = 0.72% NA. ARCC/ASIF Vantage at par ($195.9M; ASIF data-centre subtotal 3.04% NA). Apollo Debt Solutions CoreWeave FV $17.8M. KKR/FSK none found (KB-BRK-532/533) |
| Post-brief (KB-BRK-536, 11:51 ET) | BKLN −0.42%, SRLN −0.44% vs HYG −0.14%, JNK −0.19% intraday 11/25 11:50 ET; not a distribution artifact |
| CRMT | feed empty since the 11/24 petition (EDGAR 11/25 11:43 ET) |
| Fires, grades, kills | none; BRK-33 TRUE (Brier 0.4225; scoreboard 0.267, n=18) was before the baseline |
| Dropped from brief | CRMT tenth-bridge row; the LIQUID CCC/BB 6.20 [11/5] row |

**CROSS-DOMAIN / CALIBRATION:** 11/25 row to NEXUS, PROME, TERRY, VULCAN: not a transmission signal; TERRY no card. Conviction direction HIGH, timing LOW, bank recognition LOW. Exit §3 is 2 of 3 downgrades. Memo §7, unscored: about 60% high-beta equity plus single-name AI credit through mid-December; about 25% a pulled or repriced AI deal reaches a credit book first; AI line marked under 95 at 12/31 about 35%; pulled or repriced (50 bp) AI deal with an alt-manager lender about 30% by 12/16; OTF cuts base dividend about 35%.

**FORWARD:** 11/30 W3 grade (L183), BRK-32 STUCK (L716), Monroe Q4 offer expires, CRMT escrow; about 12/1 Nasdaq 3.01; 12/3 CRMT rollover documents; about 12/3 to 12/7 BCRED Q4 letter (offer expires 12/1) and Monroe final; Fri 12/4 CABO hearing (press only); 12/07 GATE-BRK-R2 review; about 12/10 CRMT 10-Q; about 12/15 bidding order; about 12/16 CABO coupon grace; 12/31 IREN draw end and BRK-25/26/34/35/37.

**NEXUS-NAMED (verbatim, new row):** "NEXUS / PROME / TERRY / VULCAN | 11/25: no score moved, 58/70. The private-credit managers are NOT leading the chip selloff: ... Not a transmission signal. Watch: manager residual under -2 sigma two sessions with chips flat; a pulled or repriced AI deal with an alt-manager lender; Blue Owl BDC AI-line marks at 12/31. TERRY: my view no card." Ten older rows also name NEXUS (11/24 to 11/11 and the 39-name discount, IREN, CABO rows).

**STALE FLAGS**
- B1: KB-BRK-534 carries CoreWeave 5Y 1,363 [11/25] and Oracle 356/362; LIQUID says 1,363 was CANCELLED at the reporter; valid 5Y 1,314 clean / 1,359 dirty [11/24 close]; Oracle 370 to 377 [11/25]. The figure is not in the brief, only in the KB. No BROCK receipt seen; WALTER 022 is still unfiled in BROCK's lane at HEAD.
- B2: "BDC calm" does not mention the loan-ETF underperformance (KB-BRK-536), which BROCK's own memo calls the possible first market sign if it widens over several sessions with BDC prices following.
- B3: 10Y 5.10 [Treasury 11/12] is 13 days old and is still the Duration-rung figure.
- B4: BDC discount 26.15% [11/6] is 19 days old.
- B5: 12 unfiled WALTER cards (022, 024 to 027, 029 to 031, 033 to 036) and 4 top-level packets (LIQUID, DAEDALUS, PROME client-name, NEXUS apartment question) are in BROCK's inbox at HEAD. They include the CoreWeave $4.5B loan, which is the "pulled or repriced deal" test: indications reported to match size (035, one source), which weakens the pulled-deal read.

---

## FLG

**HEADER:** as of 2026-11-25 13:41 ET · pin 3d1fb88ae2 · v1.0.6 (wording only).

**VIEW**
- $2.8B non-accrual book with a 5.5% specific reserve ($155M) leans on a refinance channel for NYC rent-regulated loans the bank does not control.
- Q3 exit mix inverted: cures 56.3% of outflow ($144M), payoffs 29.7%, cause undisclosed; a cure after a rate cut is not a recovery (INFERRED).
- The wall is 2027; no graded item moved.

**MOVED SINCE BASELINE**

| Item | Figure, date, basis |
|---|---|
| **Correction** | Rent freeze binds $8.1B ($8,120M at 9/30; $8,490M at 6/30, deck) of NYC loans with ≥50% rent-regulated units, NOT $8.5B, the New York State figure (KB-FLG-128). T-08's $8.9B is New York State too |
| OCC | $112,000, order AA-ENF-2026-45, 82 flood notice or force-place violations 9/2022 to 6/2024, prior management; immaterial (KB-125) |
| FDIC Q3 QBP | industry MF deterioration about 90% United Fidelity; logged not scored (KB-126) |
| Housekeeping | 44 stale KB rows (26 STALE, 3 SUPERSEDED, 15 refreshed); no fire, grade, kill or threshold |
| Price (STATUS) | $10.68 intraday 11/25 13:38 ET; $10.43 settled 11/24 (REGINALD); RED band $11.39 |

**CROSS-DOMAIN / CALIBRATION:** SENDING unchanged: REGINALD (roll-forward; SR 07-1 322.11%), NEXUS (M-05 / R10 inputs), CREED (2027 MF reset $8.4B incl. $2.9B ≥50% rent-regulated, call 10/23). Conviction direction H, timing L, level M. K-3 kill leg UNSET, so no falsifier on the loss leg. Counterevidence: SR 07-1 down 12 quarters, NAL rate 4.90% to 4.55%, CET1 12.38%.

**FORWARD:** rent-freeze merits ruling by 12/31 (press or filings only). STATUS adds Q4 release about 1/29/27, 10-K about 3/1/27. Nothing dated within three weeks.

**NEXUS-NAMED (verbatim):** "NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (10-Q) is a series low; specific reserve 5.5% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision".

**STALE FLAGS**
- F1: the body line "MF $8,519M (9/30) reprices or matures in 2027 into the freeze" was not touched by the geography fix. $8,519M is ALL multifamily 2027 repricing or maturity, not the NYC rent-regulated subset ($2.9B to $3.0B ≥50% rent-regulated per the desk's own CREED row). Do not read "into the freeze" as $8.5B bound by it. A coincidence of size with the withdrawn $8.5B invites confusion.
- F2: WAITING FOR row "REGINALD cohort read, open, its 11/07 re-score" is past; REGINALD has since published concentrated (11/25).
- F3: STATUS / history uses the Trepp MF special servicing 9.22% (HOMER relay, KB-117) as peer context; HOMER 14:35 ET says it is about one loan (Blackjack). It is not in the live brief.

---

## CARL

**HEADER:** as of 2026-11-25 09:16 ET · pin 09184a045a · v2.6.7, **52/70**.

**VIEW**
- Concentrated household strain; broad collapse still not established.
- October buffer rebuilt for one month, partly a windfall; gas squeeze easing.
- Full-thesis kill NOT FIRED; V2 subprime ABS tiers next.

**MOVED SINCE BASELINE**

| Item | Figure, date, basis |
|---|---|
| **CRL-32 MISSED** (NOT-FIRED-REBUILD, early; registered 25%) | October saving rate 4.1% first print (BEA 26-51, 11/25) vs ≤3.8; September revised 3.8 to 3.6 (KILL bar ≥4.3 not met), August 4.0 to 3.9, July 4.5 to 4.4; real DPI +0.5% (+$92.8B), real PCE 0.0 (−$5.8B); PCE prices 3.8% y/y, core 3.3%. One-time Medicare premium rebate in income; ex-rebate about 3.9% (INFERRED), so the grade does not hinge on it. Unresolved: BEA gives no rebate size |
| **V5 Gas Squeeze 4 to 3; score 53 to 52/70** | registered AAA rule, below $4.00 every observed day 11/10 ($3.979) to 11/25 ($3.587); 10 of 16 days observed, 6 gaps bracketed. EIA 11/23 $3.642; diesel AAA $5.764 11/25 (high). Next step needs <$3.50 for 4+ weeks AND diesel normalized |
| STATUS only | Conference Board November 103.3 (91.9 revised), highest since January 2025, labor differential +12.4, SECONDARY, survey closed 11/17 before the 11/20 selloff (KB-630); ERS 2027 food at home 1.9% (from 1.0), CRL-10 stays 1% |
| Retractions | none; V14 marked JUDGMENT-SCORED (WQ-726 not now, 11/23) |

**CROSS-DOMAIN / CALIBRATION:** new row to PROME, WALTER, TERRY, NEXUS, RED. 52/70 is a registered-rule tally on about ten roots, not 14 independent confirmations. TERRY: no card suggested.

**FORWARD:** about 11/30 V2 October read (EART/SDART 10-Ds); 12/01 Section 301 notice (CRL-23); 12/01 JOLTS; 12/04 NFP (V16 print 2 of 2: S>0 AND R>0 sends a 4 to 3 candidate to Will) and Michigan preliminary; 12/7 G.19; 12/8-9 FOMC; 12/10 CPI and Z.1; 12/15 PPI; 12/16 retail. 12/23 PIO, unscored view about 60% saving rate ≤3.9%.

**NEXUS-NAMED (verbatim, new row):** "PROME / WALTER / TERRY / NEXUS / RED | 11/25: CRL-32 MISSED (NOT-FIRED-REBUILD, early). BEA 26-51 October saving rate 4.1% first print vs ≤3.8% bar; September revised 3.8 → 3.6% (KILL bar ≥4.3 not met); real DPI +0.5%, real PCE 0.0. One-time Medicare premium rebate in income; CARL ex-rebate about 3.9% (INFERRED). V5 4→3 on the AAA rule." Plus "PROME / BRENT / NEXUS | AAA regular under $4.00 every observed day 11/10 ($3.979) to 11/25 ($3.587); EIA 11/16 $3.805, 11/23 $3.642." Older rows name NEXUS too.

**STALE FLAGS**
- C1: VIEW 11/21 bullet still says "leans against CRL-32's saving leg at 12/23 (direction only, 25% unchanged)". CRL-32 is resolved; residue.
- C2: brief says "October Conference Board rebounded"; STATUS has November 103.3 (secondary). Omitted from the brief.
- C3: Section 301: brief has only "12/01 notice (proposed 11/25)". ZHAO's packet (China up to 20% net of the forced-labor rate, stacking on 2018-19 duties; Annex B toys, games, linens exempt) and VULCAN/WALTER corrections arrived after the brief and are unconsumed.
- C4: FERT GATE-FERT-G5 FIRED 11/25 13:41 ET (retail MAP $1,004/ton vs strict $1,000) routed to CARL for a food-CPI read; unconsumed. FERT itself expects no measurable effect in the November, December or January CPI.

---

## LABOR

**HEADER:** as of 2026-11-25 09:14 ET · pin 24903cfe48 · 22/80.

**VIEW**
- Freeze thesis stood down 11/6 on its own kill rule; low-fire holds, low-hire loosening.
- Claims band B; no score, band or gate moved; holiday seasonal factors dominate.
- Costs accrue in legibility (long-term unemployment), not direction.

**MOVED SINCE BASELINE** (DOL advance release 11/25, read at the issuer PDF, dol.gov answered)

| Series | Print |
|---|---|
| Initial claims w/e Nov 21 | 189,000, −13,000; w/e Nov 14 revised 203 to 202K |
| 4-week average | 196,000, −1,500, mechanical |
| Continuing, w/e Nov 14 | 1,697,000, −95,000; w/e Nov 7 revised 1,763K to 1,792K (+29K); 53K inside 1,750K |
| NSA initial | 212,945; +15,894 vs factors +30,549; −13.0% vs same week 2025; NSA insured −5,578 vs factors +82,453 |
| Grades | band B; T-01 not fired (54,000 away), T-02 not fired (111,000), R13-c 1.0038, Kill B 0 of 5, v13 and v7 runs restart at 1 record-only |
| LAB-22 | draw 3 missed (4,000 above the bar); 32% to 27%, mechanical |
| T-07 WARN | Oct 22,910 (was 22,453; page updated 11/23), bar >50K, not fired |
| Cards | 12/3 claims and 12/1 JOLTS frozen (JOLTS one day late) |

**CROSS-DOMAIN / CALIBRATION:** realization channel to CARL and REGINALD stays shut; CC above 1,750K for consecutive weeks would be the first watch; record 0 for 6 at ≥60% on threshold calls, mean Brier 0.324 over 15. Supply confound narrowed, not resolved. Memo view, unscored: band C before 12/18 about 10%; JOLTS layoffs rate ≥1.2% on 12/1 about 10%.

**FORWARD:** Tue 12/1 JOLTS Oct 10:00 (layoffs ≥1.2% goes to CARL and REGINALD; LAB-21 68%); Thu 12/3 claims (X − 191,000)/4, T-01 bound X >407,000, and Challenger Nov (v5 demote, LAB-20 55%); Fri 12/4 NFP Nov (LAB-18 5%, LAB-24 50%, T-03, T-06, T-08, v8 1 of 2); 12/11 CR expiry; 12/18 FL UR Nov. Challenger card owed by about 11/26 and NFP card by about 11/27, not written.

**NEXUS-NAMED (verbatim):** "CARL · HENRY · REGINALD · NEXUS · TERRY | Freeze-thaw v2 FIRED 11/6, card §3d row 1. v4/v6/v7 stood down at the floor of 1, 27 → 22/80 ... This is a hiring read". Nothing new since the baseline names NEXUS.

**STALE FLAGS**
- L1: NEXT DECISION POINT still puts "Wed 11/25 claims ... (X − 195,000)/4; T-01 X > 404,000" first; that print is graded.
- L2: FORWARD CATALYSTS has no 12/1, 12/3 or 12/4 row and still lists "Fri Nov 6 NFP October" as pending.
- L3: CALIBRATION "LT-unemployed share 27.0% (on the >27% restore bar, not over it), CC 1.70 to 1.72M for four weeks (v7 dropped to 2)" vs STATUS 27.6% [Oct], OVER the bar (v6 stood down to 1), CC 1,697K, v7 1. A figure and direction mismatch, so schema §4.4 (a).
- L4: T-07 row "FL unemployment 4.4% Sep" vs 4.3% Oct in the FL row above it. Freeze-thaw row says claims 200,000 (11/12), superseded.
- L5: HOMER packet 11/25 asks whether LABOR carries residential construction jobs (−16,400 Oct; −40,200 over 12 months); unanswered at HEAD.

---

## ISHM

**HEADER:** as of 2026-11-25 11:04 ET · pin 93ddd61f13. Scores 18/35 raw, 13/25 shared-root, unchanged. Nothing fires.

**VIEW**
- Equipment spending real and rising, but less of it is U.S. production than measured before; imports and price fill the gap (INFERRED).
- Factory upturn real, narrow, durability unproved; R1 grades once, December 1.
- Regional November surveys diverge (KC and Richmond recovered; NY and Philadelphia cooled).

**MOVED SINCE BASELINE** (brief rewritten; previous as-of 11/19)

| Item | Figure, date, basis |
|---|---|
| Durables October advance (Census, 11/25, nominal SA) | core orders +1.2% to $89.383B, shipments +0.6% to $86.670B; September revised up ($88.343B +0.8%, $86.172B +1.3%); NSA y/y +13.3% / +10.7%; durables +0.2% |
| BEA Q3 equipment, second estimate, SAAR | +21.8% (advance 20.9); info processing +41.7% (37.4); computers +80.1% (66.7); industrial +20.6% (24.7); transportation −6.5% |
| G.17 annual revision 11/24 (base 2022) | business equipment +4.5% Dec 2022 to Oct 2026, under half the earlier estimate; October +0.1% (was +1.0); total IP −0.4%, y/y +1.7% (was 2.1); manufacturing Sep +0.2, Oct +0.3; utilization 76.8% |
| Regional Nov new orders | NY 3.0, Phila −0.4, KC 16 (composite 18), Richmond 2 (composite 3): 1 of 4 negative |
| S&P Nov flash 54.5 | SECONDARY, not graded; Oct final 54.9 |
| Deere FQ4 8-K | PPA sales −15%, profit −33%; FY27 net $4.50 to 5.25B; large ag +5 to +15%; 100+ hp dealer stocks 31% vs 23%; tariff recoveries $383M FY, about $1M Q4 (INFERRED); FS credit-loss provision higher, no dollar figure |
| Grades | J1 Q3 contraction NOT-MET reaffirmed; J2 NOT-MET; VX-ISH-02 and VX-ISH-06 unchanged. Seven due rows closed |

**CROSS-DOMAIN / CALIBRATION:** packets to VULCAN (P2), HENRY, FERT, CARL, TERRY, WALTER. Post-brief VULCAN answer 11:53 ET: Jan to Sep 2026 imports of computers, accessories and chips $590.8B vs $304.1B (+$286.7B, +94.3%, FT-900 nominal); import half measured, price half not separated. Desk frame R1 about 10% toward real / 7% toward borrowed / 83% neither. Unscored: gap does not close about 70%; Section 301 pull-forward visible about 40% (December to February).

**FORWARD:** 11/30 Dallas Fed; 12/1 S&P final 09:45 (R1) and ISM 10:00 (<47 strict); 12/2 rail; 12/3 full M3; 12/8 FT-900; 12/16 G.17; 12/23 durables and BEA third.

**NEXUS-NAMED:** none.

**STALE FLAGS**
- I1: the brief says "imports and price fill the gap (INFERRED)"; VULCAN's answer makes the import half measured. Unconsumed in ISHM's top-level inbox.
- I2: "China 20%" (STATUS row, VULCAN's read) is looser than ZHAO's "up to 20% net of the forced-labor rate, Annex A up to 10%, Annex B exempt"; the brief itself only says proposal and no effective date. No brief fault.
- I3: no cross-desk send in the brief is out of date against STATUS.

---

## CROSS-BRIEF (10 lines)

1. **High yield OAS is cited by REGINALD (363 [11/23]) and BROCK (372 [11/24]), with LIQUID the owner (372, first-published, graded 11:45 ET).** REGINALD's 363 is an earlier print, not a disagreement; BOARD_LOG 018 shows REGINALD read 372 at 15:37 ET without a brief or STATUS write.
2. **HY: one repricing on many surfaces.** BROCK says stress sits in AI single names and upper tiers, not the CCC tail (CCC/BB fell 6.33 to 6.24). REGINALD reads HY-led, bank-absent; LIQUID tier rule BROADENS on 11/24. All three read one FRED vintage: one root, one class.
3. **Nuance between desks:** "not the CCC tail" is BROCK's ratio. CCC still widened 18 bp on 11/24 and 34 bp 11/18 to 11/23 (REGINALD), so "tail calm" is not established, only that it widened less in percent.
4. **FDIC Q3 QBP: REGINALD, FLG, CREED.** All agree United Fidelity is about 90% of the multifamily rise. CREED: T-03 NOT FIRED, coverage leg met for the first time. FLG logs it as the same channel, different book.
5. **Disagreement, scope:** REGINALD CONCENTRATED ($10-250B, 3/4 OZK; 29 up, 30 down) versus CREED: foreclosed NFNR rose in EVERY size tier (all banks +15.9%; >$250B +25.1%, unattributed) and recognition is moving through foreclosure and charge-off. CREED's conjunctive letter did not fire. Plus REGINALD's "improved on every basis" versus its own >$250B multifamily 0.76 to 0.85 (R1). Both bear on the apartment question.
6. **Claims: LABOR 189,000 (DOL primary), REGINALD 189K.** CARL and the kill rule need claims <220K for 8 weeks; consistent. CC revised 1,763K to 1,792K, a level REGINALD's NEXUS-facing text does not carry.
7. **Fuel: CARL (gas under $4.00, V5 down) against ISHM and LABOR:** diesel AAA $5.764 still high; CARL's next step needs diesel normalized. No disagreement; cheaper gas and dear diesel split households from freight.
8. **Section 301 (11/25): CARL, ISHM, ZHAO, VULCAN.** Same instrument, differing detail. ISHM (STATUS) and CARL (SCRATCH, not its brief) carry the "China 20%" shorthand; ZHAO says up to 20%, net of a forced-labor rate (12.5% INFERRED), so about +7.5 points on most goods; other notices set their own rates. Consumers of "20%" should cite ZHAO.
9. **Buffer and spending: CARL saving 4.1% (about 3.9 ex rebate), real PCE 0.0; ISHM business-equipment investment +21.8% SAAR.** Not contradictory: one is household, the other corporate. CARL's Conference Board 103.3 predates the 11/20 selloff (survey closed 11/17). LABOR's labor differential +12.4 is the same secondary read: one datum.
10. **Contradictions with no resolver named:** (a) BROCK "BDC calm" versus loan ETFs underperforming HY bonds (LIQUID, KB-BRK-536), one session; (b) LABOR brief LT share 27.0% versus STATUS 27.6%; (c) FLG 2027 "$8,519M into the freeze" versus the $8.1B corrected freeze base, different objects of similar size.
