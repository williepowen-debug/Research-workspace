# SIGNAL COMBINATION / ALPHA-WEIGHTING — extracted claims + applicability grades
**Created:** 2026-07-26 · **Owner:** TERRY · **Tier:** EXTRACTED CLAIMS (middle tier)
**Source:** `sources/2026-07-26_roan_combining-50-weak-signals.docx.txt` — X/Twitter long-post, author "Roan," self-described backend dev (HFT-style execution, prediction markets). Saved by Will 7/26.

**Pipeline (mirrors `options/`):** `sources/` (raw) → **this file (claim + applicability grade)** → an adopted rule in `RISK_RULES.md` / `RISK_SCORING.md`. **Nothing here is a TERRY rule until promoted.** A claim reaching this file has been *read and graded*, **not verified**.

**Applicability grades** are always *for THIS desk* — low-breadth, discretionary-with-rails, long-premium, catalyst-driven, $500 max loss/card, ~1 fired card of history.

> **⚠️ Standing source-quality flag.** This is **content marketing**, not research. Structural tells: "Bookmark This," "DMs are open," "drop your answer in the comments," and three unfalsifiable authority claims with **zero citations** — *"institutional research covering over 550 formulas," "151 systematic trading strategies," "400 million Polymarket trades."* None is traceable. Same treatment as the tastytrade rows: **the underlying mathematics is real and checkable independently; the document's authority claims are not evidence.** Grade the math, discard the texture.

---

## The one-paragraph verdict

**The core mathematics is real and well-established — it is Grinold & Kahn's Fundamental Law of Active Management, correctly stated.** But almost nothing operational transfers: the 11-step engine needs a realized-return panel this desk does not have and will not have for quarters, and one of its two sizing prescriptions would **loosen** discipline we already hold. **The document's single valuable idea is `SC-03` — that the N in the Law is the *effective independent* count, not the signal count, and that sizing to believed-N when effective-N is smaller is the specific mechanism behind "right thesis, big loss."** That idea is not new to us: **NEXUS's Discipline F is the same insight**, and I applied it twice this week without a name for it. What the document adds is **a name, a mechanism, and an uncomfortable worked example that is already sitting in Will's book** (§ Worked example). **Adopt one thing, reject one thing, ignore the engine.**

---

## Claim grades

| ID | Claim | Applicability to THIS desk | Notes |
|---|---|---|---|
| **SC-01** | **Fundamental Law: IR = IC × √N.** Combined risk-adjusted edge scales with the square root of the number of independent signals. | **CONTEXT — true, and it indicts our design honestly** | Real, and it long predates this author: **Grinold & Kahn, *Active Portfolio Management***. Standard form is **IR = IC × √BR**, where **BR = independent bets per year** — a subtlety the document drops, and it matters more to us than to anyone. **This desk makes perhaps 10–15 independent decisions a year.** At IC 0.10 that caps IR near **0.32** no matter how good the process is. **The honest implication is structural: breadth is not available to us, so our edge must come from payoff *asymmetry* — cheap convexity on dated catalysts — not from signal count.** That is exactly what this desk already does. The Law validates the shape *and* warns we should never expect a smooth equity curve from it. |
| **SC-02** | Real institutional signals run **IC 0.05–0.15**; the best are wrong most of the time. | **CONTEXT (calibration anchor)** | Honest and consistent with the literature — the doc's most useful sentence is that a *good* signal is barely better than a coin flip. Its homework question lands squarely: **no one on this desk has ever measured the IC of anything.** That is precisely what `PAPER_BOOK.tsv` was built to eventually permit, and why its **N≥10-closed-per-lane** scoring gate is correct rather than over-cautious. **This claim independently validates the paper-book design.** |
| **SC-03** | ⭐ **The N in the Law is the number of *effective independent* signals after shared variance.** "Running 50 correlated signals gives you the diversification benefit of perhaps 10 to 15." A PM who believes she runs 20 independent signals may be running **6**. Position sizes justified by 20 views are **far too large for 6** — and that leverage mismatch is the mechanism behind most systematic blowups where the trader was **right in direction, wrong in sizing**. | **⭐ ADOPT — formalizes something we already hold qualitatively; see § Promotion** | **The highest-value row in this file, and the only one worth acting on.** We already run this: **NEXUS's Discipline F** ("oil + term-premium + hot-CPI are ~ONE Hormuz spine, ONE shared falsifier — do NOT score them as three independent break votes") is the same insight, arrived at independently. I applied it twice **this week**: the 7/16 flag on a *"~$1,650 thesis concentration with a SHARED Hormuz-de-escalation falsifier across the rates-short AND oil-long books,"* and on today's VIX card — *"the whole differential is one inference deep."* **What we lack is a number.** We state independence in prose and then size by leg count. See § Worked example for what that has already cost. |
| **SC-04** | The **11-step combination engine** — demean → normalize by σ → cross-sectionally demean → residualize expected return against the common component → weight `w(i) = η·ε(i)/σ(i)` → normalize to Σ\|w\|=1. | **NOT-APPLICABLE (data-starved) + rigor flags** | **The idea is sound** — it is orthogonalization plus inverse-volatility weighting, a standard construction. **It is un-runnable here.** Step 1 requires, for each signal, a **realized return series across M periods**. We have **one fired card (N=1)**, two open paper rows, and a self-imposed rule that nothing is scored until **10 closed rows per lane**. Running an 11-step optimizer on that would fit noise with great precision. **Two rigor flags on the write-up itself:** (a) Steps 5 and 7 claim that *dropping the most recent observation* "ensures the weight calculation uses only historical out-of-sample data" — **it does not**; out-of-sample requires a holdout or walk-forward, and dropping one row prevents nothing. (b) Step 9's spec — *"regression of E_normalized over Λ without an intercept, using unit weights"* — is **garbled as written**; the intent (residualize against the common factor) is clear, the specification is not reproducible. |
| **SC-05** | **Empirical Kelly: `f = f_kelly × (1 − CV_edge)`**, where CV_edge comes from 10,000-path Monte Carlo. | **🔴 REJECT — adopting it would LOOSEN existing discipline** | **This is a trap and it must not be quietly absorbed.** `RISK_SCORING.md` §3 already sets a hard **0.25× Kelly cap** and says *"if edge estimate is uncertain, shrink aggressively or mark NO TRADE."* His formula at a plausible CV_edge of 0.5 yields **0.5× Kelly — twice our existing ceiling.** It only becomes more conservative than our cap at CV_edge > 0.75. **Dressed in Monte-Carlo language it reads more rigorous while being materially more aggressive.** The shrinkage *direction* is right and already ours; the *level* is a downgrade. Keep the 0.25× cap. |
| **SC-06** | Prediction-market application: combine implied-probability signals, then **edge = combined estimate − market price**, sized by empirical Kelly. | **NOT-APPLICABLE — already superseded in-house, and wrong lane** | His "edge" is the **gross** number. `RISK_SCORING.md` §7 already requires `tradeable_edge = edge − spread − fees − liquidity discount − resolution-risk discount − model-uncertainty discount`, and states *"if tradeable_edge ≤ 0, no trade."* **Our existing framework is strictly stronger than the one being sold here.** Separately: **ORACLE owns prediction markets**, not TERRY, and auto-memory `finding_thin_liquidity_prediction_market_discipline` already governs the venue. Nothing to import. |
| **SC-07** | *(TERRY-derived, not his claim)* **The document's Part 4 refutes its own Part 1 headline.** | **CONTEXT (rigor flag)** | Part 1 sells "50 signals at IC 0.05 → **IR 0.354**, 3.5× better than one signal at IC 0.10." Part 4 then concedes that **50 correlated signals deliver the benefit of "perhaps 10 to 15."** Substituting his own effective-N: **IR = 0.05 × √12 ≈ 0.17**, which is *not* 3.5× a single 0.10 signal — it is **1.7×**. **The headline number is the fully-independent case the author himself says never occurs.** Real edge remains, but half the advertised size. Anyone quoting "3× better" is quoting the brochure. |

---

## ⭐ Worked example — SC-03 is not hypothetical; it is the largest loss in the book

The document's sharpest sentence: *"They believed they had three independent reasons to be confident. They had **one reason expressed three times**, at a size justified for three."*

**That is a precise description of the regional-bank put basket.** From the 7/24 position snapshot:

| Leg | P/L | Dies if… |
|---|---|---|
| KRE 60P (4 lots) | ≈ **−$2,225** | regional-bank credit doesn't crack |
| OZK 45P/42.5P Aug-21 | ≈ **−$1,641** | regional-bank credit doesn't crack |
| WAL 70P + 67.5P Sep-18 | ≈ **−$1,425** | regional-bank credit doesn't crack |
| **Total** | **≈ −$5,291** | **one antecedent** |

**Claimed legs: 3. Shared falsifier: 1. Effective N ≈ 1.2** (OZK carries idiosyncratic RESG/CRE concentration and WAL the $99M life-sci credit, so not *quite* 1.0 — but nowhere near 3). **It was sized as three.**

**Two honest caveats, because hindsight is cheap:**
1. **Expressing one thesis three ways can be legitimate** — it diversifies *idiosyncratic timing and single-name defense*, which is real. The error is not the three legs; it is **sizing as though three legs were three independent views.**
2. **The realized loss came primarily from tenor/depth, not from correlation** — that was already diagnosed on 7/17 (Part B: a slow-GRIND thesis expressed with deep-OTM CRASH instruments; KRE 60 = 0% empirical 3-yr reachability). **SC-03 is a second, independent mechanism operating on the same basket, not a replacement for that finding.** Correlation set the *size*; tenor/depth set the *decay*. Both were live.

**This is why the row is worth adopting.** We have the concept (Discipline F) and we still sized to leg count. A concept applied in prose to *theses* and not to *dollars* is not yet a control.

---

## Promotion recommendation — ONE change, deliberately small

**Do NOT build the engine.** Do not import the Kelly formula. **Add one field.**

**Proposal — `EFFECTIVE-N` line, mandatory in the §9 concentration block of every card:**

```
Claimed corroborating legs:  N_claimed
Shared antecedent(s):        [the single event/fact that kills more than one leg]
EFFECTIVE N:                 N_eff   (state the reasoning in one line)
Sizing reference:            size to N_eff, never to N_claimed
```

**Why this and nothing more:**
- It is **free** — no data, no backtest, no optimizer. It is a question, asked at build time, in a block that already exists.
- It converts a discipline we already believe into a **number that constrains sizing**, which is where it failed.
- It is **falsifiable at fire-time**: if the card says `N_eff = 1` and the sizing implies three independent views, the mismatch is visible on the page before Will sees it.
- It costs nothing when N_eff = N_claimed, and it is loud exactly when it should be.

**Live test — today's VIX card already passes.** Its §5 states the position is genuinely additive (equity-vol axis vs 004 rates-vol / USO-XLE oil / bank-credit), and §7 concludes *"the entire differential is one inference deep — HENRY's gamma read."* **That is `N_eff = 1` stated in prose, and it is exactly why I sized it at $300–400 instead of the $500 cap.** The field would have made that arithmetic explicit rather than implicit. **The discipline is already working; it is just not written down as a number.**

**Status: ✅ ADOPTED 2026-07-26 (Will: "wire in the EFFECTIVE-N field"). WIRED — 5 surfaces:**

| Surface | What landed |
|---|---|
| `TRADE_CARD_TEMPLATE.md` | new **§6a EFFECTIVE-N** block, *mandatory before sizing* (placed in the risk section, where it binds) |
| `TRADE_CARD_TEMPLATE_FIRE.md` | **ZONE 1** field (pre-derivable at build, not at fire) + **ZONE 3** checklist line |
| `RISK_SCORING.md` §1 | Pre-Trade Risk Checklist gains an **Independence** row |
| `RISK_SCORING.md` **§2b** | the rule itself + the worked example + **two limits on over-application** |
| `RISK_SCORING.md` §3 | 🔴 **SC-05 explicitly rejected at the rail** — the 0.25× Kelly cap takes precedence over any external Kelly adjustment |

**Numbered rules #1–#8 deliberately untouched** — they are a stable API cited by fire cards ("rule #6") and must not churn.

**First live application: the VIOLET VIX card** (`setups/VIOLET_prefomc-vix-callspread_2026-07-26.md` §5). Result on debut — `N_claimed = 3`, **shared antecedent = the gamma sign flip**, **`N_eff = 1`**. Legs (ii) vol-channels-at-highs and (iii) catalyst-stack **were also present in all five prior absorptions**, so they are the *setting*, not independent votes. Sizing to `N_eff = 1` justified the $300–400 (below the $500 cap) that I had already chosen on instinct — **the field converted a buried judgement call into a visible number.** That is the whole point of it.

---

## What we should NOT take from this

1. **The 11-step engine.** Data-starved by two orders of magnitude. Revisit only if the paper book ever clears its N≥10-per-lane gate *and* we are running enough repeatable signals for a return panel to exist. Realistically: not this year.
2. **`f = f_kelly × (1 − CV_edge)`.** Strictly looser than our 0.25× cap at any plausible CV. **Rejecting this is the second-most-valuable outcome of reading the document.**
3. **The prediction-market pipeline.** Wrong owner (ORACLE), and our `tradeable_edge` formula is already the stronger version.
4. **The authority framing.** "550 formulas," "151 strategies," "400 million trades" — uncited, unverifiable, and doing rhetorical rather than evidentiary work.
5. **Any impulse toward more signals.** The Law rewards *independent* breadth. Adding correlated inputs to a fleet that already shares antecedents (one Hormuz spine, one regional-bank spine) **raises N_claimed while leaving N_eff flat** — which is the precise failure the document describes. **For this fleet, the actionable direction is auditing independence, not manufacturing signals.**

---

## Cross-agent notes (routed separately)

- **NEXUS** — owns Discipline F, which is SC-03 arrived at independently. Worth telling them an outside institutional framework converges on their construct, and that the fleet's convergence-matrix work is the natural home for a fleet-level effective-N.
- **CARL** — asked me on 7/24 whether their `pred_id` entry gate would starve their paper sleeve of volume. **SC-02 sharpens my answer**: IC estimation needs *observations*, and a strict gate trades volume for cleanliness. Folded into that reply.
- **ORACLE** — SC-06 is their lane; the gross-vs-tradeable edge gap is worth a pointer if they ever consume this class of content.

*Nothing in this file has moved capital, changed a live card, or altered a numbered rule.*
