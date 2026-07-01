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

### CHANGES SINCE LAST SESSION (Tue Jun 30 closeout → Wed Jul 1 ~11:32 AM ET boot)

- **JGB long-end BEAR-STEEPENED** (MOF Jun-30 pub): 2Y −3bp (anchored) while 20/30/40Y +8-11bp → **30Y 3.873%, ~13bp below 4.0%** (+11bp/2pubs), 10Y 2.690%. Still GRADUAL (~8bp/day). The demand-vacuum thread on the tape.
- **Tankan Q2 +22** (beat +16, highest since Mar-2018, firms lifted inflation expectations — mild hawkish) + **JGB 2Y auction BTC 4.82x/tail 0.3bp** (strong; front-end fine — confirms super-long-specific vacuum). Both confirmatory.
- USD/JPY 162.43 (40-yr-low zone, ≈flat vs 162.40; MOF silent 15d). Brent $71.37 (down further). CFTC unchanged (Jun-23; next print Fri Jul-3).
- No re-entry trigger fired (SAM-28..33 quiet); within-band → carry buckets unchanged.

### LAST SESSION (Wed Jul 1 — bear-steepener action-review + JGB→US transmission map + closeout write-back; Will-directed)

- **Booted** (git clean), full boot.py sweep + live fetch, refreshed STATUS market tables. Flagged the 30Y drift toward 4.0% as the notable development.
- **Will: "what to do about the bear-steepener?"** → **multi-lens action panel** (trade / prediction / cross-agent + act-now adversary): unanimous **HOLD**. No Will-tradeable JGB vehicle (signal-only); gradual move fires no carry-tail trigger; pre-positioning fails deploy-on-trigger + break-even-MEDIUM. Adversary's best case (small premium-only long-vol on the unwind-speed asymmetry) didn't clear — negative EV not cured by defined-risk + vol not cheap (KB-183). Decision nodes = **Jul-3 CFTC + Jul-7 30Y auction**.
- **Will: "how does it transmit to the US?"** → built the **JGB→US TRANSMISSION MAP** (multi-agent gather: live US levels + BOND/LIQUID/HENRY state + adversarial synthesis). **Finding:** transmits **DIFFUSELY via correlated global term premium, NOT repatriation** (Japan a net UST buyer; **US 30Y 4.96% co-moving up** on a shared driver, softer US ground — ACM term premium +0.73%; VIX 16/MOVE 68 calm). Ch D (capital export) = only live flow, risk-positive tailwind; tail = disorderly JGB break dragging US long end via correlation alone. Persisted → package § US-TRANSMISSION MAP.
- **KEY cross-agent finding: BOND/LIQUID/HENRY have NOT processed SAM's Jun-30 JGB signals** (all unprocessed inboxes; STATUS files predate them) → corroboration = convergent priors, not integration. **Will spawning BOND/LIQUID/HENRY today** — they'll consume the refreshed NEXUS_BRIEF + package.
- **Closeout write-back (Will asked "are files current?"):** package § US-TRANSMISSION MAP + PUNCHLINE marks; NEXUS_BRIEF (transmission + BOND sharpened-Q + **drift true-up: v1.6.1→v1.6.2, 5→7 OPEN [SAM-33/34], marks**); STATUS 7/1 note; THESIS → BOND pointer; TIMELINE Jul-1 line; CHANGELOG 2026-07-01; CALENDAR (2Y auction + Tankan RESOLVED). No thesis/position change (FLAT, v1.6.2 stands). *(No METSUKE/KURA/KOYOMI spawn — no money-doc or KB move; docket true-up done inline.)*

### NEXT SESSION

1. **JGB demand-vacuum tests (the live thread):** **Jul 2 JGB 10Y** · **Jul 7 30Y / Jul 22 40Y** = BTC/tail reads on SAM-32; Jul 31 BOJ FY2027 purchase-plan = supply read. **30Y now 3.873%, ~13bp below 4.0% at ~8bp/day** — watch velocity toward 4.0/4.5% as a *precursor* (post-RED a thin timing-window tail, not a clean trigger). A weak/failing 30Y/40Y auction (BTC toward/below ~2.0x) is the real B/C **US-transmission** trigger → would warrant a fresh BOND/HENRY signal.
1b. **Resolve the CONTESTED 4.5% mechanism (RED CH-010) — highest-value open question.** Pin the accounting basis: does the J-GAAP statutory asset-markdown (liabilities locked / AFS marked) dominate the economic-value J-ICS liability offset for super-long lifer behavior? Decides forced-SELLER (SAM) vs duration-gap-closing BUYING (RED). Net-selling favors SAM but single-sourced. Pairs with the **GPIF super-long gap** (#2). *(Note: this ALSO decides whether repatriation Ch A can level-reverse — if lifers return to JGBs at 4.5%+ funded by trimming US holdings, that IS repatriation re-arming.)*
2. **GPIF super-long stance** — the one demand-leg gap the research couldn't verify (a meaningful GPIF bid softens the vacuum). Next pull. *(Also still open from Will Jun-15 brainstorm: GPIF/pension flows broadly, BIS yen carry beyond CFTC, Taiwan/China→Japan tail, Japan semis/AI capex.)*
3. **🆕 Peers spawning today (Will) — watch for BOND/LIQUID/HENRY processing the Jun-30 signals + reacting to the transmission map.** BOND (primary) is the one to watch: sharpened Q now on record in NEXUS + package — *does a disorderly JGB break transmit to US term premium via correlation, given ACM +0.73% + thin dealer backstop?* If BOND replies, integrate + consider a routing update. (Do NOT re-send — signals already in their inboxes.)
4. **Watch-for-entry (flat book):** SAM-28..33 = entry-triggers; don't chase the grind. Re-entry only on a fired trigger (disorderly MOF spike · CFTC through −153K/85% · risk-off yen-haven re-couple · Fed-dot walk-back · 30Y JGB 4.5% disorderly). Next CFTC **Fri Jul 3** (Jun-30 data; ~7K/3.8pp below the −153K/85% reclaim line). **7 OPEN.** ⚠️ **SAM-34 action: re-verify July-hike pricing (swaps/Polymarket) by mid-July; re-mark if >40%** (Tankan +22 beat is a mild hawkish nudge — check, don't shade). **US-transmission tells to watch:** US 30Y >5.0 / 10Y >4.6 · MOVE >80 · JPY-up+DXY-down+SPX-down triad.
5. **If Will provides FXY exit detail** (close price/date/realized P&L) → log in TRADE Entry Card + CHANGELOG (the one money fact still TBD). Otherwise FLAT-from-here stands.
6. **Carried-open:** evals re-baseline (v1.6.x structure changed); archive-compress the SUPERSEDED historical bodies (TRADE Options Layer / STRATEGY OPTIONS-RULES / JUN-16-RECONCILED / TAKAICHI); KURA FLOW/VX re-derivation.
7. **Auto-memory candidate (assess, don't auto-promote):** 🆕 **workflow "adversary/refute" agent tripped a spurious AUP content-filter** (the "stress-test SAM's read / argue against" framing) → agent errored, ran the adversarial pass in the main loop instead. Transferable workflow finding: adversary/red-team subagents can hit a false-positive block; frame as "identify weaknesses/verify" rather than "argue against," and keep a main-loop fallback. Likely net-new (not covered by existing workflow findings). *(Prior candidate "proxy-misled-trust-clean-source" = already covered by KB-183 + [[finding_pull_live_primary_not_dashboard]], not promoted.)*

**Research backlog (Tier 2/3 un-pulled, Will Jun-15 brainstorm — still open):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

**Closeout (Wed Jul 1):** boot + market refresh (JGB bear-steepener 30Y 3.873% toward 4.0% orderly; Tankan +22 beat; 2Y auction BTC 4.82x strong; USDJPY 162.43) + **bear-steepener action-review = HOLD** (multi-lens panel + adversary) + **JGB→US TRANSMISSION MAP built** (diffuse-via-term-premium, NOT repatriation; US 30Y 4.96% co-moving; peers haven't processed Jun-30 signal). **Then a "make-files-current" write-back (Will asked):** package § US-TRANSMISSION MAP; NEXUS_BRIEF (transmission + BOND sharpened-Q + drift true-up v1.6.1→v1.6.2 / 5→7 OPEN); STATUS 7/1 note + tables; THESIS → BOND pointer; TIMELINE Jul-1; CHANGELOG 2026-07-01; CALENDAR (2Y+Tankan RESOLVED); MEMORY rewritten. No thesis/position change. Auto-push at closeout.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
