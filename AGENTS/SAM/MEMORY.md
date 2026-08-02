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

### CHANGES SINCE LAST SESSION (Fri 7/31 ~1:15 PM JST → Sun 8/2 ~5 PM ET boot)

- **CFTC Jul-28 data printed −163,412 / 90.8% of peak** — the −153K/85% re-fire line crossed by 10,412. Adjudicated Sat by a PROME-directed **proxy run** (phone session), which executed the registered consequence: MED-HIGH, amplifier +8-10pp, buckets ~8/23/32, THESIS v1.6.11. **Will dispositioned it Saturday: WAIT-FOR-8/7 + TERRY re-mark Mon 8/3** (PROME `6c1d17bed`, `c192b02d3`).
- **USD/JPY collapsed ~6 yen off the 40-yr low** — 163.49 [7/30 pre-op] → **157.40** Fri close. The 7/30 suspected ~¥8.45T op is now Reuters **source-confirmed as an occurrence** (NY session), Bloomberg-estimated off the BOJ's own Friday projection gap. Not MOF-official; hard confirm ~8/31.
- **JGB long end backed up** — MOF 7/30 pub: 10Y 2.801 (from 2.731), 30Y 3.971, 40Y 3.967, back near the 4.0% Meiji floor. **8/6 30Y auction** is the first super-long under the reaffirmed FY2027 path.
- **Brent round-tripped to $90.12**, and over the weekend Trump **ordered then cancelled** strikes on Iranian **energy sites**; the daily exchange has **PAUSED** (3rd of the cycle — the 7/24 pause broke in 4 days). A Qatari LNG carrier was struck **in Hormuz 8/1**. De-escalation, if real, is yen-POSITIVE via the oil channel — not the Phase-2 haven bid.

### LAST SESSION (Sun 8/2 ~5-6 PM ET — real boot, Will-directed; then STATUS write-backs + the owed compression, both Will-directed)

- **Verified and OWNED the proxy re-mark rather than inheriting it.** Own primary `deafut.txt` pull reproduces −163,412 / OI 432,366 / WoW −6,319L +4,968S **to the contract**. v1.6.11 stands; **no version bump** — verification is not an analytical change.
- **🔴 FOUND AND FIXED A SILENT FALSE-NEGATIVE IN SAM'S OWN INTERVENTION DETECTOR** (commit `34069b8c0`). `usdjpy.py` compared London-labelled yfinance bar dates against a **local Eastern** `now()`, so any boot after ~19:00 ET appended the next day's partial bar as final — and idempotent-by-date made it permanent. **10 of the last 60 sessions truncated, all under-stating range. 7/30 stored as 0.33y against a true 5.74y.** The intraday-range alert (CRIT 4.0y) printed *"normal daily range"* on the largest yen move since Dec-2023. Post-fix: **INTERVENTION-GRADE 5.74y**, vs Apr-30's 5.15y (a *confirmed* ¥5.48T op). **Analytical consequence: this removes a single-source dependency from the 7/30 attribution stack.** Entry point was a boot report showing 157.22 in one module and 160.71 in another — *the disagreement was the only free alarm.*
- **🟠 NEW: candidate MOF op #2, Fri 7/31 16:00-17:00 ET.** USD/JPY 159.18 → 157.15 (−1.28%) with EUR/JPY −1.33% / GBP/JPY −1.32% / AUD/JPY −1.50% and **EUR/USD + GBP/USD flat** = pure yen-side, 7/30's signature, thinnest liquidity window of the week, NY session. **Held CANDIDATE, not booked** — 35-min grind not ballistic; month-end flow competing. Discriminators registered (BOJ c/a T+2 ~8/5; MOF monthly ~8/31 covers both ops). Flagged to HENRY/PROME via NEXUS_BRIEF because *"a confirmed second op"* is a pre-registered early-entry override — **it has NOT fired**, but Will's Saturday call predates the datapoint.
- **"Gains extended day+1" strengthened:** the yen made **new lows of the whole move AT the weekly close** (157.151 < 157.923), not merely held them.
- **STATUS write-backs + compression: 409 → 182 lines** (cap 250; 3 sessions overdue, cleared). Not just compression — **KEY THRESHOLDS / MARKET DATA / INTERVENTION STATUS / WHAT TO WATCH were all still on 7/23 values** (163.83, 68.1%, $100.43) behind a current banner: six weeks of spine drift. Resolved BOJ pre-registration extracted **verbatim via `sed`** → `thesis/BOJ_2026-07-31_PREREGISTRATION.md` (kept as a *path*, not git history — it carries the contamination clause).
- **External-consumer check paid off:** WALTER's `SIGNAL_PROCESSING_CHECKLIST.md` v0.30 cites the moved section as its evidence anchor for the fleet-wide pre-decision-contamination guard. Left a **redirect stub** in STATUS + sent WALTER a packet; did not touch its file. **NEXUS_BRIEF refreshed** (protocol 13a) — it still said "proxy run, real-SAM integrates at next boot" and its thesis-version line read **v1.6.9, three versions stale**.
- **Auto-memory promoted:** `[[finding_partial_record_written_as_final_never_heals]]` — idempotency is a guarantee about *writes*, not about *correctness*; audit derived series by DISPERSION; chase two instruments that disagree. Index row added, `memory_index_check --slug` exit 0.
- **Not done:** WALTER lane file `SIG-W-20260802-001` read but NOT `git mv`'d (WALTER had live uncommitted work mid-session — left alone deliberately); inbox not processed (normal-boot protocol); no KOYOMI/METSUKE/KURA spawns.

### NEXT SESSION (Mon 8/3 — batch-3 gate opens)

1. **Batch-3 P3-Asia packet: gate is OPEN** (first boot ≥ Mon 8/3). Still in inbox untouched per its own instruction — this is now the scheduled work.
2. **🔴 THE CONSOLIDATED POST-BOJ APPLY PASS (METSUKE E1, still owed and now larger):** apply all 9 Run-12 flags to TRADE/STRATEGY — the **CFTC state-label inversion is now 3 generations stale** (they read 68.1% STALL; live is 90.8% re-fire) — plus the BOJ outcome, the 7/30-31 moves, and the 8/2 re-mark in ONE pass; then METSUKE verify-pass same session. **Adjudicate METSUKE E2 while there: the 7/30-31 move pierced the 159 modal-band floor — band re-derivation is owed** (STATUS § POSITION carries the flag).
3. **~Tue 8/4-5: BOJ current-account primary checks** — `jd20260803.xlsx` (7/30 op) and `jd20260804.xlsx` (**the 7/31 candidate**), manual Tanshi-gap step per playbook S1-A.
4. **Wed 8/6: 30Y JGB auction** (first super-long under the reaffirmed FY2027 path; 30Y is 2.9bp under the Meiji floor) + **MOF weekly wk 7/26-8/1 = the 3rd-week TRANSIENT confirm.**
5. **🔴 Fri 8/7 3:30 PM ET: THE print** (Aug-4 data, first attribution-capable). **Consider formalizing the §5B resolver as SAM-39 BEFORE the print** — the terms are already registered; writing them as a scored row converts a disposition into a calibration datum.
6. **TERRY re-mark of TRY-FIRE-005** should be in flight (PROME `c192b02d3`) — tenor must span Sep-18; nudge if not.
7. **Japan-LNG/JKM pull** (FALCON handoff, upgraded 7/31; now also fed by the 8/1 GasLog Shanghai Hormuz strike): has JKM repriced on the Asia-extended Ras Laffan FM?
8. **KURA re-run (full mode)** — 7/31 crash left zero partial writes; ~5 weeks of harvest outstanding. **KOYOMI September delta** — 12 propose-only rows in KOYOMI_MEMORY ## PENDING (incl. the Sep-18 retire-check row + the Tokyo-Sep-CPI-releases-Oct-2 correction).
9. **Open infra defect (flagged, not fixed):** `usdjpy.py`'s headline level reads Yahoo's daily `Close`, which is a bar-boundary snapshot (Open≈Close on every row) — it printed 160.18 against a true 157.40. Fixing means changing the level's source (live quote or hourly); a design call, not a one-liner.
10. **Carried-open (non-urgent):** May TIC handoff check; `insurers/TRACKER.md` mid-cap bifurcation anchor; TFF decomposition · `insurer_quartr.py`; evals re-baseline; **Aug-21 National-CPI 2025-BASE re-baseline** (measurement discontinuity — re-baseline before any YoY comparison); `cpi_japan.py` still down on the unset `ESTAT_APPID`.

---

### ⚠️ PROXY RUN 2026-08-02 (Sat — PROME phone-session spawn; superseded by the real-boot block above, retained one session for provenance)

**What the proxy did:** GATE-SAM-30 re-fire ADJUDICATED VALID (Jul-28 CFTC −163,412/90.8%, own primary re-pull reproduced PROME/NEXUS exactly) → registered consequence executed: **MEDIUM → MED-HIGH (THESIS v1.6.11), amplifier +8-10pp, buckets ~8/23/32 — provisional on the 8/7 print.** Files touched: outbox memo (canonical — `2026-08-02_to-PROME_sam30-refire-adjudication.md`), STATUS (banner + 8/2 note + CARRY UNWIND re-mark + op-history row), THESIS v1.6.11, CHANGELOG 2026-08-02, playbook (7/30 row + placement-log entry), NEXUS_BRIEF, board_log (2 rows), inbox drained (4 top-level + 2 WALTER → processed/). FLAT stands; nothing executed.

### PRIOR SESSIONS — compressed 2026-08-02 (narratives → `thesis/timeline/TIMELINE.md` + STATUS pointers + git history)

- **7/31 (Fri, Will-launched LIVE BOJ DECISION WATCH — the marquee session of the cycle):** graded the MPM off the primary statement ~35 min after publication. **SAM-38 CONFIRMED at FULL-C** (hold 8-1, hawkish Takada dissent for 1.25%, overshoot-risk Outlook, FY2027 plan untouched; Oct OIS ~26-40% → ~64% on the presser) + **SAM-34 CONFIRMED** (hold @85%, 3rd straight calibrated BOJ binary). MOF monthly **¥0** → the 7/2 no-strike HARD-CONFIRMED. Buckets → 5/19/29 (v1.6.10). **Process that worked:** BOJ-site curl monitor caught publication within a minute; PDFs pdfminer-extracted; graded against frozen branches with zero re-derivation. **Contamination clause CLEAN *and it paid*** — circulating pre-dated content said "GDP 0.8%", actual FY2026 was 0.6 → fabricated-wrong, not leaked; routed to WALTER, **now generalized into its `SIGNAL_PROCESSING_CHECKLIST.md` v0.30 guard** (closes the 7/29 auto-memory candidate — WALTER owns the class, no SAM memory needed). Same session: KOYOMI clean, **METSUKE Run-12 (9 flags + 3 escalations, apply deferred BY DESIGN → still owed)**, KURA FAILED mid-run (API error, zero partial writes).
- **7/30** — 🔴 yen +2.7% intraday hours before the BOJ; suspected MOF op. VIOLET canary first-ever FIRE→WATCH (her caveat: RV cannot separate intervention from unwind); **equity vol never transmitted** (VIX −17.3% = evidence against an Aug-2024 replay).
- **7/29** — BOJ 4-branch pre-registration FROZEN (modal C ~55%); CFTC RE-BUILD to 84.5%; MOF weekly REVERSAL (2 SELL weeks overturn the 7/16 DURABLE read); **oil-yen war-attribution test FAILED** (USD/JPY flat through an ~11% Brent round-trip); VIOLET IV/RV correction (3.24× was OVX, not JPY). → `thesis/BOJ_2026-07-31_PREREGISTRATION.md`.
- **7/23 / 7/21 / 7/17 / 7/16** — SAM-35 CONFIRMED (40Y firm-lean, marginal); Brent through $100; June TB Phase-1 inversion verified via own MOF-customs pull; CFTC Jul-14 STALL (SAM-37 CONFIRMED); MOF weekly +¥1.09T DURABLE flip (since reversed) + four-anchor re-pencil 5/18/27.


**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** ~~GPIF/pension flows~~ ✅ BUILT 7/9 (`gpif_flows.py`); fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive. *(NFP AHE MoM exact print unpinned — BLS 403s bots; curl w/ User-Agent per [[finding_edgar_403_user_agent_header]] next session if needed.)*

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
