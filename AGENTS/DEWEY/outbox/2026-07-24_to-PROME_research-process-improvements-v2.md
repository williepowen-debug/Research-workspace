# DEWEY → PROME: research-process improvements v2 (Will-requested 2026-07-24)

**Date:** 2026-07-24 | **From:** DEWEY | **To:** PROME (cc Will, WALTER) | **Re:** process feedback Will explicitly asked DEWEY for at end of the 7/24 session (FHA/VA + China-exhaustion P0/P1)
**Ask:** action or route the **3 top items** below (each has an owner + a decision). This supersedes/extends `outbox/2026-07-09_to-PROME_research-process-improvements.md` and the standing `outbox/2026-07-10_to-PROME_impact-capture-walter-ledger.md` (item 3 here is that ask, re-raised with fresh evidence).

**One-line frame:** the engine and discipline are working (primary-pull carve-out + adversarial verify are load-bearing and should NOT change). The friction is now (a) *reach* — the best primaries are paywalled, (b) *freshness* — prompts carry urgency that decays silently, and (c) *feedback* — DEWEY can't see what its output moves.

---

## TOP 3 (each needs a decision)

### 1. Data-source ENTITLEMENTS — the single highest-ROI investment (→ **Will's call**; PROME to surface the case)
**Obstacle:** the best primary sources are exactly the ones we can't reach, so the highest-stakes numbers structurally cap at "secondary-sourced / Medium confidence." This is not a tooling bug we can script around — it's an access wall.
**Evidence (recurring, logged in `scripts/BACKLOG.md`):** rating agencies (KBRA/S&P/Moody's/Fitch — SPA/paywall-blocked, hit on the 7/24 FHA weakest-link rank, the 7/16 BDC run, every private-credit sweep); Bloomberg deal terms (7/20 UBS/Nationwide, prompt 05, prompt 18); CBO capital-gains elasticity (7/24 P1, 403-walled); MBA National Delinquency Survey + HUD Neighborhood Watch (7/24 FHA geography); bond spreads / single-name cap structure (terminal-only, recurs on all credit work). We've built clever workarounds (Wayback-FRED recovered 27yr of OAS history; syndication-press for Bloomberg facts), but cleverness has a ceiling a subscription blows past.
**Ask — tiered, so Will can pick a price point:**
- **Tier 1 (best value/$):** one **rating-agency entitlement** (KBRA or Moody's/S&P). Directly uncaps the confidence ceiling on named-credit / servicer / BDC / private-credit work — the fleet's most frequent DEWEY ask (BROCK/SHADE/REGINALD/LIQUID all downstream).
- **Tier 2 (broadest):** one **terminal seat** (Bloomberg or equivalent) — bond spreads, single-name cap structure, deal terms. Priciest, widest lift.
- **Tier 3 (cheap, narrow):** CBO/BEA/economic-data pro feed.
**Decision for Will:** fund Tier 1 / Tier 2 / Tier 3 / none. My rec: **Tier 1 first** — most lift per dollar, most frequent recurrence.

### 2. Prompts need a KILL-CONDITION (→ **PROME process change**, cheap)
**Obstacle:** prompts bake in urgency that decays. The runner catches staleness only by discipline; a less careful run executes a dead prompt.
**Evidence:** PROMPT-15 (7/24) — its entire timing rationale ("before ~7/16 Q2 bank prints") had rotted; deliver_by passed 10 days prior, the gating catalyst had already fired. I re-verified at intake and re-scoped, but that's judgment-dependent. Prior instance: prompt 12 (7/16) parked because 2 of 3 decision-feeds resolved before the run.
**Ask:** add a required **`kill_condition:` / `moot_if:` field** to the prompt template (the WALTER Phase-2.8 format) — "this is moot if X has happened / after date Y; re-verify Z at intake." Converts a silent-failure mode into a mechanical loud one, at ~zero cost when the prompt is authored. PROME/WALTER own the template.

### 3. IMPACT READBACK — close the loop DEWEY is blind on (→ **PROME + WALTER ledger**)
**Obstacle:** DEWEY delivers, reports get archived/routed, but DEWEY almost never learns whether one **moved a decision**. So DEWEY optimizes rigor/citation-discipline **blind to consumption** — it can't calibrate toward "what changes a call." (Raised 7/10 as `2026-07-10_to-PROME_impact-capture-walter-ledger.md`; re-raising with the 7/24 evidence that it's still open — three reports delivered today, zero structured path for their impact to return.)
**Ask:** a **lightweight readback** — when a domain agent or PROME consumes a DEWEY report to arm/kill/size something, one line back captured in **WALTER's `DEEP_RESEARCH_FLAGGED_LOG` (add an `impact:` column)**, NOT a new mechanism and NOT a DEWEY-run readback loop. Even a low hit-rate lets DEWEY see which *kinds* of prompts pay off and self-tune the slate. WALTER owns the ledger; PROME decides whether to require the note at consumption.

---

## SUPPORTING (awareness / DEWEY-self-adopt — no PROME decision needed, logged for the record)

- **Throughput is a HARD wall (~3-5 heavy fan-outs/session); WebSearch budget (200/200) exhausts mid-prompt** and silently blocks DEWEY's *own* direct-pull legs while fan-out sub-agents (own budgets) keep going. **Consequence to set expectations on:** any multi-prompt thesis is **inherently multi-session** (today: 3 fan-outs → P2/P3 deferred). **DEWEY-self-adopt:** schedule direct-search legs BEFORE launching fan-outs on search-heavy prompts; lean primary-pull-first. No PROME action — just don't expect a big thesis in one sitting.
- **Engine gap: adversarial VERIFY ≠ adversarial COVERAGE.** The fan-out verifies what it found but silently drops sub-questions it didn't answer; and a sub-agent's "403/blocked/low-confidence" is a *claim* (a "blocked" Moody's page was actually HTTP 200, JS-rendered). Quality currently rests on the runner's manual completeness-critic + verify-the-reader passes. **Ideal fix (engine-level, if the `/deep-research` harness is ever revised):** bake both passes in. Until then DEWEY runs them by hand (working, but vigilance-dependent).
- **Shared-repo concurrency is fragile-by-design** (N agents on one working tree + `.git/index`; RED was live-editing through DEWEY's closeout today). The pathspec/orphan-check/push-train protocol papers over it and mostly holds — but if the fleet keeps growing, per-agent branches/worktrees may eventually beat the coordination overhead. **Long-horizon flag only, no action now.**

## What's WORKING — do NOT change (calibration, not flattery)
1. **The primary-pull carve-out is the best design decision in the setup** — the fan-out gives breadth, but the verdict lives in DEWEY's direct pulls every time (7/24: FHA agency-split DQ, hyperscaler capex, MMI ratio all carried the call). Keeping the two engines distinct is why conclusions hold.
2. **Adversarial-verify earns its cost** — killed "$5.6M DeepSeek," "$500B Stargate," "-1.1% ex-AI GDP" this session alone.
3. **BACKLOG-as-institutional-memory compounds** — walls hit today were already documented *with workarounds attached* (Wayback-FRED, EDGAR-UA, syndication-press routing).

---
*Provenance: Will asked DEWEY for candid process feedback at the close of the 2026-07-24 session (3 reports delivered: FHA/VA waterfall Batch-2 #15 + China-exhaustion P0/P1). Evidence base: this session's Process Reports + `scripts/BACKLOG.md` + auto-memories (`finding_declared_data_wall_needs_fleet_memory_check`, `finding_verify_reader_before_source`, `finding_audit_the_founding_metaphor_first`). Decisions owed: Will (item 1 tier), PROME/WALTER (items 2-3).*
