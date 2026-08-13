---
name: finding-normalization-choice-picks-opposite-winners
description: "Absolute-change and proportional-change lenses can name OPPOSITE winners off the exact same numbers, so 'X led the move' is unfalsifiable unless it states its normalization. Require a real signal to register on BOTH; when the two disagree, the disagreement IS the finding — grade it as no-clean-signal, not as whichever lens flatters the thesis."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 5326c084-a5ab-4d66-9293-f42709ed8d2f
  modified: 2026-07-27T18:23:09.173Z
---

Given a fixed set of levels moving together, **which component "led" depends entirely on the normalization you pick, and the two standard ones routinely disagree.**

**Worked instance (BROCK, 2026-07-27, HY tranche OAS, FRED/ICE BofA).** Two-session move 7/22→7/24:

| | Δ bp | Δ % of own level |
|---|---|---|
| HY | +11 | +4.10% |
| BB | +11 | **+7.01%** ← largest |
| B | +11 | +3.86% |
| CCC | **+15** ← largest | +1.53% |

**Absolute bp says CCC led. Proportionally BB moved 4.6× more than CCC.** Opposite winners, same four numbers. A fleet claim of "parallel widening / CCC-led" was an **absolute-bp artifact**; the proportional read said the move was high-quality-led, i.e. rates/beta rather than credit-quality repricing.

**The operational rule that fell out of it:**

> **A real signal registers on BOTH normalizations. When they disagree, the disagreement IS the finding — grade it "no clean signal," never "bear on the lens that agrees with me."**

Use a **ratio/dispersion** test as the tiebreak, because it is normalization-free in the direction that matters: quality-recognition *expands* the risky/safe ratio. In the instance above the CCC/BB ratio **compressed** 6.25×→5.93× across exactly the sessions that produced the whole move ⇒ beta, not recognition. Note the levels-gap and the ratio can also disagree (CCC−BB gap widened 807→828 while the ratio went 5.98→5.93) — that is the same trap one layer up, and it resolves the same way: **both, or neither.**

**Generalizes to** any decomposition where components sit at very different levels — credit tranches, sector spreads, regional NCO/DQ rates, index constituents, cohort delinquencies, YoY vs pp comparisons. **The bigger the level dispersion between components, the more violently the two lenses diverge** (BB at 157bp vs CCC at 981bp is a 6× level gap, which is why +11 vs +15 flipped to +7.01% vs +1.53%).

**Hygiene:** every "X led the move" claim — yours or an inbound one — must carry its normalization, or it cannot be checked and should not be propagated. This is a *stated-method* requirement, not a preference.

---

**n+1 — 2026-08-03, PROME. The same defect in a PASS/FAIL gate, where it is worse: the free parameter was a strike, and the wrong choice reported a gate as UNSATISFIABLE.**

BRENT's DEPLOY GATE v2 leg (b) = *net debit ≤ 33% of spread width on a live chain*, spec'd as long **~5% OTM** / short **~12–15% OTM**. I took that band, did the arithmetic off spot, landed on **USO Oct-16 127/138**, and reported leg (b) **FAILS at 33.6% paying the spread** — "MARGINAL, a coin-flip on execution." That number went to BRENT and TERRY as the answer to *"can this gate be satisfied at all?"*

It was a fact about my strikes, not about the gate:

| Structure | Long/short OTM | Width | At MID | Paying FULL spread | Open interest |
|---|---|---|---|---|---|
| 127 / 138 *(mine)* | 3.7 / 12.7% | $11 | 26.6% | **35.0% FAIL** | **93 / 263** |
| 130 / 140 | 6.2 / 14.4% | $10 | 23.5% | **29.5% PASS** | **5,924 / 7,292** |

**The arithmetic centre of a moneyness band is not where the market is.** USO's open interest sits on round numbers; strikes between them quote wide because nothing trades there. I had computed a *liquidity* penalty and reported it as a *gate* verdict — and it pointed at "don't bother," the conclusion that requires no further work.

**The rule, extending the one above:**

> **Before reporting any pass/fail computed off a free parameter, VARY the parameter.** If the verdict flips across reasonable settings, the verdict is about your choice — say so, show the range, and let the owner pick. For anything priced on a chain, **liquidity picks the strike, not arithmetic**: check open interest before quoting a debit.

Two sharpeners specific to the gate case, which the "led the move" instance above does not have:

1. **Pass/fail hides the disagreement that a ranking exposes.** "CCC led" invites "by which lens?"; "leg (b) fails" sounds like a property of the world. **A binary verdict launders a parameter choice into a fact** — so the both-or-neither rule needs stating *louder* here, not less.
2. **Check which way your default flatters you.** I picked the more permissive *tenor* earlier the same day (Sep-18 over the ratified Oct-16) and the more punitive *strikes* an hour later — inconsistent, and each error pointed at the answer needing less work. **Audit defaults for direction, not just correctness** — cf. [[finding-deliberate-and-unnoticed-asymmetry-look-identical]].

Cost: the correction reached BRENT 22 minutes before the close, and had it not, its gate grade would have carried a leg-(b) verdict that was the opposite of true.

Distinct from [[finding-composition-mask-unmask-discriminator]] (there the *reporting entity* manages the base to hide deterioration; here nobody is hiding anything — the *analyst's* lens choice manufactures the conclusion). Related: [[finding-number-carries-threshold-unit-source]], [[finding-blended-index-masks-bifurcation]], [[finding-level-vs-monthly-average-cpi-landing]].

---

**n+2 — 2026-08-13, REGINALD. TWO more instances in one session, and they extend the family in a direction the first three don't cover: it is not only the LENS (absolute vs proportional) or a free PARAMETER (strike) — the *denominator's SCOPE* and the *baseline's DATE* do it too, and both look like description rather than choice.**

**(a) Denominator SCOPE — a cross-bank screen where the basis picks a different #1.** MI3 "hidden CRE" = FFIEC `RCON2746`, whose own label says its balance sits in RC-C **items 4 AND 9**. The legacy screen divided by **item 4 only**. Re-run at primary, 14 banks × 4 quarters, Q2-2026:

| Rank | ÷ item 4 (legacy) | ÷ item 4 + item 9 (the numerator's own parent) |
|---|---|---|
| 1 | **WAL 21.20%** | **EGBN 10.77%** |
| 3 | MTB 14.45% | **WAL 8.99%** |
| 4 | **EGBN 12.44%** | CUBI 5.96% |

**WAL is #1 on one basis and #3 on the other; EGBN is #4 and #1.** Mechanism is pure arithmetic: the item-9 share of the base runs **5.5% → 65.8%** across the cohort (WAL 57.6% vs EGBN 13.4%), so the narrow denominator inflates WAL ~2.4× *relative to EGBN specifically*. A three-year-old fleet claim — "*bank X is the most concentrated / growing fastest in cohort*" — turned out to be a claim about the denominator.

**(b) Baseline DATE — the same defect inside my own attribution, found one day after I published it.** A tripwire fired and its mandatory driver-decomposition said **CCC-widening-LED** (the escalation case) rather than HY-tightening-led (benign beta):

| Baseline | CCC | HY | Read |
|---|---|---|---|
| **7/16** (the date my rule names) | +53bp (+5.5%) | +1bp (+0.4%) | **CCC-LED — escalation** |
| **7/30** (last close before the fire run actually began) | +17bp (+1.7%) | **−12bp (−4.2%)** | **~73% of the ratio's rise is HY TIGHTENING — benign beta** |

Same instrument, same fired gate, opposite mechanism. **The correction was only reachable because a peer desk questioned my *fire dates*** — the run had begun 7/31, not 8/7, and finding the true start handed me a second defensible baseline I had never computed.

**What the two add to the rule above:**

> **A denominator's SCOPE and a baseline's DATE are normalization choices wearing the costume of description.** "MI3 ÷ C&I" and "vs the 7/16 baseline" both read as *definitions*, not *settings* — which is exactly why nobody varies them. **Vary them anyway, and report both.**

Three sharpeners:
1. **Prefer the basis the numerator itself names.** `RCON2746`'s FFIEC label literally says "items 4 and 9." The defective denominator was *contradicted by the field's own definition* for three years. **Read the instrument's own label before trusting an inherited recipe** — cf. [[finding-read-the-artifacts-own-header-first]].
2. **A gate's baseline should be the gate's own event boundary, not a fixed calendar date.** A decomposition measured from an arbitrary prior date silently mixes pre-event drift into the event. Compute from the run's own start *as well*; if they disagree, that IS the finding (the parent rule, one layer up).
3. ⚠️ **Ratio-vs-dollars is the same trap and it inverted the substantive conclusion.** The cohort's *ratios* collapsed at the concentrated names — but the **dollars** told a different story: OZK −64% YoY and EGBN −38% while **HBAN +100%, BKU +193%, MTB +16% to $4.95B, the largest absolute book in the cohort while ranking as an unremarkable ratio** because its denominator is enormous. **A ratio screen structurally cannot see a book migrating up-cap.** Report level AND ratio, always — cf. [[finding-spread-metric-blind-to-common-mode]], [[finding-rising-stock-flat-inflow-means-slower-outflow]].
