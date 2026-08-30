---
name: spineaudit
description: Weekly PROME spine reconciliation — runs the 8-reader Workflow over the boot-read/protocol spine vs canon anchors, then the fix round and the STATUS stamp. Use when `PROME/STATUS.md` "Last spine audit" is >7 days old, when Will asks for a spine audit, or after a canon-moving ruling (root CLAUDE.md, ROSTER, GATES redesign).
user-invocable: true
---

# /spineaudit — weekly spine reconciliation (PROME)

1. **Check the stamp:** `grep -n 'Last spine audit' PROME/STATUS.md`. >7d or missing ⇒ run. On cadence ⇒ say so and stop unless Will asked.
2. **Run the Workflow:** `Workflow` tool with `scriptPath: PROME/tools/spine_audit.workflow.js` (8 readers / 15 files + the DOCKET >7d-PENDING anchor sampler). Go quiet while it runs; it returns blocking + minor findings per file.
3. **Triage** every finding at the artifact before fixing — a reader's flag is a prompt to LOOK (a "date drift" may be a correctly-labeled quote of a corrected error). Classify: BLOCKING (contradiction across spine files, dead fire-path pointer, stale ruling carried as live) vs minor (stamp ride-under, pointer drift, vintage rot).
4. **Fix round — delete-and-point over annotate-and-accrete.** PROME-lane fixes same session; Will-gated surfaces (root `CLAUDE.md` lines, `AGENTS.md` core) → ⚖️ WQ row, registered before the ask; owner-lane defects → packet to the owner, never edit their file. Prose catalysts found without a DOCKET row → verify at the owner, then register.
5. **Stamp:** STATUS header `Last spine audit: <date> (<n>th run — <readers>/<files>: <b> blocking [list] + ~<m> minors [classes]. Re-run when >7d.)`. The displaced stamp becomes ONE compact "Prior:" (run number · readers/files · blocking + minors count); the line carries the current audit + that one prior only — older stamps go verbatim into `PROME/archive/STATUS_SPINE_AUDIT_PRIORS_<from>_to_<to>.md` with an entry-crc32, and the line cites the file (retention changed from "last three" 2026-08-29, WQ-134 #1 — the priors paragraph had reached 6,263 B = 41% of a boot-read file).
6. **Commit** through `commit_check.py`, path-scoped; the message names the blocking finds and their fixes. The audit's own defect classes feed `PROME/proposals/` structure items when they recur (e.g. calendar-ahead-of-DOCKET ⇒ the generated calendar view).
