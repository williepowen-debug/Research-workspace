# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-09 (Mon) 10:5x ET (hook clock 10:50) · **Box:** desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0) · Session: Claude Code, Opus 5.5, window oracle-8f, booted 10:42 ET on PROME's commission (Will "go" 10:41 ET). **Closeout on prome-6f's WQ-249 ask (10:5x ET), after PROME accepted the fix.** Prior closeout: 2026-11-08 12:04 ET (oracle-e5, laptop).

## THIS SESSION (oracle-8f, 11/09 10:42 ET to closeout) — scope: the sync-first fix only

- **Boot:** git clean, 8 ahead / 0 behind (others' unpushed); ran-check OK (11/09 READ, routine 10:15 ET on the desktop, 166f9c649e); corrections rc 0; Kalshi signed rc 0. Inbox: only PROME's brief.
- **`tools/daily_pull.sh` sync-first, 45a7701876:** local read check first (no git if already read), then skip on a rebase/merge in progress, fetch (skip on failure), pull --rebase only when behind on a clean tree (abort + skip on failure), re-check, then read. Skips write no tracked file: one SKIP line to `~/.local/state/oracle_daily_pull.log`, exit 3. Read-first ordering was my deviation from the brief; PROME agreed.
- **Tests:** `tools/test_daily_pull_sync.sh` (055188d9af), 9 cases, 26/26; the pre-fix script fails 12. PROME reran it 10:49:59 ET, 26/0. Live no-op run under `env -i`: exit 0, state unchanged. A cron-environment fetch works on the desktop (credential helper `store`).
- **`SCHEDULED_RUNS.md`:** Contract 2, Known limits (residues a to d; PROME's cloud-push rebase note folded into c), Tests. Return packet `PROME/inbox/2026-11-09_from-ORACLE_daily-pull-sync-first.md` (f4d652ea39) + SendMessage; PROME ACCEPTED.
- **Process:** WALTER's 811962c856 committed my staged `git mv` of the brief from the shared index (R100; PROME: nothing to fix).
- **Not done this session (out of scope):** no market pulls, no grading. The 11/09 routine read is logged and ungraded.

## CHANGES SINCE 11/06 17:4x ET (oracle-e5, carried)

- **READ 2 (11/08 16:58Z): a NEW forward market.** PM "US x Iran Effective Ceasefire begins by...? (2 week pause)" was created 02:48Z 11/08. Legs: by 11/8 23.5 (about 76 for another qualifying strike on Iran's land within 14 days) · 11/15 36.0 · 11/22 48.5 · 11/30 62.5 · 12/31 80.0. Depth is thin. The rule differs from the old event: never difference the two. By-11/8 and by-11/30 are pinned. KB-ORC-132.
- **Read 2, other rows:** old legs through 11/05 and 11/06 firmed to 99.7/99.8 and 99.0/99.3 and are still open; their windows close 20:29Z 11/08 and 20:29Z 11/09 (my reading of the rule). Resolver evidence is still unreadable. WTI $110 17.0 (17.0), invade 10.5, war 2.0, Hormuz 12/31 8.5, Kalshi Brent 47.0 / 52.0 on thin books, spread +74.5. Fed Dec hike PM 76.5, Kalshi 76.0.

- **Effective ceasefire legs RESOLVED NO 11/07:** through 11/08 · 11/15 · 11/30 · 12/31, closed 03:20Z · 12:40Z · 03:31Z · 12:40Z (Gamma closed record; WALTER re-read, matches). Through 11/05 and 11/06 still open at 99.2/99.4 and 97.6/98.0 (13:46Z 11/07). KB-ORC-131.
- **The path:** 23:34Z 48.0 · 35.5 · 22.5 → second fall from 00:05Z to about 1 → pause, book 25.0/27.4 · 20.9/26.9 · 6.2/8.9 at 00:51:40Z → 0.1 by 03:30Z. My 00:51Z "snapback" was a pause (KB-ORC-130 SUPERSEDED).
- **Cause as far as established:** Trump, Friday evening: "We do minor strikes", an anti-aircraft device "knocked out" (relay 01:02:54Z). He named neither Qeshm nor Friday (card SIG-W-20261107-002). Spoken time, resolver's evidence and which strike qualified are not established.
- **Oil and escalation did not follow (13:43Z 11/07):** WTI $110 Nov 17.0 (19.5) · invade 10.5 · war 2.2 · Hormuz 12/31 9.5. Thin Kalshi Brent rungs rose 44.0 → 48.0, 47.0 → 56.0.
- **CENTCOM 08:30 ET 11/07 = Task Force Iron Gate**, a staff task force, not a strike (card 001). No visible price move around it.

## WHAT I DID (oracle-e5, 11/06 19:4x ET to 11/08 07:1x ET)

- **Boot (11/06):** full boot from files; `git pull --rebase` refused on other desks' dirty files, stayed on checkout; inbox drained (cards 053 to 056, then 11/07 001 to 003); COR-20261106-53 APPLIED; boot report to prome-bf.
- **11/06 evening, not a log row:** second spike read from the CLOB book; packet to WALTER (7de38dd855), research note section, KB-ORC-130 (029c4c7aec, 7a3d033080). NBC timing corrected after WALTER's note (c0e8f8bfd9).
- **WQ-646 A read 1 (11/07 08:43 ET, prome-bf):** pulls 13:43Z (PM 49 rows of 52 pins, the three legs closed; Kalshi 9/9 UNSIGNED; spread +73.5). Breaking packet to WALTER (8c8c3df300; fixes 5016daf67c, a87b7092d3), consumed as card 002. Read written: research note, KB-ORC-131, STATUS alert 00 (9b03984679). Sunday scope recorded (3678565270).
- **My own errors, caught and fixed before routing:** Brent "+3 and +5" took Kalshi's previous-price field instead of my 22:15Z log; one unsupported timing sentence. WALTER told; card 002 carries the right figures.
- **Closeout (11/08):** STATUS current state reconciled under WQ-653 (alerts 00 to 3, Iran and oil rows, matrix, bottom line, tensions, catalysts); resolved pins retired from `watchlist.tsv`; cards 001 to 003 processed; this SCRATCH; NEXUS_BRIEF.
- **WQ-646 A read 2 (11/08 16:58Z, pulled forward on prome-bf's message, Will's word 11:57 ET):** record 519ecd3d04 (research note read-2 section, KB-ORC-132, STATUS alert 000); WALTER packet 9b6404ed12 plus SendMessage; result to prome-bf. Second closeout: new legs pinned, STATUS reconciled, this SCRATCH, NEXUS_BRIEF.
- **Not done:** `TRADE.md` tables, coverage sweep, CENTCOM page or wire bodies (FALCON's), on-chain resolver text.

## NEXT SESSION (dated, priority-flagged)

- **✅ WQ-646 A done: four reads spent (prome-bf 11/08 12:03 ET); no timed read owed.** Hold the window idle, with no timer, until PROME asks.
- **🔴 New pins (11/08):** `us-x-iran-effective-ceasefire-by-november-8-20261108` has a nominal endDate of 20:29Z 11/08, but its 14-day period cannot complete before about 11/24, so it may stay open or drop from the plain query. If `pull` prints it RESOLVED, read the Gamma closed record before believing it: a NO means a qualifying strike landed after 02:48Z 11/08. Old 11/05 leg window closes 20:29Z 11/08; 11/06 leg closes 20:29Z 11/09. Check both outcomes.
- **🔴 Every boot:** `tools/routine_check.py`, then grade the routine rows into `V5_NOV110_READS.tsv` and VX-ORC-12. Next ledger row is ET Mon 11/09: the routine's 10:15 ET desktop pull (166f9c649e, spread +77.0pp), logged and NOT graded.
- **🟠 Sync-first, first real exercise Tue 11/10 10:15 ET:** read `~/.local/state/oracle_daily_pull.log` on each box for `SKIP` lines and their reasons. If "behind ... tracked files are modified" recurs, the date goes NOT READ for a live session to take (Known limits b). The laptop has not run the new script yet; its first run will be at its next slot after it pulls.
- **🔴 Mon 11/09:** did oil follow at Sunday's reopen? Unknowns to close: spoken time of Trump's remark, the resolver's evidence, which strike qualified. VX-ORC-07's 48h pair window ends 11/08 22:15Z with its leg closed; state unchanged until a registered step says otherwise. Re-test a second-venue strike market (`kalshi.py search "Iran strike"` was NOT CERTIFIED).
- **🟠 Rolls:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date · December $110 at listing (expect ~11/25 by prior pattern; bump REGIME, one edit) · R3 switch 2026-11-17T01:00Z (INFERRED) resets the arming run.
- **🟠 Kalshi CPI:** `KXCPIYOY-26OCT` 404; decide on pinning `KXCPIYOY-26NOV` rungs near the mode (November data, closes 12/10; OI 57.4K on `T3.8`) after HENRY's view. October CPI grade (KB-ORC-124) then rests on PM's thin book.
- **🟠 `TRADE.md`:** regenerate tables from `TRADE_MARKS.tsv`; rendered tables are as of 11/04.
- **🟠 Russian diesel nomination** (BRENT/OSPREY). Do not pin without the owner's read.
- **🟠 Next coverage sweep due ≤11/11.**
- **🟠 Daily grading owner:** WQ-599, was on Will's Sat 11/07 list; outcome not read. Routine unchanged.
- **🟡 Combination reviews:** 11/12 bank-book-depth, ai-unwind-read, print-miss-direction · 11/16 strike-vs-oil, diplomacy-drift · 11/19 polymarket-integrity · 11/20 venue-legal-risk.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · WQ-295 WATCH_FOR check.

## CARRY-FORWARD

- **Push state:** oracle-8f's commits 45a7701876, 055188d9af, f4d652ea39 and this closeout commit go by `scripts/safe-push.sh` at 11/09 closeout; the CONFIRMED receipt is in the reply to prome-6f. (11/08 closeout pushed via the laptop; receipt in the reply to prome-bf.)
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction · venue-legal-risk.
- **Cadence settled:** PROME 11/04: one read per weekday stands. The letter has no halt rule, and I did not propose one (Will 10/31: fewer rules).
- **`TRADE.md` refresh:** rerun `tools/trade_marks.py --write`, then regenerate the tables; never hand-type a vintage.
- **Standing framing (do not re-derive):**
  - **In a fast move read the CLOB book, not Gamma:** Gamma showed 3.75 at 00:48Z 11/07 against CLOB 21/34 (KB-ORC-130). Take several book reads and quote ranges; `liq` overstates near-touch depth.
  - **A closed market drops out of the plain Gamma slug query** (IndexError); `polymarket.py pull` finds it through its `closed=true` fallback and prints RESOLVED. A pin gone missing may be the event firing.
  - **Kalshi pull's printed `Δp` is the API's previous-price change, not the change from my last log row.** Difference against `KALSHI_ODDS_LOG.tsv`.
  - Quote a Fed move from the level held before it, with its basis. A read that catches a spike overstates the fall (KB-ORC-126). `end_period_ts` on Kalshi candles = period END.
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Never difference across segments. Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = no US strike landing on Iran (KB-ORC-111). Never difference the retired legs against the effective series. A resolution applies the market's rule; FALCON owns the event grade.
  - A later pull on the same ET date is context (O3). A US business day is an NYSE trading day (letter §10.2), so weekend reads are context.
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - Recession venues use different definitions (KB-ORC-099).
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`; Yahoo `ZQZ26.CBT`, `ZQF27.CBT` plus NY Fed EFFR gives HENRY's method for a unit match. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket trades: v1 retired. Use `data-api.polymarket.com/v2/trades?condition=<conditionId>&limit=500` (an `offset` parameter returned HTTP 400 on 11/07), fields `proxy_wallet`, `side`, `outcome`, `size`, `price`, `timestamp`; returns `{data: [...]}`.
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** First test 11/07: a confirmed minor strike resolved the legs while WTI $110 fell 19.5 → 17.0 and invade and war stayed flat; two thin Kalshi Brent rungs rose. Futures were shut, so Sunday's reopen is the real test. Read 2 (11/08 16:58Z): the new pause market priced about 76 for another strike in 14 days, while WTI $110 held 17.0 and invade held 10.5. The crowd prices more strikes but no supply shock. HAWK and BRENT own the reality.
- **The 11/05 Fed fall may be a risk-off reflex, not a Fed read (UNPROVEN).** Five markets moved together 10:40–10:50 ET; odds rebounded 11/06, 6 points before the print and 8 after. No driver found. LIQUID and HENRY own the reality.
- **Deal hopes may explain the 11/04 oil drop (cause NOT established).** Blockade-end 3/31/27 69.5 (11/07) is the check; deal top component 11.5.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book stayed dead through a −2.46% KRE day ($2.2K liq 11/06).
- **Recession gap = PM's extra NBER leg** (structural). Kalshi 3.0 vs PM 4.5 at 11/07 13:43Z.
- **Complacency decoupling:** S&P best-asset 87.5 (11/07) after a −4.4% day; gold leg not re-read.
- **Crowd misses on prints may lean the same way (UNPROVEN, n=2):** CPI above the mode, U3 below it. October CPI is the third point. KB-ORC-124.
