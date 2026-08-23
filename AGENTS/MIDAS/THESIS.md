# MIDAS — THESIS (per-channel transmission tables)

**The one-line thesis:** metals are two distinct macro tells — a **monetary** channel (gold/silver: fiscal debasement, real-rate divergence, safe-haven stress) and an **industrial** channel (copper/PGMs: global growth, China demand, supply shock) — and MIDAS owns both, keeping each channel's signal separate so the fleet reads the right message from the right metal.

*Richness lives here; STATUS.md carries the live 5-pt matrix. Each channel is `event → mechanism → repricing` with a stage table (state ∈ confirmed / open / falsified).*

---

## MONETARY CHANNEL

### M1 — Gold — debasement / real-rates (the core monetary tell)

> **✅ 2026-07-17 RESOLUTION STAMP (read before the 7/12 derivation below):** **M1 v2 is now CONFIRMED** — both catalyst tests resolved and survived: **MIDAS-03 (CPI 7/14) = HIT/v2-consistent** (cool CPI, but real yields refused to fall and gold got no premium bid → re-coupled/capped), **MIDAS-04 (China GDP 7/15) = NO-FIRE** (gold no haven spike on the miss). **Polarity FLIPPED**: `metals_watch.py` now treats CONVERGE=quiet (rc=0), DIVERGE=REVIEW (rc=1). **LIQUID curve check consumed (KB-026):** the "higher-rate bets" attribution for the 7/16 sub-$4k break is refuted (DGS2 −8bp 4.21→4.13); gold-down = real-yield **LEVEL** cap + **positioning** unwind, NOT a rate-repricing, and NOT an EndGame confirm while DXY 100.75 soft. **Gold-level ownership settled: MIDAS is metals-board canonical, LIQUID consumes.** The 7/12 scoreboard below stands as the derivation record; the live state lives in STATUS.md.

| Stage | Mechanism | State |
|---|---|---|
| 1 | Real yields set the classic opportunity-cost anchor for gold | confirmed (DFII10 2.32 [7/15], elevated near series high 2.36 [7/13]) |
| 2 | Fiscal debasement + central-bank de-dollarization buying bid gold ABOVE what real rates justify | **open — UNTESTED this session** (see Stage 3 correction; distinct from Tier-2's multi-year backdrop, which this 90d pull doesn't reach) |
| 3 | Gold holds/rises despite rising real yields → the debasement premium is confirmed | **CORRECTED 2026-07-12** (gold −18.6% while DFII10 +36bp, real-rate-consistent CONVERGE, KB-005) → **RESOLVED 2026-07-17: the delta-premium stays FALSIFIED and v2's re-coupling is CONFIRMED** — MIDAS-03 HIT (cool CPI, gold still no premium bid). The premium lives in the LEVEL (+24% YoY), not the delta. |
| 4 | A monetary/fiscal stress event → gold spikes as the safe-haven + debasement trade | open (the systemic event) |

**Repricing:** gold as a monetary-stress read (→ BOND real-rate seam, LIQUID safe-haven). **Confirms/breaks:** gold holding through rising real yields confirms the premium; gold converging back down to real rates falsifies it — **the trailing 90d data sits on the falsification side of that line**, not yet a verdict (one window). **Tier-1 vs Tier-2 distinction (load-bearing):** gold's absolute level ($4,113.70) is still historically extraordinary — that multi-year ascent may still be Tier-2 structural debasement evidence. What Stage 3's correction shows is that the *marginal, live* (Tier-1) move is currently real-rate-consistent, not an additional above-and-beyond premium. Both can be true at once; don't conflate the level with the delta. Re-test at MIDAS-03 (CPI 7/14 reaction) and MIDAS-01 (9/30).

### M1 v2 — re-derived driver structure (2026-07-12 round 2, PROME/Will-directed)

*Round 1's correction killed the simple "structurally bid vs real rates" frame. This is the replacement — each candidate mechanism worked with data, not narrative.*

**Anatomy of the move (yfinance GC=F daily closes):** gold ran **$3,317.40 [7/10/25] → $5,318.40 peak close [1/29/26] = +60% in ~6.5 months**, then fell to **$4,113.70 [7/10/26] = −22.7% off the peak, still +24.0% YoY**. The −18.6% 90d window (3/13→7/10) starts just below that top — **it is the back half of a blow-off retracement, not a fresh regime break.**

**Mechanism scoreboard:**

| Candidate mechanism | Evidence FOR (source, date) | Evidence AGAINST | Verdict |
|---|---|---|---|
| **Blow-off mean-reversion** | +60% parabola into the 1/29/26 peak; the measured window starts near the top; COMEX gold OI washed out **~528k → ~326k contracts (−38%) Jan→Jun** [CFTC 6dca-aqww, weekly]; the Feb OI cliff (528k→410k, 1/20→2/3) coincides exactly with the first leg down off the ATH | Gold still +24% YoY — not a round-trip; mean-reversion alone can't say where the floor is | **PRIMARY size-setter.** −18.6%/−22.7% is a positioning unwind's magnitude, not a rates re-pricing's |
| **Real rates (opportunity cost)** | Direction matches the whole window: DFII10 +36bp (1.95→2.31, 4/10→7/9 [FRED]) while gold fell monotonically across 5 monthly markers; WGC's June flows commentary attributes the exit to "expectations of higher rates ahead" under the hawkish Warsh Fed [gold.org, June 2026 ETF flows report] | Magnitude wildly exceeds any plausible gold/real-rate beta — +36bp does not price −18.6% on its own | **Direction-setter, not size-setter.** The cyclical layer has *re-coupled* to real rates post-blow-off |
| **ETF flows** | June 2026: **−US$8.9B / −74t, global holdings → 4,047t** [WGC gold.org]; North America −$5.5B June, −$7.7B H1 (weakest H1 since 2013); Asia −$2.3B June (worst month ever, China-led) | H1 2026 net flows still **+US$8B** — the exit is a June acceleration, not year-long | **Amplifier of the unwind** — the fast-money layer exiting confirms the mean-reversion mechanics |
| **COT spec positioning** | Net NC long fell **251,238 [1/13] → 154,260 [5/26]** as the washout ran | **Rebuilt 154k→194k during June while price kept falling** [CFTC, 6/2→7/7 weekly]; net/OI back to 52.2% | **Confirms the washout happened; warns it may be incomplete.** Specs dip-buying into a falling tape = unwind fuel if the floor fails, not capitulation |
| **Central-bank buying (structural)** | Q1 2026 net purchases **243.7t vs 237.0t Q1-25 (+3% YoY); above 5-yr avg + prior quarter — CONF via WGC primary [gold.org GDT Q1 central-banks page, round-3]**; Poland +31t, Uzbekistan +25t, Kazakhstan +12t, PBoC +7t, Czech/Malaysia +5t. *(The "17th consecutive month" streak + 700–900t FY target were NOT on the fetched WGC section — STAY PROVISIONAL; GDT Excel file 403-gated to automated pull = documented wall.)* | Turkey ~−70t (+80t via swaps), Azerbaijan −22t, Russia −22t, Bulgaria −2t sold; 243.7t/q did NOT stop a −22.7% drawdown | **Tier-2 layer INTACT (core figures now CONF).** Sets the *floor*, not the *price*. Not falsified by round 1 — never the marginal driver |
| **USD path** | — | DXY 100.36 [3/13] → 100.97 [7/10] = **+0.61%, flat over the exact window** [yfinance DX-Y.NYB] | **NOT a driver this window.** Rules out the dollar-squeeze explanation (also consistent w/ LIQUID's EndGame DXY leg not firing) |

**M1 v2 statement (falsifiable):** gold's price = a **structural CB-floor layer** (~244t/q official buying, de-dollarization motive, largely insensitive to real rates) **plus a cyclical speculative layer** (ETFs, COMEX specs, retail) that blew off into late January 2026 and is now mean-reverting, **re-coupled to real rates as its direction-setter**. The "debasement premium" is real but lives in the **LEVEL** (gold +24% YoY with DFII10 at 2.31 — far above any real-rate model), not in the **DELTA** (marginal moves now track real-rate direction). Read the monetary tell accordingly: *direction of marginal moves* = rates story; *height of the eventual floor above the $3,317 pre-run shelf* = debasement story.

**What CONFIRMS v2 (testable dates):**
1. **CPI 7/14 (MIDAS-03): ✅ RESOLVED HIT 2026-07-17.** The print was *cool* (not the hypothetical hot print), yet real yields refused to fall (DFII10 2.36 [7/13]→2.32 [7/15]) and gold got no disinflation/premium bid — the re-coupled cyclical layer behaved exactly as v2 expects. Confirmed.
2. **WGC Q2 GDT (~late July):** CB net buying ≥150t = structural layer intact. *(Still pending — kill-cond #2.)*
3. Gold basing in **$3,700–4,300** while DFII10 holds 2.2–2.5 = the floor forming well above the pre-run shelf. **✅ roughly where we are** (gold $4,021.90, DFII10 2.32).

**What KILLS v2:**
1. **Structural-floor failure:** gold closes below **$3,317** (7/10/25 pre-blow-off close) without a major real-yield spike (DFII10 still <2.6) → the CB floor isn't where v2 says; re-derive again, escalate BOND/LIQUID.
2. **CB-buying collapse:** WGC Q2 <100t net (or net selling) → the structural layer's premise is gone.
3. **Re-decoupling UP:** gold rises through *rising* real yields sustained **3+ weeks** → the "re-coupled" claim is dead; that's a v1-style premium reassertion — a *bigger* monetary-stress signal, escalate rather than celebrate.

> **SELF-RULED 2026-08-21 (DELEGATION_TIER) — L-12: does kill-cond #3's "sustained 3+ weeks" require the joint condition to hold CONTINUOUSLY, or ENDPOINT-to-endpoint?**
> → **Ruled: the duration unit is a WEEK (Friday-to-Friday close); the basis is ENDPOINT-to-endpoint over 3 weekly intervals; the DAILY-continuous reading is EXCLUDED as arithmetically unsatisfiable; and every grade must PRINT BOTH readings plus the three weekly joint-up signs.** Tests 1–5 PASS. Riders: R1 applied (dated); **R2 satisfied by non-modification** — the registered sentence above is UNCHANGED, this block adds the reading it was missing and supersedes no text; R3 applied (no confidence, probability or weight moved in this edit).
>
> **Why daily-continuous is excluded, and it is arithmetic rather than preference:** measured over **DFII10 × GC=F, 2003-01-02 → 2026-08-19, n=5,892 sessions** — the longest run of consecutive sessions with *both* gold up and DFII10 up **in the entire 23-year record is 4**. Windows satisfying 15/15 (3 trading weeks): **0**. Satisfying even 5/5: **0**. A reading under which the condition has never once been satisfiable is not a candidate reading.
>
> **The two surviving readings, base-rated on 1,133 rolling 3-week windows (weekly Friday sampling, 2004-11 → 2026-08):**
>
> | Reading | Satisfied | Base rate | Note |
> |---|---|---|---|
> | **ENDPOINT-to-endpoint** ✅ *ruled* | 217 | **19.15%** | GLD cross-check 211 / **18.62%** |
> | Weekly-continuous (3-of-3) | 9 | **0.79%** | GLD 10 / 0.88% — **24× harder** |
>
> **Weekly-continuous is a strict SUBSET of endpoint (0 contradictions in 1,133 windows)** — the readings are nested, so a continuity rule can only ever *un-fire*, never fire something endpoint did not.
>
> **⚠️ WHY I RULED THE DISAMBIGUATION AND NOT THE DIFFICULTY — the tier forbids the latter in BOTH directions.** DELEGATION_TIER test 4 fails a ruling when *"a falsifier becomes harder to trigger, **or** a threshold becomes easier to satisfy."* Kill-cond #3 is **both** — a falsifier of v2 **and** the M1→4 escalation trigger — so **any** change to its difficulty fails test 4 whichever way it points. What remains self-rulable is exactly what L-12 actually complained about: the sentence had two defensible readings and the grader picked one under pressure. **That ambiguity is now closed; the difficulty is untouched.** Three re-tunings that would change it are **escalated to Will, not banked** — weekly-continuous (24× harder), a NO-VERDICT band around the boundary (harder), and 5-session smoothed endpoints (measured **+2.5% easier**, 239→245 of 1,230).
>
> **⚠️ RETROACTIVITY — stated, because a ruling governs the next write and not the existing state.** Under the ruled basis the **7/17→8/7 fire STANDS** (+9bp DFII10, +8.17% gold, endpoint SATISFIED; GLD +8.16% agrees). Under the escalated weekly-continuous reading it would **NOT** have fired — the joint condition held **1 of 3** weeks (wk1 +12bp/+1.37% ✅ · wk2 +4bp/**−0.45%** ✗ · wk3 **−7bp**/+7.20% ✗) — which would take the fired-count 1/4 → 0/4. **I am not authorised to make that change and have not made it:** the tier explicitly withholds authority *"to grade, resolve, or re-mark a prediction."* Will's call, packet sent.
>
> **📏 CORRECTION TO L-12's OWN TEXT:** L-12 records the alternative reading as *"yields rose for 2 of 3 weeks then eased 4bp = not satisfied."* On the Am.#2-corrected figures the **joint** condition held **1 of 3**, not 2 of 3 — "2 of 3" describes the **yield leg alone**; gold *fell* 0.45% in week 2, so that week fails the conjunction independently. The conclusion (not satisfied) is unchanged; the count was wrong.
>
> **What the grade must print from now on (the L-11 pattern — when two windows disagree, print both, the disagreement IS the finding):** endpoint Δyield + Δgold · the 3 weekly joint-up signs · the magnitude check against the empirical beta · and both GC=F and an unrolled cross-check.
>
> ⚠️ **This rule governs kill-cond #3 ONLY. It does NOT govern `MIDAS-06` branch (a)**, whose letter is a single-date LEVEL conjunction (`gold ≥ $4,340.70 AND DFII10 ≥ 2.40` read 2026-08-28) with **no duration clause at all** — see the correction filed with this ruling.
>
> **✅ THE THREE ESCALATED RE-TUNINGS ARE RULED (Will, 2026-08-21, WILL_QUEUE rows 65-67; record `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md` — cited, not reconstructed; encoded here 2026-08-23):** **(e) weekly-continuous 3-of-3 = DECLINED** — the endpoint basis above STANDS as ruled, the retroactive re-mark was REFUSED, and **kill-cond #3's fired count 1/4 STANDS**; any future continuous basis is prospective-only and needs its own sitting. **(f) NO-VERDICT band = HELD until after MIDAS-06 grades 8/28, then adopt PROSPECTIVELY for successor rows only** — never the graded row; re-present ~8/29 (PROME DOCKET row registered, owner PROME→Will, not MIDAS's to chase). **(g) 5-session smoothed endpoints = DECLINED for live rows** — measured **+2.5% easier**, so it fails test 4 clause 2 on the letter; available only as a prospective design choice proposed at a future sitting.

**MIDAS-03 resolution (2026-07-17, HIT):** graded on the v2 mechanism (premium-reassertion vs re-coupling), since the actual CPI day had real yields −3bp DOWN, not the "yields up" both pre-written branches assumed (branch-coverage lesson L-10). No premium reassertion → no BOND/LIQUID escalation. The escalation case remains `gold rising THROUGH rising real yields sustained 3+wk` (v2 kill-cond #3) — now the `metals_watch.py` REVIEW trigger post-flip.

### M2 — Silver + gold/silver ratio

| Stage | Mechanism | State |
|---|---|---|
| 1 | Silver = monetary demand + industrial demand (dual nature) | open |
| 2 | Gold/silver ratio signals risk-appetite / monetary vs industrial balance | LIVE (2026-07-12): GSR 68.37 [GC=F/SI=F, 7/10], benign (<Y85) |
| 3 | GSR spike (>95) = risk-off / monetary-fear regime | open — no spike |

**Repricing:** GSR as a risk-appetite/monetary gauge (→ LIQUID). First pull closed 2026-07-12 (round 1); wired into `metals_watch.py`.

---

## INDUSTRIAL CHANNEL

### I1 — Copper — Dr. Copper / China (the growth thermometer)

| Stage | Mechanism | State |
|---|---|---|
| 1 | Copper demand tracks global industrial activity + China (the marginal buyer) | confirmed (structural) |
| 2 | Copper price + LME/COMEX inventory signal demand direction | BOTH legs LIVE w/ DEFINED baseline (round-3): price +10.5% vs 200dma, +9.2% QoQ; **LME stocks 306,500t [7/10, westmetall/LME]** = **+28.0% vs the trailing-2yr rolling median (239,400t, n=507) → YELLOW band**; 83rd pct of the 2.5yr series; but **−23.9% off the 4/15 peak (402,625t)** = drawing down ~3 months, tightening |
| 3 | Copper roll + inventory build = confirmed demand inflection (not positioning noise) | open — NOT met: the conjunction requires copper −20% AND inv +100% *vs the 2yr median* (≈479kt); current is price UP + inventory Yellow-but-falling. ✅ Threshold-definition gap CLOSED (round-3, KB-018): "+X% vs normal" now grades against the **trailing-2yr rolling median** (implemented in metals_watch.py leg 6, auto-updating), replacing the round-2 "+110.9% YTD" artifact of a multi-year-low Jan start. ✅ MIDAS-04 RESOLVED NO-FIRE (China Q2 GDP 4.3% miss, NBS 7/15): copper HELD (−0.5% 2-sess) = structural/AI-grid demand, not cyclical weakness. Next test: MIDAS-05 (China LPR ~7/20) |

**Repricing:** copper as the cleanest China-growth thermometer (→ ZHAO two-way, HENRY velocity). Price + inventory legs both closed 2026-07-12 (inventory via westmetall.com scrape, wired into `metals_watch.py`); **MIDAS still owes** the China-imports pull.

> **SELF-RULED 2026-08-21 (DELEGATION_TIER) — L-13: every registered I1 trigger is a DOWNSIDE band, so a physical *tightening* regime scores ⚪ "benign." Add an upside band?**
> → **SPLIT RULING. (a) SELF-RULED: I1's matrix cell must now distinguish `⚪ BENIGN` (scored and quiet) from `⚪ UNSCOREABLE↑` (the tape is moving in a direction the registered bands cannot score), and any I1 band call must carry its baseline value AND the baseline's as-of date. (b) NOT SELF-RULED — ESCALATED: adding an upside/tightening band fails test 4 and goes to Will, with a specced design and the evidence below.** Tests for (a): 1–5 PASS. Riders: R1 applied; R2 satisfied by non-modification (no registered band changed); R3 applied.
>
> **Why (b) is not mine:** an upside band creates a **new way for I1 to score elevated**, which is test 4's second failure clause — *"a threshold becomes easier to satisfy."* An agent whose seat is justified by producing signal must not self-grant a new way to produce it.
>
> **🔴 AND THE TAPE HAS ALREADY ARGUED AGAINST THE NAIVE VERSION — this is the substantive reason to escalate rather than ship.** L-13 was written 8/7 on a "fast physical tightening": LME copper crossing from **+16.4% above** the 2yr median to **−9.2% below** it in 15 days. It then deepened — and **reversed**:
>
> | Date | LME Cu | vs 2yr median |
> |---|---|---|
> | 22 Jul | 284,175t | +18.2% |
> | 07 Aug | 222,975t | −7.2% |
> | **14 Aug (trough)** | **204,975t** | **−14.7%** |
> | 18 Aug | 223,550t | −7.0% |
> | **20 Aug** | **239,925t** | **−0.2%** |
>
> **+17.1% restock in 4 business days**, with copper price flat ($6.48→$6.50). **A tightening band added on 8/7's evidence would have fired and then un-fired inside 9 business days.** The right band therefore needs a **sustain requirement** — and that exposes the second defect below.
>
> **⚠️ THE BASELINE IS TRACKED, NOT FROZEN — so a "sustained N sessions" band on it is incoherent as-written.** The I1 baseline is a *trailing-2yr rolling median* (L-07, auto-updating in `metals_watch.py` leg 6). It moved **244,025t → 240,325t** between 8/14 and 8/21, so **the same 8/13 tonnage that graded −14.9% on 8/14 grades −13.6% today.** A band call is therefore **only reproducible as-of its date**, and a sustain clause could un-fire because the *baseline* moved rather than the metal. Any upside band must **freeze the baseline for the duration of its own test window**. *(This is a defect in the existing downside bands too — flagged, not repaired: repairing it changes their difficulty.)*
>
> **⚠️ AND AN UPSIDE BAND IS NOT THE MIRROR OF THE DOWNSIDE BAND.** The downside has one dominant mechanism (demand collapse → growth roll), which is why `copper −20% AND inventory +100%` reads as a growth tell. The upside has **at least four**, and **three are not growth tells**: (i) genuine demand strength; (ii) **supply disruption** (Chile/Peru outage) — a supply squeeze, macro-opposite; (iii) **structural/AI-grid electrification** — my own MIDAS-05 finding, copper rallying *through* a no-stimulus LPR hold; (iv) **exchange-arbitrage relocation** (COMEX↔LME warrant shuffling on tariff spreads), which is not a demand signal at all. **A symmetric band would manufacture a China-growth reading out of a warehouse transfer.** ⇒ the escalated design is a **discriminated** band, not a mirrored one.
>
> **What (a) changes in practice, starting this session:** I1 no longer reports ⚪ without saying which direction the bands can and cannot see. **L-13's stated harm was that ⚪ implies quiet — that harm is fixed by disclosure, and the band is a separate, larger question that is Will's.**
>
> **✅ (b) IS RULED (Will, 2026-08-21, WILL_QUEUE row 69; record `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`; encoded here 2026-08-23): the design constraint is RATIFIED; NO build is commissioned.** If/when an I1 upside/tightening band ever ships, it MUST take the discriminated form specced above — **discriminated by mechanism · conjunction-based · sustain clause · baseline FROZEN for the test window — never a symmetric mirror** (the ruling adopts this desk's own tape test: a mirror band shipped on 8/7 evidence would have fired and un-fired inside 9 business days, and a symmetric band manufactures a China-growth reading out of a warehouse transfer). **Building it remains its own future escalation with measured difficulty effect.** ⚠️ **Explicitly left OPEN by the ruling (the recs took no position): the downside-band tracked-baseline defect** flagged above stays **FLAGGED-NOT-REPAIRED at this desk** — escalate it as its own sub-item with the measured difficulty effect when repair is wanted.

### I2 — PGMs (platinum / palladium)

| Stage | Mechanism | State |
|---|---|---|
| 1 | PGM demand = auto catalysts + industrial | open; price leg LIVE (2026-07-12): Pt $1,629.00 (+0.6%), Pd $1,276.30 (+2.6%, 90d strength) |
| 2 | Supply concentrated in South Africa + Russia = structural fragility | confirmed (structural); **Russia-Pd antidumping now CONF (round-3): final margin 132.83%, Russia-Wide Entity, Fed Reg 2026-08487 [5/1/26]** — resolves the round-2 132.83/828 conflict (828 was preliminary). WPIC ~240koz 2026 Pt deficit + SA power/flooding STAY PROVISIONAL (WebSearch, not primary-verified this round) |
| 3 | SA/Russia supply disruption/sanction → PGM supply shock | sanctions leg RESOLVED: the AD determination is *final* (132.83%, priced) — not an acute-outage/new-shock event. No confirmed acute SA/Russia *production* outage. Separate CVD final (doc 2026-10342, 5/22) + USITC injury (2026-12219, 6/18) |

**Repricing:** PGM supply consequence of SA/Russia events (→ HAWK geopol, HENRY auto/industrial). Price leg closed 2026-07-12; **MIDAS still owes** primary-source verification of the supply backdrop (currently PROVISIONAL) + a HAWK cross-flag.

---

## Why the two channels stay separate (the core discipline)

Monetary and industrial metals send **different messages** and can move **independently without contradiction**: gold up on debasement + copper up on growth is a coherent "reflation" read; gold up + copper down is "stagflation/risk-off." Collapsing them into "metals up/down" destroys the signal. MIDAS's job is to keep M-channel (monetary stress) and I-channel (industrial demand) as distinct tells and hand each to the right consumer.

## Boundaries (reconcile-to-one-figure, don't silo)

- **BOND** owns the real-rate level; **MIDAS** owns gold's divergence from it (the debasement premium).
- **ZHAO** owns China macro; **MIDAS** owns copper as its physical-demand thermometer.
- **LIQUID** owns credit/liquidity; **MIDAS** owns gold/silver safe-haven flow as an amplifier.
- **HAWK** owns geopolitics; **MIDAS** owns the PGM-supply repricing.
- **HENRY** owns macro velocity; **MIDAS** supplies the copper/PGM growth-tell.
