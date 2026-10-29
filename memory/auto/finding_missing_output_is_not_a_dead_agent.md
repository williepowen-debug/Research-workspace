---
name: finding_missing_output_is_not_a_dead_agent
description: A background agent's missing output file after a session pause means "not written yet", not "dead"; relaunching on the same write path produces two writers and a file whose contents change under the reader.
symptoms: "the agent apparently didn't survive the pause"; "report file doesn't exist, relaunching"; two task notifications for the same job; a report whose section numbering changes between two reads minutes apart; a claim you quoted is no longer in the file
metadata:
  type: feedback
---

**What happened (SAM, 2026-10-29):** SAM launched a news-sweep agent at ~00:30 ET, then the session paused for ~7 hours. On resume the report file didn't exist, so SAM concluded the agent "apparently didn't survive the pause" and launched a retry with the SAME output path. The original was alive: it ran 7.5 h and finished one minute after the retry. Both wrote `NEWS_SWEEP.md`. SAM read a mid-write mix at 07:51, built STATUS from it, then found at 07:52 that the file had been replaced by the other agent's version. Three STATUS claims (a quote, an OIS figure and a "no remark since 10/17" window) then had no support in the surviving file. One of them was false: the surviving version reported a 10/19 Diet remark inside that window.

**Why it happened:** "no file" was read as a fact about the agent, when it is only a fact about the file. The original brief asked for a single final write, so silence was the expected state.

**How to apply:**
- Before relaunching, check the agent's state (task list, or TaskStop the original first). Never infer death from absent output.
- If a relaunch is needed, **stop the original** or give the retry a **different output path**. Two writers on one path is the defect, whichever finishes last.
- Briefs should ask agents to write a skeleton early. That makes liveness visible, but it also makes a concurrent overwrite silent, so the different-path rule still holds.
- After any multi-writer incident, re-check every claim you took from the file against the version that survived before committing. Here, re-sourcing caught all three.

Related: [[finding_record_of_an_action_is_not_the_action]] (an artifact's state is not the actor's state), [[finding_closed_out_teammate_does_not_resume_on_reping]] (the inverse liveness error).
