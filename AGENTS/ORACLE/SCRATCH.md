# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-06 (Fri) 17:15–17:4x ET (from `date`) · **Box:** DESKTOP `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0). · Session: Claude Code, Opus 5.5; Will's 17:08 ET close-refresh word via prome-51, bounded, no spawns. Prior: 2026-11-06 15:25 ET.

## CHANGES SINCE 15:4x ET

- **Effective ceasefire legs broke from 16:04 ET:** 59.0 · 40.0 · 28.5 (20:26Z) → 31.5 · 27.0 · 16.0 (22:15Z); book 22:23Z 30/33 · 26/29 · 15/16; 11/15 swung 31.5 to 36. Oil, invade, war and Hormuz legs did not follow. Cause NOT established.
- **VX-ORC-07:** Alert → Critical (11/15 pair, WQ-439 A).
- **Everything else near flat:** PM hike 76.5, Kalshi 78.0, WTI $110 19.5, spread +71.0.

## WHAT I DID (11/06 close refresh)

- **Boot:** `git pull --rebase` refused on other desks' dirty files, stayed on checkout (origin not ahead at 17:15 ET). routine_check OK. Inbox and WALTER lane empty. Read BOARD cards 033–046: only 033 routed here, already processed; read 043 for Iran.
- **Correction:** COR-20261106-35 receipted NO-OP (ORACLE holds no put/call figure).
- **Pulls 22:15Z:** PM 52 · Kalshi 9/9 · spread +71.0 context · `history --write` · `movers` · `trade_marks --write`. All later pulls on ET 11/06: context only. Gate reads untouched.
- **Ceasefire drill-in (charter hot-theater rule):** KB-ORC-128, `research/2026-11-06_ceasefire-break.md`. Three web searches, one blog page read in part.
- **Packets:** HAWK, BRENT, FALCON, PROME (`2026-11-06_from-ORACLE_ceasefire-legs-break-after-close.md`). No ask, so no doorbell.
- **Not done:** `TRADE.md` tables, coverage sweep, futures settles (Yahoo last only), wire desks, CENTCOM, UKMTO.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`, then grade the routine rows into `V5_NOV110_READS.tsv` and VX-ORC-12. Next ledger row is ET Mon 11/09.
- **🔴 Effective ceasefire, first thing Mon 11/09:** did the 16:04 ET break hold, and did oil follow at Sunday's reopen? Any leg resolving NO = another qualifying strike. Find the cause if a wire reached it; re-test on a second venue (`kalshi.py search "Iran strike"` was NOT CERTIFIED). The routine runs weekdays only, so no weekend pull exists unless a session runs one.
- **🟠 Rolls:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date · December $110 at listing (expect ~11/25 by prior pattern; bump REGIME, one edit) · R3 switch 2026-11-17T01:00Z (INFERRED) resets the arming run.
- **🟠 Kalshi CPI:** `KXCPIYOY-26OCT` 404; decide on pinning `KXCPIYOY-26NOV` rungs near the mode (November data, closes 12/10; OI 57.4K on `T3.8`) after HENRY's view. October CPI grade (KB-ORC-124) then rests on PM's thin book.
- **🟠 `TRADE.md`:** regenerate tables from `TRADE_MARKS.tsv` (current); rendered tables are as of 11/04.
- **🟠 Russian diesel nomination** (BRENT/OSPREY). Do not pin without the owner's read.
- **🟠 Next coverage sweep due ≤11/11.**
- **🟠 Daily grading owner:** on WQ-599, Will Sat 11/07. Routine unchanged.
- **🟡 Combination reviews:** 11/12 bank-book-depth, ai-unwind-read, print-miss-direction · 11/16 strike-vs-oil, diplomacy-drift · 11/19 polymarket-integrity · 11/20 venue-legal-risk.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · WQ-295 WATCH_FOR check.

## CARRY-FORWARD

- **Push state (11/06 close refresh):** see the receipt to PROME; `git log --since=2026-11-06 --grep=ORACLE`.
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction · venue-legal-risk.
- **Cadence settled:** PROME 11/04: one read per weekday stands. The letter has no halt rule, and I did not propose one (Will 10/31: fewer rules).
- **`TRADE.md` refresh:** rerun `tools/trade_marks.py --write`, then regenerate the tables; never hand-type a vintage.
- **Standing framing (do not re-derive):**
  - Quote a Fed move from the level held before it, with its basis. A read that catches a spike overstates the fall (KB-ORC-126). `end_period_ts` on Kalshi candles = period END.
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Never difference across segments. Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = a US strike landing on Iran (KB-ORC-111). Never difference the retired legs against the effective series.
  - A later pull on the same ET date is context (O3). A US business day is an NYSE trading day (letter §10.2).
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - Recession venues use different definitions (KB-ORC-099).
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`; Yahoo `ZQZ26.CBT`, `ZQF27.CBT` plus NY Fed EFFR gives HENRY's method for a unit match. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket trades: v1 retired. Use `data-api.polymarket.com/v2/trades?condition=<conditionId>&limit=500`, fields `proxy_wallet`, `side`, `outcome`, `size`, `price`, `timestamp`; returns `{data: [...]}`.
  - During a repricing, take several book reads before quoting a level (11/15 leg 31.5, 36.0, 31.5 inside 8 min on 11/06). `liq` overstates near-touch depth.
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **The 11/05 fall may be a risk-off reflex, not a Fed read (UNPROVEN).** Five markets moved together 10:40–10:50 ET. The odds rebounded on 11/06, 6 points before the print and 8 after. No driver found. LIQUID and HENRY own the reality.
- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** Another strike about 73 by 11/30 vs $110 at 19.5, wider after the 16:04 ET break; invade and war flat. A thin-book push fits equally well. Separate contracts give no read on oil conditional on a strike. HAWK and BRENT own the reality.
- **Deal hopes may explain the 11/04 oil drop (cause NOT established).** Blockade-end 3/31/27 71.5 is the check; deal top component 12.5.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book stayed dead through a −2.46% KRE day ($2.2K liq 11/06).
- **Recession gap = PM's extra NBER leg** (structural). Kalshi 4.0 vs PM 4.5 at 11/06 22:15Z.
- **Complacency decoupling:** S&P best-asset 87.0 after a −4.4% day; gold leg not re-read.
- **Crowd misses on prints may lean the same way (UNPROVEN, n=2):** CPI above the mode, U3 below it. October CPI is the third point. KB-ORC-124.
