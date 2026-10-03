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

---

## 🔴 CORRECTION ADDENDUM 2026-10-03 (CATO review, relayed by Will) — corrected inventory + per-candidate bounded comparisons

⚠️ **My original Tier-1 OVERSTATED the "gaps" — my inventory missed existing desk tools. Corrected:**

**We are NOT missing these capabilities; the question is whether the candidates IMPROVE the existing route. Evaluate as improvements, not gap-fills.**

### Candidate A — `financial-datasets` MCP (financialdatasets.ai) [fundamentals]
- **Existing route:** DEWEY `scripts/edgar_doc.py` `xbrl_concept()` — structured SEC/XBRL financials (val/fy/fp/form/filed) via the SEC company-concept API. **Free, authoritative (filings), US-only, needs XBRL concept tags.**
- **What it could improve:** easier NORMALIZATION (pre-computed ratios, e.g. P/E, vs raw XBRL), BROADER COVERAGE (crypto, non-US, non-SEC), FASTER research (one query vs XBRL navigation).
- **Desk that benefits:** DEWEY (research), REGINALD (bank earnings), VULCAN (hyperscaler FCF/capex), CARL (consumer-co fundamentals).
- **One bounded comparison:** take ONE task a desk recently did via `edgar_doc.py` (e.g. a bank reserve ratio or a hyperscaler capex line); run the same query through financial-datasets; compare (1) agreement with the actual filing, (2) latency, (3) effort. Adopt only if it matches the filing with less effort; if it diverges from the filing, DEWEY's SEC route stays authoritative. Cost: paid API.

### Candidate B — options chains + Greeks API [options]
- **Existing route:** TERRY `scripts/chain_fetch.py` (live chain via yfinance — **IV present, delta/theta ABSENT from source**) + `scripts/greeks.py` (Black-Scholes, **FLAT vol, European, manual skew** — Greeks COMPUTED, not market-supplied). Real limits: computed Greeks under simplified assumptions; chain may be delayed.
- **Options-API IDENTIFICATION (CATO priority b):** the exact @JasonL_Capital tool is **UNIDENTIFIED** — hidden behind a video (thumbnail = Claude logo) + a "first-comment" reply too old for recent-search. **Class identified by web search:** leading candidate **Public.com MCP** (`get_options_chain`, `get_option_greeks`, `place_order` — broker-integrated, supplied Greeks, real-time if funded, but broker-tied + CAN PLACE ORDERS = safety concern); free alternatives **OptionsFlow MCP (twolven)** — but it COMPUTES Greeks (same as TERRY, **no gain**) — and **options-chain MCP (blake365)** — free tier **15-min DELAYED** (**worse**); **FlashAlpha** (40 tools, dealer positioning + vol surface + full Greeks, likely paid). ⇒ **The "supplied-Greeks" improvement over TERRY exists ONLY in the paid/broker class; a "free" options feed is either computed (no gain) or delayed (worse).** Could not retrieve official docs for the exact promoted tool — it is unnamed.
- **What it could improve:** a reliable, TIMESTAMPED feed with MARKET-SUPPLIED delta/theta (vs TERRY's BS-computed, flat-vol, manual-skew Greeks) — better accuracy for construction + monitoring, esp. where skew matters.
- **Desk that benefits:** TERRY (trade construction + position monitoring on the live options book).
- **One bounded comparison:** take ONE live position (e.g. QQQ 735P Oct-5, or VLO options); pull supplied delta/theta from the candidate feed AND compute via `greeks.py`; compare the Greeks + timestamp. Genuine improvement only if the feed SUPPLIES market Greeks (not re-computed BS), is real-time, and differs materially from TERRY's (esp. under skew). If it computes the same BS way or is delayed → no gain.

### Candidate C — `last30days-skill` (disler/mvanhorn) [research]
- **Existing route:** WALTER RESEARCH-INTAKE lane + DEWEY deep research.
- **What it could improve:** parallel multi-source (Reddit/X/YouTube/HN/Polymarket/web) + an engagement/"real-money" ranking signal — breadth + a different ranking axis.
- **Desk:** WALTER (intake), DEWEY (deep research).
- **One bounded comparison:** run ONE real research question we've already answered through last30days-skill AND our existing route; compare the EVIDENCE surfaced — did it find a load-bearing primary we missed, or just more volume? **More sources + engagement scoring do NOT establish better evidence** (CATO); the test is missed-primary recovery, not count.

### Candidate D — `ai-hedge-fund` (virattt) / `TradingAgents` (TauricResearch) [architecture reference]
- **CORRECTED:** drop my "we're already past these / perform better" claim — **unproven; similar structure does not prove our system performs better** (CATO). Keep as **architecture REFERENCE only** (like the JPM "Ask David" piece).
- **One bounded comparison (reference, not performance):** run one ticker through ai-hedge-fund; compare its decision-DECOMPOSITION + disagreement-handling to how our fleet structures the same — as an architecture learning, NOT an outcome claim.

**⛔ No installation, no paid trial yet** — these are evaluate-first. Further bookmark-cluster browsing is HELD per CATO.
