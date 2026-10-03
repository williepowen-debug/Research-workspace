# System-improvement bookmarks — curated for Will (2026-10-03, walter-f0)

Will asked (2026-10-03): *"look for anything I may have saved that would help with our system... system[-based] posts that might have things that would help our processes."*

Scanned the whole X-bookmark backlog (299 items, read-only) through a **system/process lens** instead of the financial-signal lens. Many posts I'd dispositioned as "off-domain agentic hype" are, for US specifically, operational signal — **the entire fleet runs on Claude Code**, so posts on CLAUDE.md overhead, token/context discipline, sub-agent orchestration, memory, skills, MCP and doc-handling bear directly on how we work.

⚠️ **Honesty caveat:** entries below are read off the bookmark's own text/thumbnail (+ expanded links); I have NOT opened the underlying talks/repos/PDFs. Treat as **candidate resources to evaluate**, not proven wins. Many are hype-wrapped ("worth more than a $500 course") around a real underlying artifact — the value is the artifact, not the tweet. **WALTER surfaces; DAEDALUS (fleet architect) / PROME / Will decide and own any change.** No seen-set touched; nothing auto-commissioned.

---

## TIER 1 — maps to a KNOWN pain point, substantive, worth acting on

| # | Source | What it is | Why it maps to us | Suggested owner |
|---|--------|-----------|-------------------|-----------------|
| #162 | @Mnilax (Boris Cherny / CC creator podcast) | **"9 patterns that waste 73% of your tokens"** — names 14% lost to CLAUDE.md before you type, 13% re-reading history, 11% from forgotten hooks | We auto-load **~107 KB every boot** (WALTER CLAUDE.md 65 KB + root 24 KB + memory index 18 KB) and have live read-cap/charter-bloat problems. This names the exact cost structure. | DAEDALUS / PROME |
| #96 | @0xCodila (Anthropic + Andrew Ng) | **90%-fewer-tokens via prompt caching** — put everything static at the top, mark the cache boundary (108k→11 tokens on a fixed doc) | Directly our read-cap/auto-load discipline. The "static-at-top, cache it" structure is a concrete charter-layout technique. | DAEDALUS |
| #151 | @dunik_7 | **CLAUDE.md optimization** — a 65-line file, mistake rate 41%→11% (headline) or 3% (body) across 30 codebases | Charter discipline. NB the poster himself flags the headline-vs-body gap — a built-in skepticism cue. | DAEDALUS |
| #220 | @hasantoxr | **Microsoft MarkItDown** — Python lib, PDF/Word/Excel/PPT/image/audio/YouTube → clean Markdown, 87K★, battle-tested | WALTER does heavy PDF/doc intake (pdfminer today). A robust converter could harden the intake pipeline + the X-bookmark media gap. | WALTER (own tooling) |
| #169 | @zodchiii | **CC reads `.env` before you type; one `settings.json` line blocks it; 29M secrets leaked on GitHub 2025** | 🔴 Direct security item: WALTER keeps X API tokens in `AGENTS/WALTER/.env`. Worth verifying our settings.json actually fences .env reads. | DAEDALUS / WALTER |
| #195 | @techxutkarsh | **"Agentic Design Patterns"** — 421-pg code-backed doc (prompt chaining, routing, memory, MCP, multi-agent coordination, guardrails) | A curriculum on exactly our architecture (multi-agent coordination + guardrails). High-potential reference for the fleet architect. | DAEDALUS |
| #159 | @adamghowiba | **JPMorgan "Ask David" multi-agent architecture** — supervisor agent + specialized subagents (retrieval/data/analytics) + LLM-as-judge reflection + human-in-loop | This IS our fleet's shape: PROME (supervisor) → domain subagents → RED (adversarial/judge) → Will (human-in-loop). Institutional validation + possible refinements. | PROME / DAEDALUS |
| #206 | @JoshKale | **Anthropic's internal Skills catalog — 9 categories** (library/API ref, product verification, data processing, …) | We use skills heavily; Anthropic's own taxonomy could sharpen ours. | DAEDALUS |

## TIER 2 — relevant to orchestration / memory / output discipline; evaluate

- **#152 @rubenhassid** — Anthropic 31-pg prompting guide: *positive instructions over negative* ("don't use jargon" fails), *always define the length cap*, *name every output*. → directly our output-discipline / STRICT_TEXT register.
- **#126 @slash1sol** — Guy Steele talk: *ban every big word until you've defined it*. → thematically identical to our OPERATOR_BRIEF "unpack jargon on first use." A teaching/validation resource.
- **#91 @Serantych** — Karpathy "Graph Engineering" for multi-agent systems: *agents forget; a graph remembers; parallel agents in separate worktrees*. → our file-memory + worktree orchestration.
- **#214 @karpathy** — the autoresearch repo (human iterates `prompt.md`, agent iterates `code.py`, ~630 lines). → the dynamic-workflow/loop pattern, from the source.
- **#216 @cblatts** — `/prompt` and `/review-plan` CC commands (brain-dump → instructions; agents critique a plan). → our proposal/cold-read/plan-review discipline.
- **#231 @doodlestein** — the one-line planning prompt ("single smartest, most accretive addition to this plan?") run across frontier models. → a cheap plan-hardening technique.
- **#215 @thejayden** — "building a Chief of Staff with Claude Code." → directly analogous to PROME.
- **#203 @om_patel5 / #210 @gregisenberg / #140** — Obsidian-as-persistent-brain, structured like a company with departments. → our AGENTS/ + memory structure (we already do a version of this).
- **#156 @zodchiii** — "Anthropic 2026 agent roadmap: tools, memory, **observability**." → observability maps to our doctor/telemetry.
- **#171 @eng_khairallah1** — MCP workshop from the MCP creator. → we run many MCP servers.
- **#189 @neogoose_btw** — fast index-free code search (tested on CC sources, 100k-file kernel, 500k-file chromium). → large-repo search.
- **#242 @MatthewBerman** — OpenClaw 21 use cases incl. an **"X Ingestion Pipeline"** + memory/knowledge-base systems. → literally what WALTER just built (bookmark intake) — worth a compare.
- **#245/#246** — Anthropic Academy 12 free courses (API, RAG, MCP, MCP servers). → reference/training.
- **#179 @AlfieJCarter** — CC "project brain file: what to put, what to leave out, auto-update." → CLAUDE.md discipline.

## Already flagged by the morning session (carry here so it's one list)
- **#70 anydoc** — fast PDF/DOCX parsing (pairs with #220 MarkItDown for the doc-intake pain point).
- **#84 = #96 above** — Anthropic/Ng token discipline.

## TIER 3 — hype / low-substance (named, not itemized)
A large cluster of "watch this lecture / worth more than a $500 course / make $10K/month / $750K/yr lecture" posts (e.g. #145/#146/#165/#170/#175/#176/#184/#200), generic finance-GitHub-repo roundups (#163/#180/#186 — TradingAgents etc., generic LLM-trading frameworks, not our system), and Polymarket/crypto trading-bot hype (#161/#197/#201). Low signal; skip unless a specific one is named.

## NOT system — stale financial (noted, not the focus)
Several months-old financial bookmarks surfaced in the scan (private-credit stress #185/#219/#228, Goldman/zerohedge macro #202/#227, Dodd-Frank mortgage EO #207, Bank OZK #194, NDFI loans #191, Jiangxi Bank #226). All Feb–Mar vintage and almost certainly absorbed by the owning desks; listed for completeness, not routed.

---

**Recommended next step:** route Tier 1 to **DAEDALUS** (fleet architect) as an evaluation queue, with the two security/tooling items (#169 .env fence, #220 MarkItDown) also relevant to WALTER's own pipeline. None of this is WALTER's to implement — it's surfaced for Will/DAEDALUS to pick from.
