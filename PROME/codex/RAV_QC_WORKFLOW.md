# RAV QC Workflow

**Created:** 2026-08-01
**Owner:** PROME for intake; RAV for finding production
**Status:** Proposed standing workflow
**Related:** `PROME/codex/RAV_QC_LEDGER.md`

## Purpose

This file defines how detached RAV QC findings should move into the Research-workspace without making RAV a hidden production coordinator or cross-agent editor.

## Doctrine

RAV finds. PROME verifies and routes. Owners fix. PROME closes the RAV row. RAV can later audit whether closure propagated.

RAV findings are review leads until PROME checks the current tree. Cross-vendor/detached review is valuable because it catches different failure modes, not because it is automatically correct.

## Transmission Chain

1. **RAV observes from the mirror.** RAV refreshes the read-only mirror, inspects the current repo state, and records exactly what was and was not checked.
2. **RAV records durable findings.** Small reviews go directly into `PROME/codex/RAV_QC_LEDGER.md`. Larger reviews get a dated detail report under `PROME/codex/findings/` and a linked ledger row.
3. **PROME verifies.** PROME checks each open RAV row against the live tree before acting on it.
4. **PROME routes or rejects.** If real, PROME assigns owner/severity and routes a packet or queue item. If false/stale/non-actionable, PROME marks the row rejected or superseded.
5. **Owners fix their own surfaces.** WALTER fixes WALTER, SAM fixes SAM, ORACLE fixes ORACLE, and so on. RAV should not bypass owner ownership unless Will explicitly scopes that edit.
6. **PROME closes the row.** Closeout requires a disposition and evidence: fixed artifact, routed packet, explicit rejection reason, or superseding commit/state.
7. **RAV can re-audit closure.** On a later mirror refresh, RAV may check whether accepted/routed issues actually propagated to consumer-read surfaces.

## Ledger Contract

Stable IDs:

`RAV-QC-YYYYMMDD-NNN`

Recommended columns:

`ID | Severity | Status | Owner | Surface | Concern | Suggested next action | Disposition`

Statuses:

- `Open`: RAV logged it; PROME has not dispositioned it.
- `Accepted`: PROME verified the issue and accepted it as real.
- `Routed`: PROME sent it to an owner or queue.
- `Fixed`: Owner/PROME fixed it and the artifact was verified.
- `Rejected`: PROME checked and found the issue false or non-actionable.
- `Superseded`: Later repo state made the row obsolete.
- `Watch`: Not actionable yet, but worth checking again.

Severity should reflect operational risk, not novelty.

## PROME Intake Expectations

When Will points PROME at the RAV ledger, PROME should:

1. Open `PROME/codex/RAV_QC_LEDGER.md`.
2. Scan open rows by severity.
3. Verify each candidate against the current tree.
4. Add disposition notes to the ledger or route owner packets.
5. Carry unresolved accepted rows into PROME's normal queue only if they have a clear owner and close condition.

Do not let RAV rows become free-floating prose. Each surviving row needs an owner, a status, and a close condition.

## RAV Boundaries

RAV should not directly edit agent-owned surfaces, shared trigger canon, or live coordination state as a shortcut to fixing its own findings. The default RAV deliverable is evidence plus a reproducible concern.

RAV may use the Research-workspace edit lane to add RAV-owned QC artifacts under `PROME/codex/` and, when useful, PROME inbox packets that point to those artifacts.

## Real-World Analogue

This mirrors QA/red-team triage in engineering teams:

- Finding source: QA/red team reports a suspected issue with evidence.
- Triage owner: tech lead or incident commander verifies, prioritizes, and assigns.
- Fix owner: service/domain owner changes the controlled surface.
- Tracker: issue log records status and close condition.

The main failure mode is not a bad finding. It is a good finding with no owner, no status, and no close condition.
