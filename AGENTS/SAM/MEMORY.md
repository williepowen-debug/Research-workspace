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

### CHANGES SINCE LAST SESSION (Mon Jun 15 ~7 PM ET → Tue Jun 16 ~9:40 AM ET)

- **🔴🔴 BOJ HIKED 25bp → 1.00%** (Jun 16, overnight ET — the "JGB movement last night" Will flagged). Vote **7-1, Asada dovish dissent for HOLD**; growth+inflation outlook RAISED; **Uchida fronted presser** for absent (hospitalized) Ueda, "further hikes not imminent" guidance, boilerplate FX line. **MODAL delivered-as-priced — NOT the hawkish tail.**
- **Market:** USDJPY **160.36 (+0.25%)** — yen WEAKENED on the hike (buy-rumor-sell-fact); FXY **$57.22** flat; JGB 10Y ~2.6% / 30Y ~3.78% (wire; +~1-5bp; MOF CSV reflects ~Jun 17 — boot.py still shows Jun-15 2.589/3.725); Brent **$80.51 (−3.2%, sub-$81)**. **CH-004 confirmed in live tape: fully-priced hike did NOT unwind carry** — 81%-of-peak CFTC fuel never lit (no surprise to light it).

### LAST SESSION (Tue Jun 16 AM — boot + BOJ resolution write-back)

- **Boot:** clean pull (origin synced @ 30b729ca), full doc-stack read, boot.py + live fetch.py + WebSearch (BOJ decision + reaction). Identified BOJ result as already-out overnight; reported live to Will before write-back.
- **BOJ resolution written back (Will-directed):** 5 files —
  - **PREDICTIONS.tsv:** SAM-21 ✅ CONFIRMED, SAM-24 ✅ CONFIRMED, SAM-23 ❌ FAILED (calibration win — pre-marked 72%→~30% CH-011), SAM-26 ❌ FAILED (pre-marked 70%→~25%). Scoreboard → **9 CONFIRMED / 10 FAILED / 1 special / 0 OPEN.**
  - **STATUS.md:** added § BOJ JUN 16 RESOLVED snapshot block at top; fixed stale "next catalyst" banner; flagged Jun-15 market table as pre-decision.
  - **TIMELINE.md:** new top RESOLVED — Jun 16 narrative entry; header bumped.
  - **CHANGELOG.md:** dated 2026-06-16 entry (old→new view; no version bump — v1.6 is the structural re-underwrite).
  - **CALENDAR.md:** BOJ Jun 16 row → ✅ RESOLVED.
- **Position UNCHANGED — money fields untouched** (13 sh @ $58.32, $58C, $55.05 stop, $798). **Jun-18 $58C salvage thesis flagged WEAKENED** to Will (no IV-pop to sell into; likely near-total loss vs modeled $5-10) — flagged not acted, Will's call. Stop $55.05 doesn't fire (AND-condition's "BOJ dovish" leg false).
- METSUKE not spawned (no money-field moves; TRADE/STRATEGY not staled by a resolution-only write-back — but see NEXT #1 re STRATEGY ceiling-discount scoring).

### NEXT SESSION

**Imminent (tonight / tomorrow):**

1. **🟠 Japan May trade balance — TONIGHT ~7:50 PM ET** (Jun 17 08:50 JST). Run `trade_balance_japan.py --consensus <wire ¥B>`; adjudicate branch a/b/c (diplomacy + Hormuz still physically closed → bias branch c: surplus persists, ME volumes depressed → inconclusive, defer to June TB). Cost-side lens (KB-188-190: pricier non-ME crude).

2. **🔴 Wed Jun 17 FOMC + dots** (2pm ET) — ~99% no-change; watch dots for HIKE-lean (regime-flip confirm, Pillar-1 headwind), not rescue. **Re-check Polymarket Fed-2026-hike 36% (Mon) vs 52% (Sun) discrepancy** — thin-liquidity discipline.

3. **STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION — score by Jun 18 EOD JST.** Delivered hike reclassifies SAM-08/20 as TIMING failures; the Jun-16 **dovish-side dissent (Asada) + "not imminent" guidance** is fresh evidence favoring the *retire-to-friction / modify* branches over vindicate-widen. Also resolve the $58C tail-estimate test (market ~3-4% vs SAM ~10% — SAM's ~10% looks too high in hindsight; no pop materialized).

4. **🔴 Thu Jun 18** $58C expiry; **Fri Jun 19** National May CPI. Post-settle: v1.6 re-underwrite (incl. FXY-vehicle question).

**Carry-forward (post-BOJ):**

5. **Iran docket update (Will-DEFERRED Mon Jun 15, wait-and-see):** ⚠️ keep caveated per Orc/Prome Jun-16 review — do NOT harden to "digital MOU signed / Iran confirmed / Geneva ceremony" without primary/strong-source confirmation. Current committed-doc framing ("agreement reported / leaders welcomed / formal implementation pending / NOT Tehran-issued / unsigned") is correct; update only when primary confirms a signed text + Iranian statement.
6. **v1.6 rewrite** per `proposals/2026-06-10_v16_rewrite_spec.md` (post Jun 16-18 scoring; RED pass on draft pillars first). Fold in: oil-channel-DORMANT relabel; energy transmission-severing; SoftBank tail; **NISA amplifier → CARRY-UNWIND METHOD enrichment** (residual/2nd-order term); Channel-1 deferred-vs-retired (4-of-4 + Feb-2026 regulatory-forbearance reinforcement). + A. position re-underwrite + B. PROME network-reframe + C. hedge-cost tripwire. Eval re-baseline; OS.1 close; Dec-1.25% re-verify if Branch A fires.
7. **SAM-23 framework re-anchoring CHANGELOG entry** (post-scoring; CH-011 driver/disorder + no-strike decay + Jun-14 empirical 6+ orderly-sessions cites).
8. **RED post-BOJ refresh** — hold-scenario; structural-pillar TIMING under CH-032 band; SAM-23 post-event anchor; Fed-hike → CH-005.
9. **Research backlog (Will-brainstorm Jun 15, Tier 2/3 un-pulled):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.
10. **Auto-memory candidate (Sun Jun 14, Orc-endorsed):** "a cross-agent caveat protects you not the receiver — suppress a non-physical/known-unreliable metric, don't caveat-and-ship." + KB-183 local refinement ("at non-physical magnitudes the magnitude impeaches the sign too"). Authorize at next boot.
11. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) post-Jun-16 break = BOJ dovish AND USDJPY 167+/no MOF. NEXUS_BRIEF rollout = Will-action.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
