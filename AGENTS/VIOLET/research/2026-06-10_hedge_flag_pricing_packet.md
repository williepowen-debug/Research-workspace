# Hedge-Flag Pricing Packet: Option-Implied vs Ladder Touch Probabilities

**Date:** 2026-06-10 ~6:45 PM ET (after-hours quotes — see caveats)
**Commissioned by:** Orch (item 3, Will-approved packet) — the falsifiable test for the standing HEDGING-PROTOCOL flag ("geopolitical event live = 2% VIX calls 30 DTE"), which has been flagged daily without decision. Test: if the market prices 24/25 touches materially below VIOLET's ladder (KB-VIO-087 refined), the hedge has positive EV on VIOLET's own numbers; if it agrees, the flag retires honestly.
**NOT a trade proposal.** Decision = Will. Pre-trade check = Orch.

---

## INPUTS

**VIOLET ladder (KB-VIO-087, from settle 22.22, lowest-base anchor 15.32, window ~Aug 12-21):**
P(touch 23) ~85% [spent] · **P(touch 24) ~60-70%** · **P(touch 25) ~40-50%** · P(touch 26) ~25-35%. Ordinal, n=6 (95% lower bound on a 6/6 is ~61% — locate the rung, don't polish digits).

**Option chain:** ^VIX calls, **Aug 19 expiry (69d — spans the ladder window)**, pulled ~6:45 PM via yfinance. Parity-implied forward ≈ **21.91** (vs spot settle 22.22 — mild backwardation-of-forward, consistent with mean-reversion pricing). Jul 22 chain pulled but **UNUSABLE** after hours (zero-bid strikes, incoherent spread-digitals — the known after-hours artifact, CALENDAR data-caveats).

## COMPARISON (Aug 19 expiry)

| Strike | Call mid (bid/ask) | IV | P(terminal > K): N(d2) | P(terminal > K): ±1 spread-digital | **Touch ≈ 2× terminal** | **VIOLET ladder** | Gap |
|---|---|---|---|---|---|---|---|
| 23 | 2.87 (2.48/3.25) | 82% | 0.38 | 0.21 | 0.42–0.75 | ~0.85 (spent) | excluded — spot 3.5% away |
| **24** | 2.56 (2.19/2.93) | 83% | 0.33 | 0.23 | **0.46–0.66** | **0.60–0.70** | **overlap — no material gap** |
| **25** | 2.40 (2.05/2.75) | 88% | 0.30 | 0.16 | **0.32–0.59** | **0.40–0.50** | **overlap — no material gap** |
| 26 | 2.25 (1.88/2.62) | 92% | 0.26 | 0.15 | 0.30–0.53 | 0.25–0.35 | market at/above ladder |

## VERDICT

**No material mispricing in either direction at the monetizable rungs.** The option-implied touch ranges (across the two estimators) overlap VIOLET's ladder at both 24 and 25; at 26 the market if anything prices MORE touch risk than the ladder. **The hedge does NOT have demonstrable positive EV on VIOLET's own numbers — the falsifiable test resolves toward retiring the flag honestly** (converting it from "market may be underpricing my modal path" to "market prices my modal path approximately fairly; buying it is paying fair value plus spread for convexity").

This also resolves the tension flagged at EOD ("my table says 60-70%, the surface says protection isn't bid"): SKEW/VVIX percentiles measure *relative* richness vs history, but the *absolute* strike pricing already embeds touch probabilities consistent with the ladder. The surface wasn't ignoring the war; it had it roughly priced.

## CAVEATS (all real, none verdict-flipping)

1. **After-hours quotes** — mids are indicative; bid/ask spreads are wide (±15-20% of mid). Re-pull intraday 6/11 before any decision leans on a specific number.
2. **Touch ≈ 2× terminal is a driftless-diffusion approximation.** VIX mean reversion pushes the true touch multiple ABOVE 2× for upper barriers (up-paths get pulled back before expiry) — which raises the option-implied touch estimates further and makes the "no edge for buying" verdict MORE robust, not less.
3. **Estimator disagreement** (N(d2) vs spread-digital) spans ~15-20 points — quote the range, never one number. The verdict (overlap) holds across the whole range.
4. **Expiry vs window mismatch is minor:** Aug 19 expiry vs window-close ~Aug 12-21. The 6/17 FOMC and BOJ sit inside both.
5. Ladder is ordinal (n=6); this comparison can only detect GROSS mispricing, which is exactly what it failed to find.

## DISPOSITION

- → Will: recommend the daily hedge-flag line in STATUS be **retired to a conditional** ("re-arm the flag if option-implied touch at 24-25 drops materially below the ladder, or on Hormuz-class leakage per HAWK's damage-vs-salvo frame") rather than re-flagged every session. Your call.
- Re-pull intraday 6/11 if acted on. KB row at next session if the disposition is adopted.
- Orch verification queue: estimator arithmetic + the parity-forward.
