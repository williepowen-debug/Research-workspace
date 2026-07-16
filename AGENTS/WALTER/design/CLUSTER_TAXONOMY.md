# WALTER Cluster Taxonomy

**Version:** v0.5 | **Date:** 2026-07-16 (**AI_INFRA_CAPEX split-vs-keep RESOLVED = KEEP; soft cap 15 → 40. Will-approved, Telegram.** The v0.4 check surfaced the breach [23 vs 15]; the axis check answered it. Verdict rationale + the recorded open counter live in the AI_INFRA_CAPEX row's scope cell. Headline: **the cluster CONCENTRATED, it did not fragment** — the 6/6 revisit-trigger never fired, but its "4-angle agreement" premise is dead [financing 57%; obsolescence + input-cost at 1 each]. Kept because the angles still answer one question, because VULCAN — the domain owner, **wired to this cluster only on 7/16** — needs both halves, and because **23 was tied 8th of 12 while being the ONLY capped cluster** [CONSUMER_STAGFLATION 90 / IRAN_HORMUZ 80 / HYDROCARBON_INFRA 23 all uncapped]. **The cap was the outlier, not the cluster.** 40 = peer-calibrated. **Undecided + recorded: whether cap policy deserves a fleet-wide basis at all.**) **Prior:** v0.4 (2026-07-16 — **structural — Will-approved**: the rotting `Current count` column REPLACED by a stable `Soft cap` column; per-cluster counts + the `Total:` line now POINT at `/BOARD/INDEX.md`'s ToC instead of being restated here. Rationale: counts are DERIVED and live — the INDEX ToC already carries them and `walter_doctor board_reconcile` mechanically enforces them, so restating them here bought nothing at dispatch time and rotted by construction. The **soft cap is a DECISION**, not a derived value: it does not rot, and it belongs in the doc that governs cluster structure. New `cluster_softcap_breach` doctor check reads this column.) **Prior:** v0.3 (2026-06-28) — CLIMATE_MACRO added as the 12th cluster — home for AEOLUS climate→economy signals; Will sign-off 2026-06-28 Telegram. Propagates to FORMAT_SPEC v0.12 cluster enum + CLIMATE_MACRO domain code + ROUTING_TABLE v0.16 routing row + STATE §1.)

**Prior:** v0.2 (2026-06-06) — CONSUMER_STAGFLATION split (INFLATION_TRANSMISSION carved out as 11th; AI_INFRA_CAPEX soft-cap raised to 15). v0.1 (2026-05-05) — 10-bucket taxonomy locked.

**Purpose:** Canonical source for cluster names used to categorize dispatched signals in `/BOARD/INDEX.md`. Cluster names also appear (and previously drifted) in `STATUS.md`, signal bodies, and MEMORY.md `Findings`. This file is the single source of truth — other docs reference these names, never invent.

**Spec ownership:** WALTER CLAUDE.md canonical-source-lookup table maps "cluster taxonomy" to this file. Edits to cluster names, additions, or deletions land here first, then propagate.

---

## Why clusters exist

WALTER dispatches one signal at a time, but signals don't arrive in isolation — they form themes that the network already discusses informally ("PC-stress meta-cluster ≥9 nodes," "Iran day-cluster ≥16 channels"). When BOARD INDEX is sorted only by SIG-ID (dispatch order), those themes are invisible to a reader scanning for "what does our network think about Iran right now?"

Sectioning the INDEX by cluster makes themes first-class. It also gives WALTER a stable lookup for "is this new signal in an existing cluster, or a singleton?" at intake — the answer drives where it gets archived and how recipients consume.

**Cluster ≠ domain.** Domain (LABOR, OIL_ENERGY, etc.) is the recipient-routing axis owned by FORMAT_SPEC. Cluster is the thematic axis — multi-signal narrative threads. One domain can span multiple clusters (BANK_CRE includes both BANK_COLLATERAL and PC_STRESS signals). One cluster can span multiple domains (CONSUMER_STAGFLATION includes LABOR + MACRO_INFLATION + CONSUMER_CREDIT + OIL_ENERGY transmission).

---

## The 12 clusters

Cluster names use `UPPER_SNAKE_CASE`, kept short for INDEX section headings.

| # | Cluster | Theme | Soft cap | Sample signal IDs |
|---|---------|-------|---------------|-------------------|
| 1 | **IRAN_HORMUZ** | Iran war / Hormuz chokepoint / GEOPOL_ENERGY supply disruption / sanctions enforcement / state-response. Includes oil-supply observations downstream of Iran-driven disruption. | — | 419-006, 419-014, 424-002 (Hengli), 426-007 (Pinckney), 429-001 (Brent $115), 429-003 (rial) |
| 2 | **POSITIONING_VALUATION** | Equity positioning extremes, valuation indicators, vol regime, breadth, fund flows, MMF-rolldown, short-cover, options skew, call/put extremity. Counter-evidence within cluster lives here too. | — | 419-005 (Buffett 232%), 419-002 (SKEW divergence), 419-018 ($93B short cover), 424-004 (Kobeissi $9.7B Nasdaq) |
| 3 | **BANK_COLLATERAL** | Bank-collateral-compression — distressed CRE, residential housing weakening, office vacancy, multi-family stress, individual-property credit-bid markdowns, regulatory shocks affecting bank collateral pools (ROAD Act). | — | 419-001 (Tricolor MTB), 420-008 (distressed office $5B), 426-002 (residential weakening), 428-004 (Phoenix BTR ROAD Act) |
| 4 | **CONSUMER_STAGFLATION** | Consumer-stagflation K-shape stack — sentiment, CC delinquency, labor weakness, retirement-savings stress, tier-stratification (top/bottom divergence) across consumer/wage/housing-segment/401k axes. Stagflation-Fed-reaction-function lens. **Does NOT include forward inflation transmission** (supply-chain cost-push) — that's INFLATION_TRANSMISSION (cluster 11). | — | 410-001 (CPI+UMich), 424-007 (CC delinq 12.7%), 426-008 (UMich 49.8 final), 426-005 (farm bankruptcies +46%) |
| 5 | **PC_STRESS** | Private-credit / BDC / asset-manager stress — fund redemption gates, founder/exec leverage unwinds, single-client AUM pulls, regulatory inquiries (Fed-PC), retail BDC Q1 redemption surges, mark-to-model fiction. | — | 414-002 (TCW Red Lobster 98%), 420-004 (Blue Owl founders unwind), 426-012 (Fed-PC inquiry), 429-002 (OCIC/OTIC) |
| 6 | **HYDROCARBON_INFRA** | Hydrocarbon-infrastructure stress meta-cluster — refinery fires, pipeline explosions, drone strikes on oil/petrochem assets globally (non-ME), water-emergency curtailment risk. | — | 416-002 (Geelong), 420-001 (Tuapse), 420-003 (11-event aggregation), 426-003 (LA pipeline) |
| 7 | **MISC** | Singletons + market-structure + adversarial-meta + counter-evidence-without-cluster-home. New cluster spawned only when ≥3 signals in a coherent new theme. | — | 411-001 (RED falsification), 414-003 (SEC PDT), 414-012 (KRE-XLF gap), 428-007 (INTC CAO) |
| 8 | **AI_INFRA_CAPEX** | AI infrastructure capex sustainability — hyperscaler capex guidance, OpenAI/Stargate financing, leveraged equity collateral on AI names, chip-side capex revisions, data-center spending, capex→power-demand, AI supply-chain/export-controls. **Domain owner: VULCAN** (`AI_CAPEX`, wired 2026-07-16 — the cluster ran 23 signals deep with no domain owner routed to it). *(**v0.5 2026-07-16: split-vs-keep RESOLVED = KEEP; soft cap 15 → 40, Will-approved.** The 7/16 axis check found the 6/6 revisit-trigger ["fragment beyond 4 distinct axes"] **did not fire — the cluster CONCENTRATED rather than fragmented**: financing 13/23 [~57%], ROI ~5, **obsolescence 1 [stale since 5/11], input-cost 1**, + 2 unforeseen axes [power 2, muni/fiscal 1]. But the lock's **premise is dead** — it is no longer "4-angle agreement." **Kept anyway, on 3 grounds:** [1] the angles never stopped answering ONE question ["does the buildout continue?"] — they are channels, not themes, and the lock's own "agreement is load-bearing" logic cuts **against** splitting, since the convergence view IS the value; [2] the reader-split argument **fails** — VULCAN wants BOTH halves [its S1 = capex concentration + **FCF compression**; financing stress is the *mechanism* by which capex gets cut]; [3] **23 is unremarkable by this taxonomy's own revealed standard** — it is tied 8th of 12 and was the **ONLY capped cluster**, while CONSUMER_STAGFLATION 90 / IRAN_HORMUZ 80 / BANK_COLLATERAL 77 / POSITIONING_VALUATION 73 / PC_STRESS 42 run uncapped, and **HYDROCARBON_INFRA sits at the identical 23 uncapped with nobody asking. The cap of 15 was the outlier, not the cluster.** Cap set to **40 = peer-calibrated** [PC_STRESS 42 / FED_FRAMEWORK 34 live there fine], keeping the governance prompt at a level that means something; 25 would have re-armed the same arbitrary tripwire 2 signals later. **Open counter, recorded not resolved:** "peers are bigger" is weak if the truth is that 90 SHOULD be capped and nobody did — **whether cap policy deserves a fleet-wide basis is a separate, undecided question.** **The finding that outlives the taxonomy call:** financing at 57% with obsolescence + input-cost decayed to one stale signal each is either a real domain shift **or WALTER's filter killing them** — routed to VULCAN 7/16 for the domain read; WALTER does not grade its channels.)* | **40** | 424-012 (SoftBank $10B OpenAI), 428-002 (OpenAI/Friar), 429-004 (META/MSFT capex advisory) |
| 9 | **ASIA_CHINA** | China / HK / EM-Asia contagion — China trade-surplus dynamics, export controls, residential property collapse, peg fragility, JGB unwind, supply-chain coercion. | — | 414-010 (FT China Shock 2.0), 414-011 (export controls tripled), 428-001 (China FRED residential) |
| 10 | **FED_FRAMEWORK** | Fed operating-framework regime shift / UST-foreign-holder composition / **funding plumbing** (SOFR-IORB, repo, reserve scarcity, ON-RRP drawdown, funding-seizure pre-emption gates). Beckworth Mercatus / Apollo private-vs-CB / Fed-balance-sheet-reduction / money-market plumbing. *(Description broadened 2026-07-09, Will-approved walkthrough — cluster legitimately spans Fed-framework regime AND funding-plumbing; the UST_PLUMBING rename was declined as high-churn/low-gain.)* | — | 426-001 (Beckworth framework), 426-010 (Apollo private-vs-CB), 20260709-003 (funding-seizure X1 gate) |
| 11 | **INFLATION_TRANSMISSION** | Forward goods-CPI / supply-chain cost-push transmission — freight indices, port congestion, pump-pass-through, tariff front-loading, supply-chain disruption with 3-6 month CPI lag. *Distinct from CONSUMER_STAGFLATION (which is regime-stratification, tier-divergence) — INFLATION_TRANSMISSION is mechanism (cost-push pipeline). Carved out 2026-06-06 from CONSUMER_STAGFLATION as freight axis [SIG-W-20260604-012 CCFI +114%] introduced distinct cost-push mechanism. New cluster starts forward — pre-2026-06-06 CONSUMER_STAGFLATION signals grandfathered (see Maintenance rules).* | — | 604-012 (Hedgeye CCFI +114%) |
| 12 | **CLIMATE_MACRO** | Macro climate→economy transmission — ENSO/El-Niño state, energy demand (heat-dome/cooling/power-burn), ag/food, insurance/reinsurance, property/physical risk, supply-chain/logistics (freight/water-levels), on a tiered weather→structural horizon. AEOLUS's home cluster. *Distinct from INFLATION_TRANSMISSION (cost-push pipeline) — CLIMATE_MACRO is the climate DRIVER upstream of multiple channels (energy/ag/insurance/supply-chain). FL-specific climate stays CORAL (reconcile FL numbers to AEOLUS's one ENSO figure, don't silo). Pure climate-science with no economic-transmission channel still KILLS (Relevance gate) — the discriminator is a concrete economic channel within the thesis horizon, not the word "climate." Created 2026-06-28 with AEOLUS's first routed signals; Will sign-off.* | — | 628-011 (US heat-dome+SW wildfire), 628-012 (El Niño record-strength) |

**Counts live in [`/BOARD/INDEX.md`](../../../BOARD/INDEX.md)** — its ToC carries per-cluster counts + TOTAL and is mechanically reconciled by `walter_doctor board_reconcile`. **Do NOT restate them here:** a count restated in this file is derived, duplicative, and rots by construction. The stripped v0.1-era column had drifted on every row (IRAN_HORMUZ 22-vs-80, CONSUMER_STAGFLATION 12-vs-89, FED_FRAMEWORK 2-vs-34, total ~99-vs-492) and — worse — it **hid a BREACHED soft cap**: AI_INFRA_CAPEX read **3** while actually at **23** against a cap of **15**, making the cap un-evaluable from the doc that defines it.

---

## Soft caps (added v0.4)

The `Soft cap` column is the **governance** value: the size at which a cluster's split-vs-keep decision re-opens. It is a **decision, not a measurement** — it changes only by a Will-signed-off taxonomy edit, so unlike the stripped count column it does not rot.

- `—` = no cap set (most clusters). A cap is added only when a cluster's growth actually raises a split question.
- **A breach is a PROMPT, not a rule** — it re-opens split-vs-keep (per the MISC-vs-new-cluster tree below); it does **not** auto-split, auto-raise the cap, or block dispatch. **Will signs off** on any split (adding a cluster is a structural change).
- **Mechanized:** `walter_doctor` `cluster_softcap_breach` reads this column, compares it to the **live** `/BOARD/INDEX.md` ToC count, and raises MED on a breach — so a cap can no longer sit silently breached the way AI_INFRA_CAPEX did (cap 15 set 2026-06-06; breached at 23 and invisible until 2026-07-16 because the count column said 3).

**~~Live open decision (2026-07-16): AI_INFRA_CAPEX is 23 vs its cap of 15~~ → RESOLVED same-day (2026-07-16, Will-approved): KEEP, cap 15 → 40.** The check surfaced it; an axis check of all 23 signals answered it. **The cluster CONCENTRATED rather than fragmented** — the 6/6 revisit-trigger ("fragment beyond 4 distinct axes") never fired, though its "4-angle agreement" premise is now dead (financing 57%; obsolescence + input-cost at 1 each). Kept because the angles still answer one question, because VULCAN needs both halves, and because **23 was tied 8th of 12 while being the only capped cluster.** Full rationale + the recorded open counter (does cap policy deserve a fleet-wide basis?) → the AI_INFRA_CAPEX row. **This is the intended lifecycle of a soft cap: breach → prompt → decide → re-cap, on the record.** *(The v0.2 note — 'grown to 9 with 4 distinct mediating angles, locked Option B [keep]' — was written at 9 and is superseded.)*

---

## Cluster naming convention

- `UPPER_SNAKE_CASE`
- 1-2 words, ≤20 chars
- Specific enough to be unique, generic enough to absorb new signals
- Avoid time-bound names ("APR_19_RALLY") — clusters are themes, not days
- Avoid ticker names ("OWL_CLUSTER") — name the theme, not the symbol

---

## Edge-case rules

### Cross-cluster signals (signal fits 2 clusters)

A signal gets exactly **one primary cluster** (where it lives in the INDEX). Secondary cluster, if any, is noted in the signal body via `dispatch_note` or as an inline parenthetical.

**Resolution rules** (in order):
1. If one cluster is the **substance** and the other is the **financing/transmission mechanism**, the substance wins. *Example: 424-012 SoftBank $10B margin loan on OpenAI shares → AI_INFRA_CAPEX primary (the news is about AI capex financing) / PC_STRESS secondary (margin-loan mechanism).*
2. If both are equally substantive, choose the cluster the signal **changes** rather than the cluster it merely **adds to**. *Example: 428-004 Phoenix BTR ROAD Act → BANK_COLLATERAL primary (introduces political-legislative vector to the cluster) / not split into a "POLITICAL_LEGISLATIVE" cluster of size 1.*
3. If still tied, primary = the cluster of the **action recipient** in the routing line.

### MISC vs new-cluster decision tree

Singletons go to MISC. A new cluster only spawns when:

1. ≥3 dispatched signals share a clearly bounded theme that doesn't fit existing clusters, AND
2. The theme has expected forward-momentum (will likely add more signals in coming weeks), AND
3. Will signs off on the new cluster name (per CLAUDE.md spec-ownership rule — adding a cluster is a structural change).

Avoid premature cluster-spawning. *(2026-06-06 update: AI_INFRA_CAPEX has grown to 9 with 4 distinct mediating angles — split decision considered, locked Option B [keep as one cluster, raise soft-cap to 15]. FED_FRAMEWORK still at low count but FED-framework regime is the live operative thesis — consolidation deferred.)*

### Re-categorization

A signal's cluster assignment is **not immutable**. If a signal originally placed in MISC starts looking like the seed of a new cluster (say 3 more signals join the same theme over 2 weeks), promote: spawn the new cluster (Will sign-off), move the seed signals + new ones into it.

But: signal **bodies** are immutable per CHECKLIST editorial discipline. Re-categorization touches INDEX placement only, not signal-file content.

---

## Cluster status flags (deferred — not implemented through v0.3)

INDEX cluster sections may eventually carry status flags:
- 🟢 ACTIVE — signals continuing to land
- 🟡 STALE — no new signals in 14 days
- 🔴 SUPERSEDED-FRAMING — anchor change invalidates the cluster's framing (e.g., May 4 ceasefire-break re: IRAN_HORMUZ pre-May-4 signals)
- ⚫ ARCHIVED — cluster closed; signals retained for history

v0.1 shipped without status flags. **Deferred through v0.2 + v0.3 (never implemented) — revisit only if cluster-level staleness needs its own flag. Note: the v0.10 signal-lifecycle `status`/`status_ref` tags (FORMAT_SPEC) may already cover the need at the signal level, making cluster-level flags redundant.** *(status-audit 2026-07-03.)*

---

## Maintenance rules

- **At dispatch:** WALTER assigns the cluster as part of CHECKLIST Phase 2 (post-routing, pre-output). Cluster name written to a `cluster:` field in the signal YAML header (FORMAT_SPEC update pending) AND used to place the row in the right INDEX section.
- **At closeout:** No bulk re-categorization sweeps. Inline corrections only — if I notice a misassignment while doing other work, fix it. Else leave.
- **At taxonomy version bump:** Single-pass migration. v0.1 → v0.2 is one commit that updates CLUSTER_TAXONOMY.md, INDEX section structure, and any signal `cluster:` headers that need re-assignment.

---

## What this file is NOT

- It's not a list of **active themes** (that's STATUS.md NETWORK AWARENESS + LAST_COMPLETION FOLLOW-UP).
- It's not a thesis tracker (that's CARL/RED/etc.).
- It's not a routing rule (that's ROUTING_TABLE).
- It's a **directory of named buckets** for the BOARD signal archive. Stable, slow-moving.

---

*v0.4 — 2026-07-16 (**structural, Will-approved**: `Current count` → `Soft cap`; counts + `Total:` now point at the BOARD INDEX ToC. The stripped column was a v0.1-era snapshot rotted across every row while duplicating a surface that is both live AND mechanically reconciled — and it hid a breached governance rule (AI_INFRA_CAPEX read 3 against cap 15 while actually 23, i.e. the cap was un-evaluable from the doc defining it). Replacement column holds the cap (a decision — doesn't rot); new `cluster_softcap_breach` doctor check evaluates it against live counts. Surfaced by the 7/16 `restated_set_drift` build.)* · *v0.2 — 2026-06-06 (CONSUMER_STAGFLATION → INFLATION_TRANSMISSION carved out; AI_INFRA_CAPEX cap raised to 15; cluster count 10 → 11). Decisions logged in `LAST_COMPLETION.md` (5-decision walkthrough closeout).*

*v0.1 — 2026-05-05 (Pass 1 BOARD INDEX cluster-organization refactor — 10-bucket taxonomy locked)*
