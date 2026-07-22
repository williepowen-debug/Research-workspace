# BEST-PRACTICES HARVEST — best-of-breed patterns across the fleet

> 🗄 **HARVEST SNAPSHOT (2026-06-27) — consumed by the Phase-3 blueprint builds 6/28; not maintained.** The live standards are `market-agent.md` / `utility-agent.md` / `meta-agent.md`; this documents where each section was sourced FROM.

**Owner:** DAEDALUS · **Source:** full fleet structural survey, 2026-06-27 (5 parallel reads, 23 agents)
**Purpose:** the pattern library the `market-agent` / `utility-agent` blueprints are assembled FROM. Best-of-breed per dimension — no single agent wins, so the standard is composed, not cloned.

> Key finding: the fleet has collectively out-designed the original template. HENRY's INVALIDATION TRIAD and banded-threshold-with-routing are strong, but **HENRY is weak on cross-agent-comparable scoring** (no universal 5-pt), where BOND/BRENT are better. The best standard takes the best of each.

---

## Best-of-breed by dimension

| Dimension | Winner | The pattern | Why it wins |
|---|---|---|---|
| **Falsification / exit** | **LIQUID** | **Channel-kill vs thesis-kill + migration theorem** — thesis survives by *rerouting* through another transmission leg when one resolves, not by dying. Partial kills allowed. | Prevents false thesis-death; models how stress actually shifts routes mid-crisis. |
| ↳ *live format* | **HENRY** | **INVALIDATION TRIAD — standing rule vs state** — each leg: standing rule \| current state @ level \| fired/not-fired, with a literal fired-count. | Continuously evaluated falsification, not a static list. |
| ↳ *bidirectional* | **BRENT** | **"Cleanest flip each way"** — names the single thing that would falsify the thesis in BOTH directions, testable at the next data release. | Pre-commits the counter; lets other agents spot when BRENT should break. |
| ↳ *compound gate* | **MARCO / OTTO** | **3-part AND-gate kill** + **mechanism-vs-thermometer split** (high-conf mechanism separated from confounded readout). | Thesis survives noise; narrow and defensible. |
| **Thresholds / triggers** | **HENRY** | **Banded table (Yellow/Orange/Red) with inline cross-agent routing** (`KRE <$65 → REGINALD/PROME`). | Severity + addressee in one table; no silent breaches. |
| ↳ *advanced* | **LIQUID** | **X1 conjunction triggers** (fire only on A AND B) + **pre-written KILL_MEMO library** (durable trigger ladder, decoupled from ephemeral STATUS). | Compound logic kills single-metric knee-jerks; library survives STATUS rewrites. |
| ↳ *multi-horizon* | **OTTO** | **Dual-layer thresholds** (prediction-specific + mechanical + composite) with STATUS as arbitrator when they disagree. | Tracks near-term predictions and broad pattern separately. |
| **Convergence / scoring** | **BOND** | **5-point scale + explicit composite formula** (e.g. 11/35, transparent arithmetic). | Most cross-agent comparable — the thing the synthesis layer (NEXUS) needs. **HENRY lacks this.** |
| ↳ *independence* | **NEXUS** | Convergence matrix with an **independence column** + Δ-discipline (signed pp, last-updated). | Stops "1 root in 6 costumes" counting as 6 signals. |
| **Thesis structure** | **OTTO** | **Transmission-chain stage table** (7 stages, current-state per stage: confirmed/open/falsified). | Reproducible "where is the contagion actually manifesting?" checklist. |
| ↳ *interaction* | **REGINALD** | **Cluster × entity exposure grid** (banks × 4 independent causal clusters; 3/4-exposure = non-linear risk). | Captures compounding, not just correlation. |
| ↳ *buffers* | **LIQUID** | **3 structural-failure legs** (buffers, not thresholds) + migration map with per-leg owner. | Durable across regime change. |
| **Cross-agent routing** | **MARCO** | **Standing route-matrix in CLAUDE** (conditional) + outbox protocol + **NEXUS_BRIEF writeback every closeout**. | Maintainable standing rules, not one-off decisions. |
| ↳ *discipline* | **LIQUID / NEXUS** | **NEXUS_BRIEF = sync-point** (curated, every session) + **outbox = crisis-only** (async). | Kills notification fatigue. |
| ↳ *delivery infra* | **WALTER** | **Delivery-layer split**: produced ≠ received ≠ consumed, with telemetry (`delivered_but_unconsumed` checks). | Operationalizes "routed" = "actually got it." |
| **Prediction tracking** | **OTTO** | **PREDICTIONS_ARCHIVE + calibration scoreboard + failure-pattern synthesis fed back to THESIS** + boot-time `predictions_due.py`. | Turns resolved predictions into institutional learning. |
| ↳ *action-linked* | **CARL** | **Position-action commitment** — every prediction has an "if falsified → trim 25%, extend duration, −25pp conf" action, not just a confidence. | Falsification drives portfolio action. |
| ↳ *evidence tiers* | **VIOLET** | **KB-linked resolution + confidence tiers** (EMPIRICAL / PROVISIONAL / ASSUMPTION); never over-weight N=1. | Traceable, calibrated. |
| ↳ *honesty* | **LABOR** | **Honest post-hoc re-grading** ("scored 9 pts too bearish, adjusting 57→48"). | Falsification-friendly culture; no narrative hiding. |

---

## Novel / cross-cutting patterns worth a standing library

| Pattern | Owner | What it does |
|---|---|---|
| **Mechanism-vs-thermometer split** | MARCO | Separate confidence in the mechanism (high) from its confounded readout (medium) — thesis survives bad readouts. |
| **Disclosure-channel split detection** | SHADE | Signal present in one venue, absent in another (AMAPS in Apollo not Athene) = hidden-leverage tell. Forensic. |
| **Scenario-posture preamble** | HAWK | Pre-committed meta-rules ("declaratory ≠ physical", "rhetoric ≠ resolution") to inoculate against headline whipsaw. |
| **Velocity-not-level intervention framing** | SAM | Intervention fires on *disorder/velocity*, not level proximity; + stop-vs-payoff whipsaw warning. |
| **Shared-antecedent independence re-test (Discipline F)** | NEXUS | Re-test latent shared assumptions at integration, not just creation; collapse costumes to roots. |
| **Citation-count vs observation-count guard** | NEXUS | Same HY OAS in 4 rows = 1 observation seen 4×, not 4 rails. |
| **Trigger-level granularity** | BRENT | Decompose a 6-month thesis into weekly micro-tests ("gasoline YoY ≤−5% ×3wk, 0/3 so far"). |
| **Data-deletion as meta-signal** | MARCO | A cancelled official survey = information-asymmetry edge (stress stays out of consensus longer). |
| **EXPECTED_SIGNALS (absence-is-information)** | MARCO | Track signals that SHOULD appear if the thesis holds; their absence is data. |
| **Boot↔Closeout symmetry** | WALTER/RED/NEXUS/ORACLE/TERRY/YEYOU | What you read at boot, you write back at closeout — the anti-rot force. |
| **Three-column Δ discipline** | RED/NEXUS/ORACLE | `metric · Δ signed pp · last-updated` — only bumps on material change; catches silent drift. |

---

## Exemplars to source blueprints from (Phase 3)

- **Market-agent blueprint:** REGINALD (cluster grid, exemplar), + LIQUID (exit/migration + thresholds), + OTTO (predictions + transmission stages), + BOND (comparable scoring), + MARCO (routing + mechanism/thermometer).
- **Utility-agent blueprint:** WALTER (delivery infra, overall exemplar), + NEXUS (synthesis disciplines), + RED (adversarial structure), + YEYOU (severity scale + escalation budget), + ORACLE (boot/closeout symmetry).

No agent is the whole standard. The blueprint = best-of-breed, assembled.
