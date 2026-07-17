# MIDAS — STATUS

**Last Updated:** 2026-07-17 early PM ET (review-and-grade session: MIDAS-03 + MIDAS-04 graded, polarity FLIPPED, MIDAS-05 staged, two-channel week read) · prior full session 2026-07-12 (3 rounds) · **Status:** 🟡 monitoring (all 4 channels live; nothing firing; **M1 v2 CONFIRMED by both catalyst tests — polarity now UN-frozen/flipped**)
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR/LME live via `metals_watch.py`; COT 12-mo arc + WGC-primary CB + Fed-Register PGM sanctions established)

> **All prices Fri 7/17 ~12:55 ET (COMEX futures via yfinance, live intraday/last-close) unless noted.** FRED DFII10 is T+1: latest available obs is 2026-07-15.

> **✅ POLARITY — FLIPPED 2026-07-17 (was FROZEN):** both M1 v2 catalyst tests resolved this week and v2 SURVIVED — **MIDAS-03 (CPI 7/14) = HIT/v2-consistent**, **MIDAS-04 (China GDP 7/15) = NO-FIRE**. Per the PROME-round-3/Will-approved conditional, `metals_watch.py`'s M1 classifier polarity is now **INVERTED**: **CONVERGE (gold re-coupled, inverse to real rates) = quiet baseline (rc=0)**; **DIVERGE (gold holding/rising THROUGH rising real yields = premium reassertion, v2 kill-cond #3) = the REVIEW trigger (rc=1)**. Verified: current CONVERGE state now returns rc=0. Header + verdict-block + SCRATCH updated. Flagged to PROME (pre-authorized action, not a new decision).

---

## HEADLINE — M1 v2 CONFIRMED (read this first)

The closure week was a **natural experiment for v2** and v2 won on both channels. **Monetary:** gold FELL over the week (**$4,104.10 [7/10] → $3,985.60 [7/16], sub-$4k, → $4,021.90 [7/17]**) despite TWO classically gold-bullish catalysts — a **cool June CPI** (hdln −0.42% MoM, core 0.0%) and a **6-night war escalation** — because **real yields refused to fall** (DFII10 2.36 [7/13 series high] → 2.32 [7/15]; BOND's 86%-real-yield/term-premium move) and the war transmitted through the **RATES channel, not the haven channel** (WALTER SIG-011: energy→rate-bets→gold headwind). Gold is **re-coupled to real rates and capped by them**; the debasement premium lives in the **LEVEL** (+24% YoY, CB floor 243.7t Q1 intact), not the delta. **Industrial:** copper **HELD** ($6.26–6.33) through a **China GDP miss (4.3% YoY, weakest since Q4-2022)** + reported China Cu imports −41.3% YoY + a falling LME stock — reading **structural/AI-grid demand + visible tightness, NOT China cyclical weakness**. The two channels **diverged**, and that divergence is the polarity datum: **NOT reflation, NOT risk-off — the THIRD state (high-real-rate regime + structural-industrial demand)**. Kill-triad still 0/4 fired.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates (**v2, CONFIRMED**) | **2 🟡** | **v2 confirmed by CPI+GDP tests.** Gold re-coupled, capped by series-high real yields; broke sub-$4k into a war escalation via the RATES channel (7/16), recovered $4,021.90 (7/17). CB floor intact (243.7t Q1 — CONF, WGC primary). No debasement-premium reassertion despite cool CPI + war | monetary root (shared w/ M2) | gold **$4,021.90** [GC=F, 7/17]; DFII10 **2.32** [FRED, 7/15]; peak 2.36 [7/13] | DIVERGE (gold rises through rising yields) sustained 3+wk = premium reassertion → 3-4 + escalate BOND/LIQUID; gold <$3,317 w/o yield spike → floor failure, re-derive; break <$4k + COT capitulation → positioning/real-yield unwind (an EndGame signature ONLY if DXY squeezes UP >102-103 — LIQUID's gate; DXY 100.75 soft now), cross-flag LIQUID |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | GSR **71.46** [computed, 7/17] — up from 68.37 (7/10) but well below Yellow(85). Silver **−5.9%** on the week ($59.81 [7/10] → $56.26 [7/17]), underperforming gold = mild risk-appetite softening, not a risk-off spike | monetary root (shared w/ M1) + industrial overlap | GSR 71.46; silver **$56.26** [SI=F, 7/17] | GSR >85 sustained 3+ sessions → 2; >95 → 4 |
| **I1** | Copper — Dr. Copper / China | **1 ⚪** | Copper **held** through the China GDP miss (2-session −0.5%). **LME stocks 300,600t [16 Jul]** = **+24.3% vs the trailing-2yr median (241,750t) → benign band** (slipped just under Yellow+25 as inventory drew further down), **−25.3% off the 4/15 peak (402,625t) = falling**. Growth-firm + tightening, not demand-collapse | industrial/China root | copper **$6.26** [HG=F, 7/17]; LME 300,600t (+24% vs 2yr-med) [7/16] | copper QoQ <−5% sustained → 2; LPR hold + copper −5% in 2 sess (MIDAS-05) → yellow; conjunction fire (5) needs copper −20% AND inv +100% (≈484kt) — both far off |
| **I2** | PGMs (platinum/palladium) | **2 🟡** | Platinum **$1,610.50** (−1.5% 7/17), Palladium **$1,253.00** (−0.8% 7/17) — both softened on the week, consistent w/ mild industrial-demand caution, no supply shock. Russia-Pd antidumping margin **132.83% final** (Fed Reg 2026-08487, 5/1 — priced). WPIC ~240koz 2026 Pt deficit + SA power/flooding still PROVISIONAL | supply root (SA/Russia) | Pt $1,610.50 / Pd $1,253.00 [PL=F/PA=F, 7/17]; AD margin 132.83% [Fed Reg, 5/1] | confirmed major SA/Russia outage → 4 (sanction determination final, priced) |

**Composite: 6/20** *(M1 2 + M2 1 + I1 1 + I2 2). Held from 7/12 — the two catalyst tests sharpened confidence (v2 confirmed) without moving any score. I1 band eased Yellow(+28%, 7/10)→benign(+24%, 7/16) as LME drew down further.*

**Independence note:** the two channels are **NOT co-moving** the risk-off way (gold up / copper down). This week: gold DOWN (rate-driven), copper FLAT-firm (structural-demand-driven) — a **"high-real-rate + structural-industrial-demand" third state** (KB-MIDAS-009/024), confirmed on a live natural experiment. Count the (absent) shared risk-off root once.

---

## LIVE CHANNEL READS (sourced + dated)

- **M1 — Gold — debasement / real-rates (v2 CONFIRMED)**: gold **$4,021.90** [GC=F, 7/17]; DFII10 **2.32** [FRED, 7/15], peak **2.36** [7/13, series high per BOND]. Week path: $4,104.10 [7/10] → $3,997.0 [7/13] → $4,061.1 [7/14, CPI +1.60%] → $4,044.0 [7/15] → **$3,985.60 [7/16, sub-$4k]** → $4,021.90 [7/17]. 90d divergence: DFII10 1.9→2.32 (+42bp), gold −12.6% = **CONVERGE** (re-coupled, v2-consistent). **MIDAS-03 GRADED HIT**: cool CPI, but real yields refused to fall and gold got no disinflation bid → re-coupled/capped, no premium reassertion (KB-021). **WALTER SIG-011**: gold broke $4k INTO the 7/16 war escalation, NOT de-risking (KB-025). **CORRECTION — LIQUID curve check (KB-026):** the Yahoo "higher-rate bets" mechanism is refuted by the tape — DGS2 (2Y) FELL 8bp this week (4.21→4.13 [7/10→7/15], MIDAS-verified vs FRED) and DFII10 ticked DOWN off its 7/13 peak. So gold's sub-$4k dips = real-yield **LEVEL** opportunity-cost cap + **positioning-unwind** fuel (specs 52% of OI net-long into a falling tape), NOT a rate-hike repricing. The "gold weakness ≠ risk-on" conclusion holds; the causal story is corrected. CB floor intact (243.7t Q1, CONF WGC primary). Gold-leg for LIQUID EndGame: $4,021.90 above $4k close, leg **NOT fired** (dipped $3,963 intraday 7/17). **Not an EndGame confirm while DXY 100.75 soft** — a real liquidity event pairs gold-down with a dollar-squeeze UP; this is benign opportunity-cost/positioning (LIQUID, EndGame 1-of-4). Routes to BOND (real-yield level) + LIQUID (safe-haven / EndGame).
- **M2 — Silver + gold/silver ratio**: silver **$56.26** [SI=F, 7/17], −5.9% on the week; GSR **71.46** (up from 68.37, benign, well below 85). Silver's underperformance = mild risk-appetite fade, not risk-off. Routes to LIQUID.
- **I1 — Copper — Dr. Copper / China**: copper **$6.26/lb** [HG=F, 7/17]. **MIDAS-04 GRADED NO-FIRE**: China Q2 GDP 4.3% YoY MISSED 4.5% (NBS 7/15, weakest since Q4-2022, H1 4.7%) yet copper held — 2-session $6.29 [7/15] → $6.30 [7/16] → $6.26 [7/17] = −0.5%, far short of the −5% trigger; I1 did NOT fire (KB-022). **LME stocks 300,600t [16 Jul]**: +24.3% vs the 2yr median (241,750t) = **benign** (eased under Yellow), −25.3% off the 4/15 peak = falling. Discrimination: copper reads structural/AI-grid demand + tightness, NOT China cyclical softness — reconciles PROME's 7/16 seam to ONE story w/ ZHAO. **China Cu imports −41.3% YoY** [BRENT 7/17] = ZHAO's series, base-effect UNVERIFIED (YoY). Cross-flag ZHAO — LPR ~7/20 (MIDAS-05). 
- **I2 — PGMs**: platinum **$1,610.50** [PL=F, 7/17, −1.5%], palladium **$1,253.00** [PA=F, 7/17, −0.8%] — both eased on the week. Russia-Pd antidumping **132.83% final** (Fed Reg 2026-08487, 5/1; POI Jan-Jun 2025; CVD doc 2026-10342, USITC injury 2026-12219) — priced. WPIC ~240koz Pt-deficit + SA power/flooding stay PROVISIONAL. Cross-flag HAWK (supply geopol).

**Inherited cross-agent context:** BOND owns the real-rate level (2.32 [7/15]/peak 2.36 [7/13]) M1 is re-coupled to; ZHAO owns China demand + the −41.3% import series + LPR; LIQUID owns the EndGame gold leg MIDAS confirms live (above $4k, not fired).

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 (v2) | v2 kill-triad: gold <$3,317 w/o yield spike (floor failure) · WGC Q2 <100t (CB collapse) · gold re-decouples UP 3+wk (premium reassertion) | gold $4,021.90, +21% above the $3,317 shelf; CB Q1 243.7t; re-coupled (CONVERGE, gold DOWN as yields held high) | **NOT-FIRED** (all three clear) |
| M2 | gold/silver ratio >95 sustained (risk-off) | GSR 71.46, below Yellow(85) | NOT-FIRED |
| I1 | copper −20% AND LME inventory +100% (demand collapse) | copper held (−0.5% on the GDP miss); LME stocks **falling** −25.3% off peak (300,600t [7/16]) | NOT-FIRED (both legs directionally opposite) |
| I2 | major SA/Russia PGM supply outage/sanction | structural deficit + sanctions final/priced, no acute outage | NOT-FIRED |

**Fired-count: 0 of 4.** **v2 status:** CONFIRMED by both catalyst tests (MIDAS-03 HIT, MIDAS-04 NO-FIRE) → polarity flipped. v2's kill-triad now the standing watch; the UP-decoupling leg (gold rising through rising yields) is the one to escalate on — it would be a *bigger* monetary-stress signal than v2 itself.

**Cleanest bidirectional flip (BRENT discipline), v2 edition:** if gold *bases $3,700–4,300 while DFII10 holds 2.2–2.5*, v2 confirmed (floor forming above the pre-run shelf) — **this is roughly where we are** (gold $4,021.90, DFII10 2.32); if gold *breaks <$3,317 without a real-yield spike*, v2's floor is falsified. Other direction: a sustained UP-decoupling re-falsifies v2's "re-coupled" claim = escalate, don't celebrate.

---

## OPEN ON MIDAS (next session)

1. **MIDAS-05 (China LPR ~7/20 → copper 2-session reaction)** — pre-staged, grades ~7/23. **VERIFY the exact LPR date** vs pbc.gov.cn (convention = 20th; 7/20 is a Monday) AND reconcile ZHAO's docketed 7/21 (1-day fork). Mechanical read staged in PREDICTIONS.tsv.
2. **WGC Q2 GDT (~late July) = v2 kill-condition #2 test (<100t kills the CB floor)** — calendar it. GDT Excel (file 20499) 403-gated to automated curl (documented wall, L-09); WGC web pages carry the figures. "17th consecutive month" streak + 700–900t FY target still need a primary confirm.
3. **MIDAS-01 cushion thinning** — gold $4,021.90 is now only ~8.6% above the $3,702.33 falsify line (was ~10%+); dipped $3,963 intraday 7/17. Still OPEN, DFII10 2.32 >2.0. Watch the $4k close.
4. **Remaining PGM PROV legs** — WPIC ~240koz 2026 Pt-deficit + SA power/flooding vs the actual WPIC platinum quarterly (sanctions leg CONF at 132.83%).
5. **COT weekly-cadence wiring** — lightweight weekly leg (the 12-mo arc pull was manual Socrata).
6. **China Cu imports −41.3% YoY [BRENT 7/17]** — base-effect check owed (ZHAO's series; my 7/12 palladium/base-effect lesson applies). Does it reconcile with firm price + falling LME? (destocking/base-effect, not demand collapse — provisional read).

---

## BOTTOM LINE

**MIDAS 2026-07-17: the closure week was a natural experiment and M1 v2 won on both channels — polarity now flipped from FROZEN to live.** Monetary: gold fell over the week and broke sub-$4k into a 6-night war escalation, but through the RATES channel (energy→rate-bets→headwind, WALTER SIG-011), not de-risking — because real yields held near a series high (DFII10 2.36 [7/13]) and refused to fall on a cool CPI. Gold is re-coupled to and capped by real rates; the debasement premium is in the LEVEL (+24% YoY, CB floor intact), not the delta. **MIDAS-03 graded HIT (v2-consistent).** Industrial: copper HELD through a China GDP miss (4.3%, weakest since Q4-2022) + reported imports −41.3% YoY + a falling LME stock — reading structural/AI-grid demand and visible tightness, not China cyclical weakness. **MIDAS-04 graded NO-FIRE**, reconciling the copper-strength-vs-GDP-miss seam to one story with ZHAO. The two channels **diverged** — gold down (rate-driven), copper firm (structural-demand-driven) — and that divergence is the datum: the market is pricing a **high-real-rate / term-premium stress regime (BOND's complex), not a growth-collapse and not a debasement panic.** Both catalyst tests survived → `metals_watch.py` polarity flipped (CONVERGE→quiet, DIVERGE→the alarm). Next: **MIDAS-05** (China LPR ~7/20, staged to grade itself ~7/23), the WGC Q2 GDT CB-floor kill-test (~late July), and the thinning MIDAS-01 cushion (gold ~8.6% above its falsify line).
