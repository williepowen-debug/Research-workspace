# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-09-27 (Sun) 12:3x ET (16:3xZ) · **Box:** DESKTOP, authed Kalshi lane LIVE (`kalshi.py status` rc=0) · Session: boot 12:20 ET at Will's ask ("catch up … pull updated numbers … report back"), then a PROME-commissioned bounded read (`prome-09`, Nano Banc), closed out at PROME's WQ-249 ask.

## CHANGES SINCE LAST SESSION (9/25 ~01:2x ET → 9/27)

- **Nano Banc (Irvine CA, $736M) failed Fri 9/25**, the 6th US failure of 2026. PROME/REGINALD/CREED investigation live today (`PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md`).
- **Tape:** Fed Oct hike PM 66.5 → 64.5 / Kalshi 67 → 63 · Sept CPI `>3.6` 46 → 36.5 mid · recession PM 10.5 → 8.5 · ceasefire-thru-9/30 85.5 → 94.5 · next US–Iran meeting by 12/31 69 → 77.5 · October WTI ladder listed ($110 24.5%).

## WHAT I DID

1. **Boot:** 0 behind origin; WALTER + PROME + CREED dirty ⇒ no pull (none needed). Corrections rc=0 (1 ALL-row broadcast warn, COR-20260925-13, warn-never-block). Kalshi rc=0.
2. **Dual-venue pull** 16:20Z: PM 52 rows, Kalshi 14/14, v5 row 3 **+78.2pp** (Sept leg decay). Iran ×3, Fed count, CPI, 10Y, 30Y, end-rate and named-bank event drill-ins.
3. **Bank-failure read (PROME packet 12:24 ET):** NONE priced on either venue; the any-bank Dec-31 market resolved YES on Nano, reactive (19:08 ET first repricing trade), priced below the 2026 base rate on a $4.1K book. → `analysis/2026-09-27_bank-failure-markets.md`, KB-ORC-101, PROME packet. **PROME consumed it and accepted it as delivered** (note added: Sunwest release 19:45 ET; regulator time stays unverified). Commits `db4c7a588`, `0ccb6c527`.
4. **Watchlist:** any-bank pin retired, and the 7/02, 7/22, 8/27 "delisted/relisted" notes corrected to **resolutions** · Hormuz weekly → wk-of-9/28.
5. **WQ-295 reply to PROME:** `CADENCE: WEEKLY`. **WATCH_FOR coverage check SKIPPED** (list not located), carried below.
6. **Closeout:** STATUS full rewrite (14.2 KB), NEXUS_BRIEF rewrite, this file.
7. **Closeout completion pass (Will: "did you run the full ORACLE close out?" → no, then "go ahead", ~13:30 ET):** NEXUS `STATUS commit:` placeholder → `c1d4b4a98` · `history --write` 8,223 rows / 52 markets · **KB overdue sweep: 4 SUPERSEDED (005/030/031 → 101; 082 → 084/091) + 30 STALE** (ACTIVE past own Stale_By, not re-verified) + 9/27 notes on 093/098 · MAINTENANCE 2026-09-27 entry · auto-memory `finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect` extended (n=2, HOT, index hook updated; `memory_index_check --slug` 0 blocking; MEMORY.md 71% of byte cap) · orphan check: 0 mine outside my dir besides the memory pair · claim check 8 files clean (incl. PROME DOCKET/GATES/WILL_QUEUE) · consumer check 66.5→64.5: 0 🔴, 72 bare-needle 🟠, none the same series ⇒ no packets.

## NEXT SESSION (dated, priority-flagged)

0. **🔴 Mon 2026-09-28: DOCKET L299, the October WTI $110 roll.** Market exists: `will-wti-reach-110-in-october-2026` (24.5% @9/27, $9.1K event, **thin**). ⚠️ **Pinning it auto-rolls the supply leg** (`SUPPLY_PREFIX` match in `tools/disruption_supply_spread.py`) **without a REGIME bump**. So in ONE edit: pin + bump `REGIME` (v4 precedent: every month roll bumped it; a fresh month-start contract is structurally higher) + a MAINTENANCE entry. Verify the Active-Month switch (~10/16; CLX26 last trade 10/20) at the contract. The thin October book affects the spread's quality; state it on the first row.
1. **🔴 ~Tue 9/29: Iran deadline.** Re-read the ceasefire / blockade-end / next-meeting ladders with `event` (the dashboard top leg is wrong for all three). The 9/30 legs resolve Wed.
2. **🟠 Every pull: re-search for a relisted any-bank successor** (`search "bank fail"` + Gamma `public-search` active). Past relist gaps: 58d / 10d / 3d. When one lists, pin it AND send WALTER the `bank failure` watch phrase (PROME's 9/27 condition). Monday 9/28 open read of the named-bank legs was asked "if you run again".
3. **🟠 By 2026-10-04: WQ-295 WATCH_FOR coverage check**. Locate ORACLE's WATCH_FOR list (not in `AGENTS/ORACLE/`; try WALTER's watch registry / `SIGNAL_INTAKE.md`) and confirm each registered trigger (CLAUDE.md CROSS-AGENT SIGNALS table) has a phrase. Reported to PROME as SKIPPED.
4. **🟠 9/30–10/02 resolutions:** 10Y/30Y Sept ladders, Houthi 9/30, Hormuz Sept ladders (avg transits, any-day), ceasefire-9/30, Saudi on-date (event ends 9/30), Kalshi Brent Sep-30, Kalshi Sept U3 (10/02). Roll or retire each.
5. **🟠 ~10/01 coverage sweep** (`--domain` first) + `history --write` (not run 9/27) + `movers`.
6. **🟠 Propose v5 thresholds to PROME** (VX-ORC-04 Alert/Critical UNSET), on the October leg. DAEDALUS PR#6 ① due **9/30**.
7. **🟠 Sat 10/10: Sept CPI T-4 re-read** (like-for-like vs August's 63.0 / 25.0 / 10.0).
8. **🟠 Kalshi Fed pins keyed to the 4.00% upper bound**: re-key after the next move. Pin `KXFED-26OCT >4.25` again if the differenced read is wanted (not in this pull).
9. **🟠 Roll the Kalshi Iran-crude context column** monthly (OI 0: never a probability).
10. **🟠 KB-ORC-086 sweep** (50.0-mid citations off settled Kalshi rungs). Open check.
11. **🟠 DAEDALUS F-1**: Brier per resolved market. **New test case: the bank-failure family** (4 YES resolutions in 2026 with logged pre-failure prices).
12. **🟡 Read NEH's resolution text.** 🟡 Demote the four Kalshi gap-fills to a quarterly re-check (flag PROME; CLAUDE.md edit). 🟡 Spec-has-implementation prototype owed to DAEDALUS. ⚪ Archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`.
13. **🟡 TRADE_MARKS refresh** (`tools/trade_marks.py --write`), 7+ sessions behind.

## CARRY-FORWARD

- **Push state:** `db4c7a588`, `0ccb6c527`, `c1d4b4a98`, `d59ecb124` PUSHED. safe-push CONFIRMED HEAD `d59ecb124` on origin/master 2026-09-27 ~12:4x ET. The completion-pass commit is pushed next; its receipt is in the reply to Will.
- **Concurrent sessions live on this box** (PROME `prome-09`, REGINALD, CREED, WALTER). Path-scoped commits only.
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
