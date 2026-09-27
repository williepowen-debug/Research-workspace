---
name: finding_parallel_agents_sharing_one_scratchpad_overwrite_each_others_files
description: parallel subagents pointed at ONE scratchpad clobber each other's generic working files (q.txt) and can read another company's filing silently; give each a filename prefix
symptoms: "my working file now contains a different company's 10-Q"; "figures don't match the filer"; two agents both using q.txt / t.txt / x.html
metadata:
  type: finding
---

On 2026-09-26 REGINALD launched three read-only research agents in parallel (FLG, EGBN and OZK loss inputs). Each prompt named its OUTPUT file in the parent's scratchpad (`q2_FLG.md` etc.) but said nothing about WORKING files. The FLG agent's `scratchpad/q.txt` was overwritten mid-run by the EGBN agent's download of EGBN's 10-Q. The FLG agent noticed only because the text named the wrong filer. It re-extracted, and REGINALD then made the still-running EGBN agent re-fetch into `egbn_*` files and re-verify 48 figures by CIK and company name.

**Why:** a subagent treats the scratchpad it was given as its own. Short generic names (`q.txt`, `t.txt`, `page.html`) are what every agent reaches for, so N agents in one directory race on the same names. **The failure is silent:** a bank 10-Q parses fine whichever bank it belongs to.

**How to apply:** preferred fix: give each concurrent worker its OWN scratch path (e.g. `scratchpad/<ticker>/`), which removes the overwrite mechanism entirely. Minimum fix when spawning parallel agents into a shared scratchpad: put a line in EVERY prompt: "use only working files prefixed `<ticker>_`; confirm the filer name/CIK inside any document before extracting figures from it." If a collision is discovered mid-run, message the still-running agents immediately with the same instruction and ask them to state which figures they re-verified. Related: [[finding_workflow_scratch_crash_recovery]] (the same scratch dirs, a different failure).

⚠️ **The EGBN agent's 48-figure re-check is RECOVERY evidence, not proof that the collision was harmless** (CATO, 9/26): it shows the figures it re-checked, nothing more.
