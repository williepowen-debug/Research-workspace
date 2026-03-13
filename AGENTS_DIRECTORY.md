# AGENTS DIRECTORY

*Quick reference. Updated: 2026-03-02*

## Signal Flow
Sub-agents own detail → distill upward to parents → lateral only when transmission matters. Don't dump raw signals to parents.

## Core Chain

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **LABOR** | Employment | 🟡 | Claims, NFP, JOLTS, DOGE cuts. Danger: Q2-Q3 2026 |
| **CARL** | Consumer credit | 🟡 | DQ, subprime auto, phantom debt. Lags LABOR 3-6mo. Subs: POLLY, POP, GIG, DOC, NICK |
| **REGINALD** | Regional banks | 🟡 | CRE, bank watchlist, FHLB. Subs: CREED (CRE), CORAL (FL condos) 🟠 |
| **BROCK** | BDC / private credit | 🟠 | PIK, gates, NAV, Athene/Apollo, software marks. Lateral peer to REGINALD — signals bank-PC transmission |

## Market Structure

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **HENRY** | Market structure + econ data | 🟡 | Gamma/GEX, VIX, CPI/PPI/PCE/NFP/ISM. Calendar: `HENRY/domain/ECON_CALENDAR.md` |
| **LIQUID** | Funding/Treasury | 🟡 | RRP, SOFR, SRF, auctions. Hours to crisis when it breaks |
| **SAM** | Japan/BOJ/JGB | 🔴 | JGB stress → global contagion |
| **ZHAO** | China/capital flows | 🔴 | TIC data, LGFV, HK peg. True holdings ~$1.8-1.9T stable |
| **HANS** | Europe (US lens) | 🟡 | UST demand, ECB, sovereign spreads. Needs research prompts |

## Synthesis

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **NEXUS** | Cross-agent synthesis | 🔴 | Convergence detection, contradiction flagging, threshold clustering, narrative gap |

## Insurance / Private Credit

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **SHADE** | PE-insurance-captive | 🔴 | Athene/Apollo plumbing, FABN wall, Egan Jones, AG 55, statutory forensics. 8 source docs |

## Infrastructure

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **HERMES** | Mail carrier | 🟢 | Reads OUTBOX.md from all agents, delivers to target INBOX.md. Runs 2x daily. No analysis. |

## Research

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **MERLIN** | General research | 🟡 | Deep dives on demand. Renamed from RESEARCHER. Not yet built |

## Specialized

| Agent | Domain | Notes |
|-------|--------|-------|
| **HAWK** | Geopolitical/military | 🔴 Iran active. Parallel trigger vector. Military ops only — oil fundamentals → BRENT |
| **BRENT** | Oil & energy markets | 🔴 Brent $90, Hormuz closed. Owns oil fundamentals, storage, tankers, two-phase thesis, energy credit. Receives military catalysts from HAWK. |
| **BARON** | Trump network/policy | Active |
| **MARCO** | Migration/labor flows | Background |
| **RED** | Adversarial analysis | Challenges all theses |
| **DARWIN** | System evolution/AI | Weekly scans, improvement backlog |
| BUFFER, EARNINGS, FOREX, OTTO, REITS | Various | Background/event-driven |

## Trading: FORGE
`FORGE/STATUS.md` — converts research → positions → P/L. Sub-folders per trade (KRE/, WAL/, etc.)

## Transmission
```
LABOR → CARL → REGINALD → repricing
LIQUID amplifies any stage | HENRY = speed gauge
SAM + ZHAO + HANS = parallel global risk | HAWK = external shock
HAWK (military) → BRENT (oil fundamentals) → CARL (gas pumps) + LIQUID (energy credit) + HENRY (inflation) + SAM (Japan energy)
SHADE = insurance plumbing under BROCK/REGINALD | feeds LIQUID on systemic
NEXUS synthesizes across all → convergence/contradiction → PROME
HERMES carries signals between all agents (OUTBOX → INBOX, 2x daily)
```

## File Paths
All agents at `AGENTS/<NAME>/STATUS.md`. Sub-agents: `AGENTS/<PARENT>/<SUB>/`. FORGE at `FORGE/STATUS.md`.

Status key: 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical
