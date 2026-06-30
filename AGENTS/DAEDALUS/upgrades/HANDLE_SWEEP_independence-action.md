# Handle Sweep — §2 `Independence` column + §5 `If-Falsified ACTION` column (market cohort, fleet-wide)

**By:** DAEDALUS · **Date:** 2026-06-29 · **Status:** 🟡 DRAFT — routed to PROME (+Will); **NOT applied.**
**Source:** the `firm7-profiles-cards` pass surfaced the *same two handles* missing across the market cohort — a pattern invisible per-agent, visible only across all 7 cards at once. [[finding_fleet_selfreport_convergence]] / PAT-011: a convergent gap is **one fleet-wide fix, not N per-agent items.**

## Why this is a sweep, not N card items
**Both handles are ALREADY REQUIRED by `BLUEPRINTS/market-agent.md`** — §2 (line 42-43, Independence column) and §5 (line 66, if-falsified action). **The gap is enforcement, not standard:** these agents predate the 2026-06-27 standard and were never swept against it. So review the two handles **once here** → apply to every in-scope idle agent (task-packet the live ones). This **consolidates** what is currently scattered across BATCH_01 (done), BATCH_02, and the net-new card items — saving PROME from re-deciding the same handle nine times.

## Rules (unchanged — floor-not-ceiling, PAT-015)
- ADD the handle **alongside** the rich local representation; **never flatten.**
- Each is an **encode-EXISTING-reasoning** handle — the shared-antecedent / position-consequence logic already lives in prose; the column just lifts it into the table. (No new analysis.)
- Per-agent application: permission + **fresh idle-check** (AUTHORITY) → re-read live (PAT-009) → pathspec commit → record in FLEET_MAP + card. **Task-packet any live agent** (REGINALD is heavily active).

---

## Handle A — §2 Convergence matrix `Independence` column
*Vectors on the same root count once — surfaces hidden double-counts in the composite.*

| Agent | Matrix | Encode-source (reasoning already present) | Status |
|---|---|---|---|
| BROCK | 14-vector, 60/70 | shared-node "score once" prose | ✅ DONE (BATCH_01) |
| BOND | 7-headline, 11/35 | VX-08…16 "feed-not-double-counted" note | 🟡 in BATCH_02 A5 → **review here** |
| REGINALD | own 0-20 per-bank | 8→4 cluster independence analysis (`thesis/THESIS.md`) | 🟡 BATCH_02 item 1 (Independence sub-part) → **review here** |
| CARL | 14-vector, 52/70 | ROADMAP L80: VX-1.01 vs VX-CC-01 both track CC 90+ DQ (double-count it already flags) | 🔵 NET-NEW |
| LABOR | 16-vector, 48/80 | announcement-layer cluster (WARN#1 / Sector#2 / AI#5 = the *same* Spirit/Meta/MSFT announcements) | 🔵 NET-NEW |
| BRENT | 14-vector, 47/70 | shared-kinetic-root (Hormuz↔Ceasefire↔Tanker) "score once" prose | 🔵 NET-NEW |
| HAWK | — | **N/A** — light single-channel; no cross-vector shared-antecedent risk | ⚪ N/A-by-design |
| VIOLET/LIQUID/MARCO/OTTO/HANS/SAM | (un-firmed) | add at their firming pass | ⏳ deferred |

## Handle B — §5 Predictions `If-Falsified ACTION` column
*Every prediction carries its position consequence (→ trim / extend / −Npp / route), not just a confidence number.*

| Agent | Predictions | Encode-source | Status |
|---|---|---|---|
| BROCK | ledger + archive | TRADE.md trigger ladder | ✅ DONE (BATCH_01) |
| CARL | 25 preds (CRL-01..25) | **ALREADY HAS IT** (CRL-21/24 position-action) — the blueprint's **named source** | ✅ exemplar (no-op) |
| REGINALD | REG-01..25 | EXIT RULES consequences | 🔵 NET-NEW |
| LABOR | 10 OPEN / 6 resolved | TRADE §3 forward-catalyst playbook | 🔵 NET-NEW |
| BOND | BND-01..10 | consequence currently buried in `Notes` prose | 🔵 NET-NEW |
| BRENT | 54 preds (BRT-xx) | optional — calibration loop already exceeds floor; low value | 🟢 optional/defer |
| HAWK | strong calibration | **N/A** — no book / no position to act on | ⚪ N/A-by-design |
| ORACLE | (utility) | **N/A** (utility); its truth-loop is the Brier scoreboard → BATCH_02 §C | ⚪ N/A-by-design |

---

## What this supersedes / touches
- **Folds in** the scattered handle line-items: BATCH_01 (BROCK — done) · BATCH_02 item 1 (REGINALD Independence sub-part) + item A5 (BOND Independence) · the net-new card items (CARL/LABOR/BRENT Independence; REGINALD/LABOR/BOND ACTION). **Review the two handles here once;** the per-agent batch entries defer to this spec.
- **Untouched:** BATCH_02's NON-handle items (REGINALD/CARL BOTTOM LINE + REGINALD/LABOR NEXUS_BRIEF, hygiene) stay in BATCH_02.
- **Blueprint:** added a one-line "commonly-missing / N/A-exception" conformance note to `market-agent.md` §2 + §5 (so future firmings check these two first).

## Net effect for review
**One approval** covers **6 Independence applications** (1 done, 2 already in BATCH_02, 3 net-new) + **3 ACTION applications** (net-new) across the market cohort — instead of re-deciding the same handle 9× across 3 batches.

**Gate:** nothing applied. Awaiting PROME (+Will). — DAEDALUS
