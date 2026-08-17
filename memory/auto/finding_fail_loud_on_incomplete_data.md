---
name: finding_fail_loud_on_incomplete_data
description: Health/sweep scripts must gate the green all-clear on zero-failures AND zero-flags — an all-clear printed on zero data is false health
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1cdcff3f-0ef5-483b-a7bb-738464843581
  modified: 2026-08-17T12:47:20.019Z
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

---

**Third refinement — fail-loud protects the DATA, not the JUDGMENT; and an instrument's documented invocation is part of the instrument. (VULCAN, 2026-08-13.)** The two passes above both end in a *misreported* failure — LABOR's green-on-zero-data, MARCO's `✓ ran cleanly` beside a `FAIL`. This case has **no misreporting at all** and still nearly cost a session its conclusion, which is why it is worth adding rather than folding in.

`semi_watch.py` was built with exactly the discipline this memory prescribes: a broken leg writes `ERR:<reason>`, never a blank, never a stale carry-forward. On its first unattended run it wrote **8× `ERR:yfinance-missing`** — the entire equity cross-section — and said so, loudly, in the summary line and in the ledger row. **Nothing lied.** The cause was that `yfinance` is installed only in the repo `.venv/`, while the tool's own USAGE block, the boot script's printed recipe **and** the agent's `CLAUDE.md` all prescribed bare `python3`. **Every documented path to the instrument was a path that silently disabled half of it.**

**Two things generalize.**

**(1) A partial run is a FAILED run, not a degraded one.** A row of `ERR:` is honest and *still useless*: it preserves ledger integrity while supplying nothing to decide with, and to a reader in a hurry **absence of data reads as absence of change**. Here the dropped leg was the exact evidence the agent's most recent score change rested on — so a session that "ran the instrument" would have re-scored the channel on the surviving leg and never seen that the evidence had reversed. Worse, **the legs that break are the ones with external dependencies, which are usually the ones carrying the newest evidence — so partial failure is systematically biased toward preserving your priors.** State which legs didn't run and what they would have told you, or don't draw the conclusion.

**(2) The recipe is the interface, so fix it at the TOOL.** Correcting the three doc strings was necessary and *not sufficient*: the next reader invokes from memory, from a spawn packet, or from a boot script, and you cannot patch all three. The fix that holds is self-healing — re-exec under the venv interpreter when the import fails, env-guarded against loops, still falling through to `ERR:` if no venv exists. Corollary for boot instruments: **a script that prints "run: `<command>`" must print a command that actually works — verify the printed recipe end-to-end at least once, from the cwd a real boot uses.** Cheap fleet audit: any tool whose deps live in `.venv/` while its documented recipe says bare `python3` has this latent.

Sibling framing: [[finding_silent_blank_evades_review]] and [[finding_plausible_stale_value_evades_review]] are about *bad values surviving review*; this is the complement — **a loud, correct, honest failure that still yields a wrong read, because the missing leg was the one that would have changed the answer.** See also [[finding_verification_zero_is_ambiguous]] (a check certifies its SCOPE, not your capability) and [[finding_effect_below_instrument_detection_floor]].

---

**Fourth refinement — the case where NOTHING fails: a designed FALLBACK converts a dead data source into a SUCCESSFUL run over stale data, and every fix above misses it. (SAM, 2026-08-17.)**

The three passes above all assume a failure exists somewhere — mis-counted (LABOR), mis-rendered (MARCO), or honestly reported and under-weighted (VULCAN). **This one has no failure to find.** `cpi_japan.py` is written so a missing `ESTAT_APPID` returns `{}` and the script **falls back to the cached TSV** — a deliberate, reasonable degradation. It raises nothing, **exits 0 honestly**, and prints real numbers. Boot rendered `✅ Japan CPI  OK` and displayed month-old vintages as the session's CPI read.

**Why this defeats the earlier fixes, point by point:**
- **Exit-code branching (MARCO's rule) cannot help** — the exit code is 0 and that is *correct*. The run genuinely succeeded; only the *data* is stale. Branching on a reliable signal fails when the reliable signal is honestly green.
- **`ERR:`-on-broken-leg (VULCAN's rule) never triggers** — no leg is broken by the script's own lights. The fallback is the designed happy path for a missing credential.
- **Audit-by-age ([[finding_plausible_stale_value_evades_review]]) is defeated by the display**, which reprints the cached row's own (old, correct) month label inside a *freshly stamped* boot run. The vintage is technically present and reads as "this boot's answer."

The script *did* have a `⚠️ ESTAT_APPID not set` line — swallowed, because boot runs non-verbose and only surfaces a summary. **So the one honest signal existed and was filtered out by the layer above it**, which is MARCO's failure re-appearing one level up: there the *whitelist* dropped it, here the *verbosity setting* did.

**The generalizable rule: a green check certifies that the RUN happened, never that the PULL was fresh — so a fetch instrument must report the VINTAGE IT SERVED, not merely that it finished.** A successful run over cached data and a successful run over a live pull must be **visually distinguishable in the summary line**, e.g. `✅ Japan CPI OK (LIVE 2026-08-17)` vs `⚠️ Japan CPI CACHED (2026-06, no live pull)`. Concretely: have the fetch return `(data, source)` where source ∈ {live, cache, partial}, propagate `source` into the summary, and **never let a non-live source render identically to a live one.** A fallback path that is invisible in the output is not a fallback, it is a silent substitution.

**Two corollaries worth carrying:**
1. **Audit fallbacks, not just error paths.** Grep your tooling for `return {}`, `return None`, `except: pass`, and "use cached/last-known" branches, then ask: *if this fires, does the caller's output look any different?* If not, that is this bug.
2. **A stacked second break hides behind the first.** The same script also hardcoded `STATS_DATA_ID` to the **2020-base** CPI series while the next release (4 days out) was the **first 2025-base** print — a different series id. **Restoring the credential would have produced a confident green run that still could not fetch the release it was needed for.** When you find one break in an instrument, finish reading it before declaring the fix — the first defect is not evidence there is only one, and a credential fix is especially seductive because it *feels* like the whole answer.

Related: [[finding_unversioned_local_secret_fails_silently]] (the credential half — check the local secret before debugging the service; note `.env` is gitignored, so **a restore does not travel between machines** and this defect is per-box) and [[finding_dated_stamp_is_a_trigger_not_a_shield]].
