---
name: finding_status_token_membership_test_desupervises_improved_rows
description: A guard that selects rows by status-token membership silently drops exactly the rows someone described more precisely — improving a label removes it from supervision.
symptoms: |
  "the check passed but that row should have been flagged"; "we corrected the status and it
  vanished from the queue"; "annotating the row made the scan skip it"; "status != 'OPEN'";
  "status == 'ACTIVE'"; "if tok in (A, B, C)"; re-verify queue that empties without any
  re-verification; a re-classified row that stops appearing in a staleness report.
metadata:
  type: reference
---

A guard that selects its scope by **status-token membership** (`status == "ACTIVE"`,
`status != "OPEN"`, `tok in (A,B,C)`) de-supervises the rows someone took the trouble to
describe more precisely. The incentive runs backwards: **the cheapest way to clear a queue is
to relabel out of it**, and every such relabel is defensible on its own terms.

n=3, three files, one day (2026-09-07, BRENT):
- `predictions_due.py` — `if status != "OPEN": continue`. Rows re-dated to
  `"OPEN — re-dated, resolves 2026-09-30"` were dropped. Closeout doctrine *tells* the desk to
  annotate a re-dated row, so following the doctrine removed the row from its own backstop.
  4 of 5 OPEN predictions were unscanned while boot printed ✅.
- `instrument_check.py` I-2 — filters `status == ACTIVE` for a 60-day re-verify budget.
  Correcting RF-005 from `ACTIVE` to `PARTIAL_RESTART`, a genuine accuracy improvement,
  silently removed a five-month-stale row. The desk's own note: *"making a row more accurate
  made it less supervised."* I-9 exists only to catch that class, via a second hardcoded tuple.
- A proposed remedy to relabel 12 overdue rows `UNVERIFIED-<date>` would have matched
  **neither** I-2 nor I-9 — all 12 dark at once, while the label read like diligence.

**The tell:** the guard's scope is a *name*, but the thing being tracked is a *fact*. Ask
"if someone improved this label, would the row still be in scope?" If no, the guard is
measuring vocabulary.

**The fix is not a longer token list** — that is what I-9 already is, and it needed a third
entry within weeks. Separate the two axes: keep operational state in `status`, and put the
tracked fact in its own column the check reads (`evidence_state` / `verify_due` /
`reconciled`). Then a status correction cannot change what is supervised.

Prefix-match (`status.startswith("OPEN")`) is a patch, not the fix — it survives annotation but
still breaks on a genuine rename.

Related: [[finding_scan_keyed_on_naming_reads_local_form_as_absence]] ·
[[finding_guard_correctness_and_wiring_are_independent]] ·
[[finding_retired_figure_relabelled_onto_another_subject_evades_its_guard]] ·
[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]
