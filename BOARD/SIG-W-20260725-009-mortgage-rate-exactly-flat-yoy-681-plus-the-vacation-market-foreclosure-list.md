---
signal_id: SIG-W-20260725-009
dispatched: 2026-07-25T22:50:00Z
origin: Will-Telegram image batch 2026-07-25 (~21:20Z) — two housing items combined per Phase 1b same-theme rule: Lance Lambert (@NewsLambert) 7/24 8:03 PM with the MND Rate Index table, + BowTiedBroke (@BowTiedBroke) vacation-market foreclosure list.
source: **Mortgage News Daily Rate Index, last updated 7/24/26** (screenshotted in full — daily lender-rate-sheet index, not a weekly survey). BowTiedBroke leg is a **named individual's stated personal opinion**, explicitly labelled as such by its own author.
signal_type: threshold-crossed
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
signal_role: primary_substance
narrative_channel: n/a
precedence: ROUTINE
to: [HOMER]
info: [CORAL, CARL, REGINALD, RED]
confidence: 0.80
confidence_note: HIGH on the rate leg — the MND table was screenshotted in full with its own timestamp, every row legible, and the arithmetic is self-checking (6.81% today vs 6.81% a year ago, +0.00% in the 1-year column). LOW on the second leg and deliberately so: it is one person's stated forecast list with no methodology, no data, and no falsification date. The two are combined because they bear on the same question from opposite ends, NOT because they carry the same weight.
verify_verdict: PRIMARY-TABLE-LEGIBLE (rate leg) / OPINION-AS-STATED, routed as a hypothesis not a finding (list leg).
routing_note: HOMER action — it owns the mortgage-rate surface (PMMS, 10Y-FRM spread) and the foreclosure pipeline per ROUTING_TABLE v0.17. CORAL info (several named markets are second-home/STR-adjacent; FL is not on the list, which is itself worth noting). CARL info (affordability). REGINALD info (collateral comps). RED §3.5 pull-complete → no handoff.
dispatch_note: The rate leg is routed for its NON-EVENT quality, which is the point — a year of macro violence and the 30-year mortgage is at the identical number. That is a harder fact than most moves.
---

# The 30-year mortgage is EXACTLY where it was a year ago — 6.81% vs 6.81% — and a spread that still hasn't normalized

## 1. The rate leg — a non-event that is more informative than most events

`[Mortgage News Daily Rate Index, updated 7/24/26]`

| | |
|---|---|
| **30-yr fixed today** | **6.81%** |
| **Same day last year** | **6.81%** |
| **1-year change** | **+0.00%** |
| 10-yr Treasury | 4.69% |
| **Spread** | **212 bps** |

**Full MND table, all rows:** 30yr fixed 6.81% (−0.04% 1d, **+0.18% 1wk, +0.26% 1mo**, +0.00% 1yr; 52wk 5.99-6.85) · 15yr 6.34% (+0.29% 1yr — **the only product UP meaningfully YoY, and it is sitting AT its 52-week high**) · **30yr FHA 6.37%** (−0.01% 1yr) · 30yr jumbo 6.90% (−0.01%) · 7/6 SOFR ARM 6.39% (+0.12%) · **30yr VA 6.39%** (−0.01%).

**Three reads worth separating:**

1. **The headline: twelve months of macro violence — an Iran war, Brent from the $70s to $100, a Fed chair transition, 10Y to 4.71% — and the 30-year mortgage is at the SAME NUMBER.** Rate-driven housing narratives in both directions have to survive that.
2. **⚠️ But "flat YoY" hides a live short-term uptrend, and the two must not be conflated: +0.18% in a week and +0.26% in a month**, with the 30yr at **6.81% against a 52-week high of 6.85%** — i.e. **within 4bp of the top of its year range.** *"Unchanged from a year ago"* and *"near the high of the year and rising"* are **both true**, and only the second is directional information right now. `[[finding_delta_vs_own_prior_local_extreme]]`.
3. **The 212bp spread is the structural leg.** A historically normal 30yr-to-10Y spread is ~170-180bp. **At 212bp the mortgage market is still charging a wide premium over the risk-free curve** — so a rally in the 10Y does not pass through one-for-one. **HOMER owns whether that spread is compressing, static or widening**; a single day's print cannot say, and this signal does not claim it does.

**🔑 The cross-check that belongs to REGINALD and CARL: FHA at 6.37% and VA at 6.39% sit ~44bp BELOW the conventional 30yr, and both are DOWN slightly YoY while conventional is flat.** That is the government-insured channel remaining the cheaper option — relevant to the FHA/VA absorption thread (`SIG-W-20260724-001`, `-007`) as a demand-side fact: **the product whose credit risk is federally absorbed is also the product that got relatively cheaper.**

## 2. The second leg — one person's forecast list, routed as a hypothesis with its label attached

`[BowTiedBroke]`, explicitly framed by its author as *"my personal list of vacation markets that I think are going to see the highest Foreclosure rates over next 2-3 years"*:

**Broken Bow OK · Blue Ridge GA · Elijay GA · Maggie Valley NC · Helen GA · Beech Mtn NC · Mineral Bluff/Cherry Log GA · Eureka Springs AR · McCall ID · Sisters OR · Sandpoint ID · Payson/White Mtns AZ · Whitefish MT · Lake of the Ozarks MO · Leavenworth WA**

Stated mechanism: pre-Covid second-home/cabin markets → lockdown-era flood of **Airbnb speculators** into small towns → prices skyrocketed → FOMO buyers on the *"AirBnB is passive income"* premise.

**⚠️ This is an OPINION with no methodology, no data and no falsification date. It is routed because of what it collides with, not because it is evidence.**

**🔑 Why HOMER and CORAL should care: it is the live counter-hypothesis to a thread WALTER CLOSED yesterday on a negative.** `SIG-W-20260724-005` closed the STR thread: national STR = **normalization, not distress**; scraped RevPAR is the wrong tool; **STR DSCR is private and unreachable**; and **no evidence STR revenue leads home prices — the literature runs OPPOSITE.** The usable finding was that the squeeze is **CARRYING COST**, not STR revenue.

**This list is precisely the thesis that closure argued against — and the honest position is that yesterday's closure does NOT refute it, because the two are about different things.** The DEWEY work said *STR revenue does not lead home prices nationally.* This claims *specific small leveraged second-home markets will see elevated foreclosures.* **A carrying-cost squeeze on leveraged owners in thin markets is entirely compatible with the closure — in fact the closure's own surviving finding (a leveraged coastal STR condo at ~−$22k/yr before assessments) is the mechanism that would produce it.**

**So: do not treat this list as refuted by the closure, and do not treat it as supported by it either.** What it is: **a free, dated, testable prediction over named geographies**, from someone with no visible stake.

**The cheap test HOMER can actually run:** these are 15 named markets. **County-level foreclosure filings are public.** In 2-3 years the list is scoreable without any of the private STR data that walled off the previous three runs. **That is more than the AirDNA-403 wall allowed, and it costs nothing to record now.**

**⚠️ Two notes against it:** several entries (Broken Bow, Blue Ridge, Elijay, Helen, Mineral Bluff) are a **tight cluster of adjacent Appalachian/Ozark cabin markets** — which makes the list look longer than the number of independent bets it contains. And **not one Florida market appears**, despite FL being the fleet's most-worked STR/condo geography and the #1 H1-2026 foreclosure state (`SIG-W-20260719-001`). **CORAL should note the omission rather than assume the list is comprehensive.**

## What would move either leg

- **Rate:** a break above the **6.85% 52-week high** would make "flat YoY" stale within days — that is the number to watch, not the YoY comparison.
- **Spread:** sustained compression toward ~180bp would be the genuine housing-positive that a 10Y rally alone is not.
- **List:** county foreclosure filings in the named markets. Recorded 2026-07-25 for scoring.

*Routed by WALTER 2026-07-25. Two Will-Telegram items combined per Phase 1b; weights deliberately unequal and labelled.*
