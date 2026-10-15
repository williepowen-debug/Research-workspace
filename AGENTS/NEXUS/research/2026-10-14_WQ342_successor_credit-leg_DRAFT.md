# WQ-342 SUCCESSOR — A CREDIT LEG FOR THE SPLIT · DRAFT v1, 2026-10-14 (NOT REGISTERED)

**Author:** NEXUS (Will-launched; Will 2026-10-14 21:21 ET, verbatim: *"start the draft now"*; cold read run at his word *"run the cold read on the draft now"*). **Status: DRAFT for the DOCKET L558 sitting (Mon 2026-10-19), where Will rules.** Nothing here moves the split or any Conf %; nothing is frozen until Will's word, and the anchor is an observation that does not yet exist. **v1 = v0 (`361a70df6`) corrected on a cold read — 8 ❌ · 25 ⚠️ · 33 ✅, ledger `recon/2026-10-14_coldread_wq342_draft_v0_ledger.md`; what changed is §6.** **Owed before the sitting:** a scoped re-read of v1 (a correction pass is unreviewed work), the commissioned CCC read (DOCKET L708, due 10/19), and a re-run of §1 on the cells published by then.
**Brief (DOCKET L558):** *"a SUCCESSOR duration-split gate with a CREDIT LEG and its own base rate, decided at the `GATE-NEXUS-T12S-DFII10` grade; the frozen 9/02 letter is NOT edited."* **My rider binds:** PRED-50 graded OBSERVED (10/9), so the successor must admit a credit-class candidate — if one is admissible. **Admission rules:** the frozen gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` §2 (a)–(e).

## 0. The answer, with the caveats that could change the decision

1. **First, eligibility, which is Will's.** No credit instrument is on the frozen gate's pre-named candidate list (gate §4.2: CCC flow share · CCC issuance/refi · the 319bp basket · single-name CDS). Will refused WQ-224 (ii) on 9/17 (Decision Deck APPROVE of PROME's rec: "try (i) FIRST, fallback (iii), NOT (ii)" — `PROME/archive/WILL_QUEUE_ROWS_2026-09-26_rolloff.md` row 224), and the recommendation he approved gave exactly that ground: *"NOT (ii) — admitting a spec the letter excludes is the WQ-189 failure"* (`PROME/registry/WQ_LEDGER.tsv` line 290). (ii) itself was *"accept NEXUS's CCC-relative 21-session ±50bp spec as a registered OBSERVABLE (it passes the gate arithmetic but the letter excludes it)"* (`git show 1a3fe9c53:PROME/WILL_QUEUE.md` L42) — and the real-yield leg needed his word for the same reason (WQ-261 added `DFII10` to the list). **So any credit leg here needs Will's word adding its instrument. Question for him: does L558's 9/30 "with a CREDIT LEG" already give it, or is a separate word needed?**
2. **The standard applied — one, to every candidate:** the frozen gate as written, with the letter family's **5-session run held fixed** (the real-yield letter's run length, not searched here). Every robustness view is **reported** for every candidate and **used to veto none** — the 9/24 precedent ("reported, not used to veto: the gate has no episode-exclusion rule").
3. **Under that standard:** HY and B have **no gate-admissible cell** at the 5-session run. The **CCC−B OAS gap** (21 sessions, ±25bp, 5-session run) **passes every gate set** (unconditional and regime-conditional), and 18 of 24 neighbouring cells do too.
4. ⚠️ **Three years of data is about one credit cycle, and it shows in every candidate.** FRED serves ICE spreads only from 2023-10-16. Each candidate's stressed-regime base rate is an average of a few one-sided episodes. For CCC−B: April 2025 resolved DOWN in 12 of 13 starts, October–November 2023 supplied 5 of the 6 past UP fires, and the live episode resolves UP in 31 of 35 starts with DOWN never. **No cell choice fixes this; it is a property of the data length.**
5. ⚠️ **In the episode it would run in, the CCC−B leg is one-sided.** Live episode: UP 88.6% · DOWN 0%; trailing year: UP 42.9% · DOWN 5.5% (fails the ratio test, 7.85×). **An UP fire is the expected outcome and would be weakly informative; a DOWN fire would be the informative result.** The gap also has **no history at today's level**: it first reached 700bp on 2026-07-24 and sits at 950bp [10/13], the sample maximum.
6. ⚠️ **Actionable life is flagged:** 14 of 21 cells (67%) by DAEDALUS's formula (§1.4) ⇒ BASIS-UNNAMED (actionable-life) — named here.
7. **The alternative Will could choose:** at a **3-session run**, three HY cells are gate-admissible. One (15 sessions, ±10bp) passes 5 of 6 robustness views, more than CCC−B. NEXUS does not recommend it: the run length was searched after the 5-session run failed, and ±10bp is about 0.4σ of a 15-session HY move (26.6bp), so it fires in ~71% of windows.
8. **Recommendation:** if Will adds the instrument, register the CCC−B leg (§2) with caveats 4–5 printed on the split line. If he does not, register no credit leg, and the split line carries the gate's prescribed words (§4.3) **"currently un-falsifiable"** on credit. The rider cannot be met by an inadmissible leg, and saying so is the honest outcome.

---

## 1. CONSTRUCTION CHECKS — recorded before the letter

### 1.1 Instrument and data (pulled at primary)

FRED ICE BofA OAS series via `FORGE/tools/market-data/fetch.py fred <id> --periods 1200`, pulled 2026-10-14 (CSV mtime 21:26 ET). **FRED serves ICE history only from 2023-10-16:** 785 cells for HY, B, CCC and BB; IG has 784 (no 2024-12-24 cell). The scripts intersect all five series, so G loses the 2024-12-24 cell (one cell; not re-run without it — disclosed). Copies + scripts committed: `research/2026-10-14_wq342_grid/` (`gate_grid.py`, `gate_robust.py`; rerun `python3 -I gate_robust.py CCCmB 21 25 5`). Levels compared in **integer basis points** (published precision 0.01% = 1bp). The gate's ratio test is applied to counts (pass iff the larger branch ≤ 3× the smaller; two HY cells sit at exactly 3.00× and pass). **14 carry-forward cells** — all five series identical to the prior cell (every one a bond-market holiday, e.g. 2025-10-13, 2026-10-12) — are dropped; n = 770. BB and IG are used only to detect carry-forwards; they were not rated.

**Regime set (gate 2(d), frozen text: "(here: sessions starting with CCC ≥1000)"):** six episodes — 2023-10-20→11-13 (17 cells) · 2024-08-02→08-06 (3) · 2025-04-03→04-22 (13) · 2025-04-30 (1) · 2026-03-27→03-30 (2) · **2026-07-27→live (56)**; 92 cells. In the 21-session gate set the live episode is 35 of 71 starts (49%). ⚠️ The 9/24 letter used its instrument's own regime (`DFII10` ≥2.50); G cannot be base-rated in its own terms, because G ≥700 exists only from 2026-07-24.

### 1.2 Broad credit — HY (`BAMLH0A0HYM2`) and B (`BAMLH0A2HYB`)

Spec family identical to the 9/24 letter: anchor L; UP = ≥ L + D on k consecutive cells; DOWN = ≤ L − D on k consecutive; within the W cells after L; first to complete wins; else NO-VERDICT. Grid W ∈ {10, 15, 21, 25, 30} × D ∈ {10, 15, 20, 25, 30, 40, 50}bp.

| Candidate | Cells passing (a)–(c) on BOTH gate sets |
|---|---|
| **HY, k = 5** | **0 of 35** (the regime set alone passes at W15/D20 and W25/D30, where the unconditional set fails) |
| **B, k = 5** | **0** |
| *HY, k = 3 (run length searched after k = 5 failed)* | *3 — W15/D10 · W15/D15 · W21/D20 (robustness below; Will's option, §0.7)* |
| *CCC level, k = 5 (D ∈ {25, 50, 75, 100})* | *6 — not proposed: WQ-224 (ii) refused this instrument class on the pre-named-list ground* |

**HY k = 3, robustness views for all three gate-admissible cells (reported, not used to veto):**

| HY k3 | Uncond | Non-overlap | Regime | Regime ex-live | Live only | Trailing year | Views passed |
|---|---|---|---|---|---|---|---:|
| W15/±10 | 29.1/42.3/28.6 ✅ | ✅ | 18.2/54.5/27.3 ✅ (3.00×) | 5.6/94.4/0.0 ❌ | 29.3/19.5/51.2 ✅ | 30.7/28.3/41.0 ✅ | 5 of 6 |
| W15/±15 | 21.3/28.2/50.5 ✅ | ✅ | 14.3/42.9/42.9 ✅ (3.00×) | 2.8/88.9/8.3 ❌ | 24.4/2.4/73.2 ❌ | 18.9/15.2/66.0 ❌ | 3 of 6 |
| W21/±20 | 21.2/28.0/50.7 ✅ | ✅ | 16.9/47.9/35.2 ✅ | 2.8/91.7/5.6 ❌ | 31.4/2.9/65.7 ❌ | 18.9/15.5/65.5 ❌ | 3 of 6 |

*(UP / DOWN / NO-VERDICT %.)*

### 1.3 The CCC−B gap (`BAMLH0A3HYC` − `BAMLH0A2HYB`) — passes the gate at k = 5

| CCC−B, W21 / ±25bp / k5 | n | UP | DOWN | NV | ratio | Gate |
|---|---:|---:|---:|---:|---:|---|
| Unconditional | 749 | 32.6% | 19.2% | 48.2% | 1.69 | ✅ |
| Regime, pooled (what 2(d) requires) | 71 | 52.1% | 23.9% | 23.9% | 2.18 | ✅ |
| *Robustness — non-overlapping (every 21st)* | 36 | 22.2% | 22.2% | 55.6% | 1.00 | pass |
| *Robustness — regime, live episode removed* | 36 | 16.7% | 47.2% | 36.1% | 2.83 | pass (by 0.17×) |
| *Robustness — live episode only* | 35 | 88.6% | 0.0% | 11.4% | ∞ | **fail** |
| *Robustness — trailing year* | 238 | 42.9% | 5.5% | 51.7% | 7.85 | **fail** |

**By episode (regime starts with a complete window):** 2023-10/11: UP 5 · DOWN 1 · NV 11 · 2024-08: 0 · 1 · 2 · 2025-04-03→22: UP 1 · **DOWN 12** · NV 0 · 2025-04-30: 0 · 1 · 0 · 2026-03: 0 · 2 · 0 · **live: UP 31 · DOWN 0 · NV 4**. The "ex-live" pass is April 2025 against 2023 — one-sided episodes averaging out, the same shape seen in HY.

**Neighbouring cells (W ∈ {15, 21, 25} × D ∈ {20, 25, 30, 35} × k ∈ {3, 5} = 24), all six views:** unconditional 18 · non-overlapping 14 · regime 24 · **both gate sets 18** · gate sets + ex-live 12 · ex-live 16 · live only **0** · trailing year **0**. The one-sidedness belongs to the instrument in this regime, not to the chosen cell.

**Caveats that travel with this leg:**
1. ⚠️ **Thin and one-sided episodes** (above). The 9/24 letter's §5 named a minimum-episode floor as the lesson its own failure would teach; it was never set. Its past UP fires come from three episodes (2023: 5 · April 2025: 1 · live: 31) and its DOWN fires from five, so any floor of more than three episodes per branch would fail it.
2. ⚠️ **Trend:** G ran 524 (first cell) → 428 (minimum, 2025-01-23) → 950 (maximum, now); median 578 (n = 770). Relative anchoring stops the level deciding the outcome; it does not stop the trend tilting it.
3. ⚠️ **One-sided in the live episode** (§0.5). Disclosed, not used to veto: the gate has no live-episode rule, and adding one after seeing this would be tuning.
4. ⚠️ **Grid exposure:** 4 instruments rated (HY · B · CCC level · CCC−B) × up to 2 run lengths × 3–5 windows × 4–7 magnitudes. The leg's cell was chosen because it passes both gate sets at the fixed run length; its outcome is unknown (the anchor is unpublished).
5. ⚠️ **Scale:** daily-change σ 6.9bp, but the relevant scale is the 21-session move, σ 44.4bp; ±25bp ≈ 0.56σ of a month's move, held five sessions.
6. **Vintage:** LIQUID's 10/14 check found first-published = latest-revised for B, CCC and HY over 8/20–10/13 (LIQUID STATUS), and PRED-50's 27 re-pulled cells were unchanged. `fetch.py` returns latest-revised values, so "first published" in §2 means **first read by NEXUS**, logged at read.

### 1.4 Charter tests against §2

| Test | Where |
|---|---|
| Disc-J 1 symmetric magnitudes | ±25bp edges; ±6pp consequences |
| Disc-J 2 numeric NO-VERDICT band | L ± 25bp, run 5, window 21; C = neither run completes (C does not measure stability — the 9/24 RC1 lesson) |
| Disc-J 3 non-renewable | §2: C#1 ⇒ one re-anchored window; C#2 ⇒ EXHAUSTED, with the split-line words named |
| Disc-J 4 repeated no-move | §3 |
| Disc-J 5 reachability base rate | §1.3 |
| BOOT 0b (i) date · (ii) magnitude · (iii) resolver exists · (iv) exclusive + exhaustive with five counterexamples | §2: expected calendar + backstop date · ±25bp · FRED ICE series (the resolver exists; a data outage is handled by VOID) · counterexample table |
| DAEDALUS Gate-Basis #2 (owed at this registration) | precision 1bp, integer compare · ties inclusive at exactly L ± 25 · **actionable life = 21 − 1 (publication lag) − 5 (minimum run) − 1 (one tradable session) = 14 of 21 = 67% ⇒ BASIS-UNNAMED (actionable-life), named** · earliest completion = cell 5 |

---

## 2. THE LETTER — DRAFT (🔒 frozen only on Will's word at the 10/19 sitting)

**Instrument:** G = FRED `BAMLH0A3HYC` − `BAMLH0A2HYB`, integer bp, each cell **as first read by NEXUS** (logged at read in `analysis/WQ342_grading_log.tsv`). **A cell on which all five ICE series (`BAMLH0A0HYM2` · `BAMLH0A1HYBB` · `BAMLH0A2HYB` · `BAMLH0A3HYC` · `BAMLC0A0CM`) equal their prior cell is not an observation**: it does not count toward the window and does not break a run. A cell not yet published is not an observation.
**Anchor L:** the G cell for the **observation date of Will's ruling** (if he rules Mon 10/19: the 10/19 observation, published ~10/20); if that date is not an observation, the next observation.
**Window:** the **21 observations after L**. If L = obs 10/19, the expected calendar is earliest fire = cell 5 = obs Mon 10/26, cell 21 = obs Tue 11/17 (Wed 11/18 if Veterans Day 11/11 is a carry-forward). NEXUS packets PROME both dates for DOCKET wake rows on registration.
**Backstop (n = 0 / n = 1 / outage):** if cell 21 is not published by **L's observation date + 45 calendar days** (≈ 12/03 for L = 10/19), grade on the cells published: a completed run fires; ≥5 cells and no run ⇒ C; **fewer than 5 cells ⇒ VOID** (instrument fault; does not consume C#1; re-anchor only on Will's word).

| Branch | Condition | Consequence on the split (Break · Grind-lasts · Unresolved) |
|---|---|---|
| **UP — bottom-tier stress persisting** | 5 consecutive observations **≥ L + 25** | **Break +6pp, from Grind-lasts** |
| **DOWN — bottom tier healing** | 5 consecutive observations **≤ L − 25** | **Break −6pp, to Grind-lasts** |
| **C — NO-VERDICT** | neither completes by cell 21 | scores nothing; written EARNED |

First to complete wins (a cell cannot satisfy both edges, so the branches are exclusive; UP / DOWN / C / VOID are exhaustive). Unresolved-divergence is untouched (alternative mapping, §5).

**Counterexamples** (L = 900; computed by running the rule):
| Case | Cells | Grade |
|---|---|---|
| Lower boundary, inclusive | 875 ×5 | DOWN at cell 5 |
| One bp inside the lower edge | 876 ×5, then 900 | C |
| Upper boundary, inclusive | 925 ×5 | UP at cell 5 |
| Mixed: UP run of 4 broken, then a DOWN run | 925, 930, 926, 940, 900, 870, 860, 875, 850, 872 | DOWN at cell 10 |
| Mixed: both edges touched, neither held five | alternating ±30–40 around L | C |
| n = 0 at the backstop | none | VOID |
| n = 1 at the backstop | 990 | VOID |
| Short window at the backstop, run completes | 900 ×4, 930 ×5, 900 ×3 (12 cells) | UP at cell 9 |

**Non-renewable:** C#1 ⇒ exactly one re-anchored window (L₂ = cell 21); C#2 ⇒ EXHAUSTED, terminal; the split line then reads **"credit leg EXHAUSTED — currently un-falsifiable on credit"**, and no third window is registered without Will's word.
**Vintage (mirrors PRED-50 C1):** at every grade, including C, re-pull L and every window cell. If any revision changes the outcome — it moves L, or creates or breaks a run — grade on both vintages; if they differ ⇒ INDETERMINATE-BY-VINTAGE (= C); if they agree, the grade stands.
**Count-once with the real-yield letter** (L13's re-anchored window 2, running in parallel): if both letters fire in the **same** direction with fire **observation dates ≤30 calendar days apart**, apply **one** ±6pp. A shared antecedent is presumed unless a registered test separates them. Opposite directions ⇒ both apply (net 0), and the conflict is written on the grade.
**Disc-A — graded separately, never a branch leg (gate (e)).** ΔCCC and ΔB = fire-cell value − value at L:
- **UP is TRUE-in-spirit iff ΔCCC > 0.** ΔCCC ≤ 0 (the gap widened because B tightened: a decompression on a rally) ⇒ TRUE-in-letter / FALSE-in-spirit.
- **DOWN is TRUE-in-spirit iff ΔCCC < 0 AND ΔB ≤ 0.** Otherwise (e.g. ΔCCC −5 with ΔB +25: the gap closed because B widened toward CCC — contagion, a break reading) ⇒ FALSE-in-spirit.
- The letter's consequence applies as written either way; a letter/spirit split is recorded and routed to PROME. The commissioned read (DOCKET L708) informs the Disc-A note, never the branch.

**Grade:** first NEXUS session on/after the fire observation, cell 21, or the backstop is published. Owner NEXUS; no other desk grades it.

## 3. What a repeated no-move would mean

C runs 48% unconditional, 24% in the pooled regime, and **11.4% in the live episode** (4 of 35). One C is ordinary. A C in this episode would be unusual and mildly informative (the trend paused). A double-C means neither direction held a 5-observation run in two windows: no verdict on the K-shape; the clause is EXHAUSTED (§2 words). It does not mean credit was calm. **The self-protection tell:** if a branch fires and the split does not move ±6pp at the next re-mark, say so on the STATUS line.

## 4. What would falsify this draft — operational

- **An UP fire with Disc-A FALSE** (G widened while CCC did not) ⇒ the gate passed a dispersion move that is not stress. The lesson would be to require the CCC leg's own direction inside the branch, proposed to Will, never applied retroactively.
- **An UP fire with Disc-A TRUE** is the base-rate-expected outcome (88.6% in the live episode). It is recorded on the split line as **weakly informative** and does not validate the leg.
- **A DOWN fire** in this episode (0 of 35 so far) would be the informative result: the leg tested something.

## 5. Choices that are Will's at the sitting

| # | Choice | NEXUS's recommendation |
|---|---|---|
| 1 | Add a credit instrument to the gate's pre-named list — does L558's 9/30 "with a CREDIT LEG" already do it, or is a separate word needed? (the ground in the WQ-224 rec Will approved: "admitting a spec the letter excludes") | Will's reading; without his word no credit leg is admissible |
| 2 | Which instrument, if added: CCC−B at k = 5 (§2), or HY at k = 3 (§0.7) | CCC−B, with caveats 4–5 on the split line |
| 3 | Mapping: Break ±6 from Grind (as drafted), or Unresolved-divergence ±6 from Grind (the K-shape as divergence) | Break, to parallel L13; Unresolved is defensible |
| 4 | If no instrument is added | The split line carries "currently un-falsifiable on credit" (gate §4.3) |

## 6. v0 → v1 (the cold read's findings and what changed)

❌ fixed: one standard for every candidate (v0 vetoed HY on episode splits and refused them for CCC−B) · "not admissible" now means the gate's word (HY k=3 cells ARE gate-admissible; shown) · HY robustness published for all three k=3 cells (v0 generalised from W21/D20; W15/D10 passes 5 of 6 views) · "clears every set" → every GATE set, with the live-only and trailing failures in §0 · WQ-224 (ii) ground corrected: the pre-named list, not CCC-relativity (the cold read located the quote in the rolloff row; it is in PROME's rec, `WQ_LEDGER.tsv` line 290, which Will approved — re-located at the source before use) · live episode 56 cells (v0: 57) · actionable life 14 of 21, flagged (v0: 17 of 21, escaped the flag) · counterexamples, backstop/VOID and expected calendar added. ⚠️ fixed: per-episode table · G's own-regime limit · all six plateau views · anchor named by observation date · carry-forward series named, not counted in the window · count-once in calendar days · Disc-A as iff with tie rules · vintage re-pull at every grade · first-read capture named · vintage caveat updated (LIQUID 10/14) · rider vs "no leg" resolved in §0.8 · gate §4.3 citation · σ at the window scale · minimum/first-cell/median corrected · IG missing cell disclosed · ratio test on counts · regime share at W21 · EXHAUSTED words · live-episode C rate · D values listed · data time from file metadata.

*Receipts:* data + scripts `research/2026-10-14_wq342_grid/` (CSV sha256 prefixes `e47f73e2…` BAMLC0A0CM · `84c4961b…` HYM2 · `7ffcf93b…` BB · `253ee0d5…` B · `12746ff2…` CCC) · gate `research/2026-09-02_t12_respec_admission_gate_prereg.md` (§2, §4.2 list, §4.3) · real-yield letter `research/2026-09-24_t12_successor_DFII10_letter.md` · rider DOCKET L558 · commission DOCKET L708 · WQ-224 record as cited in §0.1 · DAEDALUS formula `AGENTS/DAEDALUS/sweeps/GATE_BASIS_SWEEP.md` · cold-read ledger `recon/2026-10-14_coldread_wq342_draft_v0_ledger.md`.
