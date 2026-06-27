# BLUEPRINT — Market-Agent (gold standard, composed best-of-breed)

**Owner:** DAEDALUS · **Assembled:** 2026-06-27 from `BEST_PRACTICES.md` (full fleet survey)
**Use for:** domain agents that own a market/risk slice (CARL, BRENT, SAM, REGINALD, …).
**Supersedes:** the market half of `AGENTS/templates/CLAUDE_TEMPLATE.md`.

> Composed, not cloned. Each section is the fleet's best pattern for that job, attributed to its source agent. No single agent is the whole standard (PAT-011). Where winners conflicted, the reconciliation is noted in *italics*.

---

## Section sources at a glance

| Section | Best-of-breed source | Pattern taken |
|---|---|---|
| Thesis structure | REGINALD + LIQUID + OTTO | independent-channel grid / failure-legs / transmission-stage table |
| Convergence matrix | BOND + NEXUS | universal 5-pt + transparent composite + independence column |
| Thresholds | HENRY + LIQUID + BOND | banded+routed rules / conjunction triggers + KILL_MEMO / durable-rule-vs-live-value split |
| Invalidation / exit | LIQUID + HENRY + BRENT | channel-kill + migration / standing-rule-vs-state / bidirectional flip |
| Predictions | OTTO + CARL + VIOLET | archive+calibration+failure-synthesis / if-falsified action / confidence tiers |
| Cross-agent routing | MARCO + LIQUID/NEXUS | standing matrix + NEXUS_BRIEF / crisis-only outbox |
| Disciplines | MARCO + NEXUS | mechanism-vs-thermometer / expected-signals / Δ-discipline |

---

## 1. THESIS STRUCTURE (REGINALD / LIQUID / OTTO)

Decompose the thesis into **independent causal channels** — not correlated risk factors. State for each: mechanism, speed, and what would confirm/break *that channel alone*.

- **Channel/leg grid** (REGINALD): entity × channel exposure where relevant; mark multi-channel exposure as **non-linear** risk, not additive.
- **Failure-legs + migration** (LIQUID): if the thesis can reroute when one leg resolves, say so — list the legs as buffers and the migration path.
- **Transmission-stage table** (OTTO): for contagion theses, a stage-by-stage table (`stage | mechanism | current state: confirmed/open/falsified`). This is the live "where is it actually manifesting?" checklist.

## 2. CONVERGENCE MATRIX (BOND / NEXUS) — the cross-agent backbone

**Non-negotiable: the universal 5-point scale.** This is what lets PROME/NEXUS stack agents against each other. Losing it (HENRY's one weakness) breaks fleet comparability.

Required columns: `# | Vector | Score (1–5) | Status | Independence | Key Signal | Upgrade Trigger`
- **Score 1–5** on the universal scale (5 🔴🔴 firing → 1 ⚪ dormant).
- **Composite** stated as transparent arithmetic (BOND): e.g. `Total 42/70`. No hidden weighting.
- **Independence column** (NEXUS): note shared antecedents — two vectors on the same root count once, not twice. Guards "1 root in 6 costumes."

## 3. THRESHOLDS (HENRY / LIQUID / BOND)

*Reconciliation (BOND vs HENRY conflict): durable **rules** carry NO live values (anti-drift); the live **read** lives in STATUS with `[src M/D]` + as-of. Same metric, two surfaces — never one drifting copy.*

- **Durable banded rules** (HENRY), in CLAUDE.md / a stable doc: `Metric | Yellow | Orange | Red | Routes to →`. Routing is inline and addressee-specific.
- **Live banded read**, in STATUS: current value + as-of + which band + cushion. Sourced, dated, never naked.
- **Conjunction triggers** (LIQUID): compound `A AND B` where a single metric would knee-jerk.
- **KILL_MEMO** (LIQUID): for any cascade trigger, a pre-written ladder file (durable, decoupled from STATUS rewrites).

## 4. INVALIDATION / EXIT (LIQUID / HENRY / BRENT)

- **Channel-kill vs thesis-kill** (LIQUID): distinguish a dead *channel* from a dead *thesis*; allow partial kills + state the migration path. Prevents false thesis-death.
- **Standing-rule-vs-state triad** (HENRY): live table — `leg | standing rule | current state @ level | FIRED / NOT-FIRED` + a literal fired-count.
- **Bidirectional "cleanest flip each way"** (BRENT): name the single thing that would falsify the thesis in BOTH directions, testable at the next data release.
- **Session counts mandatory**: "sustained" always carries an `N+ sessions` count. No vague thresholds; none already-breached at write time.

## 5. PREDICTIONS (OTTO / CARL / VIOLET)

- **Ledger + archive + calibration scoreboard** (OTTO): `PREDICTIONS.tsv` live; resolved rows → `PREDICTIONS_ARCHIVE.md` with post-mortems; **failure-pattern synthesis fed back into the thesis** as rules gating future predictions. (This is the agent's institutional-learning loop — the market-agent analogue of DAEDALUS's own PATTERNS.tsv.)
- **If-falsified action column** (CARL): every prediction carries its position consequence (`→ trim 25%, extend duration, −25pp conf`), not just a confidence number.
- **Confidence tiers** (VIOLET): `EMPIRICAL / PROVISIONAL / ASSUMPTION` — never load-bear on N=1.
- **Boot resolution**: scan past-trigger rows at boot; resolve HIT/MISS/TRUE-letter-FALSE-spirit/FALSIFIED; never leave OPEN-but-stale.

## 6. CROSS-AGENT ROUTING (MARCO / LIQUID / NEXUS)

- **Standing route-matrix** (MARCO) in CLAUDE.md: `condition → target → priority`, conditional, maintained as standing rules.
- **NEXUS_BRIEF.md writeback every closeout** (sync-point, curated) + **outbox crisis-only** (🔴 async). Kills notification fatigue.
- Route to the **domain owner**, not the transmission-adjacent agent.

## 7. STANDING DISCIPLINES (MARCO / NEXUS)

- **Mechanism-vs-thermometer split** (MARCO): separate high-confidence *mechanism* from its confounded *readout*; the thesis survives a bad thermometer.
- **EXPECTED_SIGNALS** (MARCO): track signals that *should* appear if the thesis holds — their absence is data.
- **Three-column Δ discipline** (NEXUS): `metric · Δ signed pp · last-updated`; bump only on material change.
- **Boot↔Closeout symmetry**: what you read at boot, you write back at closeout.

## 8. BOTTOM LINE (required)

End STATUS.md with 2–4 plain-language sentences: domain state now, the single most important thing, what's next. Update every session. STATUS under 250 lines — archive overflow to `domain/sources/`.

---

*Open for Will: §3 reconciliation (durable-rule-vs-live-value split) is a design call, not a harvested fact — veto-able.*
