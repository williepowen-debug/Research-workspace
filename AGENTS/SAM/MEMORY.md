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
- *(Promoted to auto-memory Jun 10: [[finding_ohlc_verify_before_session_claims]], [[finding_pre_registration_discipline_through_corroboration]] — Advisor-endorsed, Will-forwarded; veto = delete files + index lines.)*

*Calibration / process lessons live in auto-memory: see [[finding_threshold_vs_mechanism]], [[feedback_audit_behavioral_ranking]], [[feedback_doc_routing_data_drops]], [[finding_followup_audit_pass]], [[finding_shallow_clone_false_fork]], [[feedback_position_cost_basis_not_authoritative]], [[finding_thin_liquidity_prediction_market_discipline]], [[finding_subagent_baseline_audit]], [[finding_teams_mode_iterative_tasks]].*

## References
- Primary data sources + scripts: see `CLAUDE.md` boot step 7 (canonical list).
- Vol/options: CME CVOL (JPVL) license-gated; FXY proxies auto-pulled (caveat KB-183 — read sign not level).

## Session Notes

### CHANGES SINCE LAST SESSION (Sun Jun 14 ~12:45 PM ET → Mon Jun 15 ~7 PM ET)

- **Market:** Brent $87.33 → **$83.33** (deeper sub-$90/sub-$85; de-escalation pricing extending). JGB long-end −~10bp (10Y 2.589 / 30Y 3.725 / 40Y 3.674; SAM-26 further FALSE). USDJPY/FXY flat (160.15 / $57.24; 8th orderly day at 160, no MOF). **FXY 25d RR reverted +24.05 → −8.37** (Sun non-physical artifact GONE — validates Sun HENRY caveat); ATM IV bled 12.49 → 10.28. No new CFTC (Jun 9 −145,818 stands to Fri).
- **News (Mon sweep):** **US-Iran signed a DIGITAL MOU Jun 14-15, Iran CONFIRMED** (closes the Sun "not confirmed" gap); formal signing ceremony **Fri Geneva**; conflicting terms ($25B frozen-asset release vs Trump "no money") = re-break risk into Friday; Hormuz authorized-but-no-tankers-yet. **BOJ confirmed-quiet** (Polymarket 99%, no dovish leak; Uchida runs presser — Bloomberg "set for historic hike"). US **Empire State miss** (5.7 vs 13.2), DXY soft 99.56. Polymarket Fed-2026-hike scraped **~36%** (single-print vs Sun ~52% — re-check at FOMC, thin-liquidity discipline).

### LAST SESSION (Mon Jun 15 PM — boot + 3 research threads; all committed & PUSHED, origin synced @ 30b729ca)

- **Boot + reconciliation:** SAM-21 **75 → ~90 (CH-009)** propagated into canonical PREDICTIONS.tsv (caught STATUS↔PREDICTIONS drift); STATUS Mon market table refreshed. Per Will: **Iran docket update DEFERRED (wait-and-see)** — see NEXT #5.
- **3 research threads built + persisted** (detail lives in the files, not recapped here):
  1. **Japan energy complex** — KB-187–190, `research/outputs/JAPAN_ENERGY_COMPLEX.md`, THESIS § OIL-IN-YEN. Japan SPR ~205d (vs 254 baseline); energy shock severs PPI→CPI (transmits **FISCAL not monetary** → Pillar 2); oil-shock-not-grid-shock (oil ~96% ME / LNG ~11% / coal 0%).
  2. **SoftBank-OpenAI** — KB-191/192, `research/outputs/SOFTBANK_OPENAI_RISK.md`, THESIS RISK FACTORS row, outbox flag → CARL/HENRY/BROCK. NOT a UST/JGB holder (equity holdco/bond issuer); **risk-off cross-current** (yen-UP / JGB-yield-DOWN / BOJ-pause-cover tail); Jun-10 $6B OpenAI-margin-loan stalled.
  3. **NISA + bank/BOJ duration** — KB-193/194, THESIS § STRUCTURAL COUNTER-FLOW + RISK FACTORS non-constraint, CALENDAR RETAIL FLOW MONITOR, mof_flows.py infra item. **NISA = "right but early" steelman + latent unhedged amplifier** (tripwire: MoF toshin → net foreign-equity selling); **bank/BOJ duration NOT the BOJ brake** (it's fiscal).
- **3 commits pushed** (Will-opened window): 576ab73d / 9ea1a7cb / 30b729ca. Pull-rebase clean (origin hadn't moved); push carried only SAM work.
- **Position UNCHANGED, marks FROZEN (blackout).** Money fields untouched (13 sh @ $58.32, $58C, $55.05 post-event stop, $798). METSUKE NOT spawned — additions were research-reference, not position/mark moves (TRADE/STRATEGY not staled).

### NEXT SESSION

**Imminent (BOJ tomorrow Tue Jun 16 = 1 trd day):**

1. **🔴🔴 Tue Jun 16 BOJ MPM** — apply pre-registered frames, don't re-derive:
   - STRATEGY § JUN-16 RECONCILED EXPECTATION ~80/10/10 (modal −1 to +2% + vol crush; hawkish-of-pricing ~10% = +5-8%; hold ~10% = −3-5% event-capped). Sell-into-pop on the **Tuesday IV spike itself**; Uchida-presser muddiness = don't wait for clean post-presser repricing.
   - STRATEGY § TAKAICHI-CEILING DISCOUNT DISPOSITION (3 branches CH-010 + C1/C2 split), score by Jun 18 EOD JST.
   - $58C tail-estimate test (market ~3-4% vs SAM ~10%) — score Tue.
   - **Ueda-attribution check:** a hold via Uchida dovish-cover ≠ Branch C1 (Takaichi-political) ≠ C2 (fiscal/long-end); Apr-13 Himino precedent informs.
   - SAM-21/23/24/26 resolve on own terms.

2. **🔴 Wed Jun 17 FOMC + dots** — ~99% no-change; watch dots for HIKE-lean (regime-flip confirm), not rescue. **Re-check Polymarket Fed-2026-hike 36% vs 52% discrepancy.**

3. **🔴 Wed Jun 17 (~7:50 PM ET Tue eve)** — **May trade balance**; run `trade_balance_japan.py --consensus <wire>`; adjudicate branch a/b/c (diplomacy + Hormuz-still-closed → bias branch c). Now also reads through the energy-complex **cost-side** lens (KB-188-190: pricier non-ME crude).

4. **🔴 Thu Jun 18** $58C expiry; **Fri Jun 19** National May CPI. Post-settle: v1.6 re-underwrite (incl. FXY-vehicle question).

**Carry-forward (post-BOJ):**

5. **Iran docket update (Will-DEFERRED Mon Jun 15, wait-and-see):** when ready, supersede stale "Iran has NOT confirmed" caveat (Iran confirmed Jun 14-15) + add Fri Geneva signing if it lands.
6. **v1.6 rewrite** per `proposals/2026-06-10_v16_rewrite_spec.md` (post Jun 16-18 scoring; RED pass on draft pillars first). Fold in: oil-channel-DORMANT relabel; energy transmission-severing; SoftBank tail; **NISA amplifier → CARRY-UNWIND METHOD enrichment** (residual/2nd-order term); Channel-1 deferred-vs-retired (4-of-4 + Feb-2026 regulatory-forbearance reinforcement). + A. position re-underwrite + B. PROME network-reframe + C. hedge-cost tripwire. Eval re-baseline; OS.1 close; Dec-1.25% re-verify if Branch A fires.
7. **SAM-23 framework re-anchoring CHANGELOG entry** (post-scoring; CH-011 driver/disorder + no-strike decay + Jun-14 empirical 6+ orderly-sessions cites).
8. **RED post-BOJ refresh** — hold-scenario; structural-pillar TIMING under CH-032 band; SAM-23 post-event anchor; Fed-hike → CH-005.
9. **Research backlog (Will-brainstorm Jun 15, Tier 2/3 un-pulled):** GPIF/pension flows; fiscal/Takaichi trajectory + JGB supply; digital deficit; BIS yen carry (beyond CFTC); Taiwan/China→Japan tail; Japan semis/AI capex.
10. **Auto-memory candidate (Sun Jun 14, Orc-endorsed):** "a cross-agent caveat protects you not the receiver — suppress a non-physical/known-unreliable metric, don't caveat-and-ship." + KB-183 local refinement ("at non-physical magnitudes the magnitude impeaches the sign too"). Authorize at next boot.
11. **Position next-touch:** no add/trim under v1.5.1. Triggers: (a) USDJPY <156 ×3 sessions; (b) post-Jun-16 break = BOJ dovish AND USDJPY 167+/no MOF. NEXUS_BRIEF rollout = Will-action.

**⏸️ DEFERRED:** Layer B cross-agent (BROCK/HANS PC-cascade pull); KB cleanup tier-2; insurer profiles audit; Japanese-source pipeline retire; SIGNAL_INTAKE archive.

### NEXT INFRA SESSION (script build queue — re-prioritized Jun 10)

1. ~~`trade_balance_japan.py`~~ — **✅ BUILT Jun 10 PM** (selftest 6/6; 14-mo backfill; boot.py-wired with fast-exit; spec = Orch 4 gaps + SAM 3 refinements, see MAINTENANCE 6/10 PM). **Found: May TB provisional = Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16, BOJ evening ET) — docket said Jun 18, corrected.** On print evening: run with `--consensus <wire ¥B>`; routing suggestion prints, SAM adjudicates branch.
2. **`insurer_quartr.py`** — Quartr watcher for Big 3 + Norinchukin + mid-tier. ~45-60 min + auth. **🔺 PRIORITY BUMPED (Will-directed Jun 10): third coverage-gap instance this week** (Jun 9 PPI/taper-pause slipped past WALTER; Jun 10 Norinchukin FY2025 surfaced 3 weeks late — results were public May 21, IR HTML 403s hid them; direct-PDF probing or Quartr feed would have caught it). Build right after trade_balance.
3. **`mof_flows.py` enhancement — NISA retail-flow tripwire** (per KB-SAM-193 / CALENDAR RETAIL FLOW MONITOR, added Jun 15): the weekly MoF ITS CSV already pulled for LT-debt net carries the sector breakdown — extend the parser to also extract + alert on the "investment-trust mgmt cos" foreign-equity line flipping to net SELLING (regime-change tell; the modal "right but early" steelman + latent carry amplifier). ~30-45 min.
4. **`boj_events.py`** — BOJ Summary of Opinions + speeches + MPM minutes. ~45 min. Next SoO ~Jun 26.
5. **`boj_swap_pricing.py`** — re-recon Polymarket/Kalshi. 10-min recon, build only if source exists.

Also deferred (low priority): per-insurer profiles retire-vs-refresh; `research/` reorg; SIGNAL_INTAKE.md refresh (pending messaging overhaul).
