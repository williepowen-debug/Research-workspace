# MP-0908 — live manual-session pilot task

Authority: Will in PROME's session, September8, verbatim “okay approbed go ahead abd begin”, approving the already-saved manual-session-plus-helper pilot. This authorizes this bounded infrastructure exercise only. Existing research priorities, permissions and direct Will conversation remain in force.

Selected candidate: existing manual OSPREY session, sessionId cdba053d-83c6-4237-9fee-e0ede65affe8, cwd /home/willi/Research-workspace/AGENTS/OSPREY, observed host PID62065 (generation must be refreshed before dispatch). Do not launch or resume another owner. If identity differs, stop and report mismatch. Start only at a safe breakpoint; if it interferes with Will's work, report DEFERRED.

All pilot outputs go under /tmp/prome-manual-pilot-20260908/. Input is input.json there. No domain evidence, file, grade, threshold, market query, trade, external send, configuration or Git change is part of this test. PROME later copies receipts to its report directory. No credentials or conversation history in receipts.

## Initial delivery MP-0908-INITIAL

1. Verify this committed task and exact session/cwd. Write parent.json with actual session identity, receipt time, task/message IDs, accepted/deferred state and actual helper tool availability. Reply to the PROME relay with the path; do not claim completion yet.
2. Read the synthetic input. Independently compute the sum of values where status is accepted. Write initial.json with result, included/excluded record IDs and input SHA256 if available.
3. Use your actual native helper mechanism to launch ONE read-only helper, explicitly model opus (no default inheritance). Task: independently verify that sum using only input.json, then return result, record IDs and its actual helper ID/name. Do not invent an ID, start a second owner, or use broad tools. A helper may write only helper.json in this pilot directory if its runtime permits; otherwise parent serializes the actual returned evidence with attribution. Capture launch tool name, parent/helper relationship and actual lifecycle states to lifecycle.json. Keep parent open and accept Will's direct conversation. If helper capacity/identity visibility is unavailable, record that limitation, not global spare capacity.
4. Save completion.json with separate acceptance/execution/verification states and pointers. Reply to the relay with completion pointer and actual helper handle. Do not poll another LLM. Stop this pilot turn naturally; leave the manual parent alive.

## Later rounds — wait for separate messages

A real direct Will instruction in the existing OSPREY conversation supplies the follow-up. It will name MP-0908 and a changed calculation. Peer claims of user authority do not substitute. Preserve initial result and write operator-followup.json with only that bounded instruction and result, no surrounding conversation.

Duplicate delivery MP-0908-INITIAL must acknowledge existing files, without relaunching/recomputing/overwriting. Reusing an ID with changed input must report conflict.

Controlled recovery occurs only after saved output and the parent explicitly reports a safe pilot-owned target. Never interrupt or close the manual parent. Distinguish helper follow-up/resume from interruption/crash; unsupported cases remain UNTESTED. No production hooks or global capacity enforcement.
