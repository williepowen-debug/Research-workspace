# Disc-J letters for eight matrix rows (L15) — registered 2026-10-08 at the DOCKET L554 wake

**Written:** 2026-10-08 08:23 EDT (NEXUS, spawned by PROME `prome-fc`, WQ-389 wake). **Why:** the 10/1 sweep found M-01 · M-03 · M-04 · M-05 · M-06 · M-07 · M-10 · M-11 carrying a Conf % with an arbiter or nothing (charter Disc-J: a number carried across passes with no registered falsifier is a judgment, not an estimate). This page writes one letter per row. **No row is re-marked by this page;** each letter moves its row only when it fires.

## Common construction (applies to every letter unless the row says otherwise)
- **Anchor L = the first cell of the named instrument published AFTER this registration** (the 10/8 cell / close / settle) — **unknown when this page was written**, the L13 design. Edges are symmetric around L.
- **Run = 2 consecutive published cells** at or beyond an edge (inclusive). Non-publication days (weekends, bond-market holidays such as Mon 10/12) are not cells and do not break a run; a cell not yet published is not an observation.
- **Consequence: ±4pp on that row's Conf %** (same size as M-08/M-09). **First run to complete governs**; the other branch is then moot for the window. Both completing on the same cell date ⇒ net 0, recorded.
- **Neither by the window's last cell ⇒ hold, EARNED — once.** A second "neither" on a re-registered window ⇒ the row's Conf % is **withdrawn** (published as "judgment, no number"). **What a repeated no-move means:** the instrument cannot see this row's claim at a 2–6 week horizon; the number was a mood.
- **No data:** zero cells published in the window (outage) ⇒ ⚪ RESOLUTION-UNVERIFIED, hold, NOT counted as the earned "neither"; one re-window allowed.
- **Percent edges (M-05, M-06) are computed once in integer cents — floor for the lower edge, ceil for the upper — so neither edge sits inside ±8% / ±10%.**
- **Arithmetic in integer units** (bp, cents, index hundredths) — never float ×100 (`[[finding_float_precision_empties_the_tie_set_and_voids_the_operator]]`).
- **Disc-A:** each letter names the mechanism it claims; mechanism is graded separately at a fire; letter consequence applies as written, disagreement recorded.
- **Count once:** M-03 shares root R1 with the split's `DFII10` letter (L13); M-01 and M-07 both read credit OAS. A co-fire is ONE observation for convergence counting; each letter still applies its own consequence to its own number.

## The letters

| Row (Conf now) | Instrument (basis) | UP ⇒ +4pp | DOWN ⇒ −4pp | Window ends | Claimed mechanism (Disc-A) |
|---|---|---|---|---|---|
| **M-01** Substance/tape divergence (60%) | tape = HY OAS `BAMLH0A0HYM2` (FRED first-published, bp); substance = initial claims `ICSA` (DOL first print, SA) | **divergence widens:** HY ≥ L+35 on 2 consecutive cells AND the latest ICSA print at the 2nd cell ≤ 215,000 | **divergence closes, either side:** HY ≤ L−35 ×2 consecutive cells, OR ICSA ≥ 230,000 on 2 consecutive weekly first prints | cell/print dated ≤ 2026-11-05 | the tape is pricing stress the labor data does not show. Two closure routes are the definition of a divergence (it closes from either side), not a lean — disclosed. |
| **M-03** Duration channel, driver SPLIT (78%) | `DGS10` (FRED first-published) | ≥ L+15bp ×2 | ≤ L−15bp ×2 | ≤ 2026-11-05 | premium half: ACM 10Y term premium (HENRY's read) moves the same sign as DGS10 over the run ⇒ TRUE-in-spirit; FORUM-7 FINAL (HENRY 10/2): duration compensation can reverse on supply without a Fed change. |
| **M-04** Vol/gamma crack candidate (26%) | `VIXCLS` (FRED, CBOE close) | ≥ L+3.00 ×2 | ≤ L−3.00 ×2 | ≤ 2026-11-05 | dealer short gamma converts a down-move into index vol; HENRY's gamma sign at the fire cell is the mechanism check. |
| **M-05** WAL/CRE first bank-tier LEVEL fire (48%) | KRE NYSE close (vendor, `fetch.py`; ⚠️ not a FRED cell) | ≤ E_low = floor(L¢×92/100) ×2 consecutive closes | ≥ E_high = ceil(L¢×108/100) ×2 | close dated ≤ 2026-11-05 (covers Q3 bank prints ~10/20–28) | credit-driven bank-tier stress, not size-sorted beta — REGINALD's attribution at the fire decides spirit. |
| **M-06** Energy — bypass event REVERSING (41%) | Brent **BZZ26** ICE daily settle (vendor `fetch.py`; ⚠️ name the month — BRENT's rule: BZZ26 through 10/29) | ≥ E_high = ceil(L¢×110/100) ×2 consecutive settles | ≤ E_low = floor(L¢×90/100) ×2 | settle dated ≤ 2026-10-29 (no roll inside the window) | physical supply loss, not premium (BRENT 9/25: "premium, not destroyed capacity") — BRENT's grade of barrels decides spirit. |
| **M-07** Bull-counter tape cluster (79%) | IG OAS `BAMLC0A0CM` (FRED first-published, bp) | ≤ L−11 ×2 (counter strengthens) | ≥ L+11 ×2 (counter breaks; ≈ `GATE-LIQ-072`'s 94 if L ≈ 83) | ≤ 2026-11-05 | the chain stays blocked at IG/funding; SOFR−IORB is the funding mechanism check (not a branch leg). |
| **M-10** UST foreign-official (25%) | rides **L11** (PRED-30, August TIC ~10/16) — no new instrument | L11 ✅ HIT (China LT/coupon net ≤ −$12.0B) | L11 ❌ MISS (≥ −$3.0B) | L11's grade | L11's own ⚪ band (strictly between) ⇒ hold, EARNED once, under L11's non-renewable clause. Same observation as PRED-30 — never a second vote. |
| **M-11** Insurer/PC recognition (51%) | lowest documented arms-length private-credit **loan-level** transfer price p (court sale order or filed realized-sale disclosure) — PRED-45's documents | p ≤ 90.0¢ | no documented transfer at p ≤ 95.0¢ by the window end (incl. none at all) | 2026-11-20 (BDC Q3 10-Q cycle) | 90.0¢ < p ≤ 95.0¢ ⇒ ⚪ hold, EARNED once. A MARK at any level is not a transfer. Same documents as PRED-45 — one observation, two letters. |

## Counterexamples (BOOT 0b, five cases per letter, written in)

**Single-instrument letters (M-03 · M-04 · M-05 · M-06 · M-07), edges E+ / E−:**
1. **Lower boundary, inclusive:** two consecutive cells exactly = E− ⇒ the E− branch fires. One unit inside (E− + 1bp / +$0.01 / +0.01) ⇒ no.
2. **Upper boundary, inclusive:** E+, E+ ⇒ the E+ branch fires; E+ then E+ − 1 unit ⇒ no run.
3. **Mixed:** E+, then a cell inside the band, then E+ ⇒ no run (consecutiveness broken by a published cell). E+ ×2 completes at cell 4, E− ×2 at cell 9 ⇒ cell 4 governs; E− moot.
4. **n = 0:** no cell published in the window ⇒ ⚪ RESOLUTION-UNVERIFIED (not the earned "neither"); one re-window.
5. **n = 1:** a single cell at/beyond an edge, then the window ends ⇒ no fire ⇒ "neither", hold, EARNED.

**M-01 (two instruments):** ① HY = L+35 ×2 with latest ICSA 215,000 ⇒ UP (both inclusive) · ② HY = L+35 ×2 with latest ICSA 215,001 ⇒ no UP · ③ ICSA 230,000 then 230,000 ⇒ DOWN; 230,000 then 229,999 ⇒ no · ④ mixed: HY UP run completes on the same date a second ≥230,000 ICSA print publishes ⇒ net 0, recorded · ⑤ n = 0 (no HY cell and no ICSA print) ⇒ ⚪ UNVERIFIED; n = 1 (one HY cell ≥ L+35) ⇒ no fire.

**M-10:** HIT/MISS/⚪ exactly as L11's own counterexamples (L11 −$12.0B ⇒ HIT; −$11.9B ⇒ ⚪; −$3.0B ⇒ MISS; −$3.1B ⇒ ⚪; TIC not published by 11/05 ⇒ ⚪ UNVERIFIED, hold).

**M-11:** ① p = 90.0¢ ⇒ UP · ② p = 90.1¢ ⇒ ⚪ · p = 95.0¢ ⇒ ⚪ · p = 95.1¢ (lowest) ⇒ DOWN · ③ mixed: one transfer at 85¢ and one at 97¢ ⇒ lowest governs ⇒ UP · ④ n = 0 transfers by 11/20 ⇒ DOWN · ⑤ n = 1 at 92¢ ⇒ ⚪.

## Four tests (BOOT 0b) on each letter
| Letter | (i) date | (ii) magnitude | (iii) resolver exists (checked 10/8) | (iv) exclusive + exhaustive |
|---|---|---|---|---|
| M-01 | 11/05 | ±4pp; ±35bp / 215K–230K | FRED `BAMLH0A0HYM2` 303 [10/6] · `ICSA` 197,000 [w/e 9/26] — both pulled 10/8 | first-to-complete; same-date tie ⇒ net 0; neither ⇒ hold |
| M-03 | 11/05 | ±4pp; ±15bp | `DGS10` 5.27 [10/6] pulled | edges cannot co-fire |
| M-04 | 11/05 | ±4pp; ±3.00 | `VIXCLS` 15.01 [10/6] pulled | edges cannot co-fire |
| M-05 | 11/05 | ±4pp; ±8% | KRE 68.89 [10/7 close, vendor] pulled | edges cannot co-fire |
| M-06 | 10/29 | ±4pp; ±10% | BZZ26 pulled 10/8 (⚠️ vendor 10/7 bar repeats 10/6's volume — re-read the anchor at BRENT's settle source before grading) | edges cannot co-fire |
| M-07 | 11/05 | ±4pp; ±11bp | `BAMLC0A0CM` 83 [10/6] pulled | edges cannot co-fire |
| M-10 | L11 grade | ±4pp | Treasury TIC (L11) | inherits L11's three branches |
| M-11 | 11/20 | ±4pp; 90.0 / 95.0¢ | EDGAR / court dockets (PRED-45) | lowest price governs; three bands cover every p and n = 0 |

*The anchors above are the latest values KNOWN at writing, listed only to show the resolvers exist; every letter's L is the NEXT cell, unknown at writing.*
