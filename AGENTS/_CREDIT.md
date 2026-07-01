# AGENTS — Credit / Consumer / Banks

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Core credit chain

| Agent | Path | Role |
|---|---|---|
| LABOR | [`LABOR/`](./LABOR/) | Employment, claims, labor-market deterioration; upstream credit trigger. |
| CARL | [`CARL/`](./CARL/) | Consumer credit, housing, delinquencies, phantom debt; receives LABOR stress. |
| OTTO | [`OTTO/`](./OTTO/) | Auto and consumer DQ canary; feeds CARL. |
| REGINALD | [`REGINALD/`](./REGINALD/) | Regional banks, NDFI exposure, CRE bank transmission, WAL/OZK bank transmission. |
| OZK | [`OZK/`](./OZK/) | Bank OZK focused surface; spun out from REGINALD. |
| CORAL | [`CORAL/`](./CORAL/) | Florida convergence: real estate, insurance, FL banks, migration/tourism. |
| CREED | [`CREED/`](./CREED/) | National CRE / CMBS market stress plus public REIT equity-market tape; feeds REGINALD, CORAL, LIQUID, and CARL. Claude Code roster — do not spawn without explicit Will permission. |

## Transmission map

```text
LABOR → CARL → REGINALD → repricing
           ↘ OTTO
CREED → REGINALD (national CRE/CMBS + REIT tape bank bridge) + LIQUID (refi/funding) + CARL (multifamily)
REGINALD ↔ OZK / CORAL / BROCK
LIQUID amplifies; HENRY gauges market speed; VIOLET tracks credit→vol lag.
```

## Closest bridges

- Private credit / BDC stress → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Treasury/funding amplification → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
- Cross-agent synthesis/trade conversion → [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md)

## Archived / dormant

- **REITS** folder was pruned in the 2026-06 public-prep cleanup (recoverable from git history); public REIT equity-market tape is now owned by CREED via `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md`.
- **DOC** retired → `AGENTS/_archive/DOC/`.
