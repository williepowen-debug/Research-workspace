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

**Leg 2 — RE-SPECCED. Measure the flow, not the stock.**

> A quarter counts as a **"CC 90+ decline"** when the **quarterly transition rate into serious delinquency (90+) for credit cards** falls quarter-over-quarter.
>
> **Instrument:** NY Fed *Quarterly Report on Household Debt and Credit*, **"Flow into Serious Delinquency (90+) by Loan Type," Credit Card series** — `HHD_C_Report_<QTR>.xlsx`, sheet **`Page 14 Data`**. Numeric in the data file; the report prose is chart-only for this series and must not be used.
>
> **The kill fires when leg 1 holds AND leg 2 records a decline in 2 consecutive quarters.**

**Revision policy** (complies with the fleet L-15 convention ruled 2026-08-12, row 36b — *thresholds grade once at publication vs re-grade on revision is a property of DATA, not of one desk's instrument*):
> Grade both quarters from **one vintage — the report current at the grading date.** Never splice a prior report's quarter against a later report's quarter. **Record the vintage on the grading card.** If the series itself is ever revised, re-grade on the revised series and say so.

**Standing under the re-spec, applied to Q2-2026:** CC flow into 90+ **7.10% → 6.97% = a decline.** **Decline #1 of 2 — identical to the as-written rule.** The kill remains **1-of-2**.

---

## §4 — ANSWER TO `CHG-RED-045` (RIDER 2 — required explicitly, in the spec text)

RED's condition: *"a dollar leg is legitimate only if symmetric — it must be able to fire the kill as well as prevent it."*

**Answer: no dollar leg is registered, so the ratchet objection does not arise.** The re-spec **replaces** the measure rather than **adding** a conjunct. There is no enter-any-1-of-N / exit-all-N asymmetry, because leg 2 remains a single condition.

Symmetry demonstrated on the letter — the re-spec is two-directional, not protective:

| State of the world | As-written (share) | Re-spec (flow) |
|---|---|---|
| Share falls on denominator growth; **inflows rise** | **decline** ✓ | not a decline |
| Share flat-or-rising on denominator growth; **inflows fall** | not a decline | **decline** ✓ |
| **Q2-2026 actual** (share −20bps; inflows 7.10→6.97) | **decline #1** | **decline #1** |

**The re-spec can kill this thesis in states the old rule could not** (row 2) — the second row is the anti-ratchet proof. And **it does not rescue CARL on the observation that prompted it** (row 3): Q2 counts as decline #1 under both rules, so the kill sits one print from firing under the new spec exactly as it does under the old one.

**The strongest form of the answer:** the re-spec was chosen on a *measurement* — that the flow series was unrevised where the balance series moved $10B — not on which rule was kinder. Had the measurement gone the other way it would have argued for the dollar leg, and I would have owed RED a symmetric one.

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
| **AS-WRITTEN** | CC 90+ balance share, QoQ | *(record)* | *(record — Q2 was decline #1)* |
| **RE-SPEC** | CC flow into 90+, QoQ | *(record)* | *(record — Q2 was decline #1)* |

**If the as-written rule fires and the re-spec does not, that fact is written on the card and escalated to Will in the same session — it is not absorbed.** This exists so the rewrite can never hide an inconvenient fire.

Both counts currently stand at **1**.

**Other open items (flagged, not fixed here — the rider forbids moving them in this edit):**
- **Leg 1 revision exposure.** Initial claims are revised weekly and benchmarked annually. A *"<220K sustained 8+ weeks"* level test on a revision-prone series has the same class of exposure §2(b) found in the balance series, and is un-specced for it. Separate re-spec candidate.
- **CRL-05's own resolver** still reads on the 90+ *share* (Q3 endpoint). Whether it should follow leg 2 onto flow is a **separate** decision — not bundled, because CRL-05 is a confidence line and this is a thesis kill.

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
