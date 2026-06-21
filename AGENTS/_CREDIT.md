# AGENTS — Credit / Consumer / Banks

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Core credit chain

| Agent | Path | Role |
|---|---|---|
| LABOR | [`LABOR/`](./LABOR/) | Employment, claims, labor-market deterioration; upstream credit trigger. |
| CARL | [`CARL/`](./CARL/) | Consumer credit, housing, delinquencies, phantom debt; receives LABOR stress. |
| OTTO | [`OTTO/`](./OTTO/) | Auto and consumer DQ canary; feeds CARL. |
| DOC | [`DOC/`](./DOC/) | CARL-linked consumer/medical/adjacent credit subdomain. |
| REGINALD | [`REGINALD/`](./REGINALD/) | Regional banks, CRE, NDFI exposure, WAL/OZK bank transmission. |
| OZK | [`OZK/`](./OZK/) | Bank OZK focused surface; spun out from REGINALD. |
| CORAL | [`CORAL/`](./CORAL/) | Florida convergence: real estate, insurance, FL banks, migration/tourism. |
| CREED | [`CREED/`](./CREED/) | CRE-focused bank/credit subdomain. |
| REITS | [`REITS/`](./REITS/) | Public REIT/real-estate stress monitor. |

## Transmission map

```text
LABOR → CARL → REGINALD → repricing
           ↘ OTTO / DOC / REITS
REGINALD ↔ OZK / CREED / CORAL
LIQUID amplifies; HENRY gauges market speed; VIOLET tracks credit→vol lag.
```

## Closest bridges

- Private credit / BDC stress → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Treasury/funding amplification → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
- Cross-agent synthesis/trade conversion → [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md)
