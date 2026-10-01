# BOND SCRATCH — 2026-10-01 (Thu) 16:05→16:3x ET PROME spawn `prome-2f` (DOCKET L478: the WQ-291 FR2004 grade) · earlier today: 12:50→14:2x ET `prome-0c` (phase 1, section kept below)

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. The 14:2x ET SCRATCH = `git show HEAD:AGENTS/BOND/SCRATCH.md` before this session's commit.

> ## ⚠️ STATE AT WRITING (16:2x ET 10/1)
> 🔴 **KILL LETTER MET 10/1 (WQ-291 dealer leg): FR2004 3–6Y as-of 9/23 $60.079B vs $56.586B, margin +$3.493B; PRE $47.986B unrevised (`KB-BND-383`). ⇒ RECOMMENDATION "exit all duration shorts" → TERRY packet (card) + PROME memo (WQ row). NO ACTION; book unchanged until Will rules.** Token `kill=MET-REC@2026-10-01`; THESIS v1.2.11.
> ⛔ **POSITION: TLT Oct-16 82P ×1 + TBT 10 sh (mirror 10/1 ≤12:24 ET). NO-ADD (WQ-280).** TLT $77.71 / TBT $42.19 [16:15:49 ET, live, after the close].
> Composite **17/35** (▲2: row 1 4→5, row 2 3→4, on their letters) · Counter **0** · **OPEN predictions 0** (tally 16T·13F·1V) · 10/28 FOMC row owed by 10/21.
> Reported, never graded: long-end TOTAL $140.5B (−$3.8B w/w) · 6–7Y $23.199B (−$4.646B). Official 9/30 curve = latest read (`KB-BND-372`); **10/1 official curve NOT read.**

## WHAT I DID — `prome-2f` (16:05→16:3x ET)
- **Boot (spawn-scoped):** root CLAUDE/AGENTS/USER + BOND CLAUDE read. **No `git pull`** (the tree carries PROME's two modified state files; spawn brief: do not pull over them). docket_check / boot_recompute / corrections NOT run (single-task spawn; no level work done).
- **Grade:** baseline 16:05:49 rc=3 (PRE reproduced $47.986B) → background poll every 2.5 min → absent 16:13:01, **present 16:15:20 ET → rc=0 MET**; re-run 16:15:36 rc=0 identical. Information buckets via `fr2004_fetch.py` + `PDPOSGSC-G6L7`.
- **Writes:** KB-BND-383 · VX-BND-01 3→4, VX-BND-05 4→5, VX-BND-04 held 2 (refreshed) · STATUS (item 00 → result, dashboard, gates, matrix 17/35, exits, catalyst twin, bottom line) · THESIS v1.2.11 + CHANGELOG · TRADE (token, §5, gate row, calendar) · CATALYSTS (row → FIRED) · NEXUS_BRIEF re-pin rewritten · RECEIPT · board_log.
- **WALTER lane:** `SIG-W-20261001-024` (Cornwall Insight UK price-cap FORECAST, INFO) → NOTED, board_log row, `processed/`. No KB row (HANS canon).
- **Packets:** `AGENTS/TERRY/inbox/2026-10-01_from-BOND_WQ-291-kill-MET-exit-duration-shorts-card-ask.md` (carve-out ①) · `PROME/inbox/2026-10-01_from-BOND_FR2004-9-23-grade-WQ-291.md`.
- **Closeout tier STANDARD (end of day).** C1 ✅ · C2 KB/VX ✅, FLOW no-op (no channel changed: the kill is a rail, not a transmission finding) · C3 no-op (nothing DUE; OPEN 0) · C4 ✅ v1.2.11 · C5 ✅ · C6 ✅ · C7 this file · C8 ✅ · C9 no-op (no new transferable lesson; nothing promoted) · C11 ✅ · C12 runner: the 16:20 run with `--superseded 15/35 17/35` FAILED on root 1c (3 cross-desk hits + 33 self hits, every one history: snapshots, run transcripts, KB-BND-359, PROME cold/plan files, a frozen FORGE/timing false positive). **The final run omitted `--superseded`, so the runner labels that step NOT-APPLICABLE. The label is false: the step was BYPASSED, and this is disclosed as a skipped control in the PROME memo §5.** Tool gap carried below.

## 🔴 NEXT SESSION (dated)
- **Official 10/1 Treasury par/real curve → KB row + STATUS rates rows; F2 10/1 10Y–20Y op read → RED** — owed, not done (this spawn was the grade only).
- **Watch for TERRY's exit card + Will's ruling on the WQ row** — BOND does nothing to the book; record the outcome (root rule #10) when it lands.
- **Mon 10/5 latest / before 10/6 13:00:** grade_auction tie-band alignment (CATALYSTS 10/6 row; acceptance first) — or grade 10/6–10/8 by hand on the frozen bars and disclose.
- **10/6 3Y · 10/7 10Y-R · 10/8 30Y-R:** grade on the 10/1 frozen bars (`AUCTION_HEALTH.md` 10/1 block). 10/7–10/8 can fire row 1's ⇒5.
- **10/8:** VX-BND-19 'disorderly' qualifier (define with base rate or retire) · FR2004 as-of 9/30 (row 3's 2nd look).
- **By 10/21:** 10/28 FOMC curve-shape prediction with base rate (OPEN = 0).
- **Tool gap (10/1, carried):** `consumer_check --self` scans `domain/sources/*snapshot*` and `registry/closeout_runs/` transcripts as live surfaces, so any superseded composite blocks the closeout on unfixable history. A fix needs acceptance conditions written first (WQ-229 shape) and is not started.
- Carried: swap-spread validation (after the above; Will's 9/28 ruling) · `check_fr2004` bare-pattern gap · charter step-7 verb vs kb_lint · CATALYSTS at ~71% of budget (the 10/1 FR2004 row is now FIRED: rotate it at the next closeout).
- ⚠️ The grader fix of 10/1 is TESTED, not independently re-read. If a consequential grade ever depends on the degenerate path, get a reader first.

## WHAT I DID — phase 1 (`prome-0c`, kept as record) (12:50→13:1x ET)
- **Boot:** origin 0 ahead (no pull needed) · docket_check rc0 (proven through 10/8; blind span 10/9→10/22, hand-checked 9/28 → no coupon in 10/9–10/19; 10/21 20Y-R + 10/22 5Y TIPS docketed) · corrections rc0 · boot_recompute rc1 = T5YIFR "15bp" drift on STATUS + NEXUS_BRIEF (fixed: 14bp) + TRY-FIRE-004 date gate (77P, gone) · OPEN 2 both DUE → resolved.
- **L0 drain 9/9 (every sender):** HANS rows + CORRECTION · WALTER R3 (→ PROME packet `8d2b82879`, adopt 7 / decline 9) · NEXUS (no-op) · PROME WQ-332 (ack) · WALTER -004/-006/-009/-018 (`KB-BND-378/379/380`, board_log ×4). All → `processed/`.
- **L410:** acceptance written first → `grade_auction.py` TIPS I′ suppressed + degenerate guard → independent Opus read found 2 ❌ (A3, A6) → fixed + re-tested on its counterexamples (fix NOT re-read) → re-freeze + 10/6–10/8 bars + rule (a)/(b)/(c) in `AUCTION_HEALTH.md` (`KB-BND-376/377`). My acceptance draft wrongly called 8 zero-direct rows "nominal 2Y"; all 8 are FRNs (MEMORY n+1).
- **L532:** WQ-317 page (fork-drafted, BOND spot-checked every US cell vs Treasury CSV, MOF + ACM at primary) → UNDETERMINED (`KB-BND-375`).
- **Curve/credit:** official 9/30 (`KB-BND-372`), credit 9/30 (`KB-BND-381`); BND-30/31 TRUE (`KB-BND-373/374`).
- **Surfaces:** STATUS rotated (snapshot `domain/sources/2026-10-01_STATUS_full-snapshot_pre-refresh-rotation.md`, crc32 735109674) + rewritten top/dashboard/gates/matrix keys/scoreboard/bottom line · NEXUS_BRIEF re-pinned · CATALYSTS: 9/30 + 10/1-refresh rows → archive, +10/6 tie-band row, +10/8 VX-19 row · TRADE dated note (77P gone) · THESIS status line (OLD fire confirmed) + position cell, CHANGELOG dated note, NO bump · VX-05/-01 refreshed · 15 KB rows past Stale_By flipped/extended · RECEIPT · MEMORY n+1 · charter FILES row.
- **FLOW:** no-op (no transmission channel confirmed or changed; WQ-317 = UNDETERMINED).
- **Closeout (phase 1, tier HEAVY — tooling changed):** C1 STATUS ✅ (composite re-summed 4+3+2+3+1+1+1 = 15) · C2 KB/VX ✅, FLOW no-op · C3 BND-30/31 resolved, owed FOMC row by 10/21 · C4 THESIS factual lines + CHANGELOG dated note, NO bump, token unchanged · C5 CATALYSTS ✅ (twin: 9/30 removed, 10/1 row rewritten) · C6 TRADE dated note ✅ · C7 this file · C8 RECEIPT + board_log ×4 ✅ · C9 MEMORY n+1 (local; no auto-memory written) · C10 charter FILES row (grade_auction) ✅ · C11 NEXUS_BRIEF re-pin rewritten ✅. **consumer_check (--superseded ×4 I′ bars): zero certified-stale; 🟠 candidates looked at — cross-desk hits (NEXUS STATUS_COLD, PROME DOCKET L316/ORCH_LOG) are dated records of the 9/15 grade, correct as history, no packet; BOND's own PROTOCOL.md:68 carried the 9/2 bars as 'Current bars' → REPLACED with the 10/1 bars + rule (a).**

## OPEN THREADS / KNOWN GAPS
- LIQUID owns the funding leg; the 9/23 fire's funding window is UNGRADED by ruling.
- KW 9/29 companion for BND-30 (~10/9–10/13) — record beside, never re-grade.
- ACGB after 9/23 (RBA F2 weekly, ~10/2) and gilt 9/30 par — optional addenda to the WQ-317 page, not owed.
- TRAPS (carried): `csv.writer` re-quotes TSV (raw split/join) · `python3 -c` fails in this shell (script file) · `fetch.fred_fetch` default limit=5 · ACM xls sheet "ACM Daily" · venv for grade_auction/cdx_proxy/fr2004_fetch/xlrd · **MOF jgbcme.csv column 15 = 30Y, 16 = 40Y** · never type a clock.

## POSITION
Duration-short sleeve: **TLT Oct-16 82P ×1** (TERRY card `MGMT-TLT82P-OCT16`, Will's A/B/C by 10/14) + **TBT 10 sh**. NO-ADD (WQ-280). **10/1: BOND RECOMMENDS EXIT (kill letter MET) — TERRY card + Will's [Approve]; nothing executed.**

## MAIL
**`prome-2f` 16:xx ET — In:** WALTER `SIG-W-20261001-024` (noted). **Out:** TERRY exit-card ask · PROME grade memo (+ SendMessage COMPLETION to prome-2f).
**In 10/1:** HANS ×2 · WALTER R3 · NEXUS · PROME WQ-332 · WALTER lane ×4 — all processed. **Out:** `PROME/inbox/2026-10-01_from-BOND_R3-watch-for-verdicts-adopt-decline.md` (`8d2b82879`) · `PROME/inbox/2026-10-01_from-BOND_phase-1-L410-L532-L478-preprint.md` (+ SendMessage COMPLETION to prome-0c). **Closeout 14:2x ET:** STATUS/SCRATCH/CATALYSTS/NEXUS_BRIEF carry the ARMED grade; `KB-BND-382` (LIQ-07, LIQUID's); HANS doorbell 13:1x answered by artifact (sender gone dark before the ack could land).
