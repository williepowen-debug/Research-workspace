---
name: Telegram Plugin Must Be WALTER-Project-Scope, Not User-Scope
description: Telegram plugin enablement belongs at AGENTS/WALTER/.claude/settings.json (project scope), never at ~/.claude/settings.json (user scope). User-scope enablement makes every claude session spawn its own bot, competing for the same bot token via getUpdates polling.
type: project
originSessionId: f6f9fd10-e477-47bc-86e2-7aa37af0abfd
---
The Telegram MCP plugin (`telegram@claude-plugins-official`) must be enabled ONLY at the WALTER project scope — specifically at `/home/willi/Research-workspace/AGENTS/WALTER/.claude/settings.json` under `enabledPlugins`. Never at `~/.claude/settings.json` (user scope).

**Why:** User-scope enablement is inherited by every claude session started on this machine. Every session then spawns its own `bun server.ts` process polling the same Telegram Bot API token. Telegram's `getUpdates` delivers each inbound message to ONLY one poller — so when multiple bots compete, ~50% of Will's Telegram messages get routed to non-WALTER sessions (e.g., REGINALD) and silently dropped. This was the root cause of the "Telegram inbound MCP delivery broken" bug flagged in commit `887b8d73` on 2026-04-22. Diagnosed and fixed 2026-04-24: moved telegram from `~/.claude/settings.json` → `AGENTS/WALTER/.claude/settings.json`, killed REGINALD's orphan bot (PID 65765).

**How to apply:** If you find `telegram@claude-plugins-official: true` in `~/.claude/settings.json` (user scope), move it to WALTER project scope. If another agent's project scope (REGINALD, SAM, etc.) has it enabled, remove it — per root CLAUDE.md only WALTER + PROME are on Telegram. Before declaring an inbound-delivery bug on Telegram, first check `ps -ef | grep bun.*telegram` — if more than one bot is running against the same token, that's the bug, not an MCP layer issue. Kill all but WALTER's bot, then verify scope config.

---

**SECOND FAILURE MODE — found 2026-09-10 (WALTER, Will: "have not been able to [reach WALTER via Telegram] for a while"): INBOUND IS GATED BY A LAUNCH FLAG, NOT BY THE TOKEN OR THE ALLOWLIST.** Claude Code 2.1.x (observed at 2.1.267) only delivers `<channel>` notifications from an MCP channel server if the session was launched with that server in its `--channels` list. The harness log says exactly this: `Channel notifications skipped: server plugin:telegram:telegram not in --channels list for this session` (`~/.cache/claude-cli-nodejs/-home-willi-Research-workspace-AGENTS-WALTER/mcp-logs-plugin-telegram-telegram/<ts>.jsonl`). **Symptoms:** outbound `reply` works; the phone shows the bot "typing" (the plugin's server received the message and acked it) but nothing reaches the session; `getUpdates` shows zero queued updates because the poller consumed them. Token valid at `getMe`, no webhook, single poller — every classic check passes.

**Fix (plugin README v0.0.7 step 4):** launch WALTER with
```
cd ~/Research-workspace/AGENTS/WALTER && claude --channels plugin:telegram@claude-plugins-official
```
(plus `--dangerously-skip-permissions` as usual). A session launched without the flag cannot be fixed in place — restart it. **Launch-only: no settings.json equivalent exists (claude-code-guide, 2026-09-10), and the flag is absent from `claude --help` (research-preview feature).** The MCP server's scoped name `plugin:telegram:telegram` in the log is NOT the flag value; the flag takes `plugin:<name>@<marketplace>`. **Timeline:** inbound last worked 2026-08-28 (image batch landed), recorded broken at the 2026-09-06 closeout; the gate arrived with a Claude Code update in that window, not with any change to the token, `access.json` (Will's ID 8463631023 is allowlisted, DMs `allowlist` policy) or the plugin cache (0.0.7, 2026-08-13).

**How to apply:** before diagnosing Telegram inbound, `grep -h "Channel notifications skipped" ~/.cache/claude-cli-nodejs/*/mcp-logs-plugin-telegram-telegram/*.jsonl | tail -1` — if it prints, the fix is the launch flag, nothing else. The launch line belongs in `PROME/MACHINE_LOCAL.md` (PROME-owned; flagged 2026-09-10).
symptoms: telegram inbound not received; bot shows typing but no reply; outbound works inbound dead; Channel notifications skipped; not in --channels list
