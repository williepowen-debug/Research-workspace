# HENRY MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis, STATUS, or LESSONS and delete, never just accumulate.*

*Audience: next HENRY instance. For Will-facing session closeout see `LAST_COMPLETION.md`.*

---

## Feedback

- [2026-04-17] Always pull fresh EOD levels before closing the week — partial retracements during the session are the tell.
- [2026-04-17] File-system cleanup touching a system-wide convention → present options + recommendation, don't just execute.
- [2026-05-21] **Literal triad-count framing, not trajectory.** Invalidation criteria with literal thresholds ("HY OAS <260 sustained") must be counted literally ("not fired"), not by trajectory ("approaching"). Use "1 fired + 1 compressing + 1 flat." Keep "trap clinching vs soft kill" as the conceptual mental model.
- [2026-06-03] **Decompose ratios into numerator vs denominator before assigning weight.** CCC/HY "widened to 3.48x" was mostly the HY denominator compressing (286→272), not CCC blowing out (948→946 flat). State it as levels ("tail didn't follow index tighter"), not a ratio that overstates tail stress. Don't let a ratio carry weight its components don't earn.
- [2026-06-03] **Verify gate/catalyst dates against source — especially load-bearing ones.** Wrote "6/12 May CPI"; actual is 6/10 (BLS, and my own ECON_CALENDAR had it right). The whole duration gate keys off that date. Check BLS/source, don't trust recall.
- [2026-06-03] **"Confirm, don't assume" on cross-agent data points.** APO<$130 — verified live ($125.44) AND verified it's a BROCK *position* trigger not a thesis soft-kill (mildly helps APO puts). The check changed the conclusion. Always pull the sibling's actual threshold semantics, not just the headline.
- [2026-06-03] **Duration-gate discipline: don't push harder either way; wait for confirmation at better levels.** When near-term easing is real but structural thesis intact, "hold core + defer the add until the catalyst confirms" beats forcing a directional call. Will explicitly endorsed this restraint.

## Findings

- [2026-04-17] When oil shocks reverse on unilateral headlines, regional-bank beta (KRE, APO) gives back most of the AM rally by close — conviction bid is small vs beta bid.
- [2026-05-21] **Surface decisively fading a "loaded" catalyst is the most consequential vol-structure read.** NVDA 5/20 max-loaded; outcome SKEW dropped out of 140+, VIX9D crushed — "no catalyst expected." HENRY's job pivots catalyst-anticipation → drift-monitoring after such an event.
- [2026-05-21] **Breakeven decomposition = independent Fed-can't-cut confirmation channel.** Real yields rising + breakeven flat = term-premium/Fed-pinned, not reflation. Triangulates from the bond market vs the PCE print.
- [2026-06-03] **Split-axis decomposition when a "uniform" divergence meets contradicting new data.** 5/21 thesis was "tape calm / substance uniformly hot." By 6/3 substance split: cyclical (rates/energy/index credit) eased while structural (CCC tail + PC/BDC prints) held. Don't force the old binary — decompose by axis, name which axis each datum belongs to, and identify the resolving catalyst (here 6/10 CPI). Honest downgrade beats defending the framework.
- [2026-06-03] **Sibling-STATUS staleness cascade — check the sibling's Last-Updated before citing.** Multiple agents frozen at 5/21 (HENRY + BROCK) while tape moved. BROCK's "APO entrenched >$130" was a 5/21 snapshot; live APO $125.44. When pulling cross-agent data, read the sibling's timestamp and flag stale reads rather than propagating them as current. (Per saved memory: verify-state-before-propagating.)
- [2026-06-03] **Energy-driven yield easing ≠ Fed-pivot yield easing.** 10Y −20bps was Brent −$15 (Hormuz unwind) disinflation relief, not "Fed about to cut." Sticky core (PCE 3.2%, PPI 6.0%) unmoved. Decompose WHAT drove a rate move before reading it as thesis-relevant — the move can be real and directionally adverse to the position while leaving the structural thesis intact.

## References

- [2026-04-17] Live refresh: `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price ^GSPC ^VIX ^SKEW ^VIX3M ^VIX9D ^VVIX KRE WAL JPY=X ^TNX TLT APO`. Use `^GSPC`/`^VIX` (SPX/VIX bare fail). **.venv works on this surface** (Will's "no venv" note was a different container 6/3).
- [2026-05-21] Cross-source-tier: vol/SPX/NVDA = yfinance HENRY-primary. Macro/credit/bank-tier (HY OAS, CCC, Brent, USD/JPY) = pull from BROCK/REGINALD/VIOLET STATUS or dashboard (Prome dashboard lacks HENRY-tier vol metrics).
- [2026-06-03] **FRED convention (adopted):** FRED series publish T+1 — latest = yesterday's close. Date-stamp every FRED row `[FRED M/D]`; yfinance rows are intraday-live. Don't call a FRED number "live/today." Re-run `dashboard.py --compact` at boot. Full: `FORGE/tools/market-data/README.md`.
- [2026-06-03] Credit-tier current source: REGINALD STATUS (HY/CCC/IG date-stamped) + VIOLET STATUS (vol + credit + 10Y). Both refreshed ~6/1-6/2; faster than waiting on own FRED pull (and FRED was 503'ing per Will).

---

## Session Notes

### CHANGES SINCE LAST SESSION (5/22 → 6/3, 13-day gap)
- **R11 analog CONFIRMED DEAD** (VIOLET 6/1) — window 5/28-6/02 expired un-fired, VIX trended DOWN, 0/7 triggers. HEN-31 EXPIRED. The 5/21 "R11 clock running, prior 36%" framing is fully resolved (low-prob outcome hit).
- **Substance side SPLIT.** Cyclical eased (10Y −20bps to 4.50, Brent −$15 to ~$97 Hormuz-unwind, HY OAS −14bps to 272); structural held (CCC flat 946, BROCK PC/BDC Max Bear print substance, WAL v2.2 Bear-medium). Thesis downgraded trap-clinch-WIDER → SPLIT-AXIS / hinges-on-6/10-CPI.
- **USD/JPY crossed 160** (yellow → SAM carry-unwind fired).
- **APO fell below $130** ($125.44) — BROCK position-trigger un-fired on tape; BROCK STATUS frozen 5/21 doesn't reflect it.
- **TLT 5/22 decision executed-on-paper but ticket sat unplaced 11d** (Will salvaging broker side); Jun $85P decayed +92%→−32% as TLT rallied. Will now holds 3× Jun as catalyst bet + 2× Sep 30 $85P.

### LAST SESSION (2026-06-03 Wed ~13:30-15:00 ET — data catch-up + architecture, Will-driven phased brief)
**3 phases, all Will-checkpointed:**
- **Phase 1 (read-only):** credit pull from VIOLET 6/1 + REGINALD 6/2; HEN-30 = NOT fired (272/274/272 oscillating, direction flipped toward kill); HEN-31 = EXPIRED; **duration read** delivered as Will's TLT Sep-leg gate → HOLD 2× Sep 30, DON'T add Sep 19 until 6/10 CPI confirms (energy-driven easing is real but structural thesis intact). Will accepted, said don't push harder.
- **Phase 2 (writes):** STATUS full rewrite (5/21→6/3, split-axis thesis, FRED convention applied, SKEW spot>140/regime<140 reconciled w/ VIOLET); PREDICTIONS.tsv (HEN-31 EXPIRED, HEN-30 updated, HEN-32 CPI-gate added); PROME outbox flag (TLT ticket superseded).
- **Phase 3 (cleanup):** VX.tsv "CURRENT (Mar 3-5)" boot-hazard fixed (relabeled LIVE/STALE-SELLOFF/BEIGE-BOOK; regime-inverted gamma/put-wall/DMA rows flagged STALE); MARKET_DATA.tsv 6/3 row appended; 2 inbox SIGs → processed/, TLT reply → delivered/ (git mv).

**Will's two corrections this session (both right):** CCC/HY is denominator-driven (state as levels not 3.48x); CPI is 6/10 not 6/12 (verify gate dates). Both folded into Feedback above.

### NEXT SESSION
1. **🔴 6/10 May CPI (8:30 ET) = THE GATE (HEN-32).** Consensus core +0.3% MoM. >0.3% → cyclical axis re-arms, 10Y backs up, ADD TLT Sep $85P. ≤0.2% → soft-kill confirms cyclical, only structural axis carries. Drives Will's Sep-leg decision.
2. **🟠 6/5 NFP (May)** — Will selling 3× Jun $85P into first hot print; HEN-28 labor-cliff (CARL-domain).
3. **🟠 USD/JPY >160 sustained** — SAM carry-unwind yellow fired 6/3; watch for 162 orange + any vol-catalyst pairing (non-CPI path to cyclical re-fire).
4. **🟡 SKEW 20d-avg re-establishment ~6/05** (VIOLET — if SKEW holds 144). + VVIX 92+ by 6/05 = leading-indicator activation. Read from VIOLET, don't re-pull.
5. **🟡 6/16-17 FOMC + SEP/dot plot** — primary vol catalyst; Fed-can't-cut test.
6. **🟢 Flag BROCK STATUS stale (5/21)** — APO drop + cyclical easing not reflected. Cross-agent note, not HENRY edit.

### GAPS — PERSISTENT
- **0DTE SPX share + GEX regime** STILL PENDING (5+ sessions). VIOLET 6/1 downgraded GEX-as-regime-specific-mechanism but it's still a HENRY market-structure gap. Manual estimate acceptable.
- **VX.tsv duplicate ID collision** — VX-HEN-19.01-19.06 used twice (Beige Book Mar 4 block AND oil-shock SLOW-MOVING block). Pre-existing; not fixed this session. Renumber on next workbook pass.
- **Stale 4/17 VIOLET outbox file** undelivered (overtaken by 5/21 LIAISON) — left in place; messaging-overhaul will sweep.
- **KB.tsv** — split-axis + FRED-convention + sibling-staleness entries pending (deferred this session).

### INFRASTRUCTURE NOTES
- 6/3: FRED citation convention adopted (date-stamped rows). VX.tsv boot-hazard relabel pattern (split CURRENT into LIVE/STALE-with-reason headers) — transferable to any agent whose VX has a mislabeled "current" block.
