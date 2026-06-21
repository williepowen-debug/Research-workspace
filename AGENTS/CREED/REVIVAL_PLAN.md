# CREED REVIVAL PLAN

**Created:** 2026-06-21
**Owner:** Prome until CREED is bootable; CREED owns after revival.
**Status:** Phase 2 boot surface installed. Not yet live analytical truth.

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

Top-level `AGENTS/CREED/` is now bootable but not analytically current:
- `AGENTS/CREED/CLAUDE.md`
- `AGENTS/CREED/STATUS.md`
- `AGENTS/CREED/REVIVAL_PLAN.md`
- `AGENTS/CREED/inbox/2026-02-24_signals.md`
- no live refresh/workbook/research tree yet

The real legacy CREED body lives under REGINALD:
- `AGENTS/REGINALD/sub-agents/CREED/STATUS.md`
- `AGENTS/REGINALD/sub-agents/CREED/EXPECTED_SIGNALS.md`
- `AGENTS/REGINALD/sub-agents/CREED/workbook/`
- `AGENTS/REGINALD/sub-agents/CREED/research/`
- `AGENTS/REGINALD/sub-agents/CREED/sources/`
- `AGENTS/REGINALD/sub-agents/CREED/inbox/2026-02-27_office_reit_selloff.md`

Treat the REGINALD sub-agent tree as **source archive**, not current live truth.

---

## Legacy Thesis Snapshot — Do Not Trade From This Yet

Legacy CREED frame from Feb 2026:
- CRE stress is real and severe.
- Bank CRE can look healthier than CMBS because of mods, forbearance, FHLB liquidity, and delayed recognition.
- Office CMBS delinquency / special servicing and the maturity wall were the core signals.
- Employment was the key transmission trigger into broader bank loss recognition.

Revival must update this with current June data before making claims or recommendations.

---

## Inventory — Key Legacy Assets

### Top-level stale inbox

- `AGENTS/CREED/inbox/2026-02-24_signals.md`
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

Create a dated CREED research refresh.

Minimum refresh list:
- latest Trepp CMBS delinquency / special servicing by property type
- Morningstar/DBRS 2026 maturity wall and maturity-default outlook
- FDIC Q1 2026 CRE delinquency / PDNA
- office REIT / CMBS tape
- multifamily / Sunbelt stress
- bank mod/provision disclosures where relevant

### Phase 4 — Thesis + signal integration

Create/update current CREED thesis rails and optional coverage map.

Process stale inboxes only after fresh data refresh.

### Phase 5 — Topology integration

Only after Will approves top-level revival:
- update `AGENTS.md`
- update `AGENTS_DIRECTORY.md`
- update `AGENTS/_INDEX.md` / `AGENTS/_NETWORK.md` if needed
- add REGINALD/CORAL handoff notes if scoped

### Phase 6 — Optional migration

Only after CREED is bootable and topology is approved:
- decide whether to copy/move `AGENTS/REGINALD/sub-agents/CREED/` into a CREED legacy archive folder
- run grep/ref updates and verification before any move

---

## Guardrails

- Do not delete or move REGINALD sub-agent CREED files during revival Phase 1–4.
- Do not trade from legacy Feb 2026 CREED numbers without a fresh refresh.
- Do not let CREED duplicate CORAL’s Florida mandate or REGINALD’s bank-level mandate.
- Do not make CREED canonical in `AGENTS.md` until Will explicitly approves the topology change.
- Use pathspec commits only.
