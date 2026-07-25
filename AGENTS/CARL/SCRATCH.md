# CARL SCRATCH
**Last session:** 2026-07-24 (Fri) ~14:00–21:00 ET — long Will-directed session, 7 passes
**Type:** 6-day-gap catch-up → then Will-directed build-out. **No score change all session: 51/70 holds.** THESIS **v2.6.3**.

---

## 🔴 PRIORITY-1 — FOMC Tue-Wed 7/28-29. The leg is WRITTEN; Tuesday's job is to EXECUTE it, not rebuild it.

`thesis/FOMC_JUL28-29_CARL_CONSUMER_LEG.md`. **Consume RED-20 / BOND's falsifier map / VIOLET's tree — do NOT build a fourth rates tree.**
- **Pre-registered language priors (grade regardless of the rate decision):** L1 pass-through **35** · **L2 look-through 40** *(RED says 30 — both on the record, grade both)* · L3 growth-tax **10** · mixed **12** · **L4 cohort language 15%**, scored independently.
- **L4 is the CARL-specific tell:** does Warsh bring *distributional* language into the presser himself? The Beige Book has said "increasingly bifurcated" twice; the Chair has not. **Bias guard is pre-registered** — counts only in his own framing, about US household distribution. Don't loosen it on Wednesday.
- **Listen to the presser or read the full transcript — never a wire summary.**
- ⚠️ **§0.2 is WITHDRAWN** (RED rejected it on sequencing and was right): the correction *raises* hold-and-point-at-September; it does **not** strengthen hike-now. Do not re-introduce it.

**PRIORITY-2 — ~8/3: V5 3→4 decides.** ✅ **Will ruled: decide at the sustained-window close per the 7/16 card, no early bump.** Gas $4.105 on 7/24 — 4 days above $4.00 and rising.

---

## ⚠️ CARRY FORWARD — corrections that are easy to lose
1. **July CPI prints Wed 8/12, NOT 8/13. August CPI Fri 9/11, NOT ~9/10. Sept CPI 10/14.** (RED S25b off the OMB PFEI schedule; `bls.gov` 403s even with a browser UA — use the OMB PDF with `pdftotext -layout`.) **September's FOMC carries an SEP + fresh dots; July's does not. The August CPI lands INSIDE the Fed blackout (opens 9/5).**
2. **The 8/12 print will be SOFT on gasoline by arithmetic (~−2.6% MoM)** — June averaged $4.050 running downhill, July ~$3.95. **A soft print is a base effect, NOT a mechanism failure.** Pre-registered so neither I nor RED can score it as falsification. **The real oil test is 9/11.** Three independent derivations (CARL + HENRY off gasoline; **RED off spot Brent — theirs is load-bearing, it carries no retail-lag assumption**).
3. **Never blanket-replace a date across files** — my first pass silently rewrote RED's verbatim quote inside my own doc. The quote stays wrong; the correction goes beside it.

---

## ✅ WILL'S RULINGS (proposal loop closed, Rule 10)
- **CRL-21 position-action → DEFERRED to the ~8/15 HHDC, decided by the frozen card's cells.** D → full commitment (trim 25% + duration); C → duration-half only; A/B → hold to the ~Oct vintage leg. TERRY constructs. Aug-21 expiries (OZK ×5, KRE ×3, WAL ×1) handled in the same post-8/15 session. **Recorded as a dated ADDENDUM to the frozen card — its cells now move capital, not just confidence.**
- **V5 3→4 → decide at the ~8/3 window close.** No early bump.
- **Paper sleeve → APPROVED** (Phase 1, no capital) · **CRL-22 v3 → delegated**, executed · **V2 trigger re-spec → approved**, executed (v2.6.3).

---

## WHAT HAPPENED (7 passes)
1. **Catch-up:** CRL-26 ✅ CONFIRMED (gas crossed $4.00); CRL-08 re-armed 28→45 (Brent settled $100.19); **CRL-24 ❌ MISSED**, the 4-name cluster went **0-for-4** → six confidence cuts; 9 inbox drained; **46 BOARD signals** dispositioned.
2. **HHDC card FROZEN 22d early** — writing it caught that the downgrade was armed against an instrument (HHDC) that publishes no subprime series.
3. **CRL-22 → v3:** the culling *causes* the margin improvement, so every margin-deterioration spec was anti-correlated with its own mechanism.
4. **POP refreshed → demoted;** found a parent↔sub-agent **monotonicity bug** (P06 >5% @50 vs CRL-15 >6.5% @65).
5. **Fitch ATR refreshed** → V2's trigger was **seasonally mis-specified** (fires every spring on tax refunds) → re-specced, **v2.6.3**.
6. **Brier audit run** — 0.300/0.340, **NEGATIVE skill**, +28.9pp overconfident. One surgical cut (CRL-07 85→40).
7. **Tooling:** `consistency_check.py` now runs **A/B/D/E/F/G** at boot; `brier_audit.py` built.

---

## NEXT SESSION SHOULD

### IMMEDIATE
1. **Execute the FOMC leg** (PRIORITY-1); grade the language priors.
2. **Mark the paper sleeve** (`book/PAPER_SLEEVE.tsv`) — Check F/F5 flags it if skipped. **Never delete a losing row.**

### OWED — read but NOT integrated (KB-362 — do not mistake "read" for "handled")
3. **LABOR:** *"if your income core uses AHE +3.5% as wage growth it is OVERSTATING what a continuing worker earns"* — composition-contaminated by the ~720K labor-force exit. **STATUS currently carries AHE as a mild cost-squeeze COUNTER-signal; if LABOR is right, that counter is weaker than logged and the real-wage K-shape may understate the squeeze.** Clean test: **ECI Q2, Fri 7/31** (composition-controlled by construction).
4. **DEWEY (ACTION, CRL-05):** C2 score-cascade — *does* student-loan delinquency **cause** the CC 90+ breach? `AGENTS/DEWEY/output/2026-07-24_c2-score-cascade-cc-breach-attribution.md`. **Read before 8/15** — if causal rather than co-moving, the card's discriminator cells may need a causal caveat.

### DATED
5. **~8/3** V5 window closes · **8/3–8/17** diesel natural experiment, peak ~8/10 (grade **timing**, not magnitude — contaminated by the insurance step) · **~8/10 Fitch ATR** (the actual V2 resolver; V2 still rests on a Jan print) · **8/12 July CPI** (pre-registered soft) · **~8/15 NY Fed Q2 HHDC — the most load-bearing print on the board** · **8/21** Iran waiver + expiry cluster · **9/11 August CPI** (the real oil test).

### AWAITING
6. **REGINALD** on the SYF/COF/ALLY surface split — blocks the purest CRL-27 expression. Silence past their next session reads as agree.
7. **TERRY** on whether the sleeve's `pred_id` gate reproduces PAT-028's zero-volume problem.

### BACKLOG
8. Re-run Brier at N≈20 · add an ex-ante confidence column (only 5/10 recoverable) · re-validate Check G tiers at N≈20 · Check C declined (reasoning in spec) · container-freight AEOLUS reconcile (KB-344).

---

## ⚠️ RED HAS PRE-REGISTERED A RATIONALIZATION TEST AGAINST ME — accepted
> *"The test isn't today's decision, it's whether the arming is a **commitment** or a **queue**."*

If ~8/15 comes in benign and I nominate **yet another instrument** rather than moving, RED files a scored rationalization finding. **Accepted — and I re-pointed their grading condition at instruments that actually exist** (Fitch ATR ~8/10 → V2; CC 90+ on the HHDC → CRL-05/V1), because theirs named V2-on-HHDC, which cannot fire.

## CALIBRATION — the load-bearing lesson
I hit *"established trend reaches a level"*; I miss *"series turns or crosses a threshold by a date."* **No conjunctions without pricing them as conjunctions.** Threshold calls on revision-prone series (JOLTS/NFP/hires) → ≤40% or don't register. **Check G now gates these at registration** (tier-1 HARD on new rows) — because reading the taxonomy at boot demonstrably did not stop CRL-24.

## WORKBOOK HEALTH
| File | Size | Note |
|---|---|---|
| STATUS.md | **250** | at cap; 16 superseded rows retired this session |
| KB.tsv | **362** | +18 (345–362) |
| PREDICTIONS.tsv | 28 | 16 OPEN · CRL-27 new · CRL-24 MISSED / CRL-26 CONFIRMED |
| CATALYSTS.tsv | 20 | 0 past-due; CALENDAR synced; dates corrected |
| BOARD_LOG.tsv | 568 | 0 backlog |
| PAPER_SLEEVE.tsv | 9 | 5 legs OPEN, marked 7/24, net −$13.37 (entry slippage only) |
| MEMORY.md | 69 | under the 100 cap |

## URGENT
- **FOMC Tuesday.** Leg written — execute, don't rebuild.
- **~8/15 HHDC decides V2/CRL-05, CRL-21's capital commitment, AND whether RED scores me for rationalization.** Card is frozen: **do not edit it, only append dated addenda.**
