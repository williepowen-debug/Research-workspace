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

### CHANGES SINCE LAST SESSION (Mon Jun 29 closeout → Tue Jun 30 ~10:23 AM ET boot)

- **USD/JPY 162.40 — fresh 40-yr high** (from 161.96), continued ORDERLY grind (+0.31% day, normal intraday range); MOF silent 14d at 160+. 🟠 **Market re-anchored the intervention line 160 → 162** (ING) — we now sit AT it, but orderly ≠ fire.
- JGB 10Y **2.644%** (from 2.611, MOF Jun-29 pub, drifting up). Brent $74.25 (oil-in-yen dormant). FXY $56.49.
- Wires frame the drivers as **widening US-Japan yield gap + Japan fiscal expansion → JPY as a funding currency** — converges directly on the JGB-supply thread.
- No re-entry trigger fired (SAM-28..32 quiet); within-band → carry buckets unchanged.

### LAST SESSION (Tue Jun 30 — yen-weakness read + JGB thesis EXECUTED + full "make files current" closeout; Will-directed)

- **Booted** (git clean), full boot.py sweep, refreshed STATUS market data (162.40, intervention-line re-anchor 160→162, JGB 10Y 2.644). News-verified the fresh 40-yr high (no MOF strike / rate-check — orderly grind).
- **Will: "yen continued to weaken — still no relevant trade?"** → honest **full-trade-space** read: NO compelling trade, and the weakness makes BOTH directional trades WORSE (long-yen deepens the bleed; short-yen = pennies in front of the convexity steamroller at the 40-yr-low/intervention line). Only candidate = a small optional long-vol ticket; flat is correct. Explained the level-without-catalyst / widow-maker point.
- **#2 VOL-CHECK (clean source):** the FXY proxy (16%) MISLED — true USD/JPY implied vol **~sub-10 (~7.9 Jun-23) ≈ realized** → long-vol = *defensible SMALL convexity ticket, NOT cheap-vol arbitrage* (KB-183 confirmed). Corrected my own boot-time framing in real time.
- **#1 JGB long-end DEMAND-VACUUM thesis EXECUTED** — 3 parallel primary-source Sonnet legs (BOJ reaction-function / supply / demand). Verdict: structurally bearish demand-vacuum steepener; **BOJ conditional-let-run** (pace-not-level; 2025 precedent let 30Y run +100bp uncapped); **supply = forward amplifier** (FY2026 gross super-long CUT to ¥17.4T → demand collapse, not supply glut); **30Y 4.5% = reflexive forced-selling zone**; **SIGNAL-ONLY** (no Will-tradeable vehicle). Promoted scoping→executed (`research/outputs/JGB_SUPPLY_DEMAND_THESIS.md`).
- **Routed 3 tailored signals** (Will-authorized direct-to-inbox, recipients inactive): **BOND** (primary/term-premium) / **LIQUID** (conditional — repatriation DORMANT, don't double-count Pillar 2) / **HENRY** (carry trigger 30Y-4.5%). Committed + pushed (a4329961).
- **"Make all files current" closeout (Will-directed):** THESIS **v1.6.1** (Pillar 2 deepened + 30Y-4.5% threshold + JGB-disorderly carry route + → BOND cross-link) + CHANGELOG 2026-06-30 [MINOR]; STATUS (session output + watch-triggers now SAM-28..32 + clean vol read); PREDICTIONS **SAM-32** (mechanism-based, 72%); NEXUS_BRIEF refreshed (JGB thesis + 3 SENDING rows + SAM-32 + vol). **Spawned the trio** (KOYOMI docket / METSUKE trade-doc drift / KURA KB) — proposals applied at closeout.
- **🆕 RED adversarial pass (Will-directed; Opus) → v1.6.2 correction.** RED's 5-axis sweep on the never-reviewed JGB thesis landed real hits: **one-way-street → slow grind** (CH-009: vacuum live ~13mo = orderly +56bp drift, not a break); **30Y-4.5% forced-seller CONTESTED** (CH-010 sign-tension — economic-value J-ICS argues duration-gap-closing BUYING; SAM's asset-markdown rebuttal supported by net-selling but single-sourced) + **demoted from KEY THRESHOLD** (CH-014, SAM-26 trap); **JGB-disorderly carry route → thin timing-window tail** (CH-011, BOJ truncates the disorder it needs); **regime-map not edge** (CH-012); GPIF/2nd-month/Uchida = load-bearing GAPS (CH-013); SAM-32 got a ¥/month bright line (CH-015). Demand-reduction + reconciliation + SAM-32 SURVIVE. Applied across THESIS v1.6.2 / CHANGELOG / package § RED CORRECTION / PREDICTIONS / KB-202 / STATUS / NEXUS / STRATEGY; HENRY route-correction sent; `red/` files committed. **Honest net: the JGB thesis dropped from "sharp edge" → "sound but consensus regime-map with one contested mechanism."**

### NEXT SESSION

1. **JGB demand-vacuum tests (the live thread):** Jul 7 JGB 30Y / Jul 22 40Y auctions = BTC/tail reads on SAM-32; Jul 31 BOJ FY2027 purchase-plan = the supply read. Watch 30Y velocity toward 4.5% as a *precursor* (post-RED it's a thin timing-window tail, not a clean trigger; currently ~3.76% orderly).
1b. **🆕 Resolve the CONTESTED 4.5% mechanism (RED CH-010) — the highest-value open question.** Pin the accounting basis: does the J-GAAP statutory asset-markdown (liabilities locked / AFS assets marked) dominate the economic-value J-ICS liability offset for super-long lifer behavior? This decides whether 4.5% is a forced-SELLER zone (SAM's read) or whether higher yields pull duration-gap-closing BUYING (RED's read). Observed net-selling favors SAM but it's single-sourced. Pairs with the **GPIF super-long gap** (#2) — both are the demand-leg's load-bearing unknowns.
2. **GPIF super-long stance** — the one demand-leg gap the research couldn't verify (a meaningful GPIF bid would soften the vacuum). Next pull. *(Also still open from Will Jun-15 brainstorm: GPIF/pension flows broadly, BIS yen carry beyond CFTC, Taiwan/China→Japan tail, Japan semis/AI capex.)*
3. **Watch BOND/inbox + outbox for a reply** on the JGB → US-term-premium transmission question (LIQUID = conditional cc; HENRY = carry trigger).
4. **Watch-for-entry (flat book):** SAM-28..32 = entry-triggers; don't chase the grind. Re-entry only on a fired trigger (disorderly MOF spike · CFTC through −153K/85% · risk-off yen-haven re-couple · Fed-dot walk-back · 30Y JGB 4.5% disorderly). Next CFTC **Fri Jul 3** (Jun-30 data).
5. **If Will provides FXY exit detail** (close price/date/realized P&L) → log in TRADE Entry Card + CHANGELOG (the one money fact still TBD). Otherwise FLAT-from-here stands.
6. **Carried-open:** evals re-baseline (v1.6/v1.6.1 structure changed); archive-compress the SUPERSEDED historical bodies (TRADE Options Layer / STRATEGY OPTIONS-RULES / JUN-16-RECONCILED / TAKAICHI); KURA FLOW/VX re-derivation.
7. **Auto-memory candidate (assess, don't auto-promote):** "proxy-misled-trust-clean-source" — the FXY vol proxy (16%) vs true CME CVOL (~7.9) confirmed KB-183 in real time; likely already covered by KB-183 + [[finding_pull_live_primary_not_dashboard]], so probably NOT net-new. (Prior candidate — phantom-position reconciliation — assessed clean application of [[feedback_position_cost_basis_not_authoritative]], not promoted.)

**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

**Closeout (Tue Jun 30):** boot + market refresh (162.40 fresh 40-yr low, intervention-line re-anchor 160→162) + yen-weakness full-trade-space read + #2 vol-check (clean source → long-vol = small convexity ticket, not arb) + #1 JGB DEMAND-VACUUM thesis EXECUTED (3 primary-source legs) → 3 tailored signals routed direct-to-inbox (BOND/LIQUID/HENRY; committed+pushed `a4329961`). **Then a full "make-files-current" pass (Will-directed):** JGB package promoted scoping→executed; THESIS v1.6.1 + CHANGELOG [MINOR]; STATUS (session output + SAM-28..32 trigger + vol read); PREDICTIONS SAM-32; NEXUS_BRIEF refreshed; MEMORY rewritten. Trio (KOYOMI docket / METSUKE TRADE-STRATEGY drift / KURA KB) spawned + proposals applied. Auto-push at closeout.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
