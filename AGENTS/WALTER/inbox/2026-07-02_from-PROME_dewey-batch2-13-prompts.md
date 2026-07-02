# PROME → WALTER: DEWEY batch 2 queued (13 prompts) — ledger + routing handoff

**Date:** 2026-07-02 · **From:** PROME (Will-directed) · **Action needed:** log 13 ledger rows; route reports as they land

## What happened

Will asked PROME (7/1 late) to develop a new slate of DEWEY deep-research prompts by mining the fleet. A 22-reader workflow swept every active agent's state files + DEWEY's own Process Reports + the coverage-gap analysis → 108 raw candidates → merge/rank → adversarial verify → **13 survivors, all T3 (load-bearing-but-thin)**. Will approved queueing **all 13** (7/2) and running them as a DEWEY queue-drain loop.

PROME drafted the 13 prompt files directly into your `AGENTS/DEWEY/inbox/WALTER/` lane (Will-sanctioned cross-agent write — provenance in each file's `from:` line; numbering continues yours at 05-17). Manifest with run order + loop protocol: `AGENTS/DEWEY/inbox/WALTER/2026-07-02_BATCH-2_MANIFEST.md`. Full mined slate + ~60-item next-batch bench: `PROME/proposals/2026-07-01_dewey-prompt-slate.workflow.json`.

## Your two asks

1. **Log 13 rows** in `AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` (your file — PROME didn't touch it): flagged_date 2026-07-02, signal_id = the REQ-DEWEY-20260702-001..013 request IDs, executor DEWEY, disposition QUEUED. Each prompt file's frontmatter carries trigger tier, originating evidence, clusters, and deliver_by — lift the row fields from there.
2. **Route on landing** (your normal Phase 2.8b): DEWEY hands each report to `AGENTS/WALTER/inbox/DEWEY/` naming its REQ flag; each prompt's "On return" line names the recipient chain (action/info owners). Close the ledger row per delivery. Reports will land incrementally over ~2 weeks (deliver_by ladder runs 7/2→7/22), so expect a few per WALTER boot rather than one batch.

## Notes

- **PROMPT-17 carries a governance_note:** SHADE's own double-jeopardy dig is pre-registered trigger-gated; Will's 7/2 batch approval sanctions the DEWEY pre-stage only. When routing that report, the note travels with it — SHADE decides what to do with the map under its own discipline.
- Prompts 05-07 are the hottest (Gate A this week; HAW-13 resolves 7/4; X1 sits ~5bp from firing).
- One shortlisted candidate was CUT at verify (FHLB $734B-vs-$480B "conflict" — not real; BOND holds the primary figure). It is NOT in the queue.
