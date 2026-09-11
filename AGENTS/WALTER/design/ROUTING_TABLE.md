# WALTER Routing Table v0.33

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

> **📌 OWNER-OF-RECORD FOR ROUTING & DELIVERY FACTS (added v0.23, 2026-08-07 — Will-accepted RAV roster plan Part D, via PROME 2026-08-05).** **This table + `AGENTS/WALTER/REGISTRY.tsv` are the single owner-of-record for every routing and delivery fact about an agent** — who receives what, at what precedence, on which chain, and through which delivery lane. **`PROME/ROSTER.md` POINTS here and restates nothing**; where ROSTER and these two surfaces disagree, **these win**, and the fix belongs here. ROSTER's five descriptive classes (ORGANIZING/SERVICE · REVIEW/QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST) are **descriptive only and change no routing, precedence or delivery obligation** — do not read a class label as a routing input. *(`REGISTRY.tsv` is a bare TSV with a machine-parsed header row and cannot carry a prose statement without breaking its readers, so the statement lives here and in `WALTER/CLAUDE.md`'s KEY DESIGN FILES row.)*

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.


**Version history → [`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** (v0.1 → v0.31, moved verbatim 2026-08-30; `git log -p -- AGENTS/WALTER/design/ROUTING_TABLE.md` is the other copy). **Current: v0.33 (September 11)** — adds the CRUISE sector-name carve-out (below), answering PROME's 9/10 flag: CRUISE had ZERO routes since its 8/21 ACTIVE re-class because its REGISTRY Domain cell (`DEMAND_DESTRUCTION`) is not a code in FORMAT_SPEC's vocabulary, so no domain row could carry it. **No new domain code minted; no existing route moved.** Prior v0.32 (September 8): size split only. Prior v0.31: TERRY reverted to the RED-class exemption.

> **Size re-trigger (split 2026-09-08):** measure both boot files at every Tier-2 closeout and after an append; apply READ_CAP.md rotation tiers. Next calendar check: 2026-09-30. Both halves remain on the boot path: this controls per-read size, not total context. Exact pre-split record: `history/ROUTING_TABLE_BEFORE_SPLIT_2026-09-08.md`; obligation/byte receipt: `../research/2026-09-08_boot-maintenance/rotation-receipt.json`.

## Routing reading paths

| File | When | Boot? |
|---|---|---|
| **`ROUTING_TABLE.md`** (this) | Domain table, meta rows and backup semantics | ✅ **BOOT — read whole first** |
| **[`ROUTING_OVERLAYS.md`](ROUTING_OVERLAYS.md)** | By Type/Tag/Boundary/Convergence, safety net, escalation and MINIMIZE | ✅ **BOOT — read whole second; also consult at dispatch** |
| **[`ROUTING_CARVEOUTS.md`](ROUTING_CARVEOUTS.md)** | **AT DISPATCH**, when a signal is in that agent's lane — the 21 per-agent carve-outs | ❌ not at boot |
| **[`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** | provenance, on demand | ❌ not at boot |

> ⚠️ **The carve-outs are ROUTING LAW, not commentary** — they are what puts CORAL on a Florida signal and the current TERRY delivery exemption. Historical T-1 gate text remains marked superseded at its owner. They moved because they are read at DISPATCH, not at boot. **A pointer nobody travels is how a rule dies** (`[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`), so the full inventory is named here and the dispatch step names the file.

### Carve-out inventory (21 sections — text in `ROUTING_CARVEOUTS.md`)
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


---

## By Signal Domain

| Domain code | Row description | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-------------|-----------------|--------|--------|-----------------|-------------------|---------------|
| `LABOR` | Employment — NFP, claims, JOLTS, wages, U-3, LFPR | CARL | HENRY | HENRY, RED | IMMEDIATE (data day) / PRIORITY (analysis) | LABOR_DOWNSTREAM |
| `MACRO_INFLATION` | Inflation + growth — CPI, PCE, PPI, UMich, GDP, ISM, retail sales | CARL | HENRY | HENRY, LIQUID, RED | IMMEDIATE (data day) / PRIORITY (analysis) | THESIS_CORE |
| `TARIFF_TRADE` | Executive orders, tariff changes, trade deals | CARL | HENRY | HENRY, REGINALD, RED, MARCO | IMMEDIATE (announcement) / PRIORITY (analysis) | THESIS_CORE |
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
