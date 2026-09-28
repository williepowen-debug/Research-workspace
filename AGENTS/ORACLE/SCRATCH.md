# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-09-28 (Mon) 09:5x ET · **Box:** DESKTOP, authed Kalshi lane LIVE (`kalshi.py status` rc=0) · Session: PROME-spawned (`prome-7f`, Tier-1 follow-up), DOCKET L299 October roll + whole-inbox drain. Market open.

## CHANGES SINCE LAST SESSION (9/27 12:3x ET → 9/28 09:45 ET)

- October WTI ladder deepened a little ($9.1K → $19.9K event). The Oct $110 leg is 25.5% on $224 vol / $3.3K liq, still THIN.
- **US–Iran talks jumped:** the meeting-by-10/31 leg went 50.0 → 75.5 and the 9/30 leg 38.0 → 66.5 (the 9/30 leg is thin). Fed Oct hike: Kalshi 63 → 69, PM 64.5 → 65.5.

## WHAT I DID

1. **Boot:** 0 behind origin. PROME's two state files were dirty (not mine), so no pull. Corrections rc=1: COR-20260927-05/06 receipted **NO-OP** (ORACLE never carried the WAL/$108M claims) and then rc=0. Kalshi rc=0.
2. **Pull** 13:48Z (PM 52, Kalshi 14/14), then the last Sept-segment spread row **+75.1pp** (supply 1.4%).
3. **DOCKET L299, all three items:** ① Oct $110 **pinned** (id 4936102). ② Month-roll rule named first: it **stays v5** per WQ-260 record row 260, and the roll opens a new REGIME segment `v5-oct26-icewti110`. ③ Active Month **verified at ICE**: Nov26 LTD 10/19 ⇒ the switch is at **8:00 PM ET Wed 10/14**, not ~10/16. ⛔ **Found:** the October market resolves on **ICE WTI (CLL)**, while September resolved on CME. That goes to Will via PROME (rec: stays v5). First Oct-segment row **+51.0pp** @ 13:49Z, THIN.
4. **v5 threshold PROPOSAL** to PROME (in the memo and the VX-ORC-04 Alert cell, **NOT encoded**): arm after 3 consecutive reads with liq ≥$5K; Alert ≥40% sustained 3 reads; Critical ≥60% sustained 3 reads, or YES.
5. **Inbox drain, 4/4:** the CATO NB5 relabel is done (§3 of the 9/27 analysis + KB-ORC-101: "depth" → lifetime volume per instance). SIG-W-20260927-004/005/006 noted. board_log +4, all moved to processed.
6. STATUS partial update (alert 0 movers, alert 5 oil), NEXUS_BRIEF oil line + catalysts, VX-ORC-04, MAINTENANCE 2026-09-28.

## NEXT SESSION (dated, priority-flagged)

0. ✅ **DONE 9/28: DOCKET L299** (see WHAT I DID 3). **Owed next:** re-read the Oct $110 leg on 3 separate days before any mark (thin), and watch the **10/14 20:00 ET** Active-Month step. Superseded text follows: Market exists: `will-wti-reach-110-in-october-2026` (24.5% @9/27, $9.1K event, **thin**). ⚠️ **Pinning it auto-rolls the supply leg** (`SUPPLY_PREFIX` match in `tools/disruption_supply_spread.py`) **without a REGIME bump**. So in ONE edit: pin + bump `REGIME` (v4 precedent: every month roll bumped it; a fresh month-start contract is structurally higher) + a MAINTENANCE entry. Verify the Active-Month switch (~10/16; CLX26 last trade 10/20) at the contract. The thin October book affects the spread's quality; state it on the first row.
1. **🔴 ~Tue 9/29: Iran deadline.** Re-read the ceasefire / blockade-end / next-meeting ladders with `event` (the dashboard top leg is wrong for all three). The 9/30 legs resolve Wed.
2. **🟠 Every pull: re-search for a relisted any-bank successor** (`search "bank fail"` + Gamma `public-search` active). Past relist gaps: 58d / 10d / 3d. When one lists, pin it AND send WALTER the `bank failure` watch phrase (PROME's 9/27 condition). Monday 9/28 open read of the named-bank legs was asked "if you run again".
3. **🟠 By 2026-10-04: WQ-295 WATCH_FOR coverage check**. Locate ORACLE's WATCH_FOR list (not in `AGENTS/ORACLE/`; try WALTER's watch registry / `SIGNAL_INTAKE.md`) and confirm each registered trigger (CLAUDE.md CROSS-AGENT SIGNALS table) has a phrase. Reported to PROME as SKIPPED.
4. **🟠 9/30–10/02 resolutions:** 10Y/30Y Sept ladders, Houthi 9/30, Hormuz Sept ladders (avg transits, any-day), ceasefire-9/30, Saudi on-date (event ends 9/30), Kalshi Brent Sep-30, Kalshi Sept U3 (10/02). Roll or retire each.
5. **🟠 ~10/01 coverage sweep** (`--domain` first) + `history --write` (not run 9/27) + `movers`.
6. ✅ **v5 thresholds PROPOSED 9/28** (awaiting Will's word; encode only on it). Old text: (VX-ORC-04 Alert/Critical UNSET), on the October leg. DAEDALUS PR#6 ① due **9/30**.
7. **🟠 Sat 10/10: Sept CPI T-4 re-read** (like-for-like vs August's 63.0 / 25.0 / 10.0).
8. **🟠 Kalshi Fed pins keyed to the 4.00% upper bound**: re-key after the next move. Pin `KXFED-26OCT >4.25` again if the differenced read is wanted (not in this pull).
9. **🟠 Roll the Kalshi Iran-crude context column** monthly (OI 0: never a probability).
10. **🟠 KB-ORC-086 sweep** (50.0-mid citations off settled Kalshi rungs). Open check.
11. **🟠 DAEDALUS F-1**: Brier per resolved market. **New test case: the bank-failure family** (4 YES resolutions in 2026 with logged pre-failure prices).
12. **🟡 Read NEH's resolution text.** 🟡 Demote the four Kalshi gap-fills to a quarterly re-check (flag PROME; CLAUDE.md edit). 🟡 Spec-has-implementation prototype owed to DAEDALUS. ⚪ Archive `DIVERGENCE_2026-07-09.md` + `OPEN_THREADS_2026-07-09.md`.
13. **🟡 TRADE_MARKS refresh** (`tools/trade_marks.py --write`), 7+ sessions behind.

## CARRY-FORWARD

- **Push state (9/28):** see the 9/28 commit + safe-push receipt in PROME/inbox/2026-09-28_from-ORACLE memo. **Prior:** `db4c7a588`, `0ccb6c527`, `c1d4b4a98`, `d59ecb124` PUSHED. safe-push CONFIRMED HEAD `d59ecb124` on origin/master 2026-09-27 ~12:4x ET. The completion-pass commit is pushed next; its receipt is in the reply to Will.
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
