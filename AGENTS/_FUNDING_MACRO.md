# AGENTS — Funding / Macro / Market Structure

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Core funding and macro surfaces

| Agent | Path | Role |
|---|---|---|
| LIQUID | [`LIQUID/`](./LIQUID/) | Funding, Treasury plumbing, repo, reserves, SOFR/IORB, auction stress. |
| BOND | [`BOND/`](./BOND/) | Bond market structure, auctions, issuance, HY/IG, CDX/cash divergence. |
| HENRY | [`HENRY/`](./HENRY/) | Market structure and econ data velocity: gamma/GEX, VIX, CPI/PPI/PCE/NFP/ISM. |
| SAM | [`SAM/`](./SAM/) | Japan/BOJ/JGB/carry-unwind risk. |
| ZHAO | [`ZHAO/`](./ZHAO/) | China, TIC, foreign UST demand, capital flows, HK peg. |
| HANS | [`HANS/`](./HANS/) | Europe through US-risk lens: ECB, sovereign spreads, UST demand. |
| VULCAN | [`VULCAN/`](./VULCAN/) | AI-capex / semis / memory / concentration risk — systemic market-structure surface (DAEDALUS-built 2026-07-10/11); feeds VIOLET (concentration), HENRY (capex/FCF), WATT (power demand); ZHAO (export controls) + HAWK (Taiwan chokepoint) feed in. |

## Transmission map

```text
SAM / ZHAO / HANS → LIQUID
BOND ↔ LIQUID ↔ HENRY
VULCAN → VIOLET / HENRY / WATT (AI-capex concentration)
{BOND, ZHAO} ↔ MIDAS → LIQUID / HENRY (metals bridge: gold↔real-rates w/ BOND, copper↔China w/ ZHAO — MIDAS home page: _ENERGY.md)
Credit / energy shocks become systemic when LIQUID confirms funding amplification.
```

## Archived / retired

- **FOREX** retired → `AGENTS/_archive/FOREX/` (FX workbook scaffold, never launched). Residual FX/flows covered by ZHAO (TIC) + BOND.

## Closest bridges

- Credit/bank stress → [`_CREDIT.md`](./_CREDIT.md)
- Private-credit/insurance stress → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Energy/geopolitical shocks + power (WATT) + metals (MIDAS) → [`_ENERGY.md`](./_ENERGY.md)
- Vol lag / synthesis / trading → [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md)
