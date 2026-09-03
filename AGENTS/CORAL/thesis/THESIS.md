# CORAL THESIS — The Coral Bleaching

**Version:** **v1.1** *(bumped 2026-08-23 — two rail changes: a new falsify rail for the 🔴 supply-side leg, and a pre-registered grading rule + first-ever grade for the falsify criteria. Core mechanism UNCHANGED from v1.0.)*  
**Installed:** 2026-06-20 · **Rails last reviewed:** 2026-08-23 (Will-approved) · **Next falsify grade: 2026-11-15**  
**State:** 🟠 ELEVATED / thesis split — household + condo stress confirmed; bank-loss transmission not confirmed. **Supply-side price-discovery leg 🔴 (Will-ratified 7/23) — collateral repricing via cash capitulation-clearing; scoped to that leg, bank-transmission rail untouched (0-of-≥2).** **⭐ STAND-DOWN RAIL ADDED 2026-08-23 (Will-ruled): breadth <5-of-5 FL metros with Parcl MSI >6.0 on TWO CONSECUTIVE readings ≥10 DAYS APART ⇒ 🔴→🟠, this leg only. Canonical letter → `STATUS.md` OQ §A. Until 8/23 this leg had a trigger and NO falsifier.**
**Changelog:** `thesis/CHANGELOG.md`

---

## Current Thesis

Florida is not in a clean statewide crash. It is in a **geography-concentrated cost-stack and demand-normalization cycle** where condo/household stress is real, but bank losses have not yet crystallized.

**Working model:**

> Post-Surfside reserve law forces aging condo stock to recapitalize. Special assessments, commercial/condo master-policy insurance, HOA burden, and weaker migration/tourism demand push owners toward forced selling, default, bankruptcy, or association delinquency. The bank leg only becomes tradeable when that household/association stress appears in FL bank NPL/NPA, NCO, reserve, or association-loan data.

**Core distinction:** household/condo stress is confirmed; **bank-loss transmission is not.** Do not turn “Florida real estate is stressed” into “Florida banks are breaking” until bank evidence confirms the bridge.

---

## Core Mechanism — “The Coral Bleaching”

```text
SIRS / reserve funding mandate live Jan 1 2026
  → reserve gaps surface
  → special assessments / association borrowing
  → owner forced selling, strategic default, or bankruptcy
  → association delinquency + cash-flow stress
  → master-loan / condo-association loan stress
  → receivership / termination / bulk-sale path
  → bank loss crystallization
```

**Status:** mechanism intact at the household/condo level; final bank-loss leg delayed.

**Legal bottleneck:** *Biscayne 21* keeps voluntary termination hard where declarations require unanimous consent, making receivership / judicial resolution the live endgame to monitor.

**Calibration warning:** the retired SSB short showed the failure mode — correct mechanism, premature bank-expression timing.

---

## Current Evidence Context as of v1.0

Keep exact live values in `STATUS.md`, `workbook/KB.tsv`, `workbook/VX_Vectors.md`, and `workbook/FLOW_Pathways.md`. Thesis only carries the durable read:

| Channel | Thesis read | Role |
|---|---|---|
| **Condo assessments** | Reserve mandate is live; special assessments are the primary forcing function. | Converts deferred maintenance into immediate household cash need. |
| **Negative equity** | Recent-vintage FL buyers are an upstream collateral canary, especially SW-FL. | Reduces willingness/ability to fund assessments or hold through downturn. |
| **Supply-side price discovery (MSI leg 🔴, 7/23)** | Sustained seller distress (≥5 SW/Central-FL metros MSI >6.0) is clearing via **cash end-user/foreign capitulation** (VX-CORAL-BUYER-01: cash share rising, investor share falling). | **Cash comps mark collateral DOWN → erodes LTV cushion** on the SW-FL collateral behind FL bank books — the collateral-repricing leg *upstream* of the bank bridge. Collateral-side, NOT bank-P&L; does not alone upgrade the bank rail. |
| **Bankruptcy / consumer stress** | Filing acceleration is a consumer canary; volume ranks need per-capita validation. | Complements foreclosure; tests household cost-stack stress. |
| **Insurance split** | Personal/reinsurance easing does **not** equal commercial/condo master-policy easing. | Master-policy costs remain an association cash-flow amplifier. |
| **Migration / tourism** | Demand engine is weaker and geographically uneven. | Stacks with housing stress, especially SW-FL; coordinate values with MARCO. |
| **FL banks** | Q1 2026 did not confirm bank-loss transmission. | Upgrade only on observable credit deterioration, not collateral stress alone. |
| **Property-tax / fiscal** | Nov 3 2026 amendment is two-sided. | Homeowner relief vs local revenue/service stress. |
| **Climate / hurricane / sargassum** | Second-order unless hurricane landfall or severe coastal demand shock. | Can flip insurance or demand channels acute. |

**Insurance writing rule:** never write “insurance easing” without specifying the layer. Personal/reinsurance easing is not condo/commercial master-policy easing.

---

## Confirm / Falsify Criteria

### Confirm / upgrade toward 🔴 bank-transmission

**Bank-upgrade rail:** CORAL does **not** upgrade to 🔴 bank-transmission unless at least **two FL-exposed banks** show synchronized deterioration **or** one pure canary like **USCB** shows explicit condo-association loan deterioration with corroborating consumer/collateral data.

Deterioration means one or more of:

- NPL / NPA migration.
- Realized NCOs.
- Specific reserve builds tied to FL condo, association, CRE, or household collateral stress.
- Classified/current reclass migrating to nonaccrual or loss content.
- Explicit USCB condo-association loan deterioration.

Bridge / corroborating signals that raise pressure but do **not** alone upgrade the bank leg:

- Condo association bankruptcies / receiverships form a visible cluster beyond one-offs, especially if paired with bank credit movement.
- Ch.7 filings in M.D./S.D. Fla exceed the tracked per-capita tripwire and keep accelerating.
- Foreclosure + negative-equity clusters broaden from SW-FL into SE-FL condo collateral.
- Hurricane landfall reverses insurance easing and shocks commercial/condo master-policy costs.

### ⭐ How these are graded (added 2026-08-23, Will-approved — this was missing and it mattered)

**These criteria were written 2026-06-20 and had NEVER been formally graded in either direction.** The overall 🟠 sat unchanged from June to August on **no scored rail** — which is the same defect as a fired signal with no falsifier: *a condition nobody evaluates cannot come back negative.*

- **The criteria below are FROZEN as written. Do not reword them to fit a print.** If one is unmeasurable, mark it UNGRADED and say why; do not substitute a proxy silently.
- **Grade on a DATE, not on a feeling** — at each formal grade, score every criterion MET / NOT MET / HALF / UNGRADED and record it with its evidence.
- **A criterion with no live instrument is a defect, not a pass.** (Bankruptcy per-capita went untracked from June to August and was neither met nor refuted — it was simply unobserved.)

### ⛔ REGISTRATION AT FIRE-TIME — the owner's one-line duty (WQ-86 RULED, Will 2026-09-01: *"approve all of those with your recs"*)

**At ratification or fire of ANY CORAL gate/threshold, the SAME SESSION packets `PROME/inbox/` (repo ROOT — never `AGENTS/PROME/`) with four fields: `gate_id` · `condition` · `consequence` · `consumed_by`.** PROME registers the row in `PROME/GATES.tsv`; CORAL keeps the canonical letter on its own surface (PAT-006).

- **This is CORAL's half of a two-sided join, not apportionment.** The registrar's half: a GATES row naming a non-self owner is **undelivered until that owner has a read-path**. Each end's own audit passes clean while nobody owns the join — which is why it is written down on both sides.
- ⭐ **Why this exists, on this desk's own record: `GATE-CORAL-MSI-01` fired 2026-07-23 and went 31 DAYS UNREGISTERED.** A leg can be live, Will-ratified and load-bearing while invisible to the fleet ledger that exists to catch exactly that.
- **A grade or a state-change on an already-registered gate carries the same duty** — packet the reading with a confirmed-or-re-dated `review_by` and the next `consumed_by`, so the row never goes stale-by-silence. *(Discharged 2026-09-02 for MSI reading #5.)*
- ⚠️ **Ordering discipline, stated because the first grade violated it:** the 2026-08-23 grade below was made *openly, from data already in hand*, and only then was this decision rule written. **That ordering is backwards and is recorded rather than hidden.** From the next grade onward the decision rule is pre-registered and the criteria are frozen, so the ordering weakness does not recur.

**PRE-REGISTERED DECISION RULE (filed 2026-08-23, before the next grading date):**
> Of the six falsify criteria: **≥4 MET ⇒ 🟠→🟡 candidate, route to Will** · **2–3 MET ⇒ HOLD 🟠 and name which** · **≤1 MET ⇒ 🟠 holds unqualified.**
> **A HALF-MET criterion counts as 0.5.** **UNGRADED counts as 0 and obliges an instrument note, not a shrug.**
> ⛔ **No criterion may be reworded, split or merged at grading time.** A criterion that turns out to be badly specified is flagged for amendment *between* grades, never during one.
> **Next formal grade: 2026-11-15** (after Nov-3 Amendment 3 and inside the Q3-bank-print aftermath). Earlier only if ≥2 criteria change state on a single print.

**GRADE OF RECORD — 2026-08-23 (first ever; see the ordering caveat above):**

| # | Criterion (abbreviated — full text below) | Grade | Evidence |
|---|---|---|---|
| 1 | Q2/Q3 banks keep curing | **HALF (0.5)** | Q2 closed **7-of-7 benign**, sharpest pre-registered tell falsified in the opposite direction, REGINALD 10-Q watch-card **4-of-4 REVERT**. **Q3 does not print until ~late Oct** — the criterion names Q2 *and* Q3 and only half exists. |
| 2 | Classified CRE stays rate-shock reclass, not loss content | **MET (1.0)** | Held all year across the FL cohort; no loss content emerged in the Q2 sweep. |
| 3 | Condo inventory tightens **and** price stabilizes **without forced-sale acceleration** | **NOT MET (0)** | Inventory ✓ (**8.9→8.6→8.1→7.8**, 4 straight) and price ✓ (**0.0% YoY**, off −6.1% Apr) — **but the third clause FAILS: REO +33% H1 and the 🔴 MSI leg is live.** All three clauses must hold. |
| 4 | Personal **and** commercial master-policy layers ease materially | **NOT MET (0)** | Personal has **stopped easing** (Citizens personal **+138** in July, six weeks flat); commercial/condo-association layer still rising (+10.4% capped). The conjunction fails on both halves. |
| 5 | Bankruptcy acceleration fades per-capita | **UNGRADED (0)** | ⚠️ **Untracked June→August.** Neither met nor refuted — unobserved. **Instrument note owed:** Ch.7 per-capita M.D./S.D. Fla, tripwire >~230/100k. |
| 6 | Property-tax relief lowers carrying cost | **PENDING (0)** | Resolves **Nov 3**; Amendment-3 ruling still unlocated, pre-reg ML-CORAL-042 unresolved. |

**SCORE: 1.5 of 6 ⇒ HOLD 🟠.** Under the rule above this is the *"2–3 MET"* band's lower edge and **does not approach a downgrade** — but it is the first time the number has existed at all, and **two criteria (1, 2) are moving toward falsification while two (3, 4) are firmly against it.** ⭐ **The honest read: the thesis split is not weakening, it is SHARPENING — the bank half keeps curing while the household/collateral half does not.**

⚠️ **Cross-check against the winter composite (ML-CORAL-043), which is a separate and stricter test:** two of its five legs are currently moving AWAY from firing (leg 5 needs inventory to re-widen **>9.5mo**, it went to **7.8**; leg 2 needs condo median YoY **<−5%**, it is **0.0%**). **Not graded — the window is Dec-26→Feb-27 and grading early is exactly the re-fit its spec forbids** — but the two tests are pointing the same way and that agreement is worth carrying.

### Falsify / downgrade toward 🟡

- Q2/Q3 banks keep curing: low NCOs, stable/improving NPLs, no reserve build.
- Classified CRE remains current/rate-shock reclassification rather than loss content.
- Condo inventory tightens and price declines stabilize without forced-sale acceleration.
- Personal **and** commercial/condo master-policy layers ease materially.
- Bankruptcy acceleration fades on a per-capita basis.
- Property-tax relief materially lowers household carrying-cost pressure without offsetting fiscal/service backlash.

---

## Timing Gates

| Gate | When | What decides |
|---|---:|---|
| **Q2 FL bank earnings** | Late Jul 2026 | First clean retest of bank transmission after reserve mandate + spring stress. |
| **Fresh foreclosure / bankruptcy updates** | Monthly / quarterly | Whether household stress is accelerating or plateauing. |
| **Hurricane season** | Through Nov 30 2026 | Landfall risk can reverse insurance-easing channel. |
| **Property-tax amendment** | Nov 3 2026 | Carrying-cost relief vs municipal/fiscal stress. |
| **Winter snowbird / assessment season** | Winter 2026-27 | Demand and cash-flow stress retest when seasonal owners face carrying costs. |

---

## Agent Boundaries / Source-of-Truth Rules

| Domain | Owner rule |
|---|---|
| **MARCO** | Owns national population-flow framing and live FL migration/tourism/snowbird metrics. CORAL can use shared metrics only after reconciling to one number. |
| **REGINALD** | Owns national/regional-bank convergence. CORAL owns FL bank-level reads and loss estimates; REGINALD integrates them. |
| **CARL** | Owns consumer-credit system read. CORAL sends assessment/insurance/bankruptcy pressure as FL household cash-flow input. |
| **NEXUS** | Owns cross-agent synthesis. CORAL provides geography-convergence view, not every raw metric. |

**Rule:** one source of truth per metric. If CORAL and MARCO carry the same FL condo inventory / migration / tourism number, reconcile before publishing.

---

## What Belongs Where

| Doc | Owns |
|---|---|
| **`thesis/THESIS.md`** | Mechanism, confirm/falsify rails, timing gates, ownership rules. Change only when the thesis changes. |
| **`thesis/CHANGELOG.md`** | Standalone history of major thesis moves and retired frames. |
| **`STATUS.md`** | Current levels, latest dashboard, live operating view. |
| **`workbook/KB.tsv`** | Permanent timestamped fact ledger. |
| **`workbook/VX_Vectors.md`** | Indicator thresholds and current vector state. |
| **`workbook/FLOW_Pathways.md`** | Transmission mechanics and pathway changes. |
| **`SCRATCH.md`** | Session handoff only. |
| **`NEXUS_BRIEF.md`** | Cross-agent surface: sends, waits, synthesis. |

**Reference rule:** Reference this file from `STATUS.md`, `CLAUDE.md`, and `NEXUS_BRIEF.md`; do not duplicate the whole thesis into live dashboards.
