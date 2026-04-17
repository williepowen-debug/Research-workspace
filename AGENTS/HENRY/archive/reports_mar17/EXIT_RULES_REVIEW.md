# EXIT RULES REVIEW — HENRY
**Authored:** 2026-03-06 | **Reviewing draft submitted to PROME**

---

## OVERALL ASSESSMENT

The draft framework is structurally sound — right categories (thesis kill vs position-specific vs convergence downgrade), right approach (falsification vs price targets). Core issue: **some thresholds are internally inconsistent with current data**, and **two significant exit triggers are missing entirely**.

---

## 1. ARE THESE THRESHOLDS CORRECT?

### Thesis Kill

**BTFP 2.0 / Fed backstop** ✅ Correct. A backstop announcement would break the credit stress transmission chain entirely — HY OAS would compress, quality rotation reverses, the "Loaded Machine" unloads in the wrong direction. No issues here.

**HY OAS reverses below 260bps sustained** ✅ Reasonable floor. Current sequence: 265 (Jan) → 284 (Feb peak) → 312 (Mar 3 peak) → 308 → 297 (Mar 4 confirmed). At 260bps we'd be below the January baseline — below where this thesis began. That's a correct kill level. One note: "sustained" needs a session count. Recommend specifying 10+ sessions explicitly (not just directional dip).

### Position-Specific

**IWM $250P: ISM Mfg >52 for 2 months + claims <220K** ⚠️ **Partially triggered already.** Claims are currently 213K (Feb 28 week confirmed). The claims leg of this exit condition is essentially met NOW. If you're writing this exit rule, claims need to be reset to a lower level OR the condition needs to reflect improvement *from current levels*, not an absolute floor that's already breached.

**Suggested revision:** ISM Mfg >52 for 2 consecutive months + claims sustained *below 200K* (i.e., net tightening from here) — OR drop the claims leg entirely and let ISM Mfg carry the exit.

**HYG $75P: HY OAS reverses below 275bps for 5+ sessions** ⚠️ **Threshold is too tight.** The floor has been rising: 265 Jan → 284 Feb → 308 Mar peak → 297 current. A reversal to 275bps is only a 22bps move from here, which can happen in a single week of risk-on (we saw -11bps on Mar 4 alone during a one-day relief rally). 5 sessions at 275bps could be triggered by a normal NFP beat bounce without the thesis actually breaking.

**Suggested revision:** Exit HYG $75P if HY OAS reverses below **265bps** (back to January baseline, meaning the entire rising-floor thesis is invalidated) sustained 10+ sessions. Or keep 275bps but extend to 15+ sessions.

### Convergence Downgrade (trim 50%)

**NFP >200K + ADP confirms** ✅ Correct. ADP printed +63K this cycle. A >200K NFP beat would be a massive miss on the stagflation leg. Valid trigger. One refinement: since HEN-01 resolves Mar 6 (imminently), this rule should apply to the *next* NFP cycle (April) for the ongoing trim decision.

**VIX sustained <16 for 2 weeks** ✅ Directionally correct. VIX is currently ~23-25; reaching <16 would require a dramatic structural reset. Two-week threshold is reasonable. No changes suggested.

**SPX reclaims 200-day MA (6,902) on closing basis for 3 sessions** ✅ Level confirmed in STATUS.md and KEY LEVELS table. This is exactly the gamma flip point — above 6,902 = dealer hedging becomes a tailwind (positive gamma), meaning the mechanical cascade thesis breaks. 3-session close threshold is appropriate (avoids fakeout flushes above). No changes.

---

## 2. MISSING EXIT TRIGGERS

### Missing: Geopolitical De-escalation (Hormuz)
Brent is at $84.75 (+4%) and the Hormuz premium is embedding into the stagflation narrative. If Hormuz reopens / ceasefire announced and Brent drops back toward $72-75, the "Fed trapped by oil" leg collapses. This would downgrade vectors 4 (Stagflation), 9 (Geo/Commodity), and potentially 6 (Vol Structure) simultaneously.

**Suggested addition (Convergence downgrade):** Brent crude closes below $76 for 5+ sessions → trim 30-50% (stagflation input signal weakens, Fed cut path reopens, risk-on bid).

### Missing: FOMC Surprise Cut
Currently pricing FOMC hold (HEN-04, 70% confidence). If FOMC cuts in March — even 25bps — it signals the Fed sees growth risk as primary. This would initially be bearish-for-HY-spreads-wrong: a cut could tighten HY OAS as credit stress softens. The thesis doesn't automatically break, but the rate path thesis needs reassessment.

**Suggested addition (Convergence downgrade):** Unscheduled inter-meeting FOMC cut OR March 18 cut → immediately reassess H4 (equity cannot bottom until HY OAS peaks) — credit may bottom faster than expected.

### Missing: Time-Based Expiry Review
Both positions expire Jun 2026. No time-based review trigger exists. At 60 days to expiry (approximately Apr 6), theta decay accelerates meaningfully for OTM puts. If thesis hasn't materialized by then (HY OAS <330bps, IWM still above $240), consider rolling or trimming regardless of signal state.

**Suggested addition:** 60-day to expiry review (mandatory) — if underlying hasn't moved meaningfully toward strike, evaluate roll vs hold vs trim independent of macro thesis.

---

## 3. THRESHOLDS TOO TIGHT OR TOO LOOSE?

| Rule | Assessment | Reason |
|------|-----------|--------|
| HYG exit: OAS <275bps / 5 sessions | **Too tight / too short** | 22bps reversal happened in a single day (Mar 4). 5 sessions is 1 week. |
| IWM exit: claims <220K | **Already breached (213K)** | Condition partially met NOW — not a forward-looking threshold |
| NFP >200K convergence trim | **Slightly loose** | Should specify whether it's the next single print or must persist across 2 months |
| HY OAS thesis kill <260bps | **Reasonable but needs session count** | "Sustained" is vague without a number |
| SPX 200-day MA (6,902) / 3 sessions | **Correct** | Matches KEY LEVELS table exactly |
| VIX <16 / 2 weeks | **Slightly loose** | From ~24, this is a 33% VIX compression — may want to also add "VIX inverts back to contango (near-term futures premium returns)" as an earlier signal |

---

## 4. SUGGESTED CHANGES — SUMMARY TABLE

| Original | Issue | Suggested Revision |
|----------|-------|-------------------|
| HYG $75P: OAS <275bps / 5 sessions | Too easy to trigger on noise | OAS <265bps sustained 10+ sessions |
| IWM $250P: claims <220K | Already at 213K | Claims <200K sustained OR drop claims leg entirely |
| HY OAS kill <260bps "sustained" | Session count ambiguous | Add "10+ consecutive sessions" |
| NFP >200K trim | Time ambiguity | Specify "single print + ADP confirms same month" |
| [MISSING] Hormuz/Brent | Geopolitical leg has no exit | Add: Brent <$76 / 5 sessions → convergence downgrade |
| [MISSING] FOMC surprise cut | Rate path flip has no trigger | Add: FOMC cut in March → H4 immediate reassessment |
| [MISSING] Time decay | Jun 2026 expiry has no review | Add: 60-DTE mandatory review (≈Apr 6) |

---

## BOTTOM LINE

The draft is 80% right. The structural categories (kill / position-specific / trim) are correct and match how REGINALD formats his rules. The main problems are:
1. **Claims threshold already breached** — needs recalibration
2. **HYG OAS threshold too loose** — single week of risk-on could falsely trigger
3. **Two material exit vectors missing** — Hormuz de-escalation, time decay
4. **"Sustained" needs session counts throughout**

Fix those four points and this is a solid falsification framework.

*— HENRY | Domain: Velocity / Derivatives / Credit Transmission*
