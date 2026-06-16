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

### CHANGES SINCE LAST SESSION (Thu Jun 11 ~10:45 AM ET → Sun Jun 14 ~12:45 PM ET)

- **🔴🔴 UEDA HOSPITALIZED Jun 10 — MISSES JUN 16 MPM** (5-source primary verified: Bloomberg/Reuters/Jiji/Nippon.com/Japan Times). Infected hepatic cyst, ~2wk stay; **first sitting BOJ Governor to miss MPM since the 1998 framework**. Himino chairs, Uchida hosts presser, Ueda written-no-vote. Cabinet (Katayama Jun 12 paraphrase): no impact on meeting. Market read = guidance-clarity risk via Uchida-presser tone, NOT hike risk.
- **🟢 BRENT SUB-$90 BREACHED Sun ($87.33)** — first sub-$90 close this cycle; cum ~−10% from $96.78 Jun-3 baseline. Driver: 14-pt Pakistan-mediated draft Jun 12 (Pakistan PM "final, agreed-upon text"; 30-day Hormuz reopen clause) + Bessent "signing weekend or Monday" 80% odds. Trump pushback "doesn't reflect agreed terms" = paused-via-diplomacy, unsigned; Iran has NOT confirmed. US-Iran drone/vessel exchange near Hormuz Jun 12 AM = kinetic NOT ceased.
- **🔴 CFTC −145,818** (Jun 9 data, rel Fri Jun 12, 6th build week, +16,251 WoW; 81% of −180K cycle peak vs 72% Jun 2; 7,182 shy of −153K/85% escalation). No cover.
- **Polymarket BOJ Jun 16 hike: 97.5% Thu → 99.2% Sun** (+1.7pp hawkish drift, $584K vol). Swaps 93% (Tokyo Tanshi Jun 9 baseline). Bloomberg 49/51 economists for 25bp → 1.00% (Jun-9 piece, date corrected from earlier loose Jun 13-14 stamp).
- **Fed-hike-2026 pricing held ~51-52%** (Polymarket Jun 11); regime flip cut→HIKE matured.
- SPR drained THROUGH BRENT's conventional ~350M throttle (349.192M Jun 10 EIA, 6th wk at ~8M/wk); per CRS R42460/EPCA real floors are 252.4M (non-emergency only) / ~150M operational / NO statutory floor for emergency. War-driven drain = emergency authority → ~6mo runway. War-conditional: diplomacy lands → non-emergency framing → 252.4M reactivates → ~3mo.

### LAST SESSION (Sun Jun 14 PM — pre-blackout consolidated 6-input re-mark + STATUS/STRATEGY/CALENDAR/TRADE/MEMORY tier-1 pass + LIQUID/HENRY outbox ship + Orc verify loop on each commit)

- **Six-input re-mark landed in STATUS** (commit `0f02a485`, Orc-verified clean): (a) CFTC −145,818 + 81% amplifier state; (b) taper-pause hawkish-tail shrink; (c) Fed-anchor #4 → 0 matured; (d) **SAM-21 75 → ~90 per CH-009** (S4 void-gate clear: Polymarket 99.2%, swaps 93%, Bloomberg 49/51, no dovish leak found); (e) **SAM-23 72 → ~30 per CH-011** (disorder-not-level FALSIFIED empirically: 6+ orderly sessions at 160+ no strike); (f) Ueda absence integrated. **Carry-unwind buckets recomputed ~14/37/49 → ~8/23/32** (4 named-driver anchor changes attributed inline; BOJ-surprise NET-SHRINKS: hike 70→90% × hawkish-tail 30→10%).
- **STRATEGY weights re-marked** (commit `55349fd0`): pre-registered L202 gate fired ~65/10/25 → ~80/10/10. Event-EV ~−0.11% → ~+0.60% (sign flip; reframes event posture from "hold despite the print" to "hold *and* modestly favorable"). Insertion 2 (exit-rule #3) sharpened for Uchida-presser muddiness per Orc framing: take Tuesday event-vol spike itself, don't wait for clean post-presser repricing.
- **Outbox ship to LIQUID + HENRY** (commit `5aa6f551`) with severity-up framing per Orc reminder: "probability down, severity-if-triggered UP" (CFTC fuel at cycle-peak proximity, no cover). **HENRY RR correction follow-up** (commit `d322bc7f`): struck out +24.05 RR positioning read per Orc — non-physical magnitude is KB-183 proxy artifacting at the magnitude where even the sign read is suspect; ATM IV build retained as real signal.
- **CALENDAR + TRADE + MEMORY tier-1** this commit. Money fields untouched (13 shares @ $58.32, $58C strike+expiry, $55.05 post-event stop, $798 exposure — all frozen).
- **Orc + Will collaboration loop**: 4 verify rounds (STATUS / outbox / STRATEGY / CALENDAR+TRADE+MEMORY) — each surfaced a real catch (Phase-2-reopening directional fix; force-push concern → benign shallow-clone; STRATEGY weight update I'd missed; HENRY RR non-physical magnitude). Net session yield = high quality from the loop; spoke clean STRATEGY + outbox + STATUS to LIQUID/HENRY downstream-ready.
- **Force-push concern investigated**: BENIGN. All 21 commits since f35b65a2 are in current master chain via `git merge-base --is-ancestor`. Orc was looking at a shallow clone false-fork per `[[finding_shallow_clone_false_fork]]`.

### NEXT SESSION (single block — no duplicate)

**Imminent (2 trd days to BOJ):**

1. **🔴🔴 Tue Jun 16 BOJ MPM** — apply pre-registered frames, don't re-derive:
   - STRATEGY § JUN-16 RECONCILED EXPECTATION re-marked weights ~80/10/10 (modal −1 to +2% + vol crush; hawkish-of-pricing ~10% = +5-8%; hold ~10% = −3-5% event-capped). Sell-into-pop salvage path holds; Uchida-presser muddiness = take the Tuesday IV spike itself.
   - STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches per CH-010 + Branch C1/C2 split), score by Jun 18 EOD JST.
   - $58C tail-estimate test (market ~3-4% vs SAM ~10%) — score Tuesday.
   - **NEW Ueda-attribution check:** a hold attributed to Uchida-presser dovish-cover ≠ Branch C1 (Takaichi-political) ≠ Branch C2 (fiscal/long-end); separate carefully. Apr-13 Himino dovish-cover precedent informs.
   - SAM-21/23/24/26 all resolve on own terms.

2. **🔴 Wed Jun 17 FOMC + dots** — ~99% no-change priced; watch dots for HIKE-lean (regime-flip confirmation), not for rescue.

3. **🔴 Wed Jun 17 (~7:50 PM ET Tue eve)** — **May trade balance** (provisional). Run `trade_balance_japan.py --consensus <wire>`; adjudicate routing branch (a/b/c per CALENDAR). Diplomacy track + Hormuz still-closed biases toward branch (c) (surplus persists, volumes depressed).

4. **🔴 Thu Jun 18** — $58C expiry. Fri Jun 19 National May CPI (post-BOJ check). Post-settle: position re-underwrite (v1.6 spec item A — Will decides; incl. FXY-vehicle question).

**Carry-forward (open after BOJ settles):**

5. **SAM-23 framework re-anchoring CHANGELOG entry (post-Jun-16)** — substance settled via CH-011 (driver/disorder dimension + no-strike decay clause); Mimura "deviate AND persist" + Sun-Jun-14 empirical 6+ orderly sessions at 160 no-strike = supporting cites. Write the formal entry post-scoring.

6. **RED post-BOJ refresh** — hold-scenario response; structural-pillar TIMING under CH-032 band; SAM-23 post-event scenario-weighted anchor; Fed-hike → CH-005.

7. **Post-BOJ stack per `proposals/2026-06-10_v16_rewrite_spec.md`** (Will+Orch-endorsed): v1.6 re-derivation (AFTER Jun 16-18 scoring; RED pass on draft pillars BEFORE version commit) + A. position re-underwrite + B. PROME network-reframe packet + C. hedge-cost tripwire build. **THESIS Tier-2 — Orc hard-verify watch:** oil-in-yen channel DORMANT relabel at L222-224 (NOT "Phase 2 re-opening") + L300 RISK FACTORS "Brent re-accelerating" flip + thin CRS-cited SPR conclusion. Channel-1 deferred-vs-retired folds in (4-of-4 against). Eval re-baseline; OS.1 close disposition; Dec-1.25% re-verify if Branch A fires.

8. **Auto-memory candidate (Sun Jun 14, Orc-endorsed):** "Cross-agent sends: a caveat protects you, not the receiver — they may act on the sign/direction regardless. A metric outside its physical range (or known-unreliable) should be SUPPRESSED from the send, not caveat-and-shipped." Fleet-interface discipline, transferable. KB-183 local refinement separate: "at non-physical magnitudes the magnitude impeaches the sign too." One auto-memory line + one local KB refinement. Authorize at next boot or in this session if Will green-lights.

9. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) post-Jun-16 thesis break = BOJ dovish AND USDJPY 167+/no MOF. NEXUS_BRIEF rollout = Will-action.

**⏸️ DEFERRED:** Layer B cross-agent signals (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire decision; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
