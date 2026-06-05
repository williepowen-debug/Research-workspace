---
name: finding_boot_closeout_hardening_recipe
description: "Phased recipe for hardening an agent's boot/closeout protocol — mirror, strip live-state, audit-produce doc-ownership + deferred punch-list"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 62753db2-b165-4faa-aec5-895d9bcf863f
---

Validated on OTTO 2026-06-02 (Will-directed, collaborative multi-phase). A repeatable recipe for hardening any agent's boot/closeout protocol; transferable to CARL/REGINALD/BROCK/HENRY.

**Phases (each one Will-drafted → agent-refined → applied, with a checkpoint between):**
1. **Boot rewrite** — `git pull` as step 0 (+blocked-pull fallback so it never stalls); PREDICTIONS scan flags due-in-7d AND passed-but-OPEN; **calendar past-due-catch** distinguishing *unswept* (a miss) from *acknowledged-pending* (clean carry); end on the action scan (freshest-in-context).
2. **Closeout = write-back mirror of boot** — explicit read→write pairing spine; **catalyst-sweep BEFORE prediction-resolve** (deliberate cross vs boot order, because catalyst outcomes feed prediction resolution). Closes the loop: what boot flags, closeout must resolve or re-arm-with-reason.
3a. **Strip live-state** from the instructions/CLAUDE file so the dashboard (STATUS) is single source of truth — durable framing + threshold *rules* stay; every current value/case-status goes. Label coarse single-metric triggers vs composite severity ("when they disagree, STATUS is operative").
3b. **Evidence & Hygiene Conventions** as a top-level section both boot & closeout reference: provenance tags `[CONF]/[PRESS]/[ALLEG]/[EST]` (`[ALLEG]` ≤40% weight per [[feedback_corrected_framing_calibration]]), `[STALE <date>]` composing orthogonally with provenance; **audit-produced Doc Ownership table**.

**Key moves that made it work:**
- **Audit-first, apply-second**: run the cross-doc audit to ground-truth before writing the ownership table — don't write a starter then re-edit.
- **Deferred punch-list**: the audit produces TWO outputs — the ownership table AND a stale punch-list (rotted/duplicated copies, ranked by *behavioral* impact, not line count). **Inventory now, fix content later** — keep the structural pass pure.
- **Dogfood immediately**: the new past-due-catch caught 3 unswept hearings on its first run; the closeout sweep resolved them same session.

Extends [[finding_closeout_as_writeback_tail]] and [[finding_boot_predictions_scan]] with the live-state-strip + audit-produced-ownership + deferred-punch-list method. Phase 4 (per-agent) = build a machine-readable `CATALYSTS.tsv` (SAM schema) and flip the boot calendar-scan to read it as primary.
