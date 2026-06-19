---
name: finding-risk-control-separate-from-sizing
description: "When a hard trigger's conditional leg collapses post-binary-event (e.g., AND-condition leg goes permanently true/false), the stop is functionally DISARMED — that's a risk-control gap requiring immediate re-spec, distinct from any sizing decision. \"No sizing rec yet\" should not quietly mean \"ride unprotected.\" Will Jun 18 2026 distinguished the two on SAM's post-BOJ AND-stop collapse."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 74e6629c-7de8-44a9-8f52-2e2d3a93c875
---

When you manage a position with a conditional-trigger stop (AND / OR composition of multiple legs), a post-event audit must check whether any leg has gone permanently true or false. If it has, the stop is functionally disarmed and needs immediate re-spec — **independent of any sizing decision the post-event audit will produce.**

**Incident (SAM Jun 18 2026 — Step 1.5 stop re-arm).** SAM's pre-event STRATEGY had a post-event AND-condition stop: exit if (a) BOJ turned dovish at Jun 16 meeting AND (b) USDJPY at/above 167 with no MOF response. BOJ hiked to 1.00% Jun 16 (modal as-priced). The "BOJ dovish" leg of the AND condition was now **permanently FALSE** — the AND could never fire — the shares were operationally **unprotected**, not just "stop wide." Hawkish Fed Jun 17 (Warsh debut +40bp dot) then accelerated USDJPY 161.34 with no MOF, drifting toward the dead stop's $167 reference level. The disarmed-AND gap sat for ~2 days post-event before being audited.

**Will's framing (the load-bearing call).** PROME initially folded "stop re-arm" into the v1.6 re-underwrite (which was post-CPI / post-RED / post-Sat-Jun-20-CFTC — multiple days out). Will distinguished sharply: **the disarmed AND-stop is a separate, interim *risk-control* item**, not a sizing decision. Specifically: "no sizing rec until after the v1.6 audit + CPI. But the disarmed AND-stop is a separate, cheap interim risk-control item (the shares are currently unprotected; the 'BOJ dovish' leg is permanently false now). It's ~$40 of exposure, so minor — but 'no sizing rec yet' shouldn't quietly mean 'ride unprotected.' Will can re-arm a single-leg stop now independent of the v1.6 sizing decision. **Risk-control ≠ recommendation.**"

The Step 1.5 stop re-arm collapsed the dead BOJ-dovish leg out: single-leg stop at FXY ≤ $55.05 (preserving the pre-approved Jun-3 price level without the dead conjunction). Interim risk-control; v1.6 may tighten or replace based on the pillar audit.

**Why the two get confused.** Both involve "what stop should the position have?" Both will get touched at v1.6 finalize. So the lazy default is to lump them under "wait for v1.6" — which leaves the position effectively unprotected during the 2-7 day window between the binary event and the v1.6 finalize. That window can carry real downside.

**How to apply:**

1. **Post-binary-event stop-spec audit.** After any binary catalyst resolves (Fed meeting, BOJ meeting, earnings, election, regulatory decision), audit every conditional leg of every active stop:
   - Did any leg go permanently TRUE? (e.g., "stock holds above $X" — if it already broke $X yesterday and recovered, can the leg ever go true again in the relevant window?)
   - Did any leg go permanently FALSE? (e.g., "BOJ dovish" — if BOJ already hiked, the dovish leg is permanently false until the *next* meeting)
   - For AND-conditions: if any leg is permanently false, the AND is permanently false → stop is disarmed
   - For OR-conditions: if all but one leg is permanently false, the OR collapses to single-leg → stop spec is effectively narrower than authored
2. **Re-spec as INTERIM risk-control.** If a leg has collapsed, propose a re-spec that collapses the dead leg out — preserving the pre-approved price level where possible — and label it explicitly as **INTERIM**. This is not a re-derivation; it's a cleanup of a defunct spec.
3. **Keep it separate from sizing.** Frame the re-spec to Will (or the position owner) as "risk-control re-arm — does NOT propose adding/trimming size, just closes the gap left by the dead leg. Sizing rec follows from the larger v1.6/re-underwrite audit." Will's distinction (Jun 18 2026): "Risk-control ≠ recommendation."
4. **Cost-justify the interim status.** ~$1.81 of additional FXY drawdown to the existing pre-approved $55.05 level was acceptable to Will as interim risk-control — the alternative was a tighter spec (Option (b): USDJPY ≥162.5) that required fresh approval. Match the interim-vs-fresh-decision discriminator to the position size: small position (e.g., SAM's $798), interim is fine; larger position, may justify the fresh decision.

**Cross-applicable.** Any agent managing positions with conditional-trigger stops:
- **HENRY** — equity-vol positions often have multi-leg conditional exits (VIX level AND time decay; gamma squeeze AND chain-state)
- **LIQUID** — UST positions with AND-stops on yield + funding signals
- **BROCK / CARL / REGINALD** — credit positions with AND-stops on spread + ratings + collateral
- **OZK** — single-name with AND-stops on price + filing trigger
- **FORGE** — any active trade spec with composite-condition stops; audit at every binary catalyst resolution

**The lesson generalizes.** Any spec with composite conditions (stops, alerts, rebalance triggers, escalation rules) needs a post-binary-event audit pass to check whether any leg has collapsed. Disarmed specs are the cheapest production bug: the code didn't change, the world did.

Related: [[feedback_position_cost_basis_not_authoritative]] (verify with Will, don't assume STATUS values are live); [[feedback_exit_recommendations_need_mark_context]] (surface execution-mark context before recommending close-now); [[feedback_dont_bank_unpassed_forecast]] (a pending event isn't resolved until it clears — same logic in reverse: a *resolved* event's downstream consequences need explicit audit).
