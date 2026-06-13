# LIQUID — Cross-Session Memory

## Session Notes

### CURRENT SESSION (2026-06-13 Sat — boot + Fri closes + HY OAS retirement)

**Context:** Saturday boot (markets closed). Pull skipped — VIOLET tree dirty (uncommitted workbook/fred_cache files), my dir clean, no loss. Will gave three directives: pull Fri 6/12 closes, TEN calls closed, retire HY OAS tracking.

**Done:**
- **Fri 6/12 closes pulled** (yfinance, CBOE proxy basis): 10Y 4.487 / 30Y 4.975 (both still sub-threshold — oscillation holds); **Brent $87.33 = FIRST sub-$90 CLOSE** (stagflation-ladder clause-1 trigger; −$23.3 from peak); USD/JPY 160.19 (5th close >160); VIX 17.68 (cooled off the 22.22 CPI-day spike); APO $133.88 (Day 4 >$130); TLT 85.77; BIZD 12.71. *(FRED H.15 6/12 yields not yet posted — proxy stands.)*
- **TEN calls CLOSED** (Will, winner booked ~$7.11 ITM). Struck from Active Positions in STATUS + STRATEGY.
- **HY OAS tracking FULLY RETIRED (Will's call) → KB-LIQ-060.** Scope confirmed "full retire" via AskUserQuestion. Removed: macro HY OAS kill(<260)/confirmation(>320)/freeze trips, HY Energy >300, the `>320 → ALL` cross-agent signal (out of CLAUDE.md), KILL_MEMO_HY_OAS_260 (→ `archive/KILL_MEMO_HY_OAS_260_RETIRED_20260613.md`). Kept: CCC OAS as standalone tail watch (KB-LIQ-058). Credit leg now reads via BDC marks + APO mark-decoupling. **Files touched:** STATUS, CLAUDE (KEY THRESHOLDS + CROSS-AGENT SIGNALS + IDENTITY para + FILES), STRATEGY (3 trigger sections + positions + workbooks + asymmetry), IDENTITY (focus pts 1-3), CALENDAR (daily watch row), KB.tsv (+060), MEMORY.
- **Not rewritten (flagged):** thesis-architecture docs (`thesis/THESIS.md` §"bilateral 320/260 credit framework", `thesis/TIMELINE.md`) still describe the HY OAS frame structurally — left for a Will-steered thesis-level pass (cosmetic-vs-rederive decision), not unilaterally torn out. Historical record (inbox/processed, outbox/delivered, CHANGELOG, ML_historical, VX/FLOW registries, resolved PREDICTIONS LIQ-01/02) preserved as-is.

**Open follow-ups (carried):**
- **HYG $75P expires Fri 6/19 (T-4)** — recommend expire/close (dead, $79.94 vs $75; the 320-retest premise died with HY OAS). Will decision.
- **Thesis-doc HY OAS sweep** — THESIS.md / TIMELINE.md credit-framework sections await the thesis-level decision above.
- Externally-gated: FSK P/NAV 0.52 split/vintage verify; OBDC Q1 NAV owed; LIQ-03 resolves 6/30.
- **Push pending** — Saturday, no coordinated window; committed locally, sweeps next window.

---

### SESSION (2026-06-12 AM — boot + live refresh + APO trigger fire)

**Context:** Friday-morning boot, 4d since last session. All live-primary pulls (FRED + yfinance per the rule).

**Delivered:**
- **APO >$130 ×3 closes — HEARTBEAT line-80 reassess trigger FIRED 6/11** (6/9 $132.70 / 6/10 $131.14 / 6/11 $133.91). **NOT Trigger C** — KILL_MEMO escalation requires HY OAS *compression* concurrency; HY widened 274→280 over the window. Outbox → BROCK (they hold APO Dec $95P, same line).
- **OHLC count correction:** prior STATUS had 6/8 as "Day 1" off an intraday print ($131.5); the 6/8 CLOSE was $127.57 — below the line. Streak starts 6/9. Day-counts are close-basis only (fleet memory `finding_ohlc_verify_before_session_claims` applied).
- **HY OAS direction REVERSED:** 280 (6/10), cushion to 260 kill back out to 20bps — first sustained widening since mid-May. CCC 957, BB 170 (CCC−BB 787).
- **May CPI integrated (printed 6/10 while dark): HOT** — headline +0.48% MoM / 4.18% YoY (accel from 3.78%), core +0.21% / 2.81%. VIX spiked 22.22 on the print. Claims 229k (4th straight rise). Stagflation-trap texture into 6/17 FOMC.
- USD/JPY 5 sessions >160 sustained; Brent $87.95 (-$22.6 from peak); SOFR-IORB -5bps clean; 30Y 5.03 >5% sustained.
- STATUS (header/kill-proximity/3 dashboards/signals/positions/windows) + CALENDAR (CPI+claims resolved, rolled to 6/12) refreshed.

**Session continuation (6/12 PM — domain audit + THESIS pass via Orc review loop):** Full-domain staleness audit (punchlist Tiers 2-7). THESIS v2.0 restamped to 6/12 through a three-round review loop with Will's coordinator layer ("Orc") — plan → their grade → my recomputation. **Material outcome: duration regime re-derived** (30Y "sustained >5%" was wrong since 5/28 — 5.00-pivot oscillation; 6/11 closed 4.951/4.463 on a SOFT 30Y auction the market rallied through: BTC 2.33, indirect 59.9%, dealer 14.7%; vs 10Y reopen 78.2% STRONG = tenor-bifurcated Leg B). **Conviction 65→60** (CHANGELOG pivot). Review-loop scorecard 2-1 Orc: my 6/8 ">5% sustained" error, Orc's 6/4-anchoring error, then **my adjusted-vs-raw basis error** — re-graded APO's May streak on yfinance's `auto_adjust=True` default and "found" a 5/11 dip ($129.91 adj) that never printed ($130.46 raw; ex-div 5/19 $0.563). Raw record: ten straight closes >$130, 5/8–5/21 — original HEARTBEAT Day-3/Day-9 reckonings were right all along. **Rule now in THESIS §9 + auto-memory: price triggers grade on unadjusted closes (`auto_adjust=False`, Close column), basis declared inline; adjusted series mutate retroactively at ex-dates.** Auto-memory `finding_circular_corroboration_via_state_file` extended with writer-AND-grader variant + the three basis variants. Bonus finds: 5/21 "10Y reopening" Leg-2 gate was actually the 10Y TIPS reopening (mislabeled since BOND's 5/19 signal); CALENDAR/USER "May 5 30Y auction" misdate fixed (actual 5/13, stop 5.0460). Tier-5 auction gap closed via TreasuryDirect.

**Session continuation 2 (6/12 PM — TIMELINE + Tier-5 data + BDC light populate):** TIMELINE rolled forward (Orc-graded; Row-2 conflation fixed pre-commit; 8 live rows; KB-LIQ-059). Tier-5 closed: Leg A UN-STALED (reserves $3.081T stable — "draining" unsupported; SRF ~$0 both legs; RRP zero), April PCE 3.72%/3.27% accel, NFP +172k, May auction indirect filled. LIQ-02 → MISS at the letter (+31bps max vs +50); LIQ-03 OPEN, resolves 6/30 (interim ~S+130-145). Basis canon += Brent ICE settle / JPY 5pm ET / H.4.1 as-of. Energy-HY ask → formal BRENT outbox. BDC monitor light-populated (Will's call): div-cut trigger FIRED ×4 (MFIC/OCSL/OBDC/FSK), activation conditionally met pending FV/Cost; ⚠️ FSK P/NAV 0.52 needs split/vintage verify; OBDC NAV not found (avoided Onex-conflation trap). **First push window opened — everything through 6bee0ca3 on origin.**

**CLOSEOUT (6/12 PM, Heavy tier; model switched Fable→Opus mid-close):** Full-day session done. **CATCHUP_PUNCHLIST fully closed** (all tiers; boot docs / thesis layer / TIMELINE / workbook / predictions / data gaps / BDC monitor — green). **All work committed AND pushed** (coordinated window opened; tree clean, ahead 0/behind 0; my commits rebased to new SHAs, content intact). Audit method this session: every load-bearing count recomputed from raw series + Orc review loop on the 5 load-bearing thesis/TIMELINE surfaces.

**Open follow-ups (carried):**
- **HYG $75P + TEN $30 calls both expire Fri 6/19 (T-5).** HYG: recommend expire/close (dead, $79.94 vs $75). TEN: ITM ~$7.11 winner — exercise/sell decision needed. **Both Will decisions, window closing.**
- **Externally-gated waits:** BRENT energy-HY OAS pull (outbox sent); FRED 6/11 yield prints (H.15 lag, ^TNX/^TYX proxy stands); FSK P/NAV 0.52 split/vintage verify; OBDC Q1 NAV still owed.
- **Dated:** LIQ-03 resolves 6/30 at the letter (interim ~S+130-145, below 160 trigger).

### PRIOR SESSION (2026-06-08 — boot from 18d-stale + NEXUS blocker + full Tier-1 catch-up)

**Context:** Will booted LIQUID after ~18d dormancy (STATUS frozen 5/20). Two goals: (1) clear NEXUS's reactivate-before-6/10 blocker, (2) bring all boot docs current via a phased Tier-1 cleanup. Long multi-phase session.

**Delivered:**
- **Boot + live-tape catch-up:** STATUS refreshed 5/20→6/8 (3 dashboards). Big moves: APO co-trigger self-resolved then **RE-ARMED** (re-crossed $130 on 6/8 bounce, ~$131.5); Brent reversed $110→~$91; USD/JPY crossed 160; 30Y eased to 5.01 (still >5%); HY OAS 276 (16bps to kill, narrowing).
- **NEXUS blocker cleared (C3 + T-08):** reads → NEXUS outbox + PROME (Will-decision Option A executed). C3: macro HY 276 counter-signal partially artificially strong — CCC +17 vs macro -10 (~24bps bifurcation); energy HY (285 stale) the primed corner. T-08: credit-pin intact-and-primed + caveat that a leakage event may widen HY *without* a safe-haven UST cushion (30Y>5%, foreign exit, JPY 160). New durable finding **KB-LIQ-058** (aggregate HY masks sector bifurcation).
- **Tier-1 boot-doc cleanup (5 phases):** CLAUDE.md thresholds / CALENDAR (rolled fwd, past events→Resolved w/ pending markers) / IDENTITY Current Focus / STRATEGY (+false-kill guard) / USER. All restamped 6/8 from corrected STATUS. `CATCHUP_PUNCHLIST.md` created (tracks Tier 0-5).
- **Live-primary catch:** double-checking Phase-3 figures caught dashboard.py staleness on yfinance rows — APO $129.93→$131.55 (re-crossing $130), BIZD $12.56 (back above trigger), not stale dashboard values. FRED rows (HY/CCC/rates) confirmed reliable. The FRED-reliable / yfinance-laggy split is the sharpened rule.
- **BROCK read (for APO question):** we already hold **APO Dec $95P** (deep-OTM tail-hedge — correct size, since APO mega-cap is last domino to crack via fee/Athene insulation). BROCK PC thesis ACCELERATING (Stage 2→3 pivot, 4-fund gate cluster, record 6% default). Folded into IDENTITY #3.

**Open follow-ups (carried):**
- **APO re-cross watch — Day 1 of 3.** If it holds >$130 next 2 sessions → Trigger C re-arms → BROCK/PROME signal candidate.
- **Catch-up NOT finished:** Tier 2 (thesis), Tier 3 (workbook — incl. KILL_MEMO false-kill detail deferred from Phase 4, + likely-stale BDC monitor + PREDICTIONS scan), Tier 4 (reference/inbox), Tier 5 (external data). See `CATCHUP_PUNCHLIST.md`.
- **HYG put decision** still open (recommend close/expire; HYG $79.54 deep OTM, June expiry).
- **Pending push:** committed locally 6/8; NOT pushed (Will-coordinated). Next window sweeps it.

### PRIOR SESSION (2026-05-20 — file-tree audit + 20Y auction + STATUS restructure)

**Context:** Will requested file-tree audit at boot. Session evolved through 4 distinct phases: hygiene → 20Y signal pickup → STATUS prune → POV-preservation + dashboard restructure.

**Delivered:**

**Phase 1 — File-tree audit + 5 cleanups:**
- CLAUDE.md FILES table expanded (was missing 9 active files — boot docs, thesis/, workbook secondary). 12 → 22 rows.
- `archive/recon_legacy_20260315/recon_subfolder/` flattened (single-file ghost dir).
- `archive/status_snapshots/` subdir created for 3 loose STATUS files; archive root now uniform subdir-only structure.
- CALENDAR.md verify-pass — 8 dates corrected via web-search vs Treasury/BLS/BEA/Fed schedules. Biggest: **20Y auction was 5/20 (today), not 5/21**; April PCE Thu 5/28 (not Fri 5/30); NFP Fri 6/5; CPI Wed 6/10; FOMC Wed 6/17 (decision day, not 6/18).
- `CUSTODIAL_VELOCITY_PROTOCOL.md` (270 lines, Feb 11) — Belgium watch cadence dormant ~14 weeks. Decision: **slim to KB entries.** Wrote KB-LIQ-055 (Foreign_Custodial_Flow_Disaggregation) + KB-LIQ-056 (Collateral_Velocity_Ratio); moved full doc to `domain/sources/CUSTODIAL_VELOCITY_PROTOCOL_20260211.md`. Resolves an open-follow-up that had been carrying for 2 sessions.

**Phase 2 — 20Y auction integration (Will-prompted; signal not in my inbox yet):**
- Will flagged that BOND had probably sent a signal. Found 2 BOND outbox files awaiting HERMES delivery: `2026-05-19_to-LIQUID_10y_break_30y_sustained.md` (pre-auction ask: SOFR-IORB -12bps = ample-reserves or stress-not-yet-funded?) and `2026-05-20_to-PROME_20Y-post-auction.md` (post-auction read).
- **5/20 20Y NEW issue ($16B, CUSIP 912810UV8) printed soft-but-functional, NO orange trigger:** BTC 2.55 (soft), indirect 67.7% (STRONG vs 55% LIQUID trigger), tail 0bp (stopped on screws, paid through screen), dealer 9.4% (clean near 4/22 baseline 8.6%).
- KB-LIQ-057 (Foreign_Demand_Showed_At_Price) authored — refines v2 Leg B: foreign-demand-canary reading of 5/13-5/19 long-end break is disproved by this print. Demand hole compresses price, doesn't break mechanism. Late-session sharpened to two-poles framing after Will-prompted reflection (see "Open follow-ups" below).
- Outbox to BOND: 4-point cross-check answering SOFR-IORB ample-reserves question. (HERMES sweep pending.)

**Phase 3 — STATUS prune (265 → 153 lines, 42% reduction; well under 250 ceiling):**
- Steps 1+2: Deleted Apr 16 Refresh (~48 lines) + Apr 16 Plumbing Dashboard (~23 lines) + replaced Durable Signals Log table with KB.tsv pointer (~16 lines). Fixed thresholds-table contradiction (Apr 16 LIQ-01-320 framing was contradicting current 260-kill / 320-confirmation HEARTBEAT framework). Deduped USD/JPY rows. Pinned APO day-count at Day 9 (5/8→5/20 inclusive).
- Steps 3+4: Compressed May 18 Revival Read + May 19 Live Re-Verification narrative sections (~50 lines) into one 5-line "Key Recent Marks" preserving the load-bearing 30Y 5.168 intra-day life-high. Restructured single mixed-metric Thresholds table into **3 separate dashboards per CLAUDE.md prescription** — Credit Spreads, Domestic Plumbing, Foreign Official. Each dashboard is a single table; metrics no longer mixed across categories.
- Re-stamped 5/19→5/20 across Cross-Domain Signals / Active Proposals / Active Positions / Danger Windows.

**Phase 4 — POV preservation + KB-LIQ-057 sharpening:**
- Before pruning historical STATUS narrative, Will raised the concern that LIQUID's POV-evolution arc would be lost. Extended `thesis/CHANGELOG.md` with **5 POV-pivot entries** (5/20 foreign-demand-canary refined → 5/19 trigger-watch dormancy → 5/18 channel migration → 4/16 SOFR breach → 4/10 Path A confirmation). Each entry: prior view → revised view + trigger + durable anchor (KB entry / file).
- Late-session reflection: KB-LIQ-057 headline could be misread as "demand-hole is fine." Sharpened with "⚠️ READ BEFORE CITING" preamble + two-poles framing (mechanism-failure DORMANT, term-premium ratchet ACTIVE). A successful 5.122% auction is now explicitly framed as evidence of transmission via term premium (price had to rise ~+50bps from late-2024 absorption to clear).
- Added explicit "5/21 10Y is the reassessment trigger" callout to Thesis-Kill Proximity in STATUS — names the gate that should resolve the APO co-trigger reassessment that's been carrying ~10 days.

**Commits pushed:**
- `71d6a9f3` LIQUID: file-tree audit + 20Y auction integration + STATUS prune (5/20) — initially got bundled into BRENT commit f246d36f due to concurrent agent staging; BRENT session corrected before push; my commit landed clean afterward.
- `06f28e2d` LIQUID: STATUS 3-dashboard restructure + KB-LIQ-057 sharpened — rebased onto SENTRY feed update ab86b6c8 and pushed clean.

**Major findings this session:**

- **POV-pivots-in-CHANGELOG is a transferable pattern** — bridges KB.tsv (point-in-time facts) and formal version revisions (CHANGELOG's original role). Captures the "I changed my mind about X because Y" trajectory that neither alone preserves. Will explicitly noted transferability to CARL/BROCK. Saved as auto-memory `finding_pov_changelog_pattern.md`.
- **Concurrent agent commits can bundle work into wrong-titled commits.** When two Claude Code sessions stage files simultaneously, one session's commit can sweep up the other's staged files under its own message. Reinforces existing memory `feedback_agent_git_isolation.md` and `feedback_check_staged_before_commit.md`. The fix this time was BRENT noticing + amending; the pattern to remember is: **on concurrent activity, watch the commit's file list, not just the staged diff.**
- **KB entries with strong directional language need guard-rails.** KB-LIQ-057 needed a "READ BEFORE CITING" preamble because the headline framing could be misread. Pattern: when a KB entry refines transmission *mode* (not *whether*), explicitly state both — what's now-active and what was-disproved — to prevent the entry being cited for the wrong conclusion in a future session.

**Open follow-ups (carried into NEXT SESSION):**

- **5/21 10Y reopening (today, 1pm ET) is the reassessment trigger.** Leg 2 of BOND's two-leg watch. Corroboration test for KB-LIQ-057 (term-premium-digestion vs mechanism-failure poles). The input that should finally resolve the APO co-trigger reassessment that's been carrying for ~10 days.
- **APO co-trigger reassessment STILL pending.** Day 10 by 5/21 close if APO holds >$130. Reassessment overdue per HEARTBEAT line 80; STATUS now explicitly tells next session to resolve on 5/21 print or carry-forward with stated reason.
- **HYG $75P Jun x10** — June expiry, theta-killer with HY OAS 286 (vs 320 trigger; cushion to kill widening, not narrowing). Cut/hold decision gated on (1) 5/21 10Y print and (2) APO reassessment.
- **Cross-agent outboxes**: BROCK on APO Day 10+ if reassessment fires; HENRY on duration acute if 10Y reopening prints weak.
- BDC Q1 continuation (OBDC/ARCC/BXSL/MAIN) if any prints land.

### PRIOR SESSION (2026-05-19 PM #2 — workbook triage)

**Context:** Cleared context after earlier afternoon session. Will queued workbook cleanup (NEXT SESSION item #3 from prior block).

**Delivered (2 passes):**

**Pass 1 — episode + framework triage:**
- 5 frameworks → `domain/sources/frameworks_20260311/` + README (STAGFLATION_TRAP_MAR11, VIX_COILED_SPRING_MAR11, DIFC_TRANSMISSION_MAR11, HAMILTON_NOPI_MAR18, RAS_LAFFAN_LNG_MAR18). These were episode-attached but contain reusable methodology.
- 3 episode narratives → `archive/workbook_resolved_mar2026/` + README (GULF_ESCALATION_MAR18, BRENT_SCENARIOS_MAR18, KUWAIT_CURTAILMENT_MAR18). Resolved Mar 18-20 phase-change narrative.
- 1 auction playbook → `archive/workbook_resolved_jan2026/PLAYBOOK_7Y_AUCTION_20260129.md` + README flagging template-reuse value.
- 1 misfiled status snapshot → `archive/STATUS_archive_20260325.md`.
- **2 new KB entries** for durable frameworks: **KB-LIQ-053** Stagflation_Trap_Structural (Mar 10 oil-11%/30Y+4bps confirmation + 60/40 breakdown + trap-broken test), **KB-LIQ-054** Financial_Hub_Transmission (4-path framework: FOI / Bank CDS / War-Risk Insurance / CLO Arranger). Both pointer-link back to the source files now in `domain/sources/frameworks_20260311/`.
- 5 in-workbook cross-refs updated in KB.tsv/ML.tsv/VX.tsv to new paths. Archive snapshots left untouched as historical state.

**Pass 2 — domain frameworks + tsv files:**
- `TREASURY_BUYBACK_PATTERN.md` → `domain/sources/frameworks_20260311/` (added to README). Mar-episode-attached but durable insight: Treasury has advance TIC visibility, pre-positions buybacks ahead of release.
- `ML.tsv` → `domain/sources/ML_historical.tsv` (renamed). KB.tsv is the durable track per operating notes; ML.tsv was effectively superseded. Preserved as historical learning log.
- `VX_HISTORY.tsv` → `archive/VX_HISTORY_through_20260317.tsv`. Untouched since Mar 17.
- `CUSTODIAL_VELOCITY_PROTOCOL.md`: kept in workbook/, but 4 internal `ML.tsv` refs updated → `KB.tsv` to match durable-track convention.
- KEPT in workbook/: AUCTION_FRAMEWORK.md (20Y auction this week), TIC_FRAMEWORK.md (monthly recurring), FLOW.tsv + VX.tsv (registries — load-bearing for KB/ML cross-refs), PREDICTIONS.tsv (small active log), KB.tsv, KILL_MEMO_HY_OAS_260.md, BDC_MARK_CONVERGENCE_MONITOR.md.

**Final workbook/ state:** 9 active files (down from 22). All actively used or referenced.

**Top-level LIQUID surface:** 9 files + 6 directories (was 8 files — added `CLOSEOUT.md`).

**Pass 3 — closeout codification (post-push):**
- `CLOSEOUT.md` created — mirrors PROME's 4-tier model (Bounce / Light / Standard / Heavy) for cross-agent vocabulary consistency, but rebuilt for LIQUID's surface (STATUS-primary, 3-dashboard structure, KB.tsv durable track, outbox/SIGNALS.md cross-agent rails). Includes pre-closeout inventory, 5 chunked steps (state / workbook / cross-agent / auto-memory / git), skip rules, file-ownership reference table.
- `CLAUDE.md` SPAWN PROTOCOL gets step 5 pointer to CLOSEOUT.md; FILES table adds CLOSEOUT.md row.
- This session is the first dogfooded Standard closeout under the new doc.

**Open follow-ups (not addressed this session):**
- `CUSTODIAL_VELOCITY_PROTOCOL.md` (270 lines, Feb 11) prescribes weekly SIFMA velocity pulls that aren't happening. Belgium watch IS live in STATUS thresholds; collateral-velocity piece is unimplemented. Either revive cadence or slim the doc — flagged for separate session.
- No active "observation" log distinct from KB.tsv durable-findings. If desired in future, that's an architectural choice.

### PRIOR SESSION (2026-05-19 PM #1 — afternoon hygiene + thesis v2 sweep)

**Context:** Multi-pass session. Will directed: "get LIQUID working properly as an agent — much is still stale." Sequenced staleness inventory → THESIS rewrite → architectural hygiene.

**Delivered:**

1. **Boot + live re-verify** — tape pulled mid-session (13:23 UTC). Yields extending: **30Y 5.168% fresh life-of-cycle high** (vs 5.046 May 5; first since 2007), 10Y 4.647 (+24bps day), 5Y 4.301 (+21bps day). Whole curve at 1mo highs, roughly parallel bear. Added intra-day flag to STATUS.md "May 19 Live Re-Verification" section.

2. **THESIS v2.0 written** (`thesis/THESIS.md`, 162 lines, full rewrite from v1.0 Apr 8). Approved framing (ii): **narrower active scope** with explicit transmission interfaces. 9 sections covering core frame, what LIQUID actively owns vs receives, three structural failure legs (A Fed rate-control / B FOI demand hole / C basis-trade leverage), transmission channel map, bilateral 320/260 credit framework, stagflation trap, kill conditions, cross-agent interfaces (BOND placeholder), epistemic notes.

3. **CHANGELOG v2.0 entry** (`thesis/CHANGELOG.md`) — documents what changed (narrower scope, channel migration framing, bilateral credit, gamma-suppression caveat, BOND interface, channel-kill vs full-thesis-kill distinction), what stayed (core frame, three legs, stagflation trap, LIQ-01), and drivers (32-day gap, 30Y >5%, missed APO co-trigger, BOND scaffold, Stage 3 recognition).

4. **TIMELINE.md slimmed** to forward-only Active Branch Points (13 decision windows May 19 → Jun 18). Dropped Resolved Events half (lives in STATUS Durable Signals Log). Each window has bull/bear resolution + which channel(s) affected.

5. **IDENTITY.md reconciled** with v2 — fixed "BOTH buffers" → "all three", reframed duration as BOND-domain transmission (not LIQUID-owned), refreshed numbers to 5/19 live, added APO co-trigger and Leg A dormant items, added pointer to THESIS v2.0.

6. **Architectural hygiene — major directory cleanup:**
   - **`red/`** (4 files Apr 8) → `archive/red_legacy_20260408/` + README. Reason: RED is now top-level peer agent at `AGENTS/RED/`.
   - **`research/`** Category A foundational deep research (8 files + RESEARCH_RESULTS/, Jan 25, ~3,500 lines including $1.85T basis-trade research, $300B/yr demand hole, China/Belgium stealth exit) → `domain/sources/research_foundations_20260125/` + README. These are the empirical bedrock under v2's three legs.
   - **`research/`** Category B tactical resolved (`KRE_HYG_ROLL_ANALYSIS.md`, `QUARTER_END_PLAYBOOK_MAR31.md`) → `archive/research_tactical_resolved/` + README. Both resolved; methodology preserved as template.
   - **`recon/`** + `RECON_REPORT.md` + `RECON_DRY_RUN.md` (War Day 14 Mar 15 artifacts) → `archive/recon_legacy_20260315/` + README. All findings already in KB.tsv (KB-LIQ-006 through 011).
   - **`DECK_EVIDENCE.md`** (Mar 13 investor-pitch evidence) → trashed via gio. Fully superseded by v2 + KB.tsv.
   - **`research/` directory removed** (empty after moves).

7. **BOND interface acknowledged.** Will confirmed BOND is scaffolded but not built out. v2 names the interface (duration / yield curve / term-premium / dealer positioning will migrate to BOND-primary when stood up) but LIQUID retains all current scope; no actual handoff this session. **Read BOND/CLAUDE.md** — formal scope claims overlap LIQUID significantly (HY OAS, IG OAS, CDX, auctions, yield curve). Defer reconciliation until BOND is active.

**Major findings this session:**

- **Duration channel intensified intra-session.** 30Y 5.168 fresh life-high TODAY confirms the channel-migration thesis in v2 in real time.
- **THESIS v1.0 had drift risk.** Old doc framed HY OAS 320 as "orange systemic stress" — but current STATUS treats 320 as confirmation and 260 as kill. A future session reading v1.0 would have acted on wrong levels. Now reconciled in v2.
- **`research/` had ~3,500 lines of orphaned foundational work.** Not referenced anywhere on the active surface but contains the empirical basis for v2's $1.85T basis-trade, $300B/yr FOI demand hole, and auction thresholds. Preserved into `domain/sources/` rather than lost.

**Top-level LIQUID surface now (post-cleanup):**
```
CALENDAR.md  CLAUDE.md  CREDIT_THRESHOLDS.md  IDENTITY.md
MEMORY.md    STATUS.md  STRATEGY.md           USER.md
+ archive/  domain/  inbox/  outbox/  thesis/  workbook/
```
8 active files + 6 directories, all referenced in CLAUDE.md. Down from 13 top-level files + 7 directories before sweep.

**Still open / carrying forward:**

- **POSITIONS read still gating.** APO co-trigger has now been live ~8 sessions (5/12 → 5/19). HYG $75P Jun x10 cut/hold decision still deferred. Will explicitly directed not to cut anything this session — focus was agent hygiene.
- **Cross-agent outboxes NOT written.** Still pending if escalation warranted: BROCK (APO Day 7+), HENRY (10Y / 30Y duration acute).
- **`workbook/` cleanup not started.** Mar/Apr resolved-episode files + domain frameworks + Tier 2 tsv files (FLOW/PREDICTIONS/VX/ML/VX_HISTORY) still need triage. Deferred to next session.

### NEXT SESSION

*(Updated 6/13. HY OAS tracking retired this session — KB-LIQ-060. Forward watches, not cleanup.)*

1. **First boot move — verify Mon 6/16 closes** (per basis canon): Brent — does the sub-$90 hold / extend (ICE settle; clause-1 clock running since 6/12 $87.33)? APO streak (raw close, Day 4 was 6/12). 30Y/10Y vs the 5.00/4.50 pivots into FOMC. CCC OAS + BDC marks (the credit-leg read now — NOT HY OAS).
2. **HYG $75P — single position left, expires Fri 6/19 (T-4 from 6/13).** Recommend expire/close (dead). Will decision; surface every boot until resolved. *(TEN closed 6/12-13.)*
3. **FOMC Wed 6/17** — the duration-regime + conviction-60 resolver (dot plot vs hot May CPI; Warsh color; liquidity-facility language = Leg A kill watch). → **TIC Thu 6/18** (Japan net / Belgium $481B vs $500B orange — KB-LIQ-055; gates the USD/JPY>160 flow confirmation, now 5 closes).
4. **Thesis-doc HY OAS sweep (Will-steered):** THESIS.md §"bilateral 320/260 credit framework" + TIMELINE.md still describe the retired frame — decide cosmetic-note vs full re-derivation before next thesis restamp.
5. **Open verifies:** FSK P/NAV 0.52 (split/vintage); OBDC Q1 NAV (search avoided Onex conflation); FRED H.15 6/12 yield prints confirm the proxy.
6. **LIQ-03 resolves 6/30** at the letter (CLO AAA vs 160 trigger; interim ~S+130-145).
7. **Inbox (2 pending, process on inbox-spawn)** — HAWK OFAC toll-risk 5/22; PROME FRED-citation-convention 5/21.

### PRIOR SESSION (2026-05-19 morning)

**Context:** Live tape re-verification of Prome's 5/18 pass-through. Pulled dashboard via `FORGE/tools/market-data/dashboard.py` and APO 10-day history via yfinance.

**Delivered:**
1. STATUS.md live re-verification — added "May 19 Live Re-Verification" section with full dashboard table; restamped 5/19. Header status flipped to 🟠.
2. **APO co-trigger discovered as MISSED.** APO closed >$130 starting 5/8 ($133.20), sustained through 5/18 ($134.07, peak $135.52 on 5/14). HEARTBEAT line 80 reassessment trigger fired on 5/12 (Day 3) and has been live for ~6 sessions of LIQUID inattention. Coincides with HY OAS compression run (282 → 276 cycle-tight). Per KILL_MEMO co-trigger language, this is the Trigger C precondition (APO + HY OAS compression concurrent).
3. Updated thresholds table with APO co-trigger row + USD/JPY row; updated cross-domain signals; trimmed stale Apr-16 Danger Windows/Watch into single forward-looking 5/19 table.
4. 10Y observation refined: not just chronic +30bps, but acute +12bps on 5/18 alone.

### PRIOR SESSION (2026-05-18 PM) — Revival
- 32-day revival. Integrated Prome's revival-proxy packet.
- STATUS.md surgical update (4 edits + new "Thesis-Kill Proximity" + "May 18 Revival Read"). Active channel reframed PLUMBING → DURATION.
- KB-LIQ-051 (SOFR April resolved mechanical), KB-LIQ-052 (Duration regime break May 2026).
- `workbook/KILL_MEMO_HY_OAS_260.md` drafted — 5-tier trigger ladder.
- PLAYBOOK_SOFR_IORB_20260417.md archived to domain/sources/.
- Inbox swept: 21 → 0 (5 synthesized, 14 archived, 2 Prome packets retained as reference).
- Boot doc refresh — CLAUDE.md (broken "removed:" text, KEY THRESHOLDS, FILES), CALENDAR.md (rolled forward), STRATEGY.md, IDENTITY.md, USER.md, CREDIT_THRESHOLDS.md.

### PRIOR-PRIOR (Apr 16 PM)
- Computer crash interrupted; resumed to close out.
- Apr 16 STATUS refresh (SOFR>IORB Apr 15 first cycle breach, credit Path A holding, APO/BIZD reversal, HYG thesis weakened).
- Processed 6-signal inbox (IMF GFSR, TCW Red Lobster, GS whipsaw, SEC PDT, CPI/UMich, March PPI).
- Built PLAYBOOK_SOFR_IORB (now archived) and BDC_MARK_CONVERGENCE_MONITOR scaffold.

### OLDER CONTEXT (see git history + `archive/`)
- Apr 10: Live data refresh — Path A (squeeze resolution) winning. LIQ-01 at 290bps, 30bps below 320 trigger.
- Apr 8: Full data refresh + file structure upgrade (SAM parity). Stagflation trap double confirmed. Japan repatriation upgraded LATENT→ARMED.
- Apr 6: Processed 11-signal inbox batch (PC Stage 3 + plumbing fragility).

## Operating Notes

- **FORGE/tools/market-data/** (dashboard.py, fetch.py) works well for FRED + yfinance series. Use for live pulls.
- **Git protocol:** `reset HEAD → add AGENTS/LIQUID/ → diff --cached --stat → commit → push`. Other agents frequently have uncommitted work in HENRY/REGINALD directories — never stage those.
- **STATUS.md is the single source of truth** for active positions, proposals, thresholds. TRADE.md was retired — no second copy to keep in sync.
- **Inbox processing is its own task.** Don't auto-process on spawn; wait to be told.

## Durable Findings

- Stagflation trap is structural and persistent — double confirmed across two separate oil crashes.
- Q-end SOFR spikes (Mar 31, Apr 2-3) were seasonal, not structural.
- **Apr 15 SOFR-IORB +7bps breach resolved mechanical, not structural** (tax-day TGA build, normalized within 2-3 sessions; KB-LIQ-051). Pattern: 1-day SOFR-IORB sign flip on tax-day mechanics is NOT structural confirmation. Apply the same skepticism to future quarter-end / settlement-window single-print breaches.
- **Active transmission channel can migrate without thesis abandonment.** Bear thesis stayed intact through 32-day gap by migrating from PLUMBING (SOFR-IORB) into DURATION (10Y +30bps, TLT confirms, Brent reflation). When one channel resolves, scan the others before declaring the thesis dead (KB-LIQ-052).
- **Gamma/momentum suppression hypothesis** (per Will/Prome 5/14 signal): positive gamma may suppress VIX/HY OAS even as substance prints (FSK NAV -9.9%, 2nd bank failure, Brent $109) accumulate. The HY OAS 276-282 floor that held May 6 → May 17 may be tape, not substance. Watch for the moment gamma unwinds — HY OAS could gap.
- **Trigger watch can go dormant during agent staleness.** APO crossed >$130 on 5/8 and the HEARTBEAT-grade co-trigger fired on 5/12 (Day 3). LIQUID was stale Apr 16 → May 18 (32 days). The trigger was live for ~6 sessions before live-tape re-verify caught it on 5/19. Pattern: on revival, **don't trust the proxy's narrative summary alone — pull live values for every named threshold in HEARTBEAT line 80 and verify day-counts.** A proxy synthesizing 5 inbox items can cite "APO >$130" as macro context without computing the trigger ladder. The agent's own first-session work after revival should include a full trigger sweep, not just STATUS surgical edits.
- DIFC geopolitical flows de-escalating while domestic structural flows (Japan, TGA) upgrading.
- **Public-equity PC sentiment (APO/BIZD) can decouple from underlying mark divergence** — TCW Red Lobster 98% / par is the canonical example. FSK Q1 NAV -9.9% (5/18) confirms mark catch-down direction. Don't over-weight equity price action for Stage 3 timing.
