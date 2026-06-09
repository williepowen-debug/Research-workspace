# L1–L4 Divergence Stack — Post-Mortem of the 6/5 Live Test

**Date:** 2026-06-09
**Author:** VIOLET
**Status:** Retrospective. Closes the 6/5 NEXT-SESSION item "L1-L4 stack post-mortem."
**Sources:** KB-VIO-067 (L1), KB-VIO-069 (L2), KB-VIO-068 (L3), KB-VIO-064/065 (L4), KB-VIO-070 (6/5 live test), KB-VIO-071 (hot-NFP analog universe), KB-VIO-073 (multi-root attribution). Underlying research: `2026-06-01_diet_coiled_spring_backtest.md`, `2026-06-01_episode17_postmortem.md`, `2026-06-01_feb2018_m1m2_volmageddon_analog.md`.

---

## One-line thesis

The 6/5 NFP shock was the first clean live test of the 4-layer divergence stack built over the 6/1 evening session. **The single mechanism-agnostic layer (L1, population/base-rate) paid forward exactly as backtested. All three mechanism-discriminator layers (L2–L4) failed — not because they were wrong about their own mechanisms, but because the actual driver (consensus-miss labor shock + AI/factor concentration unwind) was not in any of their enumerated mechanism sets.** A novel mechanism bypasses discriminator-layers silently and with false confidence; it cannot bypass a base-rate layer.

---

## 1. The stack as it stood pre-6/5

The stack was assembled to answer one question: *when a STRICT or DIET SKEW-divergence signature fires, should we size into it?* Episode-17 (4/13 STRICT fire, one of the cleanest signatures in the 19-yr sample) had been sized at **L1-only** and expired worthless — so L2–L4 were built to catch what L1-only missed.

| Layer | Name / KB | What it measures | What it was tuned to discriminate |
|-------|-----------|------------------|-----------------------------------|
| **L1** | Population context — KB-VIO-067 | Is the DIET/STRICT signature present, and what is its forward base rate? | **Mechanism-agnostic.** DIET (ΔSKEW≥+10, ΔVIX≤−2, ΔVVIX≤−10 / 20d) → 25 episodes/19yr, fwd60 VIX mean +30.7% (vs +7.1% NEITHER), peak>50% hit-rate 65%. Pure "signal present + history" — does not ask *why*. |
| **L2** | Regime-context-at-fire — KB-VIO-069 | Is the fire happening during vol BUILD-UP or vol DECAY? | **Absorbed-trap mechanism.** 5 modern STRICT failures shared 3 markers within 4td: prior-4wk VIX downward, post-fire SKEW breaks pre-fire avg in 2-3td, credit compressed. Fires in decay = "decay-as-divergence" → fail. Assumes catalysts stay **consensus-aligned** (absorbed). |
| **L3** | Direction-matrix — KB-VIO-068 | M1:M2 contango × spot-VIX direction quadrant | **Volmageddon-shape mechanism.** From Feb-2018: steep M1:M2 is "pre-spike pile-up" only if VIX is *rising* while contango compresses. Expanding contango + falling VIX = absorbed/inactive. |
| **L4** | Compound-confirmation entry — KB-VIO-064 refined + KB-VIO-065 COT | Positioning crowding / entry timing | **Short-vol-crowding-unwind mechanism.** COT Lev Money positioning to disambiguate whether crowding sets up a self-reinforcing unwind. |

**Key structural fact, visible only in hindsight:** L1 is the only layer that does not name a mechanism. L2 names "absorbed-trap," L3 names "Volmageddon pile-up," L4 names "short-vol crowding unwind." Each discriminator is exactly as good as its enumerated mechanism — and blind outside it.

Pre-6/5, the stack read the 6/1 setup as **absorbed-trap** across L1-L3 (same reading Episode-17 had at T+4), and was internally consistent. The triangulation *felt* like confirmation. It was actually three views of the same assumed mechanism.

---

## 2. The 6/5 event

| Fact | Value |
|------|-------|
| May NFP | 172k vs **80k** consensus (Dow Jones, corrected per KB-VIO-073) = ~2.15× beat, **+92k surprise** |
| DGS2 | +6–7bp (just **below** the ≥8bp hot-NFP rate-shock filter) |
| VIX | **+40%** to 21.51 — worst SPX day (−2.64%) since October |
| Concentration leg | NVDA −6%, memory-chip ETF −15%, Nasdaq −4.1%, single-name vega cascade |
| Credit | HY 2.74 flat, did NOT crack |
| Cross-asset | MOVE +5.68%, gold −3.65% (crashed = rate-shock, not flight-to-safety) |

**The actual mechanism (KB-VIO-071 + 073):** rate-shock *alone* historically **deflates** VIX (16/20 hot-NFP-DGS2+8bp days had VIX fall/flat; the 4 closest analogs all fell). 6/5 was an **outlier with no clean precedent** in that class. The spike required an amplifier: AI/factor concentration unwind, partially independent of the labor print. Two partially-independent convergences on one tape — not a single root.

That mechanism — *consensus-miss labor shock triggering a factor-concentration unwind* — was in **none** of L2/L3/L4's vocabularies.

---

## 3. Layer-by-layer verdict

| Layer | Pre-6/5 reading | What happened | Verdict |
|-------|-----------------|---------------|---------|
| **L1** | DIET fired 5/20–5/29; base rate says 65% chance of >50%@fwd60 | +40% spike at **td-4**, cleanly inside the base-rate distribution | ✅ **VALIDATED** — real-money layer |
| **L2** | Absorbed-trap (vol-decay entry → expect failure, as Episode-17) | Absorption assumption requires consensus-aligned catalyst; NFP was 2.15× miss → assumption void | ❌ **WRONG MECHANISM** — no consensus-miss carve-out |
| **L3** | (M1:M2 expansion + VIX *falling*) = inactive | Spike flipped it to (M1:M2 expansion + VIX *rising*) — a **previously-unobserved quadrant (Q3)**, N=1 | ⚠️ **NEW QUADRANT, PROVISIONAL** — matrix had no cell for this |
| **L4** | COT to discriminate short-vol crowding | COT correctly showed speculators **de-risked** (covered ~16k into spike, pct3y 17.9→43.6) = event-hedger bid, not crowding. **But the spike happened anyway** via a driver L4 doesn't see | ❌ **ANSWERED THE WRONG QUESTION** — correct about its mechanism, irrelevant to the actual one |

L4 is the sharpest illustration: it was *factually correct* about short-vol crowding (there wasn't any) and that correctness was *useless*, because the move came from somewhere L4 never looks. A mechanism-discriminator that is right about an absent mechanism gives false reassurance.

---

## 4. The meta-lesson — and the Episode-17 ↔ 6/5 inversion

The decisive observation is that **the same L2–L4 filters were *right* on Episode-17 and *wrong* on 6/5.**

| | Episode-17 (4/13) | 6/5 NFP shock |
|---|---|---|
| L1 signature | STRICT fire, very clean | DIET fire (5/20–5/29) |
| L2–L4 read | "absorbed-trap / inactive" | "absorbed-trap / inactive" (until the spike) |
| Actual mechanism | **Was** absorbed-trap (consensus-aligned absorption, GEX suppression) | Consensus-miss + factor unwind — **not** absorbed-trap |
| Correct action | Don't size (L1-only sizing FAILED) | Size (L2–L4 would have vetoed a winner) |
| Filters' verdict | **Right** (saved the trade) | **Wrong** (would have missed +40%) |

Same filters, same reading, opposite correct outcomes — **because the discriminating mechanism differed and the filters can only recognize one.** This is not a calibration error inside any layer. It is a structural property of stacking a base-rate signal with mechanism-specific vetoes:

> **A base-rate layer is robust to mechanism-surprise because it never asks *why*. A mechanism-discriminator layer is only as good as its enumerated mechanism set, and a novel mechanism passes through it silently — voting "inactive/absorbed" with false confidence rather than abstaining.**

The danger is asymmetric. When the mechanism matches (Episode-17), the filters add real value — they overrode L1 and were right. When the mechanism is novel (6/5), the filters don't say "I don't know"; they say "inactive," and a confident wrong veto on a base-rate winner is worse than no filter at all.

---

## 5. Forward discipline — concrete re-weighting

1. **Weight L1 heavier as the sizing anchor.** L1 is the only layer validated under a *novel* mechanism. It is the real-money signal. L2–L4 are veto/context layers, not co-equal confirmers. Sizing should start from L1's base rate and let L2–L4 *reduce* conviction only when their named mechanism is positively identified — never let them silently zero out an L1 fire.

2. **Discriminator layers must be able to abstain.** Add an explicit "**mechanism not recognized**" output to L2/L3/L4. When the live driver isn't the mechanism the layer discriminates, it should return *null* (no signal), not its default "inactive/absorbed" reading. A null defers to L1; a false "inactive" overrides it. This is the single most important fix — it removes the false-confidence veto.

3. **L2 — consensus-miss carve-out (KB-VIO-069 patch).** The absorbed-trap mechanism is valid *only for consensus-aligned catalysts*. Define a surprise threshold (1.5σ? 2σ? — 6/5 was ~2.15×) above which L2 abstains rather than reads "absorbed." Backtest the carve-out against the modern STRICT-failure set. **Open — owed.**

4. **L3 — resolve Q3 (KB-VIO-068).** The (M1:M2 expansion + VIX rising) quadrant is N=1. Run the pre-FOMC-week historical scan to populate it or kill it. Until then it is PROVISIONAL and carries no veto weight. **Open — owed before 6/17.**

5. **L4 — demote from discriminator to descriptive.** COT positioning is *context colour*, not a confirm/veto gate. It answers "is short-vol crowded," which is one of many possible mechanisms. Keep logging it; stop letting it gate entries.

---

## 6. Open follow-ons

- **L2 consensus-miss carve-out backtest** — define σ threshold + test against the 5-failure modern set. (Research-queue 🟡.)
- **L3 Q3 base-rate scan** — pre-FOMC-week M1:M2-expansion-with-VIX-rising cases. Resolve PROVISIONAL → base rate or kill. (Before 6/17.)
- **Right analog universe for the actual mechanism** — VIX +30% single-day-from-low-base with concentrated tech selling (Aug-2024 yen carry, Nov-2018 FANG, Feb-2018, Mar-2020). This is the *missing* discriminator the stack needs: a "factor-concentration-unwind" mechanism layer to sit alongside absorbed-trap and Volmageddon-shape. (Research-queue 🟠 — the highest-value gap this post-mortem exposes.)

---

## 7. Transferable lesson (auto-memory candidate)

**When a signal stack combines a base-rate/population layer with mechanism-specific discriminator layers, the discriminators are only as good as their enumerated mechanism set. A novel mechanism bypasses them silently — they emit their default "inactive" reading with false confidence rather than abstaining, which produces a confident wrong veto on a base-rate winner. Fixes: (1) anchor sizing on the mechanism-agnostic layer; (2) give every discriminator an explicit "mechanism-not-recognized → abstain/null" output so it defers to the base rate instead of overriding it.** Generalizes to any agent stacking a base-rate signal with mechanism-specific filters (CARL labor/inflation regime filters, BROCK credit-stress discriminators, HENRY gamma-regime gates).
