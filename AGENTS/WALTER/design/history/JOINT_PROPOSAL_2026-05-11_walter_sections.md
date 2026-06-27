# JOINT PROPOSAL — WALTER ↔ REGINALD LIAISON wrap (WALTER sections)

*WALTER-side sections (§2 + §4) of the joint-proposal artifact bundling the WALTER ↔ REGINALD LIAISON Turns 1-5 (2026-05-10 23:11 UTC → 2026-05-11 11:42 UTC). Per LIAISON_PLAYBOOK §8 closing pattern. Pairs with REGINALD §1 + §3 (`AGENTS/REGINALD/design/JOINT_PROPOSAL_2026-05-11_reginald_sections.md`). Will-mediated stitched final at `design/JOINT_PROPOSAL_2026-05-11_reginald_walter.md` repo-root.*

*Source dialog:* `AGENTS/REGINALD/handoff_WALTER/LIAISON.md` (5 turns, 712 lines).

---

## §2 — Instantiated files (WALTER-side audit)

### 2.1 `AGENTS/WALTER/design/CROSS_REFS/REGINALD.md` v0.1 (216 lines, 8 sections)

Denormalized identifier-cache for WALTER dispatch-time grep. Modeled on `AGENTS/WALTER/design/CROSS_REFS/RED.md` scaffold (canonical CROSS_REFS pattern, post RED LIAISON 5/6).

**Section structure:**
- **§0 Operational state pointers** — REGINALD STATUS / CALENDAR / workbook anchors (BANK_EXPOSURE_MATRIX / CHANNELS / CONVERGENCE / CRE_ARCHITECTURE / NDFI_RESEARCH paths)
- **§1 Bank watchlist (Q4-A overlap surface)** — 5-tier hierarchy with multi-channel scores: TIER-1 EGBN(20)/WAL(20) + TIER-2 CFG(15)/ZION(8-9)/SSB(11)/FLG(8) + NEW-TRACKING FITB/HBAN + EXTERNAL-WATCH MTB/VLY + PEER-ROUTED OZK + HISTORICAL FBC/WBS/BHRB/FHN
- **§2 Predictions (REG-NN)** — active + recent-resolved with confidence + status; REG-01 through REG-25 (most recent additions Apr 24 — REG-24 WAL Office classified + REG-25 WAL ex-fraud NCO; recent resolution REG-20 ✅ CONFIRMED-PARTIAL 2026-05-08)
- **§3 KB anchors** — KB-WAL-NNN (~105 rows WAL-specific deep dive) / KB-REG-NNN (~116 rows general bank-thesis) / KB-OZK-NNN (~185 rows PEER AGENT, OZK-specific) / VX-REG-NN (59 rows counter-evidence) / FLOW-REG-N (22 rows transmission paths)
- **§4 Channel codes (Q4-B overlap surface)** — 8-channel framework → v0.9 `bank_transmission` enum candidate
- **§5 Cross-bank pattern keys (Q4-C overlap surface)** — 7 cohort/structural indicators (cohort_fade_pattern / fhlb_bifurcation / provisions_mask_deterioration / office_single_point_concentration / hidden_cre_relabeling_trajectory / mi3_rcon2746_screen / ndfi_breakout_decomposition)
- **§6 Specific exposure terms (Q4-D overlap surface)** — 8 high-precision greppable strings (Memo Item 3 / RCON2746 / FHLB advance / Schedule O / Table 16 / criticized assets / classified assets / 30-89 day past due / Special Mention / Capital call / office concentration / hidden CRE / MI3)
- **§7 Thresholds pointer** — cross-ref to `AGENTS/REGINALD/registry/THRESHOLDS.tsv` 8 rows + WALTER spawn-protocol step 6b auto-dispatch mechanics
- **§8 Calendar pointer** — cross-ref to `AGENTS/REGINALD/CALENDAR.md` markdown + future `CALENDAR_DATA.tsv` machine-parseable

**Refresh trigger discipline:**
| Trigger | Sections to refresh | Cost |
|---------|--------------------|------|
| REGINALD STATUS bump | §0 + §1 + §2 + recent-activity | ~5min |
| New KB / VX / FLOW row | §3 row counts | ~1min |
| Watchlist add/remove | §1 + §0 | ~5min |
| New REG-NN prediction | §2 | ~2min |
| Threshold tune (REG-T-NN) | §7 | ~2min |
| CALENDAR event add/remove | §8 | ~3min |
| BANK_EXPOSURE_MATRIX scoring change | §1 multi-channel score column | ~3min |
| New cohort pattern surfaced | §5 | ~5min |

**Read-by:** WALTER at signal-dispatch time (NOT at boot — too dense for boot read; lookup-on-demand only).

**Pattern locked:** WALTER-side CROSS_REFS scaffold is now the second instance (RED 5/6 + REGINALD 5/11). Pattern transferable to CARL + BRENT (carry-forward WALTER self-task next session per LAST_COMPLETION FOLLOW-UP).

### 2.2 `AGENTS/WALTER/design/ROUTING_TABLE.md` v0.8 → v0.9 (By Convergence section)

New section inserted after By Boundary Threshold (v0.8). Auto-fire `signal_type: convergence_event` precedence IMMEDIATE override on N≥2 prior BOARD signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern.

**Rule structure (2 conditions):**

| Detection condition | Action | Recipient chain |
|---------------------|--------|-----------------|
| N≥2 prior BOARD signals within 5-session window mention same bank ticker (from CROSS_REFS/REGINALD.md §1 watchlist: TIER-1 / TIER-2 / NEW-TRACKING / EXTERNAL-WATCH tiers) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | REGINALD action + originating-channel agents info + RED info |
| N≥2 prior BOARD signals within 5-session window touch same cross-bank pattern key (from CROSS_REFS/REGINALD.md §5: cohort_fade_pattern / fhlb_bifurcation / provisions_mask_deterioration / office_single_point_concentration / hidden_cre_relabeling_trajectory / mi3_rcon2746_screen / ndfi_breakout_decomposition) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | REGINALD action + originating-channel agents info + RED info (cohort-level convergence is RED-watchable as structural-bifurcation candidate) |

**Detection mechanics:** cluster-filtered grep at dispatch on BANK_COLLATERAL / PC_STRESS / FED_FRAMEWORK / CONSUMER_STAGFLATION sections (secondary expand on bank-ticker hit); ~50-200ms cost; estimated volume ~1-2 convergence_events/week.

**dispatch_note format:** prior signal IDs + count + cluster + date / convergence type (ticker vs pattern-key vs both) / channel codes touched / cluster_mediating tag if cross-cluster.

**De-dupe behavior:** RED-info appears once even when multiple v0.7+ rules compose (cluster_mediating + CORRECTED-FRAMING + convergence_event); single convergence_event signal even when multi-trigger fires.

**Composition with other rules:**
- v0.7 By Tag/By Verdict still applies (cluster_mediating + CORRECTED-FRAMING auto-cc RED)
- v0.8 By Boundary Threshold still applies (BRENT-IMMEDIATE 8-row crosses)
- Safety Net Auto-Upgrades still apply (VIX>30 / HY OAS +25bps)

### 2.3 `AGENTS/WALTER/CLAUDE.md` spawn-protocol step 6b update

Extended from single-registry (RED FALSIFICATION_TRIGGERS) to multi-registry (RED-FT-NN + REG-T-NN) read at boot:

**Before (5/6 ship):** read 1 registry (7 RED-FT rows) + 1 fire-log (FALSIFICATION_FIRED_LOG)

**After (5/11 update):** read 2 registries (7 RED-FT + 8 REG-T = 15 total triggers v0.1) + 2 fire-logs (FALSIFICATION_FIRED_LOG + REG_THRESHOLDS_FIRED_LOG). Build combined in-memory trigger array; carry forward to dispatch phase.

**Sustain-window discipline noted in protocol:**
- REG-T-01 KRE<$60 sustain=1 (binary-trigger fire-now)
- REG-T-02 WAL<$78 sustain=1 (binary-trigger)
- REG-T-05 INITIAL-CLAIMS>300K sustain=1 (binary-trigger)
- REG-T-03/04 HY-OAS / REG-T-06 FHLB / REG-T-07 OFFICE-CMBS-DQ / REG-T-08 SOFR-IORB all sustain=3 (credit metrics noise-smoothed)

**Architecture preserves Critical Rule #2** (don't restate from prior surface text — fire history lives in WALTER-owned ledgers, not RED/REGINALD trees).

### 2.4 `AGENTS/WALTER/registry/REG_THRESHOLDS_FIRED_LOG.tsv` (NEW, header-only)

5-col WALTER-owned fire-history ledger for REG-T-NN namespace. Schema identical to FALSIFICATION_FIRED_LOG.tsv (the RED-FT-NN ledger):

```
trigger_id  fired_date  metric_value_at_fire  dispatched_signal_id  sustain_confirmation
```

Appended on each REG-T fire per CHECKLIST v0.10 Phase 2 step 7 (eval pass mechanics unchanged — query market-data, threshold + sustain check, suppress repeat-fires within sustain_window, append fire row, dispatch downstream per recipient_chain).

Header-only at ship — first fire will instantiate first data row. Stale-fire suppression lookup at next-fire-check identical to RED-FT pattern.

---

## §4 — Cross-agent decisions (Q-trail summary)

Compact Q-by-Q decision-lock table mirroring REGINALD §3 architectural-locks summary but tracing WALTER-side rationale:

### Q1 — Boot-step BOARD scan, scoped

WALTER Turn 2 accepted 3-tier scope per REGINALD Turn 1 proposal: (a) action-recipient unconditional / (b) cluster_mediating unconditional / (c) info-recipient cluster-filtered diff-against-last-session. WALTER calibration on (c): primary clusters BANK_COLLATERAL/PC_STRESS/FED_FRAMEWORK/CONSUMER_STAGFLATION + secondary clusters IRAN_HORMUZ/ASIA_CHINA/AI_INFRA_CAPEX on bank-ticker hit + skip POSITIONING_VALUATION/HYDROCARBON_INFRA/MISC unless cluster_mediating fires. **Lock both sides Turn 2/3.**

### Q2 — Threshold-cross auto-dispatch

WALTER Turn 2 DECISION: yes, publish as REG-T-NN registry mirror of RED-FT-NN; identical 8-col schema. WALTER Turn 4 confirmed REG-T-01 sustain=1 binary-trigger discipline (KRE crash-through-$60); same logic REG-T-02 WAL<$78 + REG-T-05 Claims>300K. Other 5 thresholds sustain=3 (credit-metric noise filter). **Lock both sides Turn 3; WALTER Turn 4 ship spawn-protocol 6b + FIRED_LOG.**

### Q3 — Bank-watchlist cross-ref at dispatch

WALTER Turn 2 DECISION: yes, high-leverage; pair with Q8 CROSS_REFS scaffold. Pattern is identifier-cache lookup (RED CROSS_REFS / CARL CROSS_REFS): WALTER owns the cache, REGINALD owns the source-of-truth in STATUS/workbook/BANK_EXPOSURE_MATRIX. Refresh-trigger on REGINALD KB-row add or threshold change or watchlist add/remove. **Lock both sides Turn 2; WALTER Turn 4 ship CROSS_REFS/REGINALD.md §1.**

### Q4 — Sub-agent fan-out routing + exposure-overlap-key list

WALTER Turn 2 proposed 3-tier routing table (bank-exposure-context-touching → sub-agent action + REGINALD-info mandatory / pure sub-agent domain → sub-agent action / REGINALD-thesis-mediating → REGINALD action). REGINALD Turn 3 delivered 4-dim overlap-key list (A bank tickers + B 8-channel codes + C cross-bank pattern keys + D specific exposure terms). **Lock both sides Turn 3; WALTER Turn 4 ship CROSS_REFS/REGINALD.md §1+§4+§5+§6.**

### Q5 — Convergence-event detection

WALTER Turn 2 DECISION: yes, build atop named-entity grep from Q3. REGINALD Turn 3 preferred ROUTING_TABLE v0.9 "By Convergence" section over standalone doc (incremental routing-rule extension, not new conceptual layer; one fewer doc to maintain). WALTER Turn 4 SHIP ROUTING_TABLE v0.9 (§2.2 above). **Lock both sides Turn 3.**

### Q6 — Earnings/Call-Report cycle pre-positioning

WALTER Turn 2 DECISION: yes, calendar-driven dispatch overlay is clean (separate from content-driven). REGINALD Turn 3 proposed dual-doc CALENDAR (markdown primary + TSV machine-parseable). WALTER Turn 4 ACCEPT; TSV instantiation deferred to REGINALD self-task ~7d post-CARL DATA_RELEASE_CALENDAR.md landing (~May 17-20 ETA). **Schema lock Turn 3; instantiation deferred.**

### Q7 — BOARD_LOG.tsv stand-up

WALTER Turn 2 DECISION: yes; 11-col schema = CARL 9-col + REGINALD-specific Channels_Touched + Bank_Tickers. **Lock both sides Turn 2; REGINALD Turn 3 ship 32-row backfill stub** (3 INTEGRATED Apr 14 + 16 BACKFILL action-primary + 13 BACKFILL info-cc + 3 PROME-pinch-hitter 5/9 BACKFILL-PENDING).

### Q8 — CROSS_REFS/REGINALD.md scaffold

WALTER Turn 2 DECISION: yes, top of WALTER self-task queue. Modeled on `AGENTS/WALTER/design/CROSS_REFS/RED.md` (canonical pattern). **Lock both sides Turn 2; WALTER Turn 4 ship v0.1.**

### Empirical-reframe pattern (cross-cutting)

WALTER Turn 2 grep-pass disconfirmed REGINALD Turn 1 claim "None of the 51 were ACTION → REGINALD; all were info." Actual: **16 ACTION + 33 info + 2 body-mention**. REGINALD Turn 3 explicitly accepted the correction.

**Pattern locked across 3 substantive LIAISONs:**
- RED Turn 1 "WALTER mostly absent" → grep showed 97% routing target (107/110 BOARD signals)
- BRENT Turn 1 framing tighter (47-signal back-disposition pass — closer match)
- REGINALD Turn 1 "zero action" → grep showed 16 ACTION

**Bias mechanism:** target-agents underestimate WALTER dispatch volume because they aren't *consuming* dispatches. BOARD-consumption rollout (each agent's CLAUDE.md boot-step) is the keystone fix. 4-of-5 Tier-1-CC agents now have boot-step (CARL/BRENT/RED/REGINALD); WALTER itself is 5th; 11 remaining agents in BOARD_CONSUMPTION rollout backlog.

**Process discipline takeaway:** every future LIAISON Turn 2 should bring routing-side data the target agent can't see (counts of to:/info: appearances, verdict distribution, cluster_mediating volume) regardless of whether target's Turn 1 surfaced a gap.

---

## §5 — Future-work / open externalities

(Not Will-sign-off-blockers — informational status of items downstream of this LIAISON close.)

### 5.1 V0_9_STACK additions

`bank_transmission` enum 8-val pre-cosigned (REG §3.2 / WAL §2.1 §4 / V0_9_STACK.md tracker pending row-add). Joins:
- `energy_transmission` (BRENT LIAISON 5/5-6, 10-val)
- `regime_state` (BRENT LIAISON 5/5-6, 5-val)

FORMAT_SPEC v0.9 batched ship deferred per Will-walkthrough-grouped-by-weight cadence. Will-surface timing TBD; likely when v0.9 stack reaches 4-5 candidates or one becomes load-bearing.

### 5.2 REGINALD self-tasks (LIAISON-deliverable downstream)

| Task | Trigger | ETA |
|------|---------|-----|
| BOARD_LOG.tsv full disposition backfill on 16 missed-action signals | Next REGINALD session | Open |
| CALENDAR_DATA.tsv instantiation | ~7d post-CARL DATA_RELEASE_CALENDAR.md landing | ~May 17-27 |
| BOARD_LOG `Channels_Touched` column snake_case conversion | On FORMAT_SPEC v0.9 ship | Deferred |

### 5.3 WALTER self-tasks (LIAISON-deliverable downstream)

| Task | Trigger | ETA |
|------|---------|-----|
| CROSS_REFS/CARL.md + CROSS_REFS/BRENT.md cache scaffolds | Next WALTER session | This week |
| V0_9_STACK.md tracker `bank_transmission` row-add | Next WALTER session | This week |
| design/STATE.md maintenance bump (ROUTING_TABLE v0.8→v0.9 + spawn-protocol 6b) | Next WALTER session | This week |
| BOARD_CONSUMPTION_SPEC v0.2 dual-pattern doc (CARL v0.1 + REG-pattern) | Post-CARL CROSS_REFS scaffold | This week |

### 5.4 Calibration cycle 1 clock (NEW from this LIAISON)

- **Primary trigger:** 2026-05-25 (14d from Turn 5 close)
- **Early-fire alternative:** N=15 forward BOARD dispositions in REGINALD `board/BOARD_LOG.tsv` (whichever first)
- **Sync:** matches BRENT clock per WALTER Turn 4 note
- **At trigger:** REGINALD post-hoc calibration deltas (verify-verdict accuracy on routed signals; missed-route catches; threshold-fire false-positives) → WALTER tunes verify-research thresholds + routing-rule refinements

### 5.5 BOARD_CONSUMPTION rollout state (post-REGINALD)

| Agent | Status | Notes |
|-------|--------|-------|
| CARL | ✅ shipped 4/20 (v0.1 reference) | Calibration cycle 1 trigger 5/19 |
| BRENT | ✅ shipped 5/6 (BRENT_ORIGIN pattern variant) | Calibration cycle 1 ETA 5/20-27 |
| RED | ✅ shipped 5/6 (consumption-mode-not-yet-ledger variant) | Calibration cycle 1 ETA 5/20 |
| REGINALD | ✅ shipped 5/11 (this LIAISON) | Calibration cycle 1 5/25 OR N=15 |
| WALTER itself | n/a (router) | — |
| **HENRY** | 🟡 PENDING | Top of remaining queue; LIAISON open candidate next-session |
| **NEXUS** | 🟡 PENDING | Blocked on NEXUS spawn (STALE 37d) |
| **BROCK** | 🟡 PENDING | Mid-priority |
| **8 others** | ⬜ open backlog | LABOR/MARCO/SAM/ZHAO/LIQUID/HAWK/HANS/SHADE etc. |

Rollout cadence: opportunistic LIAISON-by-LIAISON; not a separate WALTER-driven push.

---

*WALTER §2 + §4 ship. Pair with REGINALD `JOINT_PROPOSAL_2026-05-11_reginald_sections.md` §1 + §3. Will-mediated stitched final at `design/JOINT_PROPOSAL_2026-05-11_reginald_walter.md` repo-root.*
