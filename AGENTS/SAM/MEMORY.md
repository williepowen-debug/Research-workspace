# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or auto-memory, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. Lean toward restraint on thesis-level updates; one data point rarely justifies 15-25pp probability shifts.
- [2026-05-25] **Will wants gap-check before writebacks.** When SAM proposes writebacks, Will asks "any other searches?" — surfaces gaps the synthesis missed. Build in a "what's still missing?" beat before executing multi-file passes.

## Findings
- [2026-05-28] **Position cost-basis in state files was inaccurate — recorded "$57.48 blend" vs $58.32 actual (Will ground truth).** The recorded per-tranche fills (8 @ $57.36 + 5 @ $57.66) were estimates that didn't even reconcile — an average can't exceed both components, so the fills were wrong, not just the blend. Flipped live P/L from "+0.4%" to **−1.1%** and R:R from 1:1.86 to 1:1.13. **Never cite position cost-basis / P/L from STATUS-file figures as authoritative — confirm with Will (CLAUDE.md rule #3 data-can-be-hallucinated + #4 prices-live).** Auto-memory promotion candidate.
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (May 27 evening → May 28 13:57 ET)

- FXY $57.54 → $57.65 (+$0.11); position **−1.1% vs $58.32 avg cost** (corrected from bad "$57.48 blend" 2026-05-28 — Will ground truth; see Findings)
- USDJPY 159.44 → 159.21 (-0.23, marginally firmer); EUR/GBP/AUD-JPY all near flat
- Brent $92.86 → $92.46 — Phase 2 still firing; MOU framework hardening continues
- JGB curve published May 27 (was May 26): 10Y 2.687 (-2.6bp), 30Y 3.856 (-1bp), 40Y 3.796 (-4bp) — SAM-26 deeper FALSE (30Y now 14bp below 4.0%)
- CFTC unchanged at -93,905 (next release TOMORROW Fri May 29)
- No events resolved; v1.5 single-path holds
- BOJ Jun 16 now 13 trd days out

### LAST SESSION (2026-05-28 — boot + git-sync verify + KOYOMI house-in-order)

**Boot + market refresh:** clean pull (fast-forward b5d5e12a → 8c186608, brought the docket reorg from another instance). boot.py 9/9 green. Refreshed STATUS market table + banner to May 28 levels.

**Git-sync verification (Will's request):** confirmed local HEAD == origin/master (8c186608), 0 ahead / 0 behind — latest safely saved local. Working-tree changes all SAM-owned (STATUS + 3 boot.py workbook appends). Untracked files belong to other agents — left untouched.

**KOYOMI house-in-order (the session's main work):** Will spawned KOYOMI for the FIRST time as a named/persistent teammate for a shakedown run; locked in **she/her**. First run caught a real CALENDAR↔CATALYSTS divergence (CALENDAR missing 6–7 forward events) and surfaced 3 design questions. Will decided all 3 → I encoded them:
- **TRUTH MODEL (split ownership):** CATALYSTS.tsv owns the dated-event SET; CALENDAR owns narrative/thresholds; neither carries live spot.
- **Prune by CALENDAR's own >1-week rule, not on sight** (KOYOMI's instinct; codified).
- **Strip live spot from CALENDAR** (KOYOMI executed round 2 — forward monitors stripped, resolved-outcome records left intact).
- Built **`docket/RELEASES.md`** (recurring-releases reference: cadence rules + official schedule links + confirmed-dates scratchpad); updated KOYOMI.md spec; web-verified Jun 8 GDP date (cadence-consistent, ⚠️ pending ESRI). Full structural detail in MAINTENANCE 2026-05-28 (PM) entry. **Prototype validated — Will likes the pattern; KOYOMI now operational.**

**Tier-1 doc updates:** MAINTENANCE 5/28 (PM) entry + MEMORY rewrite.

**Position cost-basis correction (Will ground truth):** Will corrected avg cost to **$58.32** (13 sh) — prior "$57.48 blend" (8 @ $57.36 + 5 @ $57.66) was inaccurate (avg can't exceed both fills). Propagated across STATUS/TRADE/STRATEGY/MEMORY; P/L flipped +0.4% → −1.1%, R:R 1:1.86 → 1:1.13, stop now 5.6% below cost, breakeven $58.32 above spot. Logged Finding (above). **TRADE.md cleanups also done:** Position A "still authorized" leftover → NOT WARRANTED; embedded spot genericized to "see STATUS"; dates tidied (+FOMC Jun 17). **SIG dropped to RED** (`red/SIG-FROM-SAM-2026-05-28...`) to correct its $57.48 refs on next boot.

**Committed + pushed:** cb3f9b97 (12 files, SAM-scoped). Origin synced 0/0.

**KOYOMI top-sheet design Q (resolved — NO build):** Will asked whether KOYOMI should synthesize an at-a-glance state sheet. Decided against: I only boot-read CALENDAR.md (not the whole docket), so a top-sheet saves no reading; the only real gap (cross-session escalation orphaning) is covered by routing unresolved KOYOMI escalations into this MEMORY NEXT SESSION list (zero-cost, no new file/sync surface). Also: KOYOMI must NOT synthesize the macro "situation" — that's STATUS (analysis line). Revisit a dedicated STATE.md only if KOYOMI's scope grows to multiple dockets.

**Position:** 13 sh @ $58.32 avg + 1 Jun-18 $58C (ACTIVE), both unchanged. No action warranted today — quiet tape, no thresholds tripped, v1.5 single-path intact; shares modestly underwater (−1.1%), breakeven above spot.

### NEXT SESSION

1. **🔴 Fri May 29: Tokyo May CPI** (tomorrow, 1 trd day) — `cpi_japan.py` auto-pulls. Core-core <1.9% → June BOJ pricing breaks lower from 55-65%, materially impairing v1.5 single-path AND partially confirming RED CH-008. Watch Tokyo-vs-National gap. **Resolves the directional read on SAM-21.**
2. **🔴 Fri May 29: CFTC weekly (May 22 data)** (tomorrow) — watch for break of -102K cycle peak; currently -93,905 (3rd build week, 92% of peak).
3. **🟠 ongoing: Iran/Hormuz MOU framework** — binary. Sign → Phase 2 accelerates; collapse → Brent snapback → intervention #3 zone reactivates.
4. **🟠 USDJPY 160 watch** — currently 159.21; #3 zone dormant pending Brent direction.
5. **🔴🔴 Tue Jun 16 BOJ MPM** (13 trd days) — DOMINANT REMAINING CATALYST. Pre-cable Jun 13-15. RED CH-008 resolves here. Note Jun 17 FOMC now lands 24h later (rate-diff other half) — co-headline cluster.
6. **🟠 Jun FY2025 Norinchukin** — only remaining near-term Channel 1 reactivation gate. Watch for CLO-book reduction language / CEO Kitabayashi escalation.
7. **⚠️ Eval re-baseline DUE:** today's CLAUDE.md SPAWN PROTOCOL change (docket path + KOYOMI step 10) is a standing re-baseline trigger (criterion d). Will runs evals in a fresh skip-boot session — flag at next opportunity.
8. **outbox PROME/LIQUID pickup:** 5/27 v1.5-demotion (PROME) + channel-1-deferred (LIQUID) signals still in `outbox/` (not delivered/). Verify integration or surface to Will. (Messaging mid-overhaul — don't over-invest.)
9. **KOYOMI now operational** — spawn for sizeable docket refreshes (e.g. post-BOJ Jun 16 event cluster), not quiet days. Standing rules in `docket/KOYOMI.md` + `docket/RELEASES.md`. **Escalation convention:** route any unresolved KOYOMI escalation into this NEXT SESSION list (decided 5/28 — no top-sheet). Open KOYOMI escalation carried forward: **Jun 8 GDP 2nd-prelim date** is cadence-derived (⚠️ in RELEASES.md), confirm at ESRI when it nears.
10. **RED to self-correct** the $57.48 → $58.32 basis in COUNTER_THESIS on its next boot (SIG dropped); evals also still carry $57.48 in frozen inputs — folds into the re-baseline (#7).
11. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-meeting cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch: if Tokyo CPI in-line/hot, consider close-into-pop for salvage; if soft, hold as Phase 2 lottery.
12. **Git:** clean at last session-close (cb3f9b97 pushed, origin 0/0). This MEMORY closeout edit is the only pending commit.

### NEXT INFRA SESSION (script build queue — unchanged from prior session)

When time allows for non-thesis work, in this priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape. Same pattern as `mof_flows.py`. June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR (mechanism-aware routing already specified). ~30 min build.
2. **`insurer_quartr.py`** — Quartr-based watcher for Big 3 mutuals + Norinchukin + mid-tier (7 tracked insurers). Scope question first: does Quartr have all 7? Architectural call — building this opens Quartr pattern for BOJ/Treasury/corp IR later. ~45-60 min build + auth/workspace setup.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. Quartr or direct scrape boj.or.jp. ~45 min build. Less time-pressure (next SoO ~Jun 26).
4. **`boj_swap_pricing.py`** — Re-recon Polymarket/Kalshi for BOJ rate markets (was previously blocked on "no good free source"). 10-min recon, then build only if source exists.

Also deferred (low priority):
- Pass 2b: `insurers/<name>.md` per-insurer profiles retire-vs-refresh — Big 3 state now fully known post-v1.5; can be tackled. Promote in priority once Tokyo CPI + CFTC week settles.
- Pass 3: `research/` reorg into outputs/+archive/ — cosmetic, defer indefinitely.
- SIGNAL_INTAKE.md full refresh — pending messaging-system overhaul decision.
