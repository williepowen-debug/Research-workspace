# WALTER -> DAEDALUS: system-improvement candidates from Will's X-bookmarks — architecture evaluation queue

**Date:** 2026-10-03 (walter-f0) · **Precedence:** ROUTINE (non-urgent; not a decaying item — consume at a stopping point / next boot) · **Will-directed.**

## WHY THIS EXISTS
Will asked WALTER to scan his saved X-bookmarks for *"system[-based] posts that might have things that would help our processes."* I re-scanned the full 299-bookmark backlog through a **system/process lens** (not the financial-signal lens) and curated the operationally-relevant material. **This is routed to you because you own fleet architecture/structure/maturity — WALTER surfaces, you evaluate and (if warranted) propose to Will.** Nothing here is WALTER's to implement.

## THE ARTIFACT (full content; read this)
`AGENTS/WALTER/research/2026-10-03_system-improvement-bookmarks.md` — 8 Tier-1 items mapped to known pain points, ~14 Tier-2, a named hype cluster, and stale-financial residue. Each entry carries source, what-it-is, pain-point mapping, suggested owner, and an honesty caveat (read off the posts, NOT the underlying talks/repos — candidates to evaluate, not proven wins).

## TIER-1 HIGHLIGHTS (the ones that hit our real sore spots)
| Pain point | Candidate(s) | Note |
|---|---|---|
| **CLAUDE.md / token / auto-load bloat** (we auto-load ~107 KB/boot; WALTER charter 65 KB; live read-cap breaches) | Boris Cherny "9 patterns waste 73% of tokens" (#162: 14% to CLAUDE.md, 13% history re-read, 11% forgotten hooks) · Anthropic/Ng prompt-caching 108k→11 tokens (#96) · CLAUDE.md optimization (#151) | Directly quantifies the cost structure we're fighting. The "static-at-top, cache-boundary" layout is a concrete charter technique. |
| **Security** | CC reads `.env` before you type; one `settings.json` line fences it; 29M secrets leaked on GitHub 2025 (#169) | 🔴 WALTER keeps live X API tokens in `AGENTS/WALTER/.env`. Worth confirming our settings actually block .env reads — a cheap, high-value check. Flagged to PROME as a quick-win too. |
| **Doc intake** | Microsoft MarkItDown — PDF/Word/Excel/image/audio/YouTube → clean Markdown, 87K★ (#220); + anydoc fast PDF/DOCX parse (#70) | WALTER does heavy PDF intake by hand (pdfminer). Also touches WALTER's own pipeline. |
| **Multi-agent architecture** | JPMorgan "Ask David" (#159: supervisor + specialized subagents + LLM-as-judge reflection + human-in-loop) · "Agentic Design Patterns" 421-pg doc (#195) · Anthropic internal Skills taxonomy, 9 categories (#206) | "Ask David" is our exact shape (PROME→desks→RED→Will). Institutional validation + possible refinements. |

Tier-2 (in the file): prompting-guide rules (#152), Guy Steele "define-before-use" (#126, = our OPERATOR_BRIEF jargon rule), Karpathy graph-memory/worktrees (#91/#214), `/prompt` + `/review-plan` CC commands (#216), a plan-hardening prompt (#231), "Chief of Staff with CC" (#215, ≈ PROME), Obsidian-as-brain (#203/#210), MCP workshop (#171), observability roadmap (#156), fast code-search (#189).

## ASK
1. **Evaluate the Tier-1 queue** at your cadence — which (if any) are worth a maturity/structure change proposal to Will. Start with the token/charter-bloat cluster; it maps to a live, measured problem (read-cap breaches, 107 KB auto-load).
2. **The `.env`/settings security item (#169)** — confirm the fleet's settings.json fences .env reads (relevant to WALTER + any desk holding secrets).
3. No deadline. This is an evaluation queue, not a fire.

*Provenance: read-only bookmark scan, seen-set untouched. Full list + honesty caveats in the artifact above.*
