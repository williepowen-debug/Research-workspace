---
name: Telegram Reply Required
description: When Will messages via Telegram, ALL substantive replies must go through the Telegram reply tool, not session output
type: feedback
originSessionId: 95eb2b13-10a6-4aa9-8a80-58a9f1561f8f
---
When Will messages WALTER (or any agent) via Telegram, every substantive response must go through the `mcp__plugin_telegram_telegram__reply` tool. The session transcript output does NOT reach his phone — he only sees what is sent via the reply tool.

**Why:** Will reads from Telegram, not the terminal session. If I respond only in the session, he sees nothing and has to ask me to resend. This wastes a turn and breaks the workflow.

**How to apply:**
- If the inbound message came from a `<channel source="plugin:telegram:telegram">` block, the reply MUST go via the telegram reply tool.
- Use the session output only for tool calls, brief status notes about what I'm doing, or context that doesn't need to reach Will.
- The reply tool accepts the same chat_id as the inbound message.
- For long answers (analysis, explanations, multi-part responses), still use Telegram — break into multiple replies if needed rather than dropping to session output.
- When in doubt: if Will asked a question, the answer goes to Telegram.

**High-risk slip-mode (observed 2026-05-15, twice in one session):** Long analytical responses to design / architecture questions are the slip-mode. Operational dispatch responses (signal triage, threshold scans, dispatch confirmations) self-discipline because the action ends in a tool call that includes the reply. Design-conversation answers are pure prose, no tool-call action, so they default-route to transcript unless I consciously wrap them in the reply tool. **Rule:** before generating any multi-paragraph response to a Telegram inbound, the FIRST tool call must be the reply tool — compose the response *inside* it, not as transcript prose that I then re-send. Catches the slip at the right step.
