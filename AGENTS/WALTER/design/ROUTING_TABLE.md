# WALTER Routing Table v0.6

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.

**Version history:**
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
| `MARKET_VOL` | VIX, index moves, vol regime, dealer gamma, correlation breaks | HENRY | LIQUID | LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
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

*v0.6 — May 6, 2026 (Iran-cluster CARL-info override section added per CARL ↔ WALTER LIAISON Q3 — concrete Brent thresholds replace heuristic "near $110" framing; boundary-trigger threshold-cross dispatch sub-rule added for CARL-side ≤$95/5sess and ≥$115/5sess crosses; BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred pending Will sign-off on JOINT_PROPOSAL §2c) | v0.5 — April 20, 2026 (thesis-frame signal_type row added per FORMAT_SPEC v0.5; Residential-housing stress exception section added per Filter v2 Segment A — geo-narrow residential → REGINALD action not CARL) | v0.4 — April 14, 2026 (ASIA_CONTAGION + UST_FOREIGN rows added per FORMAT_SPEC v0.4) | v0.3 — April 11, 2026 PM (canonical domain codes applied, Gap C resolved) | v0.2 — April 11, 2026 AM (rows + backup column) | v0.1 — April 7, 2026*
