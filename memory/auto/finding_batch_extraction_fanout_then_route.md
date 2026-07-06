---
name: finding-batch-extraction-fanout-then-route
description: "For a large image/document batch (dozens+), split OCR/extraction (mechanical, parallelizable, cheap model) from judgment (dedup/filter/route/verify — the owner keeps this). Fan out N sub-agents to TRANSCRIBE chunks in parallel, then the owner routes on the structured extractions. Keeps fidelity where it matters, keeps the owner's context clean, and is a live instance of role-separation (LOOPS.md Rule 2)."
metadata:
  node_type: memory
  type: finding
  originSessionId: d9a79aa6-b7ad-4507-a82f-87ec36f35f50
---

When a bulk visual batch lands (WALTER processed a **47-image** desktop drop 2026-07-06), do NOT read it all in one context and do NOT delegate the routing. **Split the two layers:**

- **Extraction (fan out):** chunk the set (~8 per agent), spawn parallel sub-agents on a **cheap model** (Sonnet) whose ONLY job is to faithfully TRANSCRIBE each image — source, date, headline, every number/ticker, chart trend + annotated values — into a fixed structured record. No routing, no filtering, no judgment. This is mechanical, parallelizes cleanly (6 agents × ~8 images returned complete extractions in ~90s), and keeps the owner's context clean.
- **Judgment (keep):** the owner (WALTER) then does dedup (vs the archive + intra-batch), filter, verify load-bearing/extraordinary claims against primaries, decide precedence + recipient, and dispatch — on the structured *text*, re-reading only the handful that survive to dispatch.

**Why it works:** extraction is where a cheap model is fine and parallelism pays; routing/framing is where the owner's judgment is the whole value, so it stays un-delegated. This is exactly LOOPS.md Rule 2 (separate the roles — planner/generator/evaluator in separate context windows; mixing them produces slop) applied to signal intake. The extraction agents are the "generator," the owner is the "evaluator."

**Pre-dedup before you even extract:** drop obvious duplicate FILES first. iPhone drops carry `IMG_E####` *edited* copies alongside the base `IMG_####` — these are re-crops of the same content (verified: `IMG_E1445` == `IMG_1445`). Dropping the 10 E-variants took 57 files → 47 unique before spawning, saving 10 reads. (Telegram's version is file-id-stem dedup, `[[finding]]` image-batch dedup.)

**Checkpoint on the first run of a new method / large commit:** 47 images yielded ~15 dispatch candidates = a big durable write. Present a triage table (dispatch / kill / hold, with reasons) for a go/prune before committing dozens of BOARD files. After the operator confirms the bar, run end-to-end autonomously.

Related: [[project-walter-image-signal-intake]] (WALTER = image-capable intake), [[finding-gitignored-private-drop-boot-surfaced]] (the drop-zone that fed this), [[feedback-parallel-spawn-independent-agents]] (spawn independent work concurrently in one message), [[feedback-subagent-prompt-discipline]] (tight extraction-only prompt), [[finding-triage-summary-compression-inversion]].
