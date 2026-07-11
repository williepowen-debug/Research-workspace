# AGENTS Network Map

**Purpose:** canonical topology for agent transmission, synthesis, and routing.

**Status:** live map source. Historical visual maps live in `PROME/archive/agent_network.*`. Do not maintain separate live topologies. Dormant / archive-source / retired agents are omitted here (they don't currently transmit) — full roster + tiers → [`_INDEX.md`](./_INDEX.md) + [`../PROME/ROSTER.md`](../PROME/ROSTER.md).

## Core model

Prome is the chief-of-staff/orchestration layer. Domain agents own source-detail. NEXUS/RED/VIOLET/TERRY convert domain work into synthesis, challenge, vol/tape timing, and trade construction.

```mermaid
flowchart LR
    PROME[[PROME<br/>Chief of staff / orchestration]]
    WALTER[[WALTER<br/>Signal/news routing]]
    NEXUS[[NEXUS<br/>Cross-agent synthesis]]
    RED[[RED<br/>Adversarial review]]
    VIOLET[[VIOLET<br/>Credit → vol lag]]
    TERRY[[TERRY<br/>Trade construction]]
    ORACLE[[ORACLE<br/>Prediction markets]]

    subgraph CREDIT[Credit / consumer / banks]
        LABOR[LABOR<br/>Employment / claims]
        CARL[CARL<br/>Consumer credit / housing]
        OTTO[OTTO<br/>Auto / consumer DQ]
        REGINALD[REGINALD<br/>Regional banks]
        OZK[OZK<br/>Bank OZK]
        CORAL[CORAL<br/>Florida convergence]
        CREED[CREED<br/>National CRE / CMBS / REIT tape]
    end

    subgraph PC[Private credit / insurance]
        BROCK[BROCK<br/>BDCs / private credit / CLOs]
        SHADE[SHADE<br/>PE-insurance wrappers]
    end

    subgraph ENERGY[Energy / geopolitics / commodities / climate]
        HAWK[HAWK<br/>Geopolitical / military]
        BRENT[BRENT<br/>Oil / energy markets]
        MARCO[MARCO<br/>Migration / labor supply]
        AEOLUS[AEOLUS<br/>Climate → economy]
        BARON[BARON<br/>Policy network]
        WATT[WATT<br/>Grid stress / power price]
        MIDAS[MIDAS<br/>Metals: monetary + industrial]
    end

    subgraph MACRO[Funding / macro / market structure]
        LIQUID[LIQUID<br/>Funding / Treasury plumbing]
        BOND[BOND<br/>Bond market structure]
        HENRY[HENRY<br/>Market structure / econ tape]
        SAM[SAM<br/>Japan / BOJ / carry]
        ZHAO[ZHAO<br/>China / TIC / capital flows]
        HANS[HANS<br/>Europe / UST demand]
        VULCAN[VULCAN<br/>AI-capex / semis / memory]
    end

    subgraph RESEARCH[Research / ops]
        DEWEY[DEWEY<br/>Deep research executor]
    end

    %% Primary transmission chains
    LABOR -->|labor stress| CARL
    OTTO -->|auto DQ| CARL
    CARL -->|consumer/housing losses| REGINALD
    CORAL -->|FL bank/real estate convergence| REGINALD
    CREED -->|CRE / CMBS / public REIT tape bank bridge| REGINALD
    CREED -->|maturity wall / refi pressure| LIQUID
    CREED -->|multifamily spillovers| CARL
    CREED -->|Florida overlap only| CORAL
    OZK -. peer bank surface .- REGINALD

    BROCK -->|private-credit vehicle stress| SHADE
    SHADE -->|insurer/funding wrapper stress| LIQUID
    BROCK -->|NDFI / BDC bank bridge| REGINALD
    BROCK -->|credit market stress| BOND

    HAWK -->|kinetic/chokepoint catalyst| BRENT
    BRENT -->|inflation / demand destruction| HENRY
    BRENT -->|energy credit / funding shock| LIQUID
    BRENT -->|gas pump / consumer pressure| CARL
    MARCO -->|labor supply / migration| LABOR
    MARCO -->|tourism / migration bridge| CORAL
    BARON -->|policy vector| HAWK
    AEOLUS -->|energy demand| BRENT
    AEOLUS -->|FL insurance / property| CORAL
    AEOLUS -->|food CPI / migration| MARCO

    %% Power (WATT), AI-capex (VULCAN), Metals (MIDAS) — DAEDALUS build 2026-07-10/11
    AEOLUS -->|grid-stress detection| WATT
    WATT -->|power cost / FCF input| HENRY
    WATT -->|retail pass-through| CARL
    BRENT -->|gas → power| WATT
    VULCAN -->|AI-capex concentration| VIOLET
    VULCAN -->|capex / FCF| HENRY
    VULCAN -->|compute → power demand| WATT
    ZHAO -->|China export controls| VULCAN
    HAWK -->|Taiwan chip chokepoint| VULCAN
    MIDAS -->|gold ↔ real-rate tell| BOND
    MIDAS -->|safe-haven flow| LIQUID
    MIDAS -->|copper ↔ China demand| ZHAO
    MIDAS -->|copper / PGM growth tell| HENRY
    HAWK -->|PGM supply SA/Russia| MIDAS

    SAM -->|carry unwind / JGB stress| LIQUID
    SAM -->|carry volatility| HENRY
    ZHAO -->|foreign UST demand / capital flows| LIQUID
    ZHAO -->|Asia flow feedback| SAM
    HANS -->|Europe / UST demand| LIQUID
    BOND -->|auctions / issuance / CDX-cash| LIQUID
    BOND -->|credit-equity lead| HENRY
    LIQUID -->|funding amplification| REGINALD
    LIQUID -->|market plumbing regime| HENRY
    HENRY -->|velocity / tape read| NEXUS

    %% Synthesis and decision loop
    WALTER -->|routed signals| LABOR
    WALTER -->|routed signals| CARL
    WALTER -->|routed signals| REGINALD
    WALTER -->|routed signals| BROCK
    WALTER -->|routed signals| HAWK
    WALTER -->|routed signals| BRENT
    WALTER -->|routed signals| LIQUID
    WALTER -->|routed signals| NEXUS

    LABOR --> NEXUS
    CARL --> NEXUS
    REGINALD --> NEXUS
    BROCK --> NEXUS
    SHADE --> NEXUS
    HAWK --> NEXUS
    BRENT --> NEXUS
    LIQUID --> NEXUS
    BOND --> NEXUS
    SAM --> NEXUS
    VIOLET --> NEXUS
    ORACLE --> NEXUS

    BOND -->|credit → vol lead| VIOLET
    BROCK -->|credit stress / vol lag| VIOLET
    REGINALD -->|bank stress / vol lag| VIOLET
    VIOLET --> HENRY

    NEXUS --> RED
    RED --> NEXUS
    NEXUS --> TERRY
    VIOLET --> TERRY
    HENRY --> TERRY
    LIQUID --> TERRY
    TERRY -->|trade cards / rails| PROME
    NEXUS -->|decision synthesis| PROME
    PROME -->|tasking / priorities| WALTER
    PROME -->|research execution| DEWEY
```

## Chain summary

| Chain | Primary path | What confirms stress |
|---|---|---|
| Credit | LABOR → CARL → REGINALD → HENRY/LIQUID, with CREED feeding CRE/CMBS and public REIT tape bank-bridge stress | Claims/payroll composition, consumer DQ/housing, CRE maturity/default recognition, REIT equity/NAV/dividend stress, bank loss recognition, market repricing |
| Private credit | BROCK → SHADE → LIQUID / REGINALD | Gates, PIK/NAV stress, insurer wrapper funding, NDFI bank bridge |
| Energy shock | HAWK → BRENT → HENRY/LIQUID/CARL | Kinetic/chokepoint events, Brent/storage/insurance, inflation/demand destruction, energy credit |
| Climate → economy | AEOLUS → BRENT / CORAL / MARCO | Insurance losses, ag/food supply shifts, energy-demand swings on a weather/structural horizon |
| Power | AEOLUS → WATT → HENRY / CARL; BRENT → WATT | Grid emergencies (PJM EEA), LMP spikes, capacity-auction clears at cap, data-center load |
| AI-capex | VULCAN → VIOLET / HENRY / WATT; ZHAO / HAWK → VULCAN | Hyperscaler capex guides, Mag-7 concentration, memory cycle, export controls, Taiwan chokepoint |
| Metals | {BOND, ZHAO} ↔ MIDAS → LIQUID / HENRY; HAWK → MIDAS | Gold real-rate divergence (debasement), copper/China demand, GSR, PGM supply |
| Japan/carry | SAM → LIQUID/HENRY | JGB/BOJ/carry unwind, USDJPY/FXY, global funding volatility |
| Credit-to-vol | BOND/BROCK/REGINALD → VIOLET → HENRY/LIQUID/RED | Credit spreads or bank stress widen before VIX/vol catches up |

## Ownership rules

- `AGENTS.md` owns compact roster, spawn restrictions, and canonical transmission chains.
- `AGENTS/_INDEX.md` owns grouped directory navigation.
- This file owns the live topology map.
- Runtime architecture / operating model → root `CLAUDE.md` ("How The System Works") + `PROME/SYSTEM.md`. *(`AGENTS_DIRECTORY.md` retired → `archive/` 2026-06-30.)*
