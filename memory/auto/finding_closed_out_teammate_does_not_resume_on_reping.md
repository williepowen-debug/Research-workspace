---
name: finding_closed_out_teammate_does_not_resume_on_reping
description: A SendMessage re-ping to an in-process desk teammate that has answered its WQ-249 closeout and gone "idle for good" does not resume it; a follow-up on a closed-out desk is a fresh spawn, not a message.
metadata:
  type: feedback
symptoms: "re-ping sent, no reply; closed-out teammate silent; pane still listed but no commit or dirty path after the message; touch 2 never started; 'a send resumes it from its transcript' did not hold"
---

**What happened (PROME, 2026-10-09 10:26–10:54 ET):** after eight desk spawns had delivered and answered their WQ-249 closeout ask ("going idle for good"), PROME sent SendMessage re-pings to four of them (WAL, BROCK, HANS, OSPREY) with bounded follow-ups, logged them as `2-REPING` touches, and waited. ListAgents still listed all four panes. In 25–30 minutes: no commit, no dirty path, no message from any of the four. The four were re-launched as fresh `desk` spawns the same minute; the re-ping rows were closed NO RESPONSE.

**Why:** the harness note that a send "resumes an agent from its transcript" did not hold for a teammate that had completed its turn after an explicit go-idle-for-good instruction; whatever the mechanism, the observable is four-for-four silence. A listed pane is not a live worker (same class as `finding_record_of_an_action_is_not_the_action`: the ORCH_LOG row said IN-FLIGHT, the desk was not).

**How to apply:** a follow-up on a desk that has closed out is a FRESH spawn (the desk's own CLAUDE.md boots again; cost is the re-boot, not a loss of record — the record is in its files). Re-ping only a teammate that has NOT yet answered its closeout ask (it is still in its turn loop). When a re-ping is tried anyway, give it a hard check at ~5 minutes (commit · dirty path · message); silence ⇒ spawn. Log the dead re-ping as NO RESPONSE, never leave it IN-FLIGHT. See [[finding_record_of_an_action_is_not_the_action]], [[finding_transfer_completes_only_when_the_receiver_encodes]].

**Counter-observation (PROME, 2026-10-09 13:1x–13:19 ET, n=2 resumes):** osprey-1009c, an in-process `desk` subagent that had delivered and sent its WQ-249 receipt, DID resume on two SendMessages sent ~10 and ~15 minutes after its closeout (it committed 46e5e67bf and cf6ac0878 and answered each). The difference from the four silent re-pings of the morning is not established — candidates: the morning's four were teammates in a prior harness session that had been told "idle for good" and were re-pinged 25–30 minutes later; today's resume came from the same session that spawned it, within minutes. Keep the rule (a fresh spawn is the safe follow-up; hard check at ~5 minutes), but the mechanism claim "does not resume" is NOT settled — record which case you are in.
