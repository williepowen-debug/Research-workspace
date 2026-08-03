# AEOLUS — THESIS (per-channel transmission tables)

**Owner:** AEOLUS · The richness layer. STATUS.md carries the live reads + 5-pt handles; this file carries the full `stage → mechanism → state` transmission tables per channel.

> **Sync note (2026-07-09 self-sweep):** this file was 11 days stale (last touched 6/28) — C1 and C3 stage-states below refreshed to match tonight's STATUS.md; C2/C4/C5 stage tables NOT independently re-verified this session (still [6/28] — no material contradicting evidence surfaced, but treat as unrefreshed, not re-confirmed).

**Core thesis:** Climate and weather reprice markets through a small, fixed set of causal channels. The edge is positioning ahead of consensus on tradeable-horizon weather events (Tier 1) while a structural-climate backdrop (Tier 2) tells us which direction the slow drift runs. We win by keeping each channel *live and falsifiable*, not by forecasting weather better than NOAA.

---

## C1 — INSURANCE / REINSURANCE

**Line:** catastrophe losses → reinsurance rate-on-line ↑ → primary insurer solvency stress + coastal insurability collapse → repricing of (re)insurers, P&C carriers, coastal property.

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Active season / major landfall → insured losses spike | **open, benign-leaning, deepened** — CSU cut further to 9/4/1 (from 11/5/2 on 6/10), fewest storms since 2014; zero active storms, none expected 7 days [NHC/CSU 7/9] |
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
| 1 | Heat dome (summer) or polar vortex (winter) → demand spike | **confirmed (partial) — first realized event** — PJM EEA2 grid emergency 7/3 (MD/VA 102-104°F + data-center demand amplifier); did not break 2006 record [PJM/WALTER SIG 7/9] |
| 2 | CDD/HDD vs normal breaches band → storage draw / price move | open — June CDD −15% baseline (benign then); Henry Hub still storage-cushioned (+6% vs 5-yr avg) as of 22 Jun read, not re-verified fresh this session [6/28 price data, 7/9 demand-event overlay] |
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

**Tradeable surface:** shipping/freight names, goods-CPI-sensitive trades. **Owner handoffs:** goods/food-CPI → **CARL** (repointed from MARCO 2026-07-31 — MARCO holds no CPI transmission instrument after 3 pre-registered nulls; the food leg transferred MARCO→CARL Jan-2026); macro pass-through → HENRY.
**Bidirectional flip:** *bear-kill* = chokepoints at normal capacity (Panama ≥32 transits) AND freight index normalized for 3+ sessions; *bull-confirm* = sustained draft restrictions (≤22 transits) with a freight-rate spike.

## C6 — WATER SCARCITY / ALLOCATION

**Line:** reservoir depletion + snowpack/aquifer decline → Reclamation shortage-tier / compact-guideline **decision** → mandatory delivery cuts + hydropower generation loss → repricing of ag allocations, SW municipal supply, industrial (data-center) siting, and the ag-lending / muni credit that sits on them.
*Promoted Tier-2 → core 2026-08-03 by Will (via WALTER 7/28). The channel that behaves like a policy meeting, not a weather condition — dated instruments, not the word "drought." Discriminator + kill rules in CLAUDE.md §THE CHANNELS.*

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Reservoir/snowpack/aquifer decline vs the level that triggers an allocation decision | **confirmed** — Lake Powell 3,522 ft / 23% full (~2-3 ft above the Apr-2023 all-time low 3,519.92 ft; lowest-ever *summer* level, on track to break the record Aug/Sep); Lake Mead 1,041 ft / 27%, Tier-1 shortage; WY2026 inflow 36% of avg [USBR 7/31-8/2] |
| 2 | Instrument/decision milestone (shortage-tier declaration, compact/guideline EIS→ROD) | **confirmed live** — Post-2026 Colorado River guidelines: **Final EIS published 7/31/2026**; ROD earliest ~8/30, target ~10/1; 2007 Interim Guidelines expire 12/31/2026 (`CALENDAR.md`) |
| 3 | Mandatory delivery cuts + hydropower loss reprice ag/municipal/industrial water | open — preferred alternative allows Lower-Basin cuts up to 3.0 MAF, Arizona-weighted; Glen Canyon ~32 ft above min power pool |
| 4 | Pass-through to ag prices / SW muni fiscal / data-center siting / ag-lending + muni credit | open → WATT (hydro), CARL/MARCO (ag & SW municipal), VULCAN (data-center water), REGINALD/CREED (credit) |

**Tradeable surface:** hydro-exposed utilities, SW munis, ag-water names, data-center siting. **Owner handoffs:** hydro gen → WATT; ag/food + SW municipal → CARL/MARCO; data-center water (3rd AI-capex constraint after credit + power) → VULCAN; ag-lending/muni credit → REGINALD/CREED; **FL water stays CORAL** (not imported here).
**Shared antecedent:** El Niño drives C6 (Western hydrology) alongside C2/C3/C5 — but the European-autumn/Rhine teleconnection is weak/contested; do NOT weld C5-Rhine to the same ENSO root as C6-Colorado. Count roots per basin.
**Bidirectional flip:** *bear-kill* = reservoirs recover above tier thresholds AND a signed ROD resolves the guideline uncertainty benignly; *bull-confirm* = a Tier-2/3 shortage declaration OR the 12/31 expiry passing with no successor regime (governance vacuum).

---

## TIER-2 BACKDROP (structural, multi-year — slow thesis, tested by Tier-1 events)
- **Insurance retreat** (validates C1 structurally): carriers exiting CA/FL/Gulf markets.
- **Sea-level rise / chronic flood** (feeds C4): coastal property + muni credit.
- **Aquifer depletion** (feeds C6, and C2): Ogallala/High Plains — decades-horizon, carried as a watch-note with the horizon stated; not a score-mover until it reaches an acreage/cost/water-rights-pricing decision. *(Chronic drought / water stress / Colorado River graduated to core C6 2026-08-03.)*
- **Climate migration** (→ MARCO): population shifts repricing regional housing/labor.

EXPECTED_SIGNALS discipline: if the structural thesis holds, these should appear in Tier-1 events over time — their *absence* is data against the backdrop.

---

## CHANNEL ROSTER NOTE
Six channels **core**: C1–C3 (2026-06-28), C4/C5 promoted from Tier-2 by Will 2026-06-28, **C6 water scarcity/allocation promoted from Tier-2 by Will 2026-08-03** (assigned via WALTER 7/28; cleared the #1-guard empty-channel test because a standing live read exists — Powell/Mead vs shortage tier + the Colorado River guideline calendar). Any *new* channel beyond C6 must be added deliberately — by an explicit promotion decision, never by drift (PAT-018). Candidate future lines if ever needed: tourism/coastal-recreation weather, labor-productivity heat effects. **C6 standalone-agent promotion trigger** (WALTER): sustained ~6 weeks OR the AI-water join producing its own dispatches → DAEDALUS maturity review, Will-gated.
