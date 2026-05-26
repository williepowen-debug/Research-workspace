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
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION
*(populated at next boot — step 7 market refresh)*

### LAST SESSION (2026-05-26 evening — folder + MEMORY cleanup)

Folder cleanup Pass 1a/1b/2a/2c executed (4 dead dirs + 2 stale top-level files + 7 workbook staging files + 7 inbox + 2 outbox files; 14 trashed, 10 moved, 2 edited; commit 5a7e5c42). MEMORY.md audit + cleanup Phases 1-5: promoted threshold-vs-mechanism + audit-behavioral-ranking lessons to auto-memory; compressed Session Notes; retired 2 stale Findings (PROME SCRATCH, EUR/JPY); retired PENDING + INFRASTRUCTURE STATUS sub-sections; collapsed References. Fixed dangling [[feedback_audit_cleanup_ranking]] → [[feedback_audit_behavioral_ranking]] in MAINTENANCE. Position unchanged: 13 shares + 1 Jun-18 $58C.

### NEXT SESSION

1. **🔴 Wed May 27: Sumitomo Life FY2025 ESR** (~15:00 JST / ~2-3 AM ET). IR: sumitomolife.co.jp/about/company/ir/settlement/. Pattern-confirmation test. Check: ESR level + M&A-vs-stress decomposition; Symetra/US PC ($10.7B) update; JGB unrealized loss; foreign securities mark; explicit foreign-bond reduction language. Routing per TRACKER table: M&A-style sub-200% → 🟡 counter-thesis (v1.5 Channel 1 downgrade); stress-driven sub-200% → 🔴 LIQUID + PROME (Channel 1 reactivates); 200-220% manageable → 🟠 watch.
2. **If Sumitomo confirms M&A pattern:** write v1.5 THESIS update + CHANGELOG (old/new view); scenario weights 70/25/5 → 75/20/5; LIQUID 🟡 counter-thesis signal.
3. **If Sumitomo breaks pattern (stress-driven):** Channel 1 reactivates per TRACKER 🔴 row; consolidated LIQUID + HENRY 🔴 signal; scenario weights toward stress case 50/40/10.
4. **🟠 Thu-Fri May 28-29: Tokyo May CPI** — core-core <1.9% → June BOJ pricing breaks lower from 55-65%.
5. **🟠 Fri May 29: CFTC weekly (May 22 data)** — watch for break of -102K cycle peak.
6. **🟠 ongoing: Iran/Hormuz MOU** — binary watch (sign → Phase 2 accelerates; collapse → intervention #3 zone reactivates).
7. **Position decision deferred:** Sep $60 calls (Position A authorized) — case rests on June BOJ + CFTC reload + Sumitomo read.
