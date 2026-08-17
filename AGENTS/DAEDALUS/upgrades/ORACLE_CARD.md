# Upgrade Card — ORACLE (read-only assessment, no agent files touched)

> 🗄 **ROUTED 2026-07-03 — CLOSED AS A QUEUE 2026-08-17 (self-audit F5 banner pass).** This card's findings were routed to the owner/FLEET_MAP when written; per-row states below are historical. Not maintained — current gaps live on the agent's FLEET_MAP row. Do not work rows from here without re-verifying at the agent.

**By:** DAEDALUS · **Date:** 2026-06-29 · **Class:** Utility (prediction-market diagnostics — Polymarket + Kalshi real-money crowd-implied odds)
**Method:** `UPGRADE_PROTOCOL.md` (one section at a time) · graded vs `BLUEPRINTS/utility-agent.md` (the floor; NOT `market-agent.md`) · comprehension in `profiles/ORACLE.md`
**Verdict: L4 (conf H), adversarially verified 6/28.** ORACLE is the agent that **SURFACED** the utility-blueprint gap (blueprint authored 6/28, day after ORACLE's heavy 6/27 session). **Conformant or exemplary on 7 of 8 floor sections** — it is the blueprint's *named source* for boot↔closeout symmetry. The one floor handle-gap is a missing standardized 3-line CONTRACT block. The only real L5 build — a **Brier calibration scoreboard** — is already **HELD in BATCH_02 §C (pending PROME)** and is NOT re-proposed here. Every proposal below is an *added handle* or a *staleness refresh*, never a rewrite (PAT-015 floor-not-ceiling). Nothing applied — this is the queue.

**↳ BATCH_02 cross-ref (do NOT re-propose — referenced, not duplicated):**
- **Calibration / resolution Brier scoreboard** (`workbook/RESOLVED.tsv` + Brier) → **routed in BATCH_02 §C (HELD, pending PROME).** Gated on *justify-the-upkeep-first* AND the open tractability question (Polymarket slug-rot → markets resolve and drop): is the loop a *fix-it gap* or a *structural ceiling*, PAT-028? Resolve that design call **before** any build or any L5 claim.
- **ORACLE `TRADE.md` staleness** falls under **BATCH_02 §D** fleet-wide TRADE.md/ledger-staleness sweep (PAT-025, DAEDALUS's own lane). The ORACLE-specific live-vs-frozen call sits in the L4→L5 table below.
- **BATCH_02 per-agent DO-NOT-TOUCH (ORACLE):** market constructs (convergence matrix / TRADE.md / predictions ledger) are correctly **N/A** — do NOT impose them. The crowd-signal read is the role. Encoded as the DARWIN-guard row below.

---

## Section grade — one row per `utility-agent.md` floor section (+ DARWIN guard, + role-ceiling)

| § | Blueprint section | ORACLE current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Header + IDENTITY** (class, role, no-overlap, File>verbal) | CLAUDE.md IDENTITY + domain scope + core-market tiers; class=Utility; no-overlap stated ("cedes substance to domain owners — spreads→LIQUID, fundamentals→REGINALD, oil→BRENT; owns only the prediction-market read") | ✅ APPLIES | conformant | None material. *(Optional polish: lift the cede-to-owners line into an explicit `where-it-sits / no-overlap` table; low value.)* | 0 |
| 2 | **THE CONTRACT** (produces / consumed-by / proof) — *the defining handle, L4 gate + the SPINE* | Content present but **scattered** (CLAUDE.md IDENTITY + CROSS-AGENT SIGNALS route-matrix + NEXUS_BRIEF); **NO formal 3-line CONTRACT block** — predates the 6/28 blueprint. Proof exists (NEXUS reads brief; LIQUID picked up July-hike figure-check → in LIQUID `processed/`; TERRY handoff packet a defined surface) | ✅ APPLIES | **missing handle** | Add the 3-line CONTRACT block to CLAUDE.md/STATUS: **PRODUCES** = prediction-market probability reads (crowd odds + dislocation/entropy scores) + `NEXUS_BRIEF`; **CONSUMED BY** = NEXUS·LIQUID/HENRY·HAWK/BRENT·RED·REGINALD/CARL·VIOLET·PROME·TERRY via brief + CROSS-AGENT routes; **PROOF** = NEXUS reads brief in place of raw STATUS + LIQUID `processed/` July-hike check + TERRY packet (qualitative per PAT-028). Encode existing content; do NOT invent new routing. | **1** |
| 3 | **Role rubric** (explicit, consistently applied — L3 gate) | `PREDICTION_MARKET_METRICS.md` (272 ln): entropy, KL-bits dislocation score, tradeable-gap discount stack, entropy-collapse k-σ anomaly alert, signal-fusion, routing table, TERRY handoff packet, Python ref, anti-patterns | ✅ APPLIES | conformant (exemplary) | None — far richer than the floor requires; this is the L3 rubric, applied consistently | 0 |
| 4 | **Structured record (logging)** — valid, accruing, class-aware (L2 floor) | `workbook/`: 13-col KB (19 entries, Admiralty conf + EMPIRICAL/ESTIMATE + ACTIVE/SUPERSEDED/CORRECTED lifecycle w/ DerivedFrom chains) + ODDS_LOG (174 rows) + **HISTORY (4,796 rows daily trajectory)** + VX threshold ledger + KALSHI_ODDS_LOG (separate schema) | ✅ APPLIES | conformant (exemplary) | None — 5 accruing valid-schema logs; daily-trajectory view defeats stale baselines. *(SOURCE_TAG + Kalshi-accrual = hygiene, see L4→L5 table.)* | 0 |
| 5 | **Standing disciplines** (boot↔closeout symmetry + 3-col Δ + anti-bias) | **Blueprint's named exemplar** for boot↔closeout symmetry (14-step BOOT-read↔CLOSEOUT-writeback mirror). STATUS Trajectory table carries Δ30/90d. Anti-bias = anchor-to-surprise-vs-pricing + thin-liq ≥3-day re-check + no-naked-numbers + `closed`-field authoritative | ✅ APPLIES | conformant (exemplary) | None — fleet sourcing exemplar; do not touch the mirror (breaking it caused the 6/22 retracted-claim broadcast) | 0 |
| 6 | **Cross-agent routing** (route-matrix + NEXUS_BRIEF writeback + crisis-only outbox) | CLAUDE.md condition→target→priority route-matrix + `SIGNAL_INTAKE.md` (WALTER subscription spec) + `NEXUS_BRIEF` MANDATORY every closeout + crisis-only outbox | ✅ APPLIES | conformant | None | 0 |
| 7 | **AUTHORITY & SAFETY** (state read-only boundary if no write power) | Read-only boundary stated explicitly: TRADE.md + METRICS §0 — "does NOT size or execute; TERRY sizes." No cross-fleet structure-mutation authority (correctly utility, not meta) | ✅ APPLIES | conformant | None | 0 |
| 8 | **BOTTOM LINE** (required; STATUS under cap) | STATUS.md (122 ln) ends with BOTTOM LINE; well under cap | ✅ APPLIES | conformant | None | 0 |
| — | **DARWIN guard** — *no* convergence matrix / TRADE.md / thesis-predictions ledger | ORACLE *carries* a 5-row convergence "matrix" + a TRADE.md — but both are **repurposed utility surfaces** (matrix tracks which prediction-markets are firing, live/scored 6/27; TRADE.md is a no-sizing crowd-odds→implications routing surface). EQUIVALENT, vestigial market-template labels on utility content — **not market constructs, not debt** | N/A by design | **N/A-by-design** | None — do NOT delete as DARWIN violations; do NOT grade vs the market blueprint for "having" them. Touch only to rename/clarify or to refresh TRADE.md's stale numbers (see L4→L5) | 0 |
| — | **Role calibration loop** (ceiling — `utility-agent.md` role table → ORACLE → **Brier scoreboard**) | EXIT RULES (CLAUDE.md) **promise** "track accuracy over time"; **NO Brier/resolution scoreboard file exists** — the role's truth-loop is named, not built. This is the headline L5 gap | ✅ APPLIES | missing substance → **routed BATCH_02 §C** | **Do NOT re-propose** — HELD in BATCH_02 §C (pending PROME). Build gated on upkeep-justification + slug-rot tractability (gap-vs-ceiling, PAT-028) | in BATCH_02 (pending PROME) |

**Gap-type tally:** 7 conformant (3 of them exemplary: §3/§4/§5) · 1 missing-handle (§2 CONTRACT) · 1 N/A-by-design (DARWIN guard) · 1 in-BATCH_02 (Brier calibration loop).

---

## Separately — the real L4→L5 work (staleness / builds, not section-handle gaps)

| Item | Why | Net-new vs BATCH_02 | Effort |
|---|---|---|---|
| **TRADE.md — resolve live-vs-frozen, then refresh-or-banner** | Stale since 6/19: "live reads" (enrichment 66.5% / recession 12.5% / no-cuts 81.9%) superseded by STATUS 6/27 (1.4% / 11% / 79.5%); NOT on the closeout write-back loop (CLOSEOUT steps 8–13 omit it) = silent ledger-drift-behind-STATUS, textbook PAT-023. **Open design Q first** (profile §7): is TRADE.md meant to be live or FROZEN-with-banner? | Per-agent call is **net-new**; umbrella = BATCH_02 §D fleet sweep (PAT-025) | S |
| **Verify the Kalshi 2nd-source loop is accruing** | `KALSHI_ODDS_LOG` has a single pull (6/27, 8 rows). Two-fetcher EXECUTE contract says every session pulls `kalshi.py pull --log` too — confirm it's building, not stalled after wiring. **Calibration value depends on the 2nd source accruing** | net-new (verify, not edit) | S |
| **Add `POLY`/`KALSHI` SOURCE_TAG to VOCABULARIES.tsv** | KB uses free-text "Polymarket 6/27" for source; flagged in MEMORY, unresolved. Small vocab handle → normalizes provenance across the 13-col KB | net-new | S |
| **Brier calibration scoreboard** (`workbook/RESOLVED.tsv` + Brier) | The role's designated truth-loop (EXIT RULES promise it) and the headline L5 gap | **NOT net-new — BATCH_02 §C (HELD, pending PROME)** | M (build) |
| **Clear / obtain a YEYOU clean bill** | L5 requires zero YEYOU flags + current | n/a (YEYOU-side) | n/a |

---

## The queue (quick wins first)

1. ✅ **APPLIED 7/3 (BATCH_03, DAEDALUS direct — ORACLE idle).** **§2 CONTRACT block** — *net-new, highest value.* The blueprint's defining handle (THE SPINE / L4-gate visibility); content already existed, just unstandardized → encoded as a 3-line block after IDENTITY in `CLAUDE.md` (PRODUCES/CONSUMED-BY/PROOF, conservative consumer list = NEXUS/TERRY/LIQUID + all-via-probabilities). The single biggest gap-closer for ORACLE. **(Was not in BATCH_02.)**
2. **TRADE.md live-vs-frozen design call → banner-or-refresh** — *net-new at agent level* (umbrella = BATCH_02 §D). Resolve the by-design question (profile §7) before touching; an unambiguous FROZEN banner is idle-applicable with approval, a number-refresh is owner work → prefer a task-packet (ORACLE's own crowd-odds domain).
3. **Verify Kalshi loop accrual** — *net-new*, S, gates the calibration value; pure read/verify, no ORACLE-file edit.
4. **`POLY`/`KALSHI` SOURCE_TAG** — *net-new*, S polish; closes the MEMORY-flagged provenance gap.
5. **Brier calibration scoreboard** — **already in BATCH_02 §C (pending PROME)** — do NOT re-propose; resolve the upkeep-justification + slug-rot tractability (gap-vs-ceiling, PAT-028) design call there.

> **Note for application:** ORACLE last committed 6/27 (`2b74152b`) — current state equals the graded state (no temporal drift). All handle-adds touch ORACLE's files → gate on **permission + a fresh idle-check** (AUTHORITY); re-read the live file before editing (PAT-009). Where the change is owner-judgment (TRADE.md number refresh, Brier build), prefer routing a task-packet to ORACLE's `inbox/` over a live edit.
