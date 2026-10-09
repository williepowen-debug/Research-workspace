# SELL-OR-ROLL CARD — QQQ $750C Oct-09-2026 ×1 (Fidelity IRA) — expires FRIDAY 10/09

**Date:** 2026-10-08 Thu, written from 19:05 ET (`date` 19:05:09; reads 19:00–19:04 ET, all after the 16:00 close). **Session:** PROME spawn `terry-1008pm` (PROME's C5 commission, WQ-348, plus Tier-1 follow-up of PROME's 15:32 ET booking packet). Model: Claude Opus 5.5 (`claude-opus-5-5`).
**Id:** `MGMT-QQQ750C-OCT09`. A management card on a line Will opened by his own hand. No SETUPS row (management-card convention); registered in `setups/INDEX.md`. ⛔ **A new identity.** It does not continue any earlier QQQ card.
**Thesis owner:** Will. No agent thesis is on file, so this is the off-thesis class. Will has not declared any link to the `MGMT-QQQ755P-OCT09` put, and this card infers none. § 4 states only what happens mechanically when both lines are held together.
**Terry verdict:** 🔒 **CLOSED 2026-10-09 — SOLD TO CLOSE ×1 @ $2.38 by Will's own hand (limit $2.32 Day; proceeds $237.34; realized ≈ +$80.68 vs the $156.66 basis). Fill booked in § 8 (root rule #10). Nothing left on this line.** *(The 10/8 19:05 ET verdict — sell before Friday's close, morning window, no roll — is the dated record: `git show beb763aa3:AGENTS/TERRY/setups/QQQ750C_oct09-sell-or-roll_2026-10-08.md`.)*
**Confidence in the read:** Medium on structure, Low on marks. After hours the option quotes are dead, so tonight's figures are vendor end-of-session screening quotes, and Friday's marks come from Fidelity's bid at the open.
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** The order is Will's (root rule #5).

---

## 1. Position (broker: `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md`; mirror: `git show ef2bc83f1:FORGE/STATUS.md`, ANVIL)

| Field | Value |
|---|---|
| Line | QQQ $750C Oct-09-2026 ×1, long, Fidelity Traditional IRA. The broker shows `NE` on this line, as on the other two Oct-09 lines |
| Fill | **BOUGHT TO OPEN 10/8 ×1 @ $1.56 (limit $1.56, Day order), −$156.66** (Activity, Pending). Broker average $1.57, basis **$156.66** |
| Capture mark | last $1.79 ⇒ $179.00, +$22.34 (+14.26%) `[10/8 rcv]`, i.e. intraday, received ≤ 15:26 ET, exact time UNKNOWN. The broker's "last change −7.14" is shown verbatim and is unexplained (FORGE) |
| Entry half | **UNRECOVERABLE (construction rule #20).** The fill time, the trigger, the do-not-chase level and the reason for the structure are not on any surface and are **not reconstructed here**. This card is **management-only**. `[POSITION_STATE_INCOMPLETE]` (fill time) |
| Working orders | All four 10/8 orders were **Day** orders (Activity), so none of them carries into Friday. Any other working order is UNKNOWN |

## 2. Read at the 10/8 close (moment property, construction rule #14). These are closes and screening marks, NEVER bids

| Item | Value | Basis |
|---|---|---|
| QQQ | **$747.58 [10/8c]** (−1.34% vs $757.73 [10/7c]; day range $743.23–$757.18) ⇒ the 750 strike is **$2.42 (0.32%) OUT of the money** | `fetch.py` 19:00 ET; yfinance daily bar, `regularMarketTime` 16:00:00 ET |
| QQQ after the close | $748.00 at 16:14 (post-close print) · **$748.92–748.99 at 18:55–19:00 ET** (post-market, not a close) | yfinance 1-min / 5-min bars, `prepost` |
| Vendor 750C Oct-09 | **1.92 / 1.94**, mark 1.93, vendor IV 13.55%, volume 66,087, OI 8,667, last trade **16:15** | `chain_fetch.py --no-cache` 19:00 ET. SCREENING ONLY (durable finding 5b). The quote sits against QQQ ≈ $748.0 at 16:14, not the 16:00 close |
| ×1 at that screening bid, after the $0.65 fee | ≈ **$191.35 ⇒ ≈ +$34.69 vs $156.66** (INFERRED, not a fill, not a Friday bid) | arithmetic |
| Catalyst left in the line's life | **None registered for Fri 10/09** on BOND's calendar (`docket/CATALYSTS.tsv`, read 19:0x ET; the 30-year reopening was Thu 13:00). The next dated QQQ-relevant event is the bank prints on Tue 10/13 | BOND docket |

## 3. The sell branch, and why Friday morning

**What waiting costs at an unchanged QQQ** (MODEL: Black–Scholes on a trading-hour clock, calibrated to the 1.93 mid at QQQ $748.00 ⇒ 15.0%. Treat it as shape, not price. Fidelity's bid governs):

| Fri 10/09 | 750C ≈ (QQQ $747.58) | ×1 after the fee ≈ |
|---|---|---|
| 09:45 | $1.72 | $171 |
| **10:30** | **$1.56** | **$155** |
| 12:00 | $1.21 | $120 |
| 14:00 | $0.64 | $63 |
| 15:00 | $0.29 | $28 |
| 15:45 | $0.02 | ≈ $1 |

- **The whole bid is time value** (the call is out of the money), and on expiry day that time value decays fastest in the afternoon. **To get back the $156.66 basis after the fee**, QQQ needs to be at about **$747.3 by 10:00, $748.6 by noon and $750.0 by 14:00** (model). A flat tape turns the line into a loss within the morning.
- **How the price moves with QQQ at Fri 10:00** (model): QQQ $740 ⇒ $0.21 · $745 ⇒ $0.91 · $747.58 ⇒ $1.67 · $750 ⇒ $2.71 · $752.5 ⇒ $4.15 · $755 ⇒ $5.92. Delta ≈ +0.36. One standard deviation to Friday's close ≈ ±$7.
- **Model chance that QQQ closes above $750 on Friday ≈ 36%** (from the 10/8 close). If the sale slips, the exercise branch in § 4 is a real risk.
- **The window, 09:45–10:30 ET:** after the open settles, while most of the time value is still there. **No later than 12:00 ET.** Earlier is cheaper on decay. What a later sale buys is Friday's direction, and that is Will's view to hold, not the desk's: there is no agent thesis behind this call.
- **Suggested harvest (durable finding 9), Will's to adopt or ignore:** sell at any Fidelity bid ≥ **$3.14** (2× the $1.57 average) before the morning window ends. That needs QQQ at about **$750.7–751.0 by 09:45–10:30** (model). On a 1-DTE line the time rail binds first. This is offered only so that the profit zone is not left without a rule.

## 4. The in-the-money-into-the-close branch, the mirror image of the 755P caveat

- **Call alone:** a Friday close **above $750.00** ⇒ an automatic exercise. OCC's standard exercise-by-exception threshold is $0.01 in the money; that it applies to this account is INFERRED. The IRA **BUYS 100 QQQ at $750 = $75,000.**
- **Cash:** $11,421.19 money market, plus +$1,283.98 pending from the three 10/8 fills, ≈ $12,705 once they settle `[10/8 rcv]`. That leaves the purchase **≈ $62,300 unfunded.** An IRA cannot borrow. Fidelity may close the position, act to limit risk, or decline to exercise and forfeit the intrinsic value. A close placed by Fidelity is charged at the Rep-Assisted rate ($32.95 + $0.65 per contract) (Options Agreement 1.734349.120, quoted on `setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` § 4). **Fidelity's actual in-the-money handling in this IRA is UNOBSERVED (FORGE D-60).**
- **This is the mirror image of `MGMT-QQQ755P-OCT09`.** A put in the money at the close *sells* 100 QQQ the IRA does not own (≈ $75,500 short). A call in the money *buys* 100 QQQ the IRA cannot pay for (≈ $75,000).
- ⛔ **With both Oct-09 lines held, no Friday close is safe.** Below $750 the 755P is at least $5 in the money. Above $755 the 750C is at least $5 in the money. Between $750 and $755 **both** are in the money. The closest the pair comes to safety is QQQ $752.50, where each line is still $2.50 in the money. **So whatever QQQ does, at least one of the two lines finishes in the money.**
  - **Between $750 and $755, on paper,** the two exercises cancel each other: buy 100 at $750 and sell 100 at $755 leaves no shares and +$500 gross. Whether Fidelity would process both together in an IRA, or instead close one or both itself at the Rep-Assisted rate, is **UNOBSERVED (D-60). Do not plan on the netting.**
  - ⇒ **Exercise is not a plan; the sale is.** Neither line should be held into Friday's close.

## 5. Roll: NONE unless a trigger appears, and none has

- **No agent thesis and no fired trigger** (durable finding 1: fresh capital goes in only on a fired trigger). A roll pays new cash to keep a 1-DTE bet that no desk has underwritten, and construction rule #21(c) makes any roll a fresh Will decision.
- **For the record, in case Will keeps the bet (construction rule #21: same strike, later expiry, nothing else).** Vendor end-of-session screening quotes, last trades 16:14:

| Form | Far ask − Oct-09 bid 1.92 | ×1 incl. $1.30 fees | Whole far leg (the forward max loss after a roll, construction rule #20(d)) |
|---|---|---|---|
| 750C **Mon Oct-12** (OI 700) | 3.24 − 1.92 = **$1.32/ct** | ≈ $133.30 | ≈ $324 |
| 750C **Fri Oct-16** (OI 36,268) | 6.79 − 1.92 = **$4.87/ct** | ≈ $488.30 | ≈ $679, **above the $500 cap** |

  Re-price on Fidelity's chain at the order. These numbers are moment properties.

## 6. Day colour (root rule #6), written before any order

- **The sale is an EXIT, and root rule #6 governs buys.** A **green** QQQ session gets a better price for a call sale and a red one a worse price. Neither is a break. If both Oct-09 lines are sold in the same session, the colour helps one leg and hurts the other.
- **The buy is recorded, not re-opened.** Will bought on a **red** QQQ day (QQQ $747.16 at 15:26 ET, about −1.4% against $757.73 [10/7c]; it closed −1.34%). That is the rule's favourable colour for buying a call.
- **A roll's buy leg** wants a **red** QQQ session. On a green Friday it would be a wrong-colour call buy, legitimate only with the refuting measurement that `RISK_RULES.md` § "Breaking root rule #6" requires, written in figures before the fill. "It expires today" is a chase.

## 7. Rules on this line, in figures

| Rule | State |
|---|---|
| $500 per card | Forward max loss = the remaining mark (construction rule #20(d)) ≈ **$192 at the screening bid**, inside the cap |
| Construction rule #16 (tenor vs horizon) | A 1-DTE call is a pure timing trade, and the instrument makes Friday's direction the whole bet. Recorded, not graded: this is Will's own hand |
| Durable finding 9 | No harvest rule existed. A suggested form is in § 3 |
| C5 lead (WQ-348: a card two sessions before expiry) | **Impossible at 1 DTE.** This card is written the evening before the last session, which is the earliest any card could exist (the line was bought at ≈ 15:26 ET on 10/8 at the latest) |
| Book context `[10/8 rcv]` | QQQ Oct-09: this call ×1 + 755P ×1. QQQ Oct-15: 745P ×1 + 740P ×4. All are Will's own hand, with no agent thesis |

## Decision

> **For Will:** sell the QQQ $750C Oct-09 ×1 at **Fidelity's bid on Fri 10/09, 09:45–10:30 ET** (desk lean), **no later than 12:00 ET**. At an unchanged QQQ it is worth ≈ $172 at 09:45, ≈ $120 at noon and ≈ $28 at 15:00 (model), and it gets the $156.66 basis back only if QQQ is above ≈ $747.3 at 10:00. **Do not carry it into the close.** Above $750 the IRA would buy 100 QQQ for ≈ $75,000 against ≈ $12.7K of cash. With the 755P ×1 also held, **no Friday close leaves both lines out of the money**, so sell both lines that morning. **No roll is the desk's lean.**
> ⚠️ Tonight's figures are the 10/8 close and vendor end-of-session quotes, not bids. Fidelity's chain at the open governs. Fidelity's handling of an in-the-money option in this IRA has never been observed (D-60).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---

## 8. FILL BOOKED 2026-10-09 Fri, written 13:4x ET (`date` 13:45:36): the line is CLOSED. Root rule #10, a record. PROME spawn (prome-75, Tier 1, DOCKET L660)

**`$0` MOVED BY THE DESK · NO ORDER · NO GATE OR THRESHOLD MOVED.** Source: Will's Fidelity screenshot of 09:52 ET 10/9, relayed by PROME in the spawn brief (PROME's transcription; the screenshot itself is not on this desk's surfaces).

| Order (Will's own hand) | Status | Net |
|---|---|---|
| Sell to Close 1 QQQ Oct 9 2026 750 Call, limit $2.32 (Day) | **FILLED at $2.38** | **+$237.34** |

- **Realized ≈ +$80.68** ($237.34 − the $156.66 basis, § 1) ≈ **+51.5%**. Gross $238.00 − net $237.34 ⇒ **$0.66 of fees** (the $0.65 commission plus ≈ $0.01 Options Fee; INFERRED from gross minus net). The fill was $0.06 above the limit.
- **Fill time: not shown.** The screenshot is 09:52 ET, so the fill is at or before 09:52; whether it fell inside the 09:45–10:30 ET window of § 3 is UNKNOWN. **No execution grade** (durable finding 6: grade only against marks taken at the same time). The § 3 model values are not compared to the fill for the same reason.
- **On record, not graded:** $2.38 is below the ≥ $3.14 harvest level § 3 suggested and Will never adopted; it is above the 10/8 end-of-session screening bid of 1.92. The sale came before the close, so the § 4 exercise branch (buy 100 QQQ ≈ $75,000, UNFUNDABLE) is **void for this line**.
- **Not known to the desk at this write, and NOT inferred:** whether the **`MGMT-QQQ755P-OCT09` ×1** was sold on 10/9, and at what price · whether the **`MGMT-USO150C-OCT09` ×1** was sold (its Fri 15:00 ET hard stop stands). Both are UNKNOWN until Will's next screenshot or Activity view.
- **What this changes on the 755P card:** § 4's "no Friday close is safe with both lines held" was a property of the PAIR. With the call closed, it no longer applies. **If the 755P ×1 is still held, its own rail stands unchanged: never into Friday's close** (in the money at the close ⇒ the IRA sells 100 QQQ at $755 ≈ $75,500 short; D-60).

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
