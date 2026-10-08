# SELL-OR-ROLL CARD — QQQ $755P Oct-09-2026 ×2 (Fidelity IRA) — expires FRIDAY 10/09

**Date:** 2026-10-07 Wed, written from 21:58 ET (`date` 21:58:33; live reads 21:44–21:56 ET below, all after the 16:00 close). **Session:** PROME `prome-0e` spawn (Tier 1, C5 commission: every option line Will holds gets a sell-or-roll card at least two sessions before expiry; WQ-347 / DOCKET L614). Model: Claude Opus 5.5 (`desk` agent definition).
**Id:** `MGMT-QQQ755P-OCT09` (management card on a line Will opened by his own hand; no SETUPS row, by convention for management cards; registered in `setups/INDEX.md`). ⛔ **A new identity.** It does not continue `MGMT-QQQ740P-OCT02` or `MGMT-QQQ735P-OCT05`; how those left the account is UNKNOWN (no Activity view).
**Thesis owner:** Will (no agent thesis on file; off-thesis class).
**Terry verdict:** 🔴 **SELL-OR-ROLL BEFORE FRIDAY'S CLOSE. Desk lean: SELL both at Fidelity's bid on Fri 10/09 between 09:45 and 10:30 ET, and no later than 12:00 ET. No roll.** Holding to Friday's close is BAD STRUCTURE: worthless above $755, and below $755 an exercise into a 200-share QQQ short (≈ $151,000) sitting in the IRA over a weekend. **The times above are a PROPOSAL for Will to adopt or change. Nothing registers them as a deadline until he does.**
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

> **For Will:** sell the QQQ $755P Oct-09 ×2 at Fidelity's bid **Fri 10/09, 09:45–10:30 ET, no later than 12:00 ET** (desk lean; Thursday 14:00–15:30 ET, after the 30-year auction result, is an equally good form), or **Thursday morning** if you no longer want Thursday's session (holding it costs ≈ $160 for the two at an unchanged QQQ). **No roll is the desk's lean**; if you roll anyway, roll **one** to the **755P Oct-16** as one net-debit order at no more than **$4.85/ct**, on a green QQQ session, and sell the other.
> ⚠️ Every quote here is a vendor mark taken after the close; Fidelity's chain at the open governs. Holding to the close risks an assignment into a ≈ $151,000 short the IRA cannot carry.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
