---
name: project_public_prep_anthropic_fellows
description: repo being prepped public as portfolio for Will's Anthropic Fellows (Economics & Policy) application; Track A declutter DONE, Track B history-scrub PENDING (the go-public gate)
metadata:
  type: project
---

Will is prepping this repo to go public as the centerpiece portfolio artifact for his application to the **Anthropic Fellows Program — Economics & Policy** (The Anthropic Institute) — a 4-month research fellowship (greenhouse job 5183053008). Thread started 2026-06-30.

**Audience + framing (agreed):** reviewers value empirical rigor, calibration, null findings, fast implementation, and "translating research into actionable recommendations." Present the repo as a **multi-agent AI-orchestration system + a primary-source case study in AI-augmented economic knowledge work** — methodology forward, the trading objective demoted to "the testbed." Honest fit read: the repo aligns on *method/temperament*, NOT on the *AI-economic-effects subject* — bridge that gap with the reflective essay.

**Essay drafted:** `PROME/drafts/essay_conservation_of_cost.md` — thesis: *AI relocates (doesn't abolish) the costs of organizing knowledge work — coordination / verification / management / maintenance.* Grounded in the auto-memory findings corpus; hardened against an adversarial steelman (key reframes: "conservation-of-cost-under-redesign" not the unfalsifiable "relocates"; demote Coase to analogy; the safety payload = synthetic labor fails confidently + with fabricated provenance, so the human audit gate is a safety control). Will reviewing/editing — NOT final as of close.

**Key decision — CLEAN-IN-PLACE, not a fresh repo.** Reason: preserve the ~3,465-commit / 5-month longevity signal. Commit-history and current-tree-cleanliness are INDEPENDENT axes — removing files today does not erase the history of having had them. Keep the messy history; only scrub private/unprofessional content. Will's two real concerns: **(a) readable TODAY**, **(b) private/unprofessional OUT of history.** Transparent human (1879 williepowen) / agent (1446 Prome) commit split = a *feature* for this audience; do NOT re-attribute to inflate the contribution graph.

**Track A — readability today: DONE 2026-06-30.** git-rm clutter from the current tree (no history rewrite). 5,303 → ~3,920 tracked files (~26%). Cut: `/docs` OpenClaw vestiges (8), `dashboard/` web app + `TOOLS.md` (dead OpenClaw infra; server.py held a dead telegram token), pure junk (`_trash`/pycache/recovered), emptied every `processed/`+`delivered/` container (915 signals; KEPT the containers via `.gitkeep` per Will — "keep the concept, clear the churn"), 0-ref agent archives (~320). KEPT: referenced archives (`PROME/archive`, `AGENTS/_archive`, `FORGE/_archive`, `REGINALD/archive` etc.), `BOARD/` (live → route to WALTER to thin), `memory/` daily logs, current unprocessed inbox. README overhauled + fixed (markdown structure, dead `.clawhub/` citation → real Feb evidence, commit# rounded).

**Track B — history scrub: PENDING = the real go-public gate.** filter-repo (targeted — messy history is fine) to remove from ALL history: (i) OBJECTIVE — secrets (telegram tokens, Google OAuth `client_secret`, `.env`/keys) + private financial data (`WILL/trading-journal` broker photos [gone from tree, still in history], positions, broker details); (ii) SUBJECTIVE — "unprofessional" content (**Will must DEFINE the criteria**). Process: read-only inventory → manifest → Will-approval → ONE filter-repo pass → flip repo public. Do while repo still PRIVATE.

**Next session:** Track B inventory (offered), or essay revision after Will's edits. BOARD thinning → WALTER. Related: [[finding_passive_surface_rot_push_not_dashboard]] (why the dead infra rotted).
