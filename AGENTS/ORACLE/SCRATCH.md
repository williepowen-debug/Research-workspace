# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-10-21 (Wed) 22:2x–22:4x ET (from `date`) · **Box:** LAPTOP `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data). · Session: PROME-spawned by prome-56 (Claude Code, Opus), catch-up wave 2, Tier 1. Prior: 2026-10-16 (prome-ac, L729 read 1) · 2026-10-15 (prome-73, WQ-436 crash recovery).

## 10/21 SESSION — read first

- **Pulls 2026-10-22T02:22Z** (22:22 EDT = first pull of ET Wed 10/21 ⇒ the 10/21 business-day read under letter O3): PM 53 rows · Kalshi 11/11 · spread +75.0pp.
- **Oct $110 13.5%**, liq $32.6K QUALIFIED. **10/19 and 10/20 were NOT read** (no ORACLE pull between 10/16T17:36Z and 10/22T02:22Z; PROME's prompt said 10/19 was consumed — the ledger and ODDS_LOG show no such read). Gap 10/16 → 10/21: 2 business days strictly between / 3 by difference ⇒ run 4 or 1 (letter ⚠️39 OPEN, §8.3); state none under both.
- **WQ-453 encoded** (commit 6a0d46555): ORC09 → **VX-ORC-11** (VX-ORC-09 is the best-asset row; label only) · DEF + ROLLCARRY → letter §8 + VX-ORC-04 Alert cell.
- **WTI $100 Oct leg RESOLVED YES 2026-10-20T10:55Z** (Gamma id 4936103). $110 CLOB swung 24.0 → 8.5 → 15.0 on 10/20 (context only). VX-ORC-07 🔴 → 🟠 on that CLOB pair.
- Inbox 3/3 consumed (PROME wq453 + WALTER -20261019-003, -20261021-025). KB-ORC-106/107/108.

## NEXT SESSION (dated, priority-flagged)

- **🔴 Thu 10/22 L729 read** (first pull of ET 10/22), then every business day to Fri 10/30. Each read: `polymarket.py pull --log` + `kalshi.py pull --log` + `tools/disruption_supply_spread.py`, append `workbook/V5_OCT110_READS.tsv`, grade VX-ORC-04 (≥40.0 ×3 Alert) **and VX-ORC-11** (≥50.0 on 2 consecutive business days; retires at the 10/28 FOMC — record the decision, Critical if a hike is announced). A 10/22 read also gives VX-ORC-07 an ODDS_LOG pair ≤48h.
- **🔴 ~10/25 04:0xZ: November $110 leg lists → pin in ONE edit** (pin, REGIME `v5-nov26-icewti110` only if strike/venue/rule unchanged, relabel the Oct pin to drop `war premium`, MAINTENANCE). Read the November resolution text first. A fired October state (none today) is carried per WQ-453 ROLLCARRY.
- **🔴 At the next DESKTOP boot: `kalshi.py status` must return rc=0** (signed lane after the 10/15 change).
- **🟠 For Will via PROME (in the 10/21 memo):** ⚠️39 gap counting (rec: strictly-between) · DEF residue (do reads <40 inside the Critical-clearing run count toward Alert's clearing; fail-closed until ruled).
- **🟠 Rolls:** Hormuz 0-ships closure pin RESOLVED since 8/01 → live rung · Hormuz weekly wk-of-10/12 (ended 10/19, `⏮stale-date`) · ceasefire-through top leg (ends 10/23) · Kalshi Oct CPI when `KXCPIYOY-26OCT` lists · Iran-crude successor (Kalshi Oct13 leg settled; the spread tool suppresses it).
- **🟠 Coverage sweep OVERDUE** (last ~9/22) + `history --write` (HISTORY.tsv is the 9/27 file) + `movers`. Not run 10/21 (catch-up scope).
- **🟠 STATUS Signal Dashboard tables are 9/27 vintage** → full rewrite at the next full session (the 10/21 block carries the moved rows).
- **🟠 KB rows still owed from 10/15:** Sept CPI calibration datum (print 3.7 vs mode 3.6) · Iran crude 1.957M.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH resolution text · KB-ORC-086 sweep · TRADE_MARKS refresh · WQ-295 WATCH_FOR check · archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`.

## CARRY-FORWARD

- **Push state (10/21):** commit shas and the safe-push receipt are in `PROME/inbox/2026-10-21_from-ORACLE_catchup-wave2-WQ453-encode-L729-read.md` and the SendMessage to prome-56. (10/16 and 10/15 pushes per their memos.)
- **Concurrent sessions and other desks' uncommitted work are on this box** (10/21: YURI dirty; AEOLUS, FLG, GIBBS, HANS, BRENT, WALTER sessions concurrent). Path-scoped commits only; no pull while the tree is dirty.
- **Standing framing (do not re-derive):**
  - Fed hiked 25bp to 3.75–4.00% on 2026-09-16 (KB-ORC-083). Venue-vs-futures only in expected bp at a matched time (KB-ORC-100).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260).
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079).
  - Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086).
  - **`PINNED BUT NOT FOUND` → query Gamma `closed=true` before calling it delisted** (the bank family's not-founds were all resolutions, KB-ORC-101).
  - Recession venues use different definitions (KB-ORC-099); the RED correction packet is still unconsumed.
  - Three published σ remain retracted (KB-ORC-064). CME FedWatch unreachable: do NOT re-attempt `WebFetch`. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket `prices-history` returns **empty for long spans at fidelity=60** (n=0 for month-long windows 9/27). Use ≤~10-day windows or ORACLE's ODDS_LOG. Python `urllib` gets **403** from CLOB (user-agent), so use `curl`.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).
- DAEDALUS owes the three-window vocabulary; profile clock → 2026-10-20.

## OPEN HYPOTHESES

- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Four 2026 instances priced 55–73% for multi-month windows while the realized pace implied ~90%+. Test in F-1 (Brier). Caveat: all $4–14K books.
- **Iran: three axes.** Deadline priced as leverage; talks odds rising (next meeting by 12/31 77.5); near-term tempo legs thin. HAWK owns the reality.
- **Recession gap = PM's extra NBER leg** (structural, not decomposed).
- **NEH: complacency or a very high bar?** 82.5% flat through a hike cycle; resolution text unread.
- **8/27 complacency decoupling:** S&P best-asset 56.5 (+2.0/7d); the registered tell (gold retaking the lead) has not fired.
