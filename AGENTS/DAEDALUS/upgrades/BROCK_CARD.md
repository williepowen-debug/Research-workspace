# Upgrade Card — BROCK (read-only assessment, no agent files touched)

> 🗄 **ROUTED 2026-07-12 — CLOSED AS A QUEUE 2026-08-17 (self-audit F5 banner pass).** This card's findings were routed to the owner/FLEET_MAP when written; per-row states below are historical. Not maintained — current gaps live on the agent's FLEET_MAP row. Do not work rows from here without re-verifying at the agent.

**By:** DAEDALUS · **Date:** 2026-06-28 · **Class:** Market (private credit / BDC contagion → bank transmission)
**Method:** `UPGRADE_PROTOCOL.md` (one section at a time) · graded vs `BLUEPRINTS/market-agent.md` · comprehension in `profiles/BROCK.md`
**Verdict: L4 (conf H), adversarially verified.** BROCK is among the most complete market agents in the fleet — **conformant or exemplary on 6 of 8 sections**. The FLEET_MAP previously under-rated it L3 on a **false "No TRADE.md" premise** (corrected; see PAT-020). Every proposal below is an *added handle* or a *staleness refresh*, never a rewrite. Nothing applied — this is the queue.

**↳ PROME scoping (6/28) — ✅ APPLIED 6/28 (commit 7435022d; item5 routed to BROCK inbox):** batch-1 (gated, `BATCH_01_handles.md`) = Independence col (§2) + if-falsified ACTION col (§5) + BANK_BDC_MATRIX freeze. **Position-truth (stale TRADE.md marks) = PROME's lane, NOT DAEDALUS** (FORGE decision-a) — do not route or edit marks. Apply only after PROME/Will approve + idle-check.

---

| § | Blueprint section | BROCK current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Thesis structure** | FLOW.tsv 21-pathway status engine + NAMES cascade + CROSS_ANALYSIS + Stage 1-6 tracker | ✅ APPLIES | conformant (exemplary) | None — FLOW Status field exceeds the OTTO stage table | 0 |
| 4 | **Invalidation / exit** | EXIT RULES w/ FIRED/NOT-FIRED + literal session counts + bidirectional flip; 5-step Decision Tree | ✅ APPLIES | conformant (exemplary) | None — among the strongest exit rails in the fleet | 0 |
| 6 | **Cross-agent routing** | CLAUDE route-matrix + NEXUS_BRIEF writeback every closeout + domain-owner discipline | ✅ APPLIES | conformant | None | 0 |
| 7 | **Standing disciplines** | mechanism-vs-thermometer + EXPECTED_SIGNALS absence-is-data + Δ cols + boot↔closeout symmetry | ✅ APPLIES | conformant (fleet model) | None material (matrix Δ already serves the 3-col discipline) | 0 |
| 8 | **BOTTOM LINE** | STATUS ends w/ 4-para BOTTOM LINE, single-read lead, updated 6/28; 211 ln <cap | ✅ APPLIES | conformant | None (richer than floor — OK per floor-not-ceiling) | 0 |
| 3 | **Thresholds** | EXPECTED_SIGNALS durable bands (no live values) + VX/STATUS live + conjunction triggers | ✅ APPLIES | conformant | *Optional only:* extract the 5-step Decision Tree into a standalone KILL_MEMO.md (survives STATUS rewrites). Low value. | 3 |
| 2 | **Convergence matrix** | 14-vector matrix, composite 60/70; shared-node "score once" reasoning in **prose only** | ✅ APPLIES (adapted) | missing **handle** — ✅ **DONE 6/28 (see banner)** | Add an `Independence` column (+ optional `#`) lifting the score-once reasoning into the table. Keep the prose; do NOT flatten to a bare flag. | 2 |
| 5 | **Predictions** | ledger + 7-resolved archive + Brier-0.244 scoreboard + failure-synthesis; **no if-falsified ACTION column** | ✅ APPLIES (adapted) | missing **handle** — ✅ **DONE 6/28 (see banner)** | Add `If-Falsified ACTION` column to PREDICTIONS.tsv (→trim/extend/−Npp), sourced from the TRADE.md trigger ladder | 2 |

### Separately — the real L4→L5 work (staleness, not structure)
| Item | Why | Effort |
|---|---|---|
| **Refresh TRADE.md position-truth layer** | anchored to 5/21 (superseded); ~90%-loss residuals unresolved; trade surface LAGS the 6/28 STATUS — the main thing separating it from L5 | M (owner work, idle-apply or task-packet) |
| **Freeze-or-refresh BANK_BDC_MATRIX.tsv** | flagged-stale but NOT frozen = silent-rot middle (root-CLAUDE hygiene violation) — pick (a) FROZEN banner or (b) LIVE w/ mtime alert | S |
| **Reconcile VX self-count** | STATUS says 18 / ARCH says 21 / file = 20 — agent closeout hygiene | S |
| **Clear / obtain a YEYOU clean bill** | L5 requires zero YEYOU flags + current | n/a (YEYOU-side) |

---

## The queue
1. **§ FLEET_MAP correction (DAEDALUS's own file — DONE 6/28):** L3→L4, struck "No TRADE.md caps at L3", rewrote next_upgrade to the L4→L5 path. Pure additive win, no concurrency risk.
2. **§2 Independence column** + **§5 if-falsified ACTION column** — two cheap formalization handles; the only real handle gaps. Batch as one BROCK changelist.
3. **TRADE.md position-truth refresh** — the highest-value *real* work; the staleness blocking L5. Position truth = `WILL/trading-journal` + TERRY; coordinate, don't guess marks.
4. BANK_BDC_MATRIX freeze decision + VX count reconcile — polish.

> **Note for application:** BROCK is idle (last touched 6/28 via PROME catch-up spawn, not a live session) — handle-adds are idle-applicable with approval, but they touch BROCK's files, so gate on **permission + a fresh idle-check** (AUTHORITY). The TRADE.md refresh is BROCK's own domain work — route a task-packet rather than editing marks myself.
