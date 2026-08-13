---
name: finding_bare_since_date_drops_same_day_commits
description: "git log --since=YYYY-MM-DD silently drops SAME-DAY commits (bare date resolves to now's time-of-day) — delivery checks read it as \"agent never delivered\""
metadata: 
  node_type: memory
  type: project
  originSessionId: f2074874-2a57-499f-882e-1b471a12735a
  modified: 2026-08-13T17:16:02.719Z
---

`git log --since=YYYY-MM-DD` resolves a bare date to that date **at the current
time of day**, so at 13:15 it means "since 13:15 today" and every commit made
earlier today is silently excluded. Reproduced live 2026-08-13 (PROME
private-credit grouping session, SHADE's find):

- `git log --since=2026-08-13 -- AGENTS/SHADE/` → **0 commits**
- `git log --since='2026-08-13 00:00' -- AGENTS/SHADE/` → **4 commits**

Same path, same repo, same moment.

**Why:** the failure direction is a FALSE NEGATIVE that reads exactly like "the
agent went idle without delivering" — a delivery/chase check built on a bare
date will manufacture false chases fleet-wide, and nothing errors. Sibling of
[[finding_verification_zero_is_ambiguous]] (a zero certifies the check's scope,
not the world) and the [[finding_record_of_an_action_is_not_the_action]] family
on the checking side.

**How to apply:** in any git date filter, never pass a bare `YYYY-MM-DD` to
`--since`/`--after` when same-day commits matter — use an explicit time
(`'YYYY-MM-DD 00:00'`), a relative window (`--since='90 minutes ago'`), or
count-based forms (`-n`, ancestry checks). Before concluding an agent didn't
deliver from a zero-result log, re-run with an explicit midnight time. Note:
even a correct relative window can race in-flight work — a chase that crosses
a commit by minutes is a timing artifact, not a failure; verify by ancestry
(`git merge-base --is-ancestor`) before treating a chase as substantiated.
