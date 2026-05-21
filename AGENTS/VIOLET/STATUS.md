# VIOLET STATUS

**Signal Status:** 🟠→🟡 **STAGE 2 CONFIRMED, NOT STAGE 3. REGIME LIKELY TERMINATED, BUT VIX HAS NOT YET FIRED.** May 21 boot (Prome ask; 7d gap). **SKEW collapsed 5/15 145.77 → 5/20 132.31 (-13.5 pts in 3 td); 4 of last 5 closes below 140.** This is materially more decisive than the Apr 23-28 mini-break (low 138.16, bounced 2 td). **R12 regime end is the high-probability call now — and that starts the R11 analog clock.** R11 had SKEW collapse → VIX 52.33 in 8 td (PRE_EVENT_FADE). But R12 ended on a *softer* slope (-1.0 vs R11's -2.0): could be GRADUAL_FADE instead. **Episode-17 25C expired worthless 5/19 (VIX ~18 vs strike 25)** — lottery did not print, as expected from a low-vol regime termination not yet completed by a vol event. **The trap is intensifying** (vol absorbed CPI/PPI/FOMC/BOJ/NVDA; SKEW now fading without VIX event; credit deteriorating per BROCK), **but transmission to vol has not occurred.** Stage 2 = "low VIX + widening tape-substance gap" is the read.

**Live (May 21, 12:45 ET — Prome gap-fill batch):** VIX **17.39** | VIX9D **15.01** | VIX3M **20.58** | VIX6M **22.76** | VVIX **94.20** | SKEW **132.31** (5/20; 5/21 EOD not yet posted) | VIX3M/VIX **1.183** | final_5d_change(SKEW) **-9.20** (5/20) | 20d_regr_slope(SKEW) **-0.14**/day (5/20) | HY OAS **2.80** | CCC OAS **9.40** | IG OAS **0.75** (all FRED 5/20 force-fetch) | Regime **R12 likely terminated** | **Last Updated:** 2026-05-21 12:45 ET

---

## SIGNAL DASHBOARD

| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| VIX Spot | **17.39** | May 21 (intraday) | 🟡 | [CONF] yfinance ^VIX |
| VIX9D | **15.01** | May 21 | 🟢 | [CONF] yfinance ^VIX9D — short-dated crushed BELOW spot ⇒ market pricing immediate calm post-NVDA |
| VIX3M | **20.58** | May 21 | 🟡 | [CONF] yfinance ^VIX3M |
| VIX6M | **22.76** | May 21 | 🟡 | [CONF] yfinance ^VIX6M |
| VVIX | **94.20** | May 21 | 🟢 | [CONF] yfinance ^VVIX — **eased from 5/12 peak 98.55; vol-of-vol no stress** |
| SKEW | **132.31** | May 20 | 🟢 | [CONF] yfinance ^SKEW — **broke 140 sustained: 4/5 last closes below; low 132.31. 5/21 close not yet posted via yfinance at 12:45 ET refresh; CBOE publishes ^SKEW EOD; refresh deferred to next boot.** |
| VIX3M/VIX | **1.183** | May 21 | 🟢 | [CONF] Calculated — contango deep, holding |
| VIX Futures Curve | Contango (deep) | May 21 | 🟢 | [CONF] CBOE |
| HY OAS | **2.80** | May 20 | 🟢 | [CONF] FRED BAMLH0A0HYM2 force-fetch 5/21. Tightened -6bps 5/19→5/20 (2.86→2.80, FURTHER from 2.90 kill). BROCK 5/21 brief cited 2.86 = 5/19 print (1d stale). |
| CCC OAS | **9.40** | May 20 | **🟠** | [CONF] FRED BAMLH0A3HYC force-fetch 5/21. Tightened -8bps 5/19→5/20 (9.48→9.40, 60bps from 10.00 analog). 20d trajectory still +25bps (9.15 5/07 → 9.40 5/20). BROCK 5/21 brief cited 9.48 = 5/19 print (1d stale). |
| 10Y UST | **4.67%** (LIQUID 5/18) | May 21 | **🟠** | [CONF LIQUID 5/18] — **+42bps over 20d; duration channel FIRING** |
| IG OAS | **0.75** | May 20 | 🟢 | [CONF] FRED BAMLC0A0CM force-fetch 5/21. IG continues tightening through CCC bifurcation — complacency persists. |
| final_5d_change (SKEW) | **-9.20** | May 20 | 🟠 | [CONF] regime_termination.py:118 = SKEW(t) - SKEW(t-5td). **Steepest 5d decline of regime; this IS the regime-termination indicator. (Mislabeled "20d-SKEW-slope" in 5/13 STATUS; see KB-VIO-059 for methodology audit.)** |
| 20d_regr_slope (SKEW) | **-0.14**/day | May 20 | 🟢 | [CONF] regr through 5/20. Separate metric from final_5d_change. Attenuated from -0.49 (early May). Has been negative since early May (not "sign-flipped" — earlier STATUS conflated this with final_5d_change). |
| NVDA ATM IV (1-2wk) | **30-37%** | May 21 | 🟢 | [CONF] yf option chain — **post-print IV crush; 5/22 ATM 37%, 5/26 ATM 30%, 6/12 ATM ~33%** |
| NVDA 20d realized | **40.1%** | May 21 | 🟢 | [CONF] computed — realized > short-dated implied = IV crushed below realized |
| NVDA put-call IV skew | **+3-4 vol pts** | May 21 | 🟡 | [CONF] yf 5/29 chain — OTM puts (40%-43% IV) > OTM calls (37%-41% IV); modest negative skew, not tail-bid |

---

## CONVERGENCE MATRIX

| Vector | Score | Evidence | Last Updated |
|--------|-------|----------|--------------|
| Spot VIX elevation | ⚪ | 17.39 — drifted DOWN 0.48 over 8d through NVDA print, hot CPI/PPI, geopolitics. Vol-surface absorption now 5+ catalysts deep. | 2026-05-21 |
| Term structure inversion | ⚪ | 1.183 — contango holds deep; VIX9D 15.01 BELOW spot = market pricing immediate calm post-NVDA. | 2026-05-21 |
| VVIX stress | ⚪ | 94.20 — EASED from 5/12 peak 98.55; option-of-option market relaxed, not bidding tail vol. | 2026-05-21 |
| **SKEW-VIX-VVIX divergence** | **🟡↓** | **SKEW collapsed 145.77 (5/15) → 132.31 (5/20). 5d-change -9.20, steepest of regime. 4/5 closes <140. R12 regime likely TERMINATED. But final slope softer than R11's (-2 to -3 PRE_EVENT_FADE archetype). Could be R11 analog (VIX 52 in 8 td) OR GRADUAL_FADE (R6/R7-type, peaceful resolution). Downgrade 🟠→🟡 because the *signal* the divergence was supposed to deliver (vol event) didn't fire on R12 termination day.** | 2026-05-21 |
| **Credit-to-vol transmission** | **🟠** | **FRED spot-check 5/21 (latest data 5/20): CCC 9.40 (+25bps 20d, +36bps from cycle low 9.04, 60bps from 10.00 analog). HY 2.80 (cycle-low retest, 10bps from 2.90 kill). IG 0.75 (still tightening). BROCK 5/21 brief was 1-day stale (cited 5/19 prints: HY 2.86 / CCC 9.48). 20d bifurcation thesis intact (CCC +25 / HY ~flat) but most recent 1d (5/19→5/20) showed BOTH HY and CCC tightening — risk-on retrace at the substance-side. Substance-side Stage-3 triggers (#4 HY>2.90, #5 CCC>10.00) FARTHER away than 5/13 STATUS implied. VIX not pricing any of this. Classic stage-2 decoupling.** | 2026-05-21 |
| **Index concentration / breadth** | **🟡** | WALTER signal KB-VIO-056 — SPX record high with bad breadth. Persists. | 2026-05-13 |
| **Call-notional/dealer-flow stretch** | **🟡** | KB-VIO-055 + 5/14 gamma-momentum signal — gamma index reportedly record-high; suppresses realized vol mechanically. Explains the absorption pattern: VIX <20 is mechanical (positive-gamma damping) not informational. | 2026-05-21 |
| **NVDA post-print vol verdict (new)** | **⚪** | **Post-print IV crush: 5/22 ATM 37%, 5/26 ATM 30%, 6/12 ATM ~33%. 20d realized 40.1% > short-dated implied = option market pricing LESS forward vol than recent history. Modest -3 to -4 vol-pt put-call skew (puts 40-43%, calls 37-41%), not tail-bid. Verdict: NVDA print absorbed cleanly; options market signals calm.** | 2026-05-21 |

**Convergence Score:** 8/40 (20%) — Credit-to-vol 🟠 (3), SKEW divergence 🟡 (2; downgraded — divergence regime ended without vol event), Index concentration 🟡 (2), Call-notional stretch 🟡 (2; supported by 5/14 WALTER gamma signal), NVDA print ⚪ (1), all others ⚪. **Score dropped from 9/35 because (1) the SKEW divergence regime appears to have terminated WITHOUT vol event, removing the strongest near-term firing-signal vector, and (2) VVIX eased rather than stressed. The Stage-2 trap framing is intact but the imminence read for Stage 3 is WEAKER than it was 7d ago, not stronger.**

**Drift assessment (May 13 → May 21):**
- 🟡 **SKEW regime R12 likely TERMINATED.** 5/15 145.77 → 5/20 132.31 (-13.5 pts in 3 td). 4 of 5 last closes below 140. Materially more decisive than the Apr 23-28 mini-break (low 138.16, bounced in 2 td). The May 13 STATUS forecast was: regime ends → R11 clock starts → VIX event 0-8 td later. **R12 ended ~5/18-5/20. Clock is now running.** Window: peak vol 5/26 - 6/01 if R11 analog holds.
- ⚠️ **HOWEVER: R12 ended on a softer 5d-slope (-9.2 absolute / regr -0.14 per-day) than R11 (-2.0 final 5d).** Of the 4 PRE_EVENT_FADE regimes, the slopes were R1 -1.0 (still produced VIX 36), R2 -0.6, R5 -1.9, R11 -2.0. R12 sits at the *softer* end of the PRE_EVENT_FADE distribution — and PRE_EVENT_FADE is only 4 of 11 historical regimes (36%). GRADUAL_FADE (R6, R7 — 18%) is also live; those resolved peacefully into modest VIX of 21-36.
- 🟠 **Credit bifurcation 20d trajectory intact, but 1d retrace.** FRED 5/21 fetch (latest data 5/20): CCC 9.40 (+25bps 20d from 9.15 5/07), HY 2.80 (vs 2.79 5/07, ~flat 20d). The bifurcation thesis (CCC widening while HY flat = quality-sensitive credit stress) is intact on 20d window. BUT the most recent 1d (5/19→5/20) was -8bps CCC and -6bps HY — risk-on retrace at the substance-side, both tiers tightening together. **BROCK 5/21 brief cited 9.48 / 2.86 = 5/19 prints (1d stale; FRED OAS publishes T+1). KB-VIO-060 flags. Stage-3 substance triggers (#4 HY>2.90, #5 CCC>10.00) are FARTHER away than 5/13 STATUS implied.** Stage-2 archetype (tape loose while substance worsens) holds on 20d frame but recent 1d shows the credit-side easing too.
- 🟠 **10Y +42bps over 20d to 4.67% (LIQUID 5/18).** Duration channel firing without vol event = vol surface ignoring real-rate stress. Adds to the "vol absorption" tally.
- ⚪ **Episode-17 May 19 25C expired worthless 5/19** (VIX ~18 vs strike 25). Confirms regime termination did not transmit to vol within DTE window. Trade-thesis post-mortem: SKEW divergence as VIX-spike predictor was correct on direction (regime ended) but failed on transmission (no spike). Mechanism candidate: positive-gamma suppression (5/14 WALTER signal) damped realized vol mechanically.
- ⚪ **NVDA print absorbed cleanly (5/20 print, 5/21 -1.5% spot move).** Post-print IV crush: 5/22 ATM 37%, 5/26 ATM 30%. Short-dated implied LESS than 20d realized 40.1% = option market pricing forward calm. Modest -3-4 vol-pt put-call skew (40-43% puts vs 37-41% calls), NOT tail-bid. NVDA was not a vol catalyst.
- ⚪ **VVIX EASED, not stressed.** 5/12 peak 98.55 → 5/21 94.20. The 5/13 STATUS noted "climbing toward 100" — that climb reversed. If transmission were imminent, VVIX would lead VIX higher; it isn't.

**Methodology note (resolved 2026-05-21):** STATUS 5/13 cited "20d-SKEW-slope -1.0 SIGN-FLIPPED" — that was `final_5d_change = SKEW(t) - SKEW(t-5)` per `regime_termination.py:118`, not a 20-day regression slope. The literal 20d regression slope through 5/13 was -0.118 (per-day), had been negative since early May (not "sign-flipped"). Substantive call (regime fading) was directionally right; the label was wrong. **Corrections completed 5/21:** KB-VIO-051 and KB-VIO-058 prepended with [LABEL CORRECTED 2026-05-21] preambles; new KB-VIO-059 logs the methodology note; STATUS dashboard rows renamed to `final_5d_change (SKEW)` and `20d_regr_slope (SKEW)` as two separate metrics; MEMORY.md gained durable "METRIC SEMANTICS" section.

**Prior drift assessment (May 3 → May 13) — preserved for trajectory:**
- 🟠 **20d-SKEW-slope SIGN-FLIPPED +0.6 → -1.0 (KB-VIO-058).** First negative reading in the entire 223-td regime. PRE_EVENT_FADE trajectory now activating. Of 11 historical regimes, 4 (36%) ended PRE_EVENT_FADE; all 4 had final 5d slopes -2.0 to -3.5. Closest analog R11 (150 td) had -2.0 → VIX 52.33 just 8 td after regime end. Current -1.0 is BEGINNING of that pattern — needs continued steepening to confirm.
- 🟠 **CCC OAS REVERSED through the dark interval (KB-VIO-057).** Cycle low 9.04 May 1 → 9.37 May 12, +33bps. Crossed 9.30 early-stress threshold May 11. **Critically: CCC widened ON THE CPI DAY itself** (9.20 May 8 → 9.31 May 11 → 9.37 May 12). Credit DID NOT absorb the hot inflation the way vol did. HY +7bps only (cycle low 2.75 → 2.82); IG still tightening (0.77). Classic late-cycle CCC decoupling.
- 🔴 **CPI/PPI gate FIRED without vol event.** Two consecutive HOT inflation prints (CPI May 12, PPI May 13 — 6.0% YoY largest MoM since Dec 2022). VIX moved from 16.99 to 17.87 (+5.2%). This was the last named material catalyst in the pre-mortem (May 3 STATUS). **Gate fired; lottery did not print** — but credit and slope tell a different story than VIX surface.
- ⚪ **VVIX climbing 95.17 → 98.36** — option market mildly bidding vol-of-vol but nowhere near 120 stress threshold. Watch.
- ⚪ **VIX9D 15.87 BELOW spot** = short-dated implied vol crushed; market pricing immediate calm even as CPI/PPI dropped HOT. Aggressive complacency on near-term tape.
- 🟡 **Two regime-fragility signals from WALTER inbox (May 9):** record SPX call notional + bad breadth at record high with 1929/1973/1999 analogs. Both processed → KB-VIO-055, KB-VIO-056. Operate on weeks-to-months horizon, not 6-DTE trade horizon.

---

## REGIME STATUS

**Current Regime:** LOW VOL (VIX 17.39, 15-20 bucket) — SKEW R12 regime **likely TERMINATED 5/18-5/20** after 230+ td (longest in 19-yr history). Last 5 closes: 145.77 / 138.40 / 135.50 / 132.31 (5/15-5/20). Term structure deeply in contango (1.183), VIX9D 15.01 BELOW spot (front crushed). VVIX 94.20, EASED from 5/12 peak. **R11 analog clock now running, but R12 ended on a softer 5d-decline (-9.2) than R11's final-5d -2.0; PRE_EVENT_FADE is one of three live trajectories (PRE_EVENT_FADE 36%, GRADUAL_FADE 18%, POST_EVENT_PERSIST 45% historically). Stage-3 transmission window: 5/26 - 6/01 IF R11 analog holds; if GRADUAL_FADE, vol drifts to 20-25 over weeks without spike.** Credit substance worsening (CCC 9.48 +26bps, 10Y 4.67% +42bps) while vol absorbs — Stage-2 trap framing fully canonical.

*Full regime framework, threshold logic, and crisis-analog library: `thesis/VIX_THESIS.md`.*

---

## POSITION SNAPSHOT

**VIX May 19 25C — Episode #17 — EXPIRED WORTHLESS 5/19** (VIX 18.06 close vs strike 25). Episode-17 closed. Post-mortem to be written in `research/` — key learning: SKEW divergence as VIX-spike predictor was directionally correct (regime ended within DTE window) but failed on transmission (no spike). Candidate mechanism: positive-gamma suppression (KB-VIO-055, 5/14 WALTER signal) damped realized vol mechanically through CPI/PPI/NVDA. No open positions.

**Prior framing (preserved for record):** As of 5/13 status, position had non-trivial path to ITM if slope steepened to -2.0 + HY broke 2.90 within 6 DTE. **Neither happened.** Slope stayed shallow (5d-change peaked at -9.2 on the last day BEFORE regime-end was confirmed); HY moved *opposite* direction (now 2.86, further from 2.90 trigger).

**Material context flip from earlier this session.** When I wrote the post-CPI take, the framing was "lottery did not print, expire worthless." The FRED + slope refresh changed that:
- 🟠 20d-slope sign-flipped (+0.6 → -1.0) — PRE_EVENT_FADE trajectory beginning
- 🟠 CCC OAS reversed +33bps from cycle low, crossed 9.30 early-stress May 11
- ⚪ HY OAS at 2.82 (8bps from 2.90 dual-trigger second half)

**Why this matters for 6 DTE:** Closest historical analog R11 (also long regime: 150 td) had final 5d slope -2.0 → VIX 52.33 just 8 td after regime end. Current slope -1.0 → if it steepens to -2.0+ over the next 4 td (May 14-19), the historical PRE_EVENT_FADE lag could align with expiry. Mechanism: regime ends (SKEW collapses below 140) → vol event 0-8 td later. The R11 precedent is the most relevant case in the dataset.

**Watchlist through expiry (daily, May 14-19):**
1. 20d-SKEW-slope trajectory — does it steepen toward -2.0?
2. HY OAS — does it break 2.90 (currently 2.82)?
3. CCC OAS — does it continue widening or stall at 9.37?
4. VVIX — does it break 100, then 110?
5. SKEW absolute level — sustained <140 = regime ends, R11 clock starts

**Re-decision closed by expiry.** Per Will-approved HOLD (May 3) → ran to expiry. No new position recs without Will.

Full position framework: `TRADE.md`.

---

## CROSS-AGENT SIGNALS (Pending)

**Outbound:**
- `outbox/SIG-VIOLET-LIQUID-20260415-hy-oas-trigger-monitor.md` — STILL QUEUED (status unconfirmed; messaging system overhaul in progress per project memory)
- **New (pending draft):** SIG to HENRY+RED — CPI+PPI both hot, VIX absorbed both → regime-absorption framing now a confirmed pattern, not anecdote

**Inbound:** ✅ **Processed May 13:**
- signal_2026-05-09_spx-call-notional-sox-rsi-meltup.md → KB-VIO-055 → `inbox/processed/`
- signal_2026-05-09_spx-record-high-breadth-deterioration.md → KB-VIO-056 → `inbox/processed/`

---

## RESEARCH QUEUE

| Priority | Topic | Status |
|----------|-------|--------|
| ✅ | **HY/CCC OAS FRED refresh** | **DONE May 13. CCC reversed +33bps (9.04→9.37), crossed 9.30 early-stress May 11. HY +7bps only. KB-VIO-057.** |
| ✅ | **20d-SKEW-slope refresh** | **DONE May 13. SIGN-FLIPPED +0.6 → -1.0. PRE_EVENT_FADE trajectory activating. KB-VIO-058.** |
| 🔴 | **Daily slope + CCC + HY monitoring through expiry** | NEW. Trigger watch: CCC >9.30 ✅ (May 11). Need HY >2.90, slope steepening to -2.0+. Re-check daily May 14-19. |
| 🟠 | **Draft SIG to HENRY+RED on regime-absorption pattern** | Five consecutive absorbed catalysts is now a documented phenomenon worth flagging. |
| 🟠 | **Verify WALTER signals (KB-VIO-055, 056)** | $2.6T notional methodology + Goepfert breadth source primary check. Defer to NEXUS/RED if convergent. |
| 🟠 | **May 19 25C expiry record-and-close** | Post-expiry: write trade post-mortem; lock Episode-17 record. |
| 🟡 | **Phase 1: CFTC COT VIX futures pipeline** | Deferred — ~90 min. Spec in MEMORY.md 2026-04-17. |
| 🟡 | **KB-VIO-042 within-cycle bounce rule revision** | Long regime broke the 1-3 td bounce rule (took 4-td + post-FOMC catalyst). Rule needs amendment. |

---

## THESIS CONNECTION

**Updated assessment (May 13):** The trade-thesis is now functionally closed (6 DTE, deep OTM, no remaining named catalyst). The **regime-thesis is stronger than it was May 3** — vol surface has now absorbed five consecutive macro stressors (FOMC, BOJ, CPI hot, PPI hot, plus general stagflationary tape from WALTER BOARD signals 001-007). Two new regime-fragility vectors arrived from WALTER inbox: record call notional and bad-breadth at index records with 1929/1973/1999 analogs. **The regime is bending under accumulating fragility evidence but has not broken — and the trade-window is expiring before the break.**

**Resolved gates (full list):**
- ❌ Apr 22 SKEW >145 — never breached
- ✅ Apr 23-28 strict invalidation — hit, low 138.16
- 🟢 Apr 30 REBOUND_AFTER_INVALIDATION — bounced to 143.33 post-FOMC
- 🟡 Apr 28-29 FOMC — 4 dissents (most since 1992), vol did not spike
- 🟡 Apr 28 BOJ — 3 dissents, vol did not spike
- 🟡 **May 12 April CPI HOT — vol did not spike** (KB-VIO-054)
- 🟡 **May 13 April PPI HOT 6.0% YoY +1.4% MoM largest since Dec 2022 — vol did not spike** (KB-VIO-054)

**Forward gates:** May 19 25C expiry (HOLD; non-trivial path to ITM emerging) · **20d-slope steepening watch: -1.0 → -2.0+** (R11 analog threshold) · **Dual credit-stress trigger: CCC >9.30 ✅ FIRED May 11; HY >2.90 pending (currently 2.82, 8bps away)** · SKEW <140 sustained (regime end → R11 clock starts) · Jun 12-15 (60d window close + FOMC + SEP Jun 16-17 — secondary vol gate).

*Core hypothesis, transmission chain, and regime-dependent lead-lag logic: `thesis/VIX_THESIS.md`.*

---

*Last updated: 2026-05-13 20:55 ET (boot + FRED refresh + slope refresh. Two material findings: (1) CCC OAS reversed +33bps through CPI hot, crossed 9.30 early-stress May 11 → KB-VIO-057; (2) 20d-SKEW-slope SIGN-FLIPPED +0.6 → -1.0 → KB-VIO-058. SKEW divergence and credit-to-vol both upgraded ⚪→🟠. Convergence Score 4/35 → 9/35 (8% → 26%). Position re-framed: not "dead lottery" — now "sunk-cost optionality with non-trivial path to ITM" if slope steepens + HY clears 2.90 within DTE window. Watchlist established for daily May 14-19. Signal status ⚪→🟠.)*
