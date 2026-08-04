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

### CHANGES SINCE LAST SESSION (Mon 8/3 close → Tue 8/4 10:33 ET boot)

- **Brent $79.98, THROUGH $80** (−4.5% d/d; $82.88 on 8/3, $90.12 on 7/31, $100.43 on 7/23). Trump paused Iran strikes **and** announced Hormuz-reopening talks; Iran denies direct talks but confirms the Oman shipping track. Phase-1 oil-in-yen pressure decisively unwinding.
- **USD/JPY 157.49 — flat vs Friday's 157.40, i.e. the post-op range is HOLDING into session 3.** Mon 8/3 traded a **155.215 low, closest to the 155 Phase-2 line since May-6.**
- **Bessent doubled down 8/4:** yen level "problematic," Treasury "would not hesitate" to intervene again, **and purchases "would need to be followed by Japanese policies addressing the forces driving the yen lower"** — the US Treasury publicly pressuring Japan on **rates**.
- **JGB long end drifted up** (MOF 8/3 pub): 10Y 2.824 (from 2.801), 30Y 3.982, 40Y 3.948.

### LAST SESSION (Tue 8/4, 10:33 ET boot — full sweep)

- **🔴 JGB 10Y auction printed the SOFTEST of the tracked series** — BTC **2.558×**, tail **6.0bp** (own MOF `eresul20260804`); **4th straight month of decay in both legs** (BTC 3.904→3.530→3.130→2.558; tail 0.4→0.7→2.6→6.0). Wires: lowest BTC since May-2025, widest tail in 2 years; drivers = consumption-tax funding uncertainty + BOJ early-hike risk. **Held the discipline line: this is the BELLY, not the super-long** — the demand-vacuum thesis and the Meiji ~4.0% floor are 30/40Y objects and did not soften here. Flagged, not re-marked; it upgrades the **8/6 30Y** from formality to live test.
- **🔧 SAM-39's registered base rate was computed on TRUNCATED data — corrected, mark unchanged.** Yesterday's L3 alarm flagged 4 pre-fix sessions *outside* the 10d self-heal window. After backfill: prior-year **3/259 ≈1.16%/sess → naive P ≈32%** (was 2/250 ≈0.8% → ~23%); pre-episode max 1.90y → **1.98y**; **0/60 leg unchanged**. **SAM-39 stays 55%; only the rationale is corrected** — the edge is ~+23pp, not the ~+32pp I wrote. *The lesson: I fixed the instrument on 8/2-8/3 and did NOT propagate the fix into the numbers that instrument had already produced.* Recorded against my own interest: 8/3 printed **2.67y** — a third consecutive qualifying session immediately *before* the window opens. **Explicitly NOT credited** (window starts 8/4), but it means the naive annual base rate is arguably the wrong reference class and 55% may be too LOW.
- **🆕 SAM-40 REGISTERED before the 8/7 print** (the owed item): the resolver was a *disposition*; it is now a scored calibration datum. **45% CONFIRM-band — deliberately below even odds against my own long-biased frame**, because SAM-22 (@65%, FAILED) is the direct precedent for intervention forcing mass cover. Terms verbatim from memo §5B, **not re-tuned while writing the row.**
- **🔧 `usdjpy.py` gained a `--revise-window N` hatch.** L3 audited 60d but L2 only rewrote 10d, so pre-fix rows were re-reported forever and could never self-heal. One-off `--revise-window 90`: 59 sessions repaired, **all** under-stating, 1366 rows in/out, 2nd run revises 0, alarm clears. Both negative branches tested. Widening rewrites history → **flag, not default.**
- **BOJ ladder extended: no third op Monday.** `jp20260805.xlsx` 財政等要因 **−¥3.35T** = ordinary for an early-month day (peer median −2.54T, worst −6.21T) vs the −11.42T Aug-4 anomaly. ⚠️ Sovereign-blind instrument. `jd20260804.xlsx` (the ACTUAL) **404s — not yet published**; owed. Moved the whole closed pre-registration to **`thesis/INTERVENTION_2026-07-30_CONFIRMATION.md`**.
- **Buckets UNCHANGED ~8/23/32 — and I wrote down WHY**, rather than leaving silence: route-5 oil/MOU **down** on de-escalation, BOJ-hawkish-of-priced **up-risk** on US rate pressure; net offsetting, neither >5pp. **Did NOT re-mark the hawkish leg — could not source current Sep/Oct OIS, and rhetoric ≠ priced policy** (SAM-08/20 failure cluster).
- **STATUS compressed 250 → 224** (the required item), playbook `jd`/`jp` series correction applied (owed since 8/3), docket trued up (CALENDAR + CATALYSTS, 2 mislabelled rows replaced with one corrected ACTUAL row), WALTER lane drained (3 signals logged + `git mv`'d), Amendment-10 brief-fold ordering rule folded into CLAUDE.md 13a.
- **FXY vol proxy is now demonstrably unreadable, not merely "degraded"** — the 25d RR *sign* flips on consecutive days at both live tenors (Aug-21 +3.42→−77.0→−32.18; Sep-18 −24.66→−5.66→+19.95). KB-183 says read the sign; there is no stable sign. Told STATUS to route TERRY to the live chain instead.

### NEXT SESSION (Wed 8/5)

1. **Re-pull `jd20260804.xlsx`** (the ACTUAL vs the −11.42T projection) — 404'd today, durable archive so it will appear. Also still hunting **Tanshi broker forecasts** on the wires (the gap IS the signal; the BOJ line alone cannot separate an op from a big fiscal day).
2. **Thu 8/6 is a triple:** 30Y auction (**live test now** — does the ~4.0% super-long bid still show up after the 10Y cleared at a 6bp tail?) · MOF weekly wk 7/26-8/1 (**3rd-week TRANSIENT confirm**; ⚠️ the cadence defect is STILL unresolved — RELEASES says Sat–Fri, STATUS/CALENDAR label Sun–Sat) · the `jd20260804` re-pull.
3. **🔴 Fri 8/7 15:30 ET — THE print.** SAM-40 now scores it. Resolver map UNCHANGED. Do not let a MED-HIGH conviction shade the fuel test.
4. **Try to source Sep/Oct BOJ OIS.** The Bessent rate-pressure mechanism is a real up-risk on the biggest in-window catalyst and is currently un-priced-unverified — an OIS print is what converts it from watch input to re-mark.
5. **The 7/30 projection leg stays PERMANENTLY UNVERIFIED** (file rotated off). Only independent read is **MOF monthly ~Aug-31**. **Do not let anyone grade the silence as a negative.**
6. **Carried:** modal-band re-derivation (gated on 8/7 by design; the 7/30-31 move pierced the 159 floor — METSUKE E2) · **KURA full-mode re-run** (~5wk harvest outstanding, now incl. the whole 8/2-8/4 cluster) · **METSUKE post-8/7** · Japan-LNG/JKM pull (FALCON handoff) · Batch-3 P3-Asia packet (gate open since 8/3, still untouched) · May TIC · `cpi_japan.py` down on unset `ESTAT_APPID` · Aug-21 National-CPI 2025-BASE re-baseline · evals re-baseline.
7. **Unprocessed top-level inbox** (deliberately not touched — normal-boot MAIL rule): 2 BRENT (TTF/Japan-LNG, EU-storage qualification), 2 PROME (GasLog, two-sovereign routing flag), 1 TERRY (TRY-FIRE-007 built), Batch-3 dispatch, and `MSG-PROME-20260803-001` whose obligations MEMORY records as INTEGRATED 8/3 — **verify its receipts are terminal and `git mv` it to `processed/`; the move looks owed.**

---

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
