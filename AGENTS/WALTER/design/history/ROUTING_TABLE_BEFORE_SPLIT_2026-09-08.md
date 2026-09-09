# WALTER Routing Table v0.31

Default routing rules. WALTER uses this table to determine recipients and precedence when classifying incoming information. These are defaults — WALTER can override based on context, safety net triggers, or MINIMIZE state.

> **📌 OWNER-OF-RECORD FOR ROUTING & DELIVERY FACTS (added v0.23, 2026-08-07 — Will-accepted RAV roster plan Part D, via PROME 2026-08-05).** **This table + `AGENTS/WALTER/REGISTRY.tsv` are the single owner-of-record for every routing and delivery fact about an agent** — who receives what, at what precedence, on which chain, and through which delivery lane. **`PROME/ROSTER.md` POINTS here and restates nothing**; where ROSTER and these two surfaces disagree, **these win**, and the fix belongs here. ROSTER's five descriptive classes (ORGANIZING/SERVICE · REVIEW/QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST) are **descriptive only and change no routing, precedence or delivery obligation** — do not read a class label as a routing input. *(`REGISTRY.tsv` is a bare TSV with a machine-parsed header row and cannot carry a prose statement without breaking its readers, so the statement lives here and in `WALTER/CLAUDE.md`'s KEY DESIGN FILES row.)*

**Canonical domain vocabulary:** The `Domain` column uses codes from `SIGNAL_FORMAT_SPEC.md` Domain Vocabulary section (v0.3, Apr 11). Don't invent new domain codes here without updating FORMAT_SPEC first per the canonical-source rule in `WALTER/CLAUDE.md`.


**Version history → [`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** (v0.1 → v0.31, moved verbatim 2026-08-30; `git log -p -- AGENTS/WALTER/design/ROUTING_TABLE.md` is the other copy). **Current: v0.31 (Aug 26)** — §3.5.5's non-renewable falsifier FIRED, TERRY reverted to the RED-class exemption.

> **📏 SIZE RE-TRIGGER — A DATED CONDITION, NOT A CLAIM OF LEANNESS.** Split 2026-08-30, when this file was **121,557 B = 224% of the 54,250 B read cap** (sha256 `8c4d77417a26`, 637 lines) as a boot-mandated WHOLE read. **~30 KB of that was version history and a single 6,672-byte trailing changelog line — a changelog inside a boot read.** ⇒ **`stat -c %s` at every Tier-2; RE-SPLIT above 32,550 B. NEXT MANDATORY CHECK: 2026-09-30.** ⛔ Do not replace this with a leanness claim.

## 📕 THREE FILES — read the right one

| File | When | Boot? |
|---|---|---|
| **`ROUTING_TABLE.md`** (this) | the domain table · By Type/Tag/Boundary/Convergence · safety net · escalation · MINIMIZE | ✅ **BOOT** |
| **[`ROUTING_CARVEOUTS.md`](ROUTING_CARVEOUTS.md)** | **AT DISPATCH**, when a signal is in that agent's lane — the 20 per-agent carve-outs | ❌ not at boot |
| **[`history/ROUTING_TABLE_VERSION_HISTORY.md`](history/ROUTING_TABLE_VERSION_HISTORY.md)** | provenance, on demand | ❌ not at boot |

> ⚠️ **The carve-outs are ROUTING LAW, not commentary** — they are what puts CORAL on a Florida signal and TERRY on a T-1. They moved because they are read at DISPATCH, not at boot. **A pointer nobody travels is how a rule dies** (`[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`), so the full inventory is named here and the dispatch step names the file.

### Carve-out inventory (20 sections — text in `ROUTING_CARVEOUTS.md`)
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
