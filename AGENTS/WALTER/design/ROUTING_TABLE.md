# WALTER Routing Table v0.3

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.

**Version history:**
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

*v0.3 — April 11, 2026 PM (canonical domain codes applied, Gap C resolved) | v0.2 — April 11, 2026 AM (rows + backup column) | v0.1 — April 7, 2026*
