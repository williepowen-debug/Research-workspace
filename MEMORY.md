# MEMORY — Durable Kernels

**Last Updated:** 2026-06-14

**Positions → `PROME/POSITIONS.md`** | **Agent roster → `AGENTS_DIRECTORY.md` / `AGENTS.md`** | **Background → `WILL/BACKGROUND.md`**
**Pre-prune archive:** `memory/archive/MEMORY_ROOT_PRE_PRUNE_2026-06-14.md`

---

## CORE DISCOVERIES

- **Blue Owl Dual Gating** — PE-insurer transmission is confirmed: gates plus related-party insurer asset transfers are the private-credit dump pattern to watch. Treat Blue Owl→Kuvare, Ares→IHAM, Apollo→Athene, KKR→Global Atlantic as the 2026 SIV analog set. → `AGENTS/BROCK/STATUS.md`
- **LABOR Shadow Adjustment** — Reported claims can be materially suppressed by administrative/data timing; use LABOR’s shadow-adjustment framework before treating claims as clean labor truth. → `AGENTS/LABOR/STATUS.md`
- **CCC/HY Ratio Downgraded** — CCC OAS is concentrated, not a standalone 2007-style systemic signal. Watch transmission channels (CLO→BDC→insurance, private credit→banks) rather than CCC alone. → `FORGE/timing/thesis/CHANGELOG.md`
- **Timing Thesis Codified** — Central working clock remains May-Jul acceleration test, Q4 cascade risk, Q1-Q2 2027 peak selling. Treat this as falsifiable timing framework, not truth; current tape/substance divergences stress-test it. → `FORGE/timing/thesis/`
- **Physical Supply Clocks Matter** — Hard physical depletions create nonlinear deadlines that financial tape may ignore until late. Use current FORGE/agent files for active clocks; do not boot from old clock lists. → `FORGE/research/SEVEN_DEPLETION_CLOCKS.md`
- **PE-Insurer Wholesale Funding** — PE-insurer fragility includes fast-fuse wholesale funding (FHLB/FABR/repo-like liabilities), not just asset marks. Funding pullability is the transmission accelerator. → SHADE domain + `FORGE/timing/research/`
- **Energy Physical/Price Divergence** — Energy infrastructure/chokepoint damage can remain structurally bullish even when Brent prices de-escalation. Do not treat falling crude as physical-system repair; route current truth through BRENT/HAWK/HEARTBEAT. → `FORGE/research/iran-war/`, `AGENTS/BRENT/STATUS.md`, `AGENTS/HAWK/STATUS.md`
- **Hamilton Energy-Credit Framework** — Oil/gas shocks transmit through GDP drag and behavioral breakpoints with lags; credit can peak before equity. The failed HYG Jun→Dec roll proved that timing frameworks need execution rails, not just correct macro logic. → `FORGE/research/DEMAND_DESTRUCTION_FRAMEWORK.md`
- **Fed Stealth Liquidity** — Surface calm can be intervention working, not system health. Treat Fed/Treasury bill absorption, reserves, and repo plumbing as regime modifiers before reading calm tape as clean risk appetite. → `FORGE/research/FED_TBILL_REPO_ANALYSIS.md`
- **IHAM Hidden Leverage Template** — PE-CLO/BDC stress can hide in Level 3 subsidiaries, first-loss notes, parent cash support, and insider rotation away from credit risk. Verify subsidiary economics before trading parent narratives. → `AGENTS/BROCK/trade/ARES/sources/IHAM_FINANCIALS_FY2025.md`
- **PC Contagion Mechanics** — Core chain: gate → cash substitution → financing tighten → honest marks → CLO spillover → bank impairment. Agent “stage” labels use different ontologies; reconcile vocabulary before acting. → `AGENTS/BROCK/research/PC_CONTAGION_MECHANICS.md`
- **CARL Path C** — Housing/consumer stress can crack before employment, creating parallel stress paths rather than a clean labor-first sequence. → `AGENTS/CARL/STATUS.md`
- **UST Foreign-Buyer Stigma** — Geopolitical threats/stigma can turn reserve diversification from economics into political cover, especially across Japan/China/Korea/Gulf anchors. Treat TIC/FX/BOJ/Gulf flows as a combined demand-hole watch. → `AGENTS/ZHAO/STATUS.md`, `AGENTS/SAM/STATUS.md`, LIQUID domain
- **Japan Structural Shift** — Japan is a multi-year buyer-regime shift, not a single meeting/FY-end event. Life-insurer hedged returns, BOJ policy, and carry unwind are the real mechanisms. → `AGENTS/SAM/research/JAPAN_FYEND_REPATRIATION.md`, `AGENTS/SAM/STATUS.md`
- **WAL + OZK Complementary Shorts** — WAL is fast-transmission (losses bypass delinquency pipeline into P&L); OZK is reservoir (losses accumulate behind structures/reserves). Different failure modes require different expiry logic. → `AGENTS/REGINALD/STATUS.md`, `AGENTS/OZK/`
- **FSK Q1 Confirms BDC Vehicle Stress** — FSK provided second public BDC vehicle-level stress confirmation after Blue Owl gates. Broad public-credit cascade still requires HY OAS / VIX / bank transmission. → `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`, BROCK domain
- **WAL Mgmt Credibility Gap** — WAL management guidance can lag already-visible loss velocity; maintain idiosyncratic/Q2-print gating rather than broad bank-cohort assumptions. → `AGENTS/REGINALD/STATUS.md`

---

## THESIS FRAMEWORK

- **NDFI Bridge Verified** — Bank exposure to non-depository financial institutions is the private-credit-to-bank bridge (Chain 2 → Chain 1). Use REGINALD for current NDFI loss ranges and concentration. → REGINALD domain (`NDFI_HIDDEN_CRE_HYPOTHESIS.md`)
- **Ag Labor Data Gap** — USDA Ag Labor Survey and DOL NAWS cancellations create a permanent official-data blind spot. Use indirect signals (H-2A, self-deportation, produce prices) rather than assuming absence of evidence. → `AGENTS/MARCO/STATUS.md`
- **Labor Headline Composition Risk** — Headline payroll beats can mask deterioration when concentrated in healthcare, strike returns, government, or revisions. Inspect composition before updating labor thesis. → `AGENTS/LABOR/STATUS.md`

---

## SYSTEM ARCHITECTURE

*Operating procedures live in `PROME/BOOT.md` / `PROME/CLOSEOUT.md`; tool details live in `TOOLS.md`. Only durable lessons below.*

- **Persistent Agents — Do Not Spawn** — Persistent agents have their own workflows; do not casually spawn replacements. Use `AGENTS.md` as the current source for spawn restrictions and roster. → `AGENTS.md`
- **Real Agent-Work Surface Is Claude Code** — Will mainly works with domain agents by spawning Claude Code sessions on desktop/laptop; the VPS/OpenClaw layer is primarily PROME’s Telegram-accessible orchestration/interface layer. Therefore WALTER delivery to agent files must be committed/pushed to origin before those Claude Code sessions can see it, even for agents that also exist in OpenClaw.
- **Claude Subscription Economics Govern Architecture** — Will prefers Claude Code under the flat $200/month subscription because token cost anxiety disappears. Anthropic API on VPS is technically feasible but economically wrong for this setup because it reintroduces metered billing. Treat Claude-grade work as desktop/laptop Claude Code; treat VPS/OpenClaw as Codex/Prome orchestration unless Will explicitly changes the cost model.
- **Agent Domain-Only Edit Standard** — Will’s agents are expected to edit only files inside their designated domain unless Will explicitly approves otherwise. Merge/push hygiene should assume domain-scoped pathspecs are the normal workflow, not an exceptional restriction.
- **Verify Agent-Reported Data Against Filings** — Agent-reported numbers can hallucinate; cross-check any trade-relevant data against primary filings/source documents before acting. → root `CLAUDE.md` Critical Rule #3
- **News Sweep Exists, But Tools Own Details** — Thesis-tagged news monitoring is live; operational commands/config belong in `TOOLS.md` and `FORGE/tools/news-sweep/`, not root memory.
- **Dealer Capacity Nonlinearity** — Dealer constraints make Treasury clearing nonlinear under flow shock; SLR/eSLR policy can be decisive. Use source research for current numbers. → `FORGE/timing/research/DEALER_CAPACITY_RESPONSE_1B_PERPLEXITY.md`
- **Domain Audits via Cold Subagent Are High Value** — A cold-boot agent reading a full domain catches staleness, orphan files, and evidence gaps the daily operator misses.
- **Three-Source Convergence Method** — Use Perplexity + Claude + Gemini/deep research where warranted; weight by methodology quality and primary-data citations, not confidence tone.
- **CHANGELOG-First Workflow** — Thesis/framework files should not silently drift. Major thesis edits need a changelog entry or explicit audit trail first.
- **Prome Confidence ≠ Prome Knowledge** — Tone does not imply coverage. Flag blind spots and stale dependencies proactively.
- **Execution-Rails Are Part of the Framework** — A thesis without pre-registered ladders, branches, or named decision triggers is still only a hypothesis. The missed HYG Jun→Dec roll is the canonical failure mode. → BROCK LESSONS #16, `PROME/HANDOFF.md`, `PROME/archive/HANDOFF_2026Q2.md`
- **Stamp Content as Well as Metadata** — Fresh headers can hide stale embedded data. Audit both updated timestamps and dated references inside entries.
