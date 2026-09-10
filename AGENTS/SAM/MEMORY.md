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
- [2026-09-10] **`asmade_audit.py` MISMATCH ≠ finding on this desk — 13/15 were level percentages (85%-of-peak, 200% ESR, 4.0% yield). The real defects were rows the tool cannot flag: an undated multi-hop chain, and a re-mark that landed in the SAME commit as its resolution (SAM-07 → 48%, not 75%).** Default for any arrow cell: compare the landing commit with the resolution commit before accepting it as a mark (WQ-112 ii).
- [2026-06-09] **boot.py "Days since touch: X → Nd, MOF Y" — parse carefully.** "Nd" = days since LAST touch of level X, NOT consecutive days above X. "MOF Y" = the most recent MOF op that pushed below the prior level (labels now MonYYYY after Jun-10 script fix). **Default: never propagate script-derived counts/dates without re-reading the script's source semantics; verify price history independently before claiming "Nth consecutive day" or "N days above X."**
- *(Promoted to auto-memory Jun 10-21, full text there, indexed at `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`: [[feedback_suspect_fresh_pull_over_curated_record]] · [[finding_ohlc_verify_before_session_claims]] · [[finding_pre_registration_discipline_through_corroboration]] · [[finding_boot_sweep_macro_regime_context]] · [[finding_comprehensive_grep_over_sampling]] · [[finding_risk_control_separate_from_sizing]].)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts → `CLAUDE.md` boot step 7 (canonical list). · Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — **read sign, not level**).

## Session Notes

### CHANGES SINCE LAST SESSION (found at the Sep-10 JST boot)
- BOJ Sep-9 FINAL = provisional (−¥3,590B, +¥10B vs Ueda) → Sep-9 leg closed; Sep-8 residual still OPEN. MOF weekly Aug-30–Sep-5 LT **+¥111.9B**, but 4-week −¥1.55T trips the script's 🟡 elevated line. MOF curve Sep-9 rallied (30Y 3.956, −16.6bp/5d) while US 10Y/30Y rose to 4.84/5.29 → SAM-41 gaps widened on the US leg. Yen 153.12 at the BOJ 17:00 Sep-9 reference. Brent >$100 (Iran Sep 7–9). Sep-9 US session mild risk-off (VIX 16.46). Masu 9/10 speech; Aida 9/7 Reuters; Bessent 9/9; Katayama 9/8; FY2027 requests 9/4; no 2nd extra budget 9/3; GPIF/Ueno 9/8; July BoP 9/8.

### LAST SESSION — September 10 JST / September 9 ET news-and-data catch-up (Will-directed)
- Wrote `reports/2026-09-10_news-catchup.md` (14 sections, every figure clocked; paywalled bodies cited by headline and marked). Refreshed STATUS, CALENDAR/CATALYSTS (+Sep-11 CGPI verified at `cgpi2607.pdf`; +Sep-30 17:00 JST BOJ Oct–Dec schedule verified at `mpr260831a.pdf`; early-Oct Diet and Oct-8 BoP beyond-horizon), KB-SAM-233→238, TIMELINE block, CHANGELOG, NEXUS_BRIEF.
- **SAM-33 absence claim moved from silence to the record:** `ope20260909.xlsx` vs the Aug-31 schedule — all three buckets scheduled-date/size, 25Y+ ¥75B BTC 2.51×. Method is now in KB-SAM-238; repeat at each 25Y+ date (next 9/16) and at Sep-30.
- No pull (local 12 ahead / 0 behind; BOND dirty). No prediction grade, thesis change or trade. **Inbox processed (Will-directed, second pass):** DAEDALUS as-made audit → `audits/2026-09-10_asmade-disposition.md` (13 false matches; SAM-21/23/26/08/07 to the WQ-112 field form; **SAM-07 vintage 75→48**; Date_Made placeholders corrected on 5 rows); NEXUS amendment-12 → brief reordered CROSS-DOMAIN first. Receipts to both inboxes (carve-out ①).
- URL layouts learned: BOJ finals `jd/<YYYY>/`; ops `statistics/boj/fm/ope/d_release/ope/<YYYY>/`; www3 menu pages suspended since Oct-2025.

### NEXT SESSION

**TIER 0 — DATED:**
- **Sep-10 JST/ET still due:** Totan chart 15:15 JST (review before citing; 98% image is Sep-9); BOJ Sep-10 provisional ~18:00 JST (Sep-8 residual context); EIA noon ET. **Sep-11:** 08:50 JST CGPI (Aug; vs 7.2%); 08:30 ET US CPI (Waller's vote keys on it; consensus +0.4/+0.4, 3.4/2.4 y/y); 15:30 ET CFTC Sep-8 positions per `docket/2026-09-11_CFTC_REVIEW.md` — first post-rally read. **Before Sep-14:** replacement settlement-feed decision; existing proxy stops at expiry. **Sep-16:** 25Y+ op date — repeat the KB-SAM-238 schedule check.
- **Before Sep-29 40Y:** register tenor-appropriate terms. Uniform-price 40Y has **no yield or price tail** (KB-SAM-175); do not apply the 20Y/30Y tail test. The Sep-3 30Y SOFT grade remains frozen; its 0.1bp trip margin/quote quantization is a separate precision question before the next applicable tail window. Retirement counter remains 0-of-2.
- **INFRA disposition CLOSED Sep-9:** original Aug-21 authority found; #2 evals and limited #4 orientation adopted, #3 observability and #1 state migration deferred. Delivery backlog remains owner-paced; no silent-retirement reminder owed.
- **Sep-15/16 FOMC; Sep-17/18 BOJ; Sep-18 CPI and SAM-28/31 close review.** Use `docket/2026-09-18_SAM28_SAM31_REVIEW.md`; original rows govern. FXY episode endpoints and VIX-spike fixing convention remain unresolved, not silently invented. Reminder sidecar supplies no new condition or automatic grade. SAM-33 runs through Dec-31.

**TIER 1 — OWED / MINE TO RULE:**
- **BOJ chart refresh CLOSED for Sep-9 15:15 JST-assumed vintage:** all five rows ingested; repeat zero rows. Repeat the review only when a new image appears; refresh before decision because this review expires Sep-18 00:00 JST. Never restore the old feed.
- **SAM-39 successor:** preregister SHAPE (max single-hour move or time-to-half-move) before any reopened intervention-character window.
- **METSUKE:** Run-18 E1 publisher-side monitor spec for STATUS figure rebases; **Run-12 flags/escalations apply pass remains owed** (July 31 deferred by design).
- **KB:** 209 analytical consolidation DONE; 051/197 substantive cleanup remains owed. Quote repair did not resolve analytical history. FRBNY Q3 ~Nov-13 still adjudicates the U.S. account split.
- **KURA Run-14 auto-memory routings:** verify and complete `finding_rank_is_a_property_of_a_sovereign_window_pair` and extension of `finding_synthetic_artifact_defeats_provenance_tracing` with Kharg Aug-31 AI video. Completion not assumed.
- **CFTC weekly deadband successor:** KB-SAM-231; register before next window, never retune a live one.
- **WALTER charter edit:** mine per Aug-18 lane notice, still owed.
- **JGB `--backfill-from`:** scope decision owed. Prediction boot instrument now implemented; no longer a build obligation.
- **KOYOMI:** trigger-vs-convention baseline audit execute first October; Run-16 verify block roll pending. Class ruling and infrastructure provenance/disposition now closed.
- **Retired-figure relabeling auto-memory:** routing is CLOSED. Verified existing `memory/auto/finding_retired_figure_relabelled_onto_another_subject_evades_its_guard.md` (Sep-4), covering dead BOJ 74.5 relabeled as Fed; do not create a duplicate. Companion lesson: `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]`.
- Keep STATUS <20KB target / 32,550B binding cap — **it is over the soft target after the 9/10 refresh; compress the 9/9 prior-block and the intervention paragraph at the next quiet closeout.** Default-startup promotion WITHHELD after actual eval failure. Diagnose BOJ reaction-function and FX transaction-sign errors before a newly identified trial; frozen criteria stay fixed. Assessment in `evals/runs/2026-09-09_boot-promotion/ASSESSMENT.md`.

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
