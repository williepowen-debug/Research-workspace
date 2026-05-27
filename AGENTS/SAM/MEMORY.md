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

### CHANGES SINCE LAST SESSION (overnight May 26 PM → May 27 09:24 ET)

- **Sumitomo Life printed FY2025 ESR May 26 (same day as Nippon + Meiji, NOT May 27 as historical pattern suggested)** — ESR ↑+19pt to 197% with foreign book GROWING +¥1.11T. Found retrospectively via IR sweep May 27 boot.
- USDJPY drifted 159.24 → 159.41 (+0.17) — yen WEAKER on no remaining Channel 1 yen-bullish catalyst.
- FXY -$0.07 to $57.63 (-0.12%); position +0.3% on blended entry.
- JGB long-end retraced further: 30Y 3.931% → 3.866% (-7bp); 40Y 3.921% → 3.836% (-9bp); 10Y 2.749% → 2.713% (-4bp). SAM-26 mark-down 30% → 25%.
- Brent -3.66% intraday to $93.13 on Iran/Hormuz MOU framework hardening (Phase 2 still firing but rate-diff dominating yen response).
- CPI panel live for first time at boot — April national core 1.4 / core-core 1.9 / Tokyo April matches (+0.4pp gap = subsidy-driven, BOJ can look through).

### LAST SESSION (2026-05-27 morning — Sumitomo retrospective integration + v1.5 thesis bump)

3-chunk sequenced writeback after fetching Sumitomo PDFs from IR page and extracting via pdfminer:
- **Chunk 1:** THESIS v1.4 → v1.5 (Channel 1 demoted to deferred structural backstop); CHANGELOG 2026-05-27 entry with full 3-of-3 cross-Big-3 table + old/new view + scenario weights 70/25/5 → 78/18/4 + carry unwind probs 17/65/83 → 12/62/80; Channel 1 v1.5 verdict block inline in THESIS Channel 1 section; risk factors revised (BOJ-delay elevated to 25%, intervention failure lowered to 12%, added Channel-1-reactivation at 10%).
- **Chunk 2:** STATUS full rewrite (new v1.5 banner, May 27 09:24 ET market data, single-path framing, **Sep $60 call decision logged as NOT WARRANTED**); TIMELINE Sumitomo entry logged retrospectively in May 26 cluster with asset composition table + Symetra detail; CALENDAR full rewrite (Big 3 ESR pruned from forward-looking; June 16 BOJ flagged as DOMINANT REMAINING CATALYST single-path; "v1.5 deferred structural backstop" section reframes Channel 1 monitors).
- **Chunk 3:** PREDICTIONS — SAM-14 moved OPEN → FAILED (4-of-4 Big 4 confirmation against UST reduction); SAM-25 extended (Sumitomo confirms 3-of-3 threshold-vs-mechanism trap); SAM-26 mark-down to 25%; calibration scoreboard preamble updated with new failure-pattern point (mechanism-direction assumption); outbox signals written to PROME (🟡 v1.5 reframe) + LIQUID (🟡 no acute UST sell from Japan lifer side for 2026).

**Position:** 13 shares + 1 Jun-18 $58C unchanged. Sep $60 calls (Position A, deferred from May 21) explicitly resolved as NOT WARRANTED under v1.5 single-path structure.

### NEXT SESSION

1. **🟠 Thu-Fri May 28-29: Tokyo May CPI** — `cpi_japan.py` auto-pulls at boot. Core-core <1.9% → June BOJ pricing breaks lower from 55-65%, which would materially impair v1.5 single-path. Watch Tokyo-vs-National gap.
2. **🟠 Fri May 29: CFTC weekly (May 22 data)** — watch for break of -102K cycle peak; currently -93,905 (3rd build week, 92% of peak).
3. **🟠 ongoing: Iran/Hormuz MOU framework** — binary watch. Framework hardening (Trump May 23, Axios May 24) but Tehran-obstruction friction visible. Sign → Phase 2 accelerates; collapse → Brent snapback → intervention #3 zone reactivates.
4. **🟠 USDJPY 160 watch** — currently 159.41; #3 zone dormant pending Brent direction.
5. **🔴🔴 Tue Jun 16 BOJ MPM** — DOMINANT REMAINING CATALYST under v1.5. Approach pre-cabling on Jun 13-15.
6. **PROME outbox-scan check:** verify 2026-05-27 to-PROME signal lands; if not picked up within ~24h, escalate via direct surface to Will.
7. **Position next-touch:** No add/trim warranted near-term under v1.5 single-path. Only triggers for action: (a) USDJPY <156 for 3 sessions = Phase 2 confirmed → consider add; (b) BOJ pre-meeting cabling (Jun 13-15) — assess hike probability vs market pricing; (c) thesis break (USDJPY >167 + BOJ turns dovish) = stop $55.05.

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
