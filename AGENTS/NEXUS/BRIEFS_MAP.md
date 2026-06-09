# NEXUS — Fleet Brief Map
**Purpose:** Single index of `NEXUS_BRIEF.md` status across the fleet. NEXUS reads this at BOOT step 6 to decide where the brief read-flow applies vs where raw STATUS fallback is mandatory.
**Updated:** 2026-06-08 Mon PM
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
| **CARL** | ❌ | — | — | 2026-06-08 | n/a | ⏳ MISSING | US macro / labor / CPI. Highest-volume domain agent; brief priority #1. STATUS active. |
| **REGINALD** | ❌ | — | — | 2026-06-08 | n/a | ⏳ MISSING | Regional banks / CRE. Mid-stream of LABOR→CARL→REGINALD chain. Priority #2. STATUS active. |
| **OZK** | ❌ | — | — | 2026-04-24 | n/a | ⚪ DORMANT | Spun out from REGINALD 4/24; STATUS not refreshed since. Confirm activity status before pressing for brief. |
| **SAM** | ✅ | 2026-06-07 | `6f4e531f` | `b3803c35` | +1 | ✅ FRESH | **Pilot consumer.** Schema/template ratified through SAM's brief 6/7. Drift = 1 commit (within schema threshold). |
| **RED** | ❌ | — | — | 2026-06-03 | n/a | ⏳ MISSING | Adversarial / steelman. Brief should carry counter-case to current convergences. Priority #3. |
| **BROCK** | ❌ | — | — | 2026-06-08 | n/a | ⏳ MISSING | Private credit / BDCs. M-02 + M-05 owner. STATUS active. Priority #2. |
| **LIQUID** | ❌ | — | — | 2026-05-21 | n/a | ⚪ DORMANT | Plumbing / funding. STATUS 18 days old; confirm activity before pressing. |
| **HENRY** | ❌ | — | — | 2026-06-07 | n/a | ⏳ MISSING | Velocity / tape / vol gamma. M-07 + market-structure owner. Priority #2. |
| **HAWK** | ✅ | 2026-06-08 | `8844b6a7` | `8844b6a7` | 0 | ✅ FRESH | Geopolitical / Iran war. Recent damage→salvo regime reframe; leakage-not-volume tail. |
| **BRENT** | ✅ | 2026-06-08 | `ce65758f` | `3ffba885` | +2 | 🟡 PIN-STALE | Brief content covers rev-5 BRT-27/28 work (commit `3ffba885`) but STATUS-pin not bumped. Content fresh; pin-hygiene flag to BRENT. |
| **VIOLET** | ✅ | 2026-06-08 | `725f1ffb` | `725f1ffb` | 0 | ✅ FRESH | VIX / vol structure. Fade-leaning two-leg pathway; CPI gate Wed 6/10. |
| **WALTER** | ❌ | — | — | 2026-06-07 | n/a | ⏳ MISSING | Signal/news routing. WALTER feeds NEXUS inbox; brief would surface routed-signal density + recent BOARD dispatches. Priority #3. |

**Tier-1 brief coverage: 4/12 (33%).** Missing 8 — fleet rollout pending.

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

## Fleet rollout priority (empirically re-driven by 6/8 cross-domain edge-diff)

Eight Tier-1 briefs missing. **Priority order re-driven by SENDING-vs-WAITING diff across the 4 fresh briefs** — not by convergence-matrix load-bearing alone. Empirical gap evidence reorders the original list:

1. **CARL** ⚠️ — **3 of 4 briefs explicitly waiting on him** (USD/USD-persistence, May CPI tail, post-NFP read). Touches M-01, M-06, transmission chain upstream. Highest empirical demand.
2. **HENRY** ⚠️ — **3 of 4 briefs waiting** (vol regime, breadth/gamma on AI-unwind, energy-CPI digestion). Owns M-04 (partially), M-07. (Was originally #4; promoted by gap data.)
3. **LIQUID** 🚨 — **2 of 4 briefs waiting + DORMANT 5/21 + BLOCKING C3 energy-HY refresh AND T-08 credit-pin verification.** This is no longer rollout-priority — it's a **Will-decision** (see LAST_COMPLETION blocker #X: reactivate or accept blind spot in credit corner most exposed to live Hormuz). Promoted from "last" to "needs explicit Will-decision."
4. **BROCK** — owns M-02 substance, PRED-36/37/38/40 prediction load. SAM + VIOLET also waiting on PC-cascade signal.
5. **REGINALD** — owns M-02, M-05; transmission chain midstream; tape-not-confirming counter-signal lives here.
6. **WALTER** — primary signal routing source; brief would compress BOARD-dispatch density.
7. **RED** — adversarial; brief carries forced counter-case (load-bearing per Discipline D narrative-gap requirement).
8. **OZK** — STATUS dormant since 4/24; confirm activity first.

**Reorder rationale:** original order was load-bearing-ness only. Empirical gaps say CARL + HENRY + LIQUID dissolve most of the open uncertainty across the 4 briefs already read. Let the data drive the queue.

Distribution mechanism TBD. **DEFERRED until after 6/9-12 catalyst cluster clears** per advisor (focus protection + two-machine sync surface).

---

## Maintenance rules

- **Update on every NEXUS boot** if any agent's brief status changed (new brief, refresh, pin-bump, drift state shift).
- **Update on fleet milestone** (new brief added, new Tier-1 promoted/demoted, schema amendment changes drift rules).
- **Drift recomputed via** `git log --oneline <brief-pin>..HEAD -- AGENTS/<NAME>/STATUS.md | wc -l`. ≤1 = within threshold; ≥2 = check whether content is fresh (PIN-STALE) or genuinely behind (CONTENT-STALE).
- **Pair with `brief_fallback_log.tsv`** — when fallback fires in practice, the cause-tag (stale/convergence/uncertainty/brief-gap) informs whether the map needs updating or the agent needs a flag.
