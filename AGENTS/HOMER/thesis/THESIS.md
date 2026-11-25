# HOMER — THESIS + THESIS-LEVEL KILL RAIL

**Kill rail re-derived: 2026-09-29** · **Criteria FROZEN from this commit** · **Formally graded 2026-11-20 (§10: 0 of 5 killed, 🔴 holds)** · Next formal grade: **2027-02-20** · Dated history → `archive/THESIS_history_2026-11-25.md` (blocks A–E) and `archive/THESIS_history_2026-11-25b.md` (blocks F–K) · Fleet registration: **`GATE-HOMER-THESIS-KILL`** in `PROME/GATES.tsv` (PROME, 2026-09-29). This file is the canonical letter; the gate row is a summary and pointer. **If any leg reaches its kill count before the next formal grade, re-date by packet to PROME.**

> ⚠️ **What this file is NOT:** the per-prediction machinery in `PREDICTIONS.tsv` (HOM-01, HOM-02, early-kill arms). That covers **two metrics**. This rail covers the **transmission chain**. A HOM-02 resolution is evidence for leg A1 below, not a thesis grade.
> **Convergence handle: §8.** Between-grade clarifications: **§7**.

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

## 2. The five elements per leg: ARCHIVED

Text: block F. Live rule kept: "N consecutive prints" counts the **instrument's own releases**, not HOMER sessions.

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

Open rows only; D1, D2, D4 to D11 (block G) need nothing further and still ship with every grade. D13, D14: block I. D15 to D17: §11.

| # | Date | Defect | Owed fix |
|---|---|---|---|
| D3 | 2026-09-29 | A1 base window is general knowledge | MBA NDS FHA SA history |
| D12 | 2026-11-16 | **A1 second conjunct has no reading at 11/20.** The kill needs the ICE Mortgage Monitor all-loans cure-rate YoY "on the latest issue at that grade"; the October and November editions did not print it (STATUS, HB-08 UNGRADED). The last printed value was −28% (July), worse than the −15% line. FHA-only −46% does not grade it. Found by HOMER in pre-grade prep; no level or criterion moved | At 11/20 grade A1's second conjunct UNGRADED (§4: not NOT-FIRED) and say so; A1 cannot read FIRED on the first conjunct alone. Whether to name a successor statistic is a between-grade amendment, raised to PROME, never made at grading |
| D18 | 2026-11-25 | §8a C2 cites special servicing 9.22% and Trepp 8.09% without sizing. Each October rise is about one loan: Cove ~28bp (ex-Cove flows about −3bp: flat, not falling), Blackjack ~69bp (ex-Blackjack ~8.5%, flat). DERIVED on Trepp's August base (`MULTIFAMILY.tsv` 11/25). Score and count unmoved | Read this row with C2; re-score at the 2027-02-20 grade |

---

## 7. Between-grade clarifications — 2026-10-15 (DAEDALUS Gate-Basis #2 + stranger read; no level moved)

These say what the frozen letter already meant. None moves a kill level, a count or a date. They were written before the next grade and before the September prints for C1 and the GSE books.

| # | Question | Answer |
|---|---|---|
| **V1** | **Which vintage resolves each core print?** | The value **as first published in that month's release**, read at the issuer: ICE First Look (that month's release) · Trepp (that month's headline MF DQ, 2dp) · Freddie Monthly Volume Summary · Fannie Monthly Summary. Later revisions (Fannie revised July 0.61→0.62% in the August release) are recorded beside the first print and **never re-grade a count already taken.** |
| **V2** | **Does an UNGRADED month break or pause a 3-print run?** | **It PAUSES the run.** The count neither advances nor resets, and the next graded print continues it. I chose pause because "break" would make my own thesis harder to kill, which is the self-serving direction. ⚠️ A missed release by the *instrument* is UNGRADED. A release I failed to fetch is a HOMER defect, logged as one, and also pauses. |
| **V3** | **"The provision rose" (C2 Fannie pairing) compared with what?** | **The same quarter's Fannie MF credit-loss provision vs the immediately prior quarter (QoQ)**, both as reported in the 10-Q/10-K for the graded quarter. Example of record: Q2 $259M vs Q1 $174M = rose. |
| **V4** | **C1 "FC pre-sale inventory YoY": the COUNT or the RATE?** | **The COUNT** (Aug: 298K, +41% YoY), as in the 9/29 grade of record. The pre-sale *rate* (0.54% in August) is an observation and never grades C1. The C2 GSE measure is Fannie MF **serious** DQ; the GATES summary dropped both qualifiers. |
| **V5** | What can 11/20 return? | Expired with the 11/20 grade (it held: no core leg could reach its count). Text: block K. |
| **V6** (2026-11-25; PROME answer, C1 and C3) | **A1 at 2027-02-20 if the first half is not met and the cure half is unread?** | **UNGRADED, halves reported separately:** "first half not met (n of 2); cure half unread (ICE printed no all-loans cure rate)". The label records the state of the instruments; the kill was not met on the half that could be read. No replacement instrument. Not covered: first half MET with the cure half unread (PROME, then Will, before the grade). Re-ask PROME if ICE skips its Dec, Jan AND Feb editions. No level, operator, instrument or consequence changed. |

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

**CARL scores; HOMER feeds.** Full table and CARL's answers: block H. Live rules kept:
- C1 and A1 are one root (R1): counted **once**, at V10. V8 is CARL's own reading. A2 is an input to V12, counted once. A3 is unscored; CRL-23 is CARL's resolver.
- ⛔ **Never map C2's state onto V3's score.** V3 is Fannie-only (CARL 10/12); C2 reaches CARL as peer evidence. A re-scope would be a thesis change routed to Will.
- Florida statewide figures come from CORAL, never from HOMER.

---

## 9. LIVE — fired-count ledger between grades (the only section that changes at a print; mechanical, per §4 "fired counts update at each print"; no criterion touched)

Entries 2026-10-15 to 2026-11-16 (0 of 5 legs at every entry): `archive/THESIS_history_2026-11-25.md` block D. New entries go here. Counts since the 2026-11-20 grade:

### 2026-11-25 — prints since the 11/20 grade (mechanical update only)

| Leg | First print integrated | Fired count |
|---|---|---|
| **C1** | none: ICE October First Look 404 at 2026-11-25 09:35 ET | **0 / 3** |
| **C2 · CMBS** | none (Trepp November ~12/01–05) | **0 / 3** |
| **C2 · GSE** | Freddie **0.62%**, Fannie **0.65%** October (issuers) ⇒ max 0.65% ≥ 0.50% | **0 / 3** |
| **A1** | no new MBA print. First conjunct on the §11 wording: **0 of 2**. Cure YoY not printed by ICE | **UNGRADED stands** (11/20; D12). Label answered by PROME 2026-11-25: §7 V6 |
| **A2** | **7.21% [11/25]** (−7bp; Freddie CSV, issuer); 71bp above the line | **0 / 4** |
| **A3** | none (December HMI ~12/15–17) | **0 / 3** |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.**

---

## 10. FORMAL GRADE — 2026-11-20: moved to `thesis/FORMAL_GRADES.md` (frozen, verbatim)

0 of 5 legs killed (4 NOT FIRED, 1 UNGRADED: A1) ⇒ 🔴 holds. Next formal grade 2027-02-20, appended there.

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
| D15 | 2026-11-24 | The new measure is **not seasonally adjusted**. Serious delinquency tends to fall early in the year (general knowledge; FHA history NOT read), so Q4-to-Q1 and Q1-to-Q2 falls could satisfy it without relief. The cure conjunct still guards A1 | **READ 2026-11-25 on HUD's basis (not MBA's):** raw rate fell in both Q1 and Q2 in 9 of 11 years. At most 1 of 2 at 2027-02-20; cannot reach 2. Warning only, MBA instrument not validated. Report: `reports/2026-11-25_deeper-read-FHA-newhome-DR4956.md` §2 |
| D16 | 2026-11-24 | The new measure still falls when a foreclosure **completes**, because the loan leaves the stock. Better than the old wording on entry into foreclosure, not immune on exit | Read C1 (ICE foreclosure sales) beside any A1 fall |
| D17 | 2026-11-24 | §9 (2026-10-28) "the inflow end is cooling while conversion continues", and §10's "new FC starts −3% YoY (Sept)" as a reason on C1, rest on a one-month base effect: ICE FC starts Q3 ~115.6K vs 103K (+12% YoY). FC sales growth slowed (+41% Dec-25 to +14.5% Sep). Entries left as written; no count, verdict or score moved | Use this row when citing them |

---

## 12. §1 PARAGRAPH ADOPTED — 2026-11-25 09:33 ET (Will, HOMER's window, "ok go", after CATO's assessment `AGENTS/CATO/runs/2026-11-24_2244_recent-commit-accuracy.md`)

Only the §1 paragraph changed. Old paragraph: block A. Evidence by channel: `reports/2026-11-24_thesis-paragraph-DRAFT.md`. Adoption record and United Fidelity note: block J.
