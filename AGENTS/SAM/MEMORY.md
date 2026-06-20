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
- [2026-06-20] **First-touch a wire/primary-tier source on data pulls — not an aggregator; suspect your own fresh pull before doubting curated records.** Sat Jun 20 boot websearch for May CPI hit `stockpil.com` (weak aggregator) which misreported April core 2.2% / May core 2.1% (both wrong). I carried the May 2.1% into the boot report AND initially flagged SAM's *correct* records (April core 1.4 / core-core 1.9) as the suspect "discrepancy." Cross-check vs Reuters/CNBC/Japan Times resolved it cleanly: SAM's docs match the wire exactly → **SAM-27 correctly scored TRUE, scoreboard intact; the error was mine.** **Default: verify CPI/print figures against Reuters/CNBC/Japan-Times/Stats-Bureau before reporting — especially while boot.py's `cpi_japan.py` is down (ESTAT_APPID unset) and CPI must be pulled manually. Will's "cross-check not footnote" insistence is what forced the resolution.** Auto-memory promotion candidate (verify-before-propagate family, [[feedback_verify_etf_vs_fx]]).
- *(Promoted to auto-memory Jun 10: [[finding_ohlc_verify_before_session_claims]], [[finding_pre_registration_discipline_through_corroboration]] — Advisor-endorsed, Will-forwarded; veto = delete files + index lines.)*
- *(Promoted to auto-memory Jun 18-19: [[finding_boot_sweep_macro_regime_context]] (boot regime-context check — Warsh-since-May-22 sat un-modeled 4wk), [[finding_comprehensive_grep_over_sampling]] (verifier-side discipline — PROME-named standard after Step 1.5 catch), [[finding_risk_control_separate_from_sizing]] (post-binary stop audit — Will Jun-18 distinction). All three Will-approved Phase C; cross-applicable to multiple agents — see index in `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`.)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Tue Jun 16 ~12 PM ET closeout → Thu Jun 18 ~4:13 PM ET boot)

- **🔴 FOMC Jun 17 RESOLVED HAWKISH under new Chair Warsh** (debut; sat un-modeled in SAM docs for ~4wk since 2026-05-22 — boot-sweep gap, see `[[finding_boot_sweep_macro_regime_context]]`). Held 3.50-3.75% unanimous 12-0 but **median 2026 dot +40bp (3.4 → 3.8); 9-of-18 see ≥1 hike (6 see two); core PCE 2026 +60bp to 3.3%**. Statement gutted ~300→~130 words, all forward easing bias removed. CME July hike ~75%; Polymarket "Fed hike 2026" ~52→56%.
- **🔴 Pillar 1 directional vector INVERTED across Jun 16-17 sequence:** BOJ +25bp compression < Fed-dot +40bp re-widening = rate-differential WIDER than pre-Tue, not narrower.
- **🟢 Iran/US deal SIGNED Wed Jun 17** (Pezeshkian + Trump *electronic* per Al Jazeera — NOT a Geneva ceremony); initial agreement per CNN; 60-day toll-free Hormuz reopen THEN Oman-administered fees per NBC. Verification leg OPEN (demining, insurance, HEU dilution, sanctions waivers).
- **🟢 Brent $79.68 Thu Jun 18** (~−18% cum from $96.78 Jun 3 baseline) — half deal-signing, half IEA glut warning (+8 mbpd supply by 2027 vs +2 demand).
- **🟠 Japan May TB Tue Jun 17 evening:** deficit ¥-378.7B (beat ¥-564.6B consensus by ~33%); exports +17% YoY masking structural softness; ME crude −57% YoY.
- **🔴🔴 USDJPY 161.34 Thu / FXY $56.86 / 13 shares −$19 unrealized.** MOF silent for 48h+ at 160.78 → 161.34 (Bloomberg Wed "Markets Alert for Japan Intervention"). **Jun-18 $58C expired worthless Thu Jun 18** ($40 premium written off).
- **🆕 Nikkei printed 70,000 first-ever Thu** (closed 71,053 +1.65%) — classic "BOJ behind the curve" tape (Brent collapse → risk-on JP equity, NOT yen).

### LAST SESSION (Thu Jun 18 ~4:13 PM ET → Fri Jun 19 ~6:30 PM ET — single continuous arc, 13 SAM commits)

**Frame pivot delivered:** thesis re-centered from "directional yen-compression bet (Pillar 1 + BOJ catalyst)" → "carry-trade CONVEXITY-TAIL exposure (Pillar 4 promoted to center)." v1.6 backbone DRAFT committed (`f378c0e4` + EV-table); **canonical thesis stays v1.5.1+Jun-18-strip until v1.6 finalizes post-CPI + post-RED + post-Sat-Jun-20-CFTC.**

**Commit ledger (origin @ `30ebe292` final):**
- `0f4f05f6` + `c9388bb3` + `65bc656e` — FIRST [propagation/thesis-fact] (Warsh / FOMC / Iran-signed) + workbook auto-refresh + auto-memory `finding_boot_sweep_macro_regime_context`
- `97701098` — Step 1.5 HAWK-Iran reconcile (PROME+ORC adjudicated; SAM grep-audit caught 10 overclaim spots PROME's sample missed; PROME named SAM's comprehensive-grep as the correct verifier standard going forward)
- `48dbf25c` — Step 1.5 stop re-arm: single-leg FXY ≤ $55.05 (collapsed dead BOJ-dovish AND-leg out; Will distinguished risk-control re-arm from sizing decision — see `[[finding_risk_control_separate_from_sizing]]`)
- `b3a54069` — 🔴 SIGs to LIQUID + HENRY (carry-unwind buckets re-mark Sun 8/23/32 → Thu ~5-6/17-20/24-28; Pillar 1 inversion; HAWK-aligned Iran)
- `8e86586f` — v1.6 backbone DRAFT (293 lines, 6 RED challenges embedded)
- `fb167917` — v1.6 PROME audit applied (5 fixes: USDJPY-call direction bug → USDJPY-put / JPY-call; "no cover post-catalyst" → "no cover INTO catalyst pending Sat Jun 20"; Pillar 1/3/4 split into 3 failure modes; RED #4 → explicit GATE; FXY-vol KB-183 caveat)
- `f378c0e4` — v1.6 CONVEXITY-TAIL SURVIVAL EV table (PROME-requested; closes RED #1 quant sub-clause): gross +2.21% / net 60d EV +0.0 to +0.3% — **MARGINAL positive, not strongly positive.** Sat Jun 20 CFTC = decision-grade observable.
- Sub-agent trio + KURA Run-6 (`7c52b43f` + `634f8a17` + `3835c5b6` + `6f07805e` + `7d3d2cc1` + Phase C `30ebe292`):
  - **KOYOMI Run 8:** caught CATALYSTS.tsv schema regression (7→8 fields restored, 18 rows backfilled `external`); Sat Jun 20 CFTC EV-gate row added with pre-registered dispositions; 4 resolved + 7 RECENTLY RESOLVED >7d pruned.
  - **METSUKE Run 6:** 3 CRITICAL drifts (TRADE L184 Channel-1 silent on Norinchukin RESOLVED-AGAINST + STRATEGY L16 Stage-3 advance + STRATEGY L61 forward-reads refresh) + 5 MODERATE (CFTC narrative, Fed Path → Fed-HIKE regime, header rolls, BOJ trigger PENDING→FIRED, subheader Step 1.5 stamp) + caught Stage-4 duplicate row.
  - **KURA Run 6:** 6 new KB rows (KB-SAM-195 Warsh / 196 FOMC SEP / 197 Iran-electronic / 198 IEA glut / 199 MOF-decay / 200 `[v1.6-DRAFT]` EV-table via Notes-tag routing); 4 palimpsest (KB-006 SUPERSEDED + KB-051/127/152 RE-GRADE); 2 cross-agent auto-memory promotions.
- **3 cross-agent calibration lessons promoted to auto-memory** (all Will-approved Phase C): `[[finding_boot_sweep_macro_regime_context]]` (regime-context check at boot); `[[finding_comprehensive_grep_over_sampling]]` (verifier discipline); `[[finding_risk_control_separate_from_sizing]]` (post-binary stop audit).
- **Money fields untouched throughout.** Position 13 sh @ $58.32 / Jun-18 $58C expired worthless / stop interim single-leg $55.05. No add/trim decision — sizing waits for v1.6 finalize.

### NEXT SESSION

**Imminent (this evening / tomorrow):**

1. **✅ Fri Jun 19 National May CPI — VERIFIED (Sat Jun 20 boot; `cpi_japan.py` down/ESTAT_APPID unset, pulled manually + cross-checked Reuters/CNBC/Japan Times):** headline **1.5%** (↑ from 1.4% Apr — energy base-effect from utility-subsidy *expiry*, NOT demand), core ex-fresh-food **1.4%** (held flat; 4th straight month <2% target, 4-yr low; matched fcst), core-core **1.8%** (−10bp vs Apr 1.9% / fcst 1.9% — slight dovish miss). **Net: soft/dovish underlying → thins the post-1.00% BOJ Oct-hike repricing (multi-month tail thinner); thesis-coherent (BOJ hiked on wage/activity mechanism, CPI stays soft).** Feed these verified figures into v1.6 DRAFT open question #8. ⚠️ Do NOT use the `stockpil.com` aggregator figures (core 2.1%) — wrong; see Findings 6/20.
2. **🔴 Mon Jun 22 CFTC JPY COT (Jun 16 data — first post-catalyst print; delayed from Fri Jun 19/Sat by Juneteenth holiday) — v1.6 EV-table DECISION-GRADE.** Pre-registered: cover <-120K (~67% peak) → v1.6 frame FAILS margin test → **trim/close discussion**; holds -140K to -150K (78-83%) → frame survives margin → vehicle question stays open; builds through -153K/85% → amplifier escalates +5pp → +8-10pp → frame STRENGTHENED (gross EV ~+3.0%, net ~+1.3%). This is THE observable.
3. **RED challenge pass on v1.6 backbone DRAFT** (`THESIS_v1.6_DRAFT.md`). 6 numbered RED challenges embedded inline + EV-table #1a-d sub-challenges. Spawn RED with the draft + challenges; resolve before finalize. Pre-registered gate: vehicle modeling proceeds ONLY IF RED #1-#3 survive.

**v1.6 finalize (after CPI + RED + Mon Jun 22 CFTC):**

4. **v1.6 finalize commit** — rename `THESIS_v1.6_DRAFT.md` → `THESIS.md`; archive v1.5.1 to `thesis/THESIS_v1.5.1_ARCHIVE.md`; update STATUS/CHANGELOG/STRATEGY/TRADE/PREDICTIONS per pre-listed surface list in DRAFT § SAM-LOCAL CHANGES.
5. **5 sizing decisions queued for Will (post-RED, post-CFTC):** (a) retain/trim 13 shares; (b) FXY-vol overlay yes/no [after expiry roll proxy sanity-check]; (c) USDJPY-put / JPY-call structure vehicle change yes/no [GATED on RED #1-#3 surviving]; (d) tighten stop from interim $55.05 → e.g. USDJPY ≥162.5 / FXY ~$55.50; (e) define eligibility window (90d / Jul 31 BOJ / end-CY26).
6. **Update SIGs to LIQUID + HENRY** when v1.6 commits (buckets re-recompute; vehicle disposition; Channel 1 deferred-vs-retired decision).
7. **CHANGELOG entry** for v1.6: full backbone (re-center compression → carry-convexity-tail; Pillar 1 split level-vs-vector; Pillar 4 promoted to center).

**Carry-forward (post Phase A/B/C cleanup — minor items deferred to v1.6 finalize sweep):**

8. METSUKE MINOR drifts (4 items): TRADE L246 Iran row stale-only ("substantively walking back / unsigned" — superseded by SIGNED); STRATEGY L122 Position A Jun-9 parenthetical; STRATEGY L183-187 Key Check Dates partial cleanup (multiple resolved forward-only refs); TRADE L42 hard-trigger subheader timestamp.
9. KURA archive-move (6 SUPERSEDED rows ready for Run 7 `full` mode: KB-064/081/084/087/092/137).
10. KURA FLOW/VX full re-derivation per v1.6 finalize (FLOW-JPN-5.02 / 6.02 too much moved for surgical fix; VX-SAM-11.02 trade balance refresh).
11. **Channel 1 disposition (Will-directed re-examination):** decide DEFERRED → RETIRED pending new mechanism (4-of-4 disconfirmations: Big 3 mutuals + Norinchukin). RED #6 challenges the honesty of "deferred pending" with no specified reactivation path.
12. **SAM-23 framework re-anchoring CHANGELOG entry** (post v1.6 scoring; CH-011 driver/disorder + no-strike decay).
13. **Research backlog (Tier 2/3 un-pulled per Will Jun 15 brainstorm):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.
14. **Position next-touch (post Step 1.5 stop):** interim FXY ≤ $55.05 single-leg. v1.6 finalize sizing decisions (#5 above) are the next position decision point. No add/trim before v1.6 + CPI + Mon-Jun-22 + RED converge.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive; NEXUS_BRIEF rollout = Will-action.

**Closeout (Fri Jun 19 ~6:30 PM ET):** all 13 SAM-session commits + Phase C on origin @ `30ebe292`; tree clean 0 ahead / 0 behind. WALTER/HAWK/REGINALD push-train passengers swept along the way; HAWK's auto-memory work-in-flight (`memory/auto/MEMORY.md` + new HAWK finding) left untouched per scope discipline.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
