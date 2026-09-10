# PHAN -> CARL: 2026-09-10 dossier pass (WQ-209, +62d since 7/10)

**From:** PHAN (dossier-mode sub-agent) · **To:** CARL · **Date:** 2026-09-10 ~17:00 ET
**Spawn:** Will-approved WQ-209 (Decision Deck tap 2026-09-10 20:42Z); PROME spawned Tier 1 under CARL's card.
**Scope honored:** wrote only inside `AGENTS/CARL/sub_agents/PHAN/` (+ the PROME completion memo). **No CARL STATUS / TRADE / thesis / docket file touched. No trade proposal — report-before-execute.**
**Live surface:** `DOSSIER.md` (new dated section at top). **Ledger of record:** `workbook/PREDICTIONS.tsv`.

---

## 0. Inbox drain — explicit NULL

`AGENTS/CARL/sub_agents/PHAN/inbox/` contained **zero packets** (only `README.md` and `processed/.gitkeep`). Nothing to integrate, nothing to `git mv`, nothing PARKED.

⚠️ **This is a finding, not a clean bill of health.** The inbox card's own mitigation rule is *"age is a finding"* — but the failure mode the card names (mail sitting unread for weeks at a desk with no boot cadence) is **indistinguishable at the artifact from mail never sent**. Zero packets across 62 days means either nobody needed PHAN, or senders read the dossier-mode banner and routed to CARL instead — which is what the README tells them to do. **The channel has never been exercised.** If CARL wants to know whether it works, the test has to be a deliberate one; an empty inbox proves nothing either way.

---

## 1. What CARL must grade — ranked

### 🔴 ① The NY Fed refutes the BASIS of your CC 90+ instrument (CRL-05). This is the item.

**NY Fed Liberty Street Economics, Aug-2026 — *"How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures."***

| Claim | Figure | Vintage |
|---|---|---|
| CC 90+ **stock** delinquency rate | **12.8%** | most recent cited in the piece (Q1-2026) |
| Same measure, pre-cycle | **7.6%** | Q3-2022 |
| Share of charged-off debts still being reported **one year later** | **~40%** | 2004–2012 |
| Same share | **80%** | 2024 |
| Stock rate with charged-off balances excluded | *"falls in line with both our flow delinquency rate and the Call Report delinquency rate"* | — |
| Flow (new-delinquency) rate | *"elevated but has been largely stable since 2024"* | — |

**The consequence for you:** CRL-05 is armed on **CC 90+ DQ > 13.74% (GFC peak)**. If a material part of the 7.6% → 12.8% climb is lenders leaving charged-off balances on file for twice as long as they used to, then **the series is not measuring the same thing at the two ends of the comparison, and the GFC-peak reference point is not commensurable with the current print.** A breach could be delivered by reporting practice alone.

**What I am NOT claiming:** that consumer stress is fake, or that the flow rate is benign — the NY Fed calls it *elevated*. I am claiming the **level-vs-reference comparison** is compromised, which is a narrower and more damaging point than "the number is wrong." `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]` · `[[finding_exact_level_authenticates_a_wrong_direction]]`

**Recommended (PHAN proposes, CARL disposes):**
1. **Re-instrument CRL-05 onto the FLOW rate** (new-delinquency transitions), or carry both legs explicitly with a named basis on each. Do not silently keep the stock series.
2. **Route to RED** — this is genuine counter-evidence to a load-bearing vector and belongs in `handoff_RED/COUNTER_LOG`, not only in a KB row.
3. ⚠️ **Check the same failure at every other stock-vs-GFC-peak threshold you carry** (CRL-03 Fannie MF DQ, the auto DQ rows). The reporting-duration effect is a bureau-data property, not a credit-card property. I have not checked those — **that is your data, not mine, and I did not go looking.**

---

### 🟠 ② BNPL late-payment rate breached the RED band for the first time — and your STATUS row is a vintage behind

| | Value | Source |
|---|---|---|
| CARL `STATUS.md` row today | **41%** (+7pp YoY), tagged *"2025, CFPB"*, 🟠 | CARL STATUS.md L22 |
| **Live** | **47%** | LendingTree BNPL Tracker, n=2,060, fielded 2026-03-17/23, published **2026-08-19** |
| Series | 34% ('24) → 41% ('25) → **47% ('26)** | same tracker |
| PHAN band | Red **>45%** | `DOSSIER.md` §3 |

**Two separate defects in that one STATUS row, and the second is the worse one:**
- **Stale:** 41% is the 2025 reading; the 2026 reading published three weeks ago is 47%.
- ⚠️ **Attribution:** the row credits **CFPB**. The 34/41/47 series I can actually reach is **LendingTree's** annual BNPL Tracker. The ABA published a 34–41% figure that PHAN's own §3 attributes to ABA. **I cannot find a CFPB publication of 41%.** That may mean the row is mis-attributed, or it may mean there is a CFPB figure I did not locate — I am flagging it as a **candidate**, not asserting it. `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]` **The check costs you one grep of your own KB; it is not mine to edit.**

**Consumer-check consequence:** if you supersede 41% → 47%, run `scripts/consumer_check.py --agent CARL --old 41% --new 47%` — this figure is quotable by DOC, POP and RED.

---

### 🟠 ③ FLOW-PHAN-06 (BNPL composition-masking / ALLY analog) — trigger DOWNGRADED, and the downgrade is about BASIS not about direction

The 7/10 dossier says the trigger is **"NOW ACTIVE per legacy vintage (Affirm +40% YoY provisions vs DQ improvement)."** Worked against Affirm's **FY2026 10-K (FYE 2026-06-30, filed 2026-08-27; figures pulled from SEC XBRL, primary)**:

| Metric | FY2026 | FY2025 | Δ |
|---|---|---|---|
| GMV | **$50.2B** | — | **+37%** |
| Loans held for investment, gross | **$9,560.7M** | $7,025.5M | **+36.1%** |
| Provision for credit losses | **$796.7M** | $616.7M | **+29.2%** |
| Allowance for credit losses | **$563.3M** | $396.9M | **+41.9%** |
| **Allowance as % of loans HFI** | **5.89%** | 5.65% | **+24bp** |
| Gross write-offs | $687.2M | $552.1M | +24.5% |
| Recoveries | $75.6M | $51.3M | +47.4% |
| **Net charge-offs** | **$611.6M** | $500.8M | **+22.1%** |
| 30+ DQ ex-Peloton | **2.5%** @6/30/26 | 2.3% @6/30/25 | +19bp YoY; **down** from 2.7–2.8% in the prior 3 qtrs |

**Verdict: ACTIVE → PARTIAL, 1 of 2 legs.**
- ❌ **The "provisions outpace volume" leg FAILS on the FY basis** — provision +29.2% is *below* GMV +37% and *below* loans +36.1%. NCOs +22.1% are slower still.
- ✅ **The allowance-RATE leg HOLDS** — 5.65% → 5.89%. Expected lifetime loss **per dollar of book** rose while the headline DQ fell. That is the leading-indicator half of the pathway and it is the half that matters.
- The DQ read is genuinely two-sided and both halves are true: **2.5% is a sequential improvement and a YoY deterioration.** Quote whichever you like, but say which. `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`

⛔ **SOURCE HONESTY:** a secondary analyst read of the 8/27 earnings supplement reports **Q4-only provision growth of +42%** and NCOs rising **$128M (Q1) → $170M (Q4)**. That would support the original framing on a quarterly basis. **I could not verify it:** the primary — `Affirm FY Q4 2026 Earnings Supplement, August 27 2026`, `investors.affirm.com/static-files/c160ce8f-a9b5-4896-b8ed-6544ac430809` — **timed out on two fetch attempts (SEARCH-NOT-FOUND)**. Every FY figure in the table above is from the 10-K XBRL and is VERIFIED; the Q4-only figures are **INFERRED from a secondary and must not be cited as primary.** ⚠️ Note the trap: the secondary's "+42%" and my primary allowance growth of "+41.9%" are near-identical, which is exactly what a conflated allowance-vs-provision figure would look like. **Do not reconcile them by assuming they agree.**

**KB-CARL-228 refresh owed at your end** (Affirm/Klarna quarterlies are yours per §6): Affirm FY26 as above; **Klarna Q2-2026 (press release 2026-08-18, primary): GMV $36.6B +18% (US +27%), provisions 0.52% of GMV vs 0.56% Q2-25, US Fair Financing 30+ DPD −20bp QoQ, net income +$9M vs −$53M, active consumers 120M (+8%), FY26 GMV guidance CUT to $149–151B from >$155B.**

---

### 🟡 ④ The transmission read you asked for — gas cross, NFP drop-back, LABOR T-03

BNPL has become a **necessities** instrument, which is what makes it a CARL vector and not a retail-credit curiosity [all LendingTree, n=2,049 US consumers 18–80, fielded 2026-03-03/06, published 2026-08-19]:

| Claim | Figure |
|---|---|
| Agree they need BNPL **"to make ends meet"** | **54%** (62% of parents with children <18; 59% millennials; 57% Gen Z) |
| Have used BNPL for **groceries** | **29%** — up from 25% ('25) and **14% ('24)** |
| Have used BNPL for **rent** | 13% |
| Held **3+** BNPL loans simultaneously | 25% (Gen Z 29%) |

⭐ **The load-bearing inference, and the reason it is worth your time:** the late rate went **41% → 47%** across a year in which **payrolls were revised UP** (July −23K → +21K, BLS 9/4) and **LABOR's T-03 did not fire.** The shadow layer deteriorated *without* the employment leg. That is direct evidence for the **"rot, not detonator"** core of Beneath the Ice v2.5.1 — sourced from a series you do not currently carry.

**It cuts both ways, and I am saying the uncomfortable half too:** it also means **V16's drop-back branch can resolve DOWN at the ~10/2 NFP and this series would still be deteriorating.** So the branch is not a referendum on the consumer leg, and a V16 step-down should not be read as consumer-side relief. Symmetrically: this series is **not** a substitute for the employment evidence V16 actually grades on.

**Gas link — I have to declare a miss.** A widely-circulated 2026 breakdown puts **38% of BNPL users having used it for gasoline** (and 46% groceries / 39% utilities / 42% medical), which would be the direct **$4.146-pump → phantom-debt** channel. ⛔ **I could not attribute it to a reachable primary** — the CNBC carrier returned HTTP 403 and PYMNTS' own article does not contain the breakdown. **SEARCH-NOT-FOUND; I am not citing it and neither should you.** The LendingTree figures above are the ones that survive. **This is the single biggest evidentiary gap in the pass** and it sits exactly on the CARL link you asked for.

---

## 2. Dispositions — all 7, at the 2026-09-10 vintage

**None resolved here. CARL disposes (`DOSSIER.md` §8.4). One resolution is recommended.**

| # | Prediction | Window | 7/10 | **9/10** | Verdict | Basis (one line) |
|---|---|---|---|---|---|---|
| P01 | BNPL stacking >70% | H2 2026 | 60% | **25%** | **TRACKING → MISS-lean** | 63% in CFPB Jan-25 **and** 63% in LendingTree Mar-26 — two instruments, two populations, same level. Intensity rose (3+: 23%→25%), breadth did not. |
| P02 | Klarna credit losses >1.0% | FY2026 | 6% | **2%** | **MIXED — ⭐ recommend CARL resolve MISS at FY-close** | Q1-26 **0.55%**, Q2-26 **0.52%** of GMV, both falling, both ~half the threshold, both profitable quarters. |
| P03 | CFPB 1033 delayed past 2026 | EOY 2026 | 96% | **97%** | **TRACKING HIT** | Still enjoined + under reconsideration; <4 months left; no enforcement path. See the logged conflict below. |
| P04 | ≥2 more fintech failures | 2026 | 45% | **12%** | **TRACKING → MISS-lean** | **Explicit DID_NOT_APPEAR null.** Zero in-scope consumer failures in 8.3/12 months. |
| P05 | BNPL-linked FHA defaults identifiable | Q3–Q4 2026 | 40% | **15%** | **TRACKING → MISS-lean (unresolvable-class)** | No FHA guidance, no furnishing mandate, no loan-level attribute. **Failing on data infrastructure, not on the phenomenon.** |
| P06 | NY comprehensive BNPL licensing | 2026 | MIXED | **MIXED** | **RESOLVED 7/10, unchanged** | No new information. |
| P07 | Cash-advance AG enforcement ≥5 states | 2026 | 80% | **88%** | **TRACKING HIT** | **CO AG v. EarnIn 2026-08-27** ⇒ NY+MN+DC+CO = **4 of 5**, ~3.7 months left. |

**P04 — the candidates I ruled OUT, with reasons, because the ruling is the work:**
- **Parker** (Ch-7, 2026-05-07) — B2B ecommerce corporate card. Out of scope; **holds** the 7/10 ruling rather than re-opening it.
- **Solid Financial Technologies** (Ch-11, BaaS) — filed **2025-04-07**, Subchapter V liquidation confirmed Nov-2025. ⚠️ **PRE-WINDOW.** A search for "2026 fintech bankruptcy" surfaces it because the *coverage* is recent. Counting it would have manufactured a HIT out of a 2025 event.
- **BlockFills** (Ch-11, 2026-03-15) — crypto trading/lending, outside consumer shadow credit.

⚠️ **P03 — a conflict I am logging rather than resolving.** A secondary tracker states the CFPB **withdrew its request that the court vacate** Rule 1033 and reopened rulemaking, rather than killing the rule. That contradicts the *framing* of our own `REGULATORY.tsv` 2026-04-01 WITHDRAWAL row. **P03's verdict is unaffected either way** — enjoined-and-reconsidered and withdrawn-and-dead both foreclose 2026 enforcement — **but the mechanism sentence we have been repeating may be wrong, and a right answer resting on a wrong mechanism breaks on the next question.** ⛔ `openbankingtracker.com/guides/section-1033-status` returned **HTTP 429** on two attempts. **I did not overwrite the 4/1 row on a secondary.** Owed next pass: read the 1033 docket directly.

⚠️ **Grade the confidence WALK, not just the rows.** Five of six re-marks move **toward the verdict the row was already leaning at**. Each names a dated external fact, not a re-read of old evidence — but a self-graded ledger cannot detect its own drift, and this is the exact shape of `[[finding_confidence_walk_is_selected_for_on_the_rows_that_carry_the_most_brier_weight]]`. **That check is yours.**

---

## 3. Ledger state — the 9/1 freeze was discharged, not laundered

`COCKROACH.tsv` and `REGULATORY.tsv` were FROZEN 2026-09-01 with an explicit dated unfreeze trigger: *"docket/CATALYSTS.tsv row 2026-09-08 'PHAN SPAWN — OVERDUE'. On that spawn, delete this banner and either advance the DATA clock or record an explicit DID_NOT_APPEAR null. Do NOT unfreeze without doing one of those two things."*

**Both obligations met, both ledgers unfrozen, DATA clock advanced 2026-07-10 → 2026-09-10:**

| Ledger | Sweep result |
|---|---|
| `COCKROACH.tsv` | **+1 row** (EarnIn / CASH_ADVANCE / DISTRESS / 2026-08-27) · **explicit DID_NOT_APPEAR null on new consumer-fintech FAILURES**, with all three ruled-out candidates named in the header · **both Klarna rows upgraded 7/10 STALE → REFUTED** on two quarters of primary data (⚠️ with the growth-deceleration leg preserved separately — the credit narrative is dead, the **FY26 GMV guidance cut to $149–151B from >$155B** is not, and neither should launder the other) |
| `REGULATORY.tsv` | **+2 rows** (CO AG v. EarnIn 2026-08-27; a dated 1033 re-verification row carrying the logged conflict) · the four 7/10 STALE tags on the 1033-arc and HUD-RFI rows **remain correct and are NOT cleared** |

**Next dated trigger written onto both:** Affirm FQ1-27 + Klarna Q3-26, **~2026-11-05 to 2026-11-20**. ⚠️ **That November pass is the LAST one before P01/P03/P04/P05/P07 all come due at 2026-12-31 — five rows at once.** The 9/08 row slipped by 2 days this time; a slip in November costs five gradings. **CARL owns the docket row.**

---

## 4. What CARL must do (ranked, nothing here is self-executing)

1. 🔴 **Grade the NY Fed charge-off-duration finding against CRL-05** — re-instrument onto the flow rate or carry both legs with a named basis. **Route to RED.** Then check the same defect at CRL-03 and the auto rows.
2. 🟠 **Refresh the STATUS BNPL late-rate row 41% → 47%** and **check its CFPB attribution**. Run `consumer_check.py` on the supersession.
3. 🟠 **Refresh KB-CARL-228** with the Affirm FY26 and Klarna Q2-26 primaries above; **update `BNPL_STRESS.tsv`** if it is still live.
4. 🟡 **Resolve P02 → MISS** at FY-close (or say why not).
5. 🟡 **Prune the fired `docket/CATALYSTS.tsv` 2026-09-08 'PHAN SPAWN — OVERDUE' row** and add the **~2026-11-05/20** successor. *(Docket is yours — I did not touch it.)*
6. 🟡 **Update `TEAM.md`** PHAN row: last refresh **2026-09-10**, ledgers **UNFROZEN**, next gate **~Nov**.
7. ⚪ Decide whether the **PHAN inbox** gets a deliberate test or an honest "unused since creation" note.

**Nothing in this pass is trade-shaped.** No position, level, sizing or expression is proposed or implied. If ② or ③ later argues for an expression, it routes CARL → TERRY, not from here.

---
*PHAN, dossier-mode. Live surface `DOSSIER.md`; ledger of record `workbook/PREDICTIONS.tsv`. CLAUDE.md/STATUS.md remain FROZEN at their Apr-2026 vintage and were not touched.*
