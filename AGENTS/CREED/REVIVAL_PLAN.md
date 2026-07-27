> # ⛔ FROZEN 2026-07-27 — THE REVIVAL IS DONE. This is a closed EPISODE doc, not a live surface.
>
> **Removed from the boot order the same day.** CREED has been operational for four sessions (6/28, 7/4, 7/20, 7/27); Phase 5 topology is installed, the workbook is built, and the mandate is live in `CLAUDE.md`. **Reading 165 lines at every boot about how to revive an already-revived agent is a recurring cost for a Tier-2 spawn-on-need agent** — which is the specific thing CREED cannot afford.
>
> **Do not cite rows below as current.** Canonical: `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/`. Kept **unedited** for the source trail.
>
> **The two genuinely-live items were FORKED UP to live surfaces so they are not buried in a closed episode** *(the discipline is LIQUID's — see `CATCHUP_PUNCHLIST.md`, which froze at ~85% and forked its 2 remaining items up rather than letting them die with the doc)*:
>
> 1. **Full legacy migration remains DEFERRED** — `AGENTS/REGINALD/sub-agents/CREED/` stays in place as source archive, moved only if old-path confusion becomes a real problem, and only with grep/ref updates first. → now carried in **`CLAUDE.md` §Guardrails** and **`MAINTENANCE.md`**.
> 2. **The legacy-file inventory** (source-archive paths) → already duplicated in **`CLAUDE.md` §Source Archive** and **`STATUS.md` §Current File State**; this file is no longer the home for it.
>
> *Found in the Will-directed LIQUID/CORAL structure survey, 2026-07-27: an episode doc still sitting at boot-order step 4.*

# CREED REVIVAL PLAN

**Created:** 2026-06-21
**Owner:** Prome until CREED is bootable; CREED owns after revival.
**Status:** Phase 5 topology installed; Phase 6-lite legacy pull-forward installed. Full legacy migration deferred.

---

## Purpose

Revive CREED as the national CRE / CMBS market-stress specialist without losing the legacy REGINALD sub-agent research or accidentally trading from stale February data.

**Recommended mandate:** CREED owns national CRE market-level stress and feeds:
- `REGINALD` — bank exposure, provisions, loss recognition, trade relevance
- `CORAL` — Florida-specific overlap only
- `LIQUID` — refi/funding/channel stress
- `CARL` — multifamily / housing-consumer spillovers

CREED should not own bank-level execution, Florida whole-state synthesis, or position decisions.

---

## Current State

Top-level `AGENTS/CREED/` is now current as the national CRE / CMBS source-pack and thesis-rails surface:
- `AGENTS/CREED/CLAUDE.md`
- `AGENTS/CREED/STATUS.md`
- `AGENTS/CREED/REVIVAL_PLAN.md`
- ~~`AGENTS/CREED/inbox/2026-02-24_signals.md`~~ (removed 6/28 — triaged into `INBOX_TRIAGE_2026-06-21.md`)
- Phase 3 refresh: `AGENTS/CREED/research/REFRESH_2026-06-21.md` (superseded 7/4 by `REFRESH_2026-07-04.md`)
- Phase 4 thesis rails: `AGENTS/CREED/thesis/THESIS.md`
- Phase 4 changelog: `AGENTS/CREED/thesis/CHANGELOG.md`
- Phase 4 inbox triage: `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`
- Phase 6-lite legacy pull-forward: `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md`
- canonical topology/roster integration completed in `AGENTS.md`, `AGENTS_DIRECTORY.md`, `AGENTS/_CREDIT.md`, `AGENTS/_NETWORK.md`, and dashboard mirror
- ✅ **live workbook BUILT 2026-07-27** — `AGENTS/CREED/workbook/` (6 TSVs: SCHEMA/VX/FLOW/KB/PREDICTIONS/VX_HISTORY; 31 vectors, 8 flow chains, boot staleness check wired into `CLAUDE.md`). *This line read "no live workbook/dashboard yet" until 7/27 — corrected in the 7/27 audit sweep.*

The real legacy CREED body lives under REGINALD:
- `AGENTS/REGINALD/sub-agents/CREED/STATUS.md`
- `AGENTS/REGINALD/sub-agents/CREED/EXPECTED_SIGNALS.md`
- `AGENTS/REGINALD/sub-agents/CREED/workbook/`
- `AGENTS/REGINALD/sub-agents/CREED/research/`
- `AGENTS/REGINALD/sub-agents/CREED/sources/`
- `AGENTS/REGINALD/sub-agents/CREED/inbox/2026-02-27_office_reit_selloff.md`

Treat the REGINALD sub-agent tree as **source archive**, not current live truth.

---

## Legacy Thesis Snapshot — Superseded As Current Truth

Legacy CREED frame from Feb 2026:
- CRE stress is real and severe.
- Bank CRE can look healthier than CMBS because of mods, forbearance, FHLB liquidity, and delayed recognition.
- Office CMBS delinquency / special servicing and the maturity wall were the core signals.
- Employment was the key transmission trigger into broader bank loss recognition.

This legacy frame is mechanism context only. Current claims should use the June 2026 source pack and thesis rails.

---

## Inventory — Key Legacy Assets

### Top-level stale inbox

- `AGENTS/CREED/inbox/2026-02-24_signals.md` *(historical inventory — file removed 6/28 after triage; content in `INBOX_TRIAGE_2026-06-21.md`)*
  - CMBS 2026 maturity/default risk estimate
  - hard-maturity / no-extension concept
  - housing liquidity sentiment signal

### REGINALD sub-agent live/archive source

- `AGENTS/REGINALD/sub-agents/CREED/STATUS.md`
  - Feb 2026 status frame and signal dashboard
- `AGENTS/REGINALD/sub-agents/CREED/workbook/VX.tsv`
  - vector dashboard: CMBS DQ, mods, maturity wall, office lease wall, regional stress
- `AGENTS/REGINALD/sub-agents/CREED/workbook/FLOW.tsv`
  - transmission chains: CRE doom loop, maturity wall, NAV cascade, HOA, extend-and-pretend
- `AGENTS/REGINALD/sub-agents/CREED/workbook/KB.tsv`
  - research memory / resolved RQs
- `AGENTS/REGINALD/sub-agents/CREED/workbook/STATUS_archive_20260325.md`
  - archived detail referenced by legacy STATUS
- `AGENTS/REGINALD/sub-agents/CREED/research/`
  - RQ/RP research on special servicing, maturity wall, refinancing gap, FL condo, B/C office, bank mod disclosures, strategic defaults, private credit, AI office demand, insurance amplifier
- `AGENTS/REGINALD/sub-agents/CREED/sources/`
  - source extracts and PDFs, including VLY Q4 materials
- `AGENTS/REGINALD/sub-agents/CREED/inbox/2026-02-27_office_reit_selloff.md`
  - office REIT selloff / AI demand destruction / FDIC CRE data signal

---

## Revival Phases

### Phase 1 — Inventory + preservation

- Create this plan.
- Do not move files.
- Do not update topology.
- Do not treat old CREED data as current.

### Phase 2 — Boot surface

Completed 2026-06-21:
- `AGENTS/CREED/CLAUDE.md`
- `AGENTS/CREED/STATUS.md`

These include mandate, scope boundaries, stale-state warning, source archive pointers, and first refresh checklist.

### Phase 3 — Fresh data refresh

Completed 2026-06-21:
- `AGENTS/CREED/research/REFRESH_2026-06-21.md`

Refresh covered:
- latest Trepp CMBS delinquency / special servicing by property type
- Morningstar/DBRS 2026 maturity wall and maturity-default outlook
- FDIC Q1 2026 CRE delinquency / PDNA
- office REIT / CMBS tape
- multifamily / Sunbelt stress
- bank mod/provision disclosures where relevant

### Phase 4 — Thesis + signal integration

Completed 2026-06-21:
- `AGENTS/CREED/thesis/THESIS.md`
- `AGENTS/CREED/thesis/CHANGELOG.md`
- `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`

Resolved stale inboxes against fresh data:
- maturity wall / hard maturity: kept and promoted, timing refined toward Q4 back-loading
- office REIT / AI demand: downgraded to secondary accelerator until confirmed in leasing/vacancy/default data
- FDIC bank PDNA: kept as bank-convergence watch; Q1 does not confirm broad cascade
- residential housing liquidity: routed away from CREED core toward CARL if refreshed

### Phase 5 — Topology integration

Completed 2026-06-21 after Will approval:
- updated `AGENTS.md`
- updated `AGENTS_DIRECTORY.md`
- updated `AGENTS/_CREDIT.md`
- updated `AGENTS/_NETWORK.md`
- updated `dashboard/index.html` as mirror of the canonical network map

CREED is a Claude Code roster agent. Do not spawn without explicit Will permission.

### Phase 6 — Optional migration / legacy pull-forward

Phase 6-lite completed 2026-06-21:
- `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md`

Decision: do **not** move/delete/copy the full legacy tree now. Keep `AGENTS/REGINALD/sub-agents/CREED/` in place as source archive, and use the pull-forward map to preserve durable mechanisms while marking old values stale.

Future optional migration only if old-path confusion becomes a real problem:
- decide whether to copy/move `AGENTS/REGINALD/sub-agents/CREED/` into a CREED legacy archive folder
- run grep/ref updates and verification before any move

---

## Guardrails

- Do not delete or move REGINALD sub-agent CREED files during revival Phase 1–4.
- Do not trade from legacy Feb 2026 CREED numbers without a fresh refresh.
- Do not let CREED duplicate CORAL’s Florida mandate or REGINALD’s bank-level mandate.
- CREED is canonical after Will-approved Phase 5; future topology changes still require Will approval.
- Use pathspec commits only.
