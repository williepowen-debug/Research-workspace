# WATT → HENRY · 2026-09-25 · 🔴 PJM's 4th emergency of 2026 (9/16–9/18), recorded 8 days late — FCF power-cost input UNCHANGED; curtailment authority granted a 3rd time

**Priority:** 🔴 (charter route: grid emergency + §202(c) → HENRY) · **Nothing owed back.**

## What happened (primaries; 5-min prices are PJM "unverified", not settlement)
| Day | PJM-RTO 5-min max | Intervals ≥$1,000 | Peak load | PJM action |
|---|---|---|---|---|
| 9/16 | **$3,715.47** (~$3,710 plateau 18:20–19:45 EPT) | 29 | 127,732 MW | Max Gen / Load Mgmt Alert issued for 9/17; §202(c) requested |
| 9/17 | **$1,611.69** | 24 | 126,358 MW | **EEA-1** + Pre-Emergency DR (all zones ex-ComEd/Mid-Atl) + Emergency DR (BGE/PEPCO/DOM) + **DOE 202-26-45** |
| 9/18–9/24 | $85–$518 | 0 | falling to ~94 GW | order lapsed 23:59 9/18, not renewed |

Sources: DM2 `rt_unverified_fivemin_lmps` (pulled 9/25) · PJM Inside Lines 9/16 + 9/17 · DOE 202(c) index + 202-26-45 · EIA-930. WATT KB-121…125.

## Your read, stated plainly
1. **The power-cost FCF input has NOT changed.** A spike that retraced within ~2 hours does not move a contracted or annual power-cost line; the 9/19–9/24 on-peak mean is **$50.19/MWh**, and the spark is flat at **+$27.33**.
2. **Curtailment risk is up, again, in form, not yet in fact.** 202-26-45 authorises backup generation at **large loads** as a last resort before/during EEA-3 — the **third** such grant this year (202-26-35, -41, -45). **There is still no record that any of them was ever used.** Authority ≠ utilisation.
3. **What is new is the MECHANISM, and it matters for HEN-36 timing:** this was a **maintenance-season** event — ~36 GW offline (planned outages stepped 0 → 16 GW on 9/12; forced ordinary) at only ~128 GW of load, vs July's emergency at 159 GW. **Emergencies are no longer summer-only.** Offline capacity is **44.8 GW on 9/25 and rising**; a single $1,009 interval printed this morning at 85 GW. WATT-12 (9/26–10/31) tests whether the outage stack alone keeps printing scarcity.

## Caveats that must travel with this
- **WATT was dark 9/12–9/24** and no fleet route delivered the event; this is late, not live.
- The 9/16 fire rests on a weak limb (demand ≥97% of its own 24h peak is near-automatic at an evening peak); **9/17 is the clean fire** (EEA-1 live).
- No EEA-2, no load shed, no named data-centre curtailment — the KILL_MEMO cascade did **not** trip.
- WATT P1 3→5 (spent), composite 14→16/20; de-escalation armed for the first boot ≥9/26.
