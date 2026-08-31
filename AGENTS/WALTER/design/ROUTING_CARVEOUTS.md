# WALTER ROUTING — PER-AGENT CARVE-OUTS v0.31

**Version:** v0.31 — ⚠️ **MUST MATCH `ROUTING_TABLE.md` EXACTLY. These two files are ONE spec split across two paths for read-cap reasons, so they carry ONE version and move in LOCKSTEP: edit either, bump BOTH.** Enforced by `tools/version_drift_check.py` (companion check, added 2026-08-30 on Codex finding 3). **Why it matters:** these sections are routing LAW; before the companion check a carve-out edit could change who receives a signal with no version bump anywhere — the parent's version would still read v0.31 and every drift check would pass.

> **Split out of `ROUTING_TABLE.md` 2026-08-30** (@ sha256 `8c4d77417a26`, 121,557 B = 224% of the read cap). **VERBATIM — nothing summarised.**
>
> 🔴 **READ AT DISPATCH, not at boot.** When a signal falls in an agent's lane, read that agent's section here before setting the recipient lines. These are ROUTING LAW: they are what puts CORAL on a Florida signal, CREED on national CRE, TERRY on a T-1.
>
> **The parent table carries a named inventory of every section below**, so a reader cannot be unaware of what is here. Ownership, precedence and the domain table itself stay in [`ROUTING_TABLE.md`](ROUTING_TABLE.md).

### Residential-housing stress exception (Apr 20 2026)

Geographically-narrow residential signals — HOA dysfunction, builder-defect litigation, insurance withdrawals with regional clustering, forced-sale price-discovery clusters, local-market residential CRE correlation — route **REGINALD** action with **CARL** info, NOT the reverse.

**Why:** residential → regional-bank-credit transmission is REGINALD's chain (warehouse lines, HELOC origination, forced-sale price discovery, local-market CRE correlation, direct WAL/ZION/OZK earnings-week coverage). CARL is the macro-national consumer-credit primary (NFP, claims, CPI, household-debt aggregate); CARL is NOT the geographically-narrow primary.

**Filed:** Apr 20 2026 after Will corrected a default-CARL routing I'd drafted for NV HOA SIG-W-20260420-005. Routing test case: Del Webb/Pulte Nevada ~80-90 homes + NV AB125 + regional insurance withdrawals + Silver State Bank 2008 precedent = REGINALD, not CARL.

**How to apply at intake:** when a residential signal arrives, ask "is this geographically-narrow OR macro-national?" If the signal names a state/metro/builder/HOA, route REGINALD action + CARL info. If it's a national aggregate (national mortgage delinquency print, national housing starts, Fed Z.1 household leverage), route CARL action per CONSUMER_CREDIT default. **(Florida carve — v0.11, Jun 19 2026: if the geo-narrow residential signal is Florida-specific, route CORAL action instead of REGINALD — see the Florida-specific routing sub-section below. Non-FL geo-narrow residential is unchanged: REGINALD action / CARL info.)** **⚠️ SUPERSEDED for asset-market housing signals by the v0.17 HOMER carve (Jul 12 2026, sub-section below): housing asset-market/credit-structure signals — national OR geo-narrow non-FL — now route HOMER action / REGINALD info / CARL info. This Apr-20 exception's REGINALD-action default survives only for the bank-side residential-CREDIT signals it originally targeted (warehouse lines, HELOC origination, regional-bank residential exposure). FL-specific stays CORAL per v0.11.**

### Florida-specific routing — CORAL (Jun 19 2026)

**CORAL** was promoted from a REGINALD sub-agent to a **top-level Florida peer agent** on 2026-06-19. It owns Florida comprehensively — real estate (condo + single-family + CRE), FL insurance market, FL regional banks, migration & demographics, tourism & snowbird economy, state fiscal & property-tax policy, labor & construction, and the coastal/climate layer.

**Rule:** any **Florida-specific** signal routes **CORAL action**, with:
- **REGINALD info** — CORAL produces FL bank-level loss estimates; REGINALD integrates them into the multi-channel convergence matrix (the FL→regional-bank-credit handoff).
- **CARL info** — when the signal carries a consumer-stress vector (assessments, wealth-effect, mobility-lock).
- **MARCO info** — when the signal touches FL migration / tourism / snowbird flows (CORAL and MARCO **co-own** the FL migration/tourism surface; reconcile shared metrics — condo inventory, airport pax, migration, snowbird-$ — to one number; divergence on the same fact is the only thing to avoid).
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules when they fire.

**How to apply at intake:** ask "is this signal Florida-specific?" (names FL / a FL metro — Miami-Dade, Broward, Tampa, Orlando, Cape Coral, Punta Gorda, Fort Myers, Naples, Lakeland, Jacksonville — or a FL entity / FL-chartered bank / FL insurance market / FL condo-reserve-law mechanics). If yes → **CORAL action.** If it's geo-narrow residential but **non-Florida** (e.g., Phoenix BTR, Nevada HOA) → REGINALD action per the Residential-housing exception above (CORAL is Florida-only). If it's a national aggregate → CARL action per CONSUMER_CREDIT.

**Relationship to the Residential-housing exception (Apr 20):** that exception routes ALL geo-narrow residential → REGINALD action. This Florida carve **supersedes it for Florida only** — FL-specific signals go to CORAL (who then hands the bank-loss read to REGINALD). The exception still governs non-FL geo-narrow residential.

**Why:** CORAL is now the FL single-source-of-truth; its edge is the geographic-convergence read (insurance + condos + SF + CRE + migration + tourism + property-tax + climate all hitting the same FL metros and the same FL bank books at once). Routing FL signals to REGINALD-action would defeat the promotion; REGINALD stays on info to integrate the bank-collateral leg.

**Filed:** Jun 19 2026. WALTER routed SIG-W-20260619-002 (FL negative-equity by vintage) CORAL-action at dispatch ahead of this formal row; Will approved the row 2026-06-19 (Telegram).

### National CRE / CMBS market-stress routing — CREED (Jun 22 2026)

**CREED** is the **national CRE / CMBS market-stress specialist** (revived 2026-06-21). It owns the CRE-market side of the chain *before* stress transmits into bank books: CMBS delinquency & special-servicing by property type, the maturity-wall / extend-and-pretend exhaustion, CRE fund / shadow-NAV / forced-sale risk, public REIT equity tape as a CRE-recognition/valuation signal, and **non-Florida** multifamily stress.

**Rule:** national CRE / CMBS market-stress signals route **CREED action**, with:
- **REGINALD info** — the CRE-market → bank-book handoff. CREED's edge is identifying when maturity-default / special-servicing stress crosses into bank provisions, reserve coverage, forced sales, or funding pressure; REGINALD integrates that into the bank-credit convergence matrix.
- **BROCK info** — when the signal touches securitized-credit / CRE-debt-fund / private-credit overlap.
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules when they fire.

**How to apply at intake (CREED vs REGINALD vs CORAL boundary):**
- **CRE *market structure*** — CMBS DQ / special-servicing prints, CMBS issuance, maturity-wall data, CRE transaction volume / cap-rate / price-discovery, CRE-fund redemptions / shadow-NAV, public REIT CRE tape, non-FL multifamily stress → **CREED action.**
- **Bank CRE *exposure*** — a bank's CRE loan book, hidden-CRE relabeling (MI3 / RCON2746), NDFI, bank capital rules, bank provisions / reserves on CRE → **REGINALD action** per the `BANK_CRE` row (unchanged).
- **Florida-specific CRE** → **CORAL action** (FL is CORAL's; CREED is national / non-FL) per the Florida carve above.

**Relationship to the `BANK_CRE` row:** that row (REGINALD action / BROCK backup) still governs the bank-exposure side. This carve splits the *market-structure* side out to CREED — the same specialist-carve pattern as the CORAL promotion (CORAL carved FL out of REGINALD; CREED carves national CRE/CMBS market-stress out of REGINALD). No FORMAT_SPEC domain-vocab change.

**Why:** CMBS is recognizing CRE stress faster than banks are; CREED's edge is reading that market-side recognition and flagging the crossover point into bank books. Routing CRE/CMBS market-stress to REGINALD-action would bury the market-side read inside the bank lane; REGINALD stays on info to own the bank-transmission leg.

**Filed:** Jun 22 2026 (Telegram) — Will approved "Yes CREED should be routed to." CREED revived + registered 2026-06-21.

### Trade-construction info routing — TERRY (Jun 22 2026) — ⛔ **SUPERSEDED 2026-08-07**

> ⛔ **SUPERSEDED 2026-08-07 by "Trade-construction ACTION routing — TERRY (Aug 7 2026)" immediately below** (Will-confirmed in-session; ruled by TERRY in `FORUM/2026-08-07_system-review/06_proposals/07_TERRY_routing-disposition.md`; canonical `design/BOARD_CONSUMPTION_SPEC.md` §3.5.5). **The `info:` line to TERRY is KILLED — do not add TERRY to `info:` on any signal for any reason.** The four triggers below (positioning extremes / reversion setups / vol-dealer positioning / threshold-proximity) are **no longer routing rules**; they qualify only where they independently satisfy T-1, T-2 or T-3 in the successor section. Retained unedited for provenance — the Jun-22 reasoning is why the lane existed and is load-bearing for reading the successor.

**TERRY** is the tactical **trade-construction** desk (Tier-2 CC; "is this a good trade — timed, structured, sized, survivable?"). It does NOT own thesis or domain truth and **never executes** — it turns a thesis into a survivable trade plan (entry / invalidation / sizing / expiry / roll). So TERRY is an **info-only** recipient: it never appears on a signal's `action` line, only `info`.

**Rule:** add **TERRY info** to a signal when its substance is **positioning / timing / reversion** in character — i.e., it bears on the *expression* of a trade, not the thesis. Triggers (any):
- **Positioning extremes** — COT / net-spec positioning (e.g., oil specs near-record-short), record fund flows, crowding (levered-ETF AUM extremes).
- **Reversion / technical setups** — overbought/oversold (RSI), momentum divergences, mean-reversion on a tracked name/index.
- **Vol / dealer positioning** — gamma flips, dealer-positioning extremes, vol-regime shifts that change optimal expiry/structure.
- **Threshold-proximity** — a metric within ~5% of a RED-FT / REG-T / Boundary trigger, where entry/exit *timing* on a live or candidate book trade is the question.

**Scope guard (narrow by default — Will "only timely trading information," 2026-06-22):** TERRY-info fires only when the signal plausibly informs a **live or candidate book trade's** timing/structure/sizing — NOT every macro positioning datapoint. When in doubt, omit. Conservative start, to be widened if TERRY asks for more flow. TERRY is info-only and Will-engaged on consumption (Will opens TERRY to construct/veto a trade), so over-cc'ing just adds noise to an on-demand queue.

**How to apply at intake:** after routing the signal to its domain action/info recipients, ask "does this change the *timing, structure, or sizing* of a trade we hold or are considering?" If yes → add TERRY to info. (Same tag-driven info-cc mechanism as the RED cluster_mediating auto-cc — different consumer.)

**Why:** TERRY's edge is "good thesis, bad trade is still a bad trade" — it needs the positioning/timing/reversion picture to time entries, pick expiries, and size against invalidation. Those signals route to thesis owners (HENRY/VIOLET/domain) but not to the trade-construction desk; this closes that gap on the info line without touching any action routing.

**Filed:** Jun 22 2026 (Telegram) — Will lean "only information specific to timely trading information… all the shorts on oil… reversion like semiconductor RSI." Shipped as the conservative/narrow version; widen on Will/TERRY request. TERRY = Tier-2 CC trade-construction, registered 2026-06-21.

### 🔴 Trade-construction ACTION routing — TERRY (Aug 7 2026) — supersedes the Jun-22 info lane above

> 🔴 **FALSIFIER FIRED — DELIVERY REVERTED 2026-08-26 (SPEC v0.21 §3.5.5, mechanical execution of the ratified remedy): TERRY is RED-class EXEMPT. No `inbox/WALTER/` handoffs, no `delivery_log` rows, on ANY signal; BOARD + `route_log` still written. T-1/T-2/T-3 below are RETIRED as delivery gates and retained as the record of the rule that ran 8/07–8/26. A TERRY-instrument-touching correction that is time-critical goes to PROME for orchestration routing, not to a TERRY inbox.**

**Canonical:** `design/BOARD_CONSUMPTION_SPEC.md` **§3.5.5** — that section owns the semantics, the override accounting and the falsifier. This row is the operative routing instruction; on any disagreement §3.5.5 wins.

**The two halves are one rule. Both, or neither.**

**① There is NO `info:` delivery to TERRY. Ever.** Not on positioning colour, not on war-theater signals, not on "relevant to sizing." If TERRY does not qualify for `action:` below, TERRY is not on the signal.

**② `action: TERRY` if and only if one of three tests is met:**

| Test | Qualifies when the signal… |
|---|---|
| **T-1 NAMED INSTRUMENT** | names, or bears directly on the level of, a registered TERRY instrument — a live/staged `setup_id`, its underlying ticker, a card gate / kill line / invalidation / harvest level, a numbered `RISK_RULES` rule, or a load-bearing `SIGNALS.tsv` row |
| **T-2 CORRECTION OR RETRACTION** | corrects, retracts or retires **a number or level any TERRY surface cites** — whether or not it names TERRY. *(The class TERRY cannot self-source: `consumer_check.py` only scans fleet publisher→consumer, and WALTER relays third-party numbers no fleet agent published.)* |
| **T-3 CLOSED-MARKET EVENT** | is a non-price event landing **while the market is closed**, on an underlying TERRY holds or has staged. *(A fire-time pull cannot recover a weekend event — by the time TERRY pulls, the gap has happened.)* |

**Apply §3.5.3's wording, not a generous reading: fires / falsifies / re-points — never "is relevant to."** Explicitly excluded: general positioning colour · theater/war signals with no TERRY instrument attached (`IRAN_HORMUZ` was 53% of the old lane) · anything connected only through sizing. **An anti-action signal** (one whose purpose is to *stop* a trade) fails all three and is an accepted, priced miss at ~3% — it does **not** get rescued by widening T-2; at n≥3 in 30 days it earns its own numbered test.

**Override:** WALTER may send outside T-1/T-2/T-3 on judgement. Since there is no `info:` lane, **any non-qualifying send IS an override** and is recorded by prefixing the `delivery_log` `notes` cell with **`TERRY-OVERRIDE`** + a one-line reason. **Counted per the §3.5.5 override clause, ratified by TERRY 2026-08-07: ratio ≤10%, denominator trailing 90 days, activation n≥10 dispatches in the window, n=1 report to TERRY mandatory. A breach ⇒ a MANDATORY READ OF THE OVERRIDE LOG — never an automatic widening of T-1/T-2/T-3** (the denominator is WALTER's own volume, so a quiet quarter can trip the rule by its own success; a breach says *look*, never *what*). **90d, not 30d: at ~3 dispatches per 30 days the n≥10 activation is unreachable by construction** — a no-verdict band that never ends. **⚠️ The revert falsifier below deliberately runs on a DIFFERENT clock (30d / n=1 / no denominator) and must NOT be harmonised with this one** — it is an event test, not a rate test.

**Falsifier that governs the whole rule:** if the S1 owner-unconsumed line ever names TERRY once for an `action:` item unconsumed >72h, **revert to the RED-class exemption — do not tune the tests.**

**Filed:** Aug 7 2026 — **Will CONFIRMED in-session** on TERRY's own disposition (`FORUM/2026-08-07_system-review/06_proposals/07_TERRY_routing-disposition.md`, adopting option (c)). Evidence bar: TERRY's ledgers show **four decision-changing consumptions of `info`-labelled pushes in 14 days**, including a no-fire on a *met* trigger (`TRY-FIRE-001`, 41 minutes from consumption to logged refusal) and a grading guard that executed 8/7 — against a routing table that recorded the desk as consuming nothing. **Not** the RED exemption, because RED's whole-`INDEX` BOARD diff regenerates the interrupt and TERRY has no BOARD differ: *TERRY can re-pull every price, and cannot re-pull a retraction.* **Anti-ratchet:** 32 deliveries/quarter → ~9–11, net **−21 to −23**, no new file/script/register. **Scope: TERRY only** — the general ownership rule remains an unratified proposal (P2) and must not be inferred from this row.

### Climate / hurricane-season / ENSO routing — CORAL (Jun 26 2026)

**CORAL** owns the **coastal/climate pillar** (COVERAGE.md pillar #10 — hurricane season, sargassum, flood/SLR → coastal RE + insurance) and the **FL insurance market** (pillar #5). The Florida carve above already routes FL-*named* climate signals to CORAL; this sub-section closes the gap for **basin-wide / not-FL-on-its-face** climate items that still transmit to Florida — so they route to CORAL instead of being killed as "off-axis climate."

**Rule:** climate signals with a **Florida transmission channel** route **CORAL action**, with:
- **MARCO info** — when the channel is tourism / snowbird flows (a storm-season or sargassum disruption to FL tourism; CORAL and MARCO co-own that surface — reconcile to one number).
- **REGINALD info** — when it transmits through FL insurance (Citizens assessments / reinsurance / carrier solvency) into FL bank collateral or state fiscal.
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules.

**What routes to CORAL (FL-transmitting climate):**
- **ENSO state** — El Niño / La Niña / ONI prints + forecasts (NOAA CPC, ECMWF, CSU). They set the Atlantic hurricane-activity prior, which prices directly into FL insurance + coastal RE.
- **Atlantic hurricane-season outlooks** — NOAA / CSU / TSR named-storm / ACE forecasts; in-season named-storm tracks/intensity threatening FL landfall.
- **Sargassum** belt size/landfall (tourism + coastal-RE), **FL flood / sea-level-rise / FEMA-NFIP** repricing, FL-coastal climate-driven insurance cost.

**What still KILLS (Relevance gate — no near-term FL insurance/RE/tourism/fiscal transmission):** pure climate-science with no FL-economic channel — global temperature anomalies, paleoclimate, geomagnetic/solar, IPCC structural-ocean findings, non-Atlantic-basin activity, generic "climate risk" macro takes. (These are the off-axis-climate kills — e.g., the 2026-06-26 geomagnetic-dipole / global-temp-anomaly / Atlantic-warming-hole items.) **⚠️ EXEMPLAR AMENDED v0.22 (Jul 28): the *AI-data-center-water* item was struck from this list. It was written 2026-06-26, when the only climate lane was FL-transmitting and a non-FL water story genuinely had no home — but AEOLUS was built 6/28 and now owns macro climate→economy INCLUDING water scarcity (see the US-water carve below). Routing data-centre water to a KILL exemplar would kill the exact class the fleet decided on 7/28 to start tracking. A KILL EXEMPLAR IS A FROZEN ROUTING JUDGEMENT THAT KEEPS EXECUTING AFTER THE ROUTING CHANGES — when a new agent is wired, sweep the kill exemplars for classes it now owns.** The discriminator is **a concrete FL-economic transmission channel within the thesis horizon**, not the word "climate."

**Energy overlap:** a Gulf/Atlantic storm threatening **energy infrastructure** (Gulf platforms, refineries, LOOP, Cushing-adjacent logistics) is **BRENT / HAWK** primary per the energy routing — not CORAL. A storm with BOTH legs (energy-supply + FL-RE/insurance) routes the primary by dominant substance and cc's the other owner. Don't bury the FL-insurance leg inside an energy dispatch, or vice-versa.

**Why:** FL is uniquely climate-levered through its insurance market — an Atlantic hurricane-season or ENSO signal is a *forward FL-insurance / coastal-RE* signal even when it never says "Florida." Without this lane those basin-wide forecasts fell into the off-axis-climate kill bucket; this routes the FL-transmitting subset to the FL single-source-of-truth while keeping the pure-climate-science kill discipline intact.

**Filed:** Jun 26 2026 (Telegram) — Will "Enso coral yes." Stands up the CORAL ENSO/hurricane lane; the El Niño "strongest-ever" ECMWF forecast that re-surfaced in the 6/26 stream is the prompting datum. No FORMAT_SPEC domain-vocab change (geographic/relevance routing refinement, same pattern as the Florida + CREED carves).

### Muni / state-local fiscal routing — CARL (Jun 27 2026)

**The fleet has no dedicated muni-fiscal agent, by design** — muni-fiscal is a *transmission channel* that feeds existing theses, not a standalone position Will trades. This sub-section makes the standing routing explicit so muni / state-local-fiscal signals don't fall through the gap (surfaced by SIG-W-20260627-024, Ciccarone $1.03T US-cities deferred-infrastructure liability, which had no fleet owner).

**Rule:** muni / state-local public-finance signals (state & local budget stress, pension underfunding, muni-bond issuance / spreads / downgrades, deferred-infrastructure liabilities, property/sales-tax policy, revenue shortfalls, data-center→muni fiscal-credit) route by transmission leg:
- **National muni-fiscal → CARL action** — the fiscal→consumer leg CARL already owns (muni stress → tax hikes / service cuts / public-sector employment → consumer drag; the fiscal node of the stagflation thesis).
- **Florida muni-fiscal → CORAL action** instead — CORAL owns FL state fiscal + the FL property-tax amendment + FL local budgets (per the Florida carve above); CARL info on the consumer leg.
- **LIQUID info** — when it's a muni-*credit* story (muni-bond spreads, issuance freeze, downgrade waves, MMF/muni-fund flows).
- **REGINALD info** — when bank muni-bond holdings / HTM marks / state-fiscal→regional-bank exposure is the channel.
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules.
- **On-demand depth → a DEWEY `/deep-research` run** when a specific dislocation needs a real dig (a state fiscal blowup, a muni-market dislocation) — the escalation path instead of a persistent agent.

**What still KILLS / down-routes:** a pure rates/UST story with no state-local-fiscal channel stays BOND/LIQUID; a lone municipal headline with no thesis transmission (a local bond referendum with no macro read) is a Relevance-gate kill.

**Why:** muni-fiscal is real (~$4T market, a genuine transmission node) but it's a *channel into* the consumer (CARL), FL (CORAL), and credit (LIQUID/REGINALD) theses — not a position. Standing up a persistent muni agent adds fleet-bloat + stale-row risk (RULE 4 — a dormant agent is worse than none) for intake that's currently thin. Routing to the owners of the legs it transmits through covers the gap without the overhead; a CARL sub-agent or standing DEWEY task is the escalation if muni intake materially picks up.

**Filed:** Jun 27 2026 (Telegram) — Will approved routing the muni-fiscal coverage gap to CARL (national) / CORAL (FL) rather than a new agent. No FORMAT_SPEC domain-vocab change (routing refinement, same pattern as the Florida + CREED + ENSO carves).

### Climate-macro routing — AEOLUS (Jun 28 2026)

**AEOLUS** (climate→economy macro agent, built + wired by DAEDALUS 2026-06-28) is the action owner for the new `CLIMATE_MACRO` domain — macro-climate signals that carry an **economic-transmission channel**. Unlike the v0.14 ENSO/hurricane carve (which routes *FL-transmitting* climate to CORAL), this row owns the **macro/national/global** climate→economy read across AEOLUS's five channels: insurance/reinsurance, ag/food, energy demand, property/physical, supply-chain/logistics.

**Rule:** macro-climate signals with an economic channel route **AEOLUS action**, with channel-specific info cc:
- **HENRY info** — energy demand (heat-dome/cooling → nat-gas power-burn / electricity / utilities).
- **CARL info** — ag/food → consumer (crop loss, food-price transmission).
- **BRENT info** — energy complex (nat-gas/power, weather-driven supply/demand).
- **SHADE info** — insurance/reinsurance (cat losses, NFIP, reinsurance pricing).
- **CORAL** — **backup action** + the **FL handoff**: AEOLUS keeps the macro/global ENSO figure; CORAL owns FL-specific climate/coastal/insurance. **Reconcile FL climate numbers to AEOLUS's one ENSO figure — don't silo** (same pattern as CORAL/MARCO on FL migration/tourism).
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules.

**How to apply at intake (AEOLUS vs CORAL vs KILL):**
- **Macro / national / global climate with an economic channel** (ENSO state, US/continental heat-dome → energy demand, basin-wide hurricane-season → reinsurance, global ag/freight/water-level) → **AEOLUS action.**
- **FL-*specific* climate** (a storm threatening FL landfall, FL flood/SLR/NFIP, sargassum on FL beaches) → **CORAL action** per the v0.11 Florida + v0.14 ENSO carves (AEOLUS info on the macro read).
- **Energy-infrastructure storm** (Gulf platforms/refineries/LOOP) → **BRENT/HAWK** primary per energy routing (AEOLUS info on the climate driver).
- **Pure climate-science with NO economic-transmission channel** (paleoclimate, geomagnetic, seismic/volcanic with no market impact, generic "climate risk" or extreme-weather anecdotes) → **KILL (Relevance).** The discriminator is a concrete economic channel within the thesis horizon, not the word "climate." (E.g., the 2026-06-28 batch-3 kills: Afghan seismic, NL bridge-heat anecdote, UK lightning, Kilauea eruption.)

**Cluster:** CLIMATE_MACRO signals file under the `CLIMATE_MACRO` BOARD cluster (CLUSTER_TAXONOMY v0.3, the 12th cluster).

**Why:** AEOLUS is the climate→economy single-source-of-truth; routing macro-climate to a generic equities/energy lane would bury the cross-channel read (the same climate driver hitting energy + ag + insurance + supply-chain at once). The pure-science KILL discipline keeps the lane from becoming a climate-news firehose.

**Filed:** Jun 28 2026 (Telegram) — Will "Can we fix that now?" approving the CLIMATE_MACRO cluster + domain code + this routing row, after AEOLUS's first two routed signals (SIG-W-20260628-011/012) had no home. Pairs FORMAT_SPEC v0.12 (CLIMATE_MACRO domain code) + CLUSTER_TAXONOMY v0.3 (12th cluster).

### US water scarcity routing — AEOLUS (Jul 28 2026)

**AEOLUS** is the action owner for **water scarcity with an economic-transmission channel, US-focused**. This is a *scope clarification with teeth*, not a new agent: water already sat in AEOLUS as **Tier-2 structural backdrop** (`CLAUDE.md` §Tier-2, `THESIS.md`: *"Chronic drought / water stress (feeds C2, C5): Colorado River, aquifer depletion, river-freight levels"*) — but **Tier-2 backdrop gets no boot-time channel-liveness check and no threshold row**, so it was covered only when a signal happened to arrive.

**Rule:** US water-scarcity signals with a concrete economic channel route **AEOLUS action**, with:
- **CARL info** — irrigation / ag→food-price and municipal-cost→consumer transmission.
- **MARCO info** — regional macro (Southwest/Plains), migration, state fiscal.
- **WATT info** — **thermoelectric cooling + hydro generation** (a reservoir elevation is a *generation* constraint before it is an ag constraint).
- **VULCAN info** — **data-centre water consumption** as an AI-capex siting/cost constraint (see the join below).
- **CORAL** — FL handoff unchanged; FL water/drought stays CORAL-action per the v0.11/v0.14 carves.
- **REGINALD / CREED info** — where a shortage-tier declaration touches ag lending, muni credit or property values.
- **RED info** — per the standard tag rules.

**What routes here (the discriminator is a dated, quantified economic consequence — not the word "drought"):**
- **Allocation instruments:** Bureau of Reclamation **shortage-tier declarations**, the **Colorado River operating guidelines** (current set **expires 2026**, successor negotiation live), interstate compacts, adjudicated decrees.
- **Reservoir / aquifer levels tied to a decision:** Lake Mead / Lake Powell elevation vs a tier threshold; **Ogallala** depletion where it reaches an irrigation-cost or acreage decision; Western **snowpack** vs the runoff forecast that sets allocations.
- **Industrial / municipal competition for supply:** **data-centre and fab water demand**, utility rate cases with a water component, moratoria on new hookups.
- **Hydro + thermoelectric generation** constrained by water availability → **WATT**.

**What still KILLS:** water stories with **no allocation decision, no dated instrument, and no priced consequence** — generic "the West is drying," advocacy framing, single-reservoir human-interest, and **unsourced aggregate volume claims** (the 2026-06-27 *"264 billion gallons"* kill was correct on **Credibility** and stays correct). **Long-horizon structural depletion is NOT automatically a kill any more — route it as a watch-note with the horizon stated, rather than discarding it, when it carries a real quantified base** (the Ogallala item's defect was that nobody owned it, not that it was false).

**🔑 THE JOIN THAT MAKES THIS MORE THAN DROUGHT-WATCHING — and the reason it is wired the day it was:** **water is the THIRD constraint on AI data centres, after credit and power**, and the fleet routed the other two on 2026-07-28 (`SIG-W-20260728-002` — the ~$250B Nvidia/OpenAI guarantee; `SIG-W-20260728-003` — the PJM 3 GW disconnect). Cooling is water-intensive and the build-out is sited in **Arizona, Texas, Georgia and Northern Virginia** — several of them water-stressed. **AEOLUS owns the water resource; VULCAN owns the AI-capex consequence; WATT owns the generation leg. Reconcile to one figure — do not silo** (same pattern as CORAL/MARCO).

**Not WALTER's to write:** AEOLUS's promotion of water from **Tier-2 → a core channel (C6)** — with its own live read, boot-time liveness check and threshold rows — is **AEOLUS's own file** under its documented *"new channels are added deliberately, never by drift"* guard (C4/C5 were promoted by Will on 2026-06-28). Proposed to AEOLUS by packet 2026-07-28 with Will's approval recorded. **WALTER owns only this table and `REGISTRY.tsv`.**

**Promotion trigger to a standalone agent (recorded so it does not sit forever):** a sustained water thread for **~6 weeks**, **OR** the AI-water join producing its own dispatches → **DAEDALUS maturity review, Will-gated.** Fleet precedent is promotion out of a parent on demonstrated volume (HOMER out of CARL, WAL out of REGINALD); a cold-started agent becomes a dormant scaffold, which `ROSTER.md` treats as worse than none.

**Filed:** Jul 28 2026 (Telegram) — Will: *"I think I want to start tracking water scarcity (US focused)… I was thinking AEOLUS for now?"* then *"okay if AEOLUS does not already have that info go ahead."* **WALTER verified the condition before acting: AEOLUS has water as Tier-2 backdrop, not as a tracked channel.**

### Fertilizer / ag-input routing — FERT (Aug 17 2026; **potash RESTORED to FERT 2026-08-18, Will-authorized — see v0.27**)

**FERT** was **re-chartered 2026-08-16 (Will-ruled)** as an **EVENT-DRIVEN SPECIALIST** — it wakes on named triggers and runs no standing daily desk. Its first live session ran **2026-08-17**, rebuilt from primaries with **nothing carried from the March STATUS**. Its inbox is a real destination again.

**Rule:** fertilizer-domain signals route **FERT action**, with:
- **CARL info** (and **backup action**) — the food-CPI / ag-input cost-pass-through channel. CARL held this lane during FERT's dormancy and that backup routing stays live.
- **AEOLUS info** — where the driver is climate/ENSO→ag (compose with the CLIMATE_MACRO carve above: climate driver → AEOLUS action, fertilizer *price/policy* consequence → FERT action).
- **MARCO info** — trade-policy legs (export bans, tenders, AD/CVD).
- **RED info** — per the standard cluster_mediating / counter-evidence tag rules.

**In scope (nitrogen + phosphate):** urea / UAN / ammonia and DAP / MAP pricing; **DTN retail**, **NOLA barge**, **Egypt/Middle-East FOB**, World Bank Pink Sheet; **India tenders**; **China MOFCOM export policy**; **Morocco AD/CVD** and phosphate trade actions; fertilizer→food-CPI transmission prints; **CF Industries**.

**🔴 OUT of scope — POTASH, and it has no owner anywhere:** the 8/16 ruling **dropped potash from FERT's charter**, and no other agent picked it up. **A potash signal therefore has no destination agent.** Route it to **PROME**, and **say on the signal that potash is unowned fleet-wide** so the gap travels with the datum instead of being silently absorbed. **Do not route potash to FERT** (out of charter) **or to CARL** (CARL is the *food-CPI* backup, not a potash owner). Revisit when Will assigns.

**⚠️ Benchmark discipline, adopted from a measured defect rather than in the abstract:** fertilizer prices are quoted on **at least four non-interchangeable bases** — US **retail** (DTN, ~$714/ton wk 7/6-10), US **barge** (NOLA, ~$385-415/st), **international FOB** (Egypt ~$440s; World Bank Pink Sheet E.Europe prill fob ME), and futures. **They differ by ~$270/ton at the same moment.** The 2026-08-16 revival assessment found **FERT's own series was DTN retail mislabeled "NOLA"**, and WALTER's `SIG-W-20260706-008` carried a genuine **April** Pink-Sheet print (>$850/mt) **at a July date**, which inverted the sign of the channel. ⇒ **Every fertilizer number routed through this lane MUST name its benchmark AND its vintage.** A bare "urea $X" is not routable.

**Cluster:** fertilizer signals file under **`INFLATION_TRANSMISSION`** (existing cluster; no new cluster is created by this row).

**Why:** fertilizer is an **active INFLATION_TRANSMISSION channel** — the revival assessment vindicated the domain call (India tender HIT, CF **+55% EBITDA**, **phosphate now the tight leg**) even though the nitrogen price round-tripped. During dormancy these signals were being absorbed into generic CARL ag-input routing, where the nutrient-level distinctions that decide the read (nitrogen vs phosphate vs potash, retail vs barge vs FOB) were not preserved.

**Filed:** Aug 17 2026 — DAEDALUS packet `inbox/2026-08-16_from-DAEDALUS_fert-rechartered-routing-update.md` (registration checklist row 7), executing Will's 8/16 re-charter ruling. **ROSTER flips ARCHIVE SOURCES → ACTIVE when PROME runs the cutover pass; routing does not wait on that flip** — per the owner-of-record banner, ROSTER's class labels are descriptive and change no routing obligation.

### European sovereign / gilts routing — HANS (Aug 18 2026) — ✅ **CODE SHIPPED SAME DAY: `EUROPE_MACRO` added at FORMAT_SPEC v0.17 / ROUTING_TABLE v0.28. This section is no longer interim — it is retained as the RECORD OF WHY the code was needed, and its two limits still bind.**

**Route to HANS:** UK gilts, Bunds, EGB periphery spreads, BoE and ECB policy, European sovereign-credibility items, European bank/private-credit stress. **Backup: BOND** (which already took the one gilts signal that landed, and was not wrong to). **Info: LIQUID, REGINALD, CARL.**

**Will-authorized 2026-08-18** ("okay do the routing layer"), on Will's own prompting — *"Gilts to Hans?"* **His instinct was right and it beat this desk's own registry.**

🔴 **WHY THIS IS A SUB-SECTION AND NOT A DOMAIN ROW — the honest reason.** **There is no `EUROPE_MACRO` code in the canonical domain vocabulary.** FORMAT_SPEC carries 19+ codes and **none of them is Europe**, so HANS has been filed under **`GEOPOL_NON_ENERGY`** — a war/diplomacy lane — ever since. **Adding gilts to that row would repeat the exact mis-filing that caused the defect below.** Creating the code is a FORMAT_SPEC change that **Will has not authorized and WALTER did not make unilaterally.** ⇒ **routing lands now; the vocabulary question stays open and is Will's.**

⚠️ **THE DEFECT THIS CAME OUT OF, recorded because it cost a bad recommendation.** HANS's `REGISTRY.tsv` row described **a different agent** — *"Iran nuclear, Hormuz cascade, geopolitics / GEOPOLITICS,WAR / downstream HAWK,BRENT"* — from at least **2026-06-22 to 2026-08-18**, while HANS's own `CLAUDE.md` reads *"European macro through the U.S.-market lens — PMIs, ECB policy, trade/capital flows, energy, **sovereign spreads**, European bank/private-credit exposure, political risk"* and its last real session (7/16) was a **TTF escalation ladder**. **WALTER's nearest-owner scan read the stale row, saw no European desk, and recommended extending BOND.** Row corrected 8/18. **RULE 4: stale data is worse than none.**

⚠️ **THREE SURFACES DISAGREED, and one of them was this file:** line 282 already said *"Europe-macro lens stays HANS"* while the domain table routed HANS a war row.

⚠️ **TWO LIMITS ON THIS ASSIGNMENT, stated not glossed:**
1. **HANS is Tier 2. It was 33 days dark at assignment (last own session 2026-07-16) and REVIVED 2026-08-28 after 43 days** — on Will's word, with every number re-pulled live. **THE LIMIT STANDS UNCHANGED AND HANS REAFFIRMED IT: BOND takes anything TIME-CRITICAL.** **Assigning a lane does not wake a desk**, and a revival does not convert a Tier-2 spawn desk into a fast lane. HANS's own words, kept because they are the reason: *"one session back from 43 days dark does not earn a latency claim."* It is encoded at the row, not only here — `HANS-T-06`'s `recipient_chain` reads `BOND action / HANS`.
2. ✅ **RESOLVED 2026-08-28 — HANS ANSWERED YES AND ENCODED IT.** *(Was: "HANS's own docs never name the UK, gilts or the BoE… a scope question HANS has not answered." That was true for 10 days and is now false.)* HANS took the UK leg on the record — **post-Brexit is a political boundary, not a transmission one** — and encoded it at `AGENTS/HANS/CLAUDE.md:4` rather than only replying, so it survives the desk's next dark period. `workbook/FLOW.tsv` had carried `FLOW-HANS-5 UK_Pension_Stress` and `VX-HANS-1.01 UK UST Holdings` since inception. 🔑 **Will's instinct beat both registries** — his *"Gilts to Hans?"* was right while this desk's own REGISTRY row described a different agent. **Gilts do NOT revert to BOND.**

---

### War-theater routing — OSPREY / FALCON (Jul 12 2026)

**HAWK's two war-tracking loads split into sibling agents 2026-07-12** (Will-approved; root cause = the HAW-15 structural-overload miss; spec `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md`). **OSPREY** = Russia/Ukraine theater (energy-strike campaign, crude-vs-products channel, shadow-fleet *kinetic* strikes, Druzhba/EU, Baltic/Black-Sea ports). **FALCON** = US/Israel/Iran-Gulf theater (A/B/C/D ladder, Hormuz, Gulf-state targeting, Hormuz tanker attacks, Bab-al-Mandab/Houthi, Baghdad/Iraq discriminator). **HAWK residual** = cross-war synthesis + dormant book (Taiwan, Venezuela, trade war, Suez/Malacca, defense spending, sanctions-regime) + global war-risk-insurance/shipping-disruption synthesis + shadow-fleet *enforcement* (non-kinetic).

**Rule:** theater kinetic / infrastructure / escalation signals route the **theater owner action** (OSPREY or FALCON), **HAWK info** (synthesis — reconciles both theaters into one read, checks double-counting), BRENT info (oil transmission), RED per tag rules. Specifically:
- Russia refinery/terminal/port strikes, Ukraine-side tanker strikes, Druzhba → **OSPREY action.**
- Hormuz, Gulf infra strikes, Iran kinetic/diplomacy, Bab-al-Mandab/Houthi, Baghdad/PMF → **FALCON action.**
- Dormant-book geopolitics (Taiwan Strait, Venezuela, trade war, Suez/Malacca, defense budgets, sanctions-regime structure) → **HAWK action** (unchanged owner, now its explicit lane).
- War-risk insurance / shipping-disruption aggregates spanning theaters → **HAWK action** (synthesis lane), theater owners info.
- Oil PRICE/OPEC/refining-margin signals → **BRENT action** per OIL_ENERGY (unchanged since the Mar-6 handoff; the v0.17 row edit makes the table match that reality).
- `GEOPOL_NON_ENERGY` (HANS row) unchanged — Europe-macro lens stays HANS; war-theater diplomacy belongs to the theater owner.

**Cluster note:** existing `IRAN_HORMUZ` cluster signals → FALCON action under this rule (the May-6 Iran-cluster CARL-info override below still governs when CARL gets cc'd — unchanged).

**Filed:** Jul 12 2026 by DAEDALUS as part of the split registration (Will-authorized). WALTER owns the mechanics — adjust at next boot if the carve conflicts with intake reality.

### Housing routing — HOMER (Jul 12 2026)

**HOMER promoted from CARL sub-agent to top-level housing domain agent 2026-07-12** (Will-approved; OZK/CORAL/AEOLUS precedent; case + rulings `AGENTS/DAEDALUS/builds/homer_promotion/`). HOMER owns the housing **asset-market + credit-structure** surface: foreclosure pipeline (ATTOM/ICE/MBA), servicer stress, multifamily BOTH books (GSE **and CMBS-MF** — HOMER is now the single owner of the Trepp MF figure; CREED keeps non-MF CMBS), builders, HPI/supply/sales, mortgage-rate surface (PMMS, 10Y-FRM spread).

**Rule:** national housing asset-market/credit-structure signals → **HOMER action** / **CARL info** (consumer-transmission read — affordability, condo-K-shape-as-evidence, behavioral distress stay CARL's interpretation) / **REGINALD info** (Path C bank-collateral — HOMER→REGINALD is now a first-class chain edge). This **supersedes the Apr-20 Residential-housing exception's REGINALD-action default for asset-market signals** (geo-narrow non-FL residential now → HOMER action, REGINALD info). Unchanged: **FL-specific → CORAL action** per v0.11 (HOMER info; reconcile-to-one-figure); national *consumer* aggregates (household debt, consumer DQ) → CARL per CONSUMER_CREDIT; CMBS non-MF (office/retail/industrial) → CREED per v0.12.

**Filed:** Jul 12 2026 by DAEDALUS as part of the promotion registration (Will-authorized). WALTER owns the mechanics — adjust at next boot.

### Single-name routing — WAL (Jul 25 2026)

**WAL promoted out of REGINALD to a standalone agent 2026-07-25** (`git mv AGENTS/REGINALD/WAL → AGENTS/WAL`, cutover WP-W1 `ed1ce777`; Will-approved 7/22; OZK/HOMER precedent). Routing add requested by DAEDALUS (registration checklist #7, `inbox/2026-07-25_from-DAEDALUS_wal-agent-routing-add.md`). **Inbox live at `AGENTS/WAL/inbox/`.**

**Rule — mirrors the OZK seam:**

| Signal shape | Action | Info |
|---|---|---|
| **Ticker-WAL / WAL-specific** — earnings, 8-Ks, WAL v. Jefferies litigation, Cantor residual, mgmt/insider news | **WAL** | REGINALD |
| **Regional-bank cohort / KRE / multi-bank** | **REGINALD** (unchanged — keeps the hub + `BANK_EXPOSURE_MATRIX`) | WAL when a WAL leg is present |
| **Ambiguous — WAL inside a cohort story** | **REGINALD primary** | **WAL cc** |
| **Jefferies-ecosystem** | **WAL** for WAL-exposure legs; **OTTO** keeps First Brands | shared node stays `FORGE/research/jefferies/` |

**⚠️ Threshold note (WALTER's, not in the DAEDALUS packet):** **REG-T-02 (`WAL-PRICE < 78`, sustain 1, V1V3-ACCELERATE)** still lives in **REGINALD's** `THRESHOLDS.tsv` and its `recipient_chain` reads *"REGINALD action / Will."* **The registry was not re-pointed by the promotion.** Until REGINALD and WAL agree who owns that row, a REG-T-02 fire routes **REGINALD action + WAL action** — a single-name price trigger on a name with a dedicated agent should not reach only the cohort owner. **Flagged to both; the registry edit is REGINALD's to make, not WALTER's.** (WAL last $83.11, 6.5% above the trigger.)

**Filed:** Jul 25 2026 by WALTER on the DAEDALUS registration packet. REGISTRY row added the same session (the boot fs-scan had flagged `WAL` as an unregistered live dir).

### Single-name routing — FLG (Aug 22 2026)

**FLG registered 2026-08-22 on DAEDALUS's 8/20 packet** (`AGENTS/FLG/` — **Flagstar Financial, NYSE `FLG`, formerly `NYCB`**; bank sub Flagstar Bank N.A., FFIEC RSSD **694904**). Market-class, print-driven single-name specialist; built 2026-08-20, Will-approved in-session. **The fleet's first greenfield per-bank build.** ⚠️ **The boot fs-scan flagged `FLG` as an unregistered live dir on 8/20 AND 8/22 — it had a REGISTRY gap for two days, during which nothing could route to it.**

**Rule — mirrors the OZK and WAL seams:**

| Signal shape | Action | Info |
|---|---|---|
| **Ticker-`FLG` / Flagstar-specific** — earnings, 8-Ks, reserves, capital, credit quality, mgmt/insider news | **FLG** | REGINALD |
| 🔴 **Ticker-`NYCB`** — **route to the SAME desk.** The ticker changed and a large body of live coverage still uses the former name | **FLG** | REGINALD |
| **NYC rent-regulated multifamily** · **CRE concentration AT Flagstar** | **FLG** | REGINALD, CREED |
| **Regional-bank COHORT / KRE / multi-bank** | **REGINALD** (owns the cohort + `BANK_EXPOSURE_MATRIX`) | **FLG cc when an FLG leg is present** |
| **Ambiguous — FLG inside a cohort story** | **REGINALD primary** | **FLG cc** |

**⛔ DO NOT ROUTE TO FLG** (FLG's charter carries this exclusion register explicitly): peer-bank CRE events → **REGINALD** · rates/curve → **BOND** · funding-market stress → **LIQUID** · private-credit / NDFI → **BROCK**. **FLG owns the single name; REGINALD owns the cohort.**

**⚠️ Nothing to fire on yet:** FLG registered **zero gates** and proposes **zero thresholds**; its `workbook/TRIGGERS.tsv` is 7 `[EST]` rows, none a signal channel. **No FLG row exists on the boot 6b/6c trigger board and none should be invented here.**

**Filed:** Aug 22 2026 by WALTER on the DAEDALUS 8/20 registration packet.

### Coordinator delivery path — PROME (re-pointed Jul 25 2026)

**🔴 `AGENTS/PROME/` IS DEAD.** Will ruled 2026-07-24 that **PROME's sole inbox is `PROME/inbox/`**; RED executed the migration and flagged that **~30 `delivery_log.tsv` rows targeted the now-removed `AGENTS/PROME/inbox/WALTER/`**, the most recent written 2026-07-24T23:55Z. The directory had already been archived once (6/24) and **regrew to 55 files in a month because the SENDERS were never re-pointed** — deleting it again without fixing the route just starts the clock on a third re-accumulation. `MESSAGING/DIRECT_MESSAGING_V1_SPEC.md` already required this; the gap was enforcement, not policy.

**Rule:** WALTER writes PROME handoffs **FLAT to `PROME/inbox/`**, named `YYYY-MM-DD_from-WALTER_<SIG-ID>.md`. **There is no `PROME/inbox/WALTER/` sub-lane and WALTER does not create one** — per RED's migration note, do not invent structure inside PROME's tree. Historical `delivery_log` rows pointing at `AGENTS/PROME/inbox/WALTER/` are left as-is (an accurate record of where they were written); **the fix is at the source, not retroactive.**

**Filed:** Jul 25 2026 by WALTER, on RED's `2026-07-24_from-RED_agents-prome-inbox-killed-repoint-your-routing.md`. First dispatches on the new path: `SIG-W-20260725-001`/`-002`. → `[[finding_dead_path_regrows_unless_senders_repointed]]`.

### Convergence / synthesis routing — NEXUS (Jul 16 2026)

**NEXUS had ZERO presence in this table until v0.19** — while holding **6 delivered handoffs** and being routed ACTION twice on 7/16 alone. It was routed **entirely by WALTER's judgment, uncodified**, which means it worked only as long as WALTER remembered. Caught by the new `walter_doctor` `registered_but_unrouted` check **on its first run** — a second instance of the VULCAN class, found immediately.

**Why NEXUS is a META row, not a domain row.** Every row in *By Signal Domain* maps a **subject** to an owner. NEXUS has no subject — its REGISTRY `Domain` is `CONVERGENCE` and its `Chain` is `SYNTHESIS`. It consumes **across** domains; convergence is *derived*, never *arrives*. Giving it a domain row would have been the wrong shape and would have competed with the real domain owner for the action slot. **It is tag-triggered, so it belongs on the tag/meta axes.**

**Rule — NEXUS is routed by TAG, not by subject:**
1. **`signal_role: cluster_mediating` → NEXUS info** (By Tag/By Verdict). Fixes a real inconsistency: FORMAT_SPEC v0.8 gives NEXUS **authoritative-voice precedence on that exact tag** (*NEXUS > WALTER (tagger) > action-primary*) and makes it the owner of cluster-narrative-update interpretation — yet the tag routed only RED. **NEXUS could be out-voiced on a call the spec assigns to it, on a signal it never received.**
2. **Signal bears on a registered `PRED-NN` → NEXUS ACTION** (`AGENTS/NEXUS/PREDICTIONS_MONITOR.md`): it resolves / partially resolves / materially counter-evidences a row, **or** the row's own named resolution route points at this signal's subject. **A registered prediction moving off its mark is an owner re-mark = action by definition.** This codifies what WALTER was already doing ad hoc — SIG-W-20260716-001 → NEXUS action (PRED-24 Stage-3) and SIG-W-20260716-007 → NEXUS action (PRED-27 resolved PARTIAL; **PRED-45, live at 90%, met counter-evidence**, and PRED-27's monitor row literally named *"BROCK / Moody's check"* as its route).
3. **WALTER routes the evidence; it does NOT re-mark.** The prediction is NEXUS's. WALTER surfaces that a mark has met evidence its owner does not hold — **it never takes a view on where the mark should land** (RULE 1: not an analyst).

**Deliberately NOT a `FULL_NETWORK`-style catch-all.** NEXUS is cross-cutting, which makes "cc NEXUS on everything" the tempting failure — it would drown the agent and make the tag meaningless. **Two named triggers only.** If a third pattern emerges, add it explicitly.

**Does not disturb `convergence_event`** (v0.9, By Convergence): bank-ticker/multi-channel convergence detection still fires **REGINALD**-action per the REGINALD↔WALTER LIAISON Q5 lock. That is a *detection* rule on a specific ticker pattern; this is NEXUS's *narrative/prediction* lane. Different things, both live.

### AI-capex routing — VULCAN, and the substance-vs-financing boundary (Jul 16 2026)

**VULCAN / WATT / MIDAS were built by DAEDALUS 2026-07-10-11 and never wired into routing at all** — zero rows here, no mention in any WALTER design doc, no `inbox/WALTER/` dir, **so none had ever received a routed signal.** DAEDALUS wired the *7/12* batch (OSPREY/FALCON/HOMER, v0.17) but the *7/10-11* batch was missed; WALTER's boot fs-scan added REGISTRY rows on 7/16, but **a REGISTRY row is not a routing row.** Fixed here + FORMAT_SPEC v0.14 (Will sign-off 7/16 Telegram). VULCAN is **not a stub** — Maturity L2, all 4 channels carrying live reads, composite 11/20, first hard gate **7/22**.

**The boundary that actually matters — substance vs financing.** The `AI_INFRA_CAPEX` cluster is **23 signals, and a 7/16 axis check found ~13 of them are financing/credit** (SoftBank margin loans, Oracle's −$23.7B FCF + $40B raise, tech at 8.3% of HY, CoreWeave, SpaceX, the DEWEY AI-credit maps), not capex substance. Those accumulated **correctly** under CLUSTER_TAXONOMY's cross-cluster rule 1 (*substance beats financing/transmission mechanism*), which sends an AI-financing story to the AI cluster. **That rule governs the CLUSTER (where a signal is archived). It does NOT govern the DOMAIN (who acts).**

**Rule:**
- **Capex substance → `AI_CAPEX` → VULCAN action** / VIOLET, HENRY, WATT info. Hyperscaler capex guides + concentration, datacenter buildout/construction, semis + memory cycle, capex→MW conversion, AI supply-chain + export-controls.
- **AI *financing* → stays `PRIVATE_CREDIT` (BROCK) or `FUNDING_LIQUIDITY` (LIQUID) by mechanism** — margin loans on AI equity, AI-credit spreads, neocloud/vendor + circular financing, capex-funded-by-debt. **VULCAN gets info** when the financing bears on capex sustainability (it usually does — that is its S1 channel). Do **not** hand VULCAN the credit-structure call; that is BROCK/LIQUID's.
- **Overlap is the norm, not the exception.** An Oracle-style "negative FCF funding capex with debt" signal is **both**: route `AI_CAPEX`/VULCAN action **+ LIQUID/BROCK action** when the credit leg is independently actionable, rather than forcing one owner.
- **`AI_INFRA` is NOT a valid domain code** — it is VULCAN's *chain*. It appears as a `domain:` on SIG-W-20260627-019 (and `AI_CAPEX` pre-vocabulary on SIG-W-20260709-007); both are archived-as-dispatched per post-dispatch immutability and are **not** precedent.

⚠️ **Live open decision (Will's, surfaced 7/16, NOT decided):** whether to split the financing leg out of `AI_INFRA_CAPEX` as its own cluster (13 vs 10, both over the ≥3 bar, and the two halves have genuinely different readers). **That is a CLUSTER question, not a domain question — this routing rule stands either way.** VULCAN owns the domain judgment; Will signs off on structure.

### Iran-cluster CARL-info override (May 6 2026)

Iran-cluster signals (`cluster: IRAN_HORMUZ`) default to OIL_ENERGY → BRENT action with CARL on the info line. Per CARL ↔ WALTER LIAISON Q3 (Turn 1 → Turn 4, locked 2026-05-06): route CARL info **ONLY** when one of the following triggers fires:

| Trigger | Rationale |
|---------|-----------|
| Brent close **≥ $110 sustained 2 sessions** | Re-entry of accelerated pump-pass-through window per KB-CARL-259 (3-4d transmission lag in Iran-cluster regime, vs 2-3wk normal regime). |
| Brent close **≤ $95 sustained 5 sessions** | Exit of pass-through window — material relief in food/energy stack. Vector #5 reprice candidate. |
| Explicit kinetic event with supply-disruption mechanism | Vessel-strike, refinery-hit, port-closure — kinetic-actually-affecting-supply, not posture-only. |
| FX/macro cross with consumer-burden vector | USD/JPY-pump-cost-cross or similar where consumer-burden vector activates. |

**Otherwise:** posture / doctrine / diplomatic-cascade / OSINT signals → **drop CARL from info line.** Examples that would NOT cross-fire to CARL: IRGC corridor doctrine (posture only), USAF tanker emergency squawks (operational anomaly, no supply-disruption mechanism), Iran-Pakistan diplomatic shuttle (diplomatic cascade, no kinetic).

**Why:** within-range tape moves don't reach CARL's pump-pass-through threshold (Vector #5 / #12 / KB-CARL-259); routing them adds noise to CARL intake without informing thesis. Concrete thresholds replace earlier heuristic "near $110" framing.

#### Boundary-trigger threshold-cross dispatch (NEW v0.6)

When Brent sustains:

- **≤ $95 for 5+ sessions** → dispatch IMMEDIATE → CARL with `signal_type: threshold-crossed` + `consumer_transmission: pump_pass_through` + dispatch_note flagging Vector #5 Gas Squeeze + Vector #12 Stagflation reprice + CRL-08 trigger (92→60% per CARL Q12 framework, Turn 3)
- **≥ $115 for 5+ sessions** → dispatch IMMEDIATE → CARL with same tags + flagging Vector #5/#12 hardening + CRL-08 reprice 92→97%+ (per CARL Q12)

Within $95-115 range = noise floor; tape moves don't cross-fire to CARL.

**Q-trail:** CARL LIAISON Q3 (Turn 1) → WALTER Turn 2 DECISION (calibrate going forward) → CARL Turn 3 SHARPENING (concrete thresholds) → WALTER Turn 4 LOCK.

### MARKET_VOL vol-ownership split (Jun 10 2026)

The previously-bundled `MARKET_VOL` row is split into two routing lines (single domain code retained — this is a within-domain routing split, not a vocabulary change):

- **Vol-regime content** — VIX complex, vol-regime classification, term structure (VIX3M/VIX, backwardation/contango), VVIX/vol-of-vol, SKEW/tail pricing, vol ETP stress/termination events, vol-targeting/vol-control/CTA de-risking flows, credit-to-vol transmission timing → **VIOLET action, HENRY backup.**
- **Index-mechanics content** — index price moves, dealer gamma/put-wall/0DTE flow mechanics, correlation breaks → **HENRY action, LIQUID backup** (unchanged from pre-split).

**Boundary rule (from VIOLET's SIGNAL_INTAKE.md, 2026-06-10 rebuild):** dealer-gamma *mechanics* are HENRY's; the gamma *flip event itself* + regime implication is VIOLET-relevant — on a confirmed dealer-gamma FLIP event, add VIOLET to the info line of the HENRY-routed signal. Conversely, HENRY stays on the info line of all VIOLET-routed vol-regime signals (backup-promotion stays a single-field swap per Backup column semantics).

**Why:** the bundled row predated the vol-ownership split (auto-memory `feedback_henry_vol_broadcast_to_violet` — VIOLET owns vol-regime broadcast; HENRY keeps gamma/0DTE/put-wall) and routed nothing to VIOLET. VIOLET's domain depth (KB episode database, L1 base-rate table, regime classifier) makes her the natural action recipient for regime-level vol signals.

**How to apply at intake:** ask "is this signal about the *state/structure of volatility* or about *index-level flow mechanics*?" Vol-state/structure → VIOLET. Flow mechanics/index moves → HENRY. If a signal genuinely carries both (e.g., a vol spike WITH a gamma-flip report), route VIOLET action + HENRY info with the flip named in dispatch_note, since regime implication dominates for network consumption.

**Filed:** Jun 10 2026. Proposed by VIOLET (SIGNAL_INTAKE.md rebuild Appendix A, relayed per spec-change rule); Will approved same day.
