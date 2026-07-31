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

---

**Refinement — don't pattern-match the output to decide health; key on the exit status you already have. (MARCO, 2026-07-31.)** This memory named the latent bug *and named MARCO as a carrier*; it then sat live in `AGENTS/MARCO/scripts/boot.py` for months and hid a dead fetcher for **101 days**. Worth being precise about why, because the "add a ⚠️ marker" fix above is **necessary but not sufficient.**

MARCO's `collapse()` filtered a fetcher's output to lines containing any of `("🔴","🟠","⚠️","❌","FAIL","ERROR","TIMEOUT","wrote","Source:",…)` and, on an empty match, returned the literal `"✓ ran cleanly"`. The H-2A fetcher died on a bare `requests.exceptions.JSONDecodeError` traceback — which contains **none of those tokens** (`Traceback`/`JSONDecodeError` match neither `ERROR` nor `FAIL`, capitalization included). So boot printed:

```
  ⏳ H-2A disclosure — 101d old ≥ 85d, fetching…
    ✓ ran cleanly                 <-- the display layer
  ...
  ❌ H-2A disclosure     FAIL      <-- the summary, same run
```

**Everything upstream worked.** The tool exited non-zero, `run_script` captured it, the summary said FAIL, and the aggregator returned 1. The *rendering* destroyed it — and of the two contradictory lines, the reassuring one sits beside the step you're actually reading, so that is the one that gets believed. This is the failure sibling of [[finding_verification_zero_is_ambiguous]]: an empty match is "found nothing" AND "matched nothing," and the default must not resolve that ambiguity toward green.

**The generalizable rule:** a whitelist of expected failure markers cannot cover arbitrary failure text, because *you don't know what an unanticipated failure will print* — that's what makes it unanticipated. Any place you already hold a reliable signal (an exit code, an HTTP status, an exception object), **branch on that signal and let the text be evidence, not verdict**. Concretely: `collapse(output, status)` → if `status != OK`, never emit the all-clear; print the **raw tail** (a traceback's marker is its first line but its cause is its last). Audit for this shape with `grep -n 'else.*clean\|or \["✓\|: green'` over your boot/report tooling — the tell is a *default-to-positive fallback on an empty collection*.

See also [[finding_test_the_guard_not_just_the_guarded]] (the guard's own failure direction is the thing to test) and [[finding_stale_executable_exits_clean]] (the rc=0 sibling: there the callee lied, here the callee was honest and the caller mistranslated it).
