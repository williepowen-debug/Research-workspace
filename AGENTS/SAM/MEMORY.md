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
- [2026-06-04] **Subagent-trio habit run pays off immediately** — first parallel-spawn (METSUKE+KOYOMI+KURA, teams-mode) caught a TRADE:246 Rule #3 propagation gap I missed, primary-source verified Sato characterization, surfaced KURA-KOYOMI dependency pattern. Consistency-over-yield validated even on low-watermark days (KURA Run 4 was "low-yield" but produced KB-185 + 2 auto-memory candidates). Codified pattern. **[RE-VALIDATED 2026-07-02 at the opposite (high-watermark) extreme** — trio caught the modal-band contradiction, the Sep-18 window-end/BOJ-MPM coincidence, the 2025-base CPI discontinuity, and cleared the FLOW deadline breach. Performance review → MAINTENANCE 2026-07-02 entry. **Spawn guidance:** routine KOYOMI/KURA syncs run clean on cheaper model tiers (KOYOMI Runs 8-11 spanned Opus/Sonnet/Fable, all clean) — reserve the big model for post-pivot METSUKE runs + audit-heavy KOYOMI runs. METSUKE now has a named `verify-pass` mode (spawn same-session as any SAM inline sync); KURA default is now `full`.]**

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

### CHANGES SINCE LAST SESSION (Mon Jul 6 closeout → Wed Jul 8 ~9:30 PM ET spawn)

- **JGB 30Y auction (7/7) RESOLVED FIRM:** BTC 4.55x / tail 0.3bp — decisively above the pre-registered floor bar, highest BTC since May-2019. Meiji-Yasuda ~4.0% demand floor confirmed REAL flow.
- **US-Iran truce collapsed overnight 7/7→7/8** (US strikes, Iran retaliation); Brent +6.3% → ~$79.
- **USD/JPY 162.33 → 162.41**, holding in the 162–163 MOF zone; driver shifted from pure yen-side grind to oil-shock (Japan ~90% ME-oil-dependent) — still no risk-off yen-haven re-couple.
- CFTC Jun-30 print still unconfirmed as of this session (check next boot).

### LAST SESSION (Wed Jul 8 ~9:30 PM ET — PROME spawn: JGB 30Y auction print delivered to BOND + truce-collapse/oil-shock read)

- **(1) JGB 30Y auction (7/7) graded + relayed to BOND.** BTC 4.55x/tail 0.3bp vs Jun-10 baseline 2.936x/2.8bp — FIRM, clears the pre-registered bar with room to spare. SAM-32/v1.6.3 demand-floor thesis now has its strongest evidencing print (real flow, not announced-not-flowed); SAM-33 stays VOID. Note written to `AGENTS/BOND/inbox/2026-07-08_from-SAM_jgb-30y-auction-internals.md` — BND-11 read-through: FIRM → mildly lower P(soft US 30Y) ~−3-5pp (term-premium tilt, not flow-mechanical), leaning toward the fuller end given the print's strength; stacks with US 10Y reopen 7/8 clearing CLEAN.
- **(2) Truce-collapse/oil-shock MOF read:** USD/JPY 162.41, in-zone but oil-driven (not risk-off yen-haven — yen weakened despite the shock, consistent with THESIS § OIL-IN-YEN). No fresh MOF rate-check/strike evidence found overnight. Per CH-011, continuation of the existing orderly grind → strike-watch ARMED, still NOT FIRED. No re-mark of carry-unwind buckets (oil/MOU route already a named 60d driver; this is re-escalation of the same route, not new).
- **Files touched:** STATUS (7/8 session note + top banner + INTERVENTION STATUS + KEY THRESHOLDS refreshed) · docket/CALENDAR.md + CATALYSTS.tsv (7/7 auction row → ✅ RESOLVED) · PREDICTIONS.tsv (preamble updated) · NEXUS_BRIEF (As-of 7/8, FORWARD CATALYSTS row) · BOND inbox note (NEW). No thesis-level change; FLAT stands.
- **Prior sessions (7/6 zone-read + Packet-C first cut; 7/2 MOF-verify NO-STRIKE + Meiji-Yasuda floor → SAM-32 FALSE → v1.6.3; 7/2 subagent trio METSUKE/KOYOMI/KURA) compressed out — see git history + STATUS session notes for full detail.**

### NEXT SESSION

1. **Route the 7/7 JGB 30Y grade to LIQUID/HENRY too (shared test, not yet sent — only BOND got it 7/8).** FIRM: BTC 4.55x/tail 0.3bp, Meiji floor confirmed real. **Jul-22 40Y = second read** (super-long floor's hardest test; packet-C headline trigger paired w/ a soft 7/16 TIC — successive weeks). **Packet-C FULL synthesis w/ ZHAO due 7/16** (post May TIC + BoK).
2. **CFTC Jun-30 print — verify pulled** (was still showing Jun-23 data as of 7/8; check deafut.txt primary next boot). First read of whether shorts held through the 40-yr-low + ambush-story week; SAM-30 reclaim line ~3.8pp away; leg-1 (−108K) ~32K away.
2b. **Re-derive the STRATEGY modal band (METSUKE escalation)** — FXY $57.5-59.5 / USDJPY 154-160 contradicted by 2+ weeks of 160-162.6 tape; annotated UNDER RE-DERIVATION. Re-derive off the Jul-6 CFTC + Jul-7 30Y reads (per [[finding_re_derivation_surfaces_concept_failure]] — re-derive the framework, don't re-mark the number).
3. **MOF ambush-regime follow-through:** watch for any sharp yen-specific spike (the trigger now arrives unsignalled — catch follow-through, not the gap); ~7/31 MOF monthly = hard confirm of the 7/2 no-strike call. If a candidate fires, fast semi-confirm via BOJ current-account projections (~2bd).
4. **CH-010 accounting-basis question — REPRIORITIZED but still open:** RED's economic-value read won round 1 at 4.0% (Meiji buys); the question now is whether the impairment/forced-selling mechanism exists at ALL above 4.5% or the demand floor simply deepens with yield. Pair with **GPIF super-long stance** (still the open demand-leg gap).
5. **SAM-34 mid-July re-verify** (July-hike pricing; re-mark if >40%). NFP-soft cuts nothing BOJ-side; Ueda Sintra "underlying inflation below 2%" supports hold-85%.
6. **Route-4 watch (Fed-dot walk-back):** labor blocker cracked (NFP 57K/−74K revisions, ADP, Challenger cooling) but inflation leg intact — **Jul-14 US CPI** is the next route-4 input; a soft CPI + soft labor = the walk-back path starts pricing.
7. **If Will provides FXY exit detail** → log in TRADE Entry Card + CHANGELOG. **Carried-open:** evals re-baseline (v1.6.x); archive-compress SUPERSEDED bodies; ~~KURA FLOW/VX re-derivation~~ ✅ DONE 7/2 (full-structural review stays a KURA full-mode candidate); peers processing the Jun-30+7/2 signals (do NOT re-send); **🆕 Aug-21 National-CPI 2025-BASE re-baseline check** (measurement discontinuity — KOYOMI escalation); **🆕 verify BOJ SoO date for the Jul MPM** (fetch showed Sat "Aug 8," suspect); MOF quarterly per-op release (~early Aug, KOYOMI PENDING).
8. **Auto-memory candidates (assess, don't auto-promote):** (a) carried from 7/1 — adversary-subagent AUP false-positive (frame as "identify weaknesses," keep main-loop fallback); (b) 🆕 **rotation sell-leg vs abandonment** — net-flow prints can be the funding leg of a stated roll-up program; verify the PROGRAM (plan announcements, stated intent) before reading flow sign as regime direction. Close to [[finding_composition_mask_unmask_discriminator]]/stock-vs-flow but the program-vs-flow discriminator may be net-new.

**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive. *(NFP AHE MoM exact print unpinned — BLS 403s bots; curl w/ User-Agent per [[finding_edgar_403_user_agent_header]] next session if needed.)*

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
