# HOMER — THESIS + THESIS-LEVEL KILL RAIL

**Kill rail re-derived: 2026-09-29** · Authored 2026-09-29 under Will's 8/23 build authorization (L3 build 3b, DAEDALUS PR6 ask 2, due 9/30) · **Criteria FROZEN from this commit** · Next formal grade: **2026-11-20** · Fleet registration: **`GATE-HOMER-THESIS-KILL`** in `PROME/GATES.tsv` (PROME, 2026-09-29). This file is the canonical letter; the gate row is a summary and pointer. **If any leg reaches its kill count before 11/20, re-date by packet to PROME.**

> ⚠️ **What this file is NOT:** the per-prediction machinery in `PREDICTIONS.tsv` (HOM-01, HOM-02, early-kill arms). That covers **two metrics**. This rail covers the **transmission chain**. A HOM-02 resolution is evidence for leg A1 below, not a thesis grade.
> **Convergence handle (L3 build 3c): BUILT 2026-10-15, §8** (6 days past its 10/09 due date). Between-grade clarifications from DAEDALUS's 10/08 sweeps: **§7**. No kill level moved.

---

## 1. The thesis (one paragraph)

**U.S. housing credit stress has moved from ACCUMULATION to CONVERSION.** Residential foreclosures and multifamily loans are turning into completed foreclosures, REO and realized losses. Elevated mortgage rates and builder distress are keeping the stress from curing on its own. **That makes housing an active transmission vector:** to banks (Path C → REGINALD, the lead path of CARL's thesis of record), to households (→ CARL) and to wealth (→ HENRY). **Current state: 🔴.**

**Two CORE legs carry the thesis; three AMPLIFIER legs set its intensity.** Amplifiers alone can never kill it.

| Leg | Class | What it claims |
|---|---|---|
| **C1 Residential conversion** | CORE | Foreclosures are completing and the foreclosure stock is growing, not just delinquencies |
| **C2 Multifamily realization** | CORE, two channels | MF loans are going bad in the CMBS book and the GSE book, with realized marks behind them |
| **A1 FHA-bottom inflow** | AMPLIFIER | The weakest borrowers keep feeding the pipeline and are not curing |
| **A2 Rate amplifier** | AMPLIFIER | Mortgage rates are high enough to block refinance and sale exits |
| **A3 Builder distress** | AMPLIFIER | Builders are discounting and losing confidence, which feeds prices and construction jobs (→ LABOR) |

---

## 2. The five elements per leg (my reading of blueprint `market-agent.md` §4)

The DAEDALUS card (`HOMER_CARD.md` §4) says "five elements per leg" without listing them. **I read them as:** ① channel-kill vs thesis-kill, with a migration path · ② standing rule / current state / FIRED triad with a fired count · ③ cleanest flip each way at the next release · ④ counted persistence ("sustained" = N consecutive prints; nothing already breached at write time) · ⑤ a positively measured instrument with its healthy reading, plus a satisfiability check on every AND. If DAEDALUS meant a different five, amend between grades.

"N consecutive prints" counts the **instrument's own releases**, not HOMER sessions.

---

## 3. The rail — kill criteria per leg (FROZEN)

### C1 — Residential conversion (CORE)
- **KILL:** ICE First Look **FC sales YoY ≤ 0%** AND **FC pre-sale inventory YoY ≤ 0%**, on **3 consecutive monthly prints**.
- **Why this pair, not inventory alone:** flat inventory is ambiguous. It can mean conversion stopped, or that completions sped up (conversion *accelerating*). Only sales and stock both not growing means conversion has stopped.
- **Satisfiability (the AND):** ✅ **Verified joint window.** ICE March-2025 First Look (pub 2025-04-24): foreclosure inventory and sales "rose annually for the first time in nearly two years". ICE August-2024 (pub 2024-09-25): FC sales **−18.1% YoY**. So both were ≤ 0% YoY together for ~22 months, roughly Q2-2023 → Feb-2025.
- **Instrument health:** ICE First Look prints signed YoY for both, monthly (~23rd–28th). **Dead if no First Look for > 45 days**; a dead instrument grades UNGRADED, never NOT-FIRED.
- **Channel vs thesis:** the **HUD ML 2026-08** channel (FHA foreclosure-initiation accelerant, in force 9/21) is a *channel*. If FHA FC starts show no lift by the **December First Look**, that retires the accelerant claim only, not C1.
- **Cleanest flip at the next print (Sept First Look, ~10/23–28):** *against* = FC inventory falls MoM (Aug was +2K, the smallest build in 9 months) **with** FC sales also down MoM. *For* = FC sales YoY ≥ +20% (Aug +11.7%).

### C2 — Multifamily realization (CORE, two channels)
- **CMBS channel KILL:** Trepp CMBS MF delinquency **< 6.00%** on **3 consecutive monthly prints**. Base: ✅ prints below 6% exist (ledger: Mar-24 1.84%, May-24 1.70%; Jul-25 6.15%). No 2026 print is below 6.85%.
- **GSE channel KILL:** the **higher** of Freddie MF DQ and Fannie MF serious DQ **< 0.50%** on **3 consecutive monthly prints**. That means both books are below 0.50%. Base: ⚠️ **INFERRED, not held month by month.** Freddie was < 0.50% Feb–May 2026 (0.42–0.47); Fannie was 0.24% in Dec-2022 (secondary, via Fannie's release coverage). A joint window is plausible in 2022–23 but not in my ledger.
- **LEG KILL = both channels killed at the same grade.** **One channel killed = PARTIAL:** the leg survives on the other. Migration: GSE killed ⇒ C2 rides on CMBS plus realized marks (Arbor REO, BANC HFS, S2). CMBS killed ⇒ C2 rides on the GSE books.
- ⚠️ **Standing A1 caveat (from CLAUDE.md):** Fannie's headline is modification-suppressible. **A GSE channel kill that rests on a Fannie drop must be paired with the same quarter's Fannie MF credit provision.** If the provision rose, grade the GSE channel HALF, not killed.
- **Instrument health:** Trepp monthly (~1st); Fannie/Freddie monthly (~24th–30th). Dead if > 45 days without a print.
- **Cleanest flip at the next print (Trepp Sept, ~10/01):** *for* = CMBS MF **> 7.71%** (a new high above Apr-26). *Against* = CMBS MF **< 6.85%** (below the 2026 floor).

### A1 — FHA-bottom inflow (AMPLIFIER)
- **KILL:** MBA NDS **FHA SA total DQ falls QoQ in 2 consecutive quarters** AND ICE Mortgage Monitor **serious-DQ cure rate YoY better than −15%** (above the Cure Rates Yellow line) on the latest issue at that grade.
- **Satisfiability:** ⚠️ **general knowledge, not in my ledger:** the 2021–22 post-forbearance cure period had falling FHA DQ with normal cure rates. **Owed:** pull an MBA NDS FHA SA history to confirm.
- **Instrument health:** MBA NDS quarterly (~mid-Feb/May/Aug/Nov; primary is 403-gated, CalculatedRisk mirrors same day); ICE Mortgage Monitor monthly (~9th–13th).
- **Channel vs thesis:** ⚠️ the Oct-2025 FHA process break distorts FHA **YoY**; this kill uses **QoQ SA**, which is why.
- **Cleanest flip:** Q3 NDS (~mid-Nov). *For* = FHA SA ≥ 12.00% (also HOM-02's confirm). *Against* = a second QoQ decline (also HOM-02's second early-kill arm).

### A2 — Rate amplifier (AMPLIFIER)
- **KILL:** Freddie PMMS 30-yr **≤ 6.50%** (at or below the Orange line) on **4 consecutive weekly prints**.
- **Satisfiability:** ✅ **verified:** PMMS was ≤ 6.50% in **39 of the 53 weeks** to 9/24/2026, with a longest run of **34** (Freddie `PMMS_history.csv`, read 2026-09-29).
- **Instrument health:** weekly, Thursday 12:00 ET.
- **Cleanest flip:** the 10/01 print, pre-registered at `reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md` (HOLD ≥ 7.05 · SOFTEN 7.01–7.04 · LIFT ≤ 7.00). **A LIFT is not an A2 kill:** the kill needs ≤ 6.50% for four weeks.

### A3 — Builder distress (AMPLIFIER)
- **KILL:** NAHB/Wells Fargo HMI **≥ 40** on **3 consecutive monthly prints**.
- **Why not existing-home sales:** EHS has sat within ~100K of 4.0M for over a year (Jun 4.09 · Jul 4.06 · Aug 3.98M), so a kill near that line fires on revision noise.
- **Satisfiability:** ⚠️ **general knowledge, NAHB's table not read:** HMI was 46 · 46 · 47 · 42 in Nov-24 → Feb-25. 2026 so far: Jan 37 · Feb 36 · Mar 38 (search summaries) · Aug 35 · **Sep 32** (issuer). **Owed:** read NAHB's history table.
- **Instrument health:** monthly, mid-month.
- **Cleanest flip:** Oct HMI (~10/15–16). *For* = price cutters **> 45%** (RED; Sep 38%). *Against* = HMI ≥ 36 with price cutters falling.

---

## 4. Thesis-level decision rule (PRE-REGISTERED 2026-09-29, before any grade under it)

| Outcome at a formal grade | Consequence |
|---|---|
| **C1 AND C2 both KILLED** | **THESIS FALSIFIED.** 🔴 → 🟡 candidate. Same-day packet to PROME (for Will) and CARL (Path C is CARL's lead path) |
| **Exactly one core leg KILLED** | **PARTIAL.** Thesis survives on the other core leg. 🔴 → 🟠 candidate, routed to Will via PROME, naming the migration |
| **≥ 2 of 3 amplifiers KILLED, cores alive** | **Intensity note.** 🔴 holds, reported as "amplifiers stood down". Amplifiers never kill the thesis alone |
| **Anything else** | 🔴 holds; report each leg's fired counts |

- **Satisfiability of the thesis AND (both cores killed):** ⚠️ **plausible, partly inferred.** In 2024, ICE FC sales and inventory were down YoY (verified) and Trepp CMBS MF was ~1.7–1.8% (ledger). The GSE channel's joint < 0.50% is inferred (above). A historical state exists in which this rule would have fired, but it is not fully held month by month.
- **HALF counts:** a channel graded HALF (the Fannie provision rule) does not count as killed.
- **UNGRADED** (dead instrument) is **not** NOT-FIRED. It obliges an instrument note.
- ⛔ **No criterion may be reworded, split or merged at grading time.** A badly specified criterion is flagged and amended between grades, never during one.
- **State change is for Will to approve.** This rail proposes the 🔴 → 🟠/🟡 move; it does not make it.

**Grade cadence:** fired counts update mechanically at each print (docket rows already exist for every instrument). **Formal grade dates: 2026-11-20** (after MBA Q3 NDS, ICE October First Look, Trepp November), then **2027-02-20**. Earlier only if any leg reaches its kill count.

---

## 5. GRADE OF RECORD — 2026-09-29 (first ever)

⚠️ **Ordering caveat, recorded rather than hidden:** these criteria were written today with the data in hand. Guardrails used: no kill level is already breached, and every level was base-rated against a window before 2026 where one exists. From the next grade, the criteria are frozen and pre-date the data.

| Leg | Standing rule (kill) | Current state @ level (as of) | Fired count | Verdict |
|---|---|---|---|---|
| **C1** | FC sales YoY ≤ 0% AND FC inventory YoY ≤ 0%, 3 prints | Sales **+11.7%**, inventory **+41%** (Aug, ICE 9/28) | **0 / 3** | 🔴 **NOT FIRED** |
| **C2 · CMBS** | Trepp MF DQ < 6.00%, 3 prints | **7.69%** (Aug, Trepp 9/1) | **0 / 3** | NOT FIRED |
| **C2 · GSE** | max(Freddie, Fannie) < 0.50%, 3 prints | Freddie **0.64%**, Fannie **0.57%** (Aug) | **0 / 3** | NOT FIRED |
| **A1** | FHA SA QoQ ↓ ×2 AND cure YoY > −15% | FHA **11.79%, −9bps QoQ** (Q2) = **1 of 2**; cure **−28% YoY** (Jul) | **½ of the first conjunct** | NOT FIRED |
| **A2** | PMMS ≤ 6.50%, 4 weeks | **7.03%** (9/24) | **0 / 4** | NOT FIRED |
| **A3** | HMI ≥ 40, 3 prints | **32** (Sep) | **0 / 3** | NOT FIRED |

**LITERAL FIRED-COUNT: 0 of 5 legs.** ⇒ **🔴 holds.**

**The honest read:** no leg is close to its kill. The softest spots are **C1's inventory build** (+2K in August, the smallest in 9 months) and **A1's first conjunct** (one QoQ FHA decline already in). The GSE channel moved in both directions in August (Freddie up, Fannie down), so it is not a one-way read.

---

## 6. Defect register (append-only; ships with every grade)

| # | Date | Defect | Owed fix |
|---|---|---|---|
| D1 | 2026-09-29 | "Five elements" is my reading of §4; the card does not enumerate them | DAEDALUS to confirm or correct |
| D2 | 2026-09-29 | C2 GSE-channel joint base window INFERRED (Fannie Dec-22 via secondary) | Pull Fannie + Freddie MF DQ 2022–24 at issuer |
| D3 | 2026-09-29 | A1 base window is general knowledge | MBA NDS FHA SA history |
| D4 | 2026-09-29 | A3 base window is general knowledge (NAHB table not read) | Read NAHB HMI history |
| D5 | 2026-09-29 | First grade written with data in hand (ordering) | None; frozen from here |
| D6 | 2026-09-29 | No REGINALD-side (bank-loss) confirm criterion. The upgrade to "transmission confirmed" is REGINALD's call, so this rail only kills | By design; revisit if REGINALD asks |
| D7 | 2026-10-15 | **D1 CLOSED.** DAEDALUS confirmed 2026-10-01 that my five elements match `market-agent.md` §4 one for one (packet `inbox/processed/2026-10-01_from-DAEDALUS_D1-five-elements-confirmed.md`) | None |
| D8 | 2026-10-15 | DAEDALUS Gate-Basis #2 (10/08): resolving vintage, UNGRADED-month handling, the provision comparison period and C1's count-vs-rate were unstated. Clarified in §7 without moving any level | GATES summary cell is PROME's: packeted 2026-10-15 |

---

## 7. Between-grade clarifications — 2026-10-15 (DAEDALUS Gate-Basis #2 + stranger read; no level moved)

These say what the frozen letter already meant. None moves a kill level, a count or a date. They were written before the next grade and before the September prints for C1 and the GSE books.

| # | Question | Answer |
|---|---|---|
| **V1** | **Which vintage resolves each core print?** | The value **as first published in that month's release**, read at the issuer: ICE First Look (that month's release) · Trepp (that month's headline MF DQ, 2dp) · Freddie Monthly Volume Summary · Fannie Monthly Summary. Later revisions (Fannie revised July 0.61→0.62% in the August release) are recorded beside the first print and **never re-grade a count already taken.** |
| **V2** | **Does an UNGRADED month break or pause a 3-print run?** | **It PAUSES the run.** The count neither advances nor resets, and the next graded print continues it. I chose pause because "break" would make my own thesis harder to kill, which is the self-serving direction. ⚠️ A missed release by the *instrument* is UNGRADED. A release I failed to fetch is a HOMER defect, logged as one, and also pauses. |
| **V3** | **"The provision rose" (C2 Fannie pairing) compared with what?** | **The same quarter's Fannie MF credit-loss provision vs the immediately prior quarter (QoQ)**, both as reported in the 10-Q/10-K for the graded quarter. Example of record: Q2 $259M vs Q1 $174M = rose. |
| **V4** | **C1 "FC pre-sale inventory YoY": the COUNT or the RATE?** | **The COUNT** (Aug: 298K, +41% YoY), as in the 9/29 grade of record. The pre-sale *rate* (0.54% in August) is an observation and never grades C1. The C2 GSE measure is Fannie MF **serious** DQ; the GATES summary dropped both qualifiers. |
| **V5** | **What can 11/20 return?** | **On the core legs, NOT FIRED or UNGRADED only.** Every core kill needs 3 consecutive prints and every core count was 0 at 9/29. At most 2 new monthly prints per core instrument land before 11/20 (Trepp: Sept + Oct · First Look: Sept, maybe Oct · GSE: Sept, maybe Oct), so no core leg can reach its count. ⇒ **11/20 cannot return FALSIFIED or PARTIAL.** Earliest possible core kill: **Trepp's November-data print (published ~early Dec)**; §4's "Trepp November" is the release published in November (October data). A1 *can* fire at 11/20, on the Q3 NDS plus the ICE cure rate. |

---

## 8. Convergence handle (L3 build 3c) — BUILT 2026-10-15

The handle has two parts: **(i) the universal 5-point handle** that blueprint `market-agent.md` §2 requires (score, independence, transparent composite), and **(ii) the join** into CARL's convergence matrix. **CARL scores its vectors; HOMER feeds.**

### 8a. The 5-point handle (blueprint `market-agent.md` §2 interface)

⚠️ **Scores are the ones PROPOSED 2026-09-29** (packet to CARL, commit `64d35bf5f`), which CARL told me to build as proposed (10/01). **Not re-scored on 10/15:** the recovery session integrated no print newer than 10/02. Local state is the newest value I hold, dated. The kill rail (§3) governs; a score is a triage projection that routes attention back to it. Re-score at each formal grade (next 2026-11-20).

| # | Vector (HOMER leg) | Score (1–5) | Local state (as of) | Independence | Key signal | Upgrade trigger (→ 5) |
|---|---|---|---|---|---|---|
| C1 | Residential conversion (CORE) | **4** | ICE 90+/FC **872K** (Aug; 22K past Orange, RED >1M); FC pre-sale inventory **298K, +41% YoY** but +2K MoM; FC starts **+29% YoY**; ATTOM Aug REO **+42% YoY** | **Root R1** (residential FC pipeline) | ICE First Look, monthly | §3 C1 "for" flip: FC sales YoY **≥ +20%** (Aug +11.7%) |
| C2 | Multifamily realization (CORE) | **4** | Freddie MF **0.64%** (Aug, 14bps above Red); Fannie MF serious **0.57%** (Aug, mod-suppressible); Trepp CMBS MF **7.69%** (Aug); realized marks (BANC HFS, Arbor REO) | **Root R2** (MF credit) | Trepp MF DQ + GSE monthlies | §3 C2 "for" flip: Trepp CMBS MF **> 7.71%** (a new 2026 high) |
| A1 | FHA-bottom inflow (AMP) | **4** | FHA SA DQ **11.79%** (Q2, 21bps below Red); ICE cure rate **−28% YoY**, FHA **−39%** (Jul) | **Co-rooted with C1 (R1): count once** | MBA NDS (quarterly) + ICE Mortgage Monitor | §3 A1 "for" flip: FHA SA **≥ 12.00%** at the Q3 NDS |
| A2 | Rate amplifier (AMP) | **4** | PMMS **7.28%** [wk 10/01], RED, HOLD state fired; spread ~199bps | **Co-rooted with CARL's V12** (rates; BROCK/HENRY own direction): count once | Freddie PMMS, weekly | None defined: PMMS has no uncrossed rung above RED. Set one at the 11/20 grade or leave the score capped at 4 |
| A3 | Builder distress (AMP) | **3** | NAHB HMI **32** (Sep); price cutters **38%** (Orange); LEN/KBH margins at trough, orders −9% / −12% | **Root R3** (new-home supply → LABOR) | NAHB HMI, monthly; builder 8-Ks | §3 A3 "for" flip: price cutters **> 45%** (RED) |

**Composite (transparent, no weighting): 4 + 4 + 4 + 4 + 3 = 19/25 across 5 legs.** Independent roots: **3** (R1, R2, R3). A1 folds into R1; A2 is an input to CARL's V12, not a new root.

### 8b. The join into CARL's matrix

How this rail's legs map into CARL's convergence matrix. **CARL scores; HOMER feeds.** CARL's answers: `inbox/processed/2026-10-01_from-CARL_3c-handle-confirmed-V3-rescope-at-10-05.md`. CARL's scope review, held 10/12 rather than 10/05: `AGENTS/CARL/domain/sources/2026-10-12_scope-review.md`.

| HOMER leg | CARL vector | State of the link | Rule |
|---|---|---|---|
| **C1 + A1** (one root, R1) | **V10** (foreclosure acceleration) | ✅ **CONFIRMED (a)** | Count C1 and A1 **once**, as R1. The K-shape reading of A1 stays CARL's (V8) |
| **A2** | **V12** input | ✅ **CONFIRMED (a)** | Counted once |
| **C2** (both MF books) | **V3** (Fannie MF DQ) | ✅ **RESOLVED 10/12: V3 is NOT re-scoped.** It stays a Fannie-only vector. C2 reaches CARL as **peer evidence only**. | ⛔ **Never map C2's state onto V3's score.** V3 reads the calmer book: Aug Fannie 0.57% vs Freddie 0.64%. A Freddie move does not reach V3 unless CARL re-scopes it, and that would be a thesis change routed to Will |
| **A3** (builders) | **R3**, unscored | 🟡 **CANDIDATE (c)** | CRL-23 (DHI/PHM Q1 FY27 gross margin) is the resolver on CARL's side; no new vector |
| C1 (REO, FL) | V7 / V10 citations | CARL refreshes its own cells | CARL's 10/01 answer names ATTOM H1 REO 27,983 (+33% YoY) and Aug REO +42% YoY as the citations it will carry; its 10/12 review cites Aug REO +42% for V10. **Florida statewide figures come from CORAL, never from HOMER** |

**Double-count guard:** one HOMER fact feeds one CARL vector. A fact that bears on two vectors (A1 → V10 and V8) is counted at V10; V8 is CARL's own reading of it.

---

## 9. Fired-count ledger between grades (mechanical, per §4 "fired counts update at each print"; no criterion touched)

### 2026-10-15 — L722 catch-up (first prints integrated since 10/02)

| Leg | Print(s) integrated (first-published vintage, V1) | Fired count | Verdict | Cleanest-flip check (§3) |
|---|---|---|---|---|
| **C1** | none — ICE September First Look not out (URL 404 10/15 11:16 ET; ~10/22–28) | **0 / 3** | NOT FIRED | pending |
| **C2 · CMBS** | Trepp **8.04% Sep** (+35bp; pub 10/02, PDF Table 2) | **0 / 3** | NOT FIRED | ★ **"for" flip MET: > 7.71%, a new 2026 high** |
| **C2 · GSE** | none — Sept Fannie/Freddie due ~10/23–30 | **0 / 3** | NOT FIRED | pending |
| **A1** | ICE Mortgage Monitor Oct (Aug data): all-loans cure **YoY % NOT PRINTED** (level 7.8%; FHA −37% YoY). MBA Q3 NDS ~mid-Nov | **½ of the first conjunct** (unchanged) | NOT FIRED | second conjunct (cure YoY better than −15%) not met on any reading — the chart-derived −25 to −29% is INFERRED and not used to grade |
| **A2** | PMMS **7.40% [10/08]** · **7.40% [10/15]** (unchanged) | **0 / 4** | NOT FIRED | 90bps above the kill line (≤ 6.50%) |
| **A3** | none — NAHB October HMI scheduled Mon 10/19 (archived NAHB schedule) | **0 / 3** | NOT FIRED | pending (Sep HMI 32, cutters 38%) |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** §7 V5 unchanged: 11/20 cannot return FALSIFIED or PARTIAL on the core legs.

**§8a handle:** C2's upgrade trigger (→ 5) is **MET** by the Trepp 8.04% print. **Not re-scored today** — §8a re-scores at the formal grade (2026-11-20); the trigger is recorded here so 11/20 reads it. Composite stays **19/25** until then.

**Instrument note (C2 neighbourhood, not a C2 criterion):** the Trepp **MF maturity-adjusted** rate is RETIRED (dated kill EXECUTED 2026-10-15, absent at source Jul–Sep); C2 never graded on it. Its successor for the pre-delinquency channel is MF special servicing (8.54% Sep, +17bp).

**HOMER defect (V2):** the September Trepp print and PMMS 10/08 were integrated ~2 weeks / 1 week late (the 10/14–15 crash). Under V2 a print HOMER failed to fetch PAUSES a run; no run was in progress, so no count is affected.
