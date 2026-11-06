# ORACLE -> PROME: December hike verified at about 78; receipt for Will's 15:24 ET turn

**Date:** 2026-11-06 15:3x ET. **Runtime:** Claude Code, Opus 5.5, session `oracle-5d`, desktop `DESKTOP-BC6EF81`, Kalshi signed (`status` rc=0). **Cost:** $0, free public data only. No trade, no position language.

## The odds

| Source | Figure | Time | Depth |
|---|---|---|---|
| Polymarket "increase 25 bps after December meeting" | **77.5** (book 77/78) | 2026-11-06T20:26Z = 15:26 ET | vol $5.0M, liq $312.4K |
| Kalshi `KXFED-26DEC-T4.00` | **78.0** last (book 77/78) | 20:26Z | OI 92.5K |
| Fed funds futures, Yahoo last trades, EFFR 3.88 [11/05, NY Fed] | ZQZ26 76, ZQF27 78 | 15:18 ET | not settlement; 1 tick = 2 to 3 points |
| CME FedWatch via CNBC | 76.8 | figure time unknown | secondary |

Expected move, same units: Polymarket +19.3bp, Kalshi +19.0bp, futures +19.0 to +19.5bp. No dislocation, so nothing goes to TERRY on this read.

**Reuters check:** "78 from 70" holds as a level on my sources. Polymarket was 69.5 at 08:25 ET and 77.5 at 08:35 ET. ⚠️ The Reuters sentence itself is unverified: the Reuters story relayed at cp24.com (updated 11:53 ET) has no odds line, and I found no other copy. FedWatch as its basis is also unconfirmed.

## The 11/05 fall and its cause

"17 points" is right on two bases and overstated on one:

| Basis | Move |
|---|---|
| Polymarket 80.5 (11/04 read, a brief spike) to 63.5 (23:11Z) | −17.0 |
| Polymarket 77.5 (held 11/04 17Z to 11/05 09:30 ET) to 63.5 | **−14.0** |
| Kalshi 82.0 (hour to 09:00 ET) to 65.0 (hour to 11:00 ET) | −17.0 |

**Cause remains NOT established.** New evidence: it was not a venue artifact. Polymarket, fed funds futures, 2-year futures, SPY and QQQ all moved in the same ten minutes, 10:40 to 10:50 ET, and Kalshi in the same hour. Stocks fell from the 09:30 open; odds started down by 09:40; ten-minute data cannot show which led. The Hammack headline at 10:41 ET reads hawkish, the wrong direction, and its body is unread. Three searches found no report of the driver. A risk-off move fits the timing; timing is not cause.

**Rebound caveat:** about 6 of the 14-point rebound came before the 08:30 print (Polymarket 63.5 to 69.5 by 05:00 ET; Kalshi book 65/66 to 71/72 by 08:00 ET). The cause of that rise is not established. Do not credit payrolls with the whole move.

## Gates and state (each named)

| Row | Change | Why |
|---|---|---|
| VX-ORC-07 48h moves | **🔴 Critical → 🟠 Alert** | WTI pair left the 48h window at 11/06T07Z; largest in window Fed HIKE +14.0 log, +15.0 CLOB. Graded under WQ-439 A. Coverage: non-thin log rows, CLOB for Fed HIKE, WTI, AI bubble only |
| VX-ORC-12 / GATE-ORC-12 | No state change; read recorded | 11/06 read 77.5, liq $322.7K, Alert HELD |
| VX-ORC-04 November $110 | No state change; read recorded | 11/06 read 19.0, liq $21.4K, QUALIFIED, run 8, state none |
| Kalshi U3 pin | Rolled to `KXU3-26NOV-T4.1`, `T4.2` | October finalized 4.1%. Watchlist roll, no gate |

No score, band, threshold or other gate moved. `PROME/GATES.tsv` has no ORC-07 row, so no mirror changes. GATE-ORC-12 state is unchanged.

## Inbox

Two WALTER cards drained, both INFO: SIG-W-20261106-009 (Utah charges against Kalshi) and -033 (DraftKings suit, month old). Queue empty.

## Other

- **October jobs graded:** Kalshi crowd mode 4.2, print 4.1, one notch on the stronger-labor side. KB-ORC-124.
- **AI bubble round-tripped:** 8.25 → 15.9 → 7.55 (liq $143.6K). KB-ORC-123.
- **New combination theme:** `venue-legal-risk`, "Can a state or court action take a venue or a contract offline before it resolves?" KB-ORC-127, review 11/20. Seven themes now.
- **Unread movers for triage, not tracked, not verified:** "Susie Wiles leave the Trump administration before 2027" 100.0, +57.0 d1, vol $164.7K; "Houthis enter Saudi Arabia by October 31" 65.6, +26.7 d1, liq $6.2K, a date already past. I have not read the resolution text of either.
- **Kalshi October CPI:** `KXCPIYOY-26OCT` returns 404. Open events are `26NOV`, `26DEC`. Roll not done.
- **Peers:** the same Fed read went to HENRY, LIQUID, BOND, LABOR. No ask, no doorbell.

## Capability notes

Available: Bash, WebSearch, `SendMessage`, `ListAgents`, a web-fetch helper (one spawn, two pages). Missing: direct WebFetch; `curl` of cp24.com returned 5 bytes; FRED CSV returned empty, so NY Fed supplied EFFR. cmegroup.com not touched.

Artifact: `AGENTS/ORACLE/research/2026-11-06_dec-hike-verification.md`. Records: KB-ORC-125, -126, -127.

## COMPLETION — ORACLE — 2026-11-06
STATUS: ✅ DONE, closeout pending your ask
CHANGED: ORACLE workbook (ODDS_LOG, KALSHI_ODDS_LOG, spread, V5_NOV110_READS, VX, KB), kalshi_watchlist, board_log, STATUS, research/2026-11-06_dec-hike-verification.md, inbox moves, this packet, peer packets
RESULT: December hike 77.5 Polymarket, 78.0 Kalshi at 20:26Z, within 1bp of futures. "78 from 70" holds as a level, Reuters wording unverified. Fall −14 to −17 by basis, cause not established. One state moved: VX-ORC-07 Critical to Alert.
GAPS: Reuters sentence not found. 11/05 cause not established; Hammack and Barkin bodies unread. Commits are local, pushed at closeout. SCRATCH, NEXUS_BRIEF, history and TRADE_MARKS refresh wait for closeout.
WILL_NEEDS: None.
FOLLOW-UP: ORACLE waits for your closeout ask.

**ACTION:** PROME reads this receipt. PROME sends ORACLE the closeout ask.
