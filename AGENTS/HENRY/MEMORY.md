# HENRY MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis, STATUS, or LESSONS and delete, never just accumulate.*

*Audience: next HENRY instance. For Will-facing session closeout see `LAST_COMPLETION.md`.*

---

## Feedback

- [2026-04-17] Always pull fresh EOD levels before closing the week — partial retracements during the session are the tell.
- [2026-04-17] When a file-system cleanup proposal touches a system-wide convention, present options and recommendation, don't just execute.
- [2026-05-21] **Literal triad-count framing, not trajectory framing.** Per Will-authorized framing-precision note: when invalidation criteria use a literal threshold ("HY OAS <260 sustained"), the count must use the literal threshold ("not fired"), not the trajectory ("approaching firing"). "2 of 3 firing" invites a RED audit on the third leg. Use "1 fired + 1 compressing + 1 flat." Keep "trap clinching vs soft kill" conceptual distinction verbatim — that's the cleanest mental model on this thesis.
- [2026-05-21] **Replace bare triad-watch with tape/substance divergence metric** as primary conviction signal. Track tape side (cushion-from-kill across HY OAS/VIX/SPX) vs substance side (CPI/PPI/credit marks/bank tape/duration). Direction of resolution (which side closes the gap) is the actionable read; the triad alone is binary-ish.

## Findings

- [2026-04-17] When oil shocks reverse on unilateral headlines, regional-bank beta (KRE, APO) gives back most of the AM rally by close — the "conviction" bid is small vs the beta bid.
- [2026-04-17] SAM's closeout structure (CHANGES SINCE / LAST SESSION / NEXT SESSION in MEMORY.md) is the leanest working pattern in the codebase.
- [2026-05-21] **Surface decisively fading a "loaded" catalyst is the most consequential vol-structure read.** NVDA 5/20 was the most-watched AI catalyst of the cycle; pre-print SPX call notional record + SOX RSI 1999-high + defensives -2z = max-loaded setup. Outcome: SKEW dropped out of 140+ regime first time in 223+ td (138→132), VIX9D crushed below 15 for first time of regime, VVIX back to Apr 17 level. Three vol-surface tells, all "no catalyst expected, no pre-event hedging." Trap-clinch lens implication: the next regime-shift catalyst is unlikely to come from HENRY-domain calendar in 0-30d. HENRY's job pivots catalyst-anticipation → drift-monitoring.
- [2026-05-21] **Credit widening on a clean AI beat is a cross-asset tell.** HY OAS +6bps from cycle min 276 to 286 over 5/17-21 window while NVDA print was a clean beat. The bid that should have re-tightened credit on a risk-on catalyst is missing. CCC +13bps over same window confirms quality bifurcation deepening. The credit underlying-substance is firming wider bias regardless of catalyst direction — meaning credit is now contributing to the substance-side acceleration, not the tape-side absorption.
- [2026-05-21] **HENRY-VIOLET LIAISON resolved same day — R11 clock activates on R12 termination, doesn't deactivate.** Initial HENRY hypothesis after seeing SKEW drop out of 140+ was "R11 weakens post-NVDA." VIOLET first-pass corrected: R12 SKEW>140 regime DID terminate (4/5 closes <140, low 132.31), but **regime termination ACTIVATES R11 analog clock** (window 5/28-6/02, prior 36%) rather than deactivating it. Vol-spike pathway is LIVE not dead — conviction-via-vol-spike RE-CONFIRMED with lower prior. Pattern lesson: regime-end ≠ pathway-end; the analog library may have post-regime-termination forward-looking probability that the HENRY-side first-pass missed.
- [2026-05-21] **VIOLET methodology correction: metric label was wrong, direction-call was right.** The 5/13 "20d-SKEW-slope SIGN-FLIPPED -1.0" was actually `final_5d_change` (a 5-day delta), not a 20d regression slope. HENRY uses `final_5d_change` terminology going forward. Pattern: cross-agent metric labels need verification before propagation — substantive call survived because direction was right; risk would have been if HENRY had used "20d-slope" Will-facing and a RED audit pulled the metric definition.
- [2026-05-21] **Revival-proxy framing-precision overlay is a useful artifact.** The Prome-spawned 5/18 revival packet drafted "2 of 3 firing"; Will + Prome reviewed and added a framing-precision overlay correcting the literal count without rewriting the packet. Both layers preserved in inbox/processed/. Pattern is reusable: when a sub-agent or proxy gets the concept right but the literal claim overspecified, the overlay note + processed/ retention is cleaner than re-spawn or silent edit.
- [2026-05-21] **LIAISON-channel-open within session resolves shared-canary questions fast.** HENRY surfaced VIOLET LIAISON ask ~13:00 ET; VIOLET first-pass back same session ~14:00 ET; integrated into HENRY STATUS by ~14:30 ET. ~90 min cycle for cross-agent canary reconciliation. Pattern: when HENRY surfaces a question dependent on VIOLET's territory (or vice versa), opening LIAISON immediately (not at next session boundary) compresses cycle by an order of magnitude.
- [2026-05-21] **Breakeven decomposition = independent confirmation channel for Fed-can't-cut.** BOND TIPS 5/21 (commit `724169c3`): real 2.169% + nominal 10Y ~4.60% = breakeven ~2.43% (FRED T10YIE 2.49→2.44 on 5/19→5/20). Real yields rose, breakeven did NOT — duration repricing is term-premium / Fed-pinned driven, not reflation-driven. Pairs with HEN-27 PCE Core 3.20% YoY CONFIRMED as two independent reads: substance hot + bond market pricing Fed-pinned. When surfacing the substance leg of trap thesis, look for the bond-decomposition cross-read — cleanest independent confirmation because it triangulates from a different market.
- [2026-05-21] **Auction-demand reads soften R11 substance-trigger imminence even when proximity is intact.** BOND 5/21 TIPS: BTC 2.52 = 100th pctile / direct 27.51% = 92nd pctile; with 5/20 nominal 20Y clean = 2 consecutive clean long-end auctions. Verdict: "long end clearing demand at price — expensive, not broken." Lesson: proximity (10Y 8-15bps below 4.75% R11 trigger) vs imminence (real-money absorbing supply) are separable. Track auction-tail dynamics + cover ratios alongside yield level — when real-money cover is at cycle highs, the trigger is harder to fire even when yield level looks close. Cross-domain: BOND owns auction read; HENRY owns regime read; cross-reference before HENRY treats substance-trigger proximity as imminent-firing.

## References

- [2026-04-17] Live market refresh: `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price ^GSPC ^VIX ^SKEW ^VIX3M KRE JPY=X ^TNX TLT APO HYG LQD BZ=F CL=F`. `SPX`/`VIX` alone fail — use `^GSPC`/`^VIX`.
- [2026-04-17] HY OAS daily refresh: FRED series `BAMLH0A0HYM2`, 1-day lag.
- [2026-04-17] `workbook/MARKET_DATA.tsv` is the sparse EOD snapshot log.
- [2026-05-21] **Cross-source-tier discipline:** for vol/SPX/NVDA-tier metrics, yfinance fetch.py is HENRY-primary. For macro/credit/bank-tier (HY OAS, CCC OAS, Brent, USD/JPY), pull from BROCK/LIQUID STATUS or Prome dashboard (the Prome dashboard does not carry HENRY-tier vol metrics — that's a tier-mismatch the proxy flagged in v2 packet).

---

## Session Notes

### CHANGES SINCE LAST SESSION
- 34-day dark window Apr 17 → May 21. Three revival-proxy files (5/18) integrated this session.
- Trap-clinching framing now canonized in BROCK STATUS 5/21 ("Sister revivals integrated by reference: ... HENRY 2026-05-18 — complacency-trap clinching; framing-precision literal-vs-trajectory") — concept propagated cross-agent.
- LIQUID 5/18 reframe: PLUMBING → DURATION channel migration (active transmission channel shifted from funding stress to term-premium / fiscal repression).
- REGINALD V2.2 today (5/21): WAL Bear-medium 30% dominant (Bear-fast only 12%), EV $67.98, 14% overvaluation vs current $77.96. $99M life-science office walk-away (10-Q subsequent event, B1 fired) + Curley resignation same week.
- NVDA 5/20 print: clean beat, no tone-shift catalyst, vol surface decisively faded (SKEW 138→132, VIX9D 16.86→15.02).
- BROCK Stage 2 APO trigger entrenched (sustained >$130 13+ sessions); broad-thesis HY OAS widening from 260 kill (276 cycle min → 286).

### LAST SESSION (2026-05-21 Wed mid-day-to-PM — Session 1 of revival; 3-arc continuation)

**Session arc summary (audience: next HENRY):** Single multi-arc continuation session. Three commits, all pushed:
1. `15f450b1` — Revival + STATUS rewrite + NVDA read-through + VIOLET LIAISON integration
2. `36a8219b` — Gap-fill (USD/JPY pull + HEN-27 PCE scoring + HEN-28 claims + PREDICTIONS.tsv refresh)
3. `526d3586` — BOND TIPS integration (R11 imminence softened + breakeven decomp as 3rd Fed-can't-cut confirmation channel)

**Net state at close:** trap-clinching thesis with 3 independent Fed-can't-cut confirmations (PCE Core 3.20% YoY CONFIRMED + LIQUID duration reframe + BOND breakeven decomposition). R11 analog clock running 5/28-6/02 (prior 36%) per VIOLET LIAISON; 10Y substance trigger proximity intact but imminence softened by BOND auction-demand reads. R12 SKEW>140 regime terminated 5/18-5/20.

**Detail (arc 1 — revival + LIAISON):**
- **Inbox cleared (18 → 0).** Revival packet + draft STATUS + framing-precision note integrated. 15 signal/sweep files moved to processed/ via git mv. 8 LIVE absorbed into STATUS narrative; 7 archived (per revival packet §5 triage — items 11-15 + 8 + 9).
- **STATUS rewrite.** Apr 17 → May 21. New status header (TRAP CLINCHING), live tape table with Δ vs 5/18 and Apr 17, vol regime block updated (VIX9D <15, SKEW out of 140+), literal triad-status table (1 fired + 1 compressing + 1 flat per framing-precision overlay), tape/substance divergence metric replaces bare triad watch, thesis state with confirmed/counter/counter-evidence/vol-spike-pathway sub-sections, soft-kill vs trap-clinch invalidation reframe, updated thresholds with kill-watch sub-rows, May-Jun catalyst stack, predictions table (HEN-29 scored partial disconfirm), updated cross-agent dependencies (BRENT direction FLIPPED 5/21 — sustained >$100 NOW CONFIRMS, sustained <$85 inverts to soft-kill watch).
- **NVDA 5/20 read-through one-pager** filed at `research/NVDA_5_20_READ_THROUGH_2026-05-21.md`. Vol structure context + options market signal + broader regime tell + drafted cross-agent sends (VIOLET, LIQUID, PROME).
- **Position read for Prome:** Macro/structure tape SUPPORTS trap-clinching + REGINALD V2.2 Bear-medium 30%. Push-back surface limited to: (1) WALTER 5/13 bull-counter signals (SIG-006 small/mid-cap discount + SIG-007 retail-puts-at-SPY-ATH) deserve calibration weight; (2) HENRY's "R11 weakens post-NVDA" hypothesis was half-right (corrected in arc 1).

**Detail (arc 2 — VIOLET LIAISON resolution + gap-fill):**
- **VIOLET LIAISON resolved same session (~90 min cycle).** R12 SKEW>140 regime terminated 5/18-5/20 confirmed; R11 analog clock ACTIVATES on termination (window 5/28-6/02, prior 36%) — HENRY's "R11 weakens" hypothesis was half-right; regime-end ≠ pathway-end. 7-trigger Stage 3 watch list integrated into cross-agent dependency table. Metric label correction: `final_5d_change` not "20d-slope" going forward.
- **Gap-fill batch (Prome relay):** USD/JPY 159.16 (+0.23 vs 5/18 packet; 0.84 handles from 160 yellow trigger); HEN-27 PCE March CONFIRMED via core YoY +3.20% (>3.0% threshold; MoM +0.293% just under 0.3% but OR-trigger met); HEN-28 labor cliff NOT-FIRING on headline (ICSA 4-wk avg 202.5K, single-week 209K) — shadow-adjusted ~266K firing via WALTER 5/13 BAA series; PREDICTIONS.tsv refreshed HEN-22 through HEN-31.

**Detail (arc 3 — BOND TIPS integration):**
- **BOND TIPS 5/21 read** (commit `724169c3`) integrated as 3rd Fed-can't-cut confirmation channel.
- **R11 trigger #6 (10Y) imminence SOFTENED:** BOND live intraday 10Y 4.599-4.635 = 15bps below 4.75% trigger (not 8bps from FRED 5/19 DGS10 print). 2 consecutive clean long-end auctions (5/20 nominal 20Y + 5/21 TIPS BTC 2.52 = 100th pctile / direct 27.51% = 92nd pctile) → "long end clearing demand at price — expensive, not broken." Proximity intact, imminence reduced.
- **Breakeven decomposition:** TIPS 2.169% real + nominal ~4.60% = breakeven ~2.43% (FRED T10YIE 2.49→2.44 on 5/19→5/20). Real yields rose, breakeven did not. Duration repricing is term-premium / Fed-pinned, NOT reflation-driven. Independent confirmation of HEN-27 PCE-CONFIRMED Fed-can't-cut via bond-decomposition angle.

**Cross-session lessons added to Findings (this MEMORY pass):**
- R11 clock activates on R12 termination, doesn't deactivate (regime-end ≠ pathway-end)
- VIOLET metric label correction (`final_5d_change` not "20d-slope")
- LIAISON-channel-open within session = ~90 min cycle for cross-agent canary reconciliation
- Breakeven decomposition = independent confirmation channel for Fed-can't-cut framing
- Auction-demand softens R11 substance-trigger imminence even with proximity intact (proximity vs imminence are separable; cross-reference BOND auction-tail dynamics before treating yield-level proximity as imminent-firing)

### NEXT SESSION
1. **🟠 R11 analog window 5/28-6/02** — 7-trigger Stage 3 watch (VIOLET surface side; HENRY substance side). Current proximity: 10Y closest (8-15bps depending on FRED-vs-live framing), HY 4bps, CCC 52bps. Imminence softened by BOND auction-demand 5/20+5/21 reads — watch auction-tail dynamics alongside yield level for next 20Y/30Y/10Y prints.
2. **🟢 Daily HY OAS** — watch for sub-265 ×2 sess (HEN-30 leading invalidation tell). Currently 286, moving wrong way.
3. **🟡 Inbox arrival to process:** `SIG-PROME-HENRY-2026-05-21_fred-citation-convention.md` (Prome FRED citation convention — deferred this session per closeout holds).
4. **🟡 WAL 10-Q drill closeout** (REGINALD V2.2). Watch KRE/WAL beta into Q2 (late Jul second migration test).
5. **🟡 BDC tail prints** (GCRED/OTF/BCRED/CTAC late May / early Jun, BROCK-primary; HENRY watches credit-tape reaction).
6. **🟡 PCE Apr release** when scheduled — Fed framework test.
7. **🟢 Workbook updates** — KB.tsv entries pending for gamma/momentum-suppression hypothesis + duration regime break + AI capex air-pocket + tape/substance divergence metric + breakeven-decomposition-as-confirmation-channel. (PREDICTIONS.tsv done arc 2.)

### GAPS — PERSISTENT
- **0DTE SPX share + GEX regime** STATUS PENDING. 4+ sessions deferred. NVDA passed; less urgent now but still a HENRY gap. Manual estimate acceptable.
- **VX.tsv 11 STALE Jan/Feb rows** — refresh or archive.
- **KB.tsv** — 5 entries pending from today's session (see NEXT SESSION #7).

### RESEARCH QUEUE (current priorities — pruned 5/21)
1. **Historical cascade fired-vs-aborted cases** — NVDA 5/20 added as case study. **Promoted.**
2. **NVDA post-print transmission tracking** — daily SMH/AVGO/AMD vs NVDA; AI capex air-pocket transmission firing incrementally vs needing fresh catalyst?
3. **Structural bid decomposition** — gamma/momentum suppression (5/14 signal) framework; quantify $/day mechanical bid.
4. **Regional bank credit-vs-margin playbook** — sharpens WAL/KRE read post-V2.2.
5. **Credit-vol decoupling phase tracker** — complements VIOLET LOW_VOL framework.
6. **GEX wire-up decision doc** — backlog.

### INFRASTRUCTURE CHANGES (persistent)
- 5/21: Tape/substance divergence metric replaces bare triad watch (Feedback). Revival-proxy framing-precision overlay pattern documented (Findings).
