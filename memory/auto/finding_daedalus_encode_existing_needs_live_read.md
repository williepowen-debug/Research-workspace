---
name: finding_daedalus_encode_existing_needs_live_read
description: DAEDALUS "encode-existing handle" self-labels over-classify partial builds as pure lifts; read-verify each vs the live file before applying a batch
metadata:
  type: finding
---
DAEDALUS grades and proposes agent-doc "handles" from its cards/profiles, not always the live file at propose-time. Its "encode-existing-reasoning handle (additive, no new analysis)" self-label **systematically over-classifies partial builds as pure lifts** — the card sees the reasoning exists *somewhere* in prose but doesn't test whether lifting it into a table/column/section requires new synthesis.

BATCH_02 (2026-07-01): of ~13 proposed handles, only **3** were genuinely clean encode-existing applies (CARL BOTTOM LINE, BOND Independence column, HAWK FROZEN banner). Several self-labeled "encode-existing" items were actually builds or new judgments: REG-1 (a per-channel 1-5 score that "doesn't exist yet" per DAEDALUS's own card), REG-2 (a NEXUS_BRIEF that doesn't exist = net-new infra), and the net-new Independence / If-Falsified-ACTION columns for CARL/LABOR (the raw facts are in prose but the *independence conclusion* / *falsification action* is a new analytical call the owner must make).

**Why:** applying a "build" as if it were a mechanical lift means PROME (or DAEDALUS) fabricates analysis the owner should own — violating the encode-existing-only guardrail for cross-agent edits, and putting invented reasoning into a domain agent's canonical file.

**How to apply:** before applying any DAEDALUS handle batch, run a live-file read-verify per item (a fresh reader per target agent works well) answering: does the handle already exist? does the source reasoning genuinely exist AND does lifting it require zero new synthesis? Only APPLY the true lifts; TASK-PACKET the partial-builds/net-new to the owner; HOLD builds. See [[finding_re_derivation_surfaces_concept_failure]], [[project_daedalus_maturity_map_hygiene_input]].
