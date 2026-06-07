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

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Sat Jun 6 close → Sun Jun 7 PM)

- **Weekend lull** — markets closed; no live tape moves. Sun PM boot.py spot reads roughly equal to Fri close (USDJPY 160.17, Brent $93.09, cross-pairs marginally bigger yen-strength on rolling reads).
- **NEXUS E-phase shipped Sat 6/6 PM** — energy "deflation un-traps Fed" hypothesis CLOSED at step 1 (Iran SUSPENDED MOU 6/1, kinetic re-armed); C-19 Stagflation Trap INTACT; probability split 30/30/40. NEXUS was waiting on E-phase to ratify the NEXUS_BRIEF schema — now ready.

### LAST SESSION (Sun Jun 7 PM — NEXUS_BRIEF rollout + Monday prep)

Multi-track session — NEXUS_BRIEF schema ratification → SAM pilot brief at canonical path → fleet template → STATUS Monday prep.

- **NEXUS R3 ratification of NEXUS_BRIEF schema:** NEXUS proposed 6 amendments + 1 scope clarification + 1 SENDING-table drop-rule. Will accepted the 6 amendments + scope clarification; rejected the drop-rule (kept single-table-per-Will). Amendments: (1) Recent thesis pivot required; (2) Cross-agent tensions required; (3) WATCH→FORWARD CATALYSTS rename + NEXT DECISION carve-out; (4) emoji semantics locked to CLAUDE.md key; (5) conviction decomposition optional per agent; (6) Tier-1 agents only.
- **SAM NEXUS_BRIEF pilot drafted → redlined → finalized at canonical path:** `AGENTS/SAM/NEXUS_BRIEF.md` (75 lines). 5 redline fixes applied: status banner trimmed to ≤120 char cap; As-Of tagged with STATUS-data freshness; Recent thesis pivot compressed; NEXUS SENDING row moved to CALIBRATION as Type B convergence-candidate flag; HAWK WAITING FOR row self-contained. Type B candidate I'm flagging: catalyst-path decoupling (Jun 5 USDJPY 160 via USD-side NFP rather than MOU/oil path SAM-23 assumes).
- **Fleet template drafted:** `AGENTS/SAM/proposals/2026-06-07_nexus_brief_template.md` — skeleton + inline rubric comments, R3 amendments baked in. Pending promotion by Will/NEXUS to `AGENTS/NEXUS/templates/NEXUS_BRIEF_TEMPLATE.md` (SAM doesn't commit outside its dir).
- **MAINTENANCE.md entry logged** — structural docs change documented with calibration lessons (PROME-pair → NEXUS-ratify → Will-arbitrate is healthy iteration org template; "reference don't restate" is the anti-drift rule that lets distributed docs scale; single-SENDING-table + closeout-discipline is a discipline bet not a structural fix — instrument informally).
- **SAM-21 Jun-9 trigger spec freshness update** — STATUS § BOJ ASSESSMENT bumped from "status Jun 4 / 3 sequential reads" to "status Sun Jun 7 / 4 sequential Polymarket ≥90% reads, NFP-locks-Fed stress-tested, CFTC build #5 confirms"; explicit "Default Tue Jun 9 action: trigger fires +5pp" line added so Tue boot executes mechanically without reconstruction.
- **Position unchanged.** No marks moved this session. No new analytical work (SAM-21 still 70%, SAM-23 still 72%).
- **Commits:** `b88198c2` (NEXUS_BRIEF pilot + template + boot.py workbook refresh) — pushed clean, train pulled BRENT's 6/07 PM-2 along with it.

### ARCHIVED LAST-SESSION (Sat Jun 6 — Fri cut-short cleanup)

For reference (will prune next session):

### CHANGES SINCE PRIOR SESSION (Thu Jun 4 close → Sat Jun 6 AM)

- **🔴 Fri Jun 5 NFP +172K vs 85K cons** (BLS). 4.3% U/E steady; AHE +3.4% YoY. Hot — Fed-cut bets crushed. DXY +0.66% to 100.07; 2Y closed 4.17% (highest since Feb 2025); 10Y 4.55%.
- **🔴 USDJPY tagged 160.20 intraday Fri** — first sustained MOF #3 hard-trigger print this cycle. Driver = USD-side NFP, NOT yen-side flow.
- **🆕 Cross-pair divergence:** yen STRENGTHENED vs EUR (−0.63%), GBP (−0.48%), AUD (−1.13%) while WEAKENING vs USD. Real yen demand intact; USDJPY level masked by USD strength. **Vindicates carry-unwind direction read.**
- **🔴 Brent collapsed to $92.94** (-2.20% Fri, 3rd consecutive down session, -4% cumulative from $96.78 Jun-3 baseline). Driver: China demand weakness + Trump-Iran walk-back rumors — SEPARATE from USDJPY direction.
- **🟢 Polymarket BOJ Jun 16 held 96.3% Fri** despite USD-rally + Fed-cut path locking dead — no dovish capitulation. SAM-21 mechanical-trigger Jun-9 condition overdetermined.
- **🔴 CFTC Jun 2 (released Sat Jun 6 AM): net -129,567** = **72.0% of cycle peak** (was 63.7%). Shorts +16,756, longs +1,856, net WoW -14,900. 5th build week. **METHOD residual-gate test resolved AGAINST cover** — amplifier +5pp ON, residual ON. Approaching 85%/-153K danger zone.
- **🟢 Fri's prior session (cut short ~4:30 PM ET):** updated STATUS banner + MARKET DATA + FXY ATM IV proxy (11.08% restored from broken 1.17% Wed read) but session ended before news-cause identification, STATUS internal cleanup, TIMELINE, MEMORY closeout. Picked up this session.

### LAST SESSION (Sat Jun 6 — Fri cut-short cleanup: news-cause + CFTC + STATUS propagation + TIMELINE + closeout)

Sequential mechanical pass to finish Fri Jun 5's cut-short session.

- **Parallel intake (Plan a):** news-sweep via Explore agent identified May NFP +172K as USDJPY 160.20 driver (cross-pair divergence vindicates yen-strength); CFTC pull via cftc_jpy.py returned Jun 2 data (-129,567 = 72% of peak, METHOD gate against cover).
- **STATUS propagation (Plan b):** updated STATE OF PLAY (Jun 5-6 NFP shock + cross-pair + CFTC build); MARKET DATA (CFTC row Jun 2, DXY/2Y/NFP rows added, Polymarket Fri 96.3%); CARRY UNWIND ANCHOR (CFTC 72%, amplifier+residual ON); INTERVENTION STATUS (USDJPY 160.20 tag + SAM-23 Sat Jun 6 evaluation — HELD 72%, both conjunctions blocked by inverted legs; catalyst-path-decoupling analytical note); SECONDARY PATH (NFP locks Fed-cut dead through 2026); KEY THRESHOLDS (refreshed Jun 5-6 status, added CFTC + DXY rows); WHAT TO WATCH (NFP + CFTC RESOLVED rows); REFERENCE DATA Channel 2 (CFTC + cross-pair vindication line).
- **TIMELINE entry:** new ## RESOLVED — Jun 5-6 section with two ### sub-events (Fri Jun 5 NFP shock; Sat Jun 6 CFTC METHOD gate). Last Updated bumped to 2026-06-06.
- **SAM-21 HELD 70%, SAM-23 HELD 72%** — neither pre-registered conjunction trigger cleanly met (SAM-23 inverted leg on each direction; SAM-21 Jun-9 default-path mechanical fire still pending). Pre-registration discipline preserved through 2 more days of cabling.
- **Catalyst-path-decoupling note logged** — Fri's USDJPY 160 print routed via USD-side NFP, NOT yen-side MOU/oil. The SAM-23 framework's path-dependency assumption (MOU break → oil → yen-weak → USDJPY upside → MOF) has decoupled. Re-anchoring is a candidate for the next thesis CHANGELOG entry — flagged for the Jun 9 SAM-21 re-check session.

### NEXT SESSION

**Carry-forward items with deadlines:**

1. **🔴🔴 SAM-21 Jun-9 mechanical re-check — DEFAULT FIRES.** Pre-registered trigger: Polymarket ≥90% + no Takaichi pushback → +5pp to 75%. Both conditions overdetermined; STATUS § BOJ ASSESSMENT pre-positioned with explicit default-fire instruction. Tue boot executes mechanically absent regression. **What would change the hold:** Takaichi cabinet pushback materializing, Polymarket regression below 90% across 3 sequential reads, OR JGB long-end disorderly move re-opening fiscal-dominance via mechanics.

1b. **🟡 Japan Q1 GDP revised — tonight ~7:50 PM ET Sun (8:50 AM JST Mon).** Downward revision softens BOJ hawkish case; upward firms it. Unlikely to cross SAM-21 regression threshold on its own (Mon boot will integrate cleanly).

1c. **🆕 NEXUS_BRIEF rollout — Will-action items:**
   - Promote template from `AGENTS/SAM/proposals/2026-06-07_nexus_brief_template.md` → `AGENTS/NEXUS/templates/NEXUS_BRIEF_TEMPLATE.md`.
   - Possibly relocate schema spec from `AGENTS/SAM/proposals/2026-06-06_nexus_brief_schema.md` → `AGENTS/NEXUS/` (long-term home for NEXUS-owned interface).
   - Spawn other Tier-1 agents (CARL, REGINALD, OZK, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER) with rollout prompt.
   - **SPAWN PROTOCOL closeout amendment** to add brief write-back step (per-agent CLAUDE.md). For SAM: likely step 13a between docket updates and MEMORY. Awaiting Will sign-off before SAM CLAUDE.md edit.

1d. **🆕 Auto-memory promotion candidate added this session:** `finding_schema_iteration_three_tier_pattern` — PROME-pair → NEXUS-ratify → Will-arbitrate as healthy fleet-schema iteration template; each tier added value the others couldn't (rationale logged in MAINTENANCE.md Jun 7 entry).

**Carried forward from prior session:**

2. **🔴 OS.1 fiscal-dominance close — DUE BEFORE JUN 9.** Evidence in (largely-falsified-for-binary per Jun-4 news-sweep); CHANGELOG documents closure; MEMORY captures the 3-question resolution. **Pending:** decide if a tighter THESIS-side "short note" is wanted vs current CHANGELOG-only documentation. Carried forward from Jun 4.

3. **🔧 Eval re-baseline — fire-date Jun 7-8.** Operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`. Fresh skip-boot Claude Code session per `README.md` § Runner protocol. ~20 min total. Two new rows to results.tsv + new `baseline_artifacts/2026-06-XX_v1.5.1_responses.md` artifact.

4. **🆕 SAM-23 framework re-anchoring (CHANGELOG candidate).** Fri's USDJPY 160 print via USD-side NFP — not the MOU-driven oil → yen-weak path the conjunction triggers assumed. The framework's path-dependency assumption is empirically decoupled. Decision: add USD-side independent driver to SAM-23 trigger spec, or accept that the level-trigger (160) is itself sufficient for intervention probability regardless of upstream driver. Logged in STATUS § INTERVENTION STATUS Sat Jun 6 note. Bring up Jun 9 session.

5. **🟠 Sat Jun 13 CFTC next print (Jun 9 data) — last pre-blackout read.** Watch -153K (85% line) — METHOD amplifier escalates to +8-10pp at that level; build past it → 30d marks bump up ~3-5pp. Cover ↓ to -108K would flip amplifier+residual OFF.

6. **🆕 Auto-memory promotion candidates — flag for Will's call:**
   - `finding_catalyst_path_decoupling` — when a framework anchors its mark-up/down conjunction on an assumed catalyst path (MOU → oil → yen), a different path (NFP → USD → USDJPY) hitting the same level invalidates the path-dependency but not the level read. Discriminate level-driven vs path-driven triggers.
   - `finding_pre_registration_discipline_through_corroboration` — held SAM-23 through both legs inverting + SAM-21 through 4 sequential Polymarket reads of 90%+; the value compounds across multiple holds.
   - `finding_counter_frame_3_question_disposition` — Will's OS.1 closure rubric (carried forward from Jun 4).

**Other live items (not Jun-9-gated):**

7. **Position next-touch:** No add/trim under v1.5.1 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) post-Jun-16 ONLY: thesis break if BOTH BOJ dovish AND USDJPY 167+/no MOF (per Jun-3 stop-spec). **Intervention #3 fire would be yen-bullish but same-day reclaim modal (CH-003 baseline ~0.20 sustained unwind|fires).**
8. **🟡 KB-183 (FXY ATM IV proxy)** — Fri restored 11.08% suggests the Wed 1.17% was the broken read, not the calibration. KURA closure pending re-verify across 2-3 more boot.py runs.
9. **🟡 Cleanups deferred:** insurer profiles audit (~10 min); Japanese-source pipeline retire-vs-revive (lean retire); SIGNAL_INTAKE minimal fix vs archive.
10. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify.
11. **🆕 KOYOMI Run 6 escalations (informational, Will-decision pending):** (a) RELEASES.md schema gap for board-composition transitions; (b) MOU walk-back direction inverted — Phase 2 Watch pre-emptive reframe; (c) MOF quarterly per-op release watch (~Aug).
12. **Subagent cadence:** post-Jun-16 BOJ = METSUKE+KOYOMI+KURA trio. KOYOMI BASELINE AUDIT first fires first run of July. **Skipped this session** — no material new analysis, only propagation of Fri close + CFTC data + news sweep into existing structure.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers — cross-pair vindication is signal-worthy though; could trigger HENRY ping); KB cleanup tier-2.

**🟢 RESOLVED SAT JUN 6:** Fri Jun 5 cut-short session cleanup — news-cause identification (NFP shock vindicates cross-pair); CFTC Jun 2 pull (METHOD gate test); STATUS internal propagation (8 sections); TIMELINE Jun 5-6 entry; MEMORY closeout. SAM-21 HELD 70%, SAM-23 HELD 72% per discipline.

### NEXT INFRA SESSION (script build queue — unchanged)

1. **`trade_balance_japan.py`** — MOF monthly TB scrape (Jun 18-19 May TB = Phase 1 stability lag-test per CALENDAR). ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
