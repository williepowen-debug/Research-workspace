---
name: finding_deliberate_and_unnoticed_asymmetry_look_identical
description: Read the stated rationale before flagging a structural oddity — a deliberately-accepted design and an unnoticed defect are byte-for-byte identical in the artifact
metadata:
  type: feedback
---

From the condition/artifact **alone**, a **deliberately-accepted** asymmetry and an **unnoticed** one are byte-for-byte identical. The rationale is the only discriminator, and it never lives *inside* the thing being screened — it lives on the adjacent line, if the author wrote it.

**Why:** DAEDALUS's 2026-07-30 compound-gate screen ran on grep context (the gate line ± a few chars) and produced 4 candidates. Reading each candidate's surrounding text moved **3 of 4 verdicts** — one *up* to the strongest finding in the set, two *down to cleared*. Both downgrades had the same cause: the designer had already seen the asymmetry, reasoned about it in writing one line away, and chosen it (OSPREY `CLAUDE.md:145` "a strike-pause alone is see-saw noise"; TERRY `PAPER_BOOK_DESIGN.md:35` "row-count is the easy number to reach and the misleading one"). Skipping that read turns a cheap structural screen into a **false-positive generator aimed precisely at the agents who document their reasoning best** — it punishes the good behaviour, and any *mechanized* version of the check ships with that failure mode by default.

**How to apply:** when screening structurally (grep-driven audits, conformance passes, pattern sweeps), never flag off the matched line — read the surrounding rationale first. **A construct with a written justification beside it is presumed deliberate until that justification is shown wrong.** Two corollaries: (1) when you withdraw a flag, *tell the owner you withdrew it and why* — it confirms their rationale is load-bearing and readable; (2) the inverse case is unfixable this way — **an ABSENT row leaves no rationale to read**, so deliberate silence and blind silence cannot be told apart unless the exclusion is written down explicitly (see [[finding_scope_negative_needs_the_counterparty_standard]]).

Related: [[finding_comprehensive_grep_over_sampling]], [[finding_read_the_artifacts_own_header_first]], [[finding_triage_summary_compression_inversion]].
