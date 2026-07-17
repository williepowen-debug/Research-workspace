# NEXUS — Fleet Brief Map
**Purpose:** Single index of `NEXUS_BRIEF.md` status across the fleet. NEXUS reads this at BOOT step 6 to decide where the brief read-flow applies vs where raw STATUS fallback is mandatory.
**Updated:** 2026-07-17 Fri (full pin-hygiene brief-read loop — the owed 7/16 item, executed. Current freshness = the ★7/17 note below; ★6/27 keeps the MODEL-SHIFT rationale only. Prior ★7/5/★7/16 snapshot layers replaced per the no-accretion rule.)
**Schema reference:** `templates/NEXUS_BRIEF_SCHEMA.md` §4.4 fallback triggers (a/b/c) + `brief_fallback_log.tsv` for run-time instrumentation.

> **★ 2026-07-17 — full pin-hygiene loop (the owed 7/16 item, DONE). The brief fleet EXPANDED 13 → 23** since the 7/5 map: the three "highest-value gaps" (RED, REGINALD, LIQUID) all stood up briefs ~7/6-7/10 (the 7/5 brief-standup routing landed), and the six DAEDALUS-built agents (FALCON, OSPREY, HOMER, VULCAN, WATT, MIDAS) + AEOLUS all carry schema-conformant briefs. Freshness (brief / STATUS commit dates, scanned 7/17):
> | Verdict | Agents | Note |
> |---|---|---|
> | ✅ FRESH, read this pass | **ORACLE 7/17, CORAL 7/17, HOMER 7/17, BRENT 7/17, FALCON 7/17** (BRENT/FALCON also via 7/17 outbox memos); CARL 7/16, SAM 7/16, HENRY 7/16 (7/16-anchor reads re-verified — content matches STATUS) | ORACLE's is load-bearing this pass (NEH crack, premium-not-shortage crowd corroboration, July-CPI disinflation counter-signal — all folded to STATUS 7/17) |
> | ✅ Fresh-but-agent-quiet | LABOR 7/9 (STATUS 7/10, self-flagged stale-note honest; LAB-17 window 7/23-30 next), RED 7/10, VIOLET 7/11, ZHAO 7/16, WATT 7/16, MARCO 7/9, AEOLUS 7/9, MIDAS 7/12, OSPREY 7/12, OTTO 7/4 (T2) | Brief = last-session state; the staleness is the AGENT's, not the brief's |
> | 🟠 CONTENT-STALE → raw-STATUS fallback taken | **BROCK** (brief 7/9 vs STATUS 7/17 — read 7/17 memo direct), **REGINALD** (brief 7/9 vs STATUS 7/16 — read raw: bank-read benign cohort, CHG-RED-040, CCC/HY armed 1-of-3), **VULCAN** (brief 7/12 vs STATUS 7/17 — 7/17 memo via packet), **LIQUID** (brief 7/6 vs STATUS 7/11 — read raw: LIQ-06, SOFR-short decomp) | All logged `stale` in fallback log |
> | ⏳ Reclassified / not read | HAWK 7/12 (cross-war synthesis + dormant book since the OSPREY/FALCON split — theater intake now via FALCON/OSPREY direct; read HAWK only for cross-war synthesis questions) | Not a fallback event |
>
> **⚠️ AGENT-staleness flags (freshness *discipline*, not brief quality — 9a decision rule):** **VIOLET dark since 7/11** — through the MOVE 77.77 spike/round-trip, its own domain's core event (GATE-VIO-116 was graded by TERRY/PROME in its absence); **RED dark since 7/10** — the adversarial layer missed the entire re-fire window (closure, arm-#2, CPI) exactly when the bear book upgraded; **LIQUID dark since 7/11** — X1 owner dark through the closure week (mitigant: hy_oas_watch systemd timer runs between sessions; LIQ-06 pre-reg covered the week mechanically). All three flagged to PROME via outbox 7/17.
> **Brief-LESS (raw STATUS when live):** **BOND** — now the TOP brief gap (load-bearing M-03/M-10 input, read via memos each anchor), **SHADE** (BROCK→SHADE double-jeopardy node), **OZK**, WALTER (architectural, no brief expected), TERRY (trade-construction surface, reads NEXUS not vice-versa — consumes my STATUS as its regime PIN, refreshed 7/17).
> **9a fallback-rate rollup (first formal pass, trailing 6/16→7/17, 16 rows):** causes = **100% `stale`-class** (incl. missing-brief rows), **zero `brief-gap`, zero (b)/(c)** logged. Read: NO brief-quality defect anywhere in the fleet — the standard is working; the dominant failure mode is **agent-session staleness during event windows** (the three flags above). No fix-or-drop conversations warranted. *(Caveat: (b)/(c) under-logging is possible — event-driven anchors read memos direct, which the log doesn't capture as fallbacks.)*

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
