# NEXUS pass record: L554 weekly wake, L850 rollup #7, L1189 WQ-712 answer

**Written:** 2026-11-25T00:29:43-05:00 (from `date`). **Wake:** PROME prome-77 on DOCKET L554 (due Tue 11/24, not run: the machine was off about 25 hours), L850 (rollup #7, rides L554) and L1189 (WQ-712 re-ask). **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop, spawned by PROME (cwd inherited from `PROME/`). **Tier:** HEAVY (STATUS rule-5 rotation of two header paragraphs, so 15a cold read on STATUS) plus 9a.

## 0. Boot receipt

| Step | Result |
|---|---|
| Explicit reads (bounded reader, to `eof: true`) | root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/NEXUS/CLAUDE.md` 6 · `PROME/COMPLETION_SPEC.md` 4. No NEXUS `AGENTS.md` exists |
| 0a read-cap | rc 0. STATUS 24,325 B = 74.7% (87 B to the trigger): rotated this pass before the write (§H34). LAST_COMPLETION 73%, brief_fallback_log 73%, PREDICTIONS 72%, BRIEFS_MAP 70%: not fresh rotations |
| 0b self-letter audit | resolvers present: DOCKET L554, L850, L1100 (PRED-41), L1218 (PRED-51), L1219 (PRED-52); both NEXUS gates RESOLVED at PROME. No letter text changed |
| 1–3 | STATUS, LAST_COMPLETION, CONFIRMED (not re-analysed), PREDICTIONS_MONITOR whole. Past-trigger items: none (PRED-52's first week, w/e 11/21, prints Wed 11/25) |
| 4 / 7 inbox | 31 files, every sender: HOMER CORRECTION (info-only) + 30 WALTER cards (12 acted, 15 noted, 3 info-only), one `board_log.tsv` row each, all moved to `processed/` |
| 7a corrections | rc 1 at boot (6 named, all WALTER self-corrections) → six NO-OP receipts (no live NEXUS surface carried the corrected claims) → rc 0 |
| 6 briefs | 31 briefs; 28 moved since dcdaa06bce (11/17 17:05 ET); FLG, MARCO, WAL unmoved; HAWK excluded (no cross-war question). Three fresh-context Opus read-only digest readers (10/9/8 briefs), all returned → `digest/`. Owner artifacts read directly: REGINALD, LIQUID, HENRY, VULCAN STATUS heads; LIQUID's D:L1252 packet row for the mid-80s sale |
| Pin check | `brief_pin_check.py` rc 0: 31 briefs, OK-PINNED 21 · OK-SAME-COMMIT 7 · STALE-PIN 1 (FLG, 1 commit, advisory) · UNPINNED 2 (BROCK, RED) |

## 1. Data, pulled by NEXUS 2026-11-25 00:23 ET (FRED first-published) and 00:24 ET (vendor closes 11/24)

| Series | 11/17 | 11/18 | 11/19 | 11/20 | 11/23 |
|---|---|---|---|---|---|
| HY OAS (bp) | 343 | 347 | 352 | **376** | **363** |
| IG OAS | 92 | 93 | 94 | **98** | 97 |
| BB / B / CCC | 204 / 368 / 1,329 | 205 / 373 / 1,353 | 210 / 380 / 1,361 | 229 / 408 / 1,402 | 219 / 393 / 1,387 |
| DGS10 / DFII10 (%) | 5.10 / 2.89 | 5.07 / 2.88 | 5.04 / 2.88 | 4.92 / 2.77 | 4.92 / 2.79 |
| VIXCLS | 25.46 | 24.56 | 28.44 | **35.89** | 26.62 |

Initial claims 203,000 [w/e 11/14, first print]. Vendor closes 11/24: SPY $718.78 (−0.49%), RSP +0.54%, SMH −7.26%, NVDA $155.38 (−5.86%), TSM −3.96%, KRE $69.76 (+0.32%), HYG $76.43 (−0.12%), GLD $325.45 (−2.27%), ^VIX 26.36, CRMT $0.33 (−53.52%). S&P 500: 6,910.39 [11/20], 7,237.17 [11/23, FRED via HENRY], 7,201.09 [11/24 vendor]. 11/24 FRED cells not posted.

## 2. Convergence read: the three cross-desk links that matter now

**Link 1. AI repricing reaches financing at the AI-infrastructure edge (R4 into R3), not the market as a whole.**
- Evidence: NVDA −14.01% [11/20] on a Reuters report of SEC enforcement-staff scrutiny of its accounting (claim; no order, subpoena or Wells notice in any page read, VULCAN), then +32.87% intraday [11/23] on the 8-K reinstating Huang; SOX −7.88% [11/24] (AMD's 336.9M-share resale registration, memory scarcity at Ambarella); Asia 11/25 intraday Kospi −5.8%, SoftBank −14.4% (WALTER 20261125-001, not closes). Credit: LIQUID GATE-LIQ-069 L4 FIRED (IREN −17.97%, APLD −17.81%, NBIS −16.11% with HY +24 [11/20]); GATE-LIQ-072 leg 2 FIRED (IG 98 [11/20], first above 94 since 7/9); CoreWeave 5Y CDS about 1,314 bp [11/24 DTCC] from 1,078 [11/18]. Refusals: UST Global $400M loan pulled 11/16; ING about $500M data-centre loans short of bids 11/20; **an HSBC $300M piece of an Oracle New Mexico data-centre loan sold in the mid-80s 11/16** (Bloomberg via Weekender, secondary; LIQUID's D:L1252 table row, and GIBBS's brief names HSBC US as the seller: two desks, one sale, neither joined it).
- Not shown: a primary document for the mid-80s sale (price, buyer); any AI capex cut (VULCAN 15/25, S1 not fired); US HY weekly volume (paywalled); that the 376 print is AI-caused (REGINALD: BB +14 of the index's +16 bp 11/18→11/23; HENRY: the HY trend began 9/21, two weeks before the S&P peak, so it has its own clock).
- Forward view (unscored, no row): I expect the stress to stay concentrated in AI-infrastructure borrowers and the bottom tier through LIQUID's issuance test (week of 11/30–12/04) and Nvidia's 10-Q deadline (12/04 by VULCAN's arithmetic, 12/09 with a 12b-25), about 65%. Alternative, about 35%: it broadens, a mainstream HY or IG deal is pulled outside AI and weak credit. Horizon: to the 12/09 FOMC. What would change my mind: a pulled mainstream deal in LIQUID's test week; a primary filing showing a bank sold data-centre loans at 90 or under to a nonbank (that would also meet PRED-24's second condition); a late or restated Nvidia 10-Q.

**Link 2. The bond bid came back while the Fed leans hawkish; gold is not hedging.**
- Evidence: DGS10 5.10 → 4.92 and DFII10 2.89 → 2.77 [11/17 → 11/20], held 4.92 / 2.79 [11/23]; RED-FT-11 precondition MET at FRED (30Y −16 bp 11/13 → 11/20) with FUNDAMENTAL legs (2Y −25 bp, 10Y breakeven −9 bp), no weight; RED graded it FUNDAMENTAL at 00:30 ET 11/25 (S69, D:L1242), read at the 9c re-scan. Fed: Williams 11/23 "the risk to achieving price stability is dialed up", "still work to do"; Cook says she dissented for a hike in October. December pricing is ORACLE's (Polymarket +25 bp 92.5 [11/18]). Gold sold with stocks as real yields fell: GLD −3.67% [11/20] (MIDAS residual −5.35%, largest on file), −2.27% [11/24].
- Reading: falling real yields and breakevens are a growth scare in the bond market; the Fed's words point the other way. That is the widest narrative gap on the board, and it reverses my 11/17 note ("no bond bid").
- Not shown: whether the rally is flight to quality or a growth repricing (RED's classifier says FUNDAMENTAL, no weight); gold tonnes after 11/17 (the issuer archive refuses automation, MIDAS).
- Forward view (unscored): the 10Y holds under 5.00 into the 12/04 payrolls, about 60%. Alternative: a hot PCE (11/25 08:30) or a hike signal takes the bid away while spreads stay wide; that is the worse mix for credit (higher real yields with wider spreads). Horizon 12/09–12/10 (FOMC, CPI). What would change my mind: DFII10 back at or over 2.90 with HY at or over 376.

**Link 3. Credit stress has not reached banks; Car-Mart and Florida are named-issuer and local events.**
- Evidence: REGINALD's REG-T-04 FIRED on 352 / 376 / 363 [11/19, 11/20, 11/23] (consequence ISSUANCE-FREEZE); LIQUID's read of it: "NOT A FREEZE, SELECTIVE"; REGINALD's bank cross-check BANK-ABSENT (KRE −1.39% vs SPY −1.08%, 11/18 → 11/23; KRE 69.54 [11/23] → 69.76 [11/24]); its WQ-512 rider: the fire does not rest on named issuers (INFERRED; Car-Mart has no bonds in HYG). Car-Mart prepack Chapter 11 11/24 (8-K): $311.6M private-lender debt accelerated and stayed, $60M DIP plus up to $65M roll-up, ACMAT ABS trusts not debtors; BROCK BRK-33 resolved TRUE. Florida: St. Johns at Cocoa record 18.77 ft [11/21]; a federal major-disaster declaration REPORTED 11/24 (Sen. Scott, local TV) but not in OpenFEMA at 04:22Z 11/25 (HOMER, CORAL; REGINALD found none at 22:32 ET 11/24); Seacoast holds 12.4% of its deposits in the basin (REGINALD, a map, not a loss).
- Not shown: HY weekly volume; any bank's exposure to data-centre loans beyond the one HSBC sale; flood losses; who holds Car-Mart's prepetition debt beyond the two private lenders named.
- Unnamed thread (logged, not scored): nonbank mortgage and auto servicers. HOMER: Fitch negative outlooks on Pennymac, Planet and Freedom (11/16); CARL: RITM Ginnie 60+ 6.1%; BROCK: Car-Mart servicing passes to Cardinal. No desk names servicer credit as one channel.
- Forward view: the bank leg stays absent through 12/11 (REGINALD about 70%, its unscored projection; I agree). Alternative: HENRY's broadening test, HY over 376 on a day equal-weight falls with KRE under $65. Florida: about 80% no nameable flood credit effect at listed banks in Q4 (REGINALD).

## 3. Root map, counts and counter-signal

- **Effective N unchanged: 1 established root (R1 rates) plus 2 candidates.** R3 credit: REG-T-04 fired, but funding NOT SHOWN (SOFR99−IORB +9 [11/23]) and banks absent; cause not established. R4 AI: a third market episode (11/20–11/25, after 10/29–30 and 11/5) and the first financing-refusal evidence at the AI-infrastructure edge, all secondary. R3 and R4 share the 11/20 antecedent (the Nvidia report), so 11/20 counts once. No three-root alert.
- **Threshold proximity (WQ-519 (iii) A: the cluster counts LINES; the class count is stated beside it and does not gate):** lines breached or within 20%: REG-T-04 FIRED; GATE-LIQ-072 leg 2 FIRED; GATE-LIQ-069 L4 FIRED; LIQUID >320 run 7; HENRY's 7,037.04 line closed under on 11/20 (now 7,201.09, 2.3% above); VIX 30 line (26.36 [11/24], 12% away); RED-FT-11 precondition MET. **7 lines ⇒ the literal proximity-cluster alert goes to PROME. Disc-H class count: 1 (the 11/20 market repricing; the rates rally is the same day's risk-off). Root count: 1 established.** No trade follows from the alert.
- **Disc-D counter-signal (the tape against the stress story):** KRE rose on 11/23 and 11/24; equal-weight RSP +0.54% and the Dow +0.85% on the day SOX fell 7.88%; HY narrowed 13 bp on the day REG-T-04 fired; funding calm. The market is selling the AI complex, not credit broadly.

## 4. Predictions

- PRED-24 (conditional watch): **HY leg MET** (352, 376, 363: three consecutive cells at or over 350). Second leg (a primary-sourced bank to shadow fire-sale datum) **not met**: the HSBC mid-80s sale is a secondary relay with no buyer named. No number re-opened. Resolver unchanged.
- PRED-51 (HY at or over 352 on the 12/31 cell, 40%): latest 363 [11/23]. Not graded; the registered 40% stands (no update rule in the letter). Unscored current view about 55%.
- PRED-52 (claims first print at or over 240,000, w/e 11/21–12/26, 8%): first week prints Wed 11/25. Latest 203,000 [w/e 11/14].
- PRED-45 residual (D:L554 carry): EDGAR full-text, 10-Q and 8-K accepted 11/20–11/24, six phrase families from the 11/20 sweep; four hits, all "in excess of par value" balance-sheet lines (PennantPark Floating Rate 8-K 0001171843-26-007651, Equus 10-Q 0001712543-26-000063) or credit-agreement exhibits (StandardAero, KBR, a CMBS PSA). n = 0 documented loan transfers at or under 95¢. PRED-45 MISS stands; nothing re-opens.
- PRED-41: unchanged, Q4-26 print about early February.

## 5. D:L1189, WQ-712: what breaks if desks stop committing an unchanged brief

Full answer is in the PROME packet; script table in `WQ712_SCRIPT_AUDIT.md` (fresh Opus reader, read-only); schema blind read in `SCHEMA_COLDREAD.md` (Sonnet, the L1189 added step). Summary: the four NEXUS-side dependencies I named on 11/18 were removed by WQ-719 A and WQ-721 A (schema, pin checker, NEXUS BOOT 6/9a/9c, fallback-log meaning). Two desk-local scripts still break: SAM `scripts/closeout_check.py` check F (lines 516–527, exit 1 at 664; run by SAM `CLAUDE.md` line 81, labelled PROVISIONAL) now, and VIOLET `scripts/writeback_order_check.py` lines 223–229 (pin must be among the last 30 STATUS commits; blocks through `closeout_guard.py`) after roughly 30 untouched-brief STATUS commits. Both verified by NEXUS at the file. Correction to my 11/18 packet: CORAL `boot.py`'s 72-hour limit applies to CORAL's own brief, not to MARCO, REGINALD and CARL (it only prints their ages).

## 6. Fallback rows this pass and 9a

- `stale` LIQUID: brief table still reads REG-T-04 "1 of 3" against its STATUS "FIRED" (trigger (a), content); raw STATUS read.
- `convergence` LIQUID/GIBBS: one mid-80s data-centre loan sale in both briefs, neither joins it (trigger (b)); GIBBS STATUS has no line on it; LIQUID's D:L1252 packet row gives the source.
- No `brief-gap`: HENRY's fresh brief omits that its 7,037.04 line closed under on 11/20; I took that from WALTER 20261121-004 and VULCAN's brief, not from a raw STATUS fallback, so no row (recorded here).
- Rollup #7 → `brief_health.md`.

## 7. Brief content flags from the digest (each desk's own to fix; not NEXUS's)

LIQUID test table and "Next:" lag its own REG-T-04 fire · BROCK header pin text, past-dated bank waits · HOMER WQ-725 DONE vs open, the superseded −2.9% row still printed beside its withdrawal note · MIDAS no As-of, October blocks about 60% of the brief, WQ-522 contradiction · AEOLUS "no federal declaration" against CORAL's report the same night · CORAL VIEW "no household aid" against its own 11/06 correction · HENRY omits the 11/20 red-line close · RED lead VIEW overtaken (no pin) · CARL, SHADE carry HY 348 [11/05] · ZHAO, GIBBS, OSPREY, WATT past-dated waits. Under WQ-719 A these are content staleness (a figure, send or wait changed), so each owner owes a rewrite at its next session; none is load-bearing for a NEXUS grade this pass.
