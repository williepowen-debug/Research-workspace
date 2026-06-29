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

### CHANGES SINCE LAST SESSION (Mon Jun 22 closeout / 6/25 note → Mon Jun 29 ~2:29 PM ET boot)

- **🟢 POSITION CONFIRMED FLAT by Will (6/29) — the biggest change.** SAM's docs had carried a phantom 6-sh post-trim FXY stub (13→6 trim, fill "unconfirmed" since 6/25); **Will confirms NO current FXY position.** Reconciled all live surfaces to FLAT this session.
- **CFTC Jun-23 (rel Fri 6/26): −146,104 / 81.2% — FIRST COVER off the 83.4% top** (+4,028 WoW; longs −3,677, shorts −7,705). Still deep HOLD band, amplifier +5pp ON. SAM-29 leg-1 holds (~32K room); SAM-30 reclaim moved away (3.8pp shy). No bucket re-mark.
- **USD/JPY 161.96 — weakest since ~1986 (40-yr low)** via slow ORDERLY grind (+0.09% on the day); MOF silent 13d at 160+. Brent $73.85 (~−24% cum). JGB 10Y 2.611% (Jun-26 pub, ↓). MOF weekly net BUYING.
- **Tokyo Jun CPI (6/26): core-core 1.9% sticky** (+30bp vs May 1.6); BOJ SoO (6/24) hawkish-of-priced. Mild hawkish ticks; confirmatory only.

### LAST SESSION (Mon Jun 29 boot — yen-40yr-low question + POSITION RECONCILED TO FLAT; Will-driven)

- **Booted** (git clean 0/0; left PROME's uncommitted SCRATCH.md alone), ran full Monday boot.py sweep, refreshed STATUS market data + carry anchor (CFTC Jun-23 81.2%).
- **Will flagged "yen crashed to 40-yr low — surely this matters?"** Verified the live tape (161.96, **+0.09% — orderly grind, NOT a crash**); checked for fresh MOF reaction (none; $72.5B May intervention "largely ineffective — drivers structural" per CNBC). Gave the honest read: **yen-weak is AGAINST a long-yen book**; the level isn't the trigger, *velocity* is; orderly grind = no near-term catalyst. (Discipline: verified live print before answering the headline.)
- **Will: "We do not have any current FXY positions."** → **Reconciled ALL live surfaces to FLAT** (STATUS / TRADE / NEXUS_BRIEF / THESIS §POSITION / STRATEGY). Preserved every position-independent analysis (thesis/channels/pillars/predictions/watchlist); **reframed the carry-convexity-tail as a watch-for-entry thesis** (NOT EV-positive to initiate at MEDIUM/break-even — deploy only on a fired trigger). **Did NOT fabricate a close price/date** (none provided). Historical/audit files (MAINTENANCE, *_MEMORY, CHANGELOG) left intact.
- **Defaults set (Will can flip either):** record = FLAT-from-here, no exit detail; forward = keep thesis warm as watch-for-entry.
- **News sweep** (4 angles): no fired trigger; mostly Jun 16-22 vintage. Material: **US-Japan FX coordination stepped up** (Katayama-Bessent "aligned/bold steps", Jun 22 — raises the MOF-spike watch-route) + **BofA sees 3 Fed hikes → 4.25-4.5%** (hardens Fed-widening). Logged to STATUS + NEXUS SENDING(HENRY).
- **Tradeability scan (Will asked "anything tradeable now?"):** directional trades all pass — long yen break-even; **short yen = the trend (carry pays) but negative-skew → declined** (selling at the 40-yr low in front of the convexity bomb); EWJ-puts/bank-shorts un-triggered; JGB-supply gated. **Only honest candidate = non-directional LONG JPY VOL** — monetizes the coiled-at-record + 81%-positioning + rising-intervention-risk setup *without* the direction call that keeps being wrong. **GATED on a vol-cheapness check** (FXY proxy 11.78%, already up off the 9.40 post-FOMC trough; KB-183 caveat → need a clean USDJPY-IV source before greenlighting). Flat is fine if vol isn't cheap.
- **Closeout edits:** CALENDAR + CATALYSTS.tsv pruned in sync (Jun 23-26 resolved rows); CHANGELOG 6/29 entry (no version change); NEXUS refreshed (FLAT + FX-coord + JGB-supply pivot); JGB-supply scoping doc created.

### NEXT SESSION

**🆕 NEW PRIMARY THREAD (Will-directed 2026-06-29): develop the JGB long-end SUPPLY/DEMAND thesis.** SAM is flat + the carry-tail is break-even, so effort pivots to the only-pillar-still-firing (Pillar 2 J-ICS lifer abandonment) + the reflationist-board / Takaichi fiscal supply side = a DOMESTIC JGB/curve thesis needing no carry trade. **Scoping doc written: `research/outputs/JGB_SUPPLY_DEMAND_THESIS.md`.** Execute gated on Q1 = **TRADEABILITY** (resolve FIRST — is there a Will-accessible vehicle for "long-end yields rise," or is this a signal thesis that feeds LIQUID?). Then BOJ-backstop reaction-function → supply quantification → demand depth. Frame as MECHANISM/CURVE, NOT a 4.0% threshold (SAM-26 trap). Catalysts: Jun-30 Sato seats · Jul-7 30Y / Jul-22 40Y auctions · Jul-31 BOJ FY2027 purchase-plan. *(Keep carry watch-for-entry low-touch alongside.)*

1. **If Will provides exit detail** (close price/date/realized P&L) → log it in TRADE Entry Decision Card + CHANGELOG; it's the one money fact still TBD. Otherwise FLAT-from-here stands. (Note: SAM's docs had carried the position as live for ~1wk — a real data-integrity miss; positions are Will's truth.)
2. **Watch-for-entry monitoring** — SAM-28..31 now read as ENTRY-triggers, not position-tripwires. Re-entry case activates ONLY on a fired trigger: disorderly MOF spike · CFTC build through −153K/85% (SAM-30) · risk-off yen-haven re-couple (SAM-31) · Fed-dot walk-back. Don't chase the grind to the 40-yr low.
2b. **🟡 LONG-VOL CHECK (the one near-term actionable idea — Will-raised):** if Will wants it, pull a **clean USDJPY implied-vol read** (CME CVOL is license-gated; try a wire/broker vol quote or WebSearch USDJPY 1-3mo IV) and judge cheap-vs-coiled. Greenlight non-directional long vol ONLY if demonstrably cheap on a clean source (FXY proxy 11.78% is up off the 9.40 trough — NOT obviously cheap; KB-183 caveat). Kill it if vol already firmed. *This is the cleanest expression of SAM's actual (non-directional) high-conviction view.*
3. **Next CFTC = Fri Jul 3** (Jun-30 data). **Tomorrow Jun 30: Sato takes Nakagawa's BOJ seat (dissent bloc 3→2) + JGB 2Y.** Then Jul 1 Tankan, Jul 7 30Y auction, Jul 31 BOJ.
4. **CALENDAR prune (deferred this session):** clear resolved 6/23-6/26 events (SoO / Tokyo CPI / 5Y+20Y auctions / CFTC) from the forward tables → KOYOMI or inline.
5. **Carried from Jun-22 (still open):** evals re-baseline (v1.6 structure changed); KURA FLOW/VX re-derivation; archive-compress the SUPERSEDED historical bodies (TRADE Options Layer / STRATEGY OPTIONS-RULES / JUN-16-RECONCILED / TAKAICHI).
6. **Auto-memory candidate:** phantom-position reconciliation pattern (docs carried a position Will didn't hold → flag-then-confirm-then-reconcile-to-FLAT *without* fabricating money fields). Assess vs [[feedback_position_cost_basis_not_authoritative]] before promoting — likely a clean application, not net-new.

**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

**Closeout (Mon Jun 29):** boot + FLAT reconciliation (5 live surfaces) + STATUS market refresh + news sweep + tradeability scan + new JGB-supply thread + docket prune (CALENDAR+CATALYSTS in sync) + CHANGELOG/NEXUS refresh. **First commit `b43541da`** shipped the reconciliation + boot data + scoping doc (verified Jun-22 v1.6 finalize already on origin — local==origin). Closeout-edits commit + auto-push follow. **Also done this closeout (Will-requested):** STATUS PRE-v1.6 banner PRUNED (12,098→496 chars) + Signal-Status "KEY LIVE" refreshed → Jun-29. **Then a full STATUS REFACTOR (Phases 0-5, tracked):** Phase 0 verified TIMELINE coverage (gate); compressed the resolved-narrative blocks to pointers — FOMC+BOJ (37→6), BOJ ASSESSMENT (64→8), INTERVENTION+SECONDARY (39→2, kept MOF op-table + live Fed tripwire); refreshed MARKET DATA → lean Jun-29 table; pruned WHAT TO WATCH → forward-only; KEY THRESHOLDS Status refreshed Jun-26/29; fixed 3 dangling cross-refs. **STATUS 336 → ~190 lines (under the 250 cap), Doc-Ownership-clean (narrative in TIMELINE, snapshot in STATUS).** Nothing lost (Phase-0-verified). **Still deferred (flagged):** REFERENCE DATA channel-taxonomy block (v1.5-era, labeled reference — next pass); KURA FLOW/VX re-derivation (VX 31d); archive-compress SUPERSEDED TRADE/STRATEGY bodies; evals re-baseline (Will-action).

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
