---
name: Telegram Plugin Must Be WALTER-Project-Scope, Not User-Scope
description: Telegram plugin enablement belongs at AGENTS/WALTER/.claude/settings.json (project scope), never at ~/.claude/settings.json (user scope). User-scope enablement makes every claude session spawn its own bot, competing for the same bot token via getUpdates polling.
type: project
originSessionId: f6f9fd10-e477-47bc-86e2-7aa37af0abfd
---
The Telegram MCP plugin (`telegram@claude-plugins-official`) must be enabled ONLY at the WALTER project scope — specifically at `/home/willi/Research-workspace/AGENTS/WALTER/.claude/settings.json` under `enabledPlugins`. Never at `~/.claude/settings.json` (user scope).

**Why:** User-scope enablement is inherited by every claude session started on this machine. Every session then spawns its own `bun server.ts` process polling the same Telegram Bot API token. Telegram's `getUpdates` delivers each inbound message to ONLY one poller — so when multiple bots compete, ~50% of Will's Telegram messages get routed to non-WALTER sessions (e.g., REGINALD) and silently dropped. This was the root cause of the "Telegram inbound MCP delivery broken" bug flagged in commit `887b8d73` on 2026-04-22. Diagnosed and fixed 2026-04-24: moved telegram from `~/.claude/settings.json` → `AGENTS/WALTER/.claude/settings.json`, killed REGINALD's orphan bot (PID 65765).

**How to apply:** If you find `telegram@claude-plugins-official: true` in `~/.claude/settings.json` (user scope), move it to WALTER project scope. If another agent's project scope (REGINALD, SAM, etc.) has it enabled, remove it — per root CLAUDE.md only WALTER + PROME are on Telegram. Before declaring an inbound-delivery bug on Telegram, first check `ps -ef | grep bun.*telegram` — if more than one bot is running against the same token, that's the bug, not an MCP layer issue. Kill all but WALTER's bot, then verify scope config.
