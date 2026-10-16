# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-10-16 (Fri) 13:5x ET — see the 10/16 block. Prior: 2026-10-15 (Thu) 08:4x ET · **Box:** LAPTOP `WilliePOwen`. No Kalshi creds here, so `kalshi.py` reads UNSIGNED (`status` rc=3, public market data). · Session: PROME-spawned (`prome-73`, Opus), **WQ-436 crash recovery**. Will's own 10/14 23:56 ET session `0ce3f089` died in the 03:08 ET machine crash with six files uncommitted. Its last tool call was 00:03 ET.

## 10/16 SESSION (Fri 13:36–13:5x ET, PROME spawn `prome-ac`, DOCKET L729 daily pull 1 of 11) — read first

- **Pulls:** PM 2026-10-16T17:36Z (53 rows) · Kalshi 17:39Z (11/11, unsigned). Oct $110 **20.5%** QUALIFIED ⇒ band run 3 **ARMED**, no Alert. Ledger `workbook/V5_OCT110_READS.tsv` (one row per business-day read).
- **Encoded on VX.tsv:** WQ-314 (b) (ORC-04 🟡) · WQ-439 A (ORC-07 48h-pair only; 🔴 on Fed NO-change-at-Oct +20.5/29h) · WQ-440 (ORC-08 RETIRED SPENT; successor PROPOSAL `PROME/inbox/2026-10-16_from-ORACLE_ORC08-successor-october-fomc-PROPOSAL.md`, not encoded).
- **Letter fixed** (second read's 3 ❌ + clearing count; settlement text verbatim §7.1, sha256 bfff6022…0b62). Two items declined to Will via PROME: Critical→Alert downgrade path; touch-before-close timing.
- Inbox 5/5 consumed (3 PROME + 2 WALTER). COR-20261016-02 receipted NO-OP. LIQUID packet sent (Oct hike −19pp/29h). KB-ORC-104/105.
- **NEXT:** 🔴 **Mon 10/19 read** (first pull of the ET day; Fri→Mon is no gap) — run 4 continues ARMED if qualified; Alert only on 3 consecutive qualified reads ≥40.0. ORC-07 has no ≤48h pair on Mon vs Fri 17:36Z unless a pull lands earlier → UNKNOWN. 🟠 any-bank-failure 84.5 thin → re-check ≥3 days (10/19+). Older NEXT items below still stand.

## CHANGES SINCE LAST SESSION (10/9 14:26Z → 10/15 12:39Z)

- **Sept CPI printed 3.7%** (Kalshi expiration_value 3.7; on 10/9 the crowd had mode 3.6 and P(3.7) ≈ 30). **Oct hike revived:** PM CLOB 18.5 → 39.5 (10/14 15:00Z) → 27.5; Gamma 31.5 · Kalshi `>4.00` 29.0 (10/9: 15.5 / 18.0).
- **Iran:** blockade-end by 12/31 59.1 (9/27) → 37.9 · next meeting by 12/31 77.5 → 37.5 · ceasefire through 10/31 79.5.
- **Oct $110 9.0%**, spread +78.5pp. ICE Active Month → Dec26 at 10/15T00:00Z (scheduled). **Kalshi Iran crude Sept settled NO, 1.957M bpd** (OPEC MOMR).
- **Any-bank failure market relisted 9/28** (Gamma 5100024): 42.0% on a $2.2K book.
- Sept U3 printed 4.2%. Mamdani rent freeze resolved YES (closed 10/06). Sept $110 and Houthi-9/30 resolved NO.

## WHAT I DID (10/15)

1. **Boot:** root/desk instructions read explicitly (spawn from PROME cwd). Corrections rc=0. No pull (other desks' dirty work in the tree).
2. **Residue recovered (6 files), each read whole and checked against the dead session's transcript and the venue APIs:** `kalshi.py` (creds optional), both watchlists (Sept → Oct rolls), ODDS_LOG +62, KALSHI_ODDS_LOG +25, spread +1. Every appended row carries ts + market id; no deletions; September pins retired with resolution records, and each resolution was re-verified (Gamma `closed=true` / Kalshi `result`).
3. **One false claim fixed:** `watchlist.tsv` said the `bank failure` watch term had been sent to WALTER; no packet existed. Sent: `AGENTS/WALTER/inbox/2026-10-15_from-ORACLE_bank-failure-watch-term.md`.
4. **kalshi.py verified in both modes:** new `scripts/test_cred_modes.py` 13/13, kills 4/4 mutants; live unsigned `status` rc=3, `market`, `pull --log` 11/11, candlesticks. Old tests 7/7 + search-coverage PASS. **Signed live round-trip UNVERIFIED** (desktop creds).
5. **Pulls 12:39Z:** PM 53 rows, Kalshi 11/11, spread +78.5. Drill-ins: Iran ×3, 10Y, Oct CPI, WTI Oct ladder, best asset, named banks; CLOB path for the Oct hike.
6. **DAEDALUS wiring ⑰ consumed** (→ processed, board_log). Item 1 DONE: VX.tsv `Producer` column. Items 2 (ORC-07 window) and 3 (ORC-08 venue) → Will via PROME with ORACLE's recommendation. Not encoded.
7. STATUS header and alerts rewritten (tables still labelled 9/27 STALE), NEXUS_BRIEF rewritten, MAINTENANCE 2026-10-15, charter Kalshi line and FILES row (C4 class, flagged to PROME).

## NEXT SESSION (dated, priority-flagged)

- **🔴 At the next DESKTOP boot: `kalshi.py status` must return rc=0.** That verifies the signed lane survived the 10/15 change. rc=3 on the desktop means the creds were not found: check `~/.config/kalshi/` first.
- **🔴 ~10/25–10/31: pin the November $110 leg in ONE edit:** pin, REGIME `v5-nov26-icewti110` (only if strike, venue and rule are unchanged, else put it to Will), relabel the Oct pin to drop `war premium`, MAINTENANCE. Read the November resolution text first.
- **🟠 If Will rules WQ-314 (b) or the ⑰ items 2/3: encode them** (VX-ORC-04 / ORC-07 / ORC-08), test first.
- **🟠 Rolls:** Hormuz 0-ships closure pin (RESOLVED since 8/01) → a live rung · Hormuz weekly wk-of-10/12 (ends 10/19) · Kalshi Oct CPI when `KXCPIYOY-26OCT` lists · Iran-crude successor (monthly).
- **🟠 Coverage sweep OVERDUE** (last completed ~9/22) + `history --write` (HISTORY.tsv is the 9/27 file; the 10/15 run never finished) + `movers`.
- **🟠 KB rows owed** (skipped 10/15, recovery scope): Sept CPI calibration datum (print 3.7 vs crowd mode 3.6) · Oct-hike CPI repricing · Iran crude 1.957M · bank relist.
- **🟠 STATUS Signal Dashboard tables are 9/27 vintage** → full rewrite at the next full session.
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (WQ-305).
- **🟡 Carried (not re-worked 10/15):** DAEDALUS F-1 Brier (bank-failure family as test case) · NEH resolution text · KB-ORC-086 sweep · TRADE_MARKS refresh · WQ-295 WATCH_FOR coverage check (the `bank failure` term was sent 10/15; the rest of the check is still owed) · archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`.

## CARRY-FORWARD

- **Push state (10/15):** this session's commit shas and the safe-push receipt are in `PROME/inbox/2026-10-15_from-ORACLE_crash-recovery-WQ436.md` and in the SendMessage to prome-73. (The 10/9 commits were pushed per the 10/9 memo.)
- **Concurrent sessions and other desks' uncommitted work are on this box** (10/15: CARL, HOMER, LABOR, SAM, LIQUID dirty). Path-scoped commits only; no pull while the tree is dirty.
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
