# CORAL Thesis Changelog

**Installed:** 2026-06-20  
**Purpose:** Standalone history of major thesis moves and retired frames.

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
