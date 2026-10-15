# WQ-342 SUCCESSOR — A CREDIT LEG FOR THE SPLIT · DRAFT v0, 2026-10-14 (NOT REGISTERED)

**Author:** NEXUS (Will-launched; Will 2026-10-14 21:21 ET, verbatim: *"start the draft now"*). **Status: DRAFT for the DOCKET L558 sitting (Mon 2026-10-19), where Will rules.** Nothing here moves the split or any Conf %; nothing is frozen until Will's word, and the anchor is a cell that will not exist until after it. **Owed before the sitting:** a cold read of this file, the commissioned CCC read (`research/2026-10-14_commission_CCC-gap_consumer-attribution.md`, due 10/19), and a re-run of §1 on the cells published by then.
**Brief (DOCKET L558):** *"a SUCCESSOR duration-split gate with a CREDIT LEG and its own base rate, decided at the `GATE-NEXUS-T12S-DFII10` grade; the frozen 9/02 letter is NOT edited."* **My rider binds:** PRED-50 graded OBSERVED (10/9), so the successor must **admit** a credit-class candidate. **Admission rules:** the frozen gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` §2 (a)–(e), applied exactly as the 9/24 real-yield letter applied them (`research/2026-09-24_t12_successor_DFII10_letter.md` §1).

## 0. The answer in five lines

1. **No broad-credit leg is admissible on the history FRED serves.** HY and B fail the gate at the 5-session run the real-yield letter uses. The only HY cells that pass (3-session runs) pass because two opposite things average out: starts in past stressed episodes resolved DOWN 91.7% of the time, while starts in the live episode resolve UP (31.4% UP, 2.9% DOWN). Registering that would certify a base rate supplied by the episode under test. **Not recommended.**
2. **One credit-class candidate clears every set, the live episode removed included: the CCC−B OAS gap** — 21 published sessions, ±25bp, 5 consecutive cells. It is the K-shape itself (§1.3).
3. ⚠️ **In the live episode it fires UP 88.6% of the time and DOWN never (0 of 35).** Registered now, an UP fire within the month is the base-rate-expected outcome: it would say "the K-shape continued", not "something new happened". The gap is also at its 3-year high (950bp [10/13]).
4. ⚠️ **Whether it is even eligible is Will's call:** on 9/17 he ruled a "CCC-relative spec" NOT (WQ-224 (ii)). This is a different observable (CCC minus B, not CCC against its own level), but a reader could fairly call it CCC-relative. NEXUS does not decide that.
5. **Recommendation:** register the CCC−B leg (§2) **if** Will says WQ-224 (ii) does not bar it, with caveat 3 printed on the split line; otherwise register no credit leg and put the words "credit-blind by construction" on the split line, so "held" is never read as "credit quiet".

---

## 1. CONSTRUCTION CHECKS — recorded before the letter

### 1.1 Instrument and data (pulled at primary)

FRED, ICE BofA OAS series, via `FORGE/tools/market-data/fetch.py fred <id> --periods 1200`, pulled 2026-10-14 ~21:30 ET. **FRED serves ICE history only from 2023-10-16** (785 cells per series, → 2026-10-13). Copies + scripts committed: `research/2026-10-14_wq342_grid/` (`gate_grid.py`, `gate_robust.py`; rerun: `python3 -I gate_robust.py CCCmB 21 25 5`). Values compared in **integer basis points** (published precision 0.01% = 1bp; no float compares). **14 bond-holiday carry-forward cells** (every ICE series identical to the prior cell, e.g. 2025-10-13, 2026-10-12) are **dropped** — they are not observations (tonight's 0b edge, fixed here by rule). n = 770 sessions.

**Regime set (gate 2(d), frozen text: "sessions starting with CCC ≥1000"):** six episodes — 2023-10-20→11-13 (17) · 2024-08-02→08-06 (3) · 2025-04-03→04-22 (13) · 2025-04-30 (1) · 2026-03-27→03-30 (2) · **2026-07-27→live (57)**. ⚠️ **The live episode supplies most of the regime starts.** Every figure below is therefore also shown with the live episode removed, and on the live episode alone.

### 1.2 Broad credit — HY (`BAMLH0A0HYM2`) and B (`BAMLH0A2HYB`)

Spec family identical to the 9/24 letter: anchor L = one cell; UP = ≥ L + D on k consecutive cells; DOWN = ≤ L − D on k consecutive; within the W cells after L; first to complete wins; else NO-VERDICT. Grid W ∈ {10, 15, 21, 25, 30} × D ∈ {10…50}bp.

| Candidate | Cells passing (a)–(c) on BOTH sets |
|---|---|
| HY, k = 5 | **0 of 35** — the regime set passes only at W15/D20 and W25/D30, where the unconditional set fails; elsewhere the in-regime ratio exceeds 3× (DOWN-dominated) |
| B, k = 5 | **0** |
| HY, k = 3 (search widened after k = 5 failed — disclosed) | 3: W15/D10 · W15/D15 · **W21/D20** |
| *CCC level, k = 5 (D ∈ {25, 50, 75, 100})* | *6 cells pass — but this is the CCC-relative spec Will ruled NOT on 9/17 (WQ-224 (ii)); shown for completeness, not proposed* |

**Why the HY k = 3 passes are rejected — the one robustness check that matters:**

| HY W21 / ±20bp / k3 | n | UP | DOWN | NV | ratio | (a)–(c) |
|---|---:|---:|---:|---:|---:|---|
| Unconditional | 749 | 21.2% | 28.0% | 50.7% | 1.32 | pass |
| Regime, pooled | 71 | 16.9% | 47.9% | 35.2% | 2.83 | pass |
| **Regime, live episode removed** | 36 | 2.8% | **91.7%** | 5.6% | 33.0 | **fail** |
| **Regime, live episode only** | 35 | **31.4%** | 2.9% | 65.7% | 11.0 | **fail** |

The pooled pass is two opposite one-sided sets averaging to a balanced number. The gate rule that an inadmissible falsifier is worse than an absent one, because it certifies, applies (gate §2; 9/24 letter §1.2).

### 1.3 The credit-class candidate that clears: the CCC−B gap (`BAMLH0A3HYC` − `BAMLH0A2HYB`)

**Plateau, not a knife-edge:** of 24 neighbouring cells (W ∈ {15, 21, 25} × D ∈ {20, 25, 30, 35} × k ∈ {3, 5}), **all 24 pass the pooled regime set and 16 pass the ex-live set**; the chosen cell passes every set at **k = 5, the real-yield letter's run length**, so no run-length search was needed for it.

| CCC−B, W21 / ±25bp / k5 | n | UP | DOWN | NV | ratio | (a)–(c) |
|---|---:|---:|---:|---:|---:|---|
| Unconditional | 749 | 32.6% | 19.2% | 48.2% | 1.69 | ✅ |
| Unconditional, non-overlapping (every 21st) | 36 | 22.2% | 22.2% | 55.6% | 1.00 | ✅ |
| **Regime, pooled (what 2(d) requires)** | 71 | 52.1% | 23.9% | 23.9% | 2.18 | ✅ |
| Regime, live episode removed | 36 | 16.7% | 47.2% | 36.1% | 2.83 | ✅ |
| *Regime, live episode only (not a gate set)* | 35 | **88.6%** | **0.0%** | 11.4% | ∞ | — |
| *Trailing year (not a gate set)* | 238 | 42.9% | 5.5% | 51.7% | 7.85 | ❌ (published so it is visible) |

**Caveats that travel with this leg — every one:**
1. ⚠️ **Three years is about one cycle.** 770 sessions clear the gate's ≥250 floor, but the regime set is six episodes, one of them live; the 9/24 letter's own lesson (caveat 1 there; its §5) is that a thin-episode conditional set can decide the outcome. A minimum-episode floor would fail this leg as it would have failed that one.
2. ⚠️ **The series trends.** The gap ran 428 → 950bp over the sample (median 577) and sits at its maximum now. Relative anchoring stops the level deciding the outcome; it does not stop the trend tilting it (trailing year UP 42.9% vs DOWN 5.5%).
3. ⚠️ **In this episode the leg is effectively one-sided:** DOWN has not completed once in 35 live-episode starts. Disc-J asks for symmetric magnitudes so that registration smuggles in no lean. The magnitudes are symmetric; the live reachability is not. Disclosed here, not used to veto: the gate has no live-episode rule, and adding one after seeing this result would be tuning.
4. ⚠️ **Grid exposure:** 4 instruments (HY · B · CCC level · CCC−B) × up to 2 run lengths × 3–5 windows × 4–7 magnitudes were rated. The cell was chosen because it passes every set at the existing run length, not for an outcome (the anchor is unpublished).
5. ⚠️ **Noise scale:** daily change σ = 6.9bp (trailing-250 σ 5.8bp), so ±25bp ≈ 4σ, held five sessions.
6. ⚠️ **Vintage:** ICE tier cells on FRED are latest-revised; only HY is revision-tested (LIQUID KB-LIQ-137). Hence the both-vintage rule in §2.

### 1.4 Disc-J requirements against §2

| # | Requirement | Where |
|---|---|---|
| 1 | Symmetric magnitudes | ±25bp edges; ±6pp consequences |
| 2 | Numeric NO-VERDICT band | L ± 25bp, run 5, window 21; C = neither run completes (stability is NOT what C measures — the 9/24 CATO RC1 lesson) |
| 3 | Non-renewable clause | §2: C#1 ⇒ one re-anchored window; C#2 ⇒ EXHAUSTED |
| 4 | Meaning of a repeated no-move | §3 |
| 5 | Reachability base rate on the text as written | §1.3 table |
| DAEDALUS Gate-Basis #2 (L13 deferral, owed at this registration) | Precision 1bp, integer compare · ties inclusive (≥ / ≤ at exactly L ± 25, the script's rule) · **actionable life: earliest fire = cell 5 ⇒ 17 of 21 cells** | §1.1 · §2 |

---

## 2. THE LETTER — DRAFT (becomes 🔒 FROZEN only on Will's word at the 10/19 sitting)

**Instrument:** G = FRED `BAMLH0A3HYC` − `BAMLH0A2HYB` (ICE BofA CCC & lower minus single-B US HY OAS), integer bp, **each cell as first published**. A cell on which every ICE OAS series repeats the prior cell on a bond-market full-close day is **not an observation** and does not break consecutiveness; a cell not yet published is not an observation.
**Anchor L:** the **first G cell published after Will's word** (unknown at writing).
**Window:** the **21 published cells after L** (≈ one month; counts cells, not dates). Earliest fire = cell 5.

| Branch | Condition | Consequence on the split (Break · Grind-lasts · Unresolved) |
|---|---|---|
| **UP — bottom-tier stress persisting** | 5 consecutive cells **≥ L + 25** | **Break +6pp, from Grind-lasts** |
| **DOWN — bottom tier healing** | 5 consecutive cells **≤ L − 25** | **Break −6pp, to Grind-lasts** |
| **C — NO-VERDICT** | neither completes by cell 21 | scores nothing; written EARNED |

**First to complete wins.** Unresolved-divergence is untouched (alternative mapping in §5, Will's choice).
**Non-renewable:** C#1 ⇒ exactly one re-anchored window (L₂ = cell 21); C#2 ⇒ EXHAUSTED, terminal; no third window without Will's word.
**Vintage (mirrors PRED-50 C1):** at grade, re-pull every cell of the run; a revision moving any run cell across L ± 25 ⇒ grade on both vintages; verdicts differ ⇒ INDETERMINATE-BY-VINTAGE (= C); same ⇒ it stands.
**Count-once with the real-yield letter (L13's re-anchored window 2, running in parallel):** if both letters fire in the **same** direction with fire cells ≤21 published cells apart, apply **one** ±6pp, not two (Disc-F: a shared R1 antecedent is presumed unless a registered test separates them). Opposite directions ⇒ both apply (net 0) and the conflict is written on the grade.
**Disc-A — graded separately, never a branch leg (gate (e)):**
- **UP's claim** is bottom-tier deterioration: TRUE-in-spirit only if **CCC itself is wider at the fire cell than at L**. A gap widening because B tightened faster (decompression on a rally) is TRUE-in-letter / FALSE-in-spirit.
- **DOWN's claim** is healing: TRUE-in-spirit only if **CCC is tighter at the fire cell than at L**. A gap closing because B widened toward CCC is contagion, a break reading, recorded as FALSE-in-spirit.
- The commissioned read (due 10/19) names candidate causes; it informs the Disc-A note, never the branch.
- Either way the letter's consequence applies as written; a letter/spirit split is recorded and routed to PROME.

**Grade:** first NEXUS session on/after the fire cell or cell 21 is published. Owner NEXUS; no other desk grades it.

## 3. What a repeated no-move would mean

C has a 48% unconditional base rate and 24% in-regime, so one C is ordinary. A double-C means neither direction sustained a 5-cell run in two windows: **no verdict on the K-shape**, clause EXHAUSTED. It does **not** mean credit was calm (C can arrive with cells outside L ± 25). **The self-protection tell:** if a branch fires and the split does not move ±6pp at the next re-mark, say so on the STATUS line.

## 4. What would falsify this draft

It is wrong if the leg returns C, or fires, **for a reason §1 could see** — above all caveat 3: an UP fire driven by the live episode's one-sidedness would mean the gate passed a description, and the lesson would be a live-episode or minimum-episode rule for gate 2(d). A clean DOWN fire in this episode would cut the other way: the leg was a test after all.

## 5. Choices that are Will's at the sitting

| # | Choice | NEXUS's recommendation |
|---|---|---|
| 1 | Does WQ-224 (ii) ("CCC-relative spec — NOT") bar a CCC-**minus-B** spec? | Will's reading; NEXUS sees a different observable but will not decide its own eligibility |
| 2 | Register the CCC−B leg (§2), or no credit leg | Register it with caveat 3 on the split line; if not, write "credit-blind by construction" on the split line |
| 3 | Mapping: Break ±6 from Grind (as drafted) **or** Unresolved-divergence ±6 from Grind (the K-shape as divergence, not as break precursor) | Break, to parallel L13. Unresolved is defensible: the gap measures divergence under a calm index |
| 4 | Broad credit (HY / B) | Not admissible on 3 years of FRED history; revisit when a longer series or a flow feed exists (WQ-224 (i) stays exhausted) |

*Receipts:* data + scripts `research/2026-10-14_wq342_grid/` (CSV sha256 prefixes `e47f73e2…` BAMLC0A0CM · `84c4961b…` HYM2 · `7ffcf93b…` BB · `253ee0d5…` B · `12746ff2…` CCC) · gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` · real-yield letter `research/2026-09-24_t12_successor_DFII10_letter.md` · rider DOCKET L558 · WQ-224 record `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md` row 224.
