# WALTER Routing Table v0.19

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.

**Version history:**
- **v0.19 (Jul 16):** **Codified NEXUS**, which had **zero presence in this table** while holding 6 delivered handoffs and being routed ACTION twice on 7/16 — i.e. routed **entirely by WALTER's judgment, uncodified**, working only as long as WALTER remembered. Surfaced by the new `walter_doctor` `registered_but_unrouted` check **on its first run** (a 2nd instance of the v0.18 VULCAN class, found immediately). **Routed as a META/TAG row, NOT a domain row** — NEXUS has no subject (`Domain: CONVERGENCE` / `Chain: SYNTHESIS`); it consumes *across* domains, and a domain row would compete with the real owner for the action slot. Two named triggers: **(1)** `signal_role: cluster_mediating` → **NEXUS info** — fixing a real inconsistency, since FORMAT_SPEC v0.8 gives NEXUS **authoritative-voice precedence on that exact tag** yet the tag routed only RED (**NEXUS could be out-voiced on a call the spec assigns it, on a signal it never received**); **(2)** signal bears on a registered **`PRED-NN`** → **NEXUS ACTION** (a registered prediction moving off its mark is an owner re-mark = action by definition). Deliberately **not** a FULL_NETWORK catch-all — "cc NEXUS on everything" is the tempting failure and would make the tag meaningless. `convergence_event` → REGINALD (v0.9 LIAISON Q5 lock) **unchanged** — that is ticker-pattern *detection*, this is the *narrative/prediction* lane. **WALTER routes the evidence and never re-marks** (RULE 1). Will sign-off 2026-07-16 Telegram ("codify NEXUS"). Propagates to STATE §1.
- **v0.18 (Jul 16):** Added the **`AI_CAPEX` (→ VULCAN)**, **`POWER_GRID` (→ WATT)** and **`METALS` (→ MIDAS)** domain rows to the By Signal Domain table + an "AI-capex routing — VULCAN, and the substance-vs-financing boundary" sub-section. **Closes a total routing gap: all three agents (DAEDALUS-built 7/10-11) had ZERO rows here, appeared in no WALTER design doc, and had no `inbox/WALTER/` dir — none had ever received a routed signal**, while the AI_INFRA_CAPEX cluster covering VULCAN's exact domain grew to 23. Cause: DAEDALUS wired the *7/12* batch (OSPREY/FALCON/HOMER) at v0.17 but missed the *7/10-11* batch; WALTER's 7/16 boot fs-scan added REGISTRY rows, but **a REGISTRY row is not a routing row** — the two surfaces drifted independently and nothing reconciled them. Already producing drift: dispatch had invented **two de-facto codes for one lane** (`AI_CAPEX` + `AI_INFRA`, the latter being VULCAN's chain used as a domain). Domain codes land in FORMAT_SPEC v0.14 first (canonical-source rule); rows here follow. **Will sign-off 2026-07-16 Telegram ("Yes rewire your routing"), surfaced by his own question about involving VULCAN.**
- **v0.17 (Jul 12):** *(Applied by DAEDALUS — registration edit for the 2026-07-12 HAWK war-agent split + HOMER promotion; Will authorized direct shared-file edits same-day. WALTER: review at next boot, adjust judgment freely — the row mechanics are yours.)* (1) **War-theater routing — OSPREY / FALCON** sub-section added: HAWK's two war theaters split into sibling agents (OSPREY = Russia/Ukraine, FALCON = US/Israel/Iran-Gulf); theater kinetic/infrastructure signals route to the theater owner, HAWK info-cc (synthesis); HAWK reclassified to cross-war synthesis + dormant book. `OIL_ENERGY` action → BRENT (backup HAWK — price/OPEC/refining lane; war-driven facility damage → theater owner per sub-section); `GEOPOL_ENERGY` action → theater owner (OSPREY/FALCON), backup HAWK. (2) **Housing routing — HOMER** sub-section added: HOMER promoted from CARL sub-agent to top-level housing domain agent (OZK/CORAL precedent); national housing asset-market/credit-structure signals → HOMER action (was split CARL/REGINALD); supersedes the Apr-20 Residential-housing exception's REGINALD-action default for asset-market signals (REGINALD stays info + keeps bank-collateral interpretation); FL-specific stays CORAL per v0.11. No FORMAT_SPEC domain-vocab change (existing codes reused; theater/housing split is within-domain routing, same pattern as v0.10).
- **v0.16 (Jun 28):** Added the `CLIMATE_MACRO` domain row (→ **AEOLUS** action) to the By Signal Domain table + a "Climate-macro routing — AEOLUS" sub-section. AEOLUS (climate→economy agent, built by DAEDALUS 2026-06-28) is the action owner for macro-climate signals with an economic-transmission channel (ENSO state, energy demand, ag/food, insurance/reinsurance, property/physical, supply-chain). Channel-specific info cc: HENRY (energy-demand/power/nat-gas), CARL (ag/food→consumer), BRENT (energy complex), SHADE (insurance/reinsurance), RED per tag rules; **CORAL** is backup + the FL handoff (reconcile FL climate to AEOLUS's one ENSO figure — same don't-silo pattern as CORAL/MARCO). FL-*specific* climate still routes CORAL-action per the v0.14 carve; pure climate-science with no economic channel still KILLS (Relevance). Pairs FORMAT_SPEC v0.12 (CLIMATE_MACRO domain code) + CLUSTER_TAXONOMY v0.3 (12th cluster). Will sign-off 2026-06-28 (Telegram). First signals: SIG-W-20260628-011/012.
- **v0.15 (Jun 27):** Added "Muni / state-local fiscal routing — CARL" sub-section after the Climate/ENSO carve. Muni / state-local public-finance signals (budget stress, pensions, muni-bond issuance/spreads/downgrades, deferred-infrastructure liabilities, property/sales-tax policy, data-center→muni fiscal-credit) route by transmission leg: **national → CARL action** (fiscal→consumer), **FL → CORAL action** (FL state fiscal + property-tax amendment), LIQUID info (muni-credit/spread), REGINALD info (bank muni holdings / state-fiscal→regional-bank), RED per tag rules, DEWEY `/deep-research` for on-demand depth. Closes the no-owner gap surfaced by SIG-W-20260627-024 (Ciccarone $1.03T deferred-infrastructure) **without a new agent** — muni-fiscal is a transmission channel feeding existing theses, not a standalone position; a persistent muni agent would add fleet-bloat + stale-row risk (RULE 4) for thin intake. No FORMAT_SPEC domain-vocab change. Will approved 2026-06-27 (Telegram).
- **v0.14 (Jun 26):** Added "Climate / hurricane-season / ENSO routing — CORAL" sub-section after the TERRY carve. Climate signals with a **Florida transmission channel** (ENSO/El-Niño state, Atlantic hurricane-season outlooks + in-season FL-landfall tracks, sargassum, FL flood/SLR/NFIP) route **CORAL action** / MARCO info (tourism) / REGINALD info (FL insurance→bank/fiscal) / RED per tag rules — closing the gap where basin-wide / not-FL-on-its-face climate forecasts were killed as off-axis climate. Pure climate-science with no FL-economic channel still KILLS (Relevance gate); storms threatening energy infra stay BRENT/HAWK. No FORMAT_SPEC domain-vocab change. Will approved 2026-06-26 (Telegram, "Enso coral yes").
- **v0.13 (Jun 22):** Added "Trade-construction info routing — TERRY" sub-section. TERRY (Tier-2 CC trade-construction desk, registered 2026-06-21) becomes an **info-only** recipient for **positioning / timing / reversion** signals (COT/net-spec extremes, RSI/overbought-oversold, dealer-gamma/vol-positioning, threshold-proximity) — the inputs that bear on trade *expression* (entry/expiry/sizing), not thesis. Narrow/conservative scope per Will (fires only when a live/candidate book trade's timing-structure-sizing is informed; omit otherwise). Never on the action line; no FORMAT_SPEC change. Will lean 2026-06-22 ("only timely trading information… oil shorts… semiconductor RSI reversion").
- **v0.12 (Jun 22):** Added "National CRE / CMBS market-stress routing — CREED" sub-section after the Florida-CORAL carve. CREED (revived 2026-06-21) is the national CRE/CMBS market-stress specialist; national CRE-market-structure signals (CMBS DQ/special-servicing, maturity-wall, CRE funds/shadow-NAV/forced-sale, REIT CRE tape, non-FL multifamily) now route **CREED action** / REGINALD info (bank-transmission handoff) / BROCK info (securitized-credit overlap). Splits the *market-structure* side out of REGINALD's `BANK_CRE` row — same specialist-carve pattern as the CORAL promotion; bank CRE *exposure* (loan books, MI3, NDFI, capital rules, provisions) stays REGINALD-action, FL-specific stays CORAL. No FORMAT_SPEC domain-vocab change. Will approved 2026-06-22 (Telegram).
- **v0.11 (Jun 19):** Added "Florida-specific routing — CORAL" sub-section after the Residential-housing exception. CORAL was promoted from a REGINALD sub-agent to a top-level Florida peer agent on 2026-06-19; Florida-specific signals (FL real estate / FL banks / FL insurance / FL migration-tourism / FL fiscal) now route **CORAL action** / REGINALD info (bank-collateral integration) / CARL info (consumer) / MARCO info (migration-tourism co-ownership), superseding the Apr-20 Residential-housing exception **for Florida only** (non-FL geo-narrow residential still → REGINALD action per that exception). Geographic routing override, same pattern as the Apr-20 residential carve — no FORMAT_SPEC domain-vocab change. Proposed by WALTER at 2026-06-19 dispatch (SIG-W-20260619-002 routed CORAL-action ahead of the formal row); Will approved 2026-06-19.
- **v0.10 (Jun 10):** Split the bundled `MARKET_VOL` row per the HENRY/VIOLET vol-ownership decision (auto-memory `feedback_henry_vol_broadcast_to_violet`: VIOLET owns vol-regime broadcast; HENRY keeps gamma/0DTE/put-wall). Vol-regime / VIX-complex / term-structure content → VIOLET action (HENRY backup); dealer-gamma / 0DTE / index-move mechanics → HENRY action (unchanged). Single `MARKET_VOL` domain code retained (no FORMAT_SPEC change — within-domain routing split, same pattern as Apr 20 residential-housing exception). Proposed by VIOLET via SIGNAL_INTAKE.md rebuild Appendix A flag (2026-06-10); Will approved 2026-06-10.
- **v0.9 (May 11):** Added "By Convergence" section after By Boundary Threshold — auto-fire `signal_type: convergence_event` to REGINALD-action when BOARD INDEX scan finds N≥2 prior signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern. Detection via CROSS_REFS/REGINALD.md §1 watchlist + §5 pattern keys. Per REGINALD ↔ WALTER LIAISON Q5 (Turn 1 → Turn 4 LOCK 2026-05-11). v0.9 stack candidate `bank_transmission` enum (8-val: cre / hidden_cre / ndfi / private_credit / mfs_fraud / cmbs_maturity / fed_layoffs / stagflation_trap) pre-cosigned in V0_9_STACK.md tracker for batched FORMAT_SPEC v0.9 ship.
- **v0.8 (May 8):** Added "By Boundary Threshold" section after By Tag/By Verdict — 8-row BRENT-IMMEDIATE threshold-cross dispatch list per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c (3-way cosigned BRENT+CARL+WALTER 2026-05-05/06; Will sign-off 2026-05-08). Adds threshold-cross row mechanics: single-day breach = watch (no dispatch); 2-3 sess sustained = dispatch; single-print operational minima (#3 Cushing) = dispatch on print itself; re-fire convention (only on re-cross of boundary in either direction, not on continued state). BRENT-fire-as-primary; WALTER-fire-as-fallback if BRENT >5d STATUS lag. Detection via FORGE/tools/market-data + EIA scheduled scans (per §2b Phase 2 dependency). Updated By Tag/By Verdict section to reference v0.8 canonical `signal_role: cluster_mediating` form, retiring v0.7 prose-tag interim discipline.
- **v0.7 (May 6 PM):** Added "By Tag/By Verdict" section after By Signal Type table — three rules (cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`) + de-dupe rule + interim prose-tag discipline (pre-v0.8). Per RED ↔ WALTER LIAISON Q9-Q12 + JOINT_PROPOSAL_2026-05-06_red_walter §3 (Will sign-off 2026-05-06).
- **v0.6 (May 6):** Added "Iran-cluster CARL-info override" section after Residential-housing exception. Iran-cluster signals (cluster: IRAN_HORMUZ) route CARL info ONLY on concrete Brent thresholds (≥$110 sustained 2 sess OR ≤$95 sustained 5 sess) OR explicit kinetic event with supply-disruption mechanism OR FX/macro cross with consumer-burden vector. Posture/doctrine/diplomatic-cascade/OSINT signals → drop CARL. Added boundary-trigger threshold-cross dispatch sub-rule (≤$95/5sess and ≥$115/5sess fire IMMEDIATE → CARL with KB-CARL-259 + Vector #5/#12 + CRL-08 cross-refs). Per CARL ↔ WALTER LIAISON Q3 2026-05-05. **BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred pending Will sign-off on JOINT_PROPOSAL §2c.**
- **v0.5 (Apr 20):** Added `thesis-frame` row to By Signal Type table (matches FORMAT_SPEC v0.5 enum add). Added "Residential-housing stress exception" note under By Signal Domain table — geographically-narrow residential signals route REGINALD action / CARL info, not the reverse. Rule filed Apr 20 2026 after Will corrected a default-CARL routing for NV HOA SIG-W-20260420-005. Part of Filter v2 Segment A.
- **v0.4 (Apr 14):** Added ASIA_CONTAGION + UST_FOREIGN rows (ZHAO primary) to match FORMAT_SPEC v0.4. Closes vocabulary gap surfaced by 2026-04-14 FT China-trade signals (SIG-W-20260414-010/011).
- **v0.3 (Apr 11 PM):** Re-labeled all rows with canonical domain codes (LABOR, MACRO_INFLATION, etc.) to match FORMAT_SPEC v0.3 Domain Vocabulary. Resolves Gap C vocabulary drift.
- **v0.2 (Apr 11 AM):** Added MACRO_INFLATION, TARIFF_TRADE, GEOPOL_NON_ENERGY, PRIVATE_CREDIT rows + Backup column.
- **v0.1 (Apr 7):** Initial version.

---

## By Signal Domain

| Domain code | Row description | Action | Backup | Info Recipients | Default Precedence | Default Group |
|-------------|-----------------|--------|--------|-----------------|-------------------|---------------|
| `LABOR` | Employment — NFP, claims, JOLTS, wages, U-3, LFPR | CARL | HENRY | HENRY, RED | IMMEDIATE (data day) / PRIORITY (analysis) | LABOR_DOWNSTREAM |
| `MACRO_INFLATION` | Inflation + growth — CPI, PCE, PPI, UMich, GDP, ISM, retail sales | CARL | HENRY | HENRY, LIQUID, RED | IMMEDIATE (data day) / PRIORITY (analysis) | THESIS_CORE |
| `TARIFF_TRADE` | Executive orders, tariff changes, trade deals | CARL | HENRY | HENRY, REGINALD, RED, MARCO | IMMEDIATE (announcement) / PRIORITY (analysis) | THESIS_CORE |
| `CONSUMER_CREDIT` | CC/auto/student loan delinquency, household debt | CARL | REGINALD | REGINALD, RED | PRIORITY | THESIS_CORE |
| `BANK_CRE` | Bank earnings, CRE, hidden CRE (MI3), NDFI, capital rules | REGINALD | BROCK | BROCK, LIQUID, RED | IMMEDIATE (earnings) / PRIORITY (research) | CREDIT_CHAIN |
| `FUNDING_LIQUIDITY` | HY OAS, SOFR, repo, RRP, dealer capacity, Treasury auctions | LIQUID | HENRY | BROCK, SHADE, HENRY | IMMEDIATE (stress) / PRIORITY (monitoring) | CREDIT_CHAIN |
| `PRIVATE_CREDIT` | BDC gates, PC fund redemptions, PIK rates, software PE, PCDR | BROCK | SHADE | LIQUID, REGINALD, RED | PRIORITY | CREDIT_CHAIN |
| `INSURANCE_SHADOW` | PE-insurer nexus, reinsurance, Level 3, captive insurers | SHADE | BROCK | LIQUID, BROCK | PRIORITY | — |
| `OIL_ENERGY` | Crude prices, OPEC, refining, shipping (war-driven facility damage → theater owner, v0.17 sub-section) | BRENT | HAWK | HAWK, RED | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_ENERGY` | War-theater kinetic/infra/chokepoints — Russia/Ukraine → OSPREY; Iran/Gulf (Hormuz, Bab-al-Mandab) → FALCON (v0.17 sub-section) | OSPREY / FALCON (by theater) | HAWK | HAWK, BRENT, SAM | PRIORITY | ENERGY_CHAIN |
| `GEOPOL_NON_ENERGY` | Ceasefires, diplomacy, nuclear, war outside supply | HANS (Tier 2 — spawn) | HAWK | HAWK, BRENT, SAM, RED | PRIORITY | — |
| `JAPAN_BOJ` | USD/JPY, BOJ policy, JGB yields, carry trade, MOF intervention | SAM | LIQUID | LIQUID, RED | IMMEDIATE (intervention) / PRIORITY (monitoring) | — |
| `MARKET_VOL` (vol-regime) | VIX complex, vol regime, term structure, VVIX, SKEW, vol ETP stress, vol-targeting/CTA flows | VIOLET | HENRY | HENRY, LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `MARKET_VOL` (index-mechanics) | Index moves, dealer gamma, 0DTE, put-wall, correlation breaks | HENRY | LIQUID | LIQUID, RED | IMMEDIATE (spike) / PRIORITY (trend) | — |
| `ASIA_CONTAGION` | China/HK peg, LGFV, HIBOR-SOFR, Chinese trade policy, supply-chain coercion, export-control regs, EM Asia spillover | ZHAO (Tier 2 — spawn) | SAM | RED, HENRY, LIQUID, BRENT/HAWK (when rare-earths), PROME | PRIORITY (policy/research) / IMMEDIATE (CNY intervention, LGFV event) | — |
| `UST_FOREIGN` | TIC flows, foreign UST holder behavior, auction demand composition | ZHAO (Tier 2 — spawn) | BOND (Tier 2) | LIQUID, HENRY, RED | IMMEDIATE (TIC release day) / PRIORITY (composition shifts) | CREDIT_CHAIN |
| `CLIMATE_MACRO` | Macro climate→economy — ENSO/El-Niño state, energy demand (heat/cooling/power-burn), ag/food, insurance/reinsurance, property/physical, supply-chain/logistics | AEOLUS | CORAL | HENRY, CARL, BRENT, SHADE, RED (per channel) | PRIORITY (forecast/structural) / IMMEDIATE (acute landfall / grid / crop-loss event) | CLIMATE |
| `AI_CAPEX` | AI-infra capex **substance** — hyperscaler capex guidance/concentration, datacenter buildout, semis + memory cycle, capex→power-demand, AI supply-chain/export-controls. **NOT the financing leg** (→ `PRIVATE_CREDIT`/`FUNDING_LIQUIDITY`; see sub-section below) | VULCAN | HENRY | VIOLET, HENRY, WATT, RED | PRIORITY (guidance/research) / IMMEDIATE (a capex CUT — VULCAN's not-yet-fired gate) | AI_INFRA |
| `POWER_GRID` | Grid stress → power price → power cost — grid emergencies/EEA, spark spreads, capacity auctions, interconnect queue, utility rate cases, on-site generation | WATT | HENRY | HENRY, CARL, VULCAN, AEOLUS, RED | PRIORITY (rate case / capacity auction / structural) / IMMEDIATE (acute grid emergency) | POWER |
| `METALS` | Metals as macro tells — monetary (gold/silver/GSR, CB buying, ETF flows) + industrial (copper/PGM, LME/COMEX inventories, backwardation) | MIDAS | LIQUID | LIQUID, HENRY, BOND, RED | PRIORITY | METALS |

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

### Trade-construction info routing — TERRY (Jun 22 2026)

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

**What still KILLS (Relevance gate — no near-term FL insurance/RE/tourism/fiscal transmission):** pure climate-science with no FL-economic channel — global temperature anomalies, paleoclimate, geomagnetic/solar, IPCC structural-ocean findings, non-Atlantic-basin activity, generic "climate risk" macro takes. (These are the off-axis-climate kills — e.g., the 2026-06-26 geomagnetic-dipole / global-temp-anomaly / Atlantic-warming-hole / AI-data-center-water items.) The discriminator is **a concrete FL-economic transmission channel within the thesis horizon**, not the word "climate."

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

| Signal Type | Default Precedence | Upgrade Condition |
|-------------|-------------------|-------------------|
| `threshold-crossed` | IMMEDIATE | → FLASH if position directly affected |
| `pattern-match` | PRIORITY | → IMMEDIATE if convergence (2+ agents flagging same theme) |
| `thesis-frame` | PRIORITY | Stays PRIORITY. Can upgrade to IMMEDIATE only if the synthesis/framework directly changes position sizing or catalyst read (rare — most thesis-frame content is analytical context, not threshold breach). |
| `catalyst` | IMMEDIATE | → FLASH if pre-written framework exists and threshold met |
| `divergence` | IMMEDIATE | Always IMMEDIATE minimum |
| `research` | PRIORITY | Stays PRIORITY unless thesis-critical finding |
| `position-risk` | IMMEDIATE | → FLASH if stop-loss or margin proximity |
| `context` | ROUTINE | Stays ROUTINE unless safety net triggers |
| `manual-flag` | PRIORITY | Follows Will's specified urgency if given |

---

## By Tag/By Verdict (NEW v0.7)

Augments the By Signal Domain and By Signal Type tables. Applies AFTER domain + signal_type routing has been determined. Adds RED to the info line when specific tag/verdict conditions fire — adversarial overlay needs visibility into bifurcation-state and corrected-framing dispatches without requiring separate signals. Falsification-trigger rule additionally turns WALTER into an auto-dispatcher when pre-registered RED thresholds cross.

| Tag/Verdict | Rule | De-dupe behavior |
|-------------|------|------------------|
| `signal_role: cluster_mediating` (v0.8 canonical) OR legacy `cluster_mediating: true` boolean | Add **RED** to info line unconditionally regardless of domain. **v0.19: also add NEXUS to info** — FORMAT_SPEC v0.8 gives NEXUS **authoritative-voice precedence on this exact tag** (*NEXUS > WALTER (tagger) > action-primary*) and says **NEXUS owns cluster-narrative-update interpretation**. Until v0.19 the tag routed to RED but **not to the agent that owns it** — NEXUS could be out-voiced on a call the spec assigns it, on a signal it never received. | If RED/NEXUS already in to/info, no add; stays at one occurrence |
| **v0.19 — signal bears on a registered NEXUS prediction** (`PRED-NN` in `AGENTS/NEXUS/PREDICTIONS_MONITOR.md`): the signal **resolves / partially resolves / materially counter-evidences** a row, OR the row's named resolution route points at this signal's subject | **NEXUS = ACTION** (not info). A registered prediction moving off its mark is an **owner re-mark**, which is action by definition | If NEXUS already action, no change; if already info, **promote to action** |
| `verify_research_verdict: CORRECTED-FRAMING` (in dispatch_note) | Add RED to info line | If RED already in to/info, no add; stays at one occurrence |
| `falsification_trigger: <RED-FT-NN>` (auto-fired by WALTER from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` per JOINT_PROPOSAL §2 eval logic) | Action = trigger.recipient_chain.action; Info = trigger.recipient_chain.info; precedence per trigger.action enum mapping (IMMEDIATE-FALSIFY/PATH-B-CONFIRM/ADD-POSITION/etc.) | n/a — auto-generated signal, recipient chain pre-determined per FALSIFICATION_TRIGGERS row |

**De-dupe rule (general):** when multiple v0.7 rules fire on the same dispatch (e.g., signal is both `cluster_mediating: true` AND CORRECTED-FRAMING), RED is added once. Composition is informative-only; consumption mode (full-read for cluster_mediating vs body-skim for CORRECTED-FRAMING per RED CLAUDE.md boot-step 1.5 b3/b4) is RED's choice at boot.

### Interim period (pre-v0.8)

`cluster_mediating: true` is a v0.8 field (pending Will sign-off on JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a). Until v0.8 lands, the prose-tagged equivalent is dispatch_note language carrying "paper-vs-structural" / "tape-vs-substance" / "bifurcation" / "divergence" tokens. Interim WALTER discipline:

> When dispatch_note contains paper-vs-structural / tape-vs-substance / bifurcation / divergence framing, ensure RED in info line.

This carries the v0.7 rule operationally before the field formally exists. RED's bifurcation classification TSV (LIAISON Turn 5 deliverable, `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv`) seeds the historical pass; new prose-tagged signals from this point forward apply the rule.

### Composition example

SIG-W-20260505-012 (Brent intraday tape divergence vs Iran cluster confluence) — cluster_mediating + (would have been) CORRECTED-FRAMING if verdict run. Under v0.7 rules: RED auto-cc once; dispatch_note flags both rule-fires explicitly so RED knows the routing rationale; consumption mode = full-read (cluster_mediating dominates over body-skim).

### Why this is here, not in FORMAT_SPEC

`cluster_mediating` is a FORMAT_SPEC field; CORRECTED-FRAMING is a CHECKLIST verdict; falsification_trigger is a generated body field. The recipient-augmentation behavior is a routing decision — it belongs in this table per the canonical-source lookup in `WALTER/CLAUDE.md` ("Domain → recipient routing rules" → ROUTING_TABLE owns).

---

## By Boundary Threshold (NEW v0.8)

Augments the By Signal Domain table with explicit threshold-cross dispatch rows for BRENT's 8-row IMMEDIATE list per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c (BRENT+CARL+WALTER 3-way cosigned 2026-05-05/06; Will sign-off 2026-05-08). Threshold-cross signals carry `signal_type: threshold-crossed` + boundary-row reference in dispatch_note (e.g., `boundary: §2c-row-1`).

Distinct from the boundary-trigger CARL-side rule under "Iran-cluster CARL-info override" (Brent ≤$95×5sess and ≥$115×5sess fire IMMEDIATE → CARL): THIS section codifies the BRENT-action 8-row list at finer thresholds with broader cross-recipient routing.

| # | Threshold | Precedence | Action → Info | Cadence |
|---|-----------|------------|---------------|---------|
| 1 | **Brent close ≥ $120 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, SAM, HAWK, RED | 2-3 sess sustained = dispatch |
| 2 | **Brent close ≤ $75 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, RED | 2-3 sess sustained = dispatch |
| 3 | **Cushing < 20M bbl single print** | IMMEDIATE | BRENT → LIQUID, HENRY, RED | Single print = dispatch (operational minimum, WTI dislocation risk) |
| 4 | **HY Energy OAS > 400bps** | IMMEDIATE | BRENT → LIQUID-cross-feed (LIQUID may want primary depending on broader-credit context — flag at dispatch) | 2-3 sess sustained = dispatch |
| 5 | **VLCC Worldscale ≥ 2× trailing 30-day median sustained** | PRIORITY | BRENT → HAWK, SAM, RED | Sustained-cross-from-baseline (≥3 sess) — operational definition avoids absolute-threshold drift in war-risk-elevated baseline |
| 6 | **Gasoline crack — re-cross from <$30 back ≥$30 OR single-day spike ≥$50** | IMMEDIATE | BRENT → CARL, HENRY, RED | Threshold-cross logic only; standing $42 baseline = no fresh dispatch. Inverse extremum captures demand-destruction-via-crack-collapse OR refinery-substitution-exhausted scenarios |
| 7 | **US oil rigs +50 from 408 trough** | PRIORITY | BRENT → CARL (capex/wage), HENRY, RED | 2-3 sess sustained = dispatch |
| 8 | **Brent 3:2:1 crack > $50/bbl** | IMMEDIATE | BRENT → CARL (refining-margin pass-through), HENRY, REGINALD (refinery-bank) | 2-3 sess sustained = dispatch |

### Cadence convention (locked)

- **Single-day breach** = watch (no dispatch)
- **2-3 sessions sustained** = dispatch
- **Single-print operational minima** (#3 Cushing): dispatch on the print itself
- **Re-fire convention:** after initial cross, no re-fire on continued state; only on re-cross of boundary in either direction. Sustained-above-#1 stays one signal until it falls back below or escalates further to a higher threshold.

### Detection responsibility

- **WALTER:** monitors price/spread/inventory data via FORGE/tools/market-data + EIA/Baker Hughes scheduled scans (per JOINT_PROPOSAL §2b — Phase 2 dependency, calendars not yet landed at v0.8 ship)
- **BRENT:** mirrors via own data tools and STATUS refresh (BRENT self-task: PREDICTIONS.tsv BRT-04/BRT-08/BRT-15 cross-refs to these row numbers)
- **Convention:** BRENT-fire-as-primary on threshold-cross dispatches; WALTER-fire-as-fallback if BRENT stale (>5d STATUS lag)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — a threshold-crossed signal with `signal_role: cluster_mediating` AND CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence.
- Safety Net Auto-Upgrades below still apply — VIX>30 or HY OAS +25bps single session can override boundary-threshold precedence to FLASH.

### Q-trail

BRENT LIAISON Q4 (BRENT→WALTER, Turn 1, 8-row list proposed) → WALTER Turn 2 ACCEPT-WITH-REDLINES (#5 PRIORITY-not-IMMEDIATE; #6 standing-state-not-fresh-dispatch) → BRENT Turn 3 ACCEPT (with #5 ≥2× median definition + #6 dual-extremum >$50 inverse trigger) → WALTER Turn 4 LOCK → Will sign-off 2026-05-08.

---

## By Convergence (NEW v0.9)

Augments By Signal Domain + By Signal Type + By Tag/By Verdict + By Boundary Threshold sections. Applies AT DISPATCH after all other routing decisions. **Trigger:** when BOARD INDEX scan (cluster sections preferred for speed) finds N≥2 prior signals within 5-session window referencing the same bank ticker OR the same multi-channel exposure pattern, auto-fire `signal_type: convergence_event` precedence IMMEDIATE override.

### Rule

| Detection condition | Action | Recipient chain |
|---------------------|--------|-----------------|
| N≥2 prior BOARD signals within 5-session window mention same bank ticker (from `design/CROSS_REFS/REGINALD.md` §1 watchlist: TIER-1 / TIER-2 / NEW-TRACKING / EXTERNAL-WATCH tiers) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** |
| N≥2 prior BOARD signals within 5-session window touch same cross-bank pattern key (from `design/CROSS_REFS/REGINALD.md` §5: `cohort_fade_pattern` / `fhlb_bifurcation` / `provisions_mask_deterioration` / `office_single_point_concentration` / `hidden_cre_relabeling_trajectory` / `mi3_rcon2746_screen` / `ndfi_breakout_decomposition`) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** (cohort-level convergence is RED-watchable as a structural-bifurcation candidate) |

### Detection mechanics

- **At dispatch:** scan BOARD INDEX cluster sections (filtered to BANK_COLLATERAL + PC_STRESS + FED_FRAMEWORK + CONSUMER_STAGFLATION primary; expand secondary on bank-ticker hit) for prior 5-session window
- **Lookup:** use CROSS_REFS/REGINALD.md §1 ticker → watchlist row mapping + §5 pattern key list (denormalized cache, grep-speed at dispatch)
- **Cost:** cluster-filtered grep ~50-200ms per dispatch
- **Volume estimate:** ~1-2 convergence_events per week at current dispatch volume; peaks during Q1 earnings windows + threshold-cross windows

### dispatch_note format

When convergence_event fires, include in dispatch_note:

- **Prior signals (count + IDs + cluster + date):** e.g., `Convergence: SIG-W-20260420-008 (BANK_COLLATERAL, 4/20) + SIG-W-20260424-005 (BANK_COLLATERAL, 4/24) + SIG-W-20260426-009 (BANK_COLLATERAL, 4/26) — 3 signals in 6 sessions on office-distress + WAL/MTB ticker overlap`
- **Convergence type:** ticker-convergence vs pattern-key-convergence (or both)
- **Channel codes touched** (from REGINALD's 8-channel framework): e.g., `Channels: cre,hidden_cre,cmbs_maturity`
- **Cluster-mediating tag:** if convergence spans multiple clusters, set `cluster_mediating: true` + tag `cluster_secondary` per FORMAT_SPEC v0.7+

### De-dupe behavior

- If `cluster_mediating: true` already fires on the trigger signal (per v0.7 By Tag/By Verdict), convergence_event composition adds RED **once** (no double-count of RED-info)
- If multiple convergence_event triggers fire on same dispatch (e.g., signal hits both ticker-convergence AND pattern-key-convergence), single convergence_event dispatched with both reasons listed in dispatch_note
- If incoming signal IS the 2nd-or-later signal that COMPLETES a convergence window, dispatch fires from incoming-signal-dispatch side; prior signals stay at their original precedence (not retroactively re-dispatched)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — convergence_event signal with `signal_role: cluster_mediating` + CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence
- v0.8 By Boundary Threshold still applies — if convergence_event also crosses a BRENT-IMMEDIATE row (e.g., Brent ≥$120 sustained 3 sessions), BRENT row recipient chain composes with REGINALD primary; precedence stays IMMEDIATE (highest)
- Safety Net Auto-Upgrades still apply — VIX>30 or HY OAS +25bps single session can compose with convergence_event (precedence already IMMEDIATE; multi-trigger composition surfaces in dispatch_note)

### Examples (illustrative — not historical dispatch)

**Ticker convergence example:** signal SIG-W-20260512-NNN mentions WAL. WALTER greps BOARD INDEX for prior 5-session window — finds SIG-W-20260507-004 (Sternlicht-Starwood CMBS) mentions WAL + SIG-W-20260508-011 (FWRD covenant default) mentions WAL bank-covenant pattern. N=3 within 5 sessions → convergence_event fires; recipient chain REGINALD action / BRENT info / RED info. dispatch_note: `Convergence (ticker): SIG-W-20260507-004 + SIG-W-20260508-011 + (current) — 3 signals in 5 sessions on WAL; channels: cre,cmbs_maturity,private_credit`.

**Pattern-key convergence example:** signals across 4 sessions all touch `cohort_fade_pattern` (REGINALD's structural framework) — VLY provisions tell + CFG cohort-fade signal + WAL ex-fraud NCO read. Even though no single ticker repeats N≥2, pattern-key fires same convergence_event mechanics. RED-info important here because cohort-level convergence is bifurcation candidate.

### Q-trail

REGINALD LIAISON Q5 (REGINALD → WALTER, Turn 1, framework proposed) → WALTER Turn 2 DECISION (YES, build atop named-entity grep from Q3) → REGINALD Turn 3 LOCK (preference: ROUTING_TABLE v0.9 section, not standalone) → WALTER Turn 4 SHIP (this section).

---

## Safety Net Auto-Upgrades

These conditions override the routing table and force minimum IMMEDIATE precedence:

| Trigger | Detection Method | Upgrade To |
|---------|-----------------|------------|
| VIX > 30 (or +5 intraday) | Market data check | IMMEDIATE minimum |
| HY OAS widening > 25bps single session | Market data check | IMMEDIATE minimum |
| Held-position liquidity drop | Bid-ask spread monitoring | FLASH |
| 2+ agents flag same theme in 24h | Signal correlation | IMMEDIATE + flag convergence |
| Correlation break (r drops >0.3 in correlated pair) | Statistical check | IMMEDIATE minimum |

---

## Escalation Paths

Receiving agents can request WALTER re-route at higher precedence:

| Scenario | Agent Action | WALTER Response |
|----------|-------------|-----------------|
| Agent finds signal more urgent than classified | Writes to WALTER outbox: "ESCALATE SIG-W-YYYYMMDD-NNN to IMMEDIATE" | WALTER re-routes to broader group at higher precedence |
| Agent identifies cross-domain relevance | Writes to WALTER outbox: "ROUTE SIG-W-YYYYMMDD-NNN to AGENT (ACTION)" | WALTER sends copy to new recipient |
| Agent flags false positive | Writes to WALTER outbox: "REJECT SIG-W-YYYYMMDD-NNN — reason" | WALTER logs rejection, stops further routing |

---

## MINIMIZE Routing Adjustments

During MINIMIZE, routing table precedence thresholds shift:

| MINIMIZE Level | ROUTINE Signals | PRIORITY Signals | IMMEDIATE Signals | FLASH Signals |
|---------------|-----------------|------------------|-------------------|---------------|
| **Normal** | Route normally | Route normally | Route normally | Route normally |
| **MINIMIZE-1** | Queue in WALTER | Route normally | Route normally | Route normally |
| **MINIMIZE-2** | Queue in WALTER | Queue in WALTER | Route normally | Route normally |
| **MINIMIZE-3** | Queue in WALTER | Queue in WALTER | Queue in WALTER | Route normally |

---

*v0.16 — Jun 28, 2026 (CLIMATE_MACRO domain row → AEOLUS action added to By Signal Domain + "Climate-macro routing — AEOLUS" sub-section after the Muni carve; channel-specific info cc HENRY/CARL/BRENT/SHADE/RED, CORAL backup + FL-handoff reconcile-don't-silo; FL-specific climate stays CORAL [v0.14], pure-climate-science with no economic channel still KILLS; pairs FORMAT_SPEC v0.12 CLIMATE_MACRO domain code + CLUSTER_TAXONOMY v0.3 12th cluster; Will sign-off 2026-06-28 Telegram) | v0.15 — Jun 27, 2026 (Muni / state-local fiscal routing — CARL sub-section added after the Climate/ENSO carve — muni/state-local public-finance signals [budget stress, pensions, muni-bond issuance/spreads/downgrades, deferred-infrastructure liabilities, property/sales-tax policy, data-center→muni fiscal-credit] route by transmission leg: national → CARL action [fiscal→consumer] / FL → CORAL action [FL state fiscal + property-tax amendment] / LIQUID info [muni-credit/spread] / REGINALD info [bank muni holdings / state-fiscal→regional-bank] / RED per tag rules / DEWEY for on-demand depth; closes the no-owner gap surfaced by SIG-W-20260627-024 [Ciccarone $1.03T deferred-infrastructure] WITHOUT a new agent — muni-fiscal is a transmission channel feeding existing theses not a standalone position, a persistent muni agent = fleet-bloat + stale-row risk RULE 4 for thin intake; no FORMAT_SPEC domain-vocab change; Will approved 2026-06-27 Telegram) | v0.14 — Jun 26, 2026 (Climate / hurricane-season / ENSO routing — CORAL sub-section added after the TERRY carve — climate signals with a Florida transmission channel [ENSO/El-Niño state, Atlantic hurricane-season outlooks + in-season FL-landfall tracks, sargassum, FL flood/SLR/NFIP] → CORAL action / MARCO info [tourism] / REGINALD info [FL insurance→bank/fiscal] / RED per tag rules; closes the gap where basin-wide/not-FL-on-its-face climate forecasts were killed as off-axis climate; pure climate-science with no FL-economic channel still KILLS [Relevance gate]; energy-infra storms stay BRENT/HAWK; no FORMAT_SPEC domain-vocab change; Will approved 2026-06-26 Telegram "Enso coral yes") | v0.13 — Jun 22, 2026 (Trade-construction info routing — TERRY sub-section added after the CREED carve — TERRY [Tier-2 CC trade-construction] becomes info-only recipient for positioning/timing/reversion signals [COT/net-spec extremes, RSI/overbought-oversold, dealer-gamma/vol-positioning, threshold-proximity] that bear on trade expression; narrow/conservative scope, never action-line, no FORMAT_SPEC change; Will lean 2026-06-22 "only timely trading information / oil shorts / semiconductor RSI reversion") | v0.12 — Jun 22, 2026 (National CRE/CMBS market-stress routing sub-section added after the Florida-CORAL carve — national CRE-market-structure signals [CMBS DQ/special-servicing, maturity-wall, CRE funds/shadow-NAV/forced-sale, REIT CRE tape, non-FL multifamily] → CREED action / REGINALD info [bank-transmission handoff] / BROCK info [securitized-credit overlap]; splits the market-structure side out of REGINALD's BANK_CRE row, mirroring the CORAL specialist-carve; bank CRE exposure stays REGINALD, FL-specific stays CORAL; CREED revived+registered 2026-06-21; Will approved 2026-06-22 Telegram) | v0.11 — Jun 19, 2026 (Florida-specific routing sub-section added after the Residential-housing exception — FL-specific signals → CORAL action / REGINALD info [bank-collateral integration] / CARL info [consumer] / MARCO info [migration-tourism co-ownership]; supersedes the Apr-20 Residential-housing exception for Florida only [non-FL geo-narrow residential unchanged → REGINALD]; CORAL promoted REGINALD-sub-agent → top-level FL peer 2026-06-19; geographic routing override, no FORMAT_SPEC domain-vocab change; WALTER routed SIG-W-20260619-002 CORAL-action ahead of the row, Will approved 2026-06-19) | v0.10 — Jun 10, 2026 (MARKET_VOL row split into vol-regime → VIOLET action / index-mechanics → HENRY action per HENRY/VIOLET vol-ownership decision; gamma-flip-event VIOLET-info boundary rule; single domain code retained; proposed by VIOLET SIGNAL_INTAKE Appendix A flag, Will approved 2026-06-10) | v0.9 — May 11, 2026 (By Convergence section added after By Boundary Threshold per REGINALD ↔ WALTER LIAISON Q5 — auto-fire convergence_event IMMEDIATE to REGINALD action + RED info on N≥2 prior signals within 5-session window referencing same bank ticker OR same multi-channel exposure pattern; detection via CROSS_REFS/REGINALD.md §1 watchlist + §5 pattern keys; dispatch_note format + de-dupe behavior + composition with other rules locked; bank_transmission enum 8-val pre-cosigned in V0_9_STACK.md tracker for batched FORMAT_SPEC v0.9 ship; REG LIAISON Q5 LOCK Turn 4 2026-05-11) | v0.8 — May 8, 2026 (By Boundary Threshold section added after By Tag/By Verdict per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c — 8-row BRENT-IMMEDIATE threshold-cross dispatch list; cadence convention locked single-day=watch / 2-3 sess sustained=dispatch / single-print operational minima dispatch on print / re-fire only on boundary re-cross; BRENT-fire-as-primary, WALTER-fire-as-fallback if BRENT stale >5d; By Tag/By Verdict cluster_mediating row updated to reference v0.8 canonical `signal_role: cluster_mediating` form retiring v0.7 prose-tag interim discipline; Will sign-off 2026-05-08) | v0.7 — May 6, 2026 PM (By Tag/By Verdict section added after By Signal Type per RED ↔ WALTER LIAISON Q9-Q12 + JOINT_PROPOSAL_2026-05-06_red_walter §3 — three rules: cluster_mediating auto-cc to RED, CORRECTED-FRAMING auto-cc to RED, falsification_trigger auto-fire from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`; de-dupe rule + interim prose-tag discipline pre-v0.8; Will sign-off 2026-05-06) | v0.6 — May 6, 2026 (Iran-cluster CARL-info override section added per CARL ↔ WALTER LIAISON Q3 — concrete Brent thresholds replace heuristic "near $110" framing; boundary-trigger threshold-cross dispatch sub-rule added for CARL-side ≤$95/5sess and ≥$115/5sess crosses; BRENT-IMMEDIATE 8-row "By Boundary Threshold" section deferred pending Will sign-off on JOINT_PROPOSAL §2c) | v0.5 — April 20, 2026 (thesis-frame signal_type row added per FORMAT_SPEC v0.5; Residential-housing stress exception section added per Filter v2 Segment A — geo-narrow residential → REGINALD action not CARL) | v0.4 — April 14, 2026 (ASIA_CONTAGION + UST_FOREIGN rows added per FORMAT_SPEC v0.4) | v0.3 — April 11, 2026 PM (canonical domain codes applied, Gap C resolved) | v0.2 — April 11, 2026 AM (rows + backup column) | v0.1 — April 7, 2026*
