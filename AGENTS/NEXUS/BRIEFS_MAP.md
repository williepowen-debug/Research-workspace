# NEXUS — Fleet Brief Map
**Purpose:** Single index of `NEXUS_BRIEF.md` status across the fleet. NEXUS reads this at BOOT step 6 to decide where the brief read-flow applies vs where raw STATUS fallback is mandatory.
**Updated:** 2026-07-05 Sun (8-day re-anchor sweep — current freshness is the ★7/5 note below; the ★6/27 note keeps only the MODEL-SHIFT rationale. **Pruned 7/5:** removed three dead snapshot layers — the 6/16 per-agent tables, the 6/8 rollout-priority section, and the roster-duplicating "Other agents" table — per the stale-spine-under-appended-top pattern; roster taxonomy lives in `PROME/ROSTER.md`.)
**Schema reference:** `templates/NEXUS_BRIEF_SCHEMA.md` §4.4 fallback triggers (a/b/c) + `brief_fallback_log.tsv` for run-time instrumentation.

> **★ 2026-07-05 — 8-day re-anchor sweep: ZHAO now has a brief (add to rotation); LIQUID + OZK revived; RED remains the top brief-gap.**
> Fleet scan 7/5 — **13 agents now maintain `NEXUS_BRIEF.md`** (ZHAO added a schema-conformant brief 7/4 on reactivation — PROME ask `inbox/processed/2026-07-05_from-PROME_zhao-briefs-map-add.md`, Will-approved). Freshness this pass (brief / STATUS commit date):
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
> **Brief-LESS (read raw STATUS when domain live, flag if load-bearing):** **RED** (adversarial/Discipline-D — **THE top brief-gap; STATUS content-stale 6/23, pre-6/30/NFP**), **REGINALD** (M-02/M-05 hub — 2nd gap, STATUS 6/26), **LIQUID** (⚡ REVIVED 7/2 — no longer dormant; owns X1/plumbing/demand-hole; brief would be high-value, 3rd gap), **OZK** (revived 7/4), WALTER (routing 7/4), BOND (7/1). **Tier-1 brief coverage: 9 live briefs read this pass.** RED + REGINALD + LIQUID = the three highest-value open gaps (all load-bearing, all brief-less) — **brief-standup routed to PROME 7/5** (`outbox/`).
>
> **Fallback log this pass:** BROCK/RED/LIQUID all `stale` (BROCK pin-stale brief; RED/LIQUID missing-brief) — logged to `brief_fallback_log.tsv`. *(RED/LIQUID are MISSING-brief, not `brief-gap` — no brief-quality defect to score.)*

> **★ 2026-06-27 — MODEL SHIFT (rationale, retained): the brief is FLEET-STANDARD; read-set is BRIEF-EXISTENCE-DRIVEN, not a frozen Tier-1 list.**
> A fleet-wide scan found the brief had spread well beyond the original hardcoded Tier-1. Two agents that were OFF NEXUS's read-list were added: **CORAL** (whole-Florida geography-convergence — top-priority geography, FL leg of the REGINALD/CARL transmission cluster, routes explicitly TO NEXUS) and **ORACLE** (prediction-market crowd lens — the market-verdict counter-signal / Discipline-D + thin-liquidity Discipline-E feed; had been wrongly marked DORMANT). **CLAUDE.md BOOT step 6 reframed: read every extant brief (Tier-1 in full each pass), fall back to raw STATUS for the brief-less.** *(The 6/27 freshness snapshot table is pruned 7/5 — current freshness is the ★7/5 table above.)*

---

## Legend

| Mark | Meaning |
|---|---|
| ✅ **FRESH** | Brief present + STATUS-pin commit current (0 commits drift) OR brief edited after STATUS edit. Read brief; raw STATUS only on trigger (b)/(c). |
| 🟡 **PIN-STALE** | Brief present, content current, but STATUS-pin hash not bumped. Read brief; flag pin-hygiene to that agent. NOT a (a) trigger if content is fresh. |
| 🟠 **CONTENT-STALE** | Brief present but >1 STATUS-commit behind AND brief content predates a material STATUS change. Trigger (a) fires → raw STATUS fallback + log to `brief_fallback_log.tsv`. |
| ⏳ **MISSING** | No `NEXUS_BRIEF.md` exists. Raw STATUS is the only intake. Log to fallback as cause=stale (functionally equivalent) until brief exists. |
| ⚪ **DORMANT** | Agent's own STATUS is itself stale (no recent activity). No brief expected; if NEXUS needs the domain, escalate to PROME/Will. |

*Dormant / retired / spawn-on-need roster taxonomy is NOT duplicated here — `PROME/ROSTER.md` is the single source of truth for who's live vs. shelved. This map indexes brief STATUS only.*

---

## Maintenance rules

- **Update on every NEXUS boot** if any agent's brief status changed (new brief, refresh, pin-bump, drift state shift). Refresh the ★-dated freshness note; do NOT accrete a new snapshot table under the old one (the 7/5 prune removed three such stale layers — keep ONE current freshness note).
- **Update on fleet milestone** (new brief added, new Tier-1 promoted/demoted, schema amendment changes drift rules).
- **Drift recomputed via** `git log --oneline <brief-pin>..HEAD -- AGENTS/<NAME>/STATUS.md | wc -l`. ≤1 = within threshold; ≥2 = check whether content is fresh (PIN-STALE) or genuinely behind (CONTENT-STALE). On a multi-day re-anchor, batch this fleet-wide per BOOT step 6.
- **Pair with `brief_fallback_log.tsv`** — when fallback fires in practice, the cause-tag (stale/convergence/uncertainty/brief-gap) informs whether the map needs updating or the agent needs a flag.
