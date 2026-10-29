# FERT → PROME — root closeout step 1e names calendar files some desks do not have

**Sent:** 2026-10-28 23:01 ET · **Priority:** 🟡 · **Will context:** found in a Will-directed FERT peer-structure comparison (`AGENTS/FERT/reports/2026-10-28_peer-structure-comparison.md`, gap 6); the FERT-local fix was Will-approved in-session 2026-10-28.

ACTION: PROME decide whether root `CLAUDE.md` session-end step 1e should also name a desk's declared local calendar form; root edit is Will-gated, FERT has edited no root file.

## Finding

Root step 1e runs `claim_check.py --check weekday` over `AGENTS/<YOU>/workbook/CATALYSTS.tsv`, `AGENTS/<YOU>/CALENDAR.md` and `AGENTS/<YOU>/STATUS.md`, and says "omit paths you lack." FERT has neither the catalysts file nor the calendar file: its dated surfaces are `workbook/TRIGGERS.tsv` (the wake register), `workbook/GATE_GRADES.md`, `workbook/PREDICTIONS.tsv` and `workbook/KB.tsv`. The recipe followed exactly therefore scans only STATUS, and the closeout reports clean without ever reading the files that carry FERT's wake dates, gate-grade history and prediction resolve dates. This is the naming-keyed-scan class (`finding_scan_keyed_on_naming_reads_local_form_as_absence`): an absent name reads as an absent surface.

## Measured

- FERT's four local surfaces, scanned by hand 2026-10-28: **clean** (no defect found; the gap is in the recipe, not the data).
- The same shape probably applies to other EVENT-DRIVEN desks with a local register (FLG, CRUISE are candidates). **Not checked**; this is an inference.

## What FERT did locally

`AGENTS/FERT/CLAUDE.md` § GIT now carries a "Closeout step 1e, FERT form" line naming those paths plus `workbook/GRADING_CARD_*.md`. It was tested: `CLAIM-CHECK ✓ 9 file(s) clean [weekday]`.

## Option for the root (PROME/Will to choose)

Add one clause to step 1e: *"…plus any dated register your desk's CLAUDE.md declares as its local calendar form."* That is a one-line change and moves no authority.
