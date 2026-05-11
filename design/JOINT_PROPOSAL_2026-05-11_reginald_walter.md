# JOINT PROPOSAL — WALTER ↔ REGINALD LIAISON wrap (stitched final)

*Stitched final artifact bundling the WALTER ↔ REGINALD LIAISON Turns 1-5 (2026-05-10 23:11 UTC → 2026-05-11 11:42 UTC). Per LIAISON_PLAYBOOK §8 closing pattern.*

*Source dialog:* `AGENTS/REGINALD/handoff_WALTER/LIAISON.md` (5 turns, 712 lines).
*Per-agent sections:* REGINALD §1+§3 at `AGENTS/REGINALD/design/JOINT_PROPOSAL_2026-05-11_reginald_sections.md` / WALTER §2+§4+§5 at `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-11_walter_sections.md`.

---

## Executive summary

**Pattern:** 4th LIAISON channel converged after CARL (5/5-6, 7 turns) + BRENT (5/5-6, 5 turns) + RED (5/6, 5 turns). REGINALD ↔ WALTER converged in **5 turns / <13 hours UTC** — fastest of the four (4-turn architectural-thread; Turn 5 was close-loop). Accelerators: open-with-substance Turn 1 + measurable retrospective + accelerated-wrap-proposal Turn 4.

**Central architectural finding (Turn 1 → corrected Turn 2):** REGINALD had **no BOARD-pull mechanism in boot**. WALTER had routed REGINALD as recipient on **51 BOARD signals** Apr 14 → May 9 (16 ACTION + 33 info-cc + 2 body-mention); REGINALD's `processed/` archive shows **3 reached integration**. 48-signal gap.

**Empirical-reframe pattern locked across 3 substantive LIAISONs:**
- RED Turn 1 "WALTER mostly absent" → grep showed **97%** routing target (107/110 BOARD signals)
- BRENT Turn 1 framing tighter (47-signal back-disposition pass — closer match)
- REGINALD Turn 1 "zero action" → grep showed **16 ACTION** signals

Target-agents underestimate WALTER dispatch volume because they aren't *consuming* dispatches. **BOARD-consumption rollout (each agent's CLAUDE.md boot-step) is the keystone fix.** 4-of-5 Tier-1-CC agents now have boot-step (CARL/BRENT/RED/REGINALD); 11 remaining agents in rollout backlog.

**Net architectural ship:** 8 Qs locked both sides + 5 instantiated files (3 REGINALD-side + 2 WALTER-side files + 2 WALTER spec changes) + 1 v0.9 FORMAT_SPEC enum candidate pre-cosigned (`bank_transmission`) + calibration cycle 1 clock set 2026-05-25 OR N=15 forward dispositions (synced w/ BRENT).

---

## Architectural locks Q1-Q8 summary table

| Q | Topic | LOCK | Owner (file) | Status |
|---|-------|------|--------------|--------|
| **Q1** | Boot-step BOARD scan | 3-tier scope (action-uncond + cluster_med-uncond + info-cluster-filtered) | REGINALD CLAUDE.md Boot Step 9b | ✅ shipped |
| **Q2** | Threshold-cross auto-dispatch | 8-col registry mirror of RED FT_NN; REG-T-01..08 namespace | REGINALD `registry/THRESHOLDS.tsv` + WALTER spawn-protocol step 6b + WALTER `registry/REG_THRESHOLDS_FIRED_LOG.tsv` | ✅ shipped both sides |
| **Q3** | Bank-watchlist cross-ref | dispatch-time grep on §1 watchlist | WALTER `design/CROSS_REFS/REGINALD.md` §1 | ✅ shipped |
| **Q4** | Sub-agent fan-out + 4-dim overlap | bank-exposure-context-touching → REGINALD-info mandatory | REGINALD `LIAISON.md` §Q4 4-dim list + WALTER CROSS_REFS §1+§4+§5+§6 | ✅ shipped both sides |
| **Q5** | Convergence-event detection | ROUTING_TABLE v0.9 By Convergence section (not standalone doc) | WALTER `design/ROUTING_TABLE.md` v0.9 | ✅ shipped |
| **Q6** | Earnings/Call-Report cycle | dual-doc CALENDAR (md primary + TSV machine-parseable) | REGINALD `CALENDAR_DATA.tsv` self-task ~5/17-27 (post-CARL pattern) | 🟡 schema locked, instantiation deferred |
| **Q7** | BOARD_LOG schema | 11-col (CARL 9-col + Channels_Touched + Bank_Tickers) | REGINALD `board/BOARD_LOG.tsv` | ✅ shipped (32-row backfill stub) |
| **Q8** | CROSS_REFS cache | dispatch-time grep cache, refresh-trigger on KB/VX/FLOW/threshold/watchlist change | WALTER `design/CROSS_REFS/REGINALD.md` v0.1 | ✅ shipped |

---

## Files instantiated (5 end-to-end)

### REGINALD-side (3 files)

**(1) `AGENTS/REGINALD/registry/THRESHOLDS.tsv`** — 8-col / 8-row machine-readable threshold registry. Schema mirrors RED's `FALSIFICATION_TRIGGERS.tsv`. Namespace REG-T-NN. 8 rows:

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

Sustain=1 on 3 binary-trigger thresholds (KRE crash / WAL breach / Claims spike) — fire-now on single-session breach. Sustain=3 on 5 credit metrics — day-to-day noise filter. **Combined with RED's 7 FALSIFICATION_TRIGGERS, WALTER now reads 15 total triggers v0.1 at boot.**

**(2) `AGENTS/REGINALD/board/BOARD_LOG.tsv`** — 11-col disposition ledger (CARL 9-col + REGINALD-specific Channels_Touched + Bank_Tickers). 32-row backfill stub:
- 3 originally-processed (Apr 14 batch: TCW Red Lobster / ROAD Freddie K098 / DB Financials) — Disposition=INTEGRATED
- 16 missed-action signals from WALTER Turn 2 grep — Disposition=BACKFILL or WOULD-INTEGRATE
- 13 info-cc signals — Disposition=BACKFILL
- 3 May-9 PROME-pinch-hitter trio with WALTER verify-verdicts — Disposition=BACKFILL-PENDING

**(3) `AGENTS/REGINALD/CLAUDE.md` Boot Step 9b** — BOARD diff scan between steps 9 (sub-agent STATUS check) and 10 (Execute). Three-tier scope: (a) action-recipient unconditional / (b) cluster_mediating unconditional / (c) info-recipient cluster-filtered (primary BANK_COLLATERAL/PC_STRESS/FED_FRAMEWORK/CONSUMER_STAGFLATION + secondary IRAN_HORMUZ/ASIA_CHINA/AI_INFRA_CAPEX on bank-ticker hit + skip POSITIONING_VALUATION/HYDROCARBON_INFRA/MISC). Cost ~30-60s/boot.

### WALTER-side (2 new files + 2 spec edits)

**(4) `AGENTS/WALTER/design/CROSS_REFS/REGINALD.md` v0.1** — 216 lines, 8 sections (modeled on `design/CROSS_REFS/RED.md` canonical pattern):
- §0 Operational state pointers (STATUS / CALENDAR / workbook anchors)
- §1 Bank watchlist 5-tier hierarchy with multi-channel scores (Q4-A overlap surface)
- §2 Predictions REG-NN active + recent-resolved (REG-01..25)
- §3 KB anchors (KB-WAL ~105 / KB-REG ~116 / KB-OZK peer ~185 / VX 59 / FLOW 22)
- §4 Channel codes — 8-channel framework → v0.9 `bank_transmission` enum (Q4-B)
- §5 Cross-bank pattern keys — 7 cohort/structural indicators (Q4-C)
- §6 Specific exposure terms — 8 high-precision greppable strings (Q4-D)
- §7 Thresholds pointer (cross-ref to THRESHOLDS.tsv)
- §8 Calendar pointer (cross-ref to CALENDAR.md + future CALENDAR_DATA.tsv)

Read-by WALTER at dispatch-time (NOT boot — too dense; lookup-on-demand only). Refresh-trigger on REGINALD STATUS bump / KB-VX-FLOW row add / watchlist add-remove / threshold tune / CALENDAR event add-remove.

**(5) `AGENTS/WALTER/registry/REG_THRESHOLDS_FIRED_LOG.tsv`** (header-only) — 5-col WALTER-owned fire-history ledger for REG-T-NN namespace. Schema identical to FALSIFICATION_FIRED_LOG.tsv (RED-FT-NN ledger). Appended per CHECKLIST v0.10 Phase 2 step 7 on each REG-T fire. Architecture preserves Critical Rule #2 (fire history in WALTER tree, not REGINALD tree).

**(Spec edit 1) `AGENTS/WALTER/design/ROUTING_TABLE.md`** v0.8 → v0.9 — new "By Convergence" section after By Boundary Threshold. Auto-fire `signal_type: convergence_event` precedence IMMEDIATE override on N≥2 prior BOARD signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern. Recipient chain: REGINALD action + originating-channel agents info + RED info. Detection ~50-200ms cluster-filtered grep at dispatch; estimated volume ~1-2 convergence_events/week.

**(Spec edit 2) `AGENTS/WALTER/CLAUDE.md` spawn-protocol step 6b** — extended from single-registry (7 RED-FT rows) to multi-registry (7 RED-FT + 8 REG-T = 15 total triggers v0.1) read at boot. Build combined in-memory trigger array; carry forward to dispatch phase. Sustain-window discipline documented inline (REG-T-01/02/05 sustain=1 binary-trigger vs REG-T-03/04/06/07/08 sustain=3 credit-metric noise filter).

---

## Q4 4-dim exposure-overlap surface (canonical, REGINALD owns)

Per REGINALD LIAISON Turn 3 ship. WALTER caches in CROSS_REFS/REGINALD.md §1+§4+§5+§6.

### Dim A: Bank tickers (5-tier hierarchy)

```
TIER-1 (max-stress):     EGBN, WAL                     [scores 20, 20]
TIER-2 (elevated):       CFG, ZION, SSB, FLG           [scores 15, 8-9, 11, 8]
NEW-TRACKING (May 8):    FITB, HBAN                    [TBD]
EXTERNAL-WATCH:          MTB (Baltimore CRE), VLY      [watchlist-context tier]
PEER-ROUTED:             OZK (→ AGENTS/OZK/ action)    [13, peer]
HISTORICAL-ON-WATCH:     FBC, WBS, BHRB, FHN           [BANK_EXPOSURE_MATRIX]
```

**Routing rule:** any string-match on TIER-1+TIER-2+NEW-TRACKING+EXTERNAL-WATCH ticker → REGINALD-info MANDATORY regardless of sub-agent action. **OZK exception:** OZK signals route to `../OZK` action; REGINALD-info ONLY when OZK signal also touches another REGINALD-watchlist ticker (cohort signal).

### Dim B: 8-channel codes (`bank_transmission` v0.9 enum candidate)

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

v0.9 enum candidate (snake_case): `cre / hidden_cre / ndfi / private_credit / mfs_fraud / cmbs_maturity / fed_layoffs / stagflation_trap`. Pre-cosigned for V0_9_STACK.md tracker alongside BRENT's `energy_transmission` (10-val) + `regime_state` (5-val). **FORMAT_SPEC v0.9 bump deferred to batched ship per Will-walkthrough-grouped-by-weight pattern.**

### Dim C: Cross-bank pattern keys (cohort/structural indicators)

```
cohort_fade_pattern        — 12/12 active; reset on any miss-into-rally print
fhlb_bifurcation           — 4/3 split (DECLINE: FITB,RF,ZION,VLY  / SURGE: MTB,CFG,PNC)
provisions_mask_deterioration  — VLY -66% YoY tell; CFG candidate
office_single_point_concentration  — WAL Slide 12 38% / EGBN 10-Q text
hidden_cre_relabeling_trajectory   — MI3 quarterly delta tracking
mi3_rcon2746_screen        — Hidden CRE methodology applied to any bank
ndfi_breakout_decomposition  — capital-call vs secured-PC vs other-finance trajectory
```

**Routing rule:** any pattern-key string-match → REGINALD-info MANDATORY **even when no specific bank ticker named**. These are cohort-level patterns where REGINALD synthesizes across names.

### Dim D: Specific exposure terms (high-precision greppable strings)

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

### Sub-agent fan-out convention (Q4 follow-up LOCK)

| Signal type | Routing rule |
|-------------|--------------|
| **Bank-exposure-context-touching** (ticker OR channel OR pattern OR exposure-term hit) | sub-agent **action** + **REGINALD info unconditional** |
| **Pure sub-agent domain** (BDC NAV / CMBS market-level / FL HOA — no bank ticker) | sub-agent action / REGINALD-info ONLY when bank-exposure tie surfaces |
| **REGINALD-thesis-side mediating** (multi-channel convergence at named bank — see ROUTING_TABLE v0.9 By Convergence) | **REGINALD action** + sub-agent info |

Sub-agents: BROCK (BDC/PC, top-level peer) / CREED (CRE market-level) / CORAL (Florida-specific).

---

## V0_9_STACK pre-cosigns (informational, not Will-sign-off-blockers)

Three FORMAT_SPEC v0.9 enum candidates accumulated across the last three LIAISONs. Batched ship deferred per Will-walkthrough-grouped-by-weight cadence; will-surface timing TBD.

| Enum | Source LIAISON | Values | Status |
|------|----------------|--------|--------|
| `energy_transmission` (10-val) | BRENT 5/5-6 | TBD (per BRENT spec) | Pre-cosigned 5/6 |
| `regime_state` (5-val) | BRENT 5/5-6 | TBD (per BRENT spec) | Pre-cosigned 5/6 |
| `bank_transmission` (8-val) | REGINALD 5/10-11 | cre / hidden_cre / ndfi / private_credit / mfs_fraud / cmbs_maturity / fed_layoffs / stagflation_trap | Pre-cosigned 5/11 |

---

## Open externalities (post-LIAISON, not close-blockers)

1. **REGINALD BOARD_LOG.tsv backfill execution** on 16 missed-action signals → separate REGINALD-session task; 32-row backfill stub already in place
2. **CARL DATA_RELEASE_CALENDAR.md pattern landing** (~May 17-20) → REGINALD ships `CALENDAR_DATA.tsv` ~7d later (~May 17-27)
3. **WALTER CROSS_REFS/CARL.md + CROSS_REFS/BRENT.md scaffolds** — next WALTER session per LAST_COMPLETION FOLLOW-UP; pattern now battle-tested via RED.md + REGINALD.md
4. **WALTER V0_9_STACK.md `bank_transmission` row-add** — next WALTER session
5. **WALTER design/STATE.md maintenance bump** — ROUTING_TABLE v0.8→v0.9 + spawn-protocol 6b update + REG_THRESHOLDS_FIRED_LOG new file row
6. **Calibration cycle 1 trigger** 2026-05-25 calendar OR N=15 forward BOARD dispositions (early-fire) — synced w/ BRENT clock

---

## BOARD_CONSUMPTION rollout state (post-REGINALD)

| Agent | Boot-step status | Calibration cycle 1 |
|-------|-----------------|---------------------|
| CARL | ✅ shipped 4/20 (v0.1 reference) | 5/19 trigger |
| BRENT | ✅ shipped 5/6 (BRENT_ORIGIN pattern variant) | 5/20-27 ETA |
| RED | ✅ shipped 5/6 (consumption-mode-not-yet-ledger) | 5/20 ETA |
| **REGINALD** | ✅ shipped 5/11 (this LIAISON) | **5/25 OR N=15** |
| WALTER itself | n/a (router) | — |
| HENRY | 🟡 PENDING | LIAISON open candidate next-session |
| NEXUS | 🟡 PENDING | Blocked on NEXUS spawn (37d STALE) |
| BROCK | 🟡 PENDING | Mid-priority |
| 8 others | ⬜ open backlog | Opportunistic LIAISON-by-LIAISON |

**Rollout cadence:** opportunistic LIAISON-by-LIAISON, not WALTER-driven push. 4-of-5 Tier-1-CC agents complete (CARL/BRENT/RED/REGINALD); WALTER is the router (no boot-step needed for itself).

---

## Empirical-reframe pattern — regime-level finding

3-of-3 substantive LIAISONs (RED / BRENT / REGINALD) had target-agent's Turn 1 framing on WALTER dispatch surface measurably off:

| LIAISON | Target Turn 1 framing | Reality (WALTER grep) | Reframe magnitude |
|---------|----------------------|----------------------|-------------------|
| RED 5/6 | "WALTER mostly absent" | RED in to/info on 107/110 BOARD signals (97%) | High — inverted framing |
| BRENT 5/5-6 | (tighter framing; closer match) | 47-signal back-disposition pass surfaced | Low — magnitude-only |
| REGINALD 5/10-11 | "None of 51 were ACTION; all info" | 16 ACTION + 33 info + 2 body-mention | High — direction-flipping |

**Bias mechanism:** target-agents underestimate WALTER dispatch volume because they aren't *consuming* dispatches. The 48-signal gap (REGINALD) and 107-signal-on-RED-record-with-1-direct-route (RED) are symptoms of the same systemic problem — agents process inbox push, not BOARD pull.

**Keystone fix:** BOARD_CONSUMPTION rollout (each agent's CLAUDE.md boot-step BOARD diff scan). After REGINALD ships Boot Step 9b 5/11, 4-of-5 Tier-1-CC agents have boot-step (CARL/BRENT/RED/REGINALD); 11 remaining agents in backlog. Pattern transferable to HENRY/NEXUS/BROCK next-LIAISONs.

**Process discipline takeaway (for future LIAISONs):** every Turn 2 should bring routing-side data the target agent can't see (counts of to:/info: appearances, verdict distribution, cluster_mediating volume) regardless of whether target's Turn 1 surfaced a gap. Costs ~5min of grep; saves potentially-mis-architected outputs.

---

## Convergence pattern recap (cross-LIAISON tracking)

| Channel | Date | Turns | Time to converge | Notable accelerators |
|---------|------|-------|------------------|----------------------|
| CARL | 5/5-6 | 7 | ~24-30hr | Pilot; no open-with-substance Turn 1 |
| BRENT | 5/5-6 | 5 | <24hr | Substrate-prep doc (BRENT_LIAISON_PREP.md) |
| RED | 5/6 | 5 | <12hr same-day | Open-with-substance Turn 1 + concede-on-data Turn 3 |
| **REGINALD** | **5/10-11** | **5** | **<13hr UTC** | **Measurable retrospective Turn 1 + accelerated-wrap-Turn-4** |

**Pattern locked at 4-5 turns for substantive Turn 1 + retrospective-with-data.** Apply: HENRY / NEXUS / BROCK next-LIAISONs aim for 4-turn architectural-thread baseline.

---

## Will-readable summary table (what changed at the network level)

| Domain | Before this LIAISON | After |
|--------|---------------------|-------|
| BOARD-pull mechanism | 3 of 5 Tier-1-CC (CARL/BRENT/RED) | **4 of 5 (+ REGINALD)** |
| Threshold registries WALTER reads at boot | 1 (RED-FT 7 rows) | **2 (RED-FT 7 + REG-T 8 = 15 total)** |
| Fire-history ledgers | 1 (FALSIFICATION_FIRED_LOG) | **2 (+ REG_THRESHOLDS_FIRED_LOG)** |
| ROUTING_TABLE version | v0.8 | **v0.9 (+ By Convergence section)** |
| CROSS_REFS scaffolds | 1 (RED.md) | **2 (+ REGINALD.md)** |
| LIAISON channels active-converged | 3 (CARL/BRENT/RED) | **4 (+ REGINALD)** |
| FORMAT_SPEC v0.9 stack candidates | 2 (energy_transmission + regime_state) | **3 (+ bank_transmission)** |
| BOARD_LOG disposition ledgers | 1 (CARL v0.1) | **2 (+ REGINALD 11-col CARL+2)** |

---

*Stitched final 2026-05-11. Per-agent sections in `AGENTS/REGINALD/design/JOINT_PROPOSAL_2026-05-11_reginald_sections.md` + `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-11_walter_sections.md`. Source dialog: `AGENTS/REGINALD/handoff_WALTER/LIAISON.md`. Will-surface ready.*
