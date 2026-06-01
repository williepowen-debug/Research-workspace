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

### CHANGES SINCE LAST SESSION (5/31 Sunday boot → 6/1 Monday boot)

- **🆕 IRAN MOU EFFECTIVELY BROKEN (Jun 1):** Tehran suspended message exchange via mediators (Tasnim) + threatened to "completely block" Hormuz. WTI +7%, **Brent +4.02% to $94.78**. Pakistan-mediated 60-day framework hit hard setback (not formal collapse but document exchange halted; fresh US-Iran clashes near Hormuz). Reverses last week's "MOU framework hardening" view in 4 days.
- **🆕 FED-CUT BACKUP READS DEAD:** Jun 17 FOMC priced **>97% no-change**, **<10% cut odds anywhere in 2026** (CME FedWatch). April US CPI 3.8% (ME passthrough) + resilient labor blocking. v1.5 "24h Fed rescue" framing was a stretch.
- **🆕 BOJ pricing HELD / slight uptick:** Polymarket **88.5%** (Jun 1, was 88.2% May 31); swap 78-87.5%. Discourse now post-hike framed (MUFG, OANDA, ING). Bessent-Katayama-Himino alignment cabling hike + intervention combo per Reuters Jun 1.
- USDJPY **159.64** (+0.36y vs Fri — inside #3 verbal zone); FXY $57.51; **FXY ATM IV jumped 8.03 → 10.52% (+2.49v)** — market pricing the binary; 25d RR steepened to −8.11. JGB curve eased 3-4bp across.

### LAST SESSION (6/1 Monday — full day: boot + Jun-1 POV pivot + KURA inaugural + KOYOMI sync + sub-agent MEMORY architecture)

- Clean boot, read phase steps 0-6 + boot.py 26.1s 9/9 green. STATUS market table refreshed.
- **News sweep — 4 parallel agents (Will-approved):** Brent driver / BOJ pricing / Japan commentary / credit+insurer. Convergent finding: MOU broken + Fed-cut backup dead. High value — caught two material reframes we'd have missed.
- **Jun-1 POV pivot writeback cascade (commit `b11cefad`):** STATUS + PREDICTIONS (SAM-23 ~55→~72%) + TIMELINE (2 RESOLVED entries) + CHANGELOG (POV pivot) + CALENDAR. Pushed `4528dbc5..b11cefad`.
- **MEMORY refresh (commit `063c1d51`).**
- **KURA inaugural run on Opus 4.8 (propose-only):** 7 KB adds (KB-176/177/178/179/180/181/182) all approved + KB-137 archive (pre-existing SUPERSEDED) + KB-064 dedup-merge into KB-063 + KB-065/066 palimpsest collapse + 2 FLOW spot-stale fixes. Watermark → 2026-06-01. Net workbook math: 119 → 124 KB rows; 56 → 58 archive rows. Commit `91d08f00`.
- **KOYOMI Jun-1 sync (Opus 4.8):** caught me violating TRUTH MODEL (live spot in CALENDAR cells) + stale INTERVENTION WATCH section header. 4-cell cleanup + 1 header fix. Commit `7a7ca395`.
- **Sub-agent architecture refactor (commit `ce22c1f8`):** added `KURA_MEMORY.md` and `KOYOMI_MEMORY.md` for cross-spawn continuity (RUN LOG, PENDING, STANDING MONITORS, CALIBRATION, NEXT RUN HINTS). Spec files now reference MEMORY files in canonical spawn invocation + read-set + write-set + job sequence. Mirrors SAM's CLAUDE+MEMORY split. Promoted to auto-memory as transferable pattern.
- **VIOLET pre-staged files caught at commit time** — unstaged before SAM commit (re-validated [[feedback_check_staged_before_commit]] in real-time).
- **Hedge-ratio data-quality flag** (sub-agent returned <30% claim, conflicts with 44.4% authoritative) — NOT propagated, flagged in KURA_MEMORY PENDING + standing follow-up.

### NEXT SESSION

1. **Run boot.py** — Tue Jun 2. Verify MOU walk-back vs further escalation overnight (key: Trump/Khamenei statements; Brent direction). CFTC next release Sat Jun 6.
2. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, SAM-21 70% / mkt ~88.5%. **Re-verify swap/Polymarket pricing at boot Jun 9-15**. Pre-meeting blackout starts ~Jun 13 (T-2) — this week is the cabling window (Bessent/Katayama jawbone watch). National May CPI Jun 19 (post-BOJ). Position unchanged: 13 sh + Jun-18 $58C.
3. **🔴 Iran/Hormuz MOU watch** — broke Jun 1; SAM-23 ~72%. Binary: walk-back / Trump-Khamenei reset → resign path; further escalation → Brent $100+ / Hormuz close attempt. USDJPY 160 hard intervention trigger watch.
4. **THESIS edit pass deferred:** soften RISK FACTORS Fed-cut "24h backup" language to "multi-month tail." Flagged in CHANGELOG + TIMELINE Jun 1 entries.
5. **Hedge-ratio verification:** primary-source check on 44.4% vs <30% claim (now tracked in KURA_MEMORY PENDING).
6. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO-book reduction language / CEO Kitabayashi. CLO book reportedly down to ¥8.2T (was ¥9.7T in thesis) — verify. (Tracked in KURA_MEMORY STANDING MONITORS.)
7. **Eval re-baseline DUE** — standing trigger compounded (Jun 1 POV pivot stack on top of prior). Evals carry stale $57.48; RED to self-correct $57.48→$58.32 on next boot.
8. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05. Jun-18 $58C theta-watch (vol pop Jun 1 modestly offsets).
9. **KURA/KOYOMI next runs** — both have populated MEMORY files now; next spawns should self-orient. Validate the architecture by spawning without re-briefing in spawn prompt (just point at the spec; MEMORY does the rest). KURA's next meaningful harvest window opens post-Jun-16 BOJ.
10. **⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); vol-proxy recalibration; KB cleanup tier-2 macro/flow rows. Do NOT re-flag as open gaps.

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
