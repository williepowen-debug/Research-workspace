# WALTER → PROME: reviewed boot attestation and recovered local session visibility

Created 2026-10-31T19:52:03Z. Will asked WALTER: “Okay lets try to fix these.” Scope is the reported partial-boot gaps.

WALTER completed the reader review now, ahead of the November 3 checkpoint. Please transcribe only WALTER's ATTESTATION row from `AGENTS/WALTER/research/2026-10-31_boot-repair/ATTESTATION-TO-TRANSCRIBE.tsv`, citing its `BOOT-BASIS-REVIEW.md`. Twenty-nine reviewed hashes now match current bytes; seven changed files were reviewed; READ paths/modes are unchanged. Preserve other readers and prior evidence/history. The manifest WRITE PATH reserves this update to PROME, so WALTER has not edited READS.tsv.

Local visibility recovery: `codex-inventory.json` beside the review records a successful metadata-only read of the already-running default app-server control socket at 19:50:18Z. Eight loaded threads: WALTER active, CATO idle, six helpers (two active, four idle). A separate `session_bridge.py` inventory sees the PROME interactive Claude session idle. These are timestamped positive observations, not a permanent/global absence census, and idle is not closed. No message, resume, task or spawn was sent through the endpoint.

Concrete transport mismatch: current `PROME/tools/session_bridge.py` `Rpc.unix` sends newline JSON directly. The installed Codex endpoint uses a WebSocket HTTP Upgrade over Unix sockets, as documented by the current app-server API. A one-off read with the already-installed `.venv` websockets 16.0 `unix_connect` succeeded using initialize → initialized → thread/loaded/list → thread/read(includeTurns=False). The existing endpoint is `/home/willi/.codex/app-server-control/app-server-control.sock`. No daemon or dependency was installed. This is reproducible owner evidence for an existing adapter repair, not a request for a new checker or an authorization to broaden messaging. WALTER did not edit the PROME-owned bridge.

Primary API reference: https://developers.openai.com/codex/app-server . Detailed repair outcomes and remaining source dependencies are in `AGENTS/WALTER/research/2026-10-31_boot-repair/REPAIR-RECEIPT.md` once this sitting closes. Publication remains coordinated under the existing WALTER rule. Existing root CLAUDE.md and ORCH_INFLIGHT rotation warnings remain PROME-owned; no change to those files is included. Current owner/source evidence stays bounded in the receipt.

## COMPLETION — WALTER — 2026-10-31
STATUS: PARTIAL — own review complete; central registration pending.
CHANGED: Own reviewed hashes, review evidence and this create-only packet.
RESULT: Seven changed bases reviewed; 29 paths match. Eight loaded Codex threads observed at one local endpoint.
GAPS: PROME transcription; global absence/lifecycle completeness is not established.
WILL_NEEDS: None for the existing attestation transcription.
FOLLOW-UP: Transcribe WALTER's exact declaration and reconcile the November 3 checkpoint; assess existing bridge transport mismatch within its owner scope.
