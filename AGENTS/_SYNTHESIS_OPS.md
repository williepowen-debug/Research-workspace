# AGENTS — Synthesis / Trading / Operations

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Synthesis and adversarial review

| Agent | Path | Role |
|---|---|---|
| NEXUS | [`NEXUS/`](./NEXUS/) | Cross-agent synthesis, convergence detection, contradiction flagging. |
| VIOLET | [`VIOLET/`](./VIOLET/) | VIX, vol term structure, credit-to-vol lag detection. |
| RED | [`RED/`](./RED/) | Adversarial analysis; challenges all theses. |
| ORACLE | [`ORACLE/`](./ORACLE/) | Prediction-market monitoring and odds divergence. |
| SENTRY | [`SENTRY/`](./SENTRY/) | Cross-domain signal synthesis / alerting surface. |

## Trading / execution rails

| Agent | Path | Role |
|---|---|---|
| TERRY | [`TERRY/`](./TERRY/) | Trade construction, sizing, invalidation, roll/no-roll rules, postmortems. |
| EARNINGS | [`EARNINGS/`](./EARNINGS/) | Earnings-event surface / workbook. |

## Archived / dormant

| Folder | Status | Current owner |
|---|---|---|
| TRADES | [`TRADES/`](./TRADES/) source archive only | Superseded by [`TERRY/`](./TERRY/) |

## Operations / delivery / research

| Agent | Path | Role |
|---|---|---|
| PROME | [`PROME/`](./PROME/) | Chief-of-staff/orchestration state, decisions, handoffs. |
| WALTER | [`WALTER/`](./WALTER/) | Signal/news routing and intelligence desk. |
| HERMES | [`HERMES/`](./HERMES/) | Signal delivery between outboxes/inboxes. |
| DEWEY | [`DEWEY/`](./DEWEY/) | Deep research executor and data-pull script home. |
| ATHENA | [`ATHENA/`](./ATHENA/) | Reading companion and knowledge compounder. |
| BUFFER | [`BUFFER/`](./BUFFER/) | Handoff/workbuffer surface. |

## Operating rule

Synthesis agents should compress and route, not duplicate domain work. Domain agents own source-detail; synthesis surfaces own contradiction, priority, decision framing, and trade-readiness.

## Closest bridges

- Credit domains → [`_CREDIT.md`](./_CREDIT.md)
- Private credit / insurance → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Energy / geopolitics → [`_ENERGY.md`](./_ENERGY.md)
- Funding / macro → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
