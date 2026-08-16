# AGENTS — Credit / Consumer / Banks

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Core credit chain

| Agent | Path | Role |
|---|---|---|
| LABOR | [`LABOR/`](./LABOR/) | Employment, claims, labor-market deterioration; upstream credit trigger. |
| CARL | [`CARL/`](./CARL/) | Consumer credit / consumer-transmission macro, delinquencies, phantom debt; receives LABOR stress; consumes HOMER housing asset-market data. |
| HOMER | [`HOMER/`](./HOMER/) | Housing asset market (foreclosure pipeline, GSE + Trepp CMBS-MF one-owner figure, builders, HPI, mortgage-rate surface); promoted from CARL 2026-07-12. Feeds CARL (consumer transmission), REGINALD (bank collateral), HENRY (wealth effect). |
| OTTO | [`OTTO/`](./OTTO/) | Auto and consumer DQ canary; feeds CARL. |
| REGINALD | [`REGINALD/`](./REGINALD/) | Regional banks hub — cohort matrix, NDFI exposure, CRE bank transmission; WAL + OZK are peer single-name agents (pointer-only seams). |
| OZK | [`OZK/`](./OZK/) | Bank OZK focused surface; spun out from REGINALD 2026-04-24. |
| WAL | [`WAL/`](./WAL/) | Western Alliance (WAL) focused surface — thesis v2.3, frozen-frame print grading, FRAUD/ litigation arc; promoted from REGINALD 2026-07-25. |
| CORAL | [`CORAL/`](./CORAL/) | Florida convergence: real estate, insurance, FL banks, migration/tourism. |
| CREED | [`CREED/`](./CREED/) | National CRE / non-MF CMBS market stress plus public REIT equity-market tape; feeds REGINALD, CORAL, and LIQUID. Multifamily / Trepp CMBS-MF figure handed to HOMER (one-owner handoff 2026-07-12). Claude Code roster — do not spawn without explicit Will permission. |

## Transmission map

```text
LABOR → CARL → REGINALD → repricing
           ↘ OTTO
HOMER → CARL (consumer transmission) / REGINALD (bank collateral) / HENRY (wealth effect)
CREED → REGINALD (national CRE/non-MF CMBS + REIT tape bank bridge) + LIQUID (refi/funding) + HOMER (Trepp CMBS-MF, one-owner handoff)
REGINALD ↔ WAL / OZK / CORAL / BROCK
LIQUID amplifies; HENRY gauges market speed; VIOLET tracks credit→vol lag.
```

## Closest bridges

- Energy/commodity cost pass-through into consumer prices (BRENT → CARL gas-pump; WATT → CARL retail power; **FERT → CARL food-CPI, re-chartered 2026-08-16**) → [`_ENERGY.md`](./_ENERGY.md)
- Private credit / BDC stress → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Treasury/funding amplification → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
- Cross-agent synthesis/trade conversion → [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md)

## Archived / dormant

- **REITS** folder was pruned in the 2026-06 public-prep cleanup (recoverable from git history); public REIT equity-market tape is now owned by CREED via `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md`.
- **DOC** retired → `AGENTS/_archive/DOC/`.
