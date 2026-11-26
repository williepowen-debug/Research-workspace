# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-26 (Thu, Thanksgiving) 16:2x ET · **Box:** laptop `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3; signed lane is desktop-only) · Session: Claude Code, Opus 5.5, oracle-47, booted 11:15 ET. Work came from Will's status ask, then PROME prome-80's Thanksgiving tasking (11:39 and 11:52 ET), then Will's own asks ("keep going on the overdue tasks" 12:42 ET; "lets work on whats still open" 15:39 ET; "lets close out" 16:20 ET). Prior live session: 11/18.

## CHANGES SINCE 11/18

- The routine ran every weekday except **11/24**. That day the laptop was awake, and all five slots failed on `Could not resolve host: github.com`, inside PROME's recorded outage of 11/23–11/24. It was not sleep.
- **Fed:** December is near-settled (Kalshi above-4.00 96, PM +25 93.5). January 2027 is near even odds for a second hike (PM 53.5, Kalshi 57).
- **Iran:** the pause by 11/30 went 42 → 72 with no acknowledged US strike since Qeshm 11/17, while the Gulf war widened. The oil tail is gone: WTI $110 Nov 0.7, spread +96.6.
- **Nvidia:** the board reinstated Huang as CEO on 11/23 (8-K), and the successor markets resolved. The AI-downturn market whipsawed 8 → 40 → 70 → 12 → 35 → 16 on a book that thinned about 8×.
- **October CPI:** the market resolved 3.7% on 11/20, on its fallback rule.

## WHAT I DID (11/26), commits in order

- a89c2f5efe: inbox 9/9 drained; routine backlog 11/13–11/25 graded late (VX-ORC-04 none, -06 Watch touched, -07 🔴 Critical on AI −21.4, -12 Alert held); KB-ORC-143 to 151; `workbook/F1_BRIER.tsv` (bank-failure Brier 0.217, n=5, every miss under-priced a failure); STATUS full rewrite; NEH full-rules PDF read. d802836255: PROME return packet.
- 120954ff5e: `tools/routine_check.py` now prints band touches and 48h pairs since the last grade (read-only). Owner-TESTED: it reproduced the hand grade and found one Alert pair the hand grade missed (by-11/8 pause −14.0). 7e08f07b72: review ask to DAEDALUS, which is PENDING.
- d83eceed11 + 9e5d3bafb5, 82f4a16289, 5e239f219b, 09f68a333a, a9141a33e5:
  - Rolls: senior meeting → 12/31 market; pause 12/31 leg; Hormuz normal 1/31/27 and 6/30/27; Hormuz weekly → week of 11/23.
  - January FOMC pinned on both venues (KB-ORC-152).
  - Coverage sweep (KB-ORC-153), with nominations to HAWK, BRENT and VULCAN; INFO packets to BROCK and HENRY.
- 2c3b0320e6: TRADE.md regenerated (TRADE_MARKS 624 rows); KB-ORC-155 (Nvidia successor resolution), KB-ORC-156 (integrity review); blockade-end 12/31 pinned. 5ed8ac8115, 6cc2f16f07: late Iran pause routing (+30pp) to HAWK and BRENT.
- fee215bc2a: WQ-295 WATCH_FOR check closed with no proposal (KB-ORC-157); KB-ORC-086 back-sweep clean (158).
- 49d9dcfbe9, 6e317279f9, f46b13a523: November CPI rungs T3.6 and T3.7 pinned (KB-ORC-159); December oil-leg status recorded (KB-ORC-160, Kalshi $115 settle-max pinned as context); Russian diesel nomination actually sent (KB-ORC-161, correcting the unsent 11/04 note).
- Closeout commit: HISTORY.tsv refreshed, this file, NEXUS_BRIEF.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py` now prints a BAND-SCAN section. Grade each touch on its VX row, route it per the signal table, then bump the row's Updated.
- **🔴 Mon 11/30 – Tue 12/1:** the November $110 leg, Hormuz normal by 11/30, the pause by 11/30 (the run completes about 12/1 if no US strike) and Kalshi Brent month-end all resolve. Retire them with resolution records.
  - **Re-search December WTI $110.** It is absent, breaking the pattern of listing on the 25th.
  - If it is still absent, VX-ORC-04 goes UNKNOWN and the spread series ends. A substitute leg is Will's call: proposal to PROME (KB-ORC-160).
  - Also re-search December yield ladders, Hormuz December legs and Kalshi Brent December.
- **🟠 Replies owed TO ORACLE (no reply = not pinned):** HAWK (Israel–Iran ceasefire, Iran leadership change); BRENT (crude all-time-high pair; Russian diesel); OSPREY (Russian diesel); VULCAN (Anthropic bankruptcy). DAEDALUS: routine_check review.
- **🟠 Thu 12/3:** coverage sweep due. **12/04:** November U3. **12/09:** FOMC; VX-ORC-12 retires either way. **12/10:** November CPI, scored against the Kalshi mode 3.7 (combo:print-miss-direction).
- **🟡 Combination reviews:** 11/30 strike-vs-oil, diplomacy-drift, ai-unwind-read · 12/10 bank-book-depth, venue-legal-risk, polymarket-integrity (candidate to close) · 12/11 print-miss-direction.
- **🟡 12/15:** Kalshi gap-fill quarterly re-check (WQ-305). Open bank-failure instance: add its F-1 row at resolution.
- **🟡 Still unowned:** WQ-599 daily-grading owner. The same-day routine-grading variant is OFF: it changes WQ-527 C and sits in PROME's ideas list for Will.

## CARRY-FORWARD

- **Push state:** before this closeout, every 11/26 commit above was already on origin/master (fetched 16:1x ET: 0 ahead, 0 behind). The closeout commit goes by `scripts/safe-push.sh`.
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction · venue-legal-risk.
- **Fed futures method:**
  - December average = 100 − ZQZ26; post-meeting rate = (31 × average − 9 × EFFR) / 22.
  - January: the February average (100 − ZQG27) is the post-January rate.
  - Full precision via `.venv/bin/python` yfinance; one 0.005 tick = 0.7bp.
  - NY Fed EFFR API: `markets.newyorkfed.org/api/rates/unsecured/effr/last/3.json`.
- **Kalshi decision markets:** the decision market (`KXFEDDECISION-27JAN`) is deep; the `KXFED-27JAN` level ladder is thin. Use the decision market for January.
- **Polymarket monthly ladders:** WTI lists on the 25th at 04:01Z; yields and Hormuz around the 3rd of the month.
- **Standing framing (do not re-derive):**
  - **In a fast move, read the CLOB book, not Gamma** (KB-ORC-130). A by-date EVENT pin surfaces its top leg, which can be a drained far leg: pin the deep leg as a MARKET.
  - A closed market drops out of the plain Gamma slug query; `pull` finds it via `closed=true`.
  - Kalshi pull's `Δp` is the API's previous-price change. Kalshi mid applies only when `result` is empty AND OI > 0 (KB-ORC-086).
  - Quote a Fed move from the level held before it, with its basis (KB-ORC-126). ORACLE owns the December priced path (WQ-671 A): venue odds plus the futures cross-check, both caveats.
  - v5 at $110 since 9/24 (WQ-260); current segment `v5-nov26-icewti110`, which ends 11/30.
  - PM "ceasefire"/"pause" = no qualifying US strike landing on Iran (KB-ORC-111, 145). A resolution applies the market's rule; FALCON owns the event grade.
  - A later pull on the same ET date is context (O3). Holiday and weekend pulls are context.
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079). Recession venues use different definitions (KB-ORC-099).
  - NEH: strikes don't count, only a land offensive (KB-ORC-150).
  - Three published σ remain retracted (KB-ORC-064). CME is unreachable: do NOT re-attempt; use Yahoo plus NY Fed EFFR.
  - Polymarket trades: `data-api.polymarket.com/v2/trades?condition=<conditionId>&limit=500`. `prices-history`: `curl -A "Mozilla/5.0"` with startTs/endTs.
  - Never `pull --log --force` to log new pins (new 11/26 pins log at the next routine pull). Kalshi `pull` has no double-log guard.
  - **Never type a clock stamp from narrative.** This session wrote stamps 10 to 20 minutes ahead four times, all caught before commit. Run `date` in the same command.
  - **A "nominated"/"sent" note is not a packet:** git-log the recipient's inbox (the 11/04 Russian diesel item, KB-ORC-161).
  - Git: commit with a pathspec only; the shared index held RED's staged files today.

## OPEN HYPOTHESES

- **Fleet registered forecasts go stale against deep markets (n=2):** HEN-63 is still 70 against 96 on the same letter (11/26). Tested by 12/9 and 12/17.
- **The crowd separates Gulf violence from US strikes on Iran and from supply loss (strengthening, 11/26):** pause 72 and oil tail 0.7 while Iranian and Houthi strikes widen. HAWK and BRENT own the reality.
- **The AI-downturn market trades NVDA's distance to its −50% condition** (timing matches 11/23 and 11/25 Nvidia news). VULCAN can test it by measuring the distance.
- **Bank-failure crowd = the 2024–25 prior, not 2026 data:** F-1 supports it (n=5). The book is still under $5K.
- **Crowd misses on prints lean the same way (UNPROVEN, n=2):** next points are November U3 (12/04) and November CPI (12/10).
