# NEXUS — Fleet Brief Map
**Purpose:** Single index of `NEXUS_BRIEF.md` status across the fleet. NEXUS reads this at BOOT step 6 to decide where the brief read-flow applies vs where raw STATUS fallback is mandatory.
**Updated:** 2026-07-05 Sun (8-day re-anchor freshness sweep — see ★7/5 note; the ★6/27 note and table rows below are superseded for freshness, kept for the model-shift record).
**Schema reference:** `templates/NEXUS_BRIEF_SCHEMA.md` §4.4 fallback triggers (a/b/c) + `brief_fallback_log.tsv` for run-time instrumentation.

> **★ 2026-07-05 — 8-day re-anchor sweep: ZHAO now has a brief (add to rotation); LIQUID + OZK revived; RED remains the top brief-gap.**
> Fleet scan 7/5 — **13 agents now maintain `NEXUS_BRIEF.md`** (ZHAO added a schema-conformant brief 7/4 on reactivation — PROME ask `inbox/2026-07-05_from-PROME_zhao-briefs-map-add.md`, Will-approved). Freshness this pass (brief / STATUS commit date):
> | Agent | Brief | STATUS | Read-tier / note |
> |---|---|---|---|
> | CARL | 7/2 | 7/2 | T1 (R3 consumer) ✅FRESH — read full |
> | HENRY | 7/2 | 7/2 | T1 (tape/vol/M-09) ✅FRESH — read full |
> | VIOLET | 7/2 | 7/2 | T1 (vol/SKEW/gamma) ✅FRESH — read full |
> | LABOR | 7/2 | 7/2 | T1-standing (chain-head/NFP) ✅FRESH — read full |
> | ORACLE | 7/2 | 7/2 | T1 (crowd/Discipline-D) ✅FRESH — read full |
> | SAM | 7/2 | 7/2 | T1 (R6 Japan/yen/JGB) ✅FRESH — read full |
> | BRENT | 7/1 | 7/1 | T1 (R2/R5 energy) ✅FRESH — read full |
> | MARCO | 7/2 | 7/2 | T2 (FL migration) — corroborates LABOR supply-shrink; opportunistic |
> | **ZHAO** | **7/4** | **7/4** | **T1-when-hot NEW (R8 China/UST demand-hole = M-10; Korea).** Read full while the demand-hole is live (TIC 7/16). |
> | BROCK | 6/28 | 7/4 | T1 (R3 private credit/M-08) — brief PIN-STALE vs 7/4 X1 STATUS → **read raw STATUS this pass** (X1 adjudication). Flag pin-hygiene. |
> | HAWK | 6/26 | 6/26 | T1 (R2 geopol) — unchanged since prior anchor; energy dormant, low-read. |
> | CORAL | 6/25 | 6/25 | T1 (R3 FL geography) — unchanged since prior anchor; use existing read. |
> | OTTO | 6/09 | 6/09 | T2 (internal-ops) — doc-system synthesis only. |
>
> **Brief-LESS (read raw STATUS when domain live, flag if load-bearing):** **RED** (adversarial/Discipline-D — **THE top brief-gap; STATUS content-stale 6/23, pre-6/30/NFP**), **REGINALD** (M-02/M-05 hub — 2nd gap, STATUS 6/26), **LIQUID** (⚡ REVIVED 7/2 — no longer dormant; owns X1/plumbing/demand-hole; brief would be high-value, 3rd gap), **OZK** (revived 7/4), WALTER (routing 7/4), BOND (7/1). **Tier-1 brief coverage: 9 live briefs read this pass.** RED + REGINALD + LIQUID = the three highest-value open gaps (all load-bearing, all brief-less).
>
> **Fallback log this pass:** BROCK `stale` (pin-stale brief, read raw for 7/4 X1); RED/LIQUID `brief-gap`-adjacent (load-bearing, no brief) — logged to `brief_fallback_log.tsv`.

> **★ 2026-06-27 — MODEL SHIFT: the brief is now FLEET-STANDARD; read-set is BRIEF-EXISTENCE-DRIVEN, not a frozen Tier-1 list.**
> A fleet-wide scan found **12 agents now maintain `NEXUS_BRIEF.md`** — beyond the original hardcoded Tier-1. Two were OFF NEXUS's read-list and are now added: **CORAL** (whole-Florida geography-convergence, fresh 6/25 — top-priority geography, FL leg of the REGINALD/CARL transmission cluster, routes explicitly TO NEXUS) and **ORACLE** (prediction-market crowd lens, fresh 6/27 — the market-verdict counter-signal / Discipline-D + thin-liquidity Discipline-E feed; was wrongly marked DORMANT since 4/02). CLAUDE.md BOOT step 6 reframed: read every extant brief (Tier-1 in full each pass), fall back to STATUS for the brief-less.
>
> **The 12 extant briefs (last commit / STATUS / drift, scanned 6/27):**
> | Agent | Brief | STATUS | Drift | Read-tier |
> |---|---|---|---:|---|
> | CARL | 6/26 | 6/26 | 0 | T1 (R3 consumer) ✅FRESH |
> | HAWK | 6/26 | 6/26 | 0 | T1 (R2 geopol) ✅FRESH |
> | CORAL | 6/25 | 6/25 | 0 | **T1 NEW (R3 FL geography-convergence)** ✅FRESH |
> | BRENT | 6/24 | 6/26 | 2 | T1 (R2/R5 energy) — pin-stale, content fresh |
> | HENRY | 6/23 | 6/23 | 0 | T1 (tape/vol) — STATUS itself stale (missing 6/24-27) |
> | VIOLET | 6/23 | 6/23 | 1 | T1 (vol structure) ✅FRESH |
> | SAM | 6/22 | 6/25 | 3 | T1 (R6 Japan) — content fresh, pin-stale |
> | BROCK | 6/20 | 6/26 | 6 | T1 (R3 private credit) — PIN-STALE, read raw for BCRED gate |
> | ORACLE | 6/27 | 6/27 | 0 | **T1 NEW (cross-cutting: crowd/market-verdict)** ✅FRESH |
> | LABOR | 6/16 | 6/26 | 2 | T1-standing (chain-head) — refreshed every closeout |
> | MARCO | 6/15 | 6/15 | 0 | T2 (FL migration/population) |
> | OTTO | 6/09 | 6/09 | 0 | T2 (internal-ops; read on doc-system synthesis only) |
>
> **Brief-LESS (read raw STATUS when domain live, flag if load-bearing):** REGINALD (M-02/M-05 hub — biggest brief-gap), RED (adversarial — Discipline-D), WALTER (routing), LIQUID (dormant 5/21), OZK (revived 6/26, position UNSAFE), BOND. **Tier-1 brief coverage: 10/~14 priority agents.** REGINALD + RED are the highest-value remaining gaps (both load-bearing, both brief-less).

---

## Legend

| Mark | Meaning |
|---|---|
| ✅ **FRESH** | Brief present + STATUS-pin commit current (0 commits drift) OR brief edited after STATUS edit. Read brief; raw STATUS only on trigger (b)/(c). |
| 🟡 **PIN-STALE** | Brief present, content current, but STATUS-pin hash not bumped. Read brief; flag pin-hygiene to that agent. NOT a (a) trigger if content is fresh. |
| 🟠 **CONTENT-STALE** | Brief present but >1 STATUS-commit behind AND brief content predates a material STATUS change. Trigger (a) fires → raw STATUS fallback + log to `brief_fallback_log.tsv`. |
| ⏳ **MISSING** | No `NEXUS_BRIEF.md` exists. Raw STATUS is the only intake. Log to fallback as cause=stale (functionally equivalent) until brief exists. |
| ⚪ **DORMANT** | Agent's own STATUS is itself stale (no recent activity). No brief expected; if NEXUS needs the domain, escalate to PROME/Will. |

---

## Tier-1 — per-agent detail

> ⚠️ **The per-agent rows in this section + the tables below are the 2026-06-16 snapshot** (drift formulas, legend, and maintenance rules remain canonical; the per-agent freshness/classification is superseded by the ★ 2026-06-27 inventory note at the top). Notably: **CORAL and ORACLE now have fresh briefs and are Tier-1** (not reflected in the rows below); ORACLE is no longer dormant.

| Agent | Brief | Brief date | STATUS-pin | STATUS HEAD | Drift | Status | Notes |
|---|---|---|---|---|---:|---|---|
| **CARL** | ✅ | 2026-06-16 | `7182547e` | `7182547e` | 0 | ✅ FRESH | **US consumer stress — credit/housing/K-shape** (NOT labor→LABOR, banks→REGINALD, oil→HAWK/BRENT, vol→HENRY; CPI = downstream input CARL reads, not a deliverable — per CARL scope-correction 6/16). Brief stood up 6/16 10:55; energy decoupled DOWN, structural consumer core intact & rate-path-independent. |
| **REGINALD** | ❌ | — | — | 2026-06-08 | n/a | ⏳ MISSING | Regional banks / CRE. Mid-stream of LABOR→CARL→REGINALD chain. Priority #2. STATUS active. |
| **OZK** | ❌ | — | — | 2026-04-24 | n/a | ⚪ DORMANT | Spun out from REGINALD 4/24; STATUS not refreshed since. Confirm activity status before pressing for brief. |
| **SAM** | ✅ | 2026-06-07 | `6f4e531f` | `b3803c35` | +1 | ✅ FRESH | **Pilot consumer.** Schema/template ratified through SAM's brief 6/7. Drift = 1 commit (within schema threshold). |
| **RED** | ❌ | — | — | 2026-06-03 | n/a | ⏳ MISSING | Adversarial / steelman. Brief should carry counter-case to current convergences. Priority #3. |
| **BROCK** | ✅ | 2026-06-15 | `4e600135` | 2026-06-15 | 0 | ✅ FRESH | Private credit / BDCs. M-02 + M-08 owner. Brief stood up 6/15 (fleet-standard schema). Read this pass — tape re-diverged via $35B AI-origination deal. |
| **LIQUID** | ❌ | — | — | 2026-05-21 | n/a | ⚪ DORMANT | Plumbing / funding. STATUS 18 days old; confirm activity before pressing. |
| **HENRY** | ✅ | 2026-06-15 | (synced) | 2026-06-15 | 0 | ✅ FRESH | Velocity / tape / vol gamma. M-07 + M-08 owner. Brief stood up 6/15. Read this pass — cyclical SOFT-KILLED on soft core CPI; flags 3-place K-split (M-08). Gamma feed dark ~6/9 (flip-level unconfirmed). |
| **HAWK** | ✅ | 2026-06-08 | `8844b6a7` | `8844b6a7` | 0 | ✅ FRESH | Geopolitical / Iran war. Recent damage→salvo regime reframe; leakage-not-volume tail. |
| **BRENT** | ✅ | 2026-06-08 | `ce65758f` | `3ffba885` | +2 | 🟡 PIN-STALE | Brief content covers rev-5 BRT-27/28 work (commit `3ffba885`) but STATUS-pin not bumped. Content fresh; pin-hygiene flag to BRENT. |
| **VIOLET** | ✅ | 2026-06-08 | `725f1ffb` | `725f1ffb` | 0 | ✅ FRESH | VIX / vol structure. Fade-leaning two-leg pathway; CPI gate Wed 6/10. |
| **WALTER** | ❌ | — | — | 2026-06-07 | n/a | ⏳ MISSING | Signal/news routing. WALTER feeds NEXUS inbox; brief would surface routed-signal density + recent BOARD dispatches. Priority #3. |

**Tier-1 brief coverage: 7/12 (58%).** Missing 5 — REGINALD, OZK, RED, LIQUID, WALTER.

---

## Tier-2 / opportunistic (briefs present without Tier-1 mandate)

| Agent | Brief | Brief date | STATUS-pin | Status | Notes |
|---|---|---|---|---|---|
| **MARCO** | ✅ | 2026-06-08 | `ceffbb4a` | ✅ FRESH | Population/migration. Closed 2nd boot-maturity gap with brief. NOT Tier-1 but produced one — read when MARCO domain (FL CRE, ag-labor, Canadian boycott) is in active synthesis. |
| **OTTO** | ✅ | 2026-06-08 | (n/a — internal-ops agent) | ✅ FRESH | Maintenance / fleet-parity agent. Brief documents structural change-log; not domain-thesis intake. Read only on doc-system synthesis (rare). |
| **BOND** | ❌ | — | — | 2026-06-05 | Sub-agent / named-spawn validation 5/19. Currently feeds M-03 input list. No brief expected — covered via REGINALD/LIQUID when those rejoin brief-coverage. |

---

## Other agents (no brief expected — Tier-2 ad-hoc or dormant)

| Agent | STATUS | State | Notes |
|---|---|---|---|
| LABOR | 2026-06-08 | Tier-2 active | Upstream of transmission chain; brief not required per BOOT step 6. Read STATUS directly when chain firing. |
| HERMES | none | dormant | Messaging agent (deprecated/being-replaced per `[[project_messaging_overhaul]]`). |
| DARWIN | none | dormant | — |
| ZHAO | 2026-04-02 | ⚪ DORMANT (9+ wk stale) | TIC / China flows. Spawn-on-need. |
| HANS | 2026-04-30 | ⚪ DORMANT (5+ wk stale) | Geopolitical analysis. Spawn-on-need. |
| BARON | none | dormant | — |
| SHADE | 2026-03-27 | ⚪ DORMANT (10+ wk stale) | — |
| ORACLE | 2026-06-27 | 🟢 **ACTIVE — Tier-1 (reclassified 6/27)** | Prediction-market crowd lens (Polymarket + Kalshi). Fresh brief 6/27 = market-verdict counter-signal (Discipline D) + thin-liquidity (Discipline E). See top inventory note. |

---

## Fleet rollout priority (empirically re-driven by 6/8 cross-domain edge-diff; CARL/HENRY/BROCK now FRESH)

**Five Tier-1 briefs missing.** CARL + HENRY + BROCK stood up (all FRESH) — dropped from the queue. Remaining priority:

1. **LIQUID** 🚨 — **2 of 4 briefs waiting + DORMANT 5/21 + BLOCKING C3 energy-HY refresh AND T-08 credit-pin verification.** No longer rollout-priority — a **Will-decision** (reactivate or accept blind spot in the credit corner most exposed to live Hormuz).
2. **REGINALD** — owns M-02, M-05; transmission chain midstream; tape-not-confirming counter-signal lives here.
3. **WALTER** — primary signal routing source; brief would compress BOARD-dispatch density.
4. **RED** — adversarial; brief carries forced counter-case (load-bearing per Discipline D narrative-gap requirement).
5. **OZK** — STATUS dormant since 4/24; confirm activity first.

**Reorder rationale:** original order was load-bearing-ness only. With CARL + HENRY + BROCK now delivered, **LIQUID is the highest-value open gap** (and an explicit Will-decision, not a queue item). Let the data drive the queue.

Distribution mechanism TBD. 6/9-12 catalyst cluster has **cleared** (re-anchor 6/16); remaining rollout gated on the **post-FOMC 6/17 window** per advisor (focus protection + two-machine sync surface).

---

## Maintenance rules

- **Update on every NEXUS boot** if any agent's brief status changed (new brief, refresh, pin-bump, drift state shift).
- **Update on fleet milestone** (new brief added, new Tier-1 promoted/demoted, schema amendment changes drift rules).
- **Drift recomputed via** `git log --oneline <brief-pin>..HEAD -- AGENTS/<NAME>/STATUS.md | wc -l`. ≤1 = within threshold; ≥2 = check whether content is fresh (PIN-STALE) or genuinely behind (CONTENT-STALE).
- **Pair with `brief_fallback_log.tsv`** — when fallback fires in practice, the cause-tag (stale/convergence/uncertainty/brief-gap) informs whether the map needs updating or the agent needs a flag.
