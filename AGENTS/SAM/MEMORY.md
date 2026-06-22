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

### CHANGES SINCE LAST SESSION (Sat Jun 20 ~10:30 AM ET closeout → Sun Jun 21 ~5:23 PM ET boot)

- **Levels flat over the weekend** (Sun FX reopen ~unchanged): USDJPY 161.23 (MOF silent ~5 sessions at 160+; **161.96 = weakest-since-1986 record**, ~16 pips above Fri's 161.80 intraday — the precise level Tokyo trades Monday, not a loose "162"), FXY $56.85, Brent $80.59, FXY ATM IV 12.51%. No new authoritative data (CFTC/JGB/MOF weekend-frozen).
- **Iran diplomacy bumpy, NOT collapsed:** US-Iran Switzerland (Lake Lucerne) talks convened Sun Jun-21; Iran walked out ~90min over Trump rhetoric, mediators (Qatar/Pakistan) kept shuttle diplomacy alive. **Lebanon de-escalating** (cabinet ordered Hezbollah disarmament; Israel holds fire) — undercuts Iran's stated rationale for the Sat declaratory Hormuz re-closure → reads as reversible leverage. No fresh kinetic / tanker attacks since Jun-19; Phase-1 oil-in-yen stays dormant.
- **🆕 Ueda discharged Fri Jun-19, returns to work Tue Jun-23** (~5wk earlier than the modeled Jul-30/31) — leadership-overhang tail removed; back before the Jun-24 SoO / Jul-31 MPM. (Logged this session.)
- **Fed-HIKE regime firmed:** Polymarket "Fed hike 2026" ~56%→~66%; UST repricing holding (no dovish walk-back); Himino Jun-19 hawkish "cost of being late" → Pillar-1 vector further adverse to near-term long-yen.
- **JGB long-end drifted up:** 30Y 3.84% / 10Y 2.65% / 40Y 3.74% Jun-19 close (Trading Economics aggregator; ~16bp from the 4.0% line — ⚠️ confirm at next MOF pub).

### LAST SESSION (Sun Jun 21 ~5:23 PM ET boot → closeout — systems-cleanup + 48h news-sweep arc; 6 SAM commits, ALL PUSHED)

**No analytical re-marks — canonical stays v1.5.1+Jun-18-strip; v1.6 pending Mon CFTC + RED. Money fields untouched (13 sh @ $58.32 / Jun-18 $58C expired / interim stop single-leg FXY ≤ $55.05).**

- **Booted + market refresh** (boot.py 10/10 clean; Sun levels flat vs Sat — reported to Will, no STATUS-table churn).
- **Peer boot-process compare/contrast** (Will-directed; 7-agent workflow BRENT/VIOLET/HENRY/CARL/HAWK/LIQUID/REGINALD). Finding: SAM leads the fleet on *internal* apparatus (10-script boot.py wired+clean, calibration scoreboard+archive, 3 stewards, evals/RECONCILIATION) but trails on the *cross-agent* plumbing — `NEXUS_BRIEF` was unrooted; the WALTER `board_log` lane is unbuilt (deferred per [[project_messaging_overhaul]], PROME-level — not a SAM cleanup).
- **Wired `NEXUS_BRIEF` into the SPAWN PROTOCOL** (Will-approved, `89da3b7a`) — new closeout **step 13a** (mandatory refresh + no-change floor) + FILES + Doc-Ownership + messaging note; MAINTENANCE logged. The brief had rotted ~2wk stale (Jun-7 body) for lack of wiring; its own footer flagged the gap verbatim.
- **Refreshed `NEXUS_BRIEF` body** to current canonical (`e02c8695`), then again at closeout (step 13a) folding the sweep findings (Jun-24 SoO + Ueda-return + Fed-66%) — settled facts only; v1.6 re-marks flagged in-progress, NOT fabricated.
- **48h news-sweep** (Will-directed; 6-vector workflow) — quiet, net thesis-CONFIRMING weekend; 2 genuinely-new dated facts (Ueda return, Jun-24 SoO), rest extends-known and leans weak-yen/no-unwind. Full read shipped to Will.
- **Logged the 2 sweep findings** (`f4adf1b3`) — Ueda-return corrected (source-verified via BOJ/Reuters; **did NOT touch the legit Jul-30/31 next-MPM rows** — the stale fact had borrowed that date); Jun-24 BOJ Summary of Opinions added to docket (CALENDAR + CATALYSTS, parses clean at 3d). Breadcrumb 7a holds the v1.6 inputs.
- **Committed + PUSHED all** (incl. `7a0351cb` boot-TSV refresh; fast-forward, in sync with origin — push-train confirmed: WALTER's 6/21 PM push swept the first 3 SAM commits to origin).

### NEXT SESSION

**Imminent — Mon Jun 22 is the convergence point (CFTC EV-gate + Brent decoupling test, SAME DAY); then Wed Jun-24 BOJ Summary of Opinions:**

1. **✅ Fri Jun 19 National May CPI — VERIFIED (Sat Jun 20 boot; `cpi_japan.py` down/ESTAT_APPID unset, pulled manually + cross-checked Reuters/CNBC/Japan Times):** headline **1.5%** (↑ from 1.4% Apr — energy base-effect from utility-subsidy *expiry*, NOT demand), core ex-fresh-food **1.4%** (held flat; 4th straight month <2% target, 4-yr low; matched fcst), core-core **1.8%** (−10bp vs Apr 1.9% / fcst 1.9% — slight dovish miss). **Net: soft/dovish underlying → thins the post-1.00% BOJ Oct-hike repricing (multi-month tail thinner); thesis-coherent (BOJ hiked on wage/activity mechanism, CPI stays soft).** Feed these verified figures into v1.6 DRAFT open question #8. ⚠️ Do NOT use the `stockpil.com` aggregator figures (core 2.1%) — wrong; see Findings 6/20.
2. **🔴 Mon Jun 22 CFTC JPY COT (Jun 16 data — first post-catalyst print; delayed from Fri Jun 19/Sat by Juneteenth holiday) — v1.6 EV-table DECISION-GRADE.** Pre-registered: cover <-120K (~67% peak) → v1.6 frame FAILS margin test → **trim/close discussion**; holds -140K to -150K (78-83%) → frame survives margin → vehicle question stays open; builds through -153K/85% → amplifier escalates +5pp → +8-10pp → frame STRENGTHENED (gross EV ~+3.0%, net ~+1.3%). This is THE observable. **🔴 SAME DAY — also run the Brent decoupling test:** Iran re-declared Hormuz CLOSED Sat Jun 20 (Lebanon-breach; declaratory-not-physical; cross-agent BRENT THESIS v4.1 / HAWK B34/C44/D22). Mon Jun 22 Brent reopen → spike = de-escalation thesis breaks (oil-in-yen re-activates; v1.6 "Oil/MOU re-escalation" tail-route fattens); shrug = holds. Pair the read with the CFTC gate. See CALENDAR GEOPOLITICAL WATCH (logged 6/20).
3. **RED challenge pass on v1.6 backbone DRAFT** (`THESIS_v1.6_DRAFT.md`). 6 numbered RED challenges embedded inline + EV-table #1a-d sub-challenges. Spawn RED with the draft + challenges; resolve before finalize. Pre-registered gate: vehicle modeling proceeds ONLY IF RED #1-#3 survive.

**v1.6 finalize (after CPI + RED + Mon Jun 22 CFTC):**

4. **v1.6 finalize commit** — rename `THESIS_v1.6_DRAFT.md` → `THESIS.md`; archive v1.5.1 to `thesis/THESIS_v1.5.1_ARCHIVE.md`; update STATUS/CHANGELOG/STRATEGY/TRADE/PREDICTIONS per pre-listed surface list in DRAFT § SAM-LOCAL CHANGES.
5. **5 sizing decisions queued for Will (post-RED, post-CFTC):** (a) retain/trim 13 shares; (b) FXY-vol overlay yes/no [after expiry roll proxy sanity-check]; (c) USDJPY-put / JPY-call structure vehicle change yes/no [GATED on RED #1-#3 surviving]; (d) tighten stop from interim $55.05 → e.g. USDJPY ≥162.5 / FXY ~$55.50; (e) define eligibility window (90d / Jul 31 BOJ / end-CY26).
6. **Update SIGs to LIQUID + HENRY** when v1.6 commits (buckets re-recompute; vehicle disposition; Channel 1 deferred-vs-retired decision). **`NEXUS_BRIEF.md`:** wiring landed 6/21 (closeout step 13a, per MAINTENANCE) AND **body fact-refreshed 6/21 to current canonical** (post-BOJ/FOMC/Iran; predictions resolved; stale-banner removed; commit `e02c8695`). Only the **v1.6 analytical re-marks** (carry buckets, conviction re-decomposition, vehicle disposition) still ride this v1.6 SIG-broadcast pass — flagged in-brief as in-progress, not fabricated.
7. **CHANGELOG entry** for v1.6: full backbone (re-center compression → carry-convexity-tail; Pillar 1 split level-vs-vector; Pillar 4 promoted to center).
7a. **Sun Jun-21 48h news-sweep inputs (logged this session; marks unchanged/frozen):** (a) **Ueda discharged Jun-19 / back at work Jun-23** (source-verified) + **Jun-24 BOJ Summary of Opinions** → propagated to STATUS + docket (CALENDAR/CATALYSTS) this session. (b) **v1.6 inputs to fold:** JGB 30Y **3.84%** Jun-19 close (Trading Economics — ⚠️ confirm at next MOF pub; ~16bp from 4.0%); Fed-hike-2026 firmed **~56%→~66%** + Himino Jun-19 "cost of being late" → Pillar-1 vector. (c) **Mon live reads:** Brent decoupling test on the Sat declaratory Hormuz re-closure (Lebanon de-escalating Jun-21 undercuts its rationale) + the CFTC EV-gate. Net: quiet, thesis-confirming weekend; nothing forced a mark.

**Carry-forward (post Phase A/B/C cleanup — minor items deferred to v1.6 finalize sweep):**

8. METSUKE MINOR drifts (4 items): TRADE L246 Iran row stale-only ("substantively walking back / unsigned" — superseded by SIGNED); STRATEGY L122 Position A Jun-9 parenthetical; STRATEGY L183-187 Key Check Dates partial cleanup (multiple resolved forward-only refs); TRADE L42 hard-trigger subheader timestamp.
9. ✅ KURA archive-move DONE (Run 7, 2026-06-22): archived **KB-SAM-006** (the one genuinely-SUPERSEDED row; KB.tsv 142→141). ⚠️ The prior "6 rows ready (KB-064/081/084/087/092/137)" claim was STALE — those 6 were ALREADY in KB_ARCHIVE from a prior run (KURA flagged the discrepancy rather than forcing it). No archive backlog remains.
10. KURA FLOW/VX full re-derivation per v1.6 finalize (FLOW-JPN-5.02 / 6.02 too much moved for surgical fix; VX-SAM-11.02 trade balance refresh).
11. **Channel 1 disposition (Will-directed re-examination):** decide DEFERRED → RETIRED pending new mechanism (4-of-4 disconfirmations: Big 3 mutuals + Norinchukin). RED #6 challenges the honesty of "deferred pending" with no specified reactivation path.
12. **SAM-23 framework re-anchoring CHANGELOG entry** (post v1.6 scoring; CH-011 driver/disorder + no-strike decay).
13. **Research backlog (Tier 2/3 un-pulled per Will Jun 15 brainstorm):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.
14. **Position next-touch (post Step 1.5 stop):** interim FXY ≤ $55.05 single-leg. v1.6 finalize sizing decisions (#5 above) are the next position decision point. No add/trim before v1.6 + CPI + Mon-Jun-22 + RED converge.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive; NEXUS_BRIEF rollout = Will-action.

**Closeout (Sun Jun 21):** 6 SAM commits, **ALL PUSHED** to origin (in sync, tree clean): `89da3b7a` NEXUS_BRIEF wire · `e02c8695` brief refresh · `78f3128d` MEMORY breadcrumb · `f4adf1b3` sweep logging (Ueda + Jun-24 SoO) · `7a0351cb` boot-TSV data · + this closeout (NEXUS_BRIEF step-13a refresh + MEMORY session-notes + STATUS stamp). No METSUKE/KURA/KOYOMI spawn — no marks/thesis moved; the docket edit was a clean 1-row source-verified add. **Un-promoted auto-memory candidate still pending:** source-discipline finding (Findings 6/20) — left local pending Will endorsement per the prior promotion pattern.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
