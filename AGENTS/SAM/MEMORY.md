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
- [2026-05-28] **Will likes the flag-then-fetch stepwise method for big refreshes** — flag stale items first (review), THEN fetch newer data tier-by-tier. Keeps scope controlled and lets him gate each tier. Applied to the KB freshness pass; worked well.

## Findings
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask), [[finding_shallow_clone_false_fork]] (unshallow before trusting git divergence), [[feedback_position_cost_basis_not_authoritative]] (never cite cost-basis from state files).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (5/28 PM boot → 5/29 AM boot)

- **Overnight Japan (Fri Tokyo session):** April **activity beat** — IP +0.8% MoM (vs −0.4% exp; semis/AI capex) + retail sales +2.1% YoY (vs +1.4% exp). Hawkish counterweight to Tue's dovish Tokyo CPI. **Iran/Hormuz temporary ceasefire-extension** reported (60d + nuclear talks) → Nikkei +2.5%; energy lower. Takaichi ¥3T budget (5/25) surfaced + logged.
- Markets flat at boot: USDJPY 159.28, FXY $57.62, Brent $92.08, JGB 30Y 3.896% (5/28 MOF pub).
- **CFTC weekly did NOT release 5/29 AM** — still -93,905 (May 19). CFTC COT drops ~3:30pm ET Fri; with Memorial Day (Mon 5/25) it may slip to **Mon Jun 1**. Action item #1 below.

### LAST SESSION (5/29 AM — Japan news log + boot-file staleness audit + TIMELINE archive sweep; committed+pushed `cf29a3d2`)

- **Boot:** git sync clean (FF, only SIGNALS files moved); boot.py 9/9 green; STATUS market table refreshed to 5/29.
- **Japan news log (Will asked "any overnight news?"):** activity beat → **SAM-21 HELD ~50%** (balanced coin-flip — soft price / firm activity, NOT drifting lower; one activity print doesn't move a coin-flip but rebalances the split). Logged to STATUS BOJ assessment + TIMELINE (5/29 entry) + Takaichi budget (5/25 retro entry) + SAM-21 note.
- **Staleness audit (Will-requested):** found THESIS never got the 5/28 Tokyo-CPI downgrade → contradicted STATUS on the June-BOJ probability (THESIS ~57-70% vs STATUS ~50%). **Fix: replaced hardcoded probabilities/levels in THESIS with pointers to STATUS** (one-liner, Channel 2 block, triggers, OIL-IN-YEN — which had a **$107.84 / May-21 stale price**, forward table, cross-agent links) so they can't re-rot. SAM-15 flagged OPEN-FOR-REVIEW. Headers bumped; CLAUDE.md SIGNAL_INTAKE v1.4→v1.5 + insurers retire-decision marked actionable; MEMORY date-stamp note pruned + 2 findings promoted to auto-memory ([[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]]); logged to MAINTENANCE.
- **TIMELINE archive sweep (Will-requested, examined-before-cut):** MOU framework terms preserved to CALENDAR FIRST (the one at-risk item), THEN 130 lines of May 11-25 narrative moved verbatim to ARCHIVE.md (lossless, scripted w/ boundary asserts). Active TIMELINE **296→172 lines**. Branch-point table trimmed (8 resolved rows) + stale marks fixed. **Cold-boot footprint ~38.7K→~34.9K tokens (~19.4%→~17.5%).**
- **Git:** committed `cf29a3d2` (11 files), pushed clean FF to origin (CARL active but untouched — push doesn't touch working tree; origin hadn't advanced).

### NEXT SESSION

1. **🟠 FIRST: pull CFTC weekly — STILL PENDING from 5/29** (didn't release AM; slips to PM 5/29 or **Mon Jun 1** on Memorial Day). `cftc_jpy.py`. Watch break of -102K cycle peak (-93,905, 3rd build week).
2. **🪙 CONTINUE BOOT-SLIMMING (Will's stated focus for the fresh window).** Footprint now ~34.9K tok (~17.5%). Remaining targets, ranked: (a) **THESIS deferred-Channel-1 detail** → condense the "evidence it's happening NOW" / private-credit-amplifier / flow-scenario depth, point to `research/outputs/` (~2-3K, Channel 1 is DEFERRED so it shouldn't carry ~25% of THESIS); (b) **PREDICTIONS verbose post-mortems** (SAM-25/14/scoreboard) → keep one-line lessons inline, move blow-by-blow to a calibration archive (~1-2K); (c) **May 26 per-insurer ESR deep-dives in TIMELINE** → keep cross-Big-3 synthesis table, archive line-items (~2wk out, too recent now); (d) **auto-memory index growth** (~3.4K, ~60 entries, loads every agent's boot) = cross-agent flag, raise with system-org effort, not SAM-only. **Measure with boot.py + wc before/after each cut. Same discipline as the TIMELINE pass: verify the finding is captured elsewhere before archiving.**
3. **Run boot.py** — refresh market table; verify National May CPI not early.
4. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, ~50%/dovish-impaired. Jun 17 FOMC co-headline (lands ~24h after = backup catalyst). National May CPI Jun 19 (post-BOJ) — watch if national core-core holds above Tokyo's 1.6%. RED CH-008 resolves here.
5. **🔴 SAM-15 REVIEW** — "oil-in-yen forces repatriation" @80%, FLAGGED. Premise complicated by Phase-1 inversion + Brent collapse + Big-3 foreign-book growth. Reassess / restate / resolve FAILED-in-spirit (cf SAM-25). Don't leave at 80%.
6. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO-book reduction language / CEO Kitabayashi.
7. **Eval re-baseline DUE** — standing trigger now compounded (CLAUDE.md edited again 5/29 + THESIS pointers + TIMELINE restructure). Evals carry stale $57.48; RED to self-correct $57.48→$58.32 on next boot.
8. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch.
9. **🟠 Iran/Hormuz MOU** — binary; sign → Phase 2 accelerates; collapse → intervention #3 reactivates. Terms now in CALENDAR. **🟠 USDJPY 160 watch.**
10. **⏸️ DEFERRED — cross-agent signals (Will decision 5/28, still holds):** Layer B (BROCK/HANS PC-cascade pull) + HENRY carry-numbers ping shelved pending other-agent development. **Do NOT re-flag as open gaps** — captured in STATUS. Re-activate when recipients developed.
11. **Vol-proxy recalibration (infra TODO):** STRATEGY VOL SIGNALS reads FXY proxies directionally; absolute thresholds not yet recalibrated to proxy scale. FedWatch has no auto-pull — manual check Jun 9-16.
12. **KB cleanup leftover (low-effort):** Tier-2 macro/flow rows (KB-131/132/133/134, 050, 116/117, 138, 154, 155, 136, 139/140/141 — mirror workbook tsvs); Tier-1 per-insurer hedge ratios + Dai-ichi/Sumitomo detail (refresh if gaiyo PDFs accessible). **JICPA finalization MONITOR** (KB-108/125 — check site).
13. **Git:** `cf29a3d2` pushed to origin, in sync at closeout. This MEMORY closeout = follow-up commit. Verify origin/master sync at boot.

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
