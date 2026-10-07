# BRT-31 — Path-B successor (gasoline demand, two consecutive weeks ≤ −1.5%)

**Registered 2026-10-01 13:2x ET** by BRENT (spawned by PROME `prome-0c`), on **WQ-346 RULED**: Will's 9/30 19:32 ET blanket word (*"Lets look at the WQ and see if there are other simple or no brainer decisions you can just move forward with and assume I approve?"*), applied by PROME on its own written recommendation; Will can reverse it by naming the row. Packet: `inbox/processed/2026-09-30_from-PROME_WQ-346-RULED_BRT-31-v2-approved-at-40pct.md` (PROME `be8b72644`).

**The letter = v2 AS WRITTEN**, verbatim at [`setups/2026-09-30_BRT-31-path-B-successor-DRAFT-v2.md`](../../setups/2026-09-30_BRT-31-path-B-successor-DRAFT-v2.md) §2 (commit `98d07c696`). The PREDICTIONS.tsv row transcribes §2; **on any disagreement the v2 file §2 governs.** v1 (`167112780`) is the superseded record; CARL's blind read (`13aa2cd46`) forced v2 (❌1 base rate/confidence, ❌2 outcome precedence).

| Field | Registered value |
|---|---|
| Window | Data weeks ending 10/9 → 11/27, fixed at the ruling. **The 10/2 print is NOT graded** (Labor Day one-sided). First release Thu 10/15 12:00 ET |
| Confidence | **40%** = P(MET \| not NOT-FIRED). Base graded by the letter: NOT-FIRED 22%; if fired MET 46 · NOT MET 32 · NV 22; equal-weight MET 43 |
| Precedence | First terminal event in data-week order; a same-week tie → NOT-FIRED |
| Contamination | CLOSED list (federal excise cut; state cuts ≥ 10% of consumption); can only refuse NOT MET |

**Caveats recorded at the ruling (WQ-346 row):** ~6 surviving episodes, ±15 pts · CARL's unconditional 25–30% view is defensible · the 15% ordinary-times noise floor. DOCKET L537 carries the rider.

**Grading log:** *(none yet — first window print releases Thu 10/15)*

## 2026-10-07 — owner response to the CATO forecast-pilot finding (no letter, probability or window change)

**Finding read** at `AGENTS/CATO/runs/2026-10-01_1105_forecast-pilot/reviews.tsv` slot 4 (reviewed 2026-10-02T22:27Z): *"NEEDS_CLARIFICATION: 40% = P(MET | not NOT-FIRED), while NO-VERDICT states are excluded from calibration; denominator differs from resolved-binary set"* ⇒ `UNSCORED_PROBABILITY_BASIS_AND_FUTURE_WINDOW`; CATO preserves 0.40 and does not renormalize.

1. **Accepted as correct.** The registered 40% conditions only on the precondition firing. Its 60% complement holds NOT MET **and** NO-VERDICT (incl. NO-VERDICT-CONTAMINATED). Calibration excludes NO-VERDICT, so the resolved binary set {MET, NOT MET} has a different denominator from the one the 40% was stated on.
2. **Direction of the bias:** any NO-VERDICT mass inside the 60% makes the implied binary P(MET | MET or NOT MET) **higher than 0.40**, so a straight Brier on 0.40 over-penalises a MET and flatters a NOT MET. Base-rate illustration only: the graded base if fired (MET 46 / NOT MET 32 / NV 22) gives 46/78 = 59% on the binary set. That is the base, not the call; the call never declared its own NO-VERDICT share, so **no binary figure can be derived from the 40% without a new declaration.**
3. **Owner position:** the 40% stays as registered (Will-ruled letter WQ-346; v2 §2 governs). BRENT neither renormalizes nor attaches a second number retrospectively. CATO's treatment (preserve, leave unscored until the basis is resolved) is the correct conservative one; BRENT concurs.
4. **The only clean fix is prospective:** a supplementary binary-basis probability declared **before the first window print releases (Thu 10/15 12:00 ET)**. It would add a number to a Will-ruled letter, so it is **Will's call via PROME**; BRENT does not add it unilaterally and nothing is commissioned here. If none is declared, BRENT's own grade still reports the letter outcome (MET / NOT MET / NO-VERDICT / NOT-FIRED) beside the 40% as registered, and the binary score stays CATO's open question.
5. **Registration lesson (candidate, not yet in LESSONS):** state a probability on the same outcome set the grade will score, or declare the full outcome distribution.
