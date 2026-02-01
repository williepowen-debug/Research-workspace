# REGINALD METHODOLOGY NOTES

**Purpose:** Documents how REGINALD agent operates within the SAM Network methodology framework.

**Created:** 2026-01-25
**Base Methodology:** CARL_METHODOLOGY_SKELETON_v0.2.md

---

## Overview

REGINALD monitors regional bank/credit stress with characteristics:

| Characteristic | REGINALD Approach |
|----------------|-------------------|
| **Data cadence** | Mixed: Daily (KRE, CLO proxies) + Quarterly (Call Reports) |
| **Crisis speed** | Days (CLO transmission) to Quarters (CRE deterioration) |
| **Actor count** | Many regional banks, but focus on sector-wide indicators |
| **Thesis structure** | Single primary thesis with multiple transmission paths |
| **Coordination** | Peer agents (SAM, LIQUID) |

---

## 1. Session Types

| Session Type | Context | Monitoring Cadence |
|--------------|---------|-------------------|
| **Update** | Normal operations | Weekly |
| **Analysis** | Deep dive on specific bank/exposure | As needed |
| **Crisis** | Active bank stress | HOURLY |
| **Reconciliation** | Cross-reference audit | Monthly |
| **Handoff** | Session transfer | End of session |

### Crisis Session Protocol

1. Check all RED/ORANGE thresholds against current values
2. Monitor KRE intraday if bank stress emerging
3. Check CLO spread levels (coordinate with SAM)
4. Evaluate deposit flow signals
5. Alert LIQUID if FHLB stress emerging

---

## 2. Multi-Agent Coordination

REGINALD operates in a **peer coordination model**:

| Agent | Relationship | Data Flow |
|-------|--------------|-----------|
| **SAM** | Peer | SAM → CLO spreads; REGINALD → Bank stress confirmation |
| **LIQUID** | Peer | LIQUID → Funding stress; REGINALD → FHLB demand signals |
| **MASTER** | Coordinator | REGINALD reports bank sector status |

### State Vector Exchange Format

REGINALD sends to SAM:
```yaml
state_vector:
  from_agent: "REGINALD"
  to_agent: "SAM"
  domain: "Regional Banks"
  key_metric: "KRE sector health"
  status: "YELLOW"
  interpretation: "Sector down 8% from peak, approaching -10% Yellow"
  recommended_action: "Monitor for CLO transmission confirmation"
```

SAM sends to REGINALD:
```yaml
state_vector:
  from_agent: "SAM"
  to_agent: "REGINALD"
  domain: "CLO Nuclear"
  key_metric: "CLO AAA spreads"
  status: "GREEN"
  interpretation: "CLO at 125bps, 25bps cushion to Yellow"
  recommended_action: "Continue monitoring; Norinchukin stabilizing"
```

---

## 3. Inbox Check Protocol

**Step 0 of every session:**

1. Read `C:/Projects/AGENT_COMMS/REGINALD_INBOX/`
2. Process by priority:
   - **URGENT:** Handle immediately (CLO breach, deposit run signals)
   - **ELEVATED:** Incorporate into session focus
   - **ROUTINE:** Note for later

3. Acknowledge receipt if response required

---

## 4. Signal Triggers (Outbound)

### To SAM

| Trigger | Priority | Context |
|---------|----------|---------|
| KRE -15% | ELEVATED | Sector stress confirmation |
| CLO AAA >150bps confirmed | URGENT | Transmission verified |
| Bank failure | URGENT | Systemic signal |

### To LIQUID

| Trigger | Priority | Context |
|---------|----------|---------|
| Deposit flight >4% | URGENT | Funding stress emerging |
| FHLB advance surge | URGENT | Bank liquidity crisis |
| Regional bank stock -20% | ELEVATED | Individual bank run risk |

---

## 5. Data Quality Tags

| Tag | Meaning |
|-----|---------|
| REPORTED | Direct official source (FRED, Call Reports) |
| PROXY | Derived from correlated indicator (KRE for sector, CLOZ for CLO) |
| DELAYED | Accurate but lagged (Call Reports are 45-day lag) |
| TRANSLATED | Japanese source via AI (BOJ FSR) |
| TERMINAL | Requires Bloomberg (mark as GAP) |

---

## 6. Threshold Monitoring

### Color-Coded Escalation

| Color | Meaning | Action |
|-------|---------|--------|
| GREEN | Normal | Weekly monitoring |
| YELLOW | Watch | Daily monitoring, prepare contingencies |
| ORANGE | Alert | 24-hour watch, alert coordinating agents |
| RED | Critical | Continuous monitoring, crisis protocols |

---

## 7. Quarterly Data Workflow

Given Call Report lag (45 days after quarter-end):

| Quarter End | Data Available | Action |
|-------------|----------------|--------|
| Q4 (Dec 31) | Mid-February | Major review: deposit flows, CLO holdings |
| Q1 (Mar 31) | Mid-May | CRE delinquency update |
| Q2 (Jun 30) | Mid-August | Mid-year bank health assessment |
| Q3 (Sep 30) | Mid-November | Pre-year-end stress assessment |

---

*End of REGINALD Methodology Notes v1.0*
