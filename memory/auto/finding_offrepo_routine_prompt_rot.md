---
name: finding_offrepo_routine_prompt_rot
description: "Cloud-routine prompt text lives off-repo — invisible to greps, it rots past every repo-side fix; mirror it in a registry and make prompts read thresholds from repo surfaces at run time"
metadata: 
  node_type: memory
  type: project
  originSessionId: 931643fb-5ecf-4786-96ef-513c83deb9c9
  modified: 2026-08-04T01:45:09.661Z
---

**The class (found 2026-08-03):** scheduled cloud routines (claude.ai/code/routines) store their prompt text **server-side, outside the repo** — so a dead path, stale threshold, or retired thesis frame baked into a routine prompt survives every repo-side correction and is invisible to `grep`. Two live instances the same day: VULCAN's routines carried the dead `AGENTS/PROME/inbox/` path through two repo-side flags (its own diagnosis — "the surface my autonomous runs read is not in the repo at all"), and BRENT's three live weekly routines (created 4/6) were still running **April-vintage alert arithmetic** in August — "rig trough ~553" against a registered 457 line, retired Phase-B triggers, pre-canon bare `git push` — fired weekly with no human watching.

**Why:** the failure is structural, not negligence — every fleet hygiene mechanism (staleness checks, spine audits, consumer checks, greps) scans FILES. An off-repo prompt is a consumer-read surface with no file.

**How to apply (the two-part fix, both shipped 8/3):**
1. **Registry mirror:** every agent with routines keeps `AGENTS/<NAME>/SCHEDULED_RUNS.md` — routine IDs, crons, model, prompt vintage, design contract. Rule: prompt change and registry row update in the same pass. Creation includes a registry row.
2. **Thresholds live in files, not prompts:** routine prompts must NOT carry alert levels — they read the agent's STATUS/TRACKER registered lines **at run time** ("files win on drift" written into the prompt). A prompt that holds no thresholds cannot rot them. Corollary the design creates: the pointed-at surface becomes the single point of truth, so **a line missing there is a line no routine watches** — owner must verify coverage.

Mechanics: enumerate/update from a session via `RemoteTrigger` (`{action:"list"}` shows full prompt text; update requires the FULL `job_config.ccr` object — partial replaces whole). Deletion is web-UI-only. Standing check: quarterly routine-prompt audit on PROME/DOCKET (first 2026-11-03).

Related: [[finding_dead_path_regrows_unless_senders_repointed]] · [[finding_governance_doc_stale_default_drift]] · [[finding_mechanize_the_cap_not_the_ritual]]
