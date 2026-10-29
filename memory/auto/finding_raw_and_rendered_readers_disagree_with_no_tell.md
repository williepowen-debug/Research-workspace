---
name: finding_raw_and_rendered_readers_disagree_with_no_tell
description: A surface read both raw (agents, `cat`) and rendered (the operator, dashboards) can drop content for ONE of them silently — both readers believe they saw the file
metadata:
  type: feedback
symptoms: "no monthly figure on the page; the page only shows all-time totals; the chart is there but the summary says no data; numbers live in a <script> block or chart JSON; the cell is in the file but not on the page; content visible in `cat` and missing in the rendered view; a claim I wrote was never acted on though it is right there in the source; spine audit read the file and missed it; row has more cells than the header; headline truncated at render; `[:60]` slice; markdown table cell dropped; cut -c1-N hid the diff; truncated diff line read as identical; BD row marked 🆕 in the ID column but discharged in its Status cell; head -c cut the tail; my own tool cut the line"
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


**n=3 (2026-10-28, PROME prome-92):** the raw reader was ME and the renderer was my own `cut -c1-300`. Reviewing LABOR's uncommitted diff I printed each `+`/`-` line cut to 300 chars; the two versions of `CLAUDE.md:142` were identical to the cut and differed only past it (`outbox/` → `outbox/delivered/`), so I reported the change as whitespace. The same pass read a BUILD_DEBT row whose ID column still carried `🆕` and called the item open while its Status cell, past the cut, said discharged 9/07. LABOR corrected both at the artifact. **Rule for the operator of the slice:** a `cut`/`head -c`/`[:N]` you apply to a DIFF or a TABLE ROW is a render; it can only ever show you that the prefixes agree. Compare with `diff -U0` whole lines (or `md5sum` the lines), and read a row's STATUS cell, never its marker, before calling it live.

**n=4 (2026-10-28, LABOR):** an ABSENCE verdict was booked from the rendered reader. On 9/29 LABOR declared trigger T-07 "unmeasurable", with no monthly WARN source anywhere, after fetch-tool summaries of LayoffAlert.org's page TEXT showed only all-time totals (KB-LAB-196). The monthly series was on the page the whole time, in a `<script>` block as chart JSON ("Mass Layoffs by State – Last 24 Months", 46 states × 37 months). A text summary renders the page and drops scripts, so it cannot see chart data, and it reported "no monthly figure" with no error. A trigger sat dead for a month on that. Found by grepping the RAW HTML for month labels. **Rule:** before booking "the source has no X", grep the raw bytes (including `<script>`/JSON) for X's shape (month labels, dates), not just the rendered text. A negative from a renderer is a claim about the renderer. Fix: `AGENTS/LABOR/tools/warn_monthly.py` parses the JSON; KB-LAB-226 corrects KB-LAB-196. Related: [[finding_negative_reachability_is_a_claim_about_your_request]] · [[finding_scan_keyed_on_naming_reads_local_form_as_absence]].
