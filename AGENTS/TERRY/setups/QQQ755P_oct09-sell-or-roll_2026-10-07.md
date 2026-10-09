# SELL-OR-ROLL CARD — QQQ $755P Oct-09-2026 ×1 (was ×2; Will sold 1 on 10/8) (Fidelity IRA) — expires FRIDAY 10/09

**Date:** 2026-10-07 Wed, written from 21:58 ET (`date` 21:58:33; live reads 21:44–21:56 ET below, all after the 16:00 close). **Session:** PROME `prome-0e` spawn (Tier 1, C5 commission: every option line Will holds gets a sell-or-roll card at least two sessions before expiry; WQ-347 / DOCKET L614). Model: Claude Opus 5.5 (`desk` agent definition).
**Id:** `MGMT-QQQ755P-OCT09` (management card on a line Will opened by his own hand; no SETUPS row, by convention for management cards; registered in `setups/INDEX.md`). ⛔ **A new identity.** It does not continue `MGMT-QQQ740P-OCT02` or `MGMT-QQQ735P-OCT05`; how those left the account is UNKNOWN (no Activity view).
**Thesis owner:** Will (no agent thesis on file; off-thesis class).
**Terry verdict:** 🔴 **SELL-OR-ROLL BEFORE FRIDAY'S CLOSE — NOW ×1 (§ 9, 2026-10-08 19:0x ET: Will SOLD 1 of 2 on 10/8 @ $8.36; ONE remains, ≈ $7.42 in the money at the $747.58 close [10/8c]). Desk lean: SELL the remaining ×1 at Fidelity's bid on Fri 10/09, morning preferred (09:45–10:30 ET); NEVER into Friday's close (≈ $75,500 assignment branch). No roll. With the new `MGMT-QQQ750C-OCT09` also held, every Friday close leaves at least one of the two lines in the money (§ 9).** *(was, 10/8 09:5x: ~~SELL both at Fidelity's bid TODAY, the earlier the cheaper; holding for the 13:00 30-year auction is Will's call (then 14:00–15:30 ET)~~ — Will sold one of the two; § 8 is the dated record. Was, 10/7: ~~SELL both at Fidelity's bid on Fri 10/09 between 09:45 and 10:30 ET, and no later than 12:00 ET~~ — superseded 10/8 09:5x because the put went in the money and into profit with no harvest rule on file.)* Holding to Friday's close is BAD STRUCTURE: worthless above $755, and below $755 an exercise into a 100-share QQQ short (≈ $75,500; was ≈ $151,000 on ×2) sitting in the IRA over a weekend. **The times above are a PROPOSAL for Will to adopt or change. Nothing registers them as a deadline until he does.**
**Confidence in the read:** Medium. Every option figure is a vendor screening mark taken after the close; Fidelity's chain at the open governs.
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** The order is Will's (root rule #5).

---

## 1. Position (source `PROME/data/2026-10-07_broker-capture-TRANSCRIPTION.md`; mirror `FORGE/STATUS.md`, ANVIL `e8fd99acf`)

| Field | Value |
|---|---|
| Line | QQQ $755P Oct-09-2026 ×2, long, Fidelity Traditional IRA |
| Basis | **$477.33** ($2.39 average, rounded by the broker) |
| Capture mark | last $2.24 ⇒ value $448.00, −$29.33 (−6.15%). Today column $0.00: not a same-session entry. **Capture time UNKNOWN** (Will: "yes today", 10/7 intraday) |
| Entry fields | **UNRECOVERABLE from a positions view** (construction rule #20(c)): fill date, fill price and whether it was a roll leg are unknown until the Activity view (WQ-347). `[POSITION_STATE_INCOMPLETE]` |
| Badge | The capture shows `NE` on this line and on the USO Oct-09 150C, the two lines that expire Friday. Meaning not stated on the screen (INFERRED: a near-expiry flag) |

## 2. Live read, 2026-10-07 after the close (moment property, construction rule #14)

| Item | Value | Basis |
|---|---|---|
| QQQ | **$757.73 close (−0.25%)** ⇒ the 755 strike is **$2.73 (0.36%) out of the money** | `fetch.py` 21:44 ET; yfinance daily bar |
| QQQ path | 10/1 $742.03 · 10/2 $749.58 · 10/5 $756.20 · 10/6 $759.66 · 10/7 $757.73 | yfinance daily closes |
| Vendor 755P Oct-09 | **2.02 / 2.07**, mark 2.04, IV 14.57%, OI 3,632, last trade 16:14 | `chain_fetch.py --no-cache`, 21:44 ET, SCREENING ONLY |
| Two at the screening bid, after $1.30 fees | **≈ $402.70 ⇒ ≈ −$74.63 vs basis** (INFERRED, not a fill) | arithmetic |
| VXN | 21.00 (10/7 close) | yfinance |

## 3. What Friday holds, and why the proposed time is Friday morning, not Thursday

**The cost of each session, at an unchanged QQQ** (MODEL: Black–Scholes at the vendor's 14.57% IV, decay ratios applied to tonight's $2.04 mark; flat vol, so treat as shape, not price):

| When | One put ≈ | Two ≈ |
|---|---|---|
| Tonight (screening bid 2.02) | $2.02 | $404 |
| Thu 10/08 close | $1.23 | $246 |
| **Fri 10/09 09:45–10:30** | **$1.05–1.20** | **$210–240** |
| Fri 12:00 | $0.82 | $164 |
| Fri 15:00 | $0.17 | $34 |

- **The one dated event left in the line's life is Thursday's 30-year bond auction at 13:00 ET** (a reopening; BOND `docket/CATALYSTS.tsv`, TreasuryDirect upcoming). This desk has no QQQ thesis, so it cannot say the auction is worth holding for. **But a put bought this week and held through Wednesday has Thursday's session as the only exposure it still owns.**
- **Why not Thursday morning:** a sale before the auction gives up that session's exposure (the auction, and any rates-to-equity move after it) to save **≈ $160 for the two at an unchanged QQQ**, the Thursday decay in the table. If Will no longer wants that exposure, **Thursday morning is the cheaper exit and the right one.** That is his view to state, not the desk's.
- **An equally good form: Thursday AFTER the result, 14:00–15:30 ET.** It keeps the auction, avoids expiry day, and saves ≈ $10–30 of overnight decay against Friday's open. What it gives up is Friday's opening gap, which for a long put is the convexity side. The desk names Friday 09:45–10:30 as the latest good window, not the only one.
- **Why Friday morning and not Friday afternoon:** after the auction is known, the put holds nothing but time value and gamma. On expiry day that time value goes fastest in the afternoon (≈ $210–240 at 10:00 → ≈ $164 at noon → ≈ $34 at 15:00, unchanged QQQ), and **the exercise branch is a coin-flip-class risk near the close**: the model puts the chance of finishing below $755 at **≈ 38%** from tonight. Selling between 09:45 (after the open settles) and 10:30 takes most of what is left.
- **Expected move to Friday:** at 14.6% IV, about ±$9.8 (±1.3%) over the two sessions, model. So the strike is well inside one day's normal range.

## 4. The exercise path if held to Friday's close

- A close **below $755.00** ⇒ the IRA **sells 200 QQQ at $755 it does not own = $151,000 short**. Each $1 gap up on Mon 10/12 = −$200.
- Cash: **$12,993.82 money market, −$1,572.64 pending** (capture). Nowhere near $151,000. An IRA cannot hold a short (Fidelity Options Agreement, form 1.734349.120, quoted on `setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` § 4): Fidelity may close the position, act to minimize market risk, or tell the OCC not to exercise, forfeiting the intrinsic value. A Fidelity-placed close is charged at the Rep-Assisted rate ($32.95 + $0.65/contract).
- Fidelity's actual in-the-money handling in this IRA is **UNOBSERVED (FORGE D-60)**. ⇒ **Exercise is not a plan; the sale is.**

## 5. Roll form, if Will keeps the bet (construction rule #21: same strike · later expiry · nothing else)

| Form | Tonight's screening net (buy the far ask, sell the 755P Oct-09 bid 2.02) | ×2 incl. $2.60 fees | ×1 incl. $1.30 fees | $500 cap |
|---|---|---|---|---|
| **755P Oct-16** (Fri; OI 8,140) | 6.04 − 2.02 = **$4.02/ct** | ≈ $806.60 | ≈ **$403.30** | ×2 FAILS (1.6×) · ×1 passes |
| 755P Oct-15 (Thu; OI 257) | 5.43 − 2.02 = $3.41/ct | ≈ $684.60 | ≈ $342.30 | ×2 FAILS (1.4×) · ×1 passes |

- **⚠️ Friday's debit will be higher than tonight's**, because the Oct-09 leg loses most of its value by Friday while the far leg keeps most of its own: model at 10:00 Friday, unchanged QQQ, **≈ $4.30/ct for Oct-16** (≈ $431 for one).
- **If Will rolls:** **ONE 755P Oct-16, as one net-debit order, do-not-chase $4.85/ct** (≈ $486.30 all-in, inside the $500 cap), the other contract SOLD. That is "sell one, roll one". It is a trim, and root rule #7 reads a trim as a broken thesis; it is offered because the $500 cap binds on the new debit, not because the desk reads the thesis as broken. **Oct-16, not Oct-15:** Thursday 10/15 already carries the 745P ×2 and 740P ×4 (`MGMT-QQQ745P-OCT15` · `MGMT-QQQ740P-OCT15`), and the Oct-16 strike is about 30× as liquid.
- **Why the desk's lean is no roll:** no agent thesis, no fired trigger (durable finding 1), and the dated alternative that PROME proposed as the replacement for short-dated QQQ puts (WQ-365, `TRY-COND-QQQ-DATED-DOWNSIDE`) cannot arm on tonight's marks: its credit leg retraced (HY OAS 310 · 312 · 303 on 10/2 · 10/5 · 10/6, FRED; it needs two cells ≥ 321). A roll pays new cash to keep a view that the evidence desks have not moved toward this week.

## 6. Day colour (root rule #6), written before any order

- **The sale:** root rule #6 governs buys. Selling a put on a red QQQ day fetches a better price; on a green day a worse one. It is not a break either way (desk precedent, `MGMT-QQQ735P-OCT05` 10/2 addendum).
- **A roll's buy leg** wants a **green** QQQ session (QQQ last > its prior regular-session close at the order). If Friday is red and Will still rolls, that is a wrong-colour put buy. It is legitimate only with the measurement `RISK_RULES.md` § "Breaking root rule #6" requires: the live Fidelity net debit for the same strikes at or below the last green-session debit recorded on this card, in figures, before the fill. "It expires today" is a chase, not a break.

## 7. Rules on this line, in figures

| Rule | State |
|---|---|
| $500 per card | Forward max loss = the remaining mark (construction rule #20(d)) ≈ **$404 at the screening bid**, inside the cap |
| Durable finding 9 (a harvest rule for every profit zone) | ⚠️ No P/L-keyed harvest exists. Suggested form, Will's to adopt or not: sell both at any Fidelity bid ≥ $4.78 (2× the $2.39 average) before Friday's sale. Needs QQQ near $751 (−0.9%) by Thursday's close (model: ≈ $4 intrinsic plus ≈ $0.8 time value) |
| Construction rule #16 (tenor vs horizon) | A 2-session put is a timing trade. The desk's dated alternative (WQ-365) is not armable tonight (§ 5) |
| Book context (capture marks) | Eight QQQ puts on two expiries: this ×2 (Fri 10/09) + 745P ×2 and 740P ×4 (Thu 10/15). Combined capture value $1,692 vs basis $3,167.31. All are Will's own hand |

## Decision

> ⛔ **SUPERSEDED 2026-10-08 19:0x ET by § 9 below** (Will sold 1 of 2 on 10/8; the decision now covers ONE contract on Friday). Kept as the dated record:
> **For Will (REVISED 2026-10-08, § 8):** sell the QQQ $755P Oct-09 ×2 at Fidelity's bid **TODAY** — now is the desk lean (11:03 screening bid **2.42–2.57** ⇒ ≈ **$482.70–$512.70 net, +$5 to +$35** vs $477.33; it was +$181.37 at 09:3x — **the profit went in an hour**, which is why the line needs a harvest rule it does not have); **14:00–15:30 ET after the 13:00 30-year auction result** if you want that session (≈ $70–90 of decay for the two at an unchanged QQQ, against a ≈ ±$335 one-sd swing). **Do not carry it into Friday:** it is in the money, and a slipped sale lands on the ≈ $151,000 assignment branch. **No roll is the desk's lean**; if you roll anyway, roll **one** to the **755P Oct-16** as one net-debit order at no more than **$4.85/ct** on a **green** QQQ session (today is red), and sell the other. *(was: ~~Fri 10/09, 09:45–10:30 ET, no later than 12:00 ET~~.)*
> ⚠️ Every quote here is a vendor mark taken after the close; Fidelity's chain at the open governs. Holding to the close risks an assignment into a ≈ $151,000 short the IRA cannot carry.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## 8. ADDENDUM 2026-10-08 Thu, written 09:54 ET (`date` 09:54:30) — C5 re-mark at the open (Will's direct session `terry-01`, sole TERRY writer, PROME-acked; completes the 09:00 pre-open memo's §0 checklist)

**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD MOVED.** Every option figure is a vendor SCREENING mark (durable finding 5b): pulled **09:52:37 ET**, but the quotes' last trades are **09:34–09:37**, so they are ≈ 15 min old against the spot. **Fidelity's live bid governs.** Local clock checked against two external HTTP `Date` headers at 09:52:56 ET — agreement to the second.

| Item | Value | Basis |
|---|---|---|
| QQQ | **$753.57** (09:52 ET) vs $757.73 [10/7c] = **−0.55%, RED** ⇒ the 755P is **$1.43 IN the money** | yfinance `fast_info` |
| 755P Oct-09 | **3.30 / 3.31**, last 3.34, IV 11.1%, OI 4,246, vol 1,713 | `chain_fetch.fetch_chain`, last trade 09:36 |
| Intrinsic / time value | $1.43 / **$1.87** per contract | arithmetic at the screening bid |
| ×2 at the bid, after $1.30 fees | **≈ $658.70 ⇒ +$181.37 (+38.0%) vs $477.33** (INFERRED, not a fill) | arithmetic |
| ≥ $4.78 harvest suggestion (10/7, never adopted) | **NOT reached** — needs QQQ ≈ $751 or lower with today's time value | card § 7 |
| 755P Oct-16 (roll leg) | 7.39 / 7.48, OI 9,671 ⇒ roll ≈ **$4.18/ct** (7.48 − 3.30) ⇒ ×1 ≈ $419.30 incl. fees (inside $500) · ×2 ≈ $838.60 (fails the cap) | screening |

**What waiting costs, at an unchanged QQQ** (MODEL, Black–Scholes calibrated to the 3.305 mid at 10.0%, trading-hour clock; shape, not price — the spot and the quote are ≈ 15 min apart):

| When | One put ≈ | Two ≈ (gross) |
|---|---|---|
| Now (screening bid) | $3.30 | $660 |
| Thu 13:15, after the auction result | $2.94 | $588 |
| Thu 14:30 | $2.80 | $560 |
| Fri 10:00 | $2.55 | $510 |
| Fri 15:00 | $1.65 | $330 |

- One-sd QQQ move to Thu 14:30 at that vol ≈ **±$3.90** (≈ ±$470 on the pair at the put's delta); model chance of finishing below $755 ≈ **59%**.
- **Why the lean moved from "today after the auction" to "now":** the line is **in profit (+38%) and no harvest rule exists on it** — durable finding 9's exact gap (every profit zone needs its own harvest rule; the card's management was keyed to dates, not to P/L). Holding to 14:30 pays ≈ $100 of decay for a coin-flip-sized session swing, and **no agent thesis stands behind the put** (thesis owner: Will). The auction is a real dated event; holding for it is **Will's view to state, not the desk's**, and 14:00–15:30 remains a legitimate form.
- **Do not carry it into Friday:** in the money at Friday's close ⇒ exercise into a 200-share QQQ short (≈ $151,000) the IRA cannot carry (§ 4; D-60 UNOBSERVED).
- **Root rule #6:** the sale is an EXIT; the rule governs buys. A red QQQ day is the favourable colour to SELL a put. A roll's buy leg today would be a **wrong-colour put buy** (QQQ red) with no refuting measurement on file ⇒ not a break.
- **Roll: NONE** — no agent thesis, no fired trigger (durable finding 1); WQ-365 still NOT ARMABLE (HY OAS **303** [10/6], FRED own pull 09:23 ET; the 10/7 cell unpublished).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

### § 8-bis RE-PULL 2026-10-08 11:03 ET (`date` 11:02:58; external `Date` 15:02:56 GMT agrees) — after a wifi outage; § 8's 09:52 marks are a dated record, NOT current

| Item | 11:03 value | vs 09:52 |
|---|---|---|
| QQQ | **$754.27 (−0.46% vs $757.73 [10/7c]), RED ⇒ $0.73 in the money** | was $753.57, $1.43 ITM |
| 755P Oct-09 | **2.42 / 2.43** (scan 11:03:03, last trade 10:47) and **2.57 / 2.59** (`chain_fetch.py --no-cache --legs 755`, seconds later: ✓ usable, rc 0; `DIRINC` advisory fired — the vendor quote is lagging the spot) ⇒ quoted as a RANGE | was 3.30 / 3.31 |
| ×2 at the bid, after $1.30 | **≈ $482.70–$512.70 ⇒ +$5.37 to +$35.37 vs $477.33** (INFERRED) | was +$181.37 |
| 755P Oct-16 (roll leg) | 6.69 / 6.70 ⇒ roll ≈ **$4.13–4.28/ct** (×1 inside $500, ×2 fails) | was $4.18 |

- **Model** (calibrated to the 2.425 mid at 8.5%; shape, not price): at an unchanged QQQ one put ≈ $2.21 at 13:15, **$2.09 at 14:30**, $1.87 at Fri 10:00, $1.05 at Fri 15:00. One-sd QQQ move to 14:30 ≈ **±$3.05** ⇒ ≈ **±$335** on the pair (delta ≈ −0.55). Chance of finishing below $755 ≈ **56%** ⇒ the Friday assignment branch is better than even if the sale slips.
- **Lean CONFIRMED: SELL both TODAY, now preferred; after the auction result (14:00–15:30) is Will's call.** ★ **Durable finding 9 measured in one hour:** at 09:3x the line was +$181 in profit with no rule that would take it; by 11:03 it was ≈ breakeven. That is the cost of a profit zone without a harvest rule — recorded as a datum, not a grade of Will's hand.
- **Roll: NONE** (unchanged — no agent thesis, no fired trigger; a put buy on a red QQQ day is wrong-colour with no refuting measurement on file). `[POSITION_STATE_UNKNOWN]` for today: if Will has already acted, his fill governs and gets recorded (root rule #10).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## 9. ADDENDUM 2026-10-08 Thu, written 19:06 ET (`date` 19:06:47): FILL BOOKED (root rule #10). The card now governs ONE contract. PROME spawn `terry-1008pm` (C5 / WQ-348 + Tier-1 follow-up of PROME's 15:32 ET booking packet)

**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD MOVED.** Broker facts come from `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md` (ties to the cent, $34,650.69) and the reconciled mirror `git show ef2bc83f1:FORGE/STATUS.md` (ANVIL).

**Fill (Will's own hand, Activity "Pending", 10/8):**

| Order | Status | Net |
|---|---|---|
| Sell to Close 1 QQQ Oct-9 755 Put, limit $8.28 (Day) | **Filled at $8.36** | **+$835.32** |
| Sell to Close 1 QQQ Oct-9 755 Put, limit $8.50 (Day) | **Verified Canceled** | — |

- **Realized on the sold lot ≈ +$596.65** ($835.32 − the $238.67 lot basis; derived from the broker's lot basis by ANVIL `ef2bc83f1`, not shown as a single figure by the broker). **ONE contract remains:** basis $238.66 (average $2.39), capture last $7.85 ⇒ $785.00 `[10/8 rcv]`.
- **The fill time is UNKNOWN**, so no execution grade is possible (durable finding 6: grade only against marks taken at the same time). On record: $8.36 is 3.5× the $2.39 average and above the ≥ $4.78 harvest level that § 7 suggested and Will never adopted.
- Selling one of two is a trim in root rule #7's vocabulary. There is no agent thesis on this line for a trim to signal as broken, so it is recorded, not graded.
- Both 10/8 sell orders were Day orders, so neither carries into Friday. Any other working order is UNKNOWN.

**The remaining ×1, at the 10/8 close.** These are closes and screening marks, NEVER bids:

| Item | Value | Basis |
|---|---|---|
| QQQ | **$747.58 [10/8c]** (−1.34%) ⇒ the put is **≈ $7.42 IN the money** | `fetch.py` 19:00 ET (`regularMarketTime` 16:00:00) |
| Vendor 755P Oct-09 | 7.08 / 7.30, last trade 16:14. The bid sits *below* the 16:00 intrinsic of $7.42 because the quote was struck against QQQ ≈ $748.00 at 16:14, where intrinsic is $7.00 (post-close print, yfinance 1-min) | `chain_fetch.py --no-cache` 19:00 ET, SCREENING ONLY |
| ×1 at that screening bid, after $0.65 | ≈ $707.35 ⇒ ≈ +$468.69 vs $238.66 (INFERRED, not a Friday bid) | arithmetic |
| Post-market | QQQ $748.92–748.99 at 18:55–19:00 ET (not a close) | yfinance |

- **Model** (calibrated to the 7.19 mid at QQQ $748.00; shape, not price): at an unchanged QQQ the put is ≈ $7.56 at Fri 09:45 and ≈ $7.42 by 14:00. Almost all of it is intrinsic, so **waiting costs only ≈ $15 of time value. The risk is direction:** delta ≈ −0.94, so each +$1 in QQQ costs ≈ $94. The model puts the chance of a Friday close below $755 at **≈ 85%**.
- ⛔ **Never into Friday's close, now for ONE contract.** In the money at the close ⇒ an exercise that **sells 100 QQQ at $755 = ≈ $75,500 short** (was ≈ $151,000 on ×2). The IRA holds 0 QQQ and ≈ $11,421 cash (+$1,283.98 pending), and an IRA cannot carry a short. Fidelity's handling is **UNOBSERVED (FORGE D-60)**. **Exercise is not a plan; the sale is.**
- 🆕 **The new `MGMT-QQQ750C-OCT09` (Will bought it on 10/8; Will has declared no link to this put and none is inferred) changes the close arithmetic.** With both lines held, below $750 this put is at least $5 in the money, above $755 the call is, and between the two strikes both are. **No Friday close leaves both out of the money.** The pair is never safer than at QQQ $752.50, where each line is still $2.50 in the money. Full branch, including the on-paper netting that is UNOBSERVED at Fidelity: `setups/QQQ750C_oct09-sell-or-roll_2026-10-08.md` § 4.
- **Root rule #6:** the sale is an EXIT. A red QQQ session gets a better price for a put sale and a green one a worse price. Neither is a break. Selling both Oct-09 lines in one session puts one leg on each side of the colour.
- **Roll: NONE** (unchanged). There is no agent thesis and no fired trigger (durable finding 1), and WQ-365's dated alternative is still not armable. The construction rule #21 form in §§ 5 / 8 is a dated record, to be re-priced at any order.

> **For Will (CURRENT, 2026-10-08 19:0x ET):** sell the **remaining QQQ $755P Oct-09 ×1** at **Fidelity's bid on Fri 10/09, morning preferred (09:45–10:30 ET)**, in the same window as the $750C ×1. **Never into Friday's close.** It is ≈ $7.42 in the money [10/8c], and a slipped sale lands on the ≈ $75,500 assignment branch, which is ≈ 85% likely at an unchanged QQQ (model). **No roll.** ⚠️ Every figure here is a close or a vendor end-of-session quote. Fidelity's bid at the open governs.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## 10. NOTE 2026-10-09 Fri, written 13:4x ET: this line's Friday disposition is UNKNOWN to the desk. PROME spawn (prome-75, Tier 1, DOCKET L660)

- Will's 09:52 ET Fidelity screenshot (relayed by PROME) shows **only** the sale of the `MGMT-QQQ750C-OCT09` ×1 (@ $2.38, booked on that card § 8). **Whether this 755P ×1 was sold on 10/9, and at what price, is UNKNOWN. Nothing is inferred and nothing is booked here.**
- **What changed:** the call is closed, so § 9's pair caveat ("no Friday close leaves both lines out of the money") no longer applies. **If this put is still held, its own rail stands unchanged: SELL at Fidelity's bid, never into Friday's close** (in the money at the close ⇒ the IRA sells 100 QQQ at $755 ≈ $75,500 short; Fidelity's handling UNOBSERVED, D-60). Any fill is booked on Will's next screenshot or Activity view (root rule #10).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
