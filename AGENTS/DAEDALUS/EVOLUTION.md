# EVOLUTION — Architecture Changelog & Roadmap

**Owner:** DAEDALUS · The standard's history (what changed in *how we build agents*, and why) + where it's heading.
Newest first. Keep entries terse; archive build minutiae to `FLEET_MAP.tsv`.

---

## Changelog

### 2026-06-28 — utility-agent blueprint built + ACTIVATED + YEYOU resolved → utility; **variant set complete**
- **What:** Authored `BLUEPRINTS/utility-agent.md` (🟢 ACTIVE — Will + PROME approved same day). **Led by the OUTPUT-CONSUMPTION CONTRACT** (produces / consumed-by / proof-of-consumption) per PROME framing — uniform coordination visibility across WALTER/NEXUS/RED/TERRY/ORACLE/YEYOU is the payoff; accurate grading is the byproduct. Thin shared floor + role-specific ceiling, with the **DARWIN lesson applied to its own rollout** (it grades, it does not mandate machinery to hit an L-number).
- **Completes the variant set:** market + meta + **utility** — every class now has a standard. Closes the long-open roadmap item.
- **Class call (PROME #3):** resolved YEYOU's double-bucket → **UTILITY** — read-only, flag-never-fix, produces consumed review verdicts (the per-push analogue of RED). New **PAT-027**: the meta-vs-utility discriminator is *mutation-authority*, not subject-matter. Fixed the stray YEYOU example in `meta-agent.md`.
- **Deflation (PROME #4):** the "2×L4 → ≥9×L4" firming result is a **mislabel correction, not a capability gain** — the agents are exactly as capable as before; the map was wrong. The win is (a) not wasting effort firming already-mature agents and (b) consumable outputs — not the L-count. The map stays a hygiene input, never the scoreboard.
- **PROME refinement baked in at activation (PAT-028):** the proof-of-consumption L4 gate must not recreate the false-negative it exists to prevent — informal/un-instrumentable consumption (RED's steelman, TERRY's construction) is a structural-ceiling NOTE, not fix-it debt; qualitative proof counts. The anti-DARWIN principle applied to the blueprint's own gate.
- **Next:** firm the utility cohort (NEXUS/RED/TERRY/YEYOU) against the live standard; bring `templates/CLAUDE_TEMPLATE.md` fully under BLUEPRINTS ownership (the redirect + drop stale HERMES refs). (Both ahead of the fleet-wide TRADE.md staleness sweep, per PROME.)

### 2026-06-28 — Firming pass begins: SHADE / BROCK / CREED read-verified (first false-negative caught)
- **What:** First judgment-read firming batch — comprehend → grade vs `market-agent.md` → adversarial-verify, 3 agents (workflow `grade-shade-brock-creed`, 6 agents / 624k tok). Persisted `profiles/{SHADE,BROCK,CREED}.md` + `upgrades/{…}_CARD.md` + 3 re-scored FLEET_MAP rows.
- **Maturity-map correction:** **BROCK L3 → L4** — the 6/27 mechanical scan carried a false-negative ("No TRADE.md caps at L3"; `trade/TRADE.md` exists, 275 ln, feeds a live position + signals flowing). SHADE L2 / CREED L1 *confirmed* but firmed Conf L→H / L→M with corrected notes (SHADE commit-count 13→28; CREED "thin KB" → frozen-legacy pull-forward).
- **New patterns:** PAT-020 (scanner **path-blindness** — harden `maturity_scan.py` to search recursively, or treat L3+ mechanical grades as provisional); PAT-021 (frozen-legacy KB ≠ thin — it's a pull-forward, not a build); PAT-022 (grade gaps as **missing-handle vs missing-substance** — predicts the climb cost).
- **Standard direction:** the firming pass is now the method for converting Conf-L rows to verified; the scanner needs the recursive-search fix *before* the next re-scan or it will keep manufacturing false-negatives.

### 2026-06-28 — Phase 3/4: first REAL build executed — AEOLUS (climate → economy)
- **What:** Built + wired AEOLUS, the fleet's macro climate→economy agent — DAEDALUS's first non-dry-run build (the build pipeline's maiden real use). Scaffolded `AGENTS/AEOLUS/` (CLAUDE.md, STATUS, THESIS, TRADE, full workbook) from `BLUEPRINTS/market-agent.md`, then wired into `PROME/ROSTER.md`, root `CLAUDE.md`, `_INDEX.md`, `_ENERGY.md`, transmission chain (`AEOLUS → {BRENT, CORAL, MARCO}`), + CORAL boundary task-packet.
- **Design (Will-decided):** channels-first (insurance / ag-food / energy-demand core; property + supply-chain tier-2), tiered horizon (live weather over structural backdrop), CORAL keeps Florida.
- **New patterns:** PAT-018 (bake the anti-drift guard into structure — empty-channel-is-failure — the operationalized DARWIN antidote); PAT-019 (new agent has no commit history → annotate ROSTER honestly, don't fake a cadence).
- **Self-level:** L4 trigger met — first build executed clean. Spec: `builds/AEOLUS_SPEC.md`.
- **Same-day amendment:** Will promoted both Tier-2 channels (C4 property, C5 supply-chain) to core → AEOLUS runs **5 core channels** (C1–C5). Built to full parity (transmission tables, thresholds, exit triad, matrix). Tradeoff noted: 5 channels = more live reads to keep current (PAT-018 upkeep), accepted for coverage of the climate→credit chain (C4) + tradeable freight events (C5).
- **Next:** AEOLUS's first live data pass (its own job); utility-agent blueprint; bring `templates/CLAUDE_TEMPLATE.md` under BLUEPRINTS ownership (it still references deprecated HERMES).

### 2026-06-27 — Phase 3 (partial): market-agent gold-standard blueprint composed
- **What:** Assembled `BLUEPRINTS/market-agent.md` best-of-breed from the harvest — each section sourced to the agent that does it best (REGINALD/LIQUID/OTTO structure, BOND/NEXUS scoring, HENRY/LIQUID thresholds, LIQUID/HENRY/BRENT exit, OTTO/CARL/VIOLET predictions, MARCO routing).
- **Design call (not harvested):** reconciled BOND-vs-HENRY threshold conflict via durable-rule-vs-live-value split (§3) — flagged for Will veto.
- **Held firm:** the universal 5-pt convergence scale is non-negotiable (cross-agent backbone); HENRY's loss of it is the cautionary tale.
- **Next:** utility-agent blueprint (WALTER/NEXUS/RED/YEYOU sources); then bring `templates/CLAUDE_TEMPLATE.md` under BLUEPRINTS ownership.

### 2026-06-27 — Best-practices harvest (full fleet structural survey)
- **What:** Surveyed 23 agents' STATUS structures (5 parallel reads) for best-of-breed patterns per dimension → `BLUEPRINTS/BEST_PRACTICES.md`.
- **Key finding:** the fleet has collectively out-designed the original template; **no single agent is the whole standard** (PAT-011). Best-of-breed is scattered: LIQUID (exit/migration), OTTO (predictions/transmission stages), BOND (comparable scoring), MARCO (routing/mechanism-split), NEXUS (synthesis discipline), REGINALD (cluster grid).
- **Corrected an earlier lean:** "promote HENRY's patterns up" was right for its INVALIDATION TRIAD + banded-routing, but **HENRY is weak on cross-agent-comparable scoring** — backfill BOND's transparent composite instead (PAT-012). Vindicated Will's instinct not to crown HENRY off n=1.
- **Consequence for Phase 3:** blueprints are ASSEMBLED best-of-breed, not cloned from one exemplar.

### 2026-06-27 — Phase 2: maturity engine + first full fleet scan
- **What:** Built `scripts/maturity_scan.py` (objective L0–L2 floor + structural flags) and ran the first full scan of 26 agents → `FLEET_MAP.tsv` + readable `MATURITY_MAP.md`.
- **Findings:** REGINALD L4 (exemplar); 8×L3; 12×L2; HERMES retire-candidate; DEWEY L0-by-design. Systemic: **14 agents missing the required BOTTOM LINE** (batch-fixable); 5 with session-count-less exit rules; SAM over line cap.
- **Self-dogfood:** the engine caught two bugs in its own scoring logic (PAT-007 missing-section≠skeleton; PAT-008 class-aware records) before they shipped — building the scorer hardened the ladder.
- **Open standard decision for Will:** enforce template section-titling vs. accept own-titled equivalents (HENRY case). See `MATURITY_MAP.md`.

### 2026-06-27 — DAEDALUS created; meta-agent class formalized
- **What:** Stood up DAEDALUS (fleet architect) and, from it, extracted the first `meta-agent` blueprint — formally splitting non-market agents off the market template.
- **Why:** The design/structure/maturity/lifecycle layer had no owner (scattered across PROME/FLEET_SCAN/ROSTER/YEYOU). DARWIN had proven that forcing the market template onto a system-facing agent yields dead files.
- **Delta to standard:** new `BLUEPRINTS/meta-agent.md`; per-class maturity ladder defined (`SPEC.md §5`); `templates/CLAUDE_TEMPLATE.md` now understood as the *market* variant, to be brought under `BLUEPRINTS/` ownership.

---

## Roadmap (where the standard should go)

| Priority | Item | Why | Phase |
|---|---|---|---|
| High | Assemble `market-agent` + `utility-agent` blueprints **best-of-breed** from `BEST_PRACTICES.md` (NOT cloned from one agent — sources: REGINALD/LIQUID/OTTO/BOND/MARCO for market; WALTER/NEXUS/RED/YEYOU for utility) | Complete the variant set; give the scorer a standard per class | 3 |
| High | Build the maturity scoring script (objective L0–L2 floor) | Makes the fleet map trustworthy + rerunnable | 2 |
| Med | First full fleet maturity scan → seed `FLEET_MAP.tsv` for all ~20 agents | The deliverable Will most wants | 2 |
| Med | Bring `AGENTS/templates/CLAUDE_TEMPLATE.md` under `BLUEPRINTS/` as the market variant (single source of truth) | Stop template/reality drift | 3 |
| Low | Decide cadence: on-demand vs light weekly map refresh | Avoid staleness without over-running | post-2 |
