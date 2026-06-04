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

### CHANGES SINCE LAST SESSION (6/3 ~21:30 ET close → 6/4 AM)

- **USDJPY 159.92** (flat vs Wed close 159.90; Wed PM tagged 160.03 intraday then pulled back).
- **Brent 2nd consecutive down session** to ~$96.97 (−0.86% from Wed $97.81); cumulative from Jun-3 baseline ≈ flat. 4-day MOU-break rally snapped.
- **🔴 BOJ pre-blackout cabling intensified:** Bloomberg sources-leak Jun 4 ("BOJ Is Said to Mull June Rate Hike With Another Possible in 2026") + Ueda Kisaragi-kai Jun 3 ("raise at appropriate pace, upside risks sooner") + Takaichi Jun 3 verbal at 160 (intervention-permission, not pushback) + Polymarket 94.8% → 96.9% (3rd sequential build).
- **Israel-Lebanon conditional ceasefire Jun 4** removes ONE of Tehran's two stated grievances for message-suspension; walk-back precondition improved but NOT delivered.
- **JGB 30Y +3bp to 3.85%** Jun 4 — curve steepening on hike anticipation.

### LAST SESSION (Thu Jun 4 — eval scoping + v1.5.1 reconciliation + propagation + news ingest + Sato corrections + subagent-trio apply queue)

Long multi-pass session — 6 commits landed.

- **v1.5.1 narrative reconciliation** (commit `39639b06`): 4-part pass — conviction decomposed direction-HIGH/timing-MEDIUM, new STRUCTURAL PILLARS section in THESIS, Channel 2 prose reconciled with CH-004 METHOD (Aug-2024 demoted from expectation → hawkish-of-pricing-conditional upside tail), intervention paradox softened. METSUKE Run 3 fired immediately after (7 STALE-FRAMING / 100% apply).
- **v1.5.1 propagation completion** (commit `693f4e65`): 3-line gap fix — THESIS L318 (HENRY) + STATUS L198 (Channel 2 ref) + STATUS v1.5→v1.5.1 stamps. Will caught the propagation gap.
- **Open Flags rail Phase A + B** (commit `72220937`): eval re-baseline scoped & scheduled Jun 7-8 with full operator packet (`evals/REBASELINE_v1.5.1_RUN_PROMPT.md`); SAM-23 conjunction-based mark-DOWN/UP triggers pre-registered (mirrors SAM-21 Jun-9 pattern); OS.1 re-homed from generic NEXT-SESSION bucket to scoped pre-Jun-9 thesis task.
- **News-sweep + OS.1 closure + Sato corrections** (commit `079e46ca`): 4 parallel news agents surfaced Bloomberg leak + Ueda speech + Takaichi verbal + Polymarket build. OS.1 closed largely-falsified-for-binary in MEMORY + CHANGELOG. Sato date corrected Jun 16 → Jun 30 across 4 docs (verify agent's primary source).
- **Subagent-trio habit run** (commit `01e0fc93`): first parallel-spawn METSUKE+KOYOMI+KURA in teams-mode. METSUKE caught TRADE:246 Sato propagation gap. KOYOMI primary-source verified Sato (BOJ Nakagawa page: "from June 30, 2021 to June 29, 2026"; all 4 sub-claims confirmed — no quarantine). KURA promoted KB-185 (Sato A1). Polymarket cluster D1=(b) structural fix applied — 8 sites converted to STATUS-pointer.
- **Process win:** the "spawn subagents after every material multi-file edit pass" habit (Will-directed) is now validated end-to-end. METSUKE/KOYOMI/KURA dependency graph emerged organically (KURA PENDING_KOYOMI hand-off cleared by KOYOMI verify); cross-agent coordination via SendMessage didn't fire this run but is available.
- **SAM-21 HELD 70%** through multi-source corroboration that genuinely strengthened the case (Bloomberg leak + Ueda + Polymarket + Takaichi). Pre-registration discipline credibility preserved.

### NEXT SESSION

**Carry-forward items with deadlines (Will-flagged Jun 4):**

1. **🔴 OS.1 fiscal-dominance close — DUE BEFORE JUN 9.** Evidence is in (largely-falsified-for-binary per Jun-4 news-sweep), CHANGELOG documents the closure, MEMORY captures the 3-question resolution. **Pending:** decide if a tighter THESIS-side "short note" is wanted (vs current CHANGELOG-only documentation), and write it if yes. Will likely just needs the verification + final ratification.

2. **🔴🔴 SAM-21 Jun-9 mechanical re-check.** Currently 70% / market ~85-95% across surfaces. Pre-registered trigger: *if Polymarket ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75%*. Polymarket leg ≥90% across 3 sequential reads (Tue 87.6 → Wed 94.8 → Thu 96.9); Takaichi-pushback leg affirmatively CLOSED Jun 3 (verbal as intervention-permission). Both conditions overdetermined; Jun 9 fires +5pp absent regression.

3. **🔴 SAM-23 ARMED at 72%.** Symmetric conjunction triggers pre-registered Jun 4 in STATUS § INTERVENTION STATUS. Mark-DOWN: Brent ≥2 down sessions / cumulative ≥−2% from $96.78 + Tehran walk-back + USDJPY <159.50. Mark-UP: Brent +>1.5% / $100+ tag + USDJPY 160+ + Tehran further escalation. Current state: 1st direction-leg of mark-DOWN firing (2nd down session); cumulative not met; no walk-back. Hold.

4. **🆕 CFTC residual-gate test — Sat Jun 6.** First scheduled gate under CH-004 METHOD. Watch -108K (60% cycle-peak amplifier line). Cover below → amplifier 0 from +5pp, residual OFF → 30d marks slip ~5-8pp (37% → 29-32%). Build past -153K (85% line) → amplifier toward +8pp, residual stays ON.

5. **🔧 Eval re-baseline — fire-date Jun 7-8.** Operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md`. Fresh skip-boot Claude Code session per `README.md` § Runner protocol. ~20 min total. Two new rows to results.tsv + new `baseline_artifacts/2026-06-XX_v1.5.1_responses.md` artifact.

6. **🆕 Auto-memory promotion candidates — flag next session for Will's call:**
   - `finding_pre_registration_discipline_through_corroboration` — SAM held the Jun-9 trigger despite multi-source corroboration; pre-registration value comes from holding through "this time is different" pressure.
   - `finding_counter_frame_3_question_disposition` — Will's OS.1 closure rubric: (a) did market reprice THROUGH the counter-frame's evidence? (b) inside the existing discount or un-priced additional? (c) discrete binary or post-binary path/ceiling?
   - CH-004 catalyst→consequence conflation candidate `finding_catalyst_vs_consequence_conflation` — already in auto-memory per `[[finding_catalyst_vs_consequence_conflation]]` (auto-memory MEMORY.md line 96 referenced this).

**Other live items (not Jun-9-gated):**

7. **Position next-touch:** No add/trim under v1.5.1 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) post-Jun-16 ONLY: thesis break if BOTH BOJ dovish AND USDJPY 167+/no MOF (per Jun-3 stop-spec).
8. **🟡 Cleanups deferred (3 items still live):** insurer profiles audit (~10 min); Japanese-source pipeline retire-vs-revive decision (lean retire); SIGNAL_INTAKE minimal fix vs archive.
9. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. (KURA_MEMORY STANDING MONITORS.)
10. **Hedge-ratio verification:** primary-source check on 44.4% vs <30% claim (KURA_MEMORY PENDING).
11. **🆕 KOYOMI Run 6 escalations (informational, Will-decision pending):** (a) RELEASES.md schema gap for board-composition transitions; (b) MOU walk-back direction inverted — Phase 2 Watch pre-emptive reframe (hold pending Brent Jun 5-6); (c) MOF quarterly per-op release watch (~Aug).
12. **🆕 FXY ATM IV proxy investigation** — calibration glitch (KB-183). Check `fxy_options.py` source / consider real OTC pull.
13. **Subagent cadence:** next METSUKE = after any material multi-file edit pass; KOYOMI + KURA post-Jun-16 BOJ. KOYOMI BASELINE AUDIT first fires first run of July.

**⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2 macro/flow rows.

**🟢 RESOLVED THU JUN 4:** v1.5.1 narrative reconciliation (4-part: conviction decomposed, STRUCTURAL PILLARS promoted, Channel 2 prose reconciled, intervention paradox softened); v1.5.1 propagation completion (3-line HENRY + STATUS gap); Open Flags Phase A (eval scoping + operator packet) + Phase B (SAM-23 conjunction triggers); Jun 3-4 cabling-window news ingest; OS.1 fiscal-dominance counter-frame closed largely-falsified-for-SAM-21-binary; Sato corrections (date + characterization, KOYOMI primary-source verified); subagent-trio first parallel-spawn habit run (METSUKE Run 4 + KOYOMI Run 6 + KURA Run 4 — KB-185 promoted). Commits: `39639b06` `693f4e65` `72220937` `079e46ca` `01e0fc93` (+ this MEMORY closeout). Branch clean, pushed to origin.

### NEXT INFRA SESSION (script build queue — unchanged)

1. **`trade_balance_japan.py`** — MOF monthly TB scrape (Jun 18-19 May TB = Phase 1 stability lag-test per CALENDAR). ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
