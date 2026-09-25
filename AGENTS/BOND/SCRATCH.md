# BOND SCRATCH — 2026-09-25 (Fri) ~01:03→02:xx ET: PROME item 2 (Will-directed) — FR2004 timing RESOLVED + rates-move columns with HENRY (`analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md`). Before that, 2026-09-24 THIRD session ~21:37 → ~22:1x ET, post-close (Will boot: "catch up to all live figures and new data/intel"). Second ~15:07→17:1x (owed-work + cleanup + FR2004 9/16). First `bond-b0` ~13:00→14:1x after a six-day dark gap (9/18–9/23).

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. Executable COLD.

> ## ⚠️ STATE AT WRITING
> ⛔ **POSITION: TLT Sep-30 77P ×20 — HOLD to expiry, no add (WQ-280 declined 9/24 13:17 ET), `$0`.** TERRY mark 13:51 ET: 77P bid 0.01 ⇒ ~$20 for 20 vs $231.26 basis (−91%); TLT $79.82, strike −3.5% below spot. Composite **14/35**. Counter **0**. OPEN predictions **1** (`BND-27`).
> 🟠 **FR2004 as-of 9/16 (pub 9/24 16:16 ET): long-end $144.4B −1.8 w/w; 11–21Y +1.7; >21Y −2.6.** 9/15 20Y-R pairing (join convention): TOTAL legs NOT met, 11–21Y leg met (`KB-BND-326`). ⚠️ **OPEN: `KB-BND-327`: the award settled 9/18, after the as-of; FR 2004WI captures to-be-issued positions until issue date ⇒ the weekly series MAY exclude unsettled awards ⇒ the join behind WQ-157 leg ② may be mis-windowed. UNVERIFIED. Packet → `PROME/inbox/2026-09-24_from-BOND_FR2004-9-16-read-*`.**
> 🟡 Under ACM, the 9/15→9/23 10Y rise (+11bp) is expected path (~+17bp residual) while TP fell 6.4bp (`KB-BND-325`); KW frontier 9/18 can't cross-check.

## WHAT I DID — session 3 (post-close catch-up)
1. Boot: 0 behind origin (no pull needed; HENRY/ORACLE/PROME dirty, not ours) · docket_check rc0 (verified to 9/29 only; blind span 9/30→10/15 holds only the 3 refunding rows, UNVERIFIED by tool) · corrections rc0 · boot_recompute rc1 = 5 drift findings (NEXUS_BRIEF:6 FR2004 as-of 9/9 + :13 T5YIFR 14bp; CATALYSTS rows 2/12; SCRATCH:23 teaching quote) → fixed by pattern (NEXUS vintage + distance fixed; two resolved 9/18 docket rows pruned at retention; SCRATCH line rewritten).
2. **Live: Treasury official 9/24 curve = 2nd straight fresh high** (30Y 5.47, 10Y 5.18, 5Y 5.03, 10Y real 2.85, BE down) → `KB-BND-329`, STATUS top item 0 + dashboard + gates, NEXUS §0 addendum, VX-05/14. FRED now has the 9/23 cells ⇒ old NEXT-SESSION item 1 DONE.
3. Processed LIQUID's funding answer (NONE on 9/22–9/23; 9/30 quarter-end settlement of ~$183B is the real test) → `KB-BND-330`, git mv to processed; 9/30 docket row annotated. WALTER −018/−019 (USD/JPY ~158.9, no intervention) → `KB-BND-331`, git mv to processed.
4. Matrix unchanged 14/35. No trade. No new prediction.

## WHAT I DID — session 2 (commits after `d93987642`)
1. Owed-work report to Will (chat). Boot: remote 0 behind (no pull; CARL/ORACLE dirty, not ours) · docket_check rc0 (verified to 9/29 only) · corrections rc0 · boot_recompute rc1 (14 findings).
2. `ad5405323`: STATUS: `GATE-TERRY-007` struck (TERRY closed MOOT 13:5x ET, `04c5c7aad`); DFII10 two-basis label; `KB-BND-314` marked FIXED. TRADE: Next Review pruned (seven resolved bullets). WATCH_DATES: 4 serviced rows retired, 004 25x→20x. TP re-pulled (`KB-BND-325`). **Checker fixes in `watchers.py`**: supersession inherits into deeper sub-headings plus the banner line; derived distance attributed to the NEAREST preceding gate. `check_fr2004` now uses the block guard. Selftest 15/15 (new fixtures fail on old code); closeout selftest 54/54. **14 findings → 1.**
3. FR2004 9/16 read: `KB-BND-326/327`, `VX-BND-04`, STATUS (top item 7, dashboard, matrix rows 2–3, exit §1, bottom line), `DEALER_CAPACITY.md` header-only vintage note (body NOT refreshed, said so in the header). PROME packet.

## 🔴 NEXT SESSION (dated, future-verifiable)
1. ✅ **DONE 9/24 21:37 — FRED carries 9/23 (5.40 / 2.76).** 🟡 **Fri 9/25 evening:** FRED should carry the 9/24 cells (DGS30 5.47 / DFII10 2.85 per Treasury) — the STATUS "through by 35bp" is on the Treasury cell; if boot_recompute flags it before FRED updates, that is the known two-basis split, not drift.
2. ✅ **`KB-BND-327` RESOLVED (`KB-BND-332`) → WQ-290 RULED 02:16 → `fr2004_join.py` FIXED (PRE < auction ≤ POST; selftest 14/14, mutant-checked) + leg ② re-run (`KB-BND-335`; packet PROME 9/25).** Leg ② is Will's on the corrected numbers.
3. 🔴 **Wed 9/30:** `BND-27` window closes (CCC 1093 [9/23], 7bp from 1100); quarter-end; PCE + GDP 3rd; TLT expiry (TERRY).
4. ✅ **F2 10Y–20Y vintage fix DONE 9/24 ~16:3x** (`KB-BND-328`): rank = original issue date (TreasuryDirect, cached `registry/cusip_vintage.tsv`); selftest 41/41, mutant caught; **re-base-rate 1 of 53** (2026-05-06 75.00%, a 2023 20Y — definition question to RED; NOT re-tuned). Packets RED + PROME (DOCKET L406 / HEARTBEAT_COLD:438 stale). 🔴 **10/1:** at boot, confirm the op's eligible CUSIPs resolve (a missing vintage = GAP, no verdict); then quarterly `I'` refresh · TIPS-`I'` question (PROME DOCKET L410) · degenerate-row guard · `VX-19` "disorderly".
5. 🟠 **By 9/30: `READS.tsv` declaration** (BOND has 0 rows in `PROME/registry/READS.tsv`; DAEDALUS ask).
6. 🔴 **Thu 10/1 ~16:15: as-of 9/23 = POST for the 9/23 (Wednesday) 5Y on the trade-date window** (award in that day's print, `KB-BND-332`) — the dealer half of the paired kill. **Thu 10/8: as-of 9/30 = POST for the 9/24 7Y** (and the as-shipped-join POST for the 5Y — read both; which counts rides with WQ-157).
7. 🟠 **By 10/21:** register the 10/28 FOMC curve-shape prediction with a base rate.
8. 🟡 **`check_fr2004` pattern gap:** it matches the as-of phrasing but NOT the bare "FR2004 m/d:" form (the 9/24 `NEXUS_BRIEF.md:19` case). `consumer_check --self` caught `NEXUS_BRIEF.md:19` carrying 9/9 in the LIVE 9/24 block while both boot and closeout read clean (fixed by hand 9/24). Add the `FR2004 m/d` form with a selftest fixture (this exact line).
9. 🟡 `DEALER_CAPACITY.md` BODY refresh (header carries 9/16; body is 8/26-era). `KB-BND-307`'s cadence claim is wrong (lag is 8 days); correct it with a CORRECTED status when next touching the row.

10. 🔴 **FORUM-7 co-grade (DOCKET L475; letter `AGENTS/HENRY/research/2026-09-25_FORUM-7_path-vs-premium-PREREG.md` final `bc540e071`):** P1 ACM 9/24 cell (~9/25) — HENRY grades; BOND reports nothing new unless asked · P2 KW 9/21–9/24 (~9/28–29) · **FINAL Thu 10/1 ~16:15: BOND grades D3a (FR2004 3–6Y bucket as-of 9/16→9/23: STRESS ≥ +$8.6B) + D3b (long-end TOTAL: WAREHOUSING ≥ +$6.4B / NONE ≤ +$0.5B)** → qualifier -ABSORPTION / -NO-FOOTPRINT / -D3-GAP to HENRY by the 10/2 boot. `fr2004_fetch.py` only pulls 7Y+ buckets: pull `PDPOSGSC-G3L6` explicitly (see `analysis/2026-09-25_FORUM-7_fr2004_series.py`).

## OPEN THREADS / KNOWN GAPS
- ✅ **Auction corpus refreshed 9/24 ~17:0x** (`data/auction_history_v2_prome-spawned.csv` 390→405 rows, through 9/24): all 15 new rows match TA_WS on BTC/indirect/dealer; 0 of 390 old grading cells changed; FRN rows excluded (45); 9/23 5Y regrade reproduces exactly; grader selftest 29/29. **Every coupon auction since 8/13 was already graded (KB)** — the file had simply not been re-run since 8/18, masked by the TA_WS overlay (cap reaches back to 2025-04-10, so no benchmark gap occurred). 🟡 **Re-run the refresh at each quarterly `I'` refresh (next 10/1)** — nothing else triggers it.
- 🟠 **Replies owed TO BOND:** ✅ LIQUID answered 9/24 21:3x (`KB-BND-330`) · ZHAO (custody/TIC) still owed.
- 🟡 9/2 per-tenor base-rating + the WQ-157 join used pre-`KB-BND-314`-fix pools. Not re-run; disclose if re-cited. (⚠️ Corrected 9/25: the 9/2 base-rating, `matrix_v2_base_rate.py`, uses NO FR2004 data, so the join-window fix does not touch it; only the join is subject to `KB-BND-332`.)
- ⚠️ `NEXUS_BRIEF.md` 73 KB, over the read cap if any boot reads it whole (flagged to PROME). No FR2004 line in its live 9/24 re-pin; not refreshed this session.
- ⚠️ F2 review residue ⚠️2–8 (see `analysis/2026-09-24_buyback_f2_independent-read.md`).
- TRAPS (carried): `csv.writer` re-quotes TSV fields with `"`, so use raw split/join · FRED `fredgraph.csv` TIMED OUT 9/24 ~15:2x (the API endpoint with key worked) · `DSWP10/30` discontinued (re-test 10/10) · `fetch.fred_fetch` default limit=5 · ACM xls: take the **"ACM Daily"** sheet (the first sheet is MONTHLY) · venv for `grade_auction`/`cdx_proxy`/xlrd.
- 🟡 WALTER board lag (stopped 9/21 at the first session; WALTER ran 9/24 catch-up at 13:22).

## POSITION
**TLT Sep-30 77P ×20 — HOLD to expiry, `$0`.** No add (WQ-280). Harvest/expiry are TERRY's rails.

## MAIL
**In (session 3):** LIQUID funding answer · WALTER −018/−019 — all processed. **Out:** PROME ×2 (FR2004 read + `KB-BND-327`; F2 vintage fix + stale base rate) · RED ×1 (F2 re-rank + definition question). Session 1's packets to LIQUID/ZHAO/TERRY/PROME/RED stand.
