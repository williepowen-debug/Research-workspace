---
name: finding_deep_research_slate_mining
description: "Build deep-research prompt slates by mining agents' SELF-flagged gaps, then adversarial-verify each candidate (already-answered / cheap-verify / decision-real / primaries-exist) — expect survivors to concentrate in load-bearing-but-thin"
metadata: 
  node_type: memory
  type: project
  originSessionId: f5921104-0f87-443b-8cbe-4551e18336b0
---

Pattern for generating a DEWEY deep-research batch (first run 2026-07-01: 22 miners → 108 raw → 13 survivors, 0 data errors found on spot-audit).

**Why:** gaps inferred from outside an agent's domain are usually wrong or already covered; gaps the agent ITSELF flagged ("unverified", "structurally unavailable", "WAITING-FOR", stale falsifier) come pre-attached to a real decision consumer. And a merge/rank pass alone over-keeps: adversarial verify killed a shortlisted "figure conflict" that wasn't one (BOND already held the primary figure — [[finding_verify_state_before_propagating]]-class).

**How to apply:** (1) One reader per active agent + one over the deep-research agent's own past Process Reports (prior reports name their own follow-ups) + one over coverage-gap/coordination docs. Mine self-flagged gaps ONLY; require verbatim gap evidence + file path. (2) Barrier-merge across all miners — independent convergence on the same question is a ranking signal (Hormuz drew 4 miners). (3) Per-survivor adversarial verify with repo access: already answered in-repo? one-lookup cheap? does the named decision exist and move? do public primaries plausibly exist? Default CUT. (4) Expect survivors to be T3 load-bearing-but-thin — the mature-fleet research debt is unverified numbers under live triggers, not missing coverage; write prompts that carry decision consumers + deliver-by dates keyed to the docket. Keep the dropped bench (merge notes preserve "next batch" reasons). Instance: `PROME/proposals/2026-07-01_dewey-prompt-slate.workflow.json`.

Related: [[finding_thesis_loadbearing_sweep_scope]], [[feedback_subagent_prompt_discipline]].
