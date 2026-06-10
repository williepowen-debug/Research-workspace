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

### CHANGES SINCE LAST SESSION (Tue Jun 9 ~midnight ET → Wed Jun 10 ~10 AM ET boot)

- **US CPI (May, 8:30 AM): HOT-AS-EXPECTED** — headline 4.2% YoY exactly consensus (3rd consecutive accel, energy passthrough); core 2.9% in-line; core MoM 0.2% mildly soft. No soft surprise → Fed-side gate closed per pre-registration; USDJPY flat through print; no re-marks.
- **🔴 Fed pricing regime-flipped cut→HIKE** (found at CPI-resolve): Polymarket ~52% Fed hike in 2026, Oct frontrunner ~50%; cut odds ~0. Secondary path INVERTED, not just dead — Pillar 1 post-June compression burden falls on BOJ alone.
- **Swaps repriced 93%** for Jun-16 hike (Tokyo Tanshi Jun 9; was ~86% Jun 4) — converged with Polymarket (>96%, no CPI retrace). **Swaps also price 92.5% of a 2nd hike to 1.25% by Dec** + Reuters poll median 1.25% Q4 2026 → consensus treats Takaichi ceiling as dead above 1.00%.
- **USDJPY 160.38** holding above #3 trigger, still no MOF strike. Brent recovered to $92.80. DXY 99.86 (soft through hot CPI — first mildly yen-supportive USD-side signal since NFP). US 30Y touched 5.0%. JGB Jun-9 pub: 10Y 2.669 / 30Y 3.823.

### LAST SESSION (Wed Jun 10 ~10 AM – ~1 PM ET — boot, CPI resolve, Advisor-batch execution; all committed locally)

- **Boot + CPI resolve:** market refresh, CPI row resolved across STATUS/CALENDAR/CATALYSTS.tsv/TIMELINE; Fed-hike regime flip multi-source verified before propagation, logged in STATUS SECONDARY PATH (now "dead and pointing in reverse") + TIMELINE Jun-10 entry + CHANGELOG; scoped into Sat Jun 13 re-mark (Fed-cut anchor #4 → ~0).
- **🔴 $58C: WILL DECIDED HOLD.** Live quote bid $0.00/ask $0.20/last $0.09, OI 13.4K; realistic salvage ~$5-10 dominated by modeled EV ~$20-25. Logged TRADE § Position B with **companion tail-estimate test: market ~3-4% vs SAM ~10% hawkish tail — score with Jun-16 outcome.**
- **🔴 TAKAICHI-CEILING DISCOUNT DISPOSITION pre-registered** (STRATEGY new §, CHANGELOG entry; Advisor-prompted, Will-approved, advisor's verify-pre-BOJ overrule accepted after two-evidence-type verification). 3 mechanical branches: A retire-to-friction 5-10pp (hike + alive path-guidance + no cap-statement 48h) / B modify 10-20pp (hike + new ceiling language) / C vindicate-widen 25-30pp (hold). **Post-June path marks ONLY** (SAM-21/24 resolve on own terms); score by Jun 18 EOD JST; Sato 3→2 modulates within-branch (Branch A sits top of friction range). Pre-registered insight: delivered hike reclassifies SAM-08/SAM-20 as TIMING failures.
- **Script fixes (MAINTENANCE entry):** `usdjpy.py` MOF labels → MonYYYY; `jgb_auctions.py` probes JST date — verified finds the Jun-10 result it had missed, idempotent on TSV.
- **RED cites verified** (CH-005/CH-007 correct, retargeted to v1.5, resolve Jun 16; CH-008 dismissed-if-hike). Housekeeping clean (no TSV dupe; "+5-8%" residual sweep clean). LIQUID 30Y-softening outbox note written. **2 of 5 auto-memory candidates promoted** (OHLC-verify, pre-registration-discipline; Advisor-endorsed; veto = delete files + index lines).
- **No position change beyond the HOLD decision. No probability re-marks** (SAM-21 75%, SAM-23 72%, buckets held for Sat Jun 13).

### NEXT SESSION

**Imminent (the BOJ week):**

1. **🟠 Sat Jun 13 CFTC (Jun 9 data) — last pre-blackout read + EXPANDED RE-MARK (Will-confirmed scope, 3 inputs):** (a) CFTC gate (-153K escalates amplifier +8-10pp; -108K cover flips OFF); (b) taper-pause fold-in (BOJ-surprise hawkish-tail shrinks → 30d/60d likely nudge DOWN); (c) **NEW: Fed-cut anchor #4 → ~0 on the cut→hike regime flip** (re-verify Fed-hike pricing held). **Ship updated buckets to LIQUID/HENRY.** If pricing held, mature the Fed-flip CHANGELOG candidate to a full entry.

2. **🔴🔴 Blackout starts ~Jun 13 (T-2)** — pre-event deadline for any re-position/re-mark.

3. **🔴🔴 Tue Jun 16 BOJ MPM — apply the pre-registered frames, don't re-derive:** (a) outcome expectation = STRATEGY § JUN-16 RECONCILED EXPECTATION (modal −1 to +2% + vol crush, no unwind; hawkish-of-pricing ~10% = +5-8%; hold 25% = −3-5% event-capped; call sells into any spike); (b) ceiling disposition = STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches, score by Jun 18 EOD JST); (c) $58C tail-estimate test (market ~3-4% vs SAM ~10%). SAM-21/24 resolve on own terms; SAM-23 resolves (intervention by Jun 16); SAM-26 resolves (30Y vs 4.0% through meeting).

4. **🔴 Wed Jun 17 FOMC + dots** — ~99% hold priced; watch dots for HIKE-lean (regime-flip confirmation), not for rescue.

5. **🔴 Thu Jun 18:** $58C expiry (sell-into-pop salvage if spike) + May trade balance Phase-1 lag-test (routing in CALENDAR). Fri Jun 19 National May CPI (post-BOJ check).

**Carry-forward (open):**

6. **SAM-23 framework re-anchoring (CHANGELOG candidate, post-Jun-16):** add USD-side driver to trigger spec vs accept level-trigger suffices. Catalyst-path decoupling corroborated 2 micro-windows.

7. **RED post-BOJ refresh (cites verified ✅):** targets = (a) hold-scenario response; (b) structural pillars' multi-month TIMING; (c) SAM-23 path-decoupling; (d) **Fed-hike repricing STRENGTHENS CH-005 — hand RED this explicitly.**

8. **Post-BOJ stack:** METSUKE+KOYOMI+KURA trio (heaviest harvest of cycle; KURA Run 6 candidates seeded: taper-pause if delivered, subsidy-mask wedge, no-strike-at-160 pattern, **Norinchukin ¥10.1T falsification**); **eval re-baseline (DEFERRED to post-BOJ settle — Advisor call, adopted)**; OS.1 close disposition (THESIS note vs CHANGELOG-only); Dec-1.25% second-source re-verify if Branch A fires; **🆕 CHANNEL 1 DISPOSITION (Will-directed Jun 10): with 4-of-4 institutions (Big 3 mutuals + Norinchukin) resolving against the forced-selling direction, re-examine the THESIS Risk Factors Channel-1-reactivation 10% row and whether "deferred" should become "retired pending new mechanism."**

9. **Auto-memory: 3 candidates remain Will's call** (`finding_catalyst_path_decoupling`, `finding_script_label_apostrophe_strip`, `finding_counter_frame_3_question_disposition` — one-liners given Jun 10).

10. ~~Norinchukin FY2025 CLO check~~ — **✅ RESOLVED Jun 10 PM (Will-directed pull):** results were out May 21 — net income ¥121.4B beat, **CLO record ¥10.1T (+¥1.8T YoY) — "shrinking" claim FALSIFIED**, gate NOT reactivated, 4-of-4 institutions against forced-selling. Full sweep done (norinchukin.md canonical, TRACKER, THESIS+CHANGELOG, STATUS, TIMELINE, FLOW-3.01/3.03, KB-186, TRADE, research-doc supersede banner, LIQUID outbox 🟠). Known-unknown: UST split undisclosed. Next read ~Nov 2026 interim.

11. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) pre-cabling Jun 13-15; (c) post-Jun-16 thesis break = BOJ dovish AND USDJPY 167+/no MOF. **NEXUS_BRIEF rollout = Will-action.** 🟡 KB-183 close at next cleanup. KOYOMI informational: Jun-10 US CPI resolved via web (BLS page 403 retrospective-confirmed moot); Jun-2 10Y row pruned Jun 10 ✅.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. **`trade_balance_japan.py`** — MOF monthly TB scrape (Jun 18-19 May TB = Phase 1 stability lag-test per CALENDAR). ~30 min. **IN PROGRESS Jun 10 PM (Will-directed, after Norinchukin pull).**
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
