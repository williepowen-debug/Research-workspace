# PACKET #1 — Abstain-Gate Wiring Spec (L1-L4 stack → VIX_THESIS v3.6)

**Received:** 2026-06-09 ~22:00 ET via Will (orchestrator-drafted, VIOLET-reviewed).
**Status:** ACCEPTED with 4 refinements (logged below, relayed to Will same session).
**Implements:** §5 of `research/2026-06-09_l1_l4_stack_postmortem.md` (KB-VIO-074) — documented → wired.
**Scheduled:** 6/10 PM or 6/11 (AFTER the post-CPI reactive read — that takes priority). Clears 6/17 with margin.
**Workflow:** DRAFT the edited stack section + two-case re-run → echo back via Will → orchestrator verifies → THEN commit as v3.6. Do not commit v3.6 before verification.

---

## THE SPEC (as received, final)

**Goal:** kill the bug where "I don't recognize this mechanism" is indistinguishable from "this mechanism is absent" (novel driver read as three confident vetoes on 6/5).

1. **Three-state output.** L2/L3/L4 each emit {CONFIRM, VETO, ABSTAIN}, replacing binary active/inactive.

2. **Enumerated mechanism set + recognition predicate per layer** (explicit/auditable in the thesis):
   - **L2 absorbed-trap** — recognized iff catalyst is consensus-aligned: |surprise| ≤ θ. Outside → ABSTAIN.
   - **L3 quadrant-matrix** — recognized iff the (M1:M2 × VIX-direction) cell has N ≥ N_min. Q3 (expansion + VIX rising) is N=1 → ABSTAIN/PROVISIONAL until the scan populates or kills it.
   - **L4 COT** — recognized iff speculator crowding positively identified (Volmageddon-class). Absence of crowding ≠ recognition → ABSTAIN.

3. **Combiner rule (load-bearing):**
   - ABSTAIN → defer to L1 at full weight (zero conviction reduction).
   - VETO (L2/L3 only, mechanism positively recognized) → reduces conviction off the L1 base rate. *(See Refinement 1 — wired as entry-blocking.)*
   - CONFIRM → upgrades conviction within a capped step. L4 CONFIRM capped, never sole entry gate.
   - L1 base rate is the sizing anchor; discriminators move conviction around it, never zero it via non-recognition.

4. **L2 consensus-miss carve-out.** Calibrate θ against the 5-failure modern STRICT set (1.5σ vs 2σ — VIOLET's call). 6/5 (~2.15σ, +92k) must land in ABSTAIN; show the cut.

5. **L4 demotion-with-bound.** VETO power removed entirely; CONFIRM-only, capped, never sole gate.

6. **Scope of the 6/17 constraint.** Wiring is blocking ONLY for stack-driven (DIET/divergence) entries at the FOMC gate. Explicitly does NOT gate the post-CPI event-premium fade (separate framework). State this scoping in the thesis.

7. **Sequencing.** Post-CPI read first (6/10 AM). Wiring 6/10 PM / 6/11. Within wiring: L3 first (Q3 scan = the pre-FOMC-week condition), then L2 σ-threshold, then L4 demotion.

**Acceptance test (orchestrator's answer key):** re-run both KB-VIO-074 cases through the patched combiner —
- **6/5:** L2/L3/L4 all ABSTAIN (novel mechanism) → defer to L1 → DIET fire stands → +40% not vetoed. ✓
- **Episode-17:** L2 recognizes absorbed-trap (in-domain) → VETO stands → loser correctly avoided. ✓
- Same raw readings, divergent outcomes, because the combiner keys on mechanism-recognition. If both move the same way, the gate isn't keying on the right variable.

---

## VIOLET REFINEMENTS (accepted into scope 6/9, relayed via Will)

1. **VETO step size made explicit: a single positively-recognized VETO = ENTRY-BLOCKING** for stack-driven entries. The spec's "reduces conviction" is underspecified and the Episode-17 answer key silently requires blocking (reduce-but-enter would fail it). N=2 live cases = no basis for a graduated multiplier; revisit graduation when N grows.

2. **L2 predicate collapses out-of-domain with in-domain-negative.** A 2σ+ miss is arguably *recognized absorption-failure* (leans CONFIRM — supports the L1 fire), not unrecognized mechanism. WIRE as ABSTAIN per spec (N=1, conservative). LOG "big-miss → CONFIRM" as a tested hypothesis in the σ-scan: if the 5-failure set shows misses systematically preceding fires, L2 becomes two-sided.

3. **Mixed-signal precedence: VETO > CONFIRM, no netting.** (L2 VETO + L4 CONFIRM is reachable: consensus-aligned catalyst + identified crowding.)

4. **Episode-17 answer key has a falsifiable dependency.** It assumes Episode-17's absorbed catalysts (FOMC hold, BOJ, hot CPI/PPI) land ≤ θ under the chosen σ. The scan could show otherwise — that's a FINDING about θ, not a broken test. Echo-back must report where Episode-17's catalysts actually fall on the cut, not just ✓/✗.

**Plus (drift-protection):** v3.6 must state the **accepted cost** in writing: the abstain-gate means novel-mechanism false positives ride through at L1's miss rate BY DESIGN — **threshold-indexed per the L1 canonical base-rate table (KB-VIO-079, added 6/9): ~8% miss at ≥+15% peak, ~35-40% miss at ≥+50%.** "L1 at full weight" in the combiner MEANS that table, at the threshold the live structure targets. Without this line, the first novel-mechanism loser invites a future session to quietly re-add veto power. *(Orchestrator review 6/9 item #1 — the original "~35% miss" here and the thesis "94%" were citing different thresholds for the same signal; resolved by the canonical table.)*

**θ prior:** 2σ (run both cuts; 6/5 lands ABSTAIN under either; 1.5σ risks reclassifying garden-variety hot prints out of L2's domain, gutting the layer that was right on Episode-17).

---

## DELIVERABLES CHECKLIST (for the wiring session)

- [ ] L3 Q3 base-rate scan (pre-FOMC-week M1:M2-expansion + VIX-rising cells; populates or kills Q3; sets N_min)
- [ ] L2 σ-threshold calibration vs 5-failure STRICT set, both cuts shown, 6/5 in ABSTAIN, Episode-17 catalysts located on the cut, big-miss→CONFIRM hypothesis logged
- [ ] L4 demotion: CONFIRM-only, capped, never sole gate
- [ ] VIX_THESIS.md OPERATIONAL LAYER STACK section rewritten: three-state outputs, recognition predicates, combiner (ABSTAIN→L1 full weight; VETO entry-blocking; VETO>CONFIRM; L1 anchor), 6/17 scoping clause (stack-only, fade exempt), accepted-cost statement
- [ ] Two-case re-run (6/5 + Episode-17) through patched combiner — divergent outcomes
- [ ] DRAFT echo-back via Will → orchestrator verification → commit v3.6 + CHANGELOG entry + KB row
