# AGENTS — Synthesis / Trading / Operations

Canonical paths remain `AGENTS/<NAME>/` for active agents. Prome is the orchestration surface and lives in root `PROME/`; the old `AGENTS/PROME/` tree is archived.

## Synthesis and adversarial review

| Agent | Path | Role |
|---|---|---|
| NEXUS | [`NEXUS/`](./NEXUS/) | Cross-agent synthesis, convergence detection, contradiction flagging. |
| VIOLET | [`VIOLET/`](./VIOLET/) | VIX, vol term structure, credit-to-vol lag detection. |
| RED | [`RED/`](./RED/) | Adversarial analysis; challenges all theses. |
| ORACLE | [`ORACLE/`](./ORACLE/) | Prediction-market monitoring and odds divergence. |
| SENTRY | [`SENTRY/`](./SENTRY/) | Cross-domain signal synthesis / alerting surface. *(dormant — revive on need.)* |

## Trading / execution rails

| Agent | Path | Role |
|---|---|---|
| TERRY | [`TERRY/`](./TERRY/) | Trade construction, sizing, invalidation, roll/no-roll rules, postmortems. |

## Operations / delivery / research

| Agent | Path | Role |
|---|---|---|
| PROME | [`../PROME/`](../PROME/) | Chief-of-staff/orchestration state, decisions, handoffs. |
| WALTER | [`WALTER/`](./WALTER/) | Signal/news routing and intelligence desk. |
| DEWEY | [`DEWEY/`](./DEWEY/) | Deep research executor and data-pull script home. |

## Meta

| Agent | Path | Role |
|---|---|---|
| DAEDALUS | [`DAEDALUS/`](./DAEDALUS/) | Fleet architect — design/structure/maturity/lifecycle (on-demand). |
| RAV | [`RAV/`](./RAV/) | Meta — deep factual/analytical reviewer + bounded repair (Codex, Will-driven). |
| YEYOU | [`YEYOU/`](./YEYOU/) | Repo-wide reviewer (manual/branch model). |

## Archived / dormant

| Folder | Status | Current owner / note |
|---|---|---|
| ATHENA | [`ATHENA/`](./ATHENA/) archive-source (do not launch) | Reading/knowledge companion; folder left in place |
| EARNINGS | retired → [`_archive/EARNINGS/`](./_archive/EARNINGS/) | Earnings-event workbook scaffold, never launched |
| BUFFER | retired → [`_archive/BUFFER/`](./_archive/BUFFER/) | Handoff/workbuffer scaffold, never launched |
| TRADES | folder pruned (2026-06 public-prep; recoverable from git history) | Superseded by [`TERRY/`](./TERRY/) |
| HERMES | folder removed (2026-06 prune) | Mail-carrier deprecated by the messaging overhaul |
| PROME (legacy) | archived at [`../PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/`](../PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/) | Live Prome uses root [`../PROME/`](../PROME/) |

## Operating rule

Synthesis agents should compress and route, not duplicate domain work. Domain agents own source-detail; synthesis surfaces own contradiction, priority, decision framing, and trade-readiness.

## Closest bridges

- Credit domains → [`_CREDIT.md`](./_CREDIT.md)
- Private credit / insurance → [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md)
- Energy / geopolitics → [`_ENERGY.md`](./_ENERGY.md)
- Funding / macro → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
