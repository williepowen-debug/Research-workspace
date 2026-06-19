# REGINALD Sub-Agent Coordination

## Overview

REGINALD is the convergence point for regional bank stress. Five sub-agents maintain domain expertise. REGINALD coordinates, synthesizes, and escalates.

---

## Sub-Agent Directory

| Agent | Domain | Key Data | Location |
|-------|--------|----------|----------|
| **CREED** | CRE / CMBS | Delinquency, maturity wall, loss severity | `sub-agents/CREED/` |
| **BROCK** | BDC / Private Credit | PIK rates, cash coverage, dividend health | `AGENTS/BROCK/` (**top-level agent**, not sub-agent) |
| **CORAL** ⬆️ | Florida CRE / Condo Crisis | Migration, HOA/SIRS, Citizens insurance, SSB/VLY FL exposure | `AGENTS/CORAL/` (**promoted to top-level peer agent 2026-06-19** — coordinate via inbox/outbox, no longer a sub-agent) |
| **RENO** | Nevada Geographic Stress | Gaming/tourism, housing, water crisis, WAL NV exposure | `sub-agents/RENO/` |
| **TEX** | Texas/Florida Regional | Geographic concentration, HOA, housing | `sub-agents/TEX/` |
| **BELT** | Mortgage DQ Belt (MS/LA/MD) | State-level mortgage delinquency hotspots | `sub-agents/BELT/` |

---

## Data Ownership

### CREED (CRE Expert)
**Maintains:**
- `sources/CMBS_DELINQUENCY.md` — CMBS delinquency by property type
- `sources/CRE_MATURITY.md` — Maturity wall data
- `workbook/` — CRE-specific ML/FL/VX

**Key vectors for REGINALD:**
- Office CMBS DQ (currently 12.34% ATH)
- Loss severity gap (70-97% actual vs 20-40% modeled)
- Modification exhaustion rate

**Sync to REGINALD:** VX-REG-3.01, VX-REG-9.01-9.03, VX-REG-13.01-13.02

### BROCK (BDC Expert)
**Maintains:**
- `workbook/BDC_CASH_COVERAGE.tsv` — Cash NII vs dividend tracking
- `workbook/` — BDC-specific ML/FL/VX

**Key vectors for REGINALD:**
- BDC NAV discounts (PSEC -57%, FSK -34%)
- PIK interest inflation (Golub 173% spike)
- Dividend coverage ratios

**Sync to REGINALD:** VX-REG-2.03, VX-REG-9.04, VX-REG-12.01

### CORAL (Florida CRE — Condo Crisis, HOA, Citizens Insurance) — ⬆️ PROMOTED TO PEER AGENT 2026-06-19
*Now a top-level peer agent at `AGENTS/CORAL/` (not a sub-agent). REGINALD coordinates with it via inbox/outbox + read-only cross-reads, same as BROCK/OZK. The ownership notes below remain accurate for what CORAL covers; the vectors it syncs to REGINALD are unchanged.*

**Maintains:**
- FL condo receivership / SIRS mandate tracking
- HOA special assessment monitoring
- Citizens Property Insurance stress mapping
- SSB/VLY FL exposure analysis

**Key vectors for REGINALD:**
- FL migration collapse (-93%)
- HOA super-lien cascade (SB 4-D)
- Citizens $678B assessment capacity

**Sync to REGINALD:** VX-REG-8.01, VX-REG-15.03, VX-REG-19.02, FLOW-REG-6.01, FLOW-REG-20.01

### RENO (Nevada Geographic Focus)
**Maintains:**
- Nevada gaming/tourism stress tracking
- NV housing market analysis
- Water crisis monitoring
- WAL Nevada exposure mapping

**Key vectors for REGINALD:**
- Gaming/tourism revenue trends
- NV housing velocity
- WAL NV CRE concentration

**Sync to REGINALD:** VX-REG-6.04 (WAL NV), VX-REG-8.01 (NV HOA)

### TEX (Geographic Expert)
**Maintains:**
- Texas/Florida market data
- HOA/insurance crisis tracking
- Housing velocity data

**Key vectors for REGINALD:**
- HOA special assessments (FL SB 4-D)
- Housing days-on-market

**Sync to REGINALD:** VX-REG-8.01, ML-REG-054

---

## Coordination Protocol

### Daily (Heartbeat)
- Check sub-agent STATUS.md headers for status changes
- Flag any GREEN→YELLOW or worse transitions
- No spawn needed — read STATUS files directly

### Weekly (Sync)
- Pull updated vectors from sub-agents
- Update REGINALD VX.tsv with fresh data
- Log any threshold breaches to ML.tsv

### On Catalyst (Spawn)
- Spawn sub-agent for deep research
- Example: `sessions_spawn(agentId="creed", task="Update CMBS delinquency data for Q4 2025")`
- Sub-agent updates its workbook, REGINALD pulls summary

### Escalation
- Sub-agent detects threshold breach → Updates STATUS.md
- REGINALD reads breach in next heartbeat
- REGINALD alerts Will if material

---

## Last Sync Tracker

| Agent | Last Sync | Key Update |
|-------|-----------|------------|
| CREED | 2026-02-13 | Office CMBS 12.34% ATH |
| BROCK | 2026-02-14 | PSEC earnings Feb 20, FSK Feb 25 |
| CORAL | 2026-02-11 | CLO spreads stable at 115bps |
| RENO | 2026-02-12 | Bellwether prices updated |
| TEX | 2026-02-12 | FL/TX housing velocity collapse |

---

## Cross-Domain Flows

These flows require coordination across multiple sub-agents:

| Flow | Agents | Pathway |
|------|--------|---------|
| FLOW-REG-1.01 | CORAL → BROCK → RENO | CLO stress → BDC losses → Bank liquidity |
| FLOW-REG-3.01 | RENO → ALL | FHLB contagion spreads to all |
| FLOW-REG-7.01 | CREED → RENO | CRE mods exhaust → Bank recognition |
| FLOW-REG-9.01 | BROCK → RENO | BDC PIK → Bank line draws |

---

## Spawning Sub-Agents

```
# Deep dive on CRE
sessions_spawn(agentId="creed", task="...", cleanup="keep")

# BDC earnings analysis
sessions_spawn(agentId="brock", task="...", cleanup="keep")

# Check status
sessions_list(kinds=["agent"])

# Send follow-up
sessions_send(sessionKey="agent:creed:subagent:...", message="...")
```

---

*Last updated: 2026-02-16*
