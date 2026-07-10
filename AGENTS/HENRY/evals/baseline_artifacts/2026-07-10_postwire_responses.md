# Eval run 2026-07-10 — post-PAT-040-wiring re-run (01, 02) + case-03 first baseline

**Authorization:** Will, in-session via PROME, 2026-07-10 ~10:45 ET (continuation of the full-boot spawn that wired boot.py as CLAUDE.md step 3c).

**⚠️ METHODOLOGY DEVIATIONS from evals/README (record, don't hide):**
1. **Runner surface = fresh-context general-purpose subagents** instructed to read `AGENTS/HENRY/CLAUDE.md` only (skip-boot enforced), NOT a fresh interactive Claude Code session launched in `AGENTS/HENRY/`. README §"Why fresh session, not sub-agent" flags that sub-agents don't trigger the identical CLAUDE.md/auto-memory load path — here the harness injected root CLAUDE.md + the auto-memory index, and HENRY/CLAUDE.md was read explicitly, which approximates but does not equal the canonical surface.
2. **Scorer = HENRY (this session), not Will.** Contamination boundary preserved in one direction: rubrics were NOT read until after all three runners had responded; runner prompts contained INPUT-block text only.
3. **Consequence:** treat these as **provisional/proxy results**. They are evidence the wired surface didn't regress; they do NOT replace the canonical fresh-session, Will-scored run if Will wants gold-standard numbers.

**Case-maintenance flag (case 01):** the INPUT's scenario is vintage-locked to ~6/15 ("data = 6/12 close"), but a runner dated 7/10 correctly noted the file is ALSO ~4 weeks old in absolute terms. The rubric's "current to 6/12, ~3 days old" phrasing is run-date-dependent; the core discriminator (B-over-A, reject "stale to 6/1") is date-robust. Scored on the discriminator. Consider pinning "assume today is 2026-06-15" into the INPUT block at next case revision.

---

## Case 01 — sibling staleness (TARGET) — runner aa84c7fa693104d74

**Verdict: PASS.** All 4 EXPECTED met: (1) rejected "stale to 6/1" explicitly ("dead wrong... she booted, she posted the post-NFP reads"), identified Last Updated 6/14 / data 6/12, plus the correct dual framing (fresher-than-my-note AND too old for a live 7/10 read — invoked the >24h stale-data rule unprompted); (2) carried M1:M2 +9.41% and 20d-SKEW 141.01, explicitly retired 12.93/138.99, got the CCC 9.56/9.55 credit-gate bonus; (3) dep row rewritten "Post-NFP owes CLEARED"; (4) process note = "a staleness claim about another agent is itself dated data... check the counterparty's Last-Updated line before repeating" — clean paraphrase, no rubric echo. Zero DO-NOTs.

[Full response preserved in the eval-run transcript; key excerpts above. Runner tool_uses=1 (CLAUDE.md read only), ~56s.]

## Case 02 — catalyst vs pricing (GUARDRAIL) — runner a17a26618417ba7c3

**Verdict: PASS.** All 4 EXPECTED met: (1) "Sign-off: NO"; (2) reason = 0-cuts ~78% priced, "you don't get +12bps for telling the market what it already told you" — cited the banked auto-memory finding by name (anchor_prediction_to_surprise_not_priced = principle applied from the loaded surface, the intended mechanism); (3) re-anchored via a 3-branch trigger table keyed to deviation-from-pricing (modal ≈ noise band ±6bp; hawkish surprise = hike-leaning dot/next-yr cuts stripped → +10-18bp); (4) **label inversion nailed**: dovish surprise = the dots KEEP the prior 1 cut → 10Y −10 to −18bp, bull steepener. Bonus: flagged the 10Y-eased-into-meeting positioning AND the futures-vs-prediction-market venue spread w/ thin-liquidity haircut. Zero DO-NOTs; no rubric-phrase echo ("hawkish-OF-pricing" never appears).

## Case 03 — KRE rate-vs-credit (GUARDRAIL) — runner aa1e16d6e0b85ef55 — **FIRST BASELINE**

**Verdict: PASS.** All 5 EXPECTED met: (1) "Credit trade, not margin trade — and it's not close"; (2) divergence read explicit — KRE −4.1% DESPITE the flight-to-safety 10Y −12bp, "the Treasury rally is being rejected as a circuit breaker," attributed to its own CLAUDE.md attribution test; (3) corroboration table (HY +19bp/day rate-of-change + CRE charge-off + read-across via non-top-holding extrapolation); (4) "gap risk, not grind — the colleague's floor is a trapdoor," H4 credit-leads-equity invoked with the OAS-momentum no-bottom rule; (5) REGINALD flagged RED (+ LIQUID RED, PROME level-gated — correctly refused to fire threshold signals off deltas without live levels, and correctly withheld the vol broadcast as VIOLET's lane). Zero DO-NOTs. Contamination: "credit story is dominating" is CLAUDE.md-body language (always-loaded, expected per rubric), not rubric leakage.

---

**Net:** 3/3 PASS under the newly wired boot surface (step 3c live). Promotion bar (TARGET improves-or-holds + GUARDRAILS hold) met with the proxy caveat. Case 03's baseline is now on file — the harness is a full 3-case net for the next protocol change.
