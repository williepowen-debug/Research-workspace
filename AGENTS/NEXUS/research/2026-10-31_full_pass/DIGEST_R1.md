# DIGEST R1 — credit / banks / private credit / consumer briefs (9)

**Reader:** fresh-context read-only digest reader R1 (Claude Opus 5.5, Claude Code), spawned by NEXUS 2026-10-31. **Scope:** REGINALD, LIQUID, BROCK, OTTO, CARL, SHADE, WAL, FLG, GIBBS `NEXUS_BRIEF.md`, each read whole. **"MOVED" baseline:** NEXUS's last full read, 2026-10-26 23:39 ET (repo base `cf2c47fd9`). Figures are quoted from the briefs. Where a brief is stale or leaves out a load-bearing figure, the owner's STATUS line is quoted and labelled **[STATUS]**. Nothing in this file is a NEXUS grade.

## brief_pin_check.py (run from repo root, 2026-10-31)
Fleet line: `BRIEF-PIN 1 STALE: 31 brief(s) checked … OK-PINNED 15 · OK-SAME-COMMIT 14 · STALE-PIN 1 · UNPINNED 1`. My desks:
- ✅ BROCK OK-SAME-COMMIT d8970fd6b · ✅ CARL OK-PINNED 5dc1234ed · ✅ FLG OK-PINNED d61051aed · ✅ GIBBS OK-PINNED 6d1d9df51 · ✅ OTTO OK-PINNED e8d36c9f1 · ✅ REGINALD OK-PINNED a7d9d76ea · ✅ SHADE OK-SAME-COMMIT cf97c133c · ✅ WAL OK-PINNED 33bb4c4c9
- ⛔ **LIQUID STALE-PIN**: "pin ecf7b52a5 is 4 STATUS commit(s) behind HEAD 4edee7bbd". This is schema §4.4 trigger (a), so a raw-STATUS read is owed (summary under LIQUID below).
- A PASS proves the pin and nothing about the content. BROCK passes, but its brief still leaves out its own 10/29–10/30 grades (see BROCK).

Size: all nine are under the 32,550 B read cap. The largest is REGINALD at 22,806 B (70%). Form: LIQUID, SHADE and WAL do not use the schema section headers (CROSS-DOMAIN / VIEW / CALIBRATION); that is a BRIEFS_MAP order-cell matter, not load-bearing.

---

## REGINALD — regional banks, FHLB, CRE
**HEADER:** As of 2026-10-31 09:38 ET (PROME-spawned L857) | STATUS commit a7d9d76ea (= HEAD).
**VIEW:** "Concentrated bank risk." Severity is concentrated, not spread across the tier. "The 10-year (~5.0%), not HY, moves regionals." Problem loans rose at 7 of 10 names. The Florida books "hold on every read cell".
**MOVED since 10/26:**
- **L857 (10/31), FFIEC Q3, 134 of 139 banks:** frozen small universe ex-acquirers "cut borrowing −$5.70B net while deposits rose +$39.20B"; 51 of 127 increased. Santander +$10.70B is mostly inherited from Webster (pro forma +$6.72B). Six frozen-rule flags, all funding-mix shifts: Regions, Renasant, Simmons, The Bancorp (BaaS), Bank of Hawaii, Israel Discount NY. "No TERRY route." Four banks unfiled (East West, HSBC USA, First Hawaiian, Beacon). No score, threshold or probability change.
- **L801 (10/30): coverage-decline leg DROPPED as a predictor** (weight zero). DEWEY base rate: 2 of 10 episodes vs 25% of all quarters; ρ −0.06. **Problem-loan leg KEPT** (7 of 10 up [10/23]; ρ +0.46). Q3 Call Reports not at FDIC (0 rows, 10/30 09:09 ET). HY 314 [10/28]; CCC/HY 4.16×.
- **10/28 catch-up:** **REG-T-04 / DOCKET L818 NOT FIRED** (HY 338→330→318 [10/23–10/27]; BB/B lead the tightening). SBCF Q3: the FL 8-K cell HOLDS (2.90% vs ≥3.20%), NPL −15%, an unexplained $8.4M reserve on one acquired loan. Small-bank borrowings $316.4B SA [w/e 10/14], +11.8% in 6 weeks (97.5th pct), from a low level (4.55% of assets). "Not a run." The "'watch deposits' advice is retracted". Coastal holds ~$447M of Bluevine deposits [9/25] (~9%). FLG director bought 10,000 sh at $10.14 [10/27, Form 4]; FLG ladder RED −28.8%. **Correction:** the CFG $12.852B figure is March 31, not June 30.
- No new letter. Nano P&A still unposted [10/28 22:28 ET].
**CROSS-DOMAIN / CALIBRATION:** FHLB/funding goes to LIQUID as context. The FLG exit roll-forward is consumed from the FLG desk. CARL WQ-228 joins are accepted. NDFI is BROCK's; CMBS is CREED's (UNKNOWN). **Uncertain:** "(1) whether the bank-equity leg is now running AHEAD of credit (HY half-retraced while KRE/FLG/OZK kept falling)"; (2) CFG +$3.85B Q2 FHLB draw; (3) OZK causal share; (4) MI3 cohort rule before 11/07; (5) "whether the latest partial borrowing reversal persists".
**FORWARD:** 11/03 weekly Nano P&A re-check (L516). 11/05 FFIEC JWT renewal. **11/07 S1-vs-S2 ranking test / FFIEC Q3 run.** FDIC Q3 posting ~mid/late Nov (decides the frozen concentration verdict). FLG 10-Q ~11/6–9 (loss on exit). FL 10-Qs ~11/14. 11/13 FHLB CFR. REG-28/29/30 resolve Mar 2027.
**NEXUS-NAMED:** none addressed to NEXUS by name.
**FLAGS:** (i) **Stale HY vintage at a 10/31 fold.** The headline says "HY tightened to 314bp [10/28] … has partly reversed". The LIQUID and BROCK STATUS files carry **HY 326 [10/29]** (+12, every tier wider), which was published 10/30 ~10:53 ET, before this fold. (ii) WATCH / NEXT DECISION / Calibration-vintage text still refers to October 20–23 work and "credit observations still October19", which conflicts with the dated 10/28–10/31 blocks above it. (iii) The VIEW keeps "HY CREDIT-CANARY-FIRED" while the header says REG-T-04 "never" fired. These are different rungs, but a cold reader could misread them.

## LIQUID — funding, credit tiers, plumbing
**HEADER:** As of 2026-10-29T16:51:50-04:00 | STATUS commit ecf7b52a5 (**4 behind HEAD 4edee7bbd, 10/30 20:17 ET**).
**VIEW (brief):** "Mainly credit repricing; broad financing restriction is not established." The transmission map is incomplete, and "calm overnight funding does not clear" private or offshore channels.
**MOVED since 10/26 (brief):**
- HY 314, IG 86, BB 184, B 318, CCC 1,307 [10/28, FRED first-published]. Three straight days of tightening. CCC yield 17.73% [10/28] vs peak 18.17% [10/23].
- **>320 run ENDED at 9 cells; 318 [10/27] reset it to 0-of-3** (graded 10/29).
- **079 FIRE legs 3/4 banded under WQ-535 RULED A** (Will 10/29 00:26 ET). SOFR99−IORB +12bp [10/28]; NOT ARMED.
- **Swap-line SHELVED (WQ-534 RULED B, 10/29).**
- 076 MET 2 of 3 (W2 G5L10 −$1,861M [as-of 10/21], 59th-lowest of 616 weeks).
- 069 2-of-2 FIRED unchanged; L1 NOT MET (BB 184); L4 NOT FIRED. 072 QUIET.
- DTCC [10/28]: CRWV 5Y 956–995bp, ORCL 269–288, META 108–115 (eased from 121–127 [10/23]).
- XCCC composition: AI 0.0%, Tech 7.81%, Comm 16.98% [10/28/10/27].
- $63B Broadcom-supported Anthropic SPV: committed, not funded.
**MOVED since the brief [STATUS 4edee7bbd and earlier commits, trigger (a)]:**
- **HY 326 (+12), IG 89 (+3), BB 194 (+10), B 332 (+14), CCC 1,325 (+18) [10/29 first-published, pulled 10/30 10:53 ET].** "Every tier wider after three tightening days; each d/d at the 95th–99th percentile". Same day: GOOGL −12.6%, QQQ −1.4%.
- **WQ-545 call graded 10/30: "TRANSMISSION by the letter"** (HY ≥324, BB ≥189, VIX up). Caveat: "the widening rode the AI mega-cap equity repricing, not energy … n=1 session".
- **New >320 run 1-of-3** [326, 10/29]; earliest MET is the 11/2 cell.
- **10/30 intraday ETF proxies (15:38 ET vs 10/29 close, NOT spreads):** QQQ −3.86%, SPY −2.42%, KRE −1.24%, HYG −0.19%, JNK −0.25%, LQD −0.03%. VIX 21.99, MOVE 100.12. "credit ETFs lag the equity move intraday."
- **DTCC 10/30:** ORCL 5Y disseminated 293 (+10–18bp; equity −6.37%). CRWV 5Y NOT PRINTED; CRWV 4Y ≈+46bp (equity −9.66%). "Wider with equity, not leading; n=1."
- 076 **W1 NOT MET** [as-of 10/27, CFTC]: −2,535,985, w/w −162,945 is a build. W3 not met 10/30 (VIX ≥20).
- H.4.1 reserves $2,893.770B (−$68.8B w/w, TGA-linked) [week 10/28].
- CHK-40 stablecoin/Binance: "NO PLUMBING CONSEQUENCE MEASURED".
- **Hubbard ($15B Anthropic-leased data-centre loan): banks shelved the $5–7B HY bond and kept the bridge** (Bloomberg 10/28 headline only, body not read), described as "a stuck-distribution tell". Amazon 10-Q adds a secured supplier facility of up to ~$80B.
**CROSS-DOMAIN / CALIBRATION:** BROCK owns the X1 wrapper half; REGINALD owns REG-T-04 (LIQUID witness 0 of 3); VIOLET governs MOVE/VIX; ORACLE owns odds; HANS: TTF >€100 [10/28], settle not established; "EUR→USD funding unmeasured on both desks". **Uncertain / unmeasured:** haircuts, collateral calls, prime-broker limits, sponsored repo, offshore dollars; "Tier spreads are not issuer breadth"; matched bank-line draws, funding refusal and named cash restrictions "remain missing".
**FORWARD:** **11/2 ~10:3x ET: FRED ICE 10/30 cells** (decide >320 run 2-of-3, 069 L1/L4, 072). 11/2 ~20:15 ET: DTCC CRWV 5Y. 10/28–11/3 is calendar-excluded for 079. **11/05 PROME review of 069/076/079.** 11/13 BDC pre-registration. 11/30 L799 GENIUS Act.
**NEXUS-NAMED:** "NEXUS receiver consumption remains separate from this fold." 076 letter file is `workbook/DEALER_POSITIONING_NEXUS_WATCH.md`.
**FLAGS:** **STALE-PIN (4 commits).** The brief leaves out the 10/29 widening, the WQ-545 TRANSMISSION call and the 10/30 CDS read. These are load-bearing for the selloff question. A `brief_fallback_log` row with cause `stale` is owed.

## BROCK — BDCs / private credit
**HEADER:** As of 2026-10-31T09:46-04:00 (R2 review session) | STATUS commit given as a pointer ("the 2026-10-31 BROCK commit (`git log -1 …`)"); the checker resolves it to d8970fd6b. Convergence 58/70, rescore 9/25, unchanged.
**VIEW:** "🔴 STAGE 2→3 — substance firming; bank transmission unconfirmed; X1 NOT MET, wrapper NOT ARMED." "Substance is firmer than established transmission."
**MOVED since 10/26:**
- **GATE-BRK-R2 review HELD 10/31.** North Haven Q3 FINAL 43.7% (filed 10/26) and OCIC Q3 final 29.8% mean (b) <25% is NOT FIRED on either. (a) stays FIRED ×2 (one wave). **"latch" rule P13 PROPOSED.**
- 10/28 (KB-393–404): **ARCC Q3 software guide NOT MET** (FV/cost 0.946, <80 share 7.4%). **BRK-22 RESOLVED FALSE ($0.48 held).** ARCC buys MFIC at ~75% of NAV (84.6% with adviser cash).
- **39-name BDC NAV discount median 28.68% [10/30 closes over mostly 6/30 NAVs, KB-BRK-412]**; "no trend claimed".
- 🆕 SEC v. SQN Capital (settled 10/8) is a BRK-26 CANDIDATE pending RED; not graded.
**MOVED but missing from the brief [STATUS]:** "**BRK-10 ❌ RESOLVED-FALSE 10/29**" (HTGC NAV $11.90 → $12.15 → $12.26). Software-marks row: "ARCC guide NOT MET (10/28) + **HTGC falsifier FAILS-for-Q3 (10/29)** = two bellwether non-confirmations … ⇒ no rescore". **CABO L795 graded 10/30:** "MBI NOT CLOSED", TRO hearing adjourned to 11/13 (press-only), Q3 10-Q 11/05 AMC. STATUS shows "HY 326 [10/29]".
**CROSS-DOMAIN / CALIBRATION:**
- CRMT eighth bridge: $5.0M new money SENIOR to ~$305.6M; relief/STD Sun 11/01; this is a PC-to-subprime-consumer case.
- WQ524 First Brands → WAL accepted (L840).
- CFG date correction ($12.852B = 3/31; 6/30 = $14.727B) goes to REGINALD/GIBBS. JPM call shows "generic wholesale build … without PC attribution".
- CCC/BB rose 5.96→6.57 [10/1→10/20] but "DOES NOT arm X1".
- **Uncertain:** OTF denominator; "HTGC/GBDC current funding squeeze is not established"; per-name draw amounts UNKNOWN.
- Fitch PCDR 6.3% is "a record BY CONSTRUCTION".
**FORWARD:**
- 11/02 AM: CRMT post-STD (ninth bridge / waiver / acceleration / bankruptcy decides the case).
- 11/04–05: BXSL / OBDC / FSK Q3.
- 11/05: CABO Q3.
- 11/05–18: SHADE joint X1 reconcile (L185).
- 11/16: 10-Q deadline / proposed R2 review.
- 11/17: GBDC.
- ~mid-Nov: BCRED 10-Q.
- **~12/03: BCRED Q4 letter** (a third sub-100% FIRES R2 (a) at BCRED).
**NEXUS-NAMED:** SENDING rows addressed "NEXUS / PROME", "NEXUS / LIQUID / TERRY", "NEXUS / LIQUID" (CRMT, six-SOI follow-ups, CABO). Footer: "NEXUS consumption remains unverified."
**FLAGS:** **Internal contradiction / brief-gap.** The 10/31 brief still lists "HTGC 10/29" as forward, WAITING and NEXT DECISION, and CABO "Next weekly read 10/30". STATUS has already graded both (BRK-10 FALSE; CABO NOT CLOSED). The footer cites "final STATUS commit 84e7a03c1", which does not match the d8970fd6b pin. The HY figure "340 [FRED 10/22]" in the CCC/BB row is a stale vintage.

## OTTO — auto fraud / subprime collateral
**HEADER:** As of 2026-10-28 22:35 ET | STATUS commit e8d36c9f11f4… (= HEAD).
**VIEW:** "🔴🔴 fraud/recovery losses; both systemic-transmission legs DISCONFIRMED." Convergence 33/50, "21 points from one root".
**MOVED since 10/26:**
- **s040 (10/28):** the Carvana Q3 10-Q says the SEC closed its short-report investigation (Sep-2026) with no enforcement recommendation. "the registered Carvana −40% risk-row condition appears met and is applied at v1.6 10/30 (no score moved yet)". Finance GPU $2,733 (+$67 QoQ, −$307 YoY).
- Court sweep 10/28: Tricolor BlackRock Rule 2004 GRANTED; FB §721 continued to 11/17; FB DIP cash-sweep stipulation opposed. OTTO-33 stays 60%.
- No probability, colour, threshold or score change.
**CROSS-DOMAIN / CALIBRATION:** Bridgecrest D spread +30bp, yield +89.6bp Jul–Oct; Exeter D flat. Car-Mart bridge 8 runs to 11/01 and is "not maturity/automatic bankruptcy". "BROCK/LIQUID company constraints are not proof of lender-bank propagation." "search coverage of the last week was thin, so this is not evidence of absence." Brier 0.276875 vs constant 0.25: "No demonstrated forecasting edge."
**FORWARD:** Exeter ~10/29; **THESIS v1.6 10/30**; CRMT 11/01; FB status conference 11/02; Chu ruling 11/04; NY Fed window 11/04–11/12; M&T ~11/05; Manheim 11/06; Tricolor §341 11/11; SDT ~11/15; FB §721 11/17.
**NEXUS-NAMED:** "NEXUS · PROME | L708 remains NO_INSTRUMENT"; NEXUS is a recipient on rows s039, s037, Edmunds, Ally, Exeter panel, WQ524.
**FLAGS:** **THESIS v1.6 (dated 10/30) shows no OTTO commit.** OTTO's last own commit is 10/28; the 10/29 commit is an inbound DEWEY packet. The v1.6 that applies the Carvana risk row is therefore **overdue / not run**, and the brief reads as if it is pending. Exeter ~10/29 is not reflected.

## CARL — U.S. consumer
**HEADER:** As of 2026-10-29 09:36 ET | STATUS commit 5dc1234ed (= HEAD).
**VIEW:** "🔴 v2.6.6 — concentrated household strain; broad spending collapse remains unestablished." Score 53/70.
**MOVED since 10/26:**
- **10/29 BEA [first print]:** September real PCE +0.015%, real DPI −0.27%, **saving rate 3.8% (lowest since Oct 2022)**, Q3 real PCE +3.8% SAAR. "no letter fired".
- **New letter CRL-32 (WQ-537, Will 10/29) at 25%:** saving ≤3.8% at the Oct (11/25) and Nov (12/23) prints, plus Nov real DPI ≤ Sep.
- 10/28 catch-up: Conference Board Oct 91.7 (+7.5); EIA regular $4.269 (−1.5¢) vs diesel $6.352 (+7.6¢, 3rd rise) [10/26]; CCC−B 999bp vs 962 [10/16]; FOMC hold 10–2 (V12 0 of 2).
- Paper rows CLOSED 10/28 (+$313.57 paper).
- CRL-13 re-dated to Q1 2027. GIG-P02/03/04/06 closed NO-VERDICT; POP-P03 MISSED; DOC-P11/P12 registered.
**CROSS-DOMAIN / CALIBRATION:** ALLY retail-auto NCO 1.89% (+32bp QoQ, +1bp YoY); RITM GNMA 60+ DQ 5.8→6.1%; PNC card spend +6.1% YoY. "Corporate credit quality is splitting … while broad HY tightens". **Uncertain:** matched ALLY vintage losses; saving composition; student-loan cure share.
**FORWARD:** 11/03–04 EIA / FOMC transcript (V12). 11/05 Sweet v. McMahon. 11/06 payrolls (V16) / ALLY-RITM. 11/10 CPI. ~11/13–16 MOHELA (CRL-28). 11/13 COF/BFH. 11/23 AFT v. ED. **11/25 October PCE (CRL-32 leg 1)**; 12/10 DFA; 12/23 final grade.
**NEXUS-NAMED:** SENDING rows "NEXUS / RED / REGINALD", "NEXUS / RED", "NEXUS / REGINALD" ×3, "WALTER / NEXUS", "PROME / NEXUS" ×2, "NEXUS / ISHM / FERT".
**FLAGS:** **Internal contradiction.** The header records the 10/29 BEA grade, but VIEW ("The 10/29 GDP/PCE release is the next aggregate real-spending read; prep card saved"), NEXT DECISION ("When: 10/29 08:30 ET") and FORWARD (~10/29 EART, 10/30 WQ228) are pre-print residue. CARL has no brief data after the 10/30 selloff. A PROME packet (10/31 09:27) about an unlogged BOARD signal is pending at CARL.

## SHADE — PE-owned insurers
**HEADER:** As of 2026-10-29T07:43:20-04:00 | STATUS commit: "same commit as this fold" (cf97c133c).
**VIEW:** "🟠 Structural/latent insurer-wrapper stress; evidence remains partial." Composite 20/30. Vector #1 DLIC is single-name FIRING.
**MOVED since 10/26 (10/29, prome-92):** "DLIC FY25 illiquidity NOT RED (FLOOR 9.75%, CEILING 28.68%; rests on the L1 agency category rule — INDETERMINATE without it)". SHADE-R v1: DLIC 321.9% / AAIA 2,460.4%. SHADE-T v1: DLIC 1.62% / AAIA 4,452.3%. These are "Diagnostics only, no band, never TSR." "FHCF/Citizens bonds $0 at both insurers (CORAL L784)." Key Ratios #2/#4 are now Will-ruled letter. No score or threshold moved.
**CROSS-DOMAIN / CALIBRATION:** AHL AI-infra contingent guarantee (15% of WHCO obligation, base unknown) → BROCK/VULCAN. Apollo FHLB $27.7B drawn / $33.8B total, "not cash" → LIQUID/REGINALD. **T-SHADE-01 NOT MET [10/15]** ("managers led … multiple compression"); the 10/10 fire is still PROVISIONAL. "HY 331 [10/16] … is LIQUID's/RED's/REGINALD's instrument, not a SHADE trigger." **Uncertain:** Group1001 flows, actual AG55 submissions, TSR UNAVAILABLE.
**FORWARD:** No dated catalyst in the brief. BROCK's brief carries the SHADE joint X1 reconcile, L185 11/05–18.
**NEXUS-NAMED:** "NEXUS / BROCK / VULCAN", "NEXUS / BROCK / REGINALD", "PROME / NEXUS / BROCK", "NEXUS / LIQUID / REGINALD", "NEXUS / BROCK / LIQUID", "NEXUS / BROCK", "NEXUS / CREED / REGINALD".
**FLAGS:** No schema section headers, and no FORWARD section. "28.68%" appears as the DLIC illiquidity CEILING. It is unrelated to BROCK's 28.68% BDC NAV discount: same digits, different objects. Do not cross-cite either figure as the other.

## WAL — Western Alliance (single name)
**HEADER:** As of October 30 2026 17:4x ET | STATUS commit 33bb4c4c9 (= HEAD).
**VIEW:** "Q3 runs against the credit bear and slightly against the bull's NII engine." **v2.5 (10/30): Bear-fast 2 / Bear-medium 12 / Base 49 / Bull 30 / Tail 7; EV $76.60** (v2.4 was 2/16/45/30/7, EV $75.96).
**MOVED since 10/26:**
- **Q3 10-Q filed 10/30 16:38 ET, graded.** "$99M life-science loan: NO-VERDICT" (absent from all four documents; kill leg (b) open).
- **WAL-01 RESOLVED-INVALIDATED final** (926 + 165 = 1,091 ≥ 272.75). **WAL-02 10-Q-confirmed 30bps** (INVALIDATED).
- OREO 22→27 properties.
- Hotel franchise criticized $75M→$185M (nonaccrual $0).
- Cantor NARROWED.
- Dividend $0.46 (from $0.42); preferred reset 8.36% (from 4.25%).
- WQ-553 Amendment 1 ruled 10/30.
- NDFI: First Eagle PC Fund SPV **$100M commitment** (8-K 10/5), the second PC SPV joinder in two weeks.
- Ratings baseline: Baa3/BBB/BBB+/BBB(high), all Stable. Lead only: Moody's "capital below 11.0%" vs CET1 10.9% preliminary.
- Short interest 6.35M = 5.82% [10/15].
- Deposits $81.8B flat; $4.5B moved off balance sheet.
- **10/30 close $76.29** (−0.40% vs EV). [STATUS: −1.94% d/d; KRE $72.01 −1.17%.]
**CROSS-DOMAIN / CALIBRATION:** Funding, cohort and price guards are REGINALD's; Carvana auditor-nexus rows were corrected 10/30. Composite 13/25 is "not yet re-judged". "⚠️ The trim reflects the 10-Q's silence plus the print evidence, not a resolved $99M."
**FORWARD:** Q3 Call Report / MI3 retry from Sat 10/31, before the JWT expires Thu 11/5. REGINALD cohort screen 11/7. 11/30 Makhijani (unverified). **12/9 §523 hearing.**
**NEXUS-NAMED:** none.
**FLAGS:** The "What Q3 showed" table still reads "INVALIDATED (10-Q confirm pending)" and "PENDING-10-Q". The status line above it supersedes both. This is internal residue, labelled by date.

## FLG — Flagstar (single name) — **NEW BRIEF** (first fold 10/28 under WQ-520)
**HEADER:** As of 2026-10-28 23:08 ET | STATUS commit d61051aed (= HEAD).
**VIEW:** "FLG's $2.8B non-accrual book carries a 5.8% specific reserve and exits only through an outside refinance market."
- ACL $869M flat. Non-accrual $2,817M. Coverage 30.85% (derived; series low).
- $1,571M carries no allowance.
- Exits 87.5% payoff/disposition, 1.6% cure.
- ~$216M Q3 buyback; CET1 13.16%→12.38%.
- 2027 MF wall $8,503M.
**MOVED since 10/26:** The whole brief is new. Notable items: the SR 07-1 Q2 figure of 327.52% was CDR-verified 10/28 (KB-098), and a Q3 buyback adds ~+7pp (ESTIMATE). "FLG RED [10/23]".
**CROSS-DOMAIN / CALIBRATION:** The roll-forward goes to REGINALD (no peer base rate: Y-14Q is non-public). The 2027 rent-regulated reset of $8.4B incl. $2.9B goes to CREED. **Uncertain:** "who finances the buyers of exiting loans"; par-basis loss at exit; the freeze ruling. Kill leg K-3 is "UNSET … no falsifier is held there".
**FORWARD:** **10-Q ~Nov 6–9** (FLG-02 coverage <31.04% at 65%; FLG-03 MF HFI <$26,931M at 88%; FDM T-13 deadline Nov 13). **Call Report ~Nov 14** (SR 07-1 vs 300%). Rent-freeze ruling by Dec 31.
**NEXUS-NAMED:** "NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (Q3 release, derived) is a series low; specific reserve 5.8% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision".
**FLAGS:** None. The brief is event-driven and fresh to its STATUS.

## GIBBS — 16 large banks
**HEADER:** As of 2026-10-23 08:44 ET | STATUS commit 6d1d9df51 (= HEAD).
**VIEW:** "Q3 large-bank read complete (16/16)". Deposit cost rose industry-wide (+2 to +11bp at 10 banks); PNC CRE and GS impairment are the exceptions; "Not a large-bank stress break"; "no transmission measured where disclosed" on NDFI.
**MOVED since 10/26:** **Nothing.** The brief and STATUS are both unchanged since 10/23.
**CROSS-DOMAIN / CALIBRATION:** GS $368M unattributed wholesale impairment → BROCK. Custody deposits down (NTRS, BNY) → LIQUID. AXP OCC $350M penalty → PROME. **Uncertain:** GS attribution; PNC CRE trajectory. "KBW Bank Index six-week large-bank-led decline … is not explained by these fundamentals".
**FORWARD:** Q3 10-Qs ~11/06 (19 UNAVAILABLE slots; an NDFI attribution of GS moves Q2 toward transmission). Perimeter re-cut 11/14. R0 review 11/15.
**NEXUS-NAMED:** none.
**FLAGS:** Pinned and pass, but 8 days old with no post-selloff read. Still dormant-fresh.

---

## CROSS-BRIEF (instruments cited by ≥2 desks)
1. **HY OAS vintage split:**
   - REGINALD brief (10/31): 314 [10/28].
   - LIQUID brief: 314 [10/28].
   - LIQUID STATUS and BROCK STATUS: **326 [10/29]**.
   - CARL: 318 [10/27].
   - BROCK brief row: 340 [10/22].
   - Same series and basis, different dates. Only LIQUID STATUS carries the widening day.
2. **CCC dispersion:** CARL CCC−B 999bp [10/27]; LIQUID CCC−B 989 [10/28] → 993 [10/29]. REGINALD CCC/HY 4.16× [10/28], calls it a "denominator artifact".
3. **WQ524 First Brands → WAL $126.4M** (LIQUID, BROCK, OTTO; WAL silent): consistent.
4. **CRMT bridge 8 / 11/01 STD** (BROCK, LIQUID, OTTO): consistent. BROCK grades the case.
5. **CFG $12.852B = 3/31:** REGINALD and BROCK agree after the correction.
6. **FLG exits 87.5% / cure 1.6% / $1,571M without allowance:** REGINALD and FLG agree. FLG 10-Q ~Nov 6–9 in both.
7. **11/5–11/7 FFIEC JWT / MI3 / cohort screen:** WAL, REGINALD, FLG.
8. **"28.68%"** is a BROCK BDC NAV discount and also SHADE's DLIC illiquidity ceiling. The digits match by coincidence.

**Unnamed threads:**
- (a) **WAL's PC-SPV joinders** (Crestline 9/18, First Eagle $100M 10/1) are a bank→private-credit exposure edge that BROCK's NDFI lane does not list. GIBBS's GS impairment and FLG's "who finances the buyers" are the same open question about bank lines to nonbanks.
- (b) **REGINALD uncertainty #1** (bank equity running ahead of credit) and **LIQUID's 10/29–10/30 cells** (credit wider *with* AI equity, ETFs lagging) describe one tape question. Neither brief cites the other's figure.

## FOCUS QUESTION: did the 10/30 selloff transmit?
Partly, into spreads only, on one day, and in step with equity rather than ahead of it. Nothing beyond that shows yet.
1. **Credit spreads:** LIQUID [STATUS] HY 326 (+12), BB 194 (+10), IG 89 (+3) [10/29 first-published]. That is "TRANSMISSION by the letter" (WQ-545), but "rode the AI mega-cap equity repricing … n=1". On 10/30 ORCL 5Y CDS was +10–18bp (293 disseminated), with "Wider with equity, not leading".
2. **The 10/30 day itself is unmeasured in OAS:** ETF proxies at 15:38 ET read HYG −0.19%, LQD −0.03% vs QQQ −3.86%. The FRED 10/30 cells (next read 11/2) decide >320 run 2-of-3.
3. **Bank funding, private credit, consumer credit:** no post-10/30 evidence. SOFR99−IORB +12bp [10/28], 079 NOT ARMED. KRE −1.17% [10/30, WAL STATUS]. REGINALD's latest HY cell is 10/28. BROCK only adds a 28.68% BDC discount [10/30] with no trend. CARL, OTTO, SHADE and GIBBS all predate 10/30.
4. Read: **contained beyond spreads, but not yet verified.**
