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

### CHANGES SINCE LAST SESSION (6/1 evening close-out → 6/2 Tue morning)

- **USDJPY +0.28y to 159.92** (Mon 159.64 → Tue mid-session). **0.05% from 160 hard intervention trigger.** Mon intraday already tagged 159.75 high. MOF cabling window LIVE before T-2 blackout ~Jun 13.
- **Brent +$0.89 to $95.67** (+0.94% Tue, on top of Mon +4.02%). **No Iran walk-back overnight** — MOU break sticking. Tasnim/Hormuz framing intact going into US session.
- **JGB 10Y +2.5bp to 2.682%** (Jun 1 publication). 30Y +0.4bp to 3.863%, 40Y +1.1bp to 3.800%. Modest back-up across the curve.
- **10Y JGB auction TODAY (Jun 2) orderly** — BTC 3.53x, tail 0.7bp, avg 2.649%. Confirms domestic long-end is quiet despite oil rebuild; J-ICS mechanism not compounding.
- **Polymarket BOJ Jun 16 hike: 87.6%** (Tue 16:02 UTC ≈ 12:02 ET) vs Mon 88.5%, May 31 88.2%. Held within noise. MUFG ~80%, swap 77-80% (consistent with Mon read).
- **FXY ATM IV proxy printed 1.56% Jun 2 (vs 10.52% Jun 1) — calibration glitch, not real vol collapse.** USDJPY is pushing UP with BOJ T-10; vol cannot have crushed 9pp organically. Flagged STATUS table + KURA next-run.

### LAST SESSION (6/2 Tue morning — intraday verification, no thesis-level move)

- Clean boot from WALTER cwd (Will explicitly invoked SAM identity). git in sync with origin (0/0). boot.py 7.3s, 8/9 OK + FXY OI skip.
- Tape check: USDJPY 159.92 (0.05% from 160), Brent $95.67 (+0.73% on top of Mon +4.02%), FXY $57.42. MOU break sticking.
- 10Y JGB auction TODAY orderly (BTC 3.53x, tail 0.7bp). No domestic supply-stress story.
- **Polymarket BOJ Jun 16 verified intraday at 87.6%** (Jun 2 ~12:02 ET) — held vs Mon 88.5%. SAM-21 70% mark unchanged. Cross-source: MUFG 80%, swap 77-80%.
- **FXY ATM IV proxy outlier (1.56 vs 10.52 prior day) — calibration glitch flagged.** Not a real vol crush; USDJPY pushing UP at T-10 to BOJ. Investigate proxy / consider real OTC pull for KURA next run.
- No mark changes. No position changes. SAM-23 72% held; SAM-21 70% held.
- Closeout: STATUS lead + state-of-play + market table refreshed Jun 2; MEMORY session notes; commit `4e9d7f50`.

### LAST SESSION (6/2 Tue PM — KOYOMI Run 4 + KURA Run 2 + BASELINE AUDIT spec amendment) — commit `127ae123`

Same SAM window as the AM verification (long session, likely auto-compaction in between). Re-entered with a stale boot read (08:42 morning data — USDJPY 159.35 etc, didn't see the 4e9d7f50 commit until git log). Will course-corrected the parallel-SAM misread (no parallel SAM running — earlier-me, post-compaction recall loss).

- **KOYOMI Run 4 (teams-mode):** Spawned to backfill Jun 2 10Y auction + investigate why it wasn't in CATALYSTS.tsv. Investigation surfaced a ~months-old structural exclusion — prior runs cherry-picked super-long JGB (30Y/20Y/40Y) and silently dropped 2Y/5Y belly/front. Run 4 added 13 forward events (Jun 23 5Y, Jun 30 2Y, full July inc. Tankan Q2 + JGB Jul 2/7/9/14/22/30 + BOJ Jul 30-31), corrected FOMC Jul 28-29 (vs prior Jul 30 hint), 13 RELEASES.md confirmed-dates added.
- **KURA Run 2 (teams-mode):** Low-yield post-Jun-1-inaugural window. 1 KB add proposed (**KB-183 fxy-proxy-v1 Framework** — durable caveat on the FXY vol-proxy collapse-to-near-zero failure mode caught Jun 2 boot). Watermark → 2026-06-02. Precision-over-recall held (1 vs 4 rejected).
- **Will decisions (4):** track 2Y/5Y (KOYOMI Run 4 default OK), promote FOMC Jul 28-29, approve KB-183 as Framework, ping KOYOMI back via SendMessage for spec amendment (dogfood teams-mode iterative use case).
- **BASELINE AUDIT spec amendment (two-round SendMessage):** Round 1 — KOYOMI proposed monthly + post-miss + month-rollover triggers, universe table, propose-only output. Round 2 (SAM refinement) — merged monthly + month-rollover into one trigger; added decline-memory clause via SAM-owned `## CALIBRATION` read-only signal source (mirrors KURA/METSUKE CALIBRATION ownership). Applied to `docket/KOYOMI.md` (step 2a + § BASELINE AUDIT subsection + READ-SET 7a + DONE guard + RETURN line). KOYOMI_MEMORY cleanups (3 self-resolved items removed). MAINTENANCE.md 2026-06-02 AM entry logged.
- **Auto-memory promotions (2):** `finding_teams_mode_iterative_tasks` (when SendMessage earns vs synchronous spawn; default mental model bias correction) + `finding_subagent_baseline_audit` (set-maintenance sub-agents need explicit baseline-scope audit + decline-memory; incremental-update rubrics silently extend-from-precedent).
- **No thesis/STATUS/PREDICTIONS/CHANGELOG changes** this thread. Spec/process work only.
- Commit `127ae123` (KOYOMI spec amendment + KOYOMI_MEMORY cleanups + MAINTENANCE log) held for coordinated SAM+OTTO+REGINALD push.

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

### LAST SESSION — POST-14:56 ADDENDUM (3 commits after the MEMORY closeout pass; power loss hit after the 18:07 push)

- **16:03 `8b319c7c` — CLAUDE.md FILES table:** added KURA_MEMORY + KOYOMI_MEMORY entries; pointed KURA.md / KOYOMI.md rows at the new MEMORY pair-files. Codifies the sub-agent CLAUDE+MEMORY split in the boot-loaded spec.
- **17:35 `8a2f830c` — TRADE.md Jun 1 refresh:** 2-pass state-sync + thesis-loaded (header, thesis para, live P/L, all 6 Tranche 2 hard-triggers, Carry Unwind table, EWJ + Japan Banks triggers, EWJ MOU anti-trigger flipped inactive, Key Dates pruned + Jun 10 US CPI added, Risk Factors mitigation columns). Plus Position A inline partial-trigger disclosure (#3 partial via wrong leg) + Fed Path softened to multi-month tail. Mini-pass: Decision Card header relabeled + TLT watchlist v1.5 note (Channel 1 deferred → near-term TLT-put not warranted from Japan side). Position 13 sh + Jun-18 $58C unchanged.
- **18:07 `0414f49a` — THESIS surgical sync (closes NEXT-SESSION item 4):** 7 surgical edits propagating the Jun 1 POV pivot into THESIS body — header banner, Forward catalyst table (MOU watch + Intervention #3 row SAM-23 ~72%), Phase 2 Current state, "Why secondary path now" paragraph, "Timing key" paragraph rewritten from "24h rescue catalyst" → "multi-month tail not Jun-window," tripwires table Jun 1 annotations, RISK FACTORS BOJ-delays mitigation rewritten ("closer to pure downside than v1.5 originally framed"). Probabilities HELD by design (25%/15%/12%); explicit inline notes flag re-rate as separate deliberate decision pending escalation trajectory. No version bump.

### LAST SESSION — JUN 1 EVENING (post-power-loss; 3 SAM commits)

Will lost power after the 18:07 push; came back, asked SAM to verify closeout state and refresh MEMORY. Then proposed developing a 3rd sub-agent for TRADE/STRATEGY. Pushback-then-scope-tightening on the design, then ship + inaugural shakedown run.

- **18:24 `aab9ada2` — MEMORY post-power-loss reconciliation:** confirmed last commit `0414f49a` did close NEXT-SESSION item 4 (THESIS Fed-cut "24h backup" → "multi-month tail" softening landed in 7 surgical edits). Added LAST SESSION POST-14:56 ADDENDUM documenting the 3 commits between the 14:56 MEMORY closeout and the power loss at 18:07. Removed item 4; renumbered NEXT SESSION 5→4 down to 9 items. No mid-flight WIP lost.
- **19:31 `1c5e011d` — METSUKE introduction (3rd SAM sub-agent):** following KURA/KOYOMI pattern but **propose-only across the board** (no `full` mode equivalent). Mandate: hold TRADE.md + STRATEGY.md against current STATUS / THESIS / PREDICTIONS / CHANGELOG / TIMELINE / docket, return categorized drift report; SAM applies. Forbidden to touch money fields (cost basis, position size, stops, strikes, expiries, premium) — honors `[[feedback_position_cost_basis_not_authoritative]]`. 8-category drift taxonomy (STALE-MARK, STALE-FRAMING, DUP-LIVE-SPOT, TRIGGER-STATUS-DRIFT, CAL-DRIFT, ARCHIVE-CANDIDATE, MONEY-FIELD-ESCALATION, CHANGELOG-GAP). Files: `METSUKE.md` (193 lines spec) + `METSUKE_MEMORY.md` (103 lines state) at SAM root next to TRADE/STRATEGY. CLAUDE.md FILES table + write-back step 12a updated.
- **22:33 `288dae59` — METSUKE Run 1 inaugural sweep applied:** 19 flags, S/N 94.7%, 18 applied / 1 declined-with-carve-out. TRADE.md: 3 edits (live-spot strips on USDJPY-sub-155 + JGB 30Y trigger rows; Jun 10 JGB 30Y auction added to Key Dates). STRATEGY.md: 15 edits (header + Position/Thesis line + Stage 3 paragraph rewrite + Stage 4 + 4 hard-trigger rows + HOLD section + Jun-18 exit rule #3 vol-crush + Position A re-activation #3 + 2 VOL SIGNALS table rows + Current read flipped 2-of-3 → **3-of-3 directional** + Key Check Dates wholesale + CHANGELOG entry). METSUKE_MEMORY closeout: SAM-applied/declined filled, **CALIBRATION populated** (STALE-MARK 100% / STALE-FRAMING 100% / DUP-LIVE-SPOT 75% with position-card carve-out established / TRIGGER-STATUS-DRIFT 100% / CAL-DRIFT 100% with mechanism-relevance test / money-field discipline held 0/19), PENDING cleared (4/4 Run-1 items resolved this turn).
- **One decline of note:** TRADE:37 Entry Decision Card Live P/L line (`−1.4% at FXY $57.51`) flagged as DUP-LIVE-SPOT. Will kept it ("keep but unsure"). Carve-out logged: **position-card tracking fields are exempt from the no-dup-spot rule**; the rule applies to forward-trigger / forward-event / threshold-status rows only. METSUKE will not re-flag this pattern.
- **3-of-3 vol convergence** is the substantive thesis-side finding from Run 1 — ATM IV the prior laggard (~8%) has now turned UP (Jun 1 ~10.5%, +2.5v expansion as market starts pricing the BOJ binary), RR proxy steepened further (−8.11 vs −5.76). All 3 legs corroborating = highest-conviction zone per the convergence table. When hard trigger fires (BOJ Jun 16), act immediately per exit rules.

### NEXT SESSION

1. **🔴 USDJPY 160 watch** — 159.92 at Tue mid-session, 0.05% from hard trigger. Intervention #3 may fire intraday/this week pre T-2 blackout (~Jun 13). Monitor: Reuters/Bloomberg MOF headlines, Bessent/Katayama verbals (cabling window LIVE this week). If 160 prints → SAM-23 resolves (not re-rates).
2. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, SAM-21 70% / Polymarket 87.6% (verified Jun 2 intraday). **Re-verify pricing Jun 9-15.** If pricing holds >85% through cabling week with no Takaichi pushback → consider +5pp mark to 75%. National May CPI Jun 19 (post-BOJ). Position unchanged: 13 sh + Jun-18 $58C.
3. **🔴 Iran/Hormuz MOU watch** — broke Jun 1; SAM-23 ~72%. Brent +0.73% Tue confirms no walk-back overnight. Binary still: walk-back / Trump-Khamenei reset → resign path; further escalation → Brent $100+ / Hormuz close attempt.
4. **🆕 FXY ATM IV proxy investigation** — Jun 2 reading 1.56 vs Jun 1 10.52 is non-physical (USDJPY rising into BOJ binary; vol should be UP not down). Likely scraper calibration. Check `fxy_options.py` source / consider real OTC pull next session. **Now also durably captured as KB-183** (fxy-proxy-v1 Framework caveat — read sign/trend not absolute).
5. **Hedge-ratio verification:** primary-source check on 44.4% vs <30% claim (tracked in KURA_MEMORY PENDING).
6. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO-book reduction language / CEO Kitabayashi. CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. (Tracked in KURA_MEMORY STANDING MONITORS.)
7. **Eval re-baseline DUE** — standing trigger compounded. Evals carry stale $57.48; RED self-correct $57.48→$58.32 on next boot.
8. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) thesis break (USDJPY >167 + BOJ dovish) = stop $55.05.
9. **KURA / KOYOMI / METSUKE next runs** — all 3 have populated MEMORY files. Natural cadence: **METSUKE** Jun 9-15 pre-BOJ window OR on next material POV pivot; **KOYOMI + KURA** post-Jun-16 BOJ. Validate architecture by spawning without re-briefing. **KOYOMI BASELINE AUDIT first fires first run of July** (monthly trigger per amended spec) — covers Jul + Aug forward window vs MOF/BOJ/Fed source.
10. **🆕 Push coordination pending:** commit `127ae123` held for SAM+OTTO+REGINALD coordinated push. Will managing the timing — do not push solo on next boot; check with Will.
11. **🆕 KOYOMI_MEMORY ## CALIBRATION** — section deliberately NOT scaffolded (propose-to-seed). Seed structure when first declination happens: `### Declined release classes` (date + reason per line) + optional `### Accepted proposals` (pattern-tracking). Placement: between STANDING MONITORS and NEXT RUN HINTS.
12. **⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2 macro/flow rows. Do NOT re-flag.

**🟢 RESOLVED THIS SESSION (full Tue, AM + PM):** Polymarket BOJ pricing intraday verification (87.6% — held; from Mon close-out NEXT item 1); KOYOMI Jun-2 10Y backfill + structural 2Y/5Y gap closed; FOMC Jul 28-29 promoted to CATALYSTS.tsv + CALENDAR.md; KB-183 promoted (FXY vol-proxy caveat); KOYOMI spec extended with BASELINE AUDIT (Run-4 PENDING auto-resolves); teams-mode iterative-task pattern validated via SendMessage round-trip (auto-memory promoted).

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
