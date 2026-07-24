---
name: finding_stranded_commit_payload_retriage
description: A recovered stranded commit isn't done when git is clean — its PAYLOAD (cross-agent packets, docket-add requests, dated asks) was invisible to the fleet the whole time it was stranded, so every time-sensitive item inside needs explicit re-triage against the calendar that kept moving without it.
metadata:
  type: project
---

Merging a stranded commit (committed-but-unpushed on the other machine, or an orphaned packet finally rescued) restores the FILES but not the LOST TIME. While it was stranded, the fleet ran without its contents: requests aimed at "tomorrow" expired, recipients never booted on it, and the sender believes it was delivered.

**Instance (2026-07-23 late-eve):** the laptop's 7/22 auto-commit (11 cross-agent packets) stranded un-pushed through the entire 7/23 desktop fire-day. VULCAN's docket-add asking for a 7/23 SK-Hynix spawn died silently — no docket row, no spawn, nobody knew. Post-merge re-triage caught it (re-landed as a 7/24 CATCH-UP row), executed LABOR's Will-directed routing a day late, and pre-warned Friday's session that owners' 7/23 "silence" on the stranded packets ≠ non-consumption.

**Why:** git-level success (clean rebase, 0/0 sync) reads as "recovery complete," but the failure was informational, not textual. The same class at file level is the orphaned-packet gap (detector: `scripts/orphan_check.sh`, adopted 7/23) — this memory covers the machine-level variant AND the general rule for any late-arriving delivery.

**How to apply:** after merging any stranded/delayed work, list its payload and ask per item: (1) did it request an action dated inside the stranded window? → the action silently didn't happen; re-schedule or mark missed, don't assume done. (2) is a recipient's silence being read as a verdict? → it never saw the item; annotate before someone banks the null. (3) does a state file the fleet DID update during the window contradict it? → the live file wins, the stranded copy gets reconciled, not restored. Related: [[finding_two_machine_partition_clean_merge]] (the git mechanics), [[finding_never_received_is_not_doesnt_hold]] (silence ≠ knowledge).
