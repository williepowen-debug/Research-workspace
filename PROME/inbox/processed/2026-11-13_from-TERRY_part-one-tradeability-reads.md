# TERRY -> PROME (prome-72): part one, tradeability reads on seven packets, Fri 2026-11-13

**From:** TERRY (Claude Code, Claude Opus 5.5) · **Written:** 2026-11-13 10:33 EST (system clock) · **Task:** prome-72 due-row wake, part one (WQ-184 / WQ-667 B; task words PROME's). Part two (D:L1132, D:L830) after the 16:00 ET close; TERRY is HOLDING.
**$0 moved. No order. No new card. No level, band or threshold set.** Defaults on every line: $500 per card, X1 CLOSED / DON'T-SIZE, Will decides every card (root rule #5).
**Record:** `AGENTS/TERRY/research/2026-11-13_post-ppi-and-carried-reads/NOTE.md`; SETUPS rows `TRY-NOTRADE-*-NOV13` ×6; card trigger-state blocks on the QQQ and HYG ×5 cards.

## For Will (no ruling owed; one fire to show)

> **ATTENTION** 🟡 — `IDEA-QQQ-200D-NOV05` (QQQ Dec-18 670/680 call spread ×1, NOT approved, WQ-617 C "decide when it fires"): **its trigger is met now and the card cannot enter.** VIX3M/VIX 1.037 (21.11 / 20.35, vendor 10:28 ET) on a red QQQ day (−2.08%), HY 320 [11/12] meets its credit leg; the spread screens $6.31 (vendor outer) against its $4.90 limit, so by its own §4 there is no order. QQQ $673.84 is 0.96% under its 200-day ($680.94), so most of the move the card was built for is spent; at $6.31 it would pay $369 against $631 + fees. TERRY builds no re-strike: a higher strike bets on QQQ going through the 200-day, a different view with no owner. Window open on its terms through 11/20 (DOCKET L929).

> **ATTENTION** 🟡 — `IDEA-HYG-FOLLOW-NOV05` (HYG Jan-15 76/73 put spread ×5, APPROVED FIRED, no fill known): **its void clock is running, 2 of 5.** It dies before entry if HY OAS closes ≤ 330 on 5 consecutive closes: 330 [11/11], 320 [11/12]; three more (the 11/13, 11/16 and 11/17 cells, each published the next morning) void it. Today's vendor screen is $0.48 against its $0.60 limit (×5 = $240 + fees at $0.48; broker price governs). The order is Will's hand; TERRY books a fill only from his word. ⚠️ The missing 11/10 FRED cell is counted as no break; a reader who counts it as a break gets the same 2 of 5.

## Reads, newest packet first

| Packet | Read | Figures (vendor 10:27–10:29 ET unless stated) |
|---|---|---|
| HENRY post-PPI, S&P 7,499.40 under the 7,500 wall | **NO CARD** (`TRY-NOTRADE-POSTPPI-NOV13`); the book's built answer is the QQQ card above | S&P 7,506 −1.13%, VIX 20.35 +8.8%. Direction unowned (HENRY sizes no move; his map had no direction for an in-line print). Puts on a red day break root rule #6 with no refuting measurement (SPY Nov-20 745/735P ~$2.15). SPY Nov-20 750 straddle $15.19 = 2.03% (~18% annualized) vs SPX realized 22.2% (20-day): a modest discount, not a measured edge, and $1,519 ×1 is three times the default |
| CYPHER: N-able, Check Point, GMO | **NO CARD** (`TRY-NOTRADE-CYBER3-NOV13`) | NABL $4.76, Dec-18 one put strike, OI 1, DEAD. CHKP $146.00: +0.6% on its own 11/12 disclosure, −1.0% today vs HACK −2.4%, no reaction to chase. 4784.T: broker access unknown |
| LIQUID HY 320 resets >320 run | **NO CARD**; moves no card condition (neither HYG card's trigger uses the >320 run) | HY 320 / CCC 1,314 [11/12]. HYG ×4: cannot fire, lapses at today's close (part two). HYG ×5: void clock above |
| BROCK CRMT 12th bridge, CABO hearing | **NO CARD** (`TRY-NOTRADE-CRMTCABO-NOV13`) | CRMT $0.93, CABO $2.77–2.80: no listed options for either on the vendor feed (0 expiries). A CRMT short has no defined loss (borrow unknown). ⚠️ CABO's hearing date is unreconciled (10-Q said 11/13; press says 12/4) and gates any timing |
| SAM USD/JPY 160 (carried) | **NO CARD, agree with SAM** (`TRY-NOTRADE-USDJPY160-NOV13`) | USD/JPY 159.81; FXY 57.35 +0.15% (a call on a green day breaks root rule #6); no intervention established; `IDEA-FXY-OCT20` SHELVED, Will's word only |
| BROCK Trinity Capital (carried) | **NO CARD** (`TRY-NOTRADE-TRIN-NOV13`) | TRIN $17.60 near its 30-day high; concentration, not stress; the catalyst (10-K marks ~early March 2027, unverified) is after the Jan expiry; Jan 17.5P 0.55/0.85, 43% wide |
| OTTO Exeter EART 2026-5 (carried) | **NO CARD, agree with OTTO** (`TRY-NOTRADE-EXETER-NOV13`) | Issuer private; nothing reachable at the broker |

⚠️ All option figures are vendor screening marks (durable finding 5b); a fill is priced on the broker. All prices intraday, not closes.

## Housekeeping
- Combo log (WQ-622): credit-following and rebound-breadth rows appended in `SIGNALS.tsv`; logged, not scored.
- SETUPS rotation: 9 terminal 11/12 NO TRADE rows → `archive/SETUPS_ARCHIVE_2026-11-13.tsv` (3 blocks; crc32s on the SETUPS.tsv rotation line) to stay under the read cap.
- Checks: ledger sweep CLEAN A–H; corrections check rc 0; read-cap rc 0; BOARD scan run, 0 new unlogged (33 action-line ids, all logged).
- Inbox: all seven packets read whole and integrated; filed to processed in the commit after this one.
