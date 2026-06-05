---
name: Phone Signal Ingestion — Preferred Architecture
description: Will wants to send signals to WALTER from his phone; agreed target architecture is phone → GitHub API → Prome polls repo on OpenClaw
type: project
originSessionId: d2052482-afe1-4c35-bc58-66efbefeac82
---
Will wants reliable signal ingestion from his phone (Telegram MCP keeps dropping). Design discussion 2026-04-14 converged on a hybrid architecture.

**Target design:**
- Phone: iOS Shortcut POSTs signal to GitHub REST API, creating a file in `AGENTS/WALTER/inbox/incoming_<timestamp>.md` using a fine-grained PAT scoped to the Research-workspace repo only
- Coordinator: Prome on OpenClaw polls the inbox directory every ~30-60s, reacts to new signals, routes to correct agent inbox with priority
- No public endpoint on OpenClaw required — transport is GitHub, Prome only needs outbound git fetch

**Why this shape:**
- GitHub uptime as transport decouples ingestion from OpenClaw health
- Graceful degradation: if Prome is down, signals still land; Prome catches up when revived
- Eliminates TLS/Caddy/domain/public-port attack surface on OpenClaw
- Fine-grained PAT on phone limits blast radius to one repo

**How to apply:**
- Blocked on Prome revival (see OpenClaw/Prome Degraded memory)
- Once Prome is healthy, build polling loop on OpenClaw side first, then guide Will through iOS Shortcut + PAT setup on phone
- Alternative paths considered and rejected: webhook-on-OpenClaw (requires healthy public VPS), GitHub Actions + Claude API (more plumbing), GitHub-direct only (no autonomous processing)
