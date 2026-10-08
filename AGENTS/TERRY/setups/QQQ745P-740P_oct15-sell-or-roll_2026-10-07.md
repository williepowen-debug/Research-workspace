# SELL-OR-ROLL CARD — QQQ $745P Oct-15-2026 ×2 and $740P Oct-15-2026 ×4 (Fidelity IRA) — expire THURSDAY 10/15

**Date:** 2026-10-07 Wed, written from 22:01 ET (`date` 22:01:32; live reads 21:44–21:56 ET, all after the 16:00 close). **Session:** PROME `prome-0e` spawn (Tier 1, C5 commission; WQ-347 / DOCKET L615). Model: Claude Opus 5.5 (`desk` agent definition).
**Ids:** `MGMT-QQQ745P-OCT15` (×2) · `MGMT-QQQ740P-OCT15` (×4). Management cards on lines Will opened by his own hand; no SETUPS rows (management-card convention); registered in `setups/INDEX.md`. ⛔ **New identities.** They do not continue `MGMT-QQQ740P-OCT02` or `MGMT-QQQ735P-OCT05`. Whether either of those was rolled into these, and at what prices, is UNKNOWN until the Activity view (WQ-347). Nothing here books an exit for them.
**Thesis owner:** Will (no agent thesis on file; off-thesis class).
**Terry verdict:** 🟡 **SELL-OR-ROLL BEFORE THURSDAY 10/15. No action owed tonight. Desk lean: SELL both lines at Fidelity's bid on Wed 10/14 after the CPI open settles, 09:45–10:30 ET, no later than Thu 10/15 12:00 ET. No roll.** Re-mark at the C5 line, **Tue 10/13** (two sessions before expiry). The times are a PROPOSAL for Will; nothing registers them as a deadline until he adopts them.
**Confidence in the read:** Medium. Vendor marks after the close; Fidelity's chain governs.
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.**

---

## 1. Positions (source `PROME/data/2026-10-07_broker-capture-TRANSCRIPTION.md`; mirror `FORGE/STATUS.md`, ANVIL `e8fd99acf`)

| Line | Qty | Basis (broker average) | Capture last / value / G/L | Today column |
|---|---|---|---|---|
| QQQ 745P Oct-15 | ×2 | **$567.33** ($2.84) | $2.64 / $528.00 / −$39.33 | −$39.33 = total ⇒ consistent with a same-session entry (date UNVERIFIED) |
| QQQ 740P Oct-15 | ×4 | **$2,122.65** ($5.31) | $1.79 / $716.00 / −$1,406.65 | −$24.00 |

- **Entry fields UNRECOVERABLE from a positions view** (construction rule #20(c)). ⚠️ The 740P's $5.31 average is far above any 740P Oct-15 price this week; it reads like a roll's carried basis, which this desk does not assume. `[POSITION_STATE_INCOMPLETE]`.
- Capture time UNKNOWN (10/7 intraday, Will's word).

## 2. Live read, 2026-10-07 after the close (moment property, construction rule #14)

| Item | 745P Oct-15 | 740P Oct-15 |
|---|---|---|
| QQQ $757.73 close (−0.25%) ⇒ out of the money by | **$12.73 (1.7%)** | **$17.73 (2.3%)** |
| Vendor bid / ask (IV, OI) | **2.52 / 2.56** (16.2%, OI 464) | **1.71 / 1.74** (16.9%, OI 2,401) |
| At the screening bid, after fees | ×2 ≈ **$502.70 ⇒ ≈ −$64.63** | ×4 ≈ **$681.40 ⇒ ≈ −$1,441.25** |
| Model chance of finishing in the money (from tonight) | ≈ 24% | ≈ 18% |

`chain_fetch.py --no-cache` 21:45 ET, SCREENING ONLY. Expected move to Thursday at ~16.5% IV: about ±2.5% (±$19), model.

## 3. What the six sessions hold

| Date | Event | Source |
|---|---|---|
| Thu 10/08 13:00 ET | 30-year bond auction (reopening) | BOND `docket/CATALYSTS.tsv` |
| Mon 10/12 | Columbus Day: stock and option markets OPEN; the cash Treasury market is closed (SIFMA's usual calendar, INFERRED, not read today) | — |
| Tue 10/13 | JPM · WFC · Citi · GS report. **C5 line: this card is re-marked** | OZK desk calendar via the HBAN card's 10/2 addendum |
| **Wed 10/14 08:30 ET** | **September CPI** (BLS); BAC · MS report; Beige Book 14:00 | BOND `docket/CATALYSTS.tsv` |
| Thu 10/15 | **Expiry**; USB reports | as above |

**The cost of holding to CPI, at an unchanged QQQ** (MODEL: Black–Scholes at the vendor IVs, decay ratios applied to tonight's marks; flat vol):

| When | 745P ×2 ≈ | 740P ×4 ≈ | Both ≈ |
|---|---|---|---|
| Tonight (screening bids) | $504 | $684 | **$1,188** |
| Tue 10/13 close | $120 | $104 | $224 |
| **Wed 10/14 10:00 (after CPI)** | **$104** | **$84** | **$188** |
| Thu 10/15 10:00 | $20 | $8 | $28 |

**What a move into CPI does** (model, Wed 10/14 10:00): QQQ −1% (≈ $750) ⇒ both lines ≈ $760 · QQQ −2% (≈ $742.6) ⇒ ≈ $2,190, still below the combined basis of **$2,689.98** · QQQ −2.5% (≈ $738.8) ⇒ ≈ $3,330. Break-even on the two lines together needs about −2.2% by Wednesday morning.

⇒ **Said plainly:** at an unchanged QQQ, carrying these to CPI costs about **$1,000 of tonight's ≈ $1,188 screening value**. That is the price of the CPI bet, and it is Will's bet to keep or drop. If CPI is not why he holds them, **selling sooner keeps most of that $1,000**; the desk does not argue him out of the event he bought.

## 4. The proposed sell-or-roll time, and why

- **Wed 10/14, 09:45–10:30 ET** (after the CPI open settles). CPI is the last dated event the tenor spans. After it, the lines hold one session of time value and expiry-day gamma; at an unchanged QQQ that is ≈ $188 Wednesday morning against ≈ $28 Thursday morning.
- **Latest: Thu 10/15, no later than 12:00 ET.** Only if Will wants Wednesday's session too (Beige Book, BAC/MS prints).
- **Why not hold to Thursday's close:** the exercise path below.

## 5. The exercise path if held to Thursday's close

- 745P ×2 below $745 ⇒ the IRA **sells 200 QQQ = $149,000 short** · 740P ×4 below $740 ⇒ **400 QQQ = $296,000 short**. Both ⇒ **$445,000 short**, against $12,993.82 cash and −$1,572.64 pending (capture).
- An IRA cannot hold a short. Fidelity may close, minimize risk, or tell the OCC not to exercise, forfeiting the intrinsic value; a Fidelity-placed close costs $32.95 + $0.65/contract (Options Agreement 1.734349.120, quoted on `setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` § 4). Fidelity's actual handling in this IRA is **UNOBSERVED (FORGE D-60)**. ⇒ **Exercise is not a plan.**

## 6. Roll forms (construction rule #21: same strike · later expiry · nothing else)

| Form | Tonight's screening net (far ask − near bid) | Full size | One contract | $500 cap |
|---|---|---|---|---|
| 745P Oct-15 → **Oct-23** | 5.48 − 2.52 = **$2.96/ct** | ×2 ≈ $594.60 (1.2×) | ≈ $297.30 | full size FAILS · one passes |
| 740P Oct-15 → **Oct-23** | 4.35 − 1.71 = **$2.64/ct** | ×4 ≈ $1,058.60 (2.1×) | ≈ $265.30 | full size FAILS · one passes |

- Model debits at Wed 10/14 10:00, unchanged QQQ: **≈ $3.25/ct (745)** and **≈ $2.55/ct (740)**. Re-price at the order; these are moment properties.
- **If Will rolls anyway:** the cap allows **one** contract of one line per card (≈ $300), the rest sold. It is a trim, and root rule #7 reads a trim as a broken thesis; it is offered because the $500 cap binds on the new debit. Do-not-chase: **$3.60/ct (745) · $3.10/ct (740)**, as one net-debit order.
- **Why the desk's lean is no roll:** no agent thesis, no fired trigger (durable finding 1). The dated alternative PROME proposed as the replacement for short-dated QQQ puts (WQ-365) cannot arm tonight: HY OAS printed 310 · 312 · 303 on 10/2 · 10/5 · 10/6 (FRED); it needs two cells ≥ 321, and its own credit kill line is 312. ⚠️ **Construction rule #16 applies on its face:** this book now carries the same QQQ view in 2-day and 6-day puts (eight contracts, ≈ $1,590 at tonight's screening bids against $3,167.31 of basis), and that tenor is the costliest way to hold it.

## 7. Day colour (root rule #6), written before any order

- **Sales:** root rule #6 governs buys; a red QQQ day fetches a better put price. Not a break either way.
- **A roll's buy leg** wants a **green** QQQ session. A red-day roll is legitimate only with the measurement `RISK_RULES.md` § "Breaking root rule #6" requires, in figures, before the fill. "It expires tomorrow" is a chase.

## 8. Rules on these lines, in figures

| Rule | State |
|---|---|
| $500 per card | Forward max loss = the remaining marks (construction rule #20(d)) ≈ **$1,188** together ≈ 2.4× the cap. Will's own hand, recorded |
| Durable finding 9 | ⚠️ No P/L-keyed harvest on either line. Suggested forms, Will's to adopt or not: 745P ×2 at any Fidelity bid ≥ $5.68 (2× $2.84) · 740P ×4 at any bid ≥ $5.31 (back to the broker basis) |
| Book context | With the 755P Oct-09 ×2 (`MGMT-QQQ755P-OCT09`), eight QQQ puts on two expiries. Same view, same direction |

## Decision

> **For Will:** sell the QQQ $745P Oct-15 ×2 and $740P Oct-15 ×4 at Fidelity's bid on **Wed 10/14, 09:45–10:30 ET, after the CPI open** (desk lean), no later than **Thu 10/15 12:00 ET**; or sooner if CPI is not why you hold them (holding to CPI costs about $1,000 of tonight's ≈ $1,188 at an unchanged QQQ). **No roll is the desk's lean**; the $500 cap allows rolling one contract to Oct-23, not the lines.
> ⚠️ Vendor marks after the close; Fidelity governs. The desk re-marks these on Tue 10/13.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
