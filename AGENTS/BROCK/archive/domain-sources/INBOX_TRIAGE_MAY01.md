# Inbox Triage — May 1, 2026 (Apr 1 → Apr 20 catch-up)

**Context:** 17 inbox signals processed during catch-up Phase 1. This file is the input list for Phase 2 (KB.tsv backfill) and Phase 3 (PREDICTIONS update).

**Date range covered:** Apr 2 — Apr 20, 2026
**Disposition:** All 17 → `inbox/processed/` after this triage

---

## CLASSIFICATION TABLE

| # | File | Date | Category | Disposition | Phase 2/3 Action |
|---|------|------|----------|-------------|------------------|
| 1 | `2026-04-10_from-LIQUID_pc-stage3-cascade-no-fed-put.md` | Apr 10 | Frame confirmation | Integrate | KB row: "no Fed put + no synthetic price discovery" cluster |
| 2 | `HAWK_2026-04-20_imf-private-credit-confirm.md` | Apr 20 | Top-down validation | Integrate | KB row: IMF GFSR explicit naming of PC |
| 3 | `SIG-2026-04-02-002.md` (Jackson Pebbles II + 4 sub-signals) | Apr 2 | High-density facts | **Multiple KB rows** | See breakout below |
| 4 | `SIG-2026-04-02-003.md` (PE recap, Goldman TRS pause, software 32%, Congress, KPMG, Goeasy) | Apr 2 | High-density facts | **Multiple KB rows** | See breakout below |
| 5 | `SIG-W-20260414-002-tcw-red-lobster-98-writedown.md` | Apr 14 | **Stage 3 predecessor** | Integrate (HIGH) | KB row: Red Lobster equity-debt mark dislocation |
| 6 | `SIG-W-20260414-004-imf-gfsr-liquidity-dysfunction.md` | Apr 14 | Top-down validation | Integrate | KB row: IMF GFSR multi-driver framework |
| 7 | `SIG-W-20260414-005-road-to-housing-act-freddie-k098.md` | Apr 14 | REGINALD primary | **Skip BROCK KB** | Note adjacency only; defer to REGINALD |
| 8 | `SIG-W-20260414-006-gs-prime-hf-short-cover-whipsaw.md` | Apr 14 | HENRY primary | **Skip BROCK KB** | Position-mismatch context only |
| 9 | `owl-gating-apr2.md` | Apr 2 | Already in STATUS_ARCHIVE_APR10 | Skip | Already integrated |
| 10 | `research_2026-04-06_wal_jefferies_deep_dive.md` | Apr 6 | OZK/REGINALD primary | **Skip BROCK KB** | Pattern reference only |
| 11 | `signal_2026-04-06_cre_refinancing_wall.md` | Apr 6 | REGINALD primary | **Skip BROCK KB** | CRE→PC adjacency note |
| 12 | `signal_2026-04-06_goldman_pc_redemptions.md` | Apr 6 | BROCK primary | Integrate | KB row: Goldman PC outlier |
| 13 | `signal_2026-04-06_holdout_trade.md` | Apr 6 | BROCK primary | Integrate | KB row: LME 41¢ vs Ch11 68¢ recovery |
| 14 | `signal_2026-04-06_pc_insurance_transmission.md` | Apr 6 | BROCK primary | Integrate | KB row: phantom reinsurance + Gober Seven Funnels |
| 15 | `signal_2026-04-06_pc_meltdown.md` | Apr 6 | Already in STATUS_ARCHIVE_APR10 | Skip | Already in gate tracker |
| 16 | `signal_2026-04-06_wal_litigation.md` | Apr 6 | OZK/REGINALD primary | **Skip BROCK KB** | "Honest marks via litigation" pattern noted only |
| 17 | `sweep_2026-04-03_1419.md` | Apr 3 | News sweep | Partial integrate | KB row: Apollo/Athene FHLB #2 borrower (insurance/PC linkage) |

---

## HIGH-VALUE FACT EXTRACTION (for Phase 2 KB backfill)

### CLUSTER A: Stage 3 predecessor evidence (HIGHEST priority)

**A1. Red Lobster equity-debt mark dislocation [SIG-W-20260414-002]**
- TCW Private Credit Fund slashed Red Lobster equity by **98%**
- Corresponding **PIK'ing private credit loan maturing 2029 marked at PAR**
- Bloomberg-confirmed (Anders Melin & Eliza Ronalds-Hannon, Apr 14)
- @junkbondinvest framing: "Equity at zero and debt at 100 in the same company"
- **Why critical:** This IS the mark-to-model fiction — predecessor condition for arms-length fire sale at 85-90¢. Stage 3 trigger needs the loan mark to catch down.
- **Conf:** A2 EMPIRICAL (Bloomberg primary)

**A2. IMF GFSR April 2026 explicit private-credit naming [SIG-W-20260414-004 + HAWK confirm]**
- IMF formally names private credit as one of 7 vulnerability channels (alongside ME, NBFIs, AI borrowers, EM flows, tokenization, FX)
- Hard data cited: global equities -8% since Feb, sovereign yields rising sharply
- Concrete prescription: "stand up and prepare liquidity and funding facilities"
- **Why critical:** Top-down validation from highest authority. Rare for IMF to call for facility preparation.
- **Conf:** A1 EMPIRICAL (IMF.org primary)

### CLUSTER B: Gates & redemption intensity

**B1. FT/Stanger Q1 redemption book [SIG-2026-04-02-002 SIGNAL D]**
- $7.5B+ Q1 2026 redemption requests aggregate non-traded PC
- MS 10.9%, Ares 11.0%, Apollo 11.2% — **all doubled** from prior quarter
- Every one of 12 largest funds saw acceleration
- First-time appearance of "unmet redemptions" chart bar
- **Conf:** A2 EMPIRICAL (FT/Stanger via Jackson)

**B2. Goldman PC outlier [signal_2026-04-06_goldman_pc_redemptions]**
- Goldman <5% Q1 redemptions vs 10-40% peers
- Bifurcation: institutional vs retail base, mark-smoothing, asset mix
- Open question: genuine strength or hidden stress?
- **Conf:** B2 EMPIRICAL (PYMNTS/Reuters)

### CLUSTER C: Defaults & recovery

**C1. PC vs syndicated recovery gap [SIG-2026-04-02-002]**
- PC direct loans recover **33¢**
- Syndicated loans recover **52¢**
- Gap = 36% lower despite "seniority + covenants" claims
- **Conf:** A2 EMPIRICAL (Bloomberg via Jackson)

**C2. PIK-to-default dominant pipeline [SIG-2026-04-02-002]**
- Fitch: **PIK deferrals drove 60% of all PC defaults in last 12 months**
- FSK has 83 PIK holdings
- 17 companies already in BOTH non-accrual AND PIK states
- **Conf:** A2 EMPIRICAL (Fitch via Jackson)

**C3. Holdout trade — software LME mechanics [signal_2026-04-06_holdout_trade]**
- LME → filing recovery: ~41¢
- Straight Ch11: ~68¢
- Sponsors using NDAs to silo lenders, prevent coordination
- Vibrantz Technologies (American Securities) = case
- Harvard Law: majority of coercive restructurings file anyway
- **Conf:** B2 EMPIRICAL (Credit Weekly, Harvard Law)

### CLUSTER D: Concentration & contagion

**D1. Spotless Brands in 7 BDCs [SIG-2026-04-02-002]**
- One car wash chain across 7 BDC funds
- Single deterioration = 7 simultaneous markdowns
- Confirms KB-BRK-031 cross-BDC concentration thesis
- **Conf:** B2 EMPIRICAL (Jackson)

**D2. Pluralsight named precedent [SIG-2026-04-02-002]**
- Vista bought, levered, **$803M to non-accrual**
- Lenders took 100% ownership; **Vista $4B equity to zero**
- Multiple BDC fund cascading losses
- "This is not a bug. It's the architecture."
- **Conf:** A2 EMPIRICAL (Jackson)

**D3. Software = 32.2% of leveraged loan index by volume [SIG-2026-04-02-003 SIGNAL H]**
- Software 21.2% by count, 1.5x avg loan size
- KBRA forecast: software dominates defaults proportionally above allocation
- **Conf:** B2 EMPIRICAL (LCD/Pitchbook + KBRA)

### CLUSTER E: Pension/insurance contagion

**E1. CPP/Antares pension contagion [SIG-2026-04-02-002]**
- CPP Investments (C$777B, Canada's largest) owns Antares Capital
- 70 companies in both Antares and gated BDC books
- "Same loans. Different doors. Same room."
- **Conf:** B2 EMPIRICAL (Jackson)

**E2. Global pension PC exposure map [SIG-2026-04-02-002]**
- Japan life insurers: $26-78B
- AustralianSuper: tripling A$5B → A$15B
- South Korea NPS: $1.1B + NYC office
- UK pensions: 15-20% PC allocation
- **Netherlands MOST COMBUSTIBLE** — DB→DC switch Jan 1 2026 makes losses individually visible to members; political pressure for forced liquidation
- **Conf:** B2 EMPIRICAL (Jackson)

**E3. Phantom reinsurance / Seven Funnels [signal_2026-04-06_pc_insurance_transmission]**
- 7 reinsurers back 550 carriers — "all insolvent" per Gober
- $1.54T affiliated paper, 6.7% cushion on $10T balance sheet
- 5% surrender rate = system break
- Mechanism: PC downgrades → capital calls → reinsurance contracts fail → unwind
- **Conf:** C3 ASSUMPTION (YouTube/Gober — needs corroboration but pattern is consistent with FY2025 statutory data)

**E4. Apollo/Athene FHLB #2 borrower [sweep_2026-04-03]**
- Apollo's insurance arm (Athene) now second-largest FHLB borrower
- Federal Home Loan Bank as funding vehicle for PC carry trade
- **Conf:** A2 EMPIRICAL (Bloomberg)

### CLUSTER F: Regulatory/political escalation

**F1. Powell "not a systemic event" Apr 3 [SIG-2026-04-02 LIQUID summary]**
- Fed Chair explicit framing — Fed put withheld
- Combined with Goldman TRS pause = no synthetic price discovery either
- Floor removed in both directions
- **Conf:** A1 EMPIRICAL (Yahoo Finance / Powell direct)

**F2. Goldman TRS leveraged-loan short PAUSED [SIG-2026-04-02-003 SIGNAL G]**
- GS pitched HFs total return swap to short $1.4T leveraged loan market
- Now told clients "not yet ready" — paused
- Distressed software loans swelled $18B in weeks
- ABX analog withheld; Gorton transition vertical when launched
- **Conf:** A2 EMPIRICAL (Bloomberg)

**F3. Congressional grilling BX/Ares/APO/KKR [SIG-2026-04-02-003 SIGNAL I]**
- Bloomberg Mar 31: "Blackstone, Ares, Rivals Grilled by Congress Over Private Credit"
- Topics: sales practices, leverage, fees, incentives, audits, risk management
- Three-branch regulatory machinery now spinning (FSOC + Treasury + Congress)
- **Conf:** A2 EMPIRICAL (Bloomberg)

**F4. KPMG blown audit at Bridging Finance [SIG-2026-04-02-003 SIGNAL J]**
- OSC alleges KPMG "failed to properly value the loans"
- Key quote: "When KPMG found loans that were overstated, it wrongly assumed the findings were isolated"
- Auditor-as-enabler template. Same pattern as Andersen/Enron.
- **Conf:** A2 EMPIRICAL (OSC filing)

### CLUSTER G: PE financial behavior

**G1. PE Dividend Recaps at 2021 peak [SIG-2026-04-02-003 SIGNAL F]**
- 2025 $28.7B nearly matches 2021 $28.9B peak (through Nov 20)
- Trajectory: 2022 $5.2B → 2024 $23.0B → 2025 $28.7B
- PE can't exit (IPO/M&A frozen) → dividend recaps fund LP distributions
- Each recap = more debt on struggling companies → 33¢ recovery mechanism
- **Conf:** A2 EMPIRICAL (Bloomberg)

**G2. Ares $9.8B Special Opportunities Fund III [SIG-2026-04-02-002 SIGNAL A]**
- Closed Mar 31 above target
- $150B NFPAUM dry powder
- Buy-side of forced selling — vulture capital validates stress AND provides floor
- **Conf:** A2 EMPIRICAL

### CLUSTER H: Spread/macro markers (BROCK reference, LIQUID owns)

**H1. CCC-BB OAS differential vertical [SIG-2026-04-02-002 SIGNAL C]** — 7% Jan → 8% now (steepest since late 2025). Credit-quality bifurcation. **Cross-ref LIQUID; do not duplicate.**

**H2. Wells Fargo $200B+ into repo [SIG-2026-04-02-002 SIGNAL B]** — single point of failure if Wells pulls back. **LIQUID primary; reference only.**

---

## NOT INTEGRATED (out-of-domain or already in STATUS)

- WAL/Jefferies/Point Bonita litigation specifics — OZK/REGINALD primary
- ROAD to Housing Act / Freddie K-098 — REGINALD primary
- HF short cover whipsaw GS Prime — HENRY primary
- CRE refinancing wall — REGINALD primary
- Goeasy Canadian banks — adjacency note only
- News sweep duplicates — Apollo Epstein already in STATUS, ATH annuity sales reference-only
- Already in STATUS_ARCHIVE_APR10: OWL Apr 2 dual gating, Apr 6 PC meltdown timeline, Apr 6 Apollo Epstein

---

## CROSS-AGENT REPLIES

Per CLAUDE.md inbox protocol: silence = received and integrated unless we have new information for them.

| Sender | Reply needed? | Why |
|--------|--------------|-----|
| LIQUID (Apr 10 cascade letter) | **No** | Frame confirmed; we add corroborating data in Phase 4 outbox to LIQUID anyway re: HY OAS proximity to 260bps trigger |
| HAWK (Apr 20 IMF confirm) | **No** | INFO routing, no new BROCK data they don't have |
| WALTER (Apr 14 batch — 002, 004, 006) | **No** | Will routed via WALTER for verification; we are downstream |
| Prome (Apr 2 batches — Jackson, sweep) | **No** | Coordinator; integration is the reply |

---

## PHASE 2 KB.tsv ROW PLAN (preview)

Estimated **~12 KB rows** to write in Phase 2. Drafting now:

| Proposed ID | Cluster | Topic |
|-------------|---------|-------|
| KB-BRK-118 | A1 | Red Lobster TCW 98% equity / par debt dislocation |
| KB-BRK-119 | A2 | IMF GFSR explicit PC naming + multi-driver |
| KB-BRK-120 | B1 | Q1 2026 Stanger redemption book — 12-fund acceleration |
| KB-BRK-121 | C1 | PC 33¢ vs syndicated 52¢ recovery gap |
| KB-BRK-122 | C2 | PIK-to-default 60% / 17 companies in both states |
| KB-BRK-123 | D2 | Pluralsight $4B equity-to-zero precedent |
| KB-BRK-124 | E1+E2 | CPP/Antares + global pension PC exposure |
| KB-BRK-125 | E3 | Phantom reinsurance Seven Funnels (CONF C3, flagged) |
| KB-BRK-126 | E4 | Athene #2 FHLB borrower |
| KB-BRK-127 | F1+F2 | Powell "not systemic" + GS TRS pause = floor removed |
| KB-BRK-128 | F4 | KPMG Bridging Finance audit failure template |
| KB-BRK-129 | G1 | PE dividend recap surge $28.7B = 33¢ recovery mechanism |

Plus narrative-whipsaw, OWL Q1, BCRED Q1, SEC-Treasury-Fed probe rows from May 1 STATUS refresh — likely KB-BRK-130 through ~133.

**Final Phase 2 estimate: ~15-16 KB rows.**

---

## PHASE 3 PREDICTION UPDATES (preview)

| ID | Current | Proposed action |
|----|---------|-----------------|
| BRK-21 | National Dentex Apr maturity, 75% conf, target 2026-05-31 | **RESOLVE** — check actual outcome (default vs distressed refi vs amend-extend) |
| BRK-22 | ARCC dividend cut by Q4 2026, 60% conf | **RAISE to 70%** — OWL Q1 DL -1.1% return is corroborating evidence; ARCC 6-12mo behind OBDC |
| **NEW BRK-25** | First arms-length BDC mark below 90¢ on a non-related-party loan transaction by Q3 2026 | 50% — Red Lobster 98% equity is predecessor; loan mark catch-down is open question |
| **NEW BRK-26** | First SEC enforcement filing (formal action, not just open investigation) on PC valuation by Q4 2026 | 55% — Apr 24 probe has subpoena power; KPMG/OSC analog suggests timeline |
| **NEW BRK-27** | Goldman TRS for leveraged-loan shorts OR JPM PC short basket goes live by Q3 2026 | 40% — Goldman paused, S&P+JPM separate product launching; convergent infrastructure |
| **NEW BRK-28** | At least one major non-traded BDC (>$5B AUM) reports NAV markdown >5% in Q1 10-Q | 60% — landing this week through May; convergence of stress evidence |

---

*Triage complete. All 17 inbox files → `inbox/processed/`. Phase 2 (KB backfill) ready to begin.*
