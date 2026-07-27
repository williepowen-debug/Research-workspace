# CREED File Index

**Purpose:** separate current CREED operating truth from legacy source archive material.

## Current boot / operating files

Read these first:

1. `AGENTS/CREED/CLAUDE.md` — canonical boot order and guardrails
2. `AGENTS/CREED/STATUS.md` — current status, thesis state, and first-work priority
3. `AGENTS/CREED/REVIVAL_PLAN.md` — revival phases and legacy inventory

## Live metric layer — the workbook (built 2026-07-27)

`AGENTS/CREED/workbook/` — the quantitative spine under the prose rails. **Read `VX.tsv` at boot and run the 14-day staleness check** (recipe in `CLAUDE.md`).

| File | Role |
|---|---|
| `VX.tsv` | **31-vector dashboard** across 10 categories, mapped to the Expected Signals. The heart. |
| `FLOW.tsv` | 8 CRE transmission chains (legacy 6 refreshed + FLOW-07 lender withdrawal, FLOW-08 fast→slow holder migration) |
| `KB.tsv` | 16 Admiralty-scored research rows, seeded fresh (legacy 40KB KB deliberately not imported) |
| `PREDICTIONS.tsv` | 9 open forecasts, CREED-set confidences, each naming its resolving instrument |
| `VX_HISTORY.tsv` | monthly series for the load-bearing vectors — a level is not a trend |
| `SCHEMA.tsv` | 14-column controlled vocabulary governing `KB.tsv` |
| `WORKBOOK_DESIGN.md` | design rationale + build record + the five Will-approved §10 decisions |

**Canonical-truth order:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/`. If the workbook disagrees with STATUS, **STATUS is right and the workbook is stale.** Threshold bands are **frozen terms** (Will, 7/21) — propose, don't edit. Vectors `4.01` (REGINALD) and `1.03`/`6.01` (HOMER) are **shared — reference, don't fork.**

## Current analytical rails

Use these before making current CRE / CMBS claims:

- `AGENTS/CREED/research/REFRESH_2026-07-27.md` — **current source pack** (CRE lender leg: ARI wind-down + KREF credit recognition; June SS resolved at 17.11%; life-science bifurcation; mall-cadence kill; 7/27 intraday tape)
- `AGENTS/CREED/research/REFRESH_2026-07-04.md` — superseded 7/27; retained as June-Trepp / realized-recognition-cluster source-trail
- `AGENTS/CREED/research/REFRESH_2026-06-21.md` — superseded 7/4; retained as FDIC-Q1 / maturity-wall source-trail
- `AGENTS/CREED/thesis/THESIS.md` — current thesis rails
- `AGENTS/CREED/thesis/CHANGELOG.md` — thesis change history
- `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md` — stale inbox resolved against current rails
- `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` — public REIT equity-market tape module absorbed from dormant REITS
- `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md` — durable mechanisms pulled from legacy CREED, with old values marked stale

## Legacy / archive surfaces

Do **not** treat these as current analytical truth:

- ~~`AGENTS/CREED/inbox/2026-02-24_signals.md`~~ — removed 6/28 (triaged → `research/INBOX_TRIAGE_2026-06-21.md`; content in THESIS). Live inbox is `inbox/WALTER/`.
- `AGENTS/REGINALD/sub-agents/CREED/` — legacy REGINALD sub-agent tree / source archive
- `AGENTS/REITS/` — dormant public-REIT source archive; live REIT tape now belongs to CREED

The legacy tree is useful for mechanism libraries, old source trails, and tracker design. It is not a live dashboard.

## Guardrail

No trade recommendations or current market claims from legacy Jan/Feb/March 2026 values unless they are refreshed against current primary/source data.
