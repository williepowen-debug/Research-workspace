# From RAV: QC ledger and proposed intake workflow

**Date:** 2026-08-01
**To:** PROME
**From:** RAV
**Purpose:** Notify PROME of the new RAV QC ledger and expected intake workflow.

## What changed

RAV added two PROME-readable Codex/RAV surfaces:

- `PROME/codex/RAV_QC_LEDGER.md`
- `PROME/codex/RAV_QC_WORKFLOW.md`

The ledger records RAV review leads from the 7/31 evening closeout wave. The workflow defines the intended transmission chain:

RAV finds. PROME verifies and routes. Owners fix. PROME closes the RAV row. RAV can later audit whether closure propagated.

## PROME request

When Will directs you to consume RAV's QC handoff:

1. Open `PROME/codex/RAV_QC_LEDGER.md`.
2. Verify open rows against the current tree before treating them as true.
3. Assign owner/severity or reject/supersede each row.
4. Route owner packets where needed.
5. Write dispositions back to the ledger so the file does not become a stale backlog.

## Boundary

RAV did not edit agent-owned status files or trigger canon. The ledger is a review artifact, not an owner fix.
