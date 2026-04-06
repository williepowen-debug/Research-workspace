# LAST_COMPLETION — BRENT Demand Destruction Infrastructure + Gap Closure

**Completed:** 2026-04-06 ~02:00 UTC | **Agent:** BRENT (via Will/Telegram) | **Task:** Build demand destruction monitoring infrastructure, hoarding research, close data gaps, set up automated agents

---

STATUS: ✅ COMPLETE

## WHAT CHANGED

### New Files Created
- `demand_destruction/TRACKER.md` — **Centerpiece.** Live weekly dashboard for all demand destruction indicators. Path B trigger status (0/3), leading indicators dashboard (Tier 1/2/3), Hamilton NOPI scorecard, weekly data log, monitoring schedule, cross-agent routing table.
- `demand_destruction/HOARDING.md` — Deep research on oil hoarding. Who's hoarding (sovereign/commercial/wholesale), $32 spread decomposition (38-50% scarcity, 25-38% hoarding, 16-25% insurance, 6-13% quality), EIA data distortion diagnostics, Phase 2 unwind amplifier (300-600M bbl overhang = 3-8M bpd effective supply addition), academic references.
- `demand_destruction/data/EUCRBRDT_vs_CO1_20260402.jpg` — Bloomberg chart: Dated Brent vs futures, 5-year. Shows unprecedented $32 divergence.

### Files Moved (to demand_destruction/)
- `research/DEMAND_DESTRUCTION_ANALOGS.md` → `demand_destruction/ANALOGS.md`
- `domain/sources/HAMILTON_DEMAND_DESTRUCTION_FRAMEWORK.md` → `demand_destruction/HAMILTON.md`
- `research/PHASE2_TRANSITION_INDICATORS_MAR8.md` → `demand_destruction/TRANSITION_MATRIX.md`
- `research/PHASE2_MATRIX_REVIEW.md` → `demand_destruction/MATRIX_REVIEW.md`

### Files Updated
- `STATUS.md` — KEY REFERENCES section updated to point to new demand_destruction/ locations
- `demand_destruction/HAMILTON.md` — NOPI recalculated: 40.1 at $112 WTI (was 47 at projected $120). GDP drag -2.5 to -4.2pp. Between 1990 Gulf War and 1979 Iran Revolution.
- `demand_destruction/TRACKER.md` — Populated with Phase 1 gap closure data: CFTC COT (backlog cleared, NYMEX net long 73.3K Mar 31), EIA crude inventories (424.4M bbl, -19M draw), Cushing (27.5M bbl), OPEC+ Apr 5 outcome (symbolic only), airline capacity cuts (CONFIRMED FIRING: UAL -5%, DAL -4%, AAL -6%, ULCCs -10%)
- `demand_destruction/MATRIX_REVIEW.md` — Source reference updated to new path

### Automated Agents Created (3 scheduled triggers)
1. **BRENT Monday Market Open** (Mon 9:45 AM ET) — M1-M3 spread, stock prices, DXY, diplomatic news
2. **BRENT Wednesday EIA** (Wed 11:00 AM ET) — Full EIA WPSR data pull, gasoline demand YoY, alerts
3. **BRENT Friday Close** (Fri 2:00 PM ET) — CFTC COT + direction, Baker Hughes rigs, airline capacity news

All write to demand_destruction/data/ and update TRACKER.md weekly data log. Managed at https://claude.ai/code/scheduled

## KEY FINDINGS

1. **Airline capacity cuts CONFIRMED** — demand destruction Tier 2 leading indicator is NOW ACTIVE. United -5%, Delta -4%, American -6%, ULCCs -10%, SAS 1,000+ flights cancelled, 7% of global flights cancelled on one day in March. Per framework, these lead EIA gasoline data by 4-8 weeks → expect gasoline YoY to turn negative by May-June.
2. **NOPI = 40.1** (recalculated at $112 WTI) — solidly recessionary but lower than original 47 projection. GDP drag -2.5 to -4.2pp.
3. **OPEC+ Apr 5** — symbolic "paper" increase only. Can't deliver real barrels. Next meeting June 7.
4. **CFTC backlog cleared** — have Mar 31 data (NYMEX net long 73.3K). Need Friday agent to establish direction.
5. **Crude inventories drawing** — 443.1M → 424.4M bbl (~19M draw), now 4% below 5-year avg.
6. **Hoarding research** — 300-600M bbl overhang will amplify Phase 2 crash. Retracement 50-75% of spike within 3 months of resolution. China buys crashes not spikes.

## GAPS REMAINING

### Handled by Automated Agents
- EIA gasoline demand YoY (Wednesday agent, Apr 8)
- CFTC COT direction (Friday agent, Apr 10)
- M1-M3 spread live (Monday agent, Apr 7)
- LNG/EOG/USO prices (Monday agent)
- DXY level + direction (Monday agent)
- Baker Hughes rig count (Friday agent)

### Manual (when convenient)
- STNG position status — ask PROME to confirm
- SK/Japan refiner run cut status — web search or SAM signal
- Corpus Christi water shortage / refinery capacity research
- Initial claims trend (Thursday, not yet automated)

## WILL_NEEDS

- **Apr 6 deadline outcome** (tonight 8PM ET) — binary catalyst. If escalation → Brent $130+ plausible, add USO on first pullback. If surprise deal → Phase 2 exit protocol fires immediately.
- USO sizing decision deferred until after Apr 6 resolves (per BRENT recommendation)
- Cheniere Q1 earnings ~Apr 30 or May 7 — options expiry should be May 16+
