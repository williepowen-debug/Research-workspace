# FULL-THESIS KILL RULE — RE-SPEC (DRAFT, pre-registered)

**Drafted:** 2026-08-15 (Sat) · **CARL** · **Status: DRAFTED — NOT LIVE. Will ratifies before it goes live.**
**Authority:** `PROME/proposals/2026-08-12_rule-batch-RULED.md` **ROW 44** — *Option (b): commission the re-spec NOW, pre-registered before the Q3 data (~Nov)*, with two mandatory riders. Batch approval off PROME recs (Will: *"Batch-rule all 12 off my recs"*) — carries Will's authority, **not his individual attention on this row**. Row 44 closes when CARL confirms the encode; the rule text itself is Will-ratified separately.
**Needed:** ~9/30. Pre-registration value decays as the ~Nov Q3 print approaches.
**Answers:** `CHG-RED-045` (RED, 2026-08-12) — explicitly, in §4, per RIDER 2.

---

## §0 — SUPERSEDED TEXT, PRESERVED VERBATIM

> **Full thesis kill (both required):**
> - Claims <220K sustained 8+ weeks AND CC 90+ DQ declines 2 consecutive quarters

`thesis/THESIS.md:398`, in force from v2.1 through v2.6.5. **Current standing under the as-written rule: 1-of-2.** Leg 1 satisfied (initial claims 199K at drafting of the escalation; **209K w/e 8/8, still <220K, sustained well beyond 8 weeks**). Leg 2 at decline #1 of 2 (Q2 CC 90+ 13.12% → 12.92%). **A second decline at the ~Nov Q3 print fires the kill on its own registered terms.**

---

## §1 — THE DEFECT

The rule keys leg 2 on a **share**. A share can fall while the stock of distress grows, because the denominator is not exogenous to the stress.

Q2-2026 is that case exactly, and it is why this re-spec exists rather than a quiet grade:

| Q2 2026 | Value | Direction |
|---|---|---|
| CC 90+ **share** | 13.12% → **12.92%** | ↓ −20bps — *counts as decline #1 under the as-written rule* |
| CC 90+ **dollars** (same vintage) | $162.95B → **$163.18B** | ↑ **+$0.23B** |
| CC **balances** | $1.2420T → **$1.2630T** | ↑ +$21.0B (+1.69%) |

100% of the share decline is denominator growth. The numerator did not improve.

**RED conceded this defect is real** (CHG-045 §2b): *"A share can fall while the stock of distress grows. That is a genuine specification defect."*

---

## §2 — WHY THE OBVIOUS FIX (A DOLLAR LEG) IS THE WRONG ONE

The intuitive repair is to re-key leg 2 onto **delinquent dollars**. Two independent reasons not to, the second discovered by measurement on 2026-08-15 and decisive:

**(a) RED's objection — it is a ratchet.** A dollar leg *added* to a share leg can only ever block the kill, never fire it early. *"A pre-registration that can only be rescued was never pre-registered."* Correct, and conceded.

**(b) The dollar series is revision-exposed at a magnitude that swamps the signal.** The 2026Q2 report carries an explicit footnote — *"2026Q2 report includes a revision to 2026Q1 credit card balances outstanding"* (`HHD_C_Report_2026Q2.xlsx`, Page 3 Data). Pulling both vintages:

| 2026Q1 figure | Q1 report | Q2 report | Revised? |
|---|---|---|---|
| CC 90+ **share** | 13.1200% | 13.1200% | **no** |
| CC **flow into 90+** | 7.1000% | 7.1000% | **no** |
| CC **balance** | $1.2520T | $1.2420T | **yes — −$10B** |

Delinquent dollars are **derived** (share × balance), so they inherit the balance revision. The revision is **$10B against a signal of $0.23B — 43×.** Worse, it reverses the sign:

| Basis | Q1 → Q2 delinquent CC dollars | Reads as |
|---|---|---|
| **Same-vintage** (both quarters from the Q2 report) — *correct* | $162.95B → $163.18B | **+$0.23B, ROSE** |
| Cross-vintage (Q1 report's Q1 vs Q2 report's Q2) — *naive* | $164.26B → $163.18B | **−$1.08B, FELL** |

**A kill leg keyed on dollars would be measuring revision noise, and its verdict would depend on which vintage the grader happened to open.** The share and the transition were both unrevised across this same pair.

---

## §3 — THE RE-SPEC

**Leg 1 — UNCHANGED.**
> Initial claims <220K sustained 8+ weeks.

*(Not touched, per the batch rider "no threshold moved in the same edit." Its own revision exposure is logged as an open item in §6 — flagged, not fixed here.)*

**Leg 2 — RE-SPECCED. Measure the flow, not the stock — with a materiality floor.**

> Leg 2 is satisfied when the **quarterly transition rate into serious delinquency (90+) for credit cards** falls in **2 consecutive quarters** **AND** the **cumulative decline across those two quarters is ≥100bp**.
>
> **Instrument:** NY Fed *Quarterly Report on Household Debt and Credit*, **"Flow into Serious Delinquency (90+) by Loan Type," Credit Card series** — `HHD_C_Report_<QTR>.xlsx`, sheet **`Page 14 Data`**. Numeric in the data file; the report prose is chart-only for this series and must not be used.
>
> **The kill fires when leg 1 holds AND leg 2 is satisfied.**

### ⛔ THE MAGNITUDE FLOOR IS NOT COSMETIC — IT RESETS THE CURRENT COUNT FROM 1-OF-2 TO 0-OF-2. READ THIS BEFORE RATIFYING.

**Direction-only was my first draft this morning, and base-rating it killed it.** Over the full 94-quarter series (2003:Q1–2026:Q2):

| Candidate leg-2 spec | Base rate | Silent through the GFC build (06:Q1–09:Q4)? |
|---|---|---|
| **2 consecutive declines, any size** *(my morning draft)* | **43.5%** | ❌ fired 06:Q1 |
| 2 consecutive declines, each ≥25bp | 15.2% | ❌ fired 06:Q1 |
| 2 consecutive declines, cumulative ≥50bp | 21.7% | ❌ fired 06:Q1 |
| 4 consecutive declines, any size | 33.3% | ❌ fired 06:Q1 |
| YoY decline ≥100bp, 2 consecutive quarters | 16.9% | ❌ fired 06:Q1 |
| **✅ 2 consecutive declines, cumulative ≥100bp** | **5.4%** | **✅ SILENT** |

**A full-thesis kill that fires on a 43.5% base-rate event is not a kill rule — it is a coin flip with a thesis attached.** The current 8-quarter band is **6.93–7.18% = 25bp wide**, while the **median absolute QoQ move is 20bp**: the series moves nearly as much each quarter as the entire band it has occupied for two years. Direction alone is noise at this level. *(DEWEY C3, 8/12, independently flagged the same flatness — "flat at 6.93–7.18% for eight quarters" — which is what sent me to base-rate it.)*

**The winning spec was selected on base rate + GFC separation BEFORE I computed what it does to Q2.** It has excellent discrimination: in 23 years it fires **exactly once — 10:Q4 through 11:Q4**, the genuine post-GFC consumer healing episode, which is precisely the state this kill rule exists to detect. And it stays silent through the entire GFC build, where the series rose monotonically 5.51% → 10.96%.

**⚠️ AND HERE IS THE COST, STATED PLAINLY:**

| | Q2-2026 verdict | Consecutive count |
|---|---|---|
| **As-written** (share, direction-only) | decline | **1 of 2** |
| Morning draft (flow, direction-only) | decline | **1 of 2** |
| **This spec** (flow, ≥100bp floor) | **NOT a decline** — cumulative 7.13 → 7.10 → 6.97 = **−16bp vs a 100bp floor** | **0 of 2** |

**So this version of the re-spec moves the kill from one print away to two prints away, and I am the one who benefits.** That is exactly the shape RED's `CHG-045` warned about, and I am not going to pretend the base-rate justification makes it invisible. **This is a WILL DECISION, not a CARL call.** The options, with my recommendation:

- **(A) — RECOMMENDED. Ratify the ≥100bp floor and accept the reset to 0-of-2.** Rationale: the alternative is a rule with no discriminating power, and the defect that started this whole exercise was a measure that moves for reasons unrelated to household distress. A 43.5% trigger is that same disease. **The shadow-grade rider (§6) makes the as-written 1-of-2 count visible at every future print, so the reset can never hide.**
- **(B) Disjunctive, zero-rescue: leg 2 fires on EITHER the as-written share test OR the ≥100bp flow test.** Keeps the current count at **1-of-2** (via the share leg, untouched), adds the flow test as an additional faster path. **Strictly easier to fire than the status quo, so it is ratchet-proof by construction** — but it retains the defective share measure, whose known bias is toward firing on denominator growth.
- **(C) Reject the re-spec; grade the as-written rule at Q3.** Costs nothing, keeps a measure that Q2 demonstrated is 100% denominator-driven.

**I recommend (A) and would accept (B) without argument.** (B) is the honest choice if the reset looks self-serving from outside — it gives up nothing except elegance, and *"CARL took the version that keeps the kill one print away"* is worth more than a clean spec.

**Basis policy** (added 2026-08-15 on REGINALD's `SIG-W-20260812-002` relay — WALTER, `CONFIRMED-AT-PRIMARY-SOURCE-DOCUMENTATION`, conf 0.92):
> **Leg 2 grades on QoQ DIRECTION, both quarters read on a single basis. It makes no level-vs-history comparison, so the 2026:Q1 credit-score model switch (Equifax Risk 3.0 → VantageScore 4.0) does not reach it.** Two independent reasons: (i) the switch affects the **credit-score-banded** charts — HHDC **pages 6-9** (originations by credit score / credit score at origination), which the NY Fed cautions about itself — and **Page 14 is not credit-score-banded**; (ii) confirmed empirically above, the Q1 flow value is **identical across the two vintages (7.1000%)**. *(Corroborated independently by STUE's register **S4**, settled 2026-08-13: Pg 12 = 90+ stock share · Pg 13 = flow into 30+ · **Pg 14 = flow into 90+ — cite Pg 13/14 for flow.** ⚠️ Pg 28 tracked Pg 14 within ±0.01pp for five quarters then diverged **+0.39pp in 26:Q2** — **never substitute it.**)*
>
> **This is why the re-spec is basis-safer than the rule it replaces.** REGINALD's point was that *"a kill rule that resolves on a series with a model change inside it should say which basis it grades on"* — and it cuts **for** the re-spec: the as-written rule's own headline (*"first decline off the 15-year high"*) is **basis-broken**, because the 15-year level comparison runs back through Equifax 3.0. **A direction test on an unbanded series has no such exposure.**

**Revision policy** (complies with the fleet L-15 convention ruled 2026-08-12, row 36b — *thresholds grade once at publication vs re-grade on revision is a property of DATA, not of one desk's instrument*):
> Grade both quarters from **one vintage — the report current at the grading date.** Never splice a prior report's quarter against a later report's quarter. **Record the vintage on the grading card.** If the series itself is ever revised, re-grade on the revised series and say so.

**Standing under the re-spec, applied to Q2-2026:** CC flow into 90+ **7.10% → 6.97% = a decline.** **Decline #1 of 2 — identical to the as-written rule.** The kill remains **1-of-2**.

---

## §4 — ANSWER TO `CHG-RED-045` (RIDER 2 — required explicitly, in the spec text)

RED's condition: *"a dollar leg is legitimate only if symmetric — it must be able to fire the kill as well as prevent it."*

**Answer: no dollar leg is registered, so the ratchet objection does not arise.** The re-spec **replaces** the measure rather than **adding** a conjunct. There is no enter-any-1-of-N / exit-all-N asymmetry, because leg 2 remains a single condition.

Symmetry demonstrated on the letter — the re-spec is two-directional, not protective:

| State of the world | As-written (share) | Re-spec (flow, ≥100bp) |
|---|---|---|
| Share falls on denominator growth; **inflows rise** | **decline** ✓ | not a decline |
| Share flat-or-rising on denominator growth; **inflows fall ≥100bp over 2q** | not a decline | **decline** ✓ |
| Share falls sharply; inflows fall **<100bp** | **decline** ✓ | not a decline |
| **Q2-2026 actual** (share −20bps; flow 7.13→7.10→6.97 = −16bp) | **decline #1 of 2** | ⛔ **NOT a decline — 0 of 2** |

**Row 2 remains the anti-ratchet proof — the re-spec can still kill this thesis in a state the old rule cannot.** The magnitude floor is symmetric in construction: it is a **materiality threshold, not a protective conjunct**, and it makes the rule harder to fire on *noise* in both directions rather than harder to fire *against CARL* specifically.

**⛔ BUT ROW 4 IS A REVERSAL FROM THIS DOCUMENT'S FIRST DRAFT AND I AM NOT BURYING IT.** As written this morning (direction-only), the re-spec returned decline #1 of 2 and rescued nothing — that was its strongest defence against `CHG-045`. **Base-rating the trigger destroyed that defence:** direction-only fires 43.5% of the time and is not a kill rule. The spec that survives base-rating **does** reset the count to 0-of-2. **So the honest statement of where this landed is: the re-spec no longer rescues nothing. It buys CARL one extra print, and the justification for it is a measurement that was made before the consequence was computed — which is a reason to trust it, not a reason to skip saying so.**

**This is why §3 routes the choice to Will as options (A)/(B)/(C) rather than encoding my preference.** Option **(B)** — disjunctive, share OR flow — **holds the count at 1-of-2 and is ratchet-proof by construction.** RED should weigh in on which; I have pre-committed to accepting (B) without argument.

**What still holds regardless of which option is chosen:** no **dollar** leg is registered under any of them, so the specific objection `CHG-045` raised — an asymmetric dollar leg that can only rescue — does not arise. And the instrument choice rests on a measurement (the flow series was unrevised where the balance series moved $10B) made before any of the consequences were computed.

---

## §5 — WHY FLOW IS ALSO THE MECHANISM-TRUE MEASURE

Independent of the ratchet argument, RED's §3 adjudication of the Q2 counter-reads concluded that transitions are the only leg that survives, and CARL concurs:

- **Dropped entirely, per RED:** the *"$40B out of 120+ late vs $43.5B into severely derogatory"* leg. Severely-derogatory paper is **already-realized loss — the exhaust, not a forward channel.** It was the biggest-sounding number in the Q2 decomposition and it cannot carry a forward claim. **Removed from the structural read, not demoted.**
- **Conceded, per RED:** the denominator rebuttal fails. CC balances grew +1.69% QoQ against falling real disposable income, with limits +$85B and HELOC balances up a 17th consecutive quarter. **Deflating distress by distress-driven borrowing understates distress.**
- **What survives:** inflow rates. They are the forward transmission channel; everything else in the Q2 decomposition is stock accounting.

A kill rule should be keyed to the mechanism it is meant to falsify. This thesis claims cost squeeze **converts** to credit deterioration — a claim about **flow**. Keying its kill to flow makes the rule falsify the actual claim.

⚠️ **CARRIED CAVEAT — RED's unresolved challenge, recorded not waved.** RED (§3b) is right that CARL asserted mortgage transitions were *"not obviously affected"* by the Fed-stated servicer-transfer reporting gap **without verifying it**, and that a missing servicer removes a whole book, non-random by construction — biasing transitions in an unknown direction. **Two things are now known and one is not:**
1. ✅ The **credit-card** flow series — the one this re-spec registers — was **unrevised** across the Q1→Q2 vintage pair (7.1000% both). That is evidence of stability, **not** evidence the servicer gap does not touch it.
2. ✅ The caveat appears **nowhere in the Q2 data workbook** (searched all sheets: the only revision notes are the Q1 CC balance footnote and two "Revised May 2017" state-table notes). Its provenance is the **PDF prose**, which CARL no longer holds locally.
3. ❌ **Whose book went missing is still unknown**, and therefore the sign of any bias is unknown.

**Owed before ratification:** re-pull `HHD_C_Report_2026Q2.pdf` and quote the caveat verbatim with its stated scope — specifically whether it is scoped to mortgage servicing only. **If it reaches card reporting, this re-spec's instrument inherits a sign-unknown bias and Will must be told before ratifying.** Tracked as an open item, not treated as closed.

---

## §6 — RIDER 1: THE SHADOW GRADE (not optional — the point of the ruling)

At the **~Nov Q3 print**, the grading card records **both verdicts, side by side, before either is acted on**:

| | Measure | Q3 verdict | Consecutive count |
|---|---|---|---|
| **AS-WRITTEN** | CC 90+ balance share, QoQ direction | *(record)* | *(record — **Q2 was decline #1 of 2**)* |
| **RE-SPEC** | CC flow into 90+, 2 consecutive declines cumulative ≥100bp | *(record)* | *(record — **Q2 was 0 of 2**)* |

⛔ **The two counts now START ONE APART (1 vs 0), which makes the shadow grade load-bearing rather than ceremonial.** It was drawn up when both stood at 1 and cost nothing. It costs something now: **the as-written rule can fire at Q3 while the re-spec is still two prints away, and that divergence must be written on the card and escalated to Will in the same session.**

**If the as-written rule fires and the re-spec does not, that fact is written on the card and escalated to Will in the same session — it is not absorbed.** This exists so the rewrite can never hide an inconvenient fire.

Both counts currently stand at **1**.

**Other open items (flagged, not fixed here — the rider forbids moving them in this edit):**
- **Leg 1 revision exposure.** Initial claims are revised weekly and benchmarked annually. A *"<220K sustained 8+ weeks"* level test on a revision-prone series has the same class of exposure §2(b) found in the balance series, and is un-specced for it. Separate re-spec candidate.
- **CRL-05's own resolver** still reads on the 90+ *share* (Q3 endpoint). Whether it should follow leg 2 onto flow is a **separate** decision — not bundled, because CRL-05 is a confidence line and this is a thesis kill.
- ⚠️ **CRL-05 IS basis-exposed where this kill rule is not, and that asymmetry is now visible.** CRL-05 resolves on a **LEVEL** — *"CC 90+ DQ >13.74%, the GFC peak"* — and **13.74% is an Equifax Risk 3.0-era figure** while every print from 2026:Q1 forward is VantageScore 4.0. **A level test against a pre-switch historical peak is exactly the comparison the basis break invalidates.** The 90+ *share* is balance-based and therefore scoring-method-independent (STUE, 2026-06-09, methodology asterisk dropped), which is a real argument that the seam does **not** bite here — **but that argument has been asserted, not tested against the switch itself.** Flagged now, not re-specced: CRL-05 sits at 20% and resolves ~Nov, so there is time, and moving it in this edit would violate the batch rider. **Whoever grades CRL-05 in November must settle the basis question first.**

---

## §7 — WHAT CHANGES ON RATIFICATION

| Surface | Change |
|---|---|
| `thesis/THESIS.md:397-398` | Kill rule text replaced; superseded text preserved verbatim inline |
| `thesis/CHANGELOG.md` | Version bump + old→new + rationale |
| Q3 grading card (~Nov, to be frozen ahead of the print) | Shadow-grade table from §6 embedded as a required section |
| `workbook/KB.tsv` | KB row for the vintage finding (§2b) |

**No score change. No threshold moved. No confidence moved. Zero capital.**

---

*Drafted by CARL 2026-08-15 against row 44. Answers CHG-RED-045, which resolves at the Nov HHDC. **Not live until Will ratifies.***
