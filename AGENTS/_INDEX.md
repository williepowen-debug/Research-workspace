# AGENTS Index

**Purpose:** Human-friendly organization layer for the flat `AGENTS/<NAME>/` directory.

**Important:** Canonical agent paths remain flat. Do **not** move active agent folders without a migration pass; many docs, scripts, and Claude/OpenClaw workflows reference `AGENTS/<NAME>/...` directly.

Canonical topology / transmission map: [`_NETWORK.md`](./_NETWORK.md).

## Quick groups

| Group | File | What it covers |
|---|---|---|
| Credit / Consumer / Banks | [`_CREDIT.md`](./_CREDIT.md) | Labor, consumer credit, housing, banks, Florida, REIT/CRE |
| Private Credit / Insurance | [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md) | BDCs, CLOs, PE-insurance wrappers |
| Energy / Geopolitics / Commodities | [`_ENERGY.md`](./_ENERGY.md) | Military shocks, oil, fertilizer, cruise/tourism, policy/geopolitical vectors |
| Funding / Macro / Market Structure | [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md) | Treasury plumbing, rates, Japan/China/Europe, FX, econ tape |
| Synthesis / Trading / Operations | [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md) | Cross-agent synthesis, adversarial review, trade construction, delivery, research ops |

## Canonical roster

| Agent | Canonical path | Primary group |
|---|---|---|
| ATHENA | [`ATHENA/`](./ATHENA/) | Synthesis / Ops |
| BARON | [`BARON/`](./BARON/) | Energy / Geopolitics |
| BOND | [`BOND/`](./BOND/) | Funding / Macro |
| BRENT | [`BRENT/`](./BRENT/) | Energy / Geopolitics |
| BROCK | [`BROCK/`](./BROCK/) | Private Credit |
| BUFFER | [`BUFFER/`](./BUFFER/) | Synthesis / Ops |
| CARL | [`CARL/`](./CARL/) | Credit |
| CORAL | [`CORAL/`](./CORAL/) | Credit |
| CREED | [`CREED/`](./CREED/) | Credit |
| CRUISE | [`CRUISE/`](./CRUISE/) | Energy / Geopolitics |
| DEWEY | [`DEWEY/`](./DEWEY/) | Synthesis / Ops |
| DOC | [`DOC/`](./DOC/) | Credit |
| EARNINGS | [`EARNINGS/`](./EARNINGS/) | Synthesis / Ops |
| FERT | [`FERT/`](./FERT/) | Energy / Geopolitics |
| FOREX | [`FOREX/`](./FOREX/) | Funding / Macro |
| HANS | [`HANS/`](./HANS/) | Funding / Macro |
| HAWK | [`HAWK/`](./HAWK/) | Energy / Geopolitics |
| HENRY | [`HENRY/`](./HENRY/) | Funding / Macro |
| HERMES | [`HERMES/`](./HERMES/) | Synthesis / Ops |
| LABOR | [`LABOR/`](./LABOR/) | Credit |
| LIQUID | [`LIQUID/`](./LIQUID/) | Funding / Macro |
| MARCO | [`MARCO/`](./MARCO/) | Energy / Geopolitics / Credit bridge |
| NEXUS | [`NEXUS/`](./NEXUS/) | Synthesis / Ops |
| ORACLE | [`ORACLE/`](./ORACLE/) | Synthesis / Ops |
| OTTO | [`OTTO/`](./OTTO/) | Credit |
| OZK | [`OZK/`](./OZK/) | Credit |
| PROME | [`PROME/`](./PROME/) | Synthesis / Ops |
| RED | [`RED/`](./RED/) | Synthesis / Ops |
| REGINALD | [`REGINALD/`](./REGINALD/) | Credit |
| REITS | [`REITS/`](./REITS/) | Credit |
| SAM | [`SAM/`](./SAM/) | Funding / Macro |
| SENTRY | [`SENTRY/`](./SENTRY/) | Synthesis / Ops |
| SHADE | [`SHADE/`](./SHADE/) | Private Credit |
| TERRY | [`TERRY/`](./TERRY/) | Synthesis / Ops |
| TRADES | [`TRADES/`](./TRADES/) | Synthesis / Ops |
| VIOLET | [`VIOLET/`](./VIOLET/) | Synthesis / Ops |
| WALTER | [`WALTER/`](./WALTER/) | Synthesis / Ops |
| ZHAO | [`ZHAO/`](./ZHAO/) | Funding / Macro |

## Maintenance rule

When adding a new agent:
1. Create the canonical folder as `AGENTS/<NAME>/`.
2. Add it to this roster.
3. Add it to exactly one primary group file, plus cross-links if it bridges domains.
4. Update `AGENTS_DIRECTORY.md` if it is an operational agent, not just an experimental/workbook folder.
