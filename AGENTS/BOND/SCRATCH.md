# BOND SCRATCH — 2026-10-01 (Thu) 12:50→13:1x ET PROME spawn `prome-0c` (DOCKET L410 · L478 · L532), PHASE 1 of 2. Phase 2 = the FR2004 grade + the official 10/1 curve, on PROME's re-ping after ~16:15 ET.

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. Previous SCRATCH (9/29 Will session) = `git show HEAD~1:AGENTS/BOND/SCRATCH.md` (or the last commit touching this file before today's).

> ## ⚠️ STATE AT WRITING (13:07 ET 10/1)
> ⛔ **POSITION: duration-short sleeve = TLT Oct-16 82P ×1 (TERRY's card) + TBT 10 sh. Sep-30 77P GONE (sold 9/30). NO-ADD (WQ-280).** TLT $77.93 / TBT $42.03 [13:02 ET, live].
> Composite **15/35** (unchanged) · Counter **0** · **OPEN predictions 0** (`BND-30` TRUE · `BND-31` TRUE today; tally 16T·13F·1V) · 10/28 FOMC row owed by 10/21.
> **OFFICIAL 9/30 (`KB-BND-372`): 30Y 5.64 (+5; since 2002-07-08; run 61) · 20Y 5.68 · 10Y 5.29 (> 2007 high; since 2002-05-14) · 5Y 5.09 · 2Y 4.88 · DFII10 2.93 · BE 2.36. US rose ALONE 9/29–9/30.** HY 312 · CCC 1179 · IG 84 [9/30].
> **Kill: NOT FIRED. FR2004 as-of 9/23 prints ~16:15 TODAY; letter + outcome table pre-stated in `PROME/inbox/2026-10-01_from-BOND_phase-1-L410-L532-L478-preprint.md` §1.**

## 🔴 PHASE 2 — on PROME's re-ping after ~16:15 ET (do in this order)
1. **Grade:** `cd AGENTS/BOND && ../../.venv/bin/python analysis/2026-10-01_wq291_grade.py` → rc 0 MET/NOT MET · rc 3 GAP (re-run 16:30/17:00/18:00) · rc 2 GAP (revision/mismatch — Will's call via PROME WQ row). **Grade ONLY on the memo §1 table: 3–6Y alone governs (≥ $56.586B inclusive); long-end TOTAL + 6–7Y printed as info via `monitors/fr2004_fetch.py`, never graded; NO AMBIGUOUS-BY-BUCKET branch (superseded 9/26 by WQ-291).**
2. **If MET:** KB row; packets → TERRY (card: exit-all-duration-shorts REC, riders verbatim) + PROME (WQ row for Will's [Approve]); matrix row 2 3→4, row 1 4→5 ⇒ 17/35; token `kill=MET-REC@2026-10-01` on STATUS/THESIS/TRADE in ONE edit; THESIS v1.2.11 + CHANGELOG; NEXUS_BRIEF re-pin. **No action.** **If NOT MET:** KB row; STATUS kill line; THESIS kill bullet note (no bump unless text changes); no matrix move. Either way: FORUM-7 D3a/D3b numbers → HENRY (info packet); `DEALER_CAPACITY.md` body refresh (deferred to this print); `check_fr2004` vintage on all surfaces (boot_recompute).
3. **Official 10/1 curve** (Treasury CSV 202610; posts ~16:00–16:30): KB row, STATUS rates rows + gates + bottom line. Comparators by computation only (FRED full series; `since.py` pattern in this session's scratch).
4. **F2 10Y–20Y buyback op 10/1 (results ~14:15):** `boot_recompute` carrier will show OWED → read + route to RED per the F2 protocol.
5. Closeout `addendum` (second ending today) — or `standard` if it is the day's last.

## WHAT I DID — phase 1 (12:50→13:1x ET)
- **Boot:** origin 0 ahead (no pull needed) · docket_check rc0 (proven through 10/8; blind span 10/9→10/22, hand-checked 9/28 → no coupon in 10/9–10/19; 10/21 20Y-R + 10/22 5Y TIPS docketed) · corrections rc0 · boot_recompute rc1 = T5YIFR "15bp" drift on STATUS + NEXUS_BRIEF (fixed: 14bp) + TRY-FIRE-004 date gate (77P, gone) · OPEN 2 both DUE → resolved.
- **L0 drain 9/9 (every sender):** HANS rows + CORRECTION · WALTER R3 (→ PROME packet `8d2b82879`, adopt 7 / decline 9) · NEXUS (no-op) · PROME WQ-332 (ack) · WALTER -004/-006/-009/-018 (`KB-BND-378/379/380`, board_log ×4). All → `processed/`.
- **L410:** acceptance written first → `grade_auction.py` TIPS I′ suppressed + degenerate guard → independent Opus read found 2 ❌ (A3, A6) → fixed + re-tested on its counterexamples (fix NOT re-read) → re-freeze + 10/6–10/8 bars + rule (a)/(b)/(c) in `AUCTION_HEALTH.md` (`KB-BND-376/377`). My acceptance draft wrongly called 8 zero-direct rows "nominal 2Y"; all 8 are FRNs (MEMORY n+1).
- **L532:** WQ-317 page (fork-drafted, BOND spot-checked every US cell vs Treasury CSV, MOF + ACM at primary) → UNDETERMINED (`KB-BND-375`).
- **Curve/credit:** official 9/30 (`KB-BND-372`), credit 9/30 (`KB-BND-381`); BND-30/31 TRUE (`KB-BND-373/374`).
- **Surfaces:** STATUS rotated (snapshot `domain/sources/2026-10-01_STATUS_full-snapshot_pre-refresh-rotation.md`, crc32 735109674) + rewritten top/dashboard/gates/matrix keys/scoreboard/bottom line · NEXUS_BRIEF re-pinned · CATALYSTS: 9/30 + 10/1-refresh rows → archive, +10/6 tie-band row, +10/8 VX-19 row · TRADE dated note (77P gone) · THESIS status line (OLD fire confirmed) + position cell, CHANGELOG dated note, NO bump · VX-05/-01 refreshed · 15 KB rows past Stale_By flipped/extended · RECEIPT · MEMORY n+1 · charter FILES row.
- **FLOW:** no-op (no transmission channel confirmed or changed; WQ-317 = UNDETERMINED).
- **Closeout (phase 1, tier HEAVY — tooling changed):** C1 STATUS ✅ (composite re-summed 4+3+2+3+1+1+1 = 15) · C2 KB/VX ✅, FLOW no-op · C3 BND-30/31 resolved, owed FOMC row by 10/21 · C4 THESIS factual lines + CHANGELOG dated note, NO bump, token unchanged · C5 CATALYSTS ✅ (twin: 9/30 removed, 10/1 row rewritten) · C6 TRADE dated note ✅ · C7 this file · C8 RECEIPT + board_log ×4 ✅ · C9 MEMORY n+1 (local; no auto-memory written) · C10 charter FILES row (grade_auction) ✅ · C11 NEXUS_BRIEF re-pin rewritten ✅. **consumer_check (--superseded ×4 I′ bars): zero certified-stale; 🟠 candidates looked at — cross-desk hits (NEXUS STATUS_COLD, PROME DOCKET L316/ORCH_LOG) are dated records of the 9/15 grade, correct as history, no packet; BOND's own PROTOCOL.md:68 carried the 9/2 bars as 'Current bars' → REPLACED with the 10/1 bars + rule (a).**

## 🔴 NEXT SESSION (dated)
- **10/1 phase 2** — above.
- **Mon 10/5 latest / before 10/6 13:00:** grade_auction tie-band alignment (CATALYSTS 10/6 row; acceptance first) — or grade 10/6–10/8 by hand on the frozen bars and disclose.
- **10/6 3Y · 10/7 10Y-R · 10/8 30Y-R:** grade on the 10/1 frozen bars (`AUCTION_HEALTH.md` 10/1 block). 10/7–10/8 can fire row 1's ⇒5.
- **10/8:** VX-BND-19 'disorderly' qualifier (define with base rate or retire) · FR2004 as-of 9/30 (row 3's 2nd look).
- **By 10/21:** 10/28 FOMC curve-shape prediction with base rate (OPEN = 0).
- Carried: swap-spread validation (after the above; Will's 9/28 ruling) · `check_fr2004` bare-pattern gap · charter step-7 verb vs kb_lint · CATALYSTS at 71% of budget (rotate the 10/1 FR2004 row once graded).
- ⚠️ The grader fix of 10/1 is TESTED, not independently re-read. If a consequential grade ever depends on the degenerate path, get a reader first.

## OPEN THREADS / KNOWN GAPS
- LIQUID owns the funding leg; the 9/23 fire's funding window is UNGRADED by ruling.
- KW 9/29 companion for BND-30 (~10/9–10/13) — record beside, never re-grade.
- ACGB after 9/23 (RBA F2 weekly, ~10/2) and gilt 9/30 par — optional addenda to the WQ-317 page, not owed.
- TRAPS (carried): `csv.writer` re-quotes TSV (raw split/join) · `python3 -c` fails in this shell (script file) · `fetch.fred_fetch` default limit=5 · ACM xls sheet "ACM Daily" · venv for grade_auction/cdx_proxy/fr2004_fetch/xlrd · **MOF jgbcme.csv column 15 = 30Y, 16 = 40Y** · never type a clock.

## POSITION
Duration-short sleeve: **TLT Oct-16 82P ×1** (TERRY card `MGMT-TLT82P-OCT16`, Will's A/B/C by 10/14) + **TBT 10 sh**. NO-ADD (WQ-280). BOND carries no posture on the 82P.

## MAIL
**In 10/1:** HANS ×2 · WALTER R3 · NEXUS · PROME WQ-332 · WALTER lane ×4 — all processed. **Out:** `PROME/inbox/2026-10-01_from-BOND_R3-watch-for-verdicts-adopt-decline.md` (`8d2b82879`) · `PROME/inbox/2026-10-01_from-BOND_phase-1-L410-L532-L478-preprint.md` (+ SendMessage COMPLETION to prome-0c).
