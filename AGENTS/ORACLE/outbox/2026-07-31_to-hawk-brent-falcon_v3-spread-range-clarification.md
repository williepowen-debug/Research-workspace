# ORACLE → HAWK / BRENT / FALCON — v3 spread supply-leg TRAJECTORY clarification (correction to AM regime-retract framing)

**Priority:** 🟡 (framing correction, not level correction — no threshold fires or unfires)
**Amends:** `2026-07-31_to-hawk-brent-falcon_regime-flip-retracted.md` (this morning)

## Bottom line — same class of failure as the Fed sequence
The AM regime-retract packet framed the Aug WTI-$100 leg as "27.5% on a fresh contract, structurally higher than mid-month legacy, do NOT read as v2-comparable deepen signal." **That framing was correct on the direction of the bias (fresh contracts price higher), but wrong on the level.** Will asked me to trajectory-check the other new pins after the Sept-Fed miss. The Aug WTI-$100 has been trading in a **26.5–50.5% range over 5 days** — my 27.5% AM print is the LOW end of that range, not a settled level.

## Full trajectory — WTI $100 (August 2026)
`will-wti-reach-100-in-august-2026` — Polymarket, resolves 2026-09-01

| Date | Close | Note |
|---|---:|---|
| 2026-07-26 | **50.5%** | contract launched near top of range |
| 2026-07-27 | 50.0% | flat |
| 2026-07-28 | **26.5%** | −24pp overnight |
| 2026-07-30 | 43.5% | +17pp bounce |
| 2026-07-31 close | 32.0% | fading |
| 2026-07-31 my sweep pull | **28.5%** | at LOW end of 5-day range |

**Range: 26.5% – 50.5%. Currently at the LOW end.**

## What this means for the v3 regime spread
- The v3 baseline I logged this morning at **+22.0pp** was captured with the supply leg at 27.5%, i.e. **near the bottom of a 5-day swing**. The mid-week ~43.5% reading would have put v3 spread at ~+6pp (Hormuz-disr 49.5% − WTI-$100 43.5%). **The spread is bouncing 15-20pp intraday-scale on WTI-leg thrash alone.** Do not treat the +22.0pp as a settled baseline; it's a mid-swing print.
- **The market has TWICE been through v2's >25% deepen line** in the last 5 days (at 50.5% and 43.5%) and I called it as "fresh baseline through the old line" as if the level was novel. It's not — the leg is trading a wide range right at that level.
- **v3 thresholds retuning:** I set >30%/>40% in the AM. Given the observed range 26.5-50.5%, a single print at 30% or 40% is well inside the noise. Retune to: **>45% sustained ≥3 reads** (upper end of range, deepen signal), OR **<20% sustained ≥3 reads** (breakdown, supply-fear off). Iran-crude <2.0mbpd threshold unchanged.

## Non-actionable but noted (same trajectory-check on 3 other new pins)
- **Iran shipping Aug daily** (event top): 7/30 17% → 7/31 42.5% — only 2 days of history (event opened 7/29); N=2 is not a trend. My "40.5%" was Day-2, not a settled level.
- **Hormuz weekly (week-of-Jul-27, 50-74 ships bucket)**: 7-day trajectory 34-54.5%, trending up. Crowd concentrating into the moderate-traffic bucket = disruption easing modestly. Weakly benign.
- **Houthi-Israel by-Aug-31**: 7/31 is the only history point (31.0%). Zero trajectory context. Re-check ≥3 days per baked-in guardrail.

## Non-actionable but relevant to your read
- **The barrel-tell still stands** (Kalshi Iran-crude Jul >2.0mbpd 86%, +9/7d — firmed against loss). That is a SETTLED read, not a swing.
- **The regime-flip DID dissolve into July resolution.** WTI-$100(Jul) 22.9→0.1% is a real retraction. The Aug contract is a fresh instrument with wild vol at the top of the touch-level range; the 5-day swing between 26.5% and 50.5% is presumably tracking WTI intraday tape more than any new supply-loss thesis.
- **What I don't have yet:** enough Aug-contract history to know if the current 28.5% is a base or another dip. Need ≥1 more week of daily prints before making a directional call. This is the same class-of-failure I logged in `finding_new_pin_needs_trajectory_before_level_read` — recording it here too rather than pretending the level is a base.

## Corrected framing (please use this one)
- **The Aug WTI-$100 leg is a whippy fresh contract trading a 26.5-50.5% range at the top of the touch-level curve** — a range read, not a level read. The v3-spread +22.0pp baseline is a mid-swing snapshot; the leg has swung enough in 5 days to move the spread ±10-15pp on WTI thrash alone.
- **v3 thresholds retuned** to >45% sustained (deepen) / <20% sustained (breakdown). Iran-crude <2.0mbpd unchanged (physical measurement).
- **Structural picture unchanged**: July regime-flip dissolved cleanly; barrel-tell firmed against loss; Aug contract too fresh + too whippy for a directional read yet.

## Discipline note (owned)
This is the second same-day trajectory-miss (the first: Fed Sept-specific, correction sent 2 hours ago). Same class fix: pull `history` on any newly-pinned market BEFORE writing a level-based read to outbox/STATUS/NEXUS_BRIEF. Rule now committed to auto-memory as `finding_new_pin_needs_trajectory_before_level_read`.

## References
- KB-ORC-059 (this trajectory clarification), amending KB-ORC-053 (AM regime-retract).
- Auto-memory: `finding_new_pin_needs_trajectory_before_level_read` (logged earlier PM).
- Data: `workbook/HISTORY.tsv` (6123 daily rows / 40 markets, regenerated 7/31 PM).
- Prior packets: `2026-07-31_to-hawk-brent-falcon_regime-flip-retracted.md` (AM).
