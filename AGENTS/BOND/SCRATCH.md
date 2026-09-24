# BOND SCRATCH — 2026-09-24 (Thu), session `bond-b0`: ~13:00 → ET. Boot by Will after a SIX-DAY DARK GAP (no BOND session 9/18–9/23). PROME live as `prome-26`.

**Purpose:** ephemeral handoff. Read at boot, rewritten at closeout. Durable → `MEMORY.md`; evidence → `workbook/`. Executable COLD.

> ## ⚠️ STATE AT WRITING
> 🔴 **9/23 5Y `91282CRN3` = OLD CONJUNCTIVE COMPOSITION FAILURE** (ind 54.31 < 59.24 · dlr 15.77 > 15.61 by 0.16pp · BTC 2.21). **Add re-arm MET → Will DECLINED the add, WQ-280 ruled 13:17 ET** (verified `PROME/WILL_QUEUE.md:49`). **Paired kill NOT fired** (SOFR−IORB −3bp). Threshold fired, mechanism not shown failed. Graded ~24h late: **nobody on the fleet had graded it.**
> ⛔ **POSITION: TLT Sep-30 77P ×20 (NOT ×25 — 5 sold 9/10; this desk carried 25 until PROME caught it today) — HOLD, no add, `$0`, expiry 9/30.** Composite **14/35 (▲2: auction health 2→3 on the pre-registered cover rule; long-end 3→4 on its letter — 9/23 official 30Y 5.40 fresh high on a weak-composition day)**. Counter **0**. OPEN predictions **1** (`BND-27`).
> 🔑 **THE SESSION'S EPISTEMIC FACT: every defect found today was found by LOOKING AT THE INSTRUMENT'S OWN OUTPUT, not the verdict** — a window reading n=12 over 11 months exposed the cross-cycle reopening; a derived cell dated a day past its inputs exposed the provisional-cell hole; a csv.writer diff that touched 15 rows when 2 were meant exposed the re-quoting. **And one found by a peer (the ×25).**

## WHAT I DID — commits in order
1. `5103b27de` — cluster graded (2Y 🟢 · 5Y 🔴 · 7Y 🟠 `I'` by 0.037pp); packets LIQUID 🔴 · ZHAO 🟠 · TERRY 🔴 · PROME 🔴 (doorbelled live `prome-26`). Superlatives VERIFIED at the TD primary (n=117 5Y since 2017); **the dealer superlative did NOT hold on multi-year history — said so in every packet.**
2. `5c79dcb34` — `BND-25` TRUE (55%) · **`BND-26` FALSE (70%): 1y1y 5.03 on FOMC day, 5.08 [9/18] sample high ⇒ `KB-BND-283` §4 hawkish half WITHDRAWN, 4.75–4.95 band retired.** KB-BND-312→322. Mail 9 → 0. PROME's two catches applied (×20; absence claim re-scoped to the paths actually grepped).
3. `9a226b44e` — **`buyback_f2.py` `complete()` guard**: an independent Opus read showed a partial publication (2/35 rows, ops row null) reads **66.67% ON-THE-RUN FIRES, rc=0** — the exact ~14:15 state. Now fails closed. Review → `analysis/2026-09-24_buyback_f2_independent-read.md`.
4. STATUS rewrite (9/17 file rotated verbatim, crc32 `2559402921`) · docket +5 non-auction rows (9/25 H.15 · 9/30 · 10/2 · 10/14 · 10/28) · VX 01/04/08/13. **+ REPAIR: `csv.writer` had re-quoted 14 KB rows in `5c79dcb34`; restored byte-for-byte from `40726328e`. Not amended; that commit is the record.**
5. THESIS v1.2.8 + CHANGELOG · 14 KB rows past Stale_By → STALE (flagged NOT re-verified).
6. **`grade_auction.cycle_term()` (`KB-BND-314` CORRECTED)**: cross-cycle reopenings keyed to their cycle. Blast radius **exactly 2 rows** — the known Jan-26 `91282CGH8`, **and an unknown second, Feb-25 `91282CGQ8` (7Y→5Y cycle).** Selftest 29/29, mutant caught.
7. ⛔ **`boot_recompute.trim_provisional()` — BUILT, THEN RETRACTED THE SAME HOUR.** It rested on WALTER −011's mechanism, which LIQUID had retracted 9/22 (the commit was in the log I scanned at boot) and WALTER withdrew in −004: FRED builds T5YIFR/T10YIE from Treasury curves, so an early cell is REAL. Reverted to naming-only `align_notes()`; T5YIFR 2.36 [9/23] = 14bp was right all along (`KB-BND-320` CORRECTED). **Lesson: I 'reproduced' a claim on my own instrument — but the reproduction confirmed the OBSERVATION (dates differ), never the MECHANISM (provisional).**
8. WQ-280 ruling recorded (TRADE Reactivation Matrix, STATUS, THESIS, CHANGELOG); NEXUS_BRIEF 9/24 re-pin; AUCTION_HEALTH 5Y 9/02 bar struck as contaminated (clean 59.48).

## 🔴 NEXT SESSION (dated, future-verifiable)
0. ✅ **F2 READ OF THE 9/24 20–30Y OP — DELIVERED 14:1x ET:** $4.078B of $6B cap (68%) on 1.74× offered; recent_share **0.02% ⇒ OFF-THE-RUN**; complete at read (35/35); packet → `AGENTS/RED/inbox/2026-09-24_from-BOND_F2-READ-*` (RED dark — PROME told); ledger row; `KB-BND-324`. Next op **10/1 10Y–20Y — vintage fix FIRST.**
1. 🟠 **Fri 9/25 — confirm FRED DGS30[9/23] republishes 5.40** (row 1 already FIRED 9/24 on the U.S. Treasury par curve = the H.15 source, 182/182 identity, `KB-BND-323`). **New standing capability: `home.treasury.gov` daily par/real curve CSVs publish the official close ~a session before FRED.** DFII10 2.76 [9/23] = highest since 2008-11.
2. 🔴 **Wed 9/30 — `BND-27` window closes (CCC 1093 [9/23], 7bp from 1100)**; quarter-end (the kill's funding leg is excluded at quarter-end by its letter); Aug PCE + Q2 GDP 3rd 8:30; TLT expiry (TERRY).
3. 🟠 **Replies owed TO me:** LIQUID (funding 9/23–25 beyond SOFR−IORB) · ZHAO (H.4.1 custody / TIC on a foreign step-back). Integrate into `KB-BND-312` and VX-13.
4. 🟠 **10/1:** F2 **10Y–20Y vintage fix BEFORE the op** (review ⚠️3: in that bucket "newest by maturity" includes 2015–16 30Ys; a synthetic buy of three old 2.25–2.5% 30Ys reads **100% ON-THE-RUN**) · quarterly `I'` refresh · `VX-19` "disorderly" · TIPS-`I'` question · degenerate-row guard.
5. 🟠 **By 10/21: register the 10/28 FOMC curve-shape prediction** with a base rate (the `BND-25` template).
6. 🟡 The 9/2 per-tenor base-rating and the WQ-157 join used pools with the 2 cross-cycle rows — **not re-run**; disclose if re-cited.
7. 🟡 `READS.tsv` declaration owed by 9/30 (DAEDALUS PR#6 ASK 3). ACM/KW TP not re-pulled this session — last obs ACM 2026-09-15, KW 2026-09-11; re-pull at the next full boot.

## OPEN THREADS / KNOWN GAPS
- 🔴 **WALTER's board stops at 9/21** — the 9/23 PMI shock reached this desk only by my own web search. Secondary-sourced: PMI 58.4, "5Y >5% first since 2007" (Bloomberg headline), Oct hike ~70% (TE). Not primary-verified.
- ⚠️ **`csv.writer` on these TSVs re-quotes any field containing `"`. Use raw `split('\t')`/`'\t'.join` for workbook edits.** (Cost this session: 14 KB rows silently rewritten and committed.)
- ⚠️ `NEXUS_BRIEF.md` is **73 KB** — over the 32,550 B read cap IF any boot reads it whole. Flagged to PROME, not restructured.
- ⚠️ F2 review residue: ⚠️2 (quartile on present rows) · ⚠️4 (n<4 eligible) · ⚠️5 (the >50% cut is BOND-declared; RED-FT-11 has no number) · ⚠️6 (mis-scoped op dropped silently) · ⚠️7 (packet claims a cache-bust `_get` does not do) · ⚠️8 (selftest reads the live ledger).
- TRAPS (carried): FRED `DSWP10/30` discontinued (re-test 10/10) · `fetch.fred_fetch` default limit=5 · pdfminer multi-page tables · venv required for `grade_auction`/`cdx_proxy` · ACM `.xls` needs `xlrd`.

## POSITION
**TLT Sep-30 77P ×20 — HOLD, no add, `$0`. WQ-280 DECLINED the add (9/24 13:17 ET); no fresh card approved.** DFII10 2.63 [9/22] through the gate (count = WQ-246). `GATE-TERRY-007` 46bp. Live at authorship: TLT $80.05 [9/24 ~13:0x] — a moment property, re-pull (root rule #4).

## MAIL
**In: 9 → processed** (HANS ×3, PROME L409, WALTER ×5; one KB row each). **Out: 4 packets** (LIQUID · ZHAO · TERRY + correction line · PROME) + 2 `SendMessage` to `prome-26`. PROME packets consumed.
