# BOND SCRATCH — 2026-09-17 (Thu) ~08:2x–09:1x ET. PROME WQ-184 L0 spawn (`prome-ae`) on **DOCKET L404 + L401**. Markets OPEN. **CLOSED OUT AT PROME'S INSTRUCTION BEFORE THE 1:00 PM TIPS PRINT — the grade is OWED to the fresh session spawned ~13:00.** Rewritten clean at closeout.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. **Durable learnings → `MEMORY.md`; permanent evidence → `workbook/`. This file is disposable and must be executable COLD.**

> ## ⚠️ STATE AT HANDOFF
> ⏳ **THE 9/17 10Y TIPS-R `91282CRE3` $19B GRADE IS OWED AND UNEXECUTED (DOCKET L404).** Bars frozen 9/9 (`742d4533e`), reproduced 08:2x, committed pre-print at `ceaef61e6`: **ind <56.08 AND dlr >17.79 · cover BTC <2.20 · medians ind 66.94 / dlr 10.64 / BTC 2.40 · n=12 (2024-09-19 → 2026-07-23)**. ⛔ **No `I'` bar; TIPS NEVER count toward the downgrade counter (stays 0); no add re-arm; no trade action.** Procedure = `analysis/2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md` §7. Run `../../.venv/bin/python3 monitors/grade_auction.py --cusip 91282CRE3` (venv — outside it the tool fails loud on numpy, by design). A stop >2.438 = highest 10Y TIPS stop since 2008-10-08 (n=139, computed). **Confound pre-registered: day-after-FOMC + Brent −4% like-for-like ⇒ real-yield-UP, breakeven-DOWN tape; a soft print has a non-structural explanation.**
> 🔑 **SEP GRADED (`KB-BND-293`):** falsifier NOT triggered (SEP median terminal 4.125 vs ≥~5.00) — **and the DOVISH branch's predicted "large repricing" did NOT occur** (5Y +3.3bp, 10Y +1.0, 30Y −1.5, BE −5bp, vendor). Curve holds a path 60–85bp above the Fed's median ⇒ market view, not guidance view. **Official curve leg + `BND-25`/`BND-26` grade on the 9/16 H.15 cells (~16:15 ET 9/17) — grader saved `analysis/2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py`.**
> 🟢 **`BND-29` TRUE** (DFII10 2.55/2.60/2.60/2.62 = 4-of-4 ≥2.50; 70% hit). **OPEN: 3** (`BND-25/26/27`). `BND-26` sits at EXACTLY 4.95 on the 9/15 cell, one day pre-window.
> ⬜ **F2 PER-OP CARRIER BUILT (L401)** — `monitors/buyback_f2.py` + `registry/f2_reads.tsv`, every boot via `boot_recompute`. **Zero arrears** (9/15 TIPS + 9/17 7Y–10Y ops are OUT of the letter's scope). Next in-scope op **9/24 20–30Y**. Blind read LANDED before closeout: 10 ❌ fixed same session (selftest 31/31), 7 ⚠️ declared as residue in the pre-print record §5 — read that block before touching the tool.
> ⛔ **Position UNCHANGED: TLT puts HOLD, no add, `$0`. Composite 12/35 (15th consecutive). Downgrade counter 0.**
> ✅ **Read cap: STATUS 69% · CATALYSTS 74% (both rotated this session) · MEMORY 89% — rotate-tier, NOT rotated; next session that adds to MEMORY must rotate first.**

## CHANGES SINCE LAST HANDOFF (9/15)

1. **Pre-print record committed `ceaef61e6` at 08:42:21 ET** (auction 13:00): TIPS bars verified frozen at git and reproducing; SEP grade; F2 scope. Then closed out early on PROME's cost instruction.
2. **SEP graded against the pre-registered falsifier** — NOT triggered, AND the dovish branch failed its own prediction. FOMC +25bp to 3.75–4.00, 12–0, IORB 3.90 [9/17]. THESIS → **v1.2.7** + CHANGELOG. ⚠️ Brent figure CORRECTED by PROME before the print (−7.05% was the BZ=F Nov→Dec roll; like-for-like −3.98%) — carried as a dated correction on every surface that quoted it.
3. **F2 carrier built and wired** (`KB-BND-294`): metric = newest-quartile-of-eligibles share, ON-THE-RUN iff >50% strict, base rate 0/52; selftest 22/22 (v1 failed 6 on first run — the schedule loop; fixed) → **31/31 after the coldreader's 10 ❌ were fixed** (window-expiry alarm, same-date merge guard, ledger-row validity incl. RED's `processed/` move, OWED/GAP split, unclassified ⇒ gap, `--op` scope guard, rc=2, ops∪details enumeration). Issuer PDF (9/9) parsed per-page, three rows sanity-checked at FiscalData. Ledger seeded with the 9/10 read.
4. **`BND-29` TRUE; `KB-BND-293…297`; 33-row KB Stale_By sweep** (13 STALE · 15 CONFIRMED · 4 SUPERSEDED · C-36 label extended to 10/28).
5. **STATUS rotated 100%→69%** (4 blocks verbatim, crc32 `1463914424`) and rewritten to the 9/15–16 frontier; **CATALYSTS 99%→74%** (4 fired rows rotated crc32 `713924898`; 3 accreted rows compacted, full text crc32 `1917918431`); carrier row added; **2Y/5Y/7Y bars RE-FROZEN 9/17 in the venv — 54.82 / 60.27 / 57.24, UNCHANGED.**
6. 🔴 **`monitors/AUCTION_HEALTH.md` §3d counter cell read 2 through this boot** — the 9/15 grade reset it on STATUS/SCRATCH and not on the rail. Fixed to 0. (Same class as `KB-BND-287`, one surface further out.)
7. **Hyperscaler IG-share allocation DECLINED** under its own second-miss rule (`KB-BND-297`) — no free primary for the deal-level denominator (re-test: none scheduled; re-open only if a free deal-level source appears).
8. FR2004 re-pulled 09:1x: **the 9/9 as-of is NOT YET PUBLISHED** (latest 9/2; long-end TOTAL $144.7B, −$7.1B w/w while 11-21Y built). re-test: 2026-09-18 with the join.
9. Inbox drained (PROME 9/16 item; WALTER SIG-021 LOG_ONLY `KB-BND-295`). NEXUS_BRIEF re-pinned 9/17. WATCH_DATES: 5 rows retired, 9/24 F2 row added.

## 🔴 NEXT SESSION (dated, future-verifiable)

0. 🔴 **9/17 ~13:02 ET — GRADE THE TIPS-R** (STATE AT HANDOFF, bullet 1). Write `analysis/2026-09-17_GRADE_TIPS-R_91282CRE3.md`, a rolling-table row in `monitors/AUCTION_HEALTH.md`, one KB row, the STATUS catalyst row + BOTTOM LINE line, retire the WATCH_DATES 9/17 row. Send PROME the grade (L404 consumer read).
1. 🟡 **9/17 ~14:15 ET — 7Y–10Y buyback op result** (cap $4B, 10 eligible): OUT of F2 scope; one KB context row, no packet to RED; `python3 monitors/buyback_f2.py --pending` (system python is fine for this tool).
2. 🟠 **9/17 ~16:15 ET (or next boot) — run `analysis/2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py`** → resolve `BND-25` (belly-led) and check `BND-26` (1y1y ≥4.95 on 9/16 kills it); re-run the SEP curve leg on officials (`KB-BND-293` re-test: 9/18).
3. 🔴 **9/18 — DELIVER THE FR2004 WEEKLY JOIN (WQ-157 leg ②, DOCKET L271).** The `I'` leg is LIT (9/15) and the paired kill cannot be evaluated until it exists. Premises closed 9/14 (n=244; pooling defensible); **build UNSTARTED.** Also pull the 9/9 as-of (unpublished 9/17).
4. 🔴 **9/24 1:40 PM — 20Y–30Y buyback op ≥$4B = the FIRST in-scope F2 read of the carrier:** `buyback_f2.py --op 2026-09-24` → packet to `AGENTS/RED/inbox/` same day → ledger row. Then 10/1 · 10/8 · 10/15 · 10/27 · 11/4.
5. 🟠 **9/22 · 9/23 · 9/24 — 2Y/5Y/7Y** on the re-frozen bars (unchanged); counter re-arms at the 2Y.
6. 🟠 **`BND-27`**: CCC 1085 [9/15], 15bp from 1100, closing ~5bp/session. Watch, don't act.
7. 🟡 **PROME's DOCKET row for the carrier** lands once the carrier files are verified on origin (PROME said so 9/17); confirm at the next boot.
8. 🟡 **`buyback_f2.py` ⚠️ residue** (4 items, declared in the pre-print record §5): the quartile-cut precision label · the ops-endpoint truncation guard · verdict `None` on an all-zero-par op · prose "rc=" lines. Fix at the 10/1 refresh or when the first in-scope op (9/24) exercises the path; the FIXES from the blind read are author-tested only — a second independent read is owed before the 9/24 packet is trusted blind.

## OPEN THREADS / KNOWN GAPS

- 🔴 **`grade_auction.py` still has NO `--selftest`** (the 9/15 numpy repair has no regression guard; it DID fail loud today when run outside the venv — the patch works, unguarded). re-test: 2026-09-24 (build the selftest before the cluster grades).
- ⚠️ **DECLARED RESIDUE — `boot_recompute` rc=1 at boot: 14 findings.** 2 were real STATUS derived distances (fixed in the rewrite); the rest are correctly-stamped dated history (`VX.tsv:16` "17bp BELOW [9/1]"; NEXUS_BRIEF FR2004 vintage lines inside SUPERSEDED-marked blocks). **Expected again next boot; re-read this line before "fixing" them.** re-test: 2026-10-01 (the quarterly refresh is the natural point to retire the superseded NEXUS blocks).
- 🟡 **Mirror divergence STILL un-reconciled (9th session):** `VX-BND-05`=4 / `VX-BND-16`=4 vs matrix rows 3 and 2.
- 🟡 `VX-BND-19` "DISORDERLY" + the add-gate's "sustained" (WQ-246, Will) — both undefined qualifiers; 10/1 refresh.
- 🟡 **MEMORY.md at 89% of the read-cap budget** — rotate (hot/cold split) before the next append.
- ⚠️ **TRAP (unchanged):** FRED `DSWP10`/`DSWP30` discontinued (re-test 2026-10-10); `fetch.fred_fetch` defaults limit=5 newest-first; flat `pdfminer.extract_text` misaligns multi-page tables — use `extract_pages` (the 9/17 schedule parse did, and sanity-checked 3 rows).
- ⚠️ **Session cwd was `PROME/`** (PROME `Agent`-tool spawn inherits cwd — DOCKET L399); BOND's CLAUDE.md read explicitly at boot; every git op from repo root with absolute pathspecs.

## POSITION
**TLT puts HOLD, no add — UNCHANGED. `$0`.** DFII10 2.62 [9/15] +12bp through the add-gate for 4 published sessions (`BND-29` TRUE); the count is Will's (WQ-246); 7/16 NO-ADD; root rule #5. The dovish SEP arrived and did not unwind it. `GATE-TERRY-007` 50bp away (DGS10 5.00). Composite 12/35. Counter 0. OPEN predictions 3. Live at authorship: TLT $80.88 [9/16 close].

## MAIL
**In: 2** (PROME 9/16 item → processed; WALTER SIG-021 → WALTER/processed). **Out: 3 `SendMessage` to `prome-ae`** (armed state · understood · receipt) + delivery memo `PROME/inbox/2026-09-17_from-BOND_tips-preprint-sep-grade-f2-carrier.md` (outbox copy). **Nothing to RED** — no in-scope op has published since 9/10. ZHAO doorbell (9/4 packets consumed their side) — no action.
