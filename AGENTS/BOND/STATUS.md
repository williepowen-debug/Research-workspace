# BOND — Status

**Agent:** BOND | **Domain:** US Bond Market Structure (+ MBS/FHLB + EU rates per 6/27 extension, integrated 7/1)
**State:** 🟡 WATCH, **escalating** — the long end is re-engaging: 30Y **~5.00** (intraday 7/6, AT the threshold line) the day before the 7/9 reopen, into the July supply gauntlet with dealer inventory at a **fresh all-time record** and **no Fed coupon backstop** (post-QT Fed buys bills, not coupons — QT ended Dec-1-2025).
**Last Updated:** 2026-07-06 (Mon, teams session) by BOND — live refresh + QT-framing fix + BND-11 refunding pre-reg reconciled with LIQUID (ONE figure)
**Thesis:** durable thesis → `thesis/THESIS.md` (**v1.1**, bumped 7/1)

---

## Regime (one-line)

Phase-III long-end re-fire, **globally synchronized**: domestic hawkish-data repricing (JOLTS beat, ISM prices 73, Dec-hike ~79–82%) co-firing with a **JGB super-long rout** (6/30 30Y +8.8bp; weakest JGB 20Y auction since May-2025) into the 7/7–9 mini-refunding — while auctions still clear at price (**6 straight benign tests**) but with **indirect bids fading hard** (<60% at 2Y/7Y, rotated 1:1 to directs) and FR2004 dealer long-end stock at a **fresh record** ($74.6B 11–21Y, →4 trigger ARMED; 6/24 print pending). **QT-framing corrected 7/6:** QT ended Dec-1-2025 → Fed now buys **T-bills, not coupons** (RMPs) → **no Fed bid at the coupon/long end**, so 7/9 30Y absorption is entirely private/foreign/dealer. Credit: issuance **boom** (record June IG), headline calm, CCC tail sticky. Composite **12/35** (+1 via long-end 2→3).

---

## Current Dashboard

| Metric | Current | Status | Source / Date | BOND Read |
|---|---:|---|---|---|
| 30Y yield | **~5.00%** | 🟠 | [CONF ^TYX intraday, 7/6] | **AT the 5.0 line** (was 4.97 close 7/1) the day before the 7/9 reopen. BND-12 tests the *sustain* — 1–2 pokes don't falsify; only a 5-session hold. |
| 10Y yield | **4.48%** | 🟡 | [CONF ^TNX intraday, 7/6] | Flat; a few bp *through* the June 4.538 stop (market rallied into the reopens). Below 4.6 trigger. |
| 5Y / 2Y | 4.22 / 4.17 | 🟡 | [CONF ^FVX intraday 7/6 / DGS2 7/1] | Belly steady; Fed-path repricing still a real component (not pure term premium). |
| 10Y real (DFII10) | **2.25%** | 🟡 | [CONF FRED, 7/1] | +5bp off 2.20 (6/30) — real-rate leg ticking back UP toward the 2.5 re-arm after the late-June retrace. Not there; watch. |
| 5Y5Y fwd (T5YIFR) | **2.20%** | 🟢 | [CONF FRED, 7/1] | Anchored. Kinetic Iran exchange 6/25–28 bought only ~2–6bp — the oil→BE re-arm bar is HIGH (KB-064). |
| 10Y BE (T10YIE) | 2.23% | 🟢 | [CONF FRED, 7/1] | Compressed with oil through the window. |
| HY OAS | **275bps** | 🟢 | [CONF FRED `BAMLH0A0HYM2`, 7/2] | 263 trough (6/17) → 283 peak (6/26) → 275, flat through the holiday. Below 300 watch line. Credit inert — not the story this week. |
| CCC OAS | **971bps** | 🟡 | [CONF FRED, 7/2] | Still elevated, no retrace — default-cycle tail residue. Ratio ~3.5x. |
| IG OAS | 75bps | 🟢 | [CONF FRED, 7/2] | Flat; RECORD June issuance ~$175–187B absorbed 3.9x oversubscribed. |
| JGB 30Y | **3.873%** | 🟠 | [CONF MOF, 6/30] | +8.8bp 6/30 rout (super-long-led; 2Y JGB *fell*); ~3.96 TE-intraday 7/1 (different basis — use MOF). |
| USD/JPY | ~162 | 🟠 | [CONF multi-source, 6/30–7/1] | **40-year yen low**; Mimura first verbal warning since 6/5. Actual intervention = mechanical UST reserve selling (FL-BND-11). |
| FR2004 11–21Y | **$74.6B** | 🟠 | [CONF NY Fed API, as-of 6/17] | **Fresh all-time record** (+11.4% over 5/27). Combined long-end $174.5B #2 ever. **6/24 print (rel. 7/2) PENDING pull** — decisive dealer-absorption 3-vs-4 input; re-grade when it lands. |
| SOFR−IORB | **+3bps** | 🟢 | [CONF FRED, 6/30] | Quarter-end only: SRF take-up **$0** both ops, RRP $26.9B one-day blip. Watch normalization 7/2. |
| TLT | $85.31 | 🟡 | [CONF yfinance, 7/6] | −0.24% d/d, drifting lower with the long end; puts working, no add-gate fired. |
| VIX / KRE / HYG | 16.6 / 76.18 / 79.59 | 🟢 | [CONF yfinance, 7/1] | Risk-ON selloff tell: banks rallying while duration sells = policy repricing, not growth fear. |
| Brent | ~$71 | 🟢 | [CONF yfinance BZ=F, 7/1] | Fell THROUGH the kinetic window (OPEC+ 4th hike + de-escalation-from-crisis-baseline). Decoupling test resolved benign. |
| Energy HY OAS | *285 [STALE Apr 28]* | 🟡 | LIQUID owns | **Structurally unpinnable from public primaries** (FRED has no sector OAS; `…EY` = effective yield). Needs ICE access — stays [STALE]. |
| Fed b/s (WALCL) | $6.736T | 🟢 | [CONF FRED, 6/24] | **QT ENDED Dec-1-2025** (FOMC Oct-29). Fed now buys **T-BILLS** (RMPs + MBS-principal reinvestment) → **no coupon/long-end bid**. Active MBS sales deferred ("years, not months," Sintra 7/1). *Corrected 7/6 in `AUCTION_FRAMEWORK_from_LIQUID.md`.* |

---

## Auction Read — 6/23–25 cluster (RESOLVED, grade C+) + July gauntlet

| Date | Tenor | Size | BTC | High Yield | Indirect | Direct | PD | Read |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 6/23 | 2Y (91282CQY0) | $69B | 2.64 | 4.189% | **55.45%** | 34.31% | 10.24% | 0.3bp **stop-through**; HY highest since Jan-25; dealer take lowest since Feb. |
| 6/24 | 5Y (91282CQX2) | $70B | 2.35 | 4.200% | 61.60% | 25.51% | 12.89% | **0.7bp tail — 8th consecutive tailing 5Y**; indirect −13.3pp m/m. |
| 6/25 | 7Y (91282CQW4) | $44B | 2.50 | 4.260% | **57.55%** | 29.70% | 12.75% | Indirect −20.8pp m/m; tail **unpinnable** (treat as unknown). |

**Read:** no hard stress marker (nothing near BTC <2.3 / tail >1.5bp / dealer spike) — **6th straight benign test**. The story is **composition**: foreign/custodial (indirect) bid faded hard at the belly, absorbed ~1:1 by domestic directs — *rotation, not hole*; dealers were NOT stuffed. Composes with TIC-April private outflow (KB-049) + UST allocation multi-decade low (KB-057) → VX-08/13 → 3. **Next gate: 7/7 3Y · 7/8 10Y-R · 7/9 30Y-R** (settle 7/15) — **BND-11** pre-registers 70% benign; the 7/9 30Y into a **~5.00 tape**, record dealer stock, and **no Fed coupon backstop** is the single most important print of the month.

> **🔴 BND-11 refunding pre-reg — RECONCILED WITH LIQUID (ONE figure): `BND11_REFUNDING_PREREG_2026-07.md`.** BOND owns mechanics + term-premium; LIQUID owns absorption + plumbing; **both grade to ONE metric: 30Y indirect as % of _competitive accepted_ vs the June 6/11 = 60.0% benchmark.** The reconciliation that matters: a *mechanically clean* print (no tail, firm BTC) with **indirect <55% + directs/dealers backfilling** is the **masked demand-hole** — it scores BND-11 TRUE yet still escalates the thesis. Acute (BND-11 FALSE): indirect <52% AND (BTC<2.3 OR tail>2bp) AND dealer>18–20%.

---

## Global Long-End — JGB/FX panel (new, channel 6)

Japan's super-long demand vacuum is real and worsening (6/25 20Y JGB BTC 2.97x = weakest since the May-2025 rout; lifers net sellers; rinban stepped down to ¥2.5T/mo **effective 7/1**; BOJ stood aside through an 8.8bp 30Y rout) — but the 6/20–7/1 window shows **duration decoupling, not competition**: after the weak JGB 20Y, USTs *rallied* four sessions to a 7-week low. The 6/30–7/1 co-selloff had different signatures (JP: pure super-long steepener, 2Y −3/30Y +9; US: near-parallel +4–7bp policy repricing). **The armed transmission leg is FX:** yen 162+ (40-yr low), record ¥11.7T already spent Apr–May, Mimura verbal warning 7/1 — *actual* MOF intervention = mechanical selling from $1T+ UST reserves. Watch: **7/2 10Y JGB auction · USD/JPY 165 · BOJ 7/31.** Full read → KB-BND-065; reply to SAM in `outbox/`.

## New Coverage Baseline (7/1) — MBS/FHLB + EU rates

- **MBS/housing (VX-17, score 1):** primary spread ~200–205bp (at/below median — but *policy-compressed* by the Jan-26 GSE $200B purchase directive); CC spread ~100–110bp [EST]; Fed MBS $1.96T passive runoff. Catalyst-monitored: Warsh active-sales (deferred to 2027 lane), GSE-release execution.
- **FHLB advances (VX-18, score 1):** $734B (3/31/26), +8.4% Q/Q (driver unattributed — read Q1 CFR narrative), ~30% below the 2023 SVB peak. Coordinate with REGINALD.
- **EU rates (VX-19, score 2):** **ECB is HIKING** — depo 2.25% (6/11, first since 2023, war-inflation), ≥1 more priced, full QT; bund 2.94%, 2s10s +42bp; **OAT-Bund 77bp** (+10 in June; France trades on top of Italy at 73bp). Next GovC 7/23-or-24 (**verify date**). Converge xccy-basis number with LIQUID (proxy build needed).

---

## Convergence Matrix

| Vector | Score | Independence | Status | Evidence | Upgrade Trigger |
|---|---:|---|---|---|---|
| Treasury auction health | 2 | VX-08 (indirect), VX-09 (tail), VX-13 (FOI/TIC) roll up here — primary-demand; counted once. | 🟡 | 6/23–25 cluster C+ no-marker (6th straight benign) BUT indirect <60 at 2Y/7Y, rotated to directs (KB-060). | Any BND-11 marker at 7/7–9: (tail>1.5bp AND ind<60) OR BTC<2.3 OR dealer>20%. |
| HY market function | 1 | VX-11 (CCC quality-tail) rolls up; HY-spread root; counted once. | 🟢 | HY 275 (<300); issuance BOOM (Apr $40B; zero pulled deals). CCC 970 non-retrace caveat. | HY >300 watch; >350 + pulled deals = red. |
| IG market function | 1 | VX-10 (IG primary) rolls up; IG-spread root; counted once. | 🟢 | IG 76; RECORD June ~$175–187B, 3.9x books. | +20bps/wk OR clustered pulled deals. |
| Dealer absorption | **3** | VX-16 (buyback offer/accept) rolls up; dealer-stock root; counted once. | 🟠 | FR2004 6/17: 11–21Y $74.6B **fresh all-time record**; flow benign (cluster takes 10–13%). **→4 trigger ARMED.** | Fresh highs (7/2 print) + weak auction (7/9 30Y) → 4. |
| Long-end / duration | **3** ↑ | VX-12 (term prem), VX-14 (real/BE), VX-15 (5Y5Y) roll up; duration root; counted once. | 🟠 | 30Y **~5.00 intraday 7/6** (at the line), globally-synchronized re-fire (JGB co-firing); DFII10 back UP to 2.25 (7/1). Stays 3 (poke ≠ 5-session hold). | 10Y >4.6 OR 30Y >5.0 held **5 sessions** + weak auction, OR DFII10 >2.5 → 4. |
| CDX-cash basis | 1 | Standalone proxy; not double-counted. | 🟢 | 6/24–26 z-breach (−3.28) **failed the sign-check** — cash widened concurrently = co-move, not divergence; normalized 7/1 (−0.17). | Proxy z20 < −1.5 while cash HY stays TIGHT, OR VIOLET skew-vs-flat-cash. |
| Credit-equity lead | 1 | Timing lens keyed off HY OAS; setup read, not an added level. | 🟢 | HY +12bp off trough w/ VIX 16.6 — magnitude nowhere near the arm. | HY OAS +75–100bp from the 263 trough (≈338–363) while VIX <20. |
<!-- Independence column added 2026-07-01 by PROME (DAEDALUS BOND-SWEEP-A, Will-approved); preserved through the 7/1 BOND rewrite. -->

**Composite: 12/35** (was 11/35 on 6/20; +1 from long-end 2→3) — 2 vectors at 3, 1 at 2, 4 at 1. *New-coverage vectors (VX-17 MBS = 1, VX-18 FHLB = 1, VX-19 EU rates = 2) are tracked in `workbook/VX.tsv` OUTSIDE the composite to keep it comparable; they enter the matrix when they earn weight.* The configuration to respect: **record dealer stock + fading indirects + a 30Y 3bp from threshold + a supply gauntlet** — every piece of the demand-hole scenario is pre-positioned except the trigger itself (a failed auction). Six straight benign tests say the trigger keeps not firing (BND-11: 70% benign); the tape says the cost of being wrong is now concentrated in the 7/9 30Y print.

---

## Trade Interface (full view in `thesis/THESIS.md`)

- **TLT puts — HOLD, no add.** 30Y is **at ~5.00 intraday (7/6)** but that's a *poke, not a 5-session hold* — **no pre-registered add-gate has fired**: DFII10 2.25 (ticking up, not >2.5), no sustained breach, no auction marker yet. Add-gates: (a) DFII10 >2.5 sustained; (b) 30Y >5.0 / 10Y >4.6 held 5 sessions + weak auction; (c) a real marker at the **7/7–9 refunding** (BND-11 FALSE / reconciled verdict ③). The 7/9 30Y is the live gate.
- **HYG puts — stay closed.** Issuance boom, zero pulled deals; reopen the thesis only on HY OAS >300 with velocity.
- **Credit-equity lead — inactive.** Reactivate on HY +75–100bp from the 263 trough while VIX <20.

## Exit / Falsification (full set → `thesis/THESIS.md`)

- **Thesis kill:** genuine demand hole — BTC <2.3 **and** tail >2bp **and** dealer take spike **and** SOFR-IORB positive (non-quarter-end). OR 10Y <4.15 sustained 3 sessions with clean auctions. *(Neither near: SOFR-IORB +3 was clean qtr-end, SRF $0.)*
- **TLT puts kill:** 10Y <4.15 AND 30Y <5.0 for 3 sessions AND a clean refunding.
- **Convergence downgrade:** dealer-absorption →2 if the 7/2 FR2004 print shows a sharp drawdown off the 6/17 record; long-end →2 if 30Y closes back <4.85 for 3 sessions without auction stress.
- **Time-based:** 7/7–9 refunding is a mandatory re-grade (BND-11); BND-12 resolves 7/24; BND-01 resolves end-July; 60-DTE review on any options leg.

---

## Immediate Catalysts (docket = `docket/CATALYSTS.tsv`, same event set)

| Date | Catalyst | What BOND watches |
|---|---|---|
| ~~Thu 7/2~~ | FR2004 as-of 6/24 released · 7/7–9 sizes announced · 10Y JGB auction | **6/24 FR2004 print PENDING pull** (→4 input still open); sizes/JGB to reconcile next session |
| ~~Sun 7/5~~ | OPEC+ meeting | Fired — breakeven leg only, bar HIGH; BRENT owns |
| **Tue–Thu 7/7–9** | **Mini-refunding: 3Y (7/7) · 10Y-R (7/8) · 30Y-R (7/9)** | 🔴 **BND-11 predicates; 7/9 30Y = the month's decisive print** (record dealer stock + **~5.00 tape** + no Fed coupon backstop). Reconciled grade card → `BND11_REFUNDING_PREREG_2026-07.md`. Results ~1pm ET each day. |
| Wed 7/8 | June FOMC minutes | Hike-dissent breadth; task-force color |
| Wed 7/22 · Thu 7/23 | 20Y reopening · 10Y TIPS (new) · ECB GovC (7/23-or-24 — **verify**) | vs STRONG 6/16 20Y · real demand · 2nd ECB hike? (VX-19) |
| Mon–Tue 7/27–28 | **2Y+5Y same day (7/27)** + 7Y (7/28) | Compressed month-end cluster; indirect-fade trend test (VX-13 →4 candidate) |
| Tue–Wed 7/28–29 | FOMC (no SEP) | ~29% hike priced; hawkish-hold + long-end break = regime re-read |
| Fri 7/31 | BOJ decision | Post-Tankan hike odds; FL-BND-11 FX leg |
| Wed 8/5 | QRA (pattern-inferred — **verify**) | Coupon-size guidance |
| Watch | **MOF FX intervention (actual)** 🔴 · Warsh task force (end-2026) · buyback accept-cap | UST reserve selling = FL-BND-11 fires · 2027 lane · YCC-lite tell |

---

## BOTTOM LINE

**The long end is re-engaging — and this time it's global.** 30Y is **AT ~5.00 intraday (7/6)** the day before the 7/9 reopen, driven roughly equally by domestic hawkish-data repricing (JOLTS beat, ISM prices, Dec-hike ~80%) and Japan's super-long rout (weakest JGB 20Y demand since the 2025 rout; BOJ standing aside; yen 40-yr low with MOF intervention risk = mechanical UST selling). Auctions still clear — six straight benign tests — but the **composition is deteriorating** (indirects <60% at two of three June tenors), **dealer long-end inventory is at a fresh all-time record**, and — corrected this session — **QT ended Dec-1-2025 so the Fed buys T-bills not coupons: there is no Fed bid under the 7/9 30Y.** Every piece of the demand-hole configuration is pre-positioned except the trigger. **The decisive print is the 7/9 30Y reopen (BND-11, 70% benign), now graded on ONE reconciled figure with LIQUID** — 30Y indirect (comp-acc%) vs the June 60.0% benchmark, where a *clean-but-composition-soft* print (<55% indirect, directs/dealers backfilling) is the masked hole even if BTC/tail read benign. **TLT puts HOLD, no add** — add-gates pre-registered; DFII10 ticked to 2.25 (toward the 2.5 re-arm) but isn't there. Credit is a non-story at the index level (HY 275, IG 75), CCC tail (971) the only residue.
