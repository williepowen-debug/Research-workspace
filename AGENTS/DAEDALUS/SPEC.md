# DAEDALUS — Design Spec (Phase 0)

**Status:** 🟢 APPROVED — Will signed off + merged to master 2026-06-27; wired into root `CLAUDE.md` / `PROME/ROSTER.md` / `AGENTS.md` + git-aligned to fleet auto-push by PROME. Phase 4 reached 2026-06-28 (AEOLUS build). *(Historical Phase-0 snapshot — live state: STATUS.md; standard's history: EVOLUTION.md. ⚠️ SUPERSEDED-IN-PARTS, marked 2026-08-17 self-audit F29: §4's four-file memory model and §5's ladder cells lag the charter — CLAUDE.md's MEMORY MODEL and MATURITY LADDER are canonical wherever they differ; notably the Market L3 dated-falsification-surface leg [8/7] and the Meta-L5 roadmap-leg STRIKE [W1, 8/17] live there, not here.)*
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
| Authority (flag vs fix) | **Fix & create with express permission.** DAEDALUS *can* edit other agents' files and create new ones, but every mutation to something it doesn't own is gated on Will/PROME approval. Overrides root Critical Rule #2 *for DAEDALUS specifically*. **Two guards, both required:** (a) approval, and (b) the target agent must be **idle** — DAEDALUS never edits a live agent's files (permission ≠ concurrency-safe; a live session would clobber). For live agents it routes a task packet instead. Approval is **batched**: DAEDALUS proposes a changelist, Will approves the batch — not 20 prompts. | ✅ |
| Maturity map method | **Hybrid: computed + judged.** Script computes the objective floor (L0–L2: file presence, schema validity, line caps, commit recency — rerunnable, can't hallucinate). Agent-reading judges the ceiling (L3–L5: discipline/quality). | ✅ |
| Lifecycle scope | **Full lifecycle, permission-gated.** Owns spawn → track → sunset. Proposes retirements with full impact analysis; executes only on Will's go. | ✅ |
| System-evolution tie-in | **Merged, but scoped.** DAEDALUS owns *inward* evolution (how our agents are built, how the standard improves). External capability changes are an *input* to the blueprint, **not** a revival of DARWIN's open-ended landscape scan. | ✅ |
| Memory shape | **Meta-shaped, not market-shaped.** Custom memory (§4), not the KB/VX/FLOW market workbook. | ✅ |
| Runtime | On-demand standing agent. Spawnable by PROME or Will. Has persistent memory + learning. | ✅ |
| Name | **DAEDALUS** — the mythic master architect. | ✅ |

---

## 4. Memory & learning model

DAEDALUS learns the same way a domain agent does — by accruing a structured record — but the "facts" are *design facts*, not market facts. Four founding files (2026-06-27 — the live register set has since grown; CLAUDE.md MEMORY MODEL is canonical), each answering one need:

| File | Role | Analogue |
|---|---|---|
| **`BLUEPRINTS/`** | The canonical build standards DAEDALUS owns — `market-agent`, `utility-agent`, `meta-agent` variants. Supersedes `templates/CLAUDE_TEMPLATE.md` (DAEDALUS maintains the template as its public output). The "how it **should** be built." | the standard |
| **`PATTERNS.tsv`** | KB-style ledger of design lessons & anti-patterns, sourced & dated ("agents skipping exit-rules go stale fastest — REGINALD, CORAL"). The **learning engine** — where DAEDALUS gets smarter over time. | KB.tsv |
| **`EVOLUTION.md`** | Architecture changelog + roadmap. What changed in the standard, why, where it's heading. | thesis/CHANGELOG |
| **`FLEET_MAP.tsv`** | One row per agent: current maturity level, build history, deviations-from-standard + why. Doubles as the persisted maturity map. | per-agent memory |

`BLUEPRINTS/` is the single source of truth the conformance checks grade against — closing the "template drifts from reality" gap.

**Boundary vs ROSTER.md:** ROSTER owns *active/dormant classification* (git-activity based). `FLEET_MAP.tsv` owns *maturity/design state*. They **reference, never copy** (system one-source-of-truth rule). DAEDALUS reads ROSTER's classification as an input; it does not restate it. *(Longer term DAEDALUS may feed ROSTER — not in scope yet.)*

---

## 5. The maturity ladder (per-class)

A single ladder mis-scores non-market agents — NEXUS/TERRY/ORACLE/YEYOU (and DAEDALUS itself) have no convergence matrix or TRADE.md *by design*. So the ladder shares a structural floor (L0–L2, class-independent) and **diverges at L3–L5 by agent class**. The class also tells DAEDALUS which `BLUEPRINTS/` variant to grade against.

**Shared floor (all classes):**
| Level | Label | Bar |
|---|---|---|
| **L0** | Skeleton | dir + CLAUDE.md, nothing live |
| **L1** | Live | STATUS.md maintained, has a BOTTOM LINE |
| **L2** | Logging | structured record exists with valid schema, accruing |

**Class-specific ceiling (L3–L5):**
| Level | **Market** (CARL, BRENT…) | **Utility** (NEXUS, TERRY, ORACLE, YEYOU) | **Meta** (DAEDALUS) |
|---|---|---|---|
| **L3** Disciplined | convergence matrix + exit/falsification rules + predictions resolving | role-specific rubric applied consistently (e.g. YEYOU's checklist, TERRY's grade_print) | conformance checks run; FLEET_MAP current |
| **L4** Generating | TRADE.md feeding real proposals; cross-agent signals flowing | output consumed by others (briefs, trade cards, reviews landing) | builds/retirements executed cleanly; PATTERNS accruing |
| **L5** Self-maintaining | clean closeouts, zero standing YEYOU flags, current | same | same + EVOLUTION roadmap live |

L0–L2 = scripted (objective). L3–L5 = agent-judged (quality), against the class rubric. Map output per agent: `class + level + specific gap + next upgrade`.

> **YEYOU-leg waiver (Will, 2026-07-22):** the "zero standing YEYOU flags" leg is **waivable-when-dormant** — if YEYOU (manual/branch, Will-spawned) has not run within the review period, the leg auto-waives and L5 grades on the remaining criteria; a later YEYOU run can retroactively flag (which then counts against the *next* cycle, not retro-demotes). Rationale: 4 otherwise-ready candidates (LABOR/BRENT/VIOLET/WALTER) were blocked on a reviewer that never reviews — a PAT-028-class gate defect (the gate penalized an un-exercisable external dependency, not the agent). The gate stays strict whenever YEYOU actually runs.

---

## 6. Lifecycle & permission flow

- **Build:** DAEDALUS drafts a new agent from the blueprint → Will approves → DAEDALUS scaffolds + wires.
- **Maintain:** DAEDALUS finds structural gaps → proposes a **batch changelist** → Will approves the batch → DAEDALUS fixes directly **only for idle agents'** empty scaffolding; for a **live** agent (or anything touching live content) it routes a task packet to the owning agent instead.
- **Retire:** DAEDALUS proposes a sunset *with impact analysis* (what refs break, what chains rewire) → Will approves → DAEDALUS executes the clean archive + rewiring.

Every cross-agent mutation needs **both** approval **and** an idle target. DAEDALUS owns the *analysis and execution*; Will owns the *decision*.

### Oversight (who grades DAEDALUS)
DAEDALUS appears in its own `FLEET_MAP.tsv` like every other agent (no agent grades only itself). Primary oversight is **Will + PROME** — both direct and examine it. YEYOU is *designed* to review its per-push conformance as it does any agent — see the status note below before relying on that.

### Data flow with YEYOU / PROME
- **Consumes** YEYOU's per-push flags as an input → aggregates into standing "structural debt" per agent in `FLEET_MAP.tsv`. **⚠️ Designed, never yet exercised — see below.**
- **Hands** the maturity map to PROME/Will to action; routes specific fixes to owning agents as task packets.

> **Status of this data flow (2026-07-30, Will-confirmed): the YEYOU leg has never carried anything.** `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` holds **zero findings all-time** — YEYOU has never run, so the "consumes YEYOU's flags" input has produced exactly nothing since DAEDALUS was built. This is a *not-yet-launched* state, not a dead design: Will intends to revive it, the machinery verifies clean (`scripts/boot.py` rc=0), and revival is one watermark decision away (`AGENTS/YEYOU/STATUS.md` § Watermark). **Interim:** QC is covered by **RAV** (Codex, Will-driven) — the *deep-review* half of YEYOU's two-reviewer funnel, which YEYOU's own `CLAUDE.md` has named since it was written. RAV composes with YEYOU on revival rather than being replaced by it; the two differ on authority (RAV may repair within a bounded class, YEYOU is flag-never-fix). **Practical consequences while this holds:** ① the structural-debt column of `FLEET_MAP.tsv` is fed only by DAEDALUS's own sweeps and audits, never by an independent reviewer; ② the L5 "zero standing YEYOU flags" leg is vacuously true for every agent and must not be read as evidence — Will's **2026-07-22 waivable-when-dormant ruling** (§5) is what actually governs it; ③ DAEDALUS's own pushes are reviewed by nobody mechanically. Delete this box when the first digest lands.

---

## 7. Phase plan

| Phase | Deliverable | Gate |
|---|---|---|
| **0 — Spec** | *This doc.* Lock decisions in DAEDALUS's dir. | ← Will sign-off |
| **1 — Skeleton + memory** | Write DAEDALUS's CLAUDE.md first, then **extract** the meta-blueprint from it (DAEDALUS is the first worked example of its own standard — avoids the chicken-and-egg of "derive from a blueprint that doesn't exist yet"). Stand up the four memory files. Exists, "knows itself." | |
| **2 — Maturity engine** | Scoring script (objective floor) + first full fleet maturity map. *Pulled early — it's the deliverable Will most wants and it proves DAEDALUS earns its keep before it gets build authority.* | |
| **3 — Build pipeline** | The "scaffold a new agent" workflow, tested by (re)building one real agent. | |
| **4 — Maintenance + wiring** | Structural-conformance pass; lifecycle/retirement; wire into ROSTER / AGENTS.md / YEYOU / PROME. | |

Phase 2 before Phase 3 is deliberate: the map tells us what to build, and proves the agent before we hand it build authority.

---

## 8. Open / deferred *(all three RESOLVED — dispositions added 2026-07-22 self-sweep; kept for design history)*

- ~~Exact `BLUEPRINTS/` variant set (market / utility / meta — more?)~~ → **SETTLED 6/28**: three variants, all built + ACTIVE same day; no fourth class has emerged through 30 scanned agents.
- ~~Whether the scoring script lives in `AGENTS/DAEDALUS/scripts/` or `scripts/` (fleet-shared)~~ → **SETTLED**: `AGENTS/DAEDALUS/scripts/maturity_scan.py` (DAEDALUS-only consumer); genuinely shared enforcement (`ledger_staleness.py`, `tsv_append.py`) lives at root `scripts/`.
- ~~Cadence: on-demand vs weekly refresh?~~ → **SETTLED 7/4-7/12** by the sweeps system (`sweeps/REGISTRY.tsv`: staleness 21d · production review 14d + on-demand-after-heavy-sessions · falsification 21d · harness 90d/model-upgrade; boot cadence-checked via `sweeps_due.py`).
