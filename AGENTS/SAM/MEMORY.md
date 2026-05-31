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
- [2026-05-29] **Boot-slimming only wins when the content is DORMANT or SETTLED, not merely duplicated.** Duplication-in-two-places is necessary but not sufficient to cut: (a) THESIS deferred-Channel-1 and (b) closed-prediction post-mortems were clean cuts because they're dormant/settled reference. (c) the May 26 ESR window was equally duplicated (in `insurers/`) but DECLINED — it's the active v1.5 foundation, so thinning it hurts boot readability for ~800 tok. Test before cutting: "is this content load-bearing for the *current* thesis story?" If yes, leave it even if duplicated.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask), [[finding_shallow_clone_false_fork]] (unshallow before trusting git divergence), [[feedback_position_cost_basis_not_authoritative]] (never cite cost-basis from state files).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (5/29 PM boot → 5/31 Sunday boot)

- **🆕 CFTC weekly RELEASED** (May 30, data as of May 26): net short **-114,667** (was -93,905 May 19). **+27,152 NEW shorts WoW** (longs +6,390; net −20,762). **BROKE the -102K recent-cycle peak** we'd been watching — 4th straight build week. 63.7% of Jul-2024 -180K peak. Fuel load growing INTO the June catalyst, not covering. This is the action-item-#1 resolution.
- FXY options: ATM IV eased to **8.03%** (−0.56 vs 5/29) but 25d RR steepened to **−7.81** (from −6.35) — yen-strength convexity bid building further (thesis-side). IV down + skew up = market not pricing imminent shock on level but paying up for yen-strength tails.
- Brent **$91.12** (−$1 vs 5/29); JGB/USDJPY/FXY otherwise flat (weekend, mkt closed — Fri-cached). No new macro prints.

### LAST SESSION (5/31 Sunday — boot + CFTC release + BOJ repricing mark-up + KOYOMI docket audit)

- Clean boot, read phase steps 0-6 + market refresh. boot.py 11.3s, 9/9 green. Integrated CFTC release (-114,667, broke -102K cycle peak, 4th build week) into STATUS + CALENDAR.
- **Git housekeeping (Will-authorized cross-agent exception):** committed 4 stale PROME SIG/REPLY files (BROCK/HENRY/REGINALD inboxes+outbox) → `bfb9c654`; trashed WILL/share image via gio. Then committed SAM boot writebacks → `7614efc2`; **pushed both, origin clean** (`da1165d4..7614efc2`). CARL's "uncommitted" work from the boot snapshot had already been committed+pushed by CARL (commits 70cc4c41/3371ddf4/581b62c9) — boot snapshot was stale.
- **🆕 BIG ONE — Japan news check surfaced a stale mark: market repriced June BOJ hike to ~88%** (Polymarket 88.2% / swaps ~87.5%, both May 31; sustained ~60% May 22 → 88%, held through both CPI misses). We were carrying a stale 55-65%. **Marked SAM-21 ~50% → 70%** (Will-approved). Mechanism-over-threshold vindication. Ran the full cascade: PREDICTIONS + STATUS (banner/STATE-OF-PLAY/carry-table/BOJ-assessment/trigger-table) + TIMELINE (May 31 RESOLVED entry) + CHANGELOG (POV pivot reversing the May 28 "dovish-impaired" entry). Position unchanged; Sep $60 call still NOT warranted.
- **Lesson (calibration/process):** a market-pricing input we *poll* (Polymarket/swaps) went stale in STATUS while we tracked hard data — the divergence (50% vs 88%) was staleness, not a differentiated view. Re-poll BOJ swap/Polymarket pricing at every boot in the catalyst window, not just at named prints.
- **KOYOMI docket audit (spawned post-mark-up):** synced CALENDAR ↔ CATALYSTS.tsv to the 70% mark (TSV Jun 16 row still carried stale 55-65%), pruned >1wk resolved rows, stripped live levels. 2 escalations → both resolved: (#2) pruned the resolved May 29 CFTC row from THESIS forward table → `c405758b`; (#1) **confirmed Jun 8 Q1-GDP 2nd-prelim at ESRI = Mon Jun 8 8:50 AM JST (= ~7:50 PM ET Sun Jun 7)** + fixed ESRI source URL in RELEASES.md → `e01ee204`. All pushed, origin clean.
- **Timing note for Jun 8 GDP:** prints **Sunday evening ET (Jun 7 ~7:50 PM)**, the night before the US week opens — ahead of the Jun 10 US CPI / JGB 30Y cluster. (Bonus: full 2026 GDP calendar pulled from ESRI — next after Jun 8 is Q2 1st-prelim Aug 17; not yet logged, beyond horizon.)

### NEXT SESSION

1. **Run boot.py** — refresh market table (Monday Jun 1 = first live tape since this Sunday boot; FX/Brent will be fresh). Verify National May CPI not early. CFTC next weekly Sat Jun 6 (watch continued build past -114,667 vs first cover).
2. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, **SAM-21 70% / market ~88% (market-confirmed base case)**. **Re-verify swap/Polymarket pricing at boot Jun 9-15** (it went stale on us this cycle — see lesson above). Jun 17 FOMC co-headline (lands ~24h after = backup catalyst). National May CPI Jun 19 (post-BOJ) — watch if national core-core holds above Tokyo's 1.6%. RED CH-008 resolves here. CFTC fuel load -114,667 = more violent unwind if it fires.
3. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO-book reduction language / CEO Kitabayashi.
4. **Eval re-baseline DUE** — standing trigger now compounded (THESIS condensed + PREDICTIONS restructured + new PREDICTIONS_ARCHIVE, on top of 5/29 AM CLAUDE.md/THESIS edits). Evals carry stale $57.48; RED to self-correct $57.48→$58.32 on next boot.
5. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch.
6. **🟠 Iran/Hormuz MOU** — binary; sign → Phase 2 accelerates; collapse → intervention #3 reactivates. Terms in CALENDAR. **🟠 USDJPY 160 watch.**
7. **⏸️ DEFERRED — cross-agent signals (Will decision 5/28, still holds):** Layer B (BROCK/HANS PC-cascade pull) + HENRY carry-numbers ping shelved pending other-agent development. **Do NOT re-flag as open gaps** — captured in STATUS.
8. **Vol-proxy recalibration (infra TODO):** STRATEGY VOL SIGNALS reads FXY proxies directionally; absolute thresholds not recalibrated to proxy scale. FedWatch no auto-pull — manual check Jun 9-16.
9. **KB cleanup leftover (low-effort):** Tier-2 macro/flow rows (mirror workbook tsvs); Tier-1 per-insurer hedge ratios + Dai-ichi/Sumitomo detail (refresh if gaiyo PDFs accessible). **JICPA finalization MONITOR** (KB-108/125).
10. **Git:** CARL + BROCK/HENRY/REGINALD/WILL had uncommitted work at this boot — sync skipped. Verify origin/master clean before next pull.

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
