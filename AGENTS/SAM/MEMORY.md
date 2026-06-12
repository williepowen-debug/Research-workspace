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

### CHANGES SINCE LAST SESSION (Wed Jun 10 ~9 PM → Thu Jun 11 ~10:45 AM ET)

- **🔴🔴 US-IRAN KINETIC ESCALATION (primary-source verified):** 2nd consecutive day of mutual strikes — CENTCOM hit Iranian air-defense/radar near Hormuz Jun 10 PM; IRGC counter-struck US bases Kuwait/Bahrain/Jordan overnight; **Iran's Strait Authority declared Hormuz CLOSED to ALL traffic "until further notice"**; Trump: hit Iran "VERY HARD TONIGHT" + "we will be taking Kharg Island" (rhetoric-tier). Jun-9 "walk-back rumor" DEAD — resolved opposite. **TAPE FADED IT** (Thu ~10 AM own-pull): Brent $92.65 −0.5%, VIX 21.4 −3.7%, S&P +0.7%, gold −0.5%, USDJPY flat 160.49. Full narrative: TIMELINE LIVE entry.
- USDJPY 160.51 (6th day at/above zone, NO strike, orderly ~0.2y range); Polymarket BOJ **97.5%** (7th sequential ≥90%, no retrace through escalation); JGB Jun-10 pub 10Y 2.681/30Y 3.811; MOF weekly (May31-Jun6) net BUYING; Brent recovered off Tue $89.59 tag.
- US May PPI (Jun 11): headline +1.1% MoM / 6.5% YoY HOT, core +0.4% in-line (CPI-shaped, energy-driven); **Fed-hike-2026 pricing HELD ~51%** (Oct 41%/Sep 26%); Fed blackout clean.
- Japan: BSI Q2 large-mfg **−1.8** vs +4.2 exp (first neg since Q2-2025, ME-attributed; second-tier, non-blocking). **Reuters poll: ~94% economists for Jun-16 hike, median 1.25% by Dec — SECOND SOURCE for Dec-1.25% consensus** (was swaps-only single-source). Mimura Jun-4 "deviate AND persist" framing = MOF-own-mouth support for CH-011 disorder-not-level.

### LAST SESSION (Thu Jun 11 AM — boot + Will-directed live news sweep; NO re-marks; closeout+push Will-opened window for laptop switch)

- Boot clean (origin-synced 0/0 after Wed push train; boot.py 10/10). STATUS market table + banner refreshed.
- **4-agent mechanism-scoped overnight sweep** (BOJ-leak / MOF-tape / Iran / Fed buckets): 3 quiet, Iran bucket = the escalation above. Verified vs own live tape pull before propagating — **sub-agent's "Brent $95.15" did NOT verify on own pull ($92.65) — trusted own primary.** STATUS banner 🔴🔴 + TIMELINE LIVE entry written.
- **Marks discipline held:** SAM-23 mark-UP conjunction NOT met (oil leg ❌ Brent down / escalation ✅ / USDJPY ✅); CH-011 Sat re-derivation voids untouched (no strike / orderly / no 161.5); METHOD risk-off trigger NOT firing (VIX down). SAM-21 75%, SAM-23 72%, buckets all held — everything queued for Sat.
- Will Q&A (no file changes): hike→position scenario walk-through (modal hike-as-priced pays little; $58C = hawkish-tail ticket; CH-032 band context); CFTC/COT explainer (non-commercial = leveraged funds, −129,567 ≈ $10B notional, 5-week build INTO the priced hike = carry-still-pays logic; fuel-not-trigger framing).
- FXY options proxy printed scale artifact (ATM IV 0.98% vs Tue 9.64%) — NOT propagated per KB-183; sign read (calls bid) unchanged.

### NEXT SESSION

**Imminent (the BOJ week):**

1. **🟠 Sat Jun 13 CFTC (Jun 9 data) — last pre-blackout read + CONSOLIDATED RE-MARK, NOW SIX INPUTS:** (a) CFTC gate (-153K escalates amplifier +8-10pp; -108K cover flips OFF); (b) taper-pause fold-in (hawkish-tail shrinks); (c) Fed-cut anchor #4 → ~0 (hike-pricing held ~51% Thu — mature Fed-flip CHANGELOG candidate); (d) **SAM-21 75% → ~90 per CH-009** (void: dovish leak Jun 11-12 / swaps <85% — none as of Thu AM; **but check Polymarket/swaps for ESCALATION-driven retrace first — kinetic war 3 trd days pre-MPM is live Apr-13-Himino hold-cover precedent**); (e) **SAM-23 72% → ~35 per CH-011** (void: strike before Sat / disorderly session / 161.5+ — none as of Thu AM; 30d/60d MOF anchor restructured scenario-weighted); (f) **🆕 escalation check: if tonight's threatened US round hit oil-EXPORT infra (Kharg ~90% of Iran crude exports) or Brent tagged $100+, the SAM-23 oil leg flips + oil/MOU anchor #5 re-rates — re-derive before applying (d)/(e) mechanically.** Downstream same pass: reconciled-table weights ~65/10/25 → ~80/10/10, event EV, Branch-C prior, buckets ship to LIQUID/HENRY, CH-032 band-flag re-verify.

2. **🔴🔴 Blackout starts ~Jun 13 (T-2)** — pre-event deadline for any re-position/re-mark.

3. **🔴🔴 Tue Jun 16 BOJ MPM — apply pre-registered frames, don't re-derive:** (a) STRATEGY § JUN-16 RECONCILED EXPECTATION (modal −1 to +2% + vol crush, no unwind; hawkish-of-pricing ~10% = +5-8%; hold = −3-5% event-capped); (b) STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches, score by Jun 18 EOD JST; Branch C now split C1/C2 per CH-010); (c) $58C tail-estimate test (market ~3-4% vs SAM ~10%). SAM-21/23/24/26 all resolve on own terms. **NEW: a hold attributed to ME-war uncertainty = Branch C1-adjacent but check CH-010 attribution split carefully — war-cover ≠ Takaichi-political.**
4. **🔴 Wed Jun 17 FOMC + dots** (~99% hold; watch dots for HIKE-lean) **+ May TB lands ~7:50 PM ET Tue Jun 16** — run `trade_balance_japan.py --consensus <wire>`; escalation/total-closure biases diagnostic toward branch (c) (surplus persists, volumes depressed).
5. **🔴 Thu Jun 18:** $58C expiry (Will-decided HOLD; sell-into-pop salvage). Fri Jun 19 National May CPI. Post-settle: position re-underwrite (v1.6 spec item A — Will decides).

**Carry-forward (open):**

6. **SAM-23 framework re-anchoring CHANGELOG entry (post-Jun-16)** — substance settled via CH-011 (driver/disorder dimension + no-strike decay clause). Mimura "deviate AND persist" quote = supporting cite.
7. **RED post-BOJ refresh (cites verified ✅):** hold-scenario response; structural-pillar TIMING under CH-032 band; SAM-23 post-event scenario-weighted anchor; Fed-hike→CH-005.
8. **Post-BOJ stack per `proposals/2026-06-10_v16_rewrite_spec.md`:** v1.6 re-derivation (AFTER Jun 16-18 scoring; RED pass before version commit) + A. position re-underwrite (incl. FXY-vehicle Q) + B. PROME network-reframe packet + C. hedge-cost tripwire build. Channel-1 deferred-vs-retired folds in (4-of-4 against). Plus METSUKE+KOYOMI+KURA trio (KURA Run 6 seeds incl. Norinchukin ¥10.1T falsification + no-strike-at-160), eval re-baseline, OS.1 close disposition, **Dec-1.25% re-verify now has 2nd source (Reuters poll Jun 11) — fold into Branch A scoring if it fires.**
9. **Position next-touch:** no add/trim under v1.5.1. Triggers: USDJPY <156 ×3 sessions; pre-cabling Jun 13-15; post-Jun-16 break = BOJ dovish AND 167+/no-MOF. NEXUS_BRIEF rollout = Will-action. 🟡 KB-183 close at next cleanup.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

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
