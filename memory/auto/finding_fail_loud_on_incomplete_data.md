---
name: finding_fail_loud_on_incomplete_data
description: Health/sweep scripts must gate the green all-clear on zero-failures AND zero-flags — an all-clear printed on zero data is false health
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1cdcff3f-0ef5-483b-a7bb-738464843581
---

A boot/data-sweep script that prints "✅ no thresholds breached" whenever its flag-list is empty will report **health it never measured** when every fetch fails: 12/12 ERROR lines, then a green all-clear, exit 0. The empty flag-list is ambiguous — it means *either* "all clear" *or* "measured nothing."

**Why:** the summary logic only counted RED flags, not fetch failures. `if red: ... else: green` falls through to green on total fetch failure. (LABOR `labor_data.py`, Orc-caught Jun 16 2026.)

**How to apply:** count fetch failures separately and gate the all-clear: `if failures: print(INCOMPLETE warning); if flags: print(flags); elif not failures: print(all-clear)`. Return a non-zero/alert code on failures too (not just on flags) so the boot aggregator surfaces it (reuse the existing alert code if the harness only has a binary alert). Make the INCOMPLETE line carry a marker the collapsed-output filter already surfaces (e.g. ⚠️). Same latent bug lives in any agent sharing the boot.py pattern (SAM/BRENT/MARCO) and in any fallback/error instrument. Related: [[finding_measure_actionable_not_gross_rate]], [[finding_boot_py_cadence_skip_pattern]].
