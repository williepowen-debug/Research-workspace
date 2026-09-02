---
name: finding_directive_overtaken_between_authorship_and_delivery
description: On a same-box fleet a directive or queue row asserting a TARGET STATE ("execute X", "hold X", "approve the move") can be overtaken between authorship and delivery; check the target's own git log before registering or relaying, or the row describes its own outcome as a pending decision
symptoms: "the row's premise is the pre-move state" · "already executed eleven hours before your row" · "second time this morning a message described work already on disk" · a WILL_QUEUE row whose forecast equals the current measurement · GO relayed for work already committed
metadata:
  type: feedback
---

**The instances (PROME, 2026-09-02, both caught by CARL):** ① DAEDALUS packeted a ruling input at 09:09 ("CARL relocates its 15 KB PREDICTIONS mirror; STATUS at 119%"); PROME registered WQ-154 at 09:10 off that packet; CARL had executed the move at 22:10 the night before (`d1a600bad`) — the row asked Will to approve a completed move on a stale byte count, and its "move takes STATUS to ~50 KB" line was describing the file as it already was. ② Will closed the row; PROME relayed "GO on the residues" ~5 min after CARL had already committed them (`2ed23c7c0`). Both harmless only because the owner read its own log before acting.

**Why:** the relay hop on a same-box fleet (packet → PROME row → Will → PROME relay → owner) is long enough that a live owner overtakes it. A message asserting a target state is a claim about the target's CURRENT state, and neither the packet author nor the relayer measured it — each trusted the hop before. It is `[[finding_record_of_an_action_is_not_the_action]]`'s mirror: there the record lags the action; here the directive lags the action.

**How to apply:** before registering a queue row or relaying a directive about another desk's file, run `git log -1 --format='%h %ci %s' -- <target path>` (and `git status -- <target>` for in-flight work) and put the result on the row. A row whose forecast matches the measurement is a completed item, not a decision. Same-box peers share one clone: their commits are already in your HEAD — never tell them to pull, and never assume your row is newer than their file. Related: `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`, `[[finding_prome_inbox_is_repo_root_not_under_agents]]`.
