# AGENTS DIRECTORY

*Quick reference. Updated: 2026-06-21*

For a human-friendly grouped view of the flat `AGENTS/<NAME>/` tree, see [`AGENTS/_INDEX.md`](AGENTS/_INDEX.md). For the canonical topology/transmission map, see [`AGENTS/_NETWORK.md`](AGENTS/_NETWORK.md). Canonical paths remain flat to avoid breaking scripts, docs, and active Claude/OpenClaw workflows.

## Runtime Architecture

| Runtime | Agent(s) | Interface | Notes |
|---------|----------|-----------|-------|
| **OpenClaw (VPS)** | Prome + all spawn-based agents | Telegram | Orchestrator. Spawns sub-agents. Full workspace access. |
| **Claude Code** | REGINALD, CARL, OZK, CORAL, CREED, SAM, RED | Telegram | Independent sessions. Siloed to own domain folders. Push to shared repo. OZK spun out from REGINALD 2026-04-24; CORAL (Florida) spun out from REGINALD 2026-06-19; CREED (national CRE/CMBS) revived as top-level Claude Code roster agent 2026-06-21; RED is the persistent adversarial-analysis surface (not a market domain). |
| **Claude Code** | TERRY | Repo / Claude Code | Conversational trading-desk surface. Will can open Terry directly to talk through trade structure, sizing, options, exits, and postmortems. Proposes only; no execution. |
| **Claude Code** | PROME | Repo / Claude Code | Repo-native implementation surface for the same Prome identity. Uses shared Prome state, not a separate domain silo. Owns docs/tools/audits/handoffs when scoped. |

**Key rules for multi-runtime:**
- Prome does NOT spawn REGINALD, CARL, or CREED as sub-agents. They run independently; CREED requires explicit Will permission before any spawn-like work.
- Communication is via **inbox files** in the repo (`AGENTS/{NAME}/inbox/`), not session tools.
- Prome must **read before editing** any REGINALD/CARL/CREED file — they may be writing at any time.
- Their completions won't come through sub-agent channels. Check their files directly.
- **They are fully siloed** — can only see their own CLAUDE.md + domain folder. Cannot read HEARTBEAT.md, MEMORY.md, other agents' files, or cross-references. **Inbox signals must be self-contained** with all relevant context inline. No "see BRENT/research/..." links.
- **Claude Code Prome is different:** it is not a siloed market-domain agent and does not replace Telegram/OpenClaw Prome. It uses the shared `PROME/` state layer, leaves `PROME/CLAUDE_CODE_HANDOFF.md`, and does not own Will-facing approvals or final decision prompts.

## Signal Flow
Sub-agents own detail → distill upward to parents → lateral only when transmission matters. Don't dump raw signals to parents.

## Core Chain

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **LABOR** | Employment | 🟡 | Claims, NFP, JOLTS, DOGE cuts. Danger: Q2-Q3 2026 |
| **CARL** 🖥️ | Consumer credit | 🟡 | DQ, subprime auto, phantom debt. Lags LABOR 3-6mo. Subs: POLLY, POP, GIG, DOC, NICK. **Claude Code — independent, siloed.** |
| **REGINALD** 🖥️ | Regional banks | 🟡 | Bank watchlist, FHLB, NDFI/CRE bank transmission. Peers: BROCK, CORAL, CREED, OZK. Legacy CREED sub-agent tree remains source archive only. **Claude Code — independent, siloed.** |
| **BROCK** | BDC / private credit | 🟠 | PIK, gates, NAV, Athene/Apollo, software marks. Lateral peer to REGINALD — signals bank-PC transmission |
| **CORAL** 🖥️ | Florida (comprehensive) | 🟠 | **Whole-Florida agent — 10 pillars:** condo/SF/CRE real estate, insurance (Citizens), FL banks (SSB/SBCF/BKU/VLY/AMTB), migration, tourism/snowbird, state fiscal & property-tax, labor/construction, coastal/climate (hurricane/sargassum). Promoted from REGINALD sub-agent 2026-06-19; scope broadened to comprehensive FL 2026-06-19. Overlaps MARCO on migration/tourism by design. **Claude Code — independent, siloed.** |
| **CREED** 🖥️ | National CRE / CMBS | 🟡 | National CRE market-level stress, CMBS delinquency/special servicing, office/multifamily, maturity wall, mods/re-defaults, forced-sale/private-NAV risk. Feeds REGINALD/CORAL/LIQUID/CARL; does not own bank trades or Florida whole-state synthesis. Revived top-level 2026-06-21. **Claude Code roster — do not spawn without explicit Will permission.** |

## Market Structure

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **HENRY** | Market structure + econ data | 🟡 | Gamma/GEX, VIX, CPI/PPI/PCE/NFP/ISM. Calendar: `HENRY/domain/ECON_CALENDAR.md` |
| **LIQUID** | Funding/Treasury | 🟡 | RRP, SOFR, SRF, auctions. Hours to crisis when it breaks |
| **SAM** 🖥️ | Japan/BOJ/JGB | 🔴 | JGB stress → global contagion. **Claude Code — independent, siloed.** |
| **ZHAO** | China/capital flows | 🔴 | TIC data, LGFV, HK peg. True holdings ~$1.8-1.9T stable |
| **HANS** | Europe (US lens) | 🟡 | UST demand, ECB, sovereign spreads. Needs research prompts |
| **BOND** | US bond market structure | 🔴 | Auctions, dealer positioning, issuance (HY/IG), credit spreads, CDX-cash divergence, credit-equity lead. Between LIQUID (plumbing) and ZHAO (foreign flows). |

## Synthesis

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **NEXUS** | Cross-agent synthesis | 🔴 | Convergence detection, contradiction flagging, threshold clustering, narrative gap |
| **ORACLE** | Prediction markets | 🟠 | Polymarket/Kalshi monitoring. Real-money odds on bank failure, recession, bailout, Fed, geopolitical. Sentiment gauge + contrarian signal. |

## Insurance / Private Credit

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **SHADE** | PE-insurance-captive | 🔴 | Athene/Apollo plumbing, FABN wall, Egan Jones, AG 55, statutory forensics. 8 source docs |

## Infrastructure

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **HERMES** | Mail carrier | 🟢 | Reads OUTBOX.md from all agents, delivers to target INBOX.md. Runs 2x daily. No analysis. |

## Research & Learning

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **ATHENA** | Reading / knowledge | 🟢 | Reading companion + knowledge compounder. Currently: *Thinking in Systems* (Meadows). Cross-pollinates with agent network. |
| **DEWEY** | Deep research executor + data-pull script home | 🟡 | Revived 2026-06-20; formerly RESEARCHER. Cited `/deep-research` executor, WALTER handoff lane, first live run pending after CONTEXT refresh. |

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

## Trading

| Agent / Surface | Domain | Status | Key |
|---|---|---|---|
| **TERRY** 🖥️ | Trade construction / tactical execution discipline | 🟡 | Spawn-on-demand **and Claude Code conversational trading desk**. Will can talk through setups directly. Turns thesis into trade cards: entry, structure, sizing, invalidation, expiry/time stop, roll/no-roll rules, chart/tape read, postmortems. Proposes only — Will approves/rejects; never executes. |
| **FORGE** | Positions / P&L / trade artifacts | 🟡 | `FORGE/STATUS.md` converts research → positions → P/L. Sub-folders per trade (KRE/, WAL/, etc.). |

## Commodity / Sector

| Agent | Domain | Status | Key |
|-------|--------|--------|-----|
| **FERT** | Fertilizer / food security | 🔴 | Urea +32%, China export halt, CF structural bull. Qatar LNG = permanent supply destruction. |
| **CRUISE** | Cruise industry / tourism canary | 🔴 | CCL unhedged (-25-30%), NCLH fragile ($700M interest vs $600M income). Gulf season cancelled. 290K US jobs. |

## Transmission
```
LABOR → CARL → REGINALD → repricing
CREED → REGINALD (national CRE/CMBS bank bridge) + LIQUID (refi/funding) + CARL (multifamily spillovers)
LIQUID amplifies any stage | HENRY = speed gauge
SAM + ZHAO + HANS = parallel global risk | HAWK = external shock
HAWK (military) → BRENT (oil fundamentals) → CARL (gas pumps) + LIQUID (energy credit) + HENRY (inflation) + SAM (Japan energy)
BRENT (energy) → FERT (fertilizer/food) → CARL (consumer food CPI) + HENRY (inflation)
HAWK (geopolitical) → FERT (China policy, Gulf damage)
BRENT (fuel) → CRUISE (operator P&L) → CARL (port city impact) + LABOR (port employment)
HAWK (Gulf/insurance) → CRUISE (itinerary cancellations)
SHADE = insurance plumbing under BROCK/REGINALD | feeds LIQUID on systemic
BOND = bond market structure between LIQUID (plumbing) and ZHAO (foreign flows) | auctions → LIQUID (repo demand) | credit spreads → HENRY (credit-equity lead) | issuance freeze → REGINALD (bank funding)
ORACLE monitors prediction market odds → divergence signals to RED, confirmation signals to domain agents
NEXUS synthesizes across all → convergence/contradiction → PROME
HERMES carries signals between all agents (OUTBOX → INBOX, 2x daily)
```

## File Paths
All agents at `AGENTS/<NAME>/STATUS.md`. Sub-agents: `AGENTS/<PARENT>/<SUB>/`. FORGE at `FORGE/STATUS.md`.

Status key: 🟢 none | 🟡 monitoring | 🟠 elevated | 🔴 active/critical
