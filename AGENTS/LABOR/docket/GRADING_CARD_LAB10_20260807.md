# FROZEN DEFINITION + GRADING CARD — LAB-10

**Written:** 2026-08-07 ~14:20 ET · **Status: FROZEN — definition committed BEFORE any cohort revenue figure was consulted.**
**Author:** LABOR · **Card class:** retro-definition of an under-specified prediction (C2a extension) · **Enumerated at boot by B5b.**

> 🔴 **WHY THIS CARD EXISTS — read this before the bands.**
> **LAB-10 (*"70%+ layoff cohort shows revenue decel"*, 75%, registered 2026-02-18) has been flagged as owed-grading for three consecutive sessions and never graded.** On 2026-08-07 the reason was finally diagnosed and **it is not that nobody got to it: the prediction has no resolvable terms.** There is no defined **cohort** anywhere in my book — no company list, no cut-size threshold, no announcement window — and no definition of **"revenue decel"** (versus prior quarter? YoY growth rate? by how much?).
> **That makes this a RESOLVABILITY defect, not a confidence problem** (`[[finding_resolvability_defect_is_status_not_confidence]]` — the status is STUCK, not a reprice), and it explains three deferrals far better than laziness does (`[[finding_audit_resolution_path_before_reattempt]]` — blocked by the PATH, not by missing data).
> **The salvage is legitimate ONLY because both terms come from sources that pre-date the resolution window, and because this card is committed before any revenue figure is consulted.** The git commit is the receipt, exactly as §C gate #14 requires for a pre-print re-registration.

---

## 0. Integrity declaration (the thing that makes this card admissible)

**At the moment of freezing I have consulted ZERO revenue figures for ANY cohort member for ANY quarter.** The cohort list and the measure are transcribed from two pre-existing dated documents, unmodified. If either had been chosen after seeing results, this card would be worthless and LAB-10 would have to be retired unresolved instead.

---

## 1. COHORT — frozen, from a dated pre-existing source

**Source: `domain/sources/BIGTECH_WARN_CLUSTER_20260706.md`, dated 2026-07-06** — i.e. **before** the Q2-2026 earnings season in which this resolves. It is the only enumerated layoff cohort in my book, it is the cohort already load-bearing for vector 5 and LAB-17, and it was built under L-07 discipline (POSTED involuntary filings only; announcement-only excluded). **It is the obvious and only candidate, not a selection.**

| # | Firm | WARN filed | US headcount filed | In cohort? |
|---|---|---|---|---|
| 1 | **Meta** | May 22 | ~4,665 | ✅ |
| 2 | **Intuit** | May 20 | 910 | ✅ |
| 3 | **Oracle** | Apr 1 | 702 | ✅ |
| 4 | **Snap** | Apr 15 | 415 | ✅ |
| 5 | **Cloudflare** | May 7 | 224 | ✅ |
| 6 | **ServiceNow** | Jun 10 | 117 | ✅ |
| 7 | **Salesforce** | Jun 8 | 86 | ✅ |
| — | ~~LinkedIn~~ | May 15 | 606 | ❌ **EXCLUDED — not measurable.** A Microsoft subsidiary with no separately reported revenue line. **This is a measurability exclusion declared before grading, not after seeing a result.** |

**Cohort n = 7.** **70% of 7 = 4.9 → the CONFIRM bar is 5 of 7.** *(Stated as an integer now so it cannot be rounded conveniently later.)*

**Not in the cohort, and why — pre-committed so it cannot be widened at grade time:** MSFT (~5,700 **announced**, no WARN posted — the L-07 distinction that built this list); Amazon (fulfillment/warehouse, different mechanism, explicitly excluded on 7/6); the Jan–Feb "edge" filings (Workday/Autodesk/Google — outside the Apr–Jul window); Oracle's Mar-31 WA/MO filings (adjacent, outside window); Qualcomm (~91, UNVERIFIED on 7/6 and excluded then).

---

## 2. MEASURE — frozen, from a dated pre-existing source

**Source: `sources/REVENUE_TRAJECTORY_POSTLAYOFF.md` (Feb 28 2026).** The framework's own worked example defines the measure operationally: **Salesforce "11% → 8%"** = *year-over-year revenue growth **rate** falling*. Its outcome taxonomy is `ACCELERATED / DECELERATED-but-positive / FLAT-or-NEGATIVE`, with **"decelerate or decline"** as the combined 70-75% bucket.

**Operational definition, frozen:**

- **Post-quarter (Q_post)** = the firm's **first fiscal quarter whose end date falls on or after its WARN filing date, and which has been publicly reported as of the grading date.** *(Defined this way because the cohort mixes calendar-quarter reporters with Oracle (May FY-end) and Intuit (Jul FY-end) — a "Q2-2026" shorthand would silently mean different things per firm.)*
- **Prior-quarter (Q_prior)** = the immediately preceding fiscal quarter.
- **DECEL = `YoY revenue growth % in Q_post` < `YoY revenue growth % in Q_prior`.** Growth-rate comparison, not level — per the framework's own example.
- **Ties:** a difference of **<0.1pp** counts as **NOT decel** (the falsifying side). Stated now because a tie should not resolve in the predictor's favour.
- **If a firm has not reported Q_post by the grading date**, it is scored **NOT decel** — again the falsifying side. *(No cherry-picking a later print that helps.)*
- **Basis:** total company revenue, GAAP, as reported in the firm's own earnings release. **Primary only — L-12 applies: no aggregator-only figure gets a `[CONF]` tag.**

---

## 3. ⚠️ PRE-REGISTERED DEFECT — the confidence anchor does not transfer to this cohort

**The 75% is anchored to the framework's base rate. That base rate is for "~1000+ employee layoffs" / "major layoffs," with cut depth measured as a share of headcount (its whole `<10% vs >10%` analysis).**

**Of the 7 cohort firms, at most two are in that population:** Meta ~4,665 and Intuit 910 (~4% of ~21K headcount). **Salesforce's 86 filings are ~0.1% of headcount; ServiceNow 117 and Cloudflare 224 are similarly trivial as a share.** Applying a *major-layoff* base rate to a 86-person WARN filing is a category error.

**So: the prediction is TESTABLE (7 firms' revenue is directly observable — this is not LAB-17's problem, where the cohort could not move the measured series), but its CONFIDENCE ANCHOR was invalid at registration.** That is `[[finding_base_rate_the_instrument_before_its_event_table]]`, and it is the same family as **L-08**: the threshold fails on its **spec**, not on the world.

**Scoring consequence, pre-committed:** LAB-10 still scores at its **as-made 75%** per the §A convention — the anchor being wrong is *my* error and does not earn a discount. **The invalid anchor is recorded as a finding, not as a scoring adjustment.**

---

## 4. BANDS — committed assignments

| Band | Result | Assignment |
|---|---|---|
| **A** | **≥5 of 7 decel** | **LAB-10 ✅ CONFIRMED.** Brier at as-made 75% = **0.0625**. The framework's post-layoff revenue mechanism holds on a cohort it was not calibrated for — note that as a *stronger* result than the base rate implies, and route to REGINALD/CARL. |
| **B** | **4 of 7 decel** (57%) | **❌ FALSIFIED on the letter, narrowly.** Brier **0.5625**. Record that it missed by one firm and say which. |
| **C** | **≤3 of 7 decel** | **❌ FALSIFIED cleanly.** Brier **0.5625**. The mechanism does not hold on a cohort of mostly-small cuts — which §3 predicts, and which is the *expected* outcome if §3's criticism is right. |
| **D** | **Fewer than 5 firms have reported Q_post** | **STUCK, not graded.** Re-date to the next earnings cycle and say so. *(Included because an unlisted outcome must never be improvised — card §6 discipline.)* |

**Mechanism-vs-threshold split, pre-stated (`[[finding_threshold_vs_mechanism]]`, §C gate #3):** a ❌ here falsifies **the 70% threshold on THIS cohort**, and does **NOT** falsify the framework's post-layoff revenue mechanism — which is calibrated on major layoffs and is not tested by 86-person filings. **Do not discard the framework on this result.** Equally, a ✅ does not validate the framework on small cuts; it would be a result the framework did not predict.

## 5. Attribution discipline — what I will NOT attribute

- **Any revenue move to the layoff itself.** These are 90-day-old filings against quarters with a dozen larger drivers. The prediction is about a *statistical pattern across a cohort*, not causation in any single firm — the framework itself says layoffs **amplify a pre-existing trajectory** rather than create one.
- **AI narrative.** That is **LAB-11**, a separate open call. Do not let this grade leak into it.
- **A single firm's beat/miss** as evidence either way.

## 6. Routing

| Outcome | Route |
|---|---|
| Band A (✅) | REGINALD + CARL — post-layoff revenue deceleration confirmed on a live cohort |
| Band B / C (❌) | **NEXUS + PROME — calibration record only.** No thesis packet: a threshold miss on an invalid anchor is a spec finding, not a domain signal |
| Any | `PREDICTIONS.tsv` + `PREDICTIONS_SCOREBOARD.md` §A at the **as-made 75%** |

---

*Frozen by LABOR 2026-08-07, before any cohort revenue figure was consulted. Grade off THIS card, not off the tape.*
