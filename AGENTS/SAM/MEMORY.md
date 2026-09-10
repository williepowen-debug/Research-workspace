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
- [2026-09-10] **A carried obligation living only in PROSE has no instrument.** The Sep-16 25Y+ operation check sat in MEMORY and STATUS prose since 9/10 JST with **no `CATALYSTS.tsv` row** — so `catalyst_countdown.py` could not surface it and no boot would have. Identical class to SAM-33's activation going four days unstamped because its condition lived in a prediction's Notes field. **Default: when a session invents a recurring check, the same session writes the machine-readable row — a method described in prose is a method that runs only if someone remembers it.**
- [2026-06-09] **boot.py "Days since touch: X → Nd, MOF Y" — parse carefully.** "Nd" = days since LAST touch of level X, NOT consecutive days above X. "MOF Y" = the most recent MOF op that pushed below the prior level (labels now MonYYYY after Jun-10 script fix). **Default: never propagate script-derived counts/dates without re-reading the script's source semantics; verify price history independently before claiming "Nth consecutive day" or "N days above X."**
- *(Promoted to auto-memory Jun 10-21, full text there, indexed at `~/.claude/projects/-home-willi-Research-workspace/memory/MEMORY.md`: [[feedback_suspect_fresh_pull_over_curated_record]] · [[finding_ohlc_verify_before_session_claims]] · [[finding_pre_registration_discipline_through_corroboration]] · [[finding_boot_sweep_macro_regime_context]] · [[finding_comprehensive_grep_over_sampling]] · [[finding_risk_control_separate_from_sizing]].)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts → `CLAUDE.md` boot step 7 (canonical list). · Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — **read sign, not level**).

## Session Notes

### CHANGES SINCE LAST SESSION (found at the Sep-10 ET boot, ~14h gap)
- **Oil re-priced the differential, not the Japan leg.** Brent $101.68 → **$106.92 (+5.6% d/d)**, WTI +5.8%, oil-in-yen proxy **¥16,490/bbl (+5.5%)**; US 10Y **4.92%** (+8bp, wire says highest since Oct-2023); VIX 16.46 → 17.60; S&P −0.58%; **yen WEAKENED 0.6% to 154.19** and FXY −0.40% — with the BOJ 98% priced to hike Sep-18. Drivers both predate the session: **Trump 9/9** (no Iran talks; war ends after the Nov midterms; oil won't fall until then — a DURATION signal, not a mechanism) and **Houthi strikes on Saudi energy facilities 9/8** (73 wounded; ⚠️ the named Jazan refinery was already shut through August per FALCON KB-151).
- MOF Sep-10 curve **not yet published**; vendor has JGB 10Y ~2.92–2.93%. Different basis — never blended.

### LAST SESSION — September 10 ET boot + catch-up (Will-directed)
- **Both TIER-0 dated items closed at primaries, not by inference.** (1) **BOJ Sep-10 provisional** (`jx20260910.xlsx`, own pull): fiscal **+¥340B vs +¥220B projection, residual +¥120B**, CA balance ¥412.71T — **no yen-buying signature** (an op DRAINS yen and prints large negative; this is a net supply, wrong direction). Sep-7/8 attribution still OPEN. (2) **New Totan chart, publisher stamp Sep-10 11:15 JST** — visually reviewed → `workbook/boj_ois_reviews/2026-09-10T1115-JST.json`, validated with `--no-write`, ingested 5 rows. **September 98% UNCHANGED** through a +5.6% oil session; Oct 27→28, Dec 61→62, Jan/Mar flat.
- Wrote `reports/2026-09-10_et-boot.md` (8 sections, every figure clocked). Refreshed STATUS (header, new ET block, market table, intervention, thresholds, watch, SAM-28/31/33), CALENDAR + CATALYSTS, TIMELINE, CHANGELOG, NEXUS_BRIEF.
- **Docket gap closed:** added a **Sep-16 25Y+ BOJ operation row** to CATALYSTS/CALENDAR as a registered SAM-33 schedule check. It had been carried in MEMORY/STATUS *prose* since 9/10 JST but had **no docket row** — i.e. the instrument that would have surfaced it did not know it existed. Same class as SAM-33's own four-day unstamped activation.
- WALTER lane: 3 signals (001/002/007) dispositioned **INFO-ONLY**, logged and moved. Mokha is a Red Sea leg, **not** a Hormuz gate event — no Japan transmission (Japan's ME crude runs through Hormuz).
- **No pull — and 🔧 I INVERTED THE DIRECTION AT BOOT.** `git rev-list --left-right --count HEAD...origin/master` printed `5  0`; **left is AHEAD, right is BEHIND**, so the tree was **5 AHEAD / 0 BEHIND** — there was nothing to pull. I read it as "5 behind" and reported that to Will, to the PROME packet and to three surfaces. Proof it was ahead: the five "incoming" files were exactly the top five commits in my **own local log** (WALTER ×2, PROME ×3), and `git diff HEAD..origin/master` on a HEAD-ahead tree shows *our own* changes in reverse. PROME independently reported the same direction; I verified at a fresh fetch (9 ahead / 0 behind after my commits) rather than taking the relay. **The no-pull decision was still correct** — six desks were dirty, which is its own protocol bar — but the stated reason was wrong. **Default: never report a `--left-right` count without naming which side is which; the two numbers are indistinguishable once transcribed into prose.**
- **No grade, no thesis change, no trade.** v1.7 stands, book FLAT.

### NEXT SESSION

**TIER 0 — DATED:**
- **Sep-11:** 08:50 JST **CGPI** (Aug, vs Jul 7.2% — oil pass-through is the live question); 08:30 ET **US CPI** (Waller's vote keys on it; consensus +0.4/+0.4, 3.4/2.4 y/y); **15:30 ET CFTC Sep-8 positions — FIRST POST-RALLY READ**, packet ready at `docket/2026-09-11_CFTC_REVIEW.md`. Sep-1 was −92,227 and predates the move; do not read it as a post-rally position.
- **Before Sep-14:** replacement settlement-feed decision — the fixed CME proxy pair STOPS at expiry; no silent roll, no splice.
- **Sep-16:** 25Y+ op date → repeat the KB-SAM-238 record check (now a docket row) · **Japan August trade balance 08:50 JST — read crude VOLUME, not value** (Jul: value +87.8% YoY, volume +5.5%) · FOMC.
- **Sep-17/18:** BOJ MPM · National CPI · **SAM-28/31 grading at close** per `docket/2026-09-18_SAM28_SAM31_REVIEW.md`; original rows govern. FXY episode endpoints and the VIX-spike fixing convention remain UNRESOLVED — do not silently invent either at grading time.
- **Before Sep-29 40Y:** register tenor-appropriate terms. Uniform-price 40Y has **no** yield or price tail (KB-SAM-175) — do not apply the 20Y/30Y tail test. Sep-3 30Y SOFT grade frozen; its 0.1bp trip margin vs quote quantization is a separate precision question owed before the next applicable tail window. Counter stays 0-of-2.
- **Sep-30 17:00 JST:** BOJ Oct–Dec schedule. A scheduled taper-plan change does NOT count against SAM-33; an unscheduled capping op would.

**TIER 1 — OWED / MINE TO RULE:**
- ⚠️ **STATUS is 28,292 B — passes the 32,550 B binding cap but sits at 87% of budget (🟡 rotate-tier).** Two compression passes this session (8/7 frame-break paragraph, durable-reference rows) recovered only **~140 B**: the file is **dense, not bloated**, and further prose trimming will not fix it. **A real reduction needs a hot/cold split** (the 9/10-JST and 9/9 pointer paragraphs and the durable-reference block are the candidates) — that is a design decision, deliberately NOT improvised at closeout. Decide it as its own task.
- **BOJ chart review expires Sep-18 00:00 JST.** Repeat the visual review only when a NEW image appears; refresh before any decision. Never restore the retired feed.
- **SAM-39 successor:** preregister SHAPE (max single-hour move or time-to-half-move) BEFORE any reopened intervention-character window.
- **METSUKE:** Run-18 E1 publisher-side monitor spec; **Run-12 flags/escalations apply pass still owed** (July 31 deferred by design).
- **KB:** 209 consolidation DONE; 051/197 substantive cleanup owed. FRBNY Q3 ~Nov-13 adjudicates the U.S. account split; MOF quarterly per-op disclosure ~Nov-9 is the Japan-side twin.
- **KURA Run-14 auto-memory routings:** verify/complete `finding_rank_is_a_property_of_a_sovereign_window_pair` and the Kharg Aug-31 extension of `finding_synthetic_artifact_defeats_provenance_tracing`. Completion not assumed.
- **CFTC weekly deadband successor:** KB-SAM-231 — register BEFORE the next window, never retune a live one.
- **WALTER charter edit:** mine per the Aug-18 lane notice, still owed.
- **JGB `--backfill-from`:** scope decision owed.
- **KOYOMI:** trigger-vs-convention baseline audit first October; Run-16 verify block roll pending.
- Default-startup promotion WITHHELD after actual eval failure (`evals/runs/2026-09-09_boot-promotion/ASSESSMENT.md`). Diagnose the BOJ reaction-function and FX transaction-sign errors before a new trial; frozen criteria stay fixed.

**TIER 2 — SUCCESSOR AND RESEARCH:**
- v2.0 KILLED; RED body UNREAD / Will-gated. **No successor; v1.7 stands.** v1.8 candidate needs separate FX terms, RED review and Will approval; SAM-41's historical confirmation is unchanged by current 0/5 runs.
- **The live analytical question, unresolved:** the BOJ is 98% priced to hike and the yen weakened anyway because the US leg is repricing faster. Whether that survives the Sep-18 hike is the thing to watch — but it is an OBSERVATION, not a candidate frame, and must not be promoted into one without the full gate.
- Cross-pair rally and modest broad-market stress are distinct. Norway proposed weights (4.6→7.4%) are not flows; BOND's ~$18B is an estimate; no mandatory Jan-2027 ordering inferred.
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
