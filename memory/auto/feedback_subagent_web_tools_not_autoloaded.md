---
name: subagent-web-tools-not-autoloaded
description: "General-purpose research sub-agents may spawn WITHOUT WebSearch/WebFetch loaded, silently returning no data on web-dependent tasks; confirm tooling in the prompt or do the lookup in-session"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 100558f6-d8df-4075-804f-2f8e2484343f
---

A spawned general-purpose sub-agent can come up without web tools (WebSearch/WebFetch) available, and it will **fail silently** — returning "no data found" rather than erroring, which reads like a genuine negative result. On any task whose answer requires live web/docket/filing lookup, an empty return is ambiguous: real absence, or tools-not-loaded?

**Why:** A First Brands docket lookup delegated to a sub-agent returned no data — not because the docket was empty, but because the sub-agent had no web tools loaded. The empty return nearly got read as "nothing filed."

**How to apply:** When a sub-agent task depends on web work, either (a) state the tool requirement explicitly in the prompt and have the agent confirm it can search before concluding, or (b) do the lookup in-session rather than delegating. Treat an empty/negative web result from a sub-agent as *unverified* until you know its tools were live — re-run in-session before banking a "nothing found." Related: [[feedback_subagent_prompt_discipline]]. Transferable to any agent that spawns research sub-agents.
