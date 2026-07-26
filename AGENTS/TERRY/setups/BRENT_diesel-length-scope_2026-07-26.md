# SCOPE DELIVERABLE — long diesel / distillate expression at retail scale
**Setup ID:** `TRY-BRENT-DIESEL` · **Class:** SCOPE (BRENT-requested ranked structures, not an armed card)
**Date:** 2026-07-26 (Sun) · **Thesis owner:** BRENT (framework: GS Commodities 7/20 *"Hedging Escalation With Diesel Length"*)
**Request:** `inbox/2026-07-21_from-BRENT_diesel-expression-scope-request.md` — Will-approved exploration 7/21. *"Deliverable = 2-3 ranked structures with live marks → Will [Approve/No]."*

**Terry verdict:** 🟡 **CONDITIONAL — and specifically, NOT AT MONDAY'S PRICE.**
The thesis is **confirmed and arguably strengthening**. The refiner-equity channel has **already paid most of it**. The one clean entry rule was satisfiable **Friday** and will not be Monday.

> ⚠️ **All marks below are Friday 2026-07-24 closes** — markets are shut and this was built Sunday. **Barred from use at fill (rule #4).** Re-pull live before any [Approve].

---

## 1. The thesis metrics, re-checked live — BRENT's framework holds, with one important refinement

BRENT's 7/21 framework cited: OECD diesel stocks 4th percentile since 2017 · diesel premium ~$80/bbl · European diesel margin record >$60/bbl (Russian products halt from Ukrainian refinery strikes = structural) · NYMEX 3-2-1 crack record **$64.58** on 7/8.

**Computed from Friday's closes** (CL $89.31/bbl · BZ $96.78 · RB $3.2516/gal · HO $4.0954/gal):

| Crack | Now | vs BRENT's cited level | Read |
|---|---|---|---|
| **Diesel (HO) crack** | **$82.70/bbl** | vs ~$80 → **+$2.70** | ✅ **at/above** the framework level |
| Blended 3-2-1 | **$59.07/bbl** | vs $64.58 record → **−$5.51** | off the record |
| Gasoline (RB) crack | $47.26/bbl | — | **the weak leg** |

> **★ The refinement that matters for construction: the blended 3-2-1 is off its record entirely because of GASOLINE, not diesel.** The diesel crack is *above* the level BRENT's framework was built on. **This strengthens the diesel-specific thesis and simultaneously argues against gasoline-weighted expressions** — which is most US refining yield. Any equity proxy dilutes the diesel signal with the weak gasoline one. **Flagging to BRENT as a question I can't answer: which listed refiner has the highest distillate yield?** I will not assert yield splits — that's domain data, not construction.

**Two events since BRENT wrote the request (7/21), both material:**
1. 🔴 **Jazan refinery struck 7/25** (400kbpd, Houthi missiles, Saudi-Houthi truce broken after four years). **This is the correctly-signed event for THIS trade and the wrongly-signed one for crude length** — a refinery outage destroys *refining* capacity (product-bullish, crack-widening) while freeing the crude that fed it (crude-neutral-to-bearish). Per `finding_analogue_asset_class_must_match`: Abqaiq was crude *processing*, Jazan is *refining* — **opposite sign.** **Diesel/cracks is the instrument Jazan actually argues for.**
2. ✅ **BRENT's overlap warning went LIVE** — the USO call spread it flagged as "armed, not deployed" **was filled 7/24 (~$300)**. §5 now aggregates a real book, not a hypothetical one.

---

## 2. Vehicle assessment — BRENT's menu (a)–(d), answered

| # | Vehicle | Verdict | Evidence |
|---|---|---|---|
| **(d)** | **UHN** (US Diesel-Heating Oil Fund) | 🔴 **CONFIRMED DELISTED** | yfinance returns *"possibly delisted; no price data"* over 6mo. BRENT said "confirm, don't assume" — **confirmed. There is no US-listed pure diesel/heating-oil fund.** This is the structural reason the trade has to be expressed by proxy at all. |
| **(a)** | **NYMEX ULSD (HO) options** | 🔴 **OUT — scale, not preference** | HO contract = **42,000 gallons**. At $4.0954/gal that is **~$172,000 notional per contract.** Against a $200–500 max-loss budget the position is unsizable — a single option is lumpy against the entire budget, and there is no fractional version. Separately, **futures options access needs broker confirmation** (Will's flow reads as Robinhood, which does not offer them) — but the notional math kills it regardless of broker. |
| **(c)** | **CRAK** (VanEck Oil Refiners ETF) | 🔴 **OUT — liquidity** | Options exist (4 expiries) but Dec-18 quotes are unusable: **spreads 30–88% of mark** on 10 of 15 strikes, OI in single digits except three strikes. No tradeable two-leg pair. Also at **96.1% of its 6-month range** — the most extended vehicle on the board. |
| **(b)** | **Refiner equity call spreads** | 🟡 **THE ONLY VIABLE DOOR — and it's crowded** | See §3. Of the four candidates BRENT named, **DINO and PBF fail on liquidity** (DINO: 18 of 18 rows thin OI, many zero; PBF: **IV 67–78%**, OI single digits). **VLO and MPC are the survivors.** |

---

## 3. 🔴 The finding that dominates this scope — BRENT's exhaustion flag got much worse

BRENT flagged: *"refiner z-scores were ~+1.3σ/exhausted at the 7/1 read (BRT-12) — re-check before using."*

**Re-checked. It did not mean-revert. It accelerated.**

| Name | 1-month | 3-month | Position in 6-mo range | Dec IV |
|---|---|---|---|---|
| **VLO** | **+24.8%** | +30.0% | **91.0%** | ~48% |
| **MPC** | **+25.5%** | +40.4% | **93.0%** | ~46% |
| **PBF** | **+52.8%** | +51.4% | 87.1% | **67–78%** |
| **DINO** | **+34.3%** | +49.3% | 92.1% | ~50–58% |
| **PSX** | +22.6% | +30.6% | 92.6% | — |
| **CRAK** | +22.8% | +17.1% | **96.1%** | ~34% |
| *Crude (CL) for contrast* | *+27.0%* | **−6.8%** | *54.8%* | — |

**Read this against the crude row.** Over three months refiners are **+30% to +51% while crude fell 7%.** That divergence **is the crack expansion** — and it has already been monetized through the equity channel. **VLO and MPC are both sitting at their 1-YEAR highs** (VLO 6mo high = 1y high = $314.80, spot $302.50; MPC $319.76, spot $309.24).

**We are not early to this. We are being asked to buy the fourth month of a melt-up, at 46–48% implied vol, in names at 1-year highs.**

**And the entry rule is already broken.** Friday was red right across the complex — VLO −0.90%, MPC −0.97%, DINO −0.89%, CRAK −1.01%, **HO −5.67%, RB −7.00%, CL −3.12%, BZ −3.88%** (the de-escalation selloff on US-Iran talks progress). **That was the rule-#6-clean entry, and it closed before the strike.** Jazan lands into a Monday open that will most likely gap refiners **up** — which is exactly the "green product tape" BRENT told me not to chase.

> **The uncomfortable shape of this trade: Jazan made the thesis MORE right and the entry MUCH worse.** Those are not the same thing, and only one of them is tradeable.

**One lazy comparison I want to explicitly NOT make.** This is *not* the KRE-60 failure mode. KRE 60 had **0% empirical 3-year reachability** — the strike could not be reached. VLO 360 carries a **~24% risk-neutral probability** by Jan-15, and the name just moved +25% in a single month. **The strikes here are genuinely reachable.** The objection is price and timing, not an unreachable instrument. Different diagnosis, different remedy.

---

## 4. Ranked structures (Friday marks — re-pull before any fill)

Reachability is **risk-neutral** (Black-Scholes, from the chain's own IV). It is **the market's own pricing, not an independent edge estimate** — per SC-02/VRP, single-name options are ~fairly priced, so **all the edge must come from BRENT's thesis, none from the structure.**

### 🥇 #1 — VLO **Jan-15-2027 360C / 380C** call debit spread · **~$405**

| | |
|---|---|
| **Legs** | Long 360C @ mark 19.15 (bid 17.80/ask 20.50, **OI 411**, sprd 14.1%) · Short 380C @ mark 15.10 (bid 14.00/ask 16.20, **OI 232**, sprd 14.6%) |
| **Net debit** | **~$4.05 = $405** · worst-case fill $6.50 = $650 · **hard no-pay-above $4.75 ($475)** |
| **Max value / profit** | $20 width → **$2,000** max value; profit **~$1,595**; **~3.9 : 1** |
| **Breakeven** | VLO **~$364** (+20.3%) |
| **Reachability** | P(>360) ~**24%** · P(>380) ~**20%** at expiry |
| **Why this one** | **Best liquidity pair on the entire board** — Jan-2027 carries materially deeper OI at the strikes we want than Dec-18 (360C: **411 vs 95**; 350C: 295 vs 103), and both legs quote ~14% rather than 20–29%. |
| **★ Why Jan and not Dec** | **The thesis is a WINTER inventory squeeze** — OECD diesel stocks at the 4th percentile going into heating season. **Dec-18 expires before the seasonal draw peaks (Dec–Feb).** Jan-15 holds through it. Dec-18 is the tenor that looks right and quits one month early. |

### 🥈 #2 — VLO **Dec-18-2026 370C / 400C** · **~$460** — *max convexity, worse plumbing*
~5.5:1 (width $30 → $3,000 max), BE ~$374.60 (+23.8%), P(>370) ~21%. **But the 400C leg has OI 37 and a 26.5% spread** — you can get in and struggle to get out, and it expires before the seasonal peak. **Only if Will explicitly wants the higher ratio and accepts exit risk.**

### 🥉 #3 — MPC **Dec-18-2026 370C / 400C** · **~$485** — *single-name diversification only*
MPC's 370C is the most liquid high strike on either name (**OI 416**), but the 400C is OI 65 at a **28.9% spread**. Ratio ~5.2:1, BE ~$374.85 (+21.2%). **Take only as a second name if Will wants to split single-name risk** — it is not better than #1 on its own merits.

**Rejected outright:** PBF (IV 67–78% — a lottery priced like one), DINO (OI ~0 across the Dec chain), CRAK (spreads 30–88%), HO futures options (notional), UHN (delisted).

---

## 5. ★ EFFECTIVE-N — the number BRENT explicitly asked for

BRENT's request: *"If Will stacks more than one, the combined escalation-side max-loss should be presented as ONE number so he's sizing the event, not three trades."* **That instruction is an effective-N audit, and it is now the single most decision-relevant part of this scope.**

| Leg | At risk | Status |
|---|---|---|
| USO Sep-18 150/165 call spread | **~$300** | **LIVE** (filled 7/24) |
| XLE 65C Sep-30 ×2 | **~$200** (current mkt; cost $456, −56%) | **LIVE**, dying |
| TRY-FIRE-006 Kharg USO call spread | $200 fenced | **UNFIRED** ($0 today) |
| **Proposed diesel #1** | **~$405** | proposed |
| **TOTAL if diesel added** | **~$905 today · ~$1,105 if 006 also arms** | |

| Field | Entry |
|---|---|
| **N_claimed** | **4** — crude flat-price (USO) · energy equity (XLE) · crude-supply tail (Kharg/006) · refining margin (diesel) |
| **Shared antecedent** | 🔴 **Broad Middle East de-escalation.** An Iran deal or a restored truce compresses **all four at once.** |
| **EFFECTIVE N** | **≈ 1.5** — not 1.0, because the refining-margin leg has a genuinely distinct driver (**Jazan just proved it: a refinery hit is crack-bullish and crude-ambiguous**) and the Russian-products/Ukrainian-strike leg is separate geography. Not 2+, because de-escalation kills every leg. |
| **Sizing reference** | **Size the EVENT (~1.5 views), not the four tickets.** |

**The consequence, stated plainly:** Will already carries **~$500 of escalation-side risk**. The diesel add takes him to **~$905 — roughly doubling exposure to ~1.5 independent views.** At $39.5k that is ~2.3% of the book, which is *not* alarming in absolute terms. **The issue is not the size; it is that it would be four tickets bought as though they were four views.**

### 💡 The construction proposal I'd actually make: **rotate, don't stack**

**Fund the diesel leg out of the XLE 65C rather than adding on top.** XLE is a **diffuse energy-equity** bet, currently **−56%**, expiring **Sep-30**, with **zero diesel specificity** — it is the weakest-signed leg in the escalation book, and post-Jazan it is pointed at the wrong part of the barrel. The diesel spread is the **best-signed** escalation expression available. **Swapping the worse-signed leg for the better-signed one keeps effective-N flat and improves the quality of the exposure — instead of raising exposure to buy a better idea.** That is the recommendation I'd lead with if Will wants this on.

---

## 6. Entry discipline — the gate that decides this

- **🔴 DO NOT CHASE THE MONDAY JAZAN GAP.** Rule #6 (calls on red days) and BRENT's own *"don't chase a green product tape."* If refiners gap up Monday on the refinery strike, **that is a stand-down, not a signal.**
- **Preferred entry:** a **pullback** in refiner equity — a red refiner session with the diesel crack **holding above ~$80** (the thesis metric, not the equity price). The thesis and the entry are separate tests; the crack staying bid through an equity pullback is the ideal combination.
- **No-pay-above:** $4.75 net debit on structure #1. Above that the ratio degrades below ~3:1 and it stops being worth the vol tax.
- **Invalidation (thesis):** diesel crack falls **back below ~$70/bbl** (decisively under BRENT's framework level) → the premise is gone, exit regardless of equity price.
- **Invalidation (time):** no escalation follow-through **and** crack normalization by ~early Nov → the winter thesis has failed in its own window; salvage, do not ride to expiry.
- **Kill:** confirmed Middle East de-escalation (Iran deal / truce restored) — **kills this leg and the other three simultaneously**, which is the entire point of §5.

---

## 7. Why not — the honest case against

1. **We are late to the equity channel.** +30–51% over three months while crude fell 7% *is* the crack trade, already paid.
2. **We are paying elevated vol to enter an extended name** — IV 46–48% on VLO/MPC (PBF 67–78%). Worst combination for a call buyer.
3. **The clean entry was Friday and it's gone.**
4. **No structural edge exists** — single-name options are ~fairly priced (SC-02/VRP). 100% of the edge is BRENT's thesis being right *and* not yet in the price. §3 is direct evidence that a lot of it **is** in the price.
5. **The pure instrument does not exist at this scale** — UHN delisted, HO options 400× too large. **Every available expression is a proxy that dilutes diesel with gasoline**, and gasoline is the weak leg ($47.26 crack).
6. **It raises escalation-axis exposure ~2× for ~0.5 of an additional independent view** (§5) — unless taken as a rotation.

**The strongest single reason to do it anyway:** Jazan is a **refining**-capacity event and the Saudi-Houthi truce has broken after four years. The book's existing escalation legs (USO, XLE, Kharg) are all **crude-supply**-shaped and are therefore **mis-signed for the event that actually happened.** Diesel/cracks is the one expression pointed at the right part of the barrel.

---

## Decision

**Terry verdict: CONDITIONAL — thesis confirmed, channel crowded, entry compromised.**

- [ ] **APPROVE structure #1 as a ROTATION** (fund from XLE 65C; ~$405; enter on a refiner pullback with the crack holding >$80) ← *TERRY's recommendation if Will wants the exposure*
- [ ] **APPROVE structure #1 as an ADDITION** (accepts ~$905 escalation-side total at N_eff ≈ 1.5)
- [ ] **APPROVE #2 or #3 instead** (higher ratio / second name — both worse plumbing)
- [ ] **NO — thesis is right but already paid; stand down** ← *defensible and my second choice*
- [ ] **REWORK:** ______

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---
*Thesis owner BRENT — TERRY has not re-underwritten the diesel framework, only re-checked its published metrics against Friday's tape and applied construction judgement. Vehicle screening, structure, tenor, strikes, entry gates, the effective-N aggregate and the rotation proposal are TERRY's. Distillate-yield-by-name is an open question routed back to BRENT. All marks 7/24 close — barred from use at fill.*
