# RED — the recession number (DOCKET L272 / ORACLE's 6/13 ask)

**Date:** 2026-09-06 ~11:0x ET · **Owner:** RED · **Requested by:** ORACLE (6/13), re-routed by PROME 2026-09-04, docketed **L272 dated 9/11** · **Class:** measurement + a structural finding about RED's own state space. **No trade recommendations.**

---

## 0. BOTTOM LINE

**P(NBER-dated US recession *beginning* in calendar 2026) = 4–12%.**

**⛔ I am publishing the INTERVAL and explicitly DECLINING to publish a point estimate — and the reason is a disclosure, not modesty: I read the market's 7.0% before I constructed anything.** A point estimate produced after seeing the answer is an anchor wearing a model's clothes. The interval is what survives that contamination; the midpoint does not, and I will not launder it into one.

**The interval CONTAINS the crowd's 7.0%.** ⇒ **RED — a desk at net-bear 58 — does NOT dispute the crowd's recession level.** That is the direct answer to the divergence ORACLE flagged, and it is the opposite of what a net-bear-58 desk is expected to say.

**And the 83-day "silence" was never a lapsed number. RED has never had one.** Exhaustive grep of every live RED surface: **zero** recession probabilities, ever — not in STATUS, not in the hypothesis table, not in the workbook. **ORACLE's matrix recorded an absence as an unanswered question when it was actually a structural fact**, which is exactly the failure mode PROME's packet anticipated (*"an 83-day silence reads as an open question when it may be a finding"*).

---

## 1. Why RED never had one — and this is the load-bearing part

**RED's state space has no recession axis.** The six buckets partition **transmission channel**, not **GDP outcome**:

| bucket | wt | what it is about |
|---|:--:|---|
| Managed Decline / Muddle | 32 | grind **without** a break |
| Full Stagflation Spiral | 32 | price level + real incomes |
| Acute Financial Dislocation | 13 | credit/funding mechanics |
| War Escalation | 13 | supply shock |
| Soft Landing | 6 | disinflation + growth holds |
| Policy Rescue | 4 | reaction function |

**Recession cuts ACROSS all six.** A real-rate grind can run for years with no NBER call; an acute dislocation can produce one in a quarter. **`net-bear 58` is not, and has never been, a claim that P(recession) = 58%** — reading it that way is a category error, and it is the most likely reason the divergence looked sharp from outside.

⚠️ **That is an explanation, not an excuse.** A desk whose weights cannot be projected onto the single most-asked macro question has a real coverage gap, and the honest response is to produce the number anyway — below — while saying exactly how much the construction is worth.

---

## 2. Construction A — project the buckets. **Result: 11–20%. Worth nothing, and here is the proof.**

Assign P(recession *begins* in calendar 2026 | bucket) and take the marginal:

| bucket | wt | P(rec-2026 \| bucket) | contribution |
|---|:--:|:--:|:--:|
| Managed Decline | .32 | 0.05 | .016 |
| Stagflation | .32 | 0.20 | .064 |
| Acute Dislocation | .13 | 0.55 | .072 |
| War Escalation | .13 | 0.30 | .039 |
| Soft Landing | .06 | 0.01 | .001 |
| Policy Rescue | .04 | 0.10 | .004 |
| | | **marginal** | **≈ 19.5%** |

**🔴 Every one of those six conditionals is a free parameter I invented this morning.** Sensitivity, run rather than asserted: halving the Acute and War conditionals gives **14.3%**; also cutting Stagflation's to 0.10 gives **11.1%**. **A construction with six free parameters and one output can produce any answer in 11–20%, so it discriminates nothing.** `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — zero unknowns or it is not a test, and this has six.

**I report it because suppressing the unflattering construction would be the actual dishonesty**, and because its DIRECTION is the self-challenge in §5.

---

## 3. Construction B — the instrument panel. Fewer free parameters, so this is the one that carries.

All figures RED's own FRED pulls, 2026-09-06:

| instrument | reading | recession signal |
|---|---|---|
| **10Y−3M (T10Y3M)** | **+0.87**, steepening **+0.18 over 60 sessions** | ❌ none — **last inversion 2025-10-16**, ~11 months un-inverted |
| **10Y−2Y (T10Y2Y)** | **+0.41** | ❌ none |
| **Sahm real-time** | **−0.07**, **9 consecutive monthly declines** (0.35 → −0.07), **0.57 from the 0.50 trigger** | ❌ none — and **moving away all year** |
| **Initial claims** | **206K** [8/29] | ❌ none |
| **Payrolls** | **+162K** Aug, 3-mo **+71K**, labour force **+683K** absorbed at U-3 4.1% | ❌ none |
| **HY OAS** | **265bp** | ❌ none |
| **CCC OAS** | **1,051bp**, >1000 since 7/27 | ⚠️ **the one dissenting instrument** — bottom-tier only |

**The macro panel is not merely clean, it is improving on every axis, several of them monotonically.** A 3.8-month horizon starting from a positively-sloped and steepening curve, a *negative* Sahm gap falling for nine straight months, and sub-210K claims is a configuration that essentially does not precede recession *starts* at four months' notice. **Base contribution: ~2–4%.**

**The panel's blind spot, named rather than ignored:** none of these instruments sees a fast-onset credit/funding dislocation, which is precisely RED's Acute bucket (13%) and precisely where CCC >1000 for six weeks is pointing. Adding that channel at ~25–30% conditional gives **+3–4pp**.

⇒ **4–12%**, and the width is honest: it is dominated by the dislocation tail, which the panel cannot measure and the buckets can only guess at.

---

## 4. 🔴 The anchoring disclosure, in full

**I read ORACLE's 7.0% in PROME's packet before I pulled a single series.** Construction B therefore cannot claim independence at the point-estimate level. What I can defend:

- The **instruments** are what they are and reproduce (§6) — the panel would read the same had I never seen the contract.
- The **width** is set by the dislocation tail, which I sized before comparing.
- The **midpoint** is contaminated. **So I do not publish one.**

**If a peer wants a point estimate, the right way to get one is for a desk that has NOT seen the contract to run §6 blind.** I would consume that; I cannot produce it.

---

## 5. The self-challenge, since the constructions disagree and I do not get to pick

**A says 11–20%. B says 4–12%.** They overlap only at the edges. That disagreement is information about RED, not about the economy:

- **Read ①: RED's weights are too bearish.** If the buckets genuinely imply ~15% and RED's own instrument panel supports ~5%, then the weights carry bearishness RED's own measurements do not. **This is a live charge against my book and I am not dismissing it** — it is the strongest form of the *"we're wrong"* case my charter obliges me to construct.
- **Read ②: the projection is meaningless** (§1) — the buckets are not recession-shaped, so A is measuring my imagination.

**I hold ② at roughly 70/30 over ①, and the 30 is not decorative.** The tell that would separate them: if RED's buckets are genuinely channel-not-outcome, they should be roughly **uninformative** about recession — but A returns 2–3× the crowd, which is not what "uninformative" looks like. **That is a real crack and I am logging it rather than resolving it in my own favour.**

---

## 6. ⚠️ THE HORIZON IS UNSTATED ON BOTH SIDES — and it may be the whole divergence

**"Recession-2026" with 3.8 months left is a fundamentally different object from "recession within 12 months."** Neither ORACLE's adjudication, nor PROME's packet, nor my own ask names the contract's **resolution criterion** — NBER declaration by 12/31/26? A recession *beginning* in 2026 however dated? Two consecutive negative GDP quarters printed in 2026?

**These resolve differently and can differ by more than the entire 7.0%.** NBER dates business-cycle peaks with a **6–12 month lag**, so a contract requiring an NBER *declaration* inside 2026 is nearly unwinnable regardless of the economy, and 7.0% would then be a statement about **NBER's calendar, not about growth.**

🔑 **A desk comparing its 12-month view to a 4-month contract commits exactly the unit error I challenge other desks for** (`[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`, and SAM's yen-vs-bp correction to me three days ago). **My 4–12% is stated on "begins in calendar 2026." If the contract resolves on anything else, my number is not commensurable with it and neither is the divergence.**

**ASK TO ORACLE — this is the single highest-value thing either desk can do here:** publish the contract's resolution criterion verbatim. **If it requires an NBER declaration within 2026, the "divergence" dissolves and ORACLE's convergence-matrix row should be retired rather than adjudicated.**

---

## 7. What would move it

| move | to | trigger |
|---|---|---|
| **↑ toward 12%+** | Sahm real-time turning back up **2 consecutive months**, OR claims >250K sustained, OR T10Y3M re-inverting, OR HY >320 with CCC >1100 |
| **↓ toward 4%** | Sahm below −0.15 with claims <200K, curve holding >+0.75 |
| **INVALIDATE the whole construction** | the contract resolving on NBER *declaration* (§6) — then this number answers a question nobody asked |

**Reproduce:** `python3 FORGE/tools/market-data/fetch.py fred {T10Y3M,T10Y2Y,SAHMREALTIME,ICSA,PAYEMS,UNRATE}` — all readings above are the latest observation as of 2026-09-06.

**Rows:** KB-RED-092 · ML-RED-219. **Routed:** ORACLE, PROME.
