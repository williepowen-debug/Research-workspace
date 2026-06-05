---
name: OpenClaw/Prome Degraded
description: OpenClaw VPS (where Prome coordinator runs) has been unreliable since Anthropic removed Will's subscription access; Prome revival is pending work
type: project
originSessionId: d2052482-afe1-4c35-bc58-66efbefeac82
---
OpenClaw — the VPS where Prome runs as network coordinator — has been degraded since Anthropic removed Will's ability to use his subscription on that machine. As of 2026-04-14, Prome is not reliably running.

**Why:** This affects any architecture that assumes Prome is live (file-based inbox polling, signal routing via Prome, real-time coordinator reactions). CLAUDE.md still describes the healthy-state architecture but operationally Prome can't be counted on right now.

**How to apply:**
- Don't assume Prome will pick up signals dropped into inboxes — they may sit until a Claude Code agent boots manually
- When designing new infrastructure (signal ingestion, inter-agent coordination), prefer paths that work without OpenClaw, or that degrade gracefully if Prome is down
- Reviving Prome is on Will's todo list (flagged 2026-04-14); re-check status rather than assume still broken
