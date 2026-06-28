# AEOLUS — THESIS (per-channel transmission tables)

**Owner:** AEOLUS · The richness layer. STATUS.md carries the live reads + 5-pt handles; this file carries the full `stage → mechanism → state` transmission tables per channel.

**Core thesis:** Climate and weather reprice markets through a small, fixed set of causal channels. The edge is positioning ahead of consensus on tradeable-horizon weather events (Tier 1) while a structural-climate backdrop (Tier 2) tells us which direction the slow drift runs. We win by keeping each channel *live and falsifiable*, not by forecasting weather better than NOAA.

---

## C1 — INSURANCE / REINSURANCE

**Line:** catastrophe losses → reinsurance rate-on-line ↑ → primary insurer solvency stress + coastal insurability collapse → repricing of (re)insurers, P&C carriers, coastal property.

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Active season / major landfall → insured losses spike | open — unseeded |
| 2 | Losses exceed cat budgets → reinsurance ROL ↑ at next renewal (Jan/Jun) | open |
| 3 | Higher ceded cost → primary insurer margin/solvency stress; some exit markets | open |
| 4 | Coastal insurability collapse → property values / mortgage availability hit | open → hand FL specifics to CORAL |

**Tradeable surface:** reinsurers, P&C insurers, coastal carriers. **Owner handoffs:** FL → CORAL; bank exposure → REGINALD; PE-insurance captive angle → SHADE.
**Bidirectional flip:** *bear-kill* = ACE <90% normal + no major US landfall by Nov 30; *bull-confirm* = ≥150% ACE with a major metro landfall.

## C2 — AGRICULTURE / FOOD

**Line:** drought·heat·flood → crop yield ↓ → grain & softs prices ↑ → food CPI ↑ + fertilizer demand shift.

| Stage | Mechanism | State |
|---|---|---|
| 1 | ENSO state + regional drought/heat → crop stress | open — establish ENSO first |
| 2 | Crop condition % deteriorates vs normal → yield downgrades | open |
| 3 | Grain/softs futures reprice → food-producer margins, fertilizer demand | open |
| 4 | Pass-through to food CPI | open → MARCO (CPI bridge) |

**Tradeable surface:** ag commodities, food producers, fertilizer. **Shared antecedent:** ENSO state also drives C3 — count the root once.
**Bidirectional flip:** *bear-kill* = crop condition >60% G/E + ENSO-neutral; *bull-confirm* = condition <45% with a strong La Niña.

## C3 — ENERGY DEMAND

**Line:** temperature extremes → power/heating demand spike → nat-gas / power price moves.

| Stage | Mechanism | State |
|---|---|---|
| 1 | Heat dome (summer) or polar vortex (winter) → demand spike | open |
| 2 | CDD/HDD vs normal breaches band → storage draw / price move | open |
| 3 | Nat-gas / power reprice (Uri-2021 style tail in extreme cases) | open → BRENT |

**Tradeable surface:** nat gas, power, utilities. **Owner handoff:** energy pricing → BRENT; geopolitical energy → HAWK.
**Bidirectional flip:** *bear-kill* = CDD/HDD within ±10% normal 4+ sessions; *bull-confirm* = ±30% sustained with low storage.

---

## TIER-2 BACKDROP (structural, multi-year — slow thesis, tested by Tier-1 events)
- **Insurance retreat** (validates C1 structurally): carriers exiting CA/FL/Gulf markets.
- **Sea-level rise / chronic flood** (feeds C4): coastal property + muni credit.
- **Chronic drought / water stress** (feeds C2, C5): Colorado River, aquifer depletion, river-freight levels.
- **Climate migration** (→ MARCO): population shifts repricing regional housing/labor.

EXPECTED_SIGNALS discipline: if the structural thesis holds, these should appear in Tier-1 events over time — their *absence* is data against the backdrop.

---

## TIER-2 EXPANSION CHANNELS (specced, not yet built)
- **C4 Property / physical assets:** chronic peril → property values → mortgage/CRE/muni risk → CORAL/REGINALD/CREED.
- **C5 Supply chain / logistics:** drought (Panama Canal), low rivers (Rhine/Mississippi), storms → freight disruption → goods inflation → MARCO.

Promote C4/C5 to core only when a core channel goes durably dormant OR a Tier-2 line shows a live tradeable read (deliberate promotion — never drift).
