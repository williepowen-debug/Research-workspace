# NEXUS — Fleet Brief Map
**Purpose:** Single index of `NEXUS_BRIEF.md` status across the fleet. NEXUS reads this at BOOT step 6 to decide where the brief read-flow applies vs where raw STATUS fallback is mandatory.
**Updated:** 2026-06-16 Tue PM (CARL brief landed 10:55 + re-scoped to consumer-stress; coverage 6/12 → 7/12)
**Schema reference:** `templates/NEXUS_BRIEF_SCHEMA.md` §4.4 fallback triggers (a/b/c) + `brief_fallback_log.tsv` for run-time instrumentation.

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

## Tier-1 (12 agents — primary brief intake per CLAUDE.md BOOT step 6)

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
| ORACLE | 2026-04-02 | ⚪ DORMANT (9+ wk stale) | — |

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
