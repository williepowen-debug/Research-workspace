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
- [2026-06-09] **Intraday print ≠ session state — verify OHLC before session-count claims (2nd instance same day).** Midday boot pulled Brent $90.16 mid-slide and STATUS recorded "BREACHED $90, 4th consecutive down session, −7% cum." Evening OHLC verify: the sub-$90 tag was real ($89.59 low) but didn't hold ($92.40 by evening), Mon was an UP session (so not 4 consecutive), cum was −4.5%. **Default: any "Nth consecutive session" or "breached X" claim needs daily-close OHLC verification before propagation; an intraday fetch is a point-in-time tick, not a session verdict.** Pairs with the boot.py parse finding below — same failure family as the morning's USDJPY mis-parse.
- [2026-06-09] **boot.py "Days since touch: X → Nd, MOF Y" — parse carefully.** "Nd" = days since LAST touch of level X, NOT consecutive days above X. "MOF Y" = label of the most recent MOF op that pushed below the prior level. Mis-parsed today as "4 consecutive days above 160" (actual: 2 distinct tags Fri+Tue with Mon dip between) AND as "MOF May26 = May 26 intervention" (actual: label `"May26"` is `usdjpy.py:73`'s string for the **May 6** op — apostrophe-stripped `"May'26"` meaning May 2026). Will caught both. **Default: never propagate script-derived counts/dates without re-reading the script's source semantics; verify price history independently before claiming "Nth consecutive day" or "N days above X."**
- [2026-06-09] **Pre-registered mechanical trigger discipline — first clean fire (SAM-21 Jun-3 → Jun-9).** Held 70% across 5 days of overdetermining corroboration (Bloomberg sources leak Jun 4, Ueda hawkish speech Jun 3, 5 sequential Polymarket ≥90%, Sat CFTC build #5, NFP USD-rally stress test) by waiting for the structural trigger date rather than discretionary-firing early. The "discipline cost" was ~5 days of mark; the discipline benefit was a clean spec test the next time. **Auto-memory promotion candidate `finding_pre_registration_discipline_through_corroboration` flagged for Will's call.**

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Tue Jun 9 12:35 PM ET → Tue Jun 9 ~midnight ET; evening session, same day)

- **Brent's midday "$90 breach" did NOT hold:** intraday low $89.59 (~12 PM ET) recovered to $92.40 by evening. OHLC verify also showed Mon Jun 8 closed UP +1.2% — midday "4 consecutive down sessions / −7% cum" was wrong (actual: Thu-Fri down, Mon up, Tue down; cum −4.5%). All surfaces corrected.
- **JGB Jun-9 pub eased:** 10Y 2.669% (−4.6bp) / 30Y 3.823% (−5.3bp) pre-auction. USDJPY 160.42 evening (still above #3 trigger, no MOF strike).
- **🔴 BOJ taper-pause leak (Reuters-sourced Jun 9):** Jun 15-16 meeting lays out FY2027+ purchase plan; option = open-ended ~¥2.1T/mo (pausing QT). Modal Jun-16 package now hike + QT-soften = balanced/priced. **May PPI +6.3%** (fastest since Mar 2023) + **BOJ trend gauge 2.8% Apr** (subsidy-stripped, accelerating) = hawkish-mechanism side. No re-marks.
- **🟠 JGB 30Y auction (Jun 10 JST, resolved ~11:35 PM ET): SOFTENING not stress** — BTC 2.936x (vs 3.115x Apr tap), tail 2.8bp (vs 1.3bp), WA 3.860%. Softer-than-raw on the pre-registered curve (deteriorated DESPITE taper-pause tailwind); no 🔴 route; SAM-26 not re-lit.

### LAST SESSION (Tue Jun 9 ~8:50 PM – ~midnight ET — evening session: corrections, intake, reconciliation, auction)

Six-track evening session, all work pushed (Will-opened window; commits `cd9f23cd` → `7f8ad733`, all scoped fast-forwards).

- **Brent walk-back correction (Will-directed):** OHLC-verified, swept 6 surfaces (STATUS/TRADE/STRATEGY/MEMORY/TIMELINE/CALENDAR); SAM-23 leg (i) downgraded "deeply MET" → "MET," held 72%. New OHLC-verify finding logged (2nd same-day instance of intraday-print-as-session-verdict failure family).
- **Subagent pair-file annotations (Advisor-caught gap):** METSUKE/KOYOMI/KURA memories carried stale "Brent breached $90 / 4th down session" + "USDJPY 4 days above 160" in forward-looking sections. Run-logs annotated (history preserved); NEXT RUN HINTS + STANDING MONITORS rewritten; **KURA queue KB-187 status fixed to DECLINED** (was still "CLEAR PROMOTE" despite midday premise-fail).
- **Git-anomaly thread CLOSED:** Advisor retracted its force-rewrite claim — shallow-clone artifact on its side ([[finding_shallow_clone_false_fork]] confirming instance, now caught an advisor-layer agent). Not logged as incident; no VIOLET question.
- **Evening intake (Advisor sweep → primary-source verified before propagation):** taper-pause story (stale ¥2.5T/mo → ~¥2.1T fixed in STATUS+CATALYSTS); trend gauge 2.8% Apr (stale THESIS 2.2% Feb-debut cite fixed); May PPI +6.3%; 30Y auction confirmed on schedule (MOF alteration = Jun 4/19 LEA zones only). WALTER coverage gap (PPI + QT story slipped routing) noted in TIMELINE process note.
- **🔴 PRICED-HIKE RECONCILIATION executed (Will-directed, pre-blackout deadline beaten):** modal package = FXY −1 to +2% + vol crush, unwind does NOT fire (CH-004); +5-8%/unwind-fires re-scoped to hawkish-of-pricing conditional (~10% all-in); event EV ≈ −0.1% at ~98% pricing; Jun-18 $58C loses most of $40 in modal case (sell-into-pop = salvage); shares = 3-6mo structural bet. Canonical table: **STRATEGY § JUN-16 RECONCILED EXPECTATION**; 7 surfaces swept; CHANGELOG entry (no version bump). Pre-registered before the meeting.
- **30Y auction resolved same-night** via background poller + pre-registered grade-on-a-curve frame (see CHANGES above). TSV row hand-added.
- **No position change. No probability re-marks** (SAM-21 75%, SAM-23 72%, buckets held for Sat Jun 13 expanded re-mark). **METSUKE not spawned** despite TRADE/STRATEGY moves — the moves WERE the hand-applied corrections/reconciliation; next METSUKE run post-BOJ per cadence.

### NEXT SESSION

**Imminent / near-term:**

1. **🟠 Wed Jun 10 US CPI (May) — Fed-side gate.** Hot → dots stay higher; soft → opens Fed-cut tail (<10% 2026 cut odds priced). Consensus already expects HOT (~4.2% headline, Iran-war energy) — hot-as-expected changes nothing; the market-moving tail is a SOFT surprise. **SAM-side carry tripwire.**

2. **🔴 Jun-18 $58C hold-vs-salvage check (Advisor-suggested, adopted — Will decision).** Pull live bid, compare vs modeled EV (~$20-25). If market bids near modeled EV, hold-vs-salvage is near-coin-flip; tiebreaker = hawkish-branch skew (the original lottery purpose). **Surface explicitly to Will — money field, don't default to hold.**

3. **🟠 Sat Jun 13 CFTC (Jun 9 data) — last pre-blackout read + EXPANDED RE-MARK SCOPE (Will-confirmed).** CFTC gate (-153K escalates amplifier +8-10pp; -108K cover flips OFF) **PLUS taper-pause fold-in: BOJ-surprise hawkish-tail share shrinks → 30d/60d buckets likely nudge DOWN. Ship updated buckets to LIQUID/HENRY.**

4. **🔴🔴 Jun 13-15 blackout starts ~Jun 13 (T-2)** — pre-event re-position/re-mark deadline.

5. **🔴🔴 Tue Jun 16 BOJ MPM** — SAM 75% / market ~88-98%. Reconciled expectation: modal = FXY −1 to +2% + vol crush, no unwind; +5-8% = hawkish-of-pricing conditional (~10%); hold (25%) = −3-5% event-capped. Call sells into any spike. Full table: STRATEGY § JUN-16 RECONCILED EXPECTATION.

6. **🔴 Wed Jun 17 FOMC + dots** — >97% no-change priced; hold-confirming not rescue.

7. **Housekeeping at boot:** (a) verify `jgb_auctions.py` doesn't dupe the hand-added Jun-10 30Y TSV row; (b) residual check: no surface still carries unconditional "+5-8% / unwind fires"; (c) LIQUID routine-sync mention of 30Y softening.

**Carry-forward (open):**

8. **🆕 SAM-23 framework re-anchoring (CHANGELOG candidate, post-Jun-16).** Catalyst-path decoupling corroborated across 2 micro-windows. Decision: add USD-side driver to trigger spec, or accept level-trigger (160) suffices.

9. **🆕 RED post-BOJ refresh targets (Advisor-flagged).** Reconciliation concedes RED's CH-005/CH-007 core in advance (adversarial loop working — CH-002/CH-003 precedent). New ground: (a) hold-scenario response; (b) structural pillars' multi-month TIMING (known SAM failure mode); (c) SAM-23 path-decoupling. *(Verify CH-005/CH-007 cite vs `red/` log before acting.)*

10. **🆕 Auto-memory promotion candidates — Will's call:** `finding_catalyst_path_decoupling` (KURA KB-186 route-pending); `finding_pre_registration_discipline_through_corroboration`; `finding_script_label_apostrophe_strip`; `finding_counter_frame_3_question_disposition`; **NEW: `finding_ohlc_verify_before_session_claims`** (2 same-day instances).

11. **🟠 OS.1 fiscal-dominance close** — decide THESIS-side short note vs CHANGELOG-only.

12. **🔧 Eval re-baseline (queued).** `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`, fresh skip-boot session, ~20 min.

13. **🆕 Script cleanups (low):** `usdjpy.py:73` `"May26"` label; `jgb_auctions.py` date-filter uses local ET date (missed live Jun-10 JST result — fetched by hand tonight).

14. **🆕 NEXUS_BRIEF rollout (Will-action):** promote template; relocate schema; spawn Tier-1 rollout; SPAWN PROTOCOL amendment.

15. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) pre-cabling Jun 13-15; (c) post-Jun-16 thesis break = BOJ dovish AND USDJPY 167+/no MOF.

16. **🟡 KB-183** — expiry-roll artifact confirmed; close at next cleanup. **🟠 Norinchukin FY2025 (Jun)** — Channel 1 gate; verify CLO ¥8.2T vs thesis ¥9.7T.

17. **🆕 KOYOMI escalations (informational):** (a) Jun 10 US CPI BLS 403 — retrospective-confirm; (b) Jun 2 JGB 10Y row prunes Jun 10.

18. **Subagent cadence:** post-Jun-16 = METSUKE+KOYOMI+KURA trio (heaviest harvest of cycle; METSUKE Run 7 largest sweep since Run 1). KURA Run 6 KB candidates seeded tonight: taper-pause (if delivered), subsidy-mask wedge quantification, corrected no-strike-at-160 pattern.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — unchanged)

1. **`trade_balance_japan.py`** — MOF monthly TB scrape (Jun 18-19 May TB = Phase 1 stability lag-test per CALENDAR). ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
