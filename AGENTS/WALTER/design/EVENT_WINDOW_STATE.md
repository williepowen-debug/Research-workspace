# EVENT_WINDOW_STATE — Retired burst-window procedure

**Status:** RETIRED — Will approved October 31, 2026 in the WALTER session (“ok go ahead”).
**Final declared state:** `CLOSED`. No OPEN window was recorded.

The legacy oil/Hormuz BURST_WINDOW procedure is retired. No boot read, activation or verification-gate check, blanket FLASH override, daily roll-up, closing summary or stale-OPEN check remains. Boot step 7b and CHECKLIST Phase 2.5 are tombstones. This file is historical reference only; neither WALTER nor BRENT should declare a new window here.

Normal per-signal precedence, System-Critical FLASH bypass and verify-research rules continue under SIGNAL_FORMAT_SPEC, FILTER_SPEC and CHECKLIST. BRENT owns current Path-A/Path-B evidence and grades; its thesis closes BRT-08/09/21 and names BRT-31 as the successor demand test. Retirement does not map BRT-31 into the old activation formula or create a replacement window.

The optional `event_window` enum remains readable for historical signals; new signals omit it or use `closed` per SIGNAL_FORMAT_SPEC. Historical `open` never activates a current override.

Full pre-retirement procedure: git `b55973ce36f8ae09cb59217b04f2966097b69bc4:AGENTS/WALTER/design/EVENT_WINDOW_STATE.md`. Decision, implementation and validation: `research/2026-10-31_burst-window-retirement/REVIEW.md` (relative to WALTER). The following original logs are preserved as historical evidence, not an active watch or cumulative trigger count.

## State Transition Log (append-only)

*Records actual state transitions only (CLOSED ↔ OPEN ↔ PENDING_VERIFICATION). Trigger fires that do not cross the OPEN threshold are recorded in the "Pre-OPEN trigger fire log" section below.*

| Date | From | To | Declared by | Trigger | Expected close | Outcome |
|------|------|-----|-------------|---------|----------------|---------|
| 2026-05-08 | — | CLOSED (initial) | WALTER | Scaffold create per JOINT_PROPOSAL §2d Will sign-off | n/a | n/a — initial state |

## Pre-OPEN trigger fire log (Path B / Path A observability)

*Records individual Path B (3-trigger) or Path A (4-criteria) fires that have not yet crossed the OPEN-declaration threshold (≥2/3 Path B OR 4/4 Path A). Recorded for observability + cumulative count tracking; do NOT cause state transitions on their own.*

| Date | Trigger | Detail | Path B count after | Recorded by |
|------|---------|--------|--------------------|-------------|
| 2026-05-15 | Path B Trigger #3 (CFTC MM positioning) | Brent CFTC Managed Money net longs 70,791 (week of May 5) — down 29K from 99,887 peak over 2 weeks at Brent $106-111 distribution; large-spec distribution underway per BRENT thesis v2.0 + commits `ad9d29fb` (Friday data refresh) + `3ef8d916` (SIGNALS.md cross-agent alert) | 1/3 | BRENT (entered into log by WALTER 5/21 closeout) |
