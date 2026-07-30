---
name: finding_hygiene_commit_rearms_the_staleness_lie
description: "A staleness guard keyed to git-commit time is RE-ARMED by any hygiene commit — sweeping a file marks it fresh; \"ok\" without a content vintage is unverified, not fresh"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00d8e67a-7d27-4930-ac91-b16937007a63
  modified: 2026-07-30T20:35:54.583Z
---

A staleness check that falls back to git-commit time is **re-armed by the very act of sweeping**: any hygiene edit (banner, stamp, reformat) commits the file, and the tool then reports `ok +0d` — fresh *because you touched it*, not because the data is current. n=2 on 2026-07-30 from opposite directions: REGINALD's `workbook/VX.tsv` read `ok +0d` after a same-day sweep commit and flipped to `⚠️ STALE +119d` the moment the PAT-044 content token was prepended (a 106-day error in the reassuring direction); LIQUID independently flagged that `ledger_staleness` "ok" on ledgers with **no content vintage at all** is a weak pass being read as verified-fresh. Sibling class, same day, n=3 in one sweep (LIQUID): **warning surfaces carrying a state claim or a day count decay exactly like the data they guard** — a boot label asserting "X1 FIRED", a banner asserting "X1 CLOSED", a staleness counter frozen at "64d" (really 93d) — and decay invisibly, because readers treat a warning's presence as evidence someone is watching.

**Why:** the false-negative direction is the dangerous one — a file that *looks* freshly-verified suppresses the re-check that would catch it, and hygiene passes (the very activity meant to fix staleness) systematically re-arm it.

**How to apply:** (1) key freshness to the literal PAT-044 token `Last real data refresh: YYYY-MM-DD` so content vintage wins — prepending it to an existing banner line needs no schema change (REGINALD's fix pattern); (2) treat `ok` from a git-time fallback as UNVERIFIED, especially immediately after any sweep or hygiene commit; (3) any banner/label/counter containing a state claim or day count needs its own dated rewrite trigger — two-clock treatment, same as a ledger; (4) staleness tooling should print *fresh-by-content* and *fresh-by-commit* differently, never as the same "ok". Links: [[finding_mtime_is_corrupted_by_git_sync]] · [[finding_banner_is_a_warning_not_a_fix]] · [[finding_completion_stamp_skip_reads_as_current]] · [[finding_test_the_guard_not_just_the_guarded]]

**Provenance addendum (2026-07-30 closeout, REGINALD):** this was NOT a fresh 7/30 discovery — REGINALD had written the core observation in its SCRATCH on **2026-07-10** (*"adding a STALE-VINTAGE header resets the git-commit-time the staleness script keys on"*) and it sat unpromoted through three closeouts before being re-derived 20 days later, AFTER it had already cost the 106-day VX blind spot. The sharper lesson: **a SCRATCH note naming a control that has stopped working is not a half-thought — promote it at the closeout that writes it.** Ephemeral surfaces are where guard-failure observations go to die.
