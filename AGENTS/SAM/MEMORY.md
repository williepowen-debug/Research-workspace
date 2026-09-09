# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or auto-memory, never just accumulate.*

---

## Feedback
- [2026-03-31] **Will values boot transparency** — wants to know what SAM read, in what order, and whether the process is working. Don't orient silently; confirm orientation. · **Thinks long-term about infrastructure** — address scaling and durability, not just immediate need.
- [2026-04-02] When explaining complex financial mechanics, **Will needs the simplified version first.** Plain-English punchline, then layer in detail only if asked.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. One data point rarely justifies 15-25pp probability shifts.
- [2026-05-25/28] **Will wants a gap-check before writebacks** — he asks "any other searches?", which surfaces what the synthesis missed; build a "what's still missing?" beat into multi-file passes. · **He likes flag-then-fetch for big refreshes** — flag stale items first (review), THEN fetch tier-by-tier.
- [2026-06-04] **Subagent-trio habit run pays off immediately** — first parallel-spawn (METSUKE+KOYOMI+KURA, teams-mode) caught a TRADE:246 Rule #3 propagation gap I missed, primary-source verified Sato characterization, surfaced KURA-KOYOMI dependency pattern. Consistency-over-yield validated even on low-watermark days (KURA Run 4 was "low-yield" but produced KB-185 + 2 auto-memory candidates). Codified pattern. **[RE-VALIDATED 2026-07-02 at the opposite (high-watermark) extreme** — trio caught the modal-band contradiction, the Sep-18 window-end/BOJ-MPM coincidence, the 2025-base CPI discontinuity, and cleared the FLOW deadline breach. Performance review → MAINTENANCE 2026-07-02 entry. **Spawn guidance:** routine KOYOMI/KURA syncs run clean on cheaper model tiers (KOYOMI Runs 8-11 spanned Opus/Sonnet/Fable, all clean) — reserve the big model for post-pivot METSUKE runs + audit-heavy KOYOMI runs. METSUKE now has a named `verify-pass` mode (spawn same-session as any SAM inline sync); KURA default is now `full`.]**

## Findings
- [2026-05-12] **Read intraday extremes, not just closes.** Add intraday-range alert when single-day range >2.5y (Apr 30 intervention misread = misattribution to Tokyo session).
- [2026-05-29] **Boot-slimming wins only when content is DORMANT or SETTLED, not merely duplicated.** Test before cutting: "is this content load-bearing for the *current* thesis story?" If yes, leave it even if duplicated.
- [2026-06-04] **Sato verify pattern — agent-claimed characterizations need primary-source confirm BEFORE propagation into multiple docs.** Rule #3 instance: news-sweep verify agent claimed "Sato joins Jun 16" → I propagated to 4 docs; KOYOMI Run 6 primary-source verify caught the date error (actual Jun 30) + confirmed the rest. **Default: when an agent-output drives multi-doc cascade, primary-source verify the load-bearing facts BEFORE the cascade, not after.**
- [2026-06-09] **boot.py "Days since touch: X → Nd, MOF Y" — parse carefully.** "Nd" = days since LAST touch of level X, NOT consecutive days above X. "MOF Y" = the most recent MOF op that pushed below the prior level (labels now MonYYYY after Jun-10 script fix). **Default: never propagate script-derived counts/dates without re-reading the script's source semantics; verify price history independently before claiming "Nth consecutive day" or "N days above X."**
- *(Promoted to auto-memory Jun 10-21, full text there, indexed at `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`: [[feedback_suspect_fresh_pull_over_curated_record]] · [[finding_ohlc_verify_before_session_claims]] · [[finding_pre_registration_discipline_through_corroboration]] · [[finding_boot_sweep_macro_regime_context]] · [[finding_comprehensive_grep_over_sampling]] · [[finding_risk_control_separate_from_sizing]].)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts → `CLAUDE.md` boot step 7 (canonical list). · Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — **read sign, not level**).

## Session Notes

### CHANGES SINCE LAST SESSION / LAST SESSION — September 9 boot corrections

- Implemented the approved [six-part design](proposals/2026-09-09_boot-corrections.md). Tool usage → `scripts/README.md`. Neutral monitor labels, corrected live CFTC normalization/cover arithmetic, honest failure output, raw reports, BOJ review preparation and read-only prediction/orientation modes are available. Default-startup promotion awaits fresh-session eval; no simulated pass.
- No market refresh, new prediction grade, thesis change or trade in this pass. September 8 [integration](reports/2026-09-08_integration.md) and [assessment](reports/2026-09-08_catchup-assessment.md) remain current. September 9 prior boot: 13/14; changed BOJ chart remains unreviewed.
- Full previous handoff preserved verbatim in `MEMORY_ARCHIVE.md` § 2026-09-09. Feedback, Findings, auto-memory references and this template are retained. Historical narrative is cold; all open obligations are carried below.

### NEXT SESSION

**TIER 0 — DATED:**
- **Sep-9/10:** BOJ actuals/forecast plus independent pre-BOJ broker baseline; Sep-8 U.S. funding and EIA outlook. **Sep-11:** post-rally CFTC + CPI. Cause OPEN. **Before Sep-14:** validate replacement futures pair; existing proxy stops at expiry.
- **Before Sep-29 40Y:** register tenor-appropriate terms. Uniform-price 40Y has **no yield or price tail** (KB-SAM-175); do not apply the 20Y/30Y tail test. The Sep-3 30Y SOFT grade remains frozen; its 0.1bp trip margin/quote quantization is a separate precision question before the next applicable tail window. Retirement counter remains 0-of-2.
- **~Sep-18 INFRA_AGENDA:** per-item adopt/defer review owed. This is an **estimated reminder**, not an authenticated expiry timestamp; trace the original Will ruling before any automatic retirement. KOYOMI's Aug-27 class ruling is already present in `docket/KOYOMI.md`; no duplicate class ruling owed.
- **Sep-15/16 FOMC; Sep-17/18 BOJ; Sep-18 CPI and SAM-28/31 close review.** Exact grading conditions remain in the prediction rows; reminder sidecar supplies no new condition or automatic grade. SAM-33 runs through Dec-31.

**TIER 1 — OWED / MINE TO RULE:**
- **BOJ chart refresh:** run `boj_ois.py --prepare-review`, visually inspect saved image/time/terms, finish a reviewed JSON, then validate and ingest per `workbook/BOJ_OIS_README.md`. Preparation does not make a quote current. Never restore the old feed.
- **SAM-39 successor:** preregister SHAPE (max single-hour move or time-to-half-move) before any reopened intervention-character window.
- **METSUKE:** Run-18 E1 publisher-side monitor spec for STATUS figure rebases; **Run-12 flags/escalations apply pass remains owed** (July 31 deferred by design).
- **KB:** 209 analytical consolidation DONE; 051/197 substantive cleanup remains owed. Quote repair did not resolve analytical history. FRBNY Q3 ~Nov-13 still adjudicates the U.S. account split.
- **KURA Run-14 auto-memory routings:** verify and complete `finding_rank_is_a_property_of_a_sovereign_window_pair` and extension of `finding_synthetic_artifact_defeats_provenance_tracing` with Kharg Aug-31 AI video. Completion not assumed.
- **CFTC weekly deadband successor:** KB-SAM-231; register before next window, never retune a live one.
- **WALTER charter edit:** mine per Aug-18 lane notice, still owed.
- **JGB `--backfill-from`:** scope decision owed. Prediction boot instrument now implemented; no longer a build obligation.
- **KOYOMI:** trigger-vs-convention baseline audit execute first October; Run-16 verify block roll pending. Class ruling already closed; infrastructure deadline provenance still open.
- **Retired-figure relabeling auto-memory:** routing is CLOSED. Verified existing `memory/auto/finding_retired_figure_relabelled_onto_another_subject_evades_its_guard.md` (Sep-4), covering dead BOJ 74.5 relabeled as Fed; do not create a duplicate. Companion lesson: `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]`.
- Keep STATUS <20KB target / 32,550B binding cap. Default-startup promotion and deferred eval re-baseline: operator packet in `evals/BOOT_CORRECTIONS_2026-09-09_RUN_PROMPT.md`.

**TIER 2 — SUCCESSOR AND RESEARCH:**
- v2.0 KILLED; RED body UNREAD / Will-gated. **No successor; v1.7 stands.** v1.8 candidate needs separate FX terms, RED review and Will approval; historical SAM-41 remains confirmed.
- Cross-pair rally and modest broad-market stress are distinct. Sep-1 CFTC predates the move; residual does not identify an operation. Norway proposed weights (4.6→7.4%) are not flows; BOND's ~$18B estimate is separate. No mandatory January-2027 implementation ordering inferred.
- Still-open research: fiscal/Takaichi + JGB supply; digital deficit; BIS yen carry beyond CFTC; Taiwan/China→Japan tail; Japan semis/AI capex.

**SUB-AGENT CLOSEOUT — standing:** after any run, `subagent_memory_roll.py`; after KURA, also `kura_proposal_roll.py`. Never `--all` while any sub-agent is live. They propose, SAM applies. Move never delete; unmarked = LIVE.

**DO NOT:** rearm retired −153K/85%; use 180K for current display (R=188,077; legacy storage stays historical); cite unreviewed/historical BOJ or Fed probabilities as current; call allocation proposals purchases or trust accounts GPIF; infer UST sales from foreign-debt aggregates/reserve stocks; call CME residual true basis; compare continuous oil across rolls. Historical 30Y high remains 4.131% Sep-1.

## Tooling — how to find out what exists

Run `.venv/bin/python3 AGENTS/SAM/scripts/boot.py --tools` before building or pulling manually. Inventory is generated; helpers and explicit modes are documented in `scripts/README.md`. `--orient` and `--predictions` are read-only; `--quick` skips only options and still runs the other market writers. Index output is not completed orientation: read every numbered part and check hashes.

**Owed / deferred:** `env_doctor` scoping belongs to DAEDALUS, not PROME. Verify environment state on the actual hostname by executing its path; prior laptop/desktop and key-presence claims were contradictory and are historical only. Source 2027 holidays for `catalyst_countdown.py`; CPI comparisons must pair the same base/gauge (2025-base core-core artifact is not a headline/core claim); KB-202; KB-152 Q2 actuals to BROCK/HANS; Japan LNG/JKM; Batch-3 P3-Asia; May TIC; TB citation to pruned CALENDAR Jun-17 row (provenance).

### PRIOR SESSIONS — archived

Full narratives → `MEMORY_ARCHIVE.md`, TIMELINE and STATUS_ARCHIVE. Carry these calibration lessons: capacity is not use (execute fallback before claiming it fired); a subset is not the population; quote the horizon with any sovereign rank; a CANDIDATE label does not replace checking the premise; primary-source-check agent claims before a multi-doc cascade; naming a risk can coexist with underweighting it. Existing auto-memory references above stay intact.

**DEFERRED:** Layer B BROCK/HANS PC-cascade pull; tier-2 KB cleanup; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive; exact NFP AHE MoM print still unpinned (source access workaround only if needed).

### NEXT INFRA SESSION (script build queue)

BOJ unattended decoding remains an enhancement; review preparation now exists. Still deferred: `insurer_quartr.py` (auth), `mof_flows.py` NISA retail-flow tripwire, `boj_events.py` (SoO/speeches/minutes). Run `boot.py --tools` before adding a script.
