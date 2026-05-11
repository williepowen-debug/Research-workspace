# JOINT PROPOSAL — WALTER ↔ REGINALD LIAISON wrap (REGINALD sections)

*REGINALD-side sections (§1 + §3) of the joint-proposal artifact bundling the WALTER ↔ REGINALD LIAISON Turns 1-5 (2026-05-10 23:11 UTC → 2026-05-11 11:42 UTC). Per LIAISON_PLAYBOOK §8 closing pattern. Pairs with WALTER §2 + §4 (`AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-11_walter_sections.md` — anticipated). Will-mediated stitched final at `design/JOINT_PROPOSAL_2026-05-11.md` repo-root.*

*Source dialog:* `AGENTS/REGINALD/handoff_WALTER/LIAISON.md` (5 turns, 669 lines).

---

## Context

Architectural-alignment dialog between REGINALD (regional-bank convergence hub; action-primary) and WALTER (BOARD signal router) opened 2026-05-10 at Will direction. Pattern lineage: CARL pilot (5/5-6) + BRENT (5/5) + RED (5/6). 5-turn convergence in <13 hours UTC.

**Central architectural finding (Turn 1 / corrected Turn 2):** REGINALD had **no BOARD-pull mechanism in boot**. WALTER had routed REGINALD as recipient on 51 BOARD signals Apr 14 → May 9 (16 ACTION + 33 info-cc + 2 body-mention); REGINALD's processed/ archive shows **3 reached integration**. 48-signal gap. Same pattern as RED LIAISON (97% routed / consumption-side gap) and BRENT LIAISON. Conclusion: cross-network keystone is BOARD-consumption rollout per agent.

**Net architectural ship:** 8 Qs locked both sides; 5 instantiated files (3 REGINALD + 2 WALTER + 2 WALTER spec changes); 1 v0.9 FORMAT_SPEC enum candidate pre-cosigned for batched ship; calibration cycle 1 clock set 2026-05-25.

---

## §1 — Instantiated files (REGINALD-side audit)

### 1.1 `AGENTS/REGINALD/registry/THRESHOLDS.tsv` (8 rows)

8-col schema mirrors RED's `FALSIFICATION_TRIGGERS.tsv`:

```
trigger_id  metric  threshold_op  threshold_value  sustain_window  action  recipient_chain  threshold_thesis_ref
```

`trigger_id` namespace: **REG-T-NN** (RED uses RED-FT-NN, BRENT may later use BRT-T-NN). 8 rows from REGINALD STATUS.md SIGNAL DASHBOARD + KEY THRESHOLDS + CROSS-AGENT TRIGGERS:

| trigger_id | metric | op | value | sustain | action | recipient_chain |
|------------|--------|----|-------|---------|--------|-----------------|
| REG-T-01 | KRE-PRICE | < | 60 | **1** | ALL-ALL-ACUTE | REGINALD action / ALL-AGENTS info / Will |
| REG-T-02 | WAL-PRICE | < | 78 | **1** | V1V3-ACCELERATE | REGINALD action / Will |
| REG-T-03 | HY-OAS | > | 320 | 3 | CREDIT-CANARY-FIRED | REGINALD action / CARL info |
| REG-T-04 | HY-OAS | > | 350 | 3 | ISSUANCE-FREEZE | REGINALD action / LIQUID action / Will |
| REG-T-05 | INITIAL-CLAIMS | > | 300 | **1** | ORANGE-TO-RED | REGINALD action / CARL LABOR info |
| REG-T-06 | FHLB-ADVANCES | > | 700 | 3 | EARLY-CRISIS | REGINALD action / LIQUID info |
| REG-T-07 | OFFICE-CMBS-DQ | > | 15 | 3 | CRE-ACCELERATE | REGINALD action / BROCK SHADE info |
| REG-T-08 | SOFR-IORB | > | 15 | 3 | LIQUID-FHLB-SPIKE | REGINALD action / LIQUID action / Will |

**Sustain-window discipline:** 3 binary-trigger thresholds at sustain=1 (KRE crash-through-$60 / WAL <$78 / Claims >300K) — fire-now on single-session breach. 5 slower-moving credit metrics at sustain=3 — day-to-day noise filter. WALTER LOCKED Turn 4.

**At-dispatch eval mechanics:** WALTER spawn-protocol step 6b (added Turn 4) reads this registry alongside `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` at boot, builds in-memory trigger array, queries `FORGE/tools/market-data/fetch.py` for each metric in CHECKLIST Phase 2 step 7 eval pass. Stale-fire suppression via WALTER-owned `AGENTS/WALTER/registry/REG_THRESHOLDS_FIRED_LOG.tsv` (Turn 4 ship).

### 1.2 `AGENTS/REGINALD/board/BOARD_LOG.tsv` (11-col, 32-row backfill stub)

11-col schema = CARL 9-col + 2 REGINALD-specific:

```
BOARD_ID  Date  Cluster  Verdict  Disposition  Post_Hoc_Conf  Vector_Update  Cross_Links  Channels_Touched  Bank_Tickers  Notes
```

**REGINALD-specific cols:**
- `Channels_Touched` — comma-separated 8-channel codes (CRE / HC / NDFI / PC / MFS / CMBS / FED-LAYOFFS / STAGFLATION); maps to v0.9 `bank_transmission` enum candidate (snake-case at v0.9 ship)
- `Bank_Tickers` — comma-separated tickers (EGBN, WAL, FITB, etc.); empty if no named bank

**Backfill stub composition (32 rows):**
- 3 originally-processed (Apr 14 batch: -002 TCW Red Lobster / -005 ROAD Freddie K098 / -008 DB Financials) — Disposition=INTEGRATED + Post_Hoc_Conf=0.85 (TCW)
- 16 missed-action signals from WALTER Turn 2 grep — Disposition=BACKFILL or WOULD-INTEGRATE; spans ROAD Act + OTTO Tricolor MTB + NV HOA + spring purchase ARM + FHLB Trump EO + distressed office $5B + US office vacancy + Baltimore CRE + multifamily Phoenix/Denver + Louisville Home Life + Phoenix BTR ROAD + ROAD 76-letter + Grosvenor Duke Westminster + Sternlicht Starwood + FWRD Q1
- 13 info-cc signals from inferred coverage — Disposition=BACKFILL
- 3 May-9 PROME-pinch-hitter trio with verify-verdicts from WALTER Turn 2 — `SIG-W-20260509-003` BlackRock-Metcold (CONFIRMED) / `SIG-W-20260509-004` Chapter 11 +42% (CONFIRMED → reroutes REGINALD ACTION) / `SIG-W-20260509-017` US-debt-GDP (STEPPED-DOWN to ROUTINE)

**Disposition vocabulary:**
- `INTEGRATED` — read + integrated into STATUS / KB / VX / FLOW
- `INFO_ONLY` — read + flagged in BOARD_LOG, no thesis-state change
- `REFERRED` — passed to sub-agent / peer (BROCK / CREED / CORAL)
- `WOULD-INTEGRATE` — backfill marker; signal would have driven a state change had it been seen at the time
- `BACKFILL` — backfill marker; signal is logged for completeness, no current action
- `BACKFILL-PENDING` — backfill marker; full disposition-write pending (separate REGINALD-session task)

### 1.3 `AGENTS/REGINALD/CLAUDE.md` Boot Step 9b (BOARD diff scan)

New boot step inserted between 9 (sub-agent STATUS check) and 10 (Execute). Three-tier scope per Q1 LOCK:

- **(a) Action-recipient unconditional** — `grep '^to:.*REGINALD' /BOARD/SIG-W-*.md` since last `board/BOARD_LOG.tsv` row — read all hits
- **(b) cluster_mediating unconditional** — `grep 'cluster_mediating: true' /BOARD/SIG-W-*.md` since last-session — read all hits
- **(c) info-recipient cluster-filtered:**
  - **Primary clusters** (always read info-cc): BANK_COLLATERAL / PC_STRESS / FED_FRAMEWORK / CONSUMER_STAGFLATION
  - **Secondary clusters** (read info-cc only on bank-ticker hit per BANK_EXPOSURE_MATRIX watchlist): IRAN_HORMUZ (FL energy cascade) / ASIA_CHINA (Asia carry) / AI_INFRA_CAPEX (hyperscaler-collateral)
  - **Skip clusters**: POSITIONING_VALUATION / HYDROCARBON_INFRA / MISC unless cluster_mediating fires

**Per-signal disposition row** appended to `board/BOARD_LOG.tsv` for each signal read.

**Cost estimate:** 30-60s additional boot time; volume bounded by cluster-filter not time-window per Q1 lock.

---

## §3 — Channels framework + Q4 4-dim overlap-key list

REGINALD's exposure-overlap surface for WALTER dispatch-time grep. Cached at `AGENTS/WALTER/design/CROSS_REFS/REGINALD.md` §1+§4+§5+§6 (WALTER Turn 4 ship).

### 3.1 Bank tickers — REGINALD-watchlist surface (Q4 dim A)

```
TIER-1 (max-stress):     EGBN, WAL
TIER-2 (elevated):       CFG, ZION, SSB, FLG
NEW-TRACKING (May 8):    FITB, HBAN
EXTERNAL-WATCH:          MTB (Baltimore CRE thesis), VLY (cohort fade)
PEER-ROUTED:             OZK (now own agent at AGENTS/OZK/ — REGINALD info-only)
HISTORICAL-ON-WATCH:     FBC, WBS, BHRB, FHN (BANK_EXPOSURE_MATRIX scoring tracked)
```

**Routing rule:** any string-match on TIER-1 + TIER-2 + NEW-TRACKING + EXTERNAL-WATCH ticker → REGINALD-info MANDATORY regardless of sub-agent action. **OZK exception:** OZK signals route to `../OZK` action; REGINALD-info ONLY when OZK signal also touches another REGINALD-watchlist ticker (cohort signal).

### 3.2 8-channel codes — `bank_transmission` enum candidate (Q4 dim B)

```
CRE          — commercial real estate (offices, hotels, MF)
HC           — hidden CRE (RCON2746 / Memo Item 3 reclassification)
NDFI         — non-depository financial institution exposure
PC           — private credit / BDC (overlap with BROCK-primary)
MFS          — mortgage fraud / fund-finance fraud chain (LAM/Cantor template)
CMBS         — CMBS maturity wall (2026 $875B per MBA)
FED-LAYOFFS  — DOGE federal layoffs cascade (DC corridor)
STAGFLATION  — stagflation trap (oil → consumer → bank borrower stress)
```

**v0.9 enum candidate** (snake_case): `cre / hidden_cre / ndfi / private_credit / mfs_fraud / cmbs_maturity / fed_layoffs / stagflation_trap`. Pre-cosigned for V0_9_STACK.md tracker alongside BRENT's `energy_transmission` (10-val) + `regime_state` (5-val). FORMAT_SPEC v0.9 bump deferred to batched ship per Will-walkthrough-grouped-by-weight pattern.

### 3.3 Cross-bank pattern keys — cohort/structural indicators (Q4 dim C)

```
cohort_fade_pattern        — 12/12 active; reset on any miss-into-rally print
fhlb_bifurcation           — 4/3 split (DECLINE: FITB,RF,ZION,VLY  / SURGE: MTB,CFG,PNC)
provisions_mask_deterioration  — VLY -66% YoY tell; CFG candidate
office_single_point_concentration  — WAL Slide 12 38% / EGBN 10-Q text
hidden_cre_relabeling_trajectory   — MI3 quarterly delta tracking
mi3_rcon2746_screen        — Hidden CRE methodology applied to any bank
ndfi_breakout_decomposition  — capital-call vs secured-PC vs other-finance trajectory
```

**Routing rule:** any pattern-key string-match → REGINALD-info MANDATORY **even when no specific bank ticker named** (cohort-level patterns where REGINALD synthesizes across names).

### 3.4 Specific exposure terms — high-precision greppable strings (Q4 dim D)

```
"Memo Item 3" / "RCON2746"          — Hidden CRE methodology
"FHLB advance" / "FHLB borrowing"   — funding-stress indicator
"Schedule O" / "Table 16"           — large-credit disclosure (10-Q drill)
"criticized assets" / "classified assets"  — leading credit migration
"30-89 day past due" / "Special Mention"   — leading-bucket buildup
"Capital call" + "Secured PC finance" / "Other finance and insurance"  — NDFI breakout
"office concentration" / "CRE office"      — single-point office stress
"hidden CRE" / "MI3"                       — explicit framework callout
```

**Routing rule:** dispatch-time grep on signal body-text + dispatch_note + cluster_secondary; hit on any string → REGINALD-mandatory routing flag.

### 3.5 Sub-agent fan-out routing convention (Q4 follow-up LOCK)

| Signal type | Routing rule |
|-------------|--------------|
| **Bank-exposure-context-touching** (signal touches REGINALD-watchlist ticker OR multi-channel exposure key OR pattern key OR exposure term) | sub-agent **action** + **REGINALD info unconditional** |
| **Pure sub-agent domain** (BDC NAV mark / CMBS market-level price-discovery / FL HOA insurance without named bank ticker) | sub-agent action / **REGINALD info ONLY** when bank-exposure tie surfaces |
| **REGINALD-thesis-side mediating** (multi-channel convergence at named bank — see Q5 ROUTING_TABLE v0.9 By Convergence) | **REGINALD action** + sub-agent info |

Sub-agent identification:
- **BROCK** (top-level peer) — BDC dividend cuts, PIK >40%, fund gates, OWL/ARCC/MAIN/OBDC fundamentals
- **CREED** (sub-agent) — CRE market-level data (CMBS DQ, office stress, maturity wall)
- **CORAL** (sub-agent) — Florida-specific (condo crisis, HOA/SIRS, Citizens insurance, FL labor)

---

## Architectural locks Q1-Q8 — summary

| Q | Topic | LOCK | Owner | Status |
|---|-------|------|-------|--------|
| Q1 | Boot-step BOARD scan | 3-tier scope (action-uncond + cluster_med-uncond + info-cluster-filtered) | REGINALD CLAUDE.md Boot 9b | ✅ shipped |
| Q2 | Threshold-cross auto-dispatch | 8-col registry mirror of RED FT_NN; REG-T-01..08 namespace | REGINALD THRESHOLDS.tsv + WALTER spawn-protocol 6b + REG_THRESHOLDS_FIRED_LOG | ✅ shipped both sides |
| Q3 | Bank-watchlist cross-ref | dispatch-time grep on §1 watchlist | WALTER CROSS_REFS/REGINALD.md §1 | ✅ shipped |
| Q4 | Sub-agent fan-out + 4-dim overlap | bank-exposure-context-touching → REGINALD-info mandatory | REGINALD §3 list + WALTER CROSS_REFS §1+§4+§5+§6 | ✅ shipped both sides |
| Q5 | Convergence-event detection | ROUTING_TABLE v0.9 By Convergence section (not standalone doc) | WALTER ROUTING_TABLE v0.9 | ✅ shipped |
| Q6 | Earnings/Call-Report cycle | dual-doc CALENDAR (md primary + TSV machine-parseable) | REGINALD CALENDAR_DATA.tsv self-task ~May 17-20 (post-CARL pattern) | 🟡 schema locked, instantiation deferred |
| Q7 | BOARD_LOG schema | 11-col (CARL 9 + Channels_Touched + Bank_Tickers) | REGINALD board/BOARD_LOG.tsv | ✅ shipped (32-row backfill stub) |
| Q8 | CROSS_REFS cache | dispatch-time grep cache, refresh-trigger on KB/VX/FLOW/threshold/watchlist change | WALTER design/CROSS_REFS/REGINALD.md v0.1 | ✅ shipped |

---

## Pre-cosigned for v0.9 stack (deferred to batched FORMAT_SPEC ship)

- `bank_transmission` enum 8-val → V0_9_STACK.md tracker alongside `energy_transmission` (BRENT 10-val) + `regime_state` (BRENT 5-val)
- REGINALD self-task on v0.9 ship: convert BOARD_LOG.tsv `Channels_Touched` column from uppercase short-codes to snake_case enum values

## Open externalities (post-LIAISON, not close-blockers)

1. **CARL DATA_RELEASE_CALENDAR.md pattern landing** (~May 17-20) → REGINALD ships `CALENDAR_DATA.tsv` ~7d later
2. **BOARD_LOG.tsv backfill execution** on 16 missed-action signals → separate REGINALD-session task; stub already in place
3. **Will-stitch joint-proposal at repo root** `design/JOINT_PROPOSAL_2026-05-11.md`
4. **Calibration cycle 1 trigger** 2026-05-25 calendar OR N=15 forward BOARD dispositions (early-fire) — synced w/ BRENT clock

---

*REGINALD §1 + §3 ship. WALTER §2 + §4 anticipated. Will-mediated stitched final at repo-root pending Will surface.*
