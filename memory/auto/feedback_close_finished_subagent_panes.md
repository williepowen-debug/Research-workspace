---
name: feedback_close_finished_subagent_panes
description: Will (2026-10-23) wants finished subagent panes closed — a cold reader or desk that has delivered and receipted its closeout gets TaskStop'd so its pane goes away; do not leave a row of idle panes open
metadata:
  type: feedback
symptoms: "ListAgents shows six idle coldreader/desk panes", "panes piling up after readers return", "when a cold reader is done can you close their window pane"
---

Will, 2026-10-23 09:21 ET, in the PROME window, verbatim: *"When a cold reader is done can you close their window pane out?"* — asked when ListAgents showed six finished panes (two desks that had already given their WQ-249 closeout receipt, four coldreaders that had returned their ledgers).

**Why:** every subagent spawned with the Agent tool opens a pane in his terminal; a finished one is clutter he has to look past, and it reads as live work that is not. A read-only reader has nothing to close out (its ledger is its only write), so there is no reason to keep it.

**How to apply:** after a coldreader returns its ledger (its idle notification), `TaskStop <name>` it in the same turn you score it. After a desk answers the WQ-249 closeout ask (receipt in hand, ORCH_LOG CLOSE row written), `TaskStop` it too — the receipt is the ask's answer, the pane is not evidence of anything. Never stop a reader or desk that has not returned (an in-flight result is lost), and never stop a peer session that is Will's own (`ListAgents` "Peer sessions"), only teammates this session spawned. Related: [[finding_closed_out_teammate_does_not_resume_on_reping]] (a stopped desk is a fresh spawn next time, which is already the rule).

**Instance 2 (NEXUS, 2026-10-23T22:42-04:00):** a Will-direct full pass spawned three Opus digest readers and one Sonnet cold reader; all four returned and were scored, none was TaskStop'd, and Will pasted the terminal chip "← 1 agent" at 22:33 ET as feedback. By the time the stop was attempted the tasks had already exited ("No task found") — the pane chip outlived the task. Apply the rule in the same turn the result is consumed, not at closeout; n=2.

**Launcher desk windows differ (Will, 2026-11-06 13:52 ET, tentative, verbatim):** *"I think I am just going to leave these windows open incase you need them again or come across something else? Maybe that will be my norm going forward."* This rule still covers Agent-tool readers and panes inside PROME's terminal. A launcher desk window is Will's to leave open: never close it, re-use it by SendMessage instead of a second launch (HANS and CARL both resumed that way 11/6), start each re-use with a fresh read of state, and take a new receipt for new work. Limit: 21 sessions held 6.0 GB of a 10 GB machine at 13:52 ET and looked safe; 29 sessions at 15:26 ET, with swap already about 10.7 of 16 GB, made Claude Code kill background jobs at TERRY, VULCAN and BRENT. Read swap and free memory before any launch; treat about 20 sessions as the ceiling on this box; a desk's watcher is lost first, so PROME takes on its wake-ups.
