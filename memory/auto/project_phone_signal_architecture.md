---
name: Phone Signal Ingestion — Preferred Architecture
description: Will wants reliable phone→fleet signal ingestion (Telegram drops); the GitHub-as-transport idea shipped as the RESEARCH-INTAKE lane (GitHub Actions), NOT the originally-planned OpenClaw poller (cut 6/26); the phone leg (iOS Shortcut→GitHub API) remains UNBUILT
type: project
originSessionId: d2052482-afe1-4c35-bc58-66efbefeac82
---
Will wants reliable signal ingestion from his phone (Telegram MCP was dropping messages). A 2026-04-14 design discussion converged on a **GitHub-as-transport** hybrid. **Refreshed 2026-07-05: the coordinator half is obsolete, the transport half shipped as a different mechanism, the phone leg is still unbuilt.**

**Original 2026-04-14 design (for the record):**
- Phone: iOS Shortcut POSTs to the GitHub REST API, creating `AGENTS/WALTER/inbox/incoming_<ts>.md` via a fine-grained PAT scoped to this repo only.
- Coordinator: **Prome-on-OpenClaw** polls the inbox every 30–60s and routes. ⚰️ **DEAD — OpenClaw/VPS was cut 2026-06-26; there is no always-on Prome** (serial CC sessions on Will's box now). See [[finding_injection_claim_is_openclaw_vestige]].
- Core insight (still sound): GitHub uptime as transport decouples ingestion from any live server; graceful degradation — signals land even if the processor is down.

**What actually shipped — the successor:**
The GitHub-as-transport pattern became the **RESEARCH-INTAKE collection lane** ([[project_research_intake_collection_lane]]): GitHub Actions write to a private repo, agents read it read-only. Notably the April memo *rejected* "GitHub Actions + Claude API" as "more plumbing" — but once OpenClaw's healthy-VPS assumption died, that became the right (and only) path.

**Still open — the phone leg:**
The iOS-Shortcut → GitHub-API → inbox leg was **never built** (blocked on the old "Prome revival," then the coordinator model changed). The want may persist (Telegram is still the primary research channel; unverified whether it still drops).

**Modern shape if revisited (no always-on poller):**
Phone → iOS Shortcut → GitHub API → a file in the RESEARCH-INTAKE repo (or WALTER inbox) → picked up by the intake lane's next scheduled run / the next agent boot. This *is* the graceful-degradation model the April design wanted — just with GitHub Actions doing what OpenClaw-Prome would have. Route any actual build through the messaging overhaul ([[project_messaging_overhaul]]), not an inbox/outbox patch.

**Status:** design archaeology + one live open want (phone ingestion). Not scheduled. Rejected alternates (April): OpenClaw webhook (needs a live public VPS), GitHub-direct-only (no autonomous processing).
