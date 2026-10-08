# CONDITIONAL CARD — QQQ — dated downside: ONE Dec-18-2026 put spread (≈ 3% OTM / $20 wide), ≤ $491.30 all-in — **commissioned by Will (10:34 ET 2026-10-02)**

**Date:** 2026-10-02 Fri, written 10:38–11:0x ET (`date` 10:35:20 at the packet read; live reads 10:36–10:38 ET below) · **Id:** `TRY-COND-QQQ-DATED-DOWNSIDE` (NEW card; registered in `setups/INDEX.md`; no `SETUPS.tsv` / `TRADE_BOOK.md` row — both ledgers sit at the read-cap rotate tier, rotation owed by Mon 10/05)
**Asked by:** Will, through PROME `prome-70`, 10:34 ET, verbatim *"yes commission the card"*. Packet: `inbox/processed/2026-10-02_from-PROME_COMMISSION-QQQ-dated-downside-card.md`. **A commission to PREPARE a card. It does not approve a fill.**
**Thesis owner:** **Will.** No agent owns a QQQ-down thesis. The evidence desks are cited at their own artifacts in §8: LIQUID (credit), HENRY (tape, gamma, rates), BROCK (private credit), VULCAN (AI capex; its packet arrives after today's close and §8 is re-read then). **Construction:** TERRY. **Approval:** Will (root rule #5), $500 per card (Will 6/26).
**Terry verdict:** **CONDITIONAL — NOT ARMABLE at the 2026-10-07 marks, and NOT APPROVED (Will tapped LATER 10/3 21:07 ET, root rule #5). Both trigger legs moved AWAY this week: (a2) no close back below $748.65 (QQQ closed $756.20 · $759.66 · $757.73 on 10/5–10/7); (b) HY OAS 310 · 312 · 303 on 10/2 · 10/5 · 10/6, every cell under 321 and at or under the card's own 312 credit-kill line. Desk lean: let it LAPSE at Fri 10/16 15:00 ET on its own letter; a new window needs a re-card.** See ADDENDUM 2026-10-07 at the foot. *(was: **CONDITIONAL — buildable, liquid, and the right TENOR for the view. NO FILL before (i) Will's [Approve] on THIS card, (ii) §4's two-condition trigger (a failed breakout, AND credit persisting above 320), and (iii) a green QQQ session at the fill.** Today's tape argues against it, and §7 says so plainly.)*
**Confidence in the structure:** Medium-High (strikes, tenor, liquidity and cap checked on the live chain). **Confidence the trigger fires:** Low to Medium. The base rate in §7 is small (n = 12) and is against a large move even when the trigger does fire.
**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD CREATED OR MOVED ON ANY OTHER DESK.** §4's conditions are this card's own construction. They do not grade or amend LIQUID's ">320 sustained" letter, X1, or any HENRY line.

---

## 0. Inputs checked

| Item | State |
|---|---|
| Live price | QQQ **$753.53** at 10:38 ET (today: high $754.53, low $749.10; 10/1 close $742.03) · SPX 7,748.53 · RSP $210.30 · VXN 22.1 · HYG $77.22 (yfinance 1-min, 10:38) |
| Option chain | QQQ Dec-18 and Nov-20 puts, `chain_fetch.py --no-cache` 10:36:21–10:36:24 ET. **SCREENING.** The newest trades are stamped 10:09–10:20, so the quotes are probably about 15 minutes delayed. **Fidelity's chain governs at the fill** (root rule #4; `RISK_RULES.md` finding 5b) |
| Position truth | `FORGE/STATUS.md` quantities `[10/1 pc]` **plus Will's stated intent (relayed by PROME) to ROLL the Oct-02 740P ×4 today. No fill seen** ⇒ `[POSITION_STATE as of 10/1 pc]`, §6 |
| Catalysts | §5's map, each with its owner and source |
| Thesis-owner currency | Will's own words today (packet §Why). The evidence desks are cited at their 10/1–10/2 artifacts |

## 1. One-line setup

Express Will's weeks-to-months view (that the AI build-out's debt, plus yields, oil and doubts about AI profits, reaches the index, with credit moving first) through **one defined-risk QQQ put spread with about two months of life**. It is bought only after **both** of these have happened: equity has failed to hold its breakout, and credit stress has persisted. **This replaces the 0–3-day puts, not adds to them** (construction rule #16).

## 2. Why this tenor (construction rule #16)

- **How long the view needs:** Will says "weeks or months." LIQUID's credit sequence and VULCAN's dated test (the late-October hyperscaler earnings cluster, ~10/28, estimated) both sit **4–8 weeks out**.
- **What the expiry must clear:** the October auctions (10/6–8), CPI (10/14), the hyperscaler cluster and the FOMC (~10/28), and the November refunding.
- **The desk's precedent is the reason for the form.** The same QQQ view sat in this book twice, July–August 2026. The defined-risk **Aug-21 put spread (`TRY-WILL-QQQ-VFADE`) would have lost $452** on a level named in advance. The **0–1-day tickets lost ≈ $4,341**: same view, 9.6× the cost (`POSTMORTEMS.md` 2026-08-04).
- **The band and Will's "one to two months":** construction rule #21's **60–90 DTE band governs a new deployment**. Will asked for one to two months. **Dec-18 reconciles the two:**
  - It is 63–74 DTE across the whole entry window (inside the band).
  - The card's **time stop is Fri 12/04, about two months after any fill.** So the card is HELD for "one to two months", and expiry sits two weeks past the stop, so the final weeks of decay are never the trade.
  - **Nov-20** (49 DTE today) fits his words but **fails the band**. It is listed in §5 as rejected, not as the lean.

## 3. Entry trigger — BOTH (a) AND (b) must hold at the fill. (c) and (d) are context, not gates

| # | Condition | Measured today | Why this, and why AND |
|---|---|---|---|
| **(a)** | **A failed breakout.** (a1) a regular-session QQQ **CLOSE ≥ $748.65** on or after 10/2 (the breakout), THEN (a2) a later regular-session **close < $748.65** within the window, AND (a3) QQQ **< $748.65 at the fill** | ⚠️ **$748.65 is the 6/03 INTRADAY HIGH, not a close.** The highest close before today was **$747.46 (9/22)** (yfinance daily, 253 bars). Today: high $754.53, last $753.53 ⇒ (a1) is set by the **first** close ≥ $748.65 on or after 10/2, today or any later session in the window. **Until such a close exists, the card cannot arm** (no reinterpretation). *(Corrected 2026-10-02 11:1x ET: the first version said a sub-$748.65 close TODAY meant the card "does not arm". The letter lets a later close set (a1). QQQ was $749.05 at 11:13.)* | The equity half of Will's chain: a failed breakout is the first sign that the rate-relief bid is not holding. The level is the one PROME named. It is kept as an INTRADAY-high line, labelled as such |
| **(b)** | **Credit persisting:** the two most recently PUBLISHED FRED ICE BofA HY OAS cells (`BAMLH0A0HYM2`) are **both ≥ 321bp**, read at the fill | 9/30 **312** · 10/1 **324** (LIQUID, FRED, read 10/2 10:24 ET) ⇒ **one print, NOT MET.** The 10/2 cell posts **Mon 10/5 ~10:15 ET** | Will's thesis is that **credit leads equity**. One print can be a relief-rally artifact; LIQUID calls it "one print, not a regime". **This is the card's own entry test, NOT LIQUID's ">320 sustained" CONFIRMATION letter**, which has no count and is LIQUID's/PROME's to settle |
| (c) | RSP's 7th straight down week (close < $211.11 today) | RSP $210.30 at 10:38 ⇒ on course. **HENRY grades it after the close** | **Context only.** Breadth confirms a narrow market. It is a weekly, one-shot read that resolves before the window opens, so it cannot gate a fill |
| (d) | SPX below HENRY's gamma flip (~7,696) | SPX 7,748.53 ⇒ **above** (dealers dampen moves) | **Context only.** It is an SPX measurement, QQQ's dealer gamma is not measured, and it has a one-session shelf life (construction rule #14). Below the flip a decline speeds up, which **raises the payoff path, not the probability of the thesis** |

**Window:** from **Mon 10/05 09:45 ET** through **Fri 10/16 15:00 ET** (10 sessions; Dec-18 at 74 → 63 DTE, inside construction rule #21's band throughout). **If unfilled by then ⇒ the card LAPSES.** A new window needs a re-card (moment properties re-marked, and the tenor re-checked against the band).

### Root rule #6 — reconciling a red-day trigger with a green-day buy, in figures

The trigger fires on a **red close** (a2 is a fall back through $748.65). **The fill is never on that close.** The fill is the **first GREEN session after the arming close** (QQQ last > its prior regular-session close at the fill) on which (a3) and (b) still hold.

*Worked numbers:* arming close $744.00 (−1.3% from today's $753.53) ⇒ next session green at $746.50 (+0.3%) ⇒ fill allowed (still < $748.65, HY 2-of-2 ≥ 321). If that green session lifts QQQ **above $748.65**, the breakout is repaired ⇒ **no fill that session**.

**What this costs, said plainly:** a straight-line crash with no green session in the window is **missed**. That is the deliberate price of not paying up for volatility on red tape.

**The one permitted break** follows `RISK_RULES.md` § "Breaking root rule #6". A red-session fill is legitimate **only if** the live Fidelity net debit for the SAME strikes is **≤ the most recent green-session net debit recorded on this card** for those strikes, written here in figures before the fill. "The window is closing" is a chase, not a break.

## 4. Structure (construction)

| Field | Rule | Today's structure check (10:36 chain, SCREENING; a moment property, construction rule #14) |
|---|---|---|
| Instrument | **ONE QQQ Dec-18-2026 put vertical (debit)**, one net-debit order, never legged | — |
| Long strike | the **$5 strike nearest 97% of QQQ at the fill** | at $753.8 ⇒ 731.2 ⇒ **730** |
| Short strike | **long − $20** (sells the richer wing: 710 IV 21.9% vs 730 20.3%) | **710** |
| Limit | net debit **≤ $4.90** (×100 + $1.30 fees ≤ **$491.30**, under the $500 cap) | 730P 17.40/17.51 · 710P 12.60/12.69 ⇒ worst-case **$4.91**, mid **$4.81** ⇒ fillable at the limit, close to it |
| If over the limit | step BOTH strikes down $5 **once**; if still over the limit, no fill that session | 725/705: 16.05/16.15 − 11.62/11.72 ⇒ worst **$4.53**, mid $4.43 |
| Liquidity | open interest and spread checked | 730P OI 7,711 (0.63% wide) · 710P OI 25,492 (0.71%) · Dec-18 is the monthly expiry |

**Payoff, illustrated for a fill at QQQ $745 on Tue 10/06 (725/705, ≈ 73 DTE).** Black–Scholes **model estimates** at chain IVs, holding IV flat: the model reads ~10% under the chain on the long leg. **Cost $491.30. Break-even at expiry ≈ $720.09 (−3.3% from $745).**

| QQQ from the $745 fill | +3% ($767) | flat ($745) | **−5% ($708)** | **−10% ($670)** |
|---|---:|---:|---:|---:|
| Fri 11/06 (~1 month in) | $230 ⇒ **−$261** | $431 ⇒ −$60 | **$941 ⇒ +$449** | **$1,496 ⇒ +$1,004** |
| **Fri 12/04 time stop** | $74 ⇒ −$418 | $277 ⇒ −$214 | **$1,095 ⇒ +$604** | **$1,830 ⇒ +$1,339** |
| at expiry 12/18 (not held there) | $0 ⇒ −$491 | $0 ⇒ −$491 | $1,725 ⇒ +$1,234 | $2,000 ⇒ +$1,509 (max) |

- **Max loss:** the premium, **≤ $491.30**. Forward max loss after the fill = the remaining mark (construction rule #20d).
- **Max gain:** $2,000 − $491.30 = **$1,508.70** (≈ 3.1×), at QQQ ≤ the short strike at expiry.
- **Delta at the illustrative fill:** ≈ −0.088 per spread ⇒ ≈ **$6.6k of QQQ-equivalent short** (model).

## 5. Management, kill and catalyst map

| Rule | Spec |
|---|---|
| **Harvest (durable finding 9)** | **Sell the spread at a Fidelity net bid ≥ $9.80** (2× the $4.90 limit; ≈ half the width). The model puts that at about QQQ −5% within a month of the fill. A one-spread card cannot take a partial, so the harvest is the exit |
| **Kill — credit leg withdrawn** | a published HY OAS cell **≤ 312bp** (back to the 9/30 pre-spike level) ⇒ sell at the next session's bid. The thesis is "credit leads"; credit un-leading is the thesis broken on its own axis (construction rule #23) |
| **Kill — breakout vindicated** | **two consecutive QQQ closes ≥ $763.62** (2% over $748.65) ⇒ sell at the bid. The failed breakout was repaired and extended |
| **Time stop** | **sell-or-roll by Fri 12/04 15:00 ET** (14 DTE), whatever the mark. Will's standing practice is sell or roll before expiry, never hold to expiry (`USER.md` 9/30). A roll here = **same strikes, later expiry** (construction rule #21), still a Will-gated proposal (Non-Negotiable #6). Rolling also keeps the line clear of the IRA in-the-money-expiry unknown (FORGE D-60) |
| **Do not chase (Non-Negotiable #5)** | no fill above the $4.90 limit; no fill with QQQ ≥ $748.65; no fill on a red session except under the §3 break test; no strike reach beyond one $5 step |
| **No add** | one spread. A second needs a new card (construction rule #17: the size-increasing branch carries the higher burden) |

**Rejected alternatives (today's 10:36 chain):**
- **Nov-20 735/715:** $4.76 worst ⇒ $477.30. It fits "one to two months" but **fails the 60–90 DTE band** (49 DTE).
- **Dec-18 740/720:** $5.79 ⇒ over the cap.
- **An outright Dec-18 put** ≈ 3% OTM: ~$17 ⇒ $1,700 ⇒ 3.4× the cap.
- **0–3-day puts:** construction rule #16.

**Catalyst map** (each with its owner; dates marked "est." are not verified here):

| Date | Event | Owner / source |
|---|---|---|
| Mon 10/05 ~10:15 ET | HY OAS 10/2 cell (persistence or retrace — leg (b)) | LIQUID, FRED |
| Tue–Thu 10/6–10/8 | 3Y · 10Y · 30Y auctions (the FORUM-7 supply test) | HENRY / BOND |
| Wed 10/14 | September CPI | BOND `docket/CATALYSTS.tsv` |
| 10/15–16 | LIQ-07 verdict window | LIQUID |
| ~Wed 10/28 (est.) | **Hyperscaler earnings cluster — VULCAN's live §4b flip** (a stock falling on a capex RAISE in ≥2 prints, or management citing ROI pressure, confirms fragility) | VULCAN `STATUS.md`, `EXIT_PROTOCOL.md` §4b |
| ~10/28 (est.) | FOMC | — |
| Week of 11/09 | November refunding | BOND |
| Fri 12/04 | **time stop** | this card |

## 6. The book it joins — size against the TOTAL (live marks 10:37 ET, vendor bids, SCREENING; quantities `[10/1 pc]`)

| Line | Qty | Bid ×qty | Shared antecedent |
|---|---:|---:|---|
| QQQ 740P Oct-02 | 4 | ≈ $56 (09:50) — **Will says he will ROLL these (to Oct-09 ≈ $1.2–1.4k at risk if done)** | QQQ down |
| QQQ 735P Oct-05 | 5 | ≈ $212 (09:50) | QQQ down |
| KRE 60P Dec-18 | 5 | $260 (bid 0.52) | credit / banks |
| KRE 65P Dec-31 | 2 | $266 (bid 1.33) | credit / banks |
| APO 95P Dec-18 | 1 | $130 (bid 1.30) | private credit |
| HBAN 16P Oct-16 | 2 | $150 (bid 0.75) | credit / banks |
| WAL 70P Dec-18 (Robinhood) | 1 | $195 (bid 1.95) | credit / banks |
| KRE 25P Jan-15 (Robinhood) | 1 | $0 (bid 0.00) | credit / banks |
| **Risk-off put sleeve now** | — | **≈ $1,269** (≈ $2.5k if the 740s roll to Oct-09) | **one antecedent: credit stress reaching equities** |
| **+ this card** | 1 | ≤ $491.30 | **the same antecedent ⇒ N_eff = 1** |

**Read it this way:**
- This card **does not diversify** the bank and private-credit puts. It is the **equity-index leg of the same credit-leads bet.** If credit stress does not come, every line in the table loses together.
- With the card, the sleeve's dollars at risk ≈ **$1.76k** (≈ **$3.0k** if the 740s roll).
- Duration (TLT 82P / TBT) and oil (USO / VLO) are separate antecedents. They are not summed here, as on the WQ-339 card.

**The cleaner pairing, which is Will's to choose:** this card is the dated replacement for the short-dated QQQ puts. **If the 740s are rolled and this card is approved, he holds two QQQ-down expressions, one of them in the tenor that construction rule #16 says loses.** The desk's view: sell the short-dated QQQ puts (WQ-347; `MGMT-QQQ735P-OCT05`) and let this card carry the QQQ view.

## 7. ⚠️ What argues AGAINST the card (said plainly)

1. **The tape is the other way today.** QQQ is at an all-time intraday high on a rate-relief rally after a soft payrolls number. HENRY (09:5x) finds **no growth-fear tell** on any of his five flip tests: KRE up as yields fall, HY ETFs up, dealer gamma positive.
2. **The failed-breakout base rate is small and points against a big drop.** QQQ re-breakouts above an all-time high at least 40 sessions old, 2005 → 10/1/2026 (yfinance daily, 5,471 bars, adjusted): **n = 12.**
   - **5 of 12 failed** within 5 sessions. Over 40 sessions after the breakout, **their median worst drawdown was −4.1%**; **1 of 5 reached −5%** and **0 of 5 reached −10%**.
   - The 7 that held: median +6.2% over 40 sessions.
   - ⇒ **Even when (a) fires, the typical failed breakout reaches about this card's long strike (≈ −3%) and stops.** The payoff column at −10% is a tail in this sample, not a base case. *(n = 12 is a sample-size statement, not a distribution; construction rule #19: bar count stated.)*
3. **"Every drawdown bought back within weeks": measured, and PARTLY FALSE as phrased.** Since May there was **one** drawdown deeper than 3%: **−11.3%** from the 6/03 peak to the 7/29 trough, which took until **9/22 (≈ 16 weeks)** to recover. That one was not bought back within weeks, but it **was** bought back.
4. **AI capex is not cracking on the evidence in hand.**
   - VULCAN's 10/1 Micron grade went **against** the bear case: TrendForce 4Q26 DRAM **+10–15%**, MU FQ1 guide **$61.5B vs $54.23B**, VULCAN-11 FALSIFIED, S2 3 → 2.
   - **Micron is ≈ 4.75% of QQQ** (yfinance top holdings, vintage not shown), so that grade lands directly in the index.
   - Megacaps fund capex largely from cash flow (packet §5; VULCAN S1 "capex RAISED", NOT FIRED).
5. **Oracle is NOT a QQQ constituent.** It is NYSE-listed (yfinance `exchange = NYQ`), and the Nasdaq-100 admits Nasdaq-listed issuers only (INFERRED from the index rule; not checked on Nasdaq's methodology page today). VULCAN's S5 debt-financing evidence (ORCL off-balance-sheet leases $260B → $288B) therefore reaches QQQ **only indirectly**, through the hyperscalers' capex and Nvidia's order book (NVDA ≈ 8.5% of QQQ). **Do not lean on Oracle for this card.**
6. **Credit is one print.** HY 324 on 10/1 crossed LIQUID's 320 send line **once**; LIQUID calls it "TAGGED, not sustained", and a retrace on 10/2's relief rally is plausible. The private-credit evidence is narrow:
   - **BROCK:** banks cut FSK's revolver −13.8% (to ~$4.05B, +12.5bp margin; 10-Q Q2-26) while **expanding** lines to ARCC and OBDC, and **no bank loss was found**. BRK-02 resolved FALSE on the spec's instrument.
   - X1's wrapper half: **NOT ARMED**; X1 sizing **CLOSED / DON'T-SIZE** (unchanged by this card).
7. **Durable finding 1 (deploy on a fired trigger):** no fleet trigger has fired for a QQQ short. §3 is a trigger written today for this card. It is pre-registered **before** any quote is taken as an entry, but it has no track record.

**For it:**
- The view now has the right tenor and a capped loss.
- The trigger needs equity AND credit, which is Will's own causal order.
- Each of the four context legs (RSP breadth, HY widening across all six series on 10/1, IG/BBB/BB at their own p95 daily moves, gamma near the flip) is real today, even though none is a regime.
- The October–November calendar is dense with the events the thesis says matter.

## 8. What TERRY could not check

- **VULCAN's evidence packet:** it arrives after today's close. **§7.4–7.5 are re-read against it before Monday's open**, and the verdict changes if it carries a dated capex-cut or ROI signal.
- **Fidelity's live chain:** unseen. Every option figure is a vendor screening mark from about 15 minutes earlier.
- **Hyperscaler and FOMC dates:** estimates (VULCAN carries ~10/28 as estimated).
- **Nasdaq-100 eligibility of NYSE issuers:** INFERRED from the index rule, not read on the methodology page today.
- **QQQ holdings weights:** yfinance, vintage not shown.
- **Whether Will rolled the 740s:** no fill seen.

## Decision

> **For Will (PROME registers the WILL_QUEUE row):** **APPROVE / REJECT**: buy **ONE QQQ Dec-18-2026 put spread**, long strike nearest 97% of QQQ at the fill, short 20 lower, **net debit ≤ $4.90 (≤ $491.30 all-in)**. Buy it on the first **green** QQQ session from **Mon 10/05 09:45 to Fri 10/16 15:00 ET** after **(a)** QQQ has closed above $748.65 and then closed back below it (and is below it at the fill), **AND (b)** the two latest published HY OAS cells are both ≥ 321bp.
> - Harvest at a net bid ≥ $9.80.
> - Kill on HY ≤ 312 or two QQQ closes ≥ $763.62.
> - Sell or roll by Fri 12/04 15:00 ET.
>
> ⚠️ The failed-breakout base rate (n = 12) is against a large move. Today's tape is a rate-relief rally with no growth-fear signal. This card is the SAME bet as the bank and private-credit puts, not a hedge to them.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## ADDENDUM 2026-10-07 Wed 22:1x ET — DOCKET L589 status read at tonight's marks (PROME `prome-0e`, Tier 1). No new build; the trigger, kill and window letters are UNCHANGED

**Ruling on file:** WQ-365 **LATER** (Will's Decision Deck tap 2026-10-03 21:07 ET, doc `365-20261004010726615-uq7z4x`; PROME packet `inbox/processed/2026-10-03_from-PROME_WQ-357-365-366-rulings.md`). ⇒ **NOT approved; cannot arm even if (a) and (b) both held** (root rule #5). Recorded here (root rule #10).

| Leg | Letter | Tonight | Read |
|---|---|---|---|
| (a1) breakout close | first close ≥ $748.65 on/after 10/2 | **10/2 close $749.58** (yfinance daily) | SET on 10/2 |
| (a2) failed breakout | a later close < $748.65 | 10/5 **$756.20** · 10/6 **$759.66** · 10/7 **$757.73** | **NOT MET** — QQQ is $9.08 (1.2%) above the line |
| (b) credit persisting | two latest published HY OAS cells both ≥ 321bp | FRED `BAMLH0A0HYM2`: 10/1 324 · **10/2 310 · 10/5 312 · 10/6 303** | **NOT MET** — the last two are 312 and 303 |
| Kill — credit withdrawn | a cell ≤ 312 ⇒ sell at the next session's bid | 310 · 312 · 303 | **Printed three sessions running.** Nothing to sell (no fill); on the card's own construction-rule-#23 reading, credit has un-led |
| Kill — breakout vindicated | two consecutive closes ≥ $763.62 | high close $759.66 | NOT MET |
| Window | Mon 10/05 09:45 → **Fri 10/16 15:00 ET** | 7 sessions left | Lapses then on its own letter |

**§7.4–7.5 re-read against VULCAN's evidence (DOCKET L589's ask).** VULCAN never sent the tightened packet (dark since 10/2); its **10/2 16:0x ACK** (`inbox/processed/2026-10-02_from-VULCAN_ack-deferred-expression-ask.md`) carried a pre-view, read in full:
- **It agrees with §7.4:** Micron FQ4 at the primary (revenue $54.2B, FQ1 guide $61.5B up), AI-infra primary markets OPEN (CleanSpark $2.23B HY ~4.4× covered; CRWV $4.2B converts upsized; AMZN's $8B SPV aimed at IG buyers), and ORCL +3.23% on the SPV news. VULCAN's words: the strain is *"REAL in STRUCTURE … but NOT YET PRICED into levels."*
- **It agrees with the thrust of §7.5:** QQQ's link to the AI-debt thesis is **"LOOSE"** — it reaches QQQ *"by DRAG, not by DIRECT HOLDING"*; CRWV is not in QQQ.
- ⚠️ **One factual conflict, UNRESOLVED:** VULCAN lists ORCL among QQQ's direct AI-debt names; §7.5 says ORCL is NYSE-listed and so outside the Nasdaq-100 (yfinance `exchange = NYQ`; index rule INFERRED, methodology page not read). **The verdict does not depend on it.**
- Its dated catalyst: the **~10/28 hyperscaler cluster** (MSFT / GOOGL / META / AMZN), *"the single most likely ≥15% event in the window"* by VULCAN's words — after this card's 10/16 lapse, inside a Dec-18 expiry.

⇒ **Verdict change: CONDITIONAL → CONDITIONAL, NOT ARMABLE; desk lean LAPSE.** Nothing in the evidence moved toward the card, and the credit leg moved against it. If Will still wants a dated QQQ downside expression for the ~10/28 cluster, that is a **new card with a new window** (moment properties re-marked; tenor re-checked against construction rule #21's band), not a re-dating of this one.

`$0` MOVED · NO ORDER · NO GATE, LEVEL OR WINDOW CHANGED. **APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
