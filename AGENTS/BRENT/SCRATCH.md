# BRENT SCRATCH — September 28, 2026 (Monday; live session brent-d2, Will-launched 14:34 ET, PROME-doorbelled 14:4x; closeout ~15:2x ET)

## CHANGES SINCE LAST SESSION (9/25 17:2x → 9/28 14:34)
- **Iran 7-day Hormuz plan.** Timeline agreed with HAWK: private remarks Thu 9/24, public confirmation Fri 9/25 07:14 EDT, Trump rejects Sat 9/26, Araghchi says nothing has come via the mediators Sun 9/27. Also Sun 9/27 14:37 EDT: Trump tells Axios he expects talks this week.
- **Monday routine** ran ~09:5x (`66eefde69`) and flagged the Nov/Dec split to PROME. Its errors are now corrected in-file: the "Fri 9/26" weekday, the "first sub-$100" claim, and "Dec is front".
- **Bloomberg 9/28:** Yanbu exports resumed after a 17-day halt. One anonymous source; Aramco did not comment.

## WHAT I DID THIS SESSION
- **Boot:** rc=2, the standing set (TRADE.md and INCIDENTS 9d stale). The COT instrument probe reads STALE, "newest 9/06" — not investigated (see next-session item 1). Inbox: WALTER -007 acted, WALTER -001 acted (no gate consequence, answered by message). Corrections check rc=0.
- **Settles published** (settle-window proxy, yfinance VWAP 14:28–14:29; CME blocks this box): BZX26 105.29 · BZZ26 97.83 · BZF27 94.35 · CLX26 92.58 · CLZ26 89.00 · HOX26 4.4955 · HOZ26 4.3691 · RBX26 3.1581. Nov ULSD crack $96.23 vs Dec $94.50: they straddle F1's $95.
- **RULE:** BRENT GRADED-CONTRACT RULE in the `workbook/REGISTRY.tsv` header, answering PROME's doorbell. It points to TRACKER. Sized: the 9/30 switch changes no Brent line's state.
- **Found and recorded late:** Dated Brent was above the $120 line on 9/14–9/17 (peak $130.80), and the desk never logged it as a crossing. Now in STATUS, CHANGELOG and TRACKER.
- **L471 position packet** sent to PROME/inbox. Timeline aligned with HAWK by message.
- **$0. No trade, band, grade or thesis change.**

## ⚠️ MY ERRORS / NEAR-MISSES
- **The routine's weekday slip propagated:** my file said "Fri 9/26", PROME copied it into its doorbells, and PROME's own correction then said "Sun 9/28". HAWK had one too ("Thu 9/25"). L24 would have caught all three. Weekday-check every date in a timeline.
- **Registered line missed for 11 days:** the physical $120 line crossed 9/14–9/17. The desk saw $130.80 on 9/16 and filed it as a mirror figure. A NEAR THRESHOLDS/BREACH row on the boot board is not a recorded crossing unless someone writes it.

## NEXT SESSION (dated, future-verifiable)
1. **COT instrument probe says the newest datapoint is 9/06**, but vintage #7 (as-of 9/22) was graded at the raw file. Find out why the probe reads older (the Socrata lag class?) before the 10/2 grade.
2. **Tue 9/29:** last BZX26 settle; HENRY's blind BRT-12 verdict due. **Wed 9/30:** BZZ26 becomes the graded month (the rule). PROME re-pins FORGE (L461).
3. **Wed 9/30 ~10:30:** grade **BRT-29** at the WPSR wk-9/25 (T needs ≤7,555 kb/d) and **BRT-12** under the 8/13 rule. PREP: `setups/2026-09-25_Q3-predictions-grade-PREP.md`.
4. **Fri 10/2:** COT #8 (as-of 9/29), graded the same day. **Sun 10/4:** OPEC+. **~Mon 10/5:** Aramco Nov OSP plus European term allocations: the first test of the Yanbu-resumption report. **10/06:** L471 sitting. **10/24:** WQ-264 shadow run ends.
5. **Rotate:** STATUS at 84% (rotate the 9/25 PM block). NEXUS_BRIEF at ~32.1 KB against the 32,550 B cap: compress it first next session.
6. **Today's EIA retail print** (out this afternoon): regular was $4.478 on 9/21 against the $4.50 line. Read it next session.

## OPEN THREADS / WATCHES
- 🔴 **Yanbu:** resumption REPORTED (Bloomberg, anonymous). No operator figure. Tracker class is confirm-only. The successor resolver registers after 10/24.
- 🟠 **INCIDENTS:** OSPREY refinery tape (Kuibyshev/Ufa 9/22) still owed after a primary check; 11 ACTIVE rows past 60d.
- 🟠 **TRADE.md** 9d stale at 81%: pre-9/12 history rotation offered to Will twice, no answer. USO Sep-16 165C disposition is still Will's (WQ-169).
- 🟡 Data gap: CME settlements block automated access; the paid EOD feed vs manual glance question is still undecided with Will.

## POSITION DECISIONS PENDING
- None new. USO 37 sh (USO $148.70 at 14:35 ET, yfinance). VLO 1 held + 2 staged (TERRY/Will). WQ-192 stand-down holds.

## MAIL STATE
- Inbox: **empty** (2 consumed = 2 board_log rows, both git mv'd).
- Sent: PROME (L471 position packet, closeout memo) · HAWK ×2 (timeline) · WALTER (-001 answer). Outbox: clear.
