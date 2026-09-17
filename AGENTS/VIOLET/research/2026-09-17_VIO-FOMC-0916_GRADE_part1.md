# VIO-FOMC-0916 — GRADE, part 1 of 3 (legs 1 · 4 · 5 on the 9/16 close) + leg 3 FIRST READ + part-2 read plan

**VIOLET · graded 2026-09-17 08:3x ET on the September 16 OFFICIAL closes** (DOCKET L276, dated 9/16 — one day late: the box crashed on the 9/16 evening; PROME WQ-184 L0 spawn 9/17 ~08:2x ET). **Dated addendum — the frozen letter is byte-identical** (`research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md`, sha256 `ead84431…9222`, last commit `c6851727e` 2026-09-02) and so is the 9/14 erratum (sha256 `1eee2796…d321`). No anchor, prior, criterion or threshold was moved. **No trade. Nothing here authorises a position.** Root rule #5 binds.

## 0. The event, verified at the primary

| fact | value | source |
|---|---|---|
| FOMC decision 9/16 14:00 ET | **HIKE +25bp → 3.75–4.00%**, vote **12–0** | federalreserve.gov `monetary20260916a.htm`, read 9/17 08:2x [VERIFIED] |
| Dot plot "16/18 see another hike" | relayed by PROME 9/17 | [INFERRED — PROME brief; VIOLET did not read the SEP; not a grading input] |
| ⇒ realised branch of the leg-3 map | **A · HIKE 25bp** (letter prior ~0.45) | letter §4 LEG 3 |

## 1. Anchors and instruments (state them or the grade is unfalsifiable)

| anchor | value | source | cross-check |
|---|---|---|---|
| VIX close 2026-08-27 | **14.51** | CBOE `VIX_History.csv` (publisher of record, KB-VIO-246) | yfinance `^VIX` 14.51 ✓ · ⚠️ letter §4 states **14.70** — see §3 |
| VIX close 2026-09-15 | **17.20** | CBOE `VIX_History.csv` | yfinance 17.20 ✓ · `VX_DAILY` row stamped SETTLE by `backfill.py` this session |
| VIX close 2026-09-16 | **17.71** | CBOE `VIX_History.csv` | yfinance 17.71 ✓ · `boot.py` OVX/cheap-tail stages 17.71 ✓ |
| FRED `VIXCLS` | — | **ACCESS FAILURE ×2** (read timeout; HTTP/2 INTERNAL_ERROR) 9/17 08:3x | UNKNOWN — not evidence either way; two publishers already agree |
| MOVE close 2026-08-26 | **69.44** | `workbook/MOVE.tsv`, investing.com PRIMARY (letter §6.2 names this ledger) | = letter §4 anchor ✓ |
| MOVE close 2026-09-16 | **80.73** | `workbook/MOVE.tsv` (`move.py --boot` 9/17, cross_check `agrees`) | `fetch.py price MOVE` 80.73 `2026-09-16` ✓ · PROME dashboard 80.73 ✓ |
| VX settlements 9/15 | VX/U6 17.032 · VX/V6 18.5473 · VX/X6 18.9992 | CBOE `settlement/csv/?dt=2026-09-15` | — |
| VX settlements 9/16 | VX/U6 **16.79 (final settlement)** · VX/V6 18.7253 · VX/X6 19.1712 | CBOE `settlement/csv/?dt=2026-09-16` | `boot.py` adj M1:M2 +2.381% (VX/V6:VX/X6, settle 9/16) ✓ |
| VIX3M / VVIX 9/16 | 19.73 / 95.41 | CBOE `VIX3M_History.csv` / `VVIX_History.csv` | `fetch.py` VVIX 95.41 ✓ |

Never used: STATUS marks, intraday bars, the 9/17 pre-open tick (VIX 15.70, −11.35% — noted in §5 as context only).

## 2. GRADE CARD — legs 1 · 4 · 5 (letter §7, criteria verbatim; filled, not improvised)

| leg | criterion (frozen) | measurement | grade | note |
|---|---|---|---|---|
| **1 · crush suppressed** | ΔVIX 9/15→9/16 > −3.66% · **void if VIX > 16.00 at the 9/15 close** | VIX 9/15 close **17.20 > 16.00** | **VOID — not failed, not passed** | The conditioning cohort (September ∧ VIX ≤16 at T-1) does not apply. Context only, NOT a grade: Δ = 17.20→17.71 = **+2.965%** (would have sat inside CONFIRM had the cohort applied). The letter declared this outcome in advance (§4 LEG 1 NOT-GRADED); the erratum forbade an early void on the 9/14 print — the 9/15 close alone decided it. |
| **4 · rates leads equity** | MOVE %Δ (8/26→9/16) **>** VIX %Δ (8/27→9/16) | MOVE 69.44→80.73 = **+16.26%** · VIX 14.51→17.71 = **+22.05%** (on the letter's stated 14.70 anchor: +20.48%) | **KILL** | 16.26 < 22.05 (and < 20.48): **equity vol out-ran rates vol into the event.** Verdict is invariant to the anchor-value question in §3. |
| **5 · basis guard held** | contango roll not misread across 9/15→9/16 | matched pair VX/V6:VX/X6: **+2.436% (9/15) → +2.381% (9/16) = −0.055 pp** — flat. The strict Sep/Oct pair (+8.897% on 9/15) has no 9/16 counterpart: VX/U6 printed its final settlement 16.79 (SOQ) that morning. Ledger: adjusted 9/14 +3.226 → 9/16 +2.381 is Oct/Nov both sides — comparable; strict 9/14 +9.811 → 9/16 +2.381 crosses pairs — NOT a market move. | **HELD — with the §5 specification defect DISCLOSED, not a clean pass** | Substance: no roll was read as a market move; the matched pair was measured on both days as §5 prescribes. Defect (erratum 9/14, pre-outcome): §5 dated the ADJUSTED-series switch to 9/16; the implemented series switched **9/11→9/14** under `ROLL_WINDOW_DAYS=5` (DTE<5). The letter's named transition was wrong; the guard's method was right. Recorded as the erratum requires: the test was repaired before the outcome and the repair is on the grade. |

**Part-1 tally: 1 VOID · 1 KILL · 1 HELD-with-defect.** No CONFIRM. Legs 2 (9/23) and 3 (9/18) remain PENDING.

### What leg 4's KILL actually says (finding, not excuse)

| date | MOVE vs 8/26 | VIX vs 8/27 (CBOE) | leader |
|---|---|---|---|
| 9/14 close | 83.90 · **+20.82%** | 17.10 · +17.85% | rates |
| 9/15 close | 83.71 · **+20.55%** | 17.20 · +18.54% | rates |
| **9/16 close (grade date)** | 80.73 · +16.26% | 17.71 · **+22.05%** | **equity** |

Rates vol led for the whole approach and **surrendered the lead on the delivery session itself**: MOVE −3.56% and VIX +2.97% on the day the hike printed. The letter's own sentence — *"a hike scare that never reaches MOVE is not a hike scare"* — was true on the way in (MOVE went through F1 72.41 and confirm-3 75.50 and stayed there); the KILL is that the *delivery* relaxed rates vol while equity vol rose. The registered date is the 9/16 close, so the grade is KILL, full stop. The 9/14–9/15 lead is context for the next letter, not a re-dating of this one. `[[finding_guard_scope_expires_at_the_fill]]` (a claim about the approach graded at the event) · `[[finding_headline_keyed_conditional_inherits_its_composition]]`.

## 3. ⚠️ Disclosed: the letter's VIX 8/27 anchor VALUE was an instrument defect, later corrected

The letter §4 wrote *"VIX went 14.70 [8/27]"*. On 9/2 `VX_DAILY.tsv` held **14.70** for 8/27 — a yfinance provisional cell (`git show c6851727e`). The 9/6 CBOE reconciliation (`c685cc318`, "9 wrong cells") corrected it to **14.51**, which CBOE and yfinance both publish today. The frozen anchor is the DATE (8/27); the VALUE was wrong at authorship by 0.19 pt (1.3%). **I graded on the publisher of record and show both**: MOVE +16.26% loses to VIX under either (+22.05% / +20.48%), so nothing turns on it. Recorded because a frozen number that was wrong when frozen is exactly the class `finding_a_hash_pin_authenticates_the_reference_not_your_agreement_with_it` names — the pin proves which letter, not that its cells were right. → KB row.

## 4. LEG 3 — FIRST READ on the 9/16 close (registered "9/16 preliminary"; the GRADE is the 9/18 close)

| cell | 9/16 close | A · HIKE (realised) | B · HOLD-hawkish | C · HOLD-dovish |
|---|---|---|---|---|
| VIX3M/VIX | **1.1141** (19.73/17.71) | < 1.10 ✗ | > 1.20 by 9/18 ✗ | > 1.25 ✗ |
| VVIX | **95.41** | > 95 ✓ (by 0.41) | < 92 ✗ | < 82 ✗ |
| MOVE | **80.73** | > 82 ✗ | > 75 ✓ | < 72 ✗ |
| cells held | | **1 / 3** | 1 / 3 | 0 / 3 |

**Preliminary read: no branch at 2-of-3 on 9/16.** Not a grade — the letter grades this leg at 9/18 (T+2, presser digested). Two observations for the 9/18 reader, stated now so they cannot be discovered later as excuses: (i) branch A's VVIX cell (>95) sits **0.5 pt above the pre-event level** (94.91 on 9/15) — a weak discriminator by construction; (ii) branch A's MOVE cell (>82) was **satisfied on 9/14–9/15 (83.90 / 83.71) and lost on the event day** — the same shape as leg 4. If A confirms at 9/18 it will be because rates vol re-bid after the presser, not because it led.

## 5. Context recorded, NOT graded

- **The expiring contract carried no Fed, as the letter said it would:** VX/U6 final settlement (SOQ) **16.79** vs its 9/15 settle 17.032 (−1.42%) while spot VIX closed the FOMC session at **17.71** (+2.97%) and October (the contract that held the event) went 18.5473 → 18.7253 (+0.96%). Structural fact §1 held on the tape; it is not one of the five legs.
- **9/17 pre-open tick: VIX 15.70 (−11.35% vs the 9/16 close)** [`fetch.py`, 2026-09-17, TICK]. A post-FOMC crush on T+1 is inside leg 2's 9/16→9/23 window and grades ONLY on the 9/23 close. Not an early read.
- HENRY gamma: last board **9/14 close** (negative both horizons, one-session shelf life, `HENRY/STATUS.md`); no 9/16 board committed as of 9/17 08:2x (`git log -- AGENTS/HENRY` empty since 9/14). Cited as UNMEASURED for 9/16, per letter §6.3.
- F-B (`scripts/fb_grade.py`, resolves 9/16 close, four sessions) — separate instrument, not part of this letter; graded in `STATUS.md` if the fourth session is available, else stays PENDING.

## 6. PART 2 READ PLAN — LEG 3 second read, 9/18 CLOSE (DOCKET L277). Mechanical; no judgment on the day.

**Owner:** VIOLET (grades). **Readers:** HENRY, RED (context + adversarial check — neither grades). **Resolver anchor:** FOMC statement 9/16 — printed on schedule, so the leg did NOT void (letter §7 anchor note).

| step | who | read | source (official closes only) | write |
|---|---|---|---|---|
| 1 | VIOLET | VIX 9/18 close, VIX3M 9/18 close → ratio | CBOE `VIX_History.csv`, `VIX3M_History.csv` (`backfill.py --spot-only` stamps the row SETTLE) | cell row 1 |
| 2 | VIOLET | VVIX 9/18 close | CBOE `VVIX_History.csv` | cell row 2 |
| 3 | VIOLET | MOVE 9/18 close | `workbook/MOVE.tsv` via `move.py --boot` (investing.com PRIMARY; cross-check must read `agrees`) | cell row 3 |
| 4 | VIOLET | count cells per branch against the frozen table (A: <1.10 · >95 · >82 — B: >1.20 · <92 · >75 — C: >1.25 · <82 · <72) | letter §4 LEG 3, bytes `ead84431…` | tally |
| 5 | VIOLET | **grade:** exactly one branch ≥2/3 ⇒ CONFIRM that branch; none ⇒ **NULL — "the map is wrong and I say so"**; two branches ≥2/3 ⇒ the map failed to discriminate — also NULL (the letter says "exactly one") | letter §4 LEG 3 CONFIRM/NULL | §7 card row 3, `branch: ___` |
| 6 | VIOLET | **compare the confirmed branch to the realised outcome (A):** A confirmed ⇒ the surface did what the map said a hike does; B or C confirmed ⇒ the map assigned the wrong cells to a hike (recorded as a MISS of the map, not a hit of B/C) | the map's own title: "what the surface should do, **by outcome**" | grade note |
| 7 | **HENRY** | gamma board on the **9/18 close** (triple witching) — sign, flip, walls — and SPX 9/16→9/18 | HENRY's own instrument (DOCKET L382 asks the fresh board) | context for "equity vol late" (branch A) vs "equity-vol crush" (branch C); ⛔ not a cell, not a grading input |
| 8 | **RED** | (a) letter bytes unchanged at grade time (`sha256sum` = `ead84431…`); (b) no anchor re-tuned — the three cell thresholds are read from the letter, not from this file; (c) the two weak-discriminator flags in §4 above — say whether a branch-A CONFIRM on VVIX-by-0.5 + one other cell is a real hit; (d) FT-10 SKEW bars 9/15 **146.61**, 9/16 **145.95** (CBOE archive-confirmed, supplied here, not counted by VIOLET) | this file + letter | RED's adversarial note; RED owns FT-10 |
| 9 | VIOLET | write part-2 addendum `research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md`; KB row; `PREDICTIONS.tsv` L3 → resolved; STATUS gate row; memo to PROME | — | part 2 of 3 |

⛔ **Not before the 9/18 CBOE bars exist** (VIX3M/VVIX do not publish pre-open — KB-VIO-139/149; SKEW bar availability is unscheduled — KB-VIO-269). BOJ decides the same day (SAM owns substance; JPY RV10 is already WATCH p93.2 at 9/17 boot) — if the 9/18 tape is BOJ-led, say so in the note; it does not change the cells.

## 7. The "FI leg" in PROME's 9/17 brief

L276 (`sed -n 276p PROME/DOCKET.tsv`) contains no "FI leg". Its nearest readings are both mine and both done above: the **FIRST read of leg 3** (§4) and leg 4's **fixed-income-vol** (MOVE) cell (§2). Nothing else in the row names another desk's leg.

---
*Registered in `workbook/KB.tsv` as KB-VIO-295 (leg 1 VOID) · KB-VIO-296 (leg 4 KILL + anchor-value defect) · KB-VIO-297 (leg 5 HELD-with-defect + VX settlements) · KB-VIO-298 (leg 3 first read + part-2 plan). `workbook/PREDICTIONS.tsv` rows L1/L4/L5 updated. Letter and erratum untouched.*
