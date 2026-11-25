# HOMER — THESIS + THESIS-LEVEL KILL RAIL

**Kill rail re-derived: 2026-09-29** · Authored 2026-09-29 under Will's 8/23 build authorization (L3 build 3b, DAEDALUS PR6 ask 2, due 9/30) · **Criteria FROZEN from this commit** · **Formally graded 2026-11-20 (§10: 0 of 5 killed, 🔴 holds)** · Next formal grade: **2027-02-20** · Dated history → `archive/THESIS_history_2026-11-25.md` · Fleet registration: **`GATE-HOMER-THESIS-KILL`** in `PROME/GATES.tsv` (PROME, 2026-09-29). This file is the canonical letter; the gate row is a summary and pointer. **If any leg reaches its kill count before the next formal grade, re-date by packet to PROME.**

> ⚠️ **What this file is NOT:** the per-prediction machinery in `PREDICTIONS.tsv` (HOM-01, HOM-02, early-kill arms). That covers **two metrics**. This rail covers the **transmission chain**. A HOM-02 resolution is evidence for leg A1 below, not a thesis grade.
> **Convergence handle (L3 build 3c): BUILT 2026-10-15, §8** (6 days past its 10/09 due date). Between-grade clarifications from DAEDALUS's 10/08 sweeps: **§7**. No kill level moved.

---

## 1. The thesis (one paragraph)

**U.S. housing credit stress is BUILDING AND CONVERTING at once.** The stock of foreclosures is still growing and more of them are being completed, though year-over-year growth in both is below earlier readings. Multifamily loans are producing realized losses. High mortgage rates, few cures and a freeze in home sales are narrowing the ways out, and builders are discounting into it. **Transmission differs by channel. Happening now:** apartment lenders and apartment bonds (→ REGINALD, CREED), FHA and mortgage-insured borrowers (→ CARL), builders (→ LABOR). **Early, not settled:** bank-held apartment loans and nonbank servicers (→ REGINALD), residential construction jobs (→ LABOR). **Not showing yet:** a national nominal house-price decline is not showing in the latest indexes; regional and real-price effects remain HENRY's assessment. HOMER holds no evidence of broad bank losses on home mortgages; that is not proof they are absent and is REGINALD's call. **Current state: 🔴.**

*Adopted 2026-11-25 (Will 09:31 ET); evidence by channel, dates and the old wording: §12. The channel labels are dated observations, not kill criteria.*

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
- **KILL (first conjunct RESTATED 2026-11-24 under WQ-725; old wording in §11):** MBA NDS **FHA seriously delinquent rate (90 or more days past due, or in foreclosure; not seasonally adjusted) falls QoQ in 2 consecutive quarters** AND ICE Mortgage Monitor **serious-DQ cure rate YoY better than −15%** (above the Cure Rates Yellow line) on the latest issue at that grade.
- **First-conjunct source and vintage:** the QoQ change in basis points for FHA loans as MBA states it in that quarter's NDS release (CalculatedRisk's verbatim copy while mba.org refuses this box, labelled SECONDARY), **first print** (§7 V1). "Unchanged" is not a fall and resets the run. A release that states no FHA change is UNGRADED and pauses the run (V2).
- **Satisfiability:** ⚠️ **general knowledge, not in my ledger:** the 2021–22 post-forbearance cure period had falling FHA DQ with normal cure rates. **Owed:** pull an MBA NDS FHA SA history to confirm.
- **Instrument health:** MBA NDS quarterly (~mid-Feb/May/Aug/Nov; primary is 403-gated, CalculatedRisk mirrors same day); ICE Mortgage Monitor monthly (~9th–13th).
- **Channel vs thesis:** ⚠️ the Oct-2025 FHA process break distorts FHA **YoY**; this kill uses **QoQ**, which is why (restated 2026-11-24: serious DQ is not seasonally adjusted, see §11 D15).
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

## 5. GRADE OF RECORD — 2026-09-29 (first ever): ARCHIVED

0 of 5 legs, 🔴 held. ⚠️ Those criteria were written with the data in hand (D5); the grade in force is §10. Full text: `archive/THESIS_history_2026-11-25.md` block B.

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
| D9 | 2026-11-05 | **D2 CLOSED at quarter-end grain.** Issuer 10-Qs and 10-Ks: both books below 0.50% at 12/23, 3/24, 6/24 (`MULTIFAMILY.tsv` 2026-11-05 history row). Fannie Dec-22 0.24% verified | Month-by-month joint run and Freddie before 6/23 remain unshown; not needed to show satisfiability |
| D10 | 2026-11-05 | **D4 CLOSED.** NAHB Table 2: last run of three at or above 40 was Sep to Nov 2024; last reading 40 in April 2025 (`BUILDER.tsv` 2026-11-05 history row) | None |
| D11 | 2026-11-05 | **§4 grade-date input defect.** §4 says the 11/20 grade comes after the ICE October First Look, but ICE publishes about 11/23–30 (September came 10/27). Found by HOMER, no level or criterion affected | Grade 11/20 on the newest print then held, say so, and update C1 mechanically at the October print. D3 stays open: MBA history is 403 to this box |
| D12 | 2026-11-16 | **A1 second conjunct has no reading at 11/20.** The kill needs the ICE Mortgage Monitor all-loans cure-rate YoY "on the latest issue at that grade"; the October and November editions did not print it (STATUS, HB-08 UNGRADED). The last printed value was −28% (July), worse than the −15% line. FHA-only −46% does not grade it. Found by HOMER in pre-grade prep; no level or criterion moved | At 11/20 grade A1's second conjunct UNGRADED (§4: not NOT-FIRED) and say so; A1 cannot read FIRED on the first conjunct alone. Whether to name a successor statistic is a between-grade amendment, raised to PROME, never made at grading |

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

⚠️ **Scores below are the 2026-11-20 re-score (current).** The scores proposed 2026-09-29 (composite 19/25): `archive/THESIS_history_2026-11-25.md` block C. Local state for each leg is in §10 and `STATUS.md`. The kill rail (§3) governs; a score is a triage projection. Re-score at each formal grade (next 2027-02-20).

| # | Vector (HOMER leg) | Score (1–5) | Why (2026-11-20) | Independence | Key signal | Upgrade trigger (→ 5) |
|---|---|---|---|---|---|---|
| C1 | Residential conversion (CORE) | **4** | Stock and conversion still rising (FC inventory +37%, FC sales +14.5% YoY, FHA FC rate 9-year high); "for" flip (sales ≥ +20%) not met. ⚠️ "new FC starts −3%" was also given as a reason and is a one-month base effect (D17) | **Root R1** (residential FC pipeline) | ICE First Look, monthly | §3 C1 "for" flip: FC sales YoY **≥ +20%** |
| C2 | Multifamily realization (CORE) | **5** | Trigger MET (Trepp 8.04% Sept, 8.09% Oct > 7.71%); MF special servicing 9.22%; Fannie provision +72%. ⚠️ Cove at Tiburon may revert | **Root R2** (MF credit) | Trepp MF DQ + GSE monthlies | Trepp CMBS MF **> 7.71%** (met) |
| A1 | FHA-bottom inflow (AMP) | **3** | FHA headline DQ fell twice, ICE FHA new defaults −14% YoY (Sept); non-curing persists (FHA cures −46% YoY) | **Co-rooted with C1 (R1): count once** | MBA NDS (quarterly) + ICE Mortgage Monitor | §3 A1 "for" flip: FHA SA **≥ 12.00%** |
| A2 | Rate amplifier (AMP) | **4** | PMMS 7.28%, RED; capped at 4 | **Co-rooted with CARL's V12** (rates; BROCK/HENRY own direction): count once | Freddie PMMS, weekly | None defined; score capped at 4 |
| A3 | Builder distress (AMP) | **5** | Trigger MET: price cutters 46%; HMI 25, traffic 16, incentives 68% | **Root R3** (new-home supply → LABOR) | NAHB HMI, monthly; builder 8-Ks | Price cutters **> 45%** (met) |

**Composite (no weighting): 4 + 5 + 3 + 4 + 5 = 21 / 25.** Independent roots: **3** (R1, R2, R3). A1 folds into R1; A2 is an input to CARL's V12, not a new root.

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

Entries 2026-10-15 to 2026-11-16 (0 of 5 legs at every entry): `archive/THESIS_history_2026-11-25.md` block D. New entries go here. Counts since the 2026-11-20 grade:

### 2026-11-25 — prints since the 11/20 grade (mechanical update only)

| Leg | First print integrated | Fired count |
|---|---|---|
| **C1** | none: ICE October First Look 404 at 2026-11-25 09:35 ET | **0 / 3** |
| **C2 · CMBS** | none (Trepp November ~12/01–05) | **0 / 3** |
| **C2 · GSE** | Freddie **0.62%**, Fannie **0.65%** October (issuers) ⇒ max 0.65% ≥ 0.50% | **0 / 3** |
| **A1** | no new MBA print. First conjunct on the §11 wording: **0 of 2**. Cure YoY not printed by ICE | **UNGRADED stands** (11/20; D12). Open question to PROME 2026-11-25: how the letter reads at 2027-02-20 with the first half known and the cure half unread |
| **A2** | 7.28% [11/19] is the newest; next print due 2026-11-25 12:00 ET | **0 / 4** |
| **A3** | none (December HMI ~12/15–17) | **0 / 3** |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.**

---

## 10. FORMAL GRADE — 2026-11-20 (GATE-HOMER-THESIS-KILL; the first grade under criteria frozen before the data)

**Read 2026-11-20, 11:48–11:54 ET** (system clock, `date` at write; PROME prome-77 task letter written 11:48 ET; launched late, so "11/20" here means today, read in the late morning). Inputs: the newest first-published print held at the grade (V1). No criterion was reworded, split or merged (§4). WQ-700 (PROME, C3, 2026-11-16): A1 graded exactly as D12 states.

| Leg | Standing rule (kill) | Current state @ level (as of, source) | Fired count | Verdict |
|---|---|---|---|---|
| **C1** | ICE First Look FC sales YoY ≤ 0% AND FC inventory YoY ≤ 0%, 3 prints | FC sales 8.2K **+14.5% YoY**; FC inventory **303K +37% YoY** (September First Look, Business Wire 10/27). October First Look not out (due ~11/23–30, D11): graded on September, as stated | **0 / 3** | **NOT FIRED** |
| **C2 · CMBS** | Trepp MF DQ < 6.00%, 3 prints | **8.09%** (October, Trepp issuer PDF, read 11/05); November data ~12/01–05 | **0 / 3** | **NOT FIRED** |
| **C2 · GSE** | max(Freddie, Fannie serious) < 0.50%, 3 prints | Freddie **0.58%** (Sept MVS) · Fannie **0.62%** (9/30, Q3 release) ⇒ max 0.62%; Fannie MF provision **$446M vs $259M** QoQ (rose, V3). October monthlies not out | **0 / 3** | **NOT FIRED** |
| **A1** | MBA NDS FHA SA total DQ falls QoQ in 2 consecutive quarters AND ICE all-loans serious-DQ cure YoY better than −15% on the latest issue | **First conjunct MET:** Q2 11.79% (−9bps) and **Q3 11.74% (−5bps)** (MBA NDS released 11/20, quoted verbatim on CalculatedRisk; SECONDARY mirror, mba.org 403). **Second conjunct: NO READING** — ICE did not print the all-loans cure YoY in the October or November editions; last printed −28% (July), worse than −15% | first conjunct **2 of 2**; second **UNGRADED** | **NOT KILLED — UNGRADED** (§4: not NOT-FIRED; D12) |
| **A2** | PMMS ≤ 6.50%, 4 weeks | **7.21% [11/25]** (−7bp; Freddie CSV, issuer) | **0 / 4** | **NOT FIRED** — 71bp above the line |
| **A3** | HMI ≥ 40, 3 prints | **HMI 25** November (NAHB release 11/17, issuer), lowest since April 2012 | **0 / 3** | **NOT FIRED** — 15 points below |

**LITERAL RESULT: 0 of 5 legs KILLED** (4 NOT FIRED, 1 UNGRADED). §4 row "anything else" ⇒ **🔴 holds.** No colour candidate exists, so nothing goes to Will; the same-day CARL packet is owed only on FALSIFIED or PARTIAL (V5 held: neither was reachable). CARL receives this grade through `NEXUS_BRIEF.md`.

**Frozen cleanest-flip checks (§3), recorded, not graded:** C2 "for" (CMBS > 7.71%) MET again at 8.09% (⚠️ the $210M Cove at Tiburon loan may revert, PREREG §5). A3 "for" (price cutters > 45%) **MET: 46%** (HOM-04 HIT). A1 "for" (FHA SA ≥ 12.00%) NOT MET; A1 "against" (a second QoQ decline) **MET** — HOM-02 closed MISSED today. C1 had no new print.

**The honest read.** The only leg that moved toward its kill is **A1**, and the way it moved argues *for* the core, not against it. MBA's Q3 release that gave the second FHA decline also gave: FHA serious DQ **unchanged** QoQ (+197bps YoY), the **FHA foreclosure rate 1.89%, highest since Q1-2017**, all-loans foreclosure inventory **0.71% (+4bps QoQ, +21bps YoY)**, and loans 90+ or in foreclosure up a fifth straight quarter. MBA total DQ excludes loans in foreclosure, so FHA loans moving into foreclosure lower the A1 headline. That is conversion (C1's claim), with HUD ML 2026-08 in force since 9/21. Builders (A3) worsened sharply. Rates (A2) rose back. Both cores sit far from their counts.

**Leg nearest its count: A1** (one conjunct, which cannot currently be read). Even a full A1 kill changes nothing alone: amplifiers never kill (§4), and the intensity note needs 2 of 3, with A2 78bp and A3 15 points from theirs.

**Next formal grade: 2027-02-20 (unchanged).** No core leg can reach 3 prints by then on any plausible path (C1 needs both YoY legs to swing from +14.5% / +37% to ≤ 0 for three First Looks; C2 CMBS needs a fall of more than 2pp below 6.00% for three Trepp prints). **Re-date early, by packet to PROME, if:** an ICE Mortgage Monitor edition prints an all-loans cure YoY better than −15% while the two FHA declines stand (A1 reaches its count), or any core print lands on the kill side of its line.

### §8a handle re-scored at this grade: 19 → **21 / 25**

Current table: §8a. Change table as written 2026-11-20: `archive/THESIS_history_2026-11-25.md` block E.

### Defects found at this grade

| # | Date | Defect | Owed fix |
|---|---|---|---|
| D13 | 2026-11-20 | **A1's first conjunct is migration-sensitive.** MBA NDS total DQ excludes loans in foreclosure, so an *acceleration* of FHA loans into foreclosure (the thesis's own C1 mechanism, sped up by HUD ML 2026-08) lowers it. The conjunct fired today on exactly that release. The second conjunct (cure rate) guards A1 today, but it has no reading. Found by HOMER at grading; nothing moved at grading (§4) | **Between-grade amendment, drafted to PROME, not made:** restate A1's first conjunct on a migration-invariant measure (MBA FHA total DQ plus FHA foreclosure inventory, or FHA serious DQ). Will-gated as a change to a frozen leg. Pairs with D12 (successor cure statistic, WQ-700 kept as written) |
| D14 | 2026-11-20 | §7 V5 said "11/20 cannot return FALSIFIED or PARTIAL" — confirmed by this grade; the source tier for A1 is a SECONDARY mirror (CalculatedRisk quoting MBA verbatim; mba.org refuses this box) | MBA primary owed only if the 5bps decline is contested; the sign is MBA's own words |

Evidence: `reports/2026-11-20_thesis-formal-grade.md`; ledger rows dated 2026-11-20 (PIPELINE, BUILDER, RATES, PRICING); `PREDICTIONS.tsv` HOM-02 (MISSED) and HOM-04 (HIT).

---

## 11. A1 FIRST CONJUNCT RESTATED — 2026-11-24 23:39 ET (WQ-725, Will 2026-11-20 12:42 ET "725 approve"; go repeated in HOMER's window 2026-11-24 23:33 ET)

**Only A1's first conjunct moved.** The second conjunct, the two-quarter count, every other leg, §4, the colour rule and the 11/20 grade (0 of 5 killed, 🔴) stand. **PROME reads this diff and shows it to Will before the 2027-02-20 grade.**

| | Wording |
|---|---|
| **Old (frozen 2026-09-29 to 2026-11-24)** | MBA NDS **FHA SA total DQ falls QoQ in 2 consecutive quarters** |
| **New** | MBA NDS **FHA seriously delinquent rate (90 or more days past due, or in foreclosure; not seasonally adjusted) falls QoQ in 2 consecutive quarters** |

**Why this option and not FHA total delinquency plus foreclosure inventory:** MBA states the FHA serious-delinquency change every quarter; the FHA foreclosure rate is not in the Q2 copies HOMER can reach, so the sum could not be graded from sources in hand.

**Reading on the new wording (record, not a grade):** Q2-2026 **−3bps** (MBA Newslink 2026-08-17); Q3-2026 **unchanged** (MBA via CalculatedRisk 2026-11-20). Unchanged resets: **0 of 2**. The old wording had reached 2 of 2. This makes A1 further from its kill, which is the direction that helps the thesis; it is recorded for that reason.

| # | Date | Defect | Owed fix |
|---|---|---|---|
| D15 | 2026-11-24 | The new measure is **not seasonally adjusted**. Serious delinquency tends to fall early in the year (general knowledge; FHA history NOT read), so Q4-to-Q1 and Q1-to-Q2 falls could satisfy it without relief. The cure conjunct still guards A1 | **READ 2026-11-25 on HUD's basis (not MBA's):** raw rate fell in both Q1 and Q2 in 9 of 11 years. Still 0 of 2 at 2027-02-20 whatever Q4 does. No rewording. Report: `reports/2026-11-25_deeper-read-FHA-newhome-DR4956.md` §2 |
| D16 | 2026-11-24 | The new measure still falls when a foreclosure **completes**, because the loan leaves the stock. Better than the old wording on entry into foreclosure, not immune on exit | Read C1 (ICE foreclosure sales) beside any A1 fall |
| D17 | 2026-11-24 | §9 (2026-10-28) "the inflow end is cooling while conversion continues", and §10's "new FC starts −3% YoY (Sept)" as a reason on C1, rest on a one-month base effect: ICE FC starts Q3 ~115.6K vs 103K (+12% YoY). FC sales growth slowed (+41% Dec-25 to +14.5% Sep). Entries left as written; no count, verdict or score moved | Use this row when citing them |

---

## 12. §1 PARAGRAPH ADOPTED — 2026-11-25 09:33 ET (Will, HOMER's window, "ok go", after CATO's assessment `AGENTS/CATO/runs/2026-11-24_2244_recent-commit-accuracy.md`)

**Only the §1 paragraph changed.** Kill criteria, counts, §4, scores and 🔴 stand. Old paragraph verbatim: `archive/THESIS_history_2026-11-25.md` block A (in short: stress "has moved from ACCUMULATION to CONVERSION", making housing "an active transmission vector" to banks, households and wealth).

**Dated evidence for each channel label:** `reports/2026-11-24_thesis-paragraph-DRAFT.md` (the text Will read; live values: `STATUS.md`). One input moved the same morning: for bank-held apartment loans, **one bank (United Fidelity) is about 89% of the FDIC Q3 rise (1.404 → 1.74%); without it ~1.41 → 1.43%** (REGINALD 2026-11-25, KB ML-REG-325). The label "early, not settled" stands and the broad reading is weaker.
