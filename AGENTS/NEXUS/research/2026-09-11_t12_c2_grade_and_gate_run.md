# T-12 — SECOND EVALUATION (C#2) GRADE + ADMISSION-GATE RUN — 2026-09-11

**Author:** NEXUS · **Session:** PROME Tier-1 due-row spawn (WQ-184; DOCKET L289 due 2026-09-11) · **Graded:** 2026-09-11 ~10:4x ET, markets open · **Status:** 🔒 **FINAL — non-renewable clause EXHAUSTED.**
**Letter graded:** `research/2026-08-12_split_falsifier_RESOLUTION.md` ADDENDUM 2 (operative branch set, unamended). **Window:** `PREDICTIONS_MONITOR.md` L1a — FRED daily cells **2026-08-28 → 2026-09-10 inclusive**, pinned 2026-09-03 pre-event, objection window to PROME ran to 9/11 with none received (WQ-163 ⑥, Will *"163 - yes"*). **Gate applied:** `research/2026-09-02_t12_respec_admission_gate_prereg.md` (🔒 frozen 9/02, unamended; WQ-163 ⑤ RULED 9/07 = NO SPEND, run on what exists).

---

## 1. The observations, at primary, with dates

Live pull 2026-09-11 **10:37 ET** — `python3 FORGE/tools/market-data/fetch.py fred BAMLH0A0HYM2` (5-row tail) **and** `https://fred.stlouisfed.org/graph/fredgraph.csv?id=…` (full window); the two agree cell-for-cell.

| Cell | HY `BAMLH0A0HYM2` (bp) | CCC `BAMLH0A3HYC` (bp) | Inside (260, 280)? |
|---|---:|---:|---|
| 2026-08-28 | **260** | 1026 | edge — 260.0 is NOT <260 |
| 2026-08-31 | 263 | 1042 | yes |
| 2026-09-01 | 265 | 1049 | yes |
| 2026-09-02 | 266 | 1053 | yes |
| 2026-09-03 | 265 | 1051 | yes |
| 2026-09-04 | 268 | 1054 | yes |
| **2026-09-07** | **268** | 1055 | yes — ⚠️ **cell EXISTS (Labor Day); L1b had assumed no observation** |
| 2026-09-08 | 267 | 1056 | yes |
| 2026-09-09 | **271** (window max) | 1064 | yes |
| 2026-09-10 | 270 | **1070** (run high) | yes |

Window: HY max **271**, min **260.0** · CCC **1026 → 1070 = +44bp** vs HY **+10bp**.

## 2. Grade, branch by branch

- **A — RECOGNITION (HY ≥280 sustained 3 AND CCC retraces <40% of any HY retracement):** zero cells ≥280 ⇒ level leg NOT MET ⇒ **A NOT MET.** The retracement leg is moot (no A-run to attach it to; HY's only in-window retracement is 271→270 on 9/10, 1bp, during which CCC rose +6 — the degenerate-denominator case §4 of the 8/28 record warned about, not computed).
- **B — BETA (HY <260 sustained 3):** zero cells <260. The 8/28 cell is **260.0** — a STRICT miss, the same one the 8/28 grade recorded ⇒ **B NOT MET.**
- **C — neither ⇒ NO-VERDICT. EARNED. FINAL.** This is **C #2 of 2** — the non-renewable clause is **EXHAUSTED.**

**Disc-A (mechanism, graded separately from the threshold):** no threshold fired, so there is nothing to attribute — but the window's shape is itself the finding the 8/12 letter pre-wrote for a double-C: *"the CCC tail is a permanent structural feature of this index, not a signal, and T-12's level leg is measuring a constant."* CCC widened 4.4× the index inside a window in which the index moved 10bp. The K-split (M-08) is the row's characteristic, not its signal.

## 3. L1b — the reachability claim, graded against itself

**Conclusion RIGHT, premise WRONG.** WALTER `SIG-W-20260908-005` (9/8) reported a 9/7 cell at 268; **VERIFIED at FRED 9/11.** With a 9/7 cell the possible sustained-3 runs remaining as of 9/7 were {9/4, 9/7, 9/8} · {9/7, 9/8, 9/9} · {9/8, 9/9, 9/10} ⇒ the necessary condition for any non-C verdict was **the 9/8 cell alone**, not "9/8 AND 9/9". A weaker condition, satisfied the same way (9/8 = 267 inside (260, 280) ⇒ C locked on 9/8's publication). The CPI-independence finding (the 9/11 cell is outside the window) stands on the corrected premise. Lesson: a calendar assumption about a series is a claim to verify **at the series** — `[[finding_dated_carry_item_has_no_expiry_check]]`.

## 4. The consequence, executed in the pre-registered order (gate §4)

1. **Graded first** (§1–2 above). No re-spec work preceded the grade.
2. **C #2 fired ⇒ the re-spec is FORCED.** Gate §2 (a)–(e) run against each pre-named candidate (8/12 §86 · 8/28 §7.1: *CCC flow share of index moves · CCC issuance/refi volumes · the 319bp basket · single-name CDS*) at the window it would actually run:

| Candidate | History available to this desk | (a)–(e) computable? | Verdict |
|---|---|---|---|
| CCC **flow** share of index moves (RED's weight arithmetic) | no series feed at NEXUS — **SEARCH-NOT-FOUND** (checked: `FORGE/tools/market-data/fetch.py` FRED/EIA/Yahoo only; no RED-published daily series consumed here) | NO | ⛔ **NOT ADMISSIBLE — cannot be base-rated** |
| CCC issuance / refi volumes | no feed — SEARCH-NOT-FOUND | NO | ⛔ NOT ADMISSIBLE — cannot be base-rated |
| Single-name CDS (ORCL/NVDA etc.) | no feed — SEARCH-NOT-FOUND | NO | ⛔ NOT ADMISSIBLE — cannot be base-rated |
| **319bp basket** (Goldman + JPMorgan 18-name AI-credit HY baskets, launched **2026-07-23** — WALTER `SIG-W-20260727-018`, BROCK brief) | series exists at the banks; **launched ~35 trading sessions ago** | NO — the gate requires **≥250 sessions of the instrument's OWN history** | ⛔ **NOT ADMISSIBLE BY CONSTRUCTION until ~mid-2027**, feed or no feed |

   **0 of 4 admissible.** No (a)–(e) figures are published because none could be computed — publishing a blank table is the honest form; inventing a proxy series would be the contamination the gate exists to prevent.
3. **None clears ⇒ register NO successor and escalate** (gate §4.3). Done: `STATUS.md` split line now carries **"currently un-falsifiable"** (Disc-J) on its own line; the ask is in the 9/11 delivery memo to PROME for Will.
4. **Delta-leg degeneracy carried forward, not solved** — noted in §2 (1bp denominator on 9/10).
5. **Said out loud (Disc-J requirement 4):** the gate pre-committed that a third NO-VERDICT would mean *the instrument class is wrong.* Two consecutive C's plus the 9/02 window measurement (no spread-LEVEL spec admissible under 21 sessions) now make that the standing verdict for T-12 on spread levels at any horizon this desk can act on.

## 5. Noted, NOT registered — the one thing that passes the arithmetic

The gate's own §3.3 sweep found **CCC-relative, 21 sessions, ±50bp: BREAK 27.4% · GRIND 17.0% · NO-VERDICT 55.4% · ratio 1.61 — PASS.** It is **excluded** because (i) it is not on the pre-named list and choosing it now would be a post-hoc pick, and (ii) it is a spread LEVEL — the class the double-C just impeached. It is offered to Will as an **OBSERVABLE** (a dated CCC-relative watch), never as the falsifier. Regime-conditional figure for it was NOT run on 9/02 at W=21 and would be owed before any registration (gate 2(d)).

## 6. Anti-rationalization, against myself

- The interested party pinned the window (9/03) and graded it (9/11). Mitigation: the pin was pre-event, flagged to PROME for objection, and ruled (WQ-163 ⑥); the cells are public; the verdict is arithmetic on ten numbers anyone can re-pull.
- The 8/28 cell at exactly 260.0 sits on B's edge twice now. A reader could say "B nearly fired." The letter says **<260**; 260.0 is not below it; and a 1-cell touch is not a sustained-3 run in either reading.
- The flow/volume candidates were named by me on 8/12, and I have no feed for three of them. That is a construction error of the 8/12 letter — naming candidates one cannot measure — recorded here as mine; the 9/02 gate §5 named it 9 days before the deadline, and WQ-163 ⑤ ruled the response (NO SPEND, run on what exists).

## 7. What this does and does not touch

- **Touches:** `PREDICTIONS_MONITOR.md` L1/L1a/L1b (graded) · `STATUS.md` T-12 row, split block, header, docket rows · this record.
- **Does NOT touch:** any threshold, any convergence Conf %, the split's numbers (20/47/33 — the letter says a C *scores NOTHING*), the frozen letter (unamended ⇒ WQ-163 item 3 not triggered), any other desk's file. **$0.**

## 8. The ask (for Will, via PROME — decision is Will's)

One of: **(i)** a flow/issuance data feed or an owner who has one (RED for the weight arithmetic? LIQUID/BROCK for issuance?) so a candidate can be base-rated · **(ii)** accept the CCC-relative 21-session ±50bp spec as a registered **OBSERVABLE** while the split stays un-falsifiable · **(iii)** carry the un-falsifiable line as is. NEXUS recommends **(i) if it costs nothing, else (iii)** — an openly absent falsifier beats a certified one (WQ-163 ⑤'s own logic).

*Companions: `research/2026-08-28_successor_falsifier_RESOLUTION.md` (C #1) · `research/2026-09-02_t12_respec_admission_gate_prereg.md` (the gate) · `research/2026-08-12_split_falsifier_RESOLUTION.md` (the letter).*
