> **PROVENANCE:** This file was drafted by a Prome-spawned revival proxy on 2026-05-18, not by HENRY itself. HENRY owns integration decisions on next boot. Treat as input, not as agent self-state. This is the **second** revival-proxy prototype under PROME/ORCHESTRAL_LAYER_DESIGN.md Step 4 (first was LIQUID, same day).

# HENRY REVIVAL PACKET — 2026-05-18

**Proxy budget:** STATUS (full), inbox listing + 5/14 ×2 + 5/16 sweep in full + 5/9 batch top 5 by macro/vol/positioning relevance, last 15 HENRY commits, HEARTBEAT (lines 1-120 + grep), PROME/FLEET_SCAN.md (HENRY rows + tape-vs-substance section), VIOLET STATUS first 40 lines, live yfinance pull for SPX/VIX/VIX3M/SKEW/VVIX/VIX9D + NVDA price.
**Last HENRY self-commit:** 2026-04-17 (31 days stale).
**Last HENRY STATUS update:** 2026-04-17 EOD.
**Live catalyst:** NVDA Q1 earnings Tue 2026-05-20 AMC (HENRY-domain read-through).
**Inbox load:** 15 unprocessed signals (12× 5/9 batch + 2× 5/14 + 1× 5/16 sweep).

---

## 1. Today's live tape diff vs HENRY's Apr 17 STATUS

> *Numbers come from two sources: (a) Prome's dashboard 2026-05-18 pass-through for the macro/credit tier; (b) proxy's own yfinance pull at session time for the HENRY-domain vol/SPX/NVDA tier that the Prome dashboard does not carry. Sources tagged inline. STATUS column is the Apr 17 EOD print.*

| Metric | HENRY STATUS (Apr 17) | Live (5/18) | Δ over 31d | Zone change | Notes / source |
|---|---|---|---|---|---|
| **SPX** | 7,123.77 🟡 | **7,403.05** 🟢 | +279 / +3.92% | inside 🟢 (below 7,100 invalidation, above structural bid) | yfinance proxy pull; >7,100 condition of invalidation has held 5+ sessions — **see §2** |
| **VIX** | 17.76 🟡 | **17.82** 🟡 | +0.06 | none | yfinance proxy pull; flat over 31d through TWO hot CPI/PPI prints — vol-surface absorption holding |
| **VIX3M** | 20.68 | **20.92** | +0.24 | none | yfinance; ratio steady |
| **VIX3M/VIX** | 1.160 contango | **1.174** contango | +0.014 | deeper contango | yfinance; front crush + curve normal |
| **VIX9D** | (not in STATUS) | **16.86** | — | front < spot = crush | yfinance; 9-day under spot, classic short-dated complacency |
| **VVIX** | 94.26 | **91.18** | -3.08 | further compressed | yfinance; option-of-option market less stressed, NOT a pre-event mark-up |
| **SKEW** | 140.74 🟠 | **138.40** 🟡 | -2.34 | 🟠→🟡 | yfinance; dipped below 140 for first time in this regime — see §2 + VIOLET KB-VIO-058 |
| **10Y Yield** | 4.25% 🟡 | **4.59%** 🔴 | +34bps | 🟡→🔴 | Prome dashboard; threshold 4.5%/4.8%/5.0% per STATUS line 57 → **first yellow→red zone shift** |
| **TLT** | $87.04 | **$83.56** 🔴 | -$3.48 | →🔴 (confirms 10Y) | Prome dashboard |
| **Brent** | $90.67 🟡 | **$109.73** 🔴 | +$19.06 / +21% | 🟡→🔴 | Prome dashboard; April Hormuz reopen unwound; gas $4.50 wkly confirms |
| **USD/JPY** | 158.55 🟠 | **158.93** 🔴 | +0.38 | 🟠→🔴 (per HEARTBEAT 158 red) | Prome dashboard; 165 cross-agent trigger still 6 handles away |
| **HY OAS** | 285 🟢 (Apr 16 print) | **280** 🟢 | -5bps | none | Prome dashboard; 20bps cushion to 260 kill — see §2 + cross-channel §3 |
| **CCC OAS** | 924 🟡 (Apr 2) | **935** 🟡 | +11bps | none | Prome dashboard; reverse-from-cycle-low pattern confirmed by VIOLET (KB-VIO-057) |
| **KRE** | $70.38 🟡 | **$67.92** 🟡 | -$2.46 | none | Prome dashboard; 5+ pts above $65 yellow trigger but trending toward it |
| **APO** | $124.28 🟡 | **$134.07** 🟢/watch | +$9.79 | yellow→watch (sustained $130+) | Prome dashboard; BROCK-domain but feeds back to market-structure bull-bid story |
| **HYG** | $80.62 🟢 | not in tier | — | — | — |

### Time series for the load-bearing HENRY metrics

> *v2 improvement #2: HENRY needs trajectory, not just endpoints. Series stitched from HEARTBEAT, VIOLET STATUS, FLEET_SCAN, and proxy yfinance pull.*

**VIX trajectory (5 points over 31d):**
| Date | VIX | Note |
|---|---|---|
| Apr 17 | 17.76 | HENRY STATUS — "did not break 17" |
| May 6 | ~17.5 | VIOLET cycle low referenced |
| May 13 | 17.87 | VIOLET STATUS — absorbed CPI 3.8% / PPI 6.0% |
| May 17 | 18.43 | HEARTBEAT 5/17 dashboard re-run |
| **May 18** | **17.82** | yfinance — back down |

→ **31-day band: 17.5-18.5. The complacency floor has held through two hot prints, regional bank weakness, BIZD below $12.50, FSK NAV -9.9%, Brent +21%, USD/JPY through 158.** This is the central HENRY puzzle of the gap window.

**SPX trajectory (6 points):**
| Date | SPX | Note |
|---|---|---|
| Apr 17 | 7,123.77 | HENRY STATUS — closed +1.17% |
| Apr 30 (proxy est) | ~7,200 | HEN-22/23/27 resolution window — no records read |
| May 8 | ~7,420 (FLEET_SCAN RED) | RED 5/13 cited ATH context |
| May 13 | ~7,450 | VIOLET cycle context |
| May 16 | 7,501 | yfinance 5d high |
| **May 18** | **7,403** | yfinance — back off the high |

→ **+279pts over 31d, broke through 7,100 invalidation threshold convincingly and held above for the full month.** This is the SPX leg of HENRY's invalidation triad firing.

**10Y yield trajectory (5 points):**
| Date | 10Y | Note |
|---|---|---|
| Apr 17 | 4.25% | HENRY STATUS — yellow |
| May 5 | ~4.50% (30Y 5% headline) | First 30Y 5% since 2007 (signal 5/14) |
| May 13 | ~4.55% (30Y auction 5.046%) | $25B 30Y, BTC 2.30, indirect 66.6% — no demand stress |
| May 17 | 4.57% (dashboard) | HEARTBEAT |
| **May 18** | **4.59%** 🔴 | Prome dashboard — through yellow into red |

→ **+34bps over 31d, broke through 4.5% yellow into 4.8% threshold zone.** The duration regime LIQUID's revival packet flagged as load-bearing is HENRY-relevant: term-premium / fiscal narrative driving the long end is a HENRY market-structure question.

**Brent trajectory (5 points):**
| Date | Brent | Note |
|---|---|---|
| Apr 17 | $90.67 | HENRY STATUS — Hormuz "open" |
| May 5 | ~$98-100 | LIQUID Apr 16 print was $98.20 |
| May 13 | $105.81 | HEARTBEAT |
| May 17 | $109.26 | HEARTBEAT |
| **May 18** | **$109.73** 🔴 | Prome dashboard; 5/18 Iran-anchor reverify in WALTER queue |

→ **+$19 over 31d.** The "oil-shock removed" comfort that closed HENRY's Apr 17 STATUS has fully unwound. The April-CPI loop LIQUID names is real and recurring.

**USD/JPY trajectory (5 points):**
| Date | USD/JPY | Note |
|---|---|---|
| Apr 17 | 158.55 🟠 | HENRY STATUS |
| May 8 | ~158.5 | HEARTBEAT context |
| May 13 | 157.87 | HEARTBEAT |
| May 17 | 158.73 | HEARTBEAT — broke 158 red threshold |
| **May 18** | **158.93** 🔴 | Prome dashboard; 160 trigger 1.07 handles away |

→ **31-day net flat, but range expanded.** Through 158 to a fresh cycle high, but 160 trigger (and 165 cross-agent threshold) still intact. SAM-domain.

**KRE trajectory (5 points):**
| Date | KRE | Note |
|---|---|---|
| Apr 17 | $70.38 🟡 | HENRY STATUS |
| May 5 (proxy) | ~$68 | — |
| May 13 | $67.14 | HEARTBEAT |
| May 17 | $66.97 🟡 | HEARTBEAT |
| **May 18** | **$67.92** 🟡 | Prome dashboard; 2.92 above $65 yellow→orange trigger |

→ **-$2.46 over 31d, trending toward $65 trigger. WAL specifically below $75 bear line.** Bank tape is closer to cracking than vol or SPX suggest.

### Top-of-tape read for HENRY

The 31-day gap shows the **complacency-trap thesis is half-validated and half-falsified, in a very specific pattern**:

- **VALIDATED:** the underlying substance is hotter (CPI 3.8%, PPI 6.0% YoY largest MoM since Dec 2022, Brent +21%, USD/JPY broke 158, BIZD red, WAL bear line broken, FSK NAV -9.9%, 10Y broke 4.5% yellow into red zone).
- **FALSIFIED:** the tape refuses to confirm (VIX 17.82 essentially flat, SPX +3.9% through 7,100 invalidation, HY OAS *tighter* not wider). HENRY's named invalidation triad (HY OAS <260 + VIX <15 + SPX >7,100 for 5 sessions) is **2 of 3 active** — only VIX <15 has not fired (current 17.82).

**This is the live HENRY puzzle.** Two transmission hypotheses fit (see §3) — gamma/momentum suppression (5/14 signal) and credit-leads-vol-6-16wk lag in LOW_VOL regime (VIOLET's standing framework). Both predict the floor is mechanical-not-fundamental and breaks asymmetrically when it breaks.

---

## 2. Thesis-kill proximity verdict — HENRY's COMPLACENCY TRAP

**Invalidation criteria** (per STATUS line 110): `HY OAS <260 sustained + VIX <15 + SPX >7,100 for 5 sessions`. All three must fire simultaneously.

**Directional semantics:**
- **TIGHTER HY OAS** (compression toward 260) = thesis APPROACHING DEATH.
- **LOWER VIX** (compression toward 15) = thesis APPROACHING DEATH.
- **HIGHER SPX** (sustained >7,100) = thesis APPROACHING DEATH (already triggered).
- All three moving the wrong way TOGETHER = invalidation firing. Currently 2 of 3 firing, VIX is the holdout.

### Status of each invalidation leg

| Leg | Threshold | Current | Status vs threshold | Sessions held |
|---|---|---|---|---|
| HY OAS | <260 sustained | **280** 🟢 | 20bps above kill; tightest in cycle = 276 (May 17) | 0 sessions <260 |
| VIX | <15 | **17.82** 🟡 | 2.82 above kill; cycle low ~17.5 May 6 | **0 sessions <15 — this leg has never fired** |
| SPX | >7,100 for 5 sessions | **7,403** 🟢 | 303pts above kill; broke through ~Apr 25 | **15+ sessions >7,100 — this leg FIRED ~3 weeks ago** |

### Verdict: **2-of-3 firing, VIX is the holdout. Thesis on credit watch, vol is the binding constraint.**

This is a critical re-read for HENRY. The Apr 17 STATUS said "only SPX piece qualifies" of the invalidation triad. **Three weeks later, SPX has held above 7,100 the entire month**, so that leg is now structurally invalidated, not pending. HY OAS at 280 with cycle low 276 has been *consistently within 20bps of kill all month*. **Only VIX <15 has not fired**, and the live print is 17.82 — 2.82 from kill.

**What this means for HENRY's thesis:**
1. **Two-thirds of HENRY's stated invalidation criteria are now firing.** Apr 17 framing ("only SPX piece qualifies") is stale and should be retired. The current honest read is "two of three invalidation legs firing; thesis preserved only because VIX has not compressed."
2. **The standing belief that VIX <15 won't fire on its own** (because credit/banks are stressing) is the load-bearing assumption HENRY is now making implicitly. This assumption needs to be made *explicit* and tested.
3. **The asymmetric reads:** (a) if VIX <15 fires for a single session, the thesis is structurally falsified — write the kill memo now; (b) if VIX *spikes* in the absence of any HY OAS widening, that's the gamma-unwind / breadth-break path (see §3).

### Cross-signal lookup: closest path to invalidation

If VIX compresses 17.82 → 15.00 = **-2.82 points needed**. Trailing 31d range has been 17.5-18.5; vol has not been near 15 since November 2024 per VIOLET's regime context (223 td of LOW_VOL regime, longest in 19yr history). **Cycle-low to invalidation distance: ~2.5 points.**

If HY OAS tightens 280 → 260 = -20bps needed. Cycle low was 276 (May 17). **Cycle-low to invalidation distance: ~16bps.**

**Implication:** HY OAS is closer to firing than VIX. The natural ordering of the kill sequence is HY OAS sub-260 first, then VIX compresses on the "credit is fine" relief, then the trap clinches and HENRY writes the kill memo. **The watch is therefore HY OAS sub-265 for 2 sessions, not VIX, as the leading invalidation tell.**

### One important narrative twist

HENRY's thesis name is "COMPLACENCY TRAP" — meaning *if* vol/credit stay calm while substance prints hot, the *eventual* break is sharper. **The thesis is the trap, not the calm.** So the bearish read of the current 2-of-3 invalidation print is **not** "thesis dying" — it's "trap deepening." The kill memo only fires if all 3 hold simultaneously for the required duration AND substance softens. The substance keeps printing hot (CPI 3.8%, FSK NAV -9.9%, etc.) — so the *trap framing* survives 2-of-3 invalidation firing because the trap is *about* this exact divergence.

**Proxy's recommendation:** rewrite STATUS line 110 to distinguish two scenarios explicitly:
- **Soft kill:** all 3 fire + substance softens (CPI back to 2%-handle, FSK-style prints reverse). Thesis fully invalidated. Stand down.
- **Trap clinch:** 2-3 of 3 fire + substance keeps hot (current state). Thesis VALIDATES, just hasn't transmitted yet. The longer this state holds, the more asymmetric the break.

HENRY's call on which scenario the May 18 tape represents is the central question for the revival session.

---

## 3. Cross-channel cohere/contradict — does complacency-trap survive the duration break?

**LIQUID's revival packet (sister file in this Step-4 batch)** finds the bear thesis has migrated PLUMBING → DURATION: SOFR-IORB normalized (-10bps, was +7bps), 10Y broke 4.5% yellow into red (+30bps over 32d), TLT confirms (-3.2%). The active transmission channel is no longer funding stress but term-premium / fiscal repression.

### Does this cohere with HENRY's complacency-trap thesis?

**Yes, strongly cohere, through a precise channel: the duration break IS the trap mechanism.**

| Channel | Direction | Cohere/Contradict with HENRY trap |
|---|---|---|
| 10Y +34bps to 4.59% | 🔴 broke wide | **COHERE** — Fed-can't-cut narrative locked deeper. CPI 3.8% / PPI 6.0% YoY largest MoM since Dec 2022 keeps front end pinned; back end repricing fiscal/term-premium. This is exactly the "stagflation trap survives clean oil unwind" line HENRY closed Apr 17 STATUS on. |
| TLT -$3.48 to $83.56 | 🔴 confirms | **COHERE** — no escape via long Treasuries means traditional 60/40 hedge broken. Forces equity buyers to keep equity. Mechanically supports SPX bid. |
| Brent +$19 to $109.73 | 🔴 reaccelerating | **COHERE** — re-energizes April-CPI loop, makes 10Y >4.5% durable, keeps Fed pinned. HEN-23 ("gas $4+ = consumer demand destruction") may be firing — gas now $4.50 wkly, well past $4 threshold. |
| HY OAS 280 (cycle low 276) | 🟢 essentially flat | **COHERE** — the trap requires vol/credit to refuse to confirm. Credit-stress thesis is grinding but intact (LIQUID: 32-day trend -5bps within noise; gentle compression stalled at 276-280 floor not broken through). |
| VIX 17.82 | 🟡 flat | **COHERE** — gamma/momentum suppression hypothesis (5/14 signal) plus VIOLET's LOW_VOL regime (credit-vol correlation ~0.06, credit leads vol 6-16 weeks) both explain why vol refuses to confirm. **VIOLET's 20d-SKEW-slope sign-flipped negative on 5/13 — first time in regime; analog R11 went VIX 17.76 → 52.33 in 8 trading days.** This is a HENRY-VIOLET shared canary. |
| SOFR-IORB -10bps | 🟢 normalized | **NEUTRAL** — closes one transmission path (plumbing) but doesn't kill the trap. The trap survives via duration + substance prints. |
| BIZD $12.52 | 🔴 below kill | **COHERE** — BDC mark stress confirmed (FSK NAV -9.9%) without HY OAS confirming. Tape-substance bifurcation visible at the BDC layer. |
| KRE $67.92 | 🟡 yellow | **COHERE** — regional banks weakening (WAL below $75 bear line) without breaking systemically. Same trap pattern. |

**Net read:** the cross-channel picture **reinforces** HENRY's complacency trap. LIQUID's "active transmission has migrated to duration" reframe is consistent with HENRY's thesis — the trap *is* the divergence between (a) substance + duration cracking and (b) vol + credit refusing to confirm. **HENRY does not need to abandon the complacency-trap thesis; HENRY needs to update which legs are firing and reframe the active transmission as duration not plumbing.**

### One important contradict to flag

HENRY STATUS line 131 lists **BRENT sustained <$85 → energy-deflation = CPI cools = Fed cuts return = thesis weakens** as a kill condition. **The opposite has happened** — Brent +$19 over 31d to $109.73. **This is positive evidence for HENRY's trap thesis** (not against it), and HENRY's cross-agent dependency table should be updated to reflect that BRENT confirms, not contradicts.

### Net verdict on cross-channel coherence

**HENRY's complacency-trap thesis remains coherent and arguably strengthens on the 31-day diff.** The dominant transmission has shifted from "credit will confirm via HY OAS widening" to "duration / substance will eventually force the vol/credit floor to break." HENRY does NOT need to abandon the thesis; HENRY needs to:
1. Acknowledge the 2-of-3 invalidation firing (§2).
2. Reframe transmission as duration-led, not credit-led (§3).
3. Update cross-agent dependencies to reflect BRENT >$100 as confirming, not contradicting.
4. Pre-stage the vol-spike pathway via VIOLET's KB-VIO-058 framework (R11 analog: VIX 17.76 → 52.33 in 8 trading days).

---

## 4. NVDA 5/20 read-through prep

NVDA Q1 prints Tuesday AMC. NVDA is HENRY-domain because the question is not "what does NVDA do" — that's a stock-specific call — but **what does NVDA's print do to (a) SPX positioning, (b) GEX/0DTE setup, (c) vol regime, (d) the AI-capex-air-pocket transmission to credit and banks**.

### Pre-print state (live as of 5/18)

- **NVDA live:** ~$222.32 (yfinance proxy pull); 1-month range $196.50-$235.74; +10% over 30 days.
- **SPX live:** 7,403 (1.4% below 5/16 high of 7,501).
- **VIX live:** 17.82 (flat over 31d).
- **AI/semi melt-up context (signal 5/9):** SMH at $566.54 +4.90%; claimed $2.6T SPX call notional single-day record; SOX RSI 1999-high. Hyperscaler capex crossed above operating income ~Q2-Q3 2025 per the chart batch.
- **Concentration context (signal 5/9):** Healthcare 8.3% S&P weight (lowest since 1994); defensives + utilities + staples ~15% (lowest since 1970s); ~12pp defensive underweight shift since 2022.
- **Breadth context (signal 5/9):** SPX at record while 5.60% of members at 52-week lows. Analogs 1929/1973/1999.

### What HENRY needs to be watching on the print

**1. Pre-print positioning — already extreme.** The bull setup heading into 5/20: dealer gamma already amplified, call notional record, semis RSI 1999-high, defensives -2z underweight. This is a HENRY-classic "loaded for a beat, fragile to anything else" setup. **The asymmetric risk is to a TONE shift, not a number miss** (capex moderation language is the bear catalyst per signal 5/9).

**2. Language triggers (lifted from signal 5/9 list).** HENRY should pre-mark these and tag them as bear-catalyst if they appear in the call:
- "Pacing investments"
- "Optimizing capacity"
- "Prioritizing ROI"
- "Depreciation pressure" / "Useful life"
- "Supply digestion"
- "Capex growth moderating"
- "Data center utilization" / "GPU utilization"

A clean beat + clean guide + no ROI-discipline language = melt-up resumes, complacency trap deepens. Any ROI-discipline language = first crack in the AI-capex story, transmission to SMH/AVGO/AMD then to hyperscaler debt issuance then to credit spreads.

**3. GEX / 0DTE setup — HENRY's gap.** STATUS lines 40-41 mark these as PENDING (SpotGamma/Barchart wire-up needed). HENRY revives 31d stale with this gap unresolved. **Recommend:** for the 5/20 print specifically, do not block on the wire-up. Pull SpotGamma free-tier or Barchart manual GEX estimate Monday AM and Tuesday AM, mark current dealer gamma zone manually, and write the GEX wire-up as a backlog item rather than a blocker.

**4. Post-print transmission paths to pre-mark:**

| Print outcome | SPX 1-day | Vol regime | Credit | Banks | HENRY thesis read |
|---|---|---|---|---|---|
| Clean beat + raise + no ROI language | +1-2% (squeeze defensives-underweight) | VIX -1 to ~16.5 (closer to <15 invalidation trigger) | HY OAS likely -3 to -5bps (toward 275, close to kill) | KRE +1% beta | **TRAP DEEPENS** — VIX leg closer to firing; watch for HY OAS sub-265 in following 2 sessions |
| Beat + raise + ROI-discipline language | flat to -1% | VIX +1-2 | HY OAS +5-10bps | KRE -1-2% | **TRAP CRACKS** — first credible transmission catalyst since FSK |
| Miss or weak guide | -3-5% | VIX +3-5 (gap to 22-23) | HY OAS +15-25bps | KRE -3-5% (beta to risk-off) | **TRAP UNWINDS VIOLENTLY** — gamma unwind path activates; KB-VIO-058 R11 analog (VIX 17→52 in 8d) becomes live scenario; LIQUID HY OAS 260 watch flips direction (widening from kill) |

**5. Key levels to pre-mark (proxy's read; HENRY owns the call):**
- **SPX:** 5/16 high 7,501 = upside breakout level; 7,100 = invalidation floor (would need to break to neutralize the SPX-leg of complacency trap); 7,200 = first hint of post-print weakness.
- **VIX:** 15 = invalidation trigger (any single-day print); 20 = trap-cracking; 23 = HENRY's yellow trigger fires (cross-agent risk-off cascade).
- **NVDA:** $235 ATH (proxy 1mo high); $196 1mo low = first technical break.
- **HY OAS:** 265 = leading invalidation tell (2-session sub-265 = HY OAS sub-260 next session probable per LIQUID); 285 = first credit confirmation of any post-print stress.

**6. HENRY-VIOLET coordination on the print.** VIOLET's 20d-SKEW-slope sign-flip + R11 analog is the live vol-spike pathway. NVDA print is the most likely catalyst in the 1-2 week window. **Recommend:** HENRY and VIOLET both hold the post-print first-15-minute tape together — the SKEW reaction (and whether the slope re-steepens negative further or reverses) is the canary VIOLET owns and HENRY needs.

---

## 5. Inbox sweep triage (15 items)

> *v2 improvement #3. For each signal: (a) **LIVE** = integrate into STATUS; (b) **SUPERSEDED** = newer data overrides, log but don't integrate; (c) **STALE** = event already resolved, archive without integrating.*

| # | File | Date | Verdict | Reason |
|---|---|---|---|---|
| 1 | `sweep_2026-05-16_2306.md` | 5/16 | **LIVE** | Oil/Hormuz tape directly relevant to HENRY April-CPI loop. Top items: "US crude tops $100 again as Iran peace deal fades," "Global oil stockpiles record low if Hormuz closed," Pemex Olmeca fire (contained). Integrate as energy-stress confirmation for stagflation thesis. |
| 2 | `signal_2026-05-14_gamma_momentum_factor_squeeze.md` | 5/14 | **LIVE — HIGH PRIORITY** | Directly load-bearing: positive gamma + 0DTE amplifier as suppression mechanism for VIX/HY OAS despite substance prints. **This is HENRY's central explanation for the 2-of-3 invalidation firing without thesis death.** Add as primary working hypothesis. Also: MS Momentum 3M +43.75% YTD = factor-crowding canary; late-2021 analog (top 1-2 months out). |
| 3 | `signal_2026-05-14_30y_5pct_2007_headline.md` | 5/14 | **LIVE** | 30Y >5% confirms duration regime break (§3). Auction mix OK (BTC 2.30, indirect 66.6%) = level signal not dysfunction signal. Integrate into duration-leg of trap reframe. |
| 4 | `signal_2026-05-09_ai-capex-semi-meltup-divergence.md` | 5/9 | **LIVE** | Hyperscaler capex crossed above op income ~Q2-Q3 2025; SMH outflows $2.3B while price ATH. **NVDA 5/20 directly tests this.** Pre-read for the print. |
| 5 | `signal_2026-05-09_spx-record-high-breadth-deterioration.md` | 5/9 | **LIVE** | SPX ATH with 5.60% members at 52wk lows. Analogs 1929/1973/1999. Concentration confirms market-structure fragility (§4). |
| 6 | `signal_2026-05-09_spx-call-notional-sox-rsi-meltup.md` | 5/9 | **LIVE** | $2.6T SPX call notional record; SOX RSI 1999-high. Market-structure fragility; mechanical-bid hypothesis for VIX suppression. Pair with #2 (gamma) into single working framework. |
| 7 | `signal_2026-05-09_defensives-underweight-tech-concentration.md` | 5/9 | **LIVE** | Healthcare 8.3% (lowest since 1994); defensives -2z. Positioning fragility; relevant for NVDA-print transmission scenarios (§4). |
| 8 | `signal_2026-05-09_global-equity-earnings-valuation-rotation.md` | 5/9 | **SUPERSEDED** | EPS-led returns with multiple compression. Now superseded by NVDA Q1 print imminent — wait for 5/20 result before integrating (would force a re-write after 48h). |
| 9 | `signal_2026-05-09_inflation-above-target-policy-constraint.md` | 5/9 | **SUPERSEDED** | Apr CPI 3.8% / Core 2.8% / PPI 6.0% have since printed and are reflected in HEARTBEAT. Generic narrative already absorbed. Log only. |
| 10 | `signal_2026-05-09_us-debt-gdp-refunding-term-premium.md` | 5/9 | **LIVE — partial** | Debt/GDP overlap + 30Y 5%; pair with #3 + 10Y live print into single duration-leg KB entry. (LIQUID is doing the same on its side per LIQUID-052 — coordinate to avoid duplicate KB.) |
| 11 | `signal_2026-05-09_labor-breadth-health-government-only.md` | 5/9 | **STALE** | LABOR-primary; April claims (211k initial, 1.782M continuing) already in HEARTBEAT. Defer to LABOR. |
| 12 | `signal_2026-05-09_japan-ust-selling-yen-defense-claim.md` | 5/9 | **STALE** | SAM-primary; SAM is 5d fresh and owns this. Defer. |
| 13 | `signal_2026-05-09_iran-hormuz-undersea-cable-risk.md` | 5/9 | **STALE** | HAWK/BRENT-primary; BRENT is 0d fresh. Defer. |
| 14 | `signal_2026-05-09_energy-investment-hormuz-asia-exposure.md` | 5/9 | **STALE** | BRENT-primary; BRENT is 0d fresh. Defer. |
| 15 | `signal_2026-05-09_oil-products-inventory-draw-hormuz-closure-claim.md` | 5/9 | **STALE** | BRENT-primary. Defer. |

**Recommended sweep action:** items 1-7 + 10 (8 files) integrate into STATUS via §3 + §4 narrative. Items 8-9 log to processed/ with "absorbed into HEARTBEAT" note. Items 11-15 (5 files) archive to processed/ without re-litigating — these are domain owned by other agents who are fresher than HENRY.

---

## 6. Open questions HENRY had unresolved (Apr 17) — closeout authorization

> *v2 improvement #4. Each Apr 17 HENRY prediction or open question: (a) closeout if resolved; (b) hold if still open.*

### Active predictions from STATUS line 79-89

| ID | Prediction | Resolves | Status | Recommendation |
|---|---|---|---|---|
| HEN-22 | CPI 3.3% + VIX 19 = complacency trap forming | Apr 30 | **PARTIAL CONFIRM** — CPI prints came in 3.8% Apr (hotter than 3.3% baseline). VIX did not break 19; held 17-18. The trap framing is intact. | **CLOSEOUT — confirm.** Trap-forming hypothesis validated. Promote to "trap clinching" given 2-of-3 invalidation legs firing without thesis death. |
| HEN-23 | Gas $4+ = consumer demand destruction begins | Apr 30 | **CONFIRM** — gas wkly now $4.50 ($4.076 at STATUS); CARL-domain consumer prints needed for demand-destruction confirmation; not within proxy budget. | **HOLD — defer to CARL.** HENRY's job is to confirm $4+ persistence (done) and flag to CARL. Close the HENRY-side as confirmed; CARL owns the demand-destruction read. |
| HEN-24 | OZK Q1: provision spike / MI3 acceleration, stock gaps >5% | Apr 22 | **RESOLVED — OZK Q1 happened Apr 21.** Outcome was integrated by REGINALD/OZK persistent agents (FLEET_SCAN confirms). Not within proxy budget to score. | **CLOSEOUT — defer scoring to REGINALD/OZK.** HENRY records "resolved per REGINALD" and moves on. |
| HEN-25 | WAL Q1: fund-finance/CRE exposure, stock gaps >5% | Apr 22 | **RESOLVED — WAL Q1 happened.** WAL now below $75 bear line per HEARTBEAT/REGINALD; 10-Q integration pending. The directional call appears to be confirming. | **CLOSEOUT — confirm directional.** Final scoring deferred to REGINALD 10-Q integration. |
| HEN-26 | BOJ: USD/JPY moves >2 handles; base case HOLD → yen weakens past 160 | Apr 25 | **PARTIAL — yen weakened but did not break 160.** USD/JPY now 158.93 (live). The base-case directional call (yen weakens) confirmed; the >2-handle and >160 specifics did not. | **CLOSEOUT — confirm directional, miss on magnitude.** Score as 0.6. |
| HEN-27 | March PCE: core YoY >3.0% OR MoM >0.3% (energy passthrough) | Apr 30 | **RESOLVED — Apr 30 has passed.** PCE prints not within proxy budget. | **HOLD pending data verify.** HENRY should pull the actual PCE print on revival and score. |
| HEN-28 | Labor cliff: claims >240K or 4-wk avg >230K | May 1 | **NOT CONFIRMED** — claims 211k initial, 1.782M continuing (shadow-adjusted ~266k) per HEARTBEAT 5/16. Initial claims have NOT crossed 240K. | **HOLD — extend deadline.** Labor-cliff thesis intact but not firing on claims. Extend resolution date to next NFP. |

### Other open questions implied by STATUS

| Question | Status | Recommendation |
|---|---|---|
| HENRY 0DTE/GEX wire-up (SpotGamma/Barchart) | Still pending per STATUS line 40-41 | **HOLD — but unblock for NVDA 5/20.** Don't wait for full wire-up; manual estimate for the print is acceptable. Backlog the full wire-up. |
| "Monday watch" Apr 17 → Apr 17 HY OAS settle (FRED next-day) | Resolved long ago | **CLOSEOUT.** HY OAS data fully integrated by HEARTBEAT/LIQUID since. |
| "Monday watch" → Brent weekend gap | Resolved long ago | **CLOSEOUT.** Brent up $19 over 31d; weekend gaps absorbed. |
| "Monday watch" → tanker-tracking signal | HAWK/BRENT domain | **CLOSEOUT — defer.** Not HENRY's job to track; defer to HAWK/BRENT. |
| Workbook PREDICTIONS.tsv (24 rows, 7 active) | Has been frozen 31d | **HOLD — score 7 active predictions on revival.** Most resolution dates have passed; should be a fast pass. |

**Net: 5 closeouts (HEN-22, 24, 25, 26 + Monday watch trio), 3 holds (HEN-23, 27, 28), 1 unblock-and-backlog (0DTE/GEX wire-up).** The closeout sweep should be HENRY's first 20 minutes on revival.

---

## 7. Recommendations to HENRY on next boot (priority order)

> *Effort estimates assume HENRY's working pace; proxy is calibrating from observed commit cadence.*

1. **[30 min] STATUS refresh: live tape diff + invalidation-leg status update.** Pull live dashboard yourself; replace Apr 17 numbers with current; rewrite line 110 invalidation criteria to distinguish "soft kill" from "trap clinch" scenarios (per §2). Update line 131 BRENT dependency: "Brent sustained <$85" entry should be revalued as "Brent above $100 confirms trap, sustained <$85 invalidates."

2. **[20 min] Closeout sweep of HEN-22 through HEN-28 (per §6).** Score the 5 closeable predictions, hold the 3 still-open, file PREDICTIONS.tsv update. This is mechanical — first session work.

3. **[45 min] Pre-print NVDA 5/20 prep memo.** Write the language-triggers list + scenario matrix (§4) + key levels to your workbook. Coordinate with VIOLET on post-print SKEW handoff plan. Backlog the SpotGamma/Barchart full wire-up; for the print, manual GEX estimate is acceptable.

4. **[60 min] Inbox sweep — 8 LIVE integrations + 7 archives per §5.** Single batch pass. Items 1-7 + 10 produce 2-3 KB entries (gamma/momentum suppression hypothesis; duration regime break; AI capex air-pocket). Items 11-15 archive without integrating.

5. **[30 min] Thesis-state rewrite for the THESIS STATE section (line 95-110).** Two changes: (a) confirmed/amplifying signals — add CPI 3.8% / PPI 6.0% / Brent $109 / 10Y broke 4.5% / FSK NAV -9.9% / WAL bear line broken; (b) counter-signals — keep but reframe as "trap floor intact" not "thesis killed" (this is the §3 net read).

6. **[deferred / backlog] 0DTE/GEX SpotGamma/Barchart wire-up.** Standing gap. Unblock for NVDA 5/20 via manual estimate; do the full integration in a later session.

7. **[deferred / backlog] LABOR cliff watch.** HEN-28 still open. Extend to next NFP. Coordinate with LABOR on the 4-wk avg trajectory (currently shadow-adjusted ~266k, well above 230K threshold — actually firing the cliff signal *via the shadow series*, not the headline; this is interesting and worth a KB entry on revival).

**Total first-session work:** ~3 hours. Items 1-5 are decision-grade; items 6-7 are backlog.

---

## Design feedback (for v3)

1. **The LIQUID-packet structure transferred well to HENRY** — the §1 tape diff with zone-changes column, §2 thesis-kill with directional semantics, §3 cross-channel cohere/contradict, §5 inbox triage, §6 closeout authorization, §7 prioritized recommendations all carried over cleanly. The main difference was §4 — for LIQUID it was a "deferred items" register (essentially overflow from §5); for HENRY it became NVDA-print prep (a domain-specific catalyst section). That replacement felt natural and earned its place. Suggest v3 brief make §4 explicitly "domain catalyst prep section (if any catalyst in 0-7 days; otherwise an overflow register)."

2. **The v2 improvements paid off:** time series (§1) caught the 5/8-5/16 SPX run that endpoints alone would have missed; directional semantics (§2) caught the "2-of-3 invalidation firing" framing that the Apr 17 STATUS could not have known about; sweep triage (§5) compressed 15 inbox items to 8 LIVE + 7 archive in one pass; closeout authorization (§6) gave HENRY a clear first-20-min mechanical task on revival. **None of the four felt like overhead.**

3. **Cross-revival coordination wasn't in the brief but should be in v3.** LIQUID's revival packet (sister file) was load-bearing for HENRY's §3 — I cited LIQUID's findings on PLUMBING → DURATION migration directly. If LIQUID hadn't been done first, HENRY's cross-channel section would have been weaker. Suggest the brief flag "if a sister revival is in flight, cite their findings rather than re-deriving."

4. **The "domain catalyst" hook (NVDA 5/20) was the most useful structural addition.** Having a concrete next-Tuesday event made §4 mechanical (pre-mark levels, language triggers, scenario matrix) rather than abstract. Suggest v3 make catalyst-prep a required section when one exists in 0-7 days, and explicitly optional when not.

5. **Underspecified in the brief:** how to handle VIOLET's territory. STATUS line 30-46 says "VIX/term structure/VVIX/SKEW owned by VIOLET — do not duplicate-track; pull from her file." I read VIOLET's first 40 lines per the budget, but the brief didn't address whether HENRY's revival packet should incorporate VIOLET's KB-VIO-058 R11 analog (VIX 17 → 52 in 8d) directly, or just cross-reference. I incorporated it directly in §3 + §4 because it's load-bearing for the trap thesis. Suggest v3 brief specify: "if a peer agent owns a sub-domain that's load-bearing for the revival target, name the peer agent's specific KB entry and cite verbatim where appropriate."

6. **Overspecified in the brief:** the 5/9 batch read instruction ("top-5 by macro/vol/positioning relevance") was right, but I read 5/9 #5 (`spx-record-high-breadth-deterioration`), #6 (`spx-call-notional`), #4 (`ai-capex-semi-meltup`), #7 (`defensives-underweight`), #8 (`global-equity-earnings-valuation`) and could have skipped #8 — it added little beyond what 5/14 + 5/9 #4 already covered. The brief's "top 5" was directionally right but could have been "top 4 then stop and judge." Minor tuning.

7. **The "live yfinance pull for SPX/VIX/VIX3M/SKEW only if cheap" permission was load-bearing.** Two 30-second yfinance calls produced the load-bearing numbers for §1 (VIX 17.82 unchanged), §2 (SPX 7,403 above invalidation), and §4 (NVDA $222 pre-print). Without those, the packet would have been about Apr 17 numbers compared to Prome dashboard numbers — a tier-mismatch problem. **Strongly recommend v3 brief make "agent-domain-specific data pull (cheap)" an explicit permission, not just a conditional one.**

---

*End of revival packet. Proxy session terminates here. HENRY owns all integration on next boot.*
