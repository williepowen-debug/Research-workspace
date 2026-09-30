---
name: finding_crashed_session_state_lives_in_its_transcript
description: after a box crash, the commits and the orchestration log give you the RECORD, but the unwritten in-context state — the last ask to Will, an agreed-but-unwritten item, an in-flight doorbell — survives only in the dead session's transcript jsonl; recover from all three, never from memory of the session
symptoms: "computer crashed last session", "we were not able to close out properly", "tree is clean after a crash so nothing was lost", "what was the session doing when it died", "unanswered question to Will lost", "desk delivered but nothing on disk", "reconstruct a crashed session"
metadata:
  node_type: memory
  type: finding
---

**What happened (2026-09-30, prome-f4 → prome-94):** the box crashed ~15:0x ET, three hours after the day's last commit. At the 17:26 boot the tree was CLEAN, the stash empty and HEAD == origin — so "nothing lost" was the charitable reading. The record (commits + `PROME/state/ORCH_LOG.tsv`) reconstructed the morning's work, but three things existed nowhere on disk: PROME's 15:02 question to Will on WQ-316 (sold or held?), two items CREED and Will had agreed on at 15:05 in CREED's window (a KB row, a WALTER packet — never written), and the state of an in-flight HENRY doorbell. All three came from the dead session's transcript: `~/.claude/projects/<workspace>/<session-id>.jsonl` (the largest, most recently written file is the crashed main session; parse `type`/`timestamp`/`message.content` for the last user and assistant rows and the last `tool_use` calls).

**Why:** a clean tree proves only that no FILE was mid-write. Work that lived in context — asks, agreements, in-flight spawns, the closeout that was about to happen — leaves no absence to detect on disk (`[[finding_crash_residue_over_claims_toward_completion]]` is the sibling case: residue that overclaims; this is the case with NO residue at all).

**How to apply:** after any crash, three sources in this order — ① `git log --since` + ORCH_LOG rows for the day (what landed); ② the transcript's tail (what was asked, agreed or in flight and never written — re-ask Will, notify the desk's next window); ③ the desks' own dirs and `ListAgents` (whose windows died). Then rebuild the closeout write-backs from ①+②, label them RECONSTRUCTED, and fix any ledger row the crash left in a state the instruments reject (a `0-NOTE` touch token blinded the WQ-249 check for one gate).
