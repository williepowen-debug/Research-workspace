# REGINALD — WALTER wave 2: HY against 350, seven cards, Seacoast trigger, forward view

**Session:** 2026-11-19, from 12:00 ET (clock). PROME task letter prome-36 (Will's word 11:49 ET; addition 12:01 ET asking for a FORWARD VIEW). Claude Code, Opus 5.5 (claude-opus-5-5), laptop; session id not exposed (scratchpad 52cb3487). No pull (other desks' tracked files dirty: OSPREY, YURI); no push (PROME pushes).

**Boot read, in order:** root CLAUDE.md (harness-injected), AGENTS.md, USER.md, PROME/COMPLETION_SPEC.md, ORCHESTRATION_PLAYBOOK § Runtime mechanics, my CLAUDE.md (harness-injected), STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP (all whole). `market.py`, `vx_ladder_check.py` (rc 1, FLG RED unchanged), both staleness lines (clean), `boot.py` rc 2: insider and 8-K monitors TIMED OUT (~110 s each, not re-run; EDGAR read by hand below for the one filing I needed), corrections 0 owed, peer channels 0 entries, 10 predictions open, none past resolve-by.

## Bottom line

HY OAS printed **347 [11/18]** (FRED first-published, read 12:04 ET 11/19): REG-T-03 stays FIRED, **REG-T-04 NOT FIRED, run 0 of 3, 3bp short of 350**. The bank side still does not show it: the bank preferred basket fell 0.25% over the last three sessions and the two names that fell more than 2% over the longer window went ex-dividend on 11/13; IG moved +4bp; and **Pinnacle Bank sold $600M of 10-year subordinated notes at par at 7.200% on 11/18**, the same day HY printed 347. The flood trigger I wrote for Seacoast is **NOT MET**: its letter is a *federal* declaration with damage concentrated in Martin, Palm Beach or St. Lucie; none exists (OpenFEMA read 12:06 ET). Projection (labelled, below): about a 30% chance REG-T-04 fires by 12/11, registered as REG-36.

## 1. HY OAS against my lines (FRED `BAMLH0A0HYM2`, first-published via ALFRED `output_type=4`, read 12:04–12:05 ET 11/19)

| Series | 11/18 | 11/17 | 11/16 | 11/13 | 11/12 |
|---|---|---|---|---|---|
| HY OAS | **347** | 343 | 334 | 323 | 320 |
| CCC OAS (`BAMLH0A3HYC`) | **1,353** | 1,329 | 1,310 | 1,316 | 1,314 |
| B OAS (`BAMLH0A2HYB`) | 373 | 368 | 357 | 344 | 339 |
| IG OAS (`BAMLC0A0CM`) | 93 | 92 | 90 | 89 | 89 |
| HY minus IG | 254 | 251 | 244 | 234 | 231 |
| CCC/HY (my arithmetic) | **3.90×** | 3.87× | 3.92× | 4.07× | 4.11× |

The 11/11 bar (330) is the Veterans Day forward-fill: excluded and bridged (`registry/NOTES.md` § REG-T-03/04). These match LIQUID's figures in the task letter (347, CCC 1,353, HY minus IG 254) on my own read.

| My line | Letter (`registry/THRESHOLDS.tsv`) | State after the 11/18 print |
|---|---|---|
| `REG-T-03` | HY > 320 on 3 consecutive daily closes → CREDIT-CANARY-FIRED; exit HY ≤ 300 ×5 | **FIRED, held** (already fired; no re-fire). Fourth print above 320 in this run (323, 334, 343, 347; 11/12 at 320 is not above). Exit run 0 (347 is 47 above 300). |
| `REG-T-04` | HY > 350 on 3 consecutive daily closes → ISSUANCE-FREEZE (REGINALD, LIQUID, Will); exit ≤ 330 ×5 | **NOT FIRED, run 0 of 3.** 347 is 3bp below. Highest print in the window remains 348 [11/05]. The WQ-512 single-issuer rider runs only at a fire. Agrees with LIQUID's 0 of 3. |
| `REG-34` (25%, 11/05) | > 350 on 3 consecutive sessions, 11/05 to 12/29 | OPEN; no print above 350 yet. |
| `VX-REG-18.04` CCC/HY > 3.6× | HARD-FIRE; only a CCC-led re-cross escalates | **Still fired, NO escalation.** 11/17 → 11/18 was CCC-led for the day (CCC +24, HY +4; ratio 3.87 → 3.90), but the ratio never left the fired zone, so this is not a re-cross. B 373, above ORANGE 330 since 10/29 (watch row). |

**Bank-credit cross-check** (my standing rule; flip data from `reports/2026-07-30_bank-side-HY-attribution.md` §E). yfinance unadjusted closes; **ex-dividend dates checked this time** (yfinance actions): HBANM $0.356 and TFC-PR $0.297 went ex on 11/13; WAL $0.46 on 11/12; AMTB $0.09 on 11/13; USCB $0.125 on 11/16.

| Instrument | 11/13 → 11/18 (3 sessions) | 11/12 → 11/18 (4 sessions) | Flip datum | Met? |
|---|---|---|---|---|
| Bank preferred basket, same 10 names as 11/18 | **mean −0.25%**, none at or below −2% | mean −1.08% raw; HBANM −2.54% and TFC-PR −3.48% raw are mostly the 11/13 dividends (adjusted about −0.7% and −1.7%); basket about −0.7% adjusted | basket −2% or worse over 3 sessions while HY widens | **NO** |
| IG OAS | +4bp (89 → 93) | +4bp | +10bp or more, financials leading | **NO** |
| KRE vs SPY (settled; Nasdaq agrees for KRE) | KRE −3.05% vs SPY −3.20% | −2.76% vs −3.56% | (not a flip datum) | banks in line with the index |

**Read: BANK-ABSENT, unchanged.** The ex-dividend check resolves the 11/18 report's open caveat: two of the three preferred drops it flagged were dividends, not credit. ⚠️ Intraday 11/19 (~12:05 ET, vendor, not settled) KRE is −2.3% and SPY −1.5%: banks are lagging today for the first time in this window. One session, unsettled; noted, not graded.

**Counter-evidence to an issuance freeze, at the primary:** Pinnacle Bank (PNFP's bank subsidiary) issued **$600M of 7.200% fixed-to-floating subordinated bank notes due 1/15/2038**, fixed to 1/15/2037 then compounded SOFR + 2.53%, sold at par, net proceeds ~$594.4M, general corporate purposes (8-K Item 8.01 and EX-4.1, acc 0002082866-26-000098, filed 11/18, read at EDGAR 12:06 ET). A regional bank placed Tier 2 debt at size on the day HY printed 347. I did not read a comparison spread for prior regional sub-debt deals, so "7.2% is expensive or cheap" is not established here; 10Y was 5.10% [FRED DGS10 11/17], about 210bp under the coupon.

## 2. The cards (grades go to WALTER by packet)

| Card | What it is | Disposition | Why |
|---|---|---|---|
| **SIG-W-20261118-010** (ACTION) | HY 343, LIQUID's >320 ×3 MET | **INTEGRATED** | §1: REG-T-03 held, REG-T-04 0 of 3 on 347 [11/18]; cross-check BANK-ABSENT with ex-dividends checked |
| SIG-W-20261118-011 | Plaza Continental #128, NO-VERDICT on WAL's Nano lien | INFO_ONLY | Nano's shared figure (~$120M, ~17%) moves only on a sale print or the OIG; nothing here |
| SIG-W-20261118-013 | FOMC minutes, Oct 27–28 | **INTEGRATED** (KB ML-REG-315) | Read at the Fed page myself (HTTP 200, sha256 1d8f38d83c876c42…): "Several participants expressed concerns that the existing data available to bank supervisors may not fully capture banks' indirect exposure through nonbank financial institutions, including credit lines to private credit funds" and "almost all participants judged ... further action to raise the target range ... would likely be appropriate". combo:bank-lending-to-private-credit; the rate path is the channel that moves regionals (Q3 bond losses $485.7B system-wide, ML-REG-307) |
| SIG-W-20261119-001 | Claims 203K [w/e 11/14]; continuing 1,763K | INFO_ONLY | REG-T-05 (> 300K): 97K of room. FRED ICSA and CCSA read myself, match. LABOR grades |
| SIG-W-20261119-005 | Small items | **INTEGRATED** for two lines | Pinnacle $600M 7.200%: read at EDGAR (§1), KB ML-REG-314. ECB probe of bank–private-credit links: title only, EU, HANS grades; KB ML-REG-316 combo:bank-lending-to-private-credit. **Paraguay bank failure, losses up to $1B (central bank chief, via Barron's/AFP title):** outside my perimeter (no US bank linked in anything read), title only, no KB row, INFO_ONLY |
| SIG-W-20261119-008 | First Brands, Tricolor hearing dates | INFO_ONLY | Bank of America's role is ABL agent service, not a loss; no recovery figure until a ruling (First Brands D&O 12/15, Tricolor Chu 12/16) |
| SIG-W-20261119-009 | CYPHER grades | **INTEGRATED** (KB ML-REG-317) | combo:bank-vendor-breaches: TruStage extortion agreement (data review 6–8 more weeks), Wellington IT payee data at ~40–50 Irish credit unions (one vendor, many institutions, data not funds), JPMorgan vendors' marketing data. CYPHER owns grades; none touches a bank in my 14 |
| SIG-W-20261119-016 | FALCON Riyadh; GIBBS 14 grades | INFO_ONLY | GIBBS: no 8-K Item 1.05 at its 16 banks 11/16–19; vendors unnamed |
| General inbox: CYPHER packet 11/19 | Same vendor cluster, P1 JPMorgan by routing, P3 CU items | Filed with ML-REG-317 | No action asked; my 10/30 amendment makes CU-only items context |
| BOARD diff (not in my lane): -20261118-012 TIC, -20261118-015 VIX near-exit, -20261119-006 Car-Mart waiver to 11/22 | primary-cluster or FED cards | INFO_ONLY ×3 | No letter of mine; owners ZHAO, RED, BROCK |

## 3. Seacoast flood trigger and CORAL's finding

**My letter** (report 2026-11-18 §3, KB ML-REG-313, CALENDAR SBCF row): what would make the Seacoast exposure map material is "**a federal flood declaration** with damage concentrated in Martin, Palm Beach or St. Lucie", a Seacoast storm or flood provision or past-due rise at the Q4 release (~late Jan 2027), or residential or CRE 30–89 past dues up at the 12/31 Call Report. It is a watch line, not a registered trigger: no grade, gate or threshold hangs on it.

**Grade: NOT MET. CORAL's conclusion is right; its paraphrase drops one word.** CORAL wrote "a declaration with damage". My letter says *federal*. EO 26-232 (signed 11/18, 21 counties incl. Broward, Miami-Dade, Palm Beach, Martin, St. Lucie) is a **state** emergency: authority, not money, and not federal. OpenFEMA DisasterDeclarationsSummaries, Florida since 10/01, read by me 12:06 ET: only DR-4955 (Hurricane Isaias, 10/27, Panhandle counties) and EM-3655 (10/09); **no declaration for the November flooding and none naming Martin, Palm Beach or St. Lucie.** The damage leg also fails: CORAL found no damage or insured-loss count. So it fails on both legs. ⚠️ This week's rain fell hardest in Broward and Miami-Dade, which are outside Seacoast's five-county weight; Palm Beach had 5.9–10.6 inches (NWS preliminary, via CORAL).

**Are BKU, AMTB and USCB in my perimeter?**

| Bank | In my 14? | Matrix score [v2.0] | FL frame (frozen 9/24) |
|---|---|---|---|
| BKU (BankUnited, Miami Lakes) | **Yes** | 2 | Yes: MIXED final [11/06] |
| AMTB (Amerant, Coral Gables) | **Yes** | 5 (🟠; mostly non-CRE credit) | Yes: HOLDS final [11/06] |
| USCB (USCB Financial, Miami) | **No** | not scored | No; not on the WQ-624 side list (Preferred, NexBank). I can log it as context; scoring it needs Will's word |

Tape since 11/12 (settled 11/18): BKU −3.5%, AMTB −4.9%, USCB −2.3% (incl. ex-dividend 11/16), vs KRE −2.8%. Not a flood signal: the whole sector fell. First real read is Q4 provisions, late January.

## 4. Other tape (settled 11/18; Yahoo and Nasdaq agree)

WAL **$70.83** (REG-T-02 FIRED, exit 0 of 3, 56 rows; needs +15.63% to $81.90). KRE **$70.52** (REG-T-01 UN-FIRED, $10.52 above $60). FLG $10.26 (RED, 30 closes below $11.39, −27.9% vs frozen $14.24). Intraday 11/19 ~12:05 ET, vendor, not graded: WAL 69.06, KRE 68.93, FLG 10.01, VIX 24.91. KRE shares 56.80M (+0.28M) [11/19 monitor].

## 5. FORWARD VIEW — PROJECTION (my judgment; moves no score, band, gate or trade)

**Base rate first.** From an HY print between 340 and 350, three straight prints above 350 followed within 15 sessions 2 of 13 times (15%), within 28 sessions 3 of 12 (25%); FRED holds three years (11/2023 to 11/2026), overlapping windows, clustered, small n. REG-34 was registered at 25% from 332.

| Item | Base case | Main alternative | Dated tells | What it would mean |
|---|---|---|---|---|
| **HY vs 350 (REG-T-04)** | **~65%: HY chops between about 330 and 355 into mid-December; maybe one or two prints above 350, no run of three by 12/11.** Why: the widening is slowing (+11, +9, +4); HYG was flat today while stocks fell (vendor 12:05 ET, an inference about the 11/19 print); 348 has capped this cycle twice; a bank sold Tier 2 at par on 11/18 | **~30%: three straight above 350 by 12/11; REG-T-04 fires.** Why: four rising prints in a row, the whole ladder at the 94th–96th percentile, a hawkish Fed (minutes: "almost all" see more hikes, "a couple" open to more than 25bp on Dec 9), riskier firms refinancing under pressure (Fed staff). Tail ~5%: back under 320 by 12/11 | FRED HY prints from 11/20 (the 11/19 bar); two prints above 350 make it live; the Fed decision **Wed 12/9**; LIQUID's issuance read (deals pulled or not); any further bank sub-debt or preferred sold at par (a no-freeze tell) | A fire triggers the issuance-freeze consequence to LIQUID and Will, with the WQ-512 rider (I expect the named-issuer share to be small: the widening is in every tier). **For banks it means nothing on its own** unless the cross-check flips. Card: TERRY already holds LIQUID's `IDEA-HYG-FOLLOW-NOV05`; I add no card. Positions are Will's |
| **Bank-credit transmission** | **~75%: stays BANK-ABSENT through 12/11.** The selling is broad risk-off plus rates; bank capital markets are open (PNFP) | **~25%: the bank leg starts to lead.** Today's intraday KRE underperformance (−2.3% vs −1.5%) is the first sign of it in this window, one unsettled session | Preferred basket −2% over 3 sessions (dividend-adjusted); IG +10bp led by financials; a bank pulling a debt deal; KRE closing under SPY on several sessions; any Q4 pre-announcement by a name in my 14 | If it flips, the HY widening becomes partly bank credit for the first time this year: a REGINALD finding to TERRY and PROME the same day, and the concentrated-severity claim gets re-tested on prices, not quarters |
| **Rates channel** | **~60%: the 10Y stays at or above 5% through year-end and Q4 bond losses on bank books are as deep as Q3 or deeper** (Q3 $485.7B system-wide, ML-REG-307). AOCI cuts tangible book, not regulatory capital, for most banks | A December hike that brings the 10Y down (curve flattens) would ease the bond losses | 10Y daily (FRED DGS10); Dec 9 decision; 12/31 Call Reports (late Jan to Feb) | A vulnerability only if banks must sell bonds; no deposit run is visible (H.8 not re-read since 11/06) |
| **Florida floods and banks** | **~80%: no visible credit effect at BKU, AMTB or SBCF in Q4** (late Jan): small or no storm provisions | Residential or CRE 30–89 past dues rise at the 12/31 Call Report, or a named storm provision | OpenFEMA (a federal grant or an amended request adding South Florida; CORAL's window to ~12/07); Q4 releases ~late Jan; 12/31 Call Report | Even the alternative is a provision line, not a solvency issue: SBCF Q3 NCO 0.16%, Tier 1 ~14.1% |

**Registered:** `REG-36` (30%) — HY OAS prints above 350 on three consecutive sessions on FRED observations dated 2026-11-19 through 2026-12-11; resolve-by 2026-12-14 (CHOSEN). Row in `workbook/PREDICTIONS.tsv` and `registry/PREDICTION_RESOLVE_BY.tsv` in the same commit. It does not replace REG-34; my current view of REG-34 (to 12/29) would be about 35%, recorded here, not re-written into the 11/05 row.

## 6. Charter check (WQ-719 A, WQ-721 A)

My charter already reads brief-on-change only: SESSION CLOSE CHECKLIST bullet "**NEXUS brief, on change only (WQ-719 A, Will 2026-11-18)**", applied 11/18, and the FILES line "NEXUS_BRIEF: final full-schema fold after STATUS, only when its content changed (WQ-719 A)". Nothing says "every session" or "even no-change", so **no charter edit this session.** Pin check 12:09 ET: `OK-PINNED`, pin 76603c8747 = STATUS HEAD (not PIN-UNRESOLVED). The brief carries HY 343 and claims 200K, which changed, so it is **owed a rewrite at closeout** (held until PROME asks).

## 7. Gaps

- `boot.py` insider and 8-K monitors timed out (~110 s each); not re-run. Only the Pinnacle 8-K was read by hand.
- H.4.1 and H.8 since 11/06 still not read.
- Paraguay: title only; not read.
- No comparison spread for prior regional sub-debt deals; the Pinnacle coupon is a level, not a relative read.
- Laptop: Kalshi credentials, gh token and CourtListener token absent (PROME/MACHINE_LOCAL.md); none needed this session.
