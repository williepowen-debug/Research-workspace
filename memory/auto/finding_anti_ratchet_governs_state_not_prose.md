---
name: finding_anti_ratchet_governs_state_not_prose
description: "An anti-accumulation rule that counts scripts/checks/rows does not count WORDS — so specs get replaced while the prose ABOUT each replacement accumulates in the operating doc. Split what to DO from why it says so, and measure the doc in bytes, not rule count."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 820ff136-af2b-4816-8675-107e0094d840
  modified: 2026-08-05T23:56:49.822Z
---

**A retirement/anti-ratchet rule governs the things it can count.** Ours counted scripts, checks and registry rows and said nothing about prose — so **every incident still deposited a dated *"here is what was wrong and why"* block into the OPERATING doc**, each individually justified, until the instructions were a minority of the instruction file.

**★ THE MECHANISM: SPECS GET REPLACED; THE PROSE ABOUT THE REPLACEMENT ACCUMULATES.** A superseded threshold is genuinely deleted. The paragraph explaining why it was superseded is *added*, and nothing ever removes it — because removing it feels like erasing hard-won history. So the rule-count goes flat or down while the file grows.

**The case (BRENT, 2026-08-05).** A consolidation pilot's stated goal was *"flatten human boot."* It succeeded on the metric it chose — steps 31 → 24 — while the boot doc **grew 243 → 252 lines / 36.9 → 38.9 KB**, and the BOOT section carried **9 human actions against 18 lines of rationale prose**. Hot context across five boot-read files measured **317 KB**, of which **286 lines carried a date** and **66 carried RETIRED/SUPERSEDED/CORRECTED/DEFECT**. The anti-ratchet rule had been adopted the day before *specifically to oppose accumulation* — and every change since had been an addition, including the rule's own explanatory block.

**The remedy: split the OPERATING doc (what to do) from the DECISION RECORD (why it says so).** Nothing is deleted — it is moved out of hot context. Result: boot doc **−22% bytes**, below its own pre-pilot baseline for the first time, with **human actions unchanged**.

**⚠️ THE DANGEROUS PART, and it is where this goes wrong: DO NOT SWEEP BY "HAS A DATE."** Some dated blocks are **binding constraints**, not history — limits a principal ruled must travel *on* the live spec, caveats adopted onto a gate. Moving those is worse than leaving the bloat, because the spec then looks clean and has quietly lost a guard.
**The discriminator: does this block CONSTRAIN A FUTURE ACTION (stays) or RECORD A PAST ONE (moves)?**

**How to apply:**
- **Measure the doc, not the rule count.** Bytes and the ratio of imperative lines to rationale lines. A "we removed a check" claim is not evidence the surface shrank — check the file size before and after.
- **When you write an anti-accumulation rule, say explicitly whether it binds PROSE.** If it doesn't, it will be cited as protection while the thing it doesn't cover grows.
- **Extract binding rules OUT of their rationale blocks** into a standing-rules section, so they read as constraints rather than as the moral of a story. A rule buried in a war story is easy to skim past.
- **A spec and its live reading must not share a home** — a state table inside a spec block rots invisibly (ours asserted a six-day-old gate reading inside the gate spec).
- **Prefer merging versions over stacking them.** A spec written as a *delta* on its predecessor ("v2 stands except…") forces every reader to apply a patch mentally; fold it into one self-contained spec and move the lineage to the record.
- **The record file must never acquire an instruction.** If you write "always do X" there, X belongs in the operating doc.
- Related: [[finding_ownership_claim_is_last_to_move]] (the same refactor's other half — the pointer is last to move), [[finding_mechanize_the_cap_not_the_ritual]], [[finding_banner_is_a_warning_not_a_fix]], [[finding_governance_doc_stale_default_drift]], [[finding_retired_threshold_has_no_publisher]].
