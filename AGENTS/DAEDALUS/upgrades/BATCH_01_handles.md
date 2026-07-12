# Batch Changelist 01 — SHADE / BROCK / CREED "encode-existing-reasoning" handles

**By:** DAEDALUS · **Date:** 2026-06-28 · **Status:** ✅ APPLIED — all 8 items live since 2026-06-28: BROCK `STATUS.md:140` + `workbook/PREDICTIONS.tsv` Action_If_Falsified col, CREED `STATUS.md:38,200-204`, SHADE `STATUS.md:151,276-280`. *(Banner added late 2026-07-12 per DAEDALUS self-sweep — record was never updated after the 6/28 apply.)*
**Scope (per PROME direction 6/28):** encode-existing-reasoning **HANDLES only** — comparable interfaces that make these three machine-stackable for NEXUS/PROME and lift judgment they *already do* into a structured form. **No new per-session machinery** (those are held for round two, below). Every item is **additive** (floor-not-ceiling, PAT-015) — local richness is never stripped.

**Sources:** `upgrades/{SHADE,BROCK,CREED}_CARD.md` (full queues) · `profiles/{…}.md` (do-not-touch). Graded vs `BLUEPRINTS/market-agent.md`.

---

## The changelist

| # | Agent | File · location | Change (additive handle) | Encodes reasoning already in… | Effort |
|---|---|---|---|---|---|
| 1 | **SHADE** | `STATUS.md` (tail) | Add a trailing `## BOTTOM LINE` (2-4 sentences: state-now / single-most-important / what's-next), mirrored from the §0a "Net read" verdict, updated every session | §0a "Net read (NO breach)" + SCRATCH "TOP VERDICT" — verdict already written each session, just not labeled/placed | S |
| 2 | **SHADE** | `STATUS.md` §3 signal dashboard | Add `Score(1-5)` + `Independence` columns + a composite total to the existing per-vector dashboard | The 5-pt maps the emoji state machine SHADE already maintains; independence encodes its own "5-fund Q2 cluster = ONE shared-antecedent wave → count once" prose | S |
| 3 | **BROCK** | `STATUS.md` convergence matrix | Add an `Independence` column (+ optional `#`) to the 14-vector matrix | Lifts the "AI-unwind + credit-K-split share ONE node → score once" reasoning already in the matrix's prose/summary line | S |
| 4 | **BROCK** | `workbook/PREDICTIONS.tsv` | Add an `If-Falsified ACTION` column (position consequence per row) | The consequences already exist in `trade/TRADE.md` §9 trigger ladder — this maps them per-prediction (CARL pattern) | S |
| 5 | **BROCK** | `workbook/BANK_BDC_MATRIX.tsv` (header) | Kill the silent-rot middle: either a `FROZEN <date>` banner OR a live boot-time mtime staleness alert (owner picks) | Root data-hygiene rule (already flagged in BROCK CLAUDE.md "owner to confirm freeze-vs-refresh") | S |
| 6 | **CREED** | `STATUS.md` | Relabel the near-top "Bottom Line" → "Thesis"; add a tail 2-4-sentence `## BOTTOM LINE` (the canonical state-now lives in the 6/28 catch-up top-line — relocate it) | The true state-now line already exists in the catch-up section | S |
| 7 | **CREED** | `thesis/THESIS.md` (or STATUS) | Add a 5-pt **CONVERGENCE** table over the existing 8 Expected Signals: `# \| Vector \| Score(1-5) \| local-state(🔴/🟠/🟡) \| Independence \| Key Signal \| Upgrade Trigger`; composite /40 | The 8 Expected Signals already ARE the vectors w/ severity + triggers; independence encodes e.g. "Signals 1&2 share the maturity-wall antecedent → count once". **Highest cross-agent value — lets the fleet consume CREED's CRE read without spawning the tier-2 agent.** | M |
| 8 | **CREED** | `CLAUDE.md` | Consolidate the scattered routing (CLAUDE Feed + THESIS Agent Handoffs + per-signal Response + REIT Route col) into ONE `condition → target → priority` route-matrix table | Pure consolidation — all the routing substance already exists across 3 places | S |

*Exact cell values / verbatim rendering are finalized against the LIVE file at apply-time (re-read per PAT-009 — this draft specifies the structural change, not the final bytes).*

## DO-NOT-TOUCH guardrails (carried from the profiles)
- **SHADE:** keep the §0 RETRACT/DOWNGRADE discipline, peer-relative spread sub-row canary, and the trigger-gated dig lane intact. The 5-pt is ADDED to §3, not a replacement for the emoji state machine.
- **BROCK:** do not flatten the shared-node independence prose into a bare flag; do not touch the FLOW.tsv status engine, the 5-step Decision Tree, or CROSS_ANALYSIS. (Position-truth = separate lane, below.)
- **CREED:** do not impose always-on cadence (tier-2 spawn-on-need); preserve the stale-data hygiene (sourced+dated numbers, legacy firewalled). The convergence table is a handle over the 8 signals, not a replacement for the mechanism map.

## Application protocol (after approval)
1. **Idle-check each target immediately before editing** — three writers were live on the shared tree today (DAEDALUS/WALTER/PROME); confirm the agent isn't mid-spawn (PAT-004).
2. **Re-read the live file** before each edit (PAT-009) — this draft is structural, not verbatim.
3. Apply per-agent, commit by pathspec (cross-agent edits ride the closeout push); **record** each in the agent's `FLEET_MAP.tsv` row + the upgrade card status column.
4. If a target is live → route the item as a task-packet to its `inbox/` instead of editing.

---

## HELD for round two (NOT in this batch — per PROME)
A separate, justified proposal — *does new per-session ledger machinery earn its upkeep on a watch/spawn-on-need agent?*
- **SHADE:** full `PREDICTIONS.tsv` + standing exit-triad (FIRED-count). *(SHADE is a watch agent — directional calibration is lower-value; justify cadence first.)*
- **CREED:** live-workbook stand-up / `PREDICTIONS.tsv` **rehab** (pull-forward the frozen legacy VX/FLOW schema seeds under `REGINALD/sub-agents/CREED/`). *(Spawn-on-need — justify before imposing accruing machinery.)*

## OUT OF DAEDALUS'S LANE (noted, not actioned)
- **BROCK position-truth refresh** (the stale 5/21 TRADE.md marks / ~90%-loss residuals): **PROME's lane** — tied to the FORGE position-truth decision (a) (truth = `WILL/trading-journal/` + broker export). DAEDALUS does the structural handles above; **does not route or edit TRADE.md marks.**
- **Root `CLAUDE.md` Data Hygiene** could name agent-level `TRADE.md` explicitly in the ledger-staleness rule (currently lists "KB/VX/FLOW/etc."). Shared file → **flagged to PROME**, not edited by DAEDALUS. (DAEDALUS has encoded it in `BLUEPRINTS/market-agent.md` + PAT-023.)
