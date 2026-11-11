# HENRY → PROME: why futures were up on 11/11, gamma at the pre-open and the open, rows touched

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, launched from AGENTS/HENRY) · **For:** prome-2b, ask 09:06 ET · **Written:** 2026-11-11 09:5x ET
**Record:** `AGENTS/HENRY/research/2026-11-11_futures-up/PREOPEN_READ.md` · KB ML-HEN-215 (pre-open), ML-HEN-216 (open) · STATUS § VIEW 11/11 and § GAMMA MAP

## The story in plain words

Futures rose because chip and AI-infrastructure stocks bounced: CoreWeave after its results, and Nvidia after Tuesday's 5.5% fall. A smaller bid in cyclicals and small caps came with it. **Rates gave no help.** Treasury futures sold off, and December hike pricing was unchanged to slightly higher. Before the open, the S&P was set to start just under its gamma flip (~7,622–7,625), the level where dealer hedging switches from adding to moves to damping them. **It did not get there.** The index traded near 7,600 around the open and was back at 7,575 by 09:48, about 0.6% under the flip. Down there dealer hedging adds to a fade as readily as it added to the gap, and the next concentration below is 7,500, about 1% down. Breadth narrowed after the open, so the move became more of a chip trade than it looked in the futures.

## 1. Gamma map (gamma_flip.py --both --publish; Cboe chain asof 11/11 = end-of-11/10 open interest)

| Chain | Pre-open 09:09 ET (spot implied from futures) | Opening 09:49 ET (live vendor spot) |
|---|---|---|
| SPX | ~7,593; flip 7,622–7,625; NEGATIVE, −$11B / −$15B per 1%; put wall 7,500, call wall 7,700 (clean at both horizons) | 7,575.26; flip 7,621–7,624; NEGATIVE, **−$18B / −$22B** per 1%; walls 7,500 / 7,700 |
| QQQ | 687.31; flip 690–691; NEGATIVE; walls 680 (14d band 680–685) / 700 | 684.44; 6 pts under the flip; NEGATIVE |
| NDX | ~28,270; flip 27,887–28,026; POSITIVE; walls 28,000 / 29,675 | 28,140.36; flip 27,970–28,118; POSITIVE but net zero on 35d |

**So what:** under ~7,620 the S&P move is amplified in either direction; above it the move damps, with 7,700 next. All six walls passed the cross-horizon check and are published (the 11/10 WITHHELD rows are superseded). Nasdaq sits at its boundary: QQQ just under its flip, NDX just over. Read it as neither damped nor amplified.
⚠️ **Limits:** free-tier estimate. The sign and the flip are the reliable parts; dollar sizes depend on assumptions. Today's same-day (0DTE) options flow is not in the open interest. The pre-open spot was implied from futures. A map is a reading of hedging pressure, not a forecast of direction.

## 2. Drivers, from my own quotes

| Item | Pre-open (Cboe ~09:08 ET) | After the open (vendor 09:48 ET) |
|---|---|---|
| Cap weight vs equal weight | SPY +0.96% vs RSP +0.43% | SPY +0.71% vs RSP +0.23% |
| Chips / AI infrastructure | SMH +4.52%, CRWV +14.78%, NVDA +3.42%, MU +6.88%, AMD +5.19%, ORCL +4.82%, TSM +4.28% | SMH +3.04%, CRWV +12.37%, NVDA +1.78% |
| Rest | IWM +0.90%, DIA +0.28%, XLI +1.02%, XLE +1.21%, XLV −0.77%, XLF −0.21% | IWM +0.48%, DIA −0.16% |
| Treasury futures vs the vendor 11/10 bar (cash closed for Veterans Day; no par print today) | 2Y about +3bp, 10Y about +2bp, 30Y about +1bp | 2Y about +4–5bp, 10Y about +3–4bp, 30Y about +3bp |
| December fed funds ZQZ26 | 95.915 (08:51 ET) = about +28.9bp | 95.920 (09:38 ET) = +28.2bp, the same as Tuesday's 16:01 ET last trade |
| VIX | 18.33 | 18.19 (VIX9D 16.92) |

**Verdict:** chip-led with a real but much smaller broad bid. It is not a rates-relief rally: yields rose and the hike pricing did not ease. ⚠️ **Attribution:** the CoreWeave and Nvidia story is the press account plus the cross-section of moves, not a flow measurement. CoreWeave's Q3 headline beat and capex guide come via WALTER 20261110-011 and -013 (relay; I did not read CoreWeave's release). The TrendForce "Nvidia may slow orders" report (WALTER 20261111-003) is not being priced: TSM was +4.3% premarket. Rate yields are converted from futures prices with approximate durations, so the signs are robust and the basis points approximate. All quotes are vendor or Cboe delayed, not settlement. Futures quotes run about 10 minutes behind.

## 3. Rows touched, graded on their letter

| Row key | Letter | Grade 11/11 |
|---|---|---|
| **HEN-57** | Oct core CPI 0.4+ = FIRED | RESOLVED 11/10, NOT FIRED (core +0.3). Untouched |
| **HEN-60** (0.50) | an official S&P close under its 200-session average, 11/9–11/30 | OPEN, NOT FIRED. Only closes count; 200-day 7,331.08 (11/10 basis), spot 3.3% above at 09:48 |
| **HEN-61** (0.28) | an official close above 7,818.93 by 12/31 | OPEN, NOT FIRED; spot 3.1% under |
| **HEN-63** (0.70) | December FOMC upper bound above 4.00% | OPEN, not re-marked (the letter has no re-mark clause). The market prices a 25bp hike fully plus about 13–16% of a second; the gap above my 0.70 is unchanged to slightly wider |
| **HEN-58** | PPI Fri 11/13 | OPEN, untouched. The wake row is still to be confirmed by PROME (carried from 11/10) |
| **CYPHER ESCALATION_WATCH row 9, collapse leg** (WQ-635 A; my price read, CYPHER's row) | PANW ≤ $289.24 AND ≥10.0 points behind HACK on 2 consecutive adjusted closes; graded at the 11/18 close | NOT BREACHED on the 11/10 close: PANW 326.36 (−4.09% from 340.28), HACK 115.29 (−2.61%), PANW 1.48 points behind (yfinance adjusted). The bank leg stays unsized |
| RED-FT-06 / RED-29 (RED's rows, not graded here) | VIXCLS 18 or higher | VIX 18.19 at 09:48, 0.19 above the line; RED grades 11/12 |

No band, threshold or gate of mine fired. 2Y and 10Y Treasury par cannot print today (bond market closed).

## Tradeability

There is no new edge here, so I propose no card. This is a market-structure state that can flip on a 0.6% move. If TERRY wants it, the one fact that matters is that QQQ sits about 6 points under its ~690 flip, with 680 below and 700 above. Per USER.md "No expiry nagging", this packet says nothing about Will's held QQQ puts.

## Inbox

Drained, every sender: 13 WALTER cards (20261110-003, -005, -006, -009, -010, -011, -012, -013; 20261111-001, -002, -003, -004, -006) and FERT's October food-at-home packet. Each is logged in `AGENTS/HENRY/board_log.tsv` and moved to `processed/`. None carried an ACTION for HENRY. Corrections COR-20261110-12 and COR-20261111-06 are receipted NO-OP; the corrections check returns rc 0 for HENRY.

## COMPLETION — HENRY — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/STATUS.md, STATUS_COLD.md, board_log.tsv, workbook/KB.tsv, workbook/PUBLISHED.tsv, registry/corrections_receipts.tsv, research/2026-11-11_futures-up/PREOPEN_READ.md, inbox moves to processed/; this packet
RESULT: Published the pre-open (09:09) and opening (09:49) maps for SPX, QQQ and NDX. The S&P opened 46–49 pts under its ~7,622 flip at −$18B/−$22B per 1%, with walls 7,500/7,700. The rally was chip-led (SMH +3.0% vs RSP +0.2% at 09:48) while 2Y futures rose about 4–5bp and December pricing held at +28.2bp. Six rows were graded on their letter and none fired; 14 inbox items were drained.
GAPS: FRED 11/10 HY/CCC are not read yet (they post about 10:10 ET), and neither are FRED SP500/VIXCLS. CoreWeave's release was not read (relay only). No intraday flow or 0DTE data. The Operating Dashboard has not been refreshed.
WILL_NEEDS: None.
FOLLOW-UP: The window is held open for PROME's closeout ask. If the window is still open after about 10:10 ET, fill FRED 11/10 credit. HEN-58 PPI wake row for 11/13.
