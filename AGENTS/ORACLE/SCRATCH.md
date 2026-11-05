# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-05 (Thu) 17:58–18:3x ET (from `date`) · **Box:** LAPTOP `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data). · Session: Claude Code, Opus 5.5; boot, then Will 18:11 ET "go" on combination watch plus full closeout. Prior: 2026-11-04.

## CHANGES SINCE 11/04

- **11/05 selloff:** S&P −4.36%, QQQ −6.49%, VIX 28.17 (vendor reads; SIG-W-20261105-055, -057). Cause not established.
- **December hike repriced:** PM 80.5 → 73.5 (read) → 63.5 (context 23:11Z); Kalshi 81.0 → 73.0 → 65.0. Step between 10:00 and 11:00 ET. KB-ORC-118.
- **October U3 whipsawed:** Kalshi `>4.1` 68.0 → 78.0 → 64.0.
- **FALCON FAL-07 RESOLVED CONFIRMED 11/04:** consistent with KB-ORC-111. ⚠️ No on-record CENTCOM; 11/2 is the first CONFIRMED date.
- **WQ-622 A:** combination watch for every desk.

## WHAT I DID (11/05)

- **Boot:** routine_check OK, corrections rc=0, inbox empty, read-cap clean.
- **Graded the 11/05 routine read:** Nov $110 16.0, state none, run 7; Dec hike 73.5, Alert held (b21145bf2a).
- **Pulls 23:11Z:** PM 52 · Kalshi 7/7, then 9/9 at 23:15Z · spread +72.5 context · `history --write` · `movers` · `trade_marks --write`.
- **VX-ORC-07:** Critical stands on WTI 36.0 → 13.0 (CLOB, in window until 2026-11-06T07Z). Fed HIKE −17.0 Alert size.
- **Combination watch:** KB-ORC-119 to 124; charter step 7a.
- **Kalshi Brent re-pinned:** T97.99, T95.99.
- **KB-ORC-118.** Packets: LIQUID, HENRY, BOND, PROME (`2026-11-05_from-ORACLE_*`).
- **My error:** the boot status used the 10:15 ET pull without a live pull and called the day "less risk". Tonight's pull reversed that. Corrected to Will. Next boot status: pull first, then characterize.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`, then grade the routine rows into `V5_NOV110_READS.tsv` and VX-ORC-12. Next ledger row is ET 11/06.
- **🔴 Fri 11/06 October jobs:** grade Kalshi U3 `>4.1` 64.0 / `>4.2` 25.0 (23:11Z, last trades) against the print, in KB-ORC-124; then roll to `KXU3-26NOV` (event open).
- **🔴 Fri 11/06 Dec hike read:** first pull of the ET date. Does 63.5 hold after the jobs print? Read cash HY for 11/05 alongside (KB-ORC-123).
- **🟠 Effective ceasefire:** any leg resolving NO = another qualifying strike.
- **🟠 Rolls:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date · `KXCPIYOY-26OCT` · December $110 at listing (expect ~11/25 by prior pattern; bump REGIME, one edit) · R3 switch 2026-11-17T01:00Z (INFERRED) resets the arming run.
- **🟠 `TRADE.md`:** regenerate tables from `TRADE_MARKS.tsv` (current); rendered tables are as of 11/04.
- **🟠 Russian diesel nomination** (BRENT/OSPREY). Do not pin without the owner's read.
- **🟠 Next coverage sweep due ≤11/11.**
- **🟠 Daily grading owner:** on WQ-599, Will Sat 11/07. Routine unchanged.
- **🟡 Combination reviews:** 11/12 bank-book-depth, ai-unwind-read, print-miss-direction · 11/16 strike-vs-oil, diplomacy-drift · 11/19 polymarket-integrity.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 At the next DESKTOP boot: `kalshi.py status` must return rc=0.**
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · WQ-295 WATCH_FOR check.

## CARRY-FORWARD

- **Push state (11/05 closeout):** `git log --since=2026-11-05 --grep=ORACLE`; receipt in Will's closeout message.
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction.
- **Cadence settled:** PROME 11/04: one read per weekday stands. The letter has no halt rule, and I did not propose one (Will 10/31: fewer rules).
- **`TRADE.md` refresh:** rerun `tools/trade_marks.py --write`, then regenerate the tables; never hand-type a vintage.
- **Standing framing (do not re-derive):**
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Never difference across segments. Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = a US strike landing on Iran (KB-ORC-111). Never difference the retired legs against the effective series.
  - A later pull on the same ET date is context (O3). A US business day is an NYSE trading day (letter §10.2).
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - Recession venues use different definitions (KB-ORC-099).
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **The hike repricing may be a risk-off reflex, not a Fed read (UNPROVEN).** Timing matches the selloff; cause not established. A jobs beat with hike odds still low would support it. LIQUID and HENRY own the reality.
- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** Another strike 61.5 by 11/30 vs $110 at 17.0. Separate contracts give no read on oil conditional on a strike. HAWK and BRENT own the reality.
- **Deal hopes may explain the 11/04 oil drop (cause NOT established).** Blockade-end 3/31/27 69.5 is the check; deal top component fell to 13.5.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book stayed dead through a −2.46% KRE day ($2.6K liq).
- **Recession gap = PM's extra NBER leg** (structural). Kalshi 4.0 vs PM 4.5 tonight.
- **Complacency decoupling:** S&P best-asset 85.5 through a −4.4% day; gold leg not re-read tonight.
