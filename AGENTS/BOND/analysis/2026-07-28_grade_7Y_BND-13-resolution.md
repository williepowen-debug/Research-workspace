# BOND — 7/28 7Y auction grade · BND-13 resolution

**Written:** 2026-07-28 ~14:35 ET — **AFTER the 1:00PM print.**
**Graded against:** `analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md` §4, **FROZEN ~03:00 ET, ~10h pre-print**, registered as `BND-13`. **§4 was not edited.**
**Primary source:** TreasuryDirect TA_WS `/securities/Note` + `/securities/auctioned`, CUSIP **91282CRC7**, pulled 2026-07-28 ~14:30 ET. TD record `updatedTimestamp` **2026-07-28T13:03:18**. Competitive results PDF `R_20260728_2.pdf`.
**Denominator:** all percentages are **% of competitive accepted** — the fleet-reconciled basis. ⚠️ **No number in this memo is ported from the MATRIX_V2 backtest**, which is of-offering (see §4).

---

## VERDICT — one line

**BND-13 CONFIRMED. Branch B (POLICY-PATH HOLDS) fires. No composition failure at the 7Y; the frozen gate and the backtest-aligned standalone read AGREE.** Auction health **VX-BND-01 reverts 3 → 2** on its own registered condition. **Composite 13 → 12/35.** No TLT add-gate fired.

---

## 1. The primary (verified — supersedes all wire summaries)

**7-Year Note · 91282CRC7 · auction 2026-07-28 · $44.0B offering · single-price · issue 7/31/26 · maturity 2033-07-31**

| Field | Value | Source |
|---|---:|---|
| Offering amount | **$44,000,000,000** | TD 7/28 |
| Competitive tendered | $109,314,764,000 | TD 7/28 |
| **Competitive accepted** *(denominator)* | **$43,909,474,000** | TD 7/28 |
| **Bid-to-cover** | **2.49** | TD 7/28 |
| **High yield** | **4.4730%** | TD 7/28 |
| Low / median yield | 4.300% / 4.405% | TD 7/28 |
| Coupon / price | 4.375% / 99.416549 | TD 7/28 |
| Allocation at high | 95.17% | TD 7/28 |
| **Indirect accepted** | $30,801,964,000 = **70.15%** | TD 7/28, computed |
| **Direct accepted** | $7,413,000,000 = **16.88%** | TD 7/28, computed |
| **Primary dealer accepted** | $5,694,510,000 = **12.97%** | TD 7/28, computed |
| SOMA add-on (outside offering) | $4,864,689,800 | TD 7/28 |

*Arithmetic check: 70.15 + 16.88 + 12.97 = 100.00 ✓. Competitive accepted $43.909B + noncompetitive $0.091B = $44.000B = offering ✓ (SOMA is an add-on, correctly excluded).*

**vs the prior 7Y (6/25/26, 91282CQW4, same $44B — no size artifact):**

| | 6/25 | **7/28** | Δ |
|---|---:|---:|---:|
| BTC | 2.50 | **2.49** | −0.01 |
| Indirect | 57.55% | **70.15%** | **+12.60pp** |
| Direct | 29.70% | **16.88%** | **−12.82pp** |
| Dealer | 12.75% | **12.97%** | +0.22pp |
| High yield | 4.260% | **4.4730%** | **+21.3bp** |

**Trailing-12 7Y benchmarks (the 12 auctions 2025-07-29 → 2026-06-25, all $44B), recomputed today and identical to the frozen §4 figures:** median BTC **2.495** · median indirect **60.65%** · median dealer **11.28%**; min BTC **2.40** · min indirect **56.42%** · max dealer **13.14%**.

| Metric | Print | vs trailing-12 median | vs the frozen bar |
|---|---:|---:|---|
| BTC | 2.49 | **−0.005 (dead on median)** | not <2.45, not <2.40 |
| Indirect | 70.15% | **+9.50pp** | **+13.73pp above the 56.4% bar** |
| Dealer | 12.97% | +1.69pp | **0.032pp below the 13.0% bar** ⚠️ |

---

## 2. §4 graded EXACTLY as frozen

| Branch | Frozen condition | Print | Fires? |
|---|---|---|---|
| **A. TERM-PREMIUM CONFIRMED** | indirect <56.4% **AND** dealer >13.2% | 70.15% / 12.97% | ❌ **NO** — both legs fail, indirect by 13.73pp |
| **B. POLICY-PATH HOLDS** | indirect ≥58% **AND** dealer <13% | 70.15% ✓ / 12.97% ✓ | ✅ **YES** |
| **C. AMBIGUOUS / FOMC-eve confound** | BTC <2.45 with ind ≥58% and dlr <13% | BTC **2.49** | ❌ NO — BTC leg fails |
| **D. GENUINE DEMAND HOLE** | BTC <2.40 AND ind <56.4% AND dlr >13.2% | — | ❌ NO — all three fail |
| **Tie-break** | ind 56.4–58% with dlr 13.0–13.2% ⇒ grade C | ind 70.15% | not triggered |

⇒ **BRANCH B. `BND-13` resolves CONFIRMED** (registered at 85%).

**The 7Y tail is not graded and did not enter any branch** — TreasuryDirect publishes no when-issued yield, so it is unscoreable by construction. If a wire prints a 7Y tail today it is `[med-conf, wire]` and may not move this verdict.

### 2b. ⚠️ Two defects in the frozen spec, found at resolution — reported, not repaired

**(i) The dealer leg cleared by 0.032pp.** 12.968% vs a 13.0% bar. That is a rounding-level margin on a binary branch condition. Stated plainly so nobody reads B as having fired comfortably on both legs: **it fired comfortably on indirect and by a hair on dealer.**

**(ii) §4's branches are NOT exhaustive — there is a coverage hole, and today landed 0.03pp from falling into it.** Had dealer printed 13.05% with indirect at 70.15%: A needs indirect <56.4% (fails), B needs dealer <13% (fails), C needs BTC <2.45 (fails), D fails, and the tie-break only covers indirect 56.4–58%. **No branch would have fired and BND-13 would have been unresolvable.** This is the same defect *class* as the tail problem and the hard-to-fire problem — a pre-registration whose failure mode is "cannot grade" rather than "grades wrong." Logged for v1.1.4: **every future pre-registration must include an explicit residual branch.** I am not editing §4 to patch it; it graded as written.

---

## 3. Secondary read — the indirect leg STANDALONE (backtest-aligned, per §4b / KB-BND-094/095)

**⚠️ Denominator discipline applied.** The MATRIX_V2 backtest's indirect thresholds are **of-offering**; every threshold on BOND's surfaces is **of-competitive-accepted**. Per my own ~05:15 amendment, **I did not port the backtest's numbers.** I ported its *rule* — "per-tenor 15th percentile of trailing-12, sufficient alone" — and **recomputed the cut-off inside my own denominator** from the TD series.

| Standalone test | Bar | Print | Result |
|---|---:|---:|---|
| Indirect < trailing-12 **min** (the frozen §4 bar) | 56.42% | **70.15%** | ❌ no fire, by **13.73pp** |
| Indirect < trailing-12 **15th percentile** (the backtest's looser rule, computed of-competitive-accepted) | **57.24%** | **70.15%** | ❌ no fire, by **12.91pp** |

**⇒ NO DISAGREEMENT TO REPORT.** The frozen gate and the backtest-aligned standalone read reach the **same verdict**, and the standalone read — which the backtest calls "the single best signal" — reaches it by a wider margin than the gate does. The gap between the two bars is **0.82pp**; the print clears both by ~13pp. **The known specification defect is non-binding on today's print.**

**Honest counterweight — I am not overselling 70.15%.** It ranks **#17 of 50** in the full 7Y window (67th percentile), not a record; the series high is 87.88% (12/26/24). The 7Y indirect series is visibly **bimodal** — a ~56–63% cluster and a ~77–78% cluster — and 70.15% sits *between* the modes, above every member of the low cluster. Correct label: **strong, top third, not exceptional.**

**⚠️ And the strongest caveat cuts against my own headline.** The "+12.60pp indirect surge" **overstates the change in real end-user demand**, because directs fell almost exactly as much (−12.82pp). The indirect/direct split is subject to **bidder reclassification** — the same real money can bid through a dealer (counted indirect) or directly. What is robust:

- **End-user take (indirect + direct) = 87.03%, vs 87.25% on 6/25 — flat.** The entire composition move happened *within* the end-user bucket.
- **Dealers absorbed 12.97%, vs 12.75% in June, below the trailing-12 max 13.14% — no warehousing.** This is the leg that cannot be reclassified away, and it is the one branch A/D key on.
- **Gross demand was normal:** competitive tendered **$109.3B** vs trailing-12 median **$109.6B**.
- **Dealer hit-rate 9.27%** (they tendered $61.4B, took $5.7B) vs trailing-12 median 8.10% — dealers bid a full backstop and were *not needed*; **indirect hit-rate 85.59%** vs median 82.42%, i.e. indirect bid aggressively enough to get filled.

⇒ The defensible claim is **"no composition failure — dealers not stuffed, end-user take flat and high, cover at median, concession paid in price (+21.3bp)."** Not "foreign piled into duration."

---

## 4. Bias disclosure — which side of it this landed on

**My §4 is biased toward NOT firing** (my own finding, KB-BND-094/095): the bar was set at the trailing-12 *minimum* rather than the 15th percentile, and the indirect leg was made *conjunctive* with a dealer leg the backtest says is **wrong-signed** as bearish. **Today's print landed on the NO-FIRE side — the weak-evidence side.** HENRY has been told to discount a no-fire, and that instruction stands.

**But the discount is calibratable, and it should not be applied uniformly:**

| Leg | Margin | Does the known bias explain it? |
|---|---|---|
| **Indirect** | clears the frozen bar by **13.73pp**, and the *looser* backtest-aligned bar by **12.91pp** | **No.** The bias is a **threshold-placement** error worth **0.82pp** (min 56.42 vs 15th-pctile 57.24) — roughly one observation. It cannot manufacture a ~13pp margin. The indirect reading is an **affirmative positive that is independent of where the threshold sits**, not a marginal non-fire. |
| **Dealer** | clears by **0.032pp** | **Yes, fully.** This is genuinely knife-edge and the discount applies at full weight — but this is the **wrong-signed** leg, and *dropping* it (as the backtest advises) makes B fire on indirect alone, more cleanly. |

**⇒ Net for HENRY's calibration: discount the GATE's verdict, do not discount the INDIRECT MEASUREMENT.** A fire would have been stronger evidence than this no-fire; but this particular no-fire is not the weak kind the bias warning was written for, because the binding leg is ~13pp from any plausible placement of its threshold. **I would have graded B under the corrected v1.1.4 rule too.**

---

## 5. The third hypothesis — basis-trade shrinkage (KB-BND-092, **ESTIMATE class, LIQUID owns it**)

**Registered test** (SCRATCH 7/28): *if repo-levered basis-trade withdrawal is the driver, cover stays thin **with composition intact** and does **not** resolve post-FOMC.*

**Today bears on it, and I am reporting the observation, not adjudicating it.**

Normalizing each auction against **its own** tenor's trailing-12 median (BTC levels are not comparable across tenors):

| | 5Y 7/27 | 7Y 7/28 |
|---|---:|---:|
| BTC | 2.28 | 2.49 |
| own trailing-12 median | 2.340 | 2.495 |
| **Δ vs own median** | **−0.060** | **−0.005** |
| own trailing-12 min | 2.29 | 2.40 |
| vs own min | **BELOW — a new trailing-12 low** | comfortably inside |

**The thin cover did not persist to the next auction** — 24 hours later, in a **longer** tenor, cover printed dead on its own median with gross demand normal ($109.3B vs $109.6B median). A *general* withdrawal of a repo-levered bid across the belly would not stop at the 5Y and skip the 7Y one day later. **The observation is 5Y-specific.**

**This cuts the same way against the FOMC-eve event-risk confound** (branch C's rationale): the 7Y priced **24h closer** to an untelegraphed two-sided FOMC and **2 years longer** in duration. If event-risk premium explained the 5Y's thin cover, the 7Y should have been at least as thin. It was not. **Branch C did not fire, so I am not deferring — and the confound's own logic is now weakened by direct evidence.**

**→ Routed to LIQUID as an observation.** Whether this is 5Y-specific basis positioning, a 5Y auction-size effect ($70B vs $44B), or something else is **LIQUID's call, not mine.** I own the composition read; I do not own repo.

---

## 6. Write-back consequences (all pre-registered — no threshold moved)

| Surface | Change | Registered where |
|---|---|---|
| **VX-BND-01 Treasury auction health** | **3 → 2** | STATUS matrix, written pre-print: *"→4 if the 7/28 7Y hits pre-reg branch A or D. **Reverts to 2 on branch B.**"* Branch B fired. |
| **Composite** | **13 → 12/35** | arithmetic: 2+2+1+2+3+1+1 |
| **VX-BND-05 / matrix "Long-end / duration"** | **unchanged at 3** (VX-05 stays 4) | its auction leg required *"a composition failure at the 7/28 7Y"* — did not occur. The unconditional path to 4 remains **DFII10 >2.5 sustained**, still **7bp away** (2.43 [FRED, 7/24]; 7/27–28 not yet posted). |
| **TLT puts gate (c)** | **DID NOT FIRE** | *"composition failure at the 7/28 7Y = indirect <56.4% AND dealer >13.2%"* — 70.15% / 12.97%. **HOLD, no add.** Will's 7/16 NO-ADD stands. |
| **HEN-42 CONFIRM (7/23)** | **not downgraded** | downgrade was conditional on branch A or D. |
| **BND-13** | **CONFIRMED** | resolve in PREDICTIONS.tsv |

**⚠️ Spec note logged, NOT acted on: the VX-01 revert rule may be too fast.** One benign auction fully undoes a marker fired the previous day, on a vector meant to track a *state*. The 5Y BTC 2.28 remains a true, logged historical fact (KB-BND-089) regardless. But the revert **is** registered and it grades as written — flagging the rule for v1.1.4 review is the correct move; quietly declining to revert because I dislike the result is not.

**Market reaction (context, not a graded input):** ^TNX **4.602** vs prev close 4.657 (−5.5bp), TLT **$84.22** vs prev close $83.66 [yfinance, 7/28 ~14:30 ET] — the pre-FOMC bid deepened through the auction. Consistent with a firm clear; not evidence I am grading on.

---

## 7. v1.1.4 carry-forward (adopted AFTER this grade, so it cannot be accused of being fitted to the print)

1. **Indirect at the per-tenor 15th percentile of trailing-12, SUFFICIENT ALONE** — computed in the of-competitive-accepted denominator, never ported from the of-offering backtest.
2. **Drop dealer as a bearish leg**; retain it only as a contrarian note (>18%).
3. **BTC confirmatory only**, never a gating leg.
4. **Every branch set must include an explicit residual branch** — §2b(ii) is the reason.
5. **State the margin on every leg at resolution.** "B fired" and "B fired by 0.032pp on one leg" are different facts and only one of them is honest.
