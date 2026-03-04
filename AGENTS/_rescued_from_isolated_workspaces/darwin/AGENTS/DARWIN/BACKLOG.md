# BACKLOG.md - Darwin's Improvement Proposals

Items are ordered within priority tier. Add new items with date and source.

---

## 🔥 P0 — Try immediately, low effort

### [2026-02-18] Upgrade to Claude Sonnet 4.6
**What:** Switch from claude-sonnet-4-5 to claude-sonnet-4-6
**Why:** 1M context window, better agent tool selection, improved error correction. Same price. Released yesterday. We're already one model behind.
**Effort:** Low (config change)
**Value:** High (1M context alone is transformative for long research sessions)
**Try it:** Check OpenClaw config for model setting. Change to `claude-sonnet-4-6`. Enable 1M context window via API beta opt-in if available.
**Source:** HN #2, Anthropic blog

---

### [2026-02-18] Install unbrowse-openclaw plugin
**What:** API skill generator that captures browser traffic and replays as direct API calls
**Why:** If any of Darwin/Prome's workflows involve browser-based data collection, this replaces slow browser automation with fast direct API calls. OpenClaw-native. One command to install.
**Effort:** Low (one install command + one capture session)
**Value:** High (claimed 100x speedup for browser workflows; less fragility)
**Try it:**
```bash
openclaw plugins install @getfoundry/unbrowse-openclaw
openclaw gateway restart
# Then: unbrowse_capture { "urls": ["target-site.com"] }
```
**Source:** GitHub lekt9/unbrowse-openclaw

---

### [2026-02-18] Install planning-with-files skill
**What:** Persistent markdown planning state across sessions (Manus pattern)
**Why:** Multi-step research projects lose context on session restart. This skill creates persistent PLAN.md, PROGRESS.md, NOTES.md files. `/plan:status` gives instant project overview. 14K stars in <24h.
**Effort:** Low (skill install)
**Value:** High (better continuity on long research projects, session recovery)
**Try it:** Ask Prome: "Want me to try the planning-with-files skill for our research projects?" Install via OpenClaw skill install from OthmanAdi/planning-with-files
**Source:** GitHub OthmanAdi/planning-with-files

---

## 🟡 P1 — Evaluate this week

### [2026-02-18] Assess WebMCP adoption for browser-based research
**What:** Chrome 146's WebMCP lets websites expose structured agent tools via browser API
**Why:** 89% token efficiency improvement over screenshot-based browser automation. As sites adopt this, Darwin's web research becomes cheaper and more reliable.
**Effort:** Low (just watch + test on Chrome 146)
**Value:** Medium now, High as adoption grows
**Try it:** Check if any of our commonly-scraped sources support WebMCP. Test Chrome 146 with a site that has `toolname`/`tooldescription` HTML attributes.
**Source:** Chrome 146, W3C spec at webmcp.link

---

### [2026-02-18] Sign up for GitHub Agentic Workflows preview
**What:** Markdown-based repo automation powered by Claude Code / Copilot in GitHub Actions
**Why:** If Prome's research repos live on GitHub, automated triage, docs sync, CI fixes, and test improvements — all in plain Markdown. Strong guardrails (read-only by default).
**Effort:** Low (sign up), Medium (write first workflow)
**Value:** Medium (depends on how much GitHub repo work we do)
**Try it:** Check https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/ — sign up for preview.
**Source:** GitHub Blog

---

### [2026-02-18] Review microsoft/skills for reusable patterns
**What:** 131 agent skills + MCP configs + Agents.md templates from Microsoft
**Why:** Source of reusable MCP server configs and Agents.md patterns we could adapt for Darwin/Prome without building from scratch.
**Effort:** Low (read-only review)
**Value:** Medium (may surface skills or patterns worth copying)
**Try it:** `npx skills add microsoft/skills` to browse catalog. Look specifically at `mcp-builder` and `github-issue-creator` skills.
**Source:** GitHub microsoft/skills

---

## 🔵 P2 — Keep on radar

### [2026-02-18] Monitor HackMyClaw / OpenClaw prompt injection research
**What:** Active public challenge ($100 bounty) attacking OpenClaw agents via email prompt injection
**Why:** Real-world attack vectors against OpenClaw are being discovered and tested publicly. Darwin is an OpenClaw agent and may face similar attacks. Understanding what works helps us harden system prompts.
**Effort:** Low (monitor /log.html periodically)
**Value:** Medium (security intelligence; no immediate action needed)
**Try it:** Watch https://hackmyclaw.com/log.html for successful attacks. Read any post-contest writeups.
**Source:** HN #24 (318pts)

---

### [2026-02-18] Evaluate mem0 as persistent memory layer
**What:** Universal memory layer for AI agents (47K stars, actively developed)
**Why:** Darwin and Prome currently use file-based memory. mem0 offers structured, searchable, agent-optimized memory with APIs. Could be an upgrade path.
**Effort:** Medium (integration)
**Value:** Medium (file-based memory is working; mem0 adds search/retrieval structure)
**Try it:** Read https://github.com/mem0ai/mem0 — check if there's an OpenClaw plugin or MCP server. Look at API.
**Source:** GitHub top LLM repos

---

### [2026-02-18] Explore 1M context window use cases
**What:** Claude Sonnet 4.6 beta offers 1M token context via API
**Why:** 1M tokens ≈ 750K words ≈ entire codebases, long research corpora, many-session histories. Enables qualitatively different workflows.
**Effort:** Low (experiment)
**Value:** High (if we find workflows that need it)
**Try it:** After upgrading to 4.6, test: loading an entire research corpus into context vs RAG, multi-session history synthesis, large-scale code review.
**Source:** Anthropic Sonnet 4.6 release

---

## 🔵 P2 — Keep on radar (continued)

### [2026-02-19] Evaluate Qwen3.5 as cost fallback for bulk tasks
**What:** Qwen3.5-397B-A17B (open-weight) + Qwen3.5-Plus (hosted). 1M context. Agentic features.
**Why:** Significantly cheaper than Claude for high-volume or long-context research. Open-weight version can self-host. Competitive on benchmarks with frontier closed models.
**Effort:** Low (evaluate), Medium (integrate)
**Value:** Medium (cost savings if we ever do bulk research runs)
**Try it:** Test Qwen3.5-Plus via Alibaba Cloud's Model Studio. Compare output quality on our specific tasks.
**Source:** Multiple sources, Feb 17-18 2026

---

### [2026-02-19] Check for llms.txt on commonly-scraped sources
**What:** Sites are publishing `llms.txt` files with structured agent-friendly access instructions — bulk download URLs, APIs, auth flows.
**Why:** Saves tokens, avoids CAPTCHAs, more reliable than scraping. Anna's Archive is an early adopter. More sites will follow.
**Effort:** Very low (just append `/llms.txt` to target URLs)
**Value:** Medium (any site that has it = free research speedup)
**Try it:** Check Darwin's top research targets for `<baseurl>/llms.txt`. See https://llmstxt.org for spec.
**Source:** HN #2 (752pts), Feb 18 2026

---

## ✅ Done / Archived

*(Nothing yet — first scan 2026-02-18)*

---

## 📋 Backlog Notes

- Items move from P2 → P1 → P0 as evidence mounts
- When Prome approves a P0 item, move it to Done after completion
- Budget items go to Will for approval before acting
- Darwin re-scans weekly; add `[scan date]` to each item
