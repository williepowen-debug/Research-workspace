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

---

## 🔄 2026-07-30 ~12:35 ET — NUMBERS SYNC (Will-directed, both windows). **Verdict moves CONDITIONAL → NO AT THIS PRICE.** Still unarmed, $0 moved.

**The thesis and the trade moved in OPPOSITE directions since 7/26.**

| | Card (7/24) | **Live 7/30 12:30 ET** | |
|---|---|---|---|
| **Diesel crack** (HO×42 − WTI) | $82.70 | **$90.30** | ✅ **+9.2%** |
| WTI / Brent | 89.31 / 96.78 | **83.90 / 89.77** | **−6.1% / −7.2%** |
| VLO | 302.50 | **308.08 (+2.24% today)** | ❌ **no pullback — it rose** |
| VLO vs 1-yr high 314.80 | −3.9% | **−2.2%** | ❌ closer to the high |

**★ The crack widened 9% INTO a 6–7% crude selloff** — product tightness, not a crude bid. **This is the thesis confirming on its own mechanism**, and it **partially undercuts my own §5**: I scored the diesel leg as sharing a de-escalation falsifier with the other three escalation legs (N_eff ≈ 1.5). **If the crack widens while crude falls, de-escalation does not automatically kill this leg** → **more independent than I credited.** ⚠️ n=1 and the window contained *both* directions (7/24-28 de-escalation selloff, 7/29 resumed-strike spike, 7/30 fade) — **suggestive, not established.** Clean de-escalation evidence would re-score §5; asked of BRENT.

### 🔴 The no-chase line is BREACHED — VLO Jan-15-2027 360C/380C, live

| Leg | Bid | Ask | Mark | Spread | OI |
|---|---|---|---|---|---|
| 360C | 18.30 | 21.10 | 19.70 | 14.2% | 392 |
| 380C | 13.60 | 16.30 | 14.95 | 18.1% | 239 |

**Net mid $4.75 = EXACTLY the §6 no-pay-above. Realistic fill (pay ask / hit bid) $7.50 = 58% through it.** Tradeable bracket $2.00–$7.50 on a $4.75 mid — **mid is not obtainable at that OI and those spreads.**

**VERDICT: NO AT THIS PRICE.** The thesis strengthened; that is not a licence to pay through a pre-registered limit. Same logic as the ratified rule-#6 break test — *"the thesis is working"* is a **chase**, not a break, and the no-chase line is a **direct ratio calculation, not a proxy**, so nothing can refute it. It binds.

### ⚠️ §5's lead recommendation — "ROTATE, don't stack" — is WITHDRAWN

It assumed the **XLE 65C** had funding value. **It is now ~$112 (mark $0.56 ×2) against ~$455 cost, −75%; XLE $58.42 needs +11.3% in 62 DTE.** Rotating recovers **~$112 toward a $475+ structure** — it no longer funds anything. **"Rotate" has collapsed into "ADD," the option §5 argued against.** Closing the XLE 65C remains defensible on its own merits (worst-signed leg, zero diesel specificity, wrong part of the barrel) — **but it is now a separate decision, not a funding mechanism.**

### Two things that reopen this
1. **A genuine refiner pullback — VLO ~$280–290** puts structure #1 comfortably under $4.75 with the thesis intact.
2. **Clean de-escalation evidence** that the crack holds → re-scores effective-N in the trade's favour.

**The crack at $90.30 against a $70 invalidation means this thesis has MONTHS of room. There is no reason to buy it badly today.** Packet → BRENT (incl. the still-open **distillate-yield-by-name** ask, which could move structure #1 off VLO before price ever matters).

---

## 🔴 2026-07-30 ~13:15 ET — **THE CARD WAS MISSING A DATED BINARY THAT LANDS TOMORROW.** BRENT packet consumed. **Verdict UNCHANGED (NO AT THIS PRICE) — but the reason is now dated, not just priced.** Still unarmed, $0 moved.

**Source:** `inbox/2026-07-30_from-BRENT_russia-diesel-ban-base-case-flips-to-LAPSE-before-you-quote-those-structures.md` — BRENT, unprompted, cutting against his own thesis. Reply owed: none. **Thesis/supply data is BRENT's; everything below the divider in §D is TERRY construction judgement.**

### A. The supply leg finally has a name — and it has an expiry date

Until today the card described a crack at the top of its range without a named mechanism beyond "refinery outages." BRENT's mechanism:

> **Russia — #2 diesel exporter after the US — banned diesel/gasoil exports outright effective 7/8.** Loadings **234 kb/d (Jul 1-10)** vs **400 kb/d (June)** vs **~817 kb/d (2025 avg)** [Reuters / S&P Global, Jul-26]. Plus **Jazan** (400 kb/d, shut 7/27, restart ~8/15) and **Perm + Ryazan struck 7/29**. EIA corroboration from the volume side: **US distillate stocks BUILT +1.06M while the crack made its high at 97.2% utilisation** ⇒ the marginal barrel clears **offshore**; tightness is **export/global, not domestic**. Demand splits the same way: **distillate +4.74% YoY vs gasoline −0.25% YoY.**
>
> *(CERA's ">4 mb/d Russian refining downtime" is a **single assessment source** — BRENT flagged it rather than propagated it, and I am carrying it the same way. Not load-bearing below.)*

**This independently corroborates §1's core finding from a different direction:** §1 said the blended 3-2-1's shortfall is *entirely gasoline*. BRENT's YoY demand split (+4.74% distillate / −0.25% gasoline) is the same bifurcation measured on demand rather than margin. **Two instruments, one conclusion — and it argues again that any gasoline-weighted equity proxy dilutes the signal.** The distillate-yield-by-name ask (§1, still open) gets *more* important, not less.

### B. 🔴 **THE BAN'S STATED EXPIRY IS 2026-07-31 — TOMORROW — AND THE BASE CASE IS LAPSE, NOT EXTENSION**

**⚠️ READ-THIS-FIRST TRAP — TWO BANS, TWO PRODUCTS, TWO CLOCKS:**

| Product | Status | Source |
|---|---|---|
| **Gasoline / petrol** | **EXTENDED to 31 Dec 2026** | Novak (Deputy PM), Bloomberg 7/25 |
| **Diesel / gasoil** | **to be LIFTED "as the market recovers"** — explicitly *not* extended alongside | Interfax / S&P Global 7/27 |

> **🔴 Anyone who reads a "Russia extends export ban" headline tomorrow and applies it to diesel has this trade exactly backwards.** That includes me at a future boot. **The extension that happened was GASOLINE.** The sole counter is an **unattributed, body-less CGTN headline (7/29)** suggesting diesel may extend into August — **one weak claimant, not carried.**

### C. ★ The grading standard is pre-registered on LOADINGS, not on the decree — BRENT's, written before the print

> **The ban and the refinery destruction are not independent: the ban exists BECAUSE refining is down. You cannot export what you cannot refine.** With downtime >4 mb/d, *"ban lifted"* does **not** mean ~817 kb/d returns. The binding constraint is **capacity, not policy** — the decree looks closer to a symptom than a cause.

| 7/31 outcome | Then within ~2–3 weeks | Read |
|---|---|---|
| **Lapse** + loadings **stay ~234 kb/d** | no recovery | supply leg was **physical all along** — the crack keeps it |
| **Lapse** + loadings **recover toward 400+ kb/d** | visible recovery | 🔴 **the real bearish outcome** |
| Extension (against base case) | — | leg holds on policy, but capacity still binds |

*Base: **234 kb/d**, Jul 1-10. BRENT's own operational-vs-declaratory discipline — do not trade the announcement.*

---

### D. ★ TERRY CONSTRUCTION READ — **the wait is ~3 weeks, not 1 day, and that changes what the wait costs**

BRENT's closing line is *"tomorrow's outcome is worth waiting through."* **His own grading standard says something stronger, and I don't think he drew it out:** if the decree is uninformative and only **loadings** grade the leg, then **7/31 is not a resolver — it is the START of a ~2–3 week observation window.** The tradeable information lands **~mid-to-late August**, not tomorrow. Nothing about this card should be re-quoted on tomorrow's headline.

**And that is the point that decides it, because on THIS structure waiting is nearly free:**

| | |
|---|---|
| Structure #1 tenor | **VLO Jan-15-2027** = **~169 DTE** today |
| After a ~3-week wait | **~148 DTE** |
| Tenor surrendered | **~21 days = ~12.4%** — on a **long-dated** spread, where near-term theta is at its slowest |
| Bought with it | a resolved binary **+** a loadings read on the actual mechanism |

> **This is the rare case where the option to wait is cheap and the thing you learn is the thing the trade depends on.** Contrast the ordinary "wait for a pullback" argument, which costs you the move if you're right. Here the tenor decay over the window is a rounding error against a **99.2nd-percentile entry into an unresolved binary.** *(Payoff/theta not re-computed at live marks — the argument is tenor-fraction and does not need them; re-pull before any [Approve].)*

**A second thing the packet buys us: the $70 thesis-invalidation (§6) finally has an early-warning instrument.** Until today, "crack falls below ~$70" was a **lagging** line — by the time it printed, the leg was already gone. **Loadings recovering toward 400+ kb/d is the observable precursor** to exactly that path. Recording it as a leading tell, not a new invalidation:

- **⚠️ WATCH (new, leading):** Russian diesel/gasoil loadings recovering toward **400+ kb/d** post-lapse → the mechanism under the crack is repairing → expect the crack to head toward the $70 line. **Not itself a kill; it is the thing that predicts the kill.**
- **Invalidation (thesis) unchanged:** crack decisively below **~$70/bbl**.

**Crack figures reconcile — no discrepancy to chase.** BRENT cites **$99.08 (7/29)**; the 12:35 sync above computes **$90.30 (7/30 12:30 ET)**. These are consistent, not contradictory — BRENT's own packet says *"cracks compressed intraday"* on 7/30 while VLO/MPC rose. **Same series, one day and an intraday fade apart.** Flagging it because a future reader comparing the two sections would otherwise see a $9 gap and go looking for a data defect that isn't there.

### E. Entry discipline — §6 amended (additive; nothing relaxed)

- **🔴 NEW STAND-DOWN:** **do not quote, re-quote, or arm this card on tomorrow's 7/31 decree headline, in either direction.** A lapse headline is not a kill and an extension headline is not a green light — **§C says the decree is not the instrument.**
- **The no-pay-above $4.75 is unchanged and still breached** (mid $4.75, realistic fill $7.50). **Nothing in this packet touches price**, and a strengthening thesis is not a licence to pay through a pre-registered limit — the ratified rule-#6 break test applies: a no-chase line derived from a **direct ratio calculation** has no proxy to refute.
- **Re-open conditions unchanged** (VLO ~$280–290 / clean de-escalation evidence) **plus one added:** a post-lapse loadings print that **holds ~234 kb/d** would convert the supply leg from *policy-dependent* to *physically confirmed* — thesis-strengthening, though it still would not fix the entry price.

### F. ⚠️ UN-OWNED GATE CHECK — run per pickup rule #2 (the TRY-FIRE-005 lesson). **This gate had no named grader.**

BRENT's packet is explicitly a caution with **"reply owed: none"** — so tomorrow's decree and the ~2–3 week loadings window were, as of receipt, **owned by nobody**. That is the exact shape that let TRY-FIRE-005 drift 7 days. **Proposed split, routed to BRENT for confirm:**

| Gate | Owner | Why |
|---|---|---|
| 7/31 decree outcome + the ~2–3wk **loadings** grade (base 234 kb/d) | **BRENT** | domain data — TERRY does not source loadings and will not assert them |
| Card consequence (re-quote / re-open / stand-down) | **TERRY** | construction |

**Until BRENT confirms, TERRY carries it on its own surface so it cannot drift** → `STATUS.md` pickup item 0b.

**VERDICT: NO AT THIS PRICE — unchanged, and now additionally NOT-BEFORE-THE-LOADINGS-READ.** Thesis stronger (it has a named mechanism and volume confirmation on both halves of the barrel); entry worse (99.2nd percentile, crowding unrepaired since 7/20 GS, no-chase line breached, and an adverse dated binary that was not on the card until today). **$0 at risk, nothing armed.**
