# WALTER Routing Table v0.1

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

---

## By Signal Domain

| Domain | Action Recipient | Info Recipients | Default Precedence | Default Group |
|--------|-----------------|-----------------|-------------------|---------------|
| **Employment / Labor** | CARL | HENRY, RED | IMMEDIATE (data day) / PRIORITY (analysis) | LABOR_DOWNSTREAM |
| **Consumer Credit** | CARL | REGINALD, RED | PRIORITY | THESIS_CORE |
| **Bank Earnings / CRE** | REGINALD | BROCK, LIQUID, RED | IMMEDIATE (earnings) / PRIORITY (research) | CREDIT_CHAIN |
| **Funding / Liquidity** | LIQUID | BROCK, SHADE, HENRY | IMMEDIATE (stress) / PRIORITY (monitoring) | CREDIT_CHAIN |
| **Oil / Energy** | HAWK | BRENT, RED | PRIORITY | ENERGY_CHAIN |
| **Geopolitical Supply** | HAWK | BRENT, SAM | PRIORITY | ENERGY_CHAIN |
| **Japan / BOJ / Yen** | SAM | LIQUID, RED | IMMEDIATE (intervention) / PRIORITY (monitoring) | — |
| **Market Structure / Vol** | HENRY | LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| **Insurance / Shadow** | SHADE | LIQUID, BROCK | PRIORITY | — |
| **Thesis Confirmation** | RED | THESIS_CORE | PRIORITY | ADVERSARIAL |
| **Counter-Evidence** | RED | — | PRIORITY | ADVERSARIAL |
| **Position-Specific Risk** | Will (via Telegram) | Relevant agent | FLASH or IMMEDIATE | — |
| **Broad Market Stress** | LIQUID | FULL_NETWORK | IMMEDIATE | FULL_NETWORK |

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

*v0.1 — April 7, 2026*
