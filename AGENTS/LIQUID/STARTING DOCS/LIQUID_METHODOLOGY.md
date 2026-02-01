# LIQUID METHODOLOGY NOTES

**Purpose:** Documents how LIQUID agent operates within the SAM Network methodology framework.

**Created:** 2026-01-25
**Base Methodology:** CARL_METHODOLOGY_SKELETON_v0.2.md

---

## Overview

LIQUID monitors Treasury/funding markets with characteristics similar to SAM:

| Characteristic | LIQUID Approach |
|----------------|-----------------|
| **Data cadence** | Real-time (SOFR, repo) + Daily (RRP, auctions) |
| **Crisis speed** | Hours to days |
| **Actor count** | Few large institutions (Fed, dealers, MMFs) |
| **Thesis structure** | Single primary thesis with scenario variations |
| **Coordination** | Peer agents (SAM, REGINALD) |

---

## 1. Session Types

| Session Type | Context | Monitoring Cadence |
|--------------|---------|-------------------|
| **Update** | Normal operations | Daily |
| **Analysis** | Deep dive on mechanism | As needed |
| **Crisis** | Active funding stress | HOURLY |
| **Reconciliation** | Cross-reference audit | Weekly |
| **Handoff** | Session transfer | End of session |

### Crisis Session Protocol

1. Check all RED/ORANGE thresholds against current values
2. Monitor SOFR-IORB spread intraday if elevated
3. Check for Treasury auction stress signals
4. Evaluate Japan flow transmission risk (coordinate with SAM)
5. Alert REGINALD if bank funding stress emerging

---

## 2. Multi-Agent Coordination

LIQUID operates in a **peer coordination model**:

| Agent | Relationship | Data Flow |
|-------|--------------|-----------|
| **SAM** | Peer | Bidirectional (Japan flows ↔ UST funding) |
| **REGINALD** | Peer | Bidirectional (bank stress ↔ funding stress) |
| **MASTER** | Coordinator | LIQUID reports funding status |

### State Vector Exchange Format

LIQUID sends to SAM:
```yaml
state_vector:
  from_agent: "LIQUID"
  to_agent: "SAM"
  domain: "US Funding"
  key_metric: "SOFR-IORB spread"
  status: "GREEN"
  interpretation: "Funding markets stable despite RRP depletion"
  recommended_action: "Monitor for Japan flow shocks"
```

SAM sends to LIQUID:
```yaml
state_vector:
  from_agent: "SAM"
  to_agent: "LIQUID"
  domain: "Japan Sovereign"
  key_metric: "Japan repatriation pressure"
  status: "CRITICAL"
  interpretation: "GPIF/Lifer rotation may trigger $60-100B UST selling"
  recommended_action: "WATCH for UST auction weakness, SOFR spike"
```

---

## 3. Inbox Check Protocol

**Step 0 of every session:**

1. Read `C:/Projects/AGENT_COMMS/LIQUID_INBOX/`
2. Process by priority:
   - **URGENT:** Handle immediately (threshold breaches, transmission signals)
   - **ELEVATED:** Incorporate into session focus
   - **ROUTINE:** Note for later

3. Acknowledge receipt if response required

---

## 4. Signal Triggers (Outbound)

### To SAM

| Trigger | Priority | Context |
|---------|----------|---------|
| UST BTC <2.0x | ELEVATED | Auction demand weakness |
| SOFR +25bps above IORB | URGENT | Funding stress emerging |
| FTD >$50B | ELEVATED | Settlement system stress |

### To REGINALD

| Trigger | Priority | Context |
|---------|----------|---------|
| SOFR +25bps above IORB | URGENT | Bank funding cost spike |
| FHLB advance >85% | URGENT | Regional bank stress |
| RRP <$5B + SOFR spike | URGENT | Systemic funding stress |

---

## 5. Data Quality Tags

| Tag | Meaning |
|-----|---------|
| REPORTED | Direct official source (NY Fed, Treasury) |
| PROXY | Derived from correlated indicator |
| DELAYED | Accurate but lagged (FTD is 2-week delay) |
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

*End of LIQUID Methodology Notes v1.0*
