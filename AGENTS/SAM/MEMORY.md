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

### CHANGES SINCE LAST SESSION (Wed Jun 10 ~1 PM → ~6 PM ET, PM session — same-day continuation)

- Market flat through the PM: USDJPY 160.46 (still above #3 trigger, no MOF strike), FXY $57.20, Brent $93.28 (+2.0%, recovering off Tue's tag), JGB Jun-9 pub unchanged. Polymarket BOJ >96% holding.
- **🔴 RED filed Will-directed pre-BOJ stress-test against SAM** (`RED/challenges/SAM_PREBOJ_STRESSTEST_2026-06-10.md`, routed via PROME, **deadline ~Jun 13 blackout**): CHG-RED-029 STRONG (23pp discount regime-transfer — earned vs 55-75% market, applied at 98%; RED marks hold 5-10% vs SAM 25%; asks re-derive SIZE pre-blackout), 030 (Branch-C threshold-vs-mechanism + CH-008 double-count), 031 (SAM-23 cross-pair inversion — pairs with carry-forward re-anchoring item), 032 (Fed-flip impairs all 4 pillars; CH-005-strengthened). VX-RED-024: fully-priced BOJ = no US-paper transmission. Auto-memory [[finding_calibration_discount_regime_conditional]] landed same theme.
- Morning session's items (CPI hot-as-expected, Fed cut→HIKE flip, $58C HOLD, ceiling disposition) — see TIMELINE/STATUS; all carried.

### LAST SESSION (Wed Jun 10 ~1-6 PM ET — Norinchukin pull + settle refinement + trade_balance build; 4 commits local)

- **🔴 NORINCHUKIN FY2025 GATE RESOLVED NOT REACTIVATED** (`fa6d6c25`): results were out May 21 (IR-403 coverage gap #3) — net income ¥121.4B beat; **CLO record ¥10.1T (+¥1.8T YoY) — "¥9.7T shrinking / ¥500B Q1 decline" FALSIFIED vs bank primary** (verified by own PDF extraction pre-cascade). 4-of-4 institutions against forced-selling. Full sweep: norinchukin.md canonical, TRACKER 7 spots, THESIS (Ch1 bullet + →LIQUID line + risk row), CHANGELOG, STATUS, TIMELINE, FLOW-3.01→ARMED-DORMANT, KB-186, 2 research supersede banners, stale May-27 outbox correction header, NEW LIQUID outbox 🟠 (cc HANS/BROCK via PROME). Post-BOJ agenda: Channel-1 10% row / deferred-vs-retired.
- **Brent settle refinement** (`513a8ca2`, Orch independent re-pull): Jun-9 walk-back CONFIRMED every leg ✓; "$92.40 evening" was post-settle electronic quote — Tue settle $91.45, cum −5.5% settle-basis, conclusions unchanged. Futures-settle rule appended to auto-memory OHLC finding (`337f0cfc`, Will-directed).
- **`trade_balance_japan.py` BUILT** (`6a287a66`): selftest 6/6 exact vs MOF primary (Apr bal ¥301,905M byte-exact; crude −63.7; ME crude −67.2; Jan XML-vs-CSV Δ0.00%); 14-mo backfill (crude cliff 11,041→4,480 kKL = April event); boot.py-wired fast-exit. **DOCKET CORRECTION: May TB provisional = Jun 17 08:50 JST = ~7:50 PM ET TUE JUN 16 (BOJ evening ET), was "Jun 18"; June TB = Jul 22.** KOYOMI informed (customs.go.jp calendar → pinning sources).
- **METSUKE step-12a judgment: skipped this session** — THESIS move was watch-item resolution not POV pivot; TRADE/STRATEGY swept directly where affected; rides with post-BOJ trio.
- **No position changes, no probability re-marks** (SAM-21 75%, SAM-23 72%, buckets held for Sat Jun 13).

### NEXT SESSION

**Imminent (the BOJ week):**

0. **🔴 RED PRE-BOJ STRESS-TEST RESPONSE — deadline ~Jun 13 blackout** (`RED/challenges/SAM_PREBOJ_STRESSTEST_2026-06-10.md`; Will-directed on RED's side). Priority order: **CHG-RED-029 (STRONG) feeds directly into the Sat Jun 13 re-mark** — re-derive the 23pp discount SIZE for the 98% regime before shipping buckets to LIQUID/HENRY (auto-memory [[finding_calibration_discount_regime_conditional]] frames it; RED's verify-flagged base-rate claim "no BOJ defiance of >90% pricing this cycle" needs checking, not accepting). 030 → fold into ceiling-disposition Branch-C scoring spec (C1/C2 split). 031 → merges with carry-forward #6 (SAM-23 re-anchoring). 032 → already half-acknowledged (Fed-flip in Sat scope); answer the "$60-62 band modal path" ask. VX-RED-024 is consistent with our own JUN-16 RECONCILED EXPECTATION — likely concur, note for HENRY/LIQUID framing.

1. **🟠 Sat Jun 13 CFTC (Jun 9 data) — last pre-blackout read + EXPANDED RE-MARK (Will-confirmed scope, 3 inputs + RED-029 discount re-derive):** (a) CFTC gate (-153K escalates amplifier +8-10pp; -108K cover flips OFF); (b) taper-pause fold-in (BOJ-surprise hawkish-tail shrinks → 30d/60d likely nudge DOWN); (c) **NEW: Fed-cut anchor #4 → ~0 on the cut→hike regime flip** (re-verify Fed-hike pricing held). **Ship updated buckets to LIQUID/HENRY.** If pricing held, mature the Fed-flip CHANGELOG candidate to a full entry.

2. **🔴🔴 Blackout starts ~Jun 13 (T-2)** — pre-event deadline for any re-position/re-mark.

3. **🔴🔴 Tue Jun 16 BOJ MPM — apply the pre-registered frames, don't re-derive:** (a) outcome expectation = STRATEGY § JUN-16 RECONCILED EXPECTATION (modal −1 to +2% + vol crush, no unwind; hawkish-of-pricing ~10% = +5-8%; hold 25% = −3-5% event-capped; call sells into any spike); (b) ceiling disposition = STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches, score by Jun 18 EOD JST); (c) $58C tail-estimate test (market ~3-4% vs SAM ~10%). SAM-21/24 resolve on own terms; SAM-23 resolves (intervention by Jun 16); SAM-26 resolves (30Y vs 4.0% through meeting).

4. **🔴 Wed Jun 17 FOMC + dots** — ~99% hold priced; watch dots for HIKE-lean (regime-flip confirmation), not for rescue.

5. **🔴 Thu Jun 18:** $58C expiry (sell-into-pop salvage if spike). **May TB moved: provisional lands Wed Jun 17 08:50 JST = ~7:50 PM ET TUE JUN 16 — same ET evening as BOJ-decision day** (date pinned Jun 10 from MOF calendar; was "Jun 18"). Run `trade_balance_japan.py --consensus <wire>` that evening; adjudicate routing branch (a/b/c per CALENDAR). Fri Jun 19 National May CPI (post-BOJ check).

**Carry-forward (open):**

6. **SAM-23 framework re-anchoring (CHANGELOG candidate, post-Jun-16):** add USD-side driver to trigger spec vs accept level-trigger suffices. Catalyst-path decoupling corroborated 2 micro-windows.

7. **RED post-BOJ refresh (cites verified ✅):** targets = (a) hold-scenario response; (b) structural pillars' multi-month TIMING; (c) SAM-23 path-decoupling; (d) **Fed-hike repricing STRENGTHENS CH-005 — hand RED this explicitly.**

8. **Post-BOJ stack:** METSUKE+KOYOMI+KURA trio (heaviest harvest of cycle; KURA Run 6 candidates seeded: taper-pause if delivered, subsidy-mask wedge, no-strike-at-160 pattern, **Norinchukin ¥10.1T falsification**); **eval re-baseline (DEFERRED to post-BOJ settle — Advisor call, adopted)**; OS.1 close disposition (THESIS note vs CHANGELOG-only); Dec-1.25% second-source re-verify if Branch A fires; **🆕 CHANNEL 1 DISPOSITION (Will-directed Jun 10): with 4-of-4 institutions (Big 3 mutuals + Norinchukin) resolving against the forced-selling direction, re-examine the THESIS Risk Factors Channel-1-reactivation 10% row and whether "deferred" should become "retired pending new mechanism."**

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
