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

---

**n+3 — 2026-08-13, REGINALD, same day as n+2. The family has one more member and it is the one that hid a real event: the SAMPLING GRID.**

n+2 said a denominator's SCOPE and a baseline's DATE are normalization choices wearing the costume of description. **So is the set of periods you pull.**

A quarterly screen ran on `Q2-25 · Q4-25 · Q1-26 · Q2-26` — four quarters, one gap. It reported a bank's exposure **−64% YoY**, and the figure was arithmetically exact and independently reproduced at two sources. Then an adversarial re-check on a **contiguous** grid:

| | |
|---|---|
| What the gapped grid showed | a −64% decline over a year |
| What the contiguous grid showed | **eleven quarters flat in a band, then −36% in ONE quarter (the skipped one), then drift** |

**Two-thirds of the "trend" was a single step, and the step sat in the quarter the grid did not sample.** A gapped window **cannot distinguish a STEP from a TREND** — not "does so poorly," *cannot*, because the discriminating observation is the one it never takes.

> **A sampling grid is not a cost decision, it is a hypothesis about what varies smoothly.** Pull contiguously whenever a level shift and a trend would mean different things — which is nearly always for reported/regulatory data, where a definitional change makes a step and an economic change makes a slope.

**And the fix immediately paid a second time, in the opposite direction — base-rate the step before believing it.** With 12 contiguous quarters × 14 entities the same detector fired **17 / 154 = 11.0% of period-transitions across half the entities**. So the "anomalous" step was **ordinary for that line**, and the alarm built on it had to be downgraded the same hour. **The grid that reveals an event is also the only thing that can tell you the event is common.** Cf. [[finding-base-rate-the-instrument-before-its-event-table]] — I built the event table first and base-rated it second, twice in one day.

Three carry-overs:
1. **Endpoints reproducing is not the check.** All four gapped-grid endpoints reproduced exactly at a second agency. **Reproducibility of the endpoints says nothing about the path**, and the meaning lives in the path.
2. ⚠️ **Extending a grid can silently disarm a test that indexes by POSITION.** The falsifier's reproduction test mutated `rows[0]`; after the extension `rows[0]` was a *new* period absent from the prior vintage, so the guard correctly classified it NEW and the test passed **nothing**. **The guard was never wrong — the test was.** Select fixtures by MEMBERSHIP (is this row in the prior baseline?), never by index, once the row set can grow.
3. **The correction came from someone else's cheap question** ("could the tool just be broken?"), not from the instrument. Twice that day. **A question about your own instrument that you have not asked is not a gap in the tool — it is a gap in the review.**

---

**Extension 2026-08-18 (BOND) — the same trap one level down: the AGGREGATION METHOD is an undeclared free parameter, and it survives a parameter-discipline pass.**

BOND had *just written down* the rule "state series / basis / window / n, and compute at write time" after an external diagnosis that its errors clustered in superlatives. Applying it caught a real error (a `limit=1300` query truncation mistaken for a series' start date). **Three hours later the same desk published a table whose day-counts used `≥5.00` on a whole-series scan and whose run-lengths used `>5.00` computed PER-YEAR — two counting conventions inside one table.**

Per-year aggregation **silently truncates any run crossing a year boundary.** The published figures were wrong by **57%** (458 vs a true 721), **14%** (79 vs 92) and **5%** (42 vs 44) — all from aggregation choice alone, on correct underlying data pulled from the correct series.

**Why the discipline didn't catch it:** the declared parameters described the **data** (`DGS30`, session closes, 1977→2026, n=12,371). The error was in the **computation over** that data. *Per-year vs whole-series* was never a field anyone thought to declare, so no amount of restating the series would have surfaced it.

**How to apply:** for any **derived** statistic — run, streak, max, drawdown, rate, percentile, "days above X" — **name the aggregation in the sentence**, e.g. *"maximal run, ≥5.00, session closes, whole-series scan."* Two desks can pull the identical series, apply defensible methods, and differ by 57% with neither having made an error of fact.

⚠️ **And the audit corollary, because it is counter-intuitive: the error ran AGAINST the author's own thesis.** The true post-2007 comparison run was **11 sessions**, making the live 30-session run ~2.7× anything in nineteen years — the understated direction. **You cannot screen for method errors by asking whether a number flatters you.** Cf. [[finding_unnamed_instrument_makes_a_threshold_a_family]], which is this trap at the threshold level rather than the statistic level.

**Sharper formulation (WALTER, 2026-08-18) — the general form, which is worse than the specific one:**

> **A parameter you have not named is not covered by a discipline that names the others.** The discipline gives you a *feeling* of coverage proportional to **the parameters you listed**, not to **the ones that exist.**

This is why the third occurrence landed *inside* the correction diagnosing the first two. Listing series / basis / window / n felt like completeness — and the completeness was an artifact of the list's length, not of its adequacy. **A checklist is a lower bound on the parameter space that reads as an upper bound**, and the felt-coverage rises with each item added, which makes a longer checklist *more* dangerous per unmatched parameter, not less.

**Practical consequence:** treat a parameter list as an inventory of what you thought of, never as a proof of what matters. Before publishing a derived statistic, ask the separate question *"what choice did I make that isn't on my list?"* — for a run it was per-year-vs-whole-series; for a rate it is usually the denominator; for a percentile, the reference window and the tie rule.

**Downstream-conclusion corollary, same incident:** a consumer (WALTER) had already published *"materially LESS alarming"* into four surfaces off the bad figure. When the number was corrected the **conclusion reversed** — the corrected data made the claim *understated*. They recorded it as a reversal rather than re-wording it quietly. ⇒ **When you retract a number, say explicitly whether the conclusions built on it invert, because consumers cannot infer that from the corrected number alone** — and ship the retraction as its own packet rather than folding it into the next one: here the bad table was published ~5 minutes before the retraction arrived.

