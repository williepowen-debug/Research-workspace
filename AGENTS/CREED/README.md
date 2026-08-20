# CREED File Index

**Purpose:** separate current CREED operating truth from legacy source archive material.

## Current boot / operating files

Read these first:

0. `AGENTS/CREED/SCRATCH.md` — **read first.** Ephemeral session handoff: what the last session was mid-way through, next-boot first moves, open threads, standing traps. **Lowest authority — if it disagrees with STATUS, STATUS is right.**
1. `AGENTS/CREED/CLAUDE.md` — canonical boot order and guardrails
2. `AGENTS/CREED/STATUS.md` — current status, thesis state, and first-work priority
3. `AGENTS/CREED/COVERAGE.md` — **the map of the territory**: 12 lanes, each with its **data vintage** (not its touch date), a maturity grade, and the **blind-spot register with the finder recorded**. *(Took this boot slot 2026-07-27 from `REVIVAL_PLAN.md`, now FROZEN — a closed episode doc that was still being read at every wake.)*

## Operating ledgers and logs *(added 2026-07-27 — fleet-parity pass against SHADE/BROCK)*

| File | Role |
|---|---|
| `board_log.tsv` | **Every mail item CREED has read, with its reasoned disposition.** Logged at READ time. An unlogged consume is indistinguishable from a never-seen. ⚠️ Pre-2026-07-11 lane history is **prose-sourced, deliberately not retrofitted** — see the `[PRE-LEDGER-BACKFILL]` row. |
| `SCRATCH.md` | Ephemeral session handoff (overwritten each closeout). Created after an unclean shutdown left CREED with no in-flight-work surface. |
| `MAINTENANCE.md` | **Structural** change log — why CREED is organized this way. **Consult-on-structural-work, NOT a per-session ritual.** Analytical pivots go in `thesis/CHANGELOG.md` instead. |
| `COVERAGE.md` | Lane-by-lane coverage map keyed to **data vintage**, with maturity grades and the blind-spot register. Adopted from `CORAL/COVERAGE.md`. |
| ~~`REVIVAL_PLAN.md`~~ | ⛔ **FROZEN 2026-07-27** — closed episode doc, out of the boot order. Live items forked up to `CLAUDE.md` §Guardrails. Do not cite as current. |
| `LAST_COMPLETION.md` | Closeout stamp. ⚠️ **It skipped the 7/20 and 7/27 closeouts and went stale enough to propagate a wrong claim three hops.** If `STATUS.md` is materially newer than this file, **a closeout was skipped — treat its claims as UNKNOWN, not current.** |

## Threshold registry — `registry/` *(added to this index 2026-08-20; it existed since 7/27 and this file never listed it)*

| File | Role |
|---|---|
| `registry/THRESHOLDS.tsv` | **Machine-readable transcription of the FIRE conditions in `thesis/THESIS.md`.** 11 `CREED-T-*` rows. **Bands are FROZEN TERMS (Will, 7/21) — propose, don't edit.** ⚠️ **Only 5 rows are numerically scannable**; the rest are qualitative, compound, or HOMER-owned — **a clean scan of the 5 must never imply the 11 are clear.** ⚠️ **14 comment lines precede the header — count rows matching `^CREED-T`, never `tail -n +2`.** WALTER reads this file. |
| `registry/CREED_T_FIRED_LOG.tsv` | **NEW 2026-08-20 — the SINGLE record of CREED-T fires.** Carries `effective_date` and `detection_lag` as separate columns on purpose: the date a band was satisfied is not the date CREED noticed. ⚠️ **Deliberately the only such ledger** — WALTER asked to build a mirror and CREED declined (a fire recorded in two disagreeing places is worse than one recorded nowhere). |

## Live metric layer — the workbook (built 2026-07-27)

`AGENTS/CREED/workbook/` — the quantitative spine under the prose rails. **Read `VX.tsv` at boot and run the 14-day staleness check** (recipe in `CLAUDE.md`).

| File | Role |
|---|---|
| `VX.tsv` | **32-vector dashboard** across 10 categories, mapped to the Expected Signals. The heart. *(31 at build; `VX-CREED-3.04` added 2026-08-20 as the K5 root-cause fix.)* |
| `FLOW.tsv` | 8 CRE transmission chains (legacy 6 refreshed + FLOW-07 lender withdrawal, FLOW-08 fast→slow holder migration) |
| `KB.tsv` | **19** Admiralty-scored research rows, seeded fresh (legacy 40KB KB deliberately not imported). *(16 at build + `KB-CREED-017`, the MBA note-holder-attribution finding. This line read "16" for ~3 hours after 017 landed — caught in the 7/27 consolidation audit, which is exactly the drift class CREED spent the day catching in other agents.)*|
| `PREDICTIONS.tsv` | **9** open forecasts + 1 resolved (`PRED-CREED-009`, TRUE 2026-08-20) + `002a` excluded-for-provenance. CREED-set confidences, each naming its resolving instrument |
| `PREDICTIONS_SCOREBOARD.md` | Calibration surface + resolution protocol. **n=1** as of 2026-08-20 (`PRED-CREED-009` TRUE; 0/1, Brier 0.49 — recorded straight). **Update it in the same session as the ledger row: both writes, or neither counts.** |
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
