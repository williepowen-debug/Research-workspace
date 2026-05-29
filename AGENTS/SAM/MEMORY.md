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

### CHANGES SINCE LAST SESSION (5/29 AM boot → 5/29 PM boot)

- Same-day continuation. Markets flat: boot.py 12:15 ET → USDJPY 159.24, FXY $57.63, Brent $91.27 (−1.5%), JGB 30Y 3.896% (5/28 MOF pub). No new prints.
- **CFTC weekly STILL not released** — TSV ends May 19 (-93,905, 3rd build week). COT drops ~3:30pm ET Fri; may slip to **Mon Jun 1** on Memorial Day. Action item #1 below.

### LAST SESSION (5/29 PM — boot-slimming targets a+b + SAM-15 resolution)

- **Boot-slimming target (a):** condensed THESIS deferred-Channel-1 legacy mechanism depth (mechanism bullets / "evidence NOW" / "FLOWS at base pace" / hedge-ratio + private-credit paragraphs) → compact reference block with `research/outputs/` pointers. Verified all three blocks captured in research first (hedge-ratio verbatim in NORINCHUKIN:71, PC in PRIVATE_CREDIT, flow-scenarios in UST_DEEP_DIVE). **Preserved:** v1.5 demotion status, Lifer Long-End Abandonment (kept-live DOMESTIC JGB driver), 78/18/4 weights. THESIS **267→235 ln / 4125→3646 w**.
- **Boot-slimming target (b):** moved 9 closed-prediction post-mortems (8 FAILED + SAM-25) **verbatim** to new `thesis/PREDICTIONS_ARCHIVE.md` (option i — one-line lesson + `#sam-NN` anchor kept inline per row). Preserved scoreboard preamble (load-bearing per boot step 6) + all OPEN/CONFIRMED rows. PREDICTIONS **2481→1741 w**. Lossless verified; TSV col-integrity intact.
- **SAM-15 resolved FAILED (mechanism falsified)** — cleared the 80% OPEN-FOR-REVIEW flag. All 4 sub-claims contradicted (oil premise evaporated, deficit→liquidation inverted, rate-differential dominated, insurers grew foreign books). NEW failure-pattern cluster (6): premise-dependence + standalone-channel overreach. Scoreboard now **7C / 8F / 1RS / 4O**.
- **Combined ~1,050 w off cold-boot footprint.** Logged: 2 MAINTENANCE entries (a, b — structural), 1 CHANGELOG entry (SAM-15, view-neutral).
- **Then:** Will requested a fresh boot-process audit (in progress at this writeback).

### NEXT SESSION

1. **🟠 FIRST: pull CFTC weekly — STILL PENDING** (didn't release 5/29 AM or by 12:15 PM; slips to PM 5/29 or **Mon Jun 1** on Memorial Day). `cftc_jpy.py`. Watch break of -102K cycle peak (-93,905, 3rd build week).
2. **🪙 BOOT-SLIMMING — remaining targets.** Done this session: (a) THESIS Channel 1, (b) PREDICTIONS. Remaining, ranked: (c) **May 26 per-insurer ESR deep-dives in TIMELINE** → keep cross-Big-3 synthesis table, archive line-items (still ~recent — judge staleness); (d) **auto-memory index growth** (~60 entries, loads every agent's boot) = cross-agent flag, raise with system-org effort, not SAM-only. **Measure w/ wc before/after; verify captured elsewhere before archiving.**
3. **Run boot.py** — refresh market table; verify National May CPI not early.
4. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, ~50%/dovish-impaired. Jun 17 FOMC co-headline (lands ~24h after = backup catalyst). National May CPI Jun 19 (post-BOJ) — watch if national core-core holds above Tokyo's 1.6%. RED CH-008 resolves here.
5. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO-book reduction language / CEO Kitabayashi.
6. **Eval re-baseline DUE** — standing trigger now compounded (THESIS condensed + PREDICTIONS restructured + new PREDICTIONS_ARCHIVE this session, on top of 5/29 AM CLAUDE.md/THESIS edits). Evals carry stale $57.48; RED to self-correct $57.48→$58.32 on next boot.
7. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch.
8. **🟠 Iran/Hormuz MOU** — binary; sign → Phase 2 accelerates; collapse → intervention #3 reactivates. Terms in CALENDAR. **🟠 USDJPY 160 watch.**
9. **⏸️ DEFERRED — cross-agent signals (Will decision 5/28, still holds):** Layer B (BROCK/HANS PC-cascade pull) + HENRY carry-numbers ping shelved pending other-agent development. **Do NOT re-flag as open gaps** — captured in STATUS.
10. **Vol-proxy recalibration (infra TODO):** STRATEGY VOL SIGNALS reads FXY proxies directionally; absolute thresholds not recalibrated to proxy scale. FedWatch no auto-pull — manual check Jun 9-16.
11. **KB cleanup leftover (low-effort):** Tier-2 macro/flow rows (mirror workbook tsvs); Tier-1 per-insurer hedge ratios + Dai-ichi/Sumitomo detail (refresh if gaiyo PDFs accessible). **JICPA finalization MONITOR** (KB-108/125).
12. **Git:** verify origin/master sync at boot.

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
