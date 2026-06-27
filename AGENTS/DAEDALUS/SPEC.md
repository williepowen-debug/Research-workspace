# DAEDALUS — Design Spec (Phase 0)

**Status:** 🟡 DRAFT — awaiting Will sign-off. No fleet wiring until approved.
**Created:** 2026-06-27 · **Owner:** Will (decisions) / DAEDALUS (maintenance)
**Class:** Meta-agent — the fleet's architect. Not a market-domain agent.
**Reports to:** PROME · **Spawnable by:** PROME *or* Will (on-demand, not always-on)

---

## 1. What DAEDALUS is

The fleet's **architect**: the standing owner of the *design / structure / maturity* layer that no one owns today. It builds new agents, keeps the fleet structurally coherent, and gives Will the one view he can't produce by hand — a maturity map of where every agent actually sits.

It fills a vacant seat. Today this work is scattered: PROME does ad-hoc directory audits, FLEET_SCAN ranks staleness, ROSTER classifies by git activity, YEYOU flags per-push compliance. DAEDALUS consolidates the **design-level** slice of that into one owner.

### Where it sits (no overlap)

| Layer | Owner | Question |
|---|---|---|
| Thesis | RED | Is the bear case wrong? |
| Per-push compliance | YEYOU | Did the agent follow protocol on *this* push? (flag, never fix) |
| Prioritization / decisions | PROME | What do we work on; what reaches Will? |
| **Design / structure / maturity / lifecycle** | **DAEDALUS** | Is this agent well-built? What's missing? Build / retire. |

DAEDALUS is **not** YEYOU (mechanical, per-push, read-only), **not** RED (thesis), **not** PROME (prioritization). It operates at the design layer and across the full agent lifecycle.

---

## 2. The three jobs

1. **Build** — scaffold new agents from the blueprint; wire them into ROSTER / AGENTS.md / transmission chains. Owns the build pipeline end-to-end.
2. **Maintain structure** — keep every agent's skeleton conformant to the standard (STATUS + BOTTOM LINE, valid workbook SCHEMA, convergence matrix, exit/falsification rules, inbox/outbox, line caps).
3. **Maturity map** — score every agent on a refinement ladder; surface the specific gap + next upgrade for each. The deliverable Will most wants.

Plus the lifecycle inverse:

4. **Retire** — sunset agents cleanly (archive, fix dangling refs, rewire chains, update ROSTER/AGENTS.md). See §6.

---

## 3. Locked decisions (this session)

| # | Decision | Resolution |
|---|---|---|
| Authority (flag vs fix) | **Fix & create with express permission.** DAEDALUS *can* edit other agents' files and create new ones, but every mutation to something it doesn't own is gated on an explicit Will/PROME go-ahead per action. Overrides root Critical Rule #2 *for DAEDALUS specifically*, with permission as the safety. | ✅ |
| Maturity map method | **Hybrid: computed + judged.** Script computes the objective floor (L0–L2: file presence, schema validity, line caps, commit recency — rerunnable, can't hallucinate). Agent-reading judges the ceiling (L3–L5: discipline/quality). | ✅ |
| Lifecycle scope | **Full lifecycle, permission-gated.** Owns spawn → track → sunset. Proposes retirements with full impact analysis; executes only on Will's go. | ✅ |
| System-evolution tie-in | **Merged, but scoped.** DAEDALUS owns *inward* evolution (how our agents are built, how the standard improves). External capability changes are an *input* to the blueprint, **not** a revival of DARWIN's open-ended landscape scan. | ✅ |
| Memory shape | **Meta-shaped, not market-shaped.** Custom memory (§4), not the KB/VX/FLOW market workbook. | ✅ |
| Runtime | On-demand standing agent. Spawnable by PROME or Will. Has persistent memory + learning. | ✅ |
| Name | **DAEDALUS** — the mythic master architect. | ✅ |

---

## 4. Memory & learning model

DAEDALUS learns the same way a domain agent does — by accruing a structured record — but the "facts" are *design facts*, not market facts. Four files, each answering one need:

| File | Role | Analogue |
|---|---|---|
| **`BLUEPRINTS/`** | The canonical build standards DAEDALUS owns — `market-agent`, `utility-agent`, `meta-agent` variants. Supersedes `templates/CLAUDE_TEMPLATE.md` (DAEDALUS maintains the template as its public output). The "how it **should** be built." | the standard |
| **`PATTERNS.tsv`** | KB-style ledger of design lessons & anti-patterns, sourced & dated ("agents skipping exit-rules go stale fastest — REGINALD, CORAL"). The **learning engine** — where DAEDALUS gets smarter over time. | KB.tsv |
| **`EVOLUTION.md`** | Architecture changelog + roadmap. What changed in the standard, why, where it's heading. | thesis/CHANGELOG |
| **`FLEET_MAP.tsv`** | One row per agent: current maturity level, build history, deviations-from-standard + why. Doubles as the persisted maturity map. | per-agent memory |

`BLUEPRINTS/` is the single source of truth the conformance checks grade against — closing the "template drifts from reality" gap.

---

## 5. The maturity ladder

| Level | Label | Bar |
|---|---|---|
| **L0** | Skeleton | dir + CLAUDE.md, nothing live |
| **L1** | Live | STATUS.md maintained, has a BOTTOM LINE |
| **L2** | Logging | workbook TSVs exist, valid schema, KB accruing |
| **L3** | Disciplined | convergence matrix + exit/falsification rules + predictions being resolved |
| **L4** | Generating | TRADE.md feeding real proposals; cross-agent signals flowing |
| **L5** | Self-maintaining | clean closeouts, zero standing YEYOU flags, current |

L0–L2 = scripted (objective). L3–L5 = agent-judged (quality). Map output per agent: `level + specific gap + next upgrade`.

---

## 6. Lifecycle & permission flow

- **Build:** DAEDALUS drafts a new agent from the blueprint → Will approves → DAEDALUS scaffolds + wires.
- **Maintain:** DAEDALUS finds a structural gap → for purely empty scaffolding it may fix directly *with express permission*; for anything touching live content it routes a task packet to the owning agent.
- **Retire:** DAEDALUS proposes a sunset *with impact analysis* (what refs break, what chains rewire) → Will approves → DAEDALUS executes the clean archive + rewiring.

Every cross-agent mutation = express permission. DAEDALUS owns the *analysis and execution*; Will owns the *decision*.

### Data flow with YEYOU / PROME
- **Consumes** YEYOU's per-push flags as an input → aggregates into standing "structural debt" per agent in `FLEET_MAP.tsv`.
- **Hands** the maturity map to PROME/Will to action; routes specific fixes to owning agents as task packets.

---

## 7. Phase plan

| Phase | Deliverable | Gate |
|---|---|---|
| **0 — Spec** | *This doc.* Lock decisions in DAEDALUS's dir. | ← Will sign-off |
| **1 — Skeleton + memory** | DAEDALUS CLAUDE.md (from meta-blueprint) + the four memory files stood up. Exists, "knows itself." | |
| **2 — Maturity engine** | Scoring script (objective floor) + first full fleet maturity map. *Pulled early — it's the deliverable Will most wants and it proves DAEDALUS earns its keep before it gets build authority.* | |
| **3 — Build pipeline** | The "scaffold a new agent" workflow, tested by (re)building one real agent. | |
| **4 — Maintenance + wiring** | Structural-conformance pass; lifecycle/retirement; wire into ROSTER / AGENTS.md / YEYOU / PROME. | |

Phase 2 before Phase 3 is deliberate: the map tells us what to build, and proves the agent before we hand it build authority.

---

## 8. Open / deferred

- Exact `BLUEPRINTS/` variant set (market / utility / meta — more?) → settle in Phase 1.
- Whether the scoring script lives in `AGENTS/DAEDALUS/scripts/` or `scripts/` (fleet-shared) → Phase 2.
- Cadence: purely on-demand, or a light weekly maturity-map refresh? → revisit after Phase 2.
