# CARL — NY Fed Q3 2026 HHDC GRADING CARD **(TEMPLATE — not yet frozen)**

**Created:** 2026-08-27 (Thu) · **Status: TEMPLATE.** Freeze this ahead of the ~Nov Q3 print, then grade against the frozen text.
**Why it exists now:** §7 of `thesis/KILL_RULE_RESPEC_2026-08-15.md` requires the **shadow-grade table (§6, Rider 1)** to be embedded as a **required section** of the Q3 card. That obligation was created by the 2026-08-27 ratification and is discharged here rather than left to memory.

> ⚠️ **FREEZE DISCIPLINE (the whole point).** The Q2 card's most valuable property was that it was frozen **18 days before the data**, which is what forced the cell-B/cell-C seam defect into the open instead of being smoothed away after the fact (`[[finding_prereg_verdict_boundary_must_be_a_number]]`). **Freeze this card before the Q3 release date is known to within a week, and do not edit a cell after the release advisory posts** — addenda only, appended and dated.

> ⚠️ **SEAM CHECK BEFORE FREEZING — a Q2 defect that must not repeat.** Q2's cells **B** (*"flat ±20bps"*) and **C** (*"down ≥20bps AND…"*) **both had their first condition satisfied at exactly −20bps.** Adjacent quantitative cells must **partition**: one gets `≥`, its neighbour gets `<`. **Test-drive the exact boundary value through every cell before freezing.**

---

## §1. ⛔ REQUIRED SECTION — THE SHADOW GRADE (Rider 1, mandatory, NOT ceremonial)

**Authority:** Will, Option (A), 2026-08-16 (`PROME/proposals/2026-08-16_carl-row44-respec-optionA-RULED.md`); encoded 2026-08-27 at `thesis/THESIS.md` §Exit/Invalidation and `thesis/CHANGELOG.md`.

**Record BOTH verdicts side by side BEFORE either is acted on. Fill every cell — a blank is a failure of the rider, not an omission.**

| | Measure | Instrument | Q3 verdict | Consecutive count |
|---|---|---|---|---|
| **AS-WRITTEN** *(superseded v2.6.5 text)* | CC 90+ **balance share**, QoQ **direction** | HHDC `Page 12 Data`, CC column | *(record)* | *(record — **Q2 was decline #1 of 2**)* |
| **RE-SPEC** *(live v2.6.6 rule)* | CC **flow into 90+**, 2 consecutive declines, **cumulative ≥100bp** | HHDC `Page 14 Data`, CC series | *(record)* | *(record — **Q2 was 0 of 2**)* |

⛔ **THE TWO COUNTS START ONE APART (1 vs 0). THIS IS WHAT MAKES THE SHADOW GRADE LOAD-BEARING.**
**The as-written rule can fire at Q3 while the re-spec is still two prints away.** If that divergence occurs:
1. **Write it on this card**, both verdicts, in figures.
2. **Escalate to Will in the SAME session.** It is **never absorbed**, never deferred to a closeout, never resolved by CARL picking one.

> **Why the rider exists, in one line:** the re-spec reset the count from 1-of-2 to 0-of-2 and **CARL is the beneficiary of that reset.** The shadow grade is the mechanism that makes the reset permanently visible, so a rewrite can never hide an inconvenient fire.

### §1a. Leg 1 — record it, and record that it is NOT screening
| | Value | Source | <220K? | Sustained 8+ wks? |
|---|---|---|---|---|
| Initial claims at grading date | *(record)* | FRED `ICSA` / DOL | *(record)* | *(record)* |

⚠️ **Leg 1 currently filters NOTHING** (RED rider 1). Claims have run continuously sub-220K — **203K w/e 8/22**, 212K w/e 8/8, 207K w/e 8/15. **So leg 2 is the ENTIRE kill and the operative base rate is leg 2's 5.4%, not the joint rate.** Do not write the conjunction on this card as though leg 1 were doing screening work.
⚠️ **Leg 1 is itself revision-exposed** (open item, flagged not fixed): a level test on a weekly-revised, annually-benchmarked series. Record the **vintage** of the claims figures used.

---

## §2. INSTRUMENT DISCIPLINE — fill before grading

| Item | Requirement |
|---|---|
| **File** | `HHD_C_Report_2026Q3.xlsx` — pull **primary** from newyorkfed.org. ⚠️ **WebFetch 403s; use `curl` + browser UA.** |
| **Sheets** | **`Page 14 Data`** = flow into 90+ *(leg 2, the live rule)* · **`Page 12 Data`** = 90+ stock share *(shadow grade + CRL-05)* · `Page 13 Data` = flow into 30+ |
| ⛔ **Never substitute** | **`Page 28`** — tracked Pg 14 within ±0.01pp for five quarters, then diverged **+0.39pp in 26:Q2** |
| ⛔ **Never grade off prose** | The flow series is **chart-only** in the PDF. Numeric lives in the **data file**. *(The 30-day "unverifiable" episode was caused by reading one rendering of a release and concluding the number did not exist — `[[finding_unfetched_is_not_unavailable]]`.)* |
| **Year-trap check** | Confirm the PDF header reads **"2026:Q3"** and the release month, before extracting a single figure. |
| **Vintage record** | Grade both quarters from **ONE vintage — the report current at the grading date.** Never splice. **Write the vintage on this card.** |
| **Revision check** | ⚠️ **Open the PRIOR report, not just the new one.** A revision check that reads only the new vintage is **circular by construction** — it cannot detect a revision and returns a confident tick. This exact guard was graded WRONG on the Q2 card (`§8 addendum`, corrected 8/15). |

---

## §3. THE PRIMARY CONFIDENCE QUESTION — CRL-05 *(separate from the kill rule — do not bundle)*

**CRL-05 is at 20% and resolves on a LEVEL: CC 90+ DQ >13.74%.**

🔴 **SETTLE THE BASIS QUESTION BEFORE GRADING IT — this is a pre-condition, not a caveat.**
**13.74% is an Equifax Risk 3.0-era figure; every print from 2026:Q1 forward is VantageScore 4.0.** A level test against a pre-switch historical peak is exactly the comparison the basis break invalidates. The counter-argument — that the 90+ share is **balance-based** and therefore scoring-method-independent (STUE 2026-06-09) — is real but has been **asserted, not tested against the switch itself.**
⇒ **Whoever grades CRL-05 in November settles this first, in writing, on this card.**
*(Contrast, and it cuts for the kill rule: the re-spec grades **direction on an unbanded series** and has **no** basis exposure. Pg 14 is not credit-score-banded and the Q1 value is identical across vintages, 7.1000%.)*

---

## §4. WHAT DOES NOT COUNT — guards against known CARL failure modes

1. ⛔ **A share decline is not a numerator improvement.** Before reading any improvement, **decompose share vs dollars vs balances** and ask **what leaves the numerator when a case gets worse.** 100% of Q2's −20bps was denominator growth.
2. ⛔ **Derived figures spanning a revision boundary must carry their basis or they are not numbers.** (Q2: same-vintage +$0.23B ROSE / cross-vintage −$1.08B FELL — the sign reverses. KB-CARL-392.)
3. ⛔ **Establish the noise floor before using a directional verb.** Give the series' own quarterly dispersion, or "rose"/"fell" is doing unearned work. ⚠️ **Live instance: the Fed's own Q2 prose calls card early-delinquency transitions *"largely steady"* — the same +8bps move CARL's Q2 surfaces describe as "ROSE."** Reconcile the issuer's characterisation with your own adjective, on the card.
4. ⛔ **Two legs of one pipeline are ONE witness.** Flow into 90+ is substantially a lagged function of flow into 30+. Do not report them as independent corroboration (RED `CHG-049` §2b).
5. ⛔ **Stock + inflow cannot separate cure / extension / charge-off.** A falling stock is not evidence of loss recognition. **Split the outflow or make no claim about it** (RED `CHG-049` §1).
6. ⛔ **Issuer-reported prints are not the arbiter here.** The HHDC is bureau-wide and is the un-masked instrument — that is why the down-leg was armed against it.

---

## §5. GRADING PROTOCOL

1. Pull primary (curl+UA). Year-trap check. Record vintage.
2. **Open the PRIOR report** and diff the quarter being carried forward. Record revised / unrevised **per series** (share, flow, balance — they revise independently).
3. Fill **§1 shadow grade — both rows, every cell.** This happens **before** any interpretation.
4. If the two rows **diverge** → write it out and **escalate to Will same session.**
5. Grade CRL-05 **only after** §3's basis question is settled in writing.
6. Log to `workbook/KB.tsv`; log every prediction change to `thesis/CHANGELOG.md`.
7. Append addenda; **never edit a frozen cell.**

---

## §6. ADDENDA
*(append dated entries below — never edit above this line once frozen)*
