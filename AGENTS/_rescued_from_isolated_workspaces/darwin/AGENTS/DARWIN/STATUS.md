# STATUS.md - Darwin Scan Results

**Last scan:** 2026-02-19 00:49 UTC
**Next scan:** 2026-02-20

---

## 🔥 HOT — Act on these now

### 1. Claude Sonnet 4.6 dropped Feb 17 ✅ CONFIRMED
**Source:** Anthropic blog, Simon Willison (Feb 17), HN (confirmed)
**What:** Flagship model. Performance similar to Opus 4.5 at Sonnet pricing ($3/$15 per million tokens). Default 200K context, 1M in beta. Adaptive thinking API. No longer supports prefill/prefix. Knowledge cutoff: August 2025.
**Confirmed by:** Simon Willison released llm-anthropic 0.24 the same day with Sonnet 4.6 + Opus 4.6 support.
**Migration notes:** New `adaptive_thinking` parameter. Prefix prefill removed. See [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide).
**Backlog:** Still at P0 — upgrade config to `claude-sonnet-4-6`

---

### 2. Qwen 3.5 released Feb 17 — open-weight competitor
**Source:** Alibaba Cloud, multiple reports
**What:** Qwen3.5-397B-A17B (open-weight) + Qwen3.5-Plus (hosted). 1M token context. Expanded agentic AI features. Explicitly benchmarks against GPT-5.2 and Claude 4.5. Cost significantly lower than proprietary alternatives.
**Why it matters:** First serious open-weight 1M-context model competitive with frontier closed models. Could change cost calculus for high-volume agent workflows.
**Add to BACKLOG:** Evaluate Qwen3.5 as cost fallback for bulk/long-context research tasks.

---

### 3. unbrowse-openclaw — API skill generator for OpenClaw
**Source:** GitHub (336 stars, OpenClaw-specific) — *carried from last scan*
**Status:** Still P0 — install and test if any workflows use browser

---

## 👀 WATCH — Promising, needs more assessment

### 4. llms.txt movement gaining traction
**Source:** HN #2 (752pts), Anna's Archive blog post (Feb 18)
**What:** Sites are publishing structured `llms.txt` files that tell AI agents HOW to access their data programmatically (bulk download URLs, APIs, auth flows) instead of scraping. Anna's Archive example explicitly greets LLMs and offers SFTP access for donations.
**Why it matters:** This is the web learning to speak to agents natively — opposite direction from WebMCP (agents speaking to sites). If Darwin's research workflows involve scraping sites, checking for `llms.txt` first saves tokens and avoids CAPTCHAs.
**Try it:** Add `<baseurl>/llms.txt` to any site Darwin regularly scrapes. Check https://llmstxt.org for the spec.

---

### 5. WebMCP — Chrome ships browser-native MCP for agents
**Source:** VentureBeat, DEV.to, webmcp.link (Chrome 146, ~2 weeks ago) — *carried*
**Status:** Still early adoption. Worth monitoring. Not widely deployed yet.

---

### 6. GitHub Agentic Workflows — technical preview
**Source:** GitHub Blog (Feb 13) — *carried*
**Status:** P1 — worth signing up for preview

---

### 7. Tailscale Peer Relays — now GA
**Source:** HN #13 (309pts, Feb 18)
**What:** Peer relays are now generally available in Tailscale — allows secure relay of traffic between nodes without full mesh VPN. Relevant if Darwin/Prome run distributed agents.
**Why it matters:** Lower-latency, more reliable inter-agent networking. If we ever spin up distributed agent nodes, this is the networking layer.
**Effort:** Low (already available)

---

### 8. Agent governance tooling emerging
**Source:** BiometricUpdate (Feb 18), multiple enterprise sources
**What:** Tailscale + Saviynt offering production-ready agent governance: centralized API key custody, identity-based access, LLM session history, tool-call audit trails.
**Why it matters:** Sign of the ecosystem maturing. "From experimentation to production" narrative. If Darwin expands scope, governance becomes relevant.

---

## ⬇️ NOISE — Filtered out

- **AI Productivity Paradox (Fortune/HN #3, 763pts):** CEOs saying AI hasn't improved productivity (Solow paradox). Counternarrative noise. Not actionable.
- **"LLMs are eating specialty skills" (Martin Fowler):** Interesting directional thought, not actionable.
- **SaaSpocalypse narrative (FinancialContent):** Hyperbolic but directionally correct. Monitor, don't act.
- **arXiv papers (Feb 17-18):** No novel agent infrastructure papers — domain-specific applications only.
- **Canva LLM SEO strategy:** Not relevant to our use case.

---

## System Notes

- **Rate limiting:** Brave Search API rate-limits at 1 req/s. Space searches 2-3s apart.
- **GitHub trending:** JS-rendered, unfetchable directly. Use GitHub Search API instead.
- **arXiv listing:** `/list/cs.AI/recent` returns IDs only. Use search endpoint with queries.
- **Simon Willison blog:** Confirmed as excellent daily signal — add to SOURCES.md Tier 1.
- **Claude prefix prefill:** Removed in Sonnet 4.6. Update any prompts that use this pattern.
