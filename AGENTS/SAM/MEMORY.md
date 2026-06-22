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
- *(Promoted to auto-memory Jun 21: [[feedback_suspect_fresh_pull_over_curated_record]] — first-touch wire/primary not an aggregator; when a fresh pull conflicts with a verified record, suspect the PULL (provenance asymmetry), not the record. Re-confirmed against wire/official series 6/21 before promotion (the stockpil 2.2%/2.1% were wrong; SAM's 1.4/1.9 & 1.5/1.4/1.8 match the wire); near-missed a SAM-27 scoreboard corruption. Will-directed promotion.)*
- *(Promoted to auto-memory Jun 10: [[finding_ohlc_verify_before_session_claims]], [[finding_pre_registration_discipline_through_corroboration]] — Advisor-endorsed, Will-forwarded; veto = delete files + index lines.)*
- *(Promoted to auto-memory Jun 18-19: [[finding_boot_sweep_macro_regime_context]] (boot regime-context check — Warsh-since-May-22 sat un-modeled 4wk), [[finding_comprehensive_grep_over_sampling]] (verifier-side discipline — PROME-named standard after Step 1.5 catch), [[finding_risk_control_separate_from_sizing]] (post-binary stop audit — Will Jun-18 distinction). All three Will-approved Phase C; cross-applicable to multiple agents — see index in `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`.)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Sun Jun 21 ~5:23 PM ET closeout → Mon Jun 22 ~4:11 PM ET boot)

- **🔴 CFTC Jun-16 print landed (3:30 PM ET Mon) — the EV-gate observable:** net **−150,132 / 83.4% of cycle peak**, built −4,314 WoW, **zero cover through the catalyst** → pre-registered HOLD-band top edge: **frame SURVIVES the margin test** (decisive negative — cover <−120K → trim/close — did NOT occur), 1.6pp shy of the −153K/85% strengthened line so amplifier stays +5pp. Genuine Pillar-4 confirmation.
- **🟢 Brent decoupling test = SHRUG:** Sat Jun-20 Iran *declaratory* Hormuz re-closure produced NO spike (Brent ~$78, −2% day, ~−19% cum from $96.78 Jun-3) → declaratory-not-physical confirmed; oil-in-yen stays dormant.
- **Levels flat-to-marginally-weaker-yen:** USDJPY 161.58 (MOF silent 6d at 160+; 162 within 0.3%), FXY $56.79, JGB 10Y 2.656 / 30Y 3.786 / 40Y 3.741 (MOF Jun-19 pub — long-end drifted ↑~2-4bp on the week, no stress; below the TE-aggregator 3.84% carry-note). National May CPI soft (verified Sat: 1.5 / 1.4 / 1.8).

### LAST SESSION (Mon Jun 22 ~4:11 PM ET boot → closeout — THE v1.6 FINALIZE ARC; Will-driven, multi-turn)

**This session bumped the thesis v1.5.1 → v1.6 [MAJOR] (re-centered COMPRESSION → CARRY-CONVEXITY-TAIL) and trimmed the position. Money fields = Will's ground truth (see NEXT #1 — trim executes Tue Jun 23).**

- **Booted + caught the CFTC EV-gate** (the convergence point Will timed the boot for): −150,132 / 83.4%, held through the catalyst, no cover → HOLD-band, frame survives margin. Wrote to STATUS + CALENDAR (EV-gate row resolved). Brent decoupling test = SHRUG.
- **Refreshed the `V16_RED_DIALOGUE` scaffold** with the resolved CFTC print (anchor was pre-3:30), then ran the **SAM⇄RED adversarial dialogue** (Will relayed RED's turns). **Converged 6-of-6 in one round-trip:** #1 BROKEN@MED-HIGH / SURVIVES@MEDIUM (net EV break-even-to-negative → trim signal); #2 two-legged SPF (cover<−108K tail / no-trigger-by-Sep-18 MODE); #3+#5 window LOCKED **Sep-18-2026**; #6 Channel 1 **RETIRE** (direct foreign-SALES re-add tripwire); #4 vehicle gate → (b)/(c) OFF, finalize = (a)/(d).
- **Finalized THESIS v1.6** — canonical rewritten (carry-convexity-tail; Pillar audit; Channel 1 RETIRED, Channel 4 NEW center); v1.5.1 → `thesis/THESIS_v1.5.1_ARCHIVE.md`; DRAFT superseded (git rm at commit); CHANGELOG **[MAJOR]** entry.
- **Propagated v1.6** across STATUS (banner/position/stop/buckets/thresholds), TRADE, STRATEGY, PREDICTIONS (4 OPEN tripwires SAM-28..31), NEXUS_BRIEF (cross-agent re-marks shipped).
- **Position — Will-approved trim:** 7 of 13 → **6 sh** + stop tightened $55.05 → **$55.50 / USDJPY ≥162.5**; vehicle OFF. Market closed Mon PM → **executes Tue Jun 23** (fill TBD = Will's ground truth; recorded as decision, not fabricated).
- **METSUKE Run-7 drift sweep** (post-MAJOR-bump): 18 flags, **all 18 applied** (TRADE/STRATEGY deep v1.5.1 prose converted to v1.6 — Risk Factors/Key Dates rebuilt, Options/reconciled/Takaichi sections marked RESOLVED/closed) + 5 stragglers caught on a post-apply grep; SAM-applied logged in METSUKE_MEMORY.
- **Committed** the full finalize locally (pathspec, SAM dir only; push deferred to a coordinated window).

### NEXT SESSION

**Imminent — execute the trim + watch the v1.6 tripwires:**

1. **🔴 EXECUTE THE TRIM Tue Jun 23** (market was closed Mon PM): sell 7 → 6 sh at the open. **True up the realized P&L + exact fill** across STATUS § FXY POSITIONING + TRADE (money fields = Will's ground truth — I recorded the decision, NOT a fill price). **Flag `FORGE/STATUS.md` update to PROME** (shared file; don't self-edit). Stop is $55.50 / USDJPY ≥162.5.
2. **Monitor the convexity-tail tripwires (SAM-28..31) through the LOCKED Sep-18 window:** leg-1 cover <−108K → frame LOW (SAM-29); leg-2 no eligible trigger by Sep-18 → LOW (SAM-28); reclaim MED-HIGH if CFTC builds through −153K/85% (SAM-30, by Jul-31) OR cross-pair yen-haven re-couples (SAM-31). These are the live forward observables now.
3. **Next CFTC = Fri Jun 26** (Jun-23 data) — first post-trim read; watch vs the −108K/−153K tripwires.
4. **Wed Jun 24 BOJ Summary of Opinions** — first granular read on the 7-1 board reaction function (Asada dovish-dissent rationale; oil-inflation linkage; Q4-vs-later next-hike read). Then Jun-26 Tokyo CPI + Jun-30 Sato seat + Jul-1 Tankan + Jul-7/22 super-long auctions + Jul-31 BOJ.

**v1.6 finalize cleanup (low-priority tail):**

5. **evals re-baseline** (Will runs, fresh skip-boot session) — v1.6 changed load-bearing structure; the frozen-scenario suite needs re-baselining per `evals/README.md`.
6. **Run-8 METSUKE straggler grep** on TRADE/STRATEGY (`single-path|Channel 1 deferred|under v1.5|multi-month tail`) — 4 low-signal framing residues SAM deferred this session — + **archive-compress the historical bodies** (TRADE Options Layer, STRATEGY OPTIONS RULES / JUN-16 RECONCILED / TAKAICHI DISPOSITION — all marked SUPERSEDED at their heads this session, bodies retained for one cycle).
7. **KURA FLOW/VX full re-derivation** per the v1.6 finalize (FLOW-JPN-5.02 / 6.02 / VX-SAM-11.02 trade-balance refresh) — too much moved for a surgical fix.
8. **Auto-memory candidates (un-promoted, pending Will endorsement):** (a) the source-discipline finding (Findings 6/20); (b) NEW candidate — the RED-dialogue-scaffold (pre-registered SURVIVES-bars + interlocked-cluster resolution: locking the Sep-18 window resolved #2/#3/#5 together) converged a MAJOR thesis bump in ONE round-trip — assess vs [[finding_liaison_convergence_pattern]] / [[finding_adversarial_brief_for_pair_teams]] before promoting (may be incremental).

**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

**Closeout (Mon Jun 22):** the v1.6 MAJOR finalize — committed locally (pathspec, SAM dir only; push deferred to a coordinated window). Surfaces: THESIS v1.6 (+ v1.5.1 archive + DRAFT git-rm) / CHANGELOG / STATUS / TRADE / STRATEGY / PREDICTIONS / NEXUS_BRIEF / V16_RED_DIALOGUE / METSUKE_MEMORY (Run-7) + this MEMORY closeout. SAM⇄RED converged 6-of-6; METSUKE Run-7 18/18 applied. **Channel 1 disposition RESOLVED this session: RETIRED** (closes the prior Will-directed re-examination). **Pending push:** all of the above — next coordinated window sweeps it.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
