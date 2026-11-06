# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-06 (Fri) 15:25–15:4x ET (from `date`) · **Box:** DESKTOP `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0). · Session: Claude Code, Opus 5.5, `oracle-5d`; PROME assignment under Will's 15:24 ET word, bounded, $0. Prior: 2026-11-05.

## CHANGES SINCE 11/05

- **October jobs:** +165,000 vs about +65,000; revisions +84,000; U3 4.1 (SIG-W-20261106-001, -017).
- **December hike:** PM 63.5 (11/05 23:11Z) → 77.5; Kalshi 65.0 → 78.0. About 6 points before the print.
- **AI bubble round-tripped** to 7.55. Cash HY 348 [11/05], +16bp.
- **VX-ORC-07:** WTI pair aged out at 07Z.

## WHAT I DID (11/06)

- **Boot:** routine_check OK, corrections rc=0, Kalshi rc=0 (first desktop check of the owed item). Inbox: 2 WALTER INFO cards, both processed.
- **Pulls 20:26Z:** PM 52 · Kalshi 9/9 · spread +70.5 context · `history --write` · `movers` · `trade_marks --write`.
- **Graded:** 11/06 reads into `V5_NOV110_READS.tsv` (19.0, run 8, none) and VX-ORC-12 (77.5, Alert held). VX-ORC-07 Critical → Alert. Those are the only state touches.
- **Verified the hike at about 78:** PM, Kalshi, futures within 1bp. KB-ORC-125, -126, artifact `research/2026-11-06_dec-hike-verification.md`. Reuters sentence NOT verified; cause of 11/05 NOT established.
- **U3 graded and rolled:** finalized 4.1. KB-ORC-124. `KXU3-26NOV-T4.1`, `T4.2`.
- **New theme:** `venue-legal-risk`, KB-ORC-127, review 11/20.
- **Commits:** 03d40e3b28 (work), cf0ef74f6b (packets to PROME, HENRY, LIQUID, BOND, LABOR). PROME filed the receipt.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`, then grade the routine rows into `V5_NOV110_READS.tsv` and VX-ORC-12. Next ledger row is ET Mon 11/09.
- **🟠 Effective ceasefire:** any leg resolving NO = another qualifying strike.
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

- **Push state (11/06 closeout):** see the closeout receipt to PROME; `git log --since=2026-11-06 --grep=ORACLE`.
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
  - Polymarket `prices-history`: use `curl -A "Mozilla/5.0"` with startTs/endTs and fidelity 60 or 180 (urllib gets 403).
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged and blames merge conflicts; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **The 11/05 fall may be a risk-off reflex, not a Fed read (UNPROVEN).** Five markets moved together 10:40–10:50 ET. The odds rebounded on 11/06, 6 points before the print and 8 after. No driver found. LIQUID and HENRY own the reality.
- **Possibly the crowd separates limited strikes from a supply shock (UNPROVEN).** Another strike 60.0 by 11/30 vs $110 at 20.0. Separate contracts give no read on oil conditional on a strike. HAWK and BRENT own the reality.
- **Deal hopes may explain the 11/04 oil drop (cause NOT established).** Blockade-end 3/31/27 71.5 is the check; deal top component 12.5.
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book stayed dead through a −2.46% KRE day ($2.2K liq 11/06).
- **Recession gap = PM's extra NBER leg** (structural). Kalshi 3.0 vs PM 4.5 at 11/06.
- **Complacency decoupling:** S&P best-asset 87.5 after a −4.4% day; gold leg not re-read.
- **Crowd misses on prints may lean the same way (UNPROVEN, n=2):** CPI above the mode, U3 below it. October CPI is the third point. KB-ORC-124.
