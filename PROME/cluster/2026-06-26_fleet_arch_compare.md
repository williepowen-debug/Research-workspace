# Fleet Architecture Compare/Contrast + Improvement Options
**Date:** 2026-06-26 | **Author:** Prome (Claude Code) | **Inputs:** 5 agent self-reports (CARL/REGINALD/LABOR/BROCK/SHADE `ARCH_REPORT_2026-06-26.md`)
**Purpose:** Synthesize 5 independent architecture self-reports into a fleet compare/contrast + ranked, decision-ready improvement options for Will.

> **Headline:** Five agents introspecting independently converged on the *same* short list of strengths and failure modes. That convergence means these are **structural fleet properties, not per-agent quirks** — so the high-leverage fixes are fleet-wide standards, not 5 separate cleanups.

---

## 1. Fleet Matrix

| Dimension | CARL | REGINALD | LABOR | BROCK | SHADE |
|---|---|---|---|---|---|
| Tree size | 11 dirs / mid | **Heaviest** (9 bank dirs, WAL 64f) | 9 dirs / mid | 7 root files / mid | Clean root / rich `sources/` |
| STATUS health | **Header bloat** (~2,500c) | **Overloaded** (226 lines) | OK | OK | **Best — §-section + §0 boot-delta** |
| Boot automation | partial | `market.py` + BOARD 9b diff | **Best — `boot.py` full sweep** | none | manual scan |
| Prediction system | **Best format** (PREDICTIONS.tsv) | REG-T-NN THRESHOLDS | LAB-xx + due-scan | **BRK-NN triggers** | §10 trigger-gated lane |
| board_log | yes (no domain tag) | **Best schema** (11-col, 9b diff) | **MISSING** (wired, never built) | flat | typed (v0.2) |
| Worst friction | STATUS header | per-bank sprawl (~60 dead files) | workbook lag (C3) | **outbox ghost** (16 dead) | git-mv residue |
| Provenance | TSV-heavy | self-curl verify | KB confidence schema | Admiralty digraph KB | **Statutory MANIFEST tree** |

---

## 2. Reusable Patterns (port across the fleet)

Ranked by how many agents would benefit:

1. **Pre-registered prediction/trigger system** — *every* agent has a version (CARL PREDICTIONS.tsv, BROCK BRK-NN, SHADE §10 lane, REGINALD REG-T-NN, LABOR LAB-xx). Strongest shared pattern, but **5 different formats**. Best-of-breed = CARL's falsifier+confidence+position-action columns + BROCK's made/resolve-date + invalidation. → candidate for one fleet schema.
2. **Boot/closeout symmetry** (LABOR) — every boot-read explicitly written back at closeout. Prevents drift *structurally*, not by discipline. Most agents do this partially; LABOR formalized it (B1→C1, B3→C5…).
3. **`boot.py` automated sweep** (LABOR) — live FRED + threshold flags + predictions-due scan in ~5s. BROCK/SHADE/CARL lack full automation.
4. **§-section STATUS + §0 boot-delta** (SHADE) — cold-boot orient in 2 min via §0+§3+§10 without reading the full doc. **Direct cure for CARL/REGINALD STATUS bloat.**
5. **board_log.tsv signal routing** (REGINALD 11-col, 9b diff) — verify_verdict + conf + disposition; prevents both over-integration and signal burial. LABOR lacks it entirely.
6. **Statutory provenance tree** (SHADE — MANIFEST + dated subfolder + raw extracts) — anti-"frame-contamination" anchor for agents citing secondary sources.
7. **POSITIONS.md single-source** (REGINALD) — STATUS/CALENDAR point to it; kills a whole desync class.
8. **Numbered LESSONS.md mistake ledger** (BROCK/LABOR) — grep-able, cheap, prevents repeat errors.

---

## 3. Universal Friction (failure modes, by prevalence)

1. **TSV workbook layer chronically lags STATUS — UNIVERSAL.** CARL (FLOW 66d, VX 10d), LABOR (VX/KB/FLOW, C3 chronic), REGINALD (TSV↔display desync). "STATUS is truth; the workbook is a liability." **This is the #1 fleet friction.**
2. **STATUS bloat** — CARL (header), REGINALD (226 lines). SHADE's model is the fix.
3. **Outbox is a dead/ghost process** — BROCK (16 undelivered), CARL (Apr-17), SHADE (writes direct). *Ties to the pending messaging overhaul — see caveat.*
4. **Inbox intake only on explicit spawn → backlog** — SHADE (5), REGINALD (14 today), CARL/LABOR. No boot-time auto-triage.
5. **research/sources have no retirement policy** — LABOR (17 March files), REGINALD (growing), SHADE (Mar'26 KB), BROCK (Feb memos), CARL.
6. **`git mv` vs bash-mv residue** — SHADE (today's cleanup commit). Lesson exists in memory but didn't prevent it.
7. **Per-entity folder model doesn't scale** — REGINALD (60 dead bank files), BROCK (hollow `trade/`).
8. **Broken calibration loop** — BROCK (SCOREBOARD exists, not consulted when setting confidence).

---

## 4. Ranked Improvement Options (decision menu)

### Tier 1 — high-impact, cheap, universal
- **T1a. Stale-ledger fix (the #1 friction).** Two flavors — pick one as fleet default:
  - *(i) Freeze* (LABOR's pref): demote stale VX/KB/FLOW to frozen-archival with a header banner; stop maintaining; STATUS is truth.
  - *(ii) Automate* (CARL's pref): boot-time mtime staleness alert ("FLOW.tsv stale 66d") so it surfaces at boot not closeout.
  - *Rec:* **(ii) for live ledgers + (i) for dead ones** — automate the alert, freeze what the alert proves dead.
- **T1b. Pre-closeout `git status -- AGENTS/<NAME>/` check** (SHADE's #1). 5-sec closeout-protocol line; catches bash-mv residue + cross-dir leaks. **Universal, near-zero cost.**
- **T1c. research/sources retirement rule** (LABOR's #2): `>60d + not boot-read + not referenced → archive`. One closeout-checklist line; clears every graveyard.

### Tier 2 — high-impact, moderate effort
- **T2a. STATUS de-bloat** — port SHADE's §-section + §0 boot-delta model to CARL + REGINALD; move prior-session digests → CHANGELOG (CARL's #1). Caps STATUS, makes it diff-safe.
- **T2b. Standardize `board_log.tsv`** — adopt REGINALD's 11-col schema fleet-wide; build it for LABOR (missing); add domain-tag for CARL.
- **T2c. Port `boot.py` automation** — LABOR's sweep as the model for BROCK/SHADE/CARL (per-agent scripting lift).

### Tier 3 — structural/design (more thought)
- **T3a. One fleet prediction/trigger schema** — split outcome-PREDICTIONS vs threshold-TRIGGERS (BROCK's #2), merge in CARL's falsifier+position-action columns. Turns the fleet's best pattern into a standard.
- **T3b. Fix BROCK calibration loop** — consult PREDICTIONS_SCOREBOARD when setting new confidence.
- **T3c. Per-entity folder tiering** — REGINALD active-vs-`archive/banks/`; BROCK retire hollow `trade/`.

### Tier 4 — gated on the messaging overhaul (do NOT build new infra)
- **T4a. Outbox kill / NEXUS_BRIEF as send surface** (BROCK's #1) + **inbox boot-auto-triage** (SHADE's #2). **Caveat:** file-based messaging is slated for replacement (memory `messaging_overhaul`). Interim = *stop writing dead outbox files*; don't build a new send protocol that the overhaul will throw away. Flag to the overhaul design, don't pre-empt it.

---

## 5. Meta-Recommendation

**Most of these are the same finding 5×.** The efficient path is **3–4 fleet-wide protocol standards**, not 15 per-agent fixes:

1. **A fleet closeout-protocol addendum** (root or shared spec): adds T1b (`git status` check), T1c (retirement rule), T1a-ii (ledger staleness alert). Three cheap lines, applied everywhere. *(Editing shared/root docs needs Will's sign-off.)*
2. **A "STATUS standard"** = SHADE's §-section/§0 model + digest→CHANGELOG, adopted by the bloated agents (CARL/REGINALD).
3. **A "forward-tracking standard"** = the merged prediction/trigger schema (T3a) — the fleet's best pattern, unified.
4. **Hold the messaging items (T4) for the overhaul** — surface to that design, don't build now.

**Suggested first implementation wave (cheapest, highest universality):** T1b + T1c as a closeout addendum, then T2a (STATUS de-bloat) on CARL+REGINALD since those two are actively friction-ed today. Everything else is a deliberate follow-on.
</content>
