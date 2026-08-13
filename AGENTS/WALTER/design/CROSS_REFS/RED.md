# CROSS_REFS — RED

**Purpose:** dispatch-time identifier-cache for WALTER. When about to dispatch a signal, grep this file for relevant topic/keyword/ticker → cross-ref RED IDs (RED-NN / KB-RED-NNN / VX-RED-NN / CHG-RED-NNN / FLOW-RED-N / RED-FT-NN / ML-RED-NNN) → cite in `dispatch_note` so RED's adversarial-overlay loop tightens.

**Read-by:** WALTER at signal-dispatch time (NOT at boot — too dense for boot read; lookup-on-demand only).

**Source-of-truth:** RED's `AGENTS/RED/workbook/*.tsv` + `AGENTS/RED/thesis/PREDICTIONS.tsv` + `AGENTS/RED/STATUS.md` + `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`. This file is a denormalized **cache** for grep-speed at dispatch — RED's TSVs are the canonical source. If RED's TSV says X and this cache says Y, **trust RED's TSV**. This cache exists to surface relevance, not to replace.

**Refresh trigger:** RED thesis-version bump OR new VX-RED row OR new RED-NN prediction registered OR new CHG-RED issued OR new FALSIFICATION trigger added. WALTER self-task on detection at next dispatch session.

**Last refreshed:** 2026-05-06 PM (initial scaffold post RED LIAISON Turn 6 close-loop + 5/5 batch APPROVED end-to-end). Source commits: RED `e6477450` + `b1ed0420` + `254f6e40` + WALTER `dad58114` + `8a532073`.

---

## §0 — Operational state pointers

For dispatch-time orientation:

| Anchor | Path | Refresh trigger |
|--------|------|-----------------|
| **Current thesis confidence** | `AGENTS/RED/STATUS.md` "CURRENT ASSESSMENT" | RED-session frequent |
| **Competing hypotheses + probabilities** | `AGENTS/RED/STATUS.md` "COMPETING HYPOTHESES" | After major thesis-revision events |
| **Bull-case steelman (RED's core duty)** | `AGENTS/RED/STATUS.md` "BULL CASE STEELMAN" | Refreshed each session |
| **Falsification criteria (free-text)** | `AGENTS/RED/STATUS.md` "FALSIFICATION CRITERIA" | When new criterion added |
| **Falsification criteria (machine-readable)** | `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (**15-col**, 9 rows — *8 → 12 → **15** on 2026-08-12: RED inserted `instrument_basis`/`state`/`action_magnitude` at 7-9, moving `exit_*` to **12-15**. ⚠️ **Read by HEADER, never by position** — WALTER has no code on this path, but the boot 6b/6c human loop broke on it 8/13 (an ad-hoc `awk` labelled fields 9-11 `exit:` and returned three different columns, silently). ⚠️ `state` (`ARMED`/`FIRING-BANKED`/`FIRED-BANKED`/`UN-FIRED`/`BLOCKED`) is the answer to **"is X fired NOW"** — the `FIRED_LOG` only answers "did X EVER fire"*) | New row OR threshold tuned OR **exit defined/changed** |
| **Falsification watch (event-type)** | `AGENTS/RED/CALENDAR.md` "FALSIFICATION WATCH" | New calendar event added |
| **Position vulnerability** | `AGENTS/RED/STATUS.md` "POSITION VULNERABILITY" | Live tape moves |
| **Exit-window framework** | `AGENTS/RED/STATUS.md` "EXIT-WINDOW FRAMEWORK" (Will-approved 2026-05-06) | After Will direction |
| **Open challenges** | `AGENTS/RED/STATUS.md` "OPEN CHALLENGES" | New CHG-RED issued |
| **Predictions scorecard** | `AGENTS/RED/STATUS.md` "PREDICTIONS SCORECARD" | RED-NN resolved |
| **Top adversarial priorities** | `AGENTS/RED/STATUS.md` "TOP ADVERSARIAL PRIORITIES" | RED-session frequent |
| **Thesis evolution log** | `AGENTS/RED/thesis/CHANGELOG.md` | After thesis version bump |

**Current state at scaffold time (2026-05-06):**
- Thesis confidence: **73% bear** (was 70%, +3 after Apr 21 WAL/OZK MISS/MUTED post-cleared falsification rule)
- Bifurcation framing: **paper-vs-structural** active; "thesis survives but instruments don't" frame per KB-RED-039
- Resolved record: **4 WRONG / 1 CORRECT / 9 ACTIVE** (Will-corrected from earlier overstatement)
- Calibration cycle 1 clock: **2026-05-06 → ETA May 20-27** (synced w/ BRENT)

---

## §1 — Predictions (RED-NN)

Source: `AGENTS/RED/thesis/PREDICTIONS.tsv` (14 rows + header).

| ID | Date | Topic / Domain | Prediction (one-line) | Confidence | Status |
|----|------|----------------|----------------------|------------|--------|
| **RED-01** | 2026-04-02 | Options timeline | Jun puts (HYG, IWM, SOFI, KRE May) expire before thesis plays out (Q3-Q4) | 65% | ACTIVE |
| **RED-02** | 2026-04-02 | NFP | Apr 3 NFP between -50K and +80K (neither extreme) | 45% | RESOLVED-WRONG |
| **RED-03** | 2026-04-02 | HAWK / Iran | Apr 6 deadline extends again (no strikes, no deal) | 40% | RESOLVED-WRONG |
| **RED-04** | 2026-04-02 | Policy / Fed | Policy rescue (Fed/Treasury) before full cascade — stealth or explicit | 20% | ACTIVE (Q2-Q3 2026) |
| **RED-05** | 2026-04-02 | Staffing canaries | RHI/KFRC remain positive Q2 (first sustained positive in 3 yrs) | 35% | ACTIVE (Q2 2026) |
| **RED-06** | 2026-04-02 | CDX / HY divergence | Resolves by CDX compressing (not cash widening) | 30% | RESOLVED-WRONG |
| **RED-07** | 2026-04-02 | Bank earnings | At least 1 of OZK/WAL beats Apr expectations | 25% | **RESOLVED-CORRECT** (BOTH MISSED 4/21) |
| **RED-08** | 2026-04-02 | Brent / Hormuz | Brent fails to sustain >$120 through Q2 despite Hormuz closure | 60% | ACTIVE (leaning RIGHT — paper hit $141 then collapsed) |
| **RED-09** | 2026-04-02 | BOJ | Delays hike past May 1 meeting | 15% | RESOLVED-WRONG (BOJ held 4/28 with 3 dissents) |
| **RED-10** | 2026-04-02 | HY OAS | Fails to breach 400 by June expiry | 45% | ACTIVE (HY OAS ~285 4/16; trending RIGHT) |
| **RED-11** | 2026-04-19 | VIX / VIOLET | VIX sustained close ≥25 for 3 td by 2026-05-19 (challenges VIOLET) | 18% | ACTIVE (VIX 16.54 5/6; tracking RIGHT) |
| **RED-12** | 2026-05-06 | BRENT v2.0 challenge | Next observable Dated Brent <$115 (challenges $43-44 spread claim) | 50% | ACTIVE |
| **RED-13** | 2026-05-06 | BRENT v2.0 challenge | Brent Dec26 stays $80-95 over 60d while spot $95-130 | 65% | ACTIVE |
| **RED-14** | 2026-05-06 | BRENT v2.0 challenge | US rig count remains 400-415 with no sustained upward break | 65% | ACTIVE |

**Resolved record (5/13):** RED-02, RED-03, RED-06, RED-09 = WRONG; RED-07 = CORRECT (low-prob outcome at 25% directionally right). 8/13 ACTIVE.

**Calibration finding (KB-RED-040):** RED ranges historically too narrow in BOTH directions — systematic tail underestimation. Process fix: widen ranges, stop picking modal scenarios, assign explicit tail probabilities.

---

## §2 — Counter-evidence vectors (VX-RED-NN)

Source: `AGENTS/RED/workbook/VX.tsv` (22 rows + header).

| ID | Target Agent | Topic | Strength | Bull/Bear Wt | Status |
|----|--------------|-------|----------|--------------|--------|
| **VX-RED-001** | CARL | Employment Resilience (NFP/UE/claims/wages) | STRONG | 45/55 | ACTIVE |
| **VX-RED-002** | CARL | Real Wage Growth | MODERATE | 45/55 | ACTIVE |
| **VX-RED-003** | CARL | Consumer Spending Resilience (retail) | MODERATE | 35/65 | ACTIVE |
| **VX-RED-004** | SAM | Japan Muddle-Through | MODERATE | 35/65 | ACTIVE |
| **VX-RED-005** | REGINALD | System Bank Capital (CET1) | MODERATE | 40/60 | ACTIVE |
| **VX-RED-006** | HENRY | Zweig Breadth Thrust | STRONG | 45/55 | ACTIVE |
| **VX-RED-007** | HENRY | Structural Bid ($1.5T mechanical demand) | STRONG | 45/55 | ACTIVE |
| **VX-RED-008** | REGINALD | CRE Forbearance Precedent (2009-2012) | MODERATE-STRONG | 45/55 | ACTIVE |
| **VX-RED-009** | CARL | Auto Fraud Isolation (3 cases) | WEAK | 30/70 | ACTIVE |
| **VX-RED-010** | REGINALD | SRF Backstop ($500B) | MODERATE | 40/60 | ACTIVE |
| **VX-RED-011** | CROSS-AGENT | EARNINGS vs CARL contradiction | STRONG | 40/60 | ACTIVE |
| **VX-RED-012** | LABOR | Staffing Canaries (RHI/KFRC) | MODERATE | 45/55 | ACTIVE |
| **VX-RED-013** | BRENT | Russia Sanctions Relief | WEAK | 25/75 | ACTIVE (downgraded — physical $141 proves insufficient) |
| **VX-RED-014** | LABOR | Employment Wartime Resilience | STRONG | 40/60 | ACTIVE |
| **VX-RED-015** | LIQUID | HY OAS Not Confirming (FALSIFICATION FIRED) | FALSIFIED | 65/35 | FALSIFIED 4/10-16; bull-weight upgraded |
| **VX-RED-016** | PORTFOLIO | AAPL Concentration Risk (45% portfolio) | STRONG | 20/80 | ACTIVE — needs explicit exit triggers |
| **VX-RED-017** | HAWK | Trump Dealmaker Dynamic | STRONG | 55/45 | ACTIVE (upgraded — ceasefire was 0% per HAWK, demonstrably active) |
| **VX-RED-018** | LIQUID | SOFR-IORB Breach Apr 15 | MODERATE | 40/60 | ACTIVE pending data |
| **VX-RED-019** | BRENT | Oil Paper-Physical Bifurcation | STRONG | 50/50 | ACTIVE (binary on Apr 22) |
| **VX-RED-020** | REGINALD | Bank Cohort Fade Miss-Driven (Q1 2026) | MODERATE-STRONG | 40/60 | ACTIVE |
| **VX-RED-021** | LIQUID | Paper Markets Pricing Path A | STRONG | 60/40 | ACTIVE — captures bifurcation |
| **VX-RED-023** | REGINALD | WAL V2.0 V1-Demotion-Without-Falsifier | STRONG | 25/75 | ACTIVE (5/6 — pending mid-May FFIEC MI3) |

**Note:** VX-RED-022 doesn't exist (skipped); RED's numbering is sparse.

**Topic-to-VX index** (for dispatch-time grep):
- **Employment / NFP / claims** → VX-RED-001, -002, -012, -014
- **Consumer / retail / discretionary** → VX-RED-003, -011
- **Japan / BOJ / FXY** → VX-RED-004
- **Bank capital / CRE / forbearance** → VX-RED-005, -008, -020
- **HENRY / vol / breadth / structural bid** → VX-RED-006, -007
- **Auto fraud (CVNA/ALLY)** → VX-RED-009
- **Policy rescue / SRF / Fed** → VX-RED-010
- **Staffing canaries (RHI/KFRC)** → VX-RED-012
- **BRENT / oil / Russia / paper-physical** → VX-RED-013, -019
- **Iran / HAWK / dealmaker** → VX-RED-017
- **HY OAS / credit spreads** → VX-RED-015, -021
- **AAPL portfolio concentration** → VX-RED-016
- **SOFR / funding / IORB** → VX-RED-018
- **WAL / V2.0 / MI3 / hidden-CRE** → VX-RED-023

---

## §3 — Knowledge base claims (KB-RED-NNN)

Source: `AGENTS/RED/workbook/KB.tsv` (40 rows + header). Condensed to ID / topic / status. Full claim text in source TSV.

### Network structure / methodology

| ID | Topic | Status |
|----|-------|--------|
| KB-RED-001 | Employment as 1-of-2 master variables (war introduced oil parallel path) | REVISED |
| KB-RED-002 | ZBT regime active (100% historical 12-mo success rate) | CONFIRMED |
| KB-RED-003 | Consumer stress via K-shape masking + phantom debt | CONFIRMED |
| KB-RED-004 | Transmission gap — bear theses die in stress-exists-vs-stress-transmits gap | CONFIRMED |
| KB-RED-005 | FHLB is LAGGING not LEADING (SVB precedent) | CORRECTED |
| KB-RED-006 | ALLY auto loan exposure is $19B not $4B | CORRECTED |
| KB-RED-007 | CBRE is LEADING not LAGGING | CORRECTED |
| KB-RED-008 | LQD/HYG quality rotation invalidated by duration confound | CONFIRMED |
| KB-RED-009 | CCC OAS stress is BROAD-BASED across 15 sectors (not concentrated) | CORRECTED |
| KB-RED-010 | Unanimity risk — every Tier 1 at RED/CRITICAL = max blind-spot | ACTIVE |

### Counter-evidence (specific claims)

| ID | Topic | Status |
|----|-------|--------|
| KB-RED-011 | Continuing claims at 2-yr low (1.819M) | ACTIVE |
| KB-RED-012 | Staffing canaries (RHI/KFRC) sequential positive | ACTIVE |
| KB-RED-013 | Retail sales +0.6% MoM | ACTIVE |
| KB-RED-014 | Oil ceiling INVALIDATED — Dated Brent $141.37 (2008 high) | INVALIDATED |
| KB-RED-015 | Russia sanctions relief Apr 11 expiry | ACTIVE |
| KB-RED-024 | GDPNow 1.9% Q1 (not recessionary) | ACTIVE |
| KB-RED-025 | Savings rate 4.5% (up from 3.6%) | ACTIVE |
| KB-RED-026 | NFP March 2026 = +178K (Apr 3 print) | ACTIVE |
| KB-RED-028 | HY OAS crashed to 305 from 342 in 5 days | ACTIVE |
| KB-RED-032 | VIX-HY divergence Apr 7 (VIX 26.59 / HY OAS 305) | ACTIVE |

### Policy / Regulatory

| ID | Topic | Status |
|----|-------|--------|
| KB-RED-016 | Stealth QE active ($157B T-bills) + eSLR freed $210-384B | ACTIVE |
| KB-RED-023 | Reg forbearance — Fed dropped prior demands Feb 11 | CONFIRMED |

### Market data (point-in-time)

| ID | Topic | Status |
|----|-------|--------|
| KB-RED-020 | NDFI reconciled — $1.411T domestic Q4 / $4.2T total committed | RESOLVED |
| KB-RED-027 | Dated Brent reached $141.37 physical 4/4 | ACTIVE |
| KB-RED-029 | Gold record $4,794.80 on risk-on day Apr 2 | ACTIVE |
| KB-RED-031 | Kharg Strike Apr 7 — 90% Iran exports / muted reaction Brent +1-2% | ACTIVE |
| KB-RED-033 | 12 PC funds gated (Barings 12th) | ACTIVE |
| KB-RED-036 | SOFR 3.72% > IORB 3.65% = +7bps Apr 15 first positive spread | ACTIVE |
| KB-RED-037 | Oil paper-physical bifurcation $43-44 spread widest of cycle | ACTIVE |
| KB-RED-038 | Bank cohort fade pattern miss-driven Q1 2026 | ACTIVE |
| KB-RED-041 | (BRENT v2.0 challenge basis — see CHG-RED-024) | ACTIVE |

### Methodology / portfolio risk

| ID | Topic | Status |
|----|-------|--------|
| KB-RED-017 | AAPL 45% portfolio concentration risk | ACTIVE |
| KB-RED-018 | Options timeline mismatch (Jun puts vs Q3-Q4 thesis) | ACTIVE |
| KB-RED-019 | CDX/cash HY divergence 8+ weeks no convergence | ACTIVE |
| KB-RED-021 | SSB analyst consensus (15 analysts / 0 sells) | ACTIVE |
| KB-RED-022 | SSB three structural firewalls (PCD/LTV/payments) | ACTIVE |
| KB-RED-030 | Buffer depletion framework (revised oil-bypasses-employment) | REVISED |
| KB-RED-034 | HY energy compositional adjustment (~18bps suppression at $110+ oil) | ACTIVE |
| KB-RED-035 | HY OAS falsification rule fired Apr 10-16 | CONFIRMED |
| KB-RED-039 | Bifurcated thesis — "thesis survives, instruments don't" | ACTIVE |
| KB-RED-040 | RED calibration systemic — ranges too narrow (4/10+ wrong) | ACTIVE |

**Topic-to-KB index** (for dispatch-time grep):
- **Employment / NFP / claims / staffing** → KB-RED-001, -011, -012, -026, -030
- **Consumer / retail / wages / savings** → KB-RED-003, -013, -024, -025
- **HY OAS / credit / CDX / spreads** → KB-RED-009, -019, -028, -032, -034, -035
- **CRE / banks / NDFI / forbearance** → KB-RED-005, -007, -008, -020, -023, -038
- **WAL / SSB / OZK / regional banks** → KB-RED-021, -022, -038
- **Oil / Brent / Hormuz / paper-physical** → KB-RED-014, -015, -027, -031, -037
- **Iran / HAWK / kinetic** → KB-RED-031
- **Auto / ALLY / CVNA** → KB-RED-006
- **VIX / breadth / structural bid** → KB-RED-002, -029, -032
- **Policy / Fed / SRF / QE** → KB-RED-016, -023
- **AAPL / portfolio** → KB-RED-017
- **Options / timeline** → KB-RED-018, -039
- **SOFR / IORB / funding** → KB-RED-036
- **Methodology corrections** → KB-RED-005, -006, -007, -008, -009 (network-wide pattern)
- **Calibration / systemic** → KB-RED-040
- **PC stress / gates** → KB-RED-033
- **Buffer / transmission** → KB-RED-004, -030

---

## §4 — Formal challenges (CHG-RED-NNN)

Source: `AGENTS/RED/workbook/CHALLENGES.tsv` (25 rows + header). Schema bumped 2026-05-06 with col 11 `BOARD_Refs` (per LIAISON Q7).

| ID | Date | Target | Grade | Status | Topic |
|----|------|--------|-------|--------|-------|
| CHG-RED-001 | 2026-02-12 | SSB $90P | B- | RESOLVED | Near-neutral EV; timing risk |
| CHG-RED-002 | 2026-02-12 | Japan thesis | B+ | RESOLVED | Shunto upgrade |
| CHG-RED-003 | 2026-02-12 | Full system | B+ | RESOLVED | First full sweep |
| CHG-RED-004 | 2026-02-20 | KRE June Puts | A- | RESOLVED | Timing mispriced 2-3 quarters |
| CHG-RED-005 | 2026-03-14 | Full system (war) | A- dir / C+ timing | RESOLVED | Russia sanctions unmodeled |
| CHG-RED-006 | 2026-04-02 | Portfolio | STRONG | ACTIVE | June/May puts vs Q3-Q4 thesis |
| CHG-RED-007 | 2026-04-02 | All agents | MODERATE | ACTIVE | 100% red alignment / echo chamber risk |
| CHG-RED-008 | 2026-04-02 | PROME | MODERATE | ACTIVE | Policy rescue 11% too low (revised 20%) |
| CHG-RED-009 | 2026-04-02 | LABOR/CARL | MODERATE | ACTIVE | Counter-signals dismissed not weighted |
| CHG-RED-010 | 2026-04-02 | BROCK | MODERATE | ACTIVE | Alpha window closing on PC thesis |
| CHG-RED-011 | 2026-04-02 | BRENT | MODERATE | RESOLVED | RED was wrong — physical $141 |
| CHG-RED-012 | 2026-04-02 | HAWK | WEAK-MOD | WEAKENED | 45/45 convergence overfitting |
| CHG-RED-013 | 2026-04-05 | LABOR/CARL | MODERATE | ACTIVE | NFP +178K challenges employment-first |
| **CHG-RED-014** | 2026-04-07 | LIQUID/ALL | COMPELLING | ACTIVE | HY OAS 305 falsification approach (BOARD: SIG-W-20260411-001) |
| CHG-RED-015 | 2026-04-07 | ALL | STRONG | ACTIVE | VIX-HY divergence resolution within 3-5 days |
| CHG-RED-016 | 2026-04-07 | TLT/HYG | MODERATE | ACTIVE | Bond vol squeeze threatens rate-sensitive puts |
| CHG-RED-017 | 2026-04-07 | BRENT/HAWK | MODERATE | RESOLVED | Resolved into VX-RED-019 (paper-physical bifurcation) |
| **CHG-RED-018** | 2026-04-18 | RED/self | CRITICAL | ACTIVE | Pre-registered HYG exit recommended (BOARD: SIG-W-20260411-001) |
| **CHG-RED-019** | 2026-04-18 | LIQUID/BROCK | STRONG | ACTIVE | Public/private bifurcation (BOARD: SIG-W-20260414-002, -004; -028-005; -029-002) |
| CHG-RED-020 | 2026-04-18 | Portfolio | COMPELLING | ACTIVE | Near-dated options vs Q3-Q4 thesis timing |
| **CHG-RED-021** | 2026-04-18 | HENRY/REGINALD | MODERATE | ACTIVE | DB Asset Allocation chart (BOARD: SIG-W-20260414-008) |
| CHG-RED-022 | 2026-04-18 | Self/calibration | STRONG | ACTIVE | RED-02/03/06/08 systematic methodological failure |
| **CHG-RED-023** | 2026-04-19 | VIOLET | STRONG | RESOLVED-CONVERGED | SKEW divergence pre-commit 18% (BOARD: SIG-W-20260419-011, -012, -017) |
| **CHG-RED-024** | 2026-05-06 | BRENT | STRONG | ACTIVE | BRENT v2.0 5-challenges (3 STRONG + 2 MODERATE; predictions RED-12/-13/-14) |
| **CHG-RED-025** | 2026-05-06 | REGINALD | STRONG | ACTIVE | WAL V2.0 stress-test verdict OVER-CORRECTED (~26% weighted PASS) |

**5 historical CHGs backfilled** with BOARD_Refs (col 11): CHG-RED-014, -018, -019, -021, -023. **18 historical CHGs untouched** (pending WALTER complete-backfill self-task per Q14 — this CROSS_REFS cache is the prerequisite).

**Topic-to-CHG index** (for dispatch-time grep):
- **HY OAS / credit / falsification** → CHG-RED-014, -015, -018
- **HENRY / VIOLET / vol** → CHG-RED-021, -023
- **REGINALD / WAL / V2.0** → CHG-RED-021, -025
- **BRENT / oil / paper-physical** → CHG-RED-011, -017, -024
- **BROCK / PC stress** → CHG-RED-010, -019
- **LABOR / CARL / employment** → CHG-RED-009, -013
- **HAWK / Iran / war** → CHG-RED-005, -012
- **Portfolio / options / timeline** → CHG-RED-006, -016, -020
- **Self-calibration / methodology** → CHG-RED-018, -022
- **PROME / policy** → CHG-RED-008
- **All-agent / unanimity** → CHG-RED-007, -015

---

## §5 — Transmission-break flow (FLOW-RED-N)

Source: `AGENTS/RED/workbook/FLOW.tsv` (7 rows + header).

| ID | Name | Status | Pathway |
|----|------|--------|---------|
| FLOW-RED-001 | Employment Channel Stalls | FIRING | NFP +178K = condition met (oil-path independent) |
| FLOW-RED-002 | Policy Rescue Intercepts | WEAKENING | 20% probability; multiple tools unused |
| FLOW-RED-003 | Regulatory Forbearance Extends | WEAKENING | Feb 11 explicit (2009-2012 precedent 3-5 yrs) |
| FLOW-RED-004 | Oil Ceiling Caps Inflation | **BROKEN** (Apr 5) | Dated Brent $141 = 2008 high; SPR failed |
| FLOW-RED-005 | Japan Muddle-Through | INTACT | BOJ 30-yr precedent; long-end breakout novel |
| FLOW-RED-006 | CDX Compresses Not Cash Widens | RESOLVING-BULL | Cash tightened 37bps in 5 days (HYG puts endangered) |
| FLOW-RED-007 | Sponsor Capital Injection | INTACT | 99% current payments / PE $240B continuation vehicles |

---

## §6 — Falsification triggers (RED-FT-NN — machine-readable threshold-cross)

Source: `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (7 rows + header). WALTER reads at boot per spawn-protocol step 6b; runs at-dispatch eval per CHECKLIST v0.10 Phase 2 step 7.

| ID | Metric | Threshold | Sustain | Action | Recipient chain |
|----|--------|-----------|---------|--------|-----------------|
| **RED-FT-01** | HY-OAS | <280 | 3 sessions | IMMEDIATE-FALSIFY | RED action / LIQUID HENRY info / Will |
| **RED-FT-02** | HY-OAS | >320 | 3 sessions | PATH-B-CONFIRM | RED action / LIQUID HENRY info |
| **RED-FT-03** | BRENT-PAPER | >130 | 5 sessions | ADD-POSITION | RED action / BRENT info / Will |
| **RED-FT-04** | BRENT-PAPER | <75 | 3 sessions | BRT-15-INVALID | RED action / BRENT action / Will |
| **RED-FT-05** | INITIAL-CLAIMS | >250 | 1 session | LABOR-RE-ARM | RED action / CARL LABOR info |
| **RED-FT-06** | VIX | <16 | 5 sessions | MANAGED-DECLINE-CONFIRM | RED action / HENRY VIOLET info |
| **RED-FT-07** | CCC-OAS | >930 | 1 session | EARLY-STRESS | RED action / LIQUID info |

**Current proximity (as of 2026-05-06 PM, last live tape):**
- **RED-FT-01** HY-OAS<280×3 — closest to fire; primary OAS not pulled but tape pattern (HYG +0.33% / ^TNX -1.49%) suggests near-or-just-below-280; **needs primary confirmation for sustain-day 1 declaration** at next BOND refresh.
- **RED-FT-06** VIX<16×5 — within 6.4% of threshold (VIX 17.02; just outside 5% near-trigger band).
- **RED-FT-04** BRENT-PAPER<75×3 — NOT breached (Brent $101.63 / +35% above threshold).
- Others further from current values.

**Fire log:** `AGENTS/WALTER/registry/FALSIFICATION_FIRED_LOG.tsv` (5-col WALTER-side ledger). 0 fires as of 2026-05-06 PM; header-only.

**Out-of-scope for v1** (per JOINT_PROPOSAL §2.3): continuous live-tape polling / multi-leg compound triggers / event-type triggers (handled manually via CALENDAR.md FALSIFICATION WATCH for v1) / schema v2 with `trigger_type` discriminator (deferred until v1 operational).

---

## §7 — ML methodology audit (ML-RED-NNN)

Source: `AGENTS/RED/workbook/ML.tsv` (58 rows + header). Pointer-only — full audit trail in source TSV; cache too dense for one-line summarization. Use ML-RED-NN for grep at dispatch when methodology-correction context matters.

**High-leverage ML entries** (referenced by KB.tsv `DerivedFrom` column):
- ML-RED-008, -010, -030 → KB-RED-001 (employment as master variable)
- ML-RED-009 → KB-RED-003 (consumer stress K-shape)
- ML-RED-022 → KB-RED-008 (LQD/HYG duration confound)
- ML-RED-025 → KB-RED-005, -006, -007 (FHLB/ALLY/CBRE methodology corrections)
- ML-RED-030 → KB-RED-014, -026, -030 (oil ceiling INVALIDATED + buffer-depletion framework)
- ML-RED-034 → KB-RED-009 (CCC OAS broad-based correction)
- ML-RED-038, -042 → KB-RED-040 (RED calibration systemic)
- ML-RED-040 → KB-RED-035 (HY OAS falsification rule fired)
- ML-RED-043 → KB-RED-039 (bifurcated thesis)

---

## §8 — Topic / keyword index for dispatch-time grep

When WALTER's about to dispatch a signal touching one of these topics, grep this section first to identify all relevant RED IDs to cross-ref in `dispatch_note`.

**Macro / Fed / policy:**
- Fed balance sheet / SOMA → KB-RED-016, FLOW-RED-002
- Stealth QE / eSLR / SRF → KB-RED-016, VX-RED-010
- Reg forbearance → KB-RED-023, VX-RED-008, FLOW-RED-003
- Policy rescue probability → CHG-RED-008, FLOW-RED-002, RED-04
- SOFR / IORB / funding stress → KB-RED-036, VX-RED-018

**Credit / spreads:**
- HY OAS / spreads → KB-RED-009, -019, -028, -034, -035; VX-RED-015, -021; CHG-RED-014, -015, -018; **RED-FT-01, RED-FT-02**; FLOW-RED-006; RED-10
- CCC / distressed → KB-RED-009; **RED-FT-07**
- CDX / cash divergence → KB-RED-019, FLOW-RED-006, RED-06

**Employment / labor:**
- NFP / claims / wages → KB-RED-001, -011, -026, -030; VX-RED-001, -002, -012, -014; CHG-RED-009, -013; **RED-FT-05**; FLOW-RED-001; RED-02, RED-05
- Staffing canaries (RHI/KFRC) → KB-RED-012, VX-RED-012, RED-05

**Consumer:**
- Retail sales / spending → KB-RED-013, VX-RED-003
- Real wages → KB-RED-003 (K-shape), VX-RED-002
- Savings rate → KB-RED-025
- GDPNow → KB-RED-024

**Banks / CRE:**
- WAL / OZK / SSB / regionals → KB-RED-021, -022, -038; VX-RED-005, -020, -023; CHG-RED-001, -004, -021, -025; RED-07
- NDFI / hidden CRE → KB-RED-020, -038
- CRE forbearance → KB-RED-023, VX-RED-008, FLOW-RED-003
- Auto / ALLY / CVNA → KB-RED-006, VX-RED-009
- FHLB → KB-RED-005 (LAGGING NOT LEADING — methodology)
- CBRE → KB-RED-007 (LEADING — methodology)
- Bank cohort fade → KB-RED-038, VX-RED-020

**PC stress:**
- BDC / Apollo / Blue Owl / 12 PC gates → KB-RED-033, VX-RED-005; CHG-RED-010, -019, -020; FLOW-RED-007

**Oil / energy / Iran:**
- Brent paper / physical / Dated → KB-RED-014, -027, -031, -037; VX-RED-013, -019; CHG-RED-011, -017, -024; **RED-FT-03, RED-FT-04**; FLOW-RED-004; RED-08, RED-12, RED-13
- Oil ceiling (INVALIDATED) → KB-RED-014, FLOW-RED-004
- Russia sanctions → KB-RED-015, VX-RED-013
- Hormuz / Kharg / kinetic → KB-RED-031
- Trump dealmaker → VX-RED-017
- US rig count → RED-14

**Equities / vol / positioning:**
- VIX → KB-RED-029, -032; **RED-FT-06**; CHG-RED-015, -023; RED-11
- ZBT / breadth → KB-RED-002, VX-RED-006
- Structural bid / pensions / SWF → VX-RED-007
- AAPL portfolio concentration → KB-RED-017, VX-RED-016
- DB Asset Allocation (positioning) → CHG-RED-021
- Options timeline / Jun puts / KRE / SOFI / IWM → KB-RED-018, -039; CHG-RED-006, -016, -020; RED-01

**Japan / SAM:**
- BOJ / FXY / JGB / Shunto → KB-RED-002 (note: KB-RED-002 is for ZBT not Japan; Japan thesis primarily in VX-RED-004), VX-RED-004, FLOW-RED-005; RED-09; CHG-RED-002

**Methodology / calibration:**
- Network unanimity → KB-RED-010, CHG-RED-007
- RED systematic miss / range too narrow → KB-RED-040, CHG-RED-022
- Bifurcated thesis (paper-vs-structural) → KB-RED-039, VX-RED-021
- Buffer depletion / transmission → KB-RED-004, -030
- HY energy compositional adjustment → KB-RED-034
- LQD/HYG duration confound → KB-RED-008
- CCC broad-based correction → KB-RED-009

---

## §9 — Composition example: how to use this cache at dispatch

**Example signal:** "WAL Q1 Call Report (mid-May FFIEC bulk) shows MI3 ratio at 26%."

**WALTER dispatch-time lookup:**
1. Grep `WAL` / `MI3` in §8 → returns: KB-RED-038 (bank cohort fade), VX-RED-023 (V2.0 V1-demotion), CHG-RED-021 (DB positioning), CHG-RED-025 (V2.0 stress-test verdict).
2. Grep `Q1 Call Report` / `FFIEC` → returns: VX-RED-023 ("Q2 NCO ex-fraud <30bps clean" flip-condition), CHG-RED-025 ("M3 retroscores at full 25% weight when mid-May FFIEC bulk MI3 lands").
3. Cross-ref FALSIFICATION_TRIGGERS — none of the 7 RED-FT-NN match this metric.
4. **Result for `dispatch_note`:** "Cross-ref CHG-RED-025 ($85P Jun EV math V2.0-incoherent) + VX-RED-023 (V1-demotion-without-falsifier; 25/75 bear-leaning); MI3 print is the V1 falsifier per RED bull-bear flip-condition. KB-RED-038 (bank cohort fade pattern miss-driven Q1 2026) is the supporting context."

This is what the cache earns — turns a 5-min RED-tree-grep into a 20-second dispatch-note lookup.

---

## §10 — CHG-RED backfill prerequisite (Q14 self-task)

This CROSS_REFS/RED.md cache **unblocks** the complete-CHG-RED backfill (per LIAISON Q14): WALTER produces a backfill diff at `AGENTS/WALTER/handoff_RED/CHALLENGES_BACKFILL_diff.tsv` for the 18 untouched historical CHGs by mechanical-grep across `BOARD/SIG-W-*.md`. RED applies at next boot per Critical Rule #2.

**Approach:**
1. For each CHG-RED-NNN in §4 above (18 untouched), extract the Target / Key_Finding / KB_Links / VX_Links from CHALLENGES.tsv source.
2. Grep `BOARD/SIG-W-*.md` for matches on (a) target agent name, (b) KB-RED-NNN refs, (c) VX-RED-NN refs, (d) topic keywords from key-finding.
3. Filter matches by date-window (CHG date ± 30 days for active matches; before CHG-resolution-date for resolved ones).
4. Output diff TSV with col 1 = CHG_ID, col 2 = SIG-W-IDs (semicolon-separated).
5. RED applies the diff to `AGENTS/RED/workbook/CHALLENGES.tsv` col 11 BOARD_Refs at next RED boot.

**Status:** CROSS_REFS/RED.md cache shipped 2026-05-06; backfill diff is the next WALTER self-task.

---

*v0.1 — initial scaffold 2026-05-06 PM. Refresh trigger: any RED ID-namespace addition (new RED-NN / KB-RED-NNN / VX-RED-NN / CHG-RED-NNN / RED-FT-NN). WALTER detects on RED commit + refreshes opportunistically; not boot-blocking.*
