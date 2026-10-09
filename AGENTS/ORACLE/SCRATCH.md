# ORACLE — SCRATCH (canonical session handoff)

**Last updated:** 2026-10-09 (Fri) 10:3x ET · **Box:** DESKTOP-BC6EF81, authed Kalshi lane LIVE (`kalshi.py status` rc=0) · Session: PROME-spawned (`prome-75`, Opus), L0 drain-only wake under WQ-221 (DOCKET L618): WQ-314 (b) + whole-inbox drain. Market open. ORACLE was DARK 9/28 → 10/9 (11 days).

## CHANGES SINCE LAST SESSION (9/28 13:50Z → 10/9 14:26Z)

- **Oct $110 leg 25.5 → 8.5%**, and its book deepened ($3.3K → **$41.0K liq**, $224 → $74.8K vol). CLX26 ~$94 → $91.27. Spread +51.0 → **+73.0pp**.
- **Fed Oct hike priced out:** PM 65.5 → 15.5 · Kalshi `>4.00` 69 → 18. Dec-meeting hike PM 74.5.
- Will DROPPED DOCKET L173/L175 (Forum-4 N11-ii/N13, WQ-378, 10/9): the N13 provenance-token kill ORACLE pre-accepted is ruled; no action.
- WQ-399 (10/8): the correction-receipt writer refuses an incomplete receipt.

## WHAT I DID (10/9)

1. **Boot:** HEAD 2 ahead of origin (others' commits). The tree carried other desks' dirty work, so no pull. Corrections rc=1 → **COR-20260904-02 receipted NO-OP** (WQ-399 form; artifact KB-ORC-075) → rc=0. Kalshi rc=0.
2. **Pulls** 14:26Z: PM rc=0, Kalshi 14/14, spread row +73.0pp, Kalshi Fed Oct/Dec event drill-ins.
3. **WQ-314 (b) delivered:** `analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md`: observation rule O1–O8, resets R1–R4, the resolution record, the November roll. ICE LTDs were re-verified at ice.com (Nov26 10/19 · Dec26 11/19 · Jan27 12/18). VX-ORC-04 cells + KB-ORC-102. **Levels unchanged and NOT encoded.**
4. **Inbox drain 7/7 logged** (board_log +7): 6 consumed → processed. **1 DEFERRED, left in the inbox:** DAEDALUS wiring ⑰ (VX row→command map, ORC-07 window, ORC-08 venue; items 2 and 3 change what fires).
5. L546: `kalshi.py` rounding fix + `scripts/test_mid_flag_edge.py` 7/7. WQ-305: charter quarterly re-check. WQ-399: charter receipt line. LIQUID reply packet (late: its 9/30 ask). KB-ORC-103 (Fed).
6. STATUS partial (alerts 2 and 5 only; the rest is 9/27–9/28 and labelled), NEXUS_BRIEF floor + Fed and oil bullets, MAINTENANCE 2026-10-09.

## NEXT SESSION (dated, priority-flagged)

**10/9 adds (highest first):**
- **🔴 Oct $110 reads on separate business days.** Under the proposed rule today is run=1. The **2026-10-15T00:00Z Active-Month switch resets the run.** Without near-daily pulls the bands never arm (cadence caveat named to PROME).
- **🔴 ~10/25–10/31: pin the November $110 leg** (expected to list ~10/25T04:0xZ). Do it in ONE edit: pin, REGIME `v5-nov26-icewti110` (only if strike, venue and rule are unchanged, else put it to Will), relabel the Oct pin to drop `war premium`, MAINTENANCE. Read the November resolution text first.
- **🟠 If Will approves WQ-314 (b): encode it in VX-ORC-04** and decide whether a run counter is built (`tools/`), test first.
- **🟠 DAEDALUS wiring ⑰ packet (deferred 10/9, still in inbox):** row→command map; ORC-07 window; ORC-08 venue. Items 2 and 3 change what fires, so they go to Will via PROME.
- **🟠 Roll the resolved pins `pull` flagged 10/9:** Sept 10Y/30Y, Hormuz Sept ladders (weekly, avg-transits, any-day), Sept $110 (resolution record), Hormuz on-date stale. Kalshi Sept U3 + Brent Sep-30 are finalized.
- **🟠 Sat 10/10: Sept CPI T-4 re-read** (Kalshi `>3.6%` 39.0 @ 10/9; prints 10/14).
- **🟡 2026-12-15: Kalshi gap-fill quarterly re-check** (KXCREDEFMAX · KXCCDELINQ · KXCCCHGOFF · KXFEDFACILITY; WQ-305).
- 🟡 Coverage sweep is OVERDUE (last ~9/22; due ~10/01) + `history --write` + `movers`.

**Carried from 9/28 (not re-worked 10/9):**

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

- **Push state (10/9):** this session's commit shas + the safe-push receipt are in `PROME/inbox/2026-10-09_from-ORACLE_wq314b-observation-reset-rules.md` and the SendMessage to prome-75. (9/28 commits were pushed per the 9/28 memo.)
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
