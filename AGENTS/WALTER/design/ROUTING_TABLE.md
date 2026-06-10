# WALTER Routing Table v0.10

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.

**Version history:**
- **v0.10 (Jun 10):** Split the bundled `MARKET_VOL` row per the HENRY/VIOLET vol-ownership decision (auto-memory `feedback_henry_vol_broadcast_to_violet`: VIOLET owns vol-regime broadcast; HENRY keeps gamma/0DTE/put-wall). Vol-regime / VIX-complex / term-structure content → VIOLET action (HENRY backup); dealer-gamma / 0DTE / index-move mechanics → HENRY action (unchanged). Single `MARKET_VOL` domain code retained (no FORMAT_SPEC change — within-domain routing split, same pattern as Apr 20 residential-housing exception). Proposed by VIOLET via SIGNAL_INTAKE.md rebuild Appendix A flag (2026-06-10); Will approved 2026-06-10.
- **v0.9 (May 11):** Added "By Convergence" section after By Boundary Threshold — auto-fire `signal_type: convergence_event` to REGINALD-action when BOARD INDEX scan finds N≥2 prior signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern. Detection via CROSS_REFS/REGINALD.md §1 watchlist + §5 pattern keys. Per REGINALD ↔ WALTER LIAISON Q5 (Turn 1 → Turn 4 LOCK 2026-05-11). v0.9 stack candidate `bank_transmission` enum (8-val: cre / hidden_cre / ndfi / private_credit / mfs_fraud / cmbs_maturity / fed_layoffs / stagflation_trap) pre-cosigned in V0_9_STACK.md tracker for batched FORMAT_SPEC v0.9 ship.
- **v0.8 (May 8):** Added "By Boundary Threshold" section after By Tag/By Verdict — 8-row BRENT-IMMEDIATE threshold-cross dispatch list per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c (3-way cosigned BRENT+CARL+WALTER 2026-05-05/06; Will sign-off 2026-05-08). Adds threshold-cross row mechanics: single-day breach = watch (no dispatch); 2-3 sess sustained = dispatch; single-print operational minima (#3 Cushing) = dispatch on print itself; re-fire convention (only on re-cross of boundary in either direction, not on continued state). BRENT-fire-as-primary; WALTER-fire-as-fallback if BRENT >5d STATUS lag. Detection via FORGE/tools/market-data + EIA scheduled scans (per §2b Phase 2 dependency). Updated By Tag/By Verdict section to reference v0.8 canonical `signal_role: cluster_mediating` form, retiring v0.7 prose-tag interim discipline.
- **v0.7 (May 6 PM):** Added "By Tag/By Verdict" section after By Signal Type table — three rules (cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`) + de-dupe rule + interim prose-tag discipline (pre-v0.8). Per RED ↔ WALTER LIAISON Q9-Q12 + JOINT_PROPOSAL_2026-05-06_red_walter §3 (Will sign-off 2026-05-06).
- **v0.6 (May 6):** Added "Iran-cluster CARL-info override" section after Residential-housing exception. Iran-cluster signals (cluster: IRAN_HORMUZ) route CARL info ONLY on concrete Brent thresholds (≥$110 sustained 2 sess OR ≤$95 sustained 5 sess) OR explicit kinetic event with supply-disruption mechanism OR FX/macro cross with consumer-burden vector. Posture/doctrine/diplomatic-cascade/OSINT signals → drop CARL. Added boundary-trigger threshold-cross dispatch sub-rule (≤$95/5sess and ≥$115/5sess fire IMMEDIATE → CARL with KB-CARL-259 + Vector #5/#12 + CRL-08 cross-refs). Per CARL ↔ WALTER LIAISON Q3 2026-05-05. **BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred pending Will sign-off on JOINT_PROPOSAL §2c.**
- **v0.5 (Apr 20):** Added `thesis-frame` row to By Signal Type table (matches FORMAT_SPEC v0.5 enum add). Added "Residential-housing stress exception" note under By Signal Domain table — geographically-narrow residential signals route REGINALD action / CARL info, not the reverse. Rule filed Apr 20 2026 after Will corrected a default-CARL routing for NV HOA SIG-W-20260420-005. Part of Filter v2 Segment A.
- **v0.4 (Apr 14):** Added ASIA_CONTAGION + UST_FOREIGN rows (ZHAO primary) to match FORMAT_SPEC v0.4. Closes vocabulary gap surfaced by 2026-04-14 FT China-trade signals (SIG-W-20260414-010/011).
- **v0.3 (Apr 11 PM):** Re-labeled all rows with canonical domain codes (LABOR, MACRO_INFLATION, etc.) to match FORMAT_SPEC v0.3 Domain Vocabulary. Resolves Gap C vocabulary drift.
- **v0.2 (Apr 11 AM):** Added MACRO_INFLATION, TARIFF_TRADE, GEOPOL_NON_ENERGY, PRIVATE_CREDIT rows + Backup column.
- **v0.1 (Apr 7):** Initial version.

---

## By Signal Domain

| Domain code | Row description | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-------------|-----------------|--------|--------|-----------------|-------------------|---------------|
| `LABOR` | Employment — NFP, claims, JOLTS, wages, U-3, LFPR | CARL | HENRY | HENRY, RED | IMMEDIATE (data day) / PRIORITY (analysis) | LABOR_DOWNSTREAM |
| `MACRO_INFLATION` | Inflation + growth — CPI, PCE, PPI, UMich, GDP, ISM, retail sales | CARL | HENRY | HENRY, LIQUID, RED | IMMEDIATE (data day) / PRIORITY (analysis) | THESIS_CORE |
| `TARIFF_TRADE` | Executive orders, tariff changes, trade deals | CARL | HENRY | HENRY, REGINALD, RED, MARCO | IMMEDIATE (announcement) / PRIORITY (analysis) | THESIS_CORE |
| `CONSUMER_CREDIT` | CC/auto/student loan delinquency, household debt | CARL | REGINALD | REGINALD, RED | PRIORITY | THESIS_CORE |
| `BANK_CRE` | Bank earnings, CRE, hidden CRE (MI3), NDFI, capital rules | REGINALD | BROCK | BROCK, LIQUID, RED | IMMEDIATE (earnings) / PRIORITY (research) | CREDIT_CHAIN |
| `FUNDING_LIQUIDITY` | HY OAS, SOFR, repo, RRP, dealer capacity, Treasury auctions | LIQUID | HENRY | BROCK, SHADE, HENRY | IMMEDIATE (stress) / PRIORITY (monitoring) | CREDIT_CHAIN |
| `PRIVATE_CREDIT` | BDC gates, PC fund redemptions, PIK rates, software PE, PCDR | BROCK | SHADE | LIQUID, REGINALD, RED | PRIORITY | CREDIT_CHAIN |
| `INSURANCE_SHADOW` | PE-insurer nexus, reinsurance, Level 3, captive insurers | SHADE | BROCK | LIQUID, BROCK | PRIORITY | — |
| `OIL_ENERGY` | Crude prices, OPEC, facility damage, refining, shipping | HAWK | BRENT | BRENT, RED | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_ENERGY` | Hormuz, Gulf infrastructure strikes, chokepoints | HAWK | BRENT | BRENT, SAM | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_NON_ENERGY` | Ceasefires, diplomacy, nuclear, war outside supply | HANS (Tier 2 — spawn) | HAWK | HAWK, BRENT, SAM, RED | PRIORITY | — |
| `JAPAN_BOJ` | USD/JPY, BOJ policy, JGB yields, carry trade, MOF intervention | SAM | LIQUID | LIQUID, RED | IMMEDIATE (intervention) / PRIORITY (monitoring) | — |
| `MARKET_VOL` (vol-regime) | VIX complex, vol regime, term structure, VVIX, SKEW, vol ETP stress, vol-targeting/CTA flows | VIOLET | HENRY | HENRY, LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `MARKET_VOL` (index-mechanics) | Index moves, dealer gamma, 0DTE, put-wall, correlation breaks | HENRY | LIQUID | LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `ASIA_CONTAGION` | China/HK peg, LGFV, HIBOR-SOFR, Chinese trade policy, supply-chain coercion, export-control regs, EM Asia spillover | ZHAO (Tier 2 — spawn) | SAM | RED, HENRY, LIQUID, BRENT/HAWK (when rare-earths), PROME | PRIORITY (policy/research) / IMMEDIATE (CNY intervention, LGFV event) | — |
| `UST_FOREIGN` | TIC flows, foreign UST holder behavior, auction demand composition | ZHAO (Tier 2 — spawn) | BOND (Tier 2) | LIQUID, HENRY, RED | IMMEDIATE (TIC release day) / PRIORITY (composition shifts) | CREDIT_CHAIN |

### Residential-housing stress exception (Apr 20 2026)

Geographically-narrow residential signals — HOA dysfunction, builder-defect litigation, insurance withdrawals with regional clustering, forced-sale price-discovery clusters, local-market residential CRE correlation — route **REGINALD** action with **CARL** info, NOT the reverse.

**Why:** residential → regional-bank-credit transmission is REGINALD's chain (warehouse lines, HELOC origination, forced-sale price discovery, local-market CRE correlation, direct WAL/ZION/OZK earnings-week coverage). CARL is the macro-national consumer-credit primary (NFP, claims, CPI, household-debt aggregate); CARL is NOT the geographically-narrow primary.

**Filed:** Apr 20 2026 after Will corrected a default-CARL routing I'd drafted for NV HOA SIG-W-20260420-005. Routing test case: Del Webb/Pulte Nevada ~80-90 homes + NV AB125 + regional insurance withdrawals + Silver State Bank 2008 precedent = REGINALD, not CARL.

**How to apply at intake:** when a residential signal arrives, ask "is this geographically-narrow OR macro-national?" If the signal names a state/metro/builder/HOA, route REGINALD action + CARL info. If it's a national aggregate (national mortgage delinquency print, national housing starts, Fed Z.1 household leverage), route CARL action per CONSUMER_CREDIT default.

### Iran-cluster CARL-info override (May 6 2026)

Iran-cluster signals (`cluster: IRAN_HORMUZ`) default to OIL_ENERGY → BRENT action with CARL on the info line. Per CARL ↔ WALTER LIAISON Q3 (Turn 1 → Turn 4, locked 2026-05-06): route CARL info **ONLY** when one of the following triggers fires:

| Trigger | Rationale |
|---------|-----------|
| Brent close **≥ $110 sustained 2 sessions** | Re-entry of accelerated pump-pass-through window per KB-CARL-259 (3-4d transmission lag in Iran-cluster regime, vs 2-3wk normal regime). |
| Brent close **≤ $95 sustained 5 sessions** | Exit of pass-through window — material relief in food/energy stack. Vector #5 reprice candidate. |
| Explicit kinetic event with supply-disruption mechanism | Vessel-strike, refinery-hit, port-closure — kinetic-actually-affecting-supply, not posture-only. |
| FX/macro cross with consumer-burden vector | USD/JPY-pump-cost-cross or similar where consumer-burden vector activates. |

**Otherwise:** posture / doctrine / diplomatic-cascade / OSINT signals → **drop CARL from info line.** Examples that would NOT cross-fire to CARL: IRGC corridor doctrine (posture only), USAF tanker emergency squawks (operational anomaly, no supply-disruption mechanism), Iran-Pakistan diplomatic shuttle (diplomatic cascade, no kinetic).

**Why:** within-range tape moves don't reach CARL's pump-pass-through threshold (Vector #5 / #12 / KB-CARL-259); routing them adds noise to CARL intake without informing thesis. Concrete thresholds replace earlier heuristic "near $110" framing.

#### Boundary-trigger threshold-cross dispatch (NEW v0.6)

When Brent sustains:

- **≤ $95 for 5+ sessions** → dispatch IMMEDIATE → CARL with `signal_type: threshold-crossed` + `consumer_transmission: pump_pass_through` + dispatch_note flagging Vector #5 Gas Squeeze + Vector #12 Stagflation reprice + CRL-08 trigger (92→60% per CARL Q12 framework, Turn 3)
- **≥ $115 for 5+ sessions** → dispatch IMMEDIATE → CARL with same tags + flagging Vector #5/#12 hardening + CRL-08 reprice 92→97%+ (per CARL Q12)

Within $95-115 range = noise floor; tape moves don't cross-fire to CARL.

**Q-trail:** CARL LIAISON Q3 (Turn 1) → WALTER Turn 2 DECISION (calibrate going forward) → CARL Turn 3 SHARPENING (concrete thresholds) → WALTER Turn 4 LOCK.

### MARKET_VOL vol-ownership split (Jun 10 2026)

The previously-bundled `MARKET_VOL` row is split into two routing lines (single domain code retained — this is a within-domain routing split, not a vocabulary change):

- **Vol-regime content** — VIX complex, vol-regime classification, term structure (VIX3M/VIX, backwardation/contango), VVIX/vol-of-vol, SKEW/tail pricing, vol ETP stress/termination events, vol-targeting/vol-control/CTA de-risking flows, credit-to-vol transmission timing → **VIOLET action, HENRY backup.**
- **Index-mechanics content** — index price moves, dealer gamma/put-wall/0DTE flow mechanics, correlation breaks → **HENRY action, LIQUID backup** (unchanged from pre-split).

**Boundary rule (from VIOLET's SIGNAL_INTAKE.md, 2026-06-10 rebuild):** dealer-gamma *mechanics* are HENRY's; the gamma *flip event itself* + regime implication is VIOLET-relevant — on a confirmed dealer-gamma FLIP event, add VIOLET to the info line of the HENRY-routed signal. Conversely, HENRY stays on the info line of all VIOLET-routed vol-regime signals (backup-promotion stays a single-field swap per Backup column semantics).

**Why:** the bundled row predated the vol-ownership split (auto-memory `feedback_henry_vol_broadcast_to_violet` — VIOLET owns vol-regime broadcast; HENRY keeps gamma/0DTE/put-wall) and routed nothing to VIOLET. VIOLET's domain depth (KB episode database, L1 base-rate table, regime classifier) makes her the natural action recipient for regime-level vol signals.

**How to apply at intake:** ask "is this signal about the *state/structure of volatility* or about *index-level flow mechanics*?" Vol-state/structure → VIOLET. Flow mechanics/index moves → HENRY. If a signal genuinely carries both (e.g., a vol spike WITH a gamma-flip report), route VIOLET action + HENRY info with the flip named in dispatch_note, since regime implication dominates for network consumption.

**Filed:** Jun 10 2026. Proposed by VIOLET (SIGNAL_INTAKE.md rebuild Appendix A, relayed per spec-change rule); Will approved same day.

### Meta rows (not content domains — signal_type axis)

| Row | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-----|--------|--------|-----------------|-------------------|---------------|
| **Thesis Confirmation** (signal_type: thesis-confirmation) | RED | — | THESIS_CORE | PRIORITY | ADVERSARIAL |
| **Counter-Evidence** (signal_type: counter-evidence) | RED | — | — | PRIORITY | ADVERSARIAL |
| **Position-Specific Risk** (signal_type: position-risk) | Will (via Telegram) | — | Relevant agent | FLASH or IMMEDIATE | — |
| **Broad Market Stress** (safety-net trigger, multi-domain) | LIQUID | HENRY | FULL_NETWORK | IMMEDIATE | FULL_NETWORK |

### Backup column semantics

Backup is the second-choice Action recipient if the primary is overloaded, dormant, or unavailable. WALTER uses the backup when:
- Primary's STATUS.md is stale by >5 days
- Primary is explicitly flagged in MINIMIZE mode
- Primary's last-seen session was spawning sub-agents (deep research mode, should not be interrupted)
- Will explicitly overrides

Backup recipients should already be in the Info list for the same row, so promoting to Action is a single-field swap, not a full re-route.

---

## By Signal Type

| Signal Type | Default Precedence | Upgrade Condition |
|-------------|-------------------|-------------------|
| `threshold-crossed` | IMMEDIATE | → FLASH if position directly affected |
| `pattern-match` | PRIORITY | → IMMEDIATE if convergence (2+ agents flagging same theme) |
| `thesis-frame` | PRIORITY | Stays PRIORITY. Can upgrade to IMMEDIATE only if the synthesis/framework directly changes position sizing or catalyst read (rare — most thesis-frame content is analytical context, not threshold breach). |
| `catalyst` | IMMEDIATE | → FLASH if pre-written framework exists and threshold met |
| `divergence` | IMMEDIATE | Always IMMEDIATE minimum |
| `research` | PRIORITY | Stays PRIORITY unless thesis-critical finding |
| `position-risk` | IMMEDIATE | → FLASH if stop-loss or margin proximity |
| `context` | ROUTINE | Stays ROUTINE unless safety net triggers |
| `manual-flag` | PRIORITY | Follows Will's specified urgency if given |

---

## By Tag/By Verdict (NEW v0.7)

Augments the By Signal Domain and By Signal Type tables. Applies AFTER domain + signal_type routing has been determined. Adds RED to the info line when specific tag/verdict conditions fire — adversarial overlay needs visibility into bifurcation-state and corrected-framing dispatches without requiring separate signals. Falsification-trigger rule additionally turns WALTER into an auto-dispatcher when pre-registered RED thresholds cross.

| Tag/Verdict | Rule | De-dupe behavior |
|-------------|------|------------------|
| `signal_role: cluster_mediating` (v0.8 canonical) OR legacy `cluster_mediating: true` boolean | Add RED to info line unconditionally regardless of domain | If RED already in to/info, no add; stays at one occurrence |
| `verify_research_verdict: CORRECTED-FRAMING` (in dispatch_note) | Add RED to info line | If RED already in to/info, no add; stays at one occurrence |
| `falsification_trigger: <RED-FT-NN>` (auto-fired by WALTER from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` per JOINT_PROPOSAL §2 eval logic) | Action = trigger.recipient_chain.action; Info = trigger.recipient_chain.info; precedence per trigger.action enum mapping (IMMEDIATE-FALSIFY/PATH-B-CONFIRM/ADD-POSITION/etc.) | n/a — auto-generated signal, recipient chain pre-determined per FALSIFICATION_TRIGGERS row |

**De-dupe rule (general):** when multiple v0.7 rules fire on the same dispatch (e.g., signal is both `cluster_mediating: true` AND CORRECTED-FRAMING), RED is added once. Composition is informative-only; consumption mode (full-read for cluster_mediating vs body-skim for CORRECTED-FRAMING per RED CLAUDE.md boot-step 1.5 b3/b4) is RED's choice at boot.

### Interim period (pre-v0.8)

`cluster_mediating: true` is a v0.8 field (pending Will sign-off on JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a). Until v0.8 lands, the prose-tagged equivalent is dispatch_note language carrying "paper-vs-structural" / "tape-vs-substance" / "bifurcation" / "divergence" tokens. Interim WALTER discipline:

> When dispatch_note contains paper-vs-structural / tape-vs-substance / bifurcation / divergence framing, ensure RED in info line.

This carries the v0.7 rule operationally before the field formally exists. RED's bifurcation classification TSV (LIAISON Turn 5 deliverable, `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv`) seeds the historical pass; new prose-tagged signals from this point forward apply the rule.

### Composition example

SIG-W-20260505-012 (Brent intraday tape divergence vs Iran cluster confluence) — cluster_mediating + (would have been) CORRECTED-FRAMING if verdict run. Under v0.7 rules: RED auto-cc once; dispatch_note flags both rule-fires explicitly so RED knows the routing rationale; consumption mode = full-read (cluster_mediating dominates over body-skim).

### Why this is here, not in FORMAT_SPEC

`cluster_mediating` is a FORMAT_SPEC field; CORRECTED-FRAMING is a CHECKLIST verdict; falsification_trigger is a generated body field. The recipient-augmentation behavior is a routing decision — it belongs in this table per the canonical-source lookup in `WALTER/CLAUDE.md` ("Domain → recipient routing rules" → ROUTING_TABLE owns).

---

## By Boundary Threshold (NEW v0.8)

Augments the By Signal Domain table with explicit threshold-cross dispatch rows for BRENT's 8-row IMMEDIATE list per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c (BRENT+CARL+WALTER 3-way cosigned 2026-05-05/06; Will sign-off 2026-05-08). Threshold-cross signals carry `signal_type: threshold-crossed` + boundary-row reference in dispatch_note (e.g., `boundary: §2c-row-1`).

Distinct from the boundary-trigger CARL-side rule under "Iran-cluster CARL-info override" (Brent ≤$95×5sess and ≥$115×5sess fire IMMEDIATE → CARL): THIS section codifies the BRENT-action 8-row list at finer thresholds with broader cross-recipient routing.

| # | Threshold | Precedence | Action → Info | Cadence |
|---|-----------|------------|---------------|---------|
| 1 | **Brent close ≥ $120 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, SAM, HAWK, RED | 2-3 sess sustained = dispatch |
| 2 | **Brent close ≤ $75 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, RED | 2-3 sess sustained = dispatch |
| 3 | **Cushing < 20M bbl single print** | IMMEDIATE | BRENT → LIQUID, HENRY, RED | Single print = dispatch (operational minimum, WTI dislocation risk) |
| 4 | **HY Energy OAS > 400bps** | IMMEDIATE | BRENT → LIQUID-cross-feed (LIQUID may want primary depending on broader-credit context — flag at dispatch) | 2-3 sess sustained = dispatch |
| 5 | **VLCC Worldscale ≥ 2× trailing 30-day median sustained** | PRIORITY | BRENT → HAWK, SAM, RED | Sustained-cross-from-baseline (≥3 sess) — operational definition avoids absolute-threshold drift in war-risk-elevated baseline |
| 6 | **Gasoline crack — re-cross from <$30 back ≥$30 OR single-day spike ≥$50** | IMMEDIATE | BRENT → CARL, HENRY, RED | Threshold-cross logic only; standing $42 baseline = no fresh dispatch. Inverse extremum captures demand-destruction-via-crack-collapse OR refinery-substitution-exhausted scenarios |
| 7 | **US oil rigs +50 from 408 trough** | PRIORITY | BRENT → CARL (capex/wage), HENRY, RED | 2-3 sess sustained = dispatch |
| 8 | **Brent 3:2:1 crack > $50/bbl** | IMMEDIATE | BRENT → CARL (refining-margin pass-through), HENRY, REGINALD (refinery-bank) | 2-3 sess sustained = dispatch |

### Cadence convention (locked)

- **Single-day breach** = watch (no dispatch)
- **2-3 sessions sustained** = dispatch
- **Single-print operational minima** (#3 Cushing): dispatch on the print itself
- **Re-fire convention:** after initial cross, no re-fire on continued state; only on re-cross of boundary in either direction. Sustained-above-#1 stays one signal until it falls back below or escalates further to a higher threshold.

### Detection responsibility

- **WALTER:** monitors price/spread/inventory data via FORGE/tools/market-data + EIA/Baker Hughes scheduled scans (per JOINT_PROPOSAL §2b — Phase 2 dependency, calendars not yet landed at v0.8 ship)
- **BRENT:** mirrors via own data tools and STATUS refresh (BRENT self-task: PREDICTIONS.tsv BRT-04/BRT-08/BRT-15 cross-refs to these row numbers)
- **Convention:** BRENT-fire-as-primary on threshold-cross dispatches; WALTER-fire-as-fallback if BRENT stale (>5d STATUS lag)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — a threshold-crossed signal with `signal_role: cluster_mediating` AND CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence.
- Safety Net Auto-Upgrades below still apply — VIX>30 or HY OAS +25bps single session can override boundary-threshold precedence to FLASH.

### Q-trail

BRENT LIAISON Q4 (BRENT→WALTER, Turn 1, 8-row list proposed) → WALTER Turn 2 ACCEPT-WITH-REDLINES (#5 PRIORITY-not-IMMEDIATE; #6 standing-state-not-fresh-dispatch) → BRENT Turn 3 ACCEPT (with #5 ≥2× median definition + #6 dual-extremum >$50 inverse trigger) → WALTER Turn 4 LOCK → Will sign-off 2026-05-08.

---

## By Convergence (NEW v0.9)

Augments By Signal Domain + By Signal Type + By Tag/By Verdict + By Boundary Threshold sections. Applies AT DISPATCH after all other routing decisions. **Trigger:** when BOARD INDEX scan (cluster sections preferred for speed) finds N≥2 prior signals within 5-session window referencing the same bank ticker OR the same multi-channel exposure pattern, auto-fire `signal_type: convergence_event` precedence IMMEDIATE override.

### Rule

| Detection condition | Action | Recipient chain |
|---------------------|--------|-----------------|
| N≥2 prior BOARD signals within 5-session window mention same bank ticker (from `design/CROSS_REFS/REGINALD.md` §1 watchlist: TIER-1 / TIER-2 / NEW-TRACKING / EXTERNAL-WATCH tiers) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** |
| N≥2 prior BOARD signals within 5-session window touch same cross-bank pattern key (from `design/CROSS_REFS/REGINALD.md` §5: `cohort_fade_pattern` / `fhlb_bifurcation` / `provisions_mask_deterioration` / `office_single_point_concentration` / `hidden_cre_relabeling_trajectory` / `mi3_rcon2746_screen` / `ndfi_breakout_decomposition`) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** (cohort-level convergence is RED-watchable as a structural-bifurcation candidate) |

### Detection mechanics

- **At dispatch:** scan BOARD INDEX cluster sections (filtered to BANK_COLLATERAL + PC_STRESS + FED_FRAMEWORK + CONSUMER_STAGFLATION primary; expand secondary on bank-ticker hit) for prior 5-session window
- **Lookup:** use CROSS_REFS/REGINALD.md §1 ticker → watchlist row mapping + §5 pattern key list (denormalized cache, grep-speed at dispatch)
- **Cost:** cluster-filtered grep ~50-200ms per dispatch
- **Volume estimate:** ~1-2 convergence_events per week at current dispatch volume; peaks during Q1 earnings windows + threshold-cross windows

### dispatch_note format

When convergence_event fires, include in dispatch_note:

- **Prior signals (count + IDs + cluster + date):** e.g., `Convergence: SIG-W-20260420-008 (BANK_COLLATERAL, 4/20) + SIG-W-20260424-005 (BANK_COLLATERAL, 4/24) + SIG-W-20260426-009 (BANK_COLLATERAL, 4/26) — 3 signals in 6 sessions on office-distress + WAL/MTB ticker overlap`
- **Convergence type:** ticker-convergence vs pattern-key-convergence (or both)
- **Channel codes touched** (from REGINALD's 8-channel framework): e.g., `Channels: cre,hidden_cre,cmbs_maturity`
- **Cluster-mediating tag:** if convergence spans multiple clusters, set `cluster_mediating: true` + tag `cluster_secondary` per FORMAT_SPEC v0.7+

### De-dupe behavior

- If `cluster_mediating: true` already fires on the trigger signal (per v0.7 By Tag/By Verdict), convergence_event composition adds RED **once** (no double-count of RED-info)
- If multiple convergence_event triggers fire on same dispatch (e.g., signal hits both ticker-convergence AND pattern-key-convergence), single convergence_event dispatched with both reasons listed in dispatch_note
- If incoming signal IS the 2nd-or-later signal that COMPLETES a convergence window, dispatch fires from incoming-signal-dispatch side; prior signals stay at their original precedence (not retroactively re-dispatched)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — convergence_event signal with `signal_role: cluster_mediating` + CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence
- v0.8 By Boundary Threshold still applies — if convergence_event also crosses a BRENT-IMMEDIATE row (e.g., Brent ≥$120 sustained 3 sessions), BRENT row recipient chain composes with REGINALD primary; precedence stays IMMEDIATE (highest)
- Safety Net Auto-Upgrades still apply — VIX>30 or HY OAS +25bps single session can compose with convergence_event (precedence already IMMEDIATE; multi-trigger composition surfaces in dispatch_note)

### Examples (illustrative — not historical dispatch)

**Ticker convergence example:** signal SIG-W-20260512-NNN mentions WAL. WALTER greps BOARD INDEX for prior 5-session window — finds SIG-W-20260507-004 (Sternlicht-Starwood CMBS) mentions WAL + SIG-W-20260508-011 (FWRD covenant default) mentions WAL bank-covenant pattern. N=3 within 5 sessions → convergence_event fires; recipient chain REGINALD action / BRENT info / RED info. dispatch_note: `Convergence (ticker): SIG-W-20260507-004 + SIG-W-20260508-011 + (current) — 3 signals in 5 sessions on WAL; channels: cre,cmbs_maturity,private_credit`.

**Pattern-key convergence example:** signals across 4 sessions all touch `cohort_fade_pattern` (REGINALD's structural framework) — VLY provisions tell + CFG cohort-fade signal + WAL ex-fraud NCO read. Even though no single ticker repeats N≥2, pattern-key fires same convergence_event mechanics. RED-info important here because cohort-level convergence is bifurcation candidate.

### Q-trail

REGINALD LIAISON Q5 (REGINALD → WALTER, Turn 1, framework proposed) → WALTER Turn 2 DECISION (YES, build atop named-entity grep from Q3) → REGINALD Turn 3 LOCK (preference: ROUTING_TABLE v0.9 section, not standalone) → WALTER Turn 4 SHIP (this section).

---

## Safety Net Auto-Upgrades

These conditions override the routing table and force minimum IMMEDIATE precedence:

| Trigger | Detection Method | Upgrade To |
|---------|-----------------|------------|
| VIX > 30 (or +5 intraday) | Market data check | IMMEDIATE minimum |
| HY OAS widening > 25bps single session | Market data check | IMMEDIATE minimum |
| Held-position liquidity drop | Bid-ask spread monitoring | FLASH |
| 2+ agents flag same theme in 24h | Signal correlation | IMMEDIATE + flag convergence |
| Correlation break (r drops >0.3 in correlated pair) | Statistical check | IMMEDIATE minimum |

---

## Escalation Paths

Receiving agents can request WALTER re-route at higher precedence:

| Scenario | Agent Action | WALTER Response |
|----------|-------------|-----------------|
| Agent finds signal more urgent than classified | Writes to WALTER outbox: "ESCALATE SIG-W-YYYYMMDD-NNN to IMMEDIATE" | WALTER re-routes to broader group at higher precedence |
| Agent identifies cross-domain relevance | Writes to WALTER outbox: "ROUTE SIG-W-YYYYMMDD-NNN to AGENT (ACTION)" | WALTER sends copy to new recipient |
| Agent flags false positive | Writes to WALTER outbox: "REJECT SIG-W-YYYYMMDD-NNN — reason" | WALTER logs rejection, stops further routing |

---

## MINIMIZE Routing Adjustments

During MINIMIZE, routing table precedence thresholds shift:

| MINIMIZE Level | ROUTINE Signals | PRIORITY Signals | IMMEDIATE Signals | FLASH Signals |
|---------------|-----------------|------------------|-------------------|---------------|
| **Normal** | Route normally | Route normally | Route normally | Route normally |
| **MINIMIZE-1** | Queue in WALTER | Route normally | Route normally | Route normally |
| **MINIMIZE-2** | Queue in WALTER | Queue in WALTER | Route normally | Route normally |
| **MINIMIZE-3** | Queue in WALTER | Queue in WALTER | Queue in WALTER | Route normally |

---

*v0.10 — Jun 10, 2026 (MARKET_VOL row split into vol-regime → VIOLET action / index-mechanics → HENRY action per HENRY/VIOLET vol-ownership decision; gamma-flip-event VIOLET-info boundary rule; single domain code retained; proposed by VIOLET SIGNAL_INTAKE Appendix A flag, Will approved 2026-06-10) | v0.9 — May 11, 2026 (By Convergence section added after By Boundary Threshold per REGINALD ↔ WALTER LIAISON Q5 — auto-fire convergence_event IMMEDIATE to REGINALD action + RED info on N≥2 prior signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern; detection via CROSS_REFS/REGINALD.md §1 watchlist + §5 pattern keys; dispatch_note format + de-dupe behavior + composition with other rules locked; bank_transmission enum 8-val pre-cosigned in V0_9_STACK.md tracker for batched FORMAT_SPEC v0.9 ship; REG LIAISON Q5 LOCK Turn 4 2026-05-11) | v0.8 — May 8, 2026 (By Boundary Threshold section added after By Tag/By Verdict per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c — 8-row BRENT-IMMEDIATE threshold-cross dispatch list; cadence convention locked single-day=watch / 2-3 sess sustained=dispatch / single-print operational minima dispatch on print / re-fire only on boundary re-cross; BRENT-fire-as-primary, WALTER-fire-as-fallback if BRENT stale >5d; By Tag/By Verdict cluster_mediating row updated to reference v0.8 canonical `signal_role: cluster_mediating` form retiring v0.7 prose-tag interim discipline; Will sign-off 2026-05-08) | v0.7 — May 6, 2026 PM (By Tag/By Verdict section added after By Signal Type per RED ↔ WALTER LIAISON Q9-Q12 + JOINT_PROPOSAL_2026-05-06_red_walter §3 — three rules: cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`; de-dupe rule + interim prose-tag discipline pre-v0.8; Will sign-off 2026-05-06) | v0.6 — May 6, 2026 (Iran-cluster CARL-info override section added per CARL ↔ WALTER LIAISON Q3 — concrete Brent thresholds replace heuristic "near $110" framing; boundary-trigger threshold-cross dispatch sub-rule added for CARL-side ≤$95/5sess and ≥$115/5sess crosses; BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred pending Will sign-off on JOINT_PROPOSAL §2c) | v0.5 — April 20, 2026 (thesis-frame signal_type row added per FORMAT_SPEC v0.5; Residential-housing stress exception section added per Filter v2 Segment A — geo-narrow residential → REGINALD action not CARL) | v0.4 — April 14, 2026 (ASIA_CONTAGION + UST_FOREIGN rows added per FORMAT_SPEC v0.4) | v0.3 — April 11, 2026 PM (canonical domain codes applied, Gap C resolved) | v0.2 — April 11, 2026 AM (rows + backup column) | v0.1 — April 7, 2026*
