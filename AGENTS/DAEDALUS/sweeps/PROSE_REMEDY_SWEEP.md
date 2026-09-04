# Prose-Remedy Census — playbook (H-4, `BLUEPRINTS/DESK_HARDENING_PATTERNS.md`)

**Registry row:** `sweeps/REGISTRY.tsv` "Prose-Remedy Census" (21d; `resolve_by` 2026-09-25 for run #1). **Commission:** PROME packet 2026-09-04 16:5x (Will-directed), deliverable ②. **Canon this sweep enforces:** H-4 — a remedy carried as prose for ≥2 sessions is a defect of the class it describes; the remaining cost is the hour of typing. **Run #0 (the evidence):** VIOLET 2026-09-04, five remedies carried 2 days to 7 weeks, all typed in one pass (`ec5d05b69`, KB-VIO-240) — and one of the five typed wrong (`717c8f9a0` #1), which is why step 3 exists.

## When to run
Every 21d, or on demand after a desk reports a boot warning it has read and not actioned twice. Run #1 by **2026-09-25**.

## Perimeter (self-inclusion: DAEDALUS IN scope)
Per desk in `PROME/ROSTER.md` ACTIVE + TIER-2 + SPECIAL: `STATUS.md` · `SCRATCH.md` · `CANARY_MAP.md` · `MAINTENANCE.md` · `LAST_COMPLETION.md` (whichever exist) plus the desk's `CLAUDE.md` boot/closeout steps. Inbox packets are OUT of the mechanical leg (a peer's remedy is the owner's to carry, and appears on the owner's surface once carried).

## Procedure
### 1. Candidate list (mechanical, read-only; a generator, not a verdict)
Lines that name a script (`\b[\w-]+\.py\b`) AND carry a remedy/queue token (`queued|owed|not yet (built|wired)|unbuilt|un-wired|BUILT-UNWIRED|fix pending|should (be|compute|check|compare)|needs? (a|an|to)|TODO|remedy|as a sentence|as prose|not a check|never computed|nothing (checks|computes|compares)`). Run the pattern in Python, not ugrep (CHECK_STANDARD §14 box fact). **Base rate 2026-09-04 at registration (CHECK_STANDARD §12):** 55 lines / 22 desks; the exemplar per desk was FALSE on most desks (DONE lines, unrelated table cells); positive control = VIOLET's three 9/4 fixes, 3/3 hit. Expect a majority-false list; the count is the ceiling, not the finding.
Add the second, cheaper form: a `CLAUDE.md` boot or closeout step written as a comparison, count, or threshold (`≥`, `>=`, `≤`, `must not lag`, `N consecutive`, `under N lines/bytes`) with no script named on the same line and none in the desk's `scripts/` computing it. VIOLET's founding instance (Amendment 10 as a sentence for 31 days) is this form and the step-1 grep cannot see it.

### 2. Classify each candidate (judgment, per row)
`PROSE-REMEDY` — the fix is specified on the surface (what to compute, against what, failure direction) and no code computes it; carried ≥2 sessions by the surface's own dates · `DIAGNOSIS-ONLY` — the surface names a defect without a remedy (a different queue; note, do not count) · `BUILT` — code exists; the line is a stale claim (route to the owner as an H-1 stamp-over-body instance) · `DECLINED-BY-DESIGN` — the owner has written why it stays prose (VIOLET `thesis_bump_check` "advisory, never blocks" is the model; accept, never re-flag) · `FALSE` — grep noise.

### 3. The half the census cannot see, stated in every record
Typing the prose proves the remedy exists, not that it is right. Each `PROSE-REMEDY` row the owner builds ships under H-6: a selftest that reproduces the known defect, the premise verified at the publisher, rc read bare. The record carries the sentence *"n rows typed; premise-verified at the source for m of n"* — never "n fixed."

### 4. Disposition & authority
Detection read-only. Dispositions are TASK-PACKET-ONLY to the owner (the remedy is the owner's code; STRICT_TEXT on the ACTION line: the surface line, the carry age in sessions, the classification token). No pre-approval class; no cross-desk edits. A desk whose list is empty gets no packet and one line in the record (the perimeter clean line, §2 of CHECK_STANDARD).

### 5. Record
`runs/<date>_PROSE_REMEDY_CENSUS_<n>.md` — perimeter · candidate count per desk · classified rows with the surface line quoted · the step-3 sentence · packets sent · the false-positive rate of step 1 (feeds the next refinement of the token list, never a widening without a fleet before/after diff). Then registry row `last_run` + `last_findings` → this Run Log.

## Verdict tokens (STATE_VOCABULARY)
Per row: `PROSE-REMEDY (<sessions carried>)` · `DIAGNOSIS-ONLY` · `BUILT` · `DECLINED-BY-DESIGN` · `FALSE`. Per desk: `CLEAN (<candidates read>)` · `NOT READ (<reason>)` — an unread desk is never `CLEAN`.

## Run Log
| Run | Date | Perimeter | PROSE-REMEDY rows | Packets | Record |
|---|---|---|---|---|---|
| #0 | 2026-09-04 | VIOLET only (owner self-run, the founding evidence) | 5 typed, 1 premise-wrong on external review | — | `AGENTS/VIOLET/workbook/KB.tsv` KB-VIO-240, KB-VIO-242 |
