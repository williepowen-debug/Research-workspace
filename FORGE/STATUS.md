# FORGE — Trading Operations

> **Execution update — September 9, 2026:** Will confirmed the sale of the remaining USO October 16 $135 call and supplied the [broker receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md): ×1 sold at $17.55, net $1,754.30, settlement September 10. This position is CLOSED (qty 0); B/C management checks discharged. Remaining-lot basis $710.66 from the September 9 screenshot implies realized gain $1,043.64. Cash and account totals below retain their September 3 vintage and are not post-sale balances; closed-row historical values are retained only in its note. No share sale or other option execution inferred.

> **Structured position-truth mirror — reconciled 2026-09-03 (Thu) by ANVIL from ONE Will screenshot (PROME-transcribed → `PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md`): the Fidelity Traditional IRA 216461326 positions view ONLY. ⚠️ MARKS ARE LIVE INTRADAY Thu 9/3 ~15:07 ET, NOT CLOSES ("Today's gain/loss" populated, market open) — cite as `[Fidelity positions, 9/3 ~15:07 ET intraday]`. No activity view this pass (asked of Will); Robinhood NOT captured. Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written.** Prior vintage: the 8/29 reconcile from the Fri 8/28 CLOSE screenshot pair + Fidelity Activity 7/30–8/28 (`PROME/data/2026-08-29_broker-capture-TRANSCRIPTION.md`; this file at commit `183068dd1`; its resolved rows → `FORGE/_archive/RECONCILE_2026-08-29_RECORD.md`). Earlier reconciles (08-14, 08-02, 07-30, 07-20, 07-16, 05-21) in git history. Refresher flow = Will-on-broker-capture → PROME transcribes → ANVIL reconciles. Old execution ledger + per-trade folders → `FORGE/_archive/`.
>
> ⚠️ **ACCOUNT SCOPE — ONE ACCOUNT THIS PASS: Fidelity Traditional IRA 216461326** (number per the 8/29 capture header; not visible on this image), positions view only. **Robinhood NOT CAPTURED** — every Robinhood row below is 8/28 vintage or PROME-supplied, i.e. "not in this capture's account, unverified today." **No Fidelity activity view** ⇒ the three quantity changes vs 8/28 (QQQ 3 sh absent · USO 135C 2→1 · TLT 85P 2→1) are broker-verified as STATE, but their dates/prices are not, and the cash bridge (D-45) stays a labeled hypothesis until the activity view lands. Absence from a positions view is not itself proof of closure; rows absent today are **retained and flagged, never deleted**. See **§ Reconcile discrepancies (9/3)**.

> **Events since the 8/29 reconcile, by label.** **BROKER-VERIFIED (this capture):** USO $135C Oct-16 qty 2→1 · TLT $85P Sep-30 qty 2→1 · QQQ 3 sh absent · cash $13,600.67 → $18,025.71, no pending line. **PROME-SUPPLIED (Will's word, not broker-verified):** 9/2 14:21 ET SOLD 1× USO $135C (price **UNKNOWN — permanent by WQ-167, never an ask**) · 9/2 14:21 ET BOUGHT 1× WAL Dec-18-2026 $70P @ $2.20 in **ROBINHOOD** (TRY-WAL-ROLL70; $4.40 harvest GTC status **UNKNOWN by WQ-167, never an ask**). **RULINGS — WQ-168 (Will 12:45 9/3, verbatim "Approve WQ-168 with your rec"):** WAL $70P + $67.5P Sep-18 LAPSE (70P re-opens only if WAL closes <$71 in the week of 9/14) · KRE $60P Sep-30 ×2 LAPSE · TLT $77P ×25 HOLD to expiry · TLT $85P SELL @ $2.60 limit (TRY-EXIT-TLT85P, STAGED) · XLE $65C ×2 HOLD through OPEC+ 9/6, sell both at the 9/9 open unless XLE closed ≥$66.50 on 9/8 (DOCKET L252/L253) · USO 150/165 Sep-18 spread (RH) HOLD. **GATE-TERRY-ROLL70-EXIT** registered 9/3 (WAL official close ≥$81.90 ×3 consecutive; 0-of-3 at the 9/2 close $79.12) as the Dec-18 70P's guard.

**Updated:** 2026-09-03 [Fidelity positions, 9/3 ~15:07 ET intraday] | **Fidelity cash (money market):** $18,025.71 (47.11%) — was $13,600.67 + $722.58 pending on 8/28 ⇒ **+$4,425.04, of which +$3,702.46 is NOT explained by the settled pending (D-45)** | **Fidelity positions market value:** $20,233.73 (was $22,133.89) | **Pending activity:** none shown | **Fidelity account total:** $38,259.44 (was $36,457.14 ⇒ **+$1,802.30**) *(9/3 session to 15:07: −$137.82 / −0.36%; open-position G/L **+$1,520.73 / +8.13%** on $18,713.00 open basis — basis fell $3,106.58 = QQQ $2,144.23 + one 135C $710.67 + one 85P $251.68 removed)* | **Robinhood Individual:** NOT CAPTURED (last read 8/28: $414.81)

*ANVIL re-verified every capture cell independently: 17 rows + cash = $38,259.44 to the cent; Σ open G/L +$1,520.73; Σ today −$137.82; sole flag = APD 304.6775 × 2 = 609.355 displayed as $609.35 (broker half-cent rounding, not a transcription error). Closed this pass by WQ-168: D-32, D-33; D-29 superseded by D-44. 8/29's resolved/caveat rows → `FORGE/_archive/RECONCILE_2026-08-29_RECORD.md`. Live D-rows below are the only ones open.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All marks/values `[Fidelity positions, 9/3 ~15:07 ET intraday]`. DTE counted from 9/3.*

| Ticker | Type | Qty | Cost | Mark 9/3 | Value | P&L | Owner note |
|--------|------|-----|------|----------|-------|-----|-----|
| AAPL | Stock | 15 | $23.64 | $327.21 | $4,908.15 | **+1,283.86%** | +$4,553.48 (today +$33.75). qty 15 unchanged; the 5-sh sale predates 7/30, date/price unrecorded (D-1). 52-wk 225.95–344.57 |
| GLD | Stock | 16 | $373.59 | $411.55 | $6,584.80 | **+10.15%** | +$607.30 (today +$140.32, the book's mover). MIDAS domain. Largest position by value; last add 7/31 (activity-confirmed 8/29). 52-wk 313.07–509.70 |
| USO | Stock | 37 | $122.28 | $141.63 | $5,240.31 | **+15.82%** | +$716.04. Will's Hormuz-gap entry (BRENT). Energy sleeve in the IRA at 15:07 = 37 sh + 135C ×1 + XLE 65C ×2 = **$6,755.31 = 17.7%** of the account (RH 150/165 spread unread). TRY-EXIT-USO35 scaffold title still says 35 sh. 52-wk 65.99–154.08 |
| APD | Stock | 2 | $294.79 | $304.6775 | $609.35 | **+3.35%** | +$19.78. Thesis tag still unassigned (open since 7/30). 52-wk 229.11–314.87 |
| TBT | Stock | 14 | $34.63 | $38.08 | $533.12 | **+9.96%** | +$48.30. 2× UST short — duration-short leg (BOND/TERRY). 52-wk 31.69–39.32 |
| ~~**USO**~~ | **$135C Oct-16** | **0** | $7.11 | — | $0.00 | **CLOSED** | **SOLD September 9, 2026:** remaining ×1 at $17.55; net $1,754.30 after $0.70 costs, settles September 10. Realized gain $1,043.64 versus $710.66 screenshot basis. [Receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md). B/C discharged; no remaining call. Historical September 3: ×1, mark $11.95, value $1,195, open gain $484.34; first sale September 2 price permanently UNKNOWN (WQ-167). See D-48 |
| XLE | $65C Sep-30 | 2 | $2.28 | $1.60 | $320.00 | −29.73% | −$135.35 (was −62.7% on 8/28; today −$32). **27 DTE. RULED WQ-168 ⑦: HOLD through OPEC+ 9/6; SELL BOTH at the bid on the Wed 9/9 open unless XLE CLOSED ≥$66.50 on Tue 9/8** (DOCKET L252/L253; TRY-EXIT-XLE65C STAGED/CONDITIONAL). See **D-46** |

*Not on the 9/3 view: **VLO** (TRY-BRENT-REFINER, 3× approved 8/27) ⇒ unfilled in the IRA as of 15:07, Robinhood unread · **STNG** (D-17) · **QQQ** shares (see day-trade class).*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book. Aug-21 expirations are broker-confirmed by "EXPIRED" activity rows dated Aug-24 `[Fidelity activity, transcribed 8/29 12:50 ET]`; the thesis-put tables retain the struck-through originals for continuity.

| Position | Expiry | Qty | Cost | Outcome |
|----------|--------|-----|------|---------|
| ~~**VIX $20C/$25C call debit spread** (`VIXW`)~~ | Aug-05-2026 | ~~4~~ | $0.70 net debit | **✅ CLOSED 2026-07-30 ~09:50 ET — REALIZED −$111.60 (−38.8%).** `TRY-VIOLET-VIXCS` (VIOLET thesis / TERRY construction). Exited as one spread ticket at net $0.45 credit on the mandatory date, un-killed, no roll; exit legs broker-confirmed 8/2 and 8/29 (+$248.15 / −$72.05 = +$176.10 net). Open: TERRY card §10 grade + PB-0003 close; VIOLET settle re-grade |
| ~~**KRE $60P**~~ | Aug-21-2026 | ~~3~~ | $2.70 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$809.02.** Ruled LAPSE 8/14 |
| ~~**QQQ $710P**~~ | Aug-21-2026 | ~~1~~ | $2.4566 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$245.66.** Day-trade class; bought 8/20, never on a positions view |
| ~~**OZK $45P**~~ | Aug-21-2026 | ~~4~~ | $3.69 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$1,474.70.** Ruled RIDE to OPEX 8/4 |
| ~~**OZK $42.5P**~~ | Aug-21-2026 | ~~1~~ | $2.12 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$211.67.** Ruled RIDE to OPEX 8/4 |
| ~~**KELYA $7.5P**~~ | Aug-21-2026 | ~~1~~ | $0.76 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$75.67.** Ruled LAPSE 8/14; LABOR thesis-grade at OPEX |

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, **on no PROME rail and owned by no agent**. Recorded so it is not invisible, not because the fleet manages it. The full ticket-by-ticket record 7/20–8/28 (seven QQQ put tickets 7/20–7/31 ≈ −$2,267; the 8/3–8/28 continuation incl. the **QQQ 713C Aug-21 exercise → 100 sh @ $713 on 8/24 → 77 sh broker-liquidated ≈$707.81 same day → 18+1+1 sold 8/26–8/28 → 3 sh held**, realized −$563.81 on the 97 sh; **class realized 8/3–8/28 ≈ −$1,812.89, ≈ −$4,080 since 7/20**) → this file at `183068dd1` + the 8/29 transcription. WQ-97 ("23 QQQ, rec SELL") was executed on 20 of 23 by 8/28; **the residual 3 sh are ABSENT from the 9/3 view.**

| Position | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|----------|--------|-----|------|------|-------|-----|------|
| ~~**QQQ**~~ | — | ~~3~~ | $714.74 | — | — | **UNRECORDED (sale)** | **GONE from the 9/3 positions view** (8/28: 3 sh @ $716.43 = $2,149.29; basis $2,144.23 = ($71,300 + $174.66 premium)/100 × 3). Absence from a view is not proof of closure — **but** the cash bridge (+$3,702.46 unexplained, D-45) is consistent with QQQ + one 135C + one 85P sold, so the labeled reading is SOLD, date/price UNKNOWN. Struck so the parser carries no phantom 3-sh position; un-strike if the activity view says otherwise. See **D-44** |
| ~~**QQQ $687P**~~ | Aug-03-2026 — **LIQUIDATED 8/3** | ~~3~~ | $2.81 | — | — | **−$839.18 realized** | Activity-confirmed 8/29 (D-12 closed). Basis $841.99; Will's "sold at a loss" recall was right in direction, near-total in size |
| ~~QQQ $680P~~ | Jul-31-2026 — CLOSED 7/31 | ? (2 fills) | — | — | — | **−$1,005.48 realized** | Bought 7/30 in two fills (−$599.33, −$414.66); sold 7/31 +$8.51 (D-14 = fill-pairing inference only) |
| ~~QQQ $672P~~ | Jul-31-2026 — EXPIRED WORTHLESS | ? | — | — | — | **−$416.66 realized** | Bought 7/30 −$416.66; EXPIRED row dated Aug-03 |
| ~~QQQ $675P~~ | Jul-30-2026 — SOLD 7/30 | 1 | $3.92 | — | — | **−$389.67 realized** | Liquidation +$1.99 on 7/30 (activity) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **25** | **$0.12** *(broker basis $289.08, fees-in $0.11563)* | $0.03 | $75.00 | **−$214.08 / −74.06%** (today −$50). **27 DTE. RULED WQ-168 ④: HOLD to expiry** (bid $0.03; fees eat 22% of $75; the card pre-registered grind = $0). ⚠️ Gate proximity, NOT adjudication (rule 7): harvest line *"half at ≥3×"* — 10 ct still owed at ≥$0.3469 fees-in (PB-0002b); at $0.03 the position is **0.26× fees-in basis**, far below. Exit gate GATE-TERRY-007 *"FIVE CONSECUTIVE official FRED DGS10 closes <4.50% ⇒ TERRY builds exit proposal → Will [Approve]"* — registry **0 of 5**; 9/1 official DGS10 **4.79 = window HIGH, 29bp from the line** (owner-graded through 9/1, TERRY c8c58a363); registry caveat *"NO-VERDICT is the correct read if expiry beats the count."* No DGS10 in this capture; ANVIL grades nothing. 7/31 harvest of 5 ct @ $0.37336 = +$128.86 realized (PB-0002a). See **D-31** |
| $85P | Sep-30 | **1** | $2.52 *(basis $251.67)* | $2.72 | $272.00 | **+$20.33 / +8.07%** (today −$38). **qty 2→1 BROKER-VERIFIED — one contract SOLD before 15:07 9/3, date/price UNKNOWN.** WQ-168 ⑤ (12:45 today) = SELL 2 @ $2.60 limit (TRY-EXIT-TLT85P, STAGED per TERRY — placement unconfirmed); the 8/28 basis $503.35 halved exactly ⇒ one contract, not a re-basing. Last 2.72 > the $2.60 limit at capture. 27 DTE. **ASK — D-43** |
| $82P | Oct-16 | 2 | $1.68 | $1.02 | $204.00 | **−$131.35 / −39.17%** (today −$38). 43 DTE. No ruling recorded on this file |

*Duration-short complex (TBT + three TLT legs) open G/L at 15:07: +$48.30 − $214.08 + $20.33 − $131.35 = **−$276.80** (8/28: −$281.82 — not like-for-like: the 85P is now ×1 and the sold contract's proceeds are unknown), against the +$128.86 realized on the 7/31 harvest.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.35 | $70.00 | −$443.34 / −86.37% (today −$22; 0.57 on 8/28). 106 DTE |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.35 | $105.00 | −$773.02 / −88.05% — Fidelity multi-lot marker; **five** Dec-18 KRE 60P total across the two lots. 106 DTE |
| $60P | Sep-30 | 2 | $2.27 | $0.01 | $2.00 | −$451.35 / −99.56% — **27 DTE. RULED WQ-168 ⑥: LAPSE** (NOBID on two chain pulls per TERRY; the lapse word D-33 lacked). Rides to $0 |
| ~~$60P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~3~~ | $2.70 | — | — | **−$809.02 realized** — activity row Aug-24. Ruled LAPSE 8/14; event-box entry is the record, row retained (D-36) |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.05 | $5.00 | −$763.67 / −99.35% (today −$25) — **15 DTE. RULED WQ-168 ①: LAPSE** (forgoes ~$4.35 of bid; **re-opens only if WAL closes <$71 in the week of 9/14**). Duration-rolled: the Dec-18 $70P ×1 bought 9/2 lives in **ROBINHOOD** (see that table, D-47). D-32 closed |
| $67.5P | Sep-18 | 1 | $7.51 | $0.10 | $10.00 | −$740.67 / −98.67% — **15 DTE. RULED WQ-168 ②: LAPSE** (NOBID ×2 pulls — no other branch exists). D-32 closed |

*(The Robinhood **WAL $77.5P Aug-21 ×1** — Will confirmed the sale in-session 2026-08-18; date/proceeds still unrecorded ⇒ P&L UNRECORDED, not zero — D-18. Struck-through in the Robinhood table, retained.)*

### OZK (REGINALD) — Aug-21s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| ~~$45P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~4~~ | $3.69 | — | — | **−$1,474.70 realized** — activity row Aug-24. Ruled RIDE to OPEX 8/4. Row retained (D-36) |
| ~~$42.5P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~1~~ | $2.12 | — | — | **−$211.67 realized** — activity row Aug-24. RIDE to OPEX. Row retained (D-36) |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $0.60 | $60.00 | −$1,124.67 / −94.94% | BROCK thesis vehicle. 0.95 [8/28] → 0.60 (today −$35). 106 DTE. No ruling on file |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.20 | $40.00 | −$151.34 / −79.10% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort. 43 DTE |
| ~~KELYA~~ | ~~$7.5P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~1~~ | $0.76 | — | — | **−$75.67 realized** | LABOR thesis. Activity row Aug-24. Ruled LAPSE 8/14; LABOR's thesis-grade at OPEX. Row retained (D-36) |

## Robinhood — satellite account (Individual)

> ⚠️ **NOT CAPTURED 2026-09-03.** Last read = the Fri 8/28 positions/P&L view: account value **$414.81**, buying power **$174.90**, banner **"13 days left"** (unexplained, D-37); *"Event contracts can't be traded on the web, but may impact buying power"* ⇒ event-contract exposure invisible; no per-contract marks ⇒ costs/values back-computed from P/L pairs and the block stays machine-class `unverified` by design; ≈$8.67 residue vs stated value. **Every row below is 8/28 vintage or PROME-supplied and unverified today.** Since 8/28: the QQQ $715P passed its 8/31 expiry (outcome unrecorded) and one 9/2 fill (WAL Dec-18 $70P) landed here on Will's word. Rows absent from a capture are **retained, not deleted**.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** | UNMARKED | ⚠️ **PROME-SUPPLIED, NOT BROKER-VERIFIED** — Will's word 9/2 14:21 ET | **NEW to the mirror.** TRY-WAL-ROLL70 FIRED — the card named the Fidelity IRA; filled in ROBINHOOD (account deviation, TERRY card §5c). Guard = **GATE-TERRY-ROLL70-EXIT** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 at the 9/2 close $79.12** (REGINALD grades; rule 7, not adjudicated). Card harvest GTC ≥2.0× debit ($4.40): **resting status UNKNOWN — permanent by WQ-167, not an ask**. Time stop Fri 12/4. 106 DTE. See **D-47** |
| ~~**QQQ $715P**~~ | ~~8/31/2026~~ — **EXPIRED 8/31, outcome UNRECORDED** | ~~1~~ | ≈$193.24 | — | ⚠️ **UNRECORDED — not an ask (TERRY ④, 9/3)** | Struck on the calendar only: expired OTM / sold intraday / exercised — **none verified** (Robinhood unread since 8/28; TERRY's labeled 8/31 datum QQQ C 716.76 > 715 is a third close vintage, not a resolution). Nothing to book until a Robinhood view lands. D-28 carried as UNRECORDED |
| **USO $150/$165 call spread** | Sep-18 | 1 | **$300.00 net debit** | ≈$41.00 [8/28] | 8/28 vintage — unverified today | **RULED WQ-168 ③: HOLD** (OPEC+ 9/6 is the catalyst; realizable ≈$111 per TERRY 12:20 9/3, not read here). 15 DTE. BRENT tail-rider; BE ~$153 vs USO 141.63 [Fidelity 15:07] |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 | ≈$1.00 [8/28] | 8/28 vintage | −$52.00 / −98.11% on 8/28. Deep-OTM lottery, carried since 7/20. 134 DTE |
| ~~**VLY $14P**~~ | ~~8/21~~ — **EXPIRED 8/21 (presumed worthless)** | ~~1~~ | $40.00 | — | **presumed −$40.00** | Ruled LAPSE 8/14; no RH activity view ⇒ $0 is a labeled presumption (D-36). TERRY EbE write-back owed |
| ~~**WAL $77.5P**~~ | **Aug-21** | ~~1~~ | — | — | ✅ **CONFIRMED SOLD (Will 8/18)** | Absent 8/14 and 8/28. **Date/proceeds unrecorded ⇒ P&L UNRECORDED, not zero.** See **D-18** |
| T | stock | 1 | — | — | ⚠️ **absent 8/14 + 8/28; 9/3 unread** | 1 share (~$22 on 7/20) — larger than the $8.67 residue, so "hidden" does not fit. **Hypothesis: sold**, unconfirmed. See D-20 |
| ~~USO $128C~~ | 7/22 — **EXPIRED** | 1 | — | — | **presumed worthless** | Hormuz leg (~−$100 class). D-5 closed as far as a view can close it |
| ~~QQQ $696P~~ | 7/20 EXPIRED | 1 | — | — | **CLOSED ~−$455** | Will-reported 7/20: recovered ~$8; QQQ closed ATM $696. Day-trade class |

---

## ⚠️ Reconcile discrepancies (9/3)

> Built by ANVIL against the 9/3 ~15:07 ET intraday Fidelity positions view — one account, no activity view, Robinhood unread. **Nothing here has been resolved by invention**; every conjecture is labeled; broker view > Will's word > PROME queue/SCRATCH context. Ranked by decision urgency, **expiring first**; "Will decides" separated from "owner decides." **Permanently UNKNOWN by WQ-167 — never listed as asks:** the 9/2 USO 135C sale price · the ROLL70 $4.40 GTC's resting status. **Closed this pass by WQ-168:** D-32 (WAL Sep-18 pair — LAPSE ①②) · D-33 (Sep-30 cluster — every leg now ruled: 77P HOLD ④, 85P SELL ⑤, KRE LAPSE ⑥, XLE dated exit ⑦ → D-46) · D-29 (QQQ residual — gone from the view; residue → D-44).

### EXPIRING / DATED — Will decides

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-43** | **★ TLT $85P Sep-30 — ONE of two contracts SOLD; the other may be a WORKING order** | **🔴 now** (order status) · 27 DTE | Qty 2→1 broker-verified; remaining basis $251.67 = exactly half of 8/28's $503.35 ⇒ one contract sold, not a re-basing. WQ-168 ⑤ (ruled 12:45 9/3) = SELL 2 @ $2.60 limit; TERRY holds TRY-EXIT-TLT85P as STAGED, placement unconfirmed. Last **2.72** at 15:07 (> $2.60) | (a) partial fill of today's 2-lot @ $2.60 with one still working · (b) a 1-lot order · (c) an earlier/separate sale. **ANVIL picks none.** A resting $2.60 limit with last at 2.72 would ordinarily be marketable — but Last ≠ bid, so this is a question, not a contradiction. **Ask: sale date + price, and is the second contract still working?** | **Will** — one line (TERRY logs it on the card) |
| **D-44** | **QQQ 3 sh — GONE from the view; sale date/price UNKNOWN** | 🟠 fact owed | Absent 9/3 (8/28: 3 @ $716.43, basis $714.74). Cash bridge consistent with the sale (D-45). WQ-97 rec SELL = executed on 23 of 23 IF sold | SOLD — labeled reading, supported by the absence AND the cash bridge, still not proof. Row struck in the day-trade table so the parser carries no phantom | **Will** — date/price, or the activity view |
| **D-45** | **Cash bridge: +$3,702.46 not explained by the settled pending** | 🟠 activity view owed | $13,600.67 + $722.58 (pending settled) = $14,323.25 → $18,025.71 = **+$3,702.46** from something. Three sales are the candidates (QQQ 3 sh · 135C ×1 · 85P ×1) | PROME-derived (transcription §③): QQQ ≈$2,130–2,150 + 135C ≈$1,200–1,400 + 85P ≈$260–275 = ≈$3,590–3,825 ⇒ plausibly closes with no residue; an AAPL Aug dividend (≈$3.90) sits inside tolerance. **Hypothesis until the Fidelity Activity view (past 30 days) is read** | **Will** — post the activity view (transcription ask ①) |
| **D-46** | **XLE $65C Sep-30 ×2 — DATED EXIT, 9/8 close → 9/9 open** | 🟡 3 sessions · 27 DTE | $1.60 / $320 (−29.73%). WQ-168 ⑦ RULED: hold through OPEC+ 9/6; **XLE 9/8 close ≥ $66.50 ⇒ hold on (TERRY registers a time stop); else SELL BOTH at the bid on the 9/9 open** — DOCKET L252/L253; PROME consumer-reads the 9/8 close if TERRY is dark | None — the rule is fully specified; ANVIL reports the mark only | Will's hand at the broker 9/9 (a fired dated rule is held, not re-litigated — TERRY RISK_RULES #12) |

### RULED / GATED — owner decides (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-31** | **TLT $77P Sep-30 ×25 — HOLD to expiry (WQ-168 ④)** | 🟡 27 DTE | $0.03 / $75 on $289.08 basis (−74.06%; today −$50). 0.26× fees-in; harvest line *"half at ≥3×"* (10 ct at ≥$0.3469) far away. GATE-TERRY-007 **0-of-5**; 9/1 official DGS10 4.79 = window HIGH, 29bp from 4.50, owner-graded through 9/1 | Registry's own logic: *"NO-VERDICT is the correct read if expiry beats the count"* — a fire needs five sub-4.50 official closes inside the 18 sessions left | TERRY grades DGS10 daily → Will only on a proposal |
| **D-47** | **Robinhood WAL Dec-18 $70P ×1 @ $2.20 — PROME-SUPPLIED, unverified** | 🟡 106 DTE | Will's word 9/2 14:21 ET; TRY-WAL-ROLL70 FIRED; account deviation (RH, not the IRA). Guard GATE-TERRY-ROLL70-EXIT **0-of-3** at the 9/2 close $79.12; time stop 12/4 | Verifiable only by a Robinhood capture. $4.40 GTC status permanently UNKNOWN (WQ-167) ⇒ per TERRY the harvest is a manual act by Will, not a control | REGINALD grades / TERRY proposes / next RH capture verifies |
| **D-48** | **USO $135C Oct-16 — CLOSED September 9** | RESOLVED | Remaining ×1 sold at $17.55; net $1,754.30; settles September 10. B/C discharged; zero remaining. | Remaining-lot realized gain $1,043.64 on $710.66 basis; first-sale price permanently UNKNOWN (WQ-167). | [Receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md); owner records consume this closure |

### CARRIED — need a capture or one line from Will

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-28** | **Robinhood QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; QQQ closed 716.43 on 8/28 ($1.43 OTM). Robinhood unread since; TERRY ④ 9/3: UNRECORDED, not an ask | Expired OTM (≈−$193) / sold / exercised — none verified | Next Robinhood capture |
| **D-17** | **STNG — appears in no capture, nowhere in FORGE (carried)** | 🟠 carried | Absent from every capture since 8/2, the 7/30–8/28 activity window, and today's view. March-2026 record (STNG ×2 @ $70.01, sold next day; root Critical Rule #10's example) | (a) the 7/21 note recalled the March position · (b) closed pre-7/30 · (c) a third account. ANVIL picks none | **Will** — one line |
| **D-20** | **Robinhood: T share absent ×2 + event contracts invisible + ≈$8.67 residue (8/28)** | 🟡 carried | Unread today | Hypothesis: T sold; event-contract exposure of unknown size remains the live risk | **Will** |
| **D-1** | **AAPL 5-sh sale — date + price unrecorded** | 🟡 carried | qty 15 Will-confirmed 8/2; no AAPL activity 7/30–8/28 ⇒ predates 7/30 | ~$565 cash class | Will / an older activity window |
| **D-18** | **Robinhood WAL $77.5P Aug-21 — sale CONFIRMED (8/18), P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Date/proceeds need a Robinhood history view; do not book at $0 | Will (not urgent) |
| **D-37** | **Robinhood ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29; nothing trades off it | Deposit/transfer hypothesis; banner referent unknown | Will (one line) |

---

## Immediate Actions (9/3 session state)

| Item | State | Owner |
|---|---|---|
| **★ TLT 85P — is the second contract a working order?** (D-43) | 🔴 One sold (date/price unknown); WQ-168 ⑤ was SELL 2 @ $2.60; last 2.72 at 15:07 | **Will** — one line; TERRY logs |
| **Fidelity Activity view (past 30 days)** (D-45 · D-44 · D-43) | 🟠 Closes the +$3,702.46 bridge and dates all three sales | **Will** — post it |
| **XLE 65C ×2 dated exit** (D-46) | 🟡 9/8 close ≥$66.50? else sell both at the 9/9 open (DOCKET L252/L253) | TERRY / PROME reads 9/8 · Will's hand 9/9 |
| **Sep-18 lapses** (WAL 70P/67.5P Fidelity; USO 150/165 RH = HOLD) | 🟡 15 DTE; nothing to do — 70P re-opens only on a WAL close <$71 in the week of 9/14 | REGINALD watch |
| **TLT 77P ×25 HOLD; GATE-TERRY-007 0-of-5** (D-31) | 🟡 27 DTE; reported, not adjudicated | TERRY (DGS10 daily) |
| **Robinhood capture owed** (D-47 · D-28 · D-20 · D-37) | 🟡 One 9/2 fill + one 8/31 expiry + T share + event contracts all unverified | **Will** — next screenshot |
| **USO 135C — CLOSED September 9** (D-48) | Remaining ×1 sold; B/C discharged. Share management remains separate. | [Receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md) |
| **STNG · AAPL 5-sh** (D-17 · D-1) | 🟡 Carried; one line each | **Will** |
| **APD thesis tag** | 🟡 Unassigned since 7/30; +3.35% | PROME / Will |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Transcription of record for this pass (Fidelity positions only) → `PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md`*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069 n=3 — the 7/30 reconcile broke the parser silently). New consumers: add yourself to this list in the same commit that starts parsing. *(9/3 pass: no section/header renames except the Longs column `Mark 8/28` → `Mark 9/3`, which the parser binds by prefix (hardening #3, same rename class as every prior pass); no new columns; TWO rows newly struck-through (`~~`) = the parser's CLOSED marker — the day-trade QQQ 3-sh row (absent from the view) and the Robinhood QQQ $715P (expiry passed, already withheld by date); ONE new Robinhood row (WAL Dec-18 $70P — no Mark column there ⇒ class `unverified`). Parser re-run post-edit: 17 live / 24 withheld (14 closed · 6 event_box · 4 unverified), no defects, selftest PASS.)*
