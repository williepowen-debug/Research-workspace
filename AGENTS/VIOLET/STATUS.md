# VIOLET STATUS

**As of:** November 23, 2026 (Monday), 16:41 ET (from `date`). PROME prome-77 wake on D:L1229 (items 1 to 3; item 4 is the 11/25 close). Claude Code, Opus 5.5, laptop.
- **History:** official Cboe closes run through **11/20 (SETTLE)**; the 11/23 rows had not posted at 16:10 ET. Every 11/23 spot figure below is the 16:15 ET close print via the vendor mirror (fetch.py 16:32 ET), **PROVISIONAL**, not graded.
- **Credit:** HY through **11/20**, 376bp first-published [LIQUID owns]; 11/23 posts Tuesday.
- **Last real data refresh:** 2026-11-23. Thesis **v4.1.10**. KB-VIO-406. Record `research/2026-11-23_close-read/GRADE.md`.

## BOTTOM LINE

**🟠 Vol gave back a quarter on Monday while credit's last print was its widest of the year. VIX 26.62 on the 11/23 print (−25.83% from 35.89) after Nvidia's 8-K reinstating Huang; HY first-published 376bp for Friday 11/20 (+24bp in a day). Regime RISING_VOL on the print; the cash curve is still inverted (VIX3M/VIX 0.9579, 5th close).**
- **D:L1229 (1):** HY 376 > 348: the "+30% in 5 days, credit flat" row is **NOT MET on both windows** (+32bp to 11/19, +53bp to 11/20). Credit followed vol. The closed KB-VIO-328 watch's 368 line was passed three sessions after its endpoint (not reopened); my own "acute → lasting" condition "HY at 368" is met.
- **D:L1229 (2):** VIX9D/VIX **1.0428**, VIX3M/VIX **0.9579** (provisional). **VIO-PRED-11 not resolved, OPEN** (needs a close above 35.89, +34.8%). **40 line NOT FIRED.** VX Z6 settled **24.0844** (from 28.4582), N7 23.098: front fell, back held.
- **D:L1229 (3):** vol cheat-sheet **v16** and Operating Picture **v18** republished in place.
- **Forward (unscored):** fade 60 to 65% (curve back above 1.000 within about 8 sessions); second leg into the Nvidia 10-Q (about 12/04) 35 to 40%. PRED-11 frozen at 50%; my unscored view about 25%. Decider: HY 11/23 and 11/24 cells (under 350 = fade; 370 or more = lasting).
- **TERRY:** WQ-696 packet sent 11/23 (two-sided; candidate NOT-FIRED trigger HY ≥ 370).
- **Cboe from this box 11/23:** History, settlement and archive CSVs 200 to `research-bot/1.0`; delayed-quote JSON **403**. WQ-735: 8 scripts switched.

No Will decision, trade, score, threshold or letter change; $0 moved. Convergence left at 40/50 (11/20 basis) under this wake's limit.

## SIGNAL DASHBOARD

| Metric | Latest value | Basis / interpretation |
|---|---:|---|
| VIX | **26.62** [11/23 print, PROVISIONAL]; **35.89** [11/20], high 40.03; 28.44 [11/19]; 24.56 [11/18] | [EST] 11/23 fetch.py 16:32 ET; [CONF] Cboe History through 11/20. |
| VIX9D / VIX3M / VIX6M | **27.76 / 25.50 / 25.96** [11/23 print]; 9D/VIX **1.0428**, 3M/VIX **0.9579**; 40.72 / 30.94 / 29.54 [11/20] | [EST] 11/23 print; [CONF] 11/20 History. Inverted every close 11/17 to 11/20, and on the 11/23 print. |
| VX futures | Z6 **24.0844**, F7 23.7164, G7 23.5635, H7 23.3021, N7 23.0980 [11/23 settle]; Z6 28.4582 [11/20] | [CONF] Cboe settlement CSV 16:17 ET. Backwardated but nearly flat (Z6 over N7 0.99 pts vs 4.83). |
| VVIX | **117.36** [11/23 print]; 138.03 [11/20]; 127.10 [11/19] | [EST] print; [CONF] History. Back under 120 on the print. |
| SKEW | **138.84** [11/20]; 140.86 [11/19]; 142.84 [11/18] | [CONF] Cboe History. First close under 140; RED-FT-10 exit 1 of 4 on my reading (RED grades). |
| MOVE | **106.31** [11/20], +10.27 | [CONF] investing.com primary. BOND owns rates. |
| OVX / OVX:VIX | **54.12** (p89.2) / **1.51** (p17.4) CALM [11/20] | [CONF] Cboe History. Oil vol high but not leading. |
| JPY RV10 / RV20 | **4.76% / 4.59%**, p14.9, CALM [11/20] | USDJPY 159.71. FXY IV/RV 3.1x on a STALE off-hours chain (do not broadcast). SAM owns substance; ING title "carry trade unwind in full swing" unread. |
| Implied correlation | COR1M **25.68** [11/23 print]; 36.05 [11/20]; 16.42 [11/16] | [EST] print; [CONF] History. |
| Credit (owner references) | HY OAS **376bp** [FRED first-published 11/20], 352 [11/19], 323 [11/13]; CCC **1,402bp** [11/20] | [CONF FRED output_type=4, my pull 16:10 ET 11/23; LIQUID owns spreads]. REG-T-04 2 of 3 (REGINALD grades). 11/23 posts Tuesday. |
| SPX | 6,910.39 (−3.70%) [11/20 vendor close, HENRY via WALTER 004] | HENRY owns: −11.62% from the 10/6 record; gamma NEGATIVE, flat about 6,400 to 7,100 (HENRY's rebuild). |
| CFTC VIX futures | Report **11/17**: lev-money net **−72,916**, p10.9, **ELEVATED_SHORT** | Speculators heavily short VIX futures before the 11/19 to 11/20 rise. |

## GATE STATUS

| Instrument | State | Existing letter / limit |
|---|---|---|
| VIX regime line 30 (SETTLE, one close) | **FIRED 11/20 (35.89)** | Regime HIGH_VOL; delivered by outbox SIG 2026-11-21 and NEXUS_BRIEF. |
| VIX regime line 40 | **NOT FIRED** | 11/20 close 35.89; 11/23 print 26.62. |
| VIX +30% in 5 days, credit flat | 11/17 MET stands; **NOT MET on 11/19 and 11/20 windows** (HY +32bp and +53bp vs +25) | Graded 11/23 (KB-VIO-406). No send owed. |
| VIX3M/VIX cash inversion | **MET every close 11/17 to 11/20**; 0.9579 on the 11/23 print (5th if History agrees) | 🔴 LIQUID, HENRY. Thesis prediction 2' arms on the 11/25 close if still inverted (7th). |
| VVIX 120 daily | **MET 11/19 and 11/20**; 117.36 on the 11/23 print | 🟠 RED, HENRY. |
| RED-FT-10 | **RED-owned FIRING since 10/14** | Exit <140 ×4: **1 of 4** on my reading (138.84 [11/20]). |
| RED-FT-06 / RED-29 | **RED-owned** | FT-06 exited 11/18 on RED's registry (WALTER cards 007). |
| Regime-shift outbound row | **FIRED 11/20: RISING_VOL → HIGH_VOL** | 🟠 all agents: NEXUS_BRIEF CROSS-DOMAIN. |
| Credit-vol WATCH (KB-VIO-328) | **CLOSED 11/17, not reopened** | 376 [11/20] passed 368 three sessions after the endpoint; recorded, not regraded. |
| Path-A VIX<20 filter | **FAILS** | Vol led, credit followed: not a Path A sequence (WQ-611 A). |
| OVX/VIX canary | **CALM 1.51** [11/20] | Context only. |
| Cheap-tail alert | **DORMANT 1/4** [11/20] | Every leg far out (VVIX p98.6, VIX p95.4). Ledger rows 11/18 to 11/20 regraded 11/23. |
| BIN-A / BIN-B | **STUCK / BLOCK ACTIVE** | CCC 14.02% [11/20] ≥ 9.55. |
| MOVE pause/resume · COR1M first-tell · pre-CPI cheap-tail · Q2 L477 · VIO-FOMC-0916 · F-B · RV1 | **RETIRED / RETIRED / PASSED / CLOSED / FAILED / HELD / RETIRED** | Terminal outcomes unchanged. |

## CONVERGENCE MATRIX

**Convergence Score: 40/50** (10 vectors × 5), re-scored 11/21 on **11/20 History** (KB-VIO-404): credit 3→4, implied correlation 3→5, equity concentration 4→5, positioning 2→3, SKEW 5→4.

| Vector | Score | Dated basis |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE 106.31 [11/20]. |
| Credit | 🔴 **4** | HY 352bp [11/19], +32bp in five sessions, first close over 350; now following vol. |
| SKEW / tail pricing | 🔴 **4** | RED FT-10 FIRING, exit 1 of 4; SKEW 138.84 fell as spot vol rose. |
| Oil vol | 🟠 **3** | OVX 54.12 [11/20], p89.2; ratio CALM. |
| Positioning | 🟠 **3** | CFTC 11/17 lev-money net −72,916, p10.9 ELEVATED_SHORT. |
| Implied correlation | 🔴🔴 **5** | COR1M 36.05 [11/20], from 16.42 [11/16]. |
| Equity concentration | 🔴🔴 **5** | HENRY owns; S&P −11.62% from peak, NVDA −14.01% on the SEC report [11/20]. |
| VVIX | 🔴🔴 **5** | 138.03 [11/20]. |
| Front curve | 🔴🔴 **5** | 3M/VIX 0.8621, 9D/VIX 1.1346 [11/20 History]. |
| JPY carry | ⚪ **1** | RV10 4.76%, p14.9 CALM [11/20]. |

## REGIME STATUS AND DRIFT

**HIGH_VOL on the 11/20 close; RISING_VOL on the 11/23 print (26.62, provisional; the regime row waits for History).** Five sessions took VIX from 19.30 to 35.89 (+86%); one session took it to 26.62 (−25.83%) on Nvidia's 8-K reinstating Huang.
- Carriers in order: Nvidia CEO exit (11/12), Bessent demand (11/16), BIS chip rule (11/17, effective 11/19), results (11/17), Anthropic IPO open with a two-leg midday drop (11/19), AMD short report (11/19), then the Reuters SEC accounting report (11/20).
- **Vol led and credit followed.** HY 320 → 352 [11/12 → 11/19]. Not a Path A sequence.
- **Duration read (KB-VIO-404):** acute and front-loaded (9-day index highest, futures downhill), with a higher floor. Base n = 7: lower after 17 sessions 5 of 7, a higher close first 4 of 7.

**Dealer gamma (HENRY-owned, context only):** NEGATIVE and flat about 6,400 to 7,100 [HENRY 11/21 rebuild via WALTER 004]; November expiry 11/20 rolled off about 40% of short-dated gamma (HENRY's 11/19 figure).

**What would change my mind (acute → lasting):** HY over 350 on three closes or at 368; VIX6M over 30 or the back futures rising on a down-spot day; VIX3M/VIX still under 1 around 12/15; VVIX over 150 or a VIX close over 40. **Faster fade:** VIX9D/VIX under 1 after Thanksgiving week; VIX3M/VIX at 1.000 within about 8 sessions; COR1M under 25.

## POSITIONS

Position truth is off-repo (Will and the broker), with the separately dated FORGE mirror and TERRY owning trade construction. No quantities copied. **$0 moved.** TERRY packet 11/21 (`AGENTS/TERRY/inbox/2026-11-21_from-VIOLET_vix30-surface-tradeability-and-vixcs-thesis-grade.md`): two-sided, risk in both tails, no direction.

## RESEARCH QUEUE AND OPERATING LIMITS

1. **Wed 11/25 (D:L1229 second read):** confirm 11/23 and 11/24 on Cboe History (`backfill.py` replaces the 11/23 TICK row; regime row HIGH_VOL → RISING_VOL only on History); HY 11/23 and 11/24 first-published (LIQUID); then item (4): thesis prediction 2' arms on a 7th straight inverted close (VIX3M/VIX < 1.000 on 11/24 and 11/25 History). Re-score the convergence matrix on History (left at 40/50 this wake).
2. Bessent deadline about 11/26 (holiday).
3. **About 12/04:** Nvidia 10-Q deadline (VULCAN owns); the 8-K does not address the reported SEC accounting question.
4. **12/16:** December expiry (Z6 SOQ against 24.08 [11/23]) and VIO-PRED-11 resolves; L441 M1:M2 recheck.
5. **WQ-735 refusals to PROME's 12/07 list:** Cboe delayed-quote JSON 403 to `research-bot/1.0` (`implied_corr.py` quote leg, and `thresholds.py` `cboe_quote`); `move.py` not switched (investing.com).
6. D:L342 on 11/27.

**Done this wake (11/23):** D:L1229 items 1 to 3; inbox drained (WQ-735 packet + WALTER 001, 003, 007); COR-20261123-03 NO-OP; 8 scripts switched to the honest client name; CHEAP_TAIL 11/18 to 11/20 rows regraded; MAINTENANCE rotated under its cap; TERRY packet; 11/25 catalyst row.

**Persistence / coordination (11/23):** PROME prome-77 wake, D:L1229. No push (PROME pushes). Laptop on battery; one network drop about 16:38 ET, work resumed from committed state.
