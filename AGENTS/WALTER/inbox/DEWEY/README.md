# WALTER inbox — DEWEY lane

Create-only handoff lane for the **DEWEY** deep-research agent to return finished `/deep-research` deliverables to WALTER for routing (DEWEY revival Phase 2, 2026-06-20).

## Lifecycle (NEW → ROUTED → PROCESSED)
- **NEW** — DEWEY writes a create-only handoff file here (e.g. `YYYY-MM-DD_<topic>_handoff.md`), pointing at its `AGENTS/DEWEY/output/YYYY-MM-DD_<topic>.md` report + naming the originating WALTER Phase-2.8 flag ID (if any).
- **ROUTED** — WALTER scans this dir at boot (spawn-protocol step 7d), routes the report as ONE `research-output` BOARD signal per CHECKLIST Phase 2.8b (verbatim packet embed + per-recipient genuine-delta wrapper; **no verify-spawn → VERIFIED-PRIMARY**), and closes the originating `registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` row (`disposition: RESOLVED`, `executor: DEWEY`).
- **PROCESSED** — WALTER `git mv`s the handoff into `processed/`. The dir-move IS the state machine; it prevents the next boot-scan from repeat-routing.

## Ownership
- **DEWEY** only ever CREATES handoffs here — never edits one, never touches `processed/`.
- **WALTER** owns routing + the move to `processed/` (use `git mv`, not bash mv — per `[[feedback_git_mv_for_inbox_processing]]`).
- WALTER is the single entry point — DEWEY never routes to domain inboxes or BOARD directly.

Canonical: CHECKLIST Phase 2.8b + WALTER CLAUDE.md spawn-protocol step 7d. Mirrors the recipient-side `inbox/WALTER/` → `processed/` pattern from WALTER Routing v2 (here WALTER is the recipient of DEWEY's handoff).
