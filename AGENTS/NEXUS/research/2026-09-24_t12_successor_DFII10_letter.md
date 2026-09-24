# T-12 SUCCESSOR — REAL-RATE LEG (`DFII10`), BANDED LETTER · REGISTERED 2026-09-24 ~15:1x ET

**Author:** NEXUS (PROME spawn `prome-3f`, WQ-206 drain + encode) · **Status:** 🔒 **FROZEN AT REGISTRATION** — no amendment without a Will word or a written re-registration carrying its own date, reason and a re-run of every §1 check against the amended words (gate §1 rule: an amendment inherits the original's certificate only if the checks are re-run). **Correction 2026-09-24 ~17:5x ET (§7):** the §1.4 row-2 description and the §3 repeated-C interpretation were corrected on CATO RC1 (Will-routed via PROME); **§2, the letter, is unchanged** (hash receipt in §7).
**Authority:** WQ-261 RULED — Will, 2026-09-24 14:59 ET, verbatim *"Approve WQ-282, 254, 261, 260 and 276 with your recs"*; record `PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md` row 261 = my 9/17 rec ①: the real-rate leg is blessed into the frozen admission gate (`research/2026-09-02_t12_respec_admission_gate_prereg.md`) as the T-12 successor. ② (CCC-relative spec as an observable) stays NOT (WQ-224 (ii)); ③ (carry the line) is superseded.
**What the word did and did not do:** it added `DFII10` to the gate's pre-named candidate list (the 9/11 refusal precedent is why that needed Will). **It did not waive the gate's (a)–(e) tests**, and the ruling's own encode discipline (banded · symmetric · numeric NO-VERDICT band · non-renewable clause · checks before the letter) binds the letter. §1 below is those checks, run **before** §2 was written.

---

## 1. CONSTRUCTION CHECKS — recorded before the letter

### 1.1 The instrument, pulled at primary (not from PROME's packet)

| Source | Pull (ET) | Cells |
|---|---|---|
| FRED `DFII10` via `fredgraph.csv` (full history) | 2026-09-24 15:05 | **5,935 published sessions, 2003-01-02 → 2026-09-22**; min −1.19 · max 3.15. Last six: 2.62 [9/15] · 2.68 [9/16] · 2.61 [9/17] · 2.68 [9/18] · 2.62 [9/21] · **2.63 [9/22]** |
| `fetch.py fred DFII10` | 2026-09-24 15:05 | 2.63 [9/22] · 2.62 [9/21] · 2.68 [9/18] · 2.61 [9/17] · 2.68 [9/16] — identical to the csv |
| US Treasury Daily Real Yield Curve, `10 YR` column (the source FRED republishes) | 2026-09-24 15:06 and 15:08 | **2.76 [9/23]** · 2.63 [9/22] · 2.62 [9/21] · 2.68 [9/18] · 2.61 [9/17]. **9/24 cell NOT published at 15:08.** |

**Basis identity:** Treasury = FRED on the 4 overlapping cells 9/17–9/22 (4/4 exact). PROME's relayed **2.76 [9/23] is VERIFIED at the Treasury primary**; it is not yet on FRED. ⚠️ 9/23 is a **+13bp one-day move**, about 4× the trailing-250 daily σ (3.4bp).

### 1.2 The literal string, checked first: `DFII10 ≥ 2.50 on five published sessions` read as a one-sided branch

| Check | Result |
|---|---|
| Req 1 symmetric magnitudes | ❌ one-sided — no counterpart branch |
| Req 2 numeric NO-VERDICT band | ❌ none |
| Gate (a)–(c), W=15, unconditional | fires in **2.2%** of windows (n=5,920) |
| Gate 2(d), sessions starting ≥2.50 (the regime it would run in) | fires in **78.4%** (n=111) |
| **At registration** | the last five published cells **9/17–9/23 = 2.61 · 2.68 · 2.62 · 2.63 · 2.76 — all ≥2.50. It would fire on the day it was registered.** |

⇒ **Read literally, the first grade is IMMEDIATE, and that is exactly why the literal string cannot be the letter:** a condition already satisfied at registration is a description, not a test, and the gate's §4.3 rule is that an inadmissible falsifier is worse than an absent one, because it certifies. **The ≥2.50 string is kept as the regime definition** — the conditioning set for gate 2(d) below, and the observation that made the leg worth asking for. ⚠️ **Flagged to PROME and Will, not buried:** if Will meant the literal one-sided string as the letter, that reading fires today and certifies nothing; this record takes his word as blessing the instrument, under the discipline his same word adopted.

### 1.3 The repair — a RELATIVE, symmetric band, base-rated on a grid

Spec family: anchor **L** = one published cell; **UP** = `DFII10` ≥ L + D on **5 consecutive published cells** · **DOWN** = ≤ L − D on 5 consecutive published cells · both inside the **W published cells after the anchor**; first to complete wins; otherwise NO-VERDICT. **Single leg per branch — gate (e) holds by construction.** No ratio or retracement leg ⇒ **gate §4.4 (denominator stability) is N/A.** Grid = **W ∈ {10, 15, 21, 25, 30} × D ∈ {10, 15, 20, 25, 30}bp = 25 cells**, all inside the split's 2–6 week horizon.

| Set | Cells passing (a)+(b)+(c) |
|---|---|
| Unconditional, 2003→ | 6 of 25 (W15/D10 · W21/D10 · W25/D10 · W25/D15 · W30/D10 · W30/D15; none at D≥20) |
| Regime-conditional, start ≥2.50 | 3 of 25 (W10/D10 · W15/D10 · W15/D15) |
| **Both — what 2(d) requires** | ⭐ **exactly ONE: W = 15, D = ±10bp** |

**The one admissible cell, published in full as 2(d) requires:**

| Set | n | UP | DOWN | NO-VERDICT | ratio | Gate |
|---|---:|---:|---:|---:|---:|---|
| Unconditional 2003→ (overlapping starts) | 5,920 | 21.5% | 22.3% | 56.2% | 1.04 | ✅ |
| Unconditional, non-overlapping starts (every 15th) | 395 | 21.3% | 22.3% | 56.5% | 1.05 | ✅ (robustness) |
| **Regime-conditional, start ≥2.50** | 111 | 17.1% | 46.8% | 36.0% | 2.74 | ✅ |
| Trailing, starts since 2024-09-24 (not a gate requirement) | 483 | 22.2% | 16.6% | 61.3% | 1.34 | ❌ (c) by 1.3pp — published so it is visible |

**Caveats that travel with this letter — every one of them:**
1. ⚠️ **The conditional pass is THIN.** 111 overlapping starts ≈ **5 independent episodes** (2006-06/07 · 2007-05/07 · 2007-08 · **2008-10/11** · one 2023 day; the live 2026 run began 9/10 and has no completed window). **The 2008 TIPS-liquidity episode supplies 35 of 111 starts. Ex-2008 the conditional read is UP 11.8% / DOWN 38.2% / NV 50.0% — ratio 3.24, which FAILS (b) by 0.24×.** Reported, not used to veto: the gate has no episode-exclusion rule, and dropping data after seeing it would be tuning in the other direction.
2. ⚠️ **In the regime it runs in, the letter leans DOWN** (46.8% vs 17.1%) — mean reversion from real-rate extremes. The anchor is relative, so the regime cannot decide the outcome, but it does tilt it; a DOWN fire is the base-rate-expected result and should be read with that in mind.
3. ⚠️ **Grid selection:** 25 cells were rated and one was chosen **because it is the only one passing both sets**, not for its outcome (which is unknown — §2 anchors on an unpublished cell). One-of-25 is still a multiple-comparison exposure; disclosed.
4. ⚠️ **±10bp is small in level, not in noise:** ≈3× the trailing daily σ, and it must be **held five published sessions**, not touched once.

### 1.4 Disc-J requirements, ticked against the §2 text

| # | Requirement | Where in §2 |
|---|---|---|
| 1 | Symmetric magnitudes | ±10bp edges; ±6pp consequences |
| 2 | Numeric NO-VERDICT band | Numeric edges L ± 0.10, run length 5, window 15. **C = neither a 5-cell UP run (≥ L + 0.10) nor a 5-cell DOWN run (≤ L − 0.10) completes within the 15 published cells.** ⚠️ C is **not** "every cell inside ±10bp": cells can sit outside the band and the window still grades C (§7) |
| 3 | Non-renewable clause | §2 C: one re-anchored window, then EXHAUSTED |
| 4 | Meaning of a repeated no-move | §3 |
| 5 | Reachability base-rate on the text as written | §1.3 table |

---

## 2. 🔒 THE LETTER (frozen)

**Instrument:** FRED `DFII10` (10-Year TIPS constant-maturity real yield, percent), **each cell as first published**. The US Treasury Daily Real Yield Curve `10 YR` column may be read as the same-basis early copy; **if the two ever differ on a cell, FRED governs and the difference is written on the grade.** Non-publication days (weekends, bond-market holidays) are not cells and do not break consecutiveness; **a cell not yet published is not an observation.**

**Anchor L:** the **2026-09-24** cell — **unpublished when this letter was written** (Treasury 15:08 ET showed 9/23 as its latest row). The letter was written without knowing L; it knows only that the regime is ≥2.50.

**Window:** the **15 published cells after the anchor** (on the expected calendar ≈ 9/25 → 10/16; the letter counts cells, not dates). Earliest possible fire = the 5th cell (≈10/1).

| Branch | Condition | Consequence on the split (2–6wk: Break · Grind-lasts · Unresolved) |
|---|---|---|
| **UP — price-of-money tightening** | 5 consecutive published cells **≥ L + 0.10** inside the window | **Break +6pp, taken from Grind-lasts** |
| **DOWN — price-of-money relief** | 5 consecutive published cells **≤ L − 0.10** inside the window | **Break −6pp, given to Grind-lasts** |
| **C — NO-VERDICT** | neither completes by the 15th cell | **scores nothing; written EARNED** |

**First to complete wins; the other branch is then moot.** Unresolved-divergence is untouched by either branch.

**Non-renewable clause:** C #1 ⇒ **exactly one** re-anchored window (L₂ = the 15th cell of window 1; the next 15 published cells; same edges, same consequences). **C #2 ⇒ EXHAUSTED, terminal.** The split returns to the words "currently un-falsifiable" on its own line, and **no third `DFII10` window is registered without Will's word.**

**Disc-A mechanism — graded SEPARATELY, never a branch leg (gate (e)):** at any fire, decompose anchor → fire cell into the real move (ΔDFII10) and the breakeven move (ΔDGS10 − ΔDFII10).
- **UP's claimed mechanism** is a real-rate-led tightening: TRUE-in-spirit if |ΔDFII10| ≥ |Δbreakeven|.
- **DOWN's claimed mechanism** is relief: TRUE-in-spirit if HY OAS (`BAMLH0A0HYM2`, first-published) is **not wider** at the fire cell than at the anchor. A DOWN fire with HY wider is a **growth-scare** fall in real rates, which is a break reading, not relief.
- **Either way, the letter's consequence is applied as written**, and a letter/spirit disagreement is recorded on the grade and routed to PROME (`[[finding_headline_keyed_conditional_inherits_its_composition]]`: apply it, then record the disagreement).

**Grade:** at the first NEXUS session on/after the fire cell or the 15th cell is published at FRED. Owner NEXUS. ⛔ No other desk grades it; WALTER never re-marks it.

---

## 3. What a repeated no-move would mean (Disc-J req 4)

A C has a 56% unconditional base rate (36% in-regime), so **one C is ordinary**. Squaring those marginal rates gives ~31% (~13% in-regime) for a double-C — ⚠️ **an independence illustration (0.562², 0.36²), NOT a measured double-window frequency:** the two windows are adjacent and re-anchored, their independence is not shown, and L₂ need not sit in the ≥2.50 regime. **A double-C does not prove the instrument class wrong** the way T-12's did. What a double-C **does** establish: **neither direction sustained a 5-cell run in either window — no verdict on the price-of-money channel.** ⛔ **Stability is NOT measured by this instrument.** A C can arrive with every cell outside L ± 0.10 (CATO's counterexample, reproduced in §7: L = 2.70, cells alternating 3.00 / 2.40 ⇒ C). So a double-C is recorded as **"no verdict; clause EXHAUSTED"**, and it counts **neither against nor for** my 9/17 reading (*"the bear's case has migrated almost entirely into the price of money"*). A claim that real yields actually held still would need a **separate, registered measurement** (e.g. max |cell − L| over the window) under the normal re-registration discipline — never a re-reading of C.
**The self-protection tell:** if a branch fires and the split does not move by its ±6pp at the next re-mark, that is the pattern Disc-J was written from. Say so on the STATUS line.

## 4. First grade

**Not immediate.** The anchor cell is unpublished; the earliest possible fire is the 5th cell after it (≈10/1). *(The literal one-sided reading would have been immediate, see §1.2. That is the reason it is not the letter.)*

## 5. What would falsify this record

It is wrong if the letter returns a C (or fires) **for a reason §1 could have seen**, e.g. the thin-episode tilt of caveat 1 turns out to be what decided it. That would count against the gate's thresholds as applied to a 5-episode conditional set, and the lesson would be that 2(d) needs a minimum-episode floor, not only a minimum-session floor. It is **not** falsified by a clean fire in either direction.

## 6. Relation to WQ-224 (the flow-feed search)

Path (i) is exhausted across RED · LIQUID · BROCK (PROME packet 9/18). **I do not take LIQUID's conditional door on the three zero-pinned repo/RRP series**, so (iii)'s un-falsifiable line for the FLOW class stands, and **this `DFII10` letter is the primary T-12 successor.** If a flow series later clears the gate, the ruling makes the choice of primary leg mine, and I would make it on a fresh gate run, not by swapping legs mid-window.

## 7. Correction record — CATO RC1, 2026-09-24 ~17:5x ET (interpretation only; the letter is unchanged)

**Source:** CATO `AGENTS/CATO/runs/2026-09-24_1644_recent-commit-review.md` § RC1 (`3968db6c5`), relayed by Will to PROME at 17:34 ET; PROME packet `inbox/processed/2026-09-24_from-PROME_CATO-RC1-NO-VERDICT-is-not-a-quiet-market-fix-the-interpretation-keep-the-letter.md` (`30ec39dfd`). **Disposition: CONCUR.**

| Item | Was (registered text, `aea73389d`) | Now |
|---|---|---|
| §1.4 row 2 | *"L − 0.10 < cell < L + 0.10 held through the window"* | C = neither a 5-cell UP nor a 5-cell DOWN run completes within 15 published cells |
| §3 meaning of a double-C | *"real yields held within ±10bp for ~30 sessions … the price-of-money channel went quiet"*, counted against my 9/17 reading | no verdict on the channel; stability not measured; counts neither way |
| §3 odds | *"31% (13% in-regime)"* stated as a chance rate | labelled an independence illustration (squared marginals), not a measured frequency |

**Why the old text was wrong (reproduced, not just accepted):** the §2 rule grades C whenever no 5-consecutive-cell run completes. My own run of the §2 rule: L = 2.70, 15 cells alternating 3.00 / 2.40 ⇒ **C**, with every cell outside L ± 0.10; re-anchor L₂ = 3.00, alternate 3.30 / 2.70 ⇒ **C** again. Controls: flat ⇒ C; five cells at L + 0.15 ⇒ UP at cell 5; five at L − 0.15 ⇒ DOWN at cell 5. 0.562² = 0.3158 and 0.36² = 0.1296: the 31% / 13% figures are exactly the squared marginal rates.

**What did NOT change:** the §2 branch rule, the ±10bp edges, the 5-cell run length, the 15-cell window, the anchor (the 9/24 cell), the ±6pp consequences, the Disc-A mechanism test, the non-renewable clause and the grade owner. §2 sha256 (text from the `## 2.` heading to the `## 3.` heading) = `212a5dc7…ac858` before the edit and after it. The §1 checks were not re-run because the words they check did not change; §1.4 row 2 now describes that rule correctly. Disc-J requirement 2 (a NO-VERDICT band with numeric edges) still holds: the edges, run length and window are all numbers. What changed is that the band is no longer described as a stability region.

**Not done, offered separately:** if a stability claim is wanted, it would be a **new** instrument (e.g. max |cell − L| over the window, with its own base rate and edges), registered under the normal discipline. Not encoded here.

---
*Registration receipts:* grid script + FRED/Treasury pulls in session scratchpad (not repo); rerun: `fredgraph.csv?id=DFII10`, first-fire rule as §1.3. Companions: gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` · C#2 grade `research/2026-09-11_t12_c2_grade_and_gate_run.md` · 9/17 ask `PROME/inbox/processed/2026-09-17_from-NEXUS_full-matrix-sweep-delivered-and-the-T12-successor-ask-for-Will.md`.
