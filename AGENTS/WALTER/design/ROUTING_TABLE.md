# WALTER Routing Table v0.48

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

> **Authority by subject:** `PROME/ROSTER.md` owns fleet membership and responsibility classes; domain CLAUDE/STATUS files own domain evidence and judgment; `AGENTS/_NETWORK.md` owns transmission topology. This table and ROUTING_OVERLAYS own routing defaults and overrides; BOARD_CONSUMPTION_SPEC owns delivery duties. `REGISTRY.tsv` mirrors routing/state. Missing or conflicting mirror rows require reconciliation at the relevant owner, never erasure of a desk. Roster classes do not change routing or delivery obligations.

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.


**Version history → [`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** (v0.1 → v0.31, moved verbatim 2026-08-30; `git log -p -- AGENTS/WALTER/design/ROUTING_TABLE.md` is the other copy). **Current: v0.48 (October 23, evening)** — **the `CYBER` row stops filtering on a money channel:** WALTER sends CYPHER every cyber event or claim, including leak-site and threat-actor claims and items with no visible money channel; the money channel sets precedence, not inclusion; channel-less claims fold into one ROUTINE CYPHER card per sitting. Cause: on 10/23 WALTER dropped two leak claims as "no money channel" and closed a CVSS 10 GitLab flaw as a duplicate of a headline line (re-routed as `SIG-W-20261023-045`); CYPHER's charter owns viral-claim triage, so the inclusion call is CYPHER's. Will 2026-10-23 17:16 ET (hook clock) in the WALTER terminal (AskUserQuestion, "Approve both (Recommended)"). **No recipient moved.** CHECKLIST v0.54 rule 1b carries the companion dedup rule. Companions lockstep. Prior: **v0.47 (October 23, later)** — records **WQ-507 (RULED APPROVE A, Will 2026-10-23 10:38 ET in PROME's window, as read and stated back by PROME): HENRY's `ISM Mfg <47` trigger MOVES to ISHM, HENRY informed.** This supersedes v0.46's note that the trigger was not moved. **No route in this table moved:** the trigger's recipient chain lives in the owners' records (`AGENTS/ISHM/`, `AGENTS/HENRY/CLAUDE.md`), not here. Companions lockstep. Prior: **v0.46 (October 23)** — adds the **`INDUSTRIAL_CYCLE` → ISHM** By-Signal-Domain row (code minted at FORMAT_SPEC v0.27 the same morning; Will sign-off 2026-10-23 10:04 ET in the WALTER terminal ("Yes ISHM signoff approved")); **re-cuts `MACRO_INFLATION`** so the manufacturing-cycle read of ISM / PMI leaves CARL's row (CARL keeps prices-paid and the consumer read, one figure shared); **adds ISHM to `TARIFF_TRADE` info** (CARL keeps the announcement, ISHM the effect on manufacturers). ISHM built by DAEDALUS 080fbc7d6 on WQ-506 (Will 09:35 ET). HENRY's `ISM Mfg <47` trigger is NOT moved (WQ-506 did not rule it). Companions lockstep. Prior: **v0.45 (October 22)** — adds the **`CYBER` → CYPHER** By-Signal-Domain row (code minted at FORMAT_SPEC v0.26 the same evening; Will sign-off 2026-10-22 in the WALTER terminal (AskUserQuestion, "Approve as drafted")). CYPHER built by DAEDALUS 18770981e on Will's 17:04 ET direction. **No existing route moved;** companions lockstep. Older entries (v0.44 back to v0.32): moved verbatim 2026-10-23 to [`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md) § "Moved 2026-10-23" (read-cap rotation, 83% → below 70%).

> **Size re-trigger (split 2026-09-08):** measure both boot files at every Tier-2 closeout and after an append; apply READ_CAP.md rotation tiers. Calendar size check completed 2026-10-16; receipt: `../research/2026-10-16_instruction-fixes/RESULT.md`. Both halves remain on the boot path: this controls per-read size, not total context. Exact pre-split record: `history/ROUTING_TABLE_BEFORE_SPLIT_2026-09-08.md`; obligation/byte receipt: `../research/2026-09-08_boot-maintenance/rotation-receipt.json`.

## Routing reading paths

| File | When | Boot? |
|---|---|---|
| **`ROUTING_TABLE.md`** (this) | Domain table, meta rows and backup semantics | ✅ **BOOT — read whole first** |
| **[`ROUTING_OVERLAYS.md`](ROUTING_OVERLAYS.md)** | By Type/Tag/Boundary/Convergence, safety net, escalation and MINIMIZE | ✅ **BOOT — read whole second; also consult at dispatch** |
| **[`ROUTING_CARVEOUTS.md`](ROUTING_CARVEOUTS.md)** | **AT DISPATCH**, when a signal is in that agent's lane — the 23 per-agent carve-outs | ❌ not at boot |
| **[`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** | provenance, on demand | ❌ not at boot |

> ⚠️ **The carve-outs are ROUTING LAW, not commentary** — they are what puts CORAL on a Florida signal and the current TERRY delivery exemption. Historical T-1 gate text remains marked superseded at its owner. They moved because they are read at DISPATCH, not at boot. **A pointer nobody travels is how a rule dies** (`[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`), so the full inventory is named here and the dispatch step names the file.

### Carve-out inventory (23 sections — text in `ROUTING_CARVEOUTS.md`)
- Residential-housing stress exception (Apr 20 2026)
- Florida-specific routing — CORAL (Jun 19 2026)
- National CRE / CMBS market-stress routing — CREED (Jun 22 2026)
- Trade-construction info routing — TERRY (Jun 22 2026) — ⛔ **SUPERSEDED 2026-08-07**
- 🔴 Trade-construction ACTION routing — TERRY (Aug 7 2026) — supersedes the Jun-22 info lane above
- Climate / hurricane-season / ENSO routing — CORAL (Jun 26 2026)
- Muni / state-local fiscal routing — CARL (Jun 27 2026)
- Climate-macro routing — AEOLUS (Jun 28 2026)
- US water scarcity routing — AEOLUS (Jul 28 2026)
- Fertilizer / ag-input routing — FERT (Aug 17 2026; **potash RESTORED to FERT 2026-08-18, Will-authorized — see v0.27**)
- European sovereign / gilts routing — HANS (Aug 18 2026) — ✅ **CODE SHIPPED SAME DAY: `EUROPE_MACRO` added at FORMAT_SPEC v0.17 / ROUTING_TABLE v0.28. This section is no longer interim — it is retained as the RECORD OF WHY the code was needed, and its two limits still bind.**
- War-theater routing — OSPREY / FALCON (Jul 12 2026)
- Housing routing — HOMER (Jul 12 2026)
- Single-name routing — WAL (Jul 25 2026)
- Single-name routing — FLG (Aug 22 2026)
- Coordinator delivery path — PROME (re-pointed Jul 25 2026)
- Convergence / synthesis routing — NEXUS (Jul 16 2026)
- AI-capex routing — VULCAN, and the substance-vs-financing boundary (Jul 16 2026)
- Iran-cluster CARL-info override (May 6 2026)
- MARKET_VOL vol-ownership split (Jun 10 2026)
- 🆕 Sector-name routing — CRUISE (Sep 11 2026) — **the lane was ABSENT, not narrow: 0 hits across all three routing files at v0.32 while the desk sat ACTIVE with a live ruled falsifier (WQ-222 / `VX-CRU-06`, window open through the CCL Q3 print ~10/5)**
- 🆕 **Named-case feed — CREED (Sep 29 2026)** — any named-property CRE distress signal carries `case:` and CREED on the lines (INFO when another desk owns it); feeds CREED's case ledger. Will-approved
- 🆕 **Large-bank multi-name routing — GIBBS (Oct 14 2026)** — the 16 Category I–III firms (PERIMETER.tsv) → GIBBS action / REGINALD info; NDFI → BROCK primary, COF/AXP card → CARL, BK/STT custody → LIQUID + GIBBS; ⛔ HBAN, foreign-bank US IHCs, KRE. WQ-426 RULED


---

## By Signal Domain

| Domain code | Row description | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-------------|-----------------|--------|--------|-----------------|-------------------|---------------|
| `LABOR` | Employment — NFP, claims, JOLTS, wages, U-3, LFPR | CARL | HENRY | HENRY, RED | IMMEDIATE (data day) / PRIORITY (analysis) | LABOR_DOWNSTREAM |
| `MACRO_INFLATION` | Inflation + growth — CPI, PCE, PPI, UMich, GDP, retail sales; **ISM / PMI prices-paid and the consumer read only** (v0.46: an ISM / PMI print routes `INDUSTRIAL_CYCLE` → ISHM; put CARL on the action line beside ISHM when the prices-paid leg is the decision-relevant one) | CARL | HENRY | HENRY, LIQUID, RED | IMMEDIATE (data day) / PRIORITY (analysis) | THESIS_CORE |
| `TARIFF_TRADE` | Executive orders, tariff changes, trade deals | CARL | HENRY | HENRY, REGINALD, RED, MARCO, **ISHM** (v0.46: the effect on manufacturers) | IMMEDIATE (announcement) / PRIORITY (analysis) | THESIS_CORE |
| `CONSUMER_CREDIT` | CC/auto/student loan delinquency, household debt | CARL | REGINALD | REGINALD, RED | PRIORITY | THESIS_CORE |
| `BANK_CRE` | Bank earnings, CRE, hidden CRE (MI3), NDFI, capital rules | REGINALD | BROCK | BROCK, LIQUID, RED | IMMEDIATE (earnings) / PRIORITY (research) | CREDIT_CHAIN |
| `FUNDING_LIQUIDITY` | HY OAS, SOFR, repo, RRP, dealer capacity, Treasury auctions; **+ HY BREADTH / SPREAD DISPERSION (v0.27 — ratifying existing practice, 25 signals already routed here): CCC-vs-BB dispersion, HY advance/decline line, distressed ratio, issuer-count widening.** 🔑 **Why it is a named lane and not a detail: `RED-FT-01` and `RED-FT-02` both key on the OAS *LEVEL*, so an index that stays calm while breadth deteriorates is invisible to BOTH triggers BY CONSTRUCTION** | LIQUID | HENRY | BROCK, SHADE, HENRY | IMMEDIATE (stress) / PRIORITY (monitoring) | CREDIT_CHAIN |
| `PRIVATE_CREDIT` | BDC gates, PC fund redemptions, PIK rates, software PE, PCDR | BROCK | SHADE | LIQUID, REGINALD, RED | PRIORITY | CREDIT_CHAIN |
| `INSURANCE_SHADOW` | PE-insurer nexus, reinsurance, Level 3, captive insurers | SHADE | BROCK | LIQUID, BROCK | PRIORITY | — |
| `OIL_ENERGY` | Crude prices, OPEC, refining, shipping (war-driven facility damage → theater owner, v0.17 sub-section) | BRENT | HAWK | HAWK, RED | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_ENERGY` | War-theater kinetic/infra/chokepoints — Russia/Ukraine → OSPREY; Iran/Gulf (Hormuz, Bab-al-Mandab) → FALCON (v0.17 sub-section) | OSPREY / FALCON (by theater) | HAWK | HAWK, BRENT, SAM | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_NON_ENERGY` | Ceasefires, diplomacy, nuclear, war outside supply | HANS (Tier 2 — spawn) | HAWK | HAWK, BRENT, SAM, RED | PRIORITY | — |
| `EUROPE_MACRO` | **European macro through the US-market lens (v0.28)** — UK gilts · Bunds · EGB periphery spreads · BoE + ECB policy · European sovereign credibility · European bank/private-credit stress · euro-area PMIs. **Added because its ABSENCE was corrupting a registry row, not because a new agent appeared** — see the sub-section below for the two-month mis-filing it caused. ✅ **UK LEG ANSWERED — YES, 2026-08-28.** Gilts, the BoE and UK sovereign/LDI stress are HANS's, **encoded at `AGENTS/HANS/CLAUDE.md:4`** so the scope survives the desk's next dark period. HANS's reasoning: gilt-LDI (Sep 2022) is the canonical Europe→US funding-transmission event and this charter already claimed sovereign-spread/LDI stress — *the UK was already in the book; only the label was missing.* ⚠️ **LIMIT 1 IS NOT DISCHARGED AND WAS REAFFIRMED BY HANS ITSELF: BOND takes anything TIME-CRITICAL.** HANS revived 2026-08-28 after **43** days dark and declined to soften it — *"one session back from 43 days dark does not earn a latency claim."* **An answered question tends to retire its neighbours; this one does not.** | HANS (Tier 2 — spawn) | **BOND** | LIQUID, REGINALD, CARL | PRIORITY (policy/auction) / IMMEDIATE (sovereign stress event) | — |
| `JAPAN_BOJ` | USD/JPY, BOJ policy, JGB yields, carry trade, MOF intervention; **+ CROSS-CURRENCY / EM FX CARRY (v0.27): funding-currency unwind wherever it funds — BRL/MXN/ZAR/TRY-lira and the EM carry basket, not the yen leg alone.** **Measured cause: ~30 such signals landed on SIX different desks (SHADE+BROCK, FALCON+BRENT, VIOLET, SAM, SAM+BOND, REGINALD) with no owner — the worst scatter of the five gaps.** 🔑 **SAM's REGISTERED DOMAIN CODE IS ALREADY `CARRY_TRADE`, so this is a scope CLARIFICATION, not a new assignment** — same mechanism, different funding currency. 🟠 **The code NAME `JAPAN_BOJ` now understates the row; a rename is a FORMAT_SPEC question, flagged not taken** | SAM | LIQUID | LIQUID, RED | IMMEDIATE (intervention) / PRIORITY (monitoring) | — |
| `MARKET_VOL` (vol-regime) | VIX complex, vol regime, term structure, VVIX, SKEW, vol ETP stress, vol-targeting/CTA flows | VIOLET | HENRY | HENRY, LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `MARKET_VOL` (index-mechanics) | Index moves, dealer gamma, 0DTE, put-wall, correlation breaks | HENRY | LIQUID | LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `ASIA_CONTAGION` | China/HK peg, LGFV, HIBOR-SOFR, Chinese trade policy, supply-chain coercion, export-control regs, EM Asia spillover; **+ CHINA 10Y / CGB SOVEREIGN YIELD (v0.27 — Will-proposed 8/18, WALTER concurred).** ⚠️ **Boundary, because BOND took the one that landed and was not wrong to: the signal value in a CGB yield is *"what is Beijing doing"* (ZHAO) rather than *"how is the CGB market clearing"* (BOND). A CGB MARKET-STRUCTURE item — auction mechanics, dealer behaviour, curve plumbing — still routes BOND** | ZHAO (Tier 2 — spawn) | SAM | RED, HENRY, LIQUID, BRENT/HAWK (when rare-earths), PROME | PRIORITY (policy/research) / IMMEDIATE (CNY intervention, LGFV event) | — |
| `UST_FOREIGN` | TIC flows, foreign UST holder behavior, auction demand composition | ZHAO (Tier 2 — spawn) | BOND (Tier 2) | LIQUID, HENRY, RED | IMMEDIATE (TIC release day) / PRIORITY (composition shifts) | CREDIT_CHAIN |
| `CLIMATE_MACRO` | Macro climate→economy — ENSO/El-Niño state, energy demand (heat/cooling/power-burn), ag/food, insurance/reinsurance, property/physical, supply-chain/logistics | AEOLUS | CORAL | HENRY, CARL, BRENT, SHADE, RED (per channel) | PRIORITY (forecast/structural) / IMMEDIATE (acute landfall / grid / crop-loss event) | CLIMATE |
| `AI_CAPEX` | AI-infra capex **substance** — hyperscaler capex guidance/concentration, datacenter buildout, semis + memory cycle, capex→power-demand, AI supply-chain/export-controls. **NOT the financing leg** (→ `PRIVATE_CREDIT`/`FUNDING_LIQUIDITY`; see sub-section below) | VULCAN | HENRY | VIOLET, HENRY, WATT, RED | PRIORITY (guidance/research) / IMMEDIATE (a capex CUT — VULCAN's not-yet-fired gate) | AI_INFRA |
| `POWER_GRID` | Grid stress → power price → power cost — grid emergencies/EEA, spark spreads, capacity auctions, interconnect queue, utility rate cases, on-site generation | WATT | HENRY | HENRY, CARL, VULCAN, AEOLUS, RED | PRIORITY (rate case / capacity auction / structural) / IMMEDIATE (acute grid emergency) | POWER |
| `METALS` | Metals as macro tells — monetary (gold/silver/GSR, CB buying, ETF flows) + industrial (copper/PGM, LME/COMEX inventories, backwardation) | MIDAS | LIQUID | LIQUID, HENRY, BOND, RED | PRIORITY | METALS |
| `RU_STATE_ACTOR` | **Russia state-actor intent (v0.40, 2026-10-04)** — decrees, seizures/expropriation/nationalisation, expulsions, mobilisation/force posture, export instruments (bans/quotas/licences), Kremlin political calendar. ⚠️ **Boundaries:** NOT Russia macro; a Russia ENERGY-strike or crude-flow item is **OSPREY's** (`GEOPOL_ENERGY`), this code is the state's INTENT/instrument actions; the NATO/Western reaction is **HAWK's**. Added because YURI (DAEDALUS-wired 2026-09-24, WQ-267) had NO code and NO routing row — the same quiet mis-filing EUROPE_MACRO closed, one step earlier (no lane at all). Will sign-off 2026-10-04. | YURI (Tier 2 — spawn) | HAWK | HAWK, OSPREY, PROME, RED | PRIORITY (decree/seizure/export-instrument) / IMMEDIATE (mobilisation or a market-moving expropriation) | — |
| `CYBER` | **Cyber events with a money channel (v0.45, 2026-10-22)** — exploited flaws in widely used products, supply-chain compromises, ransomware/data theft at financial firms or their vendors, OT attacks (ships, grid, pipelines), market/payment/cloud outages, certificate-trust failures, state campaigns. **v0.48: WALTER does NOT apply the money-channel test — every cyber event or claim routes to CYPHER (leak-site and threat-actor claims, items with no visible channel); the channel sets PRECEDENCE, not inclusion; channel-less claims fold into one ROUTINE CYPHER card per sitting.** **CYPHER owns the EVENT; consequence owners keep the consequence** (boundaries: `AGENTS/CYPHER/CLAUDE.md` § IDENTITY & SCOPE). Add the CHANNEL owner to info: GIBBS (large banks), LIQUID (payments/plumbing), BOND (Treasury plumbing), OTTO (auto dealers), FALCON/OSPREY (theater), WATT (grid), HANS/SAM (Europe/Japan); for the charter's NO-OWNER classes (crypto-exchange or stablecoin hack, healthcare claims processor, trading-software trust-chain breakage) add PROME. ⚠️ Bank-by-bank exposure findings never go to the BOARD as a list (DEWEY guardrail, carried in CYPHER's charter). Will sign-off 2026-10-22 in the WALTER terminal (AskUserQuestion, "Approve as drafted"). | CYPHER (Tier 2 — spawn) | REGINALD | REGINALD, SHADE, VULCAN, RED + channel owner | PRIORITY / IMMEDIATE (a CYPHER escalation-watch row FIRED, or a named bank, core vendor or payment system hit) | — |
| `INDUSTRIAL_CYCLE` | **US industrial / manufacturing cycle (v0.46, 2026-10-23)** — the manufacturing-cycle read of ISM and S&P Global PMIs (one figure), regional Fed surveys, IP / capacity utilization, durable goods and core capex orders, factory orders, freight volumes **excluding tankers**, the frozen bellwether perimeter (CAT, DE, HON, GE, PH, MMM, EMR, UNP — `AGENTS/ISHM/PERIMETER.tsv`), tariff and reshoring effects on manufacturers. **ISHM's question:** is the upturn real end-demand, or tariff front-running plus AI / defence capex and inventory rebuild, and when does it roll over? **Add the CHANNEL owner to info:** WATT (power-equipment demand; Eaton / GE Vernova are WATT's), VULCAN (core capex vs AI capex, ISHM job J1), LIQUID (freight vs credit, job J2), OTTO (auto production inside IP), HANS (euro-area PMIs; German PMI is ISHM's inbound lead), FERT (Deere's farm-income side), GIBBS / REGINALD (C&I lending). Boundaries: `AGENTS/ISHM/CLAUDE.md` § BOUNDARIES. **First-session pointer (not a re-delivery; ISHM reads these on the BOARD):** `SIG-W-20261023-010` (US flash PMI Oct, routed to CARL under the interim rule), `SIG-W-20261023-014` (Michigan final, buying conditions for durables). Will sign-off 2026-10-23 10:04 ET in the WALTER terminal ("Yes ISHM signoff approved"). | ISHM (Tier 2 — DOCKET-woken) | HENRY | CARL, HENRY, LABOR, RED + channel owner | IMMEDIATE (ISM / PMI / IP / durables release day, or a bellwether print) / PRIORITY (analysis, regional surveys, freight) | — |
| `FERT_INPUTS` | Fertilizer supply/price/policy → food-CPI transmission — **the full N-P-K complex FOR ROUTING (v0.27), at the depths ruled 2026-08-18 (v0.29) — NITROGEN** (urea/UAN/ammonia, DTN retail, NOLA barge, India tenders, China MOFCOM export policy) **· PHOSPHATE** (DAP/MAP, Morocco AD/CVD) **· POTASH** (Belarus/Russia sanctions exposure, Nutrien/Mosaic curtailment, Saskatchewan supply) — fertilizer→ag-input cost pass-through, **CF Industries**. 🔴 **POTASH RESTORED 2026-08-18 — but at TRIAGE DEPTH, WILL-RULED IN-SESSION (root `CLAUDE.md` + `PROME/ROSTER.md`, `cd7c04bb0`). ⛔ NOT full ownership: LOG + FLAG PROME, DO NOT DEEP-DIVE**, until FERT's charter edit lands (DAEDALUS-owed) **and its benchmark row is registered.** **Revisit condition is named, not open-ended: depth is reconsidered once N+P benchmark discipline is demonstrated.** **It was never ruled OUT either: the 8/16 re-charter contains ZERO occurrences of "potash" and scoped positively as "nitrogen AND phosphate" — the exclusion was an inference about that wording, correctly registered by DAEDALUS and never decided by anyone.** ⚠️ **THE CHARTER'S "do not deep-dive" IS NOW THE RULED DEPTH, NOT A LAG. `AGENTS/FERT/CLAUDE.md` line ~51 keeps that clause on purpose; DAEDALUS's owed edit changes only the OWNER half.** *(v0.27 framed this as a temporary charter lag — that was WIDER than the ruling and is corrected at v0.29. Recorded rather than silently narrowed, because "full scope, pending implementation" and "triage depth, by ruling" read identically on a routing row and mean different things to whoever grades it.)* ⚠️ **BENCHMARK DISCIPLINE APPLIES WITH FORCE — potash is a FOURTH benchmark family (Brazil CFR · SE Asia CFR · Vancouver FOB · Midwest retail) on a desk revived precisely because a ~$270/ton basis mislabel killed its predecessor. Benchmark + unit + date on every potash cell, or the cell is wrong** | FERT | CARL | CARL, AEOLUS, MARCO, RED | PRIORITY (policy action / tender print) / ROUTINE (price monitoring) | THESIS_CORE |

### Meta rows (not content domains — signal_type axis)

| Row | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-----|--------|--------|-----------------|-------------------|---------------|
| **Thesis Confirmation** (signal_type: thesis-confirmation) | RED | — | THESIS_CORE | PRIORITY | ADVERSARIAL |
| **Counter-Evidence** (signal_type: counter-evidence) | RED | — | — | PRIORITY | ADVERSARIAL |
| **Position-Specific Risk** (signal_type: position-risk) | Will (via Telegram) | — | Relevant agent | FLASH or IMMEDIATE | — |
| **Broad Market Stress** (safety-net trigger, multi-domain) | LIQUID | HENRY | FULL_NETWORK | IMMEDIATE | FULL_NETWORK |
| **Convergence / cluster-narrative** (v0.19 — `signal_role: cluster_mediating`, or a signal bearing on a registered `PRED-NN`) | **NEXUS** | HENRY | RED | PRIORITY | SYNTHESIS |

### Backup column semantics

Backup is the second-choice Action recipient if the primary is overloaded, dormant, or unavailable. WALTER uses the backup when:
- Primary's STATUS.md is stale by >5 days
- Primary is explicitly flagged in MINIMIZE mode
- Primary's last-seen session was spawning sub-agents (deep research mode, should not be interrupted)
- Will explicitly overrides

Backup recipients should already be in the Info list for the same row, so promoting to Action is a single-field swap, not a full re-route.

---

## By Signal Type

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#by-signal-type). Read it as part of boot step 6.

## By Tag/By Verdict (NEW v0.7)

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#by-tagby-verdict-new-v07). Read it as part of boot step 6.

## By Boundary Threshold (NEW v0.8)

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#by-boundary-threshold-new-v08). Read it as part of boot step 6.

## By Convergence (NEW v0.9)

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#by-convergence-new-v09). Read it as part of boot step 6.

## Safety Net Auto-Upgrades

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#safety-net-auto-upgrades). Read it as part of boot step 6.

## Escalation Paths

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#escalation-paths). Read it as part of boot step 6.

## MINIMIZE Routing Adjustments

Canonical section: [ROUTING_OVERLAYS.md](ROUTING_OVERLAYS.md#minimize-routing-adjustments). Read it as part of boot step 6.
