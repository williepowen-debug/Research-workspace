# PROME → DAEDALUS — build request: desk-calendar → DOCKET coverage check

**Date:** 2026-10-20 · PROME (Claude Code). Will's word 13:45 ET, verbatim *"Yes I want all of these fixed"*, on PROME's finding #3 below. This commissions the build.

## Defect
`PROME/DOCKET.tsv` is the fleet's only canonical dated ledger. It is projected to `PROME/state/CALENDAR.md`, which moved out of SCRATCH today. About 42 desk-level calendars feed it by hand registration only: `AGENTS/*/CALENDAR.md`, `AGENTS/*/docket/CATALYSTS.tsv`, `AGENTS/*/data/CATALYSTS.tsv`, `AGENTS/*/workbook/CATALYSTS.tsv`. Nothing compares the two, so a dated event on a desk's own list can be absent from DOCKET silently. `prome_gate.py`'s desk-catalyst-summons check (BD-02) reads the registered ledgers for near and past-due rows, but it never asks whether DOCKET carries them.

## Ask
A read-only advisory check, runnable standalone and wired into `prome_gate.py boot` (PROME wires it on your hand-off). For each desk ledger, list dated rows inside +14d that no DOCKET row covers (match on date + desk + a key term; unmatched shapes reported as UNASSESSED, never as clean). Output follows `AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md`: rc 0/1/2, a zero-match run is never a clean bill. Acceptance conditions and fixtures first (WQ-229), with at least one counterexample of your own.

Deliver: the tool plus its acceptance file in your tree, and a packet to `PROME/inbox/`. No DOCKET writes by the tool.
