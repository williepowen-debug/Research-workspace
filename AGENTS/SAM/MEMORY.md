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

### CHANGES SINCE LAST SESSION (Sun Jun 7 PM → Tue Jun 9 12:35 PM ET)

- **Fri NFP carry-over priced through weekend:** Polymarket BOJ Jun 16 hike held 96-98% range across the gap (Tue boot pull = 98.2%). No dovish capitulation despite Fed-cut path locking dead. Cabling intact.
- **Brent choppy down-drift (CORRECTED Tue evening, OHLC-verified):** closes $97.81 (Jun 3) → $95.03 (Thu) → $93.09 (Fri) → **$94.25 (Mon, UP +1.2%)** → ~$92.40 (Tue). Tue tagged **$89.59 intraday (~12 PM ET) but did NOT hold** — recovered to $92.40 by evening; no closing breach of the $90 line. Midday "4 consecutive down sessions / −7% cum / BREACHED $90" was wrong on all three counts (actual cum −4.5%). Driver: China demand weakness + Trump-Iran walk-back rumors (rumor-tier).
- **USDJPY intermittent 160+ tags:** Fri 160.20 → Mon dipped below → Tue re-tag 160.37. Script "Days since touch: 160 → 1d" parsed correctly = LAST touch was 1d ago, NOT continuous 4-day breach (I initially mis-parsed; Will caught it; corrected).
- **Japan Q1 GDP revised Mon JST: +1.8%** (vs +2.1% prelim, −0.3pp). Composition hike-tolerant — private consumption revised UP, capex revised DOWN. No material USDJPY reaction.
- **JGB 10Y +5bp Mon to 2.715%; 30Y +4bp recovery to 3.876%** (vs Fri 3.833%). Long-end recovered most of Fri's −1.7bp.

### LAST SESSION (Tue Jun 9 ~12:35 PM ET — SAM-21 mechanical trigger fires + 3-subagent trio + verification walk-back)

Multi-track session — SAM-21 fire & propagate → subagent trio → KURA proposal premise-fail verification → TRADE/STRATEGY drift sweep.

- **🔴🔴 SAM-21 mechanical trigger FIRED → 70% → 75%** per Jun-3 pre-registered spec. Polymarket leg ✅ (98.2%, +1.9pp vs Fri, 5th sequential ≥90%, vol $403K up from $304K); Takaichi/cabinet pushback leg ✅ (Reuters "refrained from vocally pushing back"; Jun 8 Takaichi FX-side remarks reinforce intervention-permission); Q1 GDP composition non-blocking. Propagated to PREDICTIONS (Confidence trail + Notes append), STATUS (banner + § BOJ ASSESSMENT 3 new rows + trigger spec FIRED + Sep $60 call decision row + WHAT TO WATCH Tue Jun 9 RESOLVED), TIMELINE (new ## RESOLVED — Jun 8-9 with 3 sub-events). 23pp earned discount vs Polymarket preserved.
- **3-subagent trio spawned in parallel** — KOYOMI Run 7 (docket sync, applied: 3 resolved rows migrated, pruning, stamp), METSUKE Run 5 (10 surfaces TRADE/STRATEGY drift sweep proposed), KURA Run 5 (KB-187 promote-candidate + KB-186 routing-pending).
- **Premise-verification walk-back (Will-caught):** KURA's KB-187 "4d at USDJPY 160+ no-strike" failed on premise. Verified two issues via parallel agents: (a) script line `usdjpy.py:73` label `"May26"` = apostrophe-stripped `"May'26"` (May 2026) labeling the **May 6** op — NOT a separate May 26 intervention (web search confirmed no MOF op May 22-28; yen was weakening that week); (b) USDJPY did not stay above 160 continuously — Fri tag + Mon dip + Tue re-tag = 2 distinct events. **Walked back** 6 surfaces in STATUS + TIMELINE from "4th day above 160" → "tagged 160 twice in 5 trd days." KB-187 declined; KB-186 still routing-pending → auto-memory.
- **METSUKE Cluster A applied: TRADE.md + STRATEGY.md drift sweep — ~18 surfaces.** SAM-21 70% → 75% cascade (10 surfaces across both files); CFTC -114K/63.7%/4th → -129K/72%/5th week (4 surfaces); Brent direction inversion (3 surfaces — ⚠️ the "$90.16 breach / 4th down session" framing applied here was corrected in the Tue evening pass: intraday tag-no-hold, Mon was an up session); countdown 8 trd days → 5 trd days; STRATEGY L61 HOLD-section narrative reordered with new forward-reads list (Jun 10 CPI + Jun 10 JGB 30Y + Jun 13 CFTC + Jun 13-15 cabling); STRATEGY L161 vol convergence current read refreshed to Tue Jun 9 boot.py reads with expiry-roll note.
- **METSUKE TRADE L37 P/L money-field escalation:** STATUS reads −1.9% / $57.23 / ≈−$14; TRADE L37 reads −1.4% / $57.51 / ≈−$10.5. **Will-decision: LEAVE AS-IS.** Position-card by-design tracking; not the source-of-truth.
- **No position change.** 13 shares + Jun-18 $58C unchanged. Stop spec event-capped pre-Jun-16.
- **No thesis-level change.** THESIS.md and CHANGELOG.md untouched (mechanical trigger fire is not a version event).
- **Commits:** local-only this session per Will-direction; no push.

### NEXT SESSION

**Imminent / near-term:**

1. **🔴🔴 PRICED-HIKE RECONCILIATION (Will-directed Jun 9 PM; due BEFORE Jun 13 blackout, NOT after).** "Hike to 1.00% = structural FXY +5-8%; carry unwind fires" contradicts our own CH-004 finding that the modal Jun-16 package (priced 25bp + QT-soften per Jun-9 taper-pause leak) does NOT unwind carry. Both claims can't be true. The legacy language lives on **6 surfaces:** MEMORY item #6 below, STATUS WHAT TO WATCH Jun-16 row, STRATEGY asymmetry table, CALENDAR Jun-16 row, docket/CATALYSTS.tsv Jun-16 row, THESIS catalyst sequence. **Deliverables: (a)** state the FXY move actually expected from a modal delivered-as-priced package with market at ~98%; **(b)** restate realistic Jun-18 $58C + shares payoff under that scenario; **(c)** sweep all 6 surfaces to the reconciled expectation, keeping +5-8%/Aug-2024 upside explicitly conditional on hawkish-of-pricing.

2. **🟠 Wed Jun 10 US CPI (May) — Fed-side gate.** Hot → Fed dots stay higher; soft → opens Fed-cut tail (currently <10% 2026 cut odds priced). Feeds Jun 17 dots one week ahead. **SAM-side carry tripwire.** Context: consensus already expects HOT (~4.2% headline on Iran-war energy) — hot-as-expected changes nothing; the market-moving tail is a SOFT surprise.

3. **🟠 Wed Jun 10 JGB 30Y auction — GRADE ON A CURVE (frame pre-registered in CALENDAR).** Taper-pause leak contaminates the J-ICS test: strong result is partially leak-explained (weaker evidence of lifer return); weak result DESPITE the leak is more alarming than yesterday. BTC <2.0x = 🔴 route LIQUID/HENRY/PROME same-night. *(Results ~11:35 PM ET Tue Jun 9 — poller running; may already be handled by the time this is read.)*

4. **🟠 Sat Jun 13 CFTC weekly (Jun 9 data) — last pre-blackout read + EXPANDED RE-MARK SCOPE (Will-confirmed).** CFTC gate: -153K (85% line) escalates amplifier to +8-10pp; cover to -108K flips amplifier+residual OFF. **PLUS: fold the taper-pause finding into the decomposition — BOJ-surprise hawkish-tail share shrinks (QT leg pointing dovish) → 30d/60d buckets likely nudge DOWN. Ship updated buckets to LIQUID/HENRY.**

5. **🔴🔴 Jun 13-15 BOJ pre-meeting blackout starts ~Jun 13 (T-2)** — cabling window closes; further BOJ-side leaks/speeches gated. Pre-event re-position/re-mark deadline.

6. **🔴🔴 Tue Jun 16 BOJ MPM** — DOMINANT REMAINING CATALYST. SAM 75% / market ~88-98%. ⚠️ Payoff language on this item is subject to item #1 reconciliation — modal package = priced 25bp + QT-soften; +5-8%/unwind-fires framing is the hawkish-of-pricing conditional, not the base case. Jun-18 call sells into any spike per STRATEGY exit rules (vol-crush case strengthened by taper-pause leak).

7. **🔴 Wed Jun 17 FOMC + dot plot** — >97% no-change priced; hold-confirming not rescue; lands ~24h after BOJ.

**Carry-forward (open):**

7. **🆕 SAM-23 framework re-anchoring (CHANGELOG candidate, deferred to post-Jun-16 settle).** Catalyst-path decoupling now corroborated across 2 micro-windows (Fri NFP-route + Tue Brent-leg inversion under stable USDJPY). Decision: add USD-side independent driver to SAM-23 trigger spec, or accept level-trigger (160) is itself sufficient. Bring up after BOJ binary resolves.

8. **🆕 Auto-memory promotion candidates — flag for Will's call:**
   - `finding_catalyst_path_decoupling` (KURA KB-186 route-pending)
   - `finding_pre_registration_discipline_through_corroboration` (added to local Findings this session; cross-agent transferable)
   - `finding_script_label_apostrophe_strip` (NEW today — `"May26"` label-bug taught us to parse boot.py output semantics carefully; transferable to any agent with date-labeled script constants)
   - `finding_counter_frame_3_question_disposition` (carried from Jun 4)

9. **🟠 OS.1 fiscal-dominance close.** Evidence in (largely-falsified-for-binary). **Pending:** decide if tighter THESIS-side short note vs current CHANGELOG-only documentation.

10. **🔧 Eval re-baseline (still queued).** Operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`. Fresh skip-boot CC session, ~20 min.

11. **🆕 Script cleanup (low priority):** `usdjpy.py:73` label `"May26"` → `"May'26"` or `"May6"` to avoid future mis-parse. Cosmetic; no thesis impact.

12. **🆕 NEXUS_BRIEF rollout (Will-action):** Promote template (`AGENTS/SAM/proposals/2026-06-07_nexus_brief_template.md` → `AGENTS/NEXUS/templates/NEXUS_BRIEF_TEMPLATE.md`); relocate schema spec; spawn other Tier-1 agents with rollout prompt; SPAWN PROTOCOL closeout amendment for brief write-back step.

13. **Position next-touch:** No add/trim under v1.5.1 single-path. Triggers: (a) USDJPY <156 for 3 sessions; (b) BOJ pre-cabling Jun 13-15; (c) post-Jun-16: thesis break if BOTH BOJ dovish AND USDJPY 167+/no MOF.

14. **🟡 KB-183 (FXY ATM IV proxy) — closing in.** Tue Jun 9 boot.py rolled to Jul-17 expiry (9.64% IV, RR -3.34); Fri's 11.08% was earlier expiry. KURA recommends: expiry-roll artifact, not broken read — close KB-183 next cleanup.

15. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify.

16. **🆕 KOYOMI Run 7 escalations (informational, no Will-action):** (a) Jun 10 US CPI BLS schedule HTTP 403 to WebFetch — retrospective-confirm next run; (b) Jun 2 JGB 10Y row in RECENTLY RESOLVED at 7d edge — prunes Jun 10.

17. **Subagent cadence:** post-Jun-16 BOJ = METSUKE+KOYOMI+KURA trio (will be heaviest harvest of cycle per KURA's Run 6 estimate). METSUKE Run 7 will be the largest sweep since Run 1.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — unchanged)

1. **`trade_balance_japan.py`** — MOF monthly TB scrape (Jun 18-19 May TB = Phase 1 stability lag-test per CALENDAR). ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
