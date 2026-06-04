# SAM MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or auto-memory, never just accumulate.*

---

## Feedback
- [2026-03-31] Will values boot transparency — wants to know what SAM read, in what order, and whether the process is working well. Don't just orient silently; confirm orientation.
- [2026-03-31] Will thinks long-term about infrastructure. When proposing solutions, address scaling and durability, not just immediate need.
- [2026-04-01] Key dates were getting buried in STATUS.md. Will approved CALENDAR.md as standalone living doc — pure table format, forward-looking only, pruned weekly. Added to boot sequence as step 5.
- [2026-04-02] When explaining complex financial mechanics, Will needs the simplified version first. Start with the plain-English punchline, then layer in detail only if asked.
- [2026-04-02] Will uses Perplexity for deep research and shares outputs. Treat Perplexity data as high-quality but verify framework logic independently.
- [2026-04-11] **Script-defined alert thresholds MUST match THESIS scenario bucket definitions** — not invented independently.
- [2026-04-11] Will prefers intellectually honest corrections over doubling down. Lean toward restraint on thesis-level updates; one data point rarely justifies 15-25pp probability shifts.
- [2026-05-25] **Will wants gap-check before writebacks.** When SAM proposes writebacks, Will asks "any other searches?" — surfaces gaps the synthesis missed. Build in a "what's still missing?" beat before executing multi-file passes.
- [2026-05-28] **Will likes the flag-then-fetch stepwise method for big refreshes** — flag stale items first (review), THEN fetch newer data tier-by-tier. Keeps scope controlled and lets him gate each tier. Applied to the KB freshness pass; worked well.

## Findings
- [2026-05-12] **Read intraday extremes, not just closes — Apr 30 intervention misread.** May 3 STATUS logged Apr 30 yen move as "Tokyo session reprice" when it was MOF intervention (intraday range 5.15y). Add intraday-range alert when single-day range >2.5y. `usdjpy.py` touch tolerance band (May 6 low 155.05 failed strict ≤155).
- [2026-05-03] **Sub-agent fresh-context usability tests surface gaps invisible to the builder.** ~30s/test, high-yield. Re-applicable to any future SAM build/refactor.
- [2026-05-29] **Boot-slimming only wins when the content is DORMANT or SETTLED, not merely duplicated.** Duplication-in-two-places is necessary but not sufficient to cut: (a) THESIS deferred-Channel-1 and (b) closed-prediction post-mortems were clean cuts because they're dormant/settled reference. (c) the May 26 ESR window was equally duplicated (in `insurers/`) but DECLINED — it's the active v1.5 foundation, so thinning it hurts boot readability for ~800 tok. Test before cutting: "is this content load-bearing for the *current* thesis story?" If yes, leave it even if duplicated.

*Calibration / process lessons now live in auto-memory: see [[finding_threshold_vs_mechanism]] (SAM-25/26), [[feedback_audit_behavioral_ranking]] (doc-cleanup ranking), [[feedback_doc_routing_data_drops]] (snapshot-vs-narrative routing), [[finding_followup_audit_pass]] (re-read after scoped ask), [[finding_shallow_clone_false_fork]] (unshallow before trusting git divergence), [[feedback_position_cost_basis_not_authoritative]] (never cite cost-basis from state files).*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL), Barchart FXY OI, Investing.com risk reversals. FXY OI auto-captured by `fxy_options.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (6/2 Tue close-out → 6/3 Wed 09:44 ET)

- **USDJPY essentially flat at 159.94** (Tue 159.92 → Wed 09:44). Still 0.04% from 160 hard trigger; 3rd consecutive day pressing the line. MOF cabling window LIVE before T-2 blackout ~Jun 13.
- **Brent +$1.48 to $97.15** (+1.20% Wed, 3rd straight up day on top of Mon +4.02% / Tue +0.73%). **MOU break NOT walking back; deepening.** Closing in on $100 psychological level.
- **Yen STRONGER on crosses** despite USDJPY-flat — EUR/JPY -0.23%, GBP/JPY -0.32%, AUD/JPY -0.53%. Broad yen bid emerging (thesis-side); FXY masked by USD strength on USD/JPY.
- **JGB curve DROPPED 5-10bp across tenors** (10Y -10bp to 2.577%; 30Y -5bp to 3.810%) — despite oil rebuild. J-ICS mechanism NOT amplifying off the oil leg. Tue 10Y auction orderly result holding.
- **FXY ATM IV proxy 1.17%** (vs Tue 1.56% vs Mon 10.52%) — confirms the proxy-calibration glitch (KB-183 caveat). Not a real vol collapse with BOJ 9 trd days out.
- **`127ae123` push-coordination ITEM RESOLVED:** push-train via LABOR/MARCO/RED overnight closeouts pulled SAM commit to origin. Branch clean. No SAM+OTTO+REGINALD coordinated push needed.

### LAST SESSION (6/3 Wed PM — Polymarket 94.8% + MOF ¥11.73T verification + STOP-SPEC HARMONIZATION) — commits `1122060a`, `96a37dd1`

Mid-session re-engagement (Will paste — "still Wed 6/3, 3:28 PM"). Boot already done in AM; ran boot.py for fresh tape. **USDJPY tagged 160.03 (first print above hard trigger this cycle)** — yen STRONGER on crosses (USD-driven, not fresh yen weakness). Brent $97.70 (+1.77%, 4th up day). FXY $57.37.

- **Polymarket re-pull (Will-requested):** **BOJ hike 94.8%** (+7pp/24h vs Tue 87.6%). SAM-21 **HELD 70%** per Will-paste rationale (single-print ≠ "holds"; the pre-set trigger was "if pricing HOLDS >90% INTO Jun 9-15"). **Pre-registered mechanical trigger in STATUS:** "If Polymarket ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75%." Plus honesty caveat: the 70% is a deliberate Takaichi-ceiling discount (earned: SAM-08/SAM-20), NOT a 30% hold-view.
- **MOF ¥11.7T verification (Will time-boxed ~5 min):** MOF official aggregate Apr 28–May 27 = **¥11,734.9B (authoritative)**. Our STATUS ¥10T was Reuters/BofA two-op back-out (Apr 30 ¥5.48T + May 6 ¥4.3T = ¥9.78T) from BOJ daily settlement balance estimation (±10-15% noisy). Delta ~¥1.95T classified ~70% back-out slippage / ~30% possible unflagged small late-May smoothing op. **Reaction-function intensity read unchanged.** STATUS INTERVENTION table + REFERENCE DATA leads with authoritative MOF aggregate, footnotes the two-op estimate. Per Prome's pressure-test: park as 70/30 prior; revisit only if MOF acts this week or quarterly per-op release confirms.
- **Stop-spec harmonization (Will-decided, pure event-cap mode A):** Resolved a real doc contradiction surfaced by second-pair-of-eyes review. STRATEGY had two-part AND-rule ("no MOF at 167 AND BOJ dovish — both required to exit"); STATUS/THESIS/TRADE had flat "Stop $55.05" shorthand that would have misfired on a pre-Jun-16 USDJPY spike to 167 (would exit before the catalyst that resolves the AND). Five-file harmonization (STRATEGY operationalized into pre/post-Jun-16 table; STATUS lead + state-of-play + Sep-call footer; TRADE entry card + R:R + risk-factor row; THESIS POSITION VIEW + 2 risk-factor rows; CHANGELOG entry). **Operative rule:** pre-Jun-16 = no mechanical price stop, event-capped by sizing ($798 exposure); post-Jun-16 = exit if BOTH (BOJ dovish) AND (USDJPY 167+/no MOF). Catastrophic tail (USDJPY 175+) consciously left unprotected pre-event. Stop-mode and sizing-mode now match.
- **Process win:** Prome's read on this session + the second-model critique caught (a) the doc-contradiction Prome had only seen as a logical gap; (b) the math-vs-prose lag from this AM's CH-004 close (priced hike doesn't unwind → "Aug-2024-speed violence" framing is now in tension with the very METHOD I shipped this AM). Stop fix landed; #2/#3 (math-vs-prose reconciliation + promote structural pillars to thesis backbone) **deferred to next session** per Will. Push hygiene: committed inline rather than at end (Prome's nudge from earlier session-mid hand-off).

### LAST SESSION (6/3 Wed AM — CH-004 close: carry-unwind decomposition methodology, MEASUREMENT CORRECTION)

Clean boot from sync'd origin. boot.py 12.3s, all 9 scripts green. Will picked CH-004 close (option C — decompose with auditable method) from the staleness/cleanups list (4 candidates surfaced; the other 3 deferred to next session).

- **Bottom-up decomposition built, no backsolve.** Per Will's first-principles framing, seeded anchors from judgment (not from a target 70%) and let the formula land where it lands. Result: 30d 37%, 60d 49% — vs prior STATUS marks 70% / 80%. **−33pp / −31pp markdown** on the headline carry-unwind numbers. 7d 14% vs prior 15% (within noise).
- **Two structural errors surfaced by the decomposition** (both honest mismeasurements, not view changes):
  1. **Catalyst-prob → unwind-prob conflation** — SAM-21 (BOJ hike 70%) and SAM-23 (intervention #3 72%) were being transcribed as carry-unwind probabilities. A fully-priced hike doesn't unwind (only hawkish-tail subset does); an intervention that spike-reverses same-day doesn't unwind.
  2. **MOF #3 unwind|fires anchored ~0.50 against CH-003 evidence** — Apr 30 + May 6 both spike-reversed same-day, net ~zero on sustained unwind. Rebased to 0.20. This was the single largest term contribution (0.18 of the 30d union).
- **Will's two methodology corrections during the bottom-up pass:** (1) drop MOF #3 conditional 50% → 20-25% per CH-003 (caught by Will); (2) add a state-dependent residual (~5pp at 30d, ON only when CFTC > 60% of cycle peak) to symmetrically avoid false precision on the downside — Aug 2024 was partly an unattributed-cascade event. Sized small (1.5/5/7.5pp at 7/30/60d) and gated to NOT codify as a permanent floor.
- **Deliverables landed (commit pending):**
  - THESIS § CARRY-UNWIND PROBABILITY METHOD (~65 lines, formula + 5-trigger table + state-dependent residual gate + explicit CFTC amplifier + judgment-labeled overlap discount + update discipline + calibration anchors)
  - STATUS § CARRY UNWIND PROBABILITY refactored — decomposed bucket + driver weights + live anchor state; framed as "decomposed estimate, not authoritative probability"
  - CHANGELOG 2026-06-03 entry — MEASUREMENT CORRECTION framing, no version bump, explicit "yen-direction conviction HIGH unchanged" + "what's NOT changing" list to protect against misreading as thesis softening
  - STRATEGY.md header cross-ref → THESIS METHOD
  - 3 outbox signals (LIQUID 🟡 channel-scoped + UST-unchanged; HENRY 🟠 with explicit "speed unchanged, only probability down" framing; RED 🟠 CH-004 close)
- **Will's framing locks (all integrated):** MEASUREMENT CORRECTION not view change; STATUS labeled "decomposed estimate" not "true probability"; LIQUID/HENRY signals lead with "correction not softening"; residual state-dependent (not a permanent floor); overlap discount judgment-labeled (not derived).
- **Process win:** the decomposition paid for itself in one pass — caught a 33pp inflation in the headline bucket that had been shipping to LIQUID/HENRY across the v1.5 window. Aug 2024 unwind precedent (n=1) was over-anchoring the unwind|fires conditionals; CH-003 evidence was being ignored on MOF #3. RED's CH-004 challenge was right.

### LAST SESSION (6/2 Tue morning — intraday verification, no thesis-level move)

- Clean boot from WALTER cwd (Will explicitly invoked SAM identity). git in sync with origin (0/0). boot.py 7.3s, 8/9 OK + FXY OI skip.
- Tape check: USDJPY 159.92 (0.05% from 160), Brent $95.67 (+0.73% on top of Mon +4.02%), FXY $57.42. MOU break sticking.
- 10Y JGB auction TODAY orderly (BTC 3.53x, tail 0.7bp). No domestic supply-stress story.
- **Polymarket BOJ Jun 16 verified intraday at 87.6%** (Jun 2 ~12:02 ET) — held vs Mon 88.5%. SAM-21 70% mark unchanged. Cross-source: MUFG 80%, swap 77-80%.
- **FXY ATM IV proxy outlier (1.56 vs 10.52 prior day) — calibration glitch flagged.** Not a real vol crush; USDJPY pushing UP at T-10 to BOJ. Investigate proxy / consider real OTC pull for KURA next run.
- No mark changes. No position changes. SAM-23 72% held; SAM-21 70% held.
- Closeout: STATUS lead + state-of-play + market table refreshed Jun 2; MEMORY session notes; commit `4e9d7f50`.

### LAST SESSION (6/2 Tue PM — KOYOMI Run 4 + KURA Run 2 + BASELINE AUDIT spec amendment) — commit `127ae123`

Same SAM window as the AM verification (long session, likely auto-compaction in between). Re-entered with a stale boot read (08:42 morning data — USDJPY 159.35 etc, didn't see the 4e9d7f50 commit until git log). Will course-corrected the parallel-SAM misread (no parallel SAM running — earlier-me, post-compaction recall loss).

- **KOYOMI Run 4 (teams-mode):** Spawned to backfill Jun 2 10Y auction + investigate why it wasn't in CATALYSTS.tsv. Investigation surfaced a ~months-old structural exclusion — prior runs cherry-picked super-long JGB (30Y/20Y/40Y) and silently dropped 2Y/5Y belly/front. Run 4 added 13 forward events (Jun 23 5Y, Jun 30 2Y, full July inc. Tankan Q2 + JGB Jul 2/7/9/14/22/30 + BOJ Jul 30-31), corrected FOMC Jul 28-29 (vs prior Jul 30 hint), 13 RELEASES.md confirmed-dates added.
- **KURA Run 2 (teams-mode):** Low-yield post-Jun-1-inaugural window. 1 KB add proposed (**KB-183 fxy-proxy-v1 Framework** — durable caveat on the FXY vol-proxy collapse-to-near-zero failure mode caught Jun 2 boot). Watermark → 2026-06-02. Precision-over-recall held (1 vs 4 rejected).
- **Will decisions (4):** track 2Y/5Y (KOYOMI Run 4 default OK), promote FOMC Jul 28-29, approve KB-183 as Framework, ping KOYOMI back via SendMessage for spec amendment (dogfood teams-mode iterative use case).
- **BASELINE AUDIT spec amendment (two-round SendMessage):** Round 1 — KOYOMI proposed monthly + post-miss + month-rollover triggers, universe table, propose-only output. Round 2 (SAM refinement) — merged monthly + month-rollover into one trigger; added decline-memory clause via SAM-owned `## CALIBRATION` read-only signal source (mirrors KURA/METSUKE CALIBRATION ownership). Applied to `docket/KOYOMI.md` (step 2a + § BASELINE AUDIT subsection + READ-SET 7a + DONE guard + RETURN line). KOYOMI_MEMORY cleanups (3 self-resolved items removed). MAINTENANCE.md 2026-06-02 AM entry logged.
- **Auto-memory promotions (2):** `finding_teams_mode_iterative_tasks` (when SendMessage earns vs synchronous spawn; default mental model bias correction) + `finding_subagent_baseline_audit` (set-maintenance sub-agents need explicit baseline-scope audit + decline-memory; incremental-update rubrics silently extend-from-precedent).
- **No thesis/STATUS/PREDICTIONS/CHANGELOG changes** this thread. Spec/process work only.
- Commit `127ae123` (KOYOMI spec amendment + KOYOMI_MEMORY cleanups + MAINTENANCE log) held for coordinated SAM+OTTO+REGINALD push.

### NEXT SESSION

1. **✅ OS.1 (FISCAL-DOMINANCE COUNTER-FRAME) — CLOSED Jun 4 LARGELY-FALSIFIED FOR SAM-21 BINARY.** The Jun 3-4 news sweep directly addressed Will's pre-Jun-9 OS.1 test. Resolution:
   - **(a) Did the market reprice the hike UP THROUGH the fiscal news?** YES, clearly. BOJ officials openly cabling hike-plus-more-hikes (Bloomberg Jun 4: "BOJ Is Said to Mull June Rate Hike With Another Possible in 2026"; Ueda Jun 3 Kisaragi-kai: "raise at appropriate pace… upside risks sooner") WITH the Takaichi government's verbal intervention-permission (Takaichi Jun 3 at 160: "stands ready to respond to excessive moves" — reads as permission, not pushback). The market is ignoring fiscal-dominance OR has internalized it as "Takaichi-government and BOJ have aligned on the hike path." Either way, the hike is being priced through the fiscal news, not against it.
   - **(b) Inside the 70% or additional un-priced discount?** The 70% discount stays labeled Takaichi-CEILING (political) — that's now the *affirmatively-closed* leg of the Jun-9 mechanical trigger pre-condition (no Takaichi/cabinet pushback). Fiscal-dominance as an additional un-priced discount: DECLINED. There's no behavioral evidence (in Polymarket, swaps, BOJ comms, Takaichi comms) that the market is missing fiscal-dominance — they're pricing through it. The 70% discount stays at 70% on calibration grounds (SAM failed twice too-hawkish on Takaichi-ceiling: SAM-08 @90%, SAM-20 @60%), NOT on a fiscal-dominance overlay.
   - **(c) Live as post-June PATH/CEILING story?** YES — strengthened by the Sato characterization correction. Sato Ayano takes Nakagawa's seat Jun 30 (NOT Jun 16 as previously framed — date corrected this session). Nakagawa was one of 3 active Apr-28 hike-dissenters; Sato is reflationist. Apr-28-style dissent bloc drops 3 → 2 unless Sato surprises. Material dovish shift in marginal-vote count for the post-Jun-16 path. The v1.5.1 path-MEDIUM near-term-timing conviction holds; arguably strengthened by the Sato firmer-dove finding.
   - **Net:** OS.1 does NOT justify a SAM-21 discount before Jun 9. Pre-registered mechanical trigger discipline stands as-spec'd; Jun 9 re-check proceeds normally. Path-MEDIUM half of v1.5.1 conviction decomposition is validated, not strengthened-with-a-fiscal-overlay.
2. **🔴 USDJPY 160 watch** — **TAGGED 160.03 Wed 15:29 ET (first print above hard trigger this cycle)**. MOF cabling window LIVE before T-2 blackout ~Jun 13. Per new METHOD: even if MOF #3 fires, baseline unwind|fires is only 0.20-0.25 — same-day reclaim modal per CH-003. Per Jun-3 stop-spec: pre-event = no exit on price; ride through any drawdown.
3. **🔴🔴 Jun 16 BOJ MPM** — DOMINANT, SAM-21 70% / Polymarket **94.8% Jun 3** (+7pp/24h vs Tue 87.6%). **Mechanical trigger pre-registered in STATUS:** "If Polymarket ≥90% on Jun 9 re-check AND no Takaichi/cabinet pushback → mechanical +5pp to 75%. Do not move on intraday ticks before then." National May CPI Jun 19 (post-BOJ). Position unchanged: 13 sh + Jun-18 $58C.
4. **🔴 Iran/Hormuz MOU watch** — broke Jun 1; SAM-23 ~72%. Brent reversed Jun 3 evening to **$96.78 (−1.05%)** — 4-day rally snapped (one print, NOT a signal). **SAM-23 mechanical trigger discipline now pre-registered in STATUS § INTERVENTION STATUS** (mark-DOWN requires conjunction of Brent ≥2 down sessions / cumulative ≥−2% + Tehran walk-back signal + USDJPY <159.50; mark-UP requires conjunction of Brent +>1.5%/$100+ tag + USDJPY 160+ tag + Tehran further escalation). Do NOT move on single-print legs. See CALENDAR § GEOPOLITICAL WATCH for the multi-source watch entry.
5. **🆕 Sat Jun 6 CFTC re-evaluate** — first scheduled CFTC-amplifier/residual re-check under new METHOD. Watch the 60% cycle-peak line (~-108K). If short covers below it: amplifier drops 0 from +5pp, residual turns OFF → 30d marks slip ~5-8pp (37% → 29-32%). If shorts build further: amplifier may bump toward +8pp (85% line ≈ -153K), residual stays ON.
6. **🆕 FXY ATM IV proxy investigation** — Wed AM reading 1.17% confirms proxy still broken (Tue 1.56 → Wed 1.17, non-physical with BOJ T-9). Likely scraper calibration. Check `fxy_options.py` source / consider real OTC pull. Captured as KB-183.
7. **🟡 Cleanups deferred from 6/3 AM 4-candidate list** (Will picked #1 CH-004 AM + stop-spec PM; these 3 still live):
   - **#4 insurer profiles audit (~10 min)** — confirm which of the 7 per-insurer profiles have been refreshed post-v1.5; fix the stale CLAUDE.md FILES table flag
   - **#3 Japanese-source pipeline (~10 min)** — zero rows in 5 months; revive-vs-retire decision; lean retire
   - **#2 SIGNAL_INTAKE (~15 min)** — per [[project_messaging_overhaul]] minimal-correctness fix OR archive entirely
8. **🆕 Auto-memory promotion candidate** — the catalyst-prob → unwind-prob conflation pattern (CH-004) + decomposition discipline. Transferable cross-session calibration lesson. Worth promoting as `finding_catalyst_vs_unwind_conflation.md` — applies to ANY agent shipping probability-shaped signals derived from catalyst probabilities. Hold for Will's call.
9. **🆕 MOF intervention quarterly per-op release watch (next quarter)** — resolves the ~¥1.95T residual classification (70/30 slippage-vs-late-May-op prior). If late-May op confirmed, marginally hawkens reaction-function read (MOF was defending 159-160 zone *before* today's break, not just clean 160 tags). Park; no action.
10. **Hedge-ratio verification:** primary-source check on 44.4% vs <30% claim (tracked in KURA_MEMORY PENDING).
11. **🟠 Jun FY2025 Norinchukin** — only near-term Channel 1 reactivation gate; CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. (Tracked in KURA_MEMORY STANDING MONITORS.)
12. **🔧 Eval re-baseline SCOPED & SCHEDULED — fire-date Jun 7-8 (weekend, pre-Jun-9 SAM-21 mechanical trigger)** — operator packet at `evals/REBASELINE_v1.5.1_RUN_PROMPT.md` (drafted Jun 4 in Phase A of Open Flags rail). Frozen-case INPUTs do NOT need updating (they test reasoning against historical context; Case 01 contemporary state at 2026-05-26 includes "$57.48 blend / $55.05 stop" — that's the HISTORICAL test surface, correct for the case). Case 02 RUBRIC L10 had a citation-pointer refresh applied Jun 4 (no criterion change, logged in operator packet for scorer awareness). What CAN go stale (and what the new baseline captures): the runner's behavior against v1.5.1 thesis surface + 14+ new auto-memory entries. Fresh skip-boot Claude Code session per `README.md` § Runner protocol. ~20 min total (10 min/case). Two new rows to results.tsv + new `baseline_artifacts/2026-06-XX_v1.5.1_responses.md` artifact.
13. **Position next-touch:** No add/trim under v1.5 single-path. Triggers: (a) USDJPY <156 for 3 sessions → consider add; (b) BOJ pre-cabling Jun 13-15; (c) **post-Jun-16 ONLY: thesis break if BOTH BOJ dovish AND USDJPY 167+/no MOF** (per Jun-3 stop-spec).
14. **KURA / KOYOMI / METSUKE next runs** — natural cadence: **METSUKE Run 3** Jun 9-15 pre-BOJ window OR on next material POV pivot (Run 2 fired this PM at Will's prompt — lesson: spawn after *every* material multi-file edit pass, not just POV pivots; codified in METSUKE_MEMORY CALIBRATION two-pass-day pattern); **KOYOMI + KURA** post-Jun-16 BOJ. KOYOMI BASELINE AUDIT first fires first run of July. **Lesson for SAM:** when uncertain about sub-agent spawn warranted-ness post-edit-pass, default to YES — METSUKE is propose-only + cheap; declining cost the doc-consistency win we just got.
15. **KOYOMI_MEMORY ## CALIBRATION** — deliberately NOT scaffolded (propose-to-seed). Seed structure when first declination happens.
16. **⏸️ DEFERRED (still holds):** Layer B cross-agent signals (BROCK/HANS PC-cascade pull, HENRY carry-numbers); KB cleanup tier-2 macro/flow rows. Do NOT re-flag.

**🟢 RESOLVED THIS SESSION (Wed Jun 3 PM):** Polymarket re-pull (94.8% verified) + MOF ¥11.73T verification (auth aggregate vs Reuters/BofA two-op estimate, ~70/30 slippage/op prior) + STOP-SPEC HARMONIZATION (5-file pass: STRATEGY/STATUS/TRADE/THESIS/CHANGELOG → pure event-cap mode A pre-Jun-16, AND-condition post-event) + **METSUKE Run 2** (Will-prompted post-closeout; SAM had said "not warranted on operational discipline" — wrong call; Will's instinct right. Run 2: 8 flags / 8 applied / 100% apply rate. Carry Unwind table refactored to CH-004 decomposition; 6 "market ~88.5%" stale parentheticals batch-updated to "~94.8% Jun 3" with context preservation; TRADE header + STRATEGY subheader dates rolled. CALIBRATION updated with 3 new patterns: repeated-phrase clusters reported as ONE batched flag, two-pass-day single-sweep coverage, table-refactor-as-STALE-MARK). Commits `1122060a` + `96a37dd1` + `64f716d9` (MEMORY) + `6945a39e` (METSUKE apply). Branch clean, pushed to origin.

**🟢 RESOLVED EARLIER (Wed Jun 3 AM):** CH-004 close (carry-unwind decomposition methodology landed in THESIS + STATUS + STRATEGY + CHANGELOG; 3 outbox signals delivered).

### NEXT INFRA SESSION (script build queue — unchanged)

When time allows for non-thesis work, in priority order:
1. **`trade_balance_japan.py`** — MOF monthly trade balance scrape (same pattern as `mof_flows.py`). June 18-19 May TB print is Phase 1 stability lag-test per CALENDAR. ~30 min.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 mutuals + Norinchukin + mid-tier. Scope first: does Quartr have all 7? Opens Quartr pattern for BOJ/Treasury/corp IR. ~45-60 min + auth.
3. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
4. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi for BOJ rate markets. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh (Big 3 now fully known post-v1.5); `research/` reorg (cosmetic); SIGNAL_INTAKE.md refresh (pending messaging overhaul).
