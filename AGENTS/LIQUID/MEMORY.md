# LIQUID — Cross-Session Memory

## Session Notes

### CURRENT SESSION (2026-05-19 PM #2 — workbook triage)

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

**Top-level LIQUID surface unchanged** (8 files + 6 directories — same as after PM #1 sweep).

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

1. **Boot from clean workbook + top-level surface.** v2 thesis, refreshed IDENTITY, slimmed TIMELINE, CHANGELOG. STATUS has 5/19 morning re-verify + intra-day flag. Workbook now 9 active files.
2. **Re-verify tape.** APO 5/19 close (Day 8 watch), HY OAS print, 30Y/10Y direction (did 5.168 hold or extend? did 4.647 hold or extend?).
3. **POSITIONS read still gating.** APO co-trigger now ~Day 8+. HYG $75P Jun x10 cut/hold decision still deferred. Resolve when Will is ready.
4. **Cross-agent outboxes if warranted** — BROCK on APO Day 8+, HENRY on 30Y/10Y duration acute.
5. **BDC Q1 baseline** into `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` (OBDC/ARCC/BXSL/MAIN).
6. This week's calendar: 20Y auction Wed (VERIFY), initial claims Thu.
7. **CUSTODIAL_VELOCITY_PROTOCOL.md decision** — slim it or revive the SIFMA velocity cadence. Belgium watch piece is live; velocity piece is unimplemented.

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
