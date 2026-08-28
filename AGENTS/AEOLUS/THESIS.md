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
| 1 | ENSO state + regional drought/heat → crop stress | **open — REFUSING TO CONFIRM, now on four consecutive prints.** Corn **60% G/E** / soy **61%** (18 states, week ending **8/16**, USDA NASS `prog3326.txt` **primary — first primary read of this metric; the prior four were relays**), from 63/63 (7/26) → 61/63 (8/02) → 61/62 (8/09) → 60/61. A **−1/wk grind, 5 pts above the <55% Yellow band**, but **11 pts (corn) / 7 pts (soy) below last year** (71/68). ⚠️ **Corn is 25% dented** (5-yr avg 24%) and 3% mature — **past pollination and into grain fill, so the yield-determination window is closing and further condition slippage carries less yield consequence than the same slippage in July.** USDM D1-D4 50.38% but concentrated **OK / TX Panhandle, not the corn belt** [8/21] |
| 2 | Crop condition % deteriorates vs normal → yield downgrades | open — deteriorating, but too slowly and too late in phenology to force a downgrade |
| 3 | Grain/softs futures reprice → food-producer margins, fertilizer demand | open |
| 4 | Pass-through to food CPI | open → **CARL** (holds the CPI instrument); MARCO corroborates from the produce side — July CPI fresh F&V **+5.55% YoY**, third straight decline, 2-yr stack +5.86% (so not a base effect). **Two agents, two unrelated instruments, same conclusion: no US row-crop food-CPI cost-push** [MARCO 8/21] |

**Tradeable surface:** ag commodities, food producers, fertilizer. **Shared antecedent:** ENSO state also drives C3 — count the root once.
**Bidirectional flip — RE-SPECIFIED 2026-08-21. The superseded test could not fire in EITHER direction.**

> 🔴 **This is the worst instance of the gate-with-no-instrument class I have found, and it was in my own file for 54 days.** Superseded text, preserved verbatim: *"bear-kill = crop condition >60% G/E + **ENSO-neutral**; bull-confirm = condition <45% with a **strong La Niña**."*
> **Both branches are conditioned on an ENSO state that CPC assigns near-zero probability for this entire forecast horizon** — the regime is a strengthening El Niño with **>90%** odds of very-strong through NH winter 2026-27 and a **69%** chance of an event exceeding every El Niño back to 1950. **Neither "ENSO-neutral" nor "a strong La Niña" can occur inside the window this test is supposed to grade.** So C2 was **unfalsifiable in both directions** — and that is the mechanical reason I have logged it three sessions running as "the honest downgrade candidate that I am also not moving." **I was not being cautious; the test could not return a verdict.** The AND-clause is what hid it: each branch reads sensible, and only the *conjunction* against the live regime is impossible. **Check every conjunctive gate against the CURRENT regime, not against the regime it was written in.**

- *bear-kill* = **corn AND soy ≥60% G/E at the final in-season condition print** (late Sept), **with corn ≥95% dented** — i.e. the crop finishes healthy with the yield window closed. **Currently 1 pt from firing on soy.**
- *bull-confirm* = **either crop <55% G/E** *(the Yellow band)* **before 90% dented** — condition damage while yield is still determinable — **OR** a **≥10% YoY** print in CARL's goods/food-CPI instrument attributable to a named crop shortfall.
- ⚠️ **INSTRUMENT-SCOPE FLAG, stated as a hypothesis with its instrument named, not as a finding.** C2's only live instruments are **US corn and soy**, and a very strong El Niño is generally *favorable* to the US corn belt (cool/wet Midwest summers) while its drought signal lands on **Australian wheat, SE Asian rice/palm, and the Indian monsoon**. **If that holds, C2 is pointed at the crop this regime is least likely to damage, which would explain the refusal-to-confirm as an instrument artifact rather than a benign world.** **I have NOT verified those teleconnections** — the test is ABARES Australian crop reports + FAO rice/palm price indices against the El Niño composite. **Until that is pulled, C2's benign read certifies US row crops ONLY, not global food.** Registered as an open item; do not let the benign score stand for more than it measures.

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
| 1 | Hydrological/storm event (Panama drought, Rhine/Mississippi low water, port storm) | **CONFIRMED — then PEAKED AND BROKE, both inside 8 days.** Kaub daily mean fell to **6.42 cm (8/17)**, ~19 cm below the WSV all-time record `NNW` of 25 cm, and Duisburg-Ruhrort to **128.76 cm (8/17)** vs its 153 cm record; Danube ran 13 consecutive stations below their `LKV` records over 233 km. **Then rain arrived: Kaub 13.9 (8/19) → 34.8 (8/20) → 44.7 (8/21), +38 cm off the low in four days, rising at every one of Maxau/Kaub/Mainz/Duisburg/Emmerich** — driven from upstream, so the lower reaches keep filling for days. Mississippi normal; autumn is its window [8/21] |
| 2 | Chokepoint capacity cut (draft restrictions, transit caps) or route closure | **CONFIRMED on the river leg, still open on Panama** — barge loadings ran ~16% of capacity (~800 t vs 5,100 t) at the trough; Panama unrestricted, transits **38.70/day** (ACP Monthly Ops Summary A-14-2026, Apr-26 data) vs a ≤32 Yellow band [8/21] |
| 3 | Freight rates spike + delivery delays | **CONFIRMED on the river leg** — Rhine spot freight ~**€150/t vs ~€20** normal; **Kiel Institute: Q3 German GDP −0.1/−0.2% (€1.2–2.3B)**. ⚠️ The container-freight leg (Drewry WCI +40% YoY, 6/28) stays **confounded** by tariff/World Cup demand and is NOT climate-attributable [8/21] |
| 4 | Goods-price pass-through → goods CPI | open → **CARL** (repointed 7/31); HENRY (macro velocity). ⚠️ Stage 4 has never confirmed in this channel's life — the pass-through leg is the standing gap, not the peril leg |

**Tradeable surface:** shipping/freight names, goods-CPI-sensitive trades. **Owner handoffs:** goods/food-CPI → **CARL** (repointed from MARCO 2026-07-31 — MARCO holds no CPI transmission instrument after 3 pre-registered nulls; the food leg transferred MARCO→CARL Jan-2026); macro pass-through → HENRY.
**Bidirectional flip — RE-SPECIFIED 2026-08-21. C5 has TWO independent chokepoint systems and the old flip could only grade ONE of them.**

> 🔴 **The defect, stated plainly because it is the same class I fixed on 8/13 one level up.** The superseded flip was *"bear-kill = chokepoints at normal capacity (Panama ≥32 transits) AND freight index normalized for 3+ sessions; bull-confirm = sustained draft restrictions (≤22 transits) with a freight-rate spike"* — **entirely Panama-keyed.** C5 has scored **4 (RED) since 8/03 on European-river evidence**, and *neither* branch of its own written flip test mentions a river. **The channel could not have been killed or confirmed by its own falsifier while it was firing.** On 8/13 I fixed a C5 *upgrade* trigger that named a station and no level; this is the same failure at the *flip* layer, and I did not look one line further down. **A registered gate with no instrument behind it — third instance (ACE, Duisburg, this).**
> ⚠️ **Correcting DAEDALUS PR#4 ACTION 2 on the pointer:** it reported `:80` as "still publishes the RETIRED C5 trigger (superseded 8/13 by Kaub≤25∧Duisburg≤153×10d)." **It does not — the string "Duisburg" appears nowhere in `THESIS.md`.** The retired trigger lived in `CLAUDE.md` and was replaced there. The line was stale in a **different and worse** way than reported, and the finding survives the corrected pointer.

| Leg | *bear-kill* (channel dies) | *bull-confirm* (channel fires) |
|---|---|---|
| **European rivers** (Rhine/Danube — the live leg) | **Kaub daily mean back above `GlW` 78 cm for 10 consecutive days** AND Rhine spot freight back under €40/t | Kaub ≤25 cm **AND** Duisburg-Ruhrort ≤153 cm on 10 consecutive days *(the 8/13 trigger — **FIRED 8/18**, 11-day run 8/09–8/19)* |
| **Panama** (dormant leg) | transits ≥32/day sustained AND no draft restriction | binding draft/transit restriction, ≤22 transits/day, with a freight-rate spike |
| **Freight pass-through** (the never-confirmed leg) | goods-CPI contribution flat 2+ prints with rivers constrained — **this kills the CHANNEL, not the peril** | a measured river-attributable goods-CPI contribution at CARL |

**Grade the legs separately and do NOT average them.** Both chokepoint systems can be benign while the channel still fires on the third leg, and the current state is the reverse: **peril confirmed hard, pass-through never confirmed once.** ⚠️ **Use UNROUNDED daily means** — `water/workbook/SERIES.tsv` rounds to whole cm and a true mean of 25.4 rounds to 25.

## C6 — WATER SCARCITY / ALLOCATION

**Line:** reservoir depletion + snowpack/aquifer decline → Reclamation shortage-tier / compact-guideline **decision** → mandatory delivery cuts + hydropower generation loss → repricing of ag allocations, SW municipal supply, industrial (data-center) siting, and the ag-lending / muni credit that sits on them.
*Promoted Tier-2 → core 2026-08-03 by Will (via WALTER 7/28). The channel that behaves like a policy meeting, not a weather condition — dated instruments, not the word "drought." Discriminator + kill rules in CLAUDE.md §THE CHANNELS.*

| Stage | Mechanism | State (confirmed/open/falsified) |
|---|---|---|
| 1 | Reservoir/snowpack/aquifer decline vs the level that triggers an allocation decision | 🔴 **CONFIRMED AND THROUGH THE THRESHOLD.** **Powell broke its all-time record low 2026-08-15** (3,519.91 vs 3,519.92 ft set 2023-04-13) and has fallen every day since: **3,518.48 ft (8/26)** — **8.48 ft above the ROD's 3,510 ft protection line**, −0.12 ft/day. **Mead broke its post-fill record 8/06** and is **1,039.05 ft (8/26)** — **4.05 ft above the binding Hoover 1,035 ft economic threshold**, −0.065 ft/day. 🔴 **AND THE PROJECTION NOW CROSSES: USBR's August 2026 Most Probable 24-Month Study projects Mead 1,035.56 ft (Nov) and 1,034.74 ft (Dec-2026)** — below the binding line, with **no seasonal turn anywhere in the path**; the July study had Dec at 1,037.31. **Driver, at primary:** Powell's WY2026 release cut **7.48 → 6.00 maf**; April–July unregulated inflow **18% of average** (July alone 9%). [USBR 919/49 + 921/49 + 24Month_08_6.pdf, all primary] |
| 2 | Instrument/decision milestone (shortage-tier declaration, compact/guideline EIS→ROD) | ✅ **RESOLVED — the milestone LANDED.** **ROD signed 2026-08-21** (Sec. Burgum), ~6 weeks ahead of Interior's ~10/1 target and **9 days inside the earliest date I had myself inferred** (L-30). ⚠️ **The superseded text here read *"ROD earliest ~8/30, target ~10/1; 2007 Interim Guidelines expire 12/31/2026"* — all three legs are now spent:** the ROD is signed, and the 12/31 expiry **can no longer be an event because a successor regime exists**. **The clock moves to: 10/01 the 2027-28 Operating Guidelines take effect · the monthly 24-Month Study (now the primary C6 instrument) · whether the Lower Basin implementing agreements get executed.** |
| 3 | Mandatory delivery cuts + hydropower loss reprice ag/municipal/industrial water | 🔴 **NOW SCHEDULED, NOT MODELLED.** The ROD cuts the Lower Basin **1.25 maf in EACH of 2027 and 2028 — AZ 760 kaf · CA 440 · NV 50** (verbatim). ⚠️ **FOUR NUMBERS, FOUR JOBS — do not collapse them:** **1.25 maf** = the binding scheduled cut · **3.6 maf** (AZ 1.96 / CA 0.90 / NV 0.21) = the Preferred Alternative's *modelled maximum*, a tail across futures, real but not a schedule · **"up to 3.0 maf"** = the *operational sideboard* for Hoover critical-infrastructure protection · **1.5 maf** = a distribution-**METHOD** breakpoint, not a volume. 🔑 **And the ROD states the modelled assumptions do NOT bind operations** — *"the assumptions… do not limit future agreements, nor do they preclude or predetermine other legally permissible applications"* — so the matrix was never the referent for an operating-year cut (KB-085). ⚠️ **If the Lower Basin implementing agreements go unexecuted, the ROD's default is apportionment by the Law of the River — i.e. BY PRIORITY**, shielding CA's senior rights and concentrating the cut on AZ's junior CAP. **That clause carries an apparent erratum** (the same provision appears twice with opposite negation) — KB-087, route with the caveat attached. |
| 4 | Pass-through to ag prices / SW muni fiscal / data-center siting / ag-lending + muni credit | open → WATT (hydro), CARL/MARCO (ag & SW municipal), VULCAN (data-center water), REGINALD/CREED (credit) |

**Tradeable surface:** hydro-exposed utilities, SW munis, ag-water names, data-center siting. **Owner handoffs:** hydro gen → WATT; ag/food + SW municipal → CARL/MARCO; data-center water (3rd AI-capex constraint after credit + power) → VULCAN; ag-lending/muni credit → REGINALD/CREED; **FL water stays CORAL** (not imported here).
**Shared antecedent:** El Niño drives C6 (Western hydrology) alongside C2/C3/C5 — but the European-autumn/Rhine teleconnection is weak/contested; do NOT weld C5-Rhine to the same ENSO root as C6-Colorado. Count roots per basin.
**Bidirectional flip — instruments named 2026-08-21** *(the old text said "reservoirs recover above tier thresholds," which stopped being gradeable when the 8/12 Will-ruled re-key moved the binding metric off shortage tiers and onto **Hoover at Mead 1,035 ft**)*:
- *bear-kill* = **Mead sustained ≥1,045 ft for 5 consecutive daily prints** (10 ft of margin, the Yellow band) **AND** the **Most Probable 24-Month Study projecting no breach of 1,035 ft within the succeeding 12 months**.
> 🔴 **RE-SPECIFIED 2026-08-27 — the previous second leg died the moment the ROD was read.** It required *"a signed ROD whose adopted alternative is identified **from the EIS matrix**."* **The ROD adopts NO alternative** — it adopts a *Decision Framework* (a process) *based upon* the Preferred Alternative, and explicitly disclaims the modelled assumptions as limits on operations. **The leg asked the document for a thing it does not contain, so it could never have been graded** — the eighth dead gate found since 8/13, and the second whose defect was a wrong premise rather than a wrong level. Replaced with an instrument that exists and prints monthly.
- *bull-confirm* = **Mead at/below 1,035 ft** OR a **Tier-2/3 shortage declaration** OR **12/31/2026 passing with no successor regime** (governance vacuum — a missed deadline is itself the event).
- ⚠️ **Powell is NOT a flip instrument.** It broke its record on 8/15, which confirms *stage 1* — but Powell and Mead are **one coupled system with a lag** (Powell's releases are what refill Mead), so grading both would count one root twice. **Powell leads; Mead binds.** The leading indicator is **USGS Lees Ferry (09380000) discharge**, which measures the input rather than the stock.
- ⚠️ **Grade the ROD against the alternatives MATRIX, naming which alternative it adopts** — never against a headline triple. Trade-press figures for this EIS understated the Preferred Alternative by **2.0–4.2×** (KB-060 CORRECTED → KB-063).

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
