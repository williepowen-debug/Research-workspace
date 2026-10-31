# TRADE IDEA — UNG Jan-15-2027 10/12 call spread — US natural gas into a forecast polar-vortex break
**Date:** 2026-10-31 (written 14:03 EDT from `date`)
**Setup ID:** `IDEA-UNG-SSW-OCT31`
**Thesis owners (evidence, not TERRY's):** AEOLUS (stratospheric vortex forecast and observation, `AGENTS/AEOLUS/workbook/KB.tsv` KB-AEO-225 and KB-AEO-229, 10/29; winter-demand card C3) · BRENT (idea #3 of its 10/29 packet, `../inbox/processed/2026-10-29_from-BRENT_trade-ideas-nov1-3-cluster.md`: confidence "Low"; "an AEOLUS observed-reversal packet is the natural fire point").
**Terry verdict:** CONDITIONAL — NOT-FIRED; unapproved proposal under Will's 10/20 loosened rule (`USER.md` § Trade ideas loosened). Nothing fills before T1 fires and Will approves this card (root rule #5).
**Confidence in trade structure:** Medium (deep, two-sided chain) · **in the idea:** Low (BRENT's own grade; the forecast is public and the futures curve already prices a winter premium).
**Data freshness:** UNG $9.08 = 10/30 close (`fetch.py price`, pulled 10/31 13:47 ET; markets shut Saturday). Option quotes = 10/30 last quotes read 10/31 13:52 ET (`chain_fetch.py`): weekend SCREENING marks, quote time UNKNOWN (durable finding 5b); the order is priced on the broker chain at entry. Named futures = vendor daily bars for 10/30, not settlements (RISK_RULES 6c). EIA storage = weekly report released 10/29 (week to 10/23). AEOLUS's newest vortex reading = 10/29.

## 0. Missing inputs / hard caveats
- [x] Price checked (10/30 close) — re-check live before any fill (root rule #4)
- [x] Option chain checked — weekend screening only; broker quote at entry
- [x] Position truth: no natural-gas line in the book (FORGE mirror of Will's 10/30 capture; Robinhood unverified)
- [x] Catalyst dates: AEOLUS vortex watch to Thu 11/12; EIA storage every Thursday (next 11/5)
- [ ] AEOLUS has logged no vortex reading after 10/29. T1 needs AEOLUS (or TERRY on AEOLUS's method) to read the analysis on or before 11/12. AEOLUS's current route on an observed reversal is WATT/BRENT; if Will approves this card, PROME routes that log to TERRY
- [ ] UNG's roll dates are the issuer's (prospectus); not verified this session

## 1. One-line setup
If the forecast break of the polar vortex actually happens, buy a cheap, defined-risk January call spread on US natural gas on a red day, so a cold December–January pays and the loss is capped at about $250 if the cold never reaches the US.

## 2. Trigger state, in figures (NOT-FIRED)
| Leg | Line | State | Status |
|---|---|---|---|
| **T1 — the reversal is observed** | 10 hPa 60°N zonal-mean zonal wind **< 0 m/s** on an analysis (ECMWF, or NOAA GFS on AEOLUS's scout method), logged by AEOLUS, on or before **Thu 2026-11-12** | **+14.1 m/s [10/29 00z ECMWF analysis]** (NOAA GFS +14.28), falling ~3 m/s a day from +23.2 [10/24]. Forecast: every ECMWF product below zero 11/05–11/12, all 50 ensemble members below zero on 11/09 (mean −3.8 m/s); NOAA's GEFS dissents (floor ~+1 m/s, never below zero) | **NOT FIRED** |
| Entry window | the first **red UNG session** (root rule #6: calls on red days) after T1, through **Fri 2026-11-20** | — | waits on T1 |
| **Void before entry** | no observed reversal by 11/12 · or the broker-chain debit exceeds **$0.50** · or UNG closes ≥ **$10.40** before entry (the move is already priced) · or no red UNG day by 11/20 | — | — |

**Construction rule #15 check:** this gate opens on the thesis variable strengthening (forecast → observation), not on decay, so a fire is information for the card, not against it. **But an observed reversal is only the first of three steps:** AEOLUS's C3 rule is that a stratospheric warming reaches US heating demand only through persistence, downward coupling and regional surface cold, with a 1–4 week lag. The trigger buys the first step; the money needs all three.

## 3. Chart / tape read (10/30 close)
| Item | Read |
|---|---|
| UNG | **$9.08** (−1.09%, red); 60-bar range $9.08–$11.55 — **at the low of the range**; −6.78% over the window vs SPY −2.03% (`snapshot.py`, 60 of 60 bars) |
| Gas curve (vendor bars, 10/30) | December NGZ26 **$2.90** · January NGF27 **$3.37** · February NGG27 **$3.03** — the market already prices January **16% over December** (the winter premium) |
| Storage | **3,724 Bcf** [10/23], **+1.0% vs the 5-year average**, −3.8% vs last year (EIA weekly report, released 10/29) — no surplus cushion, no shortage either |
| Seasonal outlook | CPC 10/15 Dec–Feb leans **WARM**: Mid-Atlantic 40% above normal, East North Central 40–50% (AEOLUS C3) |
| Volatility | Jan-15 calls **72.6% implied at the 10 strike, 78.9% at 12** — upward skew, so a call spread sells the richer wing |
| Liquidity | 10C open interest 31,202, bid/ask 0.83/0.88 (5.9% of mark); 12C 33,917, 0.45/0.50 (10.5%); no quote defects on the strip |
| Global context (BRENT, 10/28, intraday) | US gas ~$2.94 vs European TTF above €100: export capacity, not price, limits the pull; context, not a leg |

## 4. Entry
- **Trigger:** T1 above (AEOLUS-logged observed reversal by 11/12).
- **Preferred entry:** the first red UNG session after T1; one complex order, never legged.
- **Do not chase:** net debit > **$0.50** (25% of width) on the broker chain → no order; UNG ≥ $10.40 at entry → no order.
- **If missed:** no red day by 11/20 → the card dies; no re-strike without a new card.

## 5. Structure
| Item | Figure (10/30 last quotes, screening) |
|---|---|
| Instrument | **UNG Jan-15-2027 10C long / 12C short, ×5** |
| Debit | worst case (ask − bid) **$0.43**; mid $0.38 |
| Order | net debit limit **≤ $0.50** |
| **Max loss** | **$256.50** at the limit = 5 × $50 + $6.50 assumed fees (0.65 per contract per side; budget arithmetic, not an account certification) — **$221.50** at Friday's worst-case $0.43 |
| Max gain | 5 × $200 − $256.50 = **$743.50** at UNG ≥ $12.00 on 1/15 (at the limit) |
| Breakeven at expiry | **$10.50** (+15.6% from $9.08) at the limit |
| Payoff ratio | **2.90 : 1** at the limit (3.51 : 1 at $0.43) |
| Days to expiry | 76 from 10/31 |
| What it needs in gas terms | UNG +15.6% ≈ December gas $2.90 → ~$3.35 before UNG's roll, or January gas ~$3.37 → ~$3.90 after it. **Because January already sits 16% over December, the card needs cold BEYOND the winter premium the curve already prices.** UNG holds the front-month contract and rolls ahead of expiry (December → January → February over the card's life; exact dates per the issuer, not verified here) |
| Alternatives considered | **Dec-18 10/12C ×5:** worst $0.35 ⇒ max loss $181.50, ratio 4.5 : 1 — cheaper, but only ~5 weeks after an 11/12 trigger, short of a 1–4 week coupling lag plus persistence (construction rule #16) · **outright Jan 10C ×3:** ~$266 for uncapped upside, but pays the full 72.6% implied volatility with no wing sold · **a gas producer (e.g. EQT):** adds equity beta and hedge-book noise · **futures:** not available in the IRA |

**Why this expression:** the view is a dated weather tail with a 1–4 week lag, so it wants weeks of tenor (construction rule #16) and a capped premium. The spread sells the 12 strike at ~6 volatility points richer than the 10 it buys, and the Jan-15 expiry covers the coupling window plus about a month of persistence.

## 6. Risk / scoring

### 6a. EFFECTIVE-N — independence audit (RISK_SCORING §2b)
| Field | Entry |
|---|---|
| **N_claimed** | 3: ECMWF's unanimous reversal forecast · storage near normal (no surplus to absorb a cold shock) · Europe's high gas price keeps US export demand running flat out |
| **Shared antecedent** | actual US surface cold in December–January beyond the winter premium already priced: the reversal must couple down and land on the US, and the other two legs only matter if it does |
| **N_eff** | **1 → sized as ONE small view** |
| **Book check** | No gas line is held. The oil sleeve (USO 30 sh, USO Nov-20 170C ×1, VLO 3 sh) is driven by Brent and the war, not US weather, so this card adds one independent view rather than stacking on an existing one. A cold snap would also stress PJM's thin evening supply cushion (WATT, 10/29): context, not a leg |

- **Risk unit / max loss budget:** $256.50 at the limit, about half the **$500/card default** (low-confidence idea). **X1 sizing gate: CLOSED — DON'T-SIZE.** The default is therefore no fill; a fill at ×5 is Will's per-card choice against X1, never pre-approved.
- **Energy stand-down:** HEARTBEAT carries "energy STAND DOWN". Its ruling, WQ-192 (Will 9/7, the Kylo sinking), is a no-deploy on BRENT's oil frame-breaker pair; on its letter it does not reach a US natural-gas weather structure. If Will reads it more widely, this card waits for his word on that as well.
- **Edge estimate:** **small and not demonstrated.** The forecast is public (gas traders watch the same ECMWF products), UNG sits at its 60-bar low with December gas at $2.90, and the curve already prices a 16% January premium. The card's only informational step is waiting for the forecast to become an observation, then requiring a red day.
- **Kelly reference:** no p_model for the payoff; edge undemonstrated ⇒ no Kelly size; capped at about half the default by judgment.
- **Sizing proposal:** **×5**, limit ≤ $0.50 (`risk_calc.py --premium 0.50 --max-loss 260`: 5 contracts, $250 premium before fees).
- **Invalidation:** no observed reversal by 11/12 (the card dies unfilled); after a fill, AEOLUS logs no downward coupling by Fri 12/4.
- **Gap/event risk:** a warmer December forecast can gap UNG down 5–10% in a session; weekly storage surprises move gas a few percent. The spread caps the loss at the debit.
- **Liquidity / spread check:** acceptable (open interest above 30,000 at both strikes; 5.9% / 10.5% bid-ask on Friday's last quotes).
- **Execution block:** Will's [Approve] on this card · T1 logged · red UNG day · broker-chain debit ≤ $0.50 · UNG < $10.40.

## 7. Target / management (written before any fill)
- **Harvest (durable finding 9):** sell the spread when it marks **≥ $1.00** on the broker bid (2× the limit, 50% of width). At ×5 ≈ $500 proceeds, ≈ +$243.50 before closing fees.
- **Kill:** AEOLUS has not logged downward coupling (its C3 reach condition) by the close **Fri 2026-12-04** → sell at the bid.
- **Time stop:** sell by the close **Fri 2027-01-08** (one week before expiry) if neither has fired. No roll pre-registered (Non-Negotiable #6).
- Forward max loss after a fill is the remaining mark (construction rule #20(d)).
- **Review cadence:** each AEOLUS vortex read to 11/12; after a fill, weekly at the EIA storage release (Thursdays) and at AEOLUS's C3 reads.

## 8. Why not / counter-trade
- **A stratospheric warming does not reliably deliver a US cold winter on cue.** The reversal can couple down over Europe or Asia instead, or not at all; AEOLUS's lag is 1–4 weeks and the landing is regional.
- **The seasonal outlook leans warm** (CPC, 10/15), and El Niño plus a westerly QBO make the vortex "stronger and more stable" (AEOLUS, PMD): the forecast break runs against that background.
- **NOAA's GEFS does not forecast a reversal at all.** ECMWF's skill edge in the stratosphere is the reason to wait for the observation rather than buy the forecast.
- **The curve already prices winter:** January $3.37 vs December $2.90.
- **UNG loses on the December → January roll when the curve is in contango,** so a slow, partial cold can leave the spread worthless even if gas rises somewhat.
- Positive expectancy is **not** demonstrated; this is a small, uncorrelated weather tail, sized as one.

## 8b. Trigger forecast (WQ-493 A)
- **Trigger event:** AEOLUS logs an analysis value of the 10 hPa 60°N zonal-mean zonal wind below 0 m/s (a major stratospheric warming) on at least one day.
- **Deadline:** Thu 2026-11-12, 23:59 ET.
- **Resolution basis:** AEOLUS's KB row in `AGENTS/AEOLUS/workbook/KB.tsv` citing the ECMWF 00z analysis or the NOAA GFS analysis on its scout method (KB-AEO-225/229); if AEOLUS is not woken by the deadline, TERRY reads the same NOAA GFS analysis and says so.
- **Probability:** **0.70 (subjective, TERRY's)**, from AEOLUS's KB-AEO-229 evidence: every ECMWF product below zero 11/05–11/12 and all 50 members on 11/09, deterministic runs deepening; against it, GEFS never below zero and El Niño with a westerly QBO stabilizing the vortex. Row `CAL-0003` in `CALIBRATION.tsv`. This grades the TRIGGER, not trade profit.

## 9. Decision
- [ ] APPROVE as written: UNG Jan-15-2027 10/12C ×5, limit ≤ $0.50, max loss $256.50 — NOT-FIRED, entered only after T1 and on a red UNG day
- [ ] APPROVE alternative: Dec-18 10/12C ×5, max loss ≈ $181.50
- [ ] REJECT
- [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. Chain, price and storage evidence: `../research/2026-10-31_trade-ideas/` (`chains_screening.txt`, `prices_1030close.txt`, `REPORT.md`).
