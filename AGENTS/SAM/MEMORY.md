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
- [2026-05-29] **Will likes the flag-then-fetch stepwise method for big refreshes** — flag stale items first (review), THEN fetch newer data tier-by-tier. Keeps scope controlled and lets him gate each tier. Applied to the KB freshness pass; worked well.

## Findings
- [2026-05-29] **Shallow-clone "false fork" illusion in web sessions.** Claude-Code web containers clone SHALLOW (`.git/shallow` graft present). `git merge-base` / `rev-list --left-right` then falsely report NO common ancestor + huge divergence — saw "53 ahead / 50 behind, unrelated histories" when the branch was really just **3 ahead / 1 behind** master. Fix: at boot, `git rev-parse --is-shallow-repository`; if true, `git fetch --unshallow origin` before trusting ANY ahead/behind or merge-base. Don't panic at apparent forks in web sessions. Auto-memory promotion candidate.
- [2026-05-28] **Position cost-basis in state files was inaccurate — recorded "$57.48 blend" vs $58.32 actual (Will ground truth).** Recorded per-tranche fills (8 @ $57.36 + 5 @ $57.66) didn't even reconcile (avg can't exceed both components). Flipped live P/L +0.4% → **−1.1%**, R:R 1:1.86 → 1:1.13. **Never cite position cost-basis / P/L from STATUS-file figures as authoritative — confirm with Will (CLAUDE.md rule #3 + #4).** Auto-memory promotion candidate.
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (2026-05-28 boot → 2026-05-29 workbook session)

- **No market refresh this session** — focused workbook/KB maintenance, NOT a boot. STATUS market table still as of 5/28 13:57 ET; next instance must run boot.py.
- **🔴 Tokyo May CPI + CFTC weekly (due Fri 5/29) NOT yet pulled** — were "tomorrow" last session, now today/just-passed. Next session: `cpi_japan.py` + CFTC. These resolve the directional read on SAM-21 / June BOJ.
- No events processed; v1.5 single-path holds.

### LAST SESSION (2026-05-29 — workbook audit + KB freshness refresh + branch/PR resolution)

- **Workbook audit (Will-requested):** reviewed all 12 workbook tsvs — found clean. Fixed 3 minor items (commit `77d687e`): USDJPY 5/25↔5/26 row-order swap; FLOW-3.01 CLO ¥9.7T→¥9.2T clarity; **added KB-175** documenting that 40Y/Climate uniform-price (Dutch) auctions → blank avg-yield/tail is CORRECT-by-construction (verified at MOF), not a parse bug. 40Y demand read is BTC-only.
- **KB freshness — flag-then-fetch:** flagged 23 stale LIVE rows in 3 tiers.
  - **Tier 1 (`95ea3b7`, 14 rows):** FY2025 insurer actuals. Nippon ESR 222→195% (M&A, not stress) + bond loss -¥3.6T→-¥5.73T (first impairment); Meiji -¥1.386T→-¥2.16T; Dai-ichi ~$20B est→~¥2T actual (disclosed, ESR ~220%); Sumitomo ~$15B est→¥1.518T (tripled); Big-4 agg → ~¥11.4T/$67B (¥14T outlier flagged); KB-137 SUPERSEDED. Industry hedge 44.4% confirmed still latest. Per-insurer hedge ratios flagged stale (NOT fabricated).
  - **Tier 3 (`b52f993`, 7 rows):** resolution checks. PC cascade Q2 = redemption PEAK (BofA: Apollo 15%/Ares 14%/BCRED 12%+gating, Blue Owl OCIC/OTIC 28.5%/52.9%); JICPA STILL PENDING (no finalization found); BOJ gauge core-core +2.7% Feb + gauge(>2%)-vs-headline(1.4%) divergence; repointed "May 1"→Jun 16, Brent $115→~$92.
- **Branch/PR resolution:** Will flagged "on a branch not master." Diagnosed shallow-clone false-fork (see Finding) — real state 3 ahead/1 behind. Opened **PR #1** → merged via merge commit (`2279198`). **All 3 commits + this MEMORY update now flowing to master.**
- **NOT done:** Tier 2 KB cleanup (deferred); market refresh (no boot).

### NEXT SESSION

1. **🔴 FIRST: pull Tokyo May CPI + CFTC weekly (5/29)** — were due today, NOT pulled. `cpi_japan.py` + CFTC. Core-core <1.9% → June BOJ pricing breaks lower from 55-65%. Resolves SAM-21 directional read.
2. **Run boot.py** — STATUS market table stale at 5/28 13:57 ET.
3. **🔴🔴 Tue Jun 16 BOJ MPM** — DOMINANT catalyst. Pre-cable Jun 13-15; Jun 17 FOMC co-headline. RED CH-008 resolves here.
4. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; watch CLO-book reduction language / CEO Kitabayashi.
5. **Tier 2 KB cleanup (deferred 5/29):** stale macro/flow rows — KB-131/132/133/134 (MOF flows, now in MOF_FLOWS.tsv), 050 (10Y level), 116/117 (rate-diff/breakeven "~150"), 138 (JGB levels), 154 (real wages, in VX), 155 (consumer/prime), 136 (UST indirect bidder), 139/140/141 (Japan UST $1.1T→$1,239.3B + check Mar/Apr TIC). Mostly mirror workbook tsvs → low-effort.
6. **JICPA finalization MONITOR** — pending past Mar 17 comment close; no final standard as of late May (KB-108/125). Check JICPA site.
7. **PC cascade Q2 peak (KB-152)** — fresh escalation; consider surfacing to BROCK/HANS (v1.5 secondary Fed-cut path). Messaging mid-overhaul — flag to Will, don't over-invest in outbox.
8. **🟠 Iran/Hormuz MOU** — binary; sign → Phase 2 accelerates; collapse → intervention #3 reactivates. **🟠 USDJPY 160 watch** (159.21 at last refresh).
9. **Eval re-baseline DUE** — CLAUDE.md docket-path + KOYOMI changes are standing trigger; evals carry stale $57.48. RED to self-correct $57.48→$58.32 on next boot.
10. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch.
11. **Tier-1 leftover:** per-insurer hedge ratios + Dai-ichi/Sumitomo FY2025 detail flagged stale — refresh if individual gaiyo PDFs accessible.
12. **Git:** PR #1 merged to master (`2279198`); MEMORY update is a follow-up PR. Verify origin/master sync at boot (re: shallow-clone Finding).

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
