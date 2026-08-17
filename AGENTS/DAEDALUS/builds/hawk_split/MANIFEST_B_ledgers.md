# HAWK Split — Manifest B: Ledgers (VX.tsv, FLOW.tsv, STRIKES.tsv, SUMMARY.md, KB.tsv)

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.

**Reader:** DAEDALUS sub-agent B. **Scope:** `AGENTS/HAWK/workbook/*.tsv` + `AGENTS/HAWK/domain/energy-strikes/`. **Date:** 2026-07-12.
**Read against:** `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md` (§4 content migration, §7 Tier-1 fixes).

---

## 1. VX.tsv — row-by-row assignment

**Schema (11 cols):** `ID | Name | Current_Value | Status | Green | Yellow | Orange | Red | Last_Updated | Source | Notes`. Free-text `Current_Value`/`Notes` carry pipe-delimited dated log entries (newest-first) — siblings' fresh VX.tsv should keep this convention for continuity.

**18 data rows total.** Spec §4 gives an explicit mapping; I verified it against full row content. **All 18 agree with spec — zero disagreements.**

| ID | Current Status | Disposition | Agree w/ spec? |
|---|---|---|---|
| VX-HAWK-IRAN-01 | RED | **FALCON** | ✅ |
| VX-HAWK-IRAN-02 (Hormuz) | RED | **FALCON** | ✅ |
| VX-HAWK-USIRAN-KINETIC-01 | RED | **FALCON** | ✅ |
| VX-HAWK-GULFSTATE-01 | RED | **FALCON** | ✅ |
| VX-HAWK-DIPLOMACY-01 | YELLOW | **FALCON** | ✅ |
| VX-HAWK-ISR-01 | ORANGE (dormant-armed) | **FALCON** | ✅ |
| VX-HAWK-BABMANDAB-01 | RED | **FALCON** | ✅ |
| VX-HAWK-UKR-01 | RED | **OSPREY** | ✅ |
| VX-HAWK-SHADOW-01 | RED | **OSPREY** | ✅ |
| VX-HAWK-SHADOW-02 | RED | **OSPREY** | ✅ |
| VX-HAWK-VEN-01 | YELLOW | **HAWK** (dormant) | ✅ |
| VX-HAWK-TWN-01 | RED (dormant-armed) | **HAWK** (dormant) | ✅ |
| VX-HAWK-TRADE-01 | YELLOW | **HAWK** (dormant) | ✅ |
| VX-HAWK-TRADE-02 | YELLOW | **HAWK** (dormant) | ✅ |
| VX-HAWK-SULPHUR-01 | ORANGE (deferred to BRENT) | **HAWK** (dormant) | ✅ |
| VX-HAWK-FININFRA-01 | ORANGE (dormant-armed) | **HAWK** (dormant) | ✅ |
| VX-HAWK-IRAQ-01 | RED (deferred to BRENT) | **HAWK** (dormant) | ✅ |
| VX-HAWK-CEASEFIRE-01 | SUPERSEDED/retired | **HAWK** (historical anchor) | ✅ |

**Count check:** FALCON=7, OSPREY=3, HAWK=8 → 18/18, matches row count exactly.

**One clarifying (not disagreeing) note:** `VX-HAWK-IRAQ-01` (oil-production vector, deferred to BRENT) → HAWK dormant per spec — but `scripts/baghdad_watch.py` (a different asset, Iran/Iraq political-kinetic discriminator) → **B/FALCON** per spec §4 row 8. These are two separate Iraq-adjacent assets with **different** dispositions; don't conflate them when migrating — flag this explicitly in the build spec so DAEDALUS doesn't accidentally move the VX row to FALCON by association with the script.

---

## 2. FLOW.tsv — row-by-row assignment

**Schema (9 cols):** `ID | Name | Speed | Status | Trigger | Current_Position | Pathway | Cross-Agent | Notes`. **20 data rows** (FLOW-HAWK-01 through -20, all present, none missing — stored out of strict numeric order: 06,09,07,08 mid-table).

**Spec gap:** §4 states the *principle* ("split by theater; cross-war transmission pathways → HAWK") but gives **no row-by-row list** for FLOW.tsv (unlike VX.tsv). I built one from content; 6 of 20 rows are genuinely ambiguous — flagged below for DAEDALUS/PROME to ratify, not silently resolved.

| ID | Name | Status | Recommended disposition | Confidence |
|---|---|---|---|---|
| FLOW-HAWK-01 | Hormuz Closure → Oil Price | MUTED (dormant-armed) | **FALCON** | High |
| FLOW-HAWK-02 | Oil Price → Consumer Stress | MUTED | **FALCON** (trigger = Brent>$85 off Hormuz) | High |
| FLOW-HAWK-03 | Oil Price → Japan Energy Crisis | MUTED | **FALCON** (Qatar/Hormuz-driven; SAM-facing) | Med |
| FLOW-HAWK-04 | War Escalation → Vol Regime | MUTED | **FALCON** (content is Iran-deadline-loaded) — but ⚠️ **OSPREY needs its own equivalent row from scratch**; Russia-war vol transmission isn't captured here | Med — **flagged** |
| FLOW-HAWK-05 | War Escalation → Credit Widening | MUTED | **FALCON** (same reasoning as -04) — ⚠️ same OSPREY-needs-own-row flag | Med — **flagged** |
| FLOW-HAWK-06 | Gulf Production Shutdown → Global Supply | MUTED | **FALCON** (Iraq+Qatar+Hormuz, all Gulf) | High |
| FLOW-HAWK-07 | Shadow Fleet Disruption → Russian Revenue | WARMING | **OSPREY** (feeds VX-SHADOW-01/02→OSPREY) — note: Notes text frames a "third-theater hydrocarbon-under-attack" read (Gulf+Red Sea+Black Sea) that's broader than pure-Russia; OSPREY should keep the Russia-revenue core, flag the multi-theater framing to HAWK | Med — **flagged** |
| FLOW-HAWK-08 | Ukraine Refinery Campaign → Russian Products | WARMING | **OSPREY** | High |
| FLOW-HAWK-09 | Civilian Infra Targeting → Conflict Duration Extension | MUTED | **FALCON** (content = Bahrain desal + Tehran depots only) | High |
| FLOW-HAWK-10 | Hormuz→Sulphur→Copper→Grid Stall | MUTED | **HAWK** (dormant) — mirrors VX-SULPHUR-01's HAWK disposition; structural multi-year thesis, not an active war-tracking row | Low — **flagged, recommend HAWK for VX-consistency** |
| FLOW-HAWK-11 | Hormuz→Fertilizer→Food CPI | MUTED | **FALCON** (Gulf-specific, CARL-facing) | High |
| FLOW-HAWK-12 | Physical Mining → Insurance Lag | **FIRING** | **FALCON** (Hormuz mines) | High |
| FLOW-HAWK-13 | Hormuz Duration → Taiwan LNG Crisis | MUTED | **HAWK** (dormant) — endpoint is VX-TWN-01, which is HAWK's | Low — **flagged, recommend HAWK for VX-consistency** |
| FLOW-HAWK-14 | Food Instability → Conflict Extension Loop | MUTED | **FALCON** (Gulf/Hormuz reinforcing loop) | High |
| FLOW-HAWK-15 | TSMC → Core PCE → Fed Cut Elimination | MUTED | **HAWK** (dormant) — Taiwan/Korea endpoint, same class as -13 | Low — **flagged** |
| FLOW-HAWK-16 | Ras Laffan → Helium → Semiconductor Rationing | MUTED | **HAWK** (dormant) — Taiwan/Korea endpoint | Low — **flagged** |
| FLOW-HAWK-17 | Iraq FM → Supply Gap → SPR Exhaustion | MUTED | **FALCON** (live Gulf-production transmission; task brief explicitly places Iraq/Baghdad in FALCON's theater) — ⚠️ **tension**: VX-HAWK-IRAQ-01 (the underlying vector) → HAWK dormant per spec. Recommend the FLOW *pathway* stays FALCON (operational Gulf-supply watch) while the VX *vector* stays HAWK (dormant scorecard) — same split-ownership pattern as the Baghdad-watch-script note above, but confirm with Will/PROME since it's non-obvious | Low — **flagged** |
| FLOW-HAWK-18 | China Reserve Drawdown → SPR Crack → Global Repricing | MUTED | **HAWK** (dormant/cross-cutting) — trigger is China-specific, not Iran or Russia; candidate for retirement-to-ZHAO/BRENT instead of migration, flag as an open question | Low — **flagged** |
| FLOW-HAWK-19 | Salvo Regime Decoupling (Kinetic Cadence ↔ Brent Vol) | MUTED-IN-CURRENT-REGIME | **HAWK** — explicit, high-confidence. This IS the "shared oil-decoupling thesis (spans both wars)" spec §2/§5/§6 names as HAWK's core synthesis job; row content already blends Iran-MOU and Russia-refinery data points | **Very high** |
| FLOW-HAWK-20 | Russia Refinery Strikes → Product/Crack | **FIRING** | **OSPREY** | High |

**Count:** FALCON=11 (8 solid + 04/05/17 flagged-but-recommended), OSPREY=3, HAWK=6 (1 solid [-19] + 5 flagged) = 20/20.

**Action item for the build spec:** the 6 flagged rows (04,05,10,13,15,16,17,18 — 8 actually, recount: 04,05,10,13,15,16,17,18 = 8 flagged of 20) need a DAEDALUS/PROME/Will call before migration — I've recommended a consistent principle (dormant-book endpoint → HAWK; live Gulf-operational pathway → FALCON; Russia-only → OSPREY) but the spec didn't pre-decide these and a different call is defensible.

---

## 3. STRIKES.tsv

**Schema (16 cols):** `strike_id (THEATER-YYYYMMDD-SLUG) | Date | Theater (RU-UA/GULF-IRAN) | Attacker | Facility | Region | FacilityOperator | Type | Capacity | Status | Strike# | Channel | ReturnToService | Conf | Source | Notes`.

**Row count: 36 data rows** (not ~43 as estimated in the task brief — correcting that figure). Matches the commit-message math: 29 pre-existing + 7 backfilled 7/12 = 36.

| Theater | Count |
|---|---|
| RU-UA | 32 |
| GULF-IRAN | 4 |
| Untagged/other | **0** |

**Clean split confirmed** — every row carries a valid `RU-UA` or `GULF-IRAN` tag, no ambiguous/untagged rows. Spec's "clean split" claim (§4) holds mechanically.

**Date range:** 2026-02-23 (`RU-20260223-DRUZHBA1`) → 2026-07-10 (`RU-20260710-USTLUGA-NOVATEK`, newest row).

**7/12 backfill rows — confirmed present** (all 7, per SUMMARY.md's own changelog line): `RU-20260523-NOVOROSSIYSK`, `RU-20260608-NOVOROSSIYSK`, `RU-20260620-KAVKAZ`, `RU-20260625-PRIMORSK`, `RU-20260704-STPETERSBURG`, `RU-20260706-VYSOTSK`, `RU-20260710-USTLUGA-NOVATEK`.

**GULF-IRAN theater is thin:** only 4 rows, all dated March 2026 (`GI-20260307-HAIFA`, `GI-20260319-YANBU`, `GI-20260319-MINAAHMADI`, `GI-20260319-MINAABDULLAH`). SUMMARY.md itself flags this ("Gulf–Iran theater: only 4 seed rows... full backfill pending"). **FALCON inherits a near-empty strike ledger** and needs its own backfill sweep from day one — this is the single biggest asymmetry in the split (see §6 Surprises).

**Data-quality notes to carry into Tier-1 fixes (§7 spec):**
- `RU-20260514-VOLGOGRAD` — date low-confidence (C3), flagged in ledger's own Open-Verify-Items.
- `RU-202605xx-SYZRAN` — exact date unresolved (TBD).
- `RU-20260521-UNSPEC` — facility unnamed.
- `ReturnToService` is `unk` for all 36 rows — repair-lag analysis is not currently computable from the ledger (SUMMARY.md §Metric-discipline already documents this honestly).

---

## 4. SUMMARY.md — section map + disposition

| Section | Content | Disposition |
|---|---|---|
| Header / maintainer note | "all theaters in one table," 7/12 backfill changelog | Split: intro framing → HAWK (cross-theater note); backfill changelog → OSPREY (all 7 backfilled rows are RU-UA) |
| Schema block | 16-col schema definition | Template — both OSPREY + FALCON copy verbatim for their fresh ledgers |
| Materiality bar | What earns a row | Template — both copy |
| Metric discipline (3 rules) | Don't-sum-nameplates, point-in-time Status, material-subset caveat | Template — both copy (this **is** spec §7 fix #5, "scope label," already implemented here — good pattern to carry forward) |
| Current sourced aggregates | Russia refining-offline %, crude-export volumes | **OSPREY** (100% Russia-specific) |
| Patterns ①–④ + CUT | Crude-vs-product channel model, re-strike sequences, geographic reach, under-priced product risk | **OSPREY** — this is explicitly the "crude-vs-products channel model + flip-triggers" spec §2 names as OSPREY's framework |
| Watch / flip-trigger table (4 triggers) | Storage saturation, terminal strikes, shut-ins, Urals discount | **OSPREY** |
| Open verify items | Volgograd date, Syzran date, unspec facility, ReturnToService gaps, **Gulf-Iran 4-row caveat** | Split: RU items → OSPREY; the Gulf-Iran thinness note → **FALCON** (it's their backfill mandate) |
| Cross-refs | KB-HAWK-185/186, research narrative, "Price/crack consequence = BRENT" | **OSPREY** |

**Net effect: SUMMARY.md is ~95% Russia-theater content.** FALCON inherits essentially a blank analysis file (just the schema/materiality/metric-discipline templates) — consistent with the thin GULF-IRAN ledger in §3. HAWK's "thin derived cross-war summary table" (spec §4) has almost no seed material here either — the one genuinely cross-war observation is the header's "Russia's campaign peaking the week Iran signed its MOU" line, which is worth preserving as HAWK's founding synthesis note but isn't a built-out analysis.

**Pattern ① correction — confirmed current.** Spec's claim that Pattern ① was corrected 7/12 (crude-export and product-crack channels run in **parallel**, not sequentially) is verified word-for-word in the live file: *"[CORRECTED 2026-07-12, Will-directed: NOT a clean one-way switch... The two channels run in PARALLEL now, not sequentially. HAW-15 FAILED."]* Flip-trigger #2 in the Watch table is marked **FIRED** (corrected 7/12) with the same language. This matches the 5d246d25 commit in the repo history. No drift between spec claim and file state.

---

## 5. KB.tsv — freeze-in-place viability

**Schema (13 cols):** `ID | Date | Group | Entity | Fact | Source | Conf | Epistemic | Status | Stale_By | DerivedFrom | Vectors | Notes`. Matches the fleet-standard KB schema (`AGENTS/SCHEMA.tsv`-equivalent conventions) — safe for siblings to inherit the same shape for fresh KBs.

**Row count:** 226 lines = 225 data rows. **ID range:** KB-HAWK-001 → KB-HAWK-223, sequential, **no gaps**. Discrepancy explained: **2 duplicate IDs** — `KB-HAWK-131` and `KB-HAWK-132` each appear twice (225 rows, 223 unique IDs). Minor data-quality flag, not a blocker — worth a one-line fix note but doesn't affect freeze-viability (both duplicate pairs are historical rows, not live-cited elsewhere in a way that an ID collision would break, per the citation scan below).

**Date range:** 2025-06-16 → 2026-07-12 (i.e., includes pre-war seed history, not just the Feb-2026 war-launch window).

**Group-column distribution (top):** WAR=81, GEOPOLITICS=34, HORMUZ=27, ENERGY=25, GEOPOL=14, TANKERS=11, MACRO=6, DIPLOMATIC=4, SHIPPING=3, FERTILIZER=3, others 1-2 each (UKR_ENERGY, META, FOOD, SULPHUR, REFINERY, POLITICAL, METHOD, MARKETS, LABOR_MARKET, IRAN-US, GULF_STATE, DIPLOMACY, AVIATION, ANALYSIS). No clean group-level Iran/Russia split exists in this column — theater assignment would require row-level Entity/Vectors inspection, reinforcing that **freeze-in-place (not row-surgery) is the right call**, exactly as spec §4/§8 recommends.

**Which live files cite KB-NNN IDs (freeze-break check):**

| File | KB-citations |
|---|---|
| `LESSONS.md` | present |
| `thesis/CHANGELOG.md`, `thesis/PREDICTIONS_ARCHIVE.md`, `thesis/TIMELINE.md` | present (heaviest historical load) |
| `research/*.md` (BOARD_CATCHUP, DEADLINE_SCENARIO_TREE, POST_DEADLINE_PLAYBOOK, RUSSIA_OIL_INFRA_STRIKES) | present |
| `audits/*.md` (PHASE4_WAR_RISK_INSURANCE, STALE_DATA_AUDIT) | present |
| `outbox/*.md` (3 files, incl. two 7/12 BRENT sends) | present |
| `REMARK_20260628.md` | present |
| `CLAUDE.md` | 1 mention — **stale**: "currently through KB-HAWK-034" (a schema-doc example, ~189 IDs out of date; harmless, cosmetic fix only) |
| **`STATUS.md`** | **0 citations** |
| **`SCRATCH.md`** | **1 citation** |

109 total KB-ID mentions across HAWK's `.md` files. **Freezing KB.tsv in place breaks nothing** — every citing file is either (a) archival/historical (LESSONS, thesis/*, research/*, audits/*, REMARK) and stays put or splits-with-pointers per spec, or (b) already near-zero on KB citations (STATUS.md=0, SCRATCH.md=1), meaning the **live daily-state files that get rewritten for OSPREY/FALCON don't structurally depend on row-level KB access** — they can carry forward pointer-references to frozen `KB-HAWK-NNN` IDs without needing the KB itself to move or split. This is a meaningfully **lower-risk migration than it might look** — the heaviest KB dependency lives in files spec already designates for freeze-or-split-with-provenance-pointer treatment, not in the files DAEDALUS will be actively rewriting.

**Recommendation: freeze-in-place is fully viable, confirmed.** No file requires row-level KB surgery to keep functioning.

---

## 6. Other workbook files (not in original task list, flagged for completeness)

- **`PRICE_BREACHES.tsv`** — already **FROZEN 2026-07-09** (banner present: "not maintained since 2026-04-20... oil-price tracking is BRENT's lane"). Not part of the split — stays frozen wherever HAWK's frozen-archive material lands, no action needed.
- **`SCHEMA.tsv`** — the fleet-standard KB schema definition (13-field spec, controlled vocab pointers). Not agent-specific; siblings' fresh KBs should reference this same schema (or copy it) rather than reinvent.
- **`BOOT_LOG.md`, `EXIT_PROTOCOL.md`, `FOUR_STRUCTURAL_BREAKS_MAR18.md`, `POLITICAL_SUSTAINABILITY_MODEL.md`, `STATUS_archive_*.md`** — present in `workbook/` but out of my read scope (not TSVs); flagging their existence so DAEDALUS's build spec accounts for them in the file inventory. `STATUS_archive_*` are clearly historical (freeze/HAWK); `EXIT_PROTOCOL.md`/`FOUR_STRUCTURAL_BREAKS...`/`POLITICAL_SUSTAINABILITY_MODEL.md` need a theater call not made here.

## 6b. Surprises

1. **Row-count correction:** task brief estimated STRIKES.tsv at "~43 rows" — actual is **36**. Minor, but worth fixing the number wherever it propagates into the build spec.
2. **GULF-IRAN ledger thinness is the biggest asymmetry in this split.** STRIKES.tsv is 89% RU-UA (32/36) and SUMMARY.md's entire analysis layer (Patterns, flip-triggers, aggregates) is Russia-only. FALCON isn't inheriting a mature ledger+analysis pair the way OSPREY is — it's inheriting a schema and a materiality bar, and needs a **from-scratch Gulf-Iran strike backfill sweep** as an immediate post-scaffold task, not a nice-to-have. This should be called out explicitly to Will/PROME as asymmetric migration effort, not silently absorbed.
3. **KB.tsv has 2 duplicate IDs** (KB-HAWK-131, -132) — cosmetic, doesn't block freeze, but worth a one-line fix note.
4. **FLOW.tsv has no spec-given row mapping** (unlike VX.tsv) — 8 of 20 rows are genuinely ambiguous between FALCON/HAWK on a "live Gulf pathway vs. dormant-endpoint" axis (sulphur/copper, Taiwan LNG/TSMC/helium, Iraq SPR, China SPR). I've proposed a consistent principle and a recommended assignment, but this needs explicit DAEDALUS/PROME/Will ratification, not silent resolution during migration.
5. **CLAUDE.md has a stale KB-ID-count reference** ("currently through KB-HAWK-034") — 189 IDs behind current. Cosmetic, low-priority, but easy to fix while touching the file anyway.
6. **No second strike ledger exists** — `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md` is a narrative writeup cross-referenced by SUMMARY.md, not a second data ledger. `domain/energy-strikes/STRIKES.tsv` is the only strike ledger. Confirms spec's single-ledger assumption.
7. **STATUS.md/SCRATCH.md are nearly KB-citation-free** (0 and 1 respectively) — meaningfully de-risks the freeze-in-place KB plan since the files being actively split/rewritten don't lean on row-level KB references (see §5).

---
*Written by DAEDALUS sub-agent B, 2026-07-12. Read-only on all files except this one.*
