# LESSONS.md — Fleet-wide mistake patterns (root)

*If you catch yourself breaking one, stop. This is the ROOT file — every agent also keeps its own `AGENTS/<NAME>/LESSONS.md` for domain-specific patterns; those are what agent boot protocols read.*

**Updated:** 2026-08-29 (WQ-122 refresh, Will-approved *"approve all go"* — the 19 items that restated root `CLAUDE.md` Critical Rules / TERRY Non-Negotiables were cut to the pointer line below; the lessons that live nowhere else stay here, sharpened. Prior text verbatim → `git show 5e673abc0:LESSONS.md`.) · **Refresh trigger:** any spine audit that finds an item here contradicted by root canon → fix or cut the same session.

**Rules already in canon are NOT repeated here:** read-before-edit, mechanical-before-creative, deploy-then-wait, puts-on-green / roll-don't-trim (TERRY-owned), close-the-proposal-loop, verify-against-filings, live prices, scoped git, pull at boot → root `CLAUDE.md` Critical Rules + Git Protocol (reasons in `docs/CANON_PROVENANCE.md`); deploy-on-a-fired-trigger-never-the-calendar → `AGENTS/TERRY/RISK_RULES.md`; scrub-verify-by-content → auto-memory `finding_history_scrub_verify_by_content_not_pickaxe`.

---

## 🔴 Position management

1. **Don't override conviction with probabilistic hedging.** Recommended closing the CVNA put before earnings — the stock then dropped 20%. Implied moves are consensus, not ceilings. Don't talk Will out of a position unless the THESIS is broken.
2. **Two expiry frameworks — don't mix them.** Dateable single-name catalysts (PC names: APO, ARES, ARCC) → near expiry keyed to the catalyst. Macro/index (HYG, KRE, IWM) → Hamilton demand-destruction clock → far expiry. BRENT owns the Hamilton clock; BROCK owns the PC catalyst clock.
3. **Steelman the counter-case on every position — with a real probability.** Conviction without doubt is stubbornness; a thesis 90% right still needs a plan for the 10%. (Apr 1: WAL chart looked bullish; steelmanned honestly at 15–20% wrong — position unchanged, falsifiers sharpened.) **And separate intellectual honesty from position management:** articulating why you might be wrong doesn't mean you think you are. Flag the counter-case, assign it a probability, then trade the conviction — not the anxiety.

## 🟡 Verification

4. **Earnings dates come from company IR / the 8-K**, never from an agent's memory. (OZK wrong twice.)
5. **Test the thesis against the data, not the data against the thesis.**

## 🟡 Orchestration & process

6. **One spawn, one objective.** Agent context is finite; a bundled spawn does the first job and drops the second. (REGINALD P-002 bundled inbox processing + an EARNINGS_PREP upgrade — the inbox got done, the prep didn't move.)
7. **Dry-run prompts before batch deployment.** A single dry-run agent catches file-path errors (missing KB.tsv), date errors (TIC Mar 18 not Mar 15) and context gaps you can't see from outside.
8. **Inject confirmed data into later batches — don't make them re-search it.** Findings from batch N are confirmed context for batch N+1: saves tokens, prevents conflicting figures.
9. **Will's mid-session ideas → capture, don't execute.** Log them, finish the current priority.
10. **Flag LLM-inaccessible data for Will** (Google Trends, real-time dashboards, paywalled portals) so he doesn't spend prompts on sources that return garbage.
11. **Major data releases → a synthesis .md in the owning agent's domain folder**: the 5 things that matter for positions. Agents wake with no memory; curated context beats raw dumps.
12. **Audit the auto-loaded files regularly.** Only the `CLAUDE.md` files (root + `PROME/`) and the auto-memory `MEMORY.md` index are injected every message — the most expensive real estate in the system, and entries rot silently (Apr 3 audit: 6 stale entries, 3 duplicates, 5 dead paths → ~30% context reduction). `HEARTBEAT.md`, `AGENTS.md`, `USER.md`, `KERNELS.md` are explicit reads, not injected — audit them on cadence, not per message.
