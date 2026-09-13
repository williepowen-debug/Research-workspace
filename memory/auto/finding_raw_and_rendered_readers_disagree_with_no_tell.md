---
name: finding_raw_and_rendered_readers_disagree_with_no_tell
description: A surface read both raw (agents, `cat`) and rendered (the operator, dashboards) can drop content for ONE of them silently — both readers believe they saw the file
metadata:
  type: feedback
symptoms: "the cell is in the file but not on the page; content visible in `cat` and missing in the rendered view; a claim I wrote was never acted on though it is right there in the source; spine audit read the file and missed it; row has more cells than the header; headline truncated at render; `[:60]` slice; markdown table cell dropped"
---

**A file that is read BOTH raw and rendered has two readers, and a formatting defect can hide content
from exactly one of them with no error on either side.** The raw reader (a Claude session doing `cat`)
sees the content and books it as communicated. The rendered reader (Will, a dashboard, any markdown
view) never sees it. **Neither reader can detect the disagreement from their own side** — which is why
this survives review by either one alone.

**Why:** review instruments grade CLAIMS — is this true, is it current, does it agree with its owner
surface. This defect does not falsify a claim; it DELETES one. A spine audit reading the raw file finds
a correct, current, well-sourced sentence and passes. `PROME/STATUS.md` L21 was written and audited on
the same day (spine audit #13, 2026-09-12) carrying **five cells in a three-column table** — GFM drops
the excess — so a live claim about the closeout dashboard-build procedure and the account of the L338
date slip were invisible in every rendered read from the moment they were written.

**n=2, two different mechanisms, same class:** ① the over-celled markdown row above · ②
`fleet_dashboard.py`'s `headline[:60]` slice, which severed three HEARTBEAT channel headlines mid-token
— one of them cutting a mandatory caveat off the operator's chip (2026-09-11/12). Expect more: every
`[:N]`, every column-count, every render-time slice is a candidate.

**How to apply:**
- When you write content that will ALSO be rendered, verify at the RENDER, not at the source. "It is in
  the file" is not evidence anyone can read it.
- Prefer a mechanical guard that **agrees with the renderer rather than with authorial intent** — if the
  renderer splits on a pipe inside a code span, so must the check. A check kinder than the renderer
  certifies rows the renderer still breaks.
- Put the guard where the content is WRITTEN (BLOCKING at closeout), not only where it is read
  (advisory at boot): the writer is the only one who can stop it shipping.
- Instrument for PROME's own boot-read surfaces: `PROME/tools/table_check.py`, wired into
  `prome_gate.py` both modes (advisory boot / blocking closeout), perimeter derived from
  `PROME/registry/READS.tsv`. Acceptance conditions:
  `PROME/tools/tests/ACCEPTANCE_table_check_overcelled_rows.md`.

Related: [[finding_silent_blank_evades_review]] · [[finding_truncation_returns_a_plausible_answer_not_an_error]] ·
[[finding_output_shape_implies_more_than_the_measurement]] · [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]] ·
[[finding_test_the_guard_not_just_the_guarded]]
