# AGENTS/DEWEY/inbox/WALTER/ — WALTER → DEWEY deep-research request lane

**Create-only request queue.** WALTER drops ready-to-run `/deep-research` prompts here (one file per prompt) when Will approves a Phase-2.8 deep-research flag. The symmetric counterpart to `AGENTS/WALTER/inbox/DEWEY/` (where DEWEY hands finished reports back to WALTER).

**Lifecycle (mirror of the DEWEY→WALTER lane):**
- **NEW** — WALTER creates `DEEP-RESEARCH-PROMPT-N-<slug>.md`; each file is a self-contained prompt + originating Phase-2.8 flag context (clarifiers pre-answered → paste-and-go).
- **RUN** — Will opens a DEWEY session and runs the prompt(s); DEWEY follows its boot step 4 ("read the question/prompt Will gave you").
- **PROCESSED** — after DEWEY delivers (hands the report back via `AGENTS/WALTER/inbox/DEWEY/`), the consumed request moves to `processed/`.

**Rules:** WALTER only ever CREATES here; DEWEY/Will move to `processed/` on consume. The matching `AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv` row (WALTER-owned) tracks disposition; WALTER closes it when the report returns (CHECKLIST Phase 2.8b).

*Created 2026-06-27 — first WALTER→DEWEY queued batch (3 prompts, Will-approved). DEWEY boot does not yet auto-scan this lane; Will points DEWEY here ("run your inbox/WALTER/ prompts") until/unless a boot-step is added to DEWEY's CLAUDE.md.*
