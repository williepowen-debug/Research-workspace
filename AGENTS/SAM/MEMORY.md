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

### CHANGES SINCE LAST SESSION (May 27 morning 09:24 ET → evening 17:44 ET, same-day continuation)

- Intraday FXY drift: $57.63 → $57.54 (-0.16% / -$0.09) — not material; position still flat to blended entry $57.48
- Intraday USDJPY: 159.41 → 159.44 — essentially flat
- Brent extended decline: $93.13 → $92.86 (-3.94% on day) — Phase 2 still firing; MOU framework hardening continues
- JGB curve unchanged (MOF still May 26)
- CPI panel unchanged
- 20d cal / 14d trd to BOJ Jun 16 (was 21d / 15d this morning)

### LAST SESSION (2026-05-27 — full day: morning v1.5 thesis bump + afternoon eval suite ship + evening v1.5 propagation sweep)

**Morning (Sumitomo retrospective integration + v1.5 thesis bump):**

3-chunk sequenced writeback after fetching Sumitomo PDFs from IR page and extracting via pdfminer. THESIS v1.4 → v1.5 (Channel 1 demoted to deferred structural backstop); CHANGELOG 2026-05-27 entry with full 3-of-3 cross-Big-3 table; STATUS rewrite with single-path framing + **Sep $60 NOT WARRANTED**; TIMELINE Sumitomo retrospective; CALENDAR rewrite; PREDICTIONS — SAM-14 FAILED, SAM-25 extended, SAM-26 ~25%; outbox signals to PROME + LIQUID.

**Afternoon (eval suite v1 → v1.1 → v1.1.1):**

Eval suite #2 picked from Will's Ideas.docx infra menu; capped at 2 cases. v1 ship → contamination caught (Case 02 verbatim phrase echo) → v1.1 split-file fix (INPUT pasteable, RUBRIC scorer-only with ⚠️ header) → v1.1 baseline ran CLEAN → v1.1.1 same-session refinement on Case 01 case-design issue (Jun $58C vs Sep $60 OTM distinguished in INPUT). Both PASS. Contamination flaw fixed; v1 → v1.1 redesign worked.

**Evening (v1.5 propagation sweep — full doc-stack audit, 12 files refreshed):**

Will flagged STRATEGY + TRADE as likely stale; confirmed and expanded to full audit. Behavioral-impact triage table built before edits per [[feedback_audit_behavioral_ranking]]; chunked into 5 phases per Will's "break it up if too much for one cycle" guidance.

- **Chunk 1 — STRATEGY.md + TRADE.md v1.5 sync.** Position A flipped AUTHORIZED → NOT WARRANTED with 4 explicit re-activation conditions (Channel 1 shock / Channel 3 reactivation / Tokyo CPI + CFTC sharpening / fiscal-dominance vehicle pivot); hard trigger tables refreshed; SAM-21 70% → ~57% propagated; Carry Unwind table to v1.5 (12/62/80); Risk Factors restructured (BOJ-delay 10% → 25% single-path elevation; new Channel-1-reactivation row at 10%).
- **Chunk 2 — RED v1.5 reset.** COUNTER_THESIS full rewrite v1.0 → v1.5 with calibration credit for CH-002 (FY2025 net buying) + CH-003 (intervention spike-and-reverse) wins. CHALLENGES restructured: 3 resolved (CH-002 + CH-003 CONFIRMED, CH-006 DISMISSED); 4 retargeted to v1.5 (CH-007 escalated 🟡 → 🟠 under single-path consensus risk; CH-001 + CH-004 downgraded). **NEW CH-008 — Fiscal-Dominance Frame (BOJ Frozen, Not Hike-Ready) from eval Case 02 baseline runner.** LOG new calibration scoreboard at top + full audit trail preserved.
- **Chunk 3 — Big 3 profile refresh (Nippon, Meiji, Sumitomo).** Decision point on retire-vs-refresh: Will pushed back on retire-Big-3 recommendation. Right call — durable narrative depth (executive quotes, PC deal specifics, source attributions, historical trajectory) can't be carried by TRACKER's table form. Refresh-with-trajectory-preservation path: added FY2025 ESR sections + v1.5 framing on top of preserved pre-FY2025 narrative. Stancorp attribution error fixed (Stancorp is Meiji's vehicle, not Nippon's; Nippon's is Resolution Life). Sumitomo profile = most narrative-rich with full asset-composition table + RED CH-002 cross-ref.
- **Chunk 4 — Mid-tier profile refresh (Dai-ichi, Norinchukin, Fukoku, Japan-Post).** Each tailored to v1.5 role, not formula-stamped. Norinchukin positioned as standalone independent Channel 1 reactivation gate (Jun FY2025). Fukoku preserved as J-ICS DOMESTIC mechanism precedent. Japan-Post = clean-read JGB seller (zero PC); CEO Sahara Mar-3 directional-right / timing-wrong calibration example.
- **Chunk 5 — closeout.** This MEMORY update + MAINTENANCE 2026-05-27-evening entry + auto-memory promotion of retire-vs-refresh lesson.

**Position:** 13 shares + 1 Jun-18 $58C unchanged. Sep $60 NOT WARRANTED resolution now coherent across STATUS, STRATEGY, TRADE (was split before this evening's sweep). Mid-session question from Will ("should I sell what I have?") answered with structured framework: v1.5 reframe is sizing decision not exit decision; thesis-break condition (USDJPY >167 AND BOJ dovish) unmet; direction conviction HIGH unchanged, timing conviction downgraded HIGH → MEDIUM. Hold shares, call separately considerable if Tokyo CPI prints in-line/hot. Will held position; no change executed.

### NEXT SESSION

1. **🟠 Thu-Fri May 28-29: Tokyo May CPI** — `cpi_japan.py` auto-pulls at boot. Core-core <1.9% → June BOJ pricing breaks lower from 55-65%, which would materially impair v1.5 single-path AND partially confirm RED CH-008 (fiscal-dominance frame). Watch Tokyo-vs-National gap.
2. **🟠 Fri May 29: CFTC weekly (May 22 data)** — watch for break of -102K cycle peak; currently -93,905 (3rd build week, 92% of peak).
3. **🟠 ongoing: Iran/Hormuz MOU framework** — binary watch. Framework hardening (Trump May 23, Axios May 24) but Tehran-obstruction friction visible. Sign → Phase 2 accelerates; collapse → Brent snapback → intervention #3 zone reactivates.
4. **🟠 USDJPY 160 watch** — currently 159.44; #3 zone dormant pending Brent direction.
5. **🔴🔴 Tue Jun 16 BOJ MPM** — DOMINANT REMAINING CATALYST under v1.5. Approach pre-cabling on Jun 13-15. RED CH-008 resolves here (BOJ hikes → CH-008 dismissed + thesis confirmed; BOJ holds + announces long-end op → CH-008 confirmed + thesis revisited).
6. **🟠 Jun FY2025 Norinchukin** — only remaining near-term Channel 1 reactivation gate. Watch for explicit CLO-book reduction language or new-CEO Kitabayashi public escalation.
7. **PROME outbox-scan check:** verify 2026-05-27 to-PROME signal lands; if not picked up within ~24h, escalate via direct surface to Will.
8. **Position next-touch:** No add/trim warranted near-term under v1.5 single-path. Only triggers for action: (a) USDJPY <156 for 3 sessions = Phase 2 confirmed → consider add; (b) BOJ pre-meeting cabling (Jun 13-15) — assess hike probability vs market pricing; (c) thesis break (USDJPY >167 + BOJ turns dovish) = stop $55.05. Jun-18 $58C theta-watch: if Tokyo CPI prints in-line/hot, consider close-into-pop for salvage (currently ~$20-30 estimated); if soft, hold as Phase 2 lottery.
9. **Eval suite re-baseline cadence:** v1.1.1 INPUT is the current frozen version. Re-baseline IF (a) Case 01 INPUT gets further refinement, (b) auto-memory `[[finding_threshold_vs_mechanism]]` is rewritten, (c) THESIS v1.5 → v1.6, (d) CLAUDE.md SPAWN PROTOCOL changes. Routine STATUS / CALENDAR updates do NOT trigger re-baseline.
10. **Uncommitted work pending push:** 12 files modified across STRATEGY/TRADE/TRACKER/RED/insurer-profiles + MEMORY/MAINTENANCE this evening. Confirm with Will whether to commit + push at session-close, or whether other agent state prevents push (per [[feedback_agent_git_isolation]] + [[feedback_check_staged_before_commit]]).

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
