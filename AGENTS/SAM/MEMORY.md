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

### CHANGES SINCE LAST SESSION (Tue 8/4 close → Fri 8/7 boot)

- **JGB 30Y auction 8/6 FIRM** (BTC 3.864×, tail 1.5bp) — the Meiji ~4.0% floor held its live test; belly softness did NOT spread to the super-long. Long end rallied ~7bp.
- **MOF weekly wk 7/26-8/1 = +¥478B** — reverses 2 SELL weeks but misses the ≥+¥500B durable bar by ¥22B. Dead middle.
- **Sep BOJ OIS repriced again**, 39.7% → 45.6% (8/6) — a 4th consecutive move against route 1.
- **Brent retraced UP** to $82-83 from the 8/4 $79.98 low.
- **8/7 AM: US NFP −23K with −103K net revisions**; Sep Fed *hike* odds 57% → 43.9%.

### LAST SESSION (Fri 8/7 — THE PRINT DAY. The frame broke.)

- **🔴 THE 8/7 CFTC PRINT KILLED THE THESIS. Net −45,473 = 25.3%** of the −180K peak, from 90.8%. WoW **+117,939** on ~flat OI = **position REVERSAL, not liquidation** — 3.8× the largest prior weekly cover, inside the intervention window. **Leg-1 SPF fired** (through −108K/60% by 62,527 contracts, 42 days early) → **THESIS v1.6.11 → v1.7, carry-convexity tail RETIRED TO LOW.** SAM-29 + SAM-40 both FAILED → **14/14/1**. Buckets ~8/23/32 → **~3/8/13**. **Position FLAT throughout; $0 ever at risk; nothing was ever executed on this frame.**
- **The calibration lesson, and it is not "I missed it":** SAM-22's mechanism (intervention → mass cover) was **named in writing on 8/2 AND 8/4** as one of two ways the grade could die. I then priced it at **~25%** while holding a MED-HIGH grade the same document called **PROVISIONAL**. *Naming a risk and then under-weighting it is a distinct error from not seeing it* — promoted to auto-memory.
- **What worked, recorded because it is repeatable:** PROVISIONAL flag at award · both reversion paths named in advance · resolver **frozen 8/4 and run on the letter** (not re-tuned at scoring time) · Will's **Monday-execution ruling pre-registered the morning of the print, before the number existed** · the **§5C override that fired ON THE LETTER on 8/3 deliberately not acted on** — had it been taken the book would have been long into this print.
- **Deliberately did NOT declare a successor frame.** v1.7, not v2.0 — inventing a replacement in the same hours as the print that killed the old one is the improvisation these rails exist to prevent. The open question is written into THESIS + STATUS so it cannot be skipped: *the carry trade unwound and the yen is at 157.5, not 145 — what is the thesis when the fuel has burned and the level barely moved?*
- **🟢 Killed the OIS single-witness problem with a primary derivation.** Pulled **TFX 3m-TONA futures settlements** (free daily statistics CSV — the actual instrument), verified the Reference Quarter **against the TFX rulebook** rather than assuming. Method reproduces centralbank.watch to **−0.5bp on 8/3**, diverges **+3.4bp on 8/6**; curve shift concentrated 26.09/26.12/27.03, dying past 27.06 = **hike PULL-FORWARD, not term premium.** Sep unpriced now a **band ~40-54%** with the Sep/Oct-split caveat travelling. *(`boj_ois.py` second-source gate: queued, deliberately not built hours before a print.)*
- **Pre-print discipline held all day:** the four-anchor re-pencil was computed and **committed BEFORE the print** (`ce71c5cbf`) so the fuel outcome could not contaminate the other five anchors. Two amendments to it were logged **as amendments with their causes**, not silent edits.
- **LABOR's read trimmed my own mark.** I moved route 4 off COLD on the payroll headline **before** reading the domain owner — wrong order. LABOR: **private +30K vs government −53K**, U-3 fall participation-driven = NO-SIGNAL under its L-06, matrix at cycle-low bearishness. Route 4 → ~7-8%, not ~8-9%, and LABOR explicitly **not** cited as endorsing it (it scopes rate-path out of its lane).
- **Found LABOR's packets stranded in the dead `AGENTS/PROME/` tree** — not my regrow this time. Two files, one from 8/7 carrying an escalation aimed at PROME. **Committed to git, so the orphan detector cannot catch them: they reached the repo and reached nobody.** Flagged both parties; recommended the fix go into LABOR's `CLAUDE.md`, since the identical packet-borne correction failed on me three times.
- **Ruled BND-11 dead rather than re-terming it:** the ≥+¥500B bar sits at **0.49σ** of its own series' dispersion (σ≈¥1.02T, n=26) — 4 sign flips in 8 weeks. **The gate could never have resolved.** Single-week form stood down; 4-week rolling proposed; **BOND ratifies** (it is BOND's gate, not mine to re-spec).
- **KOYOMI Run 15 caught a staleness my own 8/4 sweep missed** — CALENDAR's Sep-18 row still read "Sep priced ~23%", the pre-8/4 figure. **Third surface that one number has gone stale on.** Seeded a SAM pre-edit block in its NEXT RUN HINTS so Run 16 cannot restore "COLD" or wait on me for BND-11 terms.
- **Consumer pass: the ~60% figure is UNSEARCHABLE by numeric token.** 879 hits, essentially all false positives (`60d window`, `$60M/week`, `60K views`). **A bare 2-sig-fig number cannot be consumer-checked** — its propagation control must be editorial (publish the band + caveat) not a grep. High-information tokens (163412, 90.8) found **3 genuine consumers**: WALTER REGISTRY, NEXUS STATUS, TERRY's card. Packets sent to the first two; TERRY covered by the stand-down.

### NEXT SESSION — the frame is gone; do not rebuild it by reflex

**⚡ TIER 1 — the successor question:**
1. **Do NOT answer "what now?" from inside the old frame.** The written question: *the carry trade substantially unwound and the yen is at 157.5, not 145 — what is the thesis when the positioning fuel has already burned and the level barely moved?* Candidate angles: does a de-crowded JPY short change the *distribution* of future yen moves (thinner tails? or fresh capacity to re-short)? Is Pillar 1 compression now the live mechanism after all, given the Fed repricing? **Treat as a fresh build, not a repair.**
2. **Owed to TERRY: the "yen strengthens but BOJ does nothing" branch + exit rule.** Deferred all of 8/7 by design (never draft a thesis branch in the same hour as an entry decision). No longer blocked.
3. **Read METSUKE's post-break drift report and apply.** Expect heavy drift in TRADE/STRATEGY — a thesis break invalidates trade docs wholesale. ⚠️ Apply by pattern; watch for the inverse error (Pillar 2 / oil-in-yen / risk-discipline content is **unaffected** and must not be over-corrected).

**TIER 2 — open loops:**
4. **BOJ `jd` archive path appears DEAD** (n=3 failed sessions, every registered pattern, including one my own confirmation doc calls canonical). ⚠️ **`jd20260731` also 404s, and it must exist** — the SAM-39 base rate (n=62) was measured from it. **Consequence: that base rate is not currently reproducible.** Do proper path discovery, not another blind retry.
5. **`boj_ois.py` TFX second-source gate** — today's finding is only durable if reproducible. Script queue.
6. **SAM-39 still open** (4 sessions, none qualifying; 8/7 was 1.924y, widest since 8/3, session incomplete — verify the closed figure). **SAM-28 will very likely fail at 9/18; do NOT grade it early.**
7. **BND-11:** await BOND's ratification of the 4-week rolling terms. Do not re-add a forward MOF-weekly gate row meanwhile.
8. **P3-Asia Batch-3** (PROME, gate open since 8/3) — still in inbox, un-executed, deliberately not swept.

**⛔ DO NOT:** re-arm anything on a CFTC re-build through −153K/85% (that line is **void**, a reclaim condition inside a dead frame) · re-derive modal bands or stops for a structure that will never open · treat Sep-18 as a "retire-check" (it is now only the SAM-28/39 grading date) · quote Sep unpriced as a point estimate.

## Tooling — how to find out what exists

**Never assume, and never trust a hand-written list. Run:** `.venv/bin/python3 AGENTS/SAM/scripts/boot.py --tools`
Generated from `scripts/` at run time (name · boot-wired? · purpose), so it cannot go stale. Every boot also prints a tool count and **flags drift in both directions**. **Check it before building any script or doing a pull by hand** — the 8/4 BOJ-OIS failure was, at root, not knowing what already existed. *(12 tools, all boot-wired, as of 2026-08-04 — that count is a fact about that date, not a maintained figure; ask the command.)*

### NEXT SESSION (Wed 8/5 → the 8/7 print) — TIERED. Tier 1 exists to protect one decision.

**⚡ TIER 1 — the 8/7 print is the only thing that moves the book:**
1. **🔴 SETTLE FRIDAY-vs-MONDAY EXECUTION *BEFORE* THE PRINT — Will's call, SAM proposes.** CFTC lands **15:30 ET; the US close is 16:00.** A CONFIRM under memo §5B ("entry on TERRY live re-mark + Will [Approve]") means either a **30-minute Friday window in thin FXY options**, or **Monday 8/10 with weekend gap risk** (yen reopens Sunday-night Asia). Decided at 15:31 under a fired gate, this is the SAM-30→SAM-36 whipsaw shape. It is free to decide now and unfixable after.
2. **Pre-compute the four-anchor re-pencil for every anchor EXCEPT fuel.** Route-5 (oil decaying) and BOJ-surprise (room shrinking) have BOTH already moved **down**; 60d ~32 is flagged **known-generous**. Running the re-pencil in the same session as an entry decision = evaluating a CONFIRM against buckets I already believe are too high. Leave one slot; plug the fuel leg in Friday.
3. **Drain the legacy inbox (7 packets, oldest 8d) BEFORE 8/7.** No longer housekeeping: it demonstrably carried a **live blocking question on a live card** (TERRY's 007 tenor ask) that sat unread ~1 day and surfaced only by accident.
4. **Verify the OIS *cumulative* basis at a primary TONA source.** "~60% unpriced" is now load-bearing across ~8 surfaces and sets route 1's SIGN — resting on **one source + one wire**, basis explicitly unverified. Thinnest evidence under the most-propagated number of 8/4.

**TIER 2 — scheduled:**
5. **Thu 8/6 triple:** 30Y auction (**live test** — Meiji ~4.0% floor is 1.8bp away and the 10Y just cleared at a 6bp tail) · MOF weekly wk 7/26-8/1 = **BND-11 3rd-week TRANSIENT confirm** · **`jd20260804` re-pull** (404'd 8/4; durable archive, it will appear).
6. **🔴 Fri 8/7 15:30 ET — THE print.** Run the resolver **ON THE LETTER**; SAM-40 scores it; **do not let MED-HIGH shade the fuel test and do not re-tune the map at scoring time.** Then re-pencil (fuel plugged in) + **modal-band re-derivation** (METSUKE E2).
7. **Verify 8/4's CLOSED intraday range** (SAM-39; 0.75y was *partial*). Re-run **`boj_ois.py`** — ≥5pp Sep move = the registered named-driver bar; still single-source, corroborate before re-marking.

**TIER 3 — cheap infra, real payoff:**
8. **🆕 Boot inbox alert — count + oldest age + titles, NOT processing.** ~20 lines. Respects the MAIL rule ("don't process inbox at normal spawn") while killing the silent-staleness failure that cost a day on 8/4. Mechanize the cap, not the ritual.
9. **METSUKE apply pass** (9 flags + 3 escalations) — now safe: the ~60% guard is seeded in its NEXT RUN HINTS so flag #5 can't re-introduce ~77%.

**⛔ DO NOT:** re-mark on the 8/6 auction alone · bump the THESIS version pre-8/7 · re-tune the resolver map at scoring time · write packets to `AGENTS/PROME/` (dead path — it's `PROME/inbox/`, now in CLAUDE.md).

**Owed / deferred:** ✅ **PROME dispositioned BOTH 8/4 asks (packet 8/4 ~17:0x, processed).** `MACHINE_LOCAL.md` recipe now carries `MESSAGING/requirements.txt` ✅; **the `env_doctor` scoping call went to DAEDALUS, not PROME** — DAEDALUS owns repo-root `scripts/` since 7/31 (Will-ruled), so **don't chase PROME for it.** `ESTAT_APPID` recorded **PRESENT** (SAM fixed it 35min after sending the packet). 🔧 **The box still missing PyYAML is `DESKTOP-BC6EF81`, NOT `WilliePOwen`** — SAM wrote "laptop" repeatedly on 8/4 and had it BACKWARDS (this box IS the laptop and is fixed); PROME independently confirmed. **State it by HOSTNAME, never nickname.** Same for `ESTAT_APPID`: desktop column is ❓UNKNOWN, `.env` is gitignored so neither restore travels — both are one command at the next machine switch) · `catalyst_countdown.py` 2027 holidays (guard is loud, dates need *sourcing*) · Aug-21 National July CPI = first **2025-BASE** print (re-baseline first; read `cpi_japan.py`'s **PAIRED** line, never **LEAD**, as "the gap") · KB-202 (KURA autonomous) · KB-152 → route Q2-actuals to BROCK/HANS · Japan-LNG/JKM · Batch-3 P3-Asia · May TIC · evals re-baseline · TB ~L394 cites a pruned "CALENDAR Jun-17 row" (provenance only).

---

### PRIOR SESSIONS — compressed 2026-08-02 (narratives → `thesis/timeline/TIMELINE.md` + STATUS pointers + git history)

- **7/31 (Fri, Will-launched LIVE BOJ DECISION WATCH — the marquee session of the cycle):** graded the MPM off the primary statement ~35 min after publication. **SAM-38 CONFIRMED at FULL-C** (hold 8-1, hawkish Takada dissent for 1.25%, overshoot-risk Outlook, FY2027 plan untouched; Oct OIS ~26-40% → ~64% on the presser) + **SAM-34 CONFIRMED** (hold @85%, 3rd straight calibrated BOJ binary). MOF monthly **¥0** → the 7/2 no-strike HARD-CONFIRMED. Buckets → 5/19/29 (v1.6.10). **Process that worked:** BOJ-site curl monitor caught publication within a minute; PDFs pdfminer-extracted; graded against frozen branches with zero re-derivation. **Contamination clause CLEAN *and it paid*** — circulating pre-dated content said "GDP 0.8%", actual FY2026 was 0.6 → fabricated-wrong, not leaked; routed to WALTER, **now generalized into its `SIGNAL_PROCESSING_CHECKLIST.md` v0.30 guard** (closes the 7/29 auto-memory candidate — WALTER owns the class, no SAM memory needed). Same session: KOYOMI clean, **METSUKE Run-12 (9 flags + 3 escalations, apply deferred BY DESIGN → still owed)**, KURA FAILED mid-run (API error, zero partial writes).
- **7/30** — 🔴 yen +2.7% intraday hours before the BOJ; suspected MOF op. VIOLET canary first-ever FIRE→WATCH (her caveat: RV cannot separate intervention from unwind); **equity vol never transmitted** (VIX −17.3% = evidence against an Aug-2024 replay).
- **7/29 · 7/23-7/16** — BOJ 4-branch pre-registration frozen; CFTC re-build to 84.5%; MOF-weekly reversal to 2 SELL weeks; SAM-35/37 CONFIRMED; Brent through $100; June TB Phase-1 inversion. → TIMELINE Jul 11-23 + Jul 24-31.


**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** ~~GPIF/pension flows~~ ✅ BUILT 7/9 (`gpif_flows.py`); fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive. *(NFP AHE MoM exact print unpinned — BLS 403s bots; curl w/ User-Agent per [[finding_edgar_403_user_agent_header]] next session if needed.)*

### NEXT INFRA SESSION (script build queue)

**Queue is EMPTY as of 2026-08-04** — the last open item (`boj_swap_pricing.py`) shipped as `boj_ois.py`. `trade_balance_japan.py` ✅ 6/10 · `gpif_flows.py` ✅ 7/9 · `boj_ois.py` ✅ 8/4. **Before proposing any new script, run `boot.py --tools`** — it lists what already exists, generated from disk. Still-deferred, non-script: `insurer_quartr.py` (Quartr watcher, needs auth), `mof_flows.py` NISA retail-flow tripwire, `boj_events.py` (SoO/speeches/minutes).
