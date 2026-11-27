# VIOLET STATUS

**As of:** November 27, 2026 (Friday), 10:04 ET (from `date`). PROME prome-80 wake on D:L1292 and D:L342; NYSE closes 13:00 ET. Claude Code, Opus 5.5, laptop.
- **Close basis:** Cboe History through **11/25**, pulled 09:55 ET: every 11/25 cell matches the vendor print (VIX 28.29, VIX3M 26.29, 0.9293, SKEW 142.06). `backfill.py --spot-only` 09:58 ET: 0 corrected, 11/25 row stamped SETTLE. Today's close is not graded here.
- **Credit:** HY first-published through **11/24 = 372bp** [LIQUID owns]; **11/25 UNPOSTED** (FRED 09:57 ET).
- **Last real data refresh:** 2026-11-27. Thesis **v4.1.11**. KB-VIO-412. Record `research/2026-11-27_history-confirm/GRADE.md`.

## BOTTOM LINE

**🟠 Cboe History confirms the 11/25 close: the 7th straight inverted close stands (VIX3M/VIX 0.9293), so thesis prediction 2' is ARMED, no longer provisional. The test needs VIX above 25 on every close 11/27 to 12/10; I expect it to fail (about 78%, was about 75%). Convergence 40 → 36/50 on 11/25 History.**
- **Why 78%:** a near-match History base since 2009 (VIX 27 to 29.5, curve inverted, a peak 1.2x higher in the prior 5 sessions) held **0 of 4** (2015-08, 2018-02, 2018-12, 2024-08; each failed by close 2 to 5). Against it: sticky credit (5 of 10 held, KB-VIO-410), the Jazan refinery hit 11/26 and Nvidia's 10-Q about 12/04. By 12/02 about 65%. PRED-11 (close over 35.89 by 12/16) my view about 20%, registered 50% frozen.
- **This morning, vendor at 10:00 ET, not a close:** VIX 26.81, VIX3M 25.63 (0.956, still inverted), VVIX 113.48, S&P 7,218.85 (+0.50%). ⚠️ `fetch.py` shows VIX **+0.04%**: that is against Cboe's 11/26 holiday bar (26.80); against 11/25 it is **−5.23%** (D:L342 class).
- **D:L342, VIOLET side RESOLVED:** no 11/26 row in any VIOLET ledger, no streak, sustain or window count advanced on the 11/26 bar (an orphan VIX with no companion series). ⛔ Do not treat the 9/07 = 15.30 print as a trading session in any count.
- **Matrix moves:** VVIX 5 → 3 (115.38, under 120 on three closes), implied correlation 5 → 3 (COR1M 25.45 from 36.05). Curve, credit, tail pricing, rates vol unchanged.
- **Oil:** Jazan hit and Brent January $96.57 (+2.1%, 11/26, search summaries via WALTER 008); OVX/VIX 1.70 CALM [11/25]; opened `combo:VIOLET/oil-vol-import` (KB-VIO-412). No 11/26 OVX bar.
- **TERRY:** `2026-11-27_from-VIOLET_2prime-armed-on-history.md` (confirmation, no structure).

No Will decision, trade, threshold or letter change; $0 moved.

## SIGNAL DASHBOARD

| Metric | Latest value | Basis / interpretation |
|---|---:|---|
| VIX | **28.29** [11/25]; 26.36 [11/24]; 26.62 [11/23]; 35.89 [11/20]; 26.81 at 10:00 ET 11/27 | [CONF] Cboe History through 11/25; 11/27 [EST] vendor intraday. 11/26 bar 26.80 is no session. |
| VIX9D / VIX3M / VIX6M | **29.61 / 26.29 / 26.89** [11/25]; 26.68 / 25.47 / 26.19 [11/24] | 9D/VIX **1.0467**, 3M/VIX **0.9293** [CONF History]. |
| VX futures | settles 11/25 Z6 **25.0258**, F7 24.2921, G7 23.9679, H7 23.5523, M7 23.125; 11/24 Z6 23.9769, M7 22.9924 | [CONF] Cboe settlement CSV. Z6 3.26 points under spot; front +1.05, back +0.13. |
| VVIX | **115.38** [11/25]; 114.07 [11/24]; 117.36 [11/23] | [CONF History]; under 120 three closes. |
| SKEW | **142.06** [11/25]; 139.16 [11/24]; 140.37 [11/23]; 138.84 [11/20]; 20-day mean 147.04 | [CONF] History. RED-FT-10 exit count on my reading: reset at 142.06 [11/25] (was 1 [11/24]); RED grades. |
| MOVE | **97.54** [11/25]; 98.84 [11/24] | [CONF] investing.com primary. BOND owns rates. |
| OVX / OVX:VIX | **48.04** (p81.6) / **1.70** (p30.1) CALM [11/25] | [CONF] History; no 11/26 bar (Jazan hit that day). |
| JPY RV10 / RV20 | **3.23% / 4.74%**, p7.0, CALM [11/27 boot] | USDJPY 159.51. FXY IV/RV 3.59 (event-premium flag, context). SAM owns substance. |
| Implied correlation | COR1M **25.45** [11/25]; 24.62 [11/24]; 36.05 [11/20] | [CONF] History. |
| Credit (owner references) | HY OAS **372bp** [11/24], 363 [11/23], 376 [11/20]; CCC **1,405**; IG **98** [11/24]; 11/25 UNPOSTED | [CONF LIQUID 11/25 11:45 ET, first-published; my FRED pull 09:57 ET 11/27 agrees]. |
| SPX | 7,182.78 [11/25 vendor close]; 7,218.85 at 10:00 ET 11/27 (+0.50%) | HENRY owns. |
| CFTC VIX futures | Report **11/17**: lev-money net **−72,916**, p10.9, **ELEVATED_SHORT** | 11/24 report not published at 09:56 ET 11/27; due by 12/01 on the cadence rule. |

## GATE STATUS

| Instrument | State | Existing letter / limit |
|---|---|---|
| VIX regime line 30 (SETTLE, one close) | **FIRED 11/20 (35.89)**; RISING_VOL 11/23, 11/24, 11/25 History | Not re-fired. |
| VIX regime line 40 | **NOT FIRED** | 28.29 [11/25]; intraday high 34.95. |
| VIX +30% in 5 days, credit flat | 11/17 MET stands; NOT MET 11/19, 11/20, 11/25 (+15.2%) | 24.56 [11/18] to 28.29; sessions only. |
| VIX3M/VIX cash inversion | **MET every close 11/17 to 11/25 (7 straight, Cboe History)**; 0.9293 | 🔴 LIQUID, HENRY. **Prediction 2' ARMED on History**; 10 closes 11/27 to 12/10. |
| VVIX 120 daily | MET 11/19, 11/20; **not on 11/23, 11/24 or 11/25** | 🟠 RED, HENRY, on a close only. |
| RED-FT-10 / FT-06 / RED-29 | **RED-owned** | My SKEW read above. |
| Regime-shift outbound row | FIRED 11/20 (HIGH_VOL); RISING_VOL since 11/23 | No shift on 11/25. |
| Credit-vol WATCH (KB-VIO-328) | **CLOSED 11/17, not reopened** | |
| Path-A VIX<20 filter | **FAILS** | Vol led, credit followed (WQ-611 A). |
| OVX/VIX canary · JPY canary | **CALM / CALM** | Context only. |
| Cheap-tail alert | **DORMANT** 2/4 [11/25] | VVIX p90.2 and VIX p89.4 fail the cheap legs. |
| BIN-A / BIN-B | **STUCK / BLOCK ACTIVE** | CCC 14.05% [11/24] ≥ 9.55. |

## CONVERGENCE MATRIX

**Convergence Score: 36/50** (10 vectors × 5), re-scored 11/27 on **11/25 Cboe History** (KB-VIO-411): implied correlation 5→3, VVIX 5→3. Was 40/50 on 11/20 History (KB-VIO-404).

| Vector | Score | Dated basis |
|---|---|---|
| Rates vol | 🔴🔴 **5** | MOVE 97.54 [11/25], F1 line 72.41 breached by 25; down from 106.31 [11/20]. |
| Credit | 🔴 **4** | HY 372 [11/24] against the 376 high [11/20]; 11/25 UNPOSTED. |
| SKEW / tail pricing | 🔴 **4** | SKEW 142.06 [11/25], 20-day mean 147.04; RED graded FT-10 CORRECT 11/26. |
| Oil vol | 🟠 **3** | OVX 48.04 [11/25], p81.6; ratio 1.70 CALM. |
| Positioning | 🟠 **3** | CFTC 11/17 lev-money net −72,916, p10.9; 11/24 report not out. |
| Implied correlation | 🟠 **3** | COR1M 25.45 [11/25] from 36.05 [11/20]; above 11/17's 20.13 (scored 3), not escalating. |
| Equity concentration | 🔴🔴 **5** | HENRY owns; chip selloff through 11/25 (Kospi −6.2%, SoftBank −14.8%, WALTER 005). Not re-read by me. |
| VVIX | 🟠 **3** | 115.38 [11/25]; under 120 on three History closes (117.36, 114.07, 115.38). |
| Front curve | 🔴🔴 **5** | 3M/VIX 0.9293, 7th inverted close; 9D/VIX 1.0467 [11/25]. |
| JPY carry | ⚪ **1** | RV10 3.23%, p7.0 CALM [11/27]. |

## REGIME STATUS AND DRIFT

**RISING_VOL on the 11/23, 11/24 and 11/25 History closes.** Path: 19.30 [11/12] → 35.89 [11/20] → 26.62 → 26.36 → 28.29 (34.95 intraday).
- Carriers: Nvidia governance and accounting (11/12 to 11/23), the chip selloff 11/24 (SOX −7.88%, chipdispatch via WALTER 007), Asia chips 11/25 (Kospi −6.2%, SoftBank −14.8%, WALTER 005), proposed Section 301 tariffs, core PCE 3.3%. **No single cause established** (WALTER).
- **Vol led and credit followed, and credit is stickier than vol:** HY is 372 against its 376 high; VIX is 28.29 against 35.89.
- **Duration read:** front-loaded (9-day index highest, futures well under spot), with lower highs (40.03, 34.95) and a slightly higher close than 11/23. Day 7 landed under the 31 split (28.29).

**Dealer gamma (HENRY-owned, context only):** NEGATIVE, flat about 6,400 to 7,100 [HENRY 11/21 rebuild via WALTER 004]; not refreshed by me.

**What would change my mind (acute → lasting):** HY 11/24 or 11/25 at or above 370 (**met by 11/24, 372**; a new high over 376 would add to it); VIX6M over 30; back futures rising more than the front on a down day; VIX3M/VIX still under 1 around 12/15; VVIX over 150 or a VIX close over 40. **Faster fade:** VIX9D/VIX under 1 and VIX3M/VIX above 1 by 12/02; COR1M under 25 with VIX under 25; any VIX close at 25 or under by 12/10 fails 2'. **Oil:** OVX/VIX toward the 2.95 WATCH line after Jazan would add a source.

## POSITIONS

Position truth is off-repo (Will and the broker), with the separately dated FORGE mirror and TERRY owning trade construction. No quantities copied. **$0 moved.** TERRY packets 11/21, 11/23, three on 11/25 and one 11/27 (History confirmation; two-sided, no structure); TERRY answered the 11/25 morning one NO CARD (`TRY-NOTRADE-DRAIN-NOV25`).

## RESEARCH QUEUE AND OPERATING LIMITS

1. **Next wake (after the 11/27 13:00 ET close):** grade close 1 of 10 for prediction 2' on Cboe History (first close at 25.00 or under fails it); `backfill.py --spot-only` supersedes the 11/27 TICK row; HY 11/25 and 11/27 cells; OVX on the first session after Jazan (KB-VIO-412).
2. **12/10:** prediction 2' window ends. Closes: 11/27, 11/30, 12/01, 02, 03, 04, 07, 08, 09, 10.
3. **About 12/04:** Nvidia 10-Q deadline (VULCAN owns). CFTC 11/24 report due by 12/01.
4. **12/16:** December expiry (Z6 SOQ against 25.0258 [11/25]) and VIO-PRED-11 resolves; L441 M1:M2 recheck.
5. **WQ-735 refusals to PROME's 12/07 list:** Cboe delayed-quote JSON 403 to `research-bot/1.0`; `move.py` not switched.
6. **Tool note (PROME, D:L1179 class):** FORGE `fetch.py` ^VIX change on 11/27 is against Cboe's 11/26 holiday bar.

**Done this session (11/27 morning):** boot; WALTER card 008 drained (inbox 0); D:L1292 History check, 2' ARMED on History, matrix re-scored 36/50; D:L342 check clean; KB-VIO-411, -412; KB-VIO-402 dispositioned CORRECTED; thesis v4.1.11; TERRY packet.

**Persistence / coordination (11/27):** closeout with safe-push in this session.
