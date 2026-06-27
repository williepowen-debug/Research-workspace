# Fleet Maturity Map — First Full Scan

**By:** DAEDALUS · **Date:** 2026-06-27 · **Method:** objective script floor (`scripts/maturity_scan.py`) + judgment overrides (SPEC.md §5)
**Persisted data:** `FLEET_MAP.tsv` · **Rerun:** `python3 AGENTS/DAEDALUS/scripts/maturity_scan.py`

> 26 agents scanned (active + tier-2 + special). Dormant/archive-source agents skipped. **Confidence:** H = read-verified · M = read + mechanical · L = mechanical-only (needs a judgment read to confirm L3+).

---

## Distribution

| Level | Count | Agents |
|---|---:|---|
| **L4** | 1 | REGINALD |
| **L3** | 8 | HENRY, CARL, BROCK, LABOR, BOND*, WALTER, RED, TERRY |
| **L2** | 12 | VIOLET, HAWK, BRENT, CORAL, LIQUID, MARCO, SHADE, OTTO, SAM, HANS, NEXUS, ORACLE, YEYOU |
| **L1** | 1 | CREED (tier-2) |
| **L0** | 2 | DEWEY (by design), HERMES (deprecated) |
| **Meta** | — | DAEDALUS L3 (self) |

\* low-confidence — provisional, needs a read.

---

## Standouts

- **REGINALD — the fleet exemplar (L4).** Full convergence matrix, exit rules, DFAST integration, 6 predictions resolved, TRADE.md, top commit cadence. This is what "good" looks like; use as the **market-agent blueprint source** (Phase 3).
- **HENRY — high discipline, non-template shape (L3).** 22 resolved predictions — the best falsification loop in the fleet — but expressed through its own HEN-NN trigger/vector structure, not the template's titled sections. Raises a real standards question (below).
- **WALTER / RED / TERRY — strong utility agents (L3).** Output consumed fleet-wide; WALTER carries the highest cadence (20 commits/30d). TERRY owns real tooling (grade_print/chain_fetch).

---

## Systemic findings (fleet-wide, not per-agent)

**1. The "no BOTTOM LINE" epidemic — 13 agents.** The template *requires* every STATUS.md to end with a BOTTOM LINE; 13 don't (REGINALD, CARL, BRENT, CORAL, LIQUID, MARCO, SHADE, VIOLET, OTTO, SAM, WALTER, RED, TERRY, NEXUS). This is the single highest-value, lowest-effort fix in the fleet — and a textbook **batch changelist** (see Recommendation 1). It does NOT lower their level (it's a conformance gap, not a skeleton signal — see PAT-007), but it's exactly the kind of drift DAEDALUS exists to catch.

**2. Exit rules without session counts — 5 agents.** CORAL, LIQUID, MARCO, VIOLET (+others) have exit rules but lack the required "N+ sessions" specificity. Falsification you can't time isn't falsification.

**3. SAM over the line cap.** STATUS 317 lines (>250 cap) = structural debt; archive older research to `domain/sources/`.

**4. HERMES is a retire candidate.** Deprecated by the messaging overhaul; L0 and idle. Lifecycle-sunset candidate (impact analysis first).

**5. DEWEY's L0 is correct, not debt.** Stateless deep-research agent by design. Flagging it as a gap would be a false positive — the per-class ladder prevents that.

---

## A standards question for Will (EVOLUTION decision)

**HENRY has the substance of L4 discipline but not the template's titled sections.** Two ways to resolve, fleet-wide:
- **(a) Enforce titling** — every agent uses the literal "Convergence Matrix" / "Exit Rules" headings. Uniform, scriptable, but forces mature agents to relabel working structures.
- **(b) Accept equivalents** — score on substance (does it have scored vectors + falsification rails, by any name?), accept own-titling. Truer to maturity, harder to script.

My lean: **(b) accept equivalents, but require a one-line pointer** in STATUS ("Falsification → thesis/THESIS.md" like CORAL does) so the substance is findable. Your call — it sets how strict the standard is.

---

## Recommendations (proposals — each needs your approval + idle targets)

| # | Action | Effort | Value | First step |
|---|---|---|---|---|
| 1 | **Batch: add BOTTOM LINE to the 13** | Low | High | DAEDALUS drafts the 13 one-liners from each agent's current STATUS; you approve the batch; apply only to idle agents, task-packet the live ones |
| 2 | Batch: add session counts to the 5 exit-rule gaps | Low | Med | Draft proposed counts per agent for review |
| 3 | SAM STATUS compression <250 | Low | Med | Task-packet SAM (it owns its content) |
| 4 | Decide standards question (a)/(b) above | — | High | One-line ruling → record in EVOLUTION.md |
| 5 | HERMES sunset impact analysis | Med | Med | Phase 4 lifecycle dry-run candidate |

---

## Caveats

- **12 rows are mechanical-only (Conf L)** — provisional levels from structural signals, not deep reads. A judgment-read pass would firm these up; flagged in `FLEET_MAP.tsv`.
- The script is a **floor + flag generator**, not a quality judge. It missed HENRY's and CORAL's discipline (own-titling / content in `thesis/`) — judgment overrode it. That seam is the design, working as intended.
