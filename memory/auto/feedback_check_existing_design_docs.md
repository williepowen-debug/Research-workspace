---
name: Check for Existing Design Docs Before Writing New Ones
description: Before drafting a new design/spec/checklist file, search the agent's design folder for existing versions — past sessions may have already done the work
type: feedback
originSessionId: 95eb2b13-10a6-4aa9-8a80-58a9f1561f8f
---
Before writing a new design document, spec, or operational checklist, search the relevant design folder for existing versions. Past Claude sessions may have already produced the work, and writing a new file from scratch creates fragmentation and contradictions between specs.

**Why:** On 2026-04-10 I almost overwrote SIGNAL_PROCESSING_CHECKLIST.md by writing a new file from scratch — a checklist already existed from April 7 that incorporated most of what I was about to write. The Write tool's safety check (file already exists, must Read first) caught it. Without that check I would have lost past-me's work.

The deeper failure: I had ALL the relevant info to know it existed. I had read the WALTER CLAUDE.md earlier in the same session and seen the design docs listed. I just didn't check before drafting. The pattern of "draft first, check what exists later" wastes effort and creates spec divergence.

**How to apply:**
- Before writing a new design doc, run `Bash ls AGENTS/<agent>/design/` or Glob for likely filenames first.
- If a file with a similar name exists, READ it before writing. Decide whether to extend, supersede, or leave alone.
- Specifically for WALTER: design/ contains SIGNAL_FORMAT_SPEC, FILTER_SPEC, ROUTING_TABLE, SIGNAL_PROCESSING_CHECKLIST, SIGNAL_REGISTRY_DRAFT_A, COP_TEMPLATE, SIGNAL_INTAKE_TEMPLATE. Always check this folder first.
- Same principle applies to any agent's design/spec/research folders.
- This ALSO catches divergence between specs: when you read existing docs, you discover where they contradict each other (which is its own important finding).
