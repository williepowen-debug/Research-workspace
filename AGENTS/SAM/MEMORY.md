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

### CHANGES SINCE LAST SESSION (Thu 8/13 close → Fri 8/14 window spawn)
- **USD/JPY went nowhere for a fourth session** (159.36, −0.07%); Brent **back UP to $88.34 (+1.46%)**, reclaiming the 8/10 spike high — so the "fourth risk-premium round-trip" read is **suspended, not confirmed**.
- **🔴 The BOJ-Sep crowd leg repriced violently while my instrument crawled.** Polymarket P(+25bp Sept) **42.5% [8/10 12:00Z] → 79.5% [8/14 14:16 ET]**, continuous; own TFX/OIS only **49.0% → 51.0%**. **The gap went from ~17.8pp to ~28.5pp.**
- **FRBNY published Q2 a day EARLY (8/13)**, ahead of my docket's cadence estimate.

### LAST SESSION (Fri 8/14 — the 15:30 COT window. The graded branch was a null; the pre-window hours produced three retractions of my own prior work.)

- **✅ WINDOW TASK DONE. B0 NO-VERDICT — my own pre-registered MODAL branch at 52%.** Net **−42,085** (WoW +3,388 = **+0.28 median weeks**), deep inside the 24,320 deadband; **22.4% of corrected R = −188,077**. Dual-source verified to the contract before propagation. **Frame LOW, 70,761 contracts from leg-1. The 43,053-contract prediction held — nothing came near re-arming.** I reported the null AS a null.
- **⛔ KILL SPEC #3 FIRED — and it falsified a story I had shipped.** Asset-mgr **+16,171 (1.33 wk)** vs other-rept **−14,171 (1.17 wk)**, opposite-signed past the bar. ⇒ **"One crowd, forced out together" is the wrong description of 8/7.** ⚠️ **I checked the SPEC'S REGISTERED SET before grading** — Dealer (−8,166) is *not* in {lev-money, asset-mgr, other-rept} and does not count. **Precision on which cohorts the letter names was the difference between a correct firing and a sloppy one.**
- **🔴 The companions were louder than the branch, and they agreed: OI −27,519 = 2.53× bar with net flat ⇒ LIQUIDATION.** Longs −13,040 **and** shorts −16,428. **8/7 was reversal (net +117,939 on flat OI); 8/14 is liquidation. Mirror images.** The book **emptied out** rather than re-building or flipping.
- **🔴 RETRACTION 1 — `KB-SAM-209`'s "FIMA-Funded" label.** It rested on Bessent's *"important backstop… encourage it to be upsized"* — **availability read as use.** H.4.1 foreign-official repo = **ZERO across four vintages spanning the ops**; the weekly-average column *excludes* an intra-week draw. **Had already shipped to BOND and LIQUID; both re-packeted.** ⚠️ Does **not** invert to "USTs were sold."
- **🔧 RETRACTION 2 — "the `jd` archive is DEAD" was a missing year subdirectory in my own URL.** Cost **six days and n=3 sessions**, and took SAM-39's base rate down with it. **All three ladder legs now have FINAL ACTUALS**; the Aug-3 leg I had written off as permanently unverifiable **matches Bloomberg's ~¥8.2T to the decimal.**
- **🔧 RETRACTION 3 — FRBNY "403s the default fetcher" was false;** the registered path was simply wrong (`/markets/quarterly_reports` → 302 → `/errors/404`; correct: `/markets/quar_reports`). Q2 pulled: **SOMA $18.9B + ESF $18.9B = $37.8B** — **confirming the 8/10 retraction at primary** (equal halves ⇒ one column understates ~2×).
- **Inbox fully drained (7).** WALTER's FIMA ask answered at a primary; AEOLUS's Kumamoto ask answered **"not on my radar"** with *no DETECTED repricing* stated as the weaker claim it is; BRENT's AGSI+ feed **ACCEPTED but PARKED**, reason stated.
- **STATUS compressed 266 → 251** across five historical blocks; the 8/10 item carrying the now-falsified "one crowd" claim was **marked superseded in place**, not silently deleted.

### NEXT SESSION (from 8/14)

**⚡ TIER 0:**
0a. **🔴 THE BOJ-SEP DIVERGENCE IS THE LIVE QUESTION AND IT IS ABOUT MY OWN INSTRUMENT.** ~28.5pp between own TFX/OIS (51.0%) and Polymarket (79.5%). ⛔ **The Sep/Oct blend explanation is DEAD** — Polymarket runs separate per-meeting markets and its **Oct cumulative AGREES with mine** (~85.8% vs 82.7%). **The disagreement is isolated to the September leg.** Either a real edge or a real defect in my meeting-attribution; **I cannot yet say which, and that is the point.** Known prior: +3.4bp divergence vs centralbank.watch on 8/6 — right sign, an order of magnitude too small. **Do this before citing any Sep figure.**
0b. **🕯️ SAM-41 differential check — STILL UN-RUN, third session carried.** US leg at **Treasury/FRED primary, not Yahoo**; ⚠️ US/JGB pairs are **not synchronous** (MOF lag) so 1bp precision is unearned; **base-rate the move** — 40% is judgment, not calibration.
0c. **Owed to BOND/LIQUID:** they hold a LEAD, not a finding — foreign-official UST custody **−$59.8B 7/29→8/12 after RISING into the ops**. All-foreign-official, not Japan; redemptions/custodian shifts not separable. **Do not adjudicate it for them.**
0d. **MOF weekly wk 8/2-8/8** — if still absent, that is now a real anomaly, not an Obon delay.

**⚡ TIER 1 — the successor question, deliberately NOT answered on 8/14:**
1. **🕯️ v1.8 candidate `thesis/V18_CANDIDATE_PILLAR1.md` — PROMISING MECHANISM, ZERO ACHIEVED PROGRESS.** Bar = SAM-41. ⛔ **Not a thesis; promotion needs a separate session + RED pass + Will sign-off.** **I declined to sketch a successor in the window session on purpose — a rushed successor is worse than none.**
2. **🆕 THE SECOND CANDIDATE NOW HAS ITS FIRST REAL EVIDENCE AND IT IS UNWRITTEN.** *Does a de-crowded JPY short change the distribution of future yen moves?* **8/14 says the market is not just de-crowded — it is SHRINKING** (OI −6.6% in a week, cohorts diverging). **Fuel spent is one thing; the tank being removed is another**, and the yen still sits near 159. **This is the most under-served question on my desk.**
3. **Owed to TERRY:** the "yen strengthens but BOJ does nothing" branch + exit rule. Unblocked, still not done.
4. **METSUKE apply pass** (9 flags + 3 escalations) — apply by **pattern**; watch the inverse error, Pillar 2 / oil-in-yen content is **unaffected**.

**TIER 2:**
5. **RED owes an adversarial read** on whether "composition event" is actually better supported than "one crowd," or whether I swapped one under-evidenced story for another. **Two weeks of cohort data is thin for either.**
6. **📌 KILL SPEC #3's bar is aggregate-derived** — per-cohort medians were never computed. It fired at 1.33× and 1.17×; **a per-cohort bar could move the 1.17× call.** Compute them before the test is re-used.
7. **`boj_ois.py` TFX second-source gate** — now urgent given TIER 0a.
8. **SAM-39 feed discrepancy** (yfinance 1.730y vs workbook 1.924y for 8/7) — **resolve before a session lands near 2.5y.** **SAM-28 will very likely fail at 9/18; do NOT grade it early.**
9. **BND-11:** await BOND's ratification of 4-week rolling terms. **P3-Asia Batch-3** (PROME) still un-executed.

**⛔ DO NOT:** re-arm anything on a CFTC re-build through −153K/85% (**void** — a reclaim condition inside a retired frame) · cite the `Pct_of_Jul24_Peak` TSV column as "% of peak" (**legacy −180,000 basis**; true R = −188,077) · quote **"~60.8%"** or **"~23%"** for BOJ Sep · restate a BOJ-pricing figure in prose anywhere · read a **B0** as confirmation of anything.

## Tooling — how to find out what exists

**Never assume, and never trust a hand-written list. Run:** `.venv/bin/python3 AGENTS/SAM/scripts/boot.py --tools`
Generated from `scripts/` at run time (name · boot-wired? · purpose), so it cannot go stale. Every boot also prints a tool count and **flags drift in both directions**. **Check it before building any script or doing a pull by hand** — the 8/4 BOJ-OIS failure was, at root, not knowing what already existed. *(12 tools, all boot-wired, as of 2026-08-04 — that count is a fact about that date, not a maintained figure; ask the command.)*

*(The pre-8/7 tiered block — settle Friday-vs-Monday execution · pre-compute the non-fuel re-pencil · drain the legacy inbox · verify the OIS cumulative basis · the 8/6 triple · run the resolver on the letter — is **fully spent** and was pruned 2026-08-10. Every Tier-1 item executed; full text in git history. Its one still-open infra item is carried forward as TIER 3 above.)*

**Owed / deferred:** ✅ **PROME dispositioned BOTH 8/4 asks (packet 8/4 ~17:0x, processed).** `MACHINE_LOCAL.md` recipe now carries `MESSAGING/requirements.txt` ✅; **the `env_doctor` scoping call went to DAEDALUS, not PROME** — DAEDALUS owns repo-root `scripts/` since 7/31 (Will-ruled), so **don't chase PROME for it.** `ESTAT_APPID` recorded **PRESENT** (SAM fixed it 35min after sending the packet). 🔧 **The box still missing PyYAML is `DESKTOP-BC6EF81`, NOT `WilliePOwen`** — SAM wrote "laptop" repeatedly on 8/4 and had it BACKWARDS (this box IS the laptop and is fixed); PROME independently confirmed. **State it by HOSTNAME, never nickname.** Same for `ESTAT_APPID`: desktop column is ❓UNKNOWN, `.env` is gitignored so neither restore travels — both are one command at the next machine switch) · `catalyst_countdown.py` 2027 holidays (guard is loud, dates need *sourcing*) · Aug-21 National July CPI = first **2025-BASE** print (re-baseline first; read `cpi_japan.py`'s **PAIRED** line, never **LEAD**, as "the gap") · KB-202 (KURA autonomous) · KB-152 → route Q2-actuals to BROCK/HANS · Japan-LNG/JKM · Batch-3 P3-Asia · May TIC · evals re-baseline · TB ~L394 cites a pruned "CALENDAR Jun-17 row" (provenance only).

---

### PRIOR SESSIONS — compressed (narratives → `thesis/timeline/TIMELINE.md` + STATUS pointers + git history)

- **8/10 (Mon — first boot after the break; compressed here 8/13, full text in STATUS § 8/10 + git history):** verified the 8/7 print's **cohort composition** at the TFF primary (lev-money short −42,159 · asset-mgr −38,463 · other-rept long +36,262 ⇒ **every speculative book turned at once**, ruling out a single-fund unwind); JGB cash curve independently corroborated the TFX pull-forward finding; WALTER caught a **4th-surface** BOJ-pricing staleness SAM's own two sweeps walked past. **🔴 And SAM published a "US intervention balance-sheet ceiling" at ~16:3x and REFUTED IT at ~18:0x the same session** — three distinct failure modes worth carrying: ① **read one column of a two-column table** *(having already checked the mirror-image error and stopped there — verifying the hypothesis I had did not surface the one I didn't)*; ② **relayed a substitution framing without testing it** — "FIMA vs ESF" is a **category error**, different sovereigns, killed by one sentence of the Fed's own facility page, and SAM routed it to BOND as "the highest-value open item" **without reading that page**; ③ **let a plausible constraint stand because it was flagged CANDIDATE** — the flag was honest and it worked, but **a flag is not a substitute for the check**. Retractions sent same-session. Full work → `research/outputs/US_INTERVENTION_FUNDING_ESF_SOMA_FIMA.md`.
- **8/7 (Fri — THE PRINT DAY; narrative → TIMELINE Aug 1-7 + STATUS 8/7 closeout + CHANGELOG):** frame broke, **SAM-29 + SAM-40 FAILED**, v1.6.11 → **v1.7**, book FLAT and $0 at risk. **The calibration lesson is not "I missed it":** SAM-22's mechanism (intervention → mass cover) was named **in writing on 8/2 and 8/4** as one of two ways the grade could die, then priced at **~25%** while holding a MED-HIGH grade the same document called **PROVISIONAL**. *Naming a risk and then under-weighting it is a distinct error from not seeing it.* Also that day: the v1.8 candidate written (anchor-choice trap documented), and a **near-miss** — the candidate FILE was left untracked while six surfaces shipped pointers to it *(the same index-reaches-origin-but-content-does-not shape that produced the 8/13 prediction-count defect)*.

*Compressed 2026-08-02 (older):*

- **7/31 (Fri, Will-launched LIVE BOJ DECISION WATCH — the marquee session of the cycle):** graded the MPM off the primary statement ~35 min after publication. **SAM-38 CONFIRMED at FULL-C** (hold 8-1, hawkish Takada dissent for 1.25%, overshoot-risk Outlook, FY2027 plan untouched; Oct OIS ~26-40% → ~64% on the presser) + **SAM-34 CONFIRMED** (hold @85%, 3rd straight calibrated BOJ binary). MOF monthly **¥0** → the 7/2 no-strike HARD-CONFIRMED. Buckets → 5/19/29 (v1.6.10). **Process that worked:** BOJ-site curl monitor caught publication within a minute; PDFs pdfminer-extracted; graded against frozen branches with zero re-derivation. **Contamination clause CLEAN *and it paid*** — circulating pre-dated content said "GDP 0.8%", actual FY2026 was 0.6 → fabricated-wrong, not leaked; routed to WALTER, **now generalized into its `SIGNAL_PROCESSING_CHECKLIST.md` v0.30 guard** (closes the 7/29 auto-memory candidate — WALTER owns the class, no SAM memory needed). Same session: KOYOMI clean, **METSUKE Run-12 (9 flags + 3 escalations, apply deferred BY DESIGN → still owed)**, KURA FAILED mid-run (API error, zero partial writes).
- **7/30** — 🔴 yen +2.7% intraday hours before the BOJ; suspected MOF op. VIOLET canary first-ever FIRE→WATCH (her caveat: RV cannot separate intervention from unwind); **equity vol never transmitted** (VIX −17.3% = evidence against an Aug-2024 replay).
- **7/29 · 7/23-7/16** — BOJ 4-branch pre-registration frozen; CFTC re-build to 84.5%; MOF-weekly reversal to 2 SELL weeks; SAM-35/37 CONFIRMED; Brent through $100; June TB Phase-1 inversion. → TIMELINE Jul 11-23 + Jul 24-31.


**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** ~~GPIF/pension flows~~ ✅ BUILT 7/9 (`gpif_flows.py`); fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive. *(NFP AHE MoM exact print unpinned — BLS 403s bots; curl w/ User-Agent per [[finding_edgar_403_user_agent_header]] next session if needed.)*

### NEXT INFRA SESSION (script build queue)

**Queue is EMPTY as of 2026-08-04** — the last open item (`boj_swap_pricing.py`) shipped as `boj_ois.py`. `trade_balance_japan.py` ✅ 6/10 · `gpif_flows.py` ✅ 7/9 · `boj_ois.py` ✅ 8/4. **Before proposing any new script, run `boot.py --tools`** — it lists what already exists, generated from disk. Still-deferred, non-script: `insurer_quartr.py` (Quartr watcher, needs auth), `mof_flows.py` NISA retail-flow tripwire, `boj_events.py` (SoO/speeches/minutes).
