# CORAL Thesis Changelog

**Installed:** 2026-06-20  
**Purpose:** Standalone history of major thesis moves and retired frames.

---

## 2026-09-28 (latest) — Will RULED WQ-322 (option E): the ~230/260 bankruptcy LEVEL trigger is retired, not replaced

**Trigger:** confirm-side rail change, ruled by Will directly in the CORAL session.

| Item | Old | New |
|---|---|---|
| Bankruptcy level trigger (THESIS bridge signal L80; VX-CORAL-BKCY-01) | 🟠 >~230 / 🔴 >260 per 100k, labelled "Ch.7 M.D.+S.D." | **RETIRED, prospectively.** History kept (struck through): the label and the June ~190 anchor were different bases; the derivation is undocumented (`51475a00c`). **No 250/283 substitute, no replacement ratio threshold.** |
| Reporting | mixed bases | All chapters, M.D.+S.D., 44-county Census denominator (WQ-321 basis): per-capita level, growth and US comparison, each with coverage stated |
| Growth-warning rule (VX: 🟠 >20% YoY sustained / 🔴 >30% + bank NCO move) | — | **Retained, thresholds unchanged, NOT validated by this ruling.** A growth warning alone is not proof of broad household stress or of bank-loss transmission. |

**Unchanged:** criterion-5 slowing test (WQ-321 leg A/B), the 11/15 grade date and rule, overall 🟠, bank rail NOT met, NOT armed. **No retrospective regrading.**

## 2026-09-28 (later) — Will RULED WQ-241 and WQ-321: MSI re-fire + level guard installed; criterion 5 operationalized; tripwire rebase NOT approved

**Trigger:** confirm/falsify rail change (Will-ruled ~15:1x ET; verbatim record `PROME/WILL_QUEUE.md`, PROME commit `c0cfe7ba6`).

| Item | Old | New | Why |
|---|---|---|---|
| **GATE-CORAL-MSI-01** | 8/23 letter: stand-down only, no re-fire, count-based (fired 9/13 with Cape Coral 0.09 under) | **Amended letter (STATUS OQ §A):** re-fire = all five > 6.00; stand-down = the SAME metro < 5.90; **5.90–6.00 = policy buffer**; persistence clock from the FIRST qualifying reading's stamp, intervening qualifying readings preserve it, confirmation ≥10 days observed, a failing reading resets; reading identity by page stamp | CATO review `7522e6dcf` + Will's two amendments (no noise-probability claim for the band; first-reading clock) |
| **Criterion 5 scoring** | UNGRADED, no operational definition | **Leg A absolute, scored** (per-capita YoY ≥5pp below prior-four-table max, two consecutive tables); **leg B relative, reported only** — *prospective policy choice, not a statistically validated threshold* | WQ-321 |
| **Confirm-side ~230/260 tripwire** | "Ch.7 M.D./S.D. >~230" | **Unchanged, FLAGGED:** label and June anchor disagree; derivation undocumented → **WQ-322** (Will, separate) | Will declined the ≈250/283 rebase |

**Unchanged:** MSI leg 🟠 (reading #7 is in the band — neither re-fire nor stand-down); overall 🟠; bank rail NOT met, NOT armed; criterion text, 11/15 date and decision rule; **no retrospective regrading of anything.**

## 2026-09-28 — Two falsify criteria instrumented; one pre-registration graded; no rail moved

**Trigger:** rail-adjacent changes under the write-back rule — an UNGRADED criterion got a live instrument, and a pre-registered branch read resolved.

| Item | Old view | New view | Why | Implication |
|---|---|---|---|---|
| **Criterion 5 (bankruptcy fades per-capita)** | UNGRADED (0), no instrument since June | **Instrumented** (`tools/bkcy/`, AOUSC F-2 + Census V2025): M.D.+S.D. 217.1/100k, +21.2% YoY, FL/US 1.205×→1.231× | OQ H; DAEDALUS PR#6 neg-res ask | Points NOT MET on every candidate basis. **Two spec defects (basis label vs its ~190 anchor; "fades" has no number) go to Will BETWEEN grades — not resolved here, and not re-fit at 11/15.** |
| **Criterion 6 (property-tax relief)** | pending, ruling unlocated | Instrument named: Division of Elections certified Ballot No. 3 result, dated 2026-11-04 | DAEDALUS neg-res ask | Resolves at 11/4, feeds 11/15. |
| **ML-CORAL-042 (Amendment 3 branch read)** | UNRESOLVED since 7/29 | **Branch A (rewrite ordered 8/3, no appeal) ⇒ pillar-9 row "leaning FAIL"** | Ruling located 9/28 via AG letter (P1) | Prior re-weight only — **not a rail or thesis move** (per its own letter). ⚠️ Graded on the letter; the rationale (rewrite injects fiscal language) is **not visibly what happened** — recorded, not re-fit. |
| **MSI leg** | 🟠 since 9/13 | 🟠 — reading #7 (9/28) 4-of-5; no rule applies | 8/23 letter has no re-fire | Re-fire + level-guard proposal to Will (WQ-241), prospective. |

**Unchanged:** overall 🟠; bank-transmission rail NOT met, NOT armed; core mechanism; the 11/15 decision rule.

## 2026-09-13 — The falsify rail installed on 8/23 RESOLVED on its first live test, and firing it exposed a defect in its own construction

**Trigger:** rail change under the write-back rule — a registered confirm/falsify rail **resolved**, and the resolution moved a leg's colour.

### ① THE 8/23 STAND-DOWN RAIL FIRED — 🔴→🟠 on the supply-side price-discovery leg

**Old view:** the leg was 🔴 (fired 7/23, Will-ratified), with the 8/23 stand-down rail installed and a clock started 9/2 by a first sub-threshold reading (3-of-5).
**New view:** reading #6 on **2026-09-13** came in at **4-of-5 >6.0** — **<5-of-5**, therefore the second consecutive sub-threshold reading, **11 days** after the first by observation and **10 days** by page vintage (≥10 on both clocks), with no reading in between. **The Will-ratified condition is MET ⇒ 🔴→🟠, supply-side price-discovery leg ONLY.**
**Why it matters procedurally:** this is the **first time any CORAL rail has resolved in the direction of retiring a signal.** It was graded mechanically off a letter frozen on 8/23 — **before the data turned** — which is precisely what made today an arithmetic exercise rather than a judgement call.
**Implication:** ⛔ **Scope unchanged in both directions. CORAL's overall state stays 🟠 and the bank-transmission rail stays NOT met, NOT armed.** A supply-side leg standing down is not a Florida all-clear and says nothing about bank transmission.

### ② ⚠️ THE RAIL IS DEFECTIVE — it guards SPACING but not LEVEL, and the defect only became visible by firing

**What happened:** the leg stood down while its own series moved the **other way**. Between readings **three of five metros ROSE**, **Lakeland re-crossed back above 6.0** (5.97 → 6.01), and **Tampa printed the highest MSI in the series** (7.15). **Breadth failed on Cape Coral alone, 0.09 below the line.**
**The defect:** the 8/23 letter was written to refuse a rounding-error de-fire, and it **has now produced one by a different route.** It guards the **TIME** dimension (≥10-day spacing, the anti-noise leg) and leaves the **LEVEL** dimension unguarded — so a **single laggard metro a rounding-distance under 6.0 can hold a stand-down open indefinitely while the other four strengthen.** Breadth is a count; a count cannot see that four of five went up.
**⛔ What was NOT done about it:** nothing, today. **The grade stands as the letter gives it.** Re-fitting a rule at the grading table because its answer is inconvenient is the exact failure pre-registration exists to prevent, and it is the failure the 8/23 entry above was written to avoid. **CORAL proposes; Will rules; any amendment is PROSPECTIVE.** Registered as `STATUS.md` OQ S and escalated to PROME 2026-09-13.

### ③ THE MIRROR GAP IS NOW LIVE — a stand-down with no RE-FIRE condition

**Old view (8/23):** *"a trigger with no falsifier cannot be honestly retired when the data turns."* That gap was closed.
**New view:** the letter registers a **stand-down and no re-fire.** If breadth returns to 5-of-5 tomorrow, **there is no registered rule to take the leg back to 🔴** — and improvising one at that moment would be the 8/23 error with the sign flipped. ⭐ **The generalisable lesson: installing a falsifier on a fired signal creates a NEW unfalsifiable state — the stood-down one.** Rails need to close the loop, not just open the exit. **Named, not self-answered** (OQ S, with the rule defect).

### ④ Inference discipline held at the grading table

The rising MSI is recorded as a **measured value**, not as "seller stress is intensifying." **Rival mechanism moving the statistic the same way:** a more-distressed *remaining listing pool* (composition) vs *more motivated sellers* (breadth) — the index level cannot separate them, and **the discriminator is unit volume**, which Parcl stopped serving (now a literal `0` placeholder, ML-CORAL-079). **The causal upgrade is declined and the gap is named** rather than bridged with the adjacent number.

---

## 2026-08-23 — Two rail changes, and the first grading the falsify criteria have ever had

**Trigger:** Will-approved thesis-rail pass after a 20-day dark period. Two of the three items below are **rail changes** under the write-back rule ("confirm/falsify rail change"); the third is a governance fix to how rails are read at all. *(⚠️ Note against this file's own record: it had gone unwritten since **2026-03-03** — five months — across a leg firing 🔴, a bank window closing 7-of-7, and a new financing channel opening. A changelog that skips the moves it exists to record is a defect in itself.)*

### ① NEW FALSIFY RAIL — the 🔴 supply-side leg finally has one

**Old view:** the supply-side price-discovery leg fired 🟠→🔴 on 7/23 on a Will-ratified breadth+sustain condition, and `OQ#0` was closed RATIFIED-FIRED. **Nothing was ever registered that could un-fire it.**
**New view (Will-ruled 2026-08-23, CORAL's proposed form accepted unamended):** **breadth <5-of-5 FL metros with Parcl MSI >6.0, on TWO CONSECUTIVE readings ≥10 DAYS APART ⇒ 🔴→🟠.** Both legs bind; the ≥10d spacing is the anti-noise leg. Scoped to this leg only — bank rail and overall state untouched in both directions.
**Why:** on the 8/23 reading Cape Coral (**6.02**) and Lakeland (**6.03**) sat **0.03** from the threshold with 4-of-5 drifting down a second time. A trigger with no falsifier cannot be honestly retired when the data turns; improvising one at that moment is re-fitting a frozen frame after seeing the print. **Both errors were live simultaneously and only a pre-registered rule avoided both.**
**Implication:** the leg's 🔴 is now falsifiable and dated. **Clock has NOT started** (8/23 was 5-of-5); earliest conceivable stand-down **≈2026-09-12**. Canonical letter at `STATUS.md` OQ §A; `PROME/GATES.tsv` holds a pointer and CORAL's surface governs (PAT-006).

### ② THE FALSIFY CRITERIA WERE NEVER GRADED — first grade of record, plus a pre-registered decision rule

**Old view:** six "Falsify / downgrade toward 🟡" criteria, installed 2026-06-20, treated as live rails.
**New view:** they had **never been scored in either direction.** The overall 🟠 sat unchanged June→August on **no graded rail** — the same defect as a fired signal with no falsifier: *a condition nobody evaluates cannot come back negative.*
**Why it surfaced:** the falsifier sweep Will approved after the MSI gap. Generalising the question *"can this come back negative?"* from one leg to the whole thesis is what exposed it.
**Grade of record 2026-08-23: 1.5 of 6 ⇒ HOLD 🟠** — criterion 2 MET, criterion 1 HALF (Q2 cured 7-of-7 but Q3 does not print until ~late Oct), criteria 3 and 4 firmly NOT MET, criterion 5 **UNGRADED because untracked since June**, criterion 6 pending Nov 3.
**Implication — and this is the substantive read, not the bookkeeping:** ⭐ **the thesis split is not weakening, it is SHARPENING.** The bank half keeps curing (Q2 7-of-7 benign, sharpest tell falsified in the opposite direction, REGINALD's 10-Q watch-card 4-of-4 REVERT) while the household/collateral half does not (REO +33%, 🔴 MSI live, personal-lines depopulation stopped, commercial master-policy still rising). **No state change. A decision rule is now pre-registered for the next grade (2026-11-15) so the score cannot be reverse-engineered from a print.**
⚠️ **Recorded honestly: the 8/23 grade was made from data in hand and the decision rule written afterward. That ordering is backwards, it is stated in `THESIS.md` rather than hidden, and it does not recur — the rule is filed before the next grade.**

### ③ Two mechanism revisions inside the existing rails (no rail moved)

- **GSE financing channel upgraded PRESS-TIER → ISSUER PRIMARY, and its binding FL constraint RELOCATED.** The $10,000/unit unfunded-repair test is confirmed verbatim (`B4-2.1-03` v.08/05/2026) but is **a floor on the channel, not a description of it**: the route that binds first in Florida carries **no dollar amount** — *"failed to pass state, county, or other jurisdictional mandatory inspections… structural safety, soundness, and habitability"* — which FL's milestone/SIRS regime trips by construction. **A dollar-threshold model understates FL exposure.** Fifth route added: a master policy with a **per-unit deductible >$50,000** is non-warrantable on its own, wiring the insurance pillar directly into warrantability.
- ⛔ **A claim was drafted and RETRACTED the same session — recorded because the retraction is the useful part.** CORAL wrote that the rising blended median's composition shift *is* the Coral Bleaching mechanism (the vintage low end having stopped clearing). **Withdrawn:** a low-end *freeze* and a high-end *surge* both raise a median, all the evidence in hand was the surge, and the primary came back **mildly disconfirming** (average sale price +2.7% against a **flat** median = fattening right tail; sales +11.0% and cash sales +14.9% is not a frozen low end; a real freeze would have pushed the median **up** and it did not move). **Kept only in its narrow form: the blended medians OVERSTATE price health.** Resolution path: condo unit sales by **price band**, sub-$300K — **units, never share**, because a high-end surge cuts the low end's share with zero low-end units lost.

---

## 2026-03-03 — Red bank-cascade / SSB short frame

**Prior frame:** CORAL carried a more acute 🔴 bank-cascade read centered on Florida condo stress transmitting quickly into FL-exposed regional banks, with SSB framed as a short candidate.

**Mechanism then:**
- Surfside reserve law → assessment shock.
- Owner default / association failure → bank collateral and association-loan losses.
- FL bank exposure, especially SSB/VLY/SBCF/BKU, expected to show loss content soon.

**Status now:** superseded by the 2026-06-19 thesis split. The mechanism remains useful; the timing/expression was premature.

---

## 2026-06-19 — Thesis split installed in operating view

**Move:** CORAL downgraded from 🔴 immediate bank cascade to 🟠 thesis split.

**New read:**
- Household/condo stress is confirming.
- Bank-loss transmission is not confirmed in Q1 2026.
- The durable question is no longer “is Florida stressed?” but “when, if ever, does household/association stress hit bank P&L?”

**Evidence carried in live files:** foreclosure acceleration, condo price weakness, reserve-mandate pressure, and Q1 2026 FL bank credit stability. Exact levels live in `STATUS.md` and `workbook/VX_Vectors.md`.

---

## 2026-06-19 — Insurance channel reclassified into split read

**Old risk:** insurance was too easy to summarize incorrectly as either “the amplifier is easing” or “insurance remains a crisis.”

**New classification:** split channel.

| Layer | Read | Thesis effect |
|---|---|---|
| Personal lines / Citizens personal / reinsurance | Easing. | Counterweight to acute-crash frame. |
| Commercial / condo-association master-policy layer | Still rising / sticky. | Assessment, HOA, and association cash-flow amplifier remains live. |

**Rule added:** never write “insurance easing” without specifying the layer.

---

## 2026-06-20 — Recent-vintage negative equity added as upstream collateral canary

**Move:** Added negative equity as an upstream collateral/behavior canary.

**Why it matters:** Negative equity is the missing precondition between price declines and default behavior. Recent buyers underwater are less able or willing to fund special assessments or wait through a condo/SF downturn.

**Boundary:** upstream collateral stress, not bank P&L evidence yet.

---

## 2026-06-20 — Bankruptcy filings added as consumer canary, with per-capita caveat

**Move:** Added bankruptcy filings as household stress evidence.

**Finding:** district volume ranks are real but population-inflated. The better signal is acceleration and per-capita pressure, especially Ch.7 in M.D./S.D. Fla.

**Boundary:** bankruptcy confirms household stress pressure; bank transmission still requires bank credit metrics or association-loan deterioration.

---

## 2026-06-20 — SSB short retired / bank-loss transmission delayed

**Move:** SSB short thesis explicitly retired.

**Why:** Q1 2026 evidence broke the tradeable bank-short expression even though the underlying Florida household mechanism remains intact.

**Lesson:** do not short the bank leg on collateral/household stress alone. Upgrade only when bank data show synchronized deterioration across at least two FL-exposed banks, or one pure canary like USCB shows explicit condo-association loan deterioration with corroborating consumer/collateral data.

**New timing:** bank-leg retest moves to Q2 2026 earnings and winter 2026-27 seasonal/assessment window.

---

## 2026-07-23 — Supply-side price-discovery leg upgraded 🟠→🔴 (Will-ratified)

**Move:** the **supply-side price-discovery leg** of the housing pillar upgraded 🟠→🔴. Scoped to this leg only — the **bank-transmission rail is untouched (stays 0-of-≥2)** and the overall CORAL state stays 🟠 thesis-split.

**Trigger (pre-registered 6/26, armed 7/21, sustain-confirmed + ratified 7/23):** Parcl Motivated-Seller Index ≥5 FL metros >6.0 sustained ≥2 weeks. Fired on the 7/23 fresh pull — Tampa 6.96 / Punta Gorda 6.82 / North Port 6.45 / Cape Coral 6.2 / Lakeland 6.09, still ≥5 >6.0 ~15 days after the 7/8 snapshot (values drifted vs 7/8 = fresh read). **Documented substitution:** metro-level all-seller MSI, not the builder-cell basis the tripwire was seeded on (noted, not silent). Will ratified in-session 7/23 ~1:35 PM ET.

**Why it matters (LTV-transmission link — the durable point):** the buyer-composition read (VX-CORAL-BUYER-01) shows the absorption mechanism is **cash end-user / foreign capitulation-clearing** (cash share rising, investor share falling) — i.e., distressed inventory is clearing at **cut prices via real money**, not investor knife-catching. Cash transactions **set appraisal comps**, so capitulation-clearing **marks collateral values DOWN** → erodes LTV on the SW-FL collateral behind the FL-bank books. This is the **collateral-repricing leg upstream of the bank-loss bridge** — it lowers the cushion that has kept the bank leg curing (rate-shock reclass with intact LTVs).

**Boundary (unchanged):** this is collateral-side, NOT bank-P&L evidence. It does not upgrade the bank-transmission rail by itself — it lowers the collateral cushion that would absorb a future migration. Bank leg still upgrades only on ≥2 synchronized FL-bank credit deteriorations or USCB condo-assoc cracking.

**Implication:** the winter-26/27 composite gains a confirmed 🔴 leg; the price-discovery-at-lower-clearing-levels dynamic is now the live SW-FL collateral markdown feeding (eventually) into bank LTV.

---

## Pending / next changelog entries to resolve

- Whether Q2 2026 FL bank prints confirm or falsify bank transmission.
- Whether commercial/condo insurance remains sticky despite personal/reinsurance easing.
- Whether the Nov 3 2026 property-tax amendment passes and changes household carrying-cost math.
- Whether receivership / termination cases broaden beyond *Biscayne 21*.
