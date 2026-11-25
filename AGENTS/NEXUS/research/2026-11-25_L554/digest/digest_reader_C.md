# Digest reader C: eight NEXUS briefs (read 2026-11-25)

I read all eight briefs in full. The baseline is dcdaa06bce (git date 2026-11-17 17:03 ET). Every figure below is quoted from the brief that carries it, with that brief's date.

## Pin check (`python3 scripts/brief_pin_check.py`)
Summary line: `BRIEF-PIN 0 OK: 31 brief(s) checked ... OK-PINNED 21 · OK-SAME-COMMIT 7 · STALE-PIN 1 · UNPINNED 2`.
- BROCK: ⚠️ UNPINNED. "no STATUS hash in the first 40 header lines; A10 fallback: brief commit 90c666d04 is BEFORE STATUS HEAD d8236184a". d8236184a is a STATUS-only weekday fix: 12/3 is a Thursday.
- CARL: ✅ OK-PINNED (pin 02a927b03b = STATUS HEAD).
- GIBBS: ✅ OK-PINNED (140b247b37).
- HOMER: ✅ OK-PINNED (12df1c9940).
- LIQUID: ✅ OK-PINNED (fe3f3b877b…).
- MIDAS: ✅ OK-SAME-COMMIT (ae7fa23ad).
- SHADE: ✅ OK-PINNED (203df0459c).
- ZHAO: ✅ OK-SAME-COMMIT (840e69003).

---

## BROCK
**HEADER:** "**As of:** 2026-11-24 22:52 ET (BROCK, prome-77 due-row wake D:L1232/L1071: CRMT CHAPTER 11 FILED 11/24, D:L1232 GRADED, BRK-33 RESOLVED TRUE, KB-BRK-526; IREN AGM nothing to grade, KB-BRK-527) | STATUS commit: the 2026-11-23 BROCK commit (`git log -1 -- AGENTS/BROCK/STATUS.md`)"
**VIEW:** 🔴 STAGE 2→3. The substance is firming, but transmission to banks is unconfirmed. X1 NOT MET, wrapper NOT ARMED, convergence 58/70 (rescored 9/25, unchanged). "Substance is firmer than established transmission."
**MOVED SINCE 11/17:**
- **Car-Mart (CRMT):** "CRMT CHAPTER 11 FILED 11/24 — D:L1232 GRADED, BRK-33 RESOLVED TRUE (Brier 0.4225 at 35%; scoreboard 0.267, n=18)." 8-K 0001171843-26-007671. Terms: prepack in SD Texas; stalking-horse sale to Cardinal ("former Car-Mart CEO among its leaders"), including the ABS residuals and servicing. "same private lenders fund the DIP ($60M new + $65M roll-up) and roll debt into the buyer; $311.6M accelerated and stayed; trade and unsecured paid in full (proposed); equity ~$0.30/sh; ACMAT trusts NOT debtors."
- **Who is exposed (Car-Mart):** "Single-name exit, no listed lender or bank exposure: no vector moves." "Car-Mart has no HY bonds, so REG-T-04's fire does not rest on it (KB-BRK-528)." Lenders, per the 11/17 row: "CRMT lenders all private (Silver Point, Beach Point); no live bank line." "OTTO V9 re-colours now; TERRY read asked."
- Earlier steps since 11/17: D:L1175 graded a FOURTEENTH BRIDGE (8-K 11/19, relief to Sun 11/22); backstop #9 FINAL EMPTY; D:L1201 NOT GRADED on a silent feed (11/23); backstop #10 FINAL EMPTY.
- HY 323 [11/13] became **363 [11/23, FRED, LIQUID's; REG-T-04 FIRED, REGINALD's]**. HY 376 [11/20] came "in an AI/chip selloff, CCC/BB fell". CCC/BB "rose 6.12 → 6.33 on a narrowing day (KB-BRK-528)".
- TERRY: "HYG-BDC thesis graded WRONG for its window" (11/23 row).
- The FOMC October minutes say "'several' flag banks' indirect exposure via credit lines to PC funds, logged not scored" (KB-BRK-520).
- BRK-33 has come off the 12/31 letter list.
**CROSS-DOMAIN / CALIBRATION:** The Car-Mart row goes to NEXUS/PROME/OTTO/TERRY/REGINALD. Waits:
- Banks/REGINALD: CFG +$52M attribution.
- Car-Mart docket: rollover documents **12/3**.
- Cable One (CABO): coupon grace ~12/16 (INFERRED); hearing 12/4, a press-only date.
- BCRED Q4 letter ~12/04 (INFERRED).
- SHADE/LIQUID: X1 reconcile (L185/L186).

Conviction: "direction HIGH, timing LOW, bank-recognition LOW." Uncertain about: OTF's TII/NII denominator, whether HTGC/GBDC face a funding squeeze, and per-name draw amounts (UNKNOWN).
**FORWARD:**
- 11/30: W3 grade, BRK-32 STUCK, Monroe Q4 offer expires.
- 12/3: Car-Mart rollover documents ("Missed with no extension = APA termination right").
- ~12/03–12/07: BCRED Q4 letter and Monroe Q4 final. A sub-100% at either "FIRES R2 (a) at a third vehicle".
- 12/4: CABO hearing.
- 12/07: GATE-BRK-R2 review.
- ~12/15: Car-Mart bidding-procedures order.
- ~12/16: CABO grace ends.
- ~12/29: Car-Mart sale order.
**NEXUS-NAMED:** The first six SENDING rows and rows 22–25 and 31 are addressed "NEXUS / …" (Car-Mart, CABO, IREN/IE Mackenzie, BDC discount). Footer, verbatim: "NEXUS consumption remains unverified."
**STALE FLAGS:**
- ① The header says "STATUS commit: the 2026-11-23 BROCK commit", but STATUS was committed in the same 11/24 commit and again in d8236184a. The pin check reads it as UNPINNED.
- ② Footer: "Owner fold completed after final STATUS commit 84e7a03c1" does not match the header.
- ③ Past-dated waits:
  - Banks "early-Nov finals".
  - SHADE/LIQUID "L185 11/05–18" (SHADE's own brief says D:L185 closed).
- ④ The BDC discount of 26.15% is dated [11/6], three weeks old, and is labeled with its date.
- ⑤ The 10Y figure is 5.10 [Treasury 11/12].

## HOMER
**HEADER:** "**As of:** 2026-11-25 00:15 ET (data through 2026-11-24) | STATUS commit: `12df1c9940` — written after the final STATUS write."
**VIEW:** "Thesis formally graded 11/20: 0 of 5 legs killed, 🔴 holds" (next grade 2027-02-20). FHA delinquency is "converting, not curing". "Builders broke lower".
**MOVED SINCE 11/17:**
- Thesis grade 11/20 (GATE-HOMER-THESIS-KILL): handle rescored "19 → 21/25".
- MBA Q3 NDS (11/20): FHA SA DQ 11.74% (−5bps QoQ); FHA foreclosure rate 1.89%, the highest since Q1-2017. **HOM-02 MISSED.**
- NAHB HMI 25 (11/17), the lowest since April 2012; price cutters 46% (Red >45% crossed). **HOM-04 HIT.**
- PMMS 7.11% [11/12] is now **7.28% [11/19]**, +17bp; spread ~221bp against a 10Y of 5.07% (11/18).
- NAR pending 63.0 Oct (−16.7% YoY, "second record low (NAR)").
- Redfin gap 70.5% Oct.
- Residential construction jobs −16,400 Oct.
- Census starts 1,309K; permits −7.4%.
- Case-Shiller "+2.1% Sept, unchanged" (S&P 11/24); "No HPI trigger".
- GSE multifamily October: Fannie 0.65% ("at the Orange line"), Freddie 0.62%.
- Fitch 11/16: negative outlook on Pennymac, Planet and Freedom.
- A Florida major disaster declaration (Brevard) is "REPORTED approved 11/24; OpenFEMA empty 04:22Z 11/25".
- Registered 11/24: HOM-07 (55%), HOM-08 (60%), HOM-09 (88%), HOM-10 (60%), HOM-11 (60%).
- **CORRECTION / withdrawal.** The ICE row now reads: "conversion continues (sales up) ; ⛔ 'inflow cools' withdrawn 11/24: Q3 starts +12% YoY, Sept was a base effect." The VIEW bullet reads: "**CORRECTED 11/24: the front door is not narrowing.** ICE FC starts Q3 ~115.6K vs 103K a year ago (+12%), flat on Q2; Sept's −2.9% was a one-month base effect. FC sales YoY has slowed from +41% (Dec-25) to +12–15%; conversion is growing, not accelerating. Read 'growth past its peak' in HOMER's 11/24 correction packets as 'year-over-year growth below earlier readings' (no peak is established)."
- Housing levels unchanged: Trepp MF DQ 8.09% and SS 9.22% (Oct); 90+/FC 882K ORANGE; existing-home sales 3.75M (Oct).
**CROSS-DOMAIN / CALIBRATION:**
- Sends: CARL, REGINALD, HENRY, LABOR, CREED and CORAL (the Florida declaration, "confirm before use"; the flood sweep ask).
- Waits: Trepp Nov ~12/01–05; ICE First Look Oct ~11/25–30; ICE Monitor Dec ~12/07–14; ATTOM ("not out at 11/24").
- Uncertain about: A1 restatement (WQ-725), Cove reversion, the +9bp spread move, the ICE cure YoY, and the cause of the GSE share selloff.
- New: "FHFA Q3 Cape Coral +1.30% vs FMHPI Sept −2.28%: two methods, not reconciled."
**FORWARD:**
- ~11/25–30: ICE First Look Oct.
- 11/25: new-home sales, BEA Q3 second estimate, PMMS.
- ~11/24–30: Apartment List and FMHPI.
- ~12/01–05: Trepp Nov (HOM-05 <8.09%).
- Early to mid December: Toll, Lennar, NAHB Dec.
**NEXUS-NAMED:** none.
**STALE FLAGS:**
- ① WQ-725 is contradictory within the brief. The grade row says "D13 … is WQ-725 with Will" and CALIBRATION is "Uncertain about: whether A1's first conjunct should be restated (WQ-725)". The WAITING row says "**DONE 11/24** (THESIS §11, FHA serious DQ; reads 0 of 2)".
- ② ICE First Look Oct is dated "~11/23–30" in NEXT DECISION but "~11/25–30" elsewhere.
- ③ The "Rates turned back up" row (10Y 4.98, PMMS 7.18% [11/05]) and the Case-Shiller Aug row ("Case-Shiller Sept ~11/24 is the next direction test") are superseded but still in the table. The September GSE rows are marked as superseded.
- ④ The Sept ICE row still prints "FC starts 40.0K, −2.9% YoY — first negative YoY", with the withdrawal note beside it.

## MIDAS
**HEADER:** No As-of line and no STATUS commit pin in the brief; the pin check passes on OK-SAME-COMMIT. Its newest block is headed "**November 23 — gold fell with stocks through the 11/19–11/20 break; L2 decided (current read for peers)**".
**VIEW:** Gold is trading with risk assets. "GLD is not book protection" survives. Composite 13/20, unchanged.
**MOVED SINCE 11/17 (gold):**
- 11/18: GLD MIRROR close $341.25 (−3.19%), residual −3.34%, real 10Y 2.88% → UNEXPLAINED-DOWN. Trust +7.98 t over 11/13–11/17.
- 11/19: GLD −1.76%. 11/20: GLD −3.67% (MIRROR). Real 10Y fell 11 bp to **2.77%** (PRIMARY 11/20). Residual −5.35%, "the largest on file", and both days are LIQUIDATION-candidates.
- The SPDR issuer archive "now refuses automation, so tonnes after 11/17 are unknown".
- WQ-451 L2: "6 of 10 stress days with GLD up once". The falsifier is out of reach.
- Grades: **MIDAS-13 HIT**, **MIDAS-20 HIT** (11/18), L3-TIC SUPPORTS on sign only ("weak evidence of de-dollarisation"). MIDAS-11 (HIT side) and MIDAS-17 (MISS side) wait for the issuer row, backstop 11/27. Under MIDAS-17, "GLD −12.50% vs −1.98% implied".
- COT 11/17: net/OI 40.74% (−6.24 pp). GSR 85.60, first yellow.
- Copper: band orange (HGZ26 −13.79% vs 200-day); LME yellow.
- WPIC Q3: 2026 platinum surplus +468 koz (from +265). PPLT d200 −25.13%.
**CROSS-DOMAIN / CALIBRATION:**
- Sends to TERRY, LIQUID, RED, BOND (real 10Y 2.77%), ZHAO, HENRY, HAWK and SAM.
- Uncertain: the issuer tonnes since 11/17, and the forced-selling element ("unproven" in the 10/30 block).
**FORWARD:** 11/27 issuer-row backstop for MIDAS-11 and MIDAS-17. "WGC October (L822) early December" (from the 11/8 block).
**NEXUS-NAMED:** none.
**STALE FLAGS:**
- ① About 60% of the brief is October blocks. "Current reading basis: October 26 …" and "Next existing clocks: October 30 forecasts/map review; November 2 band-state forecasts" are past-dated, and the per-metal price lines are Oct 26.
- ② "WQ-522 remains registered/not ruled" (final line) contradicts the 10/28 block: "WQ-522 M1 successor draft RETIRED by Will".
- ③ There is no As-of stamp.

## LIQUID
**HEADER:** "**As of:** 2026-11-24T23:36:48-05:00 | STATUS commit: `fe3f3b877b90eb58063310904799186a9107c862`"
**VIEW:** Credit-price stress persists, and AI-infrastructure credit is being refused selectively. Funding is calm. "ISSUANCE-FREEZE read: NOT A FREEZE, SELECTIVE". X1 CLOSED.
**MOVED SINCE 11/17:**
- HY 334 [11/16] became **376 [November 20], 363 [November 23], first-published**. The >320 run became "MET on the November 17 observation, extending: 7 observations (323/334/343/347/352/376/363)". REGINALD's REG-T-04 (>350 ×3) "FIRED on the 11/23 cell".
- **GATE-LIQ-072**, previously NOT FIRED (IG 90, basis 244), is now "**Leg 2 FIRED on IG 98 [11/20]** (first since 7/9; basis 266 not met)", with IG 97 [11/23]. Re-assessment: "AI credit repricing inside an open IG market; HENRY + NEXUS routed via WALTER."
- **GATE-LIQ-069:** "L4 FIRED on the 11/20 session (IREN −17.97%, APLD −17.81%, NBIS −16.11%, HY +24): 3 legs, no new consequence."
- **GATE-LIQ-076** reviewed 11/20: NOT MET, 1 of 3 (W3). Next review 12/2.
- Issuance evidence:
  - Proofpoint $1.25B at 8.5% (11/18).
  - IG $46.5B in the week of 11/16.
  - Pulled or refused: UST Global $400M (11/16), Fullscript LBO to private credit (11/17), ING ~$500M data-centre loan "short of bids 11/20", "an Oracle data-centre loan piece sold mid-80s".
- CoreWeave 5Y "about 1,314 bp clean [11/24 DTCC]". Earlier: ~1,078 [11/18], 1,154 [11/10].
- **Funding legs:** "SOFR99−IORB +9 [11/23]; 079 not armed" (table: +8 [11/18], +9 [11/17]; the arming line is +30).
- Forward view (unscored): "~70% another named pull by 12/11, ~20% broad freeze, ~35% echo."
**CROSS-DOMAIN / CALIBRATION:**
- Routing: HENRY and NEXUS via WALTER; BROCK owns X1's relative half and Cable One; ORACLE owns December Fed pricing.
- ⚠️ "US HY weekly volume UNMEASURED (paywalled) … Thanksgiving week cannot separate lull from freeze; the test is the week of 11/30 to 12/4."
- Unreachable: cross-currency basis, swap spreads, margin and haircuts.
**FORWARD:**
- 11/25: 069 review_by.
- 11/30: 076 re-arm; GENIUS Act read.
- 11/30–12/4: issuance test.
- 12/2: 076 review.
- ~12/16: Cable One grace ends.
- 12/30: LIQ-08 (HY ≥400, 10%) and LIQ-09 (HY ≤320, 38%) resolve.
- 12/31: Hertz Class B condition.
**NEXUS-NAMED:** "re-assessment = AI credit repricing inside an open IG market; HENRY + NEXUS routed via WALTER."
**STALE FLAGS:**
- ① The brief contradicts itself on REG-T-04. The current judgment says it "FIRED on the 11/23 cell". The test table still says "REGINALD >350 ×3 witness 1 of 3 (352 [November 19])", and "Next:" says "REG-T-04 (1 of 3)".
- ② "Next:" still lists "069 L4 on the November 20 session (APLD/IREN closes, HY ≥ 357)". That leg is now graded FIRED.
- ③ It also lists the ING "bids-wanted (due November 19)", which is past-dated.
- ④ The funding paragraph and H.4.1 figures are dated Nov 5–9.
- ⑤ Last line: "This is the final STATUS fold of the November 14 session".
- ⑥ The Car-Mart line in the counterevidence section predates the Chapter 11 filing.

## CARL
**HEADER:** "**As of:** 2026-11-21 18:25 ET | STATUS commit: `02a927b03b`"
**VIEW:** 🔴 v2.6.6: "concentrated household strain; broad spending collapse remains unestablished." Score 53/70.
**MOVED SINCE 11/17:**
- 11/21 "**V14 HOLDS 3**". HENRY's S&P red line: "6,910.39 on 11/20 vendor, −11.62% from the 10/6 record". S&P +5.7% YoY; "card lenders fell about half the index".
- Michigan final: long-run 3.3% (V12 <3.0% not met). "low-wealth finances up, largest stockholders down".
- CARL corrects itself: its STATUS had called 7,037 a "V14 trigger"; that is HENRY's routing line.
- Projection (unscored): "about 70% Michigan 12/04 again shows top stockholders worse; about 70% November retail control ≥0; under 10% V14 moves by 12/18."
- From before baseline but stated: "CRL-34 CONFIRMED 11/17 at 72%".
**CROSS-DOMAIN / CALIBRATION:**
- Sends to PROME, WALTER, TERRY and RED. The Michigan bottom-cohort gain is "staged to RED".
- Waits: BEA 11/25 08:30; OTTO EART ~11/30; STUE court "Mon 11/23 11:00 ET"; Fed 12/8–9; payrolls 12/04.
- Uncertain: the FY2026 ALLY vintage, September real spending and saving, and the student-loan cure share.
**FORWARD:**
- 11/25: PCE and income (CRL-32 leg 1).
- 11/30: EART 10-Ds.
- 12/04: Michigan preliminary and November payrolls (V16 print 2 of 2).
- 12/09: FOMC.
- 12/10: Z.1/DFA.
- 12/16: retail.
- 12/23: CRL-32 final.
**NEXUS-NAMED:** Rows addressed "PROME / NEXUS / REGINALD / CORAL" (airfares 11/11), "PROME / RED / NEXUS" (core CPI and card APR), "PROME / BRENT / NEXUS" (gas, CRL-34) and other older NEXUS rows.
**STALE FLAGS:**
- ① The V5 downgrade check "AAA below $4.00 through 11/24" was due 11/24 and no result is recorded (As-of is 11/21).
- ② The STUE court wait "Mon 11/23" is past-dated.
- ③ HY 348bp [11/05] is in VIEW; LIQUID has 363 [11/23].

## ZHAO
**HEADER:** "**As of:** **2026-11-18 16:3x ET (by `date`)** — registered wake D:L1038 (PROME prome-6e), September TIC: **ZHA-22 RESOLVED YES** … | STATUS commit: NONE (folded in the same commit as STATUS)"
**VIEW:** 🟠 29/60 ELEVATED (unchanged since 11/06). China's demand at home is still contracting. China is not a forced Treasury seller. Selling is "MEDIUM, DECELERATING".
**MOVED SINCE 11/17:**
- **ZHA-22 RESOLVED YES** at 60% (China LT −$3,457M, Brier 0.16).
- China holdings $590.7B → **$563.9B**.
- Six-month net −$71.5B → **−$50.2B**.
- "Four straight months of coupon selling (… −3.5B); September bills −9.7B". "Sep level fall −$26.8B is ~43% price".
- Foreign official: "−$80.9B on price and bills while official coupon buying was +$27.6B".
- Q3 China+Korea −$25.9B: ">$50B route NOT met".
- Belgium $507.9B (rho +0.048, n=44).
- "BIS re-check NOT ENACTED (KB-287)."
- China and export controls (status line, unchanged since 11/17): "China's answer to the new US chip rule is a conditional threat, not a measure (MOFCOM 11/17 …「若美方一意孤行」, none named; levers in place: the 11/9 two-month pauses of a 24% tariff and two US blacklists, and the Ga/Ge/Sb ban to the US that re-arms 11/28 unless renewed)."
- Other export-control lines: the BIS Affiliates Rule is stayed to 2027-01-10. All 11/10 clocks are "re-suspended to ~1/10".
**CROSS-DOMAIN / CALIBRATION:**
- Sends: LIQUID (HK peg, TIC), HENRY (PBOC fix, China 10Y), VULCAN/WATT/HAWK (clocks), HANS (Belgium), MIDAS ("PBOC gold +0.74 Moz ≈ 23 t in Sep").
- Waits: TIC Oct ~12/17 (date unconfirmed); VULCAN on 0.1% content; LIQUID on the official-vs-private question.
- Uncertain:
  - a third extension or a deal on the 1/9–1/11/2027 cluster;
  - the cause of the August residuals;
  - HKMA intervention;
  - leg F's hit rate.
**FORWARD:**
- Fri 11/27: MOFCOM 公告2024年第46号 clause 2 ends; 11/28 is the first uncovered day (Ga/Ge/Sb/graphite).
- 11/30: November PMI (ZHA-23).
- ~12/17: TIC.
- An "UNPRICED BINARY": a BIS Entity-List package naming CXMT, YMTC and SMIC subsidiaries.
**NEXUS-NAMED:** "★ 11/17 — for NEXUS: China's answer to the new US chip rule is a conditional threat, not a measure"; "★ 11/16 — for NEXUS: China's October home demand is still contracting"; "★ 11/11 — for NEXUS: the December Fed hike now priced (ORACLE: +25bp 85.5, +50bp or more 11.8) does NOT make China a forced Treasury seller."; "★ 11/06 — FOR NEXUS: the two-clock story is now one clock"; "★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed"; "🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired".
**STALE FLAGS:**
- ① Forward catalysts are "refreshed 2026-11-06". The Thu 11/19 Trump–Xi row and the ~Fri 11/20 NFRA/LPR row are past-dated with no outcome, and the Sat 11/7 SAFE row is unticked.
- ② The BIS Entity-List note was "Re-checked 11/2; next 11/9": past-dated.
- ③ Possible contradiction on V5: the status line says "V5b rescore (now 3) owed", while VIEW and catalysts say "V5 already 5". These may be distinct vectors.
- ④ The MIDAS row (Sep ≈23 t) is superseded by MIDAS's October +25.82 t (11/8).
- ⑤ The LIQUID and VULCAN waits date from 9/19 and are open-ended.

## SHADE
**HEADER:** "**As of:** 2026-11-20T12:05-05:00 | **STATUS commit:** `203df0459c` (PROME prome-77 wake D:L241)."
**VIEW:** 🟠 "Structural/latent insurer-wrapper stress; evidence remains partial." Composite 20/30. "current liquidity crisis, illiquidity breach and cohort cascade unproven."
**MOVED SINCE 11/17:**
- New row, DLIC Q3 statutory: inflows $1,557.7M (−60.3% YoY); funding agreements zero in Q2 and Q3; surrenders $1,137.9M (+68.1% YoY, +6.1% QoQ). "no run visible".
- Note 22: $3.8B swap approved 10/21, $2.7B settled to 11/16.
- DLIC repaid Soc Gen $303.5M for 1001CF.
- Second class action (Kalinsky).
- Catalina is majority Apollo-owned; FY2025 loss −$394.4M ⇒ "that FABN risk transfer stays in the Apollo family". D:L185 closed.
- 11/20 SVO count "UNAVAILABLE by design, not zero"; "0 ER in 8,567 designation cells". Projection (unscored): P(CY2026 ≥5) ≈ 25%.
- Added caveat: "⚠️ Moody's via secondary names Athene $2.4B xAI chip debt: obligor unsettled". Moody's industry figure: $85.2B life-insurer AI debt [6/30].
- SHD-02 HIT is in the commit subject only, not in the brief.
**CROSS-DOMAIN / CALIBRATION:**
- Sends to NEXUS, BROCK, LIQUID, REGINALD, VULCAN, SAM, CREED and RED.
- Unknowns: the bank distribution channel, the TWG asset marks, DLIC RBC after the exchange, and AAIA Q3.
- A hiking Fed "makes my trigger harder to fire" (INFERRED).
**FORWARD:** There is no forward section. Dates cited: falsifier F-SHADE-01 test 2027-03-31; FY2026 annual ~2027-03-01; SVO summary ~Spring 2027.
**NEXUS-NAMED:** Every SENDING row is addressed "NEXUS / …". For example: "**Delaware Life Q3: new business collapsed, no run visible; the cleanup trades affiliation for capital charges.**"
**STALE FLAGS:**
- ① The HY figures are 348 [11/5] and 331 [10/16].
- ② `T-SHADE-01` was last read on 11/6.
- ③ "Will now requests closeout" in the evidence paragraph is stale lifecycle text.
- ④ The DLIC and Group1001 rows overlap. Row 9 says "11/18 supersedes … (row 1)".

## GIBBS
**HEADER:** "**As of:** 2026-11-19 12:04 ET | STATUS commit: `140b247b37`"
**VIEW:** 🟡 The Q3 read is unchanged: deposit repricing is shared and CRE is mostly recognition. "Post-Q3 AI-infrastructure financings show the channel open and growing, not stressed." On the Fed FSR: "Attention is rising, not stress."
**MOVED SINCE 11/17:**
- WQ-692 RULED KEEP (11/16). This replaces the pending dormancy recommendation.
- JPMorgan: outage 11/16, vendor marketing-data exposure 11/19. These "move no read".
- Fed FSR: "largest BHCs close to $1T exposure" (KB-GIB-070).
- New prediction **GIB-01** (11/19): 70% that "no firm in the 16 attributes an allowance build or charge-off to non-bank or private-credit lending … through the Q4 prints and FY2026 10-Ks; Resolve_By 2027-03-15".
- HSBC US was sighted "as seller of a data-center loan at the mid-80s".
- The HBAN hand-off is dropped; HBAN "stays in its frozen cohort".
**CROSS-DOMAIN / CALIBRATION:**
- Sends to REGINALD, BROCK (NDFI, Goldman), LIQUID (custody deposits), CYPHER, PROME (unowned enforcement and foreign IHCs) and WALTER.
- Waits: REGINALD's Q4 cohort reads (mid-January 2027); CYPHER JPMorgan vendors 11/24 and R1 flip 11/20.
- Uncertain: the sector behind Goldman's provision, PNC's 60–89 day CRE bucket, the NII guides, and a late PHP2Shell victim.
**FORWARD:**
- 12/18: vendor-guidance comment file.
- 2027-01-13: Q4 print cluster.
- Watch the 10Y above 5.29%, the 9/30 mark.
**NEXUS-NAMED:** none.
**STALE FLAGS:** The CYPHER waits (11/20, 11/24) and the forward rows for 11/20 and 11/24 are past-dated with no outcome (As-of is 11/19).

---

## CROSS-BRIEF (≤10 lines)
1. **HY OAS.** LIQUID: 376 [11/20], 363 [11/23]. BROCK: 363 [11/23], "LIQUID's". Both say REG-T-04 FIRED, but LIQUID's own table still says "1 of 3". CARL (348bp [11/05]) and SHADE (348 [11/5]) carry stale prints.
2. **Fed FSR "close to $1T" and the FOMC October minutes on indirect lines to private-credit funds.** BROCK (KB-BRK-510/520) and GIBBS (KB-GIB-070) agree. Neither brief sizes it to a named bank.
3. **IREN / GPU Financing 2.0.** BROCK: Blue Owl funds $730.0M committed / $447.7M undrawn, draws end 12/31. LIQUID: "GPU 2.0's undrawn $1.5B runs through December 31". These are different perimeters, not reconciled. IREN fell −17.97% on 11/20 (LIQUID). SHADE: "no insurer established as a holder".
4. **Cable One.** BROCK and LIQUID agree: grace ~12/16; BROCK owns it.
5. **Car-Mart.** Only BROCK has the 11/24 Chapter 11. LIQUID's "Car-Mart current eligible cash/bank-risk bridge missing" predates the filing.
6. **10Y and real yields.** 10Y: BROCK 5.10 [11/12]; HOMER 5.07% [11/18]; GIBBS watch line 5.29%. Real 10Y: MIDAS 2.77% [11/20]. There is no common date.
7. **TIC and PBOC gold.** MIDAS cites ZHAO's −$80.9B with the +$27.6B coupon caveat; they agree. PBOC gold: ZHAO's "≈23 t Sep" is superseded by MIDAS's "+25.82 t" October.
8. **Oracle $2.4B at Athene.** LIQUID cites "Oracle $2.4B [SHADE's read]". SHADE now adds "Moody's … names Athene $2.4B xAI chip debt: obligor unsettled". LIQUID's line has not picked up that caveat.
9. **Unnamed thread A, mid-80s data-centre loan sales.** LIQUID: "an Oracle data-centre loan piece sold mid-80s" and the ING ~$500M auction short of bids. GIBBS: "HSBC US … seller of a data-center loan at the mid-80s". This may be one trade; neither brief links the two or names the buyers (SHADE's insurers and BROCK's BDCs are the candidate holders).
10. **Unnamed thread B, nonbank servicers.** HOMER: Fitch negative outlooks on Pennymac/Planet/Freedom; loanDepot. CARL: RITM GNMA 60+ 6.1%. BROCK: Car-Mart servicing moves to Cardinal, and "a servicer termination notice is the ABS risk (OTTO)". All three point at servicer credit; no brief names it as one channel.
