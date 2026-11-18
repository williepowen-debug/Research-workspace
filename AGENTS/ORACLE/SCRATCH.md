# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-11-18 (Wed) 10:4x ET · **Box:** desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0) · Session: Claude Code, Opus 5.5, booted 10:32 ET on PROME's registered wake (prome-6e, DOCKET line 1173, WQ-704). Letter: no pull, no push until PROME's closeout ask; message prome-6e when the packet is committed; then hold the window. Prior live session: 2026-11-12 (oracle-a6); routine-only 11/13 to 11/18.

## CHANGES SINCE 11/12

- Routine ran every weekday 11/13 to 11/18 (ran-check OK); its rows are NOT graded (see NEXT).
- Fed December went to about 97 on both venues (Kalshi 78 → 96 on 11/10, October CPI day). Iran: confirmed US self-defense strike on Qeshm 11/17; the pause by-11/8 leg resolved NO 11/17 21:30Z. Nvidia Q3 printed 11/17 (card SIG-W-20261117-019); Huang not reinstated.

## WHAT I DID (11/18)

- **Boot:** no pull (letter); dirty tree is other desks'. Ran-check OK. Corrections rc 1 → COR-20261112-03 receipted NO-OP. Kalshi SIGNED. Pulls 15:33Z (PM 51 rows, Kalshi 9; context, after the routine's 15:15Z gate read); spread +92.8.
- **WQ-704 document:** `research/2026-11-18_WQ704_market-vs-fleet-forecast-gaps.md`. 10 of 129 open fleet predictions have a priced counterpart. Largest gaps: HNS-13 ECB December (HANS 70 vs PM 98.4, −28.4, same event) and HEN-63 Fed December (HENRY 0.70 vs Kalshi 97 same letter, −27); third France HNS-14 (30 vs 9.5, partial, cannot tell). AEO-17 likely NO-VERDICT on print timing (OND RONI prints about early January; INFERRED). No investment implication. KB-ORC-140 (December read), KB-ORC-141 (ranking), KB-ORC-142 (Iran pause leg).
- **Packets (committed, carve-out ①):** PROME delivery; TERRY (no implication, expects NO CARD); information to HENRY, HANS, AEOLUS, LABOR, RED, MIDAS.
- **Stale KB (PROME 11/16, Will 11/16 23:16 ET):** 13 rows past Stale_By: retired 7 (128, 129, 131 STALE; 132, 134, 135, 138 SUPERSEDED), refreshed 6 (099 rule re-read; combos 119, 120, 122, 123, 124). Consumer check 90.5 → 92.5: 0 certified stale.
- **Watchlist:** by-11/8 pause pin retired with a resolution record.
- **Inbox:** 5 of 5 processed (`git mv` to each lane's `processed/`).
- **Commit hashes:** see `git log --oneline -3 -- AGENTS/ORACLE/` (one session commit plus the packet commits).

## NEXT SESSION (dated, priority-flagged)

- **🔴 Every boot:** `tools/routine_check.py`; grade routine rows into `V5_NOV110_READS.tsv` (⚠️ SKIPPED 11/13 to 11/18), VX-ORC-04, VX-ORC-12; December read in the KB-ORC-140 form (venues + futures, both caveats).
- **🔴 WQ-704 follow-ups:** watch for TERRY's answer (expected NO CARD); if Fed or ECB venues fall under about 85 before 12/9 or 12/17, re-run the comparison (doc §6).
- **🟠 Iran:** HAWK/BRENT packet on the pause leg ⚠️ SKIPPED 11/18 (KB-ORC-142 carries it); pause by 11/30 42.0 (−14.5 d1).
- **🟠 Hormuz weekly re-pin** (pinned weekly resolved 11/16) and **0-ships closure** context row: re-search.
- **🟠 Coverage sweep:** due by 11/18, ⚠️ SKIPPED; run next session.
- **🟠 Full STATUS rewrite:** tier tables are 11/06 vintage under the 11/12 and 11/18 alerts.
- **🟠 Rolls:** December $110 at listing (~11/25; bump REGIME) · Kalshi Brent month-end 11/30.
- **🟠 Nomination to VULCAN via PROME:** successor market (PM `next-ceo-of-nvidia`, Kalshi `KXNVDACEO-29JAN`); blockade-end by 12/31.
- **🟠 Kalshi CPI:** pin `KXCPIYOY-26NOV` rungs after HENRY's view. **`TRADE.md`** tables (rendered 11/04). **Russian diesel** nomination (BRENT/OSPREY).
- **🟡 Combination reviews:** 11/26 bank-book-depth · 11/30 strike-vs-oil, diplomacy-drift (REVERSED this week), ai-unwind-read · 12/11 print-miss-direction · polymarket-integrity and venue-legal-risk (review dates 11/19, 11/20 per their rows).
- **🟡 ~12/10:** October CPI market fallback resolution (KB-ORC-136) → HENRY. **2026-12-15:** Kalshi gap-fill quarterly re-check (WQ-305).
- **🟡 Carried:** DAEDALUS F-1 Brier (bank-failure family) · NEH PDF unread · KB-ORC-086 sweep · WQ-295 WATCH_FOR check · WQ-599 daily-grading owner (unowned per the ruling record).

## CARRY-FORWARD

- **Push state:** 11/18 commits are LOCAL ONLY (PROME's letter: no push until its closeout ask). Find them with `git log origin/master..HEAD -- AGENTS/ORACLE/`. Earlier: ab06498512 and the 11/12 closeout commit were to go by `safe-push.sh` at the 11/12 closeout; check `git log origin/master..HEAD` before assuming.
- **Combination themes (`combo:` in KB Notes):** strike-vs-oil · diplomacy-drift · polymarket-integrity · bank-book-depth · ai-unwind-read · print-miss-direction · venue-legal-risk.
- **Cadence settled:** PROME 11/04: one read per weekday stands. No halt rule proposed (Will 10/31: fewer rules).
- **`TRADE.md` refresh:** rerun `tools/trade_marks.py --write`, then regenerate the tables; never hand-type a vintage.
- **Fed futures method (verified 11/11 and 11/18):** Dec average = 100 − ZQZ26; post = (31 × avg − 9 × EFFR) / 22; unit check ZQX26 = EFFR. Full precision via `.venv/bin/python` yfinance. One 0.005 tick = 0.7bp. NY Fed EFFR API `markets.newyorkfed.org/api/rates/unsecured/effr/last/3.json`.
- **WQ-704 method (re-usable):** open fleet rows = `AGENTS/*/workbook/PREDICTIONS.tsv` with Status OPEN/ACTIVE/PENDING/LIVE/WATCH/blank; pair only after reading each market's rule text; grade SAME / PARTIAL / SUPERSET / DERIVED; show the gap now and at registration (PM CLOB `prices-history`, own logs). Kalshi has no December 2026 ECB event (KXECB newest is September 2025). Kalshi `search` hits its page cap: a zero is not an absence; use `kalshi.py series --category` and the `/events?series_ticker=` API.
- **Standing framing (do not re-derive):**
  - **In a fast move read the CLOB book, not Gamma** (KB-ORC-130). `liq` overstates near-touch depth.
  - **A closed market drops out of the plain Gamma slug query**; `pull` finds it via `closed=true` and prints RESOLVED. A pin gone missing may be the event firing.
  - **Kalshi pull's printed `Δp` is the API's previous-price change**, not the change from my last log row.
  - Quote a Fed move from the level held before it, with its basis (KB-ORC-126). `end_period_ts` on Kalshi candles = period END.
  - Fed: hiked 25bp 9/16 to 3.75–4.00% (KB-ORC-083); HELD 10/28 (KB-ORC-109). **December priced path is ORACLE's (WQ-671 A):** venue odds + futures cross-check, both caveats.
  - **October 2026 CPI YoY does not exist at BLS**; PM's October market resolves on its fallback (KB-ORC-136).
  - v4 is history; ⛔ never compute `82.5 − 100`. v5 at $110 since 9/24 (WQ-260). Current segment `v5-nov26-icewti110`.
  - PM "ceasefire" = no US strike landing on Iran (KB-ORC-111). Never difference retired legs against the pause series. A resolution applies the market's rule; FALCON owns the event grade.
  - A later pull on the same ET date is context (O3). Weekend reads are context.
  - Hormuz legs resolve on the IMF PortWatch PRINT (KB-ORC-079). Kalshi mid only when `result` empty AND OI > 0 (KB-ORC-086). Recession venues use different definitions (KB-ORC-099, re-read 11/18).
  - Three published σ remain retracted (KB-ORC-064). CME unreachable: do NOT re-attempt; Yahoo + NY Fed EFFR. Treasury par == DGS10 unconfirmed (BOND/TERRY).
  - Polymarket trades: `data-api.polymarket.com/v2/trades?condition=<conditionId>&limit=500`. `prices-history`: `curl -A "Mozilla/5.0"` with startTs/endTs, fidelity 60 to 360.
  - Never `pull --log --force` to log new pins. Kalshi `pull` has no double-log guard.
  - **Never type a clock stamp from narrative:** this session wrote 11:0x into seven packets at 10:45 wall clock and corrected them before commit.
  - Git: `rebase --continue` refuses while ANY tracked file is unstaged; `rebase --abort` silently discards a foreign dirty file.
- `ledger_staleness` counts `HISTORY.tsv` but prints no row for it (PROME's tool; reported, not patched).

## OPEN HYPOTHESES

- **Fleet registered forecasts go stale against deep markets (n=2, 11/18):** HEN-63 and HNS-13 were 8 to 12 under the market at registration and 27 to 28 under a week later, unre-marked. Test: the 12/9 and 12/17 outcomes, and whether other desk rows registered against deep markets show the same drift.
- **The crowd separates limited strikes from a supply shock (UNPROVEN, strengthening):** strikes 11/07, 11/13–11/17 (Qeshm confirmed 11/17) while WTI $110 Nov fell 17.0 → 2.7. HAWK and BRENT own the reality.
- **Diplomacy drift reversed (11/18):** blockade end −15.5, senior meeting −16.0, deal −7.0 over 7 days. Watch the Trump–Xi–Putin trilateral (Iran "may" come up, BBC).
- **Bank-failure crowd = the 2024-25 prior, not 2026 data.** Test in F-1 (Brier). Book still under $5K (11/18).
- **Recession gap = PM's extra NBER leg** (structural).
- **Crowd misses on prints may lean the same way (UNPROVEN, n=2);** next point November U3 (12/04).
- **Huang-exit pricing reacted, did not lead (11/11–11/12).**
