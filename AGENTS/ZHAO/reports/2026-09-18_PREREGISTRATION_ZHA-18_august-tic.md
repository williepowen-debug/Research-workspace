# PRE-REGISTRATION — ZHA-18, August 2026 TIC

**Written 2026-09-18, twenty-eight days before the print.** Release: **Friday 2026-10-16, ~16:00 ET** (Treasury TIC, August 2026 reference month). **Nothing in this file may be edited after 2026-10-16 except to record the grade.**

**Why a letter at all:** ZHA-17 graded NO on July because its boundary was written before the number existed and the ambiguous zone was pre-assigned. That worked. This letter keeps that design and fixes the defect found in ZHA-15 — a threshold with a direction and no magnitude floor.

---

## 1. THE SCORED QUESTION (one question, one branch map)

> **ZHA-18: August 2026 TIC shows China, Mainland long-term / coupon net Treasury sales at ≤ −$5.0B — a THIRD consecutive month of duration selling.**

**Confidence: 40%.** Series: TIC Table 3, `for_lt_treas_net`, country `China, Mainland`, in $ millions.

| Branch | Condition (August LT net) | Grade |
|---|---|---|
| **A** | ≤ −$5,000M | **YES** — three consecutive months; a trend by the declared bar |
| **B** | −$5,000M < LT < +$5,000M | **NO** — the run breaks; June–July was a two-month episode |
| **C** | ≥ +$5,000M | **NO**, and additionally records a direction reversal (China bought duration in size) |

- **Boundary owner, declared in advance:** exactly **−$5,000M** grades **A (YES)** — the `≤` is binding.
- **Branches A/B/C are exhaustive and mutually exclusive and sum to 1.00 conditional on resolution.**
- **Non-resolution carries NO mass (WQ-161 ①):** if Treasury does not publish the August reference month by **2026-10-23**, the row takes **Status = STUCK**. STUCK is not a branch, gets no probability, and is never graded NO.
- **Graded on Treasury's published Table 3 only** — not on press characterisations, not on the holdings level, not on my own reconstruction.

### Why 40% and not the 60% the story wants — both numbers written, per `finding_corrective_inherits_the_anchor_it_corrects`

**Narrative-anchored number (written first, from the standing read): ~60%.** Two consecutive coupon-selling months; TTM LT −$75.4B; SAFE explicitly curbing concentration; trade tension into a summit.

**Cold number (computed from the series with the narrative not in view): ~33–40%.** Base-rated on TIC Table 3, n = 42 months of flow data (2023-02 → 2026-07):

| Reference class | Result |
|---|---|
| P(China LT ≤ −$5B in any month) | **23/42 = 54.8%** |
| **P(LT ≤ −$5B \| prior TWO months both ≤ −$5B)** | **3/9 = 33.3%** |
| P(LT merely negative \| prior two ≤ −$5B) | 5/9 = 56% |
| Last 12m P(≤ −$5B) | 6/12 = 50% |
| Last 12m mean / **median** | −$6.3B / **−$3.0B** |

⛔ **The conditional is LOWER than the unconditional. After two months of ≤ −$5B selling, this series extends the run only a third of the time — clustering is followed by mean reversion, not continuation.** The intuition "two months makes it a behaviour" is the opposite of what the data says. The median month is −$3.0B, which sits **inside branch B**.

**Settled at 40%,** above the raw 3/9 because of two regime facts a 42-month base rate cannot see — the TTM run-rate is more negative than the historical average, and SAFE's concentration-curbing is stated policy, not inference — and far below 60% because the narrative had no base rate under it. The two numbers disagree by ~1.7×, inside the 2× rule, and both are recorded here as that rule requires.

⚠️ **Honest limit on the cold number: n = 9 for the conditional.** The 95% interval on 3/9 runs roughly 12–65%. It is the directly relevant reference class and it is thin. It moves the estimate; it does not pin it.

⚠️ **The deceleration cuts the same way:** −$15.77B (June) → −$7.69B (July). A third step of similar proportion lands near −$4B — branch B.

## 2. 🔴 A DEFECT IN ZHAO'S OWN KILL CRITERIA, FOUND BEFORE THE PRINT

The standing thesis-kill is **"Belgium <10% YoY on two consecutive prints AND China >$700B on three."** STATUS frames the Belgium leg as *"+10.6% — 1 pt above the <10% kill-leg,"* which reads as *Belgium must fall for this to trigger.*

**It does not. The leg fires on a base effect, with Belgium perfectly flat.** Belgium's 2025 path rose steeply from July into December ($425.4B → $451.1B → $463.6B → $465.5B → $481.0B), so the YoY denominator jumps from August onward. Holding Belgium at its actual July-2026 level of **$470.7B**:

| Print | 2025 base | YoY at a flat level | Kill-leg? |
|---|---|---|---|
| Aug-26 | $451.1B | **+4.35%** | ✅ prints |
| Sep-26 | $463.6B | **+1.54%** | ✅ prints |
| Oct-26 | $465.5B | +1.12% | ✅ prints |
| Nov-26 | $481.0B | −2.14% | ✅ prints |

**To stay ABOVE 10% YoY, Belgium would have to buy +$25.5B in August and be +$39.2B above the July level by September.** Its largest single-month net buy in the entire 42-month flow series is ~$17.6B. **Staying above the line is arithmetically close to impossible.**

⇒ **Both prints of the Belgium half of the kill condition are about to satisfy themselves, carrying no information about custody migration or Chinese behaviour.** The full kill will not fire — the other leg needs China >$700B for three prints and China is at $618.0B, $82B away — but anyone later reading *"Belgium kill-leg: 2 of 2 ✓"* would believe half a thesis-kill had been met on evidence. It was met on a denominator.

**Declared now, before the print, so it cannot be back-fitted:** when the Aug and Sep prints land, **the Belgium leg is to be recorded as SATISFIED-ON-BASE-EFFECT, not as evidence.** The leg needs re-specification — a level or a flow test, not a YoY — and that re-spec is **not** done in this letter, because changing a kill criterion in the same document that grades it is the back-fit this discipline exists to prevent. Raised separately. `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`

## 3. DECLARED OBSERVATIONS — recorded, NOT scored

Deliberately kept out of the branch map: a registered conjunction that fails one leg leaves the others scoreless, and then nobody writes them down (`[[finding_broken_conjunction_leaves_its_other_legs_unrecorded]]`). These are logged at the same session **whatever ZHA-18 grades**.

1. **Belgium** — level, net flow, YoY, and the §2 base-effect annotation. Not evidence in either direction on custody migration.
2. **rho(China, Belgium net sales)** re-run at n = 43. Proxy reinstates **only** at rho < −0.5 on a rolling 24m window (VX-ZHAO-1.09); it was +0.067 at n = 42.
3. **Agency line (Table 1).** Rotation was refuted twice; the test is whether Agency holdings RISE as Treasuries fall.
4. **Official vs non-official coupon split.** July reversed June (+$25.5B official / −$29.1B private). LIQUID's to price; ZHAO records it.
5. **Korea and Japan** LT/ST — routed to SAM and LIQUID, not scored here.

## 4. WHAT WOULD MAKE ME WRONG IN A WAY I SHOULD LEARN FROM

- **A is graded YES on a number like −$25B:** then the mean-reversion base rate was the wrong reference class for a policy-driven seller, and the conditional 3/9 should be replaced by a regime-split base rate.
- **B is graded NO on a number like −$4.9B:** the letter is right and nearly worthless — a 40% call resolving 100 bp from its own boundary says the threshold, not the forecast, did the work. Record that rather than bank it.
- **C (≥ +$5B):** the two-month duration-selling read was a portfolio event, and the TTM framing on this desk needs re-examining.

---

**Registered:** `workbook/PREDICTIONS.tsv` ZHA-18, 2026-09-18, 40%, Resolve_By 2026-10-23, anchor type = scheduled data release (fixed Treasury calendar). **Sources for every figure in §1 and §2:** TIC Table 3 (`slt_table3.txt`), pulled direct 2026-09-18.
