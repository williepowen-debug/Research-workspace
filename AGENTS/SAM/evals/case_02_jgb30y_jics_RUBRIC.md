# CASE 02 — JGB 30Y 4.0% Breach — RUBRIC

> ⚠️ **SCORER ONLY — DO NOT PASTE INTO RUNNER.**
> This file contains the answer key. If any of this language enters the runner's prompt, the case is contaminated and the result is invalid.

**Pairs with:** `case_02_jgb30y_jics_INPUT.md`

**What this tests:** Whether SAM correctly frames **lifer absence at the long end as the CAUSE of the JGB 30Y blowout, not the consequence** — i.e., applies the J-ICS structural inversion vs the pre-J-ICS muscle-memory framing ("higher yields will draw insurers back").

**Lesson source:** THESIS Channel 1 § "Lifer Long-End Abandonment — JGB 30Y/40Y driver" (kept live in v1.5 / v1.5.1; DOMESTIC mechanism, independent of foreign-asset transmission) — the explicit "critical inversion" subsection on causal direction.

**Failure mode this guards against:** Pre-J-ICS reflex that says "yields reach an attractive level → buyers re-emerge → curve stabilizes." Under J-ICS solvency repricing, that reflex is structurally broken — but it's the dominant heuristic in fixed-income reasoning and easy to fall back into.

**Frozen historical date:** 2026-05-15 (JGB 30Y first prints 4.000%).

---

## EXPECTED — all must be met for PASS

Score each as MET / NOT MET / BORDERLINE. Borderline = FAIL per discipline rule.

Criteria are assertion-shape (test the concept), not quote-shape (test the words). Exact phrasing flexible — concept must be present.

- [ ] **Cites J-ICS as the operative regime.** Names the regime by name (or equivalent specific reference to the April 2025 solvency framework change) as a load-bearing factor in the analysis.

- [ ] **Causal direction is correct: lifer absence → yield blowout.** This is the load-bearing checkbox. The response must put the causal arrow such that lifer withdrawal explains the yield move. Acceptable: "the buyer strike is driving this," "absence is causing the move," "yields are clearing higher because the structural bid has gone." Unacceptable: any phrasing that puts yields → behavior (lifers sidelined BY the yields, lifers will be drawn IN by the yields), since that inverts the causality this case is testing.

- [ ] **Rejects the "yields draw insurers back" reflex.** Concludes that higher yields will NOT bring lifers back to the long end at any near-term level. Frames the reflex itself as broken under the current regime.

- [ ] **Explains why super-long is structurally unattractive under J-ICS — beyond just citing J-ICS by name.** Must connect duration repricing to solvency capital impact AND explain why this dominates the yield-pickup motivation for long duration. *(Wording is flexible. The test is whether the response articulates the structural disincentive, not whether it uses any particular phrase. If the response only names J-ICS and asserts "this is bad for lifers" without connecting the mechanism, score NOT MET.)*

- [ ] **Reconciles the 20Y/2Y strong-auction divergence as REINFORCING, not contradicting.** Engages with the 20Y BTC 4.82x and 2Y BTC 5.24x data. Frames it as evidence of a duration-specific buyer-strike pattern (insurer demand intact where J-ICS penalty is manageable, absent where it isn't). Does NOT treat the strong auctions as evidence the stress is passing.

- [ ] **BOJ implication: more pressure to act.** Concludes JGB long-end pressure pushes BOJ toward EITHER (a) policy normalization / hike to legitimize the curve, OR (b) some form of long-end-specific intervention (YCC-style cap, super-long-specific operation). Either path counts. Does NOT conclude that BOJ will sit out because "the market is solving it."

- [ ] **Reconciles the yen-weaker-vs-JGB-stress observation correctly.** Acknowledges the apparent paradox and resolves it via rate-differential dominance on short horizons, or fiscal-supply concerns pushing yields without pulling yen, or some other coherent decoupling explanation. Does NOT say "yen weakness disproves the JGB-stress story."

---

## DO NOT — any of these = FAIL even if EXPECTED met

- [ ] **Says "higher yields will eventually bring insurers back to the long end."** Canonical wrong answer. Any phrasing that puts the causal arrow yield → behavior under J-ICS is the failure mode.

- [ ] **Recommends buying JGB long-end as a "stabilizer" trade** on the thesis that lifers will re-emerge.

- [ ] **Concludes BOJ will wait it out.** Long-end stress without intervention or hike pressure does not stabilize on its own under J-ICS.

- [ ] **Mis-frames the 20Y vs 30Y/40Y divergence** as evidence of "stress passing" or "buyer demand normalizing."

- [ ] **Treats yen-weaker as thesis-breaking.** Short-horizon FX moves driven by rate-differential don't disprove the JGB-stress / Channel 1 framework.

- [ ] **Cites SMR as the operative current regime.** SMR was the pre-2025 framework. Confusing SMR with J-ICS is a structural error.

---

## Contamination check (post-response)

Before scoring PASS, scan the response for these contamination signatures:

- **Verbatim phrase from RUBRIC.** If the response contains a phrase that appears verbatim or near-verbatim in this file (and not in the INPUT), the rubric leaked. Particular watch-phrases: "solvency-capital strain," "yield pickup compensates for," "structurally punitive." These are RUBRIC-specific constructions.
- **Cites J-ICS exactly once with no surrounding articulation of the mechanism.** May indicate the runner pattern-matched the J-ICS cue rather than reasoned from it.
- **Uses bullet structure that mirrors EXPECTED checkboxes.** May indicate the runner formatted its response against the rubric structure.

If any contamination signature appears, log result as `PASS-CAVEATED` or `FAIL-CONTAMINATED` and note the signature in `results.tsv` notes column.

---

## Notes for the scorer (Will)

- The single most important checkbox is **causal direction**. If SAM gets the causality wrong (yields → behavior rather than behavior → yields), the case fails regardless of other checkboxes — this is the structural-inversion test, and inversion is what's being tested.
- Watch for hedge language. "Lifers may eventually return" is borderline — push to FAIL unless SAM explicitly conditions it on J-ICS being unwound or solvency rules relaxed.
- The 20Y/2Y auction contrast is a subtle test. If SAM ignores it, that's missing information — score that specific checkbox as NOT MET (not BORDERLINE — silence is non-engagement).
- BOJ implication has TWO acceptable paths (hike OR long-end-specific operation / YCC-style cap). Either counts. "BOJ stays put" does not.
- If SAM tries to read additional state files despite the DO-NOT-BOOT instruction, that's a soft fail signal — note in `results.tsv`. SAM honoring the skip-boot instruction is part of the test infrastructure.
