# CORAL THESIS — The Coral Bleaching

**Version:** v1.0  
**Installed:** 2026-06-20  
**State:** 🟠 ELEVATED / thesis split — household + condo stress confirmed; bank-loss transmission not confirmed. **Supply-side price-discovery leg 🔴 (Will-ratified 7/23) — collateral repricing via cash capitulation-clearing; scoped to that leg, bank-transmission rail untouched (0-of-≥2).**  
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
