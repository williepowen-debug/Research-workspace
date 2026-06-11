# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or auto-memory, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. One data point rarely justifies 15-25pp probability shifts.
- [2026-05-25] **Will wants gap-check before writebacks.** When SAM proposes writebacks, Will asks "any other searches?" — surfaces gaps the synthesis missed. Build in a "what's still missing?" beat before executing multi-file passes.
- [2026-05-28] **Will likes the flag-then-fetch stepwise method for big refreshes** — flag stale items first (review), THEN fetch newer data tier-by-tier.
- [2026-06-04] **Subagent-trio habit run pays off immediately** — first parallel-spawn (METSUKE+KOYOMI+KURA, teams-mode) caught a TRADE:246 Rule #3 propagation gap I missed, primary-source verified Sato characterization, surfaced KURA-KOYOMI dependency pattern. Consistency-over-yield validated even on low-watermark days (KURA Run 4 was "low-yield" but produced KB-185 + 2 auto-memory candidates). Codified pattern.

## Findings
- [2026-05-12] **Read intraday extremes, not just closes.** Add intraday-range alert when single-day range >2.5y (Apr 30 intervention misread = misattribution to Tokyo session).
- [2026-05-29] **Boot-slimming wins only when content is DORMANT or SETTLED, not merely duplicated.** Test before cutting: "is this content load-bearing for the *current* thesis story?" If yes, leave it even if duplicated.
- [2026-06-04] **Sato verify pattern — agent-claimed characterizations need primary-source confirm BEFORE propagation into multiple docs.** Rule #3 instance: news-sweep verify agent claimed "Sato joins Jun 16" → I propagated to 4 docs; KOYOMI Run 6 primary-source verify caught the date error (actual Jun 30) + confirmed the rest. **Default: when an agent-output drives multi-doc cascade, primary-source verify the load-bearing facts BEFORE the cascade, not after.**
- [2026-06-09] **boot.py "Days since touch: X → Nd, MOF Y" — parse carefully.** "Nd" = days since LAST touch of level X, NOT consecutive days above X. "MOF Y" = the most recent MOF op that pushed below the prior level (labels now MonYYYY after Jun-10 script fix). **Default: never propagate script-derived counts/dates without re-reading the script's source semantics; verify price history independently before claiming "Nth consecutive day" or "N days above X."**
- *(Promoted to auto-memory Jun 10: [[finding_ohlc_verify_before_session_claims]], [[finding_pre_registration_discipline_through_corroboration]] — Advisor-endorsed, Will-forwarded; veto = delete files + index lines.)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Wed Jun 10 ~6 PM → ~9 PM ET, evening session — same-day continuation #3)

- USDJPY 160.53 (5th day at/above #3 trigger zone, STILL no MOF strike), FXY $57.17. **Brent $95.62 electronic (+2.7%)** — recovery off Tue's $89.59 tag extends hard; cum-from-Jun-3-baseline back to ≈−1.2%, so SAM-23 mark-DOWN leg (i) (cum ≥−2%) is no longer met. **MOF weekly (May 31-Jun 6, fresh print): net BUYING** — no repatriation signal. JGB Jun-9 pub unchanged.

### LAST SESSION (Wed Jun 10 evening — RED packet remainder CLOSED: CH-010/011/032 responses filed pre-blackout. **PUSH DONE ~9:15 PM ET:** Will opened the window; 8-commit train swept to origin (3 SAM + VIOLET + 4 WALTER); SAM tree clean and synced — no pending push.)

- **🔴 RED PRE-BOJ PACKET CLOSED** (`research/2026-06-10_ch010_011_032_responses.md` + outbox to RED): **CH-010 ACCEPTED** — STRATEGY Branch C split C1 (political attribution → vindicate/widen) / C2 (fiscal/long-end → CH-008 scores instead) / C-ambiguous (provisional 10-15pp + post-mortem); one hold can't pay both frames. **CH-011 ACCEPTED IN SUBSTANCE — SAM-23 re-derived 72% → ~35% (band 25-45), APPLY SAT JUN 13**: MOF trigger is disorder-not-level (4 days at 160+ no strike falsifies level-anchor; orderly USD-driven tape = no G7 cover/efficacy per CH-003; post-hold spike branch is outside the "before June BOJ" scoring window). Cut deeper than RED's implied 47-57 — derived, not anchored. Absorbs carry-forward #6 (trigger-spec re-anchoring → post-Jun-16 CHANGELOG). Void conditions: strike before Sat / disorderly session (>1.5y range) / 161.5+ break. **CH-032 ACCEPTED DIRECTIONALLY — target band reclassified (interim flag): modal 3-6mo ≈ FXY $57.5-59.5 / USDJPY 154-160; $60-62 = conditional-tail ~25-30% (4 routes)**; hold-row backstop language replaced ("structural pillars carry" retired); THESIS POSITION VIEW + STRATEGY header annotated; full pillar re-derive stays v1.6's job. Pushback recorded: yen-short washout is mechanically yen-POSITIVE (RED's P4 point survives as "fuel dissipates quietly"). **CH-004 RESOLVED-CONVERGED concurred; VX-RED-024 concurred.** CHANGELOG entry written (no version bump, no marks moved tonight).
- **Closeout drift sweep (step 12a, direct — METSUKE rides post-BOJ):** TRADE.md thesis paragraph carried the unflagged $60-62 band + SAM-23 72% — CH-032/CH-011 flags added so all four band surfaces (THESIS, STRATEGY, TRADE, response doc) now read consistent.
- Earlier Wed sessions (Norinchukin gate, CH-009 hold≈10%/SAM-21→~90, v1.6 rewrite spec, trade_balance_japan.py, $58C HOLD) — see TIMELINE/STATUS/CHANGELOG; all carried.

**Evening blocks (after the 4 afternoon commits below):**
- **Auto-memory index TRIMMED** (31.8→24.8KB incl. promotion, was truncating at boot; 119 entries kept, content-preserving; generator checked first — repair-tool only, hand-curated by design). **Promotions ruled:** catalyst_path_decoupling PROMOTED (sibling cross-refs to threshold_vs_mechanism); apostrophe-strip FOLDED into number_carries; counter-frame-3Q DEFERRED post-BOJ (two-instance standard).
- **CH-009 ACCEPTED IN SUBSTANCE** — see NEXT SESSION item 0 (hold ~10% / SAM-21 ~90 lands Sat).
- **🔴 v1.6 DEBRIEF (Will + Orch — load-bearing):** thesis re-derivation agreed from "Fed hiking + Japan structural buyer" ground truth. **Full spec: `proposals/2026-06-10_v16_rewrite_spec.md`** — evidence discrimination (supported/contradicted/regime-conditional/silent), 5 guardrails (incl. RED pass before version commit), 3 named agenda items: **A. position re-underwrite incl. FXY-vehicle question; B. PROME network-reframe packet (feed sign-inversion, coordinated); C. tripwire re-aim — hedge-cost thread first (the one mechanism that re-links Japan→US transmission under hike-regime).** Headline self-assessment ratified: right on Japan-domestic mechanics, wrong on Japan→US transmission.

### (Afternoon blocks — Wed Jun 10 ~1-6 PM ET)

- **🔴 NORINCHUKIN FY2025 GATE RESOLVED NOT REACTIVATED** (`fa6d6c25`): results were out May 21 (IR-403 coverage gap #3) — net income ¥121.4B beat; **CLO record ¥10.1T (+¥1.8T YoY) — "¥9.7T shrinking / ¥500B Q1 decline" FALSIFIED vs bank primary** (verified by own PDF extraction pre-cascade). 4-of-4 institutions against forced-selling. Full sweep: norinchukin.md canonical, TRACKER 7 spots, THESIS (Ch1 bullet + →LIQUID line + risk row), CHANGELOG, STATUS, TIMELINE, FLOW-3.01→ARMED-DORMANT, KB-186, 2 research supersede banners, stale May-27 outbox correction header, NEW LIQUID outbox 🟠 (cc HANS/BROCK via PROME). Post-BOJ agenda: Channel-1 10% row / deferred-vs-retired.
- **Brent settle refinement** (`513a8ca2`, Orch independent re-pull): Jun-9 walk-back CONFIRMED every leg ✓; "$92.40 evening" was post-settle electronic quote — Tue settle $91.45, cum −5.5% settle-basis, conclusions unchanged. Futures-settle rule appended to auto-memory OHLC finding (`337f0cfc`, Will-directed).
- **`trade_balance_japan.py` BUILT** (`6a287a66`): selftest 6/6 exact vs MOF primary (Apr bal ¥301,905M byte-exact; crude −63.7; ME crude −67.2; Jan XML-vs-CSV Δ0.00%); 14-mo backfill (crude cliff 11,041→4,480 kKL = April event); boot.py-wired fast-exit. **DOCKET CORRECTION: May TB provisional = Jun 17 08:50 JST = ~7:50 PM ET TUE JUN 16 (BOJ evening ET), was "Jun 18"; June TB = Jul 22.** KOYOMI informed (customs.go.jp calendar → pinning sources).
- **METSUKE step-12a judgment: skipped this session** — THESIS move was watch-item resolution not POV pivot; TRADE/STRATEGY swept directly where affected; rides with post-BOJ trio.
- **No position changes, no probability re-marks** (SAM-21 75%, SAM-23 72%, buckets held for Sat Jun 13).

### NEXT SESSION

**Imminent (the BOJ week):**

0. ~~RED pre-BOJ stress-test~~ — **✅ PACKET CLOSED Jun 10 evening** (CH-009 PM + CH-010/011/032 evening; `research/2026-06-10_ch010_011_032_responses.md`; outbox to RED). All re-derivations queued into Sat Jun 13. Scoring: Jun 16 binary + disposition branches by Jun 18 EOD JST; post-re-mark SAM/RED marks are adjacent not opposed.

1. **🟠 Sat Jun 13 CFTC (Jun 9 data) — last pre-blackout read + CONSOLIDATED RE-MARK, NOW FIVE INPUTS:** (a) CFTC gate (-153K escalates amplifier +8-10pp; -108K cover flips OFF); (b) taper-pause fold-in (hawkish-tail shrinks); (c) Fed-cut anchor #4 → ~0 (re-verify hike-pricing held; mature Fed-flip CHANGELOG candidate if so); (d) **SAM-21 75% → ~90 per CH-009** (void: dovish leak Jun 11-12 / swaps <85%); (e) **SAM-23 72% → ~35 per CH-011** (void: strike before Sat / disorderly session / 161.5+; **30d/60d MOF anchor restructured scenario-weighted** — post-hold high, post-hike fading, not flat SAM-23 extension). Downstream same pass: reconciled-table weights ~65/10/25 → ~80/10/10, event EV, Branch-C prior, **buckets ship to LIQUID/HENRY**. Also confirm CH-032 band-flag holds (Fed-hike pricing re-verify is shared input).

2. **🔴🔴 Blackout starts ~Jun 13 (T-2)** — pre-event deadline for any re-position/re-mark.

3. **🔴🔴 Tue Jun 16 BOJ MPM — apply the pre-registered frames, don't re-derive:** (a) outcome expectation = STRATEGY § JUN-16 RECONCILED EXPECTATION (modal −1 to +2% + vol crush, no unwind; hawkish-of-pricing ~10% = +5-8%; hold 25% = −3-5% event-capped; call sells into any spike); (b) ceiling disposition = STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches, score by Jun 18 EOD JST); (c) $58C tail-estimate test (market ~3-4% vs SAM ~10%). SAM-21/24 resolve on own terms; SAM-23 resolves (intervention by Jun 16); SAM-26 resolves (30Y vs 4.0% through meeting).

4. **🔴 Wed Jun 17 FOMC + dots** — ~99% hold priced; watch dots for HIKE-lean (regime-flip confirmation), not for rescue.

5. **🔴 Thu Jun 18:** $58C expiry (sell-into-pop salvage if spike). **May TB moved: provisional lands Wed Jun 17 08:50 JST = ~7:50 PM ET TUE JUN 16 — same ET evening as BOJ-decision day** (date pinned Jun 10 from MOF calendar; was "Jun 18"). Run `trade_balance_japan.py --consensus <wire>` that evening; adjudicate routing branch (a/b/c per CALENDAR). Fri Jun 19 National May CPI (post-BOJ check).

**Carry-forward (open):**

6. **SAM-23 framework re-anchoring (CHANGELOG entry, post-Jun-16) — substance now settled via CH-011:** trigger spec gains driver/disorder dimension + no-strike decay clause (level-trigger falsified as sufficient condition, 4 days at 160+). Write the formal entry after Jun 16 settles SAM-23's scoring.

7. **RED post-BOJ refresh (cites verified ✅):** targets = (a) hold-scenario response; (b) structural pillars' multi-month TIMING (now framed by the CH-032 interim band — modal $57.5-59.5); (c) SAM-23 path-decoupling (CH-011 closed the pre-event half; post-event half = scenario-weighted intervention anchor); (d) Fed-hike repricing strengthening CH-005 — handed via CH-032 acceptance.

8. **Post-BOJ stack — NOW GOVERNED BY `proposals/2026-06-10_v16_rewrite_spec.md` (Will+Orch-endorsed):** **v1.6 re-derivation** (evidence-discrimination framework + 5 guardrails; AFTER Jun 16-18 scoring; RED pass on draft pillars BEFORE version commit) + named items **A. position re-underwrite (13 shares, incl. FXY-vehicle question — Will decides, ~Jun 18 post-settle)**, **B. PROME network-reframe packet on v1.6 ship**, **C. hedge-cost tripwire build (first re-link mechanism; calendar hooks in spec)**. Channel-1 deferred-vs-retired folds INTO the v1.6 pass (4-of-4 against). Also: METSUKE+KOYOMI+KURA trio (KURA Run 6 seeds: taper-pause if delivered, subsidy-mask wedge, no-strike-at-160, Norinchukin ¥10.1T falsification); eval re-baseline; OS.1 close disposition; Dec-1.25% second-source re-verify if Branch A fires.

9. ~~Auto-memory 3 candidates~~ — **✅ RULED Jun 10 PM (Will, Orch-concurred):** index TRIMMED first (31.8→24.5KB, 119 entries kept, was truncating at load); `catalyst_path_decoupling` PROMOTED (sibling cross-refs to threshold-vs-mechanism both ways; KB-186 draft dropped per KURA note); `apostrophe_strip` FOLDED into `number_carries_threshold_unit_source`; `counter_frame_3_question_disposition` DEFERRED to post-BOJ second instance (two-instance standard).

10. ~~Norinchukin FY2025 CLO check~~ — **✅ RESOLVED Jun 10 PM (Will-directed pull):** results were out May 21 — net income ¥121.4B beat, **CLO record ¥10.1T (+¥1.8T YoY) — "shrinking" claim FALSIFIED**, gate NOT reactivated, 4-of-4 institutions against forced-selling. Full sweep done (norinchukin.md canonical, TRACKER, THESIS+CHANGELOG, STATUS, TIMELINE, FLOW-3.01/3.03, KB-186, TRADE, research-doc supersede banner, LIQUID outbox 🟠). Known-unknown: UST split undisclosed. Next read ~Nov 2026 interim.

11. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) pre-cabling Jun 13-15; (c) post-Jun-16 thesis break = BOJ dovish AND USDJPY 167+/no MOF. **NEXUS_BRIEF rollout = Will-action.** 🟡 KB-183 close at next cleanup. KOYOMI informational: Jun-10 US CPI resolved via web (BLS page 403 retrospective-confirmed moot); Jun-2 10Y row pruned Jun 10 ✅.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
