# HOMER — THESIS + THESIS-LEVEL KILL RAIL

**Kill rail re-derived: 2026-09-29** · Authored 2026-09-29 under Will's 8/23 build authorization (L3 build 3b, DAEDALUS PR6 ask 2, due 9/30) · **Criteria FROZEN from this commit** · Next formal grade: **2026-11-20** · Fleet registration: **`GATE-HOMER-THESIS-KILL`** in `PROME/GATES.tsv` (PROME, 2026-09-29). This file is the canonical letter; the gate row is a summary and pointer. **If any leg reaches its kill count before 11/20, re-date by packet to PROME.**

> ⚠️ **What this file is NOT:** the per-prediction machinery in `PREDICTIONS.tsv` (HOM-01, HOM-02, early-kill arms). That covers **two metrics**. This rail covers the **transmission chain**. A HOM-02 resolution is evidence for leg A1 below, not a thesis grade.
> **Not built here:** the convergence handle (L3 build 3c). Still OPEN on the docket.

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
