# AEOLUS — THESIS (per-channel transmission tables)

**Owner:** AEOLUS · The richness layer. STATUS.md carries the live reads + 5-pt handles; this file carries the full `stage → mechanism → state` transmission tables per channel.

**Core thesis:** Climate and weather reprice markets through a small, fixed set of causal channels. The edge is positioning ahead of consensus on tradeable-horizon weather events (Tier 1) while a structural-climate backdrop (Tier 2) tells us which direction the slow drift runs. We win by keeping each channel *live and falsifiable*, not by forecasting weather better than NOAA.

---

## C1 — INSURANCE / REINSURANCE

**Line:** catastrophe losses → reinsurance rate-on-line ↑ → primary insurer solvency stress + coastal insurability collapse → repricing of (re)insurers, P&C carriers, coastal property.

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Active season / major landfall → insured losses spike | **open, benign-leaning** — below-normal forecast (CSU 11/5/2, ACE ~55-60%); pre-peak, light H1 losses [6/28] |
| 2 | Losses exceed cat budgets → reinsurance ROL ↑ at next renewal (Jan/Jun) | **falsified-direction** — ROL DOWN 15-30% YoY at Jun-1 renewal (soft market) [6/28] |
| 3 | Higher ceded cost → primary insurer margin/solvency stress; some exit markets | open — soft market, no stress |
| 4 | Coastal insurability collapse → property values / mortgage availability hit | open → hand FL specifics to CORAL (FL stabilizing [6/28]) |

**Tradeable surface:** reinsurers, P&C insurers, coastal carriers. **Owner handoffs:** FL → CORAL; bank exposure → REGINALD; PE-insurance captive angle → SHADE.
**Bidirectional flip:** *bear-kill* = ACE <90% normal + no major US landfall by Nov 30; *bull-confirm* = ≥150% ACE with a major metro landfall.

## C2 — AGRICULTURE / FOOD

**Line:** drought·heat·flood → crop yield ↓ → grain & softs prices ↑ → food CPI ↑ + fertilizer demand shift.

| Stage | Mechanism | State |
|---|---|---|
| 1 | ENSO state + regional drought/heat → crop stress | **open** — El Niño active; crops healthy (corn 68% / soy 66% G/E); High Plains/Nebraska dry [6/28] |
| 2 | Crop condition % deteriorates vs normal → yield downgrades | open |
| 3 | Grain/softs futures reprice → food-producer margins, fertilizer demand | open |
| 4 | Pass-through to food CPI | open → MARCO (CPI bridge) |

**Tradeable surface:** ag commodities, food producers, fertilizer. **Shared antecedent:** ENSO state also drives C3 — count the root once.
**Bidirectional flip:** *bear-kill* = crop condition >60% G/E + ENSO-neutral; *bull-confirm* = condition <45% with a strong La Niña.

## C3 — ENERGY DEMAND

**Line:** temperature extremes → power/heating demand spike → nat-gas / power price moves.

| Stage | Mechanism | State |
|---|---|---|
| 1 | Heat dome (summer) or polar vortex (winter) → demand spike | **open, building** — heat dome into early-July; El Niño summer [6/28] |
| 2 | CDD/HDD vs normal breaches band → storage draw / price move | open — June CDD −15% (benign); storage +6% cushion [6/28] |
| 3 | Nat-gas / power reprice (Uri-2021 style tail in extreme cases) | open → BRENT (HH $3.16, no stress yet) |

**Tradeable surface:** nat gas, power, utilities. **Owner handoff:** energy pricing → BRENT; geopolitical energy → HAWK.
**Bidirectional flip:** *bear-kill* = CDD/HDD within ±10% normal 4+ sessions; *bull-confirm* = ±30% sustained with low storage.

## C4 — PROPERTY / PHYSICAL ASSETS

**Line:** chronic peril (SLR, wildfire, flood, repeat hurricane) → insurability loss + property-value impairment → mortgage/CRE/muni collateral & credit risk → repricing of peril-exposed regional banks, REITs, munis.
*Promoted Tier-2 → core 2026-06-28. The deepest systemic link — plugs climate into the operation's core credit chain.*

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Peril trend/event (wildfire acreage, flood, SLR, repeat landfall) → physical-risk repricing of a region | **open, benign** — light H1 cat losses ($20B Q1, −26% vs 10-yr avg) [6/28] |
| 2 | Insurers raise rates / non-renew / exit → insurability gap | **open** — CA non-renewals reopening (SB824 moratorium lapsed May'26); FL stabilizing [6/28] |
| 3 | Uninsurable/underinsured property → value impairment + financing harder | open — CA the watch zone |
| 4 | Collateral impairment → mortgage/CRE/muni credit risk → bank/REIT/muni repricing | open → REGINALD/CREED (CORAL if FL) |

**Tradeable surface:** peril-exposed regional banks, REITs, munis. **Owner handoffs:** FL → CORAL; bank exposure → REGINALD; CRE/CMBS → CREED. **Links to C1** (insurability is the shared hinge — count the shared root once).
**Bidirectional flip:** *bear-kill* = reinsurer cat-loss tally (Gallagher Re/Munich Re) <110% of 10-yr avg AND non-renewal rates stable for 2+ quarters; *bull-confirm* = accelerating non-renewals (+40% YoY / carrier exit) with measurable property-value declines in peril zones. *(NOAA NCEI billion-$ DB discontinued 2025 — use reinsurer tallies; LESSON L-05.)*

## C5 — SUPPLY CHAIN / LOGISTICS

**Line:** drought / low-water / storms → chokepoint capacity cut + freight disruption → shipping-rate spike + goods delays → goods-price pass-through → goods CPI.
*Promoted Tier-2 → core 2026-06-28. Most event-driven/tradeable of the structural channels (Panama 2023–24 was a real repricing event).*

| Stage | Mechanism | State |
|---|---|---|
| 1 | Hydrological/storm event (Panama drought, Rhine/Mississippi low water, port storm) | **confirmed (partial)** — Rhine low (Kaub ~106cm), Mississippi driest Jan-May in 132yrs; Panama clear w/ El Niño overhang [6/28] |
| 2 | Chokepoint capacity cut (draft restrictions, transit caps) or route closure | **open** — Panama full draft restored; rivers constraining barge loads [6/28] |
| 3 | Freight rates spike + delivery delays | **confirmed, but confounded** — Drewry WCI +40% YoY (22-mo high); partly tariff/World Cup demand, not pure climate [6/28] |
| 4 | Goods-price pass-through → goods CPI | open → routed to MARCO 6/28; HENRY (macro velocity) |

**Tradeable surface:** shipping/freight names, goods-CPI-sensitive trades. **Owner handoffs:** goods-CPI → MARCO; macro pass-through → HENRY.
**Bidirectional flip:** *bear-kill* = chokepoints at normal capacity (Panama ≥32 transits) AND freight index normalized for 3+ sessions; *bull-confirm* = sustained draft restrictions (≤22 transits) with a freight-rate spike.

---

## TIER-2 BACKDROP (structural, multi-year — slow thesis, tested by Tier-1 events)
- **Insurance retreat** (validates C1 structurally): carriers exiting CA/FL/Gulf markets.
- **Sea-level rise / chronic flood** (feeds C4): coastal property + muni credit.
- **Chronic drought / water stress** (feeds C2, C5): Colorado River, aquifer depletion, river-freight levels.
- **Climate migration** (→ MARCO): population shifts repricing regional housing/labor.

EXPECTED_SIGNALS discipline: if the structural thesis holds, these should appear in Tier-1 events over time — their *absence* is data against the backdrop.

---

## CHANNEL ROSTER NOTE
All five channels (C1–C5) are **core** as of 2026-06-28 (C4/C5 promoted from Tier-2 by Will). There are no Tier-2 expansion channels currently queued. Any *new* channel beyond C5 must be added deliberately — by an explicit promotion decision, never by drift (PAT-018). Candidate future lines if ever needed: tourism/coastal-recreation weather, water-utility stress, labor-productivity heat effects.
