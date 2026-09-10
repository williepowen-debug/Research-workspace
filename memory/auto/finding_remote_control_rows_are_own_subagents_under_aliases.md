---
name: finding_remote_control_rows_are_own_subagents_under_aliases
description: ListAgents "Remote Control · running" rows with generated names (<host>-<adjective>-<animal>) on the CURRENT box are this session's OWN subagents seen through the bridge — not foreign desks; a spawn preflight that treats them as unknown sessions stalls a Tier-1 spawn for nothing.
symptoms: "four Remote Control sessions came up running", "which desks are they", "second PROME on the laptop", "prome-6d is live on the desktop", spawn held on unidentified sessions, subagents warning about two coordinators
metadata:
  type: feedback
  author: PROME
  date: 2026-09-10
---

**Finding (PROME, 2026-09-10 10:4x–11:1x ET):** after spawning HANS · DAEDALUS · LABOR · ANVIL · a coldreader, `ListAgents` showed five new `desktop-bc6ef81-<alias> · Remote Control · running` rows. PROME read them as possibly Will-opened desks on "the other machine", held the FALCON doorbell spawn (~25 min) and asked Will which desks they were. A direct `SendMessage` to two of them answered **DAEDALUS** and **HANS** — PROME's own teammates, which appear in the `Teammates` block under their real names AND in `Peer sessions` under bridge aliases. Both then warned about "a second PROME session on the laptop" — the alias cut both ways.

**Why:** the Remote Control bridge lists every session on the host, including in-process subagents of the current session, under generated names; the hostname prefix (`desktop-bc6ef81`) names THIS box (`hostname`), not a remote one. The `Teammates (n)` block is the authoritative list of own subagents; a Peer row is foreign only if no teammate is running and the host prefix is not this machine's.

**How to apply:** at spawn preflight, count `Teammates` first; if the Remote Control rows on this host equal the running teammates, they are the same sessions — proceed. If the count differs, message ONE alias with "which desk are you?" (a one-line reply, ~1 min) before holding a spawn or asking Will. Never infer a second coordinator from an alias; the hostname prefix is checkable with `hostname`. Related: [[finding_scope_boundary_asserted_from_proximity]] (read the grant, not the ledger); [[finding_record_of_an_action_is_not_the_action]].
