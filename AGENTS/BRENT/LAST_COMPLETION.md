# LAST_COMPLETION — BRENT Apr 17 PM Session (Phase-2 Cleanup + Decoupling Monitor)

**Completed:** 2026-04-17 ~17:15 EDT | **Agent:** BRENT (Claude Code, local) | **Session duration:** ~90 min
**Prior session:** Apr 17 AM (PHASE2_EXECUTION_2026-04-17.md written, outbox signals drafted)

---

STATUS: ✅ COMPLETE for items 6-9 of cleanup queue. Items 1-5 remain open for next session.

## WHAT CHANGED THIS SESSION

### Files Updated
- **`STATUS.md`** — Predictions block synced to `workbook/PREDICTIONS.tsv`. BRT-01 + BRT-14 marked CONFIRMED; BRT-07 timer (Apr 20 OPEC+ watch / Apr 24 7-day price watch) surfaced; BRT-15 noted as awaiting cleaner trigger (STNG +3.4% today ≠ clean announcement). KEY REFERENCES updated to point to new refiner ratio monitor.
- **`LESSONS.md`** — Added #18 "Disambiguate rhetorical from operational announcements before calling Phase 2." Apr 17 Iran FM case as canonical example. 4-point verification gate: Platts Dated Brent convergence, Lloyd's vessel transit counts, P&I resumption, sovereign action. STNG as fastest sanity check.
- **`research/PRODUCT_SIDE_DECOUPLING_THESIS.md`** — Added "6-MONTH BASELINE" section resolving the open "already priced in?" caveat. Finding: all 5 refiner/USO ratios sit at z = -1.5 to -2.1 — deeply compressed, not elevated. Reframes trade from "buy decoupling" to "buy mean reversion of compressed ratio."

### Files Created
- **`scripts/refiner_ratios.py`** — Daily ratio monitor. Pulls 6-mo history for MPC/PSX/VLO/DINO/PBF + USO via yfinance, computes ratio time series, z-score vs 6-mo mean/stdev, 1-day change. Classifies signals:
  - 🟢 REVERTING (z ≤ -1 + 1dΔ ≥ +1%) = entry signal firing
  - 🟡 COMPRESSED (z ≤ -1, not yet reverting)
  - ⚪ NORMAL
  - 🟠 EXHAUSTED (z ≥ +1) = reversion played out, consider exit
  - AGGREGATE 1d Δ across refiners ≥ +1% = decoupling day confirmed
- **`scripts/data/refiner_ratios.tsv`** — Daily snapshot log. Seeded with Apr 17 values.

### Apr 17 Ratio Snapshot (Day 1 reversion baseline)
| Ticker | Ratio | 6-mo μ | z | 1d Δ | Signal |
|---|---|---|---|---|---|
| PSX | 1.348 | 1.795 | -1.99 | +3.82% | 🟢 REVERTING |
| MPC | 1.842 | 2.396 | -1.83 | +2.43% | 🟢 REVERTING |
| DINO | 0.493 | 0.648 | -1.56 | +3.11% | 🟢 REVERTING |
| VLO | 1.927 | 2.339 | -1.80 | +0.33% | 🟡 COMPRESSED (Port Arthur damage — thesis predicted) |
| PBF | 0.320 | 0.430 | -2.06 | -5.47% | 🟡 COMPRESSED (outlier — needs company-specific dig) |

Aggregate 1d Δ: +0.84% (just below +1.0% confirmation threshold).

---

## OPEN THREADS FOR NEXT SESSION

### Blocked on Will (execution decisions from AM session)
1. **PHASE2_EXECUTION_2026-04-17 §1-§3** — USO trim / STNG exit / bear-put-spread build-or-skip. Default is HOLD, but bear-put question at §3 still awaits Will's call.
2. **4 outbox signals marked DRAFT — pending Will validation:**
   - `outbox/2026-04-17_to-CARL_pump-relief-timeline.md`
   - `outbox/2026-04-17_to-HENRY_energy-inflation-reversal.md`
   - `outbox/2026-04-17_to-SAM_japan-lng-import-cost.md`
   - `outbox/2026-04-17_to-HAWK_blockade-vs-strait-assessment.md`

   None sent to HERMES yet.

### Blocked on Data
3. **Dated Brent Apr 15-17 Platts refresh** — THE load-bearing TODO. Last confirmed $132 (Apr 9). If EOD passes with no print, mark STATUS "unavailable" rather than carrying stale $132.
4. **Baker Hughes Apr 17 result** — was due ~1pm ET. Did rig count move off 545?
5. **Incident cadence monitor** — Apr 17 row is baseline (0). Fill at EOD and daily thereafter for Phase-2 truth test.

### Open Questions
6. **Add `refiner_ratios.py` to `scripts/boot.py`?** My recommendation: yes (Phase-2 leading indicator, ~3s cost). Will hasn't answered.
7. **PBF investigation** — -14% outlier on Apr 17 and -5.47% ratio day-1 move is counter-thesis. Needs company-specific dig (earnings? idiosyncratic news?) before including or excluding from any trade.
8. **PRODUCT_SIDE_DECOUPLING trade proposal promotion** — current doc is thesis only. If MPC/PSX/DINO stay 🟢 REVERTING for 3-5 sessions and Phase-2 triggers fire, promote to trade proposal with specific sizing + entry structure.

### Catalyst Watch
- **Weekend:** US-Iran talk-2 possible (no date confirmed as of Apr 17 noon). If signed deal → Monday open gap down, refiner decoupling trade window opens.
- **Mon Apr 20:** OPEC+ 72hr emergency meeting watch closes (BRT-07 timer).
- **Wed Apr 22:** Ceasefire expiry + EIA Weekly Petroleum. Binary day.
- **Fri Apr 24:** Baker Hughes + CFTC COT. BRT-07 7-day price watch closes.

---

## KEY FINDINGS

1. **Paper-physical divergence is THE signal today.** Iran FM "Hormuz open" → paper -12% but physical didn't follow (Dated Brent stale at $132, blockade intact, STNG +3.4%, vessel transits restricted). LESSONS #18 memorializes this pattern.
2. **Refiner/USO ratios are compressed, not elevated.** 6-mo baseline refutes the "already priced in" caveat. The decoupling trade is a mean-reversion setup with ~30% theoretical upside (full reversion) / ~15% (halfway).
3. **VLO as the negative prediction confirmed.** Port Arthur damage = can't capture crack expansion. VLO tracking crude ~1:1 on Apr 17 (0.33% ratio gain vs MPC/PSX/DINO at 2-4%).
4. **PBF is the unexpected outlier.** Ratio down 5.47% on a day refiners as a group reverted. Not in thesis — requires investigation before trade.

---

## POSITIONS AT SESSION CLOSE (Apr 17 ~5PM EDT)

- **USO (2 shares, ~$96 entry):** $115.55 EOD, +20% on position. HOLD per PHASE2_EXECUTION §1 — physical didn't confirm.
- **STNG (2 shares, ~$76 entry):** ~flat. HOLD per PHASE2_EXECUTION §2 — BRT-15 trigger didn't cleanly fire.
- **No new positions.** Bear put spread SKIPPED today (LESSONS #15 + overshoot read).

---

*Session handoff: read this file + STATUS.md + `PHASE2_EXECUTION_2026-04-17.md` at next spawn. Open threads 1-8 above are the resume queue.*
