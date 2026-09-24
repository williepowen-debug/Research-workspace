# T-12 SUCCESSOR — REAL-RATE LEG (`DFII10`), BANDED LETTER · REGISTERED 2026-09-24 ~15:1x ET

**Author:** NEXUS (PROME spawn `prome-3f`, WQ-206 drain + encode) · **Status:** 🔒 **FROZEN AT REGISTRATION** — no amendment without a Will word or a written re-registration carrying its own date, reason and a re-run of every §1 check against the amended words (gate §1 rule: an amendment inherits the original's certificate only if the checks are re-run).
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
| 2 | Numeric NO-VERDICT band | L − 0.10 < cell < L + 0.10 held through the window |
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

A C has a 56% unconditional base rate (36% in-regime), so **one C is ordinary**, and a double-C happens by chance roughly **31% (13% in-regime)** of the time — **a double-C does not prove the instrument class wrong** the way T-12's did. What it **would** say: real yields held within ±10bp for ~30 sessions from an elevated level, i.e. **the price-of-money channel went quiet.** That counts against my own 9/17 reading (*"the bear's case has migrated almost entirely into the price of money"*) and gets recorded that way, not as "no information."
**The self-protection tell:** if a branch fires and the split does not move by its ±6pp at the next re-mark, that is the pattern Disc-J was written from. Say so on the STATUS line.

## 4. First grade

**Not immediate.** The anchor cell is unpublished; the earliest possible fire is the 5th cell after it (≈10/1). *(The literal one-sided reading would have been immediate, see §1.2. That is the reason it is not the letter.)*

## 5. What would falsify this record

It is wrong if the letter returns a C (or fires) **for a reason §1 could have seen**, e.g. the thin-episode tilt of caveat 1 turns out to be what decided it. That would count against the gate's thresholds as applied to a 5-episode conditional set, and the lesson would be that 2(d) needs a minimum-episode floor, not only a minimum-session floor. It is **not** falsified by a clean fire in either direction.

## 6. Relation to WQ-224 (the flow-feed search)

Path (i) is exhausted across RED · LIQUID · BROCK (PROME packet 9/18). **I do not take LIQUID's conditional door on the three zero-pinned repo/RRP series**, so (iii)'s un-falsifiable line for the FLOW class stands, and **this `DFII10` letter is the primary T-12 successor.** If a flow series later clears the gate, the ruling makes the choice of primary leg mine, and I would make it on a fresh gate run, not by swapping legs mid-window.

---
*Registration receipts:* grid script + FRED/Treasury pulls in session scratchpad (not repo); rerun: `fredgraph.csv?id=DFII10`, first-fire rule as §1.3. Companions: gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` · C#2 grade `research/2026-09-11_t12_c2_grade_and_gate_run.md` · 9/17 ask `PROME/inbox/processed/2026-09-17_from-NEXUS_full-matrix-sweep-delivered-and-the-T12-successor-ask-for-Will.md`.
