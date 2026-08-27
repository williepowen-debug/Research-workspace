# CHG-RED-051 — SELF, APPARATUS class: RED's falsification registry has a selectivity axis and no correctness axis

**Opened:** 2026-08-27 (S35, Will-directed) · **Target:** RED's own `registry/FALSIFICATION_TRIGGERS.tsv` — the surface that moves RED's weights
**Grade:** STRONG · **Class:** APPARATUS (the first one RED has ever opened — see ML-RED-185)
**Resolution:** 2026-10-31, or at the first fire of any registry row, whichever is sooner
**Weight impact: NONE, deliberately.** See §6.

---

## 0. Why this exists and why it is not the challenge I would have written

ML-RED-185, adopted this morning off SAM's unseal: *an author's self-attack list defends the ARGUMENT and is structurally blind to the APPARATUS.* RED's two standing self-challenges (CHG-027 bifurcation framing, CHG-028 stagflation realization) both attack the argument. Neither attacks the instruments. RED adopted the rule that it must carry **≥1 live apparatus self-challenge at all times** and stood at **0 of 2**.

The concrete form was supplied from outside, which is the pattern this challenge is about. SAM, retracting their own modal clause tonight (`c919e8f73`), attached two limits. The second:

> **Selectivity is not correctness.** Neither test asks whether the removed firings were the ones that *should* go. A leg can strip 75% of firings and strip exactly the true positives. **Separation against outcomes is a third question and neither of our tests touches it.**

They aimed it at RED-FT-11. It generalises to the whole registry, and generalised it is much worse.

---

## 1. CHARGE A (STRONG) — the registry has no outcome axis, structurally

`FALSIFICATION_TRIGGERS.tsv` carries 15 columns: `trigger_id · metric · threshold_op · threshold_value · sustain_window · action · instrument_basis · state · action_magnitude · recipient_chain · falsification_thesis_ref · exit_op · exit_threshold · exit_sustain · exit_source`.

**Not one of them records whether a fire was RIGHT.** `state` records whether it is firing. `action_magnitude` records what RED did about it. Nothing records what happened next.

Measured across every RED surface:

| Surface | carries an `Outcome` column? | what it governs |
|---|:--:|---|
| `workbook/PREDICTIONS.tsv` | **YES** | falsifiable claims — scored 8W/12C/1A |
| `registry/FALSIFICATION_TRIGGERS.tsv` | **NO** | **the hypothesis weights** |
| `workbook/VX.tsv` | **NO** | counter-evidence bull/bear weights |
| `docket/WATCHLINES.tsv` | **NO** | display lines |

⇒ **RED grades its predictions and does not grade its instruments** — and the ungraded surface is the one with write access to the book.

**Corroborating grep, run across the entire RED tree** (`STATUS.md`, `thesis/CHANGELOG.md`, `workbook/ML.tsv`, `MEMORY.md`, then widened to every file): searching for any trigger ID within 80 characters of *false positive · true positive · was the fire right · outcome-grade · separation · hit rate · precision* returns **zero hits**. Every recorded instance of a trigger being "wrong" is about its **specification** (FT-05's base rate, FT-08's inert leg), its **representation** (FT-08's half-registration), or its **grading mechanics** (FT-06's post-hoc magnitude). **None is about its signal being wrong about the world.**

**Three triggers have fired** (FT-01, FT-06, FT-07). **At least four weight events have executed off them.** **Outcome grades to date: zero.** Not "few" — the axis does not exist.

## 2. CHARGE B (STRONG, and this one is measured) — base rates were computed once and never recomputed, so two rows have silently become regime descriptors

Every trigger's selectivity credential is a base rate computed at registration (mostly S30, 2026-08-12) over a fixed ~18-month sample. **A base rate is an instrument. It goes stale like any other, and there is no `Last_Reviewed` on it.**

Recomputed today against the live series:

| ID | row-published | full-sample (repro) | last 120 sessions | last 85 | ratio vs published | |
|---|---:|---:|---:|---:|---:|---|
| **FT-01** HY<280 s=3 | 21.8% | 23.8% | **48.3%** | **68.2%** | **2.9×** | 🔴 **DESCRIPTOR in-regime** |
| **FT-07** CCC>930 s=1 | 32.5% | 34.3% | **84.2%** | **91.8%** | **2.7×** | 🔴 **DESCRIPTOR in-regime** |
| FT-06 VIX<16 s=5 | 6.9% | 8.2% | 8.2% | 8.2% | 1.0× | 🟢 stable |
| FT-02 HY>320 s=3 | 10.1% | 9.8% | 0.0% | 0.0% | — | armed, un-approached |
| FT-09 5y5y>2.55 s=5 | 0.0% | 0.0% | 0.0% | 0.0% | — | above sample max, as disclosed |

**⚠️ The published numbers REPRODUCE.** 21.8→23.8, 10.1→9.8, 6.9→8.2, 32.5→34.3, 0.0→0.0. **The S30 arithmetic was honest and competent. This is not an error finding — it is a staleness finding,** which is worse, because a correction pass would not have caught it and did not.

**This is the FT-04 defect.** FT-04's own row discloses it in these words: *"it would have been FIRING ON TWO-THIRDS OF THE LAST 18 MONTHS … the level is doing regime-detection work the threshold does not express."* That disclosure is on the row where the condition was true **at registration**. On FT-01 and FT-07 the same condition arrived **afterwards**, and nothing was watching, because base-rate review is not a scheduled event anywhere in RED's boot or write-back.

## 3. CHARGE C (STRONG) — the synthesis, and it is why A and B are one defect

**FT-01's registered action is `IMMEDIATE-FALSIFY`.** It is the registry's designated thesis-killer.

Since 2026-05-01 it has fired on **70 of 85 sessions (82.4%)**, in five episodes, and is firing now. **Read literally, RED's thesis has been falsified for most of four months.** RED runs **net-bear 60 / confidence 69**.

So exactly one of these is true:
1. FT-01 is **mislabelled** — it is a counter-signal, not a falsifier, and `IMMEDIATE-FALSIFY` overstates it; or
2. FT-01 is correctly labelled and **RED has been ignoring its own falsifier for four months.**

**The registry cannot distinguish these two cases** — and distinguishing them requires precisely the outcome axis that Charge A says does not exist. That is the whole defect in one row: **RED built a machine that can tell you a line was crossed and executes a weight move on it, and cannot tell you whether crossing that line ever meant anything.**

## 4. The axis is buildable — demonstrated, not asserted

To avoid making this challenge the thing it complains about, a first outcome grade was computed. **FT-01 claims that when credit refuses to widen, the bear is wrong. Test: after it fires, does the bear's own cohort rally?**

| fire (s=3 met) | KRE +20s | KRE +60s | verdict @60 |
|---|---:|---:|---|
| 2025-02-10 | −13.7% | −13.1% | WRONG (bear fine) |
| 2025-08-28 | −2.0% | −6.0% | WRONG (bear fine) |
| 2025-09-15 | −4.4% | +0.7% | RIGHT (bear hurt) |
| 2026-01-08 | +8.2% | −2.0% | WRONG (bear fine) |
| 2026-05-05 | −2.9% | +8.8% | RIGHT (bear hurt) |
| 2026-05-25 | +5.2% | +6.3% | RIGHT (bear hurt) |
| 2026-06-15 / 07-02 / 08-05 | +4.9% / +1.4% / — | — | UNRESOLVED (live) |

**Resolved n=6 → FT-01 correct 3/6 = 50% at 60 sessions (2/6 at 20 sessions).**

**⚠️ What this is and is not.** It is a **demonstration that the axis is computable in ~20 lines**. It is **NOT a verdict on FT-01**, and citing it as one would be the error this challenge exists to name:
- **n=6.** 3/6 is equally consistent with a fair detector and with a coin. Same caveat SAM put on RED's n=4 tonight, applied here to RED by RED.
- **KRE is RED's choice of outcome proxy and RED chose it.** It is defensible (it is the cohort the thesis is actually about) but it is a **free parameter**, and picking the proxy after seeing the answer is `[[finding_crosscheck_with_free_parameter_validates_nothing]]`. A real scorer must **pre-commit the proxy and the horizon before running.**
- **60 sessions is also RED's choice**, and the 20-session read is worse. Both are quoted so neither can be selected later.
- The sample straddles regimes; the 2025-02-10 fire predates most of the current thesis.

**Honest headline: FT-01's correctness is UNKNOWN, has always been unknown, and the first look at it says it may be a coin flip — which is exactly the state the registry is structurally unable to detect.**

## 5. Pre-registered falsifiers — run NOW, not deferred

| | Falsifier | Result today |
|---|---|---|
| **F1** | An outcome grade for any fired RED trigger exists somewhere RED has not looked ⇒ Charge A downgrades to MODERATE (labelling, not absence) | **RUN. Zero hits across the entire RED tree.** A stands. |
| **F2** | The elevated firing rates are an artifact of RED's window choice ⇒ Charge B is RED's defect, not the registry's. *(VULCAN 8/24: a rule counting N consecutive readings is ungradeable when the OBSERVER picks when to read. RED picked 85.)* | **RUN across 40/60/85/120/180/260/full. Strictly MONOTONE in recency, both series** (FT-01 23.8→32.7→41.1→48.3→68.2→73.3→77.5; FT-07 34.3→43.1→62.2→84.2→91.8→100→100). **A regime shift, not window-shopping.** ⚠️ It also means **short windows FLATTER this charge** — so §2 headlines the conservative 120-session figure, not the 85. |
| **F3** | The correctness axis cannot be specified in numbers ⇒ Charge C is rhetoric | **REFUTED by §4** — computed, with its own limits stated. |
| **F4** | *(forward)* A scorer with a **pre-committed** proxy and horizon shows FT-01 separating from chance at n≥12 ⇒ Charge C's "may be a coin flip" is withdrawn and FT-01's label stands | **OPEN — this is the deliverable, not today's claim.** |

## 6. Disposition — and the half that matters is what does NOT move

**NO HYPOTHESIS WEIGHT MOVES ON THIS. HOLD 69 / net-bear 60, unchanged.**

This is the same guard RED wrote into FT-11 four hours ago and it binds identically here: **an apparatus finding is a finding about RED's instruments, not about the world.** It does not say the bear is wrong. It says RED cannot currently tell whether its bear-side instruments have ever worked. Moving a weight on it would score an instrument defect as evidence — the ML-RED-144 class, third bucket.

**⛔ Explicitly NOT done today: no threshold re-cut.** FT-01 and FT-07 are both bear-relevant, and the standing guard puts threshold re-specs in the **9/4–9/11** window *on a day the bear is not losing*. Re-cutting a bear trigger in the session that found it defective is the move this registry exists to prevent. **Flagged, dated, not touched** — the same disposition FT-05 and FT-07 already carry.

**Owed:**
1. **`Last_Reviewed` + a rolling-window base rate on every registry row**, so Charge B cannot recur silently. This is the cheap structural fix and it is where the value is.
2. **An `outcome` axis** — pre-committed proxy + horizon per row, scored at exit, never at fire.
3. **FT-01's label adjudicated** — `IMMEDIATE-FALSIFY` or counter-signal. It cannot stay both.

## 7. Provenance, stated so it cannot be laundered later

The generalisable half of this challenge (**selectivity is not correctness**) is **SAM's**, delivered against their own retraction. RED supplied the FT-11 counterexample that forced the retraction; SAM supplied the limit that turned it back on RED. **RED did not find this unprompted** — which is the sixth externally-supplied defect on RED's book today against zero self-found, and is the exact pattern ML-RED-185 predicts. Recorded here rather than in a commit message so it is graded, not narrated.
