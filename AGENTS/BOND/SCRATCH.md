# BOND SCRATCH — 2026-10-29 catch-up session, heavy tier

> STATE AT WRITING: Composite **19/35** (5+4+3+3+1+1+2; was 17). Clean-nominal counter reached 3 on 10/21 (registered), contested by the 10/26 2Y audit-only I′ fire; auction health held 4, question with PROME. **OPEN predictions 0** (BND-32 FALSE). Position: FORGE 10/22 reconcile TBT 5 held, WQ357 sell approved 10/15 and not filled; TLT82P closed 10/12; NO-ADD WQ280. Latest official cells: Treasury 2Y/10Y/30Y 4.67/5.05/5.37 [10/28]; real 10Y 2.67; HY/CCC/IG 318/1321/88 [10/27]; SOFR−IORB +5 [10/27]; FR2004 long-end $151.396B [as-of 10/14].

## WHAT I DID

Will (10/29): boot, catch BOND up on all new data, work owed tasks. No BOND session had run 10/21–10/28. Claude Code, `claude-opus-5-5`. Pull: local was level with origin after fetch (0/0), so no pull was needed; other desks' dirty paths untouched.

- **Tool repair:** TreasuryDirect TA_WS renamed `auctionDate`, `tips` and the four competitive-award fields. The grader failed loud; `docket_check` passed rc 0 over an EMPTY set (third time for this class). Built `monitors/ta_ws_schema.py` (validated 153/153 corpus rows); docket_check now rc 2 on dateless rows. Selftests and the 18-test regression suite pass. KB-501.
- **Grades:** 20Y-R 10/21 and 5Y TIPS 10/22 REGISTERED CLEAN (20Y I′ +0.20pp). 2Y 10/26 AUDIT ONLY, I′ fire: indirect 45.68% record low, direct 41.32% record high of 46 nominal 2Ys. 5Y 10/27 audit-only clean. The 7Y 10/29 pre-print bars were captured but are not registrable (the grader requires frozen_on before the auction date; guard not loosened). KB-502/504/505/506.
- **FOMC 10/28:** hold 10–2, two +25 dissents; bear steepener; BND-32 FALSE (+10bp). KB-507.
- **Data:** FR2004 as-of 10/14 record >21Y weekly build, VX-04 2→3 (KB-509). HY 340→318, CCC 1356 3-year-window high (KB-510). Credit-equity red letter met one session 10/22, reverted, VX-07 1→2, HENRY packeted (KB-517). SOFR−IORB 0→+5 (KB-511, LIQUID owns). PMMS spread 236bp, VX-17 1→2, review says survey lag (KB-512). Bund WQ400 0/14 (KB-513).
- **Owed:** F2 10/27 read to RED (late; sixth OFF-THE-RUN). RED FT-11 v1.1 precedence ruled (FUNDAMENTAL wins, prospective, co-fire flag). CYPHER boundary confirmed plus a TAAPS/interdealer amendment. Two corrections receipted. 23 inbox packets filed.
- **Clock anomaly:** the local clock read 00:16–00:28 for early stamps. At 06:04 EDT it agreed with server headers, but uptime implied a ~01:36 restart, so the early stamps are UNVERIFIED. Caveats appended to all packets and the F2 ledger row (KB-517).

## Closeout C1–C12

C1 STATUS rewritten, composite re-summed 19/35. C2 KB 501–517 (17 new) + 29 overdue dispositioned; VX 15 states, 3 score changes; **FLOW no-op**: no channel confirmed or changed (dealer→repo co-movement is noted, not a confirmed transmission). C3 BND-32 resolved; no owed registration; 0 OPEN. C4 THESIS evidence legs + channel table + Conviction FORGE line refreshed; **no version bump, CHANGELOG no-op, token unchanged** (no gate, position, regime or version moved). C5 docket: 7Y CUSIP, 20Y 11/18, 10Y TIPS 11/19, refunding freeze 11/5 added; VX-20 rescheduled 11/11; 4 rotated. C6 TRADE view/holdings/review list. C7 this file. C8 RECEIPT overwritten; 14 board_log rows. C9 MEMORY bullet (freeze needs a session; schema-rename degenerate pass); no auto-memory change. C10 CLAUDE.md files row for ta_ws_schema. C11 NEXUS_BRIEF rewritten last. C12 heavy runner, `--superseded 17/35 19/35`.

## NEXT SESSION (dated)

1. **10/29 (today, after 13:00 ET):** grade 7Y `91282CRV5` AUDIT ONLY. FR2004 as-of 10/21 ~16:15: if the long-end total fell, VX-04 un-fires (3→2). PMMS noon: re-test the VX-17 band.
2. **10/30–11/3:** month-end/coupon settlement 11/2 (watch SOFR−IORB vs LIQUID's read); borrowing estimates 11/2.
3. 🔴 **11/4–11/8: QRA (F1/F3 adjudication, sb0607 window expiry) and FREEZE refunding bars** for 3Y 11/9 · 10Y 11/10 · 30Y 11/12 into `registry/auction_bars/<date>_<cusip>.json` with frozen_on before each auction date. F2 op 11/4.
4. 11/11 VX-BND-20 bounded review; 11/12–11/17 freeze bars for the 20Y 11/18 and 10Y TIPS 11/19; 11/13 FRBNY FX report.
5. Consider registering a prediction for the refunding (0 OPEN now), base-rated before the print.

## OPEN THREADS

Counter question with PROME. True CDX, current pulled-deal census, private/offshore funding, event-time TIPS: unchanged gaps. CDX proxy not run this session. WQ291 funding window still UNGRADED. Q4 tentative auction schedule PDF URL not found (404 ×3); November rows come from the Aug-QRA PDF, re-verify after 11/4.

## POSITION

FORGE 10/22 11:01 ET: TBT 5 held, no sell order despite WQ357 approval (FORGE D-82). TLT82P closed 10/12. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Out (carve-out ① commits): RED F2 read + FT-11 ruling; CYPHER boundary; LIQUID dealer/auction evidence; HENRY credit-equity one-session letter; PROME catch-up with two asks (wake BOND 11/4–11/8; the counter question). Delivery to the file is not consumption; none claimed. Inbox drained at writing.

## C12 note — composite not declared `--superseded` (judgement, stated)
The first heavy run declared `--superseded 17/35 19/35`. Every hit (13 self, 15 cross) was a DATED record: past analysis reports, `before_*` snapshots, prior closeout transcripts, session logs, digests, dated TSV rows. "17/35" is true as of each date, and a self finding can only be cleared by editing the file, which would falsify history. The composite is a per-session reading, not a threshold or band that other desks key on. The 10/01 composite move (15→17) was likewise never declared. Live consumer surface (NEXUS_BRIEF) carries 19/35. Re-ran without the declaration; reported to Will.
